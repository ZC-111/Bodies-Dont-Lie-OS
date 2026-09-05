# Lung Channel — Validation

| Field | Value |
|-------|-------|
| Stage | Wayfinding · [Validate](../../Constitution/Wayfinding/07-Validate.md) |
| Date | 2026-09-04 (revised after extractor fix) |
| Inputs | [deadman-extract-v0.2.json](data/deadman-extract-v0.2.json) (v0.2.1), Deadman source pp. 76–91, [comparison-v0.1.json](data/comparison-v0.1.json) |
| Question | Which Lung-channel points (LU-1…LU-11) are confirmed enough to graduate into `Knowledge/` leaves? |

## Why this note was revised

- **Pass 1** graduated 5 points from extract fields alone.
- **Pass 2** found the extractor's `propagate_cluster_fields` step was **copying clinical text between points** that merely reference each other as anatomical landmarks — LU-6 Kongzui and LU-9 Taiyuan had both been given **LU-8 Jingqu's** indications, and LU-1's fields were propagated and wrong. Fixed (extract v0.2.1); clinical sections are no longer propagated.
- **Pass 3** added a **column-aware page reader** (`deadman_extract.py --page N`) that reconstructs the two-column layout in true reading order. This resolved the remaining points and caught a further error: LU-5 Chize's indications had begun with **LU-4 Xiabai's** text (the two adjacent points' indication lists abut in the OCR). All 11 points are now read directly from the column-aware source.

See [Reflection/2026-09-04.md](../../Reflection/2026-09-04.md).

## Gate

A point is **confirmed** when:

1. Present in **both** sources — Deadman + Bencaodian.
2. Its `location`, `actions`, and `indications` are read **directly from the column-aware Deadman source pages** (not from cross-point propagation or scrambled OCR).
3. No unresolved OCR ambiguity in those fields.

## Per-point result

| Code | Pinyin | Source page | Verdict |
|------|--------|:---:|--------|
| LU-1 | Zhongfu | 76 | **Confirmed** (pass-1 leaf corrected — was contaminated) |
| LU-2 | Yunmen | 78 | **Confirmed** |
| LU-3 | Tianfu | 79 | **Confirmed** |
| LU-4 | Xiabai | 80 | **Confirmed** (recovered via column-aware read) |
| LU-5 | Chize | 80 | **Confirmed** (indications corrected — began with LU-4's) |
| LU-6 | Kongzui | 82–83 | **Confirmed** (indications corrected — were LU-8's) |
| LU-7 | Lieque | 84 | **Confirmed** |
| LU-8 | Jingqu | 86 | **Confirmed** (recovered via column-aware read) |
| LU-9 | Taiyuan | 87–88 | **Confirmed** (was contaminated with LU-6's text) |
| LU-10 | Yuji | 88–89 | **Confirmed** |
| LU-11 | Shaoshang | 90–91 | **Confirmed** |

**Confirmed: 11 / 11.**

## Systemic findings (fed back to Build)

1. **Cluster-propagation contamination — FIXED.** Codes in a point's LOCATION prose are landmarks, not a shared clinical block. The extractor no longer copies clinical sections between points; only a missing location may be shared, and it is flagged in `propagated_fields`. This removed contaminated clinical text from ~50 points book-wide (`classical_with_full_text` honestly fell 361 → 357).
2. **Column-aware reading added, full extractor migration deferred.** `render_page_columns` (exposed as `--page`) reconstructs the two-column layout and produces correct per-point sections; it is how the leaves are now verified. Swapping it in as the extractor's global text source, however, *regressed* the heuristic parser (`classical_with_full_text` 357 → 301), because header/section detection was tuned to the scrambled text. A full migration therefore needs a header-detection rewrite (OCR-corrupted caps like `CHlZE`/`YUJl`, multi-page entries) plus book-wide re-validation — tracked as the next Build step. Until then, graduation uses the column-aware reader per point.

## Related

- Leaves grown from this validation: [Knowledge/acupuncture/](../../Knowledge/acupuncture/README.md)
- [Reflection/2026-09-04.md](../../Reflection/2026-09-04.md) — what we learned
