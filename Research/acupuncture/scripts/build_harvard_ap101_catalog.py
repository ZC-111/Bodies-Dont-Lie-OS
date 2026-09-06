#!/usr/bin/env python3
"""Build harvard-ap101-catalog.json from files on the attached drive."""

from __future__ import annotations

import json
import os
import re
import stat
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOTS = [
    Path("/Volumes/Macintosh HD - Data/Users/ching/Desktop/Harvard acupuncture"),
    Path("/Volumes/Macintosh HD - Data/Users/ching/Desktop/Windows Desktop/RealPlayer Downloads"),
    Path("/Volumes/Macintosh HD - Data/Users/ching/Desktop/iTunes/Extra iTunes"),
    Path("/Volumes/Macintosh HD - Data/Users/ching/Desktop/iTunes/iTunes Media/Movies"),
    Path("/Volumes/Macintosh HD 1/Users/ching/Desktop/Harvard acupuncture"),
    Path("/Volumes/Macintosh HD 1/Users/ching/Desktop/Windows Desktop/RealPlayer Downloads"),
    Path("/Volumes/Macintosh HD 1/Users/ching/Desktop/iTunes/Extra iTunes"),
    Path("/Volumes/Macintosh HD 1/Users/ching/Desktop/iTunes/iTunes Media/Movies"),
]

VIDEO_EXTS = {".mp4", ".m4v", ".mov", ".rm", ".swf"}
HANDOUT_EXTS = {".pdf", ".doc", ".ppt", ".pptx", ".rtf"}
ALL_EXTS = VIDEO_EXTS | HANDOUT_EXTS

PREFERRED_VOLUME = "Macintosh HD - Data"

WEEK_RE = re.compile(
    r"(?:^|[\s_/])(?:Week(?:end)?\s*(\d+)|wk\s*(\d+)|Week\s*(\d+)\s*[:/]|Week\s*(\d+))",
    re.IGNORECASE,
)
TYPE_RE = re.compile(
    r"(AcuLecture|Aculecture|SciLecture|AcuStrategies|AcuDemo|Guest\s*Lecture|GuestLect|"
    r"Point Location|Laser Handouts|Clinical Demo|Treatment Strategies|Clinical Strategies|"
    r"Demonstration|Video Demo|Palpation Exercise|Palpation|Acupuncture Detox)",
    re.IGNORECASE,
)
TEST_RE = re.compile(r"\(Test[^)]*\)|\bTest\b|\btest[_ ]", re.IGNORECASE)
TYPE_INDEX_RE = re.compile(r"\b(\d+)\s*[-–]?\s*(?:Part|P)\b", re.IGNORECASE)
HMS_RE = re.compile(r"HMS[_\s-]?(\d{4})", re.IGNORECASE)
FLASH_RE = re.compile(r"\(Flash\)|\.swf", re.IGNORECASE)


def normalize_volume(path: str) -> str:
    return path.replace("/Volumes/Macintosh HD 1/", "/Volumes/_CANON_/").replace(
        "/Volumes/Macintosh HD - Data/", "/Volumes/_CANON_/"
    )


def canonical_rel(path: Path) -> str:
    parts = path.parts
    for marker in (
        "Harvard acupuncture",
        "RealPlayer Downloads",
        "Extra iTunes",
        "iTunes Media/Movies",
    ):
        marker_parts = marker.split("/")
        for i in range(len(parts) - len(marker_parts) + 1):
            if list(parts[i : i + len(marker_parts)]) == marker_parts:
                return "/".join(parts[i + len(marker_parts) :])
    return path.name


def parse_week(name: str) -> int | None:
    m = WEEK_RE.search(name)
    if not m:
        return None
    for g in m.groups():
        if g:
            return int(g)
    return None


