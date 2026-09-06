#!/usr/bin/env python3
"""Build aosrd-catalog.json from AOSRD conference materials on external drive."""

from __future__ import annotations

import json
import os
import re
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"
OUT_PATH = DATA_DIR / "aosrd-catalog.json"

ROOTS = [
    Path("/Volumes/Macintosh HD - Data/Users/chingchen/Downloads/AOSRd Slide Show 2022"),
    Path("/Volumes/Macintosh HD 1/Users/chingchen/Downloads/AOSRd Slide Show 2022"),
]

MEDIA_EXTS = {
    ".pdf", ".ppt", ".pptx", ".mp4", ".m4v", ".mov", ".m4a", ".mp3", ".jpg", ".jpeg", ".png",
}
SKIP_NAMES = {".ds_store"}
SESSION_DIR_RE = re.compile(r"^(\d+)\.\s*(.+)$")
DAYS = ("Friday", "Saturday", "Sunday")


def slugify(*parts: str) -> str:
    raw = "-".join(p for p in parts if p)
    raw = re.sub(r"[^a-zA-Z0-9]+", "-", raw.lower()).strip("-")
    return raw[:120] or "lecture"


def should_skip(name: str) -> bool:
    lower = name.lower()
    if lower in SKIP_NAMES:
        return True
    if name.startswith(".~lock") or name.startswith("~"):
        return True
    if lower.endswith("#"):
        return True
    return False


def parse_topic(filename: str, speaker: str) -> str:
    stem = Path(filename).stem
    stem = re.sub(r"^\d+\.\s*", "", stem)
    for prefix in (f"{speaker}-", f"{speaker} ", speaker):
        if stem.lower().startswith(prefix.lower()):
            stem = stem[len(prefix) :].strip(" -_")
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem or filename


def classify_kind(ext: str) -> str:
    if ext in {".mp4", ".m4v", ".mov"}:
        return "video"
    if ext in {".m4a", ".mp3"}:
        return "audio"
    if ext in {".jpg", ".jpeg", ".png"}:
        return "image"
    if ext in {".ppt", ".pptx"}:
        return "slides"
    return "document"


def iter_files() -> list[dict]:
    seen: dict[str, dict] = {}
    for root in ROOTS:
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            rel_dir = Path(dirpath).relative_to(root)
            parts = rel_dir.parts

            day = parts[0] if parts and parts[0] in DAYS else None
            session_num = None
            speaker = None
            if len(parts) >= 2 and parts[0] in DAYS:
                m = SESSION_DIR_RE.match(parts[1])
                if m:
                    session_num = int(m.group(1))
                    speaker = m.group(2).strip()
            elif parts and parts[0] == "AOSRD Between Lecture Slide Show":
                day = "Interstitial"
                speaker = "Faculty"
                session_num = 0

            for fname in filenames:
                if should_skip(fname):
                    continue
                ext = Path(fname).suffix.lower()
                if ext not in MEDIA_EXTS:
                    continue
                full = Path(dirpath) / fname
                try:
                    st = full.stat()
                except OSError:
                    continue
                key = f"{fname}|{st.st_size}|{ext}"
                if key in seen:
                    seen[key]["alternate_paths"].append(str(full))
                    continue

                topic = parse_topic(fname, speaker or "")
                entry = {
                    "filename": fname,
                    "relative_path": str(full.relative_to(root)),
                    "source_path": str(full),
                    "size_bytes": st.st_size,
                    "format": ext.lstrip("."),
                    "kind": classify_kind(ext),
                    "day": day,
                    "session": session_num,
                    "speaker": speaker,
                    "topic": topic,
                    "alternate_paths": [],
                }
                seen[key] = entry
    return list(seen.values())


def build_lectures(files: list[dict]) -> list[dict]:
    groups: dict[str, list[dict]] = {}
    for f in files:
        if f["day"] in (None, "Interstitial") and f["relative_path"] == "AOSRSD 2022 Cat notes.pdf":
            key = "meta|catalog-notes"
        elif f["day"] == "Interstitial":
            key = "interstitial|faculty"
        elif f["day"] and f["session"] is not None and f["speaker"]:
            key = f"{f['day']}|{f['session']}|{f['speaker']}"
        else:
            key = f"misc|{f['relative_path']}"
        groups.setdefault(key, []).append(f)

    lectures = []
    for key, group in groups.items():
        primary = sorted(
            group,
            key=lambda x: (
                0 if x["kind"] == "slides" else 1 if x["kind"] == "video" else 2,
                -x["size_bytes"],
            ),
        )[0]
        day = primary.get("day")
        session = primary.get("session")
        speaker = primary.get("speaker") or "Unknown"
        topic = primary.get("topic") or speaker
        if key == "meta|catalog-notes":
            topic = "AOSRD 2022 catalog notes"
            speaker = "Conference"
            day = None
            session = None

        lecture_id = slugify(day or "meta", str(session or ""), speaker, topic)
        lectures.append(
            {
                "id": lecture_id,
                "day": day,
                "session": session,
                "speaker": speaker,
                "topic": topic,
                "primary_file": primary["relative_path"],
                "formats": sorted({g["format"] for g in group}),
                "kinds": sorted({g["kind"] for g in group}),
                "file_count": len(group),
                "files": sorted(group, key=lambda x: x["filename"]),
            }
        )

    order = {"Friday": 1, "Saturday": 2, "Sunday": 3, "Interstitial": 4}
    return sorted(
        lectures,
        key=lambda l: (
            order.get(l["day"] or "", 99),
            l["session"] if l["session"] is not None else 999,
            l["speaker"],
        ),
    )


def main() -> None:
    files = iter_files()
    lectures = build_lectures(files)

    # Resolve duplicate lecture ids
    id_counts: dict[str, int] = {}
    for lec in lectures:
        base = lec["id"]
        id_counts[base] = id_counts.get(base, 0) + 1
        if id_counts[base] > 1:
            lec["id"] = f"{base}-{id_counts[base]}"

    catalog = {
        "meta": {
            "version": "0.1",
            "cataloged_at": date.today().isoformat(),
            "conference": "AOSRD — American Osteopathic Society Congress of Medical Excellence",
            "year": 2022,
            "event": "Las Vegas (virtual)",
            "dates": "March 25–27, 2022",
            "primary_archive": str(ROOTS[0]),
            "catalog_script": "Research/acupuncture/scripts/build_aosrd_catalog.py",
            "notes": (
                "Catalog of AOSRD 2022 slide decks and recordings from chingchen Downloads. "
                "Grouped by conference day and session folder. Files remain on external drive."
            ),
        },
        "summary": {
            "lectures": len(lectures),
            "files": len(files),
            "by_day": {
                d: sum(1 for l in lectures if l["day"] == d)
                for d in DAYS + ("Interstitial",)
            },
            "by_kind": dict(
                sorted({k: sum(1 for f in files if f["kind"] == k) for k in {f["kind"] for f in files}}.items())
            ),
            "with_video": sum(1 for l in lectures if "video" in l["kinds"]),
            "with_audio": sum(1 for l in lectures if "audio" in l["kinds"]),
            "slides_only": sum(
                1 for l in lectures if l["kinds"] == ["slides"] or l["kinds"] == ["document", "slides"]
            ),
        },
        "lectures": lectures,
        "files": sorted(files, key=lambda f: (f.get("day") or "", f.get("session") or 999, f["filename"])),
    }

    OUT_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(lectures)} lectures ({len(files)} files) to {OUT_PATH}")
    print(json.dumps(catalog["summary"], indent=2))


if __name__ == "__main__":
    main()
