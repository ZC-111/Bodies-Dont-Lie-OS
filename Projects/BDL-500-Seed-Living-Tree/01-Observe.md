# 01 — Observe

| Field | Value |
|-------|-------|
| Project | [BDL-500](../README.md) |
| Stage | 1 of 8 |
| Status | Complete |
| Spec | [Wayfinding 01-Observe](../../Constitution/Wayfinding/01-Observe.md) |
| Question | What is the system showing us? |
| Observed | 2026-08-25 |

## System Under Study

Bodies Don't Lie OS — the repository as it exists today, with focus on the Living Tree layers above the trunk: branches (domain folders) and leaves (knowledge objects).

## Observation Log

### Repository structure (2026-08-25)

- The repository contains 55 markdown files.
- Eight top-level folders exist: Constitution, Knowledge, Skills, Projects, Research, Templates, Reflection, Archive.
- Constitution/ holds BDL-000, BDL-001, BDL-002, 14 principle files, 8 wayfinding stage files, and 6 living-tree layer files.
- Knowledge/ holds one file: `README.md`. No subfolders. No knowledge objects.
- Research/ holds one file: `README.md`. No research artifacts.
- Skills/ holds one file: `README.md`. No skills defined.
- Reflection/ holds one file: `README.md`. No reflection logs.
- Projects/ holds one active project: BDL-500-Seed-Living-Tree (nine files including this one).
- Archive/ holds Draft 1 of the original constitution and two archive README-adjacent files.

### Asymmetry between layers

- Roots layer (Constitution, Principles): populated — 22+ documents.
- Trunk layer (BDL standards): populated — BDL-000, BDL-001, BDL-002.
- Branches layer (Knowledge/domain/): empty — no domain subfolders exist.
- Leaves layer (Knowledge/*.md objects): empty — zero atomic knowledge files.

### Domains referenced but not instantiated

BDL-000 Article II lists these scope areas:

Human Health · Medicine · Nutrition · Psychology · Ecology · Architecture · Engineering · Cities · AI · Education · Organizations · Communities

None of these appear as folders or files outside the Constitution.

### Naming and origin signals

- The project name is "Bodies Don't Lie OS."
- The repository author signed documents as "First Wayfinder."
- The GitHub repository is `ZC-111/Bodies-Dont-Lie-OS`.
- The original ChatGPT conversation that seeded this work was titled "Wayfinder Method in Practice."
- Living Tree layer docs use examples from human biology: inflammation, cytokines, TNF-alpha, IL-6, CRP.

### Templates vs. usage

- Templates exist for: principles, knowledge objects, folder READMEs, project stages.
- No file in Knowledge/ was created from the knowledge-object template.
- No file in Skills/ exists beyond the folder README.

### Growth direction already documented

- BDL-002 states: create a branch only when at least one leaf exists to put on it.
- BDL-002 states: growth happens at the leaves, not by enlarging existing documents.
- The Reflection folder defines six distillation questions but contains no dated entries.

### First Wayfinder observation (2026-08-25)

- Knowledge source material exists but is **not yet organized** into the repository.
- Some material is stored in **Otter.ai** (transcripts/recordings — format and quantity not yet measured).
- Some material is in **Gemini notebooks** (quantity and topics not yet measured).
- Additional material is on **another hard disk** (location, format, and quantity not yet documented).
- A specific domain need has been identified: **acupuncture** — particularly a cross-source comparison of acupuncture points.
- Gold standard source located: **A Manual of Acupuncture (Peter Deadman)** PDF (673 pages, text-extractable).
- Additional local PDF sources catalogued — see [Research/acupuncture/sources-library.md](../../Research/acupuncture/sources-library.md):
  - Kiiko Matsumoto Clinical Strategies Vol 1 (469 pp, **image-only — needs OCR**)
  - Nagano Clinical Strategies Vol 2 (314 pp, **image-only — needs OCR**)
  - Hecker/Peuker/Steveling Microsystems — ear/scalp/hand (338 pp, text-extractable)
  - Strittmatter Ear Atlas — Nogier/Bahr (439 pp, text-extractable)
- Comparison v0.1 completed: Deadman PDF vs Bencaodian JSON — 142 overlapping classical point codes.
- No external documents have been imported as leaves or research artifacts yet.

## Unresolved Questions

*(For Stage 02 — Measure)*

1. Which of the 12 scope areas in BDL-000 appears most often across existing documents?
2. What is the current ratio of structure files (READMEs, standards, templates) to content files (knowledge, research, skills)?
3. How many times do health- or body-related terms appear in non-Constitution files?
4. How many items are in Otter.ai? What domains or topics do they cover?
5. How many Gemini notebooks exist? What topics do they cover?
6. What is on the other hard disk? (file types, approximate volume, subject matter)
7. Is there overlap between Otter.ai, Gemini notebooks, and hard-disk content?
8. Which acupuncture websites are authoritative enough to scrape and compare?
9. How many acupuncture points need to be in the comparison set? (e.g. 361 classical points)
10. What fields must each JSON point record include? (name, location, meridian, coordinates, indications, source URL)

## Test

Can you describe what you observed without explaining why?

**Status:** ☑ Yes — the log above describes what is present and absent without assigning causes.

## Related

- Next: [02-Measure.md](02-Measure.md)
