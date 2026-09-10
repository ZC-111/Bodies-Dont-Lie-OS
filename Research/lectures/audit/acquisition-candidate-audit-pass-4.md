# BDS Library Audit — Pass 4: Acquisition Candidate / Information-Value Gate

## Purpose

This pass is the **first decision gate** after Passes 1–3.

It asks which already-known external representations could **materially increase BDS library information value** relative to acquisition/processing effort — **without acquiring anything**.

Governing principle: **acquisition is not the default.**

> SHOW US THE MONEY BEFORE WE SPEND THE MONEY  
> (information gained per unit effort — not dollar pricing or monetization)

## Scope

Read-only inputs (frozen):

| Input | Role |
|---|---|
| Pass 1 title reconciliation | Frozen identity/relationship classes |
| Pass 2 local representation inventory | What we already possess |
| Pass 3 external availability | What exists externally (unchecked acquisition) |
| Otter manifest / AOSRD catalogs | Context only |

**No downloads. No processing. No Pass 1–3 modifications. No source packet changes.**

Unit of analysis: **one row per external representation opportunity** (PDF and video evaluated separately when both exist). Catalog-only 2022 / local-downloads rows included where no public URL exists.

CSV rows: **403**

## Decision Matrix

| Decision | Count | Meaning |
|---|---:|---|
| ACQUIRE_CANDIDATE | 31 | Strong future acquisition case |
| CONDITIONAL_ACQUIRE | 35 | Acquire only after condition |
| DEFER_EXISTING_REPRESENTATION | 14 | Local coverage likely sufficient |
| DEFER_IDENTITY_UNRESOLVED | 125 | Resolve relationship first |
| DEFER_EXPENSIVE_VIDEO | 137 | Cost/effort currently unattractive |
| DEFER_LOW_INFORMATION_GAIN | 0 | Limited expected gain |
| HUMAN_REVIEW | 12 | Needs human judgment |
| NO_ACQUISITION_INDICATED | 14 | No clear acquisition opportunity |
| NOT_ENOUGH_INFORMATION | 35 | Insufficient evidence |

## Information-gain / effort distribution

| `information_gain_effort` | Count |
|---|---:|
| exceptional | 29 |
| strong | 2 |
| moderate | 35 |
| weak | 27 |
| poor | 249 |
| unknown | 61 |

---

# SHOW US THE MONEY

Decision aid only — **not a download queue**, not clinical ranking, not monetization ranking.

### Strong information-gain opportunities

Candidates with `information_gain_effort` ∈ {exceptional, strong}: **31**

