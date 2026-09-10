# Pass 4.5 Evidence Resolution — Authorization Log (PDF MVP)

- Generated: 2026-09-10T21:31:12Z
- Batch: Pass 4 `AOSRD_PDF` ∩ (`ACQUIRE_CANDIDATE` ∪ `CONDITIONAL_ACQUIRE`)
- ERC count: 66
- Status: **pending human authorization** (no downloads performed)
- Epistemic ceiling (proposed): `bytes_in_custody` + `explicitly_not_session_identity` + `explicitly_not_knowledge_object`

## Decision matrix (this batch)

| decision | count |
|---|---:|
| NEEDS_HUMAN_SCOPING (pending gate) | 66 |
| AUTHORIZE_ACTION | 0 |
| DENY_ACTION | 0 |
| DEFER | 0 |
| NO_ACTION | 0 |

## Purpose breakdown

| evidence_purpose | count |
|---|---:|
| identity_resolution | 35 |
| unlinked_source_investigation | 28 |
| representation_enrichment | 3 |

## Pending authorization inventory

Each item below requires a human decision before any `DOWNLOAD_PDF` side effect.

### erc-4.5-pdf-001-aosrd-webinars-008-w5yTm2FVNFg

- **Title:** Ancient Healing Traditions for Modern Times – Video
- **Catalog id:** `aosrd-webinars-008-w5yTm2FVNFg`
- **Pass4 row id:** `aosrd-webinars-008-w5yTm2FVNFg::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2026/06/Ancient-Wisdom-Modern-Healing1.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Ancient Healing Traditions for Modern Times – Video” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/w5yTm2FVNFg|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-002-aosrd-webinars-071-zKxcCQelKT4

- **Title:** Culinary Oncology with Chef Laura Pole 04-Mar-2025 (Video)
- **Catalog id:** `aosrd-webinars-071-zKxcCQelKT4`
- **Pass4 row id:** `aosrd-webinars-071-zKxcCQelKT4::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2025/03/Culinary-Translation_slide-handout_2.pdf
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `0pIRZSR5hLU8vZNbqCJ9pLpRE9M`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Culinary Oncology with Chef Laura Pole 04-Mar-2025 (Video)” belong to Pass-1 possible Otter candidate(s) [0pIRZSR5hLU8vZNbqCJ9pLpRE9M], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/zKxcCQelKT4|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-003-aosrd-webinars-089-YGd1siNfdVc

- **Title:** EMF and Depletion of Nitric Oxide with Beth Shirley 8-Oct-2024 (Video)
- **Catalog id:** `aosrd-webinars-089-YGd1siNfdVc`
- **Pass4 row id:** `aosrd-webinars-089-YGd1siNfdVc::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2024/10/EMF-2024.pdf
- **Pass1 class (frozen):** `strong`
- **Candidates (multiplicity=2):** `EqC6yd4bQDKMl2mpzPURPZu-_Pc;FbRyr7EkkewAoPTmXbK9DtUiA_Y`
- **Uncertainty:** `representation_uncertainty`
- **Purpose:** `representation_enrichment`
- **Evidence question:** Does AOSRD PDF for “EMF and Depletion of Nitric Oxide with Beth Shirley 8-Oct-2024 (Video)” add slide/figure/reference material not present as local images for Otter session EqC6yd4bQDKMl2mpzPURPZu-_Pc, without changing session identity?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/YGd1siNfdVc|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-004-aosrd-webinars-091-EC0ajS7U0yQ

- **Title:** Drug Induced Nutrient Depletion with Dr. Harlan Bieley 24-Sep-2024 (Video)
- **Catalog id:** `aosrd-webinars-091-EC0ajS7U0yQ`
- **Pass4 row id:** `aosrd-webinars-091-EC0ajS7U0yQ::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2024/09/Powerpoint-Drug-induced-Nutrient-Depletion-3-11-23.pptx.pdf
- **Pass1 class (frozen):** `strong`
- **Candidates (multiplicity=1):** `FbRyr7EkkewAoPTmXbK9DtUiA_Y`
- **Uncertainty:** `representation_uncertainty`
- **Purpose:** `representation_enrichment`
- **Evidence question:** Does AOSRD PDF for “Drug Induced Nutrient Depletion with Dr. Harlan Bieley 24-Sep-2024 (Video)” add slide/figure/reference material not present as local images for Otter session FbRyr7EkkewAoPTmXbK9DtUiA_Y, without changing session identity?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/EC0ajS7U0yQ|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-005-aosrd-webinars-095-DiZKcMJiLs8

- **Title:** Pushing the Limits-From Ultra-Endurance to Revolutionary Patient Care with Lisa Tamati 27-Aug-2024 (Video)
- **Catalog id:** `aosrd-webinars-095-DiZKcMJiLs8`
- **Pass4 row id:** `aosrd-webinars-095-DiZKcMJiLs8::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2024/08/Speaking-Engagement-Osteopathic-Conference.pdf
- **Pass1 class (frozen):** `strong`
- **Candidates (multiplicity=4):** `pw9yXaKVUW0ETXgSRTRBaLEzqQc;4qg44PRw27Y2Jbzl7MXMYCX0HuI;y59a2fEx8UgOiThJHr1w-HcQc1U;wcHy9pPXoWy5S62-GJbpasQtw2o`
- **Uncertainty:** `representation_uncertainty`
- **Purpose:** `representation_enrichment`
- **Evidence question:** Does AOSRD PDF for “Pushing the Limits-From Ultra-Endurance to Revolutionary Patient Care with Lisa Tamati 27-Aug-2024 (Video)” add slide/figure/reference material not present as local images for Otter session pw9yXaKVUW0ETXgSRTRBaLEzqQc, without changing session identity?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/DiZKcMJiLs8|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=4; preserve all candidates; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-006-aosrd-webinars-141-sqvJDTzrtDc

- **Title:** Neuroinflammation-The Road to Neuropsychiatric Illness with Dr. Mark Gordon Nov 21, 2023 (Video)
- **Catalog id:** `aosrd-webinars-141-sqvJDTzrtDc`
- **Pass4 row id:** `aosrd-webinars-141-sqvJDTzrtDc::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2023/11/Neuroinflammation-the-road-to-Neuropsychiatric-Illnesses-with-Dr.-Mark-Gordon.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Neuroinflammation-The Road to Neuropsychiatric Illness with Dr. Mark Gordon Nov 21, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/sqvJDTzrtDc|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-007-aosrd-webinars-152-rAUra-Qha5M

