#!/usr/bin/env python3
"""
AOSRD Hybrid Lecture Processor

- Scrapes aosrd.org/webinars and pairs videos with PDFs
- Prefers PDF slides when available; else scene detection + frames
- Local faster-whisper transcription
- Ultra-lean Markdown study guide for Cursor
- Title format: # Title \\n **Lecturer · Date**

Outputs under:
  Research/integrative-medicine/aosrd-webinars/study-guide/

Optional deps: see requirements-aosrd-hybrid.txt
This is NOT the acupuncture pipeline (see AGENTS.md).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# Heavy optional imports deferred until process time where possible
try:
    from pdf2image import convert_from_path

    HAS_PDF2IMAGE = True
except ImportError:
    HAS_PDF2IMAGE = False

# ====================== CONFIG ======================
# .../Research/integrative-medicine/aosrd-webinars/scripts/this.py → repo root
REPO_ROOT = Path(__file__).resolve().parents[4]
WEBINARS_URL = "https://aosrd.org/webinars/"
BASE_OUTPUT = REPO_ROOT / "Research" / "integrative-medicine" / "aosrd-webinars" / "study-guide"
WHISPER_MODEL = os.environ.get("AOSRD_WHISPER_MODEL", "medium")
DEVICE = os.environ.get("AOSRD_WHISPER_DEVICE", "cpu")  # "cuda" if available
COMPUTE_TYPE = os.environ.get("AOSRD_WHISPER_COMPUTE", "int8")
SCENE_THRESHOLD = 0.40
MAX_FRAMES = 30
USE_PDF_PAGES = True
# ====================================================

BASE_OUTPUT.mkdir(parents=True, exist_ok=True)


def normalize_title(title: str) -> str:
    """Clean title for matching Video ↔ PDF."""
    title = re.sub(r"[–—-]\s*(Video|PDF|Text|Slideshow).*$", "", title, flags=re.I)
    title = re.sub(r"\s*\(\s*(Video|PDF|Text).*?\)", "", title, flags=re.I)
    title = re.sub(r"\s+\d{1,2}[-/]\w+[-/]\d{2,4}.*$", "", title)
    title = re.sub(r"\s+", " ", title).strip().lower()
    return title


def similar(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def parse_title(raw_title: str) -> tuple[str, str, str]:
    """Return (clean_title, lecturer, date)."""
    title = re.sub(r"[–—-]\s*(Video|PDF|Text|Slideshow).*$", "", raw_title, flags=re.I)
    title = re.sub(r"\s*\(\s*(Video|PDF|Text).*?\)", "", title, flags=re.I)
    title = title.strip()

    date_match = re.search(
        r"(\d{1,2}[-/]\w+[-/]\d{2,4}|\w+\s+\d{4}|\d{1,2}\s+\w+\s+\d{4})",
        title,
        re.I,
    )
    date = date_match.group(0).strip() if date_match else ""

    if date:
        title = title.replace(date, "").strip(" –—-")

    lecturer = ""
    lect_match = re.search(
        r"(?:with\s+)?(Dr\.?\s+[A-Za-z\s\.]+?)(?:\s*[–—-]|$)",
        title,
        re.I,
    )
    if lect_match:
        lecturer = lect_match.group(1).strip()
        title = title.replace(lect_match.group(0), "").strip(" –—-")

    title = re.sub(r"\s+", " ", title).strip(" –—-")
    return title, lecturer, date


def scrape_webinars():
    print("Scraping webinars page...")
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (compatible; BodiesDontLieOS/1.0; "
            "+https://github.com/ZC-111/Bodies-Dont-Lie-OS)"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    resp = requests.get(WEBINARS_URL, timeout=30, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    videos = []
    pdfs = []

    for h5 in soup.find_all("h5"):
        a = h5.find("a")
        if not a or not a.get("href"):
            continue
        text = a.get_text(strip=True)
        href = a["href"]
        full_url = urljoin(WEBINARS_URL, href)

        if re.search(r"\.(pdf)$", href, re.I) or "PDF" in text or "Text" in text:
            pdfs.append({"title": text, "url": full_url, "norm": normalize_title(text)})
        elif "youtu" in href or "vimeo" in href or "Video" in text:
            videos.append({"title": text, "url": full_url, "norm": normalize_title(text)})

    results = []
    for v in videos:
        best_pdf = None
        best_score = 0.0
        for p in pdfs:
            score = similar(v["norm"], p["norm"])
            if score > best_score and score > 0.72:
                best_score = score
                best_pdf = p
        results.append(
            {
                "title": v["title"],
                "video_url": v["url"],
                "pdf_url": best_pdf["url"] if best_pdf else None,
                "has_pdf": best_pdf is not None,
                "match_score": round(best_score, 3) if best_pdf else 0,
            }
        )

    return results


def download_file(url: str, dest: Path):
    print(f"  Downloading {url} → {dest.name}")
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (compatible; BodiesDontLieOS/1.0; "
            "+https://github.com/ZC-111/Bodies-Dont-Lie-OS)"
        )
    }
    r = requests.get(url, stream=True, timeout=60, headers=headers)
    r.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
    return dest


def download_video(url: str, out_dir: Path) -> Path:
    import yt_dlp

    out_dir.mkdir(parents=True, exist_ok=True)
    ydl_opts = {
        "format": "best[height<=720]",
        "outtmpl": str(out_dir / "video.%(ext)s"),
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return Path(ydl.prepare_filename(info))


def transcribe(path: Path):
    from faster_whisper import WhisperModel

    print(f"  Transcribing ({WHISPER_MODEL} on {DEVICE})...")
    model = WhisperModel(WHISPER_MODEL, device=DEVICE, compute_type=COMPUTE_TYPE)
    segments, info = model.transcribe(str(path), beam_size=5, vad_filter=True)
    timed = [{"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments]
    return timed, info.duration


def detect_scenes(video_path: Path, threshold: float = 0.40):
    print("  Detecting scenes...")
    cmd = [
        "ffmpeg",
        "-i",
        str(video_path),
        "-vf",
        f"select='gt(scene,{threshold})',showinfo",
        "-f",
        "null",
        "-",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    times = [float(t) for t in re.findall(r"pts_time:(\d+\.\d+)", result.stderr)]
    return times


def extract_frame(video_path: Path, ts: float, out_path: Path, offset: float = 0.3):
    cmd = [
        "ffmpeg",
        "-ss",
        f"{max(0, ts + offset):.3f}",
        "-i",
        str(video_path),
        "-frames:v",
        "1",
        "-q:v",
        "3",
        "-y",
        str(out_path),
    ]
    subprocess.run(cmd, capture_output=True, check=True)


def pdf_to_frames(pdf_path: Path, frames_dir: Path, max_pages: int = 40):
    if not HAS_PDF2IMAGE:
        raise RuntimeError("pdf2image not installed. See requirements-aosrd-hybrid.txt")
    frames_dir.mkdir(exist_ok=True)
    print("  Converting PDF pages to images...")
    images = convert_from_path(str(pdf_path), dpi=150, first_page=1, last_page=max_pages)
    paths = []
    for i, img in enumerate(images):
        p = frames_dir / f"pdf_{i:03d}.jpg"
        img.save(p, "JPEG", quality=85)
        paths.append(p.name)
    return paths


def build_lean_markdown(
    out_dir: Path,
    raw_title: str,
    video_url: str,
    segments,
    duration,
    frame_files,
    source="pdf",
):
    clean_title, lecturer, date = parse_title(raw_title)

    md_path = out_dir / "visual-transcript.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {clean_title}\n")
        if lecturer or date:
            meta = " · ".join(filter(None, [lecturer, date]))
            f.write(f"**{meta}**\n")
        f.write(f"\nSource: {video_url}\n")
        f.write(f"Duration: {duration / 60:.1f} min\n")
        f.write(f"Frames: {source}\n\n---\n\n")

        for i, frame in enumerate(frame_files):
            if segments:
                idx = min(
                    int(i / max(1, len(frame_files)) * len(segments)),
                    len(segments) - 1,
                )
                text = segments[idx]["text"]
            else:
                text = ""

            f.write(f"**Slide {i + 1}**\n")
            f.write(f"![](frames/{frame})\n")
            if text:
                f.write(f"{text}\n")
            f.write("\n")

    print(f"  → {md_path}")
    return md_path


def process_one(item: dict, force_scene: bool = False):
    safe_name = re.sub(r"[^\w\s-]", "", item["title"])[:60].strip().replace(" ", "_")
    out_dir = BASE_OUTPUT / safe_name
    frames_dir = out_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nProcessing: {item['title'][:70]}...")
    print(f"  Has PDF: {item['has_pdf']}")

    video_path = download_video(item["video_url"], out_dir)
    segments, duration = transcribe(video_path)

    frame_files = []
    source = "scene"

    if item["has_pdf"] and not force_scene and USE_PDF_PAGES:
        pdf_path = out_dir / "slides.pdf"
        download_file(item["pdf_url"], pdf_path)
        try:
            frame_files = pdf_to_frames(pdf_path, frames_dir, max_pages=MAX_FRAMES)
            source = "pdf"
        except Exception as e:
            print(f"  PDF conversion failed ({e}), falling back to scene detection")
            force_scene = True

    if not frame_files or force_scene:
        scenes = detect_scenes(video_path, SCENE_THRESHOLD)
        if len(scenes) > MAX_FRAMES:
            step = len(scenes) / MAX_FRAMES
            scenes = [scenes[int(i * step)] for i in range(MAX_FRAMES)]
        for i, t in enumerate(scenes):
            name = f"scene_{i:03d}_{t:.1f}s.jpg"
            extract_frame(video_path, t, frames_dir / name)
            frame_files.append(name)
        source = "scene"

    build_lean_markdown(
        out_dir,
        item["title"],
        item["video_url"],
        segments,
        duration,
        frame_files,
        source,
    )

    with open(out_dir / "meta.json", "w", encoding="utf-8") as f:
        json.dump(item, f, indent=2)

    print("  Done.")
    return out_dir


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AOSRD hybrid lecture processor")
    parser.add_argument("--list", action="store_true", help="Only list webinars + PDF status")
    parser.add_argument("--process", type=int, help="Process the N-th item (0-based)")
    parser.add_argument("--process-all", action="store_true", help="Process everything (careful!)")
    parser.add_argument(
        "--force-scene",
        action="store_true",
        help="Ignore PDFs and always use scene detection",
    )
    args = parser.parse_args(argv)

    catalog = scrape_webinars()
    print(f"\nFound {len(catalog)} videos")
    has_pdf_count = sum(1 for x in catalog if x["has_pdf"])
    print(f"With attached PDF: {has_pdf_count}")

    BASE_OUTPUT.mkdir(parents=True, exist_ok=True)
    catalog_path = BASE_OUTPUT / "catalog.json"
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print(f"Catalog saved → {catalog_path}")

    if args.list:
        for i, item in enumerate(catalog):
            flag = "PDF" if item["has_pdf"] else "video-only"
            print(f"{i:3d} | {flag:10s} | {item['title'][:80]}")
        return 0

    if args.process is not None:
        process_one(catalog[args.process], force_scene=args.force_scene)
        return 0

    if args.process_all:
        for item in catalog:
            try:
                process_one(item, force_scene=args.force_scene)
            except Exception as e:
                print(f"FAILED: {item['title'][:50]} → {e}")
        return 0

    print("\nUsage examples:")
    rel = "Research/integrative-medicine/aosrd-webinars/scripts/aosrd_hybrid_processor.py"
    print(f"  python3 {rel} --list")
    print(f"  python3 {rel} --process 0")
    print(f"  python3 {rel} --process 12 --force-scene")
    return 0


if __name__ == "__main__":
    sys.exit(main())
