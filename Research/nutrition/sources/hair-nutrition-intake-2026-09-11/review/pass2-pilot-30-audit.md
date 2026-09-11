# Pass 2 Pilot Audit — 30-statement classification

- Created: 2026-09-11T15:55:19Z
- Input: `Research/nutrition/sources/hair-nutrition-intake-2026-09-11/statements/candidate-statements.json` (514 statements)
- Pilot artifact: `Research/nutrition/sources/hair-nutrition-intake-2026-09-11/review/pass2-pilot-30.json` (**review-only / non-authoritative**)
- Full candidate dataset modified: **NO**
- External evidence consulted: **NO**
- Commit/PR: **NOT created** (hard stop)

## Sampled IDs (n=30)

- STMT-HN-0344
- STMT-HN-0401
- STMT-HN-0457
- STMT-HN-0495
- STMT-HN-0019
- STMT-HN-0074
- STMT-HN-0129
- STMT-HN-0165
- STMT-HN-0199
- STMT-HN-0241
- STMT-HN-0283
- STMT-HN-0311
- STMT-HN-0062
- STMT-HN-0245
- STMT-HN-0355
- STMT-HN-0085
- STMT-HN-0294
- STMT-HN-0043
- STMT-HN-0189
- STMT-HN-0252
- STMT-HN-0336
- STMT-HN-0122
- STMT-HN-0281
- STMT-HN-0374
- STMT-HN-0144
- STMT-HN-0266
- STMT-HN-0436
- STMT-HN-0212
- STMT-HN-0175
- STMT-HN-0369

## Source distribution

| Artifact | Count |
|---|---:|
| SRC-HN-001 | 9 |
| SRC-HN-002 | 10 |
| SRC-HN-003 | 11 |

## Classification distribution

### statement_kind

| value | n |
|---|---:|
| classification | 13 |
| mechanistic | 5 |
| nutritional_claim | 3 |
| causal | 2 |
| laboratory_claim | 2 |
| recommendation | 2 |
| warning_or_boundary | 2 |
| clinical_claim | 1 |

### claim_status

| value | n |
|---|---:|
| candidate | 17 |
| non_claim | 13 |

### actionability_class

| value | n |
|---|---:|
| none | 14 |
| informational | 12 |
| recommendation | 4 |

### epistemic_scope

| value | n |
|---|---:|
| structural_or_metadata | 13 |
| source_assertion | 12 |
| source_recommendation | 4 |
| source_warning | 1 |

### independence

| value | n |
|---|---:|
| unclear | 24 |
| repetition | 6 |

### ambiguity_flag

| value | n |
|---|---:|
| none | 23 |
| compound_statement | 6 |
| boundary_ambiguous | 1 |

## Required confirmation counts

| Check | Value |
|---|---|
| Sampled | 30 |
| `statement_kind=unclear` | 0 |
| `ambiguity_flag=compound_statement` | 6 |
| `independence=repetition` | 6 |
| `independence=unclear` | 24 |
| evidence_relation all null | YES |
| evidence_strength all 0 | YES |
| External evidence consulted | NO |
| Promotion (KO/Pathway/recs) | NO |
| Full 514 dataset modified | NO |

## Consistency audit findings

- No blocking inconsistencies detected in the pilot set.

## Schema / category observations

- Allowed statement_kind list is broad; short nutrient labels overlap classification vs nutritional_claim — pilot treats short labels as classification + non_claim + structural_or_metadata.
- actionability_class and statement_kind can both mark directive content; kept both (kind=form, actionability=directive force).
- ambiguity_flag is single-valued in this pilot schema; secondary ambiguities placed in classification_notes.
- evidence_relation left JSON null; evidence_strength integer 0 as not assessed.

## Verdict

**PASS**

## HARD STOP

Pilot complete. Do **not** classify the remaining 484 statements without explicit human authorization.
