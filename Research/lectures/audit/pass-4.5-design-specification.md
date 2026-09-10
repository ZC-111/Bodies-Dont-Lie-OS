# Pass 4.5 Design Specification — Evidence Resolution + Human Authorization

| Field | Value |
|---|---|
| Status | Design only — **not implemented** |
| Inputs | Frozen Pass 1–4 audit outputs; Constitution principles |
| Missing upstream docs | `BDS/BDS-Evidence-Specification.md` and `BDS/BDS-Scope-Charter.md` were **not present** in this repository at design time; design is grounded in Pass 1–4 + Constitution instead |
| Non-goal | This document does not authorize acquisition, recovery, OCR, transcription, hashing, merging, deletion, Knowledge promotion, or schema migration |

---

## 1. Purpose

Pass 4.5 is the controlled transition between:

> “We have identified an information / evidence gap” (Pass 4)

and

> “A human has authorized the least costly action that may reduce a named uncertainty.”

**Pass 4.5 = Evidence Resolution + Human Authorization.**

It determines:

1. what uncertainty exists;
2. what evidence question needs answering;
3. whether an evidence action could reduce that uncertainty;
4. what the cheapest discriminating action is;
5. whether that action is authorized;
6. what the action is allowed to establish;
7. what remains unresolved afterward.

Acquisition is **not** the objective. Resolving (or deliberately leaving open) an evidence question is.

---

## 2. Position in the BDS pipeline

```text
Pass 1  Title / relationship candidates          (frozen)
Pass 2  Local representation inventory           (frozen)
Pass 3  External representation availability     (frozen)
Pass 4  Information-value / acquisition gate     (frozen)
Pass 4.5 Evidence resolution + human authorization  ← THIS SPEC
Pass 5+ Authorized acquisition / recovery / inspection (future; not specified here)
Later   Session reconciliation, Knowledge Objects (out of scope)
```

Pass 4.5 consumes Pass 4 rows (and Pass 1–3 join keys). It does **not** rewrite Pass 1–4.

---

## 3. Scope

In scope for a future Pass 4.5 *implementation*:

- Create **Evidence Resolution Cases (ERCs)** from Pass 4 candidates that still need a decision.
- Attach an explicit **evidence question** to each case.
- Choose a **representation-specific** next evidence action (or DEFER / NO_ACTION).
- Record **human authorization** (or denial / deferral) before any side-effecting work.
- After an authorized action executes (in a later pass), record **reassessment** and residual uncertainty.

Out of scope for Pass 4.5 itself:

- Downloading, recovering, OCR, transcription, hashing, renaming, moving, deleting.
- Creating Knowledge Objects or pathways.
- Merging sessions or collapsing duplicates.
- Changing Pass 1 match classes.
- Clinical / scientific / monetization ranking.

---

## 4. Non-goals

Pass 4.5 is **not**:

- a downloader or recovery robot;
- a full evidence-scoring system;
- a knowledge graph implementation;
- automatic session identity establishment;
- automatic “new lecture” discovery;
- a rewrite of the Pass 4 acquisition vocabulary into truth claims.

---

## 5. Core principles

Grounded in Constitution: Reality leaves evidence; Observation precedes understanding; Understanding precedes intervention; Stewardship over optimization; Atomic knowledge; Clarity / Simplicity.

Operational rules for Pass 4.5:

```text
UNCERTAINTY
    ↓
EVIDENCE QUESTION
    ↓
EVIDENCE NEEDED
    ↓
CANDIDATE REPRESENTATION(S)
    ↓
CHEAPEST DISCRIMINATING ACTION
    ↓
HUMAN AUTHORIZATION
    ↓
(later) ACQUISITION / RECOVERY / INSPECTION
    ↓
REASSESSMENT
```

Preserve these RED-PILL distinctions:

| Must not collapse | Meaning |
|---|---|
| Catalog record ≠ representation ≠ session/event | One catalog row may have many representations; many rows may share one representation; neither equals session identity |
| Representation identity ≠ session identity | Knowing a PDF/video file ≠ knowing which lecture event it is |
| Availability ≠ access ≠ authorization | Pass 3 “available” ≠ we can obtain it ≠ we may obtain it |
| `no_match` ≠ new session | Unrelated to Otter corpus ≠ confirmed novel lecture |
| `possible` ≠ established identity | Candidate only |
| Strong + multiple candidates remains representable | Multiplicity is structural, not a confidence bug |
| Variant/derivative ≠ unresolved identity | Different question type |
| Duplicate ≠ independent evidence | Keep both records; do not double-count |
| Temporal proximity ≠ identity proof | Context only |
| Pathway on candidate Otter ≠ pathway on unresolved historical item | No leak-through |
| `claimed_present_elsewhere` ≠ accessible/acquired/usable | Mandatory |
| Information volume ≠ expected information gain | Prefer discriminating cheap evidence |
| Whole ≠ complete | Coherent identity with explicit gaps is allowed |

