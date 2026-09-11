#!/usr/bin/env python3
"""Pass 5 — Controlled acquisition of Pass 4.5–authorized representations.

Authority: Pass 4.5 human authorization only (AUTHORIZE / DEFER / DENY).
Does NOT infer authorization from Pass 4, availability, or ACQUIRE_CANDIDATE.
Does NOT create Knowledge Objects, promote identity, OCR, or process content.

Epistemic ceiling: bytes_in_custody only.
"""

from __future__ import annotations

import csv
import hashlib
import json
import mimetypes
import os
import re
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[3]
AUDIT = ROOT / "Research" / "lectures" / "audit"
ACQUIRED_ROOT = ROOT / "Research" / "lectures" / "acquired" / "aosrd-pdf"

ERC_CSV = AUDIT / "evidence-resolution-cases-pass-4.5.csv"
# Optional override ledger; if present and complete, overrides ERC CSV fields.
LEDGER_CANDIDATES = [
    AUDIT / "evidence-resolution-human-authorization-pass-4.5.csv",
    AUDIT / "evidence-resolution-human-authorization-pass-4.5.csv",
    AUDIT / "pass-4.5-human-authorization-ledger.csv",
]

OUT_PLAN = AUDIT / "pass-5-controlled-acquisition-plan.csv"
OUT_MANIFEST = AUDIT / "pass-5-acquisition-manifest.csv"
OUT_CROSSWALK = AUDIT / "pass-5-erc-acquisition-crosswalk.csv"
OUT_EXCEPTIONS = AUDIT / "pass-5-acquisition-exceptions.csv"
OUT_NOT_ACQUIRED = AUDIT / "pass-5-not-acquired.csv"
OUT_PREFLIGHT = AUDIT / "pass-5-preflight-report.csv"
OUT_PREFLIGHT_MD = AUDIT / "pass-5-preflight.md"
OUT_SUMMARY = AUDIT / "pass-5-controlled-acquisition.md"

USER_AGENT = "BodiesDontLie-OS-Pass5/1.0 (+controlled-acquisition; audit-only)"
DOWNLOAD_TIMEOUT_SEC = 60
MAX_BYTES = 80 * 1024 * 1024  # safety ceiling

# Tracking params only when already a common, explicit normalization set.
STRIP_QUERY_KEYS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "gclid",
}

AUTHORIZE_STATES = {
    "AUTHORIZE",
    "AUTHORIZE_ACTION",
    "AUTHORIZE_ACTION",
    "AUTHORIZED",
    "authorized",
}
DEFER_STATES = {"DEFER", "DEFERRED", "deferred"}
DENY_STATES = {"DENY", "DENY_ACTION", "DENY_ACTION", "DENIED", "denied"}
PENDING_STATES = {
    "PENDING",
    "pending",
    "NEEDS_HUMAN_SCOPING",
    "NEEDS_HUMAN_SCOPING",
    "",
}

PLAN_FIELDS = [
    "acquisition_unit_id",
    "representation_type",
    "source_system",
    "external_url_original",
    "external_url_canonical",
    "canonicalization_status",
    "authorized_erc_ids",
    "catalog_record_ids",
    "acquisition_purpose",
    "shared_representation",
    "erc_reference_count",
    "local_presence_status",
    "pass4_5_authorization_state",
    "epistemic_ceiling",
    "notes",
]

MANIFEST_FIELDS = [
    "acquisition_unit_id",
    "representation_type",
    "source_system",
    "external_url_original",
    "external_url_canonical",
    "acquisition_timestamp",
    "acquisition_status",
    "http_status",
    "content_type_declared",
    "content_type_detected",
    "byte_size",
    "sha256",
    "local_path",
    "authorized_erc_ids",
    "catalog_record_ids",
    "pass4_decisions",
    "pass4_5_authorization_state",
    "acquisition_purpose",
    "candidate_session_refs",
    "candidate_multiplicity",
    "identity_uncertainty",
    "epistemic_ceiling",
    "shared_representation",
    "same_bytes_as_acquisition_unit",
    "content_hash_match",
    "notes",
]

CROSSWALK_FIELDS = [
    "erc_id",
    "erc_short_id",
    "authorization_state",
    "catalog_record_id",
    "representation_type",
    "external_url_original",
    "external_url_canonical",
    "acquisition_unit_id",
    "local_path",
    "sha256",
    "acquisition_status",
    "relationship_role",
    "notes",
]

EXCEPTION_FIELDS = [
    "exception_id",
    "exception_class",
    "erc_id",
    "acquisition_unit_id",
    "catalog_record_id",
    "external_url",
    "detail",
    "requires_human_review",
]

NOT_ACQUIRED_FIELDS = [
    "erc_id",
    "catalog_record_id",
    "external_url",
    "pass4_decision",
    "pass4_5_human_decision",
    "reason_or_defer_state",
    "candidate_multiplicity",
    "identity_uncertainty",
]

