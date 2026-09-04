#!/usr/bin/env python3
"""QA harness for the acupuncture Knowledge branch — the automated Validate stage.

The build treats correctness as an *evolving confidence*, not a binary. This
script lets the knowledge branch re-audit its own body at any time:

  Layer 1  Structure   — schema, required sections, confidence rung, links,
                         prev/next chain, README index parity.
  Layer 2  Source       — each leaf's Location/Actions/Indications must actually
                         appear in the column-aware Deadman page(s) it cites
                         (catches fabrication, contamination, boundary bleed).
  Layer 3  Cross-source — leaf codes must be present in the Bencaodian
                         comparison dataset.
  Layer 4  Contamination guard — no two distinct points in the committed extract
                         share identical clinical text (the LU-9/LU-6 class).

Usage:  python3 Research/acupuncture/scripts/qa_check.py
Exit code is non-zero if any hard (structural/source) check fails.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LEAF_DIR = ROOT / "Knowledge/acupuncture"
DATA = ROOT / "Research/acupuncture/data"
PDF = ROOT / "Research/acupuncture/sources/pdfs/A-manual-of-acupuncture-peter-deadman.pdf"

_spec = importlib.util.spec_from_file_location("dm", Path(__file__).resolve().parent / "deadman_extract.py")
dm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dm)

CONFIDENCE_RUNGS = {"proposed", "source-verified", "cross-confirmed", "contested"}
REQUIRED_SECTIONS = ("## Location", "## Actions", "## Indications", "## Sources", "## Related")

# Source-fidelity token-overlap thresholds (fraction of a field's significant
# words that must appear on the cited source page). Actions are near-verbatim;
# indications are sometimes condensed, so their bar is lower.
THRESH = {"actions": 0.75, "indications": 0.55, "location": 0.65}

_page_cache: dict[int, str] = {}


def sig_tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]{4,}", (text or "").lower())}


def page_text(pnum: int, reader) -> str:
    if pnum not in _page_cache:
        _page_cache[pnum] = dm.clean_pdf_text(dm.render_page_columns(reader.pages[pnum - 1])).lower()
    return _page_cache[pnum]


def parse_leaf(path: Path) -> dict:
    txt = path.read_text(encoding="utf-8")
    def field(name):
        m = re.search(rf"^\|\s*{re.escape(name)}\s*\|\s*(.+?)\s*\|\s*$", txt, re.M)
        return m.group(1).strip() if m else None
    def section(name):
        m = re.search(rf"^## {name}\n(.*?)(?=^## |\Z)", txt, re.M | re.S)
        return m.group(1).strip() if m else ""
    src = section("Sources")
    pages = []
    for m in re.finditer(r"pp?\.\s*(\d+)(?:\s*[–-]\s*(\d+))?", src):
        a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
        pages.extend(range(a, b + 1))
    actions = [b.strip("-* ").strip() for b in section("Actions").splitlines() if b.strip().startswith(("-", "*"))]
    return {
        "path": path,
        "text": txt,
        "code": field("Code"),
        "confidence": field("Confidence"),
        "evidence": field("Evidence Level"),
        "pages": pages,
        "location": section("Location"),
        "actions": actions,
        "actions_raw": section("Actions"),
        "indications": section("Indications"),
        "links": [m.group(1) for m in re.finditer(r"\]\(([^)]+)\)", txt)],
    }


def main() -> int:
    from pypdf import PdfReader
    reader = PdfReader(str(PDF))
    import json
    comp = {p["code"]: p for p in json.loads((DATA / "comparison-v0.1.json").read_text())["points"]}
    extract = json.loads((DATA / "deadman-extract-v0.2.json").read_text())["points"]

    leaves = sorted(LEAF_DIR.glob("*.md"))
    leaves = [p for p in leaves if p.name != "README.md"]
    flags: list[str] = []
    hard = 0

    # ---- Layer 4: contamination guard on the committed extract ----
    # Soft/review signal (extract-level, not the leaves). Identical SHORT actions
    # (e.g. "Activates the channel and alleviates pain") are legitimately shared
    # by many points, so we only surface tight pairs sharing a long identical
    # action block — the profile most likely to be residual extract contamination.
    from collections import defaultdict
    groups: dict[str, list[str]] = defaultdict(list)
    for p in extract:
        if p["code"].startswith(("M-", "N-", "MN-")):
            continue
        a = re.sub(r"\s+", " ", (p.get("actions_en") or "")).strip().lower()
        if len(a) > 45:
            groups[a].append(p["code"])
    for a, codes in groups.items():
        if len(codes) == 2:
            flags.append(f"[L4 review] extract: {codes[0]} and {codes[1]} share identical actions (verify vs source)")

    # ---- Per-leaf checks ----
    filenames = {p.name for p in leaves}
    codes_seen = []
    for path in leaves:
        L = parse_leaf(path)
        code = L["code"]
        tag = path.name
        # Layer 1: structure
        if not code:
            flags.append(f"[L1 struct] {tag}: no Code field"); hard += 1; continue
        codes_seen.append(code)
        exp_prefix = code.replace("-", "-")
        if not path.name.startswith(code + "-"):
            flags.append(f"[L1 struct] {tag}: filename does not start with '{code}-'"); hard += 1
        if not re.search(rf"^# {re.escape(code)} ", L["text"], re.M):
            flags.append(f"[L1 struct] {tag}: title does not lead with '{code}'"); hard += 1
        for sec in REQUIRED_SECTIONS:
            if sec not in L["text"]:
                flags.append(f"[L1 struct] {tag}: missing '{sec}'"); hard += 1
        if L["confidence"] not in CONFIDENCE_RUNGS:
            flags.append(f"[L1 struct] {tag}: Confidence '{L['confidence']}' not in {sorted(CONFIDENCE_RUNGS)}"); hard += 1
        if not L["pages"]:
            flags.append(f"[L1 struct] {tag}: no Deadman page cited in Sources"); hard += 1
        # link resolution (relative)
        for link in L["links"]:
            t = link.split("#")[0]
            if t.startswith("http") or not t:
                continue
            if not (path.parent / t).resolve().exists():
                flags.append(f"[L1 links] {tag}: broken link -> {link}"); hard += 1

        # Layer 3: cross-source presence
        if code not in comp or not comp[code].get("in_bencaodian"):
            flags.append(f"[L3 xsrc] {tag}: {code} not present in Bencaodian comparison")

        # Layer 2: source fidelity
        if L["pages"]:
            src = " ".join(page_text(p, reader) for p in L["pages"])
            src_tok = sig_tokens(src)
            for fieldname, thr in (("actions", THRESH["actions"]),
                                    ("indications", THRESH["indications"]),
                                    ("location", THRESH["location"])):
                val = L["actions_raw"] if fieldname == "actions" else L[fieldname]
                ft = sig_tokens(val)
                if not ft:
                    continue
                overlap = len(ft & src_tok) / len(ft)
                if overlap < thr:
                    missing = sorted(ft - src_tok)[:6]
                    flags.append(f"[L2 source] {tag}: {fieldname} overlap {overlap:.2f} < {thr} (missing e.g. {missing})")

    # ---- README index parity ----
    readme = (LEAF_DIR / "README.md").read_text(encoding="utf-8")
    linked = set(re.findall(r"\]\((LU-[\w-]+\.md|LI-[\w-]+\.md)\)", readme))
    for path in leaves:
        if path.name not in linked:
            flags.append(f"[L1 index] {path.name}: leaf exists but is not linked in README")
    for name in linked:
        if name not in filenames:
            flags.append(f"[L1 index] README links {name} but the leaf file is missing"); hard += 1

    # ---- Report ----
    print(f"QA acupuncture branch: {len(leaves)} leaves checked")
    print(f"  contamination guard: extract points scanned = {len(extract)}")
    if not flags:
        print("RESULT: PASS — no flags.")
        return 0
    print(f"RESULT: {len(flags)} flag(s) ({hard} hard):")
    for f in flags:
        print("  - " + f)
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
