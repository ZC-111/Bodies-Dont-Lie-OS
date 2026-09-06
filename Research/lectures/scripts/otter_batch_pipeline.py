#!/usr/bin/env python3
"""
Otter.ai Batch Pipeline — List, Export, Download Screenshots, Create Packets

Phases (run individually or all together):
  1. list    — Scrape conversation list from Otter home page → manifest JSON
  2. export  — Download transcript+summary ZIP for each conversation
  3. slides  — Download meeting screenshots for each conversation
  4. packet  — Create lecture-packet folder structure + packet.json

Usage:
  python3 otter_batch_pipeline.py list
  python3 otter_batch_pipeline.py export [--ids ID1,ID2,...]
  python3 otter_batch_pipeline.py slides [--ids ID1,ID2,...]
  python3 otter_batch_pipeline.py packet [--ids ID1,ID2,...]
  python3 otter_batch_pipeline.py all

Requirements:
  pip3 install playwright
  python3 -m playwright install chromium
"""
import argparse
import json
import re
import sys
import time
import zipfile
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[3]
LECTURES_DIR = REPO_ROOT / "Research" / "lectures"
MANIFEST_PATH = LECTURES_DIR / "data" / "otter-manifest.json"
PROFILE_DIR = Path.home() / ".otter-playwright-profile"


def get_browser(playwright):
    """Launch persistent Chromium with saved Otter session."""
    return playwright.chromium.launch_persistent_context(
        str(PROFILE_DIR),
        headless=False,
        viewport={"width": 1280, "height": 900},
    )


def ensure_signed_in(page):
    """Navigate to Otter home; if not signed in, wait for user."""
    page.goto("https://otter.ai/home", wait_until="domcontentloaded", timeout=60_000)
    time.sleep(3)
    if "signin" in page.url or "login" in page.url or "meet-otter" in page.url:
        print("\n=== Sign in to Otter.ai in the browser window ===")
        print("Waiting for sign-in (up to 5 minutes)...")
        page.wait_for_url("**/home**", timeout=300_000)
        print("Signed in!")
        time.sleep(2)


# ─── Phase 1: LIST ──────────────────────────────────────────────────────────

def phase_list(page):
    """Scrape all conversations from Otter home → manifest JSON.
    
    If a manifest already exists, this just reports its stats.
    Re-scraping can be triggered with --rescan.
    """
    print("\n=== Phase 1: Listing conversations ===")
    if MANIFEST_PATH.exists():
        manifest = json.loads(MANIFEST_PATH.read_text())
        total = len(manifest)
        exported = sum(1 for c in manifest if c.get("exported"))
        print(f"Manifest already exists: {total} conversations ({exported} exported)")
        print(f"Date range: {manifest[-1].get('date','?')} → {manifest[0].get('date','?')}")
        return manifest
    
    print("No manifest found. Run the browser-based scraper or create manually.")
    return []


# ─── Phase 2: EXPORT ─────────────────────────────────────────────────────────

