#!/usr/bin/env python3
"""Batch convert Harvard AP101 RealMedia (.rm) files to MP4."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import imageio_ffmpeg
except ImportError:
    print("Install imageio-ffmpeg: python3 -m pip install --user imageio-ffmpeg", file=sys.stderr)
    raise

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"
CATALOG_PATH = DATA_DIR / "harvard-ap101-catalog.json"
OUT_ROOT = SCRIPT_DIR.parent / "sources" / "harvard-ap101" / "videos"
MANIFEST_PATH = DATA_DIR / "harvard-ap101-conversions.json"

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
MIN_SOURCE_BYTES = 1000


def week_dir(week: int | None) -> str:
    return f"week-{week:02d}" if week is not None else "misc"


def convert_one(src: Path, dst: Path) -> dict:
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        FFMPEG,
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        str(src),
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "23",
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-movflags",
        "+faststart",
        str(dst),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    ok = proc.returncode == 0 and dst.exists() and dst.stat().st_size > 0
    return {
        "ok": ok,
        "returncode": proc.returncode,
        "stderr": proc.stderr.strip()[-500:] if proc.stderr else "",
        "output_bytes": dst.stat().st_size if dst.exists() else 0,
    }


def rel_repo(path: Path) -> str:
    repo = SCRIPT_DIR.parents[2]
    return str(path.relative_to(repo))


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    items = [i for i in catalog["items"] if i.get("format") == "rm"]

    manifest = {
        "meta": {
            "version": "0.1",
            "converted_at": datetime.now(timezone.utc).isoformat(),
            "ffmpeg": FFMPEG,
            "output_root": rel_repo(OUT_ROOT),
        },
        "results": [],
    }

    converted = 0
    skipped = 0
    failed = 0
    stubbed = 0

    for item in items:
        src = Path(item["source_path"])
        entry = {
            "id": item["id"],
            "source_path": item["source_path"],
            "week": item.get("week"),
            "topic": item.get("topic"),
        }

        if item.get("status") == "stub" or item.get("size_bytes", 0) < MIN_SOURCE_BYTES:
            entry["status"] = "skipped_stub"
            stubbed += 1
            manifest["results"].append(entry)
            continue

        dst = OUT_ROOT / week_dir(item.get("week")) / f"{item['id']}.mp4"
        entry["output_path"] = rel_repo(dst)

        if dst.exists() and dst.stat().st_size > 0:
            entry["status"] = "already_exists"
            entry["output_bytes"] = dst.stat().st_size
            item["converted_mp4"] = entry["output_path"]
            item["playable"] = True
            item["status"] = "converted"
            item["format"] = "mp4"
            skipped += 1
            manifest["results"].append(entry)
            continue

        if not src.exists():
            entry["status"] = "missing_source"
            failed += 1
            manifest["results"].append(entry)
            continue

        print(f"Converting: {item['id']}")
        result = convert_one(src, dst)
        entry.update(result)

        if result["ok"]:
            entry["status"] = "converted"
            item["converted_mp4"] = entry["output_path"]
            item["converted_from"] = item["source_path"]
            item["playable"] = True
            item["status"] = "converted"
            item["format"] = "mp4"
            converted += 1
            print(f"  -> {entry['output_path']} ({result['output_bytes']:,} bytes)")
        else:
            entry["status"] = "failed"
            if dst.exists():
                dst.unlink()
            failed += 1
            print(f"  FAILED: {result['stderr']}", file=sys.stderr)

        manifest["results"].append(entry)

    manifest["summary"] = {
        "total_rm": len(items),
        "converted": converted,
        "already_exists": skipped,
        "failed": failed,
        "skipped_stub": stubbed,
    }

    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    catalog["meta"]["conversion"] = {
        "converted_at": manifest["meta"]["converted_at"],
        "manifest": rel_repo(MANIFEST_PATH),
        "output_root": rel_repo(OUT_ROOT),
        **manifest["summary"],
    }
    if "summary" in catalog:
        catalog["summary"]["converted_videos"] = sum(
            1 for i in catalog["items"] if i.get("status") == "converted"
        )
        catalog["summary"]["playable_videos"] = sum(
            1 for i in catalog["items"] if i.get("playable")
        )

    CATALOG_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps(manifest["summary"], indent=2))


if __name__ == "__main__":
    main()
