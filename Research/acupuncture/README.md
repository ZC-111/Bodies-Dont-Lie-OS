# Acupuncture Research

## Purpose

Cross-source comparison of acupuncture point data to build a confirmed foundation for the Living Tree `Knowledge/acupuncture/` branch.

## What Belongs Here

- Source datasets (JSON)
- Comparison outputs
- Extraction scripts
- Research notes on discrepancies
- **Imported sources** — [sources/](sources/) (PDFs, notebook exports)
- **Assets** — [assets/](assets/) (atlases, audio)
- **Spreadsheets** — [data/spreadsheets/](data/spreadsheets/)

## Folder Layout

```
Research/acupuncture/
├── data/           JSON extracts, comparisons, manifest
├── scripts/        Extraction and enrichment tools
├── sources/
│   ├── pdfs/       Textbook PDFs (Deadman, Kiiko, Hecker, ear atlas)
│   └── notebook/   Gemini Notebook Google Docs exports
├── assets/
│   ├── infographics/  Extraordinary point PNG atlases + insomnia PDF
│   └── audio/         NotebookLM audio overviews
└── *.md            Research notes
```

Import inventory: [data/imported-manifest.json](data/imported-manifest.json)

## Naming Rules

- Sources: `{source}-acupoints.json`
- Comparisons: `comparison-v{version}.json`
- Scripts: `scripts/{name}.py`

## Related Folders

- [Knowledge/acupuncture/](../../Knowledge/acupuncture/README.md) — Confirmed leaves (future)
- [Projects/BDL-500-Seed-Living-Tree/](../../Projects/BDL-500-Seed-Living-Tree/README.md) — Parent wayfinding project
- [Constitution/BDL-002-Living-Tree.md](../../Constitution/BDL-002-Living-Tree.md) — Organizational model

## Gold Standard

| System | Source |
|--------|--------|
| Classical body points | **A Manual of Acupuncture** (Peter Deadman) |
| Ear microsystem | Hecker/Peuker/Steveling + Strittmatter/Nogier-Bahr atlas |
| Clinical strategies | Kiiko Matsumoto & David Euler (Vol 1 + Nagano Vol 2) |

See [sources-library.md](sources-library.md) and [data/sources-catalog.json](data/sources-catalog.json).

## Comparison Sources

| Source | URL | License | Points |
|--------|-----|---------|--------|
| Bencaodian | [bencaodian.org/data/v1/acupoints.json](https://bencaodian.org/data/v1/acupoints.json) | CC BY-SA 4.0 | 208 |

See [comparison-summary.md](comparison-summary.md) for latest results.

## Clinical Protocols

| Topic | File |
|-------|------|
| Sleep & spirit / insomnia | [sleep-spirit-protocols.md](sleep-spirit-protocols.md) → [data/sleep-spirit-protocols-v0.1.json](data/sleep-spirit-protocols-v0.1.json) |
| Infographics & atlases | [assets/infographics/](assets/infographics/) |
