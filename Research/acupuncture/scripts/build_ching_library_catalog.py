#!/usr/bin/env python3
"""Build ching-library-catalog.json from external drive acupuncture assets."""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"
REPO_ROOT = SCRIPT_DIR.parents[2]
OUT_PATH = DATA_DIR / "ching-library-catalog.json"
HARVARD_CATALOG = DATA_DIR / "harvard-ap101-catalog.json"

CANON_VOLUME = "/Volumes/Macintosh HD - Data"
ALT_VOLUME = "/Volumes/Macintosh HD 1"

SCAN_ROOTS: list[tuple[str, str, str]] = [
    ("acupuncture_charts", "Desktop/acupuncture charts", "visual_reference"),
    ("kiiko_ppt", "Users/chingchen/Downloads/Kikko Acupuncture PPT", "clinical_strategy"),
    ("estream", "Desktop/Windows Desktop/Acupuncture Videos estream", "harvard_ap101_extension"),
    ("deadman_cdrom", "Desktop/Windows Desktop/A Manual Of Acupuncture - Peter Deadman", "gold_standard"),
    ("podcasts", "Desktop/iTunes/iTunes Media/Podcasts", "audio_reference"),
    ("mega_partnering_tcm", "Users/chingchen/Downloads/mega partnering talk 11 1 2012/Mini Mega partnering ppt info", "visual_reference"),
    ("windows_downloads", "Desktop/Windows Desktop/Downloads", "clinical_demo"),
]

MEDIA_EXTS = {
    ".pdf", ".doc", ".ppt", ".pptx", ".mp4", ".m4v", ".mov", ".rm", ".swf",
    ".mp3", ".m4a", ".jpg", ".jpeg", ".png", ".gif", ".psd", ".rtf", ".xlsx",
}
SKIP_NAMES = {".ds_store", "thumbs.db", "desktop.ini"}
WEEK_RE = re.compile(r"Week\s*(\d+)", re.IGNORECASE)
POINT_PDF_RE = re.compile(r"^[A-Z]{2,4}-\d+\.pdf$|^[A-Z]{2,4}Intro\.pdf$|^[A-Z]{2,4}Notes\.pdf$")


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return text[:100] or "item"


def canonical_path(path: Path) -> str:
    s = str(path)
    for vol in (CANON_VOLUME, ALT_VOLUME):
        s = s.replace(vol + "/", "")
    return s


def repo_rel(path: Path) -> str | None:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return None


def load_harvard_paths() -> set[str]:
    if not HARVARD_CATALOG.exists():
        return set()
    data = json.loads(HARVARD_CATALOG.read_text(encoding="utf-8"))
    paths: set[str] = set()
    for item in data.get("items", []):
        for key in ("source_path", "converted_mp4"):
            val = item.get(key)
            if val:
                paths.add(val)
        for alt in item.get("alternate_paths", []):
            paths.add(alt)
    return paths


def classify_kind(ext: str) -> str:
    if ext in {".mp4", ".m4v", ".mov", ".rm", ".swf"}:
        return "video"
    if ext in {".mp3", ".m4a"}:
        return "audio"
    if ext in {".jpg", ".jpeg", ".png", ".gif", ".psd"}:
        return "image"
    return "document"


def parse_week(name: str) -> int | None:
    m = WEEK_RE.search(name)
    return int(m.group(1)) if m else None


def is_acupuncture_relevant(path: Path, collection_id: str) -> bool:
    name = path.name.lower()
    if collection_id == "windows_downloads":
        return any(k in name for k in ("acupunct", "kiiko", ".rm", "clinical"))
    return True


