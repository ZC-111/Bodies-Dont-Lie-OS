# BDS Archive Audit — Title Reconciliation Pass 1

| Field | Value |
|---|---|
| Generated | 2026-09-10 |
| Scope | Read-only inventory reconciliation (no downloads/transcription) |
| Otter ground truth | `Research/lectures/data/otter-manifest.json` (98) + `packet.json` enrichment |
| Web inventories | aosrd-webinars `catalog.json` + aosrd-2022 lectures + local-downloads packs |

> A title match is a **candidate relationship**, not confirmed identity. Uncertainty is a valid result.

## Sources examined

| Source | Records |
|---|---:|
| `aosrd_2022_conference` | 29 |
| `aosrd_webinars_rumble` | 1 |
| `aosrd_webinars_vimeo` | 8 |
| `aosrd_webinars_youtube` | 275 |
| `local_downloads` | 19 |
| **Total web/AOSRD/YouTube inventory records** | **332** |
| Otter Clearfield sessions | 98 |

Note: In-repo inventories total **332** records. No new scrape toward an external 385–400 estimate was performed.

## Summary counts (best class per web record)

| Class | Count |
|---|---:|
| Strong (Level 1) | 39 |
| Likely (Level 2) | 1 |
| Possible (Level 3) | 142 |
| Variant / derivative | 4 |
| No Otter candidate (Level 4) | 146 |
| Requiring human review (web records) | 303 |
| Otter sessions with ≥2 web representations (strong/likely/variant) | 10 |
| Web records mapping to ≥2 Otter candidates (strong/likely/variant) | 4 |
| Crosswalk rows (incl. multi-candidate) | 478 |

## Matching method

- Otter.ai titles are generic; comparison uses **packet.json enriched titles**, speakers, themes, segment topics, and medical terms.
- Acronym expansion for comparison only (e.g. SIBO ↔ small intestine bacterial overgrowth); originals preserved.
- Web dates parsed from titles when present; YouTube publication date is not assumed equal to Otter session date.
- **Strong requires substantive topic/title evidence** — exact date alone (or generic titles like “Video – DATE”) is not enough.
- Multiple Otter candidates retained when close in score; variants flagged, not collapsed.

## Example strong / likely candidates

| Web title | Web date | Otter date | Class | Sim | Date rel |
|---|---|---|---|---:|---|
| The Direct Primary Care Practice Model-How to Do It with Stefan H | 2026-05-12 | 2026-05-12 | strong | 0.386 | exact |
| Frequency, Sound and Autonomic Regulation with Margarita Xistris​ | 2026-03-03 | 2026-03-04 | strong | 0.521 | near_1d |
| The End of Medicine with Dr. Paul Clayton – Video – 12 March 2026 | 2026-03-12 | 2026-03-10 | strong | 0.5 | near_2d |
| Stress Dominance-Why Hormone Dysregulation Begins Before Labs Go  | 2026-02-18 | 2026-02-18 | strong | 0.14 | exact |
| Ketamine for Treatment Resistant Depression with Dr. Erwin Boco – | 2026-02-11 | 2026-02-11 | strong | 0.25 | exact |
| Mitochondrial Therapeutics for Enhancing Healthspan with Dr. Siob | 2026-02-04 | 2026-02-04 | strong | 0.373 | exact |
| The What, Why, How and How-Not of Aging with Dr. Bill Andrews – V | 2026-01-21 | 2026-01-21 | strong | 0.408 | exact |
| Cannabis for Dementia with Dr Dustin Sulak – Video – 13-Jan-2026 | 2026-01-13 | 2026-01-14 | strong | 0.462 | near_1d |
| Menopause and Vasomotor Symptoms-Therapeutic Options with Dr. Fel | 2025-12-17 | 2025-12-17 | strong | 0.385 | exact |
| Optimized Nutrient Absorption with Methylated, Nanoscale and Adap | 2025-12-10 | 2025-12-10 | strong | 0.302 | exact |
| HRT, Ice Plunges, Omega-3s and Dead Hangs Saved Me and Now we are | 2025-11-26 | 2025-11-26 | strong | 0.302 | exact |
| Neural Therapy with Dr John Burgess – Video – 13-Nov-2025 | 2025-11-13 | 2025-11-12 | strong | 0.397 | near_1d |
| Platelet Rich Fibrin; Optimizing the Glycocalyx and a Protocol to | 2025-11-05 | 2025-11-05 | strong | 0.218 | exact |
| Conference Preview, Spirituality, Progesterone After Hysterectomy | 2025-10-14 | 2025-10-14 | strong | 0.446 | exact |
| Beyond Pharmogenomics-Addressing Root Causes of Anxiety and Depre | 2025-08-05 | 2025-08-05 | strong | 0.429 | exact |