- **Title:** Dementia’s Dirty Dozen with Dr David Ajibade – Oct 31, 2023 (Video)
- **Catalog id:** `aosrd-webinars-152-rAUra-Qha5M`
- **Pass4 row id:** `aosrd-webinars-152-rAUra-Qha5M::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/dementias-dirty-dozen-with-dr-david-ajibade/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Dementia’s Dirty Dozen with Dr David Ajibade – Oct 31, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/rAUra-Qha5M|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-008-aosrd-webinars-153-xF0qI-tdmWo

- **Title:** Another View of the Endocannabinoid System with Dr. Robert Quinn – Oct 24, 2023 (Video)
- **Catalog id:** `aosrd-webinars-153-xF0qI-tdmWo`
- **Pass4 row id:** `aosrd-webinars-153-xF0qI-tdmWo::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/another-view-of-the-endocannabinoid-system-with-dr-robert-quinn/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `tAtmhIMa7fmRXEWqsjZP4Gl7vkM`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Another View of the Endocannabinoid System with Dr. Robert Quinn – Oct 24, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [tAtmhIMa7fmRXEWqsjZP4Gl7vkM], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/xF0qI-tdmWo|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-009-aosrd-webinars-154-S62qYOwRkRs

- **Title:** From Marijuana to Mushroom-Are Plants and Fungi ‘Natural’ with Dr. Jeffrey Bock – Oct 17, 2023 (Video)
- **Catalog id:** `aosrd-webinars-154-S62qYOwRkRs`
- **Pass4 row id:** `aosrd-webinars-154-S62qYOwRkRs::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/from-marijuana-to-mushroom-are-plants-and-fungi-natural-with-dr-jeffrey-bock/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “From Marijuana to Mushroom-Are Plants and Fungi ‘Natural’ with Dr. Jeffrey Bock – Oct 17, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/S62qYOwRkRs|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-010-aosrd-webinars-155-acTTjJWf9rk

- **Title:** Intermittent Fasting, Stimulating Brown Fat, and Weight Management with Dr Franco Calaveri – Oct 10, 2023 (Video)
- **Catalog id:** `aosrd-webinars-155-acTTjJWf9rk`
- **Pass4 row id:** `aosrd-webinars-155-acTTjJWf9rk::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/intermittent-fasting-stimulating-brown-fat-and-weight-management-with-dr-francisco-calaveri/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Intermittent Fasting, Stimulating Brown Fat, and Weight Management with Dr Franco Calaveri – Oct 10, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/acTTjJWf9rk|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-011-aosrd-webinars-156-rNvF48yMEag

- **Title:** How to Choose the Best Stem Cell Sources for Your Practice with Dr. Joy Kong – Oct 3, 2023 (Video)
- **Catalog id:** `aosrd-webinars-156-rNvF48yMEag`
- **Pass4 row id:** `aosrd-webinars-156-rNvF48yMEag::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/how-to-choose-the-best-stem-cell-sources-for-your-practice-with-dr-joy-kong/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “How to Choose the Best Stem Cell Sources for Your Practice with Dr. Joy Kong – Oct 3, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/rNvF48yMEag|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-012-aosrd-webinars-158-BcMb7ZimIEo

- **Title:** Ivermectin Feeds Bifidobacterium to Boost Immumity with Dr. Salaheldin Halasa – Sept 19, 2023 (Video)
- **Catalog id:** `aosrd-webinars-158-BcMb7ZimIEo`
- **Pass4 row id:** `aosrd-webinars-158-BcMb7ZimIEo::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/ivermectin-feeds-bifidobactedium-to-boost-immunity/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `b2H7gyjRNmbN0l62XtCzeLPovDE;xg4V_A-L8_Ob1jKGBewDTtKzOWg`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Ivermectin Feeds Bifidobacterium to Boost Immumity with Dr. Salaheldin Halasa – Sept 19, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [b2H7gyjRNmbN0l62XtCzeLPovDE, xg4V_A-L8_Ob1jKGBewDTtKzOWg], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/BcMb7ZimIEo|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-013-aosrd-webinars-159-5DmzZRupogw

- **Title:** Unlocking the Power of the Mind-Body Connection with Dr. Emmett Miller – Sept 12, 2023 (Video)
- **Catalog id:** `aosrd-webinars-159-5DmzZRupogw`
- **Pass4 row id:** `aosrd-webinars-159-5DmzZRupogw::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/unlocking-the-power-of-the-mind-body-connection-with-dr-emmett-miller/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Unlocking the Power of the Mind-Body Connection with Dr. Emmett Miller – Sept 12, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/5DmzZRupogw|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-014-aosrd-webinars-163--JGUhnhLGrQ

- **Title:** Nutritional Excellence-The Kohana Approach to Optimal Health with Dr Rober Quinn – Aug 15, 2023 (Video)
- **Catalog id:** `aosrd-webinars-163--JGUhnhLGrQ`
- **Pass4 row id:** `aosrd-webinars-163--JGUhnhLGrQ::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/nutritional-excellence-the-kohana-approach-to-optimal-health-with-dr-rober-quinn/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `CQdkPoyCm_xx7nnZ2b80AClK8TM`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Nutritional Excellence-The Kohana Approach to Optimal Health with Dr Rober Quinn – Aug 15, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [CQdkPoyCm_xx7nnZ2b80AClK8TM], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/-JGUhnhLGrQ|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-015-aosrd-webinars-166-RM39JRpthTg

- **Title:** Pharmacology of Key Emerging Therapies in Chronic DIseases with Dr Mike Boehmer – July 25, 2023 (Video)
- **Catalog id:** `aosrd-webinars-166-RM39JRpthTg`
- **Pass4 row id:** `aosrd-webinars-166-RM39JRpthTg::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2023/07/Pharmacology-of-Emerging-Therapies-in-Chronic-Disease-Management-2023.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Pharmacology of Key Emerging Therapies in Chronic DIseases with Dr Mike Boehmer – July 25, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/RM39JRpthTg|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-016-aosrd-webinars-169-xIY-4j04zh0

- **Title:** Live Healthier, Better and Longer with Hydrogen by Bob Settineri – July 11, 2023 (Video)
- **Catalog id:** `aosrd-webinars-169-xIY-4j04zh0`
- **Pass4 row id:** `aosrd-webinars-169-xIY-4j04zh0::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/live-healthier-better-and-longer-with-hydrogen-by-bob-settineri/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Live Healthier, Better and Longer with Hydrogen by Bob Settineri – July 11, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/xIY-4j04zh0|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-017-aosrd-webinars-170-hj4CXKqCtkg

