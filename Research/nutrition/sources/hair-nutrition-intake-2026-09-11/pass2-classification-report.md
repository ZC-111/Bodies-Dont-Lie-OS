# Pass 2 — Statement Classification Report

- Created: 2026-09-11T16:01:15Z
- Status: **PASS 2 COMPLETE — classification only**
- Population: **514 / 514** (30 pilot reconfirmed + **484 newly classified**)
- Authorization: proceed with remaining 484 only, same validated taxonomy/rules as pilot
- Pilot consistency: **PASS** (0 mismatches on the 30 pilot statement IDs)
- Taxonomy: identical to `review/run_pass2_pilot30.py` / `review/pass2-pilot-30.json`

## Epistemic ceiling

```text
source → representation → candidate statement → classification → STOP
```

No claim validation. No external evidence. No Knowledge Objects. No Pathways.
Historical wording ≠ BDS-established truth.

## Outputs

- `Research/nutrition/sources/hair-nutrition-intake-2026-09-11/statements/pass2-classified-statements.json`
- `Research/nutrition/sources/hair-nutrition-intake-2026-09-11/statements/pass2-classified-statements.csv`
- Pass 1 `candidate-statements.json` left unchanged

## Source distribution

| Artifact | n |
|---|---:|
| SRC-HN-001 | 189 |
| SRC-HN-002 | 184 |
| SRC-HN-003 | 141 |

## Classification distributions

### statement_kind

| value | n |
|---|---:|
| classification | 220 |
| nutritional_claim | 65 |
| mechanistic | 55 |
| descriptive | 54 |
| unclear | 38 |
| laboratory_claim | 27 |
| warning_or_boundary | 12 |
| traditional_use_claim | 11 |
| clinical_claim | 10 |
| recommendation | 10 |
| hypothesis | 5 |
| causal | 3 |
| associational | 2 |
| therapeutic_claim | 2 |

### claim_status

| value | n |
|---|---:|
| candidate | 292 |
| non_claim | 222 |

### actionability_class

| value | n |
|---|---:|
| informational | 256 |
| none | 234 |
| recommendation | 23 |
| suggestive | 1 |

### epistemic_scope

| value | n |
|---|---:|
| source_assertion | 259 |
| structural_or_metadata | 219 |
| source_recommendation | 23 |
| source_hypothesis | 5 |
| source_warning | 5 |
| unclear | 3 |

### independence

| value | n |
|---|---:|
| unclear | 441 |
| repetition | 73 |

### ambiguity_flag

| value | n |
|---|---:|
| none | 377 |
| compound_statement | 100 |
| type_ambiguous | 36 |
| boundary_ambiguous | 1 |

## Integrity confirmations

| Check | Result |
|---|---|
| Classified count | 514 |
| Pilot 30 consistency | PASS |
| evidence_relation all null | YES |
| evidence_strength all 0 | YES |
| Pass-1 wording preserved | YES |
| Pass-1 independence preserved | YES |
| External evidence consulted | NO |
| Knowledge Objects created | 0 |
| Pathways created | 0 |
| Claim validations performed | 0 |
| Source DOCX modified | NO |

## Checkpoint

```text
PASS 1 COMPLETE (2e0199a / 9491394)
   ↓
PASS 2 PILOT 30 — PASS
   ↓
PASS 2 FULL 514 — COMPLETE
   ↓
0 promoted
   ↓
READY FOR LATER EVIDENCE / PROMOTION PASSES (not authorized here)
```

## STOP

```
PASS 2 CLASSIFICATION COMPLETE
NO CLAIM VALIDATION
NO EVIDENCE STRENGTH
NO PROMOTION
UNCERTAINTY PRESERVED
```
