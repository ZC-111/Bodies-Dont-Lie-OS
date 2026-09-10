# Pass 5 — Controlled Acquisition

## Integrity statement

Pass 5 acquired only representations authorized through the Pass 4.5
human authorization gate. Acquisition establishes custody/preservation
of the representation only. It does not establish session identity,
lecture novelty, evidence independence, clinical truth, or Knowledge
Object status.

## Authority source

- ERC inventory: `Research/lectures/audit/evidence-resolution-cases-pass-4.5.csv`
- Human authorization ledger: `NOT FOUND — fell back to ERC CSV authorization fields`
- Pass 4 was **not** used as authorization authority

## Pre-flight result

**`FAIL — DOWNLOADS BLOCKED`**

Failures / notices:

- ZERO_AUTHORIZE_DECISIONS: no ERC has completed human AUTHORIZE; cannot acquire
- INCOMPLETE_AUTHORIZATION_LEDGER: PENDING=66 INVALID=0

## Counts (calculated from actual datasets)

| Metric | Count |
|---|---:|
| Total ERCs reviewed | 66 |
| AUTHORIZE | 0 |
| DEFER | 0 |
| DENY | 0 |
| PENDING / invalid / incomplete | 66 |
| Unique authorized representations (acquisition units) | 0 |
| Shared representation units | 0 |
| ERCs served by shared units | 0 |
| Already preserved locally | 0 |
| Successfully acquired | 0 |
| Failed acquisitions | 0 |
| Unexpected representations | 0 |
| Byte-identical matches across distinct URLs | 0 |
| Exceptions requiring review | 66 |
| Not acquired (DEFER/DENY inventory rows) | 0 |

## Blocker (if any)

Pass 5 **did not download** because the Pass 4.5 human authorization
gate is incomplete in the repository. Expected completed decisions
(`AUTHORIZE` / `DEFER` / `DENY`) were not present on ERC-001–066.

Observed: all seeded ERCs remain `authorization_state=pending` /
`decision=NEEDS_HUMAN_SCOPING`.

To unblock: record explicit human decisions in the ERC CSV fields
(`authorization_state`, `decision`, `human_authorization_record`)
and/or provide
`Research/lectures/audit/evidence-resolution-human-authorization-pass-4.5.csv`,
then re-run:

```bash
python3 Research/lectures/scripts/pass_5_controlled_acquisition.py
```

Do **not** infer AUTHORIZE from Pass 4 `ACQUIRE_CANDIDATE`,
`DOWNLOAD_PDF`, or external availability.

## Why AUTHORIZE count may differ from acquisition-unit count

Multiple ERCs may authorize the **same** representation URL. Pass 5 consolidates those into one acquisition unit (one download / one hash), while preserving all ERC and catalog relationships in the crosswalk.

## Known shared-URL checks (dataset)

| URL pattern | Catalog IDs |
|---|---|
| Biological Dentistry PDF | aosrd-webinars-224-…, aosrd-webinars-241-… |
| Integrative Immuno-Oncology page URL | aosrd-webinars-235-…, aosrd-webinars-237-… |
| Oxytocin page URL | aosrd-webinars-197-…, aosrd-webinars-202-… |

Consolidation applies **only** among ERCs that are AUTHORIZE. A DEFER/DENY ERC sharing a URL does not authorize acquisition by itself.

## Epistemic ceiling

All acquisition units carry:

`bytes_in_custody` + `explicitly_not_session_identity` + `explicitly_not_knowledge_object`

## Outputs

- `Research/lectures/audit/pass-5-preflight-report.csv`
- `Research/lectures/audit/pass-5-controlled-acquisition-plan.csv`
- `Research/lectures/audit/pass-5-acquisition-manifest.csv`
- `Research/lectures/audit/pass-5-erc-acquisition-crosswalk.csv`
- `Research/lectures/audit/pass-5-acquisition-exceptions.csv`
- `Research/lectures/audit/pass-5-not-acquired.csv`
- `Research/lectures/audit/pass-5-controlled-acquisition.md` (this file)
- Per-unit dirs under `Research/lectures/acquired/aosrd-pdf/` (only if downloads executed)

## STOP

```
PASS 5 PREFLIGHT FAILED; NO DOWNLOADS PERFORMED.
PASS 4.5 AUTHORIZATION GATE ENFORCED.
NO SESSION IDENTITY INFERRED.
NO KNOWLEDGE OBJECTS CREATED.
NO OCR / TRANSCRIPTION / EMBEDDINGS.
NO PASS 1–4 FILES MODIFIED.
```
