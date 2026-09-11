# Pass 4.5 Human Authorization — Validation Report

- Generated: 2026-09-10T22:15:45Z
- Source ERC dataset: `Research/lectures/audit/evidence-resolution-cases-pass-4.5.csv`
- Ledger used: `Research/lectures/audit/evidence-resolution-human-authorization-pass-4.5.csv`

## Counts

| Metric | Count |
|---|---:|
| Total ERCs | 66 |
| AUTHORIZE | 54 |
| DEFER | 10 |
| DENY | 2 |
| pending | 0 |
| NEEDS_HUMAN_SCOPING remaining | 0 |
| duplicate ERC short IDs | 0 |
| duplicate erc_id | 0 |
| missing ERC IDs (001–066) | 0 |
| conflicting ledger↔ERC rows | 0 |

## Expected totals (corrected)

| Metric | Expected | Actual |
|---|---:|---:|
| AUTHORIZE | 54 | 54 |
| DEFER | 10 | 10 |
| DENY | 2 | 2 |

Prior incorrect aggregate expectation of 48/16/2 has been withdrawn.
Per-ERC decisions were not modified.

## Mapping

- Authoritative ERC identifier field: `erc_id` (pattern `erc-4.5-pdf-NNN-...`)
- Short form `ERC-NNN` maps to `pdf-NNN` in `erc_id` (verified 1:1 for 001–066)
- No ambiguous matches
- No decisions inferred from Pass 4

## DEFER / DENY inventory

### DEFER

- ERC-005 `erc-4.5-pdf-005-aosrd-webinars-095-DiZKcMJiLs8` — aosrd-webinars-095-DiZKcMJiLs8
- ERC-018 `erc-4.5-pdf-018-aosrd-webinars-171-wSFbd7D8Lpw` — aosrd-webinars-171-wSFbd7D8Lpw
- ERC-030 `erc-4.5-pdf-030-aosrd-webinars-186-hUswEBL-LBc` — aosrd-webinars-186-hUswEBL-LBc
- ERC-031 `erc-4.5-pdf-031-aosrd-webinars-189-bMobTwHmWhM` — aosrd-webinars-189-bMobTwHmWhM
- ERC-033 `erc-4.5-pdf-033-aosrd-webinars-191-ZrOMyfW29og` — aosrd-webinars-191-ZrOMyfW29og
- ERC-037 `erc-4.5-pdf-037-aosrd-webinars-197-92sBrfKcyfE` — aosrd-webinars-197-92sBrfKcyfE
- ERC-053 `erc-4.5-pdf-053-aosrd-webinars-235-4ErgdNqYbRc` — aosrd-webinars-235-4ErgdNqYbRc
- ERC-055 `erc-4.5-pdf-055-aosrd-webinars-237-p59K6kGBP-Y` — aosrd-webinars-237-p59K6kGBP-Y
- ERC-057 `erc-4.5-pdf-057-aosrd-webinars-241-nqr6cW4Gw_A` — aosrd-webinars-241-nqr6cW4Gw_A
- ERC-065 `erc-4.5-pdf-065-aosrd-webinars-280-gLzMZA_eM5g` — aosrd-webinars-280-gLzMZA_eM5g

### DENY

- ERC-064 `erc-4.5-pdf-064-aosrd-webinars-268-2cecK4Jk2vw` — aosrd-webinars-268-2cecK4Jk2vw
- ERC-066 `erc-4.5-pdf-066-aosrd-webinars-283-cxoIpMhdeJw` — aosrd-webinars-283-cxoIpMhdeJw

## Invariants

- Human decision is authorization only
- Pass 1–4 datasets not modified
- Evidence questions / candidate lists / match classes / multiplicity unchanged
- No downloads performed
- No acquisition units executed
- Per-ERC AUTHORIZE/DEFER/DENY decisions unchanged in this correction pass

## Final status

**READY_FOR_PASS_5_PREFLIGHT**

## Final invariant

This operation materializes human authorization only. It does not establish
session identity, lecture novelty, evidence independence, clinical truth, or
Knowledge Object status.