def phase_export(page, ids=None):
    """Export transcript+summary for each conversation via Otter's export button."""
    print("\n=== Phase 2: Exporting transcripts ===")
    ensure_signed_in(page)

    manifest = json.loads(MANIFEST_PATH.read_text())
    to_export = [c for c in manifest if not c.get("exported")]
    if ids:
        id_set = set(ids)
        to_export = [c for c in to_export if c["otter_id"] in id_set]

    print(f"{len(to_export)} conversations to export")

    for i, conv in enumerate(to_export, 1):
        otter_id = conv["otter_id"]
        date_str = conv.get("date", "unknown")
        print(f"\n[{i}/{len(to_export)}] {date_str} ({conv.get('duration','')})...")

        safe_id = re.sub(r'[^a-zA-Z0-9_-]', '_', otter_id)
        raw_dir = LECTURES_DIR / f"_staging/{safe_id}/raw"
        raw_dir.mkdir(parents=True, exist_ok=True)

        try:
            page.goto(conv["otter_url"], wait_until="domcontentloaded", timeout=60_000)
            time.sleep(5)

            # Look for the three-dot / more-options button
            more_btn = (
                page.locator('[aria-label="More options"]').first
                or page.locator('button:has-text("⋯")').first
                or page.locator('[data-testid="more-options"]').first
            )
            more_btn.click(timeout=10_000)
            time.sleep(1)

            # Click Export in the dropdown
            page.locator('text="Export"').first.click(timeout=5_000)
            time.sleep(2)

            # The export dialog may have format options; look for a download trigger
            with page.expect_download(timeout=30_000) as download_info:
                # Try clicking the prominent export/download button
                for selector in [
                    'button:has-text("Export")',
                    'button:has-text("Download")',
                    '[data-testid="export-button"]',
                ]:
                    try:
                        page.locator(selector).last.click(timeout=3_000)
                        break
                    except Exception:
                        continue

            download = download_info.value
            dest = raw_dir / download.suggested_filename
            download.save_as(str(dest))

            # Extract ZIP if needed
            if dest.suffix == ".zip":
                with zipfile.ZipFile(str(dest), "r") as zf:
                    zf.extractall(str(raw_dir))
                dest.unlink()

            # Rename files to include date
            date_tag = conv.get("date", "").replace("-", "")
            for f in raw_dir.iterdir():
                if f.is_file() and date_tag and date_tag not in f.name:
                    new_name = f"{f.stem} {conv.get('date', '')}{f.suffix}"
                    f.rename(raw_dir / new_name)

            conv["exported"] = True
            conv["status"] = "exported"
            print(f"  ✓ Exported to {raw_dir}")

        except Exception as e:
            print(f"  ✗ Failed: {e}")
            conv["status"] = f"export_error: {str(e)[:80]}"

        # Save manifest after each conversation
        MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
        time.sleep(2)


# ─── Phase 3: SLIDES ─────────────────────────────────────────────────────────