---

## 6. Minimum concepts

### 6.1 Evidence Resolution Case (ERC)

The Pass 4.5 work unit. One ERC addresses **one evidence question** about **one catalog record**, optionally scoped to **one primary representation** (with alternate representations listed).

Pass 4 already emits one row per representation opportunity. Pass 4.5 may:

- promote a Pass 4 row into an ERC, or
- group PDF + video rows for the same catalog record under one ERC when they share one evidence question,

but **authorization and action remain representation-specific**.

### 6.2 Layers (must stay separate)

```text
CATALOG RECORD
    ↓ has
REPRESENTATION (PDF / YouTube / Vimeo / Rumble / local path / external-machine path / Otter packet)
    ↓ may relate to
SESSION / EVENT (lecture occurrence)
```

### 6.3 Three graphs Pass 4.5 must not preclude

Pass 4.5 does **not** implement these graphs. It must not encode data in a way that prevents them later:

1. **Representation graph** — PDF, YouTube, Otter transcript, slides, local file, video, …
2. **Relationship graph** — `represents`, `possible_representation_of`, `same_session_representation`, `variant_of`, `derivative_of`, `duplicate_of`, `related_to`, `unresolved`
3. **Evidence-resolution graph** — unknown → question → candidate evidence → authorization → action → reassessment → resolved / still unresolved

---

## 7. Minimum vocabulary

### 7.1 Fields / concepts

| Field / concept | Purpose | Required? | Allowed values | Why necessary |
|---|---|---|---|---|
| `erc_id` | Stable case id | Yes | string | Track authorization + reassessment |
| `catalog_record_id` | Join to Pass 1/3/4 | Yes | Pass record id | Catalog ≠ representation |
| `pass4_row_ids` | Provenance | Yes | list/string | Trace to frozen Pass 4 |
| `primary_representation_ref` | Target of proposed action | Yes if action ≠ NO_ACTION/DEFER-without-target | type + url/path/id | Representation-specific action |
| `alternate_representation_refs` | Cheaper/peer alternatives | No | list | Prevent bypassing cheaper evidence |
| `uncertainty_class` | What kind of unknown | Yes | see §8 | Drives question + action |
| `evidence_question` | Articulable question | Yes | free text (short) | No action without a question |
| `evidence_purpose` | Why we would act | Yes | see §7.3 | Separates identity vs enrichment vs recovery |
| `pass1_match_class_frozen` | Frozen Pass 1 class | Yes | strong / likely / possible / variant_derivative / no_match / (blank) | Do not rewrite Pass 1 |
| `candidate_session_refs` | Otter/session candidates | Yes (may be empty) | list; preserve multiplicity | Strong+multi must remain representable |
| `candidate_multiplicity` | Structural count | Yes | integer ≥ 0 | Not a confidence score |
| `temporal_relation` | Date context only | No | same_day / near_date / moderate_offset / large_offset / unknown | Not identity proof |
| `local_representation_state` | From Pass 2 | Yes | present_local / claimed_present_elsewhere / absent / unknown | claimed ≠ accessible |
| `external_availability_state` | From Pass 3 | Yes | available_external / unavailable_external / cataloged_unverified / not_checked / not_applicable | Availability ≠ access |
| `access_state` | Can *we* reach it now? | Yes | accessible / inaccessible / unknown / not_applicable | Distinct from availability |
| `authorization_state` | Human gate | Yes | not_requested / pending / authorized / denied / deferred | Availability ≠ authorization |
| `next_evidence_action` | Proposed action | Yes | see §7.2 | Broader than “acquire” |
| `action_cost_class` | Relative cost | Yes | trivial / low / medium / high / very_high / unknown | Compare alternatives |
| `why_this_action` | Preferability note | Yes if action not NO_ACTION | short text | Must justify vs cheaper alts |
| `decision` | Case outcome gate | Yes | see §7.4 | Separated from reason |
| `decision_reason` | Why that decision | Yes | see §7.5 | Do not overload decision enum |
| `authorized_to_establish` | Epistemic ceiling | Yes if authorized | see §7.6 | Acquisition ≠ identity ≠ Knowledge |
| `residual_uncertainty` | After reassessment | Yes after action/decision | still_unresolved / reduced / resolved / not_applicable | “Still unresolved” is valid |
| `human_authorization_record` | Who/what/when | Yes when leaving pending | actor, timestamp, scope, notes | Auditability |
| `notes` | Non-enum context | No | text | Edge cases |

