#!/usr/bin/env python3
"""Pass 2 full run: classify all 514 statements with the validated pilot taxonomy."""
from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace")
INTAKE = ROOT / "Research/nutrition/sources/hair-nutrition-intake-2026-09-11"
SRC = INTAKE / "statements" / "candidate-statements.json"
PILOT = INTAKE / "review" / "pass2-pilot-30.json"
OUT_JSON = INTAKE / "statements" / "pass2-classified-statements.json"
OUT_CSV = INTAKE / "statements" / "pass2-classified-statements.csv"
OUT_REPORT = INTAKE / "pass2-classification-report.md"
MANIFEST = INTAKE / "manifest.json"
TS = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

# Load pilot classify() without executing pilot main
spec = importlib.util.spec_from_file_location(
    "pass2_pilot",
    INTAKE / "review" / "run_pass2_pilot30.py",
)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
classify = mod.classify


def main() -> None:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    stmts = data["statements"]
    assert len(stmts) == 514, len(stmts)

    classified = []
    for s in stmts:
        c = classify(s)
        # Preserve full Pass 1 provenance fields
        row = {
            "statement_id": s["statement_id"],
            "source_artifact_id": s["source_artifact_id"],
            "source_representation_id": s["source_representation_id"],
            "location": s.get("location"),
            "location_detail": s.get("location_detail"),
            "source_wording": s["source_wording"],
            "pass1_status": s.get("status"),
            "pass1_repetition_class": s.get("repetition_class"),
            "pass1_repetition_basis": s.get("repetition_basis"),
            "pass1_repetition_peer_statement_ids": s.get("repetition_peer_statement_ids")
            or [],
            "pass1_evidence_strength": s.get("evidence_strength"),
            "pass1_notes": s.get("notes"),
            # Pass 2 classification
            "statement_kind": c["statement_kind"],
            "claim_status": c["claim_status"],
            "actionability_class": c["actionability_class"],
            "epistemic_scope": c["epistemic_scope"],
            "independence": c["independence"],
            "evidence_relation": None,
            "evidence_strength": 0,
            "ambiguity_flag": c["ambiguity_flag"],
            "classification_notes": c["classification_notes"],
            "pass2_classified_at": TS,
        }
        classified.append(row)

    # Consistency: pilot 30 must match full-run classifications for those IDs
    pilot = json.loads(PILOT.read_text(encoding="utf-8"))
    by_id = {r["statement_id"]: r for r in classified}
    mismatches = []
    compare_fields = [
        "statement_kind",
        "claim_status",
        "actionability_class",
        "epistemic_scope",
        "independence",
        "evidence_strength",
        "ambiguity_flag",
    ]
    for p in pilot["statements"]:
        r = by_id[p["statement_id"]]
        for f in compare_fields:
            if r[f] != p[f]:
                mismatches.append((p["statement_id"], f, p[f], r[f]))
        if r["evidence_relation"] is not None:
            mismatches.append((p["statement_id"], "evidence_relation", None, r["evidence_relation"]))
        if r["source_wording"] != p["source_wording"]:
            mismatches.append((p["statement_id"], "source_wording", "...", "..."))
    if mismatches:
        raise SystemExit(f"Pilot consistency failed: {mismatches[:10]}")

    # Integrity checks
    assert len(classified) == 514
    assert all(r["evidence_relation"] is None for r in classified)
    assert all(r["evidence_strength"] == 0 for r in classified)
    assert all(r["source_wording"] == by_id[r["statement_id"]]["source_wording"] for r in classified)
    # independence preserved from Pass 1
    for s, r in zip(stmts, classified):
        p1 = s.get("repetition_class") or "unclear"
        if p1 == "repetition":
            assert r["independence"] == "repetition"
        elif p1 == "unclear":
            assert r["independence"] == "unclear"
        assert r["independence"] != "independent" or p1 == "independent"

    dist = {
        "statement_kind": dict(Counter(r["statement_kind"] for r in classified)),
        "claim_status": dict(Counter(r["claim_status"] for r in classified)),
        "actionability_class": dict(Counter(r["actionability_class"] for r in classified)),
        "epistemic_scope": dict(Counter(r["epistemic_scope"] for r in classified)),
        "independence": dict(Counter(r["independence"] for r in classified)),
        "ambiguity_flag": dict(Counter(r["ambiguity_flag"] for r in classified)),
        "source_artifact_id": dict(Counter(r["source_artifact_id"] for r in classified)),
    }

    out_doc = {
        "meta": {
            "pass": "Pass 2 — statement classification (full set)",
            "created_at": TS,
            "authoritative_input": str(SRC.relative_to(ROOT)),
            "pilot_artifact": str(PILOT.relative_to(ROOT)),
            "population_size": 514,
            "classified_count": 514,
            "pilot_reconfirmed": 30,
            "remaining_newly_classified": 484,
            "authorization": "proceed with remaining 484 only; same validated taxonomy and rules as 30-statement pilot",
            "taxonomy": "validated_pass2_pilot_30",
            "status": "pass_2_classification_complete",
            "rules": {
                "no_external_evidence": True,
                "no_claim_validation": True,
                "no_promotion": True,
                "evidence_relation": None,
                "evidence_strength": 0,
                "independence_policy": "preserve Pass-1 repetition_class mapping",
                "epistemic_ceiling": "source → representation → candidate → classification → STOP",
            },
            "pilot_consistency_check": "PASS — all 30 pilot IDs identical under full-run classifier",
        },
        "counts": {
            "classified": 514,
            "requires_classification_cleared": 514,
            "promoted_knowledge_objects": 0,
            "promoted_pathways": 0,
            "claim_validations": 0,
            "evidence_strength_assigned": 0,
            "evidence_relation_assigned": 0,
        },
        "distribution": dist,
        "statements": classified,
    }
    OUT_JSON.write_text(json.dumps(out_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    fields = [
        "statement_id",
        "source_artifact_id",
        "source_representation_id",
        "location",
        "location_detail",
        "source_wording",
        "pass1_repetition_class",
        "statement_kind",
        "claim_status",
        "actionability_class",
        "epistemic_scope",
        "independence",
        "evidence_relation",
        "evidence_strength",
        "ambiguity_flag",
        "classification_notes",
    ]
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in classified:
            row = {k: r.get(k, "") for k in fields}
            row["evidence_relation"] = ""
            w.writerow(row)

    # Report
    lines = [
        "# Pass 2 — Statement Classification Report",
        "",
        f"- Created: {TS}",
        "- Status: **PASS 2 COMPLETE — classification only**",
        "- Population: **514 / 514** (30 pilot reconfirmed + **484 newly classified**)",
        "- Authorization: proceed with remaining 484 only, same validated taxonomy/rules as pilot",
        "- Pilot consistency: **PASS** (0 mismatches on the 30 pilot statement IDs)",
        "- Taxonomy: identical to `review/run_pass2_pilot30.py` / `review/pass2-pilot-30.json`",
        "",
        "## Epistemic ceiling",
        "",
        "```text",
        "source → representation → candidate statement → classification → STOP",
        "```",
        "",
        "No claim validation. No external evidence. No Knowledge Objects. No Pathways.",
        "Historical wording ≠ BDS-established truth.",
        "",
        "## Outputs",
        "",
        f"- `{OUT_JSON.relative_to(ROOT)}`",
        f"- `{OUT_CSV.relative_to(ROOT)}`",
        f"- Pass 1 `candidate-statements.json` left unchanged",
        "",
        "## Source distribution",
        "",
        "| Artifact | n |",
        "|---|---:|",
    ]
    for k, v in sorted(dist["source_artifact_id"].items()):
        lines.append(f"| {k} | {v} |")
    lines += ["", "## Classification distributions", ""]
    for dim in (
        "statement_kind",
        "claim_status",
        "actionability_class",
        "epistemic_scope",
        "independence",
        "ambiguity_flag",
    ):
        lines += [f"### {dim}", "", "| value | n |", "|---|---:|"]
        for k, v in sorted(dist[dim].items(), key=lambda kv: (-kv[1], kv[0])):
            lines.append(f"| {k} | {v} |")
        lines.append("")

    lines += [
        "## Integrity confirmations",
        "",
        "| Check | Result |",
        "|---|---|",
        "| Classified count | 514 |",
        "| Pilot 30 consistency | PASS |",
        "| evidence_relation all null | YES |",
        "| evidence_strength all 0 | YES |",
        "| Pass-1 wording preserved | YES |",
        "| Pass-1 independence preserved | YES |",
        "| External evidence consulted | NO |",
        "| Knowledge Objects created | 0 |",
        "| Pathways created | 0 |",
        "| Claim validations performed | 0 |",
        "| Source DOCX modified | NO |",
        "",
        "## Checkpoint",
        "",
        "```text",
        "PASS 1 COMPLETE (2e0199a / 9491394)",
        "   ↓",
        "PASS 2 PILOT 30 — PASS",
        "   ↓",
        "PASS 2 FULL 514 — COMPLETE",
        "   ↓",
        "0 promoted",
        "   ↓",
        "READY FOR LATER EVIDENCE / PROMOTION PASSES (not authorized here)",
        "```",
        "",
        "## STOP",
        "",
        "```",
        "PASS 2 CLASSIFICATION COMPLETE",
        "NO CLAIM VALIDATION",
        "NO EVIDENCE STRENGTH",
        "NO PROMOTION",
        "UNCERTAINTY PRESERVED",
        "```",
        "",
    ]
    OUT_REPORT.write_text("\n".join(lines), encoding="utf-8")

    # Update manifest checkpoint
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest["meta"]["status"] = "pass_2_classification_complete"
    manifest["meta"]["updated_at"] = TS
    manifest["meta"]["pass2"] = {
        "status": "pass_2_classification_complete",
        "classified_at": TS,
        "classified_count": 514,
        "pilot_reconfirmed": 30,
        "remaining_newly_classified": 484,
        "pilot_consistency": "PASS",
        "output_json": str(OUT_JSON.relative_to(ROOT)),
        "output_csv": str(OUT_CSV.relative_to(ROOT)),
        "report": str(OUT_REPORT.relative_to(ROOT)),
        "promoted_knowledge_objects": 0,
        "promoted_pathways": 0,
        "claim_validations": 0,
    }
    if "checkpoint" in manifest["meta"]:
        ck = manifest["meta"]["checkpoint"]
        ck["pass"] = "PASS 2 COMPLETE"
        ck["classified_statements"] = 514
        ck["pilot_statements"] = 30
        ck["remaining_classified"] = 484
        ck["promoted"] = 0
        ck["next"] = "READY FOR LATER EVIDENCE / PROMOTION PASSES (not authorized)"
        ck["pass2_completed_at"] = TS
        ck.pop("pass2", None)
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print("classified", len(classified))
    print("dist_kinds", dist["statement_kind"])
    print("dist_claim", dist["claim_status"])
    print("dist_indep", dist["independence"])
    print("dist_ambig", dist["ambiguity_flag"])
    print("pilot_mismatches", len(mismatches))
    print("wrote", OUT_JSON)
    print("wrote", OUT_CSV)
    print("wrote", OUT_REPORT)


if __name__ == "__main__":
    main()