- **Title:** The Incretin Hormones and the New Face of Weight Loss with Dr. William Clearfield – June 28, 2023 (Video)
- **Catalog id:** `aosrd-webinars-170-hj4CXKqCtkg`
- **Pass4 row id:** `aosrd-webinars-170-hj4CXKqCtkg::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/the-incretin-hormones-and-the-new-face-of-weight-loss-with-dr-william-clearfield/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `5HPCyqwQxi9QD1of8g-CPHrnFcc`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “The Incretin Hormones and the New Face of Weight Loss with Dr. William Clearfield – June 28, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [5HPCyqwQxi9QD1of8g-CPHrnFcc], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/hj4CXKqCtkg|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-018-aosrd-webinars-171-wSFbd7D8Lpw

- **Title:** Integrative Imunity-Part 2 Dr. Benoit Tano – June 27, 2023 (Video)
- **Catalog id:** `aosrd-webinars-171-wSFbd7D8Lpw`
- **Pass4 row id:** `aosrd-webinars-171-wSFbd7D8Lpw::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/integrative-imunity-part-2-dr-benoit-tano/
- **Pass1 class (frozen):** `variant_derivative`
- **Candidates (multiplicity=5):** `81vgkJ55QnsvesXbnyxCMQPr6Rc;wcHy9pPXoWy5S62-GJbpasQtw2o;vn-MouyIRCM7VjShKYhDQr6Mc3U;JAhRYbDDwDsC4em3dazDKyDw4gM;TNvBcRwwSnrkWGe2_L3i3lGvYYk`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Integrative Imunity-Part 2 Dr. Benoit Tano – June 27, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [81vgkJ55QnsvesXbnyxCMQPr6Rc, wcHy9pPXoWy5S62-GJbpasQtw2o, vn-MouyIRCM7VjShKYhDQr6Mc3U, JAhRYbDDwDsC4em3dazDKyDw4gM, TNvBcRwwSnrkWGe2_L3i3lGvYYk], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/wSFbd7D8Lpw|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=5; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-019-aosrd-webinars-172-aPPCKg2l-eQ

- **Title:** Introduction to Peptides with Dr. Jay Campbell – June 20, 2023 (Video)
- **Catalog id:** `aosrd-webinars-172-aPPCKg2l-eQ`
- **Pass4 row id:** `aosrd-webinars-172-aPPCKg2l-eQ::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/everything-you-ever-wanted-to-peptides-with-dr-jay-campbell/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `t9O9J5vUpWGkKXi-5TqxgKudSvY`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Introduction to Peptides with Dr. Jay Campbell – June 20, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [t9O9J5vUpWGkKXi-5TqxgKudSvY], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/aPPCKg2l-eQ|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-020-aosrd-webinars-173-yAA5qJFYPgg

- **Title:** The Importance of Polysaccharides for Brain Health and Immune Function with Dr. John E. Lewis – June 13, 2023 (Video)
- **Catalog id:** `aosrd-webinars-173-yAA5qJFYPgg`
- **Pass4 row id:** `aosrd-webinars-173-yAA5qJFYPgg::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/the-importance-of-polysacchari-unction-with-dr-john-e-lewis/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `y59a2fEx8UgOiThJHr1w-HcQc1U`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “The Importance of Polysaccharides for Brain Health and Immune Function with Dr. John E. Lewis – June 13, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [y59a2fEx8UgOiThJHr1w-HcQc1U], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/yAA5qJFYPgg|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-021-aosrd-webinars-174-LcK7emnFeVk

- **Title:** Clinical applications of Amlexonax – June 6, 2023 (Video)
- **Catalog id:** `aosrd-webinars-174-LcK7emnFeVk`
- **Pass4 row id:** `aosrd-webinars-174-LcK7emnFeVk::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/clinical-applications-of-amlexonax/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Clinical applications of Amlexonax – June 6, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/LcK7emnFeVk|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-022-aosrd-webinars-175-wTPrdOyALx0

- **Title:** Ehlers Danlos Syndrome Treated with Frequency Specific Microcurrant by Dr. Carol McMakin – May 30, 2023 (Video)
- **Catalog id:** `aosrd-webinars-175-wTPrdOyALx0`
- **Pass4 row id:** `aosrd-webinars-175-wTPrdOyALx0::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/ehlers-danlos-syndrome-treated-with-frequency-specific-microcurrant-by-dr-carol-mcmakin/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `vZKE66zexBS6KPliMMq0glRxefk`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Ehlers Danlos Syndrome Treated with Frequency Specific Microcurrant by Dr. Carol McMakin – May 30, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [vZKE66zexBS6KPliMMq0glRxefk], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/wTPrdOyALx0|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-023-aosrd-webinars-178-D7o1Fdgy42o

- **Title:** Cannabis 101 with Dr. Kent Crowley – May 9, 2023 (Video)
- **Catalog id:** `aosrd-webinars-178-D7o1Fdgy42o`
- **Pass4 row id:** `aosrd-webinars-178-D7o1Fdgy42o::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/cannabis-101-with-dr-kent-crowley/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `KPtFIYDuvg1p0CbfNkYIuOVkwIE`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Cannabis 101 with Dr. Kent Crowley – May 9, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [KPtFIYDuvg1p0CbfNkYIuOVkwIE], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/D7o1Fdgy42o|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-024-aosrd-webinars-179-9suZ_6zVHEM

- **Title:** Methylene Blue with Dr. Bill Clearfield – May 8, 2023 (Video)
- **Catalog id:** `aosrd-webinars-179-9suZ_6zVHEM`
- **Pass4 row id:** `aosrd-webinars-179-9suZ_6zVHEM::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/methylene-blue-with-dr-bill-clearfield/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `wcHy9pPXoWy5S62-GJbpasQtw2o;JAhRYbDDwDsC4em3dazDKyDw4gM`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Methylene Blue with Dr. Bill Clearfield – May 8, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [wcHy9pPXoWy5S62-GJbpasQtw2o, JAhRYbDDwDsC4em3dazDKyDw4gM], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/9suZ_6zVHEM|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-025-aosrd-webinars-180-XS22Ub34U-o

- **Title:** Autism with Dr. Jenny Blanchard Stone – April 25, 2023 (Video)
- **Catalog id:** `aosrd-webinars-180-XS22Ub34U-o`
- **Pass4 row id:** `aosrd-webinars-180-XS22Ub34U-o::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/autism-with-dr-jenny-blanchard-stone/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Autism with Dr. Jenny Blanchard Stone – April 25, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/XS22Ub34U-o|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-026-aosrd-webinars-182-FsuYMzPyjWE

- **Title:** The New Face of Weight Loss with Dr. Bill Clearfield – April 11, 2023 (Video)
- **Catalog id:** `aosrd-webinars-182-FsuYMzPyjWE`
- **Pass4 row id:** `aosrd-webinars-182-FsuYMzPyjWE::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/the-new-face-of-weight-loss-with-dr-bill-clearfield/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `5HPCyqwQxi9QD1of8g-CPHrnFcc`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “The New Face of Weight Loss with Dr. Bill Clearfield – April 11, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [5HPCyqwQxi9QD1of8g-CPHrnFcc], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/FsuYMzPyjWE|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-027-aosrd-webinars-183-CW3op9BkNI8

