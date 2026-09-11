#!/usr/bin/env python3
"""Pass 2 pilot: classify 30 statements only. No full-set write. No commit."""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace")
INTAKE = ROOT / "Research/nutrition/sources/hair-nutrition-intake-2026-09-11"
SRC = INTAKE / "statements" / "candidate-statements.json"
OUT = INTAKE / "review" / "pass2-pilot-30.json"
AUDIT = INTAKE / "review" / "pass2-pilot-30-audit.md"
TS = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def length_bin(t: str) -> str:
    n = len(t)
    if n < 40:
        return "short"
    if n < 120:
        return "med"
    return "long"


def content_bin(t: str) -> str:
    tl = t.lower()
    if any(
        w in tl
        for w in (
            "should",
            "recommend",
            "take ",
            "dose",
            " mg",
            "iu ",
            "supplement with",
        )
    ):
        return "rec_or_dose"
    if any(
        w in tl
        for w in (
            "caution",
            "avoid",
            "warning",
            "contraindic",
            "toxicity",
            "excess",
            "do not",
        )
    ):
        return "warn"
    if any(
        w in tl
        for w in (
            "wnt",
            "beta-catenin",
            "β-catenin",
            "signaling",
            "pathway",
            "mechanism",
            "activat",
            "inhibits",
            "receptor",
        )
    ):
        return "mech"
    if any(
        w in tl
        for w in (
            "vitamin",
            "zinc",
            "iron",
            "magnesium",
            "selenium",
            "copper",
            "protein",
            "amino",
            "omega",
            "nutrient",
            "folate",
            "biotin",
        )
    ):
        return "nutrient"
    if len(t.strip()) < 25 and not t.strip().endswith("."):
        return "label_or_heading"
    if any(w in tl for w in ("is a ", "defined as", "refers to", "means ", "consists of")):
        return "definitionish"
    return "other"


