# Hair / Nutrition — BDS First-Pass Intake Report

- Intake ID: `INTAKE-HN-2026-09-11`
- Created: 2026-09-11T14:53:18Z
- Pass: **first_pass_intake_only**
- Status: **BLOCKED — original artifacts not in custody**

## BDS principle

> Historical research material is evidence about what was previously researched;
> it is not automatically evidence that the underlying claim is true.

This pass does **not** interpret, improve, consolidate, validate, or promote.
No Knowledge Objects, Pathways, clinical recommendations, or patient-facing content were created.

## Custody scan

| Check | Result |
|---|---|
| Conversation attachments | 0 |
| Workspace `*.docx` | 0 |
| `raw/` preserved originals | 0 |
| Cataloged hair/nutrition historical artifact | 1 (not in custody) |

## Manifested artifacts

### SRC-HN-001 — Hair Follicle Optimization Master Research v0.2

| Field | Value |
|---|---|
| Stable ID | `src-hn-001-hair-follicle-optimization-v0.2` |
| Filename | `Hair_Follicle_Optimization_Master_Research_v0.2.docx` |
| Format | docx |
| Claimed size | 44343 bytes |
| SHA-256 | **unknown** (bytes not in custody) |
| Document date | unknown |
| Host listing date (low confidence) | 2026-08-25 (prior Mac Downloads listing in agent history) |
| Provenance | `Research/integrative-medicine/local-downloads/data/local-downloads-catalog.json` → id `hair-follicle-optimization` |
| Claimed path | `/Users/nuu/Downloads/Hair_Follicle_Optimization_Master_Research_v0.2.docx` |
| Custody state | `claimed_present_elsewhere` |
| Accessible local file | false |
| Preserved representation | false |
| Source representation | `SREP-HN-001` (stub only) |
| Statements extracted | **0** |

## Source representations

| ID | Artifact | Status |
|---|---|---|
| SREP-HN-001 | SRC-HN-001 | incomplete — awaiting original bytes |

## Candidate statements

| Metric | Count |
|---|---:|
| Extracted | 0 |
| `requires_classification` | 0 |
| Merged | 0 |
| Evidence strength assigned | 0 |

Statement extraction was **not performed**. Inventing wording from a missing file would violate intake-only rules.

## Duplicates / derivative documents

| Finding | Determination |
|---|---|
| Duplicate originals in custody | none (no originals present) |
| Derivative documents among intake set | **unclear** — insufficient provenance; cannot compare bytes or content |
| Apparent statement repetition | **not assessed** — no statements extracted |
| Independent vs derivative vs repetition | **unclear** — provenance does not permit determination |

## Unresolved provenance

1. **SRC-HN-001** binary not present in cloud workspace; only catalog + historical host path.
2. Author/speaker unknown (`speaker: null` in catalog).
3. Document date unknown.
4. No content hash available.
5. Relationship to in-repo acupuncture hair/scalp protocols is **not established** and those files were **not** included as intake subjects.

## Observed related materials (out of scope for this intake)

These exist in-repo but were **not** treated as the supplied hair/nutrition historical research set:

- `Research/acupuncture/hair-scalp-protocols.md`
- `Research/acupuncture/data/hair-scalp-protocols-v0.1.json`

Reason: derived acupuncture protocol pack (`source_file` null), not a supplied nutrition/hair research binary.

## Statements requiring later evidence review

None extracted. After originals are preserved, every extracted statement must be marked `requires_classification` before any evidence-strength or promotion work.

## What would unblock intake

1. Place unchanged original(s) under:
   `Research/nutrition/sources/hair-nutrition-intake-2026-09-11/raw/`
2. Re-run intake hashing + source representation completion.
3. Extract candidate statements with source wording + location only.
4. Still do **not** merge duplicates, assign strength from repetition, or create Knowledge Objects in that pass.

## Outputs

- `manifest.json`
- `representationsations/SREP-HN-001.json`
- `statements/candidate-statements.json`
- `statements/candidate-statements.csv` (header only)
- `raw/README.md` (custody empty)
- this report

## STOP

```
INTAKE BLOCKED — NO ORIGINAL BYTES IN CUSTODY
NO STATEMENTS INVENTED
NO KNOWLEDGE OBJECTS
NO PATHWAYS
NO CLINICAL RECOMMENDATIONS
NO CLAIM VALIDATION
UNCERTAINTY PRESERVED
```