Reuse Pass 4 fields where adequate (`acquisition_rationale`, scores, `acquisition_decision`) as **inputs only**, not as Pass 4.5 truth claims.

**Important:** Pass 4’s `ACQUIRE_CANDIDATE` / `CONDITIONAL_ACQUIRE` / `DEFER_*` vocabulary is an information-value gate. It is **not** identical to Pass 4.5’s authorization vocabulary (`AUTHORIZE_ACTION`, `DEFER`, `NO_ACTION`, …). A Pass 4 acquire candidate still requires a Pass 4.5 evidence question + human authorization before any side effect.

Do not duplicate Pass 4 score columns inside the ERC unless needed for join convenience.

### 7.2 `next_evidence_action` (minimum set)

Recommendation: prefer **`next_evidence_action`** over overloaded “acquire.” Acquisition/recovery are action subtypes.

| Action | When required by Pass 4 dataset |
|---|---|
| `VERIFY_AVAILABILITY` | URL cataloged but Pass 3 `not_checked` / blocked (e.g. Rumble 403) |
| `INSPECT_METADATA` | Cheap public metadata may discriminate identity without body fetch (oEmbed/title/PDF headers already partly used; extends carefully) |
| `DOWNLOAD_PDF` | Pass 4 ACQUIRE/CONDITIONAL PDF cases after authorization |
| `COMPARE_REPRESENTATIONS` | Shared PDF URL, shared YouTube id with conflicting titles, colchicine-like pairs, strong+multi candidates |
| `HUMAN_IDENTITY_REVIEW` | possible/variant/multi-candidate; no cheap auto discriminator |
| `RECOVER_LOCAL_REPRESENTATION` | Pass 2 `claimed_present_elsewhere` (Otter slides, local-downloads) when human authorizes machine access |
| `RECOVER_EXTERNAL_MACHINE_REPRESENTATION` | AOSRD 2022 `/Volumes/...` claims |
| `DEFER` | *(discouraged as action token)* Prefer `decision=DEFER` with deferred candidate in `next_evidence_action` — see §20.2 |
| `NO_ACTION` | Sufficient local evidence or no opportunity |

**Not** included yet: `DOWNLOAD_VIDEO`, `FETCH_CAPTIONS`, `RUN_WHISPER`, `OCR_PDF` — these are later processing actions, not Pass 4.5 authorization primitives. A future pass may add them only after Pass 4.5 shows a named evidence question that requires them.

### 7.3 `evidence_purpose` (minimum)

| Value | Meaning |
|---|---|
| `identity_resolution` | Discriminate among session candidates / clarify relationship |
| `representation_enrichment` | Add a distinct representation to an already-plausible session (e.g. PDF slides when Otter text exists) |
| `unlinked_source_investigation` | Investigate a `no_match` source **without** asserting novelty |
| `variant_or_derivative_characterization` | Characterize segment/brief/related representation links |
| `duplicate_characterization` | Test whether two records share one representation/session |
| `archive_recovery` | Recover claimed local/external-machine bytes into auditable custody |
| `availability_clarification` | Resolve access/availability uncertainty only |

Avoid the phrase “new session acquisition.” Use `unlinked_source_investigation` until identity is established by later reconciliation.

### 7.4 `decision` (gate outcomes)

| Decision | Meaning |
|---|---|
| `AUTHORIZE_ACTION` | Human authorizes the stated `next_evidence_action` under `authorized_to_establish` |
| `DENY_ACTION` | Human rejects the proposed action |
| `DEFER` | Do not act now |
| `NO_ACTION` | No useful action identified |
| `NEEDS_HUMAN_SCOPING` | Case underspecified; human must refine question/representation before authorize |

### 7.5 `decision_reason` (separate from decision)

| Reason | Example use |
|---|---|
| `IDENTITY_UNRESOLVED` | possible/multi-candidate; action deferred or limited |
| `CHEAPER_REPRESENTATION_AVAILABLE` | PDF preferred over video |
| `EXISTING_REPRESENTATION_SUFFICIENT` | Otter text covers the question |
| `AVAILABILITY_OR_ACCESS_UNCLEAR` | claimed elsewhere / not_checked |
| `COST_EXCEEDS_EXPECTED_GAIN` | expensive video, captions unknown |
| `DUPLICATE_OR_CONFLICTING_REPRESENTATION` | needs compare first |
| `AUTHORIZATION_BOUNDARY` | legal/custody/machine access |
| `QUESTION_NOT_ARTICULATED` | refuse action |
| `HUMAN_PREFERENCE` | explicit human defer/deny |
| `OTHER` | requires notes |

