# AGENTS.md

## Overview

**Bodies Don't Lie OS** is primarily a markdown/knowledge base (Constitution, Knowledge, Projects, Research, etc.). Most changes are documentation and do not require running anything.

The only executable component is the **acupuncture research pipeline** in `Research/acupuncture/scripts/`, which parses the Deadman *A Manual of Acupuncture* PDF and enriches the result with gap-fill and comparative (multilingual) data.

## Environment

- Python 3.12 on the default base image.
- Dependencies are declared in `requirements.txt` (`pypdf`) and installed by the `install` step in `.cursor/environment.json` (`pip3 install -r requirements.txt`). No extra setup is required.

## Running the pipeline

From the repository root:

```bash
# 1. Extract points from the Deadman PDF (~6s). Writes a JSON extract.
python3 Research/acupuncture/scripts/deadman_extract.py \
  Research/acupuncture/sources/pdfs/A-manual-of-acupuncture-peter-deadman.pdf \
  Research/acupuncture/data/deadman-extract-v0.2.json

# 2. Apply gap-fill + comparative (i18n) enrichments to an existing extract.
python3 Research/acupuncture/scripts/apply_deadman_enrichments.py \
  Research/acupuncture/data/deadman-extract-v0.2.json
```

Both scripts default their input/output paths to `Research/acupuncture/data/`, so they can also be run with no arguments. Gap-fill and comparative enrichment resolve their data files (`deadman-gap-fill.json`, `acupuncture-comparative-database.json`) relative to the **output** file's directory, so keep the output inside `Research/acupuncture/data/`.

## Verifying a change

A healthy run of `deadman_extract.py` reports `total_extracted: 396` (361 classical + 35 extraordinary), `gap_filled_count: 16`, `comparative_enriched_count: 320`, and empty `missing_from_index`. Running `apply_deadman_enrichments.py` on an already-enriched extract reports 0 new gap-fills (they are already present) and 320 comparative i18n records. To verify without touching committed data, write outputs to a temp path inside the data dir (e.g. `Research/acupuncture/data/tmp-verify.json`) and delete them afterward.

## Cursor Cloud specific instructions

- Documentation-only changes (markdown under `Constitution/`, `Knowledge/`, `Projects/`, `Reflection/`, `Templates/`, `Archive/`, and READMEs) do not need to be run or tested; a proofread is sufficient.
- Changes to the pipeline scripts (`Research/acupuncture/scripts/*.py`) or their input data **must** be validated by running the two commands above and confirming the expected counts (396 extracted; 16 gap-filled; 320 enriched).
- There is no web UI; verify pipeline changes with terminal output/logs rather than the `computerUse` subagent.
