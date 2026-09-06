#!/usr/bin/env python3
"""Build lecture packets that link Otter transcripts to screenshot slide sequences."""

from __future__ import annotations

import json
import os
import re
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]  # Research/lectures/scripts -> repo root? 
# This file: Research/lectures/scripts/build_screenshot_lecture_packets.py
# parents[0]=scripts, [1]=lectures, [2]=Research, [3]=repo
REPO = Path(__file__).resolve().parents[3]
LECTURES = REPO / "Research" / "lectures"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".heic"}
DOC_EXTS = {
    ".txt", ".pdf", ".mp3", ".m4a", ".mp4", ".zip", ".docx", ".rtf", ".md",
}

PACKS = [
    {
        "id": "dpc-hartman-2026-05",
        "title": "Stefan Hartman — starting a DPC practice (LLC / S-corp)",
        "speaker": "Stefan Hartman",
        "approx_date": "2026-05-12",
        "source_root": Path(
            "/Users/nuu/Downloads/Stefan Hartman presented on starting a DPC practice, "
            "emphasizing the benefits of an LLC, S corporation 512 2026"
        ),
        "slides_subdir": None,  # screenshots at root
        "primary_branch": "integrative-medicine",
        "related_branches": [],
        "themes": ["practice_systems"],
        "medical_terms": ["ethics_systems"],
        "research_priority": "low",
        "local_downloads_id": "dpc-hartman-2026-05",
        "notes": "Otter transcript + 20 slide screenshots. Practice/business — low clinical priority.",
    },
    {
        "id": "dna-repair-andrews-2026-04",
        "title": "DNA repair healing with Dr. Bill Andrews",
        "speaker": "Bill Andrews",
        "approx_date": "2026-04-28",
        "source_root": Path("/Users/nuu/Downloads/DNA repair healing with Dr. Bill Andrews 4 28 2026"),
        "slides_subdir": None,
        "primary_branch": "integrative-medicine",
        "related_branches": ["nutrition"],
        "themes": ["longevity", "regenerative", "dna_repair"],
        "medical_terms": ["regenerative", "longevity"],
        "research_priority": "normal",
        "local_downloads_id": "dna-repair-andrews-2026-04",
        "notes": "Otter transcript + PDF + 90 slide screenshots coordinated with lecture.",
    },
    {
        "id": "ivermectin-ayurveda-2026-05",
        "title": "Ivermectin for longevity, cancer, neurodegeneration & quantum Ayurveda",
        "speaker": None,
        "approx_date": "2026-05-19",
        "source_root": Path(
            "/Users/nuu/Downloads/Ivermectin for longevity, cancer, neurodegenerative diseases, "
            "& potential of quantum Ayurveda technology 5 19 2026"
        ),
        "slides_subdir": (
            "Ivermectin for longevity, cancer, neurodegenerative diseases, "
            "& potential of quantum Ayurveda technology slides 5 19 2026"
        ),
        "primary_branch": "integrative-medicine",
        "related_branches": ["immune", "materia-medica"],
        "themes": ["longevity", "cancer_onco", "neuro", "infection", "ayurveda"],
        "medical_terms": ["cancer_onco", "neuro", "infection_covid", "herbal_botanical", "longevity"],
        "research_priority": "normal",
        "local_downloads_id": "ivermectin-ayurveda-2026-05",
        "notes": "Dedicated slides/ subfolder with 99 screenshots + Otter txt/mp3/zip.",
    },
]


def shot_sort_key(rel: str):
    m = re.search(r"(\d{4}-\d{2}-\d{2}).*?(\d+)[.:](\d+)[.:](\d+)", rel)
    if m:
        return (m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), rel)
    return (rel,)


def branch_path(name: str) -> str:
    return f"Research/{name}/"


