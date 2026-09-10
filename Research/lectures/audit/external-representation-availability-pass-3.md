# BDS Library Audit — Pass 3: External Representation Availability

## Purpose

This pass checks whether **already-cataloged** external representations in the AOSRD / Clearfield ecosystem currently appear publicly available, **without acquiring or processing them**.

It answers: what additional representations exist externally, and how they relate to what BDS already has.

It does **not** decide what to download, process, or promote.

## Scope

Local catalogs/inventories used (read-only):

| Resource | Role |
|---|---|
| `Research/lectures/audit/title-reconciliation-pass-1.csv` / `.md` | Frozen relationship candidates |
| `Research/lectures/audit/local-representation-inventory-pass-2.csv` / `.md` | Frozen local representation states |
| `Research/lectures/data/otter-manifest.json` | Otter session index (98) |
| `Research/integrative-medicine/aosrd-webinars/study-guide/catalog.json` | Ongoing webinars (284 records) |
| `Research/integrative-medicine/aosrd-2022/data/aosrd-catalog.json` | 2022 conference (29 lectures) |
| `Research/integrative-medicine/local-downloads/data/local-downloads-catalog.json` | Local Downloads (19 packs) |

**This was NOT a broad new web scrape.** Only URLs already present in those inventories were availability-checked.

Methods (availability only):

- AOSRD PDFs: HTTP `HEAD` (no PDF body retained)
- YouTube: oEmbed metadata (title/channel/existence); caption track listing attempted via timedtext `type=list` (no caption text retrieved)
- Vimeo: public page reachability (small HTML peek only)
- Rumble: public page request attempted

YouTube player/innertube metadata and `yt-dlp` were blocked by a login/bot wall on this host; therefore **caption/transcript availability could not be verified** and is recorded as `not_checked`.

## External Availability Summary

| Metric | Count |
|---|---:|
| Inventory rows (CSV) | 332 |
| AOSRD webinar catalog records examined | 284 |
| AOSRD PDF URLs (catalog rows with `pdf_url`) | 71 |
| AOSRD PDFs available externally | 71 |
| AOSRD PDFs unavailable externally | 0 |
| AOSRD PDFs not checked | 0 |
| YouTube records | 275 |
| YouTube videos available (oEmbed) | 262 |
| YouTube videos unavailable (oEmbed 404) | 13 |
| YouTube captions indicated | 0 |
| YouTube transcript indication verified | 0 |
| YouTube captions status `not_checked` | 275 |
| Vimeo records | 8 |
| Vimeo videos available | 8 |
| Rumble records | 1 |
| Rumble videos available | 0 |
| Rumble `not_checked` (HTTP 403 from audit host) | 1 |
| AOSRD 2022 records (no public stream/PDF URL in catalog) | 29 |
| Local-downloads records (no public stream URL in catalog) | 19 |

## Relationship Summary

Derived from **frozen Pass 1 match classes** (not rewritten):

| Relationship | Count |
|---|---:|
| existing_session_representation (Pass1 strong) | 37 |
| probable_existing_session_representation (Pass1 likely) | 1 |
| possible_existing_session_representation (Pass1 possible/variant) | 143 |
| potentially_new_session (Pass1 no_match) | 142 |
| unclear | 9 |

| `potentially_new_source_status` | Count |
|---|---:|
| no_new_source_indicated | 38 |
| potentially_new_session | 142 |
| unclear | 152 |
| not_checked | 0 |

Webinar rows with ≥1 Pass 1 Otter candidate id: **167** / 284.

## Text Opportunity Summary

Factual external text-bearing routes only — **not a processing priority list**.

| `external_text_opportunity` | Count |
|---|---:|
| pdf_available | 71 |
| captions_available | 0 |
| transcript_indication | 0 |
| multiple_text_routes | 0 |
| none_identified | 53 |
| unclear | 0 |
| not_checked | 208 |

Notes:

- All **71** catalog PDF links that were checked resolved as `available_external`.
- YouTube caption/transcript opportunity is almost entirely `not_checked` due to the login/bot wall (oEmbed existence checks still succeeded for most videos).
- `not_checked` text opportunity rows are mostly available YouTube videos **without** a catalog PDF, where captions could not be verified.

## AOSRD Summary

| State | Count |
|---|---:|
| Webinar catalog records | 284 |
| Catalog PDF URL present | 71 |
| PDF available externally | 71 |
| PDF present locally (Pass 2, unchanged) | 1 |
| Video URL available externally (YT+Vimeo verified) | 270 |
| Video present locally (Pass 2) | 0 |

Landing page `https://aosrd.org/webinars/` was reachable during this audit (catalog hub; not per-lecture deep links).

## Clearfield/Otter Summary

- The **98** Otter sessions remain text-complete locally (Pass 2).
- Pass 3 does **not** treat every external video/PDF as a separate lecture.
- External items with Pass 1 **strong/likely** classes are treated as representations of existing BDS/Otter sessions (or probable), not new sessions.
- Otter screenshot JPEGs remain `claimed_present_elsewhere` per Pass 2; Pass 3 did **not** retrieve them and did **not** reclassify them as `available_external`.

## Potentially New Material

Records with `potentially_new_source_status=potentially_new_session`: **142**.

These are **not** confirmed new lectures. Evidence is frozen Pass 1 `no_match` (no reasonable Otter candidate in Pass 1). Worth later investigation only.

| Source | Count |
|---|---:|
| aosrd_2022_conference | 22 |
| aosrd_webinars_youtube | 108 |
| local_downloads | 12 |

Full list (title + evidence):