def classify(s: dict) -> dict:
    text = s["source_wording"]
    t = text.strip()
    tl = t.lower()
    notes: list[str] = []

    p1 = s.get("repetition_class") or "unclear"
    if p1 == "repetition":
        independence = "repetition"
    elif p1 == "derivative":
        independence = "derivative"
    elif p1 == "independent":
        independence = "independent"
    else:
        independence = "unclear"

    is_short_label = len(t) < 40 and not t.endswith((".", "!", "?")) and "\n" not in t
    looks_heading = t.isupper() or (
        len(t) < 60 and t.istitle() and not any(c in t for c in ".?!")
    )
    nutrient_label = (
        re.fullmatch(
            r"(zinc|iron|selenium|copper|magnesium|protein( / essential amino acids)?"
            r"|omega-3 fatty acids|b\d+[^.]{0,40}|thiamine|folate|biotin|"
            r"vitamin [a-z0-9\- ]+|25-oh vitamin d|core|meal|factor|why it matters)",
            tl,
        )
        is not None
    )

    if re.search(r"\b(must|shall|prescribe|take\s+\d|dose of|mg/?d|iu/?d)\b", tl):
        actionability = "prescriptive"
    elif re.search(r"\b(should|recommend(?:ed|ation)?|advise|consider taking)\b", tl):
        actionability = "recommendation"
    elif re.search(r"\b(may help|can support|could improve|suggests? that)\b", tl):
        actionability = "suggestive"
    elif re.search(r"\b(avoid|do not|should not)\b", tl):
        actionability = "recommendation"
    elif is_short_label or nutrient_label or looks_heading:
        actionability = "none"
    else:
        actionability = "informational"

    kind = "unclear"
    if re.search(r"\b(is defined as|refers to|means that|is a type of|consists of)\b", tl):
        kind = "definition"
    if re.search(
        r"\b(wnt|beta-catenin|β-catenin|signaling|pathway|mechanism|receptor|"
        r"transcription|dkk|stem cell niche)\b",
        tl,
    ):
        kind = "mechanistic"
    if re.search(r"\b(causes?|leads? to|results? in|induces?|drives?)\b", tl) and kind != "mechanistic":
        kind = "causal"
    if re.search(r"\b(associated with|linked to|correlat|related to)\b", tl):
        kind = "associational"
    if re.search(
        r"\b(hypothesis|hypothesize|may be due|possibly|proposed that|suggests a role)\b",
        tl,
    ):
        kind = "hypothesis"
    if re.search(
        r"\b(vitamin|zinc|iron|magnesium|selenium|copper|protein|amino acid|"
        r"omega-3|nutrient|folate|biotin|calorie|diet)\b",
        tl,
    ) and kind in ("unclear", "classification"):
        if actionability in ("recommendation", "prescriptive", "suggestive") or len(t) >= 40:
            kind = "nutritional_claim"
    if re.search(
        r"\b(treat|therapy|therapeutic|clinical|patient|alopecia|hair loss|regrowth|diagnose)\b",
        tl,
    ):
        if actionability in ("recommendation", "prescriptive"):
            kind = "therapeutic_claim"
        elif kind in ("unclear", "classification", "nutritional_claim") and len(t) >= 40:
            kind = "clinical_claim"
    if re.search(r"\b(lab|laboratory|assay|serum|plasma|blood test|25-oh|ferritin|biomarker)\b", tl):
        kind = "laboratory_claim"
    if re.search(r"\b(measure|concentration|level of|mg/?l|µg|ng/?ml|iu)\b", tl) and kind in (
        "unclear",
        "nutritional_claim",
        "classification",
    ):
        kind = "measurement_claim"
    if re.search(r"\b(avoid|caution|warning|toxicity|excess|contraindic|do not)\b", tl):
        kind = "warning_or_boundary"
    if re.search(r"\b(should|recommend)\b", tl) and kind not in (
        "warning_or_boundary",
        "therapeutic_claim",
        "nutritional_claim",
    ):
        kind = "recommendation"
    if re.search(r"\b(must|prescribe|take \d)\b", tl):
        kind = "prescription"
    if re.search(r"\b(traditional|ayurved|tcm|folk|historically used)\b", tl):
        kind = "traditional_use_claim"
    if re.search(r"\b(method|protocol step|procedure|we measured|study design)\b", tl):
        kind = "methodological"
    if re.search(r"\b(observed|observation|in patients we saw|clinically noted)\b", tl):
        kind = "observational"
    if kind == "unclear" and len(t) >= 40 and t.endswith((".", "!", "?")):
        kind = "descriptive"
    if kind == "unclear" and (is_short_label or looks_heading or nutrient_label):
        kind = "classification"

    if (
        kind == "classification"
        and (is_short_label or nutrient_label or looks_heading)
        and actionability == "none"
    ):
        claim_status = "non_claim"
    elif len(t) < 15 and actionability == "none":
        claim_status = "non_claim"
    else:
        claim_status = "candidate"

    if claim_status == "non_claim" and kind == "classification":
        epistemic_scope = "structural_or_metadata"
    elif kind == "hypothesis":
        epistemic_scope = "source_hypothesis"
    elif kind in ("recommendation", "prescription") or actionability in (
        "recommendation",
        "prescriptive",
    ):
        epistemic_scope = "source_recommendation"
    elif kind == "warning_or_boundary":
        epistemic_scope = "source_warning"
    elif kind == "observational":
        epistemic_scope = "source_observation"
    elif claim_status == "candidate":
        epistemic_scope = "source_assertion"
    else:
        epistemic_scope = "unclear"

    ambiguity = "none"
    clause_hits = 0
    if t.count(".") >= 2:
        clause_hits += 1
    if ";" in t:
        clause_hits += 1
    if re.search(r"\b(and|but|while|whereas|because|which)\b", tl) and len(t) > 120:
        clause_hits += 1
    if clause_hits >= 1 and len(t) > 100:
        ambiguity = "compound_statement"
        notes.append(
            "Long multi-clause wording treated as a single Pass-1 candidate; not split."
        )
    elif kind == "unclear":
        ambiguity = "type_ambiguous"
        notes.append(
            "Wording does not reliably fit a single statement_kind; left conservative."
        )
    elif claim_status == "candidate" and actionability in (
        "recommendation",
        "prescriptive",
    ) and kind in ("mechanistic", "nutritional_claim", "clinical_claim"):
        ambiguity = "boundary_ambiguous"
        notes.append(
            "Contains both descriptive/claim content and action-directed language."
        )

    if not notes:
        note_map = {
            "mechanistic": "Wording describes a proposed biological/signaling process.",
            "nutritional_claim": "Wording asserts a nutrition-related proposition or nutrient role.",
            "classification": "Short label/heading or nutrient name used as structural descriptor in the source.",
            "recommendation": "Wording directs or advises an action in the historical source.",
            "prescription": "Wording has mandatory/dosing-like directive form in the source.",
            "warning_or_boundary": "Wording sets a caution, avoidance, or safety boundary.",
            "laboratory_claim": "Wording refers to laboratory/biomarker measurement content.",
            "descriptive": "General descriptive prose without clear directive or mechanism markers.",
            "causal": "Wording uses cause/result language.",
            "associational": "Wording uses association/link language rather than explicit causation.",
            "hypothesis": "Wording is framed as possibility/proposal rather than settled assertion.",
            "therapeutic_claim": "Wording asserts a treatment/clinical effect proposition in the source.",
            "clinical_claim": "Wording asserts a clinical/hair-related proposition in the source.",
            "measurement_claim": "Wording asserts a measurable quantity or level.",
            "definition": "Wording defines or delimits a term.",
        }
        notes.append(note_map.get(kind, "Classification based on surface wording/structure only."))
    notes.append("Not evaluated for factual truth; historical source wording only.")

    return {
        "statement_id": s["statement_id"],
        "source_wording": s["source_wording"],
        "source_representation_id": s["source_representation_id"],
        "source_artifact_id": s["source_artifact_id"],
        "location": s.get("location"),
        "pass1_repetition_class": p1,
        "statement_kind": kind,
        "claim_status": claim_status,
        "actionability_class": actionability,
        "epistemic_scope": epistemic_scope,
        "independence": independence,
        "evidence_relation": None,
        "evidence_strength": 0,
        "ambiguity_flag": ambiguity,
        "classification_notes": " ".join(notes),
    }