PREFLIGHT_FIELDS = [
    "erc_id",
    "authorization_state",
    "representation_type",
    "external_url",
    "acquisition_purpose",
    "catalog_record",
    "shared_representation_status",
    "acquisition_unit_id",
    "local_presence_status",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def normalize_auth_token(raw: str) -> str:
    return (raw or "").strip()


def classify_auth(state: str, decision: str) -> str:
    """Return AUTHORIZE | DEFER | DENY | PENDING | INVALID."""
    tokens = [normalize_auth_token(state), normalize_auth_token(decision)]
    upper = {t.upper() for t in tokens if t}
    # Prefer explicit deny/defer over authorize if conflict → INVALID later
    has_auth = any(t in AUTHORIZE_STATES or t.upper() in {x.upper() for x in AUTHORIZE_STATES} for t in tokens)
    has_defer = any(t in DEFER_STATES or t.upper() in {x.upper() for x in DEFER_STATES} for t in tokens)
    has_deny = any(t in DENY_STATES or t.upper() in {x.upper() for x in DENY_STATES} for t in tokens)
    has_pending = any(
        (not t) or t in PENDING_STATES or t.upper() in {x.upper() for x in PENDING_STATES}
        for t in tokens
    )

    # Map design-spec vocabulary
    if (
        "AUTHORIZED" in upper
        or "AUTHORIZE" in upper
        or "AUTHORIZE_ACTION" in upper
        or "AUTHORIZE_ACTION" in upper
        or any(t.startswith("AUTHORIZE") for t in upper)
    ):
        has_auth = True
    if "DEFERRED" in upper or "DEFER" in upper:
        has_defer = True
    if (
        "DENIED" in upper
        or "DENY" in upper
        or "DENY_ACTION" in upper
        or "DENY_ACTION" in upper
        or any(t.startswith("DENY") for t in upper)
    ):
        has_deny = True
    if (
        "PENDING" in upper
        or "NEEDS_HUMAN_SCOPING" in upper
        or "NEEDS_HUMAN_SCOPING" in upper
        or any("NEEDS_HUMAN" in t for t in upper)
    ):
        has_pending = True

    decisive = sum(bool(x) for x in (has_auth, has_defer, has_deny))
    if decisive > 1:
        return "INVALID"
    if has_auth:
        return "AUTHORIZE"
    if has_defer:
        return "DEFER"
    if has_deny:
        return "DENY"
    if has_pending and decisive == 0:
        return "PENDING"
    return "INVALID"


def canonicalize_url(url: str) -> tuple[str, str]:
    """Return (canonical, status) where status is ok|ambiguous|empty."""
    original = (url or "").strip()
    if not original:
        return "", "empty"
    try:
        parts = urlsplit(original)
    except Exception:
        return original, "ambiguous"
    if parts.scheme not in ("http", "https") or not parts.netloc:
        return original, "ambiguous"
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()
    if netloc.endswith(":80") and scheme == "http":
        netloc = netloc[:-3]
    if netloc.endswith(":443") and scheme == "https":
        netloc = netloc[:-4]
    path = parts.path or ""
    # Collapse only empty trailing? Keep path; drop fragment.
    query_pairs = parse_qsl(parts.query, keep_blank_values=True)
    kept = [(k, v) for k, v in query_pairs if k.lower() not in STRIP_QUERY_KEYS]
    # If we stripped unknown-looking aggressive transforms needed, mark ambiguous
    query = urlencode(kept, doseq=True)
    canonical = urlunsplit((scheme, netloc, path, query, ""))
    return canonical, "ok"


def erc_short_id(erc_id: str, index_1based: int) -> str:
    m = re.search(r"pdf-(\d+)", erc_id or "", re.I)
    if m:
        return f"ERC-{int(m.group(1)):03d}"
    return f"ERC-{index_1based:03d}"


def load_ledger() -> dict[str, dict[str, str]] | None:
    for path in LEDGER_CANDIDATES:
        if path.is_file() and path.stat().st_size > 0:
            with path.open(newline="", encoding="utf-8") as f:
                rows = list(csv.DictReader(f))
            if not rows:
                continue
            out: dict[str, dict[str, str]] = {}
            for r in rows:
                key = (r.get("erc_id") or r.get("ERC_ID") or "").strip()
                if not key:
                    continue
                out[key] = r
            if out:
                return out
    return None


def load_ercs() -> list[dict[str, Any]]:
    with ERC_CSV.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    ledger = load_ledger()
    enriched = []
    for i, r in enumerate(rows, 1):
        erc = dict(r)
        erc["_index"] = i
        erc["_short_id"] = erc_short_id(erc.get("erc_id", ""), i)
        if ledger and erc.get("erc_id") in ledger:
            lr = ledger[erc["erc_id"]]
            # Ledger fields override authorization fields only
            for k in (
                "authorization_state",
                "decision",
                "human_authorization_record",
                "acquisition_purpose",
                "notes",
            ):
                if lr.get(k):
                    erc[k] = lr[k]
            # Allow human_decision / pass4_5_authorization_state aliases
            if lr.get("human_decision"):
                erc["decision"] = lr["human_decision"]
                erc["authorization_state"] = lr["human_decision"]
            if lr.get("pass4_5_authorization_state"):
                erc["authorization_state"] = lr["pass4_5_authorization_state"]
        auth = classify_auth(erc.get("authorization_state", ""), erc.get("decision", ""))
        erc["_auth"] = auth
        url_orig = (erc.get("primary_representation_url") or "").strip()
        canon, canon_status = canonicalize_url(url_orig)
        erc["_url_original"] = url_orig
        erc["_url_canonical"] = canon
        erc["_canon_status"] = canon_status
        purpose = (
            erc.get("evidence_purpose")
            or erc.get("acquisition_purpose")
            or "unknown"
        ).strip()
        # Map Pass 4.5 purpose vocabulary into Pass 5 allowed set when possible
        purpose_map = {
            "unlinked_source_investigation": "new_session_candidate",
            "identity_resolution": "identity_resolution",
            "representation_enrichment": "representation_enrichment",
        }
        erc["_purpose"] = purpose_map.get(purpose, purpose if purpose else "unknown")
        # Extract Pass 4 decision from notes if present
        notes = erc.get("notes") or ""
        m = re.search(r"pass4_acquisition_decision=([A-Z_]+)", notes)
        erc["_pass4_decision"] = m.group(1) if m else "unknown"
        enriched.append(erc)
    return enriched


def detect_local_presence(url_original: str, url_canonical: str) -> str:
    """Check whether exact representation already preserved under acquired/."""
    if not ACQUIRED_ROOT.is_dir():
        return "not_present"
    # Look for acquisition.json files pointing at same canonical/original URL
    matches = []
    for meta in ACQUIRED_ROOT.glob("AU-*/acquisition.json"):
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
        except Exception:
            continue
        if data.get("external_url_canonical") == url_canonical or data.get(
            "external_url_original"
        ) == url_original:
            if data.get("acquisition_status") in {
                "complete",
                "already_preserved_locally",
                "success",
            }:
                matches.append(data.get("acquisition_unit_id") or meta.parent.name)
    if len(matches) == 1:
        return f"already_preserved_locally:{matches[0]}"
    if len(matches) > 1:
        return "local_presence_uncertain"
    # Also check known pilot path without guessing identity
    return "not_present"


def build_acquisition_units(ercs: list[dict[str, Any]]) -> tuple[list[dict], list[dict], list[dict]]:
    exceptions: list[dict] = []
    not_acquired: list[dict] = []
    auth_by_canon: dict[str, list[dict]] = defaultdict(list)

    for erc in ercs:
        auth = erc["_auth"]
        if auth == "PENDING" or auth == "INVALID":
            exceptions.append(
                {
                    "exception_id": f"EX-AUTH-{erc['_short_id']}",
                    "exception_class": "missing_or_invalid_authorization_state",
                    "erc_id": erc.get("erc_id"),
                    "acquisition_unit_id": "",
                    "catalog_record_id": erc.get("catalog_record_id"),
                    "external_url": erc["_url_original"],
                    "detail": f"authorization_state={erc.get('authorization_state')!r} decision={erc.get('decision')!r} classified={auth}",
                    "requires_human_review": "true",
                }
            )
            continue
        if auth in ("DEFER", "DENY"):
            not_acquired.append(
                {
                    "erc_id": erc.get("erc_id"),
                    "catalog_record_id": erc.get("catalog_record_id"),
                    "external_url": erc["_url_original"],
                    "pass4_decision": erc.get("_pass4_decision"),
                    "pass4_5_human_decision": auth,
                    "reason_or_defer_state": erc.get("decision_reason")
                    or erc.get("human_authorization_record")
                    or auth,
                    "candidate_multiplicity": erc.get("candidate_multiplicity"),
                    "identity_uncertainty": erc.get("uncertainty_class")
                    or erc.get("pass1_match_class_frozen")
                    or "unknown",
                }
            )
            continue
        # AUTHORIZE
        if not erc["_url_original"]:
            exceptions.append(
                {
                    "exception_id": f"EX-URL-{erc['_short_id']}",
                    "exception_class": "authorized_erc_missing_url",
                    "erc_id": erc.get("erc_id"),
                    "acquisition_unit_id": "",
                    "catalog_record_id": erc.get("catalog_record_id"),
                    "external_url": "",
                    "detail": "AUTHORIZE but primary_representation_url empty",
                    "requires_human_review": "true",
                }
            )
            continue
        if not (erc.get("primary_representation_type") or "").strip():
            exceptions.append(
                {
                    "exception_id": f"EX-TYPE-{erc['_short_id']}",
                    "exception_class": "authorized_erc_missing_representation_type",
                    "erc_id": erc.get("erc_id"),
                    "acquisition_unit_id": "",
                    "catalog_record_id": erc.get("catalog_record_id"),
                    "external_url": erc["_url_original"],
                    "detail": "AUTHORIZE but primary_representation_type empty",
                    "requires_human_review": "true",
                }
            )
            continue
        if erc["_canon_status"] == "ambiguous":
            exceptions.append(
                {
                    "exception_id": f"EX-CANON-{erc['_short_id']}",
                    "exception_class": "canonicalization_ambiguity",
                    "erc_id": erc.get("erc_id"),
                    "acquisition_unit_id": "",
                    "catalog_record_id": erc.get("catalog_record_id"),
                    "external_url": erc["_url_original"],
                    "detail": "URL canonicalization uncertain; preserved separately for review",
                    "requires_human_review": "true",
                }
            )
            # Still allow grouping by original if needed — flag but do not invent merge
            key = f"ambiguous::{erc['_url_original']}"
        else:
            key = f"AOSRD_PDF::{erc['_url_canonical'] or erc['_url_original']}"
        auth_by_canon[key].append(erc)

    units: list[dict] = []
    for i, (key, group) in enumerate(sorted(auth_by_canon.items(), key=lambda x: x[0]), 1):
        au_id = f"AU-{i:03d}"
        originals = sorted({e["_url_original"] for e in group})
        canons = sorted({e["_url_canonical"] for e in group if e["_url_canonical"]})
        shared = len(group) > 1
        local = detect_local_presence(originals[0], canons[0] if canons else originals[0])
        if local == "local_presence_uncertain":
            exceptions.append(
                {
                    "exception_id": f"EX-LOCAL-{au_id}",
                    "exception_class": "local_presence_uncertain",
                    "erc_id": ";".join(e.get("erc_id", "") for e in group),
                    "acquisition_unit_id": au_id,
                    "catalog_record_id": ";".join(e.get("catalog_record_id", "") for e in group),
                    "external_url": originals[0],
                    "detail": "Multiple local preserved matches or uncertain presence",
                    "requires_human_review": "true",
                }
            )
        unit = {
            "acquisition_unit_id": au_id,
            "representation_type": group[0].get("primary_representation_type") or "AOSRD_PDF",
            "source_system": "aosrd",
            "external_url_original": originals[0],
            "external_url_canonical": canons[0] if canons else originals[0],
            "canonicalization_status": group[0]["_canon_status"],
            "authorized_erc_ids": ";".join(e.get("erc_id", "") for e in group),
            "catalog_record_ids": ";".join(e.get("catalog_record_id", "") for e in group),
            "acquisition_purpose": ";".join(sorted({e["_purpose"] for e in group})),
            "shared_representation": "true" if shared else "false",
            "erc_reference_count": str(len(group)),
            "local_presence_status": local,
            "pass4_5_authorization_state": "AUTHORIZE",
            "epistemic_ceiling": "bytes_in_custody;explicitly_not_session_identity;explicitly_not_knowledge_object",
            "notes": (
                f"source_type+canonical_url key={key}; "
                f"original_urls={len(originals)}; "
                f"contributing_ercs={len(group)}"
            ),
            "_ercs": group,
            "_key": key,
        }
        if len(originals) > 1:
            exceptions.append(
                {
                    "exception_id": f"EX-ORIG-{au_id}",
                    "exception_class": "canonicalization_ambiguity",
                    "erc_id": unit["authorized_erc_ids"],
                    "acquisition_unit_id": au_id,
                    "catalog_record_id": unit["catalog_record_ids"],
                    "external_url": "|".join(originals),
                    "detail": "Multiple original URL spellings map to one canonical acquisition key",
                    "requires_human_review": "true",
                }
            )
        units.append(unit)
    return units, exceptions, not_acquired


def preflight_check(
    ercs: list[dict], units: list[dict], exceptions: list[dict]
) -> tuple[bool, list[str], list[dict]]:
    failures: list[str] = []
    preflight_rows: list[dict] = []

    unit_by_erc = {}
    for u in units:
        for e in u["_ercs"]:
            unit_by_erc[e.get("erc_id")] = u

    auth_counts = Counter(e["_auth"] for e in ercs)
    if auth_counts.get("AUTHORIZE", 0) == 0:
        failures.append("ZERO_AUTHORIZE_DECISIONS: no ERC has completed human AUTHORIZE; cannot acquire")
    pending = auth_counts.get("PENDING", 0)
    invalid = auth_counts.get("INVALID", 0)
    if pending or invalid:
        failures.append(
            f"INCOMPLETE_AUTHORIZATION_LEDGER: PENDING={pending} INVALID={invalid}"
        )

    # Build preflight rows for all ERCs
    for erc in ercs:
        u = unit_by_erc.get(erc.get("erc_id"))
        shared = "n/a"
        local = "n/a"
        au = ""
        if u:
            shared = u["shared_representation"]
            local = u["local_presence_status"]
            au = u["acquisition_unit_id"]
        elif erc["_auth"] in ("DEFER", "DENY"):
            shared = "not_queued"
            local = "not_applicable"
        else:
            shared = "blocked"
            local = "not_applicable"
        preflight_rows.append(
            {
                "erc_id": erc.get("erc_id"),
                "authorization_state": erc["_auth"],
                "representation_type": erc.get("primary_representation_type"),
                "external_url": erc["_url_original"],
                "acquisition_purpose": erc["_purpose"],
                "catalog_record": erc.get("catalog_record_id"),
                "shared_representation_status": shared,
                "acquisition_unit_id": au,
                "local_presence_status": local,
            }
        )

    # Invariants on units
    for u in units:
        auths = {e["_auth"] for e in u["_ercs"]}
        if "AUTHORIZE" not in auths:
            failures.append(
                f"UNIT_WITHOUT_AUTHORIZE: {u['acquisition_unit_id']} auths={auths}"
            )
        if auths == {"DEFER"}:
            failures.append(f"DEFER_SOLE_AUTH: {u['acquisition_unit_id']}")
        if auths == {"DENY"}:
            failures.append(f"DENY_SOLE_AUTH: {u['acquisition_unit_id']}")

    # Unauthorized must not appear in plan
    for u in units:
        for e in u["_ercs"]:
            if e["_auth"] != "AUTHORIZE":
                failures.append(
                    f"UNAUTHORIZED_IN_PLAN: {e.get('erc_id')} state={e['_auth']} in {u['acquisition_unit_id']}"
                )
                exceptions.append(
                    {
                        "exception_id": f"EX-QUEUE-{e['_short_id']}",
                        "exception_class": "unauthorized_erc_in_acquisition_queue",
                        "erc_id": e.get("erc_id"),
                        "acquisition_unit_id": u["acquisition_unit_id"],
                        "catalog_record_id": e.get("catalog_record_id"),
                        "external_url": e["_url_original"],
                        "detail": "Non-AUTHORIZE ERC appeared in acquisition unit",
                        "requires_human_review": "true",
                    }
                )

    # Duplicate AU construction by key
    keys = [u["_key"] for u in units]
    if len(keys) != len(set(keys)):
        failures.append("DUPLICATE_ACQUISITION_UNIT_CONSTRUCTION")
        exceptions.append(
            {
                "exception_id": "EX-DUP-AU",
                "exception_class": "duplicate_acquisition_unit_construction",
                "erc_id": "",
                "acquisition_unit_id": "",
                "catalog_record_id": "",
                "external_url": "",
                "detail": "Two acquisition units share the same representation key",
                "requires_human_review": "true",
            }
        )

    # Known shared PDF consolidation checks (informational if not yet authorized)
    # Catalog IDs must match the Pass 4.5 ERC dataset exactly.
    known_pairs = [
        (
            "Future of Biological Dentistry",
            "aosrd-webinars-224-qORv5ARtglk",
            "aosrd-webinars-241-nqr6cW4Gw_A",
        ),
        (
            "Integrative Immuno-Oncology",
            "aosrd-webinars-235-4ErgdNqYbRc",
            "aosrd-webinars-237-p59K6kGBP-Y",
        ),
        (
            "Oxytocin",
            "aosrd-webinars-197-92sBrfKcyfE",
            "aosrd-webinars-202-x6BIrL8qmzk",
        ),
    ]
    catalog_to_unit = {}
    for u in units:
        for cid in u["catalog_record_ids"].split(";"):
            catalog_to_unit[cid] = u["acquisition_unit_id"]
    for label, a, b in known_pairs:
        ua, ub = catalog_to_unit.get(a), catalog_to_unit.get(b)
        if ua and ub and ua != ub:
            failures.append(
                f"KNOWN_SHARED_NOT_CONSOLIDATED: {label} ({a}→{ua}, {b}→{ub})"
            )

    # Pass 1–4 immutability check (files exist and we do not write them)
    frozen = [
        AUDIT / "title-reconciliation-pass-1.csv",
        AUDIT / "local-representation-inventory-pass-2.csv",
        AUDIT / "external-representation-availability-pass-3.csv",
        AUDIT / "acquisition-candidate-audit-pass-4.csv",
    ]
    for p in frozen:
        if not p.is_file():
            failures.append(f"MISSING_FROZEN_PASS_FILE: {p.name}")

    ok = len(failures) == 0 and auth_counts.get("AUTHORIZE", 0) > 0
    # Even with AUTHORIZE, incomplete ledger of other ERCs is a hard stop
    if pending or invalid:
        ok = False
    return ok, failures, preflight_rows


def sniff_pdf(data: bytes) -> bool:
    return data[:5] == b"%PDF-"


def detect_content_type(data: bytes, declared: str | None) -> str:
    if sniff_pdf(data):
        return "application/pdf"
    if data.lstrip()[:1] == b"<" or b"<html" in data[:200].lower():
        return "text/html"
    guessed, _ = mimetypes.guess_type("x.bin")
    if declared:
        return declared.split(";")[0].strip() or "application/octet-stream"
    return guessed or "application/octet-stream"


def download_unit(unit: dict) -> dict:
    """Download one acquisition unit to preservation location."""
    ts = utc_now()
    url = unit["external_url_original"]
    au_id = unit["acquisition_unit_id"]
    dest_dir = ACQUIRED_ROOT / au_id
    dest_dir.mkdir(parents=True, exist_ok=True)
    local_name = "original.pdf"
    local_path = dest_dir / local_name

    # Already preserved?
    if unit["local_presence_status"].startswith("already_preserved_locally"):
        existing = unit["local_presence_status"].split(":", 1)[-1]
        result = base_manifest(unit, ts)
        result.update(
            {
                "acquisition_status": "already_preserved_locally",
                "http_status": "n/a",
                "content_type_declared": "unknown",
                "content_type_detected": "unknown",
                "byte_size": "unknown",
                "sha256": "unknown",
                "local_path": str(ACQUIRED_ROOT / existing / "original.pdf"),
                "same_bytes_as_acquisition_unit": existing,
                "content_hash_match": "unknown",
                "notes": "Exact representation already preserved; no redownload",
            }
        )
        write_acquisition_json(dest_dir, result)
        return result

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    http_status = ""
    declared = ""
    try:
        with urllib.request.urlopen(req, timeout=DOWNLOAD_TIMEOUT_SEC) as resp:
            http_status = str(getattr(resp, "status", "") or resp.getcode())
            declared = resp.headers.get("Content-Type", "") or ""
            # Read with size cap
            chunks = []
            total = 0
            while True:
                chunk = resp.read(1024 * 256)
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_BYTES:
                    raise RuntimeError("response_exceeds_max_bytes")
                chunks.append(chunk)
            data = b"".join(chunks)
    except Exception as exc:
        result = base_manifest(unit, ts)
        result.update(
            {
                "acquisition_status": "failed",
                "http_status": http_status or "unknown",
                "content_type_declared": declared or "unknown",
                "content_type_detected": "unknown",
                "byte_size": "0",
                "sha256": "unknown",
                "local_path": "",
                "same_bytes_as_acquisition_unit": "",
                "content_hash_match": "false",
                "notes": f"error_class={type(exc).__name__}; error={exc}",
            }
        )
        write_acquisition_json(dest_dir, result)
        return result

    detected = detect_content_type(data, declared)
    sha = hashlib.sha256(data).hexdigest()
    # Expect PDF for AOSRD_PDF representation type
    is_pdf_type = (unit["representation_type"] or "").upper().endswith("PDF") or unit[
        "representation_type"
    ] == "AOSRD_PDF"
    unexpected = False
    if is_pdf_type and not sniff_pdf(data):
        unexpected = True
    if detected == "text/html":
        unexpected = True

    if unexpected:
        # Preserve failure artifact bytes under a non-success name for audit, but do not claim PDF
        fail_path = dest_dir / "unexpected.bin"
        fail_path.write_bytes(data)
        result = base_manifest(unit, ts)
        result.update(
            {
                "acquisition_status": "unexpected_representation",
                "http_status": http_status,
                "content_type_declared": declared or "unknown",
                "content_type_detected": detected,
                "byte_size": str(len(data)),
                "sha256": sha,
                "local_path": str(fail_path.relative_to(ROOT)),
                "same_bytes_as_acquisition_unit": "",
                "content_hash_match": "false",
                "notes": "Response was not a plausible PDF; not classified as successful PDF acquisition",
            }
        )
        write_acquisition_json(dest_dir, result)
        return result

    # Preserve original bytes
    with tempfile.NamedTemporaryFile(delete=False, dir=dest_dir) as tmp:
        tmp.write(data)
        tmp_path = Path(tmp.name)
    shutil.move(str(tmp_path), str(local_path))

    result = base_manifest(unit, ts)
    result.update(
        {
            "acquisition_status": "complete",
            "http_status": http_status,
            "content_type_declared": declared or "unknown",
            "content_type_detected": detected,
            "byte_size": str(len(data)),
            "sha256": sha,
            "local_path": str(local_path.relative_to(ROOT)),
            "same_bytes_as_acquisition_unit": "",
            "content_hash_match": "false",
            "notes": "original bytes preserved; no content processing",
        }
    )
    write_acquisition_json(dest_dir, result)
    return result


def base_manifest(unit: dict, ts: str) -> dict:
    ercs = unit["_ercs"]
    return {
        "acquisition_unit_id": unit["acquisition_unit_id"],
        "representation_type": unit["representation_type"],
        "source_system": unit["source_system"],
        "external_url_original": unit["external_url_original"],
        "external_url_canonical": unit["external_url_canonical"],
        "acquisition_timestamp": ts,
        "authorized_erc_ids": unit["authorized_erc_ids"],
        "catalog_record_ids": unit["catalog_record_ids"],
        "pass4_decisions": ";".join(e.get("_pass4_decision", "unknown") for e in ercs),
        "pass4_5_authorization_state": "AUTHORIZE",
        "acquisition_purpose": unit["acquisition_purpose"],
        "candidate_session_refs": ";".join(
            (e.get("candidate_session_refs") or "unknown") for e in ercs
        ),
        "candidate_multiplicity": ";".join(
            str(e.get("candidate_multiplicity") or "unknown") for e in ercs
        ),
        "identity_uncertainty": ";".join(
            (e.get("uncertainty_class") or e.get("pass1_match_class_frozen") or "unknown")
            for e in ercs
        ),
        "epistemic_ceiling": unit["epistemic_ceiling"],
        "shared_representation": unit["shared_representation"],
    }


def write_acquisition_json(dest_dir: Path, result: dict) -> None:
    path = dest_dir / "acquisition.json"
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def apply_byte_dedup(manifests: list[dict], exceptions: list[dict]) -> None:
    by_hash: dict[str, list[dict]] = defaultdict(list)
    for m in manifests:
        sha = m.get("sha256") or ""
        if sha and sha != "unknown" and m.get("acquisition_status") in {
            "complete",
            "unexpected_representation",
        }:
            by_hash[sha].append(m)
    for sha, group in by_hash.items():
        if len(group) < 2:
            continue
        # Keep all records; point later ones at the first AU
        primary = group[0]["acquisition_unit_id"]
        urls = {g["external_url_original"] for g in group}
        if len(urls) < 2:
            continue
        for g in group:
            g["content_hash_match"] = "true"
            if g["acquisition_unit_id"] != primary:
                g["same_bytes_as_acquisition_unit"] = primary
            else:
                g["same_bytes_as_acquisition_unit"] = ""
            g["notes"] = (g.get("notes") or "") + "; byte-identical across distinct URLs"
        exceptions.append(
            {
                "exception_id": f"EX-HASH-{primary}",
                "exception_class": "byte_identical_content_from_different_urls",
                "erc_id": ";".join(g["authorized_erc_ids"] for g in group),
                "acquisition_unit_id": ";".join(g["acquisition_unit_id"] for g in group),
                "catalog_record_id": ";".join(g["catalog_record_ids"] for g in group),
                "external_url": "|".join(sorted(urls)),
                "detail": f"sha256={sha}; records preserved; no deletion",
                "requires_human_review": "true",
            }
        )


def build_crosswalk(
    ercs: list[dict], units: list[dict], manifests: list[dict]
) -> list[dict]:
    man_by_au = {m["acquisition_unit_id"]: m for m in manifests}
    unit_by_erc = {}
    for u in units:
        for e in u["_ercs"]:
            unit_by_erc[e.get("erc_id")] = u
    rows = []
    for erc in ercs:
        u = unit_by_erc.get(erc.get("erc_id"))
        m = man_by_au.get(u["acquisition_unit_id"]) if u else None
        if erc["_auth"] == "AUTHORIZE" and u:
            role = (
                "shared_representation_contributor"
                if u["shared_representation"] == "true"
                else "sole_authorization"
            )
            rows.append(
                {
                    "erc_id": erc.get("erc_id"),
                    "erc_short_id": erc["_short_id"],
                    "authorization_state": "AUTHORIZE",
                    "catalog_record_id": erc.get("catalog_record_id"),
                    "representation_type": erc.get("primary_representation_type"),
                    "external_url_original": erc["_url_original"],
                    "external_url_canonical": erc["_url_canonical"],
                    "acquisition_unit_id": u["acquisition_unit_id"],
                    "local_path": (m or {}).get("local_path", ""),
                    "sha256": (m or {}).get("sha256", ""),
                    "acquisition_status": (m or {}).get("acquisition_status", "planned"),
                    "relationship_role": role,
                    "notes": "representation reuse ≠ session identity",
                }
            )
        else:
            rows.append(
                {
                    "erc_id": erc.get("erc_id"),
                    "erc_short_id": erc["_short_id"],
                    "authorization_state": erc["_auth"],
                    "catalog_record_id": erc.get("catalog_record_id"),
                    "representation_type": erc.get("primary_representation_type"),
                    "external_url_original": erc["_url_original"],
                    "external_url_canonical": erc["_url_canonical"],
                    "acquisition_unit_id": "",
                    "local_path": "",
                    "sha256": "",
                    "acquisition_status": "not_acquired",
                    "relationship_role": "authorization_gate_blocked"
                    if erc["_auth"] in ("PENDING", "INVALID")
                    else "not_authorized_for_acquisition",
                    "notes": "no acquisition without AUTHORIZE",
                }
            )
    return rows


def write_summary(
    ercs: list[dict],
    units: list[dict],
    manifests: list[dict],
    exceptions: list[dict],
    not_acquired: list[dict],
    preflight_ok: bool,
    failures: list[str],
    ledger_path: str,
) -> None:
    auth_c = Counter(e["_auth"] for e in ercs)
    shared_units = [u for u in units if u["shared_representation"] == "true"]
    ercs_in_shared = sum(int(u["erc_reference_count"]) for u in shared_units)
    status_c = Counter(m.get("acquisition_status") for m in manifests)
    byte_matches = sum(
        1
        for m in manifests
        if m.get("content_hash_match") == "true"
        and m.get("same_bytes_as_acquisition_unit")
    )
    already = status_c.get("already_preserved_locally", 0)
    complete = status_c.get("complete", 0)
    failed = status_c.get("failed", 0)
    unexpected = status_c.get("unexpected_representation", 0)

    lines = [
        "# Pass 5 — Controlled Acquisition",
        "",
        "## Integrity statement",
        "",
        "Pass 5 acquired only representations authorized through the Pass 4.5",
        "human authorization gate. Acquisition establishes custody/preservation",
        "of the representation only. It does not establish session identity,",
        "lecture novelty, evidence independence, clinical truth, or Knowledge",
        "Object status.",
        "",
        "## Authority source",
        "",
        f"- ERC inventory: `{ERC_CSV.relative_to(ROOT)}`",
        f"- Human authorization ledger: `{ledger_path}`",
        "- Pass 4 was **not** used as authorization authority",
        "",
        "## Pre-flight result",
        "",
        f"**`{'PASS' if preflight_ok else 'FAIL — DOWNLOADS BLOCKED'}`**",
        "",
        "Failures / notices:",
        "",
    ]
    if failures:
        for f in failures:
            lines.append(f"- {f}")
    else:
        lines.append("- none")
    lines += [
        "",
        "## Counts (calculated from actual datasets)",
        "",
        "| Metric | Count |",
        "|---|---:|",
        f"| Total ERCs reviewed | {len(ercs)} |",
        f"| AUTHORIZE | {auth_c.get('AUTHORIZE', 0)} |",
        f"| DEFER | {auth_c.get('DEFER', 0)} |",
        f"| DENY | {auth_c.get('DENY', 0)} |",
        f"| PENDING / invalid / incomplete | {auth_c.get('PENDING', 0) + auth_c.get('INVALID', 0)} |",
        f"| Unique authorized representations (acquisition units) | {len(units)} |",
        f"| Shared representation units | {len(shared_units)} |",
        f"| ERCs served by shared units | {ercs_in_shared} |",
        f"| Already preserved locally | {already} |",
        f"| Successfully acquired | {complete} |",
        f"| Failed acquisitions | {failed} |",
        f"| Unexpected representations | {unexpected} |",
        f"| Byte-identical matches across distinct URLs | {byte_matches} |",
        f"| Exceptions requiring review | {len(exceptions)} |",
        f"| Not acquired (DEFER/DENY inventory rows) | {len(not_acquired)} |",
        "",
        "## Blocker (if any)",
        "",
    ]
    if not preflight_ok:
        lines += [
            "Pass 5 **did not download** because the Pass 4.5 human authorization",
            "gate is incomplete in the repository. Expected completed decisions",
            "(`AUTHORIZE` / `DEFER` / `DENY`) were not present on ERC-001–066.",
            "",
            "Observed: all seeded ERCs remain `authorization_state=pending` /",
            "`decision=NEEDS_HUMAN_SCOPING`.",
            "",
            "To unblock: record explicit human decisions in the ERC CSV fields",
            "(`authorization_state`, `decision`, `human_authorization_record`)",
            "and/or provide",
            "`Research/lectures/audit/evidence-resolution-human-authorization-pass-4.5.csv`,",
            "then re-run:",
            "",
            "```bash",
            "python3 Research/lectures/scripts/pass_5_controlled_acquisition.py",
            "```",
            "",
            "Do **not** infer AUTHORIZE from Pass 4 `ACQUIRE_CANDIDATE`,",
            "`DOWNLOAD_PDF`, or external availability.",
            "",
        ]
    else:
        lines += ["Pre-flight passed; acquisition executed for authorized units only.", ""]

    lines += [
        "## Why AUTHORIZE count may differ from acquisition-unit count",
        "",
        "Multiple ERCs may authorize the **same** representation URL. Pass 5 consolidates those into one acquisition unit (one download / one hash), while preserving all ERC and catalog relationships in the crosswalk.",
        "",
        "## Known shared-URL checks (dataset)",
        "",
        "| URL pattern | Catalog IDs |",
        "|---|---|",
        "| Biological Dentistry PDF | aosrd-webinars-224-…, aosrd-webinars-241-… |",
        "| Integrative Immuno-Oncology page URL | aosrd-webinars-235-…, aosrd-webinars-237-… |",
        "| Oxytocin page URL | aosrd-webinars-197-…, aosrd-webinars-202-… |",
        "",
        "Consolidation applies **only** among ERCs that are AUTHORIZE. A DEFER/DENY ERC sharing a URL does not authorize acquisition by itself.",
        "",
        "## Epistemic ceiling",
        "",
        "All acquisition units carry:",
        "",
        "`bytes_in_custody` + `explicitly_not_session_identity` + `explicitly_not_knowledge_object`",
        "",
        "## Outputs",
        "",
        f"- `{OUT_PREFLIGHT.relative_to(ROOT)}`",
        f"- `{OUT_PLAN.relative_to(ROOT)}`",
        f"- `{OUT_MANIFEST.relative_to(ROOT)}`",
        f"- `{OUT_CROSSWALK.relative_to(ROOT)}`",
        f"- `{OUT_EXCEPTIONS.relative_to(ROOT)}`",
        f"- `{OUT_NOT_ACQUIRED.relative_to(ROOT)}`",
        f"- `{OUT_SUMMARY.relative_to(ROOT)}` (this file)",
        "- Per-unit dirs under `Research/lectures/acquired/aosrd-pdf/` (only if downloads executed)",
        "",
        "## STOP",
        "",
        "```",
        (
            "PASS 5 PREFLIGHT FAILED; NO DOWNLOADS PERFORMED."
            if not preflight_ok
            else "PASS 5 ACQUISITION COMPLETE FOR AUTHORIZED UNITS ONLY."
        ),
        "PASS 4.5 AUTHORIZATION GATE ENFORCED.",
        "NO SESSION IDENTITY INFERRED.",
        "NO KNOWLEDGE OBJECTS CREATED.",
        "NO OCR / TRANSCRIPTION / EMBEDDINGS.",
        "NO PASS 1–4 FILES MODIFIED.",
        "```",
        "",
    ]
    OUT_SUMMARY.write_text("\n".join(lines), encoding="utf-8")


def write_authorization_ledger_template(ercs: list[dict]) -> None:
    """Write a blank human ledger template if none exists (does not invent decisions)."""
    path = AUDIT / "evidence-resolution-human-authorization-pass-4.5.TEMPLATE.csv"
    fields = [
        "erc_id",
        "erc_short_id",
        "catalog_record_id",
        "primary_representation_url",
        "human_decision",
        "authorization_state",
        "decision",
        "human_authorization_record",
        "notes",
    ]
    rows = []
    for e in ercs:
        rows.append(
            {
                "erc_id": e.get("erc_id"),
                "erc_short_id": e["_short_id"],
                "catalog_record_id": e.get("catalog_record_id"),
                "primary_representation_url": e["_url_original"],
                "human_decision": "",  # AUTHORIZE | DEFER | DENY
                "authorization_state": "",
                "decision": "",
                "human_authorization_record": "",
                "notes": "Fill human_decision with AUTHORIZE, DEFER, or DENY; do not leave blank",
            }
        )
    write_csv(path, fields, rows)


def write_preflight_md(
    ercs: list[dict],
    units: list[dict],
    failures: list[str],
    preflight_ok: bool,
    execute: bool,
    ledger_path: str,
) -> None:
    auth_c = Counter(e["_auth"] for e in ercs)
    shared_units = [u for u in units if u["shared_representation"] == "true"]
    already = sum(
        1
        for u in units
        if str(u.get("local_presence_status", "")).startswith("already_preserved")
    )

    url_to_ercs: dict[str, list[dict]] = defaultdict(list)
    for e in ercs:
        key = e.get("_url_canonical") or e.get("_url_original") or ""
        if key:
            url_to_ercs[key].append(e)
    shared_urls_all = {u: es for u, es in url_to_ercs.items() if len(es) > 1}
    shared_authorized = [
        u
        for u, es in shared_urls_all.items()
        if any(e["_auth"] == "AUTHORIZE" for e in es)
    ]
    deferred_only_urls = {
        u
        for u, es in url_to_ercs.items()
        if es and all(e["_auth"] == "DEFER" for e in es)
    }
    denied_only_urls = {
        u
        for u, es in url_to_ercs.items()
        if es and all(e["_auth"] == "DENY" for e in es)
    }
    unauthorized_excluded = {
        u
        for u, es in url_to_ercs.items()
        if es and not any(e["_auth"] == "AUTHORIZE" for e in es)
    }

    verdict = "GO" if preflight_ok else "NO-GO"
    decision_line = (
        "GO — READY FOR CONTROLLED PASS 5 ACQUISITION"
        if preflight_ok
        else "NO-GO — "
        + ("; ".join(failures) if failures else "preflight invariants failed")
    )

    frozen_ok = all(
        (AUDIT / name).is_file()
        for name in (
            "title-reconciliation-pass-1.csv",
            "local-representation-inventory-pass-2.csv",
            "external-representation-availability-pass-3.csv",
            "acquisition-candidate-audit-pass-4.csv",
        )
    )
    totals_ok = (
        len(ercs) == 66
        and auth_c.get("AUTHORIZE", 0) == 54
        and auth_c.get("DEFER", 0) == 10
        and auth_c.get("DENY", 0) == 2
    )

    lines = [
        "# Pass 5 Pre-Flight Report",
        "",
        f"## Verdict: **{verdict}**",
        "",
        f"**{decision_line}**",
        "",
        "A GO means only that the repository passes the pre-flight gate.",
        "It does **not** mean acquisition has occurred.",
        "",
        "Sequence gate:",
        "",
        "```",
        "Pass 4.5 human authorization",
        "        ↓",
        "AUTHORIZE ERCs (must be explicit)",
        "        ↓",
        "representation-level deduplication",
        "        ↓",
        "shared-PDF consolidation",
        "        ↓",
        "already-preserved check",
        "        ↓",
        "unique acquisition units",
        "        ↓",
        "PASS 5 PRE-FLIGHT",
        "        ↓",
        f"       {verdict}",
        "```",
        "",
        f"- Mode: `{'execute' if execute else 'preflight-only'}`",
        f"- Downloads performed: **no**"
        + (
            " (preflight-only; re-run with `--execute` after GO)"
            if preflight_ok and not execute
            else (" (blocked by NO-GO)" if not preflight_ok else "")
        ),
        f"- Authority ledger: `{ledger_path}`",
        "",
        "## Required summary block",
        "",
        "```text",
        f"Pass 4.5 ERCs = {len(ercs)}",
        f"AUTHORIZE = {auth_c.get('AUTHORIZE', 0)}",
        f"DEFER = {auth_c.get('DEFER', 0)}",
        f"DENY = {auth_c.get('DENY', 0)}",
        "",
        f"Unique authorized representations = {len(units)}",
        f"Unique acquisition units = {len(units)}",
        "",
        f"Shared-PDF representations = {len(shared_urls_all)}",
        f"Shared-PDF representations with ≥1 AUTHORIZE = {len(shared_authorized)}",
        f"Already preserved representations = {already}",
        "",
        f"Unauthorized representations excluded = {len(unauthorized_excluded)}",
        f"Deferred representations excluded = {len(deferred_only_urls)}",
        f"Denied representations excluded = {len(denied_only_urls)}",
        "",
        "Download status = NONE",
        "Execution status = NOT EXECUTED",
        "```",
        "",
        "## Calculated counts",
        "",
        "| Metric | Count |",
        "|---|---:|",
        f"| Total ERCs | {len(ercs)} |",
        f"| AUTHORIZE | {auth_c.get('AUTHORIZE', 0)} |",
        f"| DEFER | {auth_c.get('DEFER', 0)} |",
        f"| DENY | {auth_c.get('DENY', 0)} |",
        f"| PENDING / INVALID | {auth_c.get('PENDING', 0) + auth_c.get('INVALID', 0)} |",
        f"| Unique authorized representations / acquisition units | {len(units)} |",
        f"| Shared representation units (≥2 AUTHORIZE ERCs) | {len(shared_units)} |",
        f"| Shared URLs across any ERCs (incl. DEFER/DENY peers) | {len(shared_urls_all)} |",
        f"| Already preserved (detected) | {already} |",
        "",
        "## Known shared representations",
        "",
        "| Case | Catalog IDs | Plan effect |",
        "|---|---|---|",
        "| Future of Biological Dentistry | aosrd-webinars-224-… + 241-… | AUTHORIZE peer only enters plan |",
        "| Oxytocin | aosrd-webinars-197-… + 202-… | AUTHORIZE peer only enters plan |",
        "| Integrative Immuno-Oncology | aosrd-webinars-235-… + 237-… | both DEFER → excluded |",
        "",
        "Shared representation ≠ shared session.",
        "",
        "## Invariant checks",
        "",
    ]
    checks = [
        (
            "every acquisition unit has ≥1 AUTHORIZE ERC",
            all(any(e["_auth"] == "AUTHORIZE" for e in u["_ercs"]) for u in units)
            if units
            else (auth_c.get("AUTHORIZE", 0) == 0),
        ),
        (
            "no DEFER ERC is the sole authorization for an acquisition unit",
            not any({e["_auth"] for e in u["_ercs"]} == {"DEFER"} for u in units),
        ),
        (
            "no DENY ERC is the sole authorization for an acquisition unit",
            not any({e["_auth"] for e in u["_ercs"]} == {"DENY"} for u in units),
        ),
        (
            "no unauthorized representation appears in the acquisition plan",
            not any(e["_auth"] != "AUTHORIZE" for u in units for e in u["_ercs"]),
        ),
        (
            "duplicate URLs consolidated into one unit per canonical key",
            len({u["_key"] for u in units}) == len(units),
        ),
        (
            "Pass 1–4 source files present and untouched by this pass",
            frozen_ok,
        ),
        (
            "authorization ledger complete (no PENDING/INVALID)",
            auth_c.get("PENDING", 0) == 0 and auth_c.get("INVALID", 0) == 0,
        ),
        (
            "expected AUTHORIZE/DEFER/DENY totals 54/10/2",
            totals_ok,
        ),
        (
            "at least one AUTHORIZE decision present",
            auth_c.get("AUTHORIZE", 0) > 0,
        ),
    ]
    for label, ok in checks:
        lines.append(f"- [{'x' if ok else ' '}] {label}")
    lines += ["", "## Failures / blockers", ""]
    if failures:
        for f in failures:
            lines.append(f"- {f}")
    else:
        lines.append("- none")
    lines += [
        "",
        "## Planned acquisition pipeline (not executed)",
        "",
        "```text",
        "download to temporary location",
        "        ↓",
        "validate response/content",
        "        ↓",
        "confirm actual PDF/MIME",
        "        ↓",
        "preserve original bytes",
        "        ↓",
        "calculate SHA-256",
        "        ↓",
        "record metadata",
        "        ↓",
        "place in deterministic acquisition-unit path",
        "```",
        "",
        "HTML / login / bot-wall / non-PDF responses must be recorded as failed",
        "or unexpected acquisition artifacts — never as successful PDFs.",
        "",
        "## Next action",
        "",
    ]
    if not preflight_ok:
        lines += [
            "**STOP + FIX.** Resolve blockers above, then re-run pre-flight.",
            "",
            "Do not infer authorization from Pass 4, availability, or `ACQUIRE_CANDIDATE`.",
            "",
        ]
    elif not execute:
        lines += [
            "**GO** — pre-flight passed. Downloads not started (preflight-only mode).",
            "",
            "```bash",
            "python3 Research/lectures/scripts/pass_5_controlled_acquisition.py --execute",
            "```",
            "",
        ]
    else:
        lines += ["**GO** — proceeding to download authorized acquisition units only.", ""]
    lines += [
        "## Final decision",
        "",
        f"`{decision_line}`",
        "",
        "## Integrity",
        "",
        "Pass 5 may acquire only representations authorized through the materialized",
        "Pass 4.5 human authorization ledger. Acquisition establishes custody and",
        "preservation of the representation only. It does not establish session",
        "identity, lecture novelty, evidence independence, clinical truth, or",
        "Knowledge Object status.",
        "",
    ]
    OUT_PREFLIGHT_MD.write_text("\n".join(lines), encoding="utf-8")



def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Pass 5 controlled acquisition")
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        default=True,
        help="Run pre-flight and write reports; never download (default)",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="If pre-flight reports GO, download authorized acquisition units",
    )
    args = parser.parse_args(argv)
    execute = bool(args.execute)
    # --execute disables preflight-only
    preflight_only = not execute

    if not ERC_CSV.is_file():
        print(f"FATAL: missing {ERC_CSV}", file=sys.stderr)
        return 2

    ercs = load_ercs()
    ledger = load_ledger()
    ledger_path = (
        "NOT FOUND — fell back to ERC CSV authorization fields"
        if not ledger
        else next(str(p.relative_to(ROOT)) for p in LEDGER_CANDIDATES if p.is_file())
    )

    units, exceptions, not_acquired = build_acquisition_units(ercs)
    preflight_ok, failures, preflight_rows = preflight_check(ercs, units, exceptions)

    write_csv(OUT_PREFLIGHT, PREFLIGHT_FIELDS, preflight_rows)
    write_preflight_md(ercs, units, failures, preflight_ok, execute, ledger_path)
    write_authorization_ledger_template(ercs)

    # Plan is one row per unique AU (even if downloads blocked — empty if no AUTHORIZE)
    plan_rows = [{k: u.get(k, "") for k in PLAN_FIELDS} for u in units]
    write_csv(OUT_PLAN, PLAN_FIELDS, plan_rows)

    manifests: list[dict] = []
    if not preflight_ok:
        print("=== PASS 5 PRE-FLIGHT: NO-GO ===")
        print("DOWNLOADS BLOCKED — STOP + FIX")
        for f in failures:
            print(f"  - {f}")
    elif preflight_only:
        print("=== PASS 5 PRE-FLIGHT: GO ===")
        print(f"Unique acquisition units ready: {len(units)}")
        print("Downloads NOT started (preflight-only). Re-run with --execute to acquire.")
        for u in units:
            print(
                f"  {u['acquisition_unit_id']} shared={u['shared_representation']} "
                f"local={u['local_presence_status']} {u['external_url_original'][:72]}"
            )
    else:
        print("=== PASS 5 PRE-FLIGHT: GO — EXECUTING DOWNLOADS ===")
        print(f"PREFLIGHT PASS — acquiring {len(units)} unique representation(s)")
        for u in units:
            print(f"  {u['acquisition_unit_id']} {u['external_url_original'][:80]}")
            manifests.append(download_unit(u))
        apply_byte_dedup(manifests, exceptions)
        for m in manifests:
            if m["acquisition_status"] == "failed":
                exceptions.append(
                    {
                        "exception_id": f"EX-FAIL-{m['acquisition_unit_id']}",
                        "exception_class": "failed_download",
                        "erc_id": m["authorized_erc_ids"],
                        "acquisition_unit_id": m["acquisition_unit_id"],
                        "catalog_record_id": m["catalog_record_ids"],
                        "external_url": m["external_url_original"],
                        "detail": m.get("notes", ""),
                        "requires_human_review": "true",
                    }
                )
            elif m["acquisition_status"] == "unexpected_representation":
                exceptions.append(
                    {
                        "exception_id": f"EX-MIME-{m['acquisition_unit_id']}",
                        "exception_class": "unexpected_mime_type",
                        "erc_id": m["authorized_erc_ids"],
                        "acquisition_unit_id": m["acquisition_unit_id"],
                        "catalog_record_id": m["catalog_record_ids"],
                        "external_url": m["external_url_original"],
                        "detail": f"declared={m.get('content_type_declared')}; detected={m.get('content_type_detected')}",
                        "requires_human_review": "true",
                    }
                )
            elif m["acquisition_status"] == "already_preserved_locally":
                exceptions.append(
                    {
                        "exception_id": f"EX-PRES-{m['acquisition_unit_id']}",
                        "exception_class": "representation_already_preserved_locally",
                        "erc_id": m["authorized_erc_ids"],
                        "acquisition_unit_id": m["acquisition_unit_id"],
                        "catalog_record_id": m["catalog_record_ids"],
                        "external_url": m["external_url_original"],
                        "detail": m.get("notes", ""),
                        "requires_human_review": "false",
                    }
                )

    write_csv(OUT_MANIFEST, MANIFEST_FIELDS, manifests)
    crosswalk = build_crosswalk(ercs, units, manifests)
    write_csv(OUT_CROSSWALK, CROSSWALK_FIELDS, crosswalk)
    write_csv(OUT_EXCEPTIONS, EXCEPTION_FIELDS, exceptions)
    write_csv(OUT_NOT_ACQUIRED, NOT_ACQUIRED_FIELDS, not_acquired)
    write_summary(
        ercs, units, manifests, exceptions, not_acquired, preflight_ok, failures, ledger_path
    )

    print(f"Wrote {OUT_PREFLIGHT_MD.relative_to(ROOT)}")
    print(f"Wrote {OUT_SUMMARY.relative_to(ROOT)}")
    print(
        f"ERCs={len(ercs)} AUTHORIZE={sum(1 for e in ercs if e['_auth']=='AUTHORIZE')} "
        f"units={len(units)} manifests={len(manifests)} exceptions={len(exceptions)} "
        f"verdict={'GO' if preflight_ok else 'NO-GO'}"
    )
    # Exit 0 for successful preflight-only GO; 1 for NO-GO; 0 for executed GO
    if not preflight_ok:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