### 7.6 `authorized_to_establish` (epistemic ceiling)

| Value | Action may establish… |
|---|---|
| `bytes_in_custody` | We possess a file/object under audit control |
| `metadata_observation` | Observed public metadata only |
| `representation_relationship_hypothesis` | Updated *candidate* relationship notes (not Pass 1 rewrite) |
| `availability_access_fact` | Updated access/availability fact |
| `nothing_epistemic` | Process step with no knowledge claim |
| `explicitly_not_session_identity` | Hard ban: this authorization does **not** establish session identity |
| `explicitly_not_knowledge_object` | Hard ban: no Knowledge promotion |

Multiple flags allowed. Default for `DOWNLOAD_PDF` under unresolved identity: `bytes_in_custody` + `explicitly_not_session_identity` + `explicitly_not_knowledge_object`.

---

## 8. Uncertainty model

Use only these classes unless a later RED-PILL proves another is necessary:

| Class | Question it names |
|---|---|
| `identity_uncertainty` | Which session/event (if any) does this representation belong to? |
| `representation_uncertainty` | What object is this (PDF vs page vs segment vs duplicate vs container/series)? |
| `availability_access_uncertainty` | Does it exist, can we reach it, is custody possible? |
| `decision_context_uncertainty` | Do we know enough about alternatives/cost/purpose to choose an action? |

Mapping hints from Pass 4 (non-exhaustive):

| Pass 4 pattern | Dominant uncertainty |
|---|---|
| `DEFER_IDENTITY_UNRESOLVED` / `possible` | identity_uncertainty |
| `ACQUIRE_CANDIDATE` PDF `no_match` | identity_uncertainty **and** unlinked_source_investigation (do not assume novelty) |
| `DEFER_EXPENSIVE_VIDEO` | decision_context_uncertainty (+ often identity) |
| `claimed_present_elsewhere` / 2022 volumes | availability_access_uncertainty |
| Shared YouTube id / shared PDF URL / colchicine pair | representation_uncertainty (+ identity) |
| Strong Otter + missing local slides + PDF available | low identity uncertainty; representation enrichment |

---

## 9. Evidence-question requirement

### Choice

For Pass 4.5 MVP: **`evidence_question` is a required field on the ERC**, not a separate first-class database object.

### Why

- Preserves the architecture (every action answers a named question).
- Avoids building an Evidence Question subsystem before one is needed.
- ERCs remain atomic and auditable; a later Evidence Question registry can index these strings if required.

### Rule

**No `AUTHORIZE_ACTION` without a non-empty `evidence_question`.**

Example questions:

- “Does PDF *X* share slide content with Otter packet *Y*, or is it a different session?”
- “Are catalog rows A and B the same YouTube representation with conflicting titles?”
- “Can the claimed `/Volumes/...` file for 2022 talk Z be recovered into custody?”
- “Is the colchicine ‘uses’ local item a duplicate/variant of ‘CV prevention’, or distinct?”

---

## 10. Human authorization boundary

Pass 4.5 **ends** at authorization (or defer/deny/no-action).

| Allowed in Pass 4.5 | Forbidden in Pass 4.5 |
|---|---|
| Propose ERC + action | Download / recover / process |
| Record human authorize/deny/defer | Silent auto-acquire |
| Bound `authorized_to_establish` | Establish session identity by fiat |
| Require cheaper alternative consideration | Bypass PDF for video without reason |

Human authorization record minimum: actor, timestamp, `erc_id`, authorized action, representation ref, epistemic ceiling, free-text caveat.

---

## 11. Representation-level handling

- One catalog record may yield **multiple** ERCs or one ERC with multiple representation refs.
- Decisions for PDF vs YouTube for the same title may differ (Pass 4 already shows this).
- `CHEAPER_REPRESENTATION_AVAILABLE` must be considered when a PDF exists beside a video.
- `claimed_present_elsewhere` representations use `RECOVER_*` actions, never pretend they are public-web `DOWNLOAD_*`.
- External-machine and local-download paths are **not** automatically public acquisition candidates.

---

## 12. Session-reconciliation requirements (preserve only)

Pass 4.5 does **not** implement Session Reconciliation Records. It must preserve:

1. Catalog record id(s)
2. All known representation refs (local + external)
3. All candidate session refs with frozen Pass 1 class + multiplicity
4. Relationship hypotheses as **non-authoritative** notes
5. Explicit gaps (`claimed_present_elsewhere`, unavailable video, captions `not_checked`)
6. Authorization history and epistemic ceilings
7. Residual uncertainty after each action

