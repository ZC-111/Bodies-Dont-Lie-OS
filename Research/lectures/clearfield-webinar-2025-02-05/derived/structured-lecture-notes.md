# Structured Lecture Notes — Tuesday Integrative Health Webinar, February 5, 2025

**Event:** Clearfield Training Program — Tuesday Integrative Health Webinar  
**Date:** February 5, 2025 | **Duration:** 2h 1m  
**Host:** Bill Clearfield, DO  
**Key Speaker:** Evangelica Papasterio, PhD (molecular biology; Nice / Paris, France)  
**Panelists:** Benoit Tano, Dr. Quinn, Melvin Nario, Dr. Halasa, Dr. Joseph James, Dr. Patel, Robert Fortier-Beaulieu (chat)

---

## Segment 1 — Openers & Research-Group Update (00:00–14:48)

**Speakers:** Bill Clearfield, Evangelica Papasterio (Speaker 1), Dr. Quinn (Speaker 3), Benoit Tano

### Key Points
- Guest presenting live from Paris at ~3 AM; atypical webinar topic (ocular oncology vs usual anti-aging/wellness)
- Clearfield introduces fiancée’s niece: newly minted PhD (Nov 2024), UniCA / Centre Méditerranéen, Nice; deep-tech entrepreneurship diploma; Nucleate France advisor
- **Research-group update (Dr. Quinn):** Anthony James / NAIC tribal education entity; First Nations Medical Board umbrella; practitioners/clinics need not be on reservation; Dr. Dimitri certified tribal healing; recommended text *American Indian Medicine*
- Clearfield parks tribal/regulatory discussion for end of call to protect lecture time

### Clinical Relevance
- Program expanding into rare-disease oncology and international research collaboration
- Tribal certification / First Nations Medical Board framed as practice-protection pathway (not IHS)

---

## Segment 2 — Uveal Melanoma Foundations (17:38–~35:00)

**Speaker:** Evangelica Papasterio, PhD

### ★ Core Thesis
> Uveal melanoma (UM) is **not** cutaneous melanoma with a different address — genetics, metastasis pattern, and therapy response are fundamentally different. Primary disease can be locally controlled; **metastatic disease still lacks a therapy that works for most patients**.

### 2A. Anatomy & Disease Definition
- Eye layers: fibrous sclera → **uveal tract** (iris, ciliary body, choroid) → neural retina
- Melanocytes in uveal tract → **uveal melanoma** (vs epidermal melanocytes → cutaneous melanoma)
- Melanin pathway reminder: tyrosinase → dopaquinone → eumelanin / pheomelanin

### 2B. Cutaneous vs Uveal Melanoma
| Dimension | Cutaneous | Uveal |
|---|---|---|
| Classic drivers | BRAF, NRAS | **GNAQ, GNA11** (mutually exclusive); also CYSLTR2, PLCB4/PLCB3 |
| Mutational burden | Often high | **Very low** |
| Therapy gains (targeted / IO) | Substantial recent progress | **Highly unresponsive** to agents that help cutaneous disease |
| Metastasis | Variable | ~50% → primarily **liver**; 80–90% die within ~1 year once metastatic |

### 2C. Epidemiology & Risk
- Most common primary intraocular malignancy in adults
- **3–5%** of all melanomas; incidence **5–7 per million/year** (US/Europe stats presented)
- Incidence rises **south → north latitude** → argues UV is **not** the main driver (unlike cutaneous)
- Risk factors cited: light-colored eyes, fair skin (not light hair), older age (~mean diagnosis **60**, peak **65**), atypical uveal nevi, congenital ocular melanocytosis, BAP1 predisposition syndrome; xeroderma pigmentosum weak association; familial rare
- UV signature association reported mainly for **iris** melanoma subset (Shields / related literature) — association ≠ primary cause

### 2D. Why Study a “Rare” Cancer?
1. Humanitarian: every patient deserves care
2. Affects last third of lifespan (~80y expectancy; diagnosis ~60)
3. Metastatic lethality: ~50% metastasize; rapid death after liver mets
4. Collective orphan burden: **3.5–7%** worldwide ≈ **300–500 million** people

