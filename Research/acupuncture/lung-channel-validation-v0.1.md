# Lung Channel — Validation v0.1

| Field | Value |
|-------|-------|
| Stage | Wayfinding · [Validate](../../Constitution/Wayfinding/07-Validate.md) |
| Date | 2026-09-04 |
| Inputs | [deadman-extract-v0.2.json](data/deadman-extract-v0.2.json), [comparison-v0.1.json](data/comparison-v0.1.json) |
| Question | Which Lung-channel points (LU-1…LU-11) are confirmed enough to graduate into `Knowledge/` leaves? |

## Gate

A point is **confirmed** (eligible for a Knowledge leaf) when all hold:

1. Present in **both** sources — Deadman extract v0.2 **and** Bencaodian comparison.
2. Non-empty, clean `location_en`, `actions_en`, and `indications_en` in the extract.
3. No detected field contamination (text that actually belongs to a different point).

## Per-point result

| Code | Pinyin | In both sources | location | actions | indications | Verdict |
|------|--------|:---:|:---:|:---:|:---:|--------|
| LU-1 | Zhongfu | yes | clean¹ | yes | yes | **Confirmed** |
| LU-2 | Yunmen | yes | yes | — | — | Deferred (no actions/indications) |
| LU-3 | Tianfu | yes | garbled | yes | — | Deferred (OCR + no indications) |
| LU-4 | Xiabai | yes | yes | yes | — | Deferred (no indications) |
| LU-5 | Chize | yes | yes | yes | clean¹ | **Confirmed** |
| LU-6 | Kongzui | yes | yes | yes | yes | **Confirmed** |
| LU-7 | Lieque | yes | yes | — | — | Deferred (no actions/indications) |
| LU-8 | Jingqu | yes | yes | — | yes² | Deferred (no actions; indications suspect) |
| LU-9 | Taiyuan | yes | yes | yes³ | yes³ | **Blocked** (contaminated) |
| LU-10 | Yuji | yes | yes | yes | yes | **Confirmed** |
| LU-11 | Shaoshang | yes | clean¹ | yes | yes | **Confirmed** |

¹ Minor OCR normalized when authoring the leaf (e.g. `Yunrnen`→`Yunmen`, stray `INDICATIONS o` prefix, trailing point label). 
² LU-8 `indications` text matches the LU-6/LU-9 cluster and is not trustworthy for LU-8. 
³ LU-9 `actions`/`indications` are **identical to LU-6 Kongzui** — copied by the extractor's cluster-propagation step, not Taiyuan's own text.

**Confirmed: 5 / 11** — LU-1, LU-5, LU-6, LU-10, LU-11.

## Systemic findings (feed back to Build)

1. **Cluster-propagation contamination.** `propagate_cluster_fields` in [scripts/deadman_extract.py](scripts/deadman_extract.py) copies shared text to every point named in a block. LU-9 Taiyuan inherited LU-6's `actions`/`indications`; LU-8 inherited cluster `indications`. The propagation should not overwrite a point's own section text, and copied text should be flagged rather than silently merged.
2. **OCR gaps.** Point names/locations carry recurring artifacts (`Yunrnen`, `CHlZE`, `YUJl`, letter/number confusion). Several points (LU-2, LU-7) lost their `actions`/`indications` entirely during parsing.

Both are recorded for a future extractor pass; neither blocks graduating the 5 confirmed points, whose confirmed fields were re-read directly from the source text.

## Related

- Leaves grown from this validation: [Knowledge/acupuncture/](../../Knowledge/acupuncture/README.md)
- [Reflection/2026-09-04.md](../../Reflection/2026-09-04.md) — what we learned
