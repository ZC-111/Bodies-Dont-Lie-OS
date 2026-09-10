# BDS Library Audit — Pass 2: Existing Representation Inventory

## Purpose

This pass inventories **existing local representations** of the AOSRD / Clearfield ecosystem before any additional acquisition or processing.

Governing principle: do not create a new representation until we know an equivalent usable representation does not already exist.

This is an audit pass only. No media was downloaded or processed. Pass 1 title matches remain candidate relationships, not confirmed identity.

## Scope

Inspected (local repository only; no network fetches):

| Path | Role |
|---|---|
| `Research/lectures/clearfield-webinar-*` | 98 Clearfield/Otter packets (filesystem + `packet.json`) |
| `Research/lectures/data/otter-manifest.json` | Otter export manifest (98) |
| `Research/integrative-medicine/aosrd-webinars/study-guide/catalog.json` | Ongoing webinars catalog (284) |
| `Research/integrative-medicine/aosrd-webinars/study-guide/` | Local study-guide lecture artifacts |
| `Research/integrative-medicine/aosrd-2022/data/aosrd-catalog.json` | 2022 conference catalog |
| `Research/integrative-medicine/local-downloads/data/local-downloads-catalog.json` | Local Downloads catalog |
| `Research/lectures/audit/title-reconciliation-pass-1.csv` | Pass 1 crosswalk (join only; not revised) |
| `Research/lectures/audit/title-reconciliation-pass-1.md` | Pass 1 report (context) |
| `.gitignore` | Evidence that Otter slide JPEGs are intentionally not tracked |

Workspace inspected: `/workspace` (Bodies-Dont-Lie-OS cloud checkout). Mac path `/Users/nuu/Projects/Bodies-Dont-Lie-OS` was not available as a separate mount; inventory reflects this checkout.

**Not in scope for row generation:** other non-Clearfield lecture packets under `Research/lectures/` (e.g. `dna-repair-*`, `dpc-hartman-*`) — noted only as adjacent materials.

## Counts

| Metric | Count |
|---|---:|
| Inventory rows (CSV) | 430 |
| Clearfield/Otter packets found | 98 |
| AOSRD webinars catalog records | 284 |
| AOSRD 2022 lecture records | 29 |
| Local-download catalog records | 19 |
| Records with local transcripts | 98 |
| Records with local MedNote structured notes | 98 |
| Records with local slide PDFs | 1 |
| Records with locally present slide images | 1 |
| Records where slides are claimed elsewhere | 132 |
| Records with local video | 0 |
| Records with local audio | 0 |
| Records with pathways | 3 |
| Records with content kits | 3 |
| Records with Knowledge leaf references (files exist) | 1 |

Otter-specific slide claim split (from `packet.json`, not blanket manifest):

| Otter slide state | Count |
|---|---:|
| `slides_claimed_downloaded=true` / `slides_status=claimed_present_elsewhere` | 86 |
| `slides_status=absent` (packet says none/0) | 12 |
| `slide_images_status=present_local` | 0 |

## Representation State Summary

Counts across **all 430 inventory rows** for major representation columns:

| Category | present_local | cataloged_external | claimed_present_elsewhere | absent | not_checked |
|---|---:|---:|---:|---:|---:|
| Raw transcript | 98 | 0 | 0 | 332 | 0 |
| Summary | 98 | 0 | 0 | 332 | 0 |
| Structured lecture notes | 98 | 0 | 0 | 332 | 0 |
| Quiz | 98 | 0 | 0 | 332 | 0 |
| Key takeaways | 98 | 0 | 0 | 332 | 0 |
| Infographic data | 98 | 0 | 0 | 332 | 0 |
| Rendered infographic | 0 | 0 | 0 | 430 | 0 |
| Derived README | 98 | 0 | 0 | 332 | 0 |
| Slides (aggregate) | 1 | 0 | 132 | 297 | 0 |
| Slide images | 1 | 0 | 93 | 336 | 0 |
| Slide PDF | 1 | 0 | 46 | 383 | 0 |
| Audio | 0 | 0 | 8 | 422 | 0 |
| Video | 0 | 0 | 4 | 426 | 0 |
| Pathway | 3 | 0 | 0 | 427 | 0 |
| Content kit | 3 | 0 | 0 | 427 | 0 |
| Knowledge leaves | 1 | 0 | 0 | 429 | 0 |
| AOSRD catalog record | 332 | 90 | 0 | 8 | 0 |
| AOSRD PDF URL | 0 | 127 | 0 | 261 | 42 |
| AOSRD PDF local | 1 | 0 | 22 | 407 | 0 |
| YouTube URL | 0 | 275 | 0 | 57 | 98 |
| YouTube video local | 0 | 0 | 0 | 430 | 0 |
| Vimeo URL | 0 | 8 | 0 | 324 | 98 |
| Rumble URL | 0 | 1 | 0 | 331 | 98 |

## Clearfield/Otter Summary