def parse_type(name: str) -> tuple[str | None, int | None]:
    m = TYPE_RE.search(name)
    if not m:
        lower = name.lower()
        if "clinical demo" in lower or "demonstration" in lower:
            return "ClinicalDemo", None
        if "treatment strateg" in lower or "clinical strateg" in lower:
            return "AcuStrategies", None
        if "palpation" in lower:
            return "Palpation", None
        if "video demo" in lower or "video " in lower:
            return "VideoDemo", None
        if "kiiko" in lower:
            return "ClinicalDemo", None
        return None, None

    raw = m.group(1)
    raw_key = re.sub(r"\s+", " ", raw).strip().lower()
    normalized = {
        "aculecture": "AcuLecture",
        "scilecture": "SciLecture",
        "acustrategies": "AcuStrategies",
        "acudemo": "AcuDemo",
        "guestlecture": "GuestLecture",
        "guest lecture": "GuestLecture",
        "guestlect": "GuestLecture",
        "point location": "PointLocation",
        "laser handouts": "LaserHandout",
        "clinical demo": "ClinicalDemo",
        "treatment strategies": "AcuStrategies",
        "clinical strategies": "AcuStrategies",
        "demonstration": "ClinicalDemo",
        "video demo": "VideoDemo",
        "palpation exercise": "Palpation",
        "palpation": "Palpation",
        "acupuncture detox": "SciLecture",
    }.get(raw_key, raw.title().replace(" ", ""))

    idx_m = re.search(
        r"(AcuLecture|SciLecture|AcuStrategies|AcuDemo|Guest\s*Lecture|GuestLect|Aculecture)\s*(\d+)",
        name,
        re.IGNORECASE,
    )
    type_index = int(idx_m.group(2)) if idx_m else None
    if type_index is None:
        part_m = TYPE_INDEX_RE.search(name)
        if part_m:
            type_index = int(part_m.group(1))
    return normalized, type_index


def parse_topic(name: str, lecture_type: str | None) -> str:
    stem = Path(name).stem
    stem = re.sub(r"\.swf(\s*\([^)]*\))?", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"HMS_\d+", "", stem).strip(" _-")
    stem = re.sub(r"^Week(?:end)?\s*\d+\s*", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"^wk\s*\d+\s*", "", stem, flags=re.IGNORECASE)
    if lecture_type:
        stem = re.sub(
            rf"{lecture_type}\s*\d*\s*[-–]?\s*",
            "",
            stem,
            count=1,
            flags=re.IGNORECASE,
        )
    stem = re.sub(r"\(Test[^)]*\)", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"\(PDF[^)]*\)", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"\(Flash[^)]*\)", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"_\d{4}(-\d+)?$", "", stem)
    stem = re.sub(r"\s+", " ", stem).strip(" .-_")
    return stem or name


def classify_kind(ext: str, name: str) -> str:
    if ext in {".mp4", ".m4v", ".mov", ".rm", ".swf"}:
        return "video"
    if TEST_RE.search(name):
        return "test"
    return "handout"


def video_status(ext: str, size: int) -> str:
    if size < 1000:
        return "stub"
    if ext == ".rm":
        return "needs_conversion"
    if ext == ".swf":
        return "legacy_flash"
    return "ok"


def slugify(*parts: str) -> str:
    raw = "-".join(p for p in parts if p)
    raw = re.sub(r"[^a-zA-Z0-9]+", "-", raw.lower()).strip("-")
    return raw[:120] or "item"


def iter_files() -> list[dict]:
    seen: dict[str, dict] = {}
    for root in ROOTS:
        if not root.exists():
            continue
        for dirpath, _, filenames in os.walk(root):
            for fname in filenames:
                if fname.startswith("."):
                    continue
                ext = Path(fname).suffix.lower()
                if ext not in ALL_EXTS:
                    continue
                full = Path(dirpath) / fname
                try:
                    st = full.stat()
                except OSError:
                    continue
                rel = canonical_rel(full)
                key = f"{rel}|{st.st_size}|{ext}"
                entry = {
                    "filename": fname,
                    "relative_path": rel,
                    "source_path": str(full),
                    "size_bytes": st.st_size,
                    "format": ext.lstrip("."),
                    "modified": date.fromtimestamp(st.st_mtime).isoformat(),
                }
                if key in seen:
                    seen[key]["alternate_paths"].append(str(full))
                    continue
                entry["alternate_paths"] = []
                seen[key] = entry
    return list(seen.values())


