# ApoB-First CVD Prevention — Lipid Protocol Pathway

| Field | Value |
|---|---|
| **Packet** | `clearfield-webinar-2026-06-30` |
| **Primary speaker(s)** | Stefan Hartman, DO; niacin counterpoint Steven McConnell; host Bill Clearfield |
| **Clinical core** | Drive ApoB (and LDL) to plaque-prevention / reversal thresholds with cheap evidence-based agents; optional niacin branch for LP(a) / statin-intolerant patients |
| **Pathway type** | `biomarker_driven` |
| **Priority** | `high` |
| **Sources used** | `derived/` only |
| **Slide pass** | `pending` |
| **Last updated** | 2026-09-03 |

## Disclaimer

Speaker-attributed synthesis from Clearfield Tuesday webinar materials. Verify doses, indications, and legality before clinical use. Conflicts between transcript and slides are listed explicitly — do not silently resolve them. Hartman and McConnell **disagree** on niacin strength of evidence — both branches are preserved.

## 1. Indication & Scope

**For:** Adults (and selected children with FH risk) needing atherosclerotic risk reduction; functional-medicine patients at risk of “lipid denialism”; postmenopausal women on HRT whose ApoB may improve with estradiol optimization; LP(a) elevation; statin-intolerant or uninsured patients needing low-cost options.

**Not for / refer out:** Acute coronary syndrome, unstable angina, symptomatic severe stenosis needing urgent cardiology; pediatric dosing beyond speaker’s screening guidance — specialty referral.

**Lecture framing:** “ApoB below 65 prevents plaque; LDL below 60 prevents; LDL below 40 reverses” (Hartman core thesis). Prefer ApoB over LDL-C; prefer CT angiogram over CAC for soft plaque.

## 2. Entry Criteria

### History / clinical picture
- CVD risk, family premature MI, FH suspicion, keto/carnivore high-LDL narratives, statin myalgia history, uninsured / cost-sensitive
- Women: HRT dosing context (estradiol → PCSK9 / LDL-receptor effects)

### Labs / imaging (as stated)
- **ApoB** (~$5–6; fasting not required) — primary serial marker
- Standard lipids + LP(a) when relevant; consider desmosterol (Boston Heart) if cognitive concern on statin / ApoE4
- Imaging: **CT angiogram** preferred; CAC misses soft plaque; CIMT / carotid US adjuncts
- Pediatric: ApoB as early as ~age 9 if risk; conventional panels from ~age 8 cited

### Red flags → escalate / do not start pathway
- Acute ischemic symptoms → ED / cardiology
- Suspected plaque instability — **avoid nattokinase** (Hartman stroke case warning)
- Driving desmosterol too low in ApoE4 → cognitive risk; reassess statin strategy

## 3. Pathway Overview

```text
[Order ApoB ± LP(a) ± imaging]
        ↓
 Set target: ApoB <60–65 prevention · <40 established CVD (Hartman summary)
        ↓
 First-line: Rosuvastatin 5 mg + Ezetimibe 10 mg (~$1/mo)
        ↓ intolerant / refuses / LP(a) focus
 Branch A: Ezetimibe ± niacin (Castelli titration) ± lifestyle
 Branch B: PCSK9i (Repatha) if needed / accessible
        ↓ women on HRT
 Optimize estradiol (FSH 5–24 Clearfield framing) — may lower ApoB
        ↓
 Serial ApoB — do not manage by CAC alone
```

| Phase | Goal | Typical duration (as stated) |
|---|---|---|
| Assess | ApoB + risk + imaging choice | Baseline |
| Treat | Hit ApoB / LDL targets | Ongoing titration |
| Myalgia rescue | Vitamin D ~40 ng/mL before labeling “intolerant” | Weeks |
| Niacin branch | Full effect ~3 g/day after slow titration | Weeks–months |
| Maintain | Serial ApoB; plaque reassessment via CTA as indicated | Long-term |

## 4. Phases (detail)

### Phase 1 — Assess & set targets

| Item | Detail | Claim tag |
|---|---|---|
| Interventions | ApoB on (nearly) everyone; LP(a) when indicated; prefer CTA over CAC | `speaker_claim` / `cited_study` |
| Dosing / products | ApoB test ~$5–6 | `practice_pearl` |
| Timing | Baseline before therapy; fasting optional for ApoB | `speaker_claim` |
| Expected response | Identify true atherogenic particle burden LDL-C can miss (e.g., high TG) | `cited_study` |
| Stop / modify if | Acute syndrome → stop pathway, escalate | — |

**Hartman numeric targets (summary protocol):** ApoB **&lt;60** prevention or **&lt;40** established CVD; lecture thesis also states ApoB **&lt;65** no new plaque / LDL **&lt;60** prevent / **&lt;40** reverse — treat **&lt;60–65** band as prevention language pending slide reconcile. | `speaker_claim`

### Phase 2 — First-line pharmacologic (Hartman)

| Item | Detail | Claim tag |
|---|---|---|
| Interventions | **Rosuvastatin 5 mg + Ezetimibe 10 mg** | `speaker_claim` / `cited_study` |
| Dosing / products | Rosuvastatin 5 mg ≈ **$0.42/mo** ($13.90/1000 McKesson); combo framed **&lt;$1/mo** vs ~$740/mo supplement stack | `speaker_claim` |
| Timing | Daily; follow ApoB serially | `speaker_claim` |
| Expected response | CTT: ~22% ↓ major vascular events per 38 mg/dL LDL reduction (170k / 26 RCTs framing) | `cited_study` |
| Stop / modify if | Myalgia → check vitamin D (~40 ng/mL resolves **93%** per McConnell experience) before switching; cognitive / low desmosterol → reassess | `practice_pearl` |