def phase_slides(page, ids=None):
    """Download meeting screenshots for each conversation."""
    print("\n=== Phase 3: Downloading screenshots ===")
    ensure_signed_in(page)

    manifest = json.loads(MANIFEST_PATH.read_text())
    to_download = [c for c in manifest if c["exported"] and not c["slides_downloaded"]]
    if ids:
        id_set = set(ids)
        to_download = [c for c in to_download if c["otter_id"] in id_set]

    print(f"{len(to_download)} conversations to download slides for")

    for i, conv in enumerate(to_download, 1):
        otter_id = conv["otter_id"]
        title = conv["title"][:60]
        date_str = conv.get("date", "")
        print(f"\n[{i}/{len(to_download)}] {date_str} {title}...")

        try:
            page.goto(conv["otter_url"], wait_until="domcontentloaded", timeout=60_000)
            time.sleep(3)

            # Click Transcript tab to load full content
            try:
                page.locator('text="Transcript"').first.click()
                time.sleep(5)
            except Exception:
                time.sleep(3)

            # Scroll to load content
            for _ in range(20):
                page.evaluate(
                    "document.querySelector('.clean-conversation-canvas')"
                    "?.scrollBy(0, 3000) || window.scrollBy(0, 3000)"
                )
                time.sleep(0.5)
            time.sleep(2)

            # Extract screenshot URLs
            html = page.content()
            raw_paths = re.findall(r'forward/image/[^"\'<>\s]+snapshot\.jpeg', html)
            unique_paths = list(dict.fromkeys(raw_paths))

            def sort_key(p):
                m = re.search(r'/(\d+)_\d+_SHARED', p)
                return int(m.group(1)) if m else 0

            unique_paths.sort(key=sort_key)
            urls = [f"https://otter.ai/{p}" for p in unique_paths]

            if not urls:
                print(f"  No screenshots found")
                conv["slides_downloaded"] = True
                conv["screenshot_count"] = 0
                packet_rel = conv.get("packet_dir")
                if packet_rel:
                    packet_path = REPO_ROOT / packet_rel / "packet.json"
                    if packet_path.exists():
                        packet = json.loads(packet_path.read_text())
                        packet.setdefault("slides", {})
                        packet["slides"]["status"] = "none"
                        packet["slides"]["screenshot_count"] = 0
                        if "otter" in packet:
                            packet["otter"]["screenshots"] = 0
                        packet_path.write_text(json.dumps(packet, indent=2) + "\n")
                MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
                continue

            # Download into the packet slides dir when a packet exists
            safe_id = re.sub(r'[^a-zA-Z0-9_-]', '_', otter_id)
            packet_rel = conv.get("packet_dir")
            if packet_rel:
                slides_dir = REPO_ROOT / packet_rel / "slides"
            else:
                slides_dir = LECTURES_DIR / f"_staging/{safe_id}/slides"
            slides_dir.mkdir(parents=True, exist_ok=True)

            date_tag = conv.get("date", "unknown")
            downloaded = 0
            for j, url in enumerate(urls, 1):
                fname = f"slide-{date_tag}-{j:03d}.jpeg"
                fpath = slides_dir / fname
                if fpath.exists():
                    downloaded += 1
                    continue
                try:
                    resp = page.request.get(url)
                    if resp.ok:
                        fpath.write_bytes(resp.body())
                        downloaded += 1
                except Exception:
                    pass

            conv["slides_downloaded"] = True
            conv["screenshot_count"] = downloaded
            # Keep packet.json in sync
            if packet_rel:
                packet_path = REPO_ROOT / packet_rel / "packet.json"
                if packet_path.exists():
                    packet = json.loads(packet_path.read_text())
                    packet.setdefault("slides", {})
                    packet["slides"]["status"] = "downloaded" if downloaded else "none"
                    packet["slides"]["screenshot_count"] = downloaded
                    packet["slides"]["filename_pattern"] = f"slide-{date_tag}-{{NNN}}.jpeg"
                    if "otter" in packet:
                        packet["otter"]["screenshots"] = downloaded
                    packet_path.write_text(json.dumps(packet, indent=2) + "\n")
            print(f"  ✓ {downloaded}/{len(urls)} screenshots → {slides_dir}")

        except Exception as e:
            print(f"  ✗ Failed: {e}")

        MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
        time.sleep(1)


# ─── Phase 4: PACKET ─────────────────────────────────────────────────────────