def scan_pack(cfg: dict) -> dict:
    root: Path = cfg["source_root"]
    if not root.exists():
        raise FileNotFoundError(root)

    slides_root = root / cfg["slides_subdir"] if cfg.get("slides_subdir") else root
    docs: list[dict] = []
    shots: list[dict] = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fname in filenames:
            if fname == ".DS_Store":
                continue
            full = Path(dirpath) / fname
            rel = full.relative_to(root).as_posix()
            ext = full.suffix.lower()
            try:
                sz = full.stat().st_size
            except OSError:
                continue
            is_shot = ext in IMAGE_EXTS or fname.lower().startswith("screenshot")
            # For ivermectin, only count images under slides_subdir as slides
            if is_shot:
                if cfg.get("slides_subdir"):
                    if not rel.startswith(cfg["slides_subdir"]):
                        continue
                shots.append(
                    {
                        "index": 0,  # fill later
                        "filename": fname,
                        "relative_path": rel,
                        "source_path": str(full),
                        "size_bytes": sz,
                    }
                )
            elif ext in DOC_EXTS:
                kind = (
                    "audio"
                    if ext in {".mp3", ".m4a"}
                    else "archive"
                    if ext == ".zip"
                    else "transcript"
                    if ext == ".txt"
                    else "document"
                )
                docs.append(
                    {
                        "filename": fname,
                        "relative_path": rel,
                        "source_path": str(full),
                        "size_bytes": sz,
                        "format": ext.lstrip("."),
                        "kind": kind,
                    }
                )

    shots.sort(key=lambda s: shot_sort_key(s["relative_path"]))
    for i, s in enumerate(shots, 1):
        s["index"] = i
        s["slide_id"] = f"slide-{i:03d}"

    docs.sort(key=lambda d: (-d["size_bytes"], d["relative_path"]))
    transcript = next((d for d in docs if d["kind"] == "transcript"), None)
    audio = next((d for d in docs if d["kind"] == "audio"), None)

    return {
        "docs": docs,
        "shots": shots,
        "slides_root": str(slides_root),
        "transcript": transcript,
        "audio": audio,
    }