- **Title:** Behind the Scenes Thyroid Mechanisms with Dr. Brad Watts – April 4, 2023 (Video)
- **Catalog id:** `aosrd-webinars-183-CW3op9BkNI8`
- **Pass4 row id:** `aosrd-webinars-183-CW3op9BkNI8::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/behind-the-scenes-thyroid-mechanisms-with-dr-brad-watts/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Behind the Scenes Thyroid Mechanisms with Dr. Brad Watts – April 4, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/CW3op9BkNI8|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-028-aosrd-webinars-184-4nZN4zvp_Uk

- **Title:** Bioregulatory Medicine Applied to Fur Babies with Dr. Marlene Siegel – March 21, 2023 (Video)
- **Catalog id:** `aosrd-webinars-184-4nZN4zvp_Uk`
- **Pass4 row id:** `aosrd-webinars-184-4nZN4zvp_Uk::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/bioregulatory-medicine-applied-to-fur-babies-with-dr-marlene-siegel/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Bioregulatory Medicine Applied to Fur Babies with Dr. Marlene Siegel – March 21, 2023 (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/4nZN4zvp_Uk|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-029-aosrd-webinars-185-AZvxTJWqeBA

- **Title:** Glutathione Update with Dr. Nayan Patel – March 14, 2023 (Video)
- **Catalog id:** `aosrd-webinars-185-AZvxTJWqeBA`
- **Pass4 row id:** `aosrd-webinars-185-AZvxTJWqeBA::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/glutathione-update-with-dr-nayan-patel/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `JAhRYbDDwDsC4em3dazDKyDw4gM`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Glutathione Update with Dr. Nayan Patel – March 14, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [JAhRYbDDwDsC4em3dazDKyDw4gM], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/AZvxTJWqeBA|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-030-aosrd-webinars-186-hUswEBL-LBc

- **Title:** Muscle Centric Medicine -Principles of Exercise Science with Stefan Hartmann PA – March 7, 2023 (Video)
- **Catalog id:** `aosrd-webinars-186-hUswEBL-LBc`
- **Pass4 row id:** `aosrd-webinars-186-hUswEBL-LBc::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/update-on-glutathione-therapy-with-dr-nayan-patel/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=4):** `CQjlfnZLZ-CY25UUEq35pSQ0lug;H1Iomsee4ZUONKKezPDcMBYCvQ0;TNvBcRwwSnrkWGe2_L3i3lGvYYk;ykfPBSHSL3meBk4yGojbTxMVIpA`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Muscle Centric Medicine -Principles of Exercise Science with Stefan Hartmann PA – March 7, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [CQjlfnZLZ-CY25UUEq35pSQ0lug, H1Iomsee4ZUONKKezPDcMBYCvQ0, TNvBcRwwSnrkWGe2_L3i3lGvYYk, ykfPBSHSL3meBk4yGojbTxMVIpA], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/hUswEBL-LBc|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=4; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-031-aosrd-webinars-189-bMobTwHmWhM

- **Title:** Integrative Immunology with Dr. Benoit Tano – February 14, 2023 (Video)
- **Catalog id:** `aosrd-webinars-189-bMobTwHmWhM`
- **Pass4 row id:** `aosrd-webinars-189-bMobTwHmWhM::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/integrative-immunology-with-dr-benoit-tano/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=3):** `81vgkJ55QnsvesXbnyxCMQPr6Rc;wcHy9pPXoWy5S62-GJbpasQtw2o;JAhRYbDDwDsC4em3dazDKyDw4gM`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Integrative Immunology with Dr. Benoit Tano – February 14, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [81vgkJ55QnsvesXbnyxCMQPr6Rc, wcHy9pPXoWy5S62-GJbpasQtw2o, JAhRYbDDwDsC4em3dazDKyDw4gM], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/bMobTwHmWhM|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=3; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-032-aosrd-webinars-190-5hQ-anaFGIU

- **Title:** The Ancestral Diet as Treatment for Chronic Disease with Stefan Hartmann, PA – February 8, 2023 (Video)
- **Catalog id:** `aosrd-webinars-190-5hQ-anaFGIU`
- **Pass4 row id:** `aosrd-webinars-190-5hQ-anaFGIU::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/the-ancestral-diet-as-treatment-for-chronic-disease-with-stefan-hartmann-pa/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `CQjlfnZLZ-CY25UUEq35pSQ0lug;lnZUNAyEcVNSN0i3JOEbuJcc15A`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “The Ancestral Diet as Treatment for Chronic Disease with Stefan Hartmann, PA – February 8, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [CQjlfnZLZ-CY25UUEq35pSQ0lug, lnZUNAyEcVNSN0i3JOEbuJcc15A], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/5hQ-anaFGIU|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-033-aosrd-webinars-191-ZrOMyfW29og

- **Title:** Interpreting Test Results with Dr. Andrew Campbell – January 31, 2023 (Video)
- **Catalog id:** `aosrd-webinars-191-ZrOMyfW29og`
- **Pass4 row id:** `aosrd-webinars-191-ZrOMyfW29og::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2023/01/Interpretation-of-test-results-.pdf
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=5):** `uRqtR3sy0qaYlUcYL4_tPVC7Tps;l416W8yP4i7dv3Jhd5H2F74zMnU;j3HjVUuBV5gnR4KrCUuXOZEnPm0;hFcw5MS7FSAuXJGFcnPHqL6j1gM;5HPCyqwQxi9QD1of8g-CPHrnFcc`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Interpreting Test Results with Dr. Andrew Campbell – January 31, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [uRqtR3sy0qaYlUcYL4_tPVC7Tps, l416W8yP4i7dv3Jhd5H2F74zMnU, j3HjVUuBV5gnR4KrCUuXOZEnPm0, hFcw5MS7FSAuXJGFcnPHqL6j1gM, 5HPCyqwQxi9QD1of8g-CPHrnFcc], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/ZrOMyfW29og|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=5; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-034-aosrd-webinars-193-3HKa-GZK_Qw

- **Title:** Menopause-The Impact on Skin and HAir by Dr. Felice Gersh – January 17, 2023 (Video)
- **Catalog id:** `aosrd-webinars-193-3HKa-GZK_Qw`
- **Pass4 row id:** `aosrd-webinars-193-3HKa-GZK_Qw::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/menopause-the-impact-on-skin-and-hair-by-dr-felice-gersh/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `OL_Ukp1RYjVvnjsMHnF2eXCXDC8`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Menopause-The Impact on Skin and HAir by Dr. Felice Gersh – January 17, 2023 (Video)” belong to Pass-1 possible Otter candidate(s) [OL_Ukp1RYjVvnjsMHnF2eXCXDC8], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/3HKa-GZK_Qw|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-035-aosrd-webinars-195-i-q4BtUNVuI