This allows a later session to be **whole but incomplete**: identity/relationships coherent, missing representations listed as gaps — without manufacturing completeness.

---

## 13. Decision invariants (unit tests)

Implementation must preserve:

1. No authorization without an articulable `evidence_question`.
2. Authorization does not establish session identity unless a *later* reconciliation pass explicitly does so under its own rules (Pass 4.5 default forbids it).
3. `no_match` does not establish novelty.
4. `possible` does not become `strong`/`established` via acquisition alone.
5. Duplicate/conflict candidates are not counted as independent confirming evidence.
6. Pathways/Knowledge on a candidate Otter packet do not propagate through unresolved relationships.
7. Availability does not imply access; access does not imply authorization.
8. `claimed_present_elsewhere` does not imply accessible/present/acquired/usable.
9. Date proximity does not establish identity.
10. Acquisition/recovery does not promote Knowledge Objects.
11. `still_unresolved` is a valid terminal state for an ERC cycle.
12. A cheaper discriminating representation must not be bypassed without `why_this_action` naming the reason.
13. Existing sufficient local representation may yield `decision=NO_ACTION` / `decision=DEFER` with `decision_reason=EXISTING_REPRESENTATION_SUFFICIENT`.
14. Pass 1–4 frozen outputs are not rewritten by Pass 4.5.
15. Candidate multiplicity ≥ 2 remains expressible alongside `strong` or `possible`.
16. `authorization_state=authorized` iff `decision=AUTHORIZE_ACTION` and `human_authorization_record` is present.
17. Shared representation URLs are not independent evidence.
18. Pass 4.5 MVP performs no network acquisition and writes audit outputs only.

---

## 14. Edge-case walkthroughs

For each case: **know / ask / act / must not infer**.

### 1. Colchicine uses vs low-dose colchicine CV prevention
- **Know:** Two local-download catalog rows; no public URL; Pass 4 `NOT_ENOUGH_INFORMATION`.
- **Ask:** Same representation/session, variant, or distinct?
- **Act:** Propose `RECOVER_LOCAL_REPRESENTATION` then `COMPARE_REPRESENTATIONS` (authorized in later execution), or `decision=DEFER` until custody exists.
- **Must not:** Merge/delete; count as two independent evidences; call either a new Knowledge lecture.

### 2. Same YouTube ID under two conflicting titles
- **Know:** Pass 3 collision example (YouTube id `l-_Gf5qt0l0` appears under conflicting catalog titles).
- **Ask:** One representation mis-titled in catalog, or data error?
- **Act:** `COMPARE_REPRESENTATIONS` / `INSPECT_METADATA` / `HUMAN_IDENTITY_REVIEW`.
- **Must not:** Assume two sessions; acquire twice.

### 3. Muscle Centric Medicine PDF/title mismatch
- **Know:** PDF + YouTube rows; `possible` identity; PDF conditional, video deferred.
- **Ask:** Does PDF content match candidate Otter / video title?
- **Act:** Prefer `DOWNLOAD_PDF` under `identity_resolution` purpose + epistemic ceiling, then compare; keep video `decision=DEFER`.
- **Must not:** Treat title string as session proof.

### 4. Same AOSRD PDF linked by multiple catalog records
- **Know:** Shared URL across catalog ids.
- **Ask:** Duplicate cataloguing or distinct sessions wrongly sharing a file?
- **Act:** `COMPARE_REPRESENTATIONS`; single custody object; many catalog links.
- **Must not:** Download N copies as N evidences.

### 5. Strong relationship with multiple Otter candidates
- **Know:** Multiplicity > 1 even with `strong`.
- **Ask:** Which candidate session (if any) is correct?
- **Act:** `HUMAN_IDENTITY_REVIEW` and/or PDF compare; preserve all candidates.
- **Must not:** Collapse to one Otter id silently.

### 6. Possible with five Otter candidates
- **Know:** High identity uncertainty.
- **Ask:** Can any cheap representation discriminate?
- **Act:** `HUMAN_IDENTITY_REVIEW` or conditional PDF; else `decision=DEFER` with `decision_reason=IDENTITY_UNRESOLVED`.
- **Must not:** Average candidates into a fake identity.

### 7. Variant/derivative with multiple candidate sessions
- **Know:** Different question than 1:1 identity.
- **Ask:** Segment/brief/related-to which parent representation/session?
- **Act:** `evidence_purpose=variant_or_derivative_characterization`; compare; often `decision=DEFER`.
- **Must not:** Force one-to-one identity model.