### 2E. Primary Site & Molecular Stratification
- **~90%** choroidal; remaining ~10% ciliary body + iris
- Initiators: activating **GNAQ / GNA11** (etc.), mutually exclusive
- Progressors: **BAP1 loss**, translation initiation / splicing factors (also mutually exclusive) — strongly predictive of metastasis
- High metastatic risk example: **monosomy 3 + BAP1 loss**
- Lower risk patterns: disomy 3; EIF1AX or SF3B1-type alterations (as presented)
- **PRAME** expression upshifts metastatic class within prognostic clusters
- Clinical tool: **DecisionDx-UM** (Castle Biosciences) — 15-gene signature → Class 1 / 2 risk strata; can add PRAME etc.

### 2F. Signaling & Current Care
- Downstream axes: MAPK (proliferation), PI3K–Akt (growth/survival), Rho-GDP (cytoskeleton), ARF6 as GNAQ proximal node; emerging **LKB1–SIK2** axis
- Pathway inhibitors (trametinib, etc.) often work **in vitro**, fail to translate clinically
- Primary UM: radiotherapy (plaque brachytherapy, proton beam) or surgery (local resection / enucleation); trend toward **globe-preserving** care
- Metastatic UM: **no standard of care** for all patients; many Phase 1–3 trials (targeted, IO, vaccines, antibodies)
- **Tebentafusp (Kimmtrak, 2021):** bispecific fusion protein linking gp100+ UM cells to CD3+ T cells → OS benefit, attenuates over 3-year follow-up; requires specific **HLA** allele → presenter cited **~9%** eligible/responsive pool → ~90% of metastatic patients still without a global therapy

---

## Segment 3 — CRISPR Kinome Screen → LKB1 / SIK2 / SLC8A1 / ROS Axis (35:42–~52:00)

**Speaker:** Evangelica Papasterio (lab work published *EMBO Molecular Medicine* 2023; conducted prior to her arrival / presented as lab example)

### Research Strategy
- Human primary + metastatic UM cell lines spanning mutation diversity
- **Dropout genome CRISPR-Cas9 kinome screen** (negative selection): knockouts that drop out = genes needed for proliferation/survival
- Library: Brunello human kinome (~**760 kinases**); NGS + MAGeCK-style bioinformatics
- Rationale for kinome: conserved active sites → “druggable”; kinase drugs often repurposable; MAPK activation common in UM

### Causal Cascade (validated)
```
LKB1 loss  →  SIK2 loss/dysregulation  →  ↑ SLC8A1  →  Ca²⁺ addiction + ↑ mitochondrial ROS
                                                              ↓
                                              proliferation / survival advantage
```

### Key Experimental Logic
- LKB1 loss ↑ proliferation (Western + assays); **rescue**: WT LKB1 restores; kinase-dead does not
- Xenografts: LKB1-KO tumors grow larger than WT
- Transcriptomics + GSEA → calcium metabolism hub; top hit **SLC8A1** (NCX / solute carrier family 8 member 1)
- SLC8A1 silencing in LKB1-KO context reverses proliferative gain (partial control)
- SIK2 is the LKB1 downstream hit that tracks in the same direction; SIK2 restores SLC8A1 regulation
- **Therapeutic suggestion (preclinical):** co-target **SLC8A1** (e.g. KB-R7943) + **mitochondrial ROS** (e.g. **MitoQ**) → apoptosis shift in flow cytometry; combination shrinks LKB1-KO xenografts more than either alone
- Presenter caution: many steps remain before clinical recommendation; LKB1 is a **tumor suppressor** — loss drives worse phenotype

### Presenter’s Own PhD Work (unpublished at talk)
- ~**70–80%** reduction in proliferative capacity
- ~**60%** reduction in Transwell / Boyden chamber migration (metastasis model)
- Still **preclinical** mechanism characterization — not clinical trials

---

## Segment 4 — Biotech Entrepreneurship for Rare Cancers (52:00–1:03:49)

**Speaker:** Evangelica Papasterio

### Challenge Map
| Scientific | Financial / Regulatory |
|---|---|
| Sparse models (cell lines, PDX, immunocompetent mice) | Limited non-dilutive funding / awareness |
| Tiny patient population → hard trial design | Pricing & reimbursement complexity |
| Genetic diversity across geographies | Dense regulation |

### Solution Levers Cited
- Academic shared resources; rare-disease consortia + AI on large datasets
- Adaptive trial designs; global collaborations (need research maturity)
- Orphan designation (FDA / EMA): fee relief, exclusivity
- Mission-driven investors; incubators/accelerators; education campaigns

