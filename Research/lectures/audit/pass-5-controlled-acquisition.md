# Pass 5 — Controlled Acquisition

## Integrity statement

Pass 5 acquired only representations authorized through the Pass 4.5
human authorization gate. Acquisition establishes custody/preservation
of the representation only. It does not establish session identity,
lecture novelty, evidence independence, clinical truth, or Knowledge
Object status.

## Authority source

- ERC inventory: `Research/lectures/audit/evidence-resolution-cases-pass-4.5.csv`
- Human authorization ledger: `Research/lectures/audit/evidence-resolution-human-authorization-pass-4.5.csv`
- Pass 4 was **not** used as authorization authority

## Pre-flight result

**`PASS`**

Failures / notices:

- none

## Counts (calculated from actual datasets)

| Metric | Count |
|---|---:|
| Total ERCs reviewed | 66 |
| AUTHORIZE | 54 |
| DEFER | 10 |
| DENY | 2 |
| PENDING / invalid / incomplete | 0 |
| Unique authorized representations (acquisition units) | 54 |
| Shared representation units | 0 |
| ERCs served by shared units | 0 |
| Already preserved locally | 0 |
| Successfully acquired | 0 |
| Failed acquisitions | 0 |
| Unexpected representations | 0 |
| Byte-identical matches across distinct URLs | 0 |
| Exceptions requiring review | 0 |
| Not acquired (DEFER/DENY inventory rows) | 12 |

## Blocker (if any)

Pre-flight passed; acquisition executed for authorized units only.

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
PASS 5 ACQUISITION COMPLETE FOR AUTHORIZED UNITS ONLY.
PASS 4.5 AUTHORIZATION GATE ENFORCED.
NO SESSION IDENTITY INFERRED.
NO KNOWLEDGE OBJECTS CREATED.
NO OCR / TRANSCRIPTION / EMBEDDINGS.
NO PASS 1–4 FILES MODIFIED.
```