### 8. 2022 conference record claimed on external machine
- **Know:** `catalog_only` + `/Volumes/...`; availability not publicly verified.
- **Ask:** Can we access custody path? Worth recovering for which question?
- **Act:** `RECOVER_EXTERNAL_MACHINE_REPRESENTATION` only with authorization; else `decision=DEFER` + access uncertainty.
- **Must not:** Treat as public `DOWNLOAD_*` candidate.

### 9. Local download with unknown representation type
- **Know:** Path claimed; type/format uncertain.
- **Ask:** What representation is it? Duplicate of what?
- **Act:** `RECOVER_LOCAL_REPRESENTATION` + inspect metadata; `representation_uncertainty`.
- **Must not:** Assume PDF/video/transcript.

### 10. Historical 2021/22 item only `possible` to later Otter
- **Know:** Temporal offset may be large; Pass 1 possible only.
- **Ask:** Same session, topical reuse, or unrelated?
- **Act:** `decision=DEFER` or `HUMAN_IDENTITY_REVIEW`; temporal_relation = large_offset/unknown as context only.
- **Must not:** Date proximity ⇒ identity.

### 11. Candidate Otter packet contains a pathway
- **Know:** Pathway is on the *candidate*, relationship unresolved.
- **Ask:** (Identity question only.)
- **Act:** Resolve identity first; pathway ignored for propagation.
- **Must not:** Attach pathway to historical representation via possible link.

### 12. Two YouTube representations under same catalog title
- **Know:** Representation multiplicity under one catalog label.
- **Ask:** Full vs brief? Duplicate uploads? Series container?
- **Act:** `COMPARE_REPRESENTATIONS`; possibly mark catalog as container (`representation_uncertainty`).
- **Must not:** Acquire both by default.

### 13. PDF available; YouTube captions unverified
- **Know:** Classic Pass 4 pattern.
- **Ask:** What does the PDF add relative to Otter/text need?
- **Act:** Prefer `DOWNLOAD_PDF`; video `decision=DEFER` with `decision_reason=CHEAPER_REPRESENTATION_AVAILABLE` / `COST_EXCEEDS_EXPECTED_GAIN`.
- **Must not:** Equate video availability with transcript availability.

### 14. YouTube unavailable; identity still unresolved
- **Know:** oEmbed 404 / unavailable.
- **Ask:** Identity still open; video not a path.
- **Act:** `decision=NO_ACTION` on video; pursue PDF/`HUMAN_IDENTITY_REVIEW` if any; residual identity uncertainty remains.
- **Must not:** Infer identity from unavailability.

### 15. Vimeo/Rumble with thin relationship context
- **Know:** Few rows; Rumble often `not_checked` access.
- **Ask:** Availability/access first, then identity.
- **Act:** `VERIFY_AVAILABILITY` then likely `decision=DEFER` / `HUMAN_IDENTITY_REVIEW`.
- **Must not:** Broad-scrape replacements.

### 16. Strong Otter exists; another video adds little
- **Know:** Text stack local; captions unknown.
- **Ask:** Is there a specific AV-only evidence need?
- **Act:** `decision=NO_ACTION` or `decision=DEFER` with `decision_reason=EXISTING_REPRESENTATION_SUFFICIENT` / `COST_EXCEEDS_EXPECTED_GAIN`.
- **Must not:** Acquire “because video exists.”

### 17. Still unresolved after cheapest action
- **Know:** e.g. PDF downloaded in a later pass but identity still ambiguous.
- **Ask:** Same or refined question.
- **Act:** Reassessment → `residual_uncertainty=still_unresolved`; new ERC or human review; no automatic escalation to Whisper.
- **Must not:** Pretend resolution.

### 18. Catalog record may be a series/container
- **Know:** Title/structure suggests multiple sessions.
- **Ask:** Container vs single session?
- **Act:** `representation_uncertainty` + human scoping; split candidates later.
- **Must not:** Force single-session acquisition semantics.

---

## 15. Unit tests (implementation checklist)

Map directly to §13 invariants. Minimum automated checks when Pass 4.5 is implemented:

- Reject ERC authorization rows with empty `evidence_question`.
- Reject actions that set session identity or Knowledge promotion in `authorized_to_establish` without an explicit future-pass type (default deny).
- Preserve `candidate_multiplicity` and full candidate list on write.
- Flag ERCs that choose video-class work while an available PDF alternative exists without `why_this_action`.
- Flag any write that mutates Pass 1–4 files.
- Accept `residual_uncertainty=still_unresolved` as successful case completion.
- Reject `decision=AUTHORIZE_ACTION` without `human_authorization_record`.
- Reject bare Pass 4 `record_id` as the only provenance when representation type is needed; require `pass4_row_id` / row key.

