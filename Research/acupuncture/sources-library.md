# Source Library — Acupuncture PDFs

All sources imported into the repo live under [sources/](sources/) and [assets/](assets/).

| ID | Title | System | Location | Status |
|----|-------|--------|----------|--------|
| deadman_manual | A Manual of Acupuncture | Classical body | [sources/pdfs/](sources/pdfs/) | Extracted v0.2 |
| matsumoto_clinical_vol1 | Kiiko Clinical Strategies Vol 1 | Kiiko palpatory | [sources/pdfs/](sources/pdfs/) | Needs OCR |
| matsumoto_nagano_vol2 | Nagano Clinical Strategies Vol 2 | Nagano/Kiiko | [sources/pdfs/](sources/pdfs/) | Needs OCR |
| hecker_microsystems | Microsystems (Ear–Scalp–Hand) | Auricular/microsystems | [sources/pdfs/](sources/pdfs/) | Ready to extract |
| strittmatter_ear_atlas | Ear Atlas (Nogier/Bahr) | Ear microsystem | [sources/pdfs/](sources/pdfs/) | Ready to extract |
| bencaodian_json | Bencaodian open JSON | Classical body | [data/](data/) | Compared v0.1 |
| notebook_reports | Gemini Notebook exports | Mixed | [sources/notebook/](sources/notebook/) | Imported |
| extraordinary_atlas_pngs | Extra point PNG atlases | Classical body | [assets/infographics/](assets/infographics/) | Imported |
| insomnia_infographic | Insomnia reference guide PDF | Clinical protocol | [assets/infographics/insomnia_reference_guide.pdf](assets/infographics/insomnia_reference_guide.pdf) | Imported |
| notebook_audio | Hidden Geography audio | Classical body | [assets/audio/](assets/audio/) | Imported |

Full catalog: [data/sources-catalog.json](data/sources-catalog.json)  
Import manifest: [data/imported-manifest.json](data/imported-manifest.json)

## Important: Three Different Point Systems

These sources do **not** share one flat point list:

```
classical_body     →  LU-1, ST-36, BL-40  (Deadman, Bencaodian)
ear_microsystem    →  Nogier/Bahr ear points (Hecker, Strittmatter atlas)
kiiko_clinical     →  Palpatory/active points, clinical strategies (Matsumoto vols)
```

JSON comparison schema must use a `system` field — do not merge ear points with classical body points in one array without namespace separation.

## Filename Note

Kiiko Volume 1 is at `sources/pdfs/kiiko_matsumoto_david_euler_kiiko_matsumotos_clinical_strategy vol 1.pdf` (space before `vol 1`).

## Next Extraction Priority

1. **Hecker microsystems** — extract numbered ear points to JSON
2. **Strittmatter ear atlas** — extract Nogier/Bahr ear points to JSON
3. **Cross-compare ear sources** — Hecker vs Strittmatter (same microsystem, different numbering?)
4. **OCR Matsumoto vol 1 & 2** — required before Kiiko/Nagano clinical content enters the tree