- **98** packets on disk under `Research/lectures/clearfield-webinar-*`.
- **All 98** have: `packet.json`, raw Otter transcript, raw summary, and full MedNote derived set (`structured-lecture-notes.md`, `quiz.md`, `key-takeaways.md`, `infographic-data.md`, `README.md`).
- **Pathways / content kits:** 3 packets (`2024-08-13`, `2025-03-11`, `2026-06-30`).
- **Knowledge leaves:** 1 packet (`2025-03-11`) with 4 nutrition leaf references; leaf files exist under `Knowledge/nutrition/`.
- **Audio / video:** none present locally in these packets.
- **Rendered infographics:** none found inside packets (infographic *data* markdown is present for all 98).

### Screenshot discrepancy (confirmed)

| Evidence | Observation |
|---|---|
| `packet.json` `slides.status=downloaded` + `screenshot_count>0` | **86** sessions |
| Local `slides/*.jpeg` / `*.png` on this disk | **0** files |
| `slides/` directory present | 1 packet (`2026-06-30`) with README only |
| `.gitignore` | `Research/lectures/*/slides/*.jpeg` — binaries stay local / untracked |
| `otter-manifest.json` `slides_downloaded` | **True for all 98** (conflicts with 12 packets whose `packet.json` says `status=none`, count 0) |

Classification used:

- 86 → `claimed_present_elsewhere` (not “missing”)
- 12 → `absent` per authoritative `packet.json`; notes flag stale blanket manifest values

## AOSRD Summary

Ongoing webinars (`catalog.json`):

| Item | Count |
|---|---:|
| Catalog records | 284 |
| YouTube URL cataloged | 275 |
| Vimeo URL cataloged | 8 |
| Rumble URL cataloged | 1 |
| AOSRD PDF URL cataloged | 71 |
| PDF present locally | 1 |
| Slide/frame images present locally | 1 |
| Spoken transcript present locally | 0 |
| Video present locally | 0 |

**Locally present AOSRD webinar body (1):** catalog record `aosrd-webinars-068-vS6aw3GkcRI` — *Laboratory Functional Medicine* (Clearfield) study-guide folder with `slides.pdf`, 30 PDF frame JPEGs, `meta.json`, and `visual-transcript.md` (frame index only; **not** a spoken transcript).

All other webinar rows are **cataloged_external** / **source_only** (URLs in catalog; no local media).

## Older / 2022 Summary

| Item | Count |
|---|---:|
| 2022 lecture catalog records | 29 |
| Files indexed in catalog | 37 (per catalog summary) |
| Source paths resolvable on this machine | 0 |
| Classification | `claimed_present_elsewhere` / `source_only` |

Catalog `source_path` values point at a Mac volume (e.g. `/Volumes/Macintosh HD - Data/Users/.../AOSRd Slide Show 2022/...`). Those binaries are **not** present in this checkout. No retrieval attempted.

## Local Downloads Summary

| Item | Count |
|---|---:|
| Catalog packs | 19 |
| Referenced document paths on this machine | 0 |
| Classification | `claimed_present_elsewhere` / `source_only` |

Catalog meta records source as `/Users/nuu/Downloads` (cataloged 2026-09-03). Paths are inventory references to another machine, not assets in this repo.

## Processing Readiness

Factual classification from local representations only (not a processing plan or priority queue):

| `processing_state_based_on_local_inventory` | Count | Meaning in this inventory |
|---|---:|---|
| `text_complete` | 12 | Otter packets with full text/MedNote and no slide claim |
| `text_plus_visual_claimed_elsewhere` | 86 | Otter text complete; screenshots claimed elsewhere |
| `visual_present_local` | 1 | Local PDF/frames (AOSRD pilot) |
| `source_only` | 331 | Catalog/URL/external-path only |
| `partial_representation` | 0 | — |
| `no_local_representation` | 0 | — |

## Important Discrepancies

1. **Otter screenshots vs this disk:** 86 packets claim downloaded screenshots; **0** JPEG/PNG files present here; gitignore excludes them.
2. **Manifest vs packet.json:** `otter-manifest.json` sets `slides_downloaded=true` for all 98; **12** packets explicitly have `slides.status=none` / count 0. Inventory trusts `packet.json` for those 12 and notes the conflict.
3. **AOSRD PDF URLs vs local PDFs:** 71 PDF URLs cataloged; **1** PDF present locally (pilot).
4. **Stale external paths:** aosrd-2022 `/Volumes/...` and local-downloads `/Users/nuu/Downloads/...` — cataloged, not on this machine.
5. **Pass 1 join:** webinar/2022/local-download record IDs reused from Pass 1 where matched; Otter rows list Pass 1 web candidates with match class **without** confirming identity.
6. **visual-transcript ≠ transcript:** pilot `visual-transcript.md` is a PDF frame listing only.
7. **Study-guide `.gitignore`:** ignores most binaries under `study-guide/` except `catalog.json`, `meta.json`, `visual-transcript.md`; pilot PDF/frames are present on this disk regardless.

## STOP CONDITION

```
PASS 2 COMPLETE.
NO MEDIA DOWNLOADED.
NO MEDIA PROCESSED.
NO SOURCE PACKETS MODIFIED.
NO EXISTING ARTIFACTS REGENERATED.
```

## Outputs

- `Research/lectures/audit/local-representation-inventory-pass-2.csv` (430 data rows)
- `Research/lectures/audit/local-representation-inventory-pass-2.md` (this file)