def scan_collection(collection_id: str, rel_root: str, role: str) -> tuple[dict, list[dict]]:
    base = Path(CANON_VOLUME) / "Users/ching" / rel_root
    if collection_id == "kiiko_ppt" or collection_id == "mega_partnering_tcm":
        base = Path(CANON_VOLUME) / rel_root

    if not base.exists():
        base = Path(ALT_VOLUME) / "Users/ching" / rel_root
        if collection_id in {"kiiko_ppt", "mega_partnering_tcm"}:
            base = Path(ALT_VOLUME) / rel_root

    items: list[dict] = []
    deadman_point_pdfs = 0
    deadman_support = 0
    estream_rm = 0

    if not base.exists():
        return {
            "id": collection_id,
            "title": collection_id.replace("_", " ").title(),
            "role": role,
            "source_path": str(base),
            "status": "missing",
            "item_count": 0,
        }, []

    for dirpath, _, filenames in os.walk(base):
        for fname in filenames:
            if fname.lower() in SKIP_NAMES or fname.startswith("~"):
                continue
            full = Path(dirpath) / fname
            ext = full.suffix.lower()
            if ext not in MEDIA_EXTS and ext not in {".abt", ".cat", ".ddd", ".pdd"}:
                continue
            if collection_id == "windows_downloads" and not is_acupuncture_relevant(full, collection_id):
                continue
            if collection_id == "podcasts" and "acupunct" not in str(full).lower() and "chinese medicine" not in str(full).lower():
                continue

            rel = full.relative_to(base)
            st = full.stat()

            if collection_id == "deadman_cdrom":
                if rel.parts[0:1] == ("ACUPNCTR",) and POINT_PDF_RE.match(fname):
                    deadman_point_pdfs += 1
                    continue
                if rel.parts[0:1] == ("ACUPNCTR",) and ext in {".abt", ".cat", ".ddd", ".pdd", ".did", ".plc", ".stp", ".wld", ".trn"}:
                    deadman_support += 1
                    continue
                if "index" in rel.parts and ext not in MEDIA_EXTS:
                    deadman_support += 1
                    continue

            if collection_id == "estream" and ext == ".rm":
                estream_rm += 1

            kind = classify_kind(ext)
            week = parse_week(fname)
            item = {
                "id": f"{collection_id}-{slugify(fname)}",
                "collection_id": collection_id,
                "filename": fname,
                "relative_path": str(rel),
                "source_path": str(full),
                "size_bytes": st.st_size,
                "format": ext.lstrip("."),
                "kind": kind,
                "week": week,
                "week_label": f"Week {week:02d}" if week else None,
                "status": "stub" if kind == "video" and st.st_size < 1000 else (
                    "needs_conversion" if ext == ".rm" else (
                        "legacy_flash" if ext == ".swf" else "ok"
                    )
                ),
                "playable": kind == "video" and ext in {".mp4", ".m4v", ".mov"} and st.st_size >= 1000,
            }
            items.append(item)

    collection = {
        "id": collection_id,
        "title": {
            "acupuncture_charts": "Meridian & Anatomy Charts",
            "kiiko_ppt": "Kiiko Matsumoto Clinical Strategy Materials",
            "estream": "Harvard AP101 eStream Extension (Weeks 30–32 + clinical RM)",
            "deadman_cdrom": "A Manual of Acupuncture — Deadman CD-ROM",
            "podcasts": "Acupuncture Podcasts (iTunes)",
            "mega_partnering_tcm": "TCM Qi Meridian Diagrams (Mega Partnering)",
            "windows_downloads": "Windows Desktop Downloads — Clinical Videos",
        }[collection_id],
        "role": role,
        "source_path": str(base),
        "status": "indexed",
        "item_count": len(items),
    }

    if collection_id == "deadman_cdrom":
        collection["deadman_point_pdf_count"] = deadman_point_pdfs
        collection["deadman_support_file_count"] = deadman_support
        collection["notes"] = (
            f"Main manual PDF + {deadman_point_pdfs} per-point ACUPNCTR PDFs on drive. "
            "Repo already has unified extract: Research/acupuncture/data/deadman-extract-v0.2.json"
        )
        collection["item_count"] = len(items)

    if collection_id == "estream":
        collection["realmedia_count"] = estream_rm
        collection["notes"] = (
            f"{estream_rm} RealMedia files with timestamp IDs (C_*.rm). "
            "Most are corrupt download stubs (~85–103 bytes). "
            "Named Week 30–32 handouts overlap with harvard-ap101-catalog."
        )

    return collection, items


def cross_reference(items: list[dict], harvard_paths: set[str]) -> None:
    repo_imports = {
        "kiiko_matsumoto_david_euler_kiiko_matsumotos_clinical_strate.pdf": "Research/acupuncture/sources/pdfs/kiiko_matsumoto_david_euler_kiiko_matsumotos_clinical_strategy vol 1.pdf",
        "A Manual of Acupuncture.pdf": "Research/acupuncture/sources/pdfs/A-manual-of-acupuncture-peter-deadman.pdf",
    }
    for item in items:
        fname = item["filename"]
        sp = item["source_path"]
        if sp in harvard_paths:
            item["duplicate_of"] = "harvard-ap101-catalog"
        if fname in repo_imports:
            item["imported_to_repo"] = repo_imports[fname]
        elif "clinical_strate" in fname.lower() and fname.endswith(".pdf"):
            item["imported_to_repo"] = "Research/acupuncture/sources/pdfs/kiiko_matsumoto_david_euler_kiiko_matsumotos_clinical_strategy vol 1.pdf"
            item["note"] = "Likely duplicate of Kiiko vol 1 already in repo"


def main() -> None:
    harvard_paths = load_harvard_paths()
    collections: list[dict] = []
    all_items: list[dict] = []

    for collection_id, rel_root, role in SCAN_ROOTS:
        col, items = scan_collection(collection_id, rel_root, role)
        collections.append(col)
        all_items.extend(items)

    cross_reference(all_items, harvard_paths)

    # Dedupe identical files across collections by source path + size
    seen: dict[str, dict] = {}
    deduped: list[dict] = []
    for item in all_items:
        key = f"{item['source_path']}|{item['size_bytes']}"
        if key in seen:
            seen[key]["alternate_paths"] = seen[key].get("alternate_paths", []) + [item["source_path"]]
            continue
        item["alternate_paths"] = []
        seen[key] = item
        deduped.append(item)

    summary = {
        "total_collections": len(collections),
        "total_items": len(deduped),
        "by_collection": {c["id"]: c["item_count"] for c in collections},
        "by_kind": dict(sorted({k: sum(1 for i in deduped if i["kind"] == k) for k in {i["kind"] for i in deduped}}.items())),
        "stubs": sum(1 for i in deduped if i["status"] == "stub"),
        "needs_conversion": sum(
            1 for i in deduped if i["status"] == "needs_conversion"
        ),
        "imported_to_repo": sum(1 for i in deduped if i.get("imported_to_repo")),
        "harvard_duplicates": sum(1 for i in deduped if i.get("duplicate_of")),
    }

    catalog = {
        "meta": {
            "version": "0.1",
            "cataloged_at": date.today().isoformat(),
            "owner": "ching / chingchen (same person)",
            "primary_volume": CANON_VOLUME,
            "catalog_script": "Research/acupuncture/scripts/build_ching_library_catalog.py",
            "related_catalogs": [
                "Research/acupuncture/data/harvard-ap101-catalog.json",
            ],
            "notes": (
                "Targeted index of acupuncture assets outside the main Harvard AP101 folder. "
                "Files remain on external drive unless noted imported_to_repo."
            ),
        },
        "summary": summary,
        "collections": collections,
        "items": sorted(
            deduped,
            key=lambda i: (i["collection_id"], i.get("week") or 999, i["filename"]),
        ),
    }

    OUT_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(deduped)} items across {len(collections)} collections to {OUT_PATH}")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
