# Lung Channel — Validation

| Field | Value |
|-------|-------|
| Stage | Wayfinding · [Validate](../../Constitution/Wayfinding/07-Validate.md) |
| Date | 2026-09-04 (revised after extractor fix) |
| Inputs | [deadman-extract-v0.2.json](data/deadman-extract-v0.2.json) (v0.2.1), Deadman source pp. 76–91, [comparison-v0.1.json](data/comparison-v0.1.json) |
| Question | Which Lung-channel points (LU-1…LU-11) are confirmed enough to graduate into `Knowledge/` leaves? |

## Why this note was revised

The first pass graduated 5 points from extract fields alone. Deeper inspection found the extractor's `propagate_cluster_fields` step was **copying clinical text between points** that merely reference each other as anatomical landmarks. Concretely, LU-6 Kongzui and LU-9 Taiyuan had both been given **LU-8 Jingqu's** indications, and LU-1's fields were also propagated (and wrong). The bug is fixed (extract v0.2.1); clinical sections are no longer propagated. See [Reflection/2026-09-04.md](../../Reflection/2026-09-04.md).

## Gate (revised)

A point is **confirmed** when:

1. Present in **both** sources — Deadman + Bencaodian.
2. Its `location`, `actions`, and `indications` are read/verified **directly from the Deadman source pages** (not from cross-point propagation).
3. No unresolved OCR ambiguity in those fields.

## Per-point result

| Code | Pinyin | Source page | Verdict |
|------|--------|:---:|--------|
| LU-1 | Zhongfu | 76 | **Confirmed** (prior leaf corrected — was contaminated) |
| LU-2 | Yunmen | 78 | **Confirmed** |
| LU-3 | Tianfu | 79 | **Confirmed** |
| LU-4 | Xiabai | 80 | Deferred — no clean `indications` block in source OCR |
| LU-5 | Chize | 80 | **Confirmed** |
| LU-6 | Kongzui | 82–83 | **Confirmed** (indications corrected — were LU-8's) |
| LU-7 | Lieque | 84 | **Confirmed** |
| LU-8 | Jingqu | 86 | Deferred — no clean `actions` block in source OCR |
| LU-9 | Taiyuan | 87–88 | **Confirmed** (was contaminated with LU-6's text) |
| LU-10 | Yuji | 88–89 | **Confirmed** |
| LU-11 | Shaoshang | 90–91 | **Confirmed** |

**Confirmed: 9 / 11.** Deferred: LU-4, LU-8 (partial source OCR only).

## Systemic findings (fed back to Build)

1. **Cluster-propagation contamination — FIXED.** Codes in a point's LOCATION prose are landmarks, not a shared clinical block. The extractor no longer copies clinical sections between points; only a missing location may be shared, and it is flagged in `propagated_fields`. This removed contaminated clinical text from ~50 points book-wide (`classical_with_full_text` honestly fell 361 → 357).
2. **Per-point section attribution is still imperfect** on scrambled multi-column pages, so clinical fields for graduated leaves are read directly from the source pages rather than trusted from the extract.

## Related

- Leaves grown from this validation: [Knowledge/acupuncture/](../../Knowledge/acupuncture/README.md)
- [Reflection/2026-09-04.md](../../Reflection/2026-09-04.md) — what we learned