| Record | Type | IGE | Decision | Why |
|---|---|---|---|---|
| Ancient Healing Traditions for Modern Times – Video | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| EMF and Depletion of Nitric Oxide with Beth Shirley 8-Oct-2024 (Video) | AOSRD_PDF | strong | ACQUIRE_CANDIDATE | PDF likely corresponds to an existing Otter session (Pass 1 strong) but may add slides/figures/references not present as |
| Drug Induced Nutrient Depletion with Dr. Harlan Bieley 24-Sep-2024 (Vi | AOSRD_PDF | strong | ACQUIRE_CANDIDATE | PDF likely corresponds to an existing Otter session (Pass 1 strong) but may add slides/figures/references not present as |
| Pushing the Limits-From Ultra-Endurance to Revolutionary Patient Care  | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | PDF likely corresponds to an existing Otter session (Pass 1 strong) but may add slides/figures/references not present as |
| Neuroinflammation-The Road to Neuropsychiatric Illness with Dr. Mark G | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Dementia’s Dirty Dozen with Dr David Ajibade – Oct 31, 2023 (Video) | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| From Marijuana to Mushroom-Are Plants and Fungi ‘Natural’ with Dr. Jef | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Intermittent Fasting, Stimulating Brown Fat, and Weight Management wit | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| How to Choose the Best Stem Cell Sources for Your Practice with Dr. Jo | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Unlocking the Power of the Mind-Body Connection with Dr. Emmett Miller | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Pharmacology of Key Emerging Therapies in Chronic DIseases with Dr Mik | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Live Healthier, Better and Longer with Hydrogen by Bob Settineri – Jul | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Clinical applications of Amlexonax – June 6, 2023 (Video) | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Autism with Dr. Jenny Blanchard Stone – April 25, 2023 (Video) | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Behind the Scenes Thyroid Mechanisms with Dr. Brad Watts – April 4, 20 | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Bioregulatory Medicine Applied to Fur Babies with Dr. Marlene Siegel – | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| The 14-3-3n Biomarker for Rheumatoid Arthritis Diagnosis, Prognosis, a | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| The Role of Nutrition and Prevention – December 20, 2022(Video) | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Integrative Psychiatry, Neurofeedback, and the Treatment Resistant Pat | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Osteopathic Manipulation in Treating Pain, and Substance Abuse – Novem | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Gut-Brain Connection by Dr. Brad Watts (Video) | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| The Future of Biological Dentistry: Where Do We Go from Here? with Dr. | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Anti-Aging Medicine with Dr. Mikhail Berman (Video) | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Integrative Medicine and the Law by Judge Egan Walker (Video) | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| New Horizons in Cancer Treatment by Kalapana Patel, MD (Video) | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Frequency Specific Microcurrent by Carol McMakin, MA,DC (Video) | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| What I Learned from the Osteopathic Masters-Dr. William Richwine (Vide | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Biological Dentistry by Dr. Scott Chandler (Video) | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Hypo and Hyperthyroidismare One Internal Disease with Two Different Ma | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Medical Intuition by Terri Jay  Aug 31, 2021 – Video | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |
| Post Covid 19 Vaccination Syndrome | AOSRD_PDF | exceptional | ACQUIRE_CANDIDATE | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentially_new_session — not a confir |

### Best low-effort opportunities

`ACQUIRE_CANDIDATE` / `CONDITIONAL_ACQUIRE` with low/trivial cost, low/medium processing, novelty ≥ 2: **66**

These are almost entirely **AOSRD PDFs** (finite, text/visual-bearing, publicly HEAD-reachable in Pass 3).

### Existing-library enrichment opportunities

PDFs linked to Pass 1 **strong/likely** Otter sessions where local slide images are absent (Pass 2 `claimed_present_elsewhere`): **3**

These add a durable visual/source representation without treating the lecture as new Knowledge.

### Potentially new source opportunities

PDF `ACQUIRE_CANDIDATE` rows with `pdf_role=potentially_new_source` (Pass 1 `no_match` — **not confirmed new lectures**): **28**

These are the clearest “new representation of possibly uncovered session” bets at low cost.

### Expensive traps

`DEFER_EXPENSIVE_VIDEO`: **137**

Pattern: video available externally + captions/transcript **not_checked** + (existing Otter text **or** unresolved identity **or** cheaper PDF alternative).

Do **not** spend download/Whisper budget here until a human authorizes a later pass and caption availability is known.

---

# PDF ACQUISITION OPPORTUNITY

| Metric | Count |
|---|---:|
| Externally available PDFs evaluated | 71 |
| already_local | 1 |
| enrichment_candidate | 3 |
| potentially_new_source | 28 |
| identity_resolution_candidate | 35 |
| redundant (via already_local / NO_ACQUISITION) | 1 |
| unclear | 4 |
| ACQUIRE_CANDIDATE | 31 |
| CONDITIONAL_ACQUIRE | 35 |
| Deferred / no-acquire / review | 5 |

**No PDFs were downloaded.**

---

# VIDEO ACQUISITION OPPORTUNITY

| Metric | Count |
|---|---:|
| Video representation rows | 284 |
| YouTube rows | 275 |
| Vimeo rows | 8 |
| Rumble rows | 1 |
| Pass 3 YouTube available (context) | 262 |
| Available YT with Pass1 strong/likely | 34 |
| Available YT potentially_new_session | 103 |
| YT captions status not_checked (Pass 3) | 275 |
| DEFER_EXPENSIVE_VIDEO | 137 |
| DEFER_IDENTITY_UNRESOLVED | 125 |
| NO_ACQUISITION_INDICATED | 13 |
| NOT_ENOUGH_INFORMATION | 1 |
| ACQUIRE_CANDIDATE (video) | 0 |

**No videos were downloaded.** Caption/transcript text was not fetched.

Especially useful for later human review (not acquisition): videos that are `potentially_new_session` **and** lack a companion PDF — they remain expensive until captions can be verified.

---

## Top candidate table

Strongest acquisition cases for human authorization review (capped ~18; full set in CSV). Grouped by decision quality, **not** clinical importance.

| Record | Representation | Why it matters | What we already have | Expected gain | Effort | Decision |
|---|---|---|---|---|---|---|
| Ancient Healing Traditions for Modern Times – Video | AOSRD_PDF | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentia | catalog_record_and_URL_only | PDF lecture notes/slides/figures/references for a  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| Anti-Aging Medicine with Dr. Mikhail Berman (Video) | AOSRD_PDF | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentia | catalog_record_and_URL_only | PDF lecture notes/slides/figures/references for a  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| Autism with Dr. Jenny Blanchard Stone – April 25, 2023  | AOSRD_PDF | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentia | catalog_record_and_URL_only | PDF lecture notes/slides/figures/references for a  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| Behind the Scenes Thyroid Mechanisms with Dr. Brad Watt | AOSRD_PDF | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentia | catalog_record_and_URL_only | PDF lecture notes/slides/figures/references for a  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| Biological Dentistry by Dr. Scott Chandler (Video) | AOSRD_PDF | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentia | catalog_record_and_URL_only | PDF lecture notes/slides/figures/references for a  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| Bioregulatory Medicine Applied to Fur Babies with Dr. M | AOSRD_PDF | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentia | catalog_record_and_URL_only | PDF lecture notes/slides/figures/references for a  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| Clinical applications of Amlexonax – June 6, 2023 (Vide | AOSRD_PDF | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentia | catalog_record_and_URL_only | PDF lecture notes/slides/figures/references for a  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| Dementia’s Dirty Dozen with Dr David Ajibade – Oct 31,  | AOSRD_PDF | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentia | catalog_record_and_URL_only | PDF lecture notes/slides/figures/references for a  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| Frequency Specific Microcurrent by Carol McMakin, MA,DC | AOSRD_PDF | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentia | catalog_record_and_URL_only | PDF lecture notes/slides/figures/references for a  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| From Marijuana to Mushroom-Are Plants and Fungi ‘Natura | AOSRD_PDF | AOSRD PDF is externally available and Pass 1 found no reasonable Otter candidate (potentia | catalog_record_and_URL_only | PDF lecture notes/slides/figures/references for a  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| Drug Induced Nutrient Depletion with Dr. Harlan Bieley  | AOSRD_PDF | PDF likely corresponds to an existing Otter session (Pass 1 strong) but may add slides/fig | FbRyr7EkkewAoPTmXbK9DtUiA_Y:otter_transcript+otter | Durable visual/source PDF representation (slides,  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| EMF and Depletion of Nitric Oxide with Beth Shirley 8-O | AOSRD_PDF | PDF likely corresponds to an existing Otter session (Pass 1 strong) but may add slides/fig | EqC6yd4bQDKMl2mpzPURPZu-_Pc:otter_transcript+otter | Durable visual/source PDF representation (slides,  | cost=low/proc=low | ACQUIRE_CANDIDATE |
| Another View of the Endocannabinoid System with Dr. Rob | AOSRD_PDF | Pass 1 relationship is possible only. PDF is a low-cost artifact that could help resolve i | tAtmhIMa7fmRXEWqsjZP4Gl7vkM:otter_transcript+otter | Identity-resolution evidence plus possible visual/ | cost=low/proc=low | CONDITIONAL_ACQUIRE |
| Cannabis 101 with Dr. Kent Crowley – May 9, 2023 (Video | AOSRD_PDF | Pass 1 relationship is possible only. PDF is a low-cost artifact that could help resolve i | KPtFIYDuvg1p0CbfNkYIuOVkwIE:otter_transcript+otter | Identity-resolution evidence plus possible visual/ | cost=low/proc=low | CONDITIONAL_ACQUIRE |
| Chronic Fatigue Syndrome by Dr. Jacob Teitelbaum March  | AOSRD_PDF | Pass 1 relationship is possible only. PDF is a low-cost artifact that could help resolve i | eEDmdeOTNokKYKUadQuO_9gDjuo:otter_transcript+otter | Identity-resolution evidence plus possible visual/ | cost=low/proc=low | CONDITIONAL_ACQUIRE |
| Chronic Fatigue Syndrome: Road to Resolution: Dr. Todd  | AOSRD_PDF | Pass 1 relationship is possible only. PDF is a low-cost artifact that could help resolve i | CMNjlQbT2xu4NqL-9gu4VQSt0mo:otter_transcript+otter | Identity-resolution evidence plus possible visual/ | cost=low/proc=low | CONDITIONAL_ACQUIRE |
| Culinary Oncology with Chef Laura Pole 04-Mar-2025 (Vid | AOSRD_PDF | Pass 1 relationship is possible only. PDF is a low-cost artifact that could help resolve i | 0pIRZSR5hLU8vZNbqCJ9pLpRE9M:otter_transcript+otter | Identity-resolution evidence plus possible visual/ | cost=low/proc=low | CONDITIONAL_ACQUIRE |
| Ehlers Danlos Syndrome Treated with Frequency Specific  | AOSRD_PDF | Pass 1 relationship is possible only. PDF is a low-cost artifact that could help resolve i | vZKE66zexBS6KPliMMq0glRxefk:otter_transcript+otter | Identity-resolution evidence plus possible visual/ | cost=low/proc=low | CONDITIONAL_ACQUIRE |

## Method notes

- Pass 1 classes are **frozen** (strong/likely/possible/variant/no_match untouched).
- Pass 2 local states and Pass 3 availability states are **frozen**.
- `potentially_new_session` is **not** promoted to confirmed new lecture.
- YouTube availability ≠ transcript availability (Pass 3 captions largely `not_checked`).
- Otter screenshot JPEGs remain `claimed_present_elsewhere`; not treated as acquired.
- No clinical, scientific, or monetization ranking.

## Acquisition boundary

This report does **not** authorize downloads.

Any next acquisition step requires **explicit human authorization**.

## STOP

```
PASS 4 COMPLETE.
ACQUISITION CANDIDATES AUDITED.
INFORMATION-VALUE GATE COMPLETE.
NO MEDIA ACQUIRED.
NO MEDIA PROCESSED.
NO SOURCE PACKETS MODIFIED.
NO PASS 1, PASS 2, OR PASS 3 RECORDS MODIFIED.
HUMAN ACQUISITION AUTHORIZATION REQUIRED FOR ANY NEXT STEP.
```

## Outputs

- `Research/lectures/audit/acquisition-candidate-audit-pass-4.csv` (403 data rows)
- `Research/lectures/audit/acquisition-candidate-audit-pass-4.md` (this file)