def phase_packet(ids=None):
    """Create lecture-packet folder structure + packet.json for each exported conversation."""
    print("\n=== Phase 4: Creating lecture packets ===")

    manifest = json.loads(MANIFEST_PATH.read_text())
    to_packet = [c for c in manifest if c["exported"] and not c.get("packet_created")]
    if ids:
        id_set = set(ids)
        to_packet = [c for c in to_packet if c["otter_id"] in id_set]

    print(f"{len(to_packet)} packets to create")

    for i, conv in enumerate(to_packet, 1):
        otter_id = conv["otter_id"]
        safe_id = re.sub(r'[^a-zA-Z0-9_-]', '_', otter_id)
        staging = LECTURES_DIR / f"_staging/{safe_id}"
        title = conv["title"][:80]
        print(f"\n[{i}/{len(to_packet)}] {title}...")

        date_str = conv.get("date") or conv.get("approx_date") or otter_id[:12]
        slug = f"clearfield-webinar-{date_str}"
        packet_dir = LECTURES_DIR / slug

        if packet_dir.exists():
            print(f"  Packet dir already exists: {packet_dir.name}")
            conv["packet_created"] = True
            conv["packet_dir"] = str(packet_dir.relative_to(REPO_ROOT))
            MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
            continue

        packet_dir.mkdir(parents=True, exist_ok=True)
        (packet_dir / "raw").mkdir(exist_ok=True)
        (packet_dir / "slides").mkdir(exist_ok=True)
        (packet_dir / "derived").mkdir(exist_ok=True)

        # Move raw files from staging
        if (staging / "raw").exists():
            for f in (staging / "raw").iterdir():
                f.rename(packet_dir / "raw" / f.name)

        # Move slides from staging
        if (staging / "slides").exists():
            for f in (staging / "slides").iterdir():
                f.rename(packet_dir / "slides" / f.name)

        # Find transcript and summary files
        raw_files = list((packet_dir / "raw").iterdir())
        transcript = next((f.name for f in raw_files if "transcript" in f.name.lower()), None)
        summary = next((f.name for f in raw_files if "summary" in f.name.lower()), None)
        slide_count = len(list((packet_dir / "slides").glob("*.jpeg")))

        # Create packet.json
        packet = {
            "id": slug,
            "title": conv["title"],
            "approx_date": conv.get("date") or conv.get("approx_date"),
            "duration": conv.get("duration"),
            "channel": conv.get("channel", "Clearfield Training Program"),
            "otter_url": conv["otter_url"],
            "otter_id": otter_id,
            "primary_branch": "integrative-medicine",
            "gem_status": "raw",
            "paths": {
                "packet": str(packet_dir.relative_to(REPO_ROOT)) + "/",
                "raw": str((packet_dir / "raw").relative_to(REPO_ROOT)) + "/",
                "slides": str((packet_dir / "slides").relative_to(REPO_ROOT)) + "/",
                "derived": str((packet_dir / "derived").relative_to(REPO_ROOT)) + "/",
            },
            "otter": {
                "transcript": f"{packet_dir.relative_to(REPO_ROOT)}/raw/{transcript}" if transcript else None,
                "summary": f"{packet_dir.relative_to(REPO_ROOT)}/raw/{summary}" if summary else None,
                "screenshots": slide_count,
                "audio": None,
            },
            "slides": {
                "status": "downloaded" if slide_count > 0 else "none",
                "screenshot_count": slide_count,
            },
            "derived": {
                "gem_cleanup": False,
                "study_guide": False,
                "teach_outline": False,
            },
        }
        (packet_dir / "packet.json").write_text(json.dumps(packet, indent=2))

        conv["packet_created"] = True
        conv["packet_dir"] = str(packet_dir.relative_to(REPO_ROOT))
        print(f"  ✓ Created {packet_dir.name}")

        MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))

    # Cleanup empty staging dirs
    staging_root = LECTURES_DIR / "_staging"
    if staging_root.exists():
        for d in staging_root.iterdir():
            if d.is_dir() and not any(d.rglob("*")):
                d.rmdir()


# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Otter.ai Batch Pipeline")
    parser.add_argument("phase", choices=["list", "export", "slides", "packet", "all"],
                        help="Pipeline phase to run")
    parser.add_argument("--ids", help="Comma-separated Otter IDs to process (default: all pending)")
    args = parser.parse_args()

    ids = args.ids.split(",") if args.ids else None

    if args.phase == "packet":
        phase_packet(ids)
    else:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = get_browser(p)
            page = browser.new_page()
            try:
                if args.phase in ("list", "all"):
                    phase_list(page)
                if args.phase in ("export", "all"):
                    phase_export(page, ids)
                if args.phase in ("slides", "all"):
                    phase_slides(page, ids)
                if args.phase == "all":
                    phase_packet(ids)
            finally:
                browser.close()

    print("\n=== Pipeline complete ===")
    if MANIFEST_PATH.exists():
        manifest = json.loads(MANIFEST_PATH.read_text())
        total = len(manifest)
        exported = sum(1 for c in manifest if c.get("exported"))
        slides = sum(1 for c in manifest if c.get("slides_downloaded"))
        packets = sum(1 for c in manifest if c.get("packet_created"))
        print(f"  Total: {total} | Exported: {exported} | Slides: {slides} | Packets: {packets}")


if __name__ == "__main__":
    main()