| Source | Title | Evidence |
|---|---|---|
| aosrd_2022_conference | AP, Laser AP & Bio AP-Dr Anwar — Anwar | Pass1 `no_match` |
| aosrd_2022_conference | American Osteopathic Society Congress of Medical Excellence 3-25-22-Lozano — Lozano | Pass1 `no_match` |
| aosrd_2022_conference | Autoimmune Diseases ASORD (1) — Born | Pass1 `no_match` |
| aosrd_2022_conference | Brittany Partain CB-CAPs Presentation COME 4.0 — Pertain | Pass1 `no_match` |
| aosrd_2022_conference | CHRONIC FATIGUE –DYSHOMEOSTASIS--Dr. K. Patel March 2022 Meeting — Patel | Pass1 `no_match` |
| aosrd_2022_conference | CME Federal Emergency Healthcare Response-Daniel Stock MD — Stock | Pass1 `no_match` |
| aosrd_2022_conference | COVID-19 pres 2-1 — Yutani | Pass1 `no_match` |
| aosrd_2022_conference | Dr AJ. Farshchian Powerpoit — Farshchian | Pass1 `no_match` |
| aosrd_2022_conference | Fibromyalgia and Post covid CFS Rx -Practitioners- Osteopathy group-Jacob Teitelbaum — Teitelbaum | Pass1 `no_match` |
| aosrd_2022_conference | Insulin Resistance & Effects on Fertility AOSRD Mar 25 2022 — Marsh | Pass1 `no_match` |
| aosrd_2022_conference | KOS-Slide Show — O'Neil Smith | Pass1 `no_match` |
| aosrd_2022_conference | LIFESTYLE MEDICINE-Transforming Primary Care — Sundermann | Pass1 `no_match` |
| aosrd_2022_conference | Lecture, Hidden Epidemic, Las Vegas virtual, 3.26.2022-Levy — Levy | Pass1 `no_match` |
| aosrd_2022_conference | Lillo-Coronary Artery Calcium Scoring PPT for JLL of — Lillio | Pass1 `no_match` |
| aosrd_2022_conference | McCullough Presentation Pathophysiologic Rationale for Early Treatment of COVID-19 ND Jan 30 2022 — Peter McCullough | Pass1 `no_match` |
| aosrd_2022_conference | NAD Injection and IV Therapy-2 — Macheret | Pass1 `no_match` |
| aosrd_2022_conference | Nitric Oxide for the Prevention and Treatment of Cardiovascular DIsease with a Splash of Covid — Bryan | Pass1 `no_match` |
| aosrd_2022_conference | Opioid Use Disorder-D. Leszkovitz — Lezkowitz | Pass1 `no_match` |
| aosrd_2022_conference | Stellate Ganglion Harris Final — Harris | Pass1 `no_match` |
| aosrd_2022_conference | Ultrasound in Integrative Medicine-Dr. R. Badal — Badal | Pass1 `no_match` |
| aosrd_2022_conference | looking at rheumatic diseases_1-Speer — Speer | Pass1 `no_match` |
| aosrd_2022_conference | slide show2 — Faculty | Pass1 `no_match` |
| aosrd_webinars_youtube | A Better Cleaner You!! with Dr. Aunna Herbst – Video – 23-Dec-2025 | Pass1 `no_match` |
| aosrd_webinars_youtube | Advanced Laboratory Testing for Rheumatic Diseases – Tyler O’Malley | Pass1 `no_match` |
| aosrd_webinars_youtube | Ancient Healing Traditions for Modern Times – Video | Pass1 `no_match` |
| aosrd_webinars_youtube | Anti-Aging Medicine with Dr. Mikhail Berman (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Autism with Dr. Jenny Blanchard Stone – April 25, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Basic Hormone Replacement for Men Part 1 Student Session w MM (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Basic Hormone Replacement for Men Part 2 + Dr C’s Tips for Weight Loss (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Basic Hormone Replacement for Men Part 3 Finasteride, Lab Studies and Testosterone Replacement Dosin (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Behind the Scenes Thyroid Mechanisms with Dr. Brad Watts – April 4, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Biological Dentistry by Dr. Scott Chandler (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | BiomeFx GI Testing with Katherine Sumner, Microbiome Labs Nov 28, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Bioregulatory Medicine Applied to Fur Babies with Dr. Marlene Siegel – March 21, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Breaking Free-Financial Solutions for Medical Professionals with Mr. David Silva – March 5, 2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Brown adipose tissue is associated with cardiometabolic health 18-Jun-2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Build Your Own Personalized Nutritional  Formula from the Ground Up With Michael Lomis – Video | Pass1 `no_match` |
| aosrd_webinars_youtube | COVID 19 Pathology and Treatment S Halasa Dec 22, 2020 | Pass1 `no_match` |
| aosrd_webinars_youtube | Cardio Metabolic Assessment Testing with Ron Riewold, Joe Torres and Jane Santangelo – 9-Apr-2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Case Histories Show Casing the Power of Anti Aging Medicine | Pass1 `no_match` |
| aosrd_webinars_youtube | Chronic DIsease Management Kathleen ONeil Smith | Pass1 `no_match` |
| aosrd_webinars_youtube | Chronic Fatigue-Chronic Infections by Dr. Kalapana Patel 19 Oct 2021 | Pass1 `no_match` |
| aosrd_webinars_youtube | Clearfield – Non-Hormonal Remedies to Relieve Hormonal Symptoms – December, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Clinical applications of Amlexonax – June 6, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Covid 19 Management for the Vaccinated and Unvaccinated by Dr. Dan Stock | Pass1 `no_match` |
| aosrd_webinars_youtube | Dementia’s Dirty Dozen with Dr David Ajibade – Oct 31, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Depression by Dr. Ron Centric (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Dermatology Review: Top Ten Chronic Conditions (Part 1) by Dr. Mike Boehmer (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Discovering the Path to Health by Dr. Mark Lafferty (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Early Viral Treatment Post Pandemic Clinical Applications Roundtable (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Endocrinology of TBI-Part 2 with Dr. Willliam Clearfield – Sept 26, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Estrogen-Devil or Angel with Dr. Bill Clearfield (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Estrogen-Devil or Angel​ – Video – 8 Apr 2026 | Pass1 `no_match` |
| aosrd_webinars_youtube | Fascia Decompression for You, Your Patients and Your Fur Family – Aug 8, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Fascia, Pain Modulation and Autoimmunity by Kathleen O’Neil Smith, MD, December 7, 2021 | Pass1 `no_match` |
| aosrd_webinars_youtube | Female Hormone Primer Part 2 Student Session with MM (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Female Hormone Primer-Part 1 Student Session w MM (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Female Hormone Primer-Part 3 Polycystic Ovaries and Female Pattern Hair Loss (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Frequency Specific Microcurrent by Carol McMakin, MA,DC (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | From Assessment to Action-Comprehensive Strategies for Conquering High Cholesterol – 16-Apr-2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | From Chronic Illness to High Fit Patients with Jake Guidas – Video | Pass1 `no_match` |
| aosrd_webinars_youtube | From Marijuana to Mushroom-Are Plants and Fungi ‘Natural’ with Dr. Jeffrey Bock – Oct 17, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Fundamentals of Functional Medical Testing-Cell Science Systems with Amy Pieczarka RD – Aug 29, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Good and Bad Electromagnetic Fields Jami and Dr Rugerrio, November 23, 2021 | Pass1 `no_match` |
| aosrd_webinars_youtube | Gut-Brain Connection by Dr. Brad Watts (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Hashimoto’s Thyroiditis by Dr. Pam Smith. Date: 7/19/2022 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Homeopathic Case Studies with Dr Parvin Zarrin 2-Jul-2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Homeostasis Hormesis and Chemical Sensitivity by Dr. Kalapala Patel January 25, 2022 -Video | Pass1 `no_match` |
| aosrd_webinars_youtube | How to Choose the Best Stem Cell Sources for Your Practice with Dr. Joy Kong – Oct 3, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | How to Perform a Subcutaneous Injection (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | How to Perform an Intramuscular Injection (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Hypo and Hyperthyroidismare One Internal Disease with Two Different Manifestations by Dr. Parvin Zarrin – Video | Pass1 `no_match` |
| aosrd_webinars_youtube | Integrative Immunoncology | Pass1 `no_match` |
| aosrd_webinars_youtube | Integrative Medicine and the Law by Judge Egan Walker (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Integrative Psychiatry, Neurofeedback, and the Treatment Resistant Patient with Dr. John Finnick – December 6, 2022(Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Intermittent Fasting, Stimulating Brown Fat, and Weight Management with Dr Franco Calaveri – Oct 10, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Intervegrated Interventional Radiology by Dr. Brian Evans (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Introduction to Hormone Optimization-DHEA, Pregnenolone, Prolactin and Beginning Lab Evaluation – JR Student Session (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Introduction to Hormone Optimization-Par 1-Homeopathic Edition (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Introduction to Hormone Optimization-Part 3 Thyroid, Cortisol, Insulin, DHEA, Pregnenolone and Prolactin – 9-Apr-2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Introduction to Hormone Optimization-Part 4-Laboratory Evaluation JR Student Session (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Iron Metabolism and Sucrosomial Iron with Sam Sparhawk 23-Jul-2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Live Healthier, Better and Longer with Hydrogen by Bob Settineri – July 11, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Long Term Micronutrient Depletion with Dr. Deedra Mason – March 12, 2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Medical Cannibis for Chronic Pain-Hype or Reality by Dr. Mikhail Kogan (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Medical Intuition by Terri Jay  Aug 31, 2021 – Video | Pass1 `no_match` |
| aosrd_webinars_youtube | Micronutrients in Chronic Disease States by Dr. Kedar Prasad (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Mind-Mineral Connection with Kelli Hanson – Video – 19-Nov-2025 | Pass1 `no_match` |
| aosrd_webinars_youtube | Muscle Centric Health (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Muscle Testing with Dr. Clyde Porter (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | NCRPI Monthly AcupunctureIntegrative Medicine Webinar 1200-1300 ET – Video – 07-Nov-2025 | Pass1 `no_match` |
| aosrd_webinars_youtube | Natural Immunity via Homeopathic Medicine vs Artificial Immunity via Vaccination by Dr Parvin Zarrin, Aug 3, 2021 | Pass1 `no_match` |
| aosrd_webinars_youtube | Neuroinflammation-The Road to Neuropsychiatric Illness with Dr. Mark Gordon Nov 21, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | New Horizons in Cancer Treatment by Kalapana Patel, MD (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Osteopathic Manipulation in Treating Pain, and Substance Abuse – November 29, 2022(Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Perplexing Neuromuscular and GI Symptoms in a 27 Year Old Male with Dr. Kilee Smith 9-Jul-2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Peter Zebot-The Second Law of Human Nature  – Video | Pass1 `no_match` |
| aosrd_webinars_youtube | Pharmacology of Key Emerging Therapies in Chronic DIseases with Dr Mike Boehmer – July 25, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Physician Burnout-A Real Problem and a Way Forward by Dr. Yusuf Erskine (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Post Covid 19 Vaccination Syndrome | Pass1 `no_match` |
| aosrd_webinars_youtube | Prostate Community Trial Part 2 w Dr. KAthleen T. Ruddy and Stefan Hartmann PA-C – Aug 22, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Prostatitis and Prostate Cancer and IFM Iternational Conference Summary w Dr benoit Tano and Melvin Nario 4-Jun-2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Quantum Anti-Aging by Dr. Parvin Zarrin, December 21, 2021 | Pass1 `no_match` |
| aosrd_webinars_youtube | Quantum Cellular Medicine with David Konn – May 16, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Stress Devil or Angel by Dr Mikhail Berman (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Substance Abuse in OMT, PMR, and Pain Management Medicine with Dr. David Leszkovitz (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Sunshine, Light and Why EMF Protection is More than Skin Deep with Dan Stachofsky​ – Video – 25 March 2026 | Pass1 `no_match` |
| aosrd_webinars_youtube | The 14-3-3n Biomarker for Rheumatoid Arthritis Diagnosis, Prognosis, and Monitoring with Dr. Nima Mazinani – January 10, 2023(Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | The Benefits of Adding Safe, Regular, and Effective Corrective Exercise Therapy to Supplement Pharmacological and Homeopathic Remedies. – Dr. David Neuman – Dr. David Neuman | Pass1 `no_match` |
| aosrd_webinars_youtube | The Endocrinology of Autism-Condensed Version | Pass1 `no_match` |
| aosrd_webinars_youtube | The Future of Biological Dentistry: Where Do We Go from Here? with Dr. Scott Chandler (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | The Histology of Morgellons Nobody’s Talking About – Video | Pass1 `no_match` |
| aosrd_webinars_youtube | The Importance of the Upper Cervical Spine The Atlas Orthogonal Perspective by Dr. Dennis Harding (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | The Nuts and Bolts of Bioidentical Hormone Optimization-Part 1 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | The Nuts and Bolts of Bioidentical Hormone Optimization-Part 2 Hormones-Testoste (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | The Nuts and Bolts of Hormone Optimization-Putting It All Together-Part 3 Growth Hormone Thyroid a(Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | The Psychology of Success with Dr. Jim Naccarato – Video | Pass1 `no_match` |
| aosrd_webinars_youtube | The Role of Angiotensin-Converting Enzyme 2 in Sars-CoV 2 by Dr. Halasa | Pass1 `no_match` |
| aosrd_webinars_youtube | The Role of Nutrition and Prevention – December 20, 2022(Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | The Role of Oxalates in – Nov 14, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Twelve Days of Christmas-Twelve Medical Myths We Believed from Pediatrics to Adulthood 3-Dec-2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | US Canada Hormone Conference Progesterone (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Unlocking the Power of the Mind-Body Connection with Dr. Emmett Miller – Sept 12, 2023 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | Using Precision Psychiatry to Improve Mental Health with Dr. Mizyl Damayo – Jan 30, 2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | What I Learned from the Osteopathic Masters-Dr. William Richwine (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | When Syndromes Overlap-A Complex Case History of Hyperadrogenism, Multiple Autoimmune Maladies, and Evolving Metabolic Signals – Video | Pass1 `no_match` |
| aosrd_webinars_youtube | Why Vitamin C Therapy Works – Video | Pass1 `no_match` |
| aosrd_webinars_youtube | William Clearfield, DO – American Osteopathic Society of Integrative Medicine Lectures – Jan, 2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | William Clearfield, DO – Endocrinology of Psychiatric Illnesses – Jan, 2024 (Video) | Pass1 `no_match` |
| aosrd_webinars_youtube | “Low Dose Naltrexone” by Dr William Clearfield | Pass1 `no_match` |
| local_downloads | A Manual of Acupuncture (purple cover) | Pass1 `no_match` |
| local_downloads | Acupuncture resource | Pass1 `no_match` |
| local_downloads | Brain and Mycotoxins | Pass1 `no_match` |
| local_downloads | Colchicine uses | Pass1 `no_match` |
| local_downloads | Hair Follicle Optimization Master Research v0.2 | Pass1 `no_match` |
| local_downloads | Insomnia reference guide | Pass1 `no_match` |
| local_downloads | Integrative Immunology — Nutritional Cofactors / Carbon60 | Pass1 `no_match` |
| local_downloads | Integrative medicine lecture notes | Pass1 `no_match` |
| local_downloads | Low-dose colchicine — CV prevention / anti-inflammatory | Pass1 `no_match` |
| local_downloads | Overlap between Morgellons, Lyme disease, and syphilis | Pass1 `no_match` |
| local_downloads | Peptides BPC-157, KPV, and lorazotide — gut repair / barrier | Pass1 `no_match` |
| local_downloads | The hidden geography of acupuncture channels (audio) | Pass1 `no_match` |

## Ambiguities

1. **YouTube captions unknown:** player/timedtext metadata blocked (`LOGIN_REQUIRED` / empty timedtext list). Captions recorded as `not_checked`, not `captions_unavailable`.
2. **YouTube published date / duration:** not available via oEmbed; left blank / noted as not_checked.
3. **13 YouTube oEmbed 404s:** catalog URL present but video appears unavailable externally (may be private/removed).
4. **Rumble:** HTTP 403 from this audit host → `not_checked` (not scored unavailable).
5. **Vimeo captions:** page reachable; captions not verified → `not_checked`.
6. **Many-to-one / one-to-many:** Pass 1 multi-candidate Otter links preserved as semicolon-joined `otter_id` / `packet_dir`; identity not collapsed.
7. **Pass 1 possible/variant → relationship `possible_...` with `potentially_new_source_status=unclear`:** ambiguity retained.
8. **AOSRD 2022 / local-downloads:** no public stream/PDF URLs in catalogs; external public availability not applicable; binaries remain Pass 2 `claimed_present_elsewhere` on Mac/`/Volumes` paths.
9. **Shared PDF URLs:** 71 catalog rows reference PDF URLs; unique PDF URLs checked: fewer than row count when multiple lectures share a file.
10. **Catalog vs live title:** oEmbed titles may differ slightly from catalog titles; recorded in `youtube_title` without forcing identity changes.

## Acquisition Boundary

No external media was acquired during Pass 3.

No PDFs, videos, audio, captions, transcripts, slides, or images were downloaded for retention or processing.

## STOP

```
PASS 3 COMPLETE.
EXTERNAL AVAILABILITY AUDITED ONLY.
NO MEDIA DOWNLOADED.
NO MEDIA TRANSCRIBED.
NO MEDIA PROCESSED.
NO SOURCE PACKETS MODIFIED.
NO PASS 1 OR PASS 2 RECORDS MODIFIED.
```

## Outputs

- `Research/lectures/audit/external-representation-availability-pass-3.csv` (332 data rows)
- `Research/lectures/audit/external-representation-availability-pass-3.md` (this file)
