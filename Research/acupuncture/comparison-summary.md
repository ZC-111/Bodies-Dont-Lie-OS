# Acupuncture Point Comparison v0.1

| Source | Role | Count |
|--------|------|-------|
| Deadman PDF (your file) | Gold standard | 241 points extracted |
| Bencaodian JSON | Open comparison dataset | 208 points |

## Overlap

| Status | Count |
|--------|-------|
| In both | 142 |
| Deadman only | 99 |
| Bencaodian only | 66 |
| Location text overlap (heuristic) | 104 |

## Notes

- Bencaodian already cites `deadman_manual_2e` as a source for many entries.
- PDF text extraction has OCR artifacts (e.g. `LI` appears as `L.1.`). Codes are normalized before comparison.
- This is **Measure/Build v0.1** — not yet a confirmed canonical dataset.
- Full JSON: [data/comparison-v0.1.json](data/comparison-v0.1.json)

## Sample: LU-1 (Zhongfu)

- Deadman page: 76
- Bencaodian name: 中府 (Zhongfu)
