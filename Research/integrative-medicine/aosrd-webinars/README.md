# AOSRD Webinars — Hybrid Lecture Processor

Scrape [aosrd.org/webinars](https://aosrd.org/webinars/), pair videos with PDFs, optionally transcribe (faster-whisper) and emit lean Markdown study guides for Cursor.

**Sibling:** [../aosrd-2022/](../aosrd-2022/) is the 2022 Congress *drive catalog*. This folder is the **ongoing webinars site** pipeline.

## Status

Script + docs only. Heavy outputs (video, frames, whisper caches) stay gitignored under `study-guide/`.

## Install (optional — not the default cloud `requirements.txt`)

Needs system `ffmpeg` + Poppler if converting PDFs:

```bash
pip3 install -r Research/integrative-medicine/aosrd-webinars/requirements-aosrd-hybrid.txt
# macOS: brew install ffmpeg poppler
# Debian: apt install ffmpeg poppler-utils
```

Defaults to **CPU** Whisper. For GPU:

```bash
export AOSRD_WHISPER_DEVICE=cuda
export AOSRD_WHISPER_MODEL=medium   # or turbo / large-v3
```

## Usage

```bash
# Catalog only (network)
python3 Research/integrative-medicine/aosrd-webinars/scripts/aosrd_hybrid_processor.py --list

# One lecture (download + whisper + frames) — heavy; needs yt-dlp access
python3 Research/integrative-medicine/aosrd-webinars/scripts/aosrd_hybrid_processor.py --process 0

# Force scene detection instead of PDF pages
python3 Research/integrative-medicine/aosrd-webinars/scripts/aosrd_hybrid_processor.py --process 12 --force-scene

# Cloud / bot-blocked YouTube: use a local file + optional transcript
python3 Research/integrative-medicine/aosrd-webinars/scripts/aosrd_hybrid_processor.py \
  --process 68 --local-video /path/to/file.mp4 --skip-transcribe
```

**Note:** Cursor Cloud VMs often get YouTube/Vimeo “sign in / bot” blocks. PDFs from `aosrd.org` still download. Use `--local-video` / `--local-transcript` / `--skip-transcribe` when video extractors fail.

## Pilot run (2026-09-09)

Processed catalog **#68** — *The Laboratory Functional Medicine* (Clearfield) — PDF pages → frames + `visual-transcript.md` (Whisper skipped; YouTube blocked). Frames/PDF stay gitignored; markdown + meta are tracked.
## Output layout

```text
Research/integrative-medicine/aosrd-webinars/
  scripts/aosrd_hybrid_processor.py
  requirements-aosrd-hybrid.txt
  study-guide/
    catalog.json
    <safe_title>/
      video.*
      slides.pdf          # when matched
      frames/*.jpg
      visual-transcript.md
      meta.json
```

Markdown header shape:

```markdown
# Title
**Lecturer · Date**

Source: …
```

## Living Tree notes

- Tag processed lectures into `immune` / `nutrition` / etc. via packet promotion later — do not dump binaries into Knowledge.
- Prefer promoting evergreen claims to Knowledge leaves after MedNote-style cleanup.
- This tool is **separate** from the acupuncture pipeline ([AGENTS.md](../../../AGENTS.md)).

## Related

- [../aosrd-2022/](../aosrd-2022/)
- [../../lectures/](../../lectures/) — Clearfield Otter packet pattern
- [../../BRANCH-TAXONOMY.md](../../BRANCH-TAXONOMY.md)