def build_item(raw: dict, index: int) -> dict:
    name = raw["filename"]
    ext = "." + raw["format"]
    week = parse_week(name)
    lecture_type, type_index = parse_type(name)
    topic = parse_topic(name, lecture_type)
    kind = classify_kind(ext, name)
    hms = HMS_RE.search(name)
    status = video_status(ext, raw["size_bytes"]) if kind == "video" else "ok"
    if kind == "test":
        status = "test"

    week_label = f"Week {week:02d}" if week is not None else None
    item_id = slugify(
        week_label or "misc",
        lecture_type or kind,
        str(type_index or ""),
        topic,
        raw["format"],
    )
    if item_id in {i.get("_slug") for i in []}:
        item_id = f"{item_id}-{index}"

    location = "main"
    rel = raw["relative_path"]
    if "RealPlayer Downloads" in raw["source_path"]:
        location = "realplayer_downloads"
    elif "Acupuncture Downloads" in raw["source_path"]:
        location = "acupuncture_downloads"
    elif "Extra iTunes" in raw["source_path"]:
        location = "itunes_extra"
    elif "iTunes Media/Movies" in raw["source_path"]:
        location = "itunes_movies"
    elif "Windows Desktop" in raw["source_path"]:
        location = "windows_realplayer"

    return {
        "id": item_id,
        "week": week,
        "week_label": week_label,
        "type": lecture_type,
        "type_index": type_index,
        "topic": topic,
        "kind": kind,
        "format": raw["format"],
        "playable": kind == "video"
        and raw["format"] in {"mp4", "m4v", "mov"}
        and raw["size_bytes"] >= 1000,
        "status": status,
        "size_bytes": raw["size_bytes"],
        "hms_id": hms.group(1) if hms else None,
        "filename": name,
        "location": location,
        "relative_path": rel,
        "source_path": raw["source_path"],
        "alternate_paths": raw["alternate_paths"],
        "modified": raw["modified"],
        "is_test": bool(TEST_RE.search(name)),
        "is_flash": bool(FLASH_RE.search(name)),
    }


def main() -> None:
    raw_files = iter_files()
    items = [build_item(r, i) for i, r in enumerate(raw_files, 1)]

    # Resolve duplicate ids
    id_counts: defaultdict[str, int] = defaultdict(int)
    for item in items:
        base = item["id"]
        id_counts[base] += 1
        if id_counts[base] > 1:
            item["id"] = f"{base}-{id_counts[base]}"

    videos = [i for i in items if i["kind"] == "video"]
    handouts = [i for i in items if i["kind"] == "handout"]
    tests = [i for i in items if i["kind"] == "test"]

    weeks = sorted({i["week"] for i in items if i["week"] is not None})

    catalog = {
        "meta": {
            "version": "0.1",
            "cataloged_at": date.today().isoformat(),
            "course": "Harvard Medical School AP101 — Acupuncture",
            "source_platform": "mycourses.med.harvard.edu",
            "course_year": "2009-2010",
            "primary_archive": "/Volumes/Macintosh HD - Data/Users/ching/Desktop/Harvard acupuncture/",
            "catalog_script": "Research/acupuncture/scripts/build_harvard_ap101_catalog.py",
            "notes": (
                "Catalog only — files remain on external drive. "
                "Deduped by relative path + size across HD - Data and HD 1 partitions. "
                "RealMedia (.rm) and legacy Flash (.swf) need conversion for modern playback."
            ),
        },
        "summary": {
            "total_items": len(items),
            "videos": len(videos),
            "handouts": len(handouts),
            "tests": len(tests),
            "playable_videos": sum(1 for v in videos if v["playable"]),
            "needs_conversion": sum(1 for v in videos if v["status"] == "needs_conversion"),
            "stubs": sum(1 for i in items if i["status"] == "stub"),
            "weeks_represented": weeks,
            "week_range": [min(weeks), max(weeks)] if weeks else None,
            "by_type": dict(
                sorted(
                    {
                        k: sum(1 for i in items if i["type"] == k)
                        for k in {i["type"] for i in items if i["type"]}
                    }.items()
                )
            ),
            "by_location": dict(
                sorted(
                    {
                        k: sum(1 for i in items if i["location"] == k)
                        for k in {i["location"] for i in items}
                    }.items()
                )
            ),
        },
        "items": sorted(
            items,
            key=lambda i: (
                i["week"] if i["week"] is not None else 999,
                i["type"] or "",
                i["type_index"] if i["type_index"] is not None else 0,
                i["kind"],
                i["topic"],
            ),
        ),
    }

    out = Path(__file__).resolve().parents[1] / "data" / "harvard-ap101-catalog.json"
    out.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(items)} items to {out}")
    print(json.dumps(catalog["summary"], indent=2))


if __name__ == "__main__":
    main()