def main() -> None:
    data = json.loads(SRC.read_text())
    stmts = data["statements"]
    assert len(stmts) == 514, len(stmts)
    by_id = {s["statement_id"]: s for s in stmts}

    selected: list[str] = []
    selected_set: set[str] = set()

    def take(stmt: dict) -> None:
        sid = stmt["statement_id"]
        if sid not in selected_set and len(selected) < 30:
            selected.append(sid)
            selected_set.add(sid)

    by_art: dict[str, list[dict]] = defaultdict(list)
    for s in stmts:
        by_art[s["source_artifact_id"]].append(s)
    for art in ("SRC-HN-001", "SRC-HN-002", "SRC-HN-003"):
        arr = sorted(by_art[art], key=lambda x: x["statement_id"])
        n = len(arr)
        for frac in (0.10, 0.40, 0.70, 0.90):
            take(arr[int(frac * (n - 1))])

    bins_needed = {
        "rec_or_dose": 3,
        "warn": 2,
        "mech": 4,
        "nutrient": 3,
        "label_or_heading": 3,
        "definitionish": 1,
        "other": 2,
    }
    for b, need in bins_needed.items():
        pool = [s for s in stmts if content_bin(s["source_wording"]) == b]
        pool.sort(key=lambda x: x["statement_id"])
        if not pool:
            continue
        step = max(1, len(pool) // (need + 1))
        for i in range(need):
            take(pool[min((i + 1) * step, len(pool) - 1)])

    rep_pool = sorted(
        [s for s in stmts if s.get("repetition_class") == "repetition"],
        key=lambda x: x["statement_id"],
    )
    unc_pool = sorted(
        [s for s in stmts if s.get("repetition_class") == "unclear"],
        key=lambda x: x["statement_id"],
    )
    for i in (0, len(rep_pool) // 3, 2 * len(rep_pool) // 3):
        if rep_pool:
            take(rep_pool[min(i, len(rep_pool) - 1)])
    for i in (5, len(unc_pool) // 2, len(unc_pool) - 6):
        if unc_pool:
            take(unc_pool[min(max(i, 0), len(unc_pool) - 1)])

    compoundish = []
    for s in stmts:
        w = s["source_wording"]
        wl = w.lower()
        if ((" and " in wl and len(w) > 100) or ";" in w or w.count(".") >= 2):
            compoundish.append(s)
    compoundish.sort(key=lambda x: x["statement_id"])
    for i in (
        0,
        len(compoundish) // 4,
        len(compoundish) // 2,
        3 * len(compoundish) // 4,
    ):
        if compoundish:
            take(compoundish[min(i, len(compoundish) - 1)])

    ordered = sorted(stmts, key=lambda x: x["statement_id"])
    stride = 17
    idx = 3
    while len(selected) < 30:
        take(ordered[idx % len(ordered)])
        idx += stride

    assert len(selected) == 30
    classified = [classify(by_id[i]) for i in selected]

    pilot = {
        "meta": {
            "pass": "Pass 2 pilot — statement classification only",
            "created_at": TS,
            "authoritative_input": str(SRC.relative_to(ROOT)),
            "population_size": 514,
            "pilot_size": 30,
            "status": "review_only_non_authoritative",
            "sampling_method": {
                "description": (
                    "Stratified reproducible sample: (1) per-artifact positions at "
                    "10/40/70/90% of statement_id-ordered lists; (2) quota picks from "
                    "content bins by statement_id stride; (3) forced inclusion from "
                    "Pass-1 repetition and unclear pools; (4) longer multi-clause "
                    "candidates; (5) fill to 30 via statement_id-ordered walk with "
                    "stride 17 from index 3."
                ),
                "deterministic": True,
                "seed_note": "No RNG; selection fully determined by statement_id order and fixed fractions/strides.",
            },
            "rules": {
                "no_external_evidence": True,
                "no_claim_validation": True,
                "no_promotion": True,
                "evidence_relation": None,
                "evidence_strength": 0,
                "independence_policy": "preserve Pass-1 repetition_class mapping; do not inflate independence",
            },
            "hard_stop": "Do not classify remaining 484 without human authorization.",
        },
        "sampled_ids": selected,
        "source_distribution": dict(Counter(c["source_artifact_id"] for c in classified)),
        "classification_distribution": {
            "statement_kind": dict(Counter(c["statement_kind"] for c in classified)),
            "claim_status": dict(Counter(c["claim_status"] for c in classified)),
            "actionability_class": dict(
                Counter(c["actionability_class"] for c in classified)
            ),
            "epistemic_scope": dict(Counter(c["epistemic_scope"] for c in classified)),
            "independence": dict(Counter(c["independence"] for c in classified)),
            "ambiguity_flag": dict(Counter(c["ambiguity_flag"] for c in classified)),
        },
        "statements": classified,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pilot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    issues: list[str] = []
    for c in classified:
        if c["evidence_relation"] is not None:
            issues.append(f"{c['statement_id']}: evidence_relation not null")
        if c["evidence_strength"] != 0:
            issues.append(f"{c['statement_id']}: evidence_strength != 0")
        if c["source_wording"] != by_id[c["statement_id"]]["source_wording"]:
            issues.append(f"{c['statement_id']}: wording altered")
        notes_l = c["classification_notes"].lower()
        if "supported by the literature" in notes_l or "this is a valid mechanism" in notes_l:
            issues.append(f"{c['statement_id']}: truth-justifying notes")
        if c["independence"] == "independent":
            issues.append(
                f"{c['statement_id']}: independence inflated to independent without provenance"
            )
        p1 = by_id[c["statement_id"]].get("repetition_class")
        if p1 == "repetition" and c["independence"] != "repetition":
            issues.append(f"{c['statement_id']}: failed to preserve Pass-1 repetition")
        if p1 == "unclear" and c["independence"] != "unclear":
            issues.append(
                f"{c['statement_id']}: failed to preserve Pass-1 unclear independence"
            )

    schema_notes = [
        "Allowed statement_kind list is broad; short nutrient labels overlap classification vs nutritional_claim — pilot treats short labels as classification + non_claim + structural_or_metadata.",
        "actionability_class and statement_kind can both mark directive content; kept both (kind=form, actionability=directive force).",
        "ambiguity_flag is single-valued in this pilot schema; secondary ambiguities placed in classification_notes.",
        "evidence_relation left JSON null; evidence_strength integer 0 as not assessed.",
    ]
    verdict = "PASS" if not issues else "NEEDS_REVISION"

    lines = [
        "# Pass 2 Pilot Audit — 30-statement classification",
        "",
        f"- Created: {TS}",
        f"- Input: `{SRC.relative_to(ROOT)}` (514 statements)",
        f"- Pilot artifact: `{OUT.relative_to(ROOT)}` (**review-only / non-authoritative**)",
        "- Full candidate dataset modified: **NO**",
        "- External evidence consulted: **NO**",
        "- Commit/PR: **NOT created** (hard stop)",
        "",
        "## Sampled IDs (n=30)",
        "",
    ]
    for i in selected:
        lines.append(f"- {i}")
    lines += ["", "## Source distribution", "", "| Artifact | Count |", "|---|---:|"]
    for k, v in sorted(pilot["source_distribution"].items()):
        lines.append(f"| {k} | {v} |")
    lines += ["", "## Classification distribution", ""]
    for dim, dist in pilot["classification_distribution"].items():
        lines += [f"### {dim}", "", "| value | n |", "|---|---:|"]
        for k, v in sorted(dist.items(), key=lambda kv: (-kv[1], kv[0])):
            lines.append(f"| {k} | {v} |")
        lines.append("")

    n_unclear_kind = pilot["classification_distribution"]["statement_kind"].get("unclear", 0)
    n_compound = pilot["classification_distribution"]["ambiguity_flag"].get(
        "compound_statement", 0
    )
    n_rep = pilot["classification_distribution"]["independence"].get("repetition", 0)
    n_unc_ind = pilot["classification_distribution"]["independence"].get("unclear", 0)
    lines += [
        "## Required confirmation counts",
        "",
        "| Check | Value |",
        "|---|---|",
        "| Sampled | 30 |",
        f"| `statement_kind=unclear` | {n_unclear_kind} |",
        f"| `ambiguity_flag=compound_statement` | {n_compound} |",
        f"| `independence=repetition` | {n_rep} |",
        f"| `independence=unclear` | {n_unc_ind} |",
        f"| evidence_relation all null | {'YES' if all(c['evidence_relation'] is None for c in classified) else 'NO'} |",
        f"| evidence_strength all 0 | {'YES' if all(c['evidence_strength'] == 0 for c in classified) else 'NO'} |",
        "| External evidence consulted | NO |",
        "| Promotion (KO/Pathway/recs) | NO |",
        "| Full 514 dataset modified | NO |",
        "",
        "## Consistency audit findings",
        "",
    ]
    if issues:
        for i in issues:
            lines.append(f"- {i}")
    else:
        lines.append("- No blocking inconsistencies detected in the pilot set.")
    lines += ["", "## Schema / category observations", ""]
    for n in schema_notes:
        lines.append(f"- {n}")
    lines += [
        "",
        "## Verdict",
        "",
        f"**{verdict}**",
        "",
        "## HARD STOP",
        "",
        "Pilot complete. Do **not** classify the remaining 484 statements without explicit human authorization.",
        "",
    ]
    AUDIT.write_text("\n".join(lines), encoding="utf-8")

    print("SELECTED", selected)
    print("source_dist", pilot["source_distribution"])
    print("kinds", pilot["classification_distribution"]["statement_kind"])
    print("claim", pilot["classification_distribution"]["claim_status"])
    print("action", pilot["classification_distribution"]["actionability_class"])
    print("scope", pilot["classification_distribution"]["epistemic_scope"])
    print("indep", pilot["classification_distribution"]["independence"])
    print("ambig", pilot["classification_distribution"]["ambiguity_flag"])
    print("VERDICT", verdict)
    print("issues", issues)
    print("wrote", OUT)
    print("wrote", AUDIT)


if __name__ == "__main__":
    main()