### Case Study: Roca Therapeutics (Nice)
- First-in-class small-molecule pipeline for metastatic UM (e.g. **RCT-001** oral inhibitor targeting angiogenesis/inflammation axis)
- Expansion interest: other ocular disease (e.g. neovascular glaucoma)
- Model workarounds: zebrafish, chick embryo when no good immunocompetent UM mouse
- Trial strategy tradeoff: UM-only (slow, specific) vs basket including other cancers (faster, noisier)
- France advantage: specialized UM centers (Paris + Nice / Saint-Antoine–La-Casagne cited)
- Exit framing: develop → sell to Big Pharma; keep growing pipeline
- Hardest challenge quoted: **ethical** — families asking “when will the drug be ready?”

### Closing Frame
> Rare diseases are collectively common. “From a few to more… until we have precision cures for all.” — Anna Greka TEDx (quoted)

---

## Segment 5 — Clinical Case & Integrative Q&A (1:03:49–~1:45:00)

**Speakers:** Clearfield, Papasterio, Tano, Nario, Halasa, Joseph James, Patel, chat contributors

### Live Case Context (Halasa / James / Patel)
- Patient with UM: blue eyes; **HLA-A positive** for tebentafusp eligibility discussion
- Plan discussed: Kimmtrak ± **nanoparticle loading** for targeting; polyphenols; **photodynamic therapy** (indocyanine green + methylene blue; IR/red activation)
- James: no metastasis at ~8–9 months into care; CEA normalized; considering Losartan eye drops for scar; wondering if residual mass = scar
- Patel: some patients keep globe 10+ years without enucleation — may map to lower-risk molecular class (e.g. without BAP1 loss); biopsy often refused
- Halasa: CTCs / RGCC useful adjuncts but **clinical presentation trumps CTC counts**; melanoma lacks specific classic serum markers; inflammatory markers nonspecific

### Research ↔ Clinic Bridging Points
- Papasterio: not a clinician — will connect group to lab ophthalmologist-PhD in Nice; recommends **DecisionDx-UM** for risk stratification
- Vitamin D / melatonin / pollution / telomerase: **not** part of her UM datasets; cutaneous ≠ uveal for vitamin D conference anecdotes
- Chat (Fortier-Beaulieu): vitamin D receptor hydroxylases CYP27B1, CYP24A1 + retinoid-related orphan receptors linked to UM literature
- Nario: **MitoQ** synergy with SLC8A1 inhibition is clinically interesting because RGCC can screen natural compounds; telomere shortening as general cancer risk (not UM-specific publication known to speaker)
- Nario: “superior oligonucleotide therapy” / SOT as mRNA-style cancer vaccine concept (RGCC-adjacent) — compared loosely to CRISPR precision
- Halasa: explore **repurposing** FDA-approved Ca-channel blockers (nifedipine, verapamil) given Ca addiction phenotype; nanotech (cyclodextrin nanoparticles) to spare healthy tissue
- Papasterio: Ca addiction mechanism **not** proven as classical channelopathy in the presented paper; her July 2024 trial table review did not show completed CCB trials for UM

### Actionable Clinic Takeaways from Discussion
- Use molecular risk tools (DecisionDx-UM / BAP1 / chr3) when tissue available
- Tebentafusp only if HLA-matched
- Do not over-interpret CEA / CTCs for melanoma management
- Drug-repurposing + nano-delivery = integrative oncology research agenda, still investigational
- Collaboration invite: Monday Halasa webinar + Nice clinician-scientist

---

## Segment 6 — Closers (late)

**Speakers:** Bill Clearfield, panel

### Key Points
- Gratitude for 3 AM Paris presentation; international collaboration enthusiasm
- Next week: **Allison Beasley** — light therapy (UV / red / blue)
- Chat nudge: look at AMPK, SIK2, vitamin D axes further
- Motivational interviewing aside from panel; cultural anecdotes; LinkedIn networking for follow-up

---

*Structured from Otter transcript + summary. ASR corrections applied (uveal melanoma, GNAQ/GNA11, BAP1, LKB1–SIK2–SLC8A1, tebentafusp/Kimmtrak, DecisionDx-UM, MitoQ, KB-R7943).*