## Many-to-one: Otter sessions with multiple web representations

| Otter date | Packet | # web records |
|---|---|---:|
| 2025-02-05 | `Research/lectures/clearfield-webinar-2025-02-05` | 3 |
| 2026-05-12 | `Research/lectures/clearfield-webinar-2026-05-12` | 2 |
| 2025-12-10 | `Research/lectures/clearfield-webinar-2025-12-10` | 2 |
| 2025-03-25 | `Research/lectures/clearfield-webinar-2025-03-25` | 2 |
| 2024-12-18 | `Research/lectures/clearfield-webinar-2024-12-18` | 2 |
| 2024-10-08 | `Research/lectures/clearfield-webinar-2024-10-08` | 2 |
| 2024-09-24 | `Research/lectures/clearfield-webinar-2024-09-24` | 2 |
| 2024-09-10 | `Research/lectures/clearfield-webinar-2024-09-10` | 2 |
| 2025-06-24 | `Research/lectures/clearfield-webinar-2025-06-24` | 2 |
| 2025-05-20 | `Research/lectures/clearfield-webinar-2025-05-20` | 2 |

## Potential New Work

Not a processing queue. Web/AOSRD records with **no reasonable Otter candidate** in this pass.

Count: **146**

| Source | Web date | Title |
|---|---|---|
| local_downloads |  | A Manual of Acupuncture (purple cover) |
| aosrd_2022_conference |  | AP, Laser AP & Bio AP-Dr Anwar — Anwar |
| aosrd_webinars_youtube |  | Advanced Laboratory Testing for Rheumatic Diseases – Tyler O’Malley |
| aosrd_webinars_youtube |  | Ancient Healing Traditions for Modern Times – Video |
| aosrd_webinars_youtube |  | Anti-Aging Medicine with Dr. Mikhail Berman (Video) |
| aosrd_2022_conference |  | Autoimmune Diseases ASORD (1) — Born |
| aosrd_webinars_youtube |  | Basic Hormone Replacement for Men Part 1 Student Session w MM (Video) |
| aosrd_webinars_youtube |  | Basic Hormone Replacement for Men Part 2 + Dr C’s Tips for Weight Loss (Video) |
| aosrd_webinars_youtube |  | Basic Hormone Replacement for Men Part 3 Finasteride, Lab Studies and Testosterone Replace |
| aosrd_webinars_youtube |  | Biological Dentistry by Dr. Scott Chandler (Video) |
| local_downloads |  | Brain and Mycotoxins |
| aosrd_2022_conference |  | Brittany Partain CB-CAPs Presentation COME 4.0 — Pertain |
| aosrd_webinars_youtube |  | Build Your Own Personalized Nutritional  Formula from the Ground Up With Michael Lomis – V |
| aosrd_2022_conference |  | CHRONIC FATIGUE –DYSHOMEOSTASIS--Dr. K. Patel March 2022 Meeting — Patel |
| aosrd_2022_conference |  | CME Federal Emergency Healthcare Response-Daniel Stock MD — Stock |
| aosrd_2022_conference |  | COVID-19 pres 2-1 — Yutani |
| aosrd_webinars_youtube |  | Case Histories Show Casing the Power of Anti Aging Medicine |
| aosrd_webinars_youtube |  | Chronic DIsease Management Kathleen ONeil Smith |
| aosrd_webinars_youtube |  | Clearfield – Non-Hormonal Remedies to Relieve Hormonal Symptoms – December, 2023 (Video) |
| local_downloads |  | Colchicine uses |
| aosrd_webinars_youtube |  | Covid 19 Management for the Vaccinated and Unvaccinated by Dr. Dan Stock |
| aosrd_webinars_youtube |  | Depression by Dr. Ron Centric (Video) |
| aosrd_webinars_youtube |  | Dermatology Review: Top Ten Chronic Conditions (Part 1) by Dr. Mike Boehmer (Video) |
| aosrd_webinars_youtube |  | Discovering the Path to Health by Dr. Mark Lafferty (Video) |
| aosrd_2022_conference |  | Dr AJ. Farshchian Powerpoit — Farshchian |
| aosrd_webinars_youtube |  | Early Viral Treatment Post Pandemic Clinical Applications Roundtable (Video) |
| aosrd_webinars_youtube |  | Estrogen-Devil or Angel with Dr. Bill Clearfield (Video) |
| aosrd_webinars_youtube |  | Female Hormone Primer Part 2 Student Session with MM (Video) |
| aosrd_webinars_youtube |  | Female Hormone Primer-Part 1 Student Session w MM (Video) |
| aosrd_webinars_youtube |  | Female Hormone Primer-Part 3 Polycystic Ovaries and Female Pattern Hair Loss (Video) |
| aosrd_2022_conference |  | Fibromyalgia and Post covid CFS Rx -Practitioners- Osteopathy group-Jacob Teitelbaum — Tei |
| aosrd_webinars_youtube |  | Frequency Specific Microcurrent by Carol McMakin, MA,DC (Video) |
| aosrd_webinars_youtube |  | From Chronic Illness to High Fit Patients with Jake Guidas – Video |
| aosrd_webinars_youtube |  | Gut-Brain Connection by Dr. Brad Watts (Video) |
| local_downloads |  | Hair Follicle Optimization Master Research v0.2 |
| aosrd_webinars_youtube |  | How to Perform a Subcutaneous Injection (Video) |
| aosrd_webinars_youtube |  | How to Perform an Intramuscular Injection (Video) |
| aosrd_webinars_youtube |  | Hypo and Hyperthyroidismare One Internal Disease with Two Different Manifestations by Dr.  |
| local_downloads |  | Insomnia reference guide |
| local_downloads |  | Integrative Immunology — Nutritional Cofactors / Carbon60 |
| aosrd_webinars_youtube |  | Integrative Immunoncology |
| aosrd_webinars_youtube |  | Integrative Medicine and the Law by Judge Egan Walker (Video) |
| local_downloads |  | Integrative medicine lecture notes |
| aosrd_webinars_youtube |  | Intervegrated Interventional Radiology by Dr. Brian Evans (Video) |
| aosrd_webinars_youtube |  | Introduction to Hormone Optimization-DHEA, Pregnenolone, Prolactin and Beginning Lab Evalu |
| aosrd_webinars_youtube |  | Introduction to Hormone Optimization-Par 1-Homeopathic Edition (Video) |
| aosrd_webinars_youtube |  | Introduction to Hormone Optimization-Part 4-Laboratory Evaluation JR Student Session (Vide |
| aosrd_2022_conference |  | KOS-Slide Show — O'Neil Smith |
| aosrd_2022_conference |  | LIFESTYLE MEDICINE-Transforming Primary Care — Sundermann |
| aosrd_2022_conference |  | Lecture, Hidden Epidemic, Las Vegas virtual, 3.26.2022-Levy — Levy |
| aosrd_2022_conference |  | Lillo-Coronary Artery Calcium Scoring PPT for JLL of — Lillio |
| local_downloads |  | Low-dose colchicine — CV prevention / anti-inflammatory |
| aosrd_webinars_youtube |  | Medical Cannibis for Chronic Pain-Hype or Reality by Dr. Mikhail Kogan (Video) |
| aosrd_webinars_rumble |  | Medical Freedom: Stefan Hartmann, PA’s Presentation to the Florida Delegates of State Legi |
| aosrd_webinars_youtube |  | Micronutrients in Chronic Disease States by Dr. Kedar Prasad (Video) |
| aosrd_webinars_youtube |  | Muscle Centric Health (Video) |
| aosrd_webinars_youtube |  | Muscle Testing with Dr. Clyde Porter (Video) |
| aosrd_2022_conference |  | NAD Injection and IV Therapy-2 — Macheret |
| aosrd_webinars_youtube |  | New Horizons in Cancer Treatment by Kalapana Patel, MD (Video) |
| aosrd_2022_conference |  | Nitric Oxide for the Prevention and Treatment of Cardiovascular DIsease with a Splash of C |
| aosrd_2022_conference |  | Opioid Use Disorder-D. Leszkovitz — Lezkowitz |
| local_downloads |  | Overlap between Morgellons, Lyme disease, and syphilis |
| aosrd_webinars_vimeo |  | Pathophysiologic Rationale for Early Treatment of COVID-19 with Dr. Peter McCoullough |
| aosrd_webinars_youtube |  | Peter Zebot-The Second Law of Human Nature  – Video |
| aosrd_webinars_youtube |  | Physician Burnout-A Real Problem and a Way Forward by Dr. Yusuf Erskine (Video) |
| aosrd_webinars_youtube |  | Post Covid 19 Vaccination Syndrome |
| aosrd_2022_conference |  | Stellate Ganglion Harris Final — Harris |
| aosrd_webinars_youtube |  | Stress Devil or Angel by Dr Mikhail Berman (Video) |
| aosrd_webinars_youtube |  | Substance Abuse in OMT, PMR, and Pain Management Medicine with Dr. David Leszkovitz (Video |
| aosrd_webinars_youtube |  | The Benefits of Adding Safe, Regular, and Effective Corrective Exercise Therapy to Supplem |
| aosrd_webinars_vimeo |  | The Courage to Face Covid-19 By Dr. Peter Mccullough (Video) |
| aosrd_webinars_youtube |  | The Endocrinology of Autism-Condensed Version |
| aosrd_webinars_youtube |  | The Future of Biological Dentistry: Where Do We Go from Here? with Dr. Scott Chandler (Vid |
| aosrd_webinars_youtube |  | The Histology of Morgellons Nobody’s Talking About – Video |
| aosrd_webinars_youtube |  | The Importance of the Upper Cervical Spine The Atlas Orthogonal Perspective by Dr. Dennis  |
| aosrd_webinars_youtube |  | The Nuts and Bolts of Bioidentical Hormone Optimization-Part 1 (Video) |
| aosrd_webinars_youtube |  | The Nuts and Bolts of Bioidentical Hormone Optimization-Part 2 Hormones-Testoste (Video) |
| aosrd_webinars_youtube |  | The Nuts and Bolts of Hormone Optimization-Putting It All Together-Part 3 Growth Hormone T |
| aosrd_webinars_youtube |  | The Psychology of Success with Dr. Jim Naccarato – Video |
| aosrd_webinars_youtube |  | The Role of Angiotensin-Converting Enzyme 2 in Sars-CoV 2 by Dr. Halasa |
| local_downloads |  | The hidden geography of acupuncture channels (audio) |
| aosrd_webinars_youtube |  | US Canada Hormone Conference Progesterone (Video) |
| aosrd_2022_conference |  | Ultrasound in Integrative Medicine-Dr. R. Badal — Badal |
| aosrd_webinars_youtube |  | What I Learned from the Osteopathic Masters-Dr. William Richwine (Video) |
| aosrd_webinars_youtube |  | When Syndromes Overlap-A Complex Case History of Hyperadrogenism, Multiple Autoimmune Mala |
| aosrd_webinars_youtube |  | Why Vitamin C Therapy Works – Video |
| aosrd_webinars_youtube |  | William Clearfield, DO – American Osteopathic Society of Integrative Medicine Lectures – J |
| aosrd_webinars_youtube |  | William Clearfield, DO – Endocrinology of Psychiatric Illnesses – Jan, 2024 (Video) |
| aosrd_2022_conference |  | looking at rheumatic diseases_1-Speer — Speer |
| aosrd_2022_conference |  | slide show2 — Faculty |
| aosrd_webinars_youtube |  | “Low Dose Naltrexone” by Dr William Clearfield |
| aosrd_webinars_youtube | 2020-12-22 | COVID 19 Pathology and Treatment S Halasa Dec 22, 2020 |
| aosrd_webinars_youtube | 2021-08-03 | Natural Immunity via Homeopathic Medicine vs Artificial Immunity via Vaccination by Dr Par |
| aosrd_webinars_youtube | 2021-08-31 | Medical Intuition by Terri Jay  Aug 31, 2021 – Video |
| aosrd_webinars_youtube | 2021-10-19 | Chronic Fatigue-Chronic Infections by Dr. Kalapana Patel 19 Oct 2021 |
| aosrd_webinars_youtube | 2021-11-23 | Good and Bad Electromagnetic Fields Jami and Dr Rugerrio, November 23, 2021 |
| aosrd_webinars_youtube | 2021-12-07 | Fascia, Pain Modulation and Autoimmunity by Kathleen O’Neil Smith, MD, December 7, 2021 |
| aosrd_webinars_youtube | 2021-12-21 | Quantum Anti-Aging by Dr. Parvin Zarrin, December 21, 2021 |
| aosrd_webinars_youtube | 2022-01-25 | Homeostasis Hormesis and Chemical Sensitivity by Dr. Kalapala Patel January 25, 2022 -Vide |
| aosrd_2022_conference | 2022-01-30 | McCullough Presentation Pathophysiologic Rationale for Early Treatment of COVID-19 ND Jan  |
| … | … | _(+46 more in CSV where best class = no_match)_ |

## Files created

- `Research/lectures/audit/title-reconciliation-pass-1.csv`
- `Research/lectures/audit/title-reconciliation-pass-1.md`

## STOP

Pass 1 complete. No transcription, PDF extraction, slide, or video processing performed.
