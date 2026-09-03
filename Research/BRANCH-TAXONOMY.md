# Research Branch Taxonomy

How to sort PPT/PDF sources into Living Tree branches. **Catalog first; move files only when ready.**

## Branches (folders)

| Branch | Put here | Do not put here |
|--------|----------|-----------------|
| **[acupuncture/](acupuncture/)** | Points, meridians, Kiiko, Harvard AP, laser AP | General CME |
| **[immune/](immune/)** | Autoimmune, rheumatology, mold, mycotoxins, CIRS, mast cells, immuno-oncology | Isolated vitamin product sheets |
| **[nutrition/](nutrition/)** | Food, diet, fasting, **vitamins, minerals, probiotics, nutraceuticals**, clinical nutrition | Herbals, oils, homeopathy |
| **[materia-medica/](materia-medica/)** | **Herbals, essential oils, flower essences, tinctures, homeopathy** | Vitamins/minerals (those → nutrition) |
| **[integrative-medicine/](integrative-medicine/)** | Multi-topic conferences (AOSRD, lecture dumps) with theme tags | Single-topic files that fit a domain branch |

## Medical-term tags (inside files / catalogs)

Organize by **branch folder + medical term tags**, not one folder per disease.

Filename scan of Desktop/Documents/Downloads (`ching` + `chingchen`, research-ish files only):  
[`data/filename-medical-terms-scan.json`](data/filename-medical-terms-scan.json)

| Term tag | ≈ files | Primary branch |
|----------|--------:|----------------|
| pain_msk | 51 | integrative / acupuncture if AP |
| neuro | 48 | integrative (or future `neuro/` if leaves grow) |
| ethics_systems | 42 | **exclude** from Research (ops/CME admin) |
| acupuncture | 33 | acupuncture |
| laser_light | 23 | acupuncture or integrative |
| derm | 21 | integrative (or future derm) |
| psych_behavioral | 16 | integrative / behavioral |
| cardio | 16 | integrative / cardiometabolic |
| endocrine_hormone | 15 | nutrition or integrative |
| nutrition_food | 14 | nutrition |
| infection_covid | 12 | immune |
| vitamin_supplement | 11 | nutrition |
| detox | 11 | immune or nutrition (by focus) |
| autoimmune | 9 | immune |
| gi_metabolic | 9 | nutrition |
| immune | 7 | immune |
| womens_gyn | 6 | integrative |
| regenerative | 5 | integrative |
| pediatric | 5 | integrative |
| cancer_onco | 4 | immune / integrative |
| injection_iv | 3 | integrative |
| fatigue_cfs | 3 | immune |
| herbal_botanical | 2 | materia-medica |
| mold_mycotoxin | 2 | immune |
| mast_cell | 1 | immune |
| oils / flower / homeopathy | 0 by name | materia-medica when found |

~2000 “unmatched” names were mostly **practice ops** (receipts, licenses, forms) or Harvard codes (`kid-`, `ren-`, `liv-` point PDFs, `AcuLecture` without the word acupuncture).

## Quick sort rules

1. **Mold / mycotoxins / autoimmune / mast cell** → `immune`
2. **Food / diet / fasting / vitamins / supplements** → `nutrition`
3. **Herb / oil / flower / tincture / homeopathy** → `materia-medica`
4. **Acupuncture / laser AP / meridian / Kiiko** → `acupuncture`
5. **Pain, neuro, cardio, hormones, regen** → keep under `integrative-medicine` with term tags until a branch earns enough leaves
6. **Conference with many topics** → `integrative-medicine` + `themes[]` / `terms[]`
7. **Patient PHI, receipts, NuSkin contracts, ethics/billing stacks** → exclude

## Cross-links

One file, one primary branch. Add `related_branches` + `medical_terms: []` when needed.

## Known drive clusters (not yet imported)

| Location | Likely branch |
|----------|----------------|
| `Downloads/Lectures 2021/` | Tag into immune / nutrition / integrative |
| `Desktop/Vitamin product research/` | nutrition |
| `Desktop/client resources/` | nutrition |
| AOSRD 2022 | integrative-medicine (cataloged) |
| Harvard / Kiiko / charts | acupuncture (cataloged) |

## Next step

Enrich catalogs with `medical_terms[]` from this lexicon; import selectively by branch.