- **Title:** The 14-3-3n Biomarker for Rheumatoid Arthritis Diagnosis, Prognosis, and Monitoring with Dr. Nima Mazinani – January 10, 2023(Video)
- **Catalog id:** `aosrd-webinars-195-i-q4BtUNVuI`
- **Pass4 row id:** `aosrd-webinars-195-i-q4BtUNVuI::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2023/01/14-3-3eta_AOSIM_Final_2023.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “The 14-3-3n Biomarker for Rheumatoid Arthritis Diagnosis, Prognosis, and Monitoring with Dr. Nima Mazinani – January 10, 2023(Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/i-q4BtUNVuI|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-036-aosrd-webinars-196-Td9ybE_W-wU

- **Title:** The Role of the Renin-Angiotensin Components in Atherosclerosis with Dr. James Joseph – January 3, 2023(Video)
- **Catalog id:** `aosrd-webinars-196-Td9ybE_W-wU`
- **Pass4 row id:** `aosrd-webinars-196-Td9ybE_W-wU::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/the-role-of-the-renin-angiotensin-components-in-atherosclerosis-with-dr-james-joseph/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `xg4V_A-L8_Ob1jKGBewDTtKzOWg;JAhRYbDDwDsC4em3dazDKyDw4gM`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “The Role of the Renin-Angiotensin Components in Atherosclerosis with Dr. James Joseph – January 3, 2023(Video)” belong to Pass-1 possible Otter candidate(s) [xg4V_A-L8_Ob1jKGBewDTtKzOWg, JAhRYbDDwDsC4em3dazDKyDw4gM], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/Td9ybE_W-wU|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-037-aosrd-webinars-197-92sBrfKcyfE

