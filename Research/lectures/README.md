# Lecture packets

One folder per lecture. **Catalog and extract first; keep large decks/audio on disk or external volumes until selective import.**

## Layout

```text
Research/lectures/<id>/
  packet.json     # manifest (branch, otter, slides, gem_status)
  raw/            # Otter transcript + audio (optional)
  slides/         # extracts, protocol images; PPTX may stay external
  derived/        # Gem cleanup, study/teach drafts
```

## Status fields (`packet.json`)

| Field | Values |
|--------|--------|
| `sync` | `matched` · `slides_only` · `transcript_only` · `screenshots_only` · `missing` |
| `gem_status` | `raw` · `cleaned` · `teach_ready` |
| `primary_branch` | Living Tree branch (`immune`, `nutrition`, …) |

## Packets

| ID | Branch | Sync | Notes |
|----|--------|------|-------|
| [mccullough-covid-early-tx-aosrd-2022](mccullough-covid-early-tx-aosrd-2022/) | immune | slides_only | AOSRD Sat #8 — 71 slides extracted |
| [dpc-hartman-2026-05](dpc-hartman-2026-05/) | integrative-medicine | screenshots_only (20) | Otter + slide screenshots |
| [dna-repair-andrews-2026-04](dna-repair-andrews-2026-04/) | integrative-medicine | screenshots_only (90) | Otter + slide screenshots |
| [ivermectin-ayurveda-2026-05](ivermectin-ayurveda-2026-05/) | integrative-medicine | screenshots_only (99) | Otter + slide screenshots |


## Otter batch inventory

98 Clearfield Tuesday webinars listed in [data/otter-manifest.json](data/otter-manifest.json) (2024-08-06 → 2026-06-30, dates from Otter summaries). Series reportedly starts 2022-01-11; older Otter conversations not yet ingested. One fully processed: [clearfield-webinar-2026-06-30](clearfield-webinar-2026-06-30/).

Pipeline: `scripts/otter_batch_pipeline.py` (`list` · `export` · `slides` · `packet`).

## Related

- [BRANCH-TAXONOMY.md](../BRANCH-TAXONOMY.md)
- [integrative-medicine/aosrd-2022/](../integrative-medicine/aosrd-2022/)
- [integrative-medicine/local-downloads/](../integrative-medicine/local-downloads/) — Otter-style local packs (colchicine, etc.)