---

## 16. Open questions

1. **Missing BDS docs:** When `BDS/BDS-Evidence-Specification.md` / `BDS/BDS-Scope-Charter.md` land, field names may need alignment — content of this MVP should remain stable.
2. **ERC grain:** Always 1:1 with Pass 4 rows, vs group-by-catalog-record with representation-specific actions — implementer may choose either if invariants hold.
3. **Whether `INSPECT_METADATA` may touch network** in Pass 4.5 vs only propose it for Pass 5 — recommend: Pass 4.5 proposes only; any network side effect waits for authorization + execution pass.
4. **Authorization UX:** CLI checklist vs signed markdown log — not specified here.
5. **How many ERCs to open in the first implementation batch** — product choice, not design blocker (likely start from Pass 4 `ACQUIRE_CANDIDATE` + `CONDITIONAL_ACQUIRE` PDFs only).

---

## 17. What not to add yet

- Full evidence scoring / clinical evidence grades
- Automatic Knowledge Object creation
- Automatic session or duplicate merging
- Automatic pathway assignment
- Graph database
- Epistemic confidence numerics
- Auto transcription / OCR / content generation
- Patient-facing interpretation
- Monetization or clinical importance ranking
- `DOWNLOAD_VIDEO` / Whisper as default actions

---

## 18. Suggested future outputs (not created now)

When implemented, Pass 4.5 should emit approximately:

- `Research/lectures/audit/evidence-resolution-cases-pass-4.5.csv`
- `Research/lectures/audit/evidence-resolution-authorization-pass-4.5.md`

Exact schemas must follow this design’s vocabulary and invariants.

---

## 19. GO / NO-GO

`GO — Pass 4.5 is sufficiently specified for implementation.`

Implementation must still:

- treat this as authorization design, not a downloader;
- keep Pass 1–4 frozen;
- start narrow (PDF-centered ERCs from Pass 4 acquire/conditional sets);
- leave video, Whisper, OCR, and Knowledge promotion for later authorized passes.

Residual open questions in §16 are non-blocking for a minimal ERC + authorization MVP.

---

## 20. Implementation clarifications (minimal; no redesign)

These pin ambiguities discovered in a pre-implementation review. They do **not** change Pass 4.5 purpose or scope.

### 20.1 Canonical tokens

- **`next_evidence_action` vocabulary in §7.2 is canonical.** §14 walkthroughs must use those exact tokens (`DOWNLOAD_PDF`, `VERIFY_AVAILABILITY`, `COMPARE_REPRESENTATIONS`, `INSPECT_METADATA`, `RECOVER_LOCAL_REPRESENTATION`, `RECOVER_EXTERNAL_MACHINE_REPRESENTATION`, `HUMAN_IDENTITY_REVIEW`, `DEFER` is **not** used as an action when the gate decision is defer — see §20.2).
- Field name for preferability note is **`why_this_action`** everywhere (including invariants).
- Residual value for unresolved is **`still_unresolved`** (not a synonym).

### 20.2 `decision` vs `next_evidence_action`

| Field | Role |
|---|---|
| `decision` | Gate outcome: `AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NO_ACTION` / `NEEDS_HUMAN_SCOPING` |
| `next_evidence_action` | The concrete candidate action under consideration (from §7.2), including `NO_ACTION` when none |

Rules:

- If `decision=DEFER`, set `next_evidence_action` to the **deferred candidate action** (e.g. `DOWNLOAD_PDF`) or `NO_ACTION` if none; do not set action=`DEFER`.
- If `decision=NO_ACTION`, set `next_evidence_action=NO_ACTION`.
- If `decision=AUTHORIZE_ACTION`, `next_evidence_action` must be a concrete side-effecting or review action from §7.2 other than `NO_ACTION`.
- `authorization_state=authorized` **iff** `decision=AUTHORIZE_ACTION` **and** `human_authorization_record` is present.
- `authorization_state=denied` iff `decision=DENY_ACTION` with human record; `deferred` iff `decision=DEFER` with human record (or system defer awaiting human); `pending` while awaiting human gate.

### 20.3 Pass 4 join key

Pass 4 `record_id` identifies the **catalog record**, not the representation row. It is **not unique** across Pass 4 rows (PDF + video share one `record_id`).

**Pass 4 row key** = `(record_id, external_representation_type)`  
Optional synthetic: `pass4_row_id = "{record_id}::{external_representation_type}"`

