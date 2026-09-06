#!/usr/bin/env python3
"""
Download all meeting screenshots from an Otter.ai conversation page.

Usage:
  python3 download_otter_screenshots.py <otter_url> <output_dir> [--prefix PREFIX]

The script opens a visible browser window so you can sign in to Otter,
then navigates to the conversation, extracts all screenshot image URLs
from the HTML, and downloads each one by intercepting network responses.

Requirements:
  pip3 install playwright
  python3 -m playwright install chromium
"""
import argparse
import re
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser(description="Download Otter.ai meeting screenshots")
    parser.add_argument("url", help="Otter conversation URL")
    parser.add_argument("output_dir", help="Directory to save screenshots")
    parser.add_argument("--prefix", default="slide", help="Filename prefix (default: slide)")
    args = parser.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    user_data = Path.home() / ".otter-playwright-profile"

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            str(user_data),
            headless=False,
            viewport={"width": 1280, "height": 900},
        )
        page = browser.new_page()

        # Step 1: Check if signed in
        print("Checking Otter sign-in status...")
        page.goto("https://otter.ai/home", wait_until="domcontentloaded", timeout=60_000)
        time.sleep(3)

        if "signin" in page.url or "login" in page.url or "meet-otter" in page.url:
            print("\n=== Sign in to Otter.ai in the browser window ===")
            print("Waiting for you to sign in (watching for home page)...")
            page.wait_for_url("**/home**", timeout=300_000)
            print("Sign-in detected! Continuing...")

        # Step 2: Navigate to conversation
        print(f"Navigating to {args.url} ...")
        page.goto(args.url, wait_until="domcontentloaded", timeout=60_000)
        time.sleep(3)

        # Wait for page to fully render as SPA
        print("Waiting for page to render...")
        time.sleep(5)

        # Click Transcript tab to load transcript content
        try:
            tab = page.locator('text="Transcript"').first
            tab.click()
            print("Clicked Transcript tab")
            time.sleep(5)
        except Exception as e:
            print(f"Could not click Transcript tab: {e}")

        # Scroll down to trigger lazy loading
        print("Scrolling to load content...")
        for _ in range(20):
            page.evaluate("document.querySelector('.clean-conversation-canvas')?.scrollBy(0, 3000) || window.scrollBy(0, 3000)")
            time.sleep(0.5)
        time.sleep(3)

        # Now wait for screenshot images
        print("Checking for screenshot images...")
        try:
            page.wait_for_selector('img[alt="Meeting screenshot"]', timeout=10_000)
            print("Screenshots detected in DOM")
        except Exception:
            print("No screenshot images found in DOM after waiting")

        # Debug: check what we got
        print(f"Current URL: {page.url}")
        print(f"Page title: {page.title()}")

        # Step 3: Extract all screenshot URLs from HTML
        html = page.content()
        print(f"HTML length: {len(html)}")
        # Check for key indicators
        if "snapshot.jpeg" in html:
            print("Found snapshot.jpeg references in HTML")
        else:
            print("NO snapshot.jpeg found in HTML")
            # Dump a snippet for debugging
            for marker in ["screenshot", "Meeting", "forward/image"]:
                if marker in html:
                    idx = html.index(marker)
                    print(f"  Found '{marker}' at pos {idx}: ...{html[max(0,idx-30):idx+60]}...")
                    break
            else:
                print("  No screenshot-related content found in page HTML")
        raw_paths = re.findall(r'forward/image/[^"\'<>\s]+snapshot\.jpeg', html)
        unique_paths = list(dict.fromkeys(raw_paths))  # dedupe, preserve order

        # Sort by timestamp embedded in filename
        def sort_key(p):
            m = re.search(r'/(\d+)_\d+_SHARED', p)
            return int(m.group(1)) if m else 0

        unique_paths.sort(key=sort_key)
        urls = [f"https://otter.ai/{p}" for p in unique_paths]
        print(f"Found {len(urls)} screenshot URLs")

        if not urls:
            print("No screenshots found. Make sure the page loaded fully.")
            browser.close()
            return


        # Step 4: Download each image using the authenticated browser context
        downloaded = 0
        for i, url in enumerate(urls, 1):
            fname = f"{args.prefix}-{i:03d}.jpeg"
            fpath = out / fname
            if fpath.exists():
                print(f"  [{i}/{len(urls)}] {fname} already exists, skipping")
                downloaded += 1
                continue

            try:
                resp = page.request.get(url)
                if resp.ok:
                    fpath.write_bytes(resp.body())
                    size_kb = len(resp.body()) / 1024
                    print(f"  [{i}/{len(urls)}] {fname}  ({size_kb:.0f} KB)")
                    downloaded += 1
                else:
                    print(f"  [{i}/{len(urls)}] {fname}  FAILED (HTTP {resp.status})")
            except Exception as e:
                print(f"  [{i}/{len(urls)}] {fname}  ERROR: {e}")

        browser.close()
        print(f"\nDone! Downloaded {downloaded}/{len(urls)} screenshots to {out}")


if __name__ == "__main__":
    main()