**Ezetimibe pearl:** gut cholesterol reabsorption block + brain-protection observational signal (~7× ↓ cognitive decline risk in large older-adult cohort — speaker-cited). Near-zero side effects framing. | `cited_study` / `speaker_claim`

### Phase 3 — Alternate / escalation branches

| Item | Detail | Claim tag |
|---|---|---|
| Interventions | Statin-intolerant: ezetimibe alone + **niacin** + lifestyle; or PCSK9i (Repatha, q2wk) | `speaker_claim` |
| Dosing / products | **Niacin (Castelli):** start **50 mg/meal** → titrate slowly with food → target **3 g/day**; flush education | `practice_pearl` |
| Timing | Niacin: weeks–months to full dose; flush often settles in 2 weeks–1 month | `speaker_claim` |
| Expected response | McConnell: only monotherapy moving all lipoproteins favorably; LP(a) ↓ up to **75%**; Hartman skeptical on modern morbidity RCTs | `speaker_claim` / `cited_study` |
| Stop / modify if | Hepatotoxicity / intolerance; AIM-HIGH / HPS2-THRIVE critiques are debated — do not erase disagreement | `speaker_claim` |

**Low-cost LP(a) adjuncts mentioned:** undesiccated thyroid (NZ, no Rx claimed) ~32% ↓ LP(a); red yeast rice ~23%; berberine mild PCSK9 inhibition — tag as `practice_pearl` / verify legality. | `practice_pearl`

### HRT adjunct (women)

| Item | Detail | Claim tag |
|---|---|---|
| Interventions | Dose estradiol to FSH **5–24** (Clearfield protocol framing); track lipids/ApoB | `practice_pearl` |
| Mechanism (stated) | ↑ hepatic LDL receptors; ↓ PCSK9 | `speaker_claim` |

## 5. Decision Forks

| If… | Then… | Source |
|---|---|---|
| High ApoB, cost-sensitive | Rosuva 5 + ezetimibe 10 first | notes Seg 4 / 7 |
| Statin myalgia | Vitamin D → ~40 ng/mL before declaring intolerance; CoQ10 less favored than D per McConnell | notes Seg 7 |
| ApoE4 / cognitive concern on statin | Check desmosterol; avoid over-suppression | notes Seg 7 |
| High LP(a) | Consider niacin branch (McConnell); Hartman open to trial with ApoB before/after | notes Seg 5 |
| Soft-plaque question | Prefer CT angiogram over CAC | notes Seg 4G |
| Patient asks nattokinase | Counsel against — plaque destabilization / stroke case | notes Seg 4I |
| Child with FH family history | ApoB early (~9); treat if elevated — case examples discussed | notes Seg 7 |
| Keto CTA “safe LDL” narrative | Note Norwitz et al. study **retracted**; counterexamples in practice | notes Seg 4B |

## 6. Monitoring Cadence

| Marker / check | When | Target (as stated) | Source |
|---|---|---|---|
| ApoB | Baseline + serial on therapy | &lt;60–65 prevention; &lt;40 established CVD | notes Seg 4 / 7 |
| Vitamin D | If myalgia on statin | ~40 ng/mL | notes Seg 7 |
| Desmosterol | Cognitive concern / ApoE4 | Avoid excessive suppression | notes Seg 7 |
| LP(a) | Baseline if indicated; on niacin | Downward trend (McConnell cases) | notes Seg 5 |
| CTA / imaging | Risk-based | Soft + hard plaque assessment | notes Seg 4G |
| Estradiol / FSH (women) | When optimizing HRT | FSH 5–24 framing | notes Seg 4A |

## 7. Cautions, Interactions & Controversies

- **Hartman vs McConnell on niacin** — preserve both positions; September McConnell deep-dive flagged as follow-up
- Nattokinase: explicit harm signal in this lecture
- Retracted keto CTA study — do not cite as safety evidence
- Statin brain cholesterol synthesis issue (desmosterol) especially ApoE4
- Device / esthetic segments (BTL, MP Gun) are **out of scope** for this pathway

## 8. Adjuncts Mentioned (non-core)

- Regressive vicariation / homotoxicology tip (Nario) — detox framing guardrails only
- Ayurvedic lipid protocols (Dr. James) — future lecture, not operationalized here
- Victor high-dose niacin “detox” ramp (Hubbard reference) — separate from Castelli clinical titration; do not merge

## 9. Gaps / TBD (do not invent)

- [ ] Exact ApoB target table from slides (65 vs 60 wording reconcile)
- [ ] Full Castelli titration schedule (mg steps / weeks)
- [ ] PCSK9i access / dosing chart from slides
- [ ] Pediatric dosing specifics beyond “treat if elevated”
- [ ] Slide OCR / vision pass on `slides/slide-2026-06-30-*.jpeg`

## 10. Source Map

| Claim / step | Notes file § | Slide ID(s) | Quote / paraphrase |
|---|---|---|---|
| ApoB &lt;65 / LDL &lt;60 / &lt;40 thesis | Seg 4 | pending | core thesis |
| Summary protocol (statin+ezetimibe) | Seg 7 | pending | first-line ~$1/mo |
| CTT 22% RRR framing | Seg 4D | pending | 170k / 26 RCTs |
| Ezetimibe cognition signal | Seg 4E | pending | ~7× observational |
| Niacin Castelli titration | Seg 5 | pending | 50 mg/meal → 3 g/day |
| Vitamin D myalgia 93% | Seg 7 | pending | McConnell experience |
| Nattokinase stroke case | Seg 4I | pending | carotid disease warning |
| CTA &gt; CAC | Seg 4G | pending | soft plaque |

---

*Generated from `derived/` only. Slide pass pending. Template: `Research/lectures/templates/protocol-pathway.md`*