- **Title:** Oxytocin to Treat Chronic Disease-Part 2 with Dr. Salaheldin Halasa – December 27, 2022(Video)
- **Catalog id:** `aosrd-webinars-197-92sBrfKcyfE`
- **Pass4 row id:** `aosrd-webinars-197-92sBrfKcyfE::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/oxytocin-utilization-in-chronic-disease-management-with-dr-salaheldin-halasa/
- **Pass1 class (frozen):** `variant_derivative`
- **Candidates (multiplicity=5):** `EqC6yd4bQDKMl2mpzPURPZu-_Pc;3BvIJDrhEXHdWPee7Ztw2x6EmdE;Zxy20R1uant_QctiZutXLSt-Q-E;b2H7gyjRNmbN0l62XtCzeLPovDE;SdzXWjorAW2NkmSfJoC1PdOzwAE`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Oxytocin to Treat Chronic Disease-Part 2 with Dr. Salaheldin Halasa – December 27, 2022(Video)” belong to Pass-1 possible Otter candidate(s) [EqC6yd4bQDKMl2mpzPURPZu-_Pc, 3BvIJDrhEXHdWPee7Ztw2x6EmdE, Zxy20R1uant_QctiZutXLSt-Q-E, b2H7gyjRNmbN0l62XtCzeLPovDE, SdzXWjorAW2NkmSfJoC1PdOzwAE], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/92sBrfKcyfE|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** shared_pdf_url_catalog_ids=aosrd-webinars-197-92sBrfKcyfE;aosrd-webinars-202-x6BIrL8qmzk; not independent evidence; cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=5; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-038-aosrd-webinars-198-fwLHIoDOipY

- **Title:** The Role of Nutrition and Prevention – December 20, 2022(Video)
- **Catalog id:** `aosrd-webinars-198-fwLHIoDOipY`
- **Pass4 row id:** `aosrd-webinars-198-fwLHIoDOipY::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2022/12/The-Role-of-Nutrition-and-Prevention-1.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “The Role of Nutrition and Prevention – December 20, 2022(Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/fwLHIoDOipY|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-039-aosrd-webinars-199-GpYX1_vmLFI

- **Title:** Fracture Proof Your Bones-A Comprehensive Guide to Osteoporosis with Dr. John Neustadt – December 14, 2022(Video)
- **Catalog id:** `aosrd-webinars-199-GpYX1_vmLFI`
- **Pass4 row id:** `aosrd-webinars-199-GpYX1_vmLFI::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/fracture-proof-your-bones-a-comprehensive-guide-to-osteoporosis-with-dr-john-neustadt/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `y59a2fEx8UgOiThJHr1w-HcQc1U;GH57wayNAp6iLAYz_3IRSsC5few`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Fracture Proof Your Bones-A Comprehensive Guide to Osteoporosis with Dr. John Neustadt – December 14, 2022(Video)” belong to Pass-1 possible Otter candidate(s) [y59a2fEx8UgOiThJHr1w-HcQc1U, GH57wayNAp6iLAYz_3IRSsC5few], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/GpYX1_vmLFI|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-040-aosrd-webinars-200-8vtxAVALprY

- **Title:** Integrative Psychiatry, Neurofeedback, and the Treatment Resistant Patient with Dr. John Finnick – December 6, 2022(Video)
- **Catalog id:** `aosrd-webinars-200-8vtxAVALprY`
- **Pass4 row id:** `aosrd-webinars-200-8vtxAVALprY::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/integrative-psychiatry-neurofeedback-and-the-treatment-resistant-patient-with-dr-john-finnick/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Integrative Psychiatry, Neurofeedback, and the Treatment Resistant Patient with Dr. John Finnick – December 6, 2022(Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/8vtxAVALprY|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-041-aosrd-webinars-201-8blzjFv9r8I

- **Title:** Osteopathic Manipulation in Treating Pain, and Substance Abuse – November 29, 2022(Video)
- **Catalog id:** `aosrd-webinars-201-8blzjFv9r8I`
- **Pass4 row id:** `aosrd-webinars-201-8blzjFv9r8I::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/osteopathic-manipulation-in-pain-and-substance-abuse/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Osteopathic Manipulation in Treating Pain, and Substance Abuse – November 29, 2022(Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/8blzjFv9r8I|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-042-aosrd-webinars-202-x6BIrL8qmzk

- **Title:** Oxytocin Utilization in Chronic Disease Management with Dr. Salaheldin Halasa – November 23, 2022(Video)
- **Catalog id:** `aosrd-webinars-202-x6BIrL8qmzk`
- **Pass4 row id:** `aosrd-webinars-202-x6BIrL8qmzk::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/oxytocin-utilization-in-chronic-disease-management-with-dr-salaheldin-halasa/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `GUt4yZgCp4lNVboAnJBHNMsHO7A;EqC6yd4bQDKMl2mpzPURPZu-_Pc`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Oxytocin Utilization in Chronic Disease Management with Dr. Salaheldin Halasa – November 23, 2022(Video)” belong to Pass-1 possible Otter candidate(s) [GUt4yZgCp4lNVboAnJBHNMsHO7A, EqC6yd4bQDKMl2mpzPURPZu-_Pc], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/x6BIrL8qmzk|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** shared_pdf_url_catalog_ids=aosrd-webinars-197-92sBrfKcyfE;aosrd-webinars-202-x6BIrL8qmzk; not independent evidence; cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-043-aosrd-webinars-203-4u_3c_lFUzs

- **Title:** Type-1 Diabetes Outcomes, Therapies, and Future Innovations with Dr. Andrew Koutnik – November 8, 2022(Video)
- **Catalog id:** `aosrd-webinars-203-4u_3c_lFUzs`
- **Pass4 row id:** `aosrd-webinars-203-4u_3c_lFUzs::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/type-1-diabetes-outcomes-therapies-and-future-innovations-with-dr-andrew-koutnik/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `j3HjVUuBV5gnR4KrCUuXOZEnPm0`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Type-1 Diabetes Outcomes, Therapies, and Future Innovations with Dr. Andrew Koutnik – November 8, 2022(Video)” belong to Pass-1 possible Otter candidate(s) [j3HjVUuBV5gnR4KrCUuXOZEnPm0], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/4u_3c_lFUzs|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-044-aosrd-webinars-204-Qy2mrgSpVNg

- **Title:** The Positive Side of the Plummeting Health Index in America with Dr. Mark Lafferty – November 1, 2022(Video)
- **Catalog id:** `aosrd-webinars-204-Qy2mrgSpVNg`
- **Pass4 row id:** `aosrd-webinars-204-Qy2mrgSpVNg::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/the-positive-side-of-the-plummeting-health-index-in-america/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=3):** `qwUT3cyV7gYvn34XQtrA84mAbiI;P1FgRy3FvTrrNYsXISdsJKJeiEg;Zxy20R1uant_QctiZutXLSt-Q-E`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “The Positive Side of the Plummeting Health Index in America with Dr. Mark Lafferty – November 1, 2022(Video)” belong to Pass-1 possible Otter candidate(s) [qwUT3cyV7gYvn34XQtrA84mAbiI, P1FgRy3FvTrrNYsXISdsJKJeiEg, Zxy20R1uant_QctiZutXLSt-Q-E], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/Qy2mrgSpVNg|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=3; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-045-aosrd-webinars-207-0cBElywMkUY

- **Title:** Plasmalogens, Brain Health, and Longevity-What Every Integrative and Osteopathic Physician Needs to Know by Dr. Dayan Goodenowe Tuesday October 11, 2022 (Video)
- **Catalog id:** `aosrd-webinars-207-0cBElywMkUY`
- **Pass4 row id:** `aosrd-webinars-207-0cBElywMkUY::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/plasmalogens-brain-health-and-longevity-what-every-integrative-and-osteopathic-physician-needs-to-know-by-dr-dayan-goodenowe/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=3):** `vjcply7K-rJtWMYGKgD39abIq9E;ZdpkFb1zUrwSD134tv35ZcrcaI8;HY-sCmihzh3EJ69WWVwlTT0Ri6s`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Plasmalogens, Brain Health, and Longevity-What Every Integrative and Osteopathic Physician Needs to Know by Dr. Dayan Goodenowe Tuesday October 11, 2022 (Video)” belong to Pass-1 possible Otter candidate(s) [vjcply7K-rJtWMYGKgD39abIq9E, ZdpkFb1zUrwSD134tv35ZcrcaI8, HY-sCmihzh3EJ69WWVwlTT0Ri6s], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/0cBElywMkUY|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=3; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-046-aosrd-webinars-209-728P3vA7hsU

- **Title:** Molds, Mycotoxins and the Brain-An Evidenced Based Presentation by Dr. Andrew Campbell (Video)
- **Catalog id:** `aosrd-webinars-209-728P3vA7hsU`
- **Pass4 row id:** `aosrd-webinars-209-728P3vA7hsU::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/molds-mycotoxins-and-the-brain-an-evidenced-based-presentation-by-dr-andrew-campbell/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `hFcw5MS7FSAuXJGFcnPHqL6j1gM;v3Md09l1C_mz3hrDPWngln5SYQw`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Molds, Mycotoxins and the Brain-An Evidenced Based Presentation by Dr. Andrew Campbell (Video)” belong to Pass-1 possible Otter candidate(s) [hFcw5MS7FSAuXJGFcnPHqL6j1gM, v3Md09l1C_mz3hrDPWngln5SYQw], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/728P3vA7hsU|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-047-aosrd-webinars-214-Zf7hlrZ7Ljo

- **Title:** Gut-Brain Connection by Dr. Brad Watts (Video)
- **Catalog id:** `aosrd-webinars-214-Zf7hlrZ7Ljo`
- **Pass4 row id:** `aosrd-webinars-214-Zf7hlrZ7Ljo::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2022/08/Clinical-Manifestations-on-Gut-Brain-Connections.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Gut-Brain Connection by Dr. Brad Watts (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/Zf7hlrZ7Ljo|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-048-aosrd-webinars-224-qORv5ARtglk

- **Title:** The Future of Biological Dentistry: Where Do We Go from Here? with Dr. Scott Chandler (Video)
- **Catalog id:** `aosrd-webinars-224-qORv5ARtglk`
- **Pass4 row id:** `aosrd-webinars-224-qORv5ARtglk::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2022/06/The-Future-of-Biological-Dentistry-by-Dr-Scott-Chandler.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “The Future of Biological Dentistry: Where Do We Go from Here? with Dr. Scott Chandler (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/qORv5ARtglk|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** shared_pdf_url_catalog_ids=aosrd-webinars-224-qORv5ARtglk;aosrd-webinars-241-nqr6cW4Gw_A; not independent evidence; cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-049-aosrd-webinars-230-P7DyhMvm0SA

- **Title:** Anti-Aging Medicine with Dr. Mikhail Berman (Video)
- **Catalog id:** `aosrd-webinars-230-P7DyhMvm0SA`
- **Pass4 row id:** `aosrd-webinars-230-P7DyhMvm0SA::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/anti-aging-medicine-with-dr-mikhail-berman/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Anti-Aging Medicine with Dr. Mikhail Berman (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/P7DyhMvm0SA|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-050-aosrd-webinars-232-rqFCphSMW1o

- **Title:** Integrative Medicine and the Law by Judge Egan Walker (Video)
- **Catalog id:** `aosrd-webinars-232-rqFCphSMW1o`
- **Pass4 row id:** `aosrd-webinars-232-rqFCphSMW1o::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/integrative-medicine-and-the-law-by-judge-egan-walker/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Integrative Medicine and the Law by Judge Egan Walker (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/rqFCphSMW1o|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-051-aosrd-webinars-233-GFCg9tySvGI

- **Title:** New Horizons in Cancer Treatment by Kalapana Patel, MD (Video)
- **Catalog id:** `aosrd-webinars-233-GFCg9tySvGI`
- **Pass4 row id:** `aosrd-webinars-233-GFCg9tySvGI::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/new-horizons-in-cancer-treatment-kalapana-patel-md/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “New Horizons in Cancer Treatment by Kalapana Patel, MD (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/GFCg9tySvGI|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-052-aosrd-webinars-234-5xpAcQ8J7hE

- **Title:** Frequency Specific Microcurrent by Carol McMakin, MA,DC (Video)
- **Catalog id:** `aosrd-webinars-234-5xpAcQ8J7hE`
- **Pass4 row id:** `aosrd-webinars-234-5xpAcQ8J7hE::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/frequency-specific-microcurrent-by-carol-mcmakin-madc/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Frequency Specific Microcurrent by Carol McMakin, MA,DC (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/5xpAcQ8J7hE|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-053-aosrd-webinars-235-4ErgdNqYbRc

- **Title:** Integrative Immuno Oncology Part 2 by Dr. Salaheldin Halasa (Video)
- **Catalog id:** `aosrd-webinars-235-4ErgdNqYbRc`
- **Pass4 row id:** `aosrd-webinars-235-4ErgdNqYbRc::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/integrative-immuno-oncology-salaheldin-halasa-md/
- **Pass1 class (frozen):** `variant_derivative`
- **Candidates (multiplicity=3):** `SdzXWjorAW2NkmSfJoC1PdOzwAE;b2H7gyjRNmbN0l62XtCzeLPovDE;JAhRYbDDwDsC4em3dazDKyDw4gM`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Integrative Immuno Oncology Part 2 by Dr. Salaheldin Halasa (Video)” belong to Pass-1 possible Otter candidate(s) [SdzXWjorAW2NkmSfJoC1PdOzwAE, b2H7gyjRNmbN0l62XtCzeLPovDE, JAhRYbDDwDsC4em3dazDKyDw4gM], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/4ErgdNqYbRc|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** shared_pdf_url_catalog_ids=aosrd-webinars-235-4ErgdNqYbRc;aosrd-webinars-237-p59K6kGBP-Y; not independent evidence; cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=3; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-054-aosrd-webinars-236-JdOL-00shnA

- **Title:** Chronic Fatigue Syndrome by Dr. Jacob Teitelbaum March 15, 2022 (Video)
- **Catalog id:** `aosrd-webinars-236-JdOL-00shnA`
- **Pass4 row id:** `aosrd-webinars-236-JdOL-00shnA::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/chronic-fatigue-syndrome/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `eEDmdeOTNokKYKUadQuO_9gDjuo`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Chronic Fatigue Syndrome by Dr. Jacob Teitelbaum March 15, 2022 (Video)” belong to Pass-1 possible Otter candidate(s) [eEDmdeOTNokKYKUadQuO_9gDjuo], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/JdOL-00shnA|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-055-aosrd-webinars-237-p59K6kGBP-Y

- **Title:** Integrative Immuno Oncology by Dr. Salaheldin Halasa (Video)
- **Catalog id:** `aosrd-webinars-237-p59K6kGBP-Y`
- **Pass4 row id:** `aosrd-webinars-237-p59K6kGBP-Y::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/integrative-immuno-oncology-salaheldin-halasa-md/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `b2H7gyjRNmbN0l62XtCzeLPovDE;SdzXWjorAW2NkmSfJoC1PdOzwAE`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Integrative Immuno Oncology by Dr. Salaheldin Halasa (Video)” belong to Pass-1 possible Otter candidate(s) [b2H7gyjRNmbN0l62XtCzeLPovDE, SdzXWjorAW2NkmSfJoC1PdOzwAE], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/p59K6kGBP-Y|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** shared_pdf_url_catalog_ids=aosrd-webinars-235-4ErgdNqYbRc;aosrd-webinars-237-p59K6kGBP-Y; not independent evidence; cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-056-aosrd-webinars-238-oMjTc20O6Ps

- **Title:** What I Learned from the Osteopathic Masters-Dr. William Richwine (Video)
- **Catalog id:** `aosrd-webinars-238-oMjTc20O6Ps`
- **Pass4 row id:** `aosrd-webinars-238-oMjTc20O6Ps::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2022/03/What-I-learned-from-the-Osteopathic-Masters-and....-Richwine-William-final-2022.0301-pdf.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “What I Learned from the Osteopathic Masters-Dr. William Richwine (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://youtu.be/oMjTc20O6Ps|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-057-aosrd-webinars-241-nqr6cW4Gw_A

- **Title:** Biological Dentistry by Dr. Scott Chandler (Video)
- **Catalog id:** `aosrd-webinars-241-nqr6cW4Gw_A`
- **Pass4 row id:** `aosrd-webinars-241-nqr6cW4Gw_A::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2022/06/The-Future-of-Biological-Dentistry-by-Dr-Scott-Chandler.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Biological Dentistry by Dr. Scott Chandler (Video)” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://www.youtube.com/watch?v=nqr6cW4Gw_A|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** shared_pdf_url_catalog_ids=aosrd-webinars-224-qORv5ARtglk;aosrd-webinars-241-nqr6cW4Gw_A; not independent evidence; cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-058-aosrd-webinars-242-tiIDS69FRkQ

- **Title:** Pairing Nutrition with Regenerative Medicine by Dr. Brad Watts – Video
- **Catalog id:** `aosrd-webinars-242-tiIDS69FRkQ`
- **Pass4 row id:** `aosrd-webinars-242-tiIDS69FRkQ::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/pairing-nutrition-with-regenerative-medicine-by-dr-brad-watts/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `0pIRZSR5hLU8vZNbqCJ9pLpRE9M;hxlUjPAXSClySIs4HN1P0CWe_Qk`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Pairing Nutrition with Regenerative Medicine by Dr. Brad Watts – Video” belong to Pass-1 possible Otter candidate(s) [0pIRZSR5hLU8vZNbqCJ9pLpRE9M, hxlUjPAXSClySIs4HN1P0CWe_Qk], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://www.youtube.com/watch?v=tiIDS69FRkQ|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-059-aosrd-webinars-244-DwiLCdt69H4

- **Title:** Solutions on Suicide January 18, 2022 by Joel Peterson -Video
- **Catalog id:** `aosrd-webinars-244-DwiLCdt69H4`
- **Pass4 row id:** `aosrd-webinars-244-DwiLCdt69H4::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/solutions-on-suicide-january-18-2022-by-joel-peterson/
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `FbRyr7EkkewAoPTmXbK9DtUiA_Y`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Solutions on Suicide January 18, 2022 by Joel Peterson -Video” belong to Pass-1 possible Otter candidate(s) [FbRyr7EkkewAoPTmXbK9DtUiA_Y], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://www.youtube.com/watch?v=DwiLCdt69H4|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-060-aosrd-webinars-245-y3Fz32zWP10

- **Title:** Hypo and Hyperthyroidismare One Internal Disease with Two Different Manifestations by Dr. Parvin Zarrin – Video
- **Catalog id:** `aosrd-webinars-245-y3Fz32zWP10`
- **Pass4 row id:** `aosrd-webinars-245-y3Fz32zWP10::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/hypo-and-hyperthyroidism-are-one-internal-disease/
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Hypo and Hyperthyroidismare One Internal Disease with Two Different Manifestations by Dr. Parvin Zarrin – Video” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://www.youtube.com/watch?v=y3Fz32zWP10|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-061-aosrd-webinars-249-3mTLksPwJyo

- **Title:** Mycotoxins and Autoimmunity by Andrew Campbell, MD, Dec 14, 2021
- **Catalog id:** `aosrd-webinars-249-3mTLksPwJyo`
- **Pass4 row id:** `aosrd-webinars-249-3mTLksPwJyo::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2021/12/Mold-and-Mycotoxins-1021.pdf
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `v3Md09l1C_mz3hrDPWngln5SYQw;hFcw5MS7FSAuXJGFcnPHqL6j1gM`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Mycotoxins and Autoimmunity by Andrew Campbell, MD, Dec 14, 2021” belong to Pass-1 possible Otter candidate(s) [v3Md09l1C_mz3hrDPWngln5SYQw, hFcw5MS7FSAuXJGFcnPHqL6j1gM], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://www.youtube.com/watch?v=3mTLksPwJyo|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-062-aosrd-webinars-261-qVX_h6blAQw

- **Title:** Medical Intuition by Terri Jay  Aug 31, 2021 – Video
- **Catalog id:** `aosrd-webinars-261-qVX_h6blAQw`
- **Pass4 row id:** `aosrd-webinars-261-qVX_h6blAQw::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2021/09/PowerPoint-for-Doctors-Terri-Jay-2.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Medical Intuition by Terri Jay  Aug 31, 2021 – Video” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://www.youtube.com/watch?v=qVX_h6blAQw|pass4_decision=DEFER_EXPENSIVE_VIDEO
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-063-aosrd-webinars-263-lCzuTx9LKnQ

- **Title:** Chronic Fatigue Syndrome: Road to Resolution: Dr. Todd Born Aug 17, 2021 – Video
- **Catalog id:** `aosrd-webinars-263-lCzuTx9LKnQ`
- **Pass4 row id:** `aosrd-webinars-263-lCzuTx9LKnQ::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2021/08/Chronic-Fatigue-Syndrome-ASORD-1.pdf
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=1):** `CMNjlQbT2xu4NqL-9gu4VQSt0mo`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Chronic Fatigue Syndrome: Road to Resolution: Dr. Todd Born Aug 17, 2021 – Video” belong to Pass-1 possible Otter candidate(s) [CMNjlQbT2xu4NqL-9gu4VQSt0mo], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://www.youtube.com/watch?v=lCzuTx9LKnQ|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-064-aosrd-webinars-268-2cecK4Jk2vw

- **Title:** Genetic Snips and COVID-19 Severity by Dr. Cheryl Ortel July 6, 2021 – Video
- **Catalog id:** `aosrd-webinars-268-2cecK4Jk2vw`
- **Pass4 row id:** `aosrd-webinars-268-2cecK4Jk2vw::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2021/07/Genetic-Snips-and-COVID-19-Severity-7.6.21.pdf
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=2):** `4qg44PRw27Y2Jbzl7MXMYCX0HuI;hQzjA4-OBAL6Qn7OOOywEISWs3I`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Genetic Snips and COVID-19 Severity by Dr. Cheryl Ortel July 6, 2021 – Video” belong to Pass-1 possible Otter candidate(s) [4qg44PRw27Y2Jbzl7MXMYCX0HuI, hQzjA4-OBAL6Qn7OOOywEISWs3I], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://www.youtube.com/watch?v=2cecK4Jk2vw|pass4_decision=NO_ACQUISITION_INDICATED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=2; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-065-aosrd-webinars-280-gLzMZA_eM5g

- **Title:** Immune Peptides by William Clearfield DO – Video
- **Catalog id:** `aosrd-webinars-280-gLzMZA_eM5g`
- **Pass4 row id:** `aosrd-webinars-280-gLzMZA_eM5g::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2021/06/Immune-Peptides-w-Intro.pdf
- **Pass1 class (frozen):** `possible`
- **Candidates (multiplicity=5):** `avbRWMav2fwgobz9r7HjwR4z44I;lnZUNAyEcVNSN0i3JOEbuJcc15A;Se28ZvfBuNMYHNmwQG9ua7gbTWk;zXf2JR4NKM7KxvOGrUxYJnH-ld8;CMNjlQbT2xu4NqL-9gu4VQSt0mo`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `identity_resolution`
- **Evidence question:** Does AOSRD PDF for “Immune Peptides by William Clearfield DO – Video” belong to Pass-1 possible Otter candidate(s) [avbRWMav2fwgobz9r7HjwR4z44I, lnZUNAyEcVNSN0i3JOEbuJcc15A, Se28ZvfBuNMYHNmwQG9ua7gbTWk, zXf2JR4NKM7KxvOGrUxYJnH-ld8, CMNjlQbT2xu4NqL-9gu4VQSt0mo], or is the relationship still unresolved after inspecting the PDF?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://www.youtube.com/watch?v=gLzMZA_eM5g|pass4_decision=DEFER_IDENTITY_UNRESOLVED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; candidate_multiplicity=5; preserve all candidates; pass4_acquisition_decision=CONDITIONAL_ACQUIRE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

### erc-4.5-pdf-066-aosrd-webinars-283-cxoIpMhdeJw

- **Title:** Post Covid 19 Vaccination Syndrome
- **Catalog id:** `aosrd-webinars-283-cxoIpMhdeJw`
- **Pass4 row id:** `aosrd-webinars-283-cxoIpMhdeJw::AOSRD_PDF`
- **Representation:** `AOSRD_PDF` — https://aosrd.org/wp-content/uploads/2021/04/Post-Covid-19-Vaccine-Toxic-Syndrome.pdf
- **Pass1 class (frozen):** `no_match`
- **Candidates (multiplicity=0):** `(none)`
- **Uncertainty:** `identity_uncertainty`
- **Purpose:** `unlinked_source_investigation`
- **Evidence question:** What session (if any) does AOSRD PDF for “Post Covid 19 Vaccination Syndrome” represent, given Pass 1 no_match to the Otter corpus — without treating no_match as proof of a new lecture?
- **Proposed action:** `DOWNLOAD_PDF` (cost `low`)
- **Why this action:** AOSRD PDF is finite, text/visual-bearing, and Pass 3 marked available_external; cheapest discriminating representation for this evidence question. Video alternatives remain deferred under Pass 4.
- **Authorized to establish (proposed):** `bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object`
- **Authorization state:** `pending`
- **Decision:** `NEEDS_HUMAN_SCOPING` — awaiting human
- **Human authorization record:** _(empty — pending)_
- **Alternates:** YouTube_video|https://www.youtube.com/watch?v=cxoIpMhdeJw|pass4_decision=NO_ACQUISITION_INDICATED
- **Notes:** cheaper_or_peer_alternatives_listed_in_alternate_representation_refs; pass4_acquisition_decision=ACQUIRE_CANDIDATE; pass4_5_mvp=pdf_batch_pending_authorization; no_download_performed; awaiting_human_authorization_gate

Human gate options: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`.

## STOP

```
PASS 4.5 PDF MVP COMPLETE.
EVIDENCE RESOLUTION CASES SEEDED.
AUTHORIZATION PENDING.
NO MEDIA DOWNLOADED.
NO MEDIA PROCESSED.
NO SOURCE PACKETS MODIFIED.
NO PASS 1–4 RECORDS MODIFIED.
HUMAN AUTHORIZATION REQUIRED BEFORE ANY DOWNLOAD_PDF.
```