`pass4_row_ids` on an ERC must reference that row key (or synthetic id), not bare `record_id` alone.

Shared `external_url` across catalog records is allowed. Same URL ⇒ shared representation object / custody; **not** independent evidence.

### 20.4 `candidate_session_refs` parsing

From Pass 4 `otter_id`: split on `;`, trim whitespace, drop empties, preserve order.  
`candidate_multiplicity = len(candidate_session_refs)`.

Blank Pass 4 `pass1_match_class` is allowed → store blank/unknown; **do not** coerce to `no_match`.

### 20.5 MVP grain and first batch

For the first implementation batch:

1. Select Pass 4 rows where `external_representation_type=AOSRD_PDF` and `acquisition_decision ∈ {ACQUIRE_CANDIDATE, CONDITIONAL_ACQUIRE}` (66 rows: 31 + 35).
2. Emit **one ERC per selected Pass 4 row** (1:1 grain).
3. Do **not** group PDF+video in this batch.
4. Pass 4.5 performs **no network I/O and no downloads**.

### 20.6 Seeding rules (PDF batch)

| Pass 4 `acquisition_decision` | Seed `evidence_purpose` | Seed `next_evidence_action` | Seed `decision` / `authorization_state` |
|---|---|---|---|
| `ACQUIRE_CANDIDATE` + `pass1_match_class=no_match` | `unlinked_source_investigation` | `DOWNLOAD_PDF` | `NEEDS_HUMAN_SCOPING` or leave pending human gate (`authorization_state=pending`) — **never auto-authorize** |
| `ACQUIRE_CANDIDATE` + `pass1_match_class=strong` (or `likely`) | `representation_enrichment` | `DOWNLOAD_PDF` | pending (as above) |
| `CONDITIONAL_ACQUIRE` | `identity_resolution` | `DOWNLOAD_PDF` | pending (as above) |

Default `authorized_to_establish` proposal for all of the above:

`bytes_in_custody` + `explicitly_not_session_identity` + `explicitly_not_knowledge_object`

Every seeded ERC must include a non-empty `evidence_question` before `AUTHORIZE_ACTION` is legal.

### 20.7 `residual_uncertainty` lifecycle

| When | `residual_uncertainty` |
|---|---|
| ERC created, awaiting human | `not_applicable` |
| `decision=DEFER` / `DENY_ACTION` / `NO_ACTION` | set now (`still_unresolved` or `not_applicable` as appropriate) |
| `decision=AUTHORIZE_ACTION` | `not_applicable` until a **later execution/reassessment** pass runs |
| After later execution | `still_unresolved` / `reduced` / `resolved` |

Pass 4.5 still **ends at authorization**; it only reserves the residual field and fills it for non-authorize outcomes.

### 20.8 Minimal output columns for `evidence-resolution-cases-pass-4.5.csv`

Use §7.1 field names as columns. MVP stable order:

`erc_id, catalog_record_id, pass4_row_id, pass4_row_ids, primary_representation_ref, primary_representation_type, primary_representation_url, alternate_representation_refs, uncertainty_class, evidence_question, evidence_purpose, pass1_match_class_frozen, candidate_session_refs, candidate_multiplicity, temporal_relation, local_representation_state, external_availability_state, access_state, authorization_state, next_evidence_action, action_cost_class, why_this_action, decision, decision_reason, authorized_to_establish, residual_uncertainty, human_authorization_record, notes`

Notes:

- `pass4_row_id` is the synthetic key from §20.3 (`{record_id}::{external_representation_type}`).
- `primary_representation_type` / `primary_representation_url` denormalize `primary_representation_ref` for join convenience.
- `primary_representation_ref` may also be serialized as `type|url`.

### 20.9 Authorization log (`evidence-resolution-authorization-pass-4.5.md`)

For each ERC that leaves `pending`, record a subsection:

- `erc_id`, catalog title, representation URL
- evidence question + purpose
- proposed action + epistemic ceiling
- human decision (`AUTHORIZE_ACTION` / `DENY_ACTION` / `DEFER` / `NEEDS_HUMAN_SCOPING`)
- actor + timestamp + caveat

Until a human acts, the log may list the batch as **pending authorization** (proposal inventory), which is still a valid Pass 4.5 output.

### 20.10 Additional invariants

16. `authorization_state=authorized` iff `decision=AUTHORIZE_ACTION` and `human_authorization_record` is present.  
17. Identical `primary_representation_url` across ERCs does not create independent evidence; note shared representation in `notes` or alternate refs.  
18. Pass 4.5 MVP writes audit outputs only; it does not mutate Pass 1–4 files or source packets and performs no network acquisition.
