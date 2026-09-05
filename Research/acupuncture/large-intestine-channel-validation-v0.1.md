# Large Intestine Channel — Validation v0.1

| Field | Value |
|-------|-------|
| Stage | Wayfinding · [Validate](../../Constitution/Wayfinding/07-Validate.md) |
| Date | 2026-09-04 |
| Inputs | Deadman source pp. 100–120 (column-aware), [comparison-v0.1.json](data/comparison-v0.1.json) |
| Question | Which Large Intestine points (LI-1…LI-20) are confirmed enough to graduate into `Knowledge/` leaves? |

## Method

Read every LI entry directly from the **column-aware** Deadman source (`deadman_extract.py --page 97-121`), which reconstructs the two-column layout in true reading order. Each point's `location`, `actions`, and `indications` were transcribed from its source page(s). This is the same source-verified method that completed the Lung channel; it avoids the scrambled-OCR and cross-point-contamination failure modes documented for the raw extract.

## Gate

A point is **confirmed** when: present in both sources (Deadman + Bencaodian) and its `location`, `actions`, and `indications` are read directly from the source page with no unresolved OCR ambiguity.

## Result

**All 20 of 20 confirmed.** Cross-source: all 20 LI points are present in Bencaodian (`comparison-v0.1.json`).

| Code | Pinyin | Page | Code | Pinyin | Page |
|------|--------|:---:|------|--------|:---:|
| LI-1 | Shangyang | 100 | LI-11 | Quchi | 112–113 |
| LI-2 | Erjian | 101 | LI-12 | Zhouliao | 114 |
| LI-3 | Sanjian | 102 | LI-13 | Shouwuli | 115 |
| LI-4 | Hegu | 103–104 | LI-14 | Binao | 115–116 |
| LI-5 | Yangxi | 106–107 | LI-15 | Jianyu | 116–117 |
| LI-6 | Pianli | 108 | LI-16 | Jugu | 117–118 |
| LI-7 | Wenliu | 109 | LI-17 | Tianding | 118 |
| LI-8 | Xialian | 110 | LI-18 | Futu | 118–119 |
| LI-9 | Shanglian | 110–111 | LI-19 | Kouheliao | 119 |
| LI-10 | Shousanli | 111 | LI-20 | Yingxiang | 119–120 |

## Related

- Leaves grown from this validation: [Knowledge/acupuncture/](../../Knowledge/acupuncture/README.md)
- Method precedent: [lung-channel-validation-v0.1.md](lung-channel-validation-v0.1.md)
- [Reflection/2026-09-04.md](../../Reflection/2026-09-04.md)
