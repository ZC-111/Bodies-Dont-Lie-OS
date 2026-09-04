# Acupuncture Pipeline — Usage

How to run and verify the extraction pipeline in [scripts/](scripts/): turn the Deadman PDF into an enriched acupuncture-point dataset, then confirm the result.

## Environment

Python 3.12 with `pypdf` — declared in [../../requirements.txt](../../requirements.txt) and installed by the repo's `install` step ([../../.cursor/environment.json](../../.cursor/environment.json)). No other setup.

## Run

From the repository root:

```bash
# 1. Extract points from the Deadman PDF (~6s) → JSON extract
python3 Research/acupuncture/scripts/deadman_extract.py \
  Research/acupuncture/sources/pdfs/A-manual-of-acupuncture-peter-deadman.pdf \
  Research/acupuncture/data/deadman-extract-v0.2.json

# 2. Apply gap-fill + comparative (i18n) enrichments to an extract
python3 Research/acupuncture/scripts/apply_deadman_enrichments.py \
  Research/acupuncture/data/deadman-extract-v0.2.json
```

Both scripts default their input/output paths to [data/](data/), so they also run with no arguments. Enrichment resolves its data files (`deadman-gap-fill.json`, `acupuncture-comparative-database.json`) relative to the **output** file's directory — keep outputs inside `data/`.

## Verify

A healthy `deadman_extract.py` run reports:

| Field | Expected |
|-------|----------|
| total_extracted | 396 (361 classical + 35 extraordinary) |
| gap_filled_count | 16 |
| comparative_enriched_count | 320 |
| missing_from_index | `[]` (empty) |

Running `apply_deadman_enrichments.py` on an already-enriched extract reports 0 new gap-fills (already present) and 320 comparative records. To check without touching committed data, write to a temp path inside `data/` (e.g. `data/tmp-verify.json`) and delete it afterward.

## Related

- [README.md](README.md) — Acupuncture research index
- [scripts/](scripts/) — Pipeline source
- [../../Constitution/Wayfinding/07-Validate.md](../../Constitution/Wayfinding/07-Validate.md) — Why we confirm results (Wayfinding · Validate)