def write_packet(cfg: dict, scanned: dict) -> Path:
    pkt_dir = LECTURES / cfg["id"]
    (pkt_dir / "raw").mkdir(parents=True, exist_ok=True)
    (pkt_dir / "slides").mkdir(parents=True, exist_ok=True)
    (pkt_dir / "derived").mkdir(parents=True, exist_ok=True)

    shots = scanned["shots"]
    docs = scanned["docs"]
    transcript = scanned["transcript"]
    audio = scanned["audio"]

    # screenshot manifest (paths stay in Downloads — do not copy PNGs)
    manifest = {
        "version": "0.1",
        "cataloged_at": date.today().isoformat(),
        "source_root": str(cfg["source_root"]),
        "slides_root": scanned["slides_root"],
        "sync": "screenshots_only",
        "screenshot_count": len(shots),
        "naming": "Ordered by Screenshot timestamp in filename; mapped to slide-001…",
        "screenshots": shots,
        "note": "Images remain in Downloads. Use this manifest to coordinate with Otter transcript timestamps.",
    }
    (pkt_dir / "slides" / "screenshot-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    # lightweight index markdown
    lines = [
        f"# {cfg['title']} — slide screenshot index",
        "",
        f"**Count:** {len(shots)}  ",
        f"**Source slides folder:** `{scanned['slides_root']}`  ",
        "",
        "Screenshots stay on disk; this index coordinates lecture ↔ slides.",
        "",
        "| # | File |",
        "|--:|------|",
    ]
    for s in shots:
        lines.append(f"| {s['index']} | `{s['filename']}` |")
    (pkt_dir / "slides" / "screenshot-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    (pkt_dir / "slides" / "README.md").write_text(
        "\n".join(
            [
                "# Slides (screenshot sequence)",
                "",
                f"- Manifest: [`screenshot-manifest.json`](screenshot-manifest.json) ({len(shots)} frames)",
                f"- Index: [`screenshot-index.md`](screenshot-index.md)",
                f"- On disk: `{scanned['slides_root']}`",
                "",
                "Do not copy PNGs into git; open via source_path in the manifest.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    # raw pointers
    raw_lines = [
        "# Raw (Otter)",
        "",
        "Files remain in Downloads; paths recorded for coordination.",
        "",
    ]
    if transcript:
        raw_lines += [
            f"- **Transcript:** `{transcript['source_path']}`",
            f"  - {transcript['size_bytes']} bytes",
            "",
        ]
    if audio:
        raw_lines += [
            f"- **Audio:** `{audio['source_path']}`",
            f"  - {audio['size_bytes']} bytes",
            "",
        ]
    for d in docs:
        if d in (transcript, audio):
            continue
        raw_lines.append(f"- **{d['kind']}:** `{d['source_path']}` ({d['size_bytes']} bytes)")
    (pkt_dir / "raw" / "README.md").write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

    (pkt_dir / "derived" / "README.md").write_text(
        "\n".join(
            [
                "# Derived",
                "",
                "Gem cleanup / study / teach outputs go here.",
                "",
                f"- Status: `raw` (screenshots coordinated; Gem not run yet)",
                f"- Suggested Gem inputs: Otter transcript + screenshot sequence ({len(shots)} frames)",
                "",
            ]
        ),
        encoding="utf-8",
    )

    packet = {
        "id": cfg["id"],
        "title": cfg["title"],
        "speaker": cfg.get("speaker"),
        "approx_date": cfg.get("approx_date"),
        "primary_branch": cfg["primary_branch"],
        "related_branches": cfg.get("related_branches") or [],
        "branches": [branch_path(cfg["primary_branch"])]
        + [branch_path(b) for b in (cfg.get("related_branches") or [])],
        "themes": cfg.get("themes") or [],
        "medical_terms": cfg.get("medical_terms") or [],
        "research_priority": cfg.get("research_priority", "normal"),
        "sync": "screenshots_only",
        "gem_status": "raw",
        "local_downloads_id": cfg.get("local_downloads_id"),
        "paths": {
            "packet": f"Research/lectures/{cfg['id']}/",
            "raw": f"Research/lectures/{cfg['id']}/raw/",
            "slides": f"Research/lectures/{cfg['id']}/slides/",
            "derived": f"Research/lectures/{cfg['id']}/derived/",
            "screenshot_manifest": f"Research/lectures/{cfg['id']}/slides/screenshot-manifest.json",
        },
        "otter": {
            "transcript": transcript["source_path"] if transcript else None,
            "audio": audio["source_path"] if audio else None,
            "source_root": str(cfg["source_root"]),
        },
        "slides": {
            "status": "screenshots_in_downloads",
            "screenshot_count": len(shots),
            "slides_root": scanned["slides_root"],
            "first": shots[0]["source_path"] if shots else None,
            "last": shots[-1]["source_path"] if shots else None,
            "manifest": f"Research/lectures/{cfg['id']}/slides/screenshot-manifest.json",
        },
        "documents": docs,
        "derived": {
            "gem_cleanup": False,
            "study_guide": False,
            "teach_outline": False,
        },
        "knowledge_leaves": [],
        "notes": cfg.get("notes"),
        "cataloged_at": date.today().isoformat(),
    }
    (pkt_dir / "packet.json").write_text(
        json.dumps(packet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    (pkt_dir / "README.md").write_text(
        "\n".join(
            [
                f"# {cfg['title']}",
                "",
                "| | |",
                "|--|--|",
                f"| Speaker | {cfg.get('speaker') or '—'} |",
                f"| Date | {cfg.get('approx_date') or '—'} |",
                f"| Branch | `{cfg['primary_branch']}` |",
                f"| Sync | `screenshots_only` ({len(shots)} frames) |",
                f"| Gem | `raw` |",
                "",
                "## Coordination",
                "",
                "- Otter transcript/audio paths → [`raw/README.md`](raw/README.md)",
                f"- Slide screenshots → [`slides/screenshot-manifest.json`](slides/screenshot-manifest.json)",
                "- Files stay in Downloads; packet indexes them for Gem cleanup next",
                "",
                f"**Source:** `{cfg['source_root']}`",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return pkt_dir


def main() -> None:
    LECTURES.mkdir(parents=True, exist_ok=True)
    results = []
    for cfg in PACKS:
        scanned = scan_pack(cfg)
        path = write_packet(cfg, scanned)
        results.append((cfg["id"], len(scanned["shots"]), path))
        print(f"OK {cfg['id']}: {len(scanned['shots'])} screenshots → {path}")

    # refresh lectures README table
    readme = LECTURES / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        # rebuild Packets table section simply
        table_rows = [
            "| ID | Branch | Sync | Notes |",
            "|----|--------|------|-------|",
            "| [mccullough-covid-early-tx-aosrd-2022](mccullough-covid-early-tx-aosrd-2022/) | immune | slides_only | AOSRD Sat #8 — 71 slides extracted |",
        ]
        meta = {c["id"]: c for c in PACKS}
        for pid, n, _ in results:
            c = meta[pid]
            table_rows.append(
                f"| [{pid}]({pid}/) | {c['primary_branch']} | screenshots_only ({n}) | Otter + slide screenshots |"
            )
        new_table = "## Packets\n\n" + "\n".join(table_rows) + "\n"
        text = re.sub(r"## Packets\n\n.*?(?=\n## Related)", new_table + "\n", text, flags=re.S)
        readme.write_text(text, encoding="utf-8")
        print("Updated lectures README")


if __name__ == "__main__":
    main()
