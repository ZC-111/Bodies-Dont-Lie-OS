#!/usr/bin/env python3
"""Extract acupuncture points from Deadman Manual PDF (v0.2)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Optional

from pypdf import PdfReader

DEFAULT_PDF = str(Path(__file__).resolve().parents[1] / "sources/pdfs/A-manual-of-acupuncture-peter-deadman.pdf")
BODY_START = 75
BODY_END = 612
INDEX_START = 668

CODE_PATTERN = (
    r"(?:LU|LI|L\.I\.|L\.1\.|ST|SP|HE|HT|SI|BL|KI|KID|PC|P|TE|SJ|GB|LIV|LR|REN|DU|"
    r"M-[A-Z]{2}|N-[A-Z]{2}|MN-[A-Z]{2})[\-\s\.]*\d{1,2}[A-Z]?"
)


MERIDIAN_MAX = {
    "LU": 11, "LI": 20, "ST": 45, "SP": 21, "HE": 9, "SI": 19, "BL": 67,
    "KID": 27, "PC": 9, "P": 9, "SJ": 23, "GB": 44, "LIV": 14, "REN": 24, "DU": 28,
}


def clean_pdf_text(text: str) -> str:
    """Fix common Deadman PDF OCR artifacts before parsing."""
    text = re.sub(r"\b(KID|ST|BL|GB|LU|LI|SP|SI|PC|P|SJ|REN|DU|HE|LIV)-(\d)\s+(\d)\b", r"\1-\2\3", text)
    text = re.sub(r"\bBe-(\d{1,2})\b", r"BL-\1", text)
    text = text.replace("M-BW-I", "M-BW-1")
    text = text.replace("N-HN-54", "M-HN-54")
    text = re.sub(
        r"\.H A mL -\s*\nSupport the Mountain",
        "CHENGSHAN BL-57\nSupport the Mountain",
        text,
    )
    text = re.sub(r"QlSHE ST-1 1", "QISHE ST-11", text)
    text = re.sub(r"Shuitu ST-1 0", "Shuitu ST-10", text)
    text = re.sub(r"SHUPTU ST-1 8", "SHUITU ST-10", text)
    text = re.sub(r"QlXUE KID-1 3", "QIXUE KID-13", text)
    text = re.sub(r"QUEPEN ST-1 2", "QUEPEN ST-12", text)
    text = re.sub(r"QlNGLlNC", "QINGLING", text)
    text = re.sub(r"QlNGLl", "QINGLING", text)
    return text


def is_valid_code(code: str) -> bool:
    if code.startswith(("M-", "N-", "MN-")):
        return True
    m = re.match(r"^([A-Z]+)-(\d+)$", code)
    if not m:
        return False
    mer, num = m.group(1), int(m.group(2))
    max_n = MERIDIAN_MAX.get(mer)
    return max_n is not None and 1 <= num <= max_n


def normalize_code(raw: str) -> Optional[str]:
    if not raw:
        return None

    s = raw.upper().strip().replace(" ", "")
    s = s.replace("L.1.", "LI-").replace("L.I.", "LI-").replace("L.I", "LI")
    s = re.sub(r"^(KID|ST|SP|BL|GB|LIV|REN|DU|HE|SI|PC|SJ|LU|LI)(\d{1,2})$", r"\1-\2", s)
    s = s.replace(".", "-")
    while "--" in s:
        s = s.replace("--", "-")

    m = re.match(r"^(LU|LI|ST|SP|HE|SI|BL|KID|PC|P|SJ|GB|LIV|REN|DU)-(\d{1,2})$", s)
    if m:
        return f"{m.group(1)}-{int(m.group(2))}"
    m = re.match(r"^(M-[A-Z]{2}-\d+|N-[A-Z]{2}-\d+|MN-[A-Z]{2}-\d+)$", s)
    if m:
        return s
    return None


SECTION_HEADERS = frozenset({
    "LOCATION", "LOCATION NOTE", "NEEDLING", "ACTIONS", "INDICATIONS", "COMMENTARY", "COMBINATIONS",
})


def extract_section(block: str, name: str, next_names: list[str]) -> str:
    pattern = re.compile(rf"(?<=\n){re.escape(name)}\s*\n", re.I)
    m = pattern.search(block)
    if not m:
        return ""
    start = m.end()
    end = len(block)
    for nxt in next_names:
        nm = re.search(rf"(?<=\n){re.escape(nxt)}\s*\n", block[start:], re.I)
        if nm:
            end = min(end, start + nm.start())
    return re.sub(r"\s+", " ", block[start:end]).strip()


def parse_point_block(
    block: str,
    code: str,
    header: str,
    name_en: str,
    page: int,
    point_type: str,
) -> dict:
    lines = [l.strip() for l in block.split("\n") if l.strip()]
    categories_parts = []
    for line in lines[1:6]:
        if line.startswith(("LOCATION", "NEEDLING", "ACTIONS")):
            break
        if len(line) < 180 and not re.search(CODE_PATTERN, line):
            categories_parts.append(line)
    categories = " | ".join(categories_parts)

    return {
        "code": code,
        "type": point_type,
        "header": header.strip(),
        "name_en": name_en.strip(),
        "categories": categories,
        "location_en": extract_section(block, "LOCATION", ["LOCATION NOTE", "NEEDLING", "ACTIONS", "INDICATIONS", "COMMENTARY"]),
        "location_note_en": extract_section(block, "LOCATION NOTE", ["NEEDLING", "ACTIONS", "INDICATIONS", "COMMENTARY"]),
        "needling_en": extract_section(block, "NEEDLING", ["ACTIONS", "INDICATIONS", "COMMENTARY", "COMBINATIONS"]),
        "actions_en": extract_section(block, "ACTIONS", ["INDICATIONS", "COMMENTARY", "COMBINATIONS"]),
        "indications_en": extract_section(block, "INDICATIONS", ["COMMENTARY", "COMBINATIONS"]),
        "commentary_en": extract_section(block, "COMMENTARY", ["COMBINATIONS"]),
        "combinations_en": extract_section(block, "COMBINATIONS", []),
        "page": page,
        "source": "deadman_manual_1e_pdf",
    }


HEADER_CLASSICAL = re.compile(
    rf"^([A-Za-z][A-Za-z \-\'\(\)]+?)\s+({CODE_PATTERN})\s*$",
    re.M,
)
HEADER_CAPS = re.compile(
    rf"^([A-Z][A-Z \-]+)\s+({CODE_PATTERN})\s*$",
    re.M,
)
HEADER_SPLIT = re.compile(
    rf"^([A-Za-z][A-Za-z \-]+)\s*\n\s*({CODE_PATTERN})\s*$",
    re.M,
)
HEADER_EXTRA_PARENS = re.compile(
    rf"^([A-Za-z][A-Za-z \-]+?)\s*\(({CODE_PATTERN})\)\s*$",
    re.M,
)
CODE_IN_LINE = re.compile(rf"\b({CODE_PATTERN})\b")


def entry_score(entry: dict) -> tuple:
    """Higher is better when choosing between duplicate codes."""
    loc = len(entry.get("location_en") or "")
    other = sum(len(entry.get(k) or "") for k in ("needling_en", "actions_en", "indications_en", "commentary_en"))
    name = (entry.get("name_en") or "").strip().upper()
    garbage = name in SECTION_HEADERS
    return (loc, other, 0 if garbage else 1, len(entry.get("categories") or ""))


TEXT_FIELDS = (
    "header", "name_en", "categories",
    "location_en", "location_note_en", "needling_en",
    "actions_en", "indications_en", "commentary_en", "combinations_en",
)


def merge_entry(existing: dict, candidate: dict) -> dict:
    if entry_score(candidate) > entry_score(existing):
        primary, secondary = candidate, existing
    else:
        primary, secondary = existing, candidate
    merged = dict(primary)
    for field in TEXT_FIELDS:
        cur = (merged.get(field) or "").strip()
        other = (secondary.get(field) or "").strip()
        if not cur and other:
            merged[field] = secondary[field]
        elif field == "location_en" and other and len(other) > len(cur):
            merged[field] = secondary[field]
    merged["page"] = merged.get("page") or secondary.get("page")
    return merged


GAP_FILL_FIELDS = TEXT_FIELDS + ("page",)

COMPARATIVE_CODE_ALIASES = {
    "SJ-": "TE-",
}


def looks_like_corrupted_name(name: str) -> bool:
    if not name or not name.strip():
        return True
    n = name.strip()
    if len(n) > 55:
        return True
    loc_starts = (
        "1.5 cun", "in the", "on the", "lower border", "Directly", "midway",
        "0.5", "3 cun", "At the", "Below", "Superior", "Inferior", "Between",
    )
    return any(n.startswith(s) for s in loc_starts)


def apply_gap_fill(extracted: dict[str, dict], gap_path: Path) -> int:
    """Merge manual gap-fill patches for points the PDF parser misses."""
    if not gap_path.exists():
        return 0

    data = json.loads(gap_path.read_text(encoding="utf-8"))
    patches = data.get("points", {})
    source = data.get("meta", {}).get("source", "deadman_manual_1e_pdf_manual_gap_fill")
    filled = 0

    for code, patch in patches.items():
        if code not in extracted:
            continue
        entry = extracted[code]
        had_location = bool((entry.get("location_en") or "").strip())

        for field in GAP_FILL_FIELDS:
            raw = patch.get(field)
            if raw is None:
                continue
            if field == "page":
                if not entry.get("page"):
                    entry[field] = raw
                continue
            val = str(raw).strip()
            if not val:
                continue
            cur = (entry.get(field) or "").strip()
            if field == "name_en" and cur and not looks_like_corrupted_name(cur):
                continue
            if field == "header" and cur and not is_corrupt_header(cur):
                continue
            if not cur or (field == "name_en" and looks_like_corrupted_name(cur)):
                entry[field] = patch[field] if field != "header" else patch[field].upper()
            elif field != "name_en" and field != "header":
                entry[field] = patch[field]

        if not had_location and (entry.get("location_en") or "").strip():
            filled += 1
        entry["gap_fill_source"] = source

    return filled


def comparative_lookup_code(code: str) -> str:
    for deadman_prefix, comp_prefix in COMPARATIVE_CODE_ALIASES.items():
        if code.startswith(deadman_prefix):
            return comp_prefix + code[len(deadman_prefix):]
    return code


def load_comparative_index(comp_path: Path) -> dict[str, dict]:
    if not comp_path.exists():
        return {}
    data = json.loads(comp_path.read_text(encoding="utf-8"))
    index: dict[str, dict] = {}
    for section in ("Ordinary Points", "Extraordinary Points"):
        for code, rec in (data.get(section) or {}).items():
            index[code] = rec
    return index


def parse_comparative_i18n(rec: dict) -> dict:
    """Normalize scrambled english/pinyin fields from the comparative export."""
    out: dict = {}
    if rec.get("chinese") and rec["chinese"] != "N/A":
        out["chinese"] = rec["chinese"]

    for key in ("korean", "vietnamese", "romaji", "alternative_names", "who_code"):
        val = rec.get(key)
        if val and val != "N/A":
            out[key] = val

    english = (rec.get("english") or "").strip()
    translit = (rec.get("pinyin_translit") or "").strip()
    pinyin_field = (rec.get("pinyin") or "").strip()

    tone_marks = re.compile(r"[āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]")
    if english and tone_marks.search(english):
        out["pinyin"] = english
    elif pinyin_field and tone_marks.search(pinyin_field):
        out["pinyin"] = pinyin_field

    for candidate in (english, translit):
        if not candidate or candidate == "N/A":
            continue
        if tone_marks.search(candidate):
            continue
        if re.match(r"^[A-Za-z][A-Za-z \-/'\(\),]+$", candidate):
            out.setdefault("comparative_name_en", candidate)
            break

    if rec.get("location") and rec["location"] != "N/A":
        out["comparative_location"] = rec["location"]
    if rec.get("clinical_actions") and rec["clinical_actions"] != "N/A":
        out["comparative_actions"] = rec["clinical_actions"]

    return out


def enrich_from_comparative(extracted: dict[str, dict], comp_path: Path) -> int:
    """Add i18n and cross-reference fields from acupuncture-comparative-database.json."""
    index = load_comparative_index(comp_path)
    if not index:
        return 0

    enriched = 0
    for code, entry in extracted.items():
        rec = index.get(comparative_lookup_code(code))
        if not rec:
            continue
        i18n = parse_comparative_i18n(rec)
        if not i18n:
            continue

        entry.setdefault("i18n", {})
        entry["i18n"].update(i18n)
        if not (entry.get("location_en") or "").strip() and i18n.get("comparative_location"):
            entry["location_en"] = i18n["comparative_location"]
            entry.setdefault("gap_fill_source", "acupuncture_comparative_database")
        if not (entry.get("actions_en") or "").strip() and i18n.get("comparative_actions"):
            entry["actions_en"] = i18n["comparative_actions"]
        enriched += 1

    return enriched


def is_corrupt_header(header: str) -> bool:
    h = header.strip()
    if len(h) < 3:
        return True
    if re.match(r"^I\s", h):
        return True
    if h.startswith("/"):
        return True
    if re.match(r"^\d", h):
        return True
    return False


def header_line_match(line: str) -> Optional[tuple[str, str]]:
    for pat in (HEADER_CAPS, HEADER_CLASSICAL):
        hm = pat.match(line)
        if hm:
            code = normalize_code(hm.group(2))
            header = hm.group(1).strip()
            if code and is_valid_code(code) and not is_corrupt_header(header):
                return code, header
    return None


def parse_index(text: str) -> dict[str, str]:
    index: dict[str, str] = {}
    pending_code: Optional[str] = None

    for raw_line in text.split("\n"):
        line = raw_line.strip()
        if not line or "Point numbers index" in line:
            continue
        if line.startswith("The ") and "channel" in line or line.startswith("The Extraordinary"):
            pending_code = None
            continue
        if line.startswith("Extraordinary points alphabetical"):
            pending_code = None
            continue

        m = re.match(rf"^({CODE_PATTERN})\s*(.*)$", line)
        if m:
            code = normalize_code(m.group(1))
            if not code:
                pending_code = None
                continue
            name = m.group(2).strip()
            if name:
                index[code] = name
                pending_code = None
            else:
                pending_code = code
            continue

        if pending_code and re.match(r"^[A-Za-z]", line) and not CODE_IN_LINE.search(line):
            index[pending_code] = line
            pending_code = None

    return index


def find_entry_starts(text: str) -> list[tuple[int, str, str, str]]:
    """Return list of (start_pos, code, header, format)."""
    starts: dict[int, tuple[str, str, str]] = {}

    for m in HEADER_CAPS.finditer(text):
        code = normalize_code(m.group(2))
        if code:
            starts[m.start()] = (code, m.group(1).strip(), "classical")

    for m in HEADER_CLASSICAL.finditer(text):
        code = normalize_code(m.group(2))
        if code and m.start() not in starts:
            header = m.group(1).strip()
            if not is_corrupt_header(header):
                starts[m.start()] = (code, header, "classical")

    for m in HEADER_SPLIT.finditer(text):
        code = normalize_code(m.group(2))
        header = m.group(1).strip()
        if code and not is_corrupt_header(header):
            starts[m.start()] = (code, header, "classical")

    for m in HEADER_EXTRA_PARENS.finditer(text):
        code = normalize_code(m.group(2))
        if code:
            starts[m.start()] = (code, m.group(1).strip(), "extraordinary")

    # Scrambled pages: header immediately followed by NEEDLING
    for m in re.finditer(rf"^([A-Za-z][A-Za-z \-]+)\s+({CODE_PATTERN})\s*\nNEEDLING\s*\n", text, re.M):
        code = normalize_code(m.group(2))
        header = m.group(1).strip()
        if code and not is_corrupt_header(header) and m.start() not in starts:
            starts[m.start()] = (code, header, "classical")

    return sorted((pos, code, header, fmt) for pos, (code, header, fmt) in starts.items())


def code_from_context(before: str, after: str = "") -> tuple[Optional[str], str]:
    lines = [l.strip() for l in before.split("\n") if l.strip()]
    caps_match: Optional[tuple[str, str]] = None
    last_match: Optional[tuple[str, str]] = None
    for line in lines:
        hit = header_line_match(line)
        if hit:
            last_match = hit
            if HEADER_CAPS.match(line):
                caps_match = hit
    if caps_match:
        return caps_match
    if last_match:
        return last_match

    # Split header: Name on one line, CODE on the next
    after_lines = [l.strip() for l in after.split("\n")[:4] if l.strip()]
    if lines and after_lines:
        m = re.match(rf"^({CODE_PATTERN})$", after_lines[0])
        if m:
            code = normalize_code(m.group(1))
            header = lines[-1]
            if code and is_valid_code(code) and not is_corrupt_header(header):
                return code, header

    for line in reversed(lines[-10:]):
        cm = CODE_IN_LINE.search(line)
        if cm:
            c = normalize_code(cm.group(1))
            if c and is_valid_code(c):
                return c, re.sub(CODE_PATTERN, "", line).strip()

    # Header may appear after a scrambled LOCATION section
    fwd_lines = [l.strip() for l in after.split("\n") if l.strip()]
    for line in fwd_lines[:8]:
        hit = header_line_match(line)
        if hit:
            return hit
    for i, line in enumerate(fwd_lines[:6]):
        m = re.match(rf"^({CODE_PATTERN})$", line)
        if m and i > 0:
            code = normalize_code(m.group(1))
            header = fwd_lines[i - 1]
            if code and is_valid_code(code) and re.match(r"^[A-Za-z]", header):
                return code, header
    return None, ""


def location_sentence(text: str) -> str:
    """Pull the most likely location sentence from noisy LOCATION preamble."""
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    parts = re.split(r"(?<=[\.!?])\s+", text)
    loc_keywords = (
        "cun", "depression", "border", "lateral", "midline", "intersection",
        "proximal", "distal", "inferior", "superior", "medial", "posterior",
        "anterior", "line connecting", "fold", "crease", "process", "vertebra",
        "axilla", "popliteal", "medial malleolus", "olecranon",
    )
    ranked = []
    for part in parts:
        low = part.lower()
        score = sum(1 for k in loc_keywords if k in low)
        if re.match(r"^In the ", part):
            score += 2
        if CODE_IN_LINE.search(part) and score < 2:
            score -= 1
        if len(part) > 20:
            ranked.append((score, part.strip()))
    if ranked:
        ranked.sort(key=lambda x: x[0], reverse=True)
        if ranked[0][0] > 0:
            return ranked[0][1]
    return parts[-1].strip() if parts else text


def ingest_location_match(
    text: str,
    start: int,
    end: int,
    page: int,
    existing: dict[str, dict],
) -> None:
    before = text[max(0, start - 800): start]
    after = text[start: min(len(text), start + 300)]
    code, header = code_from_context(before, after)
    if not code:
        return

    full_block = text[max(0, start - 400): end]
    name_en = ""
    hdr_idx = full_block.rfind(header) if header else -1
    tail = full_block[hdr_idx + len(header):] if hdr_idx >= 0 else full_block
    for line in tail.split("\n"):
        line = line.strip()
        if not line or line.upper().startswith(tuple(SECTION_HEADERS)):
            continue
        if CODE_IN_LINE.search(line):
            continue
        if len(line) < 80 and re.match(r"^[A-Za-z]", line):
            name_en = line
            break

    ptype = "extraordinary" if code.startswith(("M-", "N-", "MN-")) else "classical"
    entry = parse_point_block(full_block, code, header, name_en, page, ptype)
    if not entry.get("location_en"):
        loc_raw = text[start:end]
        loc_m = re.search(r"LOCATION\s*(.*)", loc_raw, re.I | re.S)
        if loc_m:
            entry["location_en"] = location_sentence(loc_m.group(1))
    if is_valid_code(code):
        existing[code] = merge_entry(existing[code], entry) if code in existing else entry


def extract_location_blocks(text: str, page: int, existing: dict[str, dict]) -> None:
    """Find LOCATION sections (standard and inline) and associate with nearest header."""
    patterns = [
        r"\nLOCATION\s*\n",
        r"(?<=[\.\"])\sLOCATION\s+\n",
        r"(?<=[\.\"])\sLOCATION\s+(?=[A-Z])",
    ]
    seen: set[int] = set()
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            if m.start() in seen:
                continue
            seen.add(m.start())
            nxt = re.search(
                r"\n(?:LOCATION NOTE|NEEDLING|ACTIONS|INDICATIONS|COMMENTARY|COMBINATIONS)\s*\n",
                text[m.end():],
                re.I,
            )
            end = m.end() + (nxt.start() if nxt else 2500)
            ingest_location_match(text, m.start(), end, page, existing)


LOCATION_FIELDS = ("location_en", "location_note_en")


def propagate_cluster_fields(extracted: dict[str, dict]) -> None:
    """Share only LOCATION text between points that name each other as landmarks.

    A code appearing in a point's LOCATION prose (e.g. "7 cun proximal to Taiyuan
    LU-9") is an anatomical landmark, not a shared clinical block. Clinical
    sections (needling / actions / indications / commentary / combinations) are
    therefore NEVER copied between points: doing so misattributes one point's
    text to another (e.g. LU-9 Taiyuan previously inherited LU-6 Kongzui's
    actions). We only fill a *missing* location from a neighbour that references
    it, and we record that fill in ``propagated_fields`` so validation can flag
    it. A point's own parsed section is never overwritten.
    """
    snapshots = {code: dict(entry) for code, entry in extracted.items()}
    clusters: list[tuple[dict, list[str]]] = []

    for entry in snapshots.values():
        blob = " ".join(entry.get(k, "") or "" for k in LOCATION_FIELDS)
        codes: list[str] = []
        for cm in CODE_IN_LINE.finditer(blob):
            c = normalize_code(cm.group(1))
            if c and is_valid_code(c) and c not in codes:
                codes.append(c)
        if len(codes) >= 2:
            clusters.append((entry, codes))

    for entry, codes in clusters:
        for code in codes:
            if code not in extracted:
                continue
            target = extracted[code]
            for field in LOCATION_FIELDS:
                if not (target.get(field) or "").strip() and (entry.get(field) or "").strip():
                    target[field] = entry[field]
                    flags = target.setdefault("propagated_fields", [])
                    if field not in flags:
                        flags.append(field)

    for entry, codes in clusters:
        own = extracted.get(entry["code"])
        if own and own.get("location_en"):
            own["location_en"] = re.sub(
                rf"\s*(?:{'|'.join(re.escape(c) for c in codes)})\s*",
                " ",
                own["location_en"],
            ).strip()
            own["location_en"] = re.sub(r"\s+", " ", own["location_en"])


def extract_from_body(reader: PdfReader) -> dict[str, dict]:
    points: dict[str, dict] = {}
    prev_tail = ""

    for page_num in range(BODY_START, BODY_END + 1):
        page_text = clean_pdf_text(reader.pages[page_num].extract_text() or "")
        if not page_text.strip():
            prev_tail = ""
            continue

        text = prev_tail + page_text
        prev_tail = page_text[-900:] if len(page_text) > 900 else page_text

        starts = find_entry_starts(text)
        tail_len = len(prev_tail)
        for i, (pos, code, header, fmt) in enumerate(starts):
            if tail_len and pos < tail_len:
                continue
            end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
            block = text[pos:end]
            name_en = ""
            after_header = text[pos:].split("\n", 2)
            if len(after_header) > 1:
                candidate = after_header[1].strip()
                if candidate and not candidate.startswith(("LOCATION", "Jing-", "Luo-", "Meeting", "Front-", "Ma ", "Gao ")):
                    if not CODE_IN_LINE.search(candidate) and len(candidate) < 100:
                        name_en = candidate
            entry = parse_point_block(block, code, header, name_en, page_num + 1, fmt)
            if is_valid_code(code):
                points[code] = merge_entry(points[code], entry) if code in points else entry

        extract_location_blocks(text, page_num + 1, points)

    return points


def main(pdf_path: str, out_path: str) -> None:
    reader = PdfReader(pdf_path)
    index_text = clean_pdf_text(
        "\n".join(
            (reader.pages[i].extract_text() or "") for i in range(INDEX_START, min(INDEX_START + 4, len(reader.pages)))
        )
    )
    canonical_index = parse_index(index_text)
    extracted = extract_from_body(reader)
    propagate_cluster_fields(extracted)

    for code, name in canonical_index.items():
        if not is_valid_code(code):
            continue
        if code in extracted:
            if not extracted[code].get("name_en"):
                extracted[code]["name_en"] = name
        else:
            ptype = "extraordinary" if code.startswith(("M-", "N-", "MN-")) else "classical"
            extracted[code] = {
                "code": code,
                "type": ptype,
                "header": "",
                "name_en": name,
                "categories": "",
                "location_en": "",
                "location_note_en": "",
                "needling_en": "",
                "actions_en": "",
                "indications_en": "",
                "commentary_en": "",
                "combinations_en": "",
                "page": None,
                "source": "deadman_manual_1e_pdf",
                "index_only": True,
            }

    # Drop invalid OCR codes; fix type for microsystem codes
    for code in list(extracted.keys()):
        if not is_valid_code(code):
            del extracted[code]
        elif code.startswith(("M-", "N-", "MN-")):
            extracted[code]["type"] = "extraordinary"

    # Remove index_only flag when full text was extracted
    for entry in extracted.values():
        if entry.get("location_en"):
            entry.pop("index_only", None)

    data_dir = Path(out_path).parent
    gap_filled = apply_gap_fill(extracted, data_dir / "deadman-gap-fill.json")
    comparative_enriched = enrich_from_comparative(extracted, data_dir / "acupuncture-comparative-database.json")

    def sort_key(code: str):
        if code.startswith(("M-", "N-", "MN-")):
            return (1, code)
        m = re.match(r"^([A-Z]+)-(\d+)$", code)
        return (0, m.group(1), int(m.group(2))) if m else (0, code, 0)

    classical_codes = sorted([c for c in extracted if extracted[c]["type"] == "classical"], key=sort_key)
    extraordinary_codes = sorted([c for c in extracted if extracted[c]["type"] == "extraordinary"], key=sort_key)

    classical_index = {c for c in canonical_index if not c.startswith(("M-", "N-", "MN-"))}
    missing = sorted(classical_index - set(classical_codes))
    index_only = sorted([c for c in classical_codes if extracted[c].get("index_only")])
    with_location = [c for c in classical_codes if extracted[c].get("location_en")]
    with_any_text = [
        c for c in classical_codes
        if any(extracted[c].get(k) for k in ("location_en", "needling_en", "actions_en", "indications_en", "commentary_en"))
    ]
    extra_with_location = [c for c in extraordinary_codes if extracted[c].get("location_en")]

    output = {
        "meta": {
            "version": "0.2.1",
            "revision": "Clinical sections no longer propagated across landmark clusters (fixes cross-point contamination, e.g. LU-9 inheriting LU-6 text).",
            "source": pdf_path,
            "total_extracted": len(extracted),
            "classical_count": len(classical_codes),
            "extraordinary_count": len(extraordinary_codes),
            "classical_in_index": len(classical_index),
            "classical_with_full_text": len(with_location),
            "classical_with_any_text": len(with_any_text),
            "extraordinary_with_full_text": len(extra_with_location),
            "classical_index_only": len(index_only),
            "missing_from_index": missing,
            "index_only_codes": index_only,
            "gap_filled_count": gap_filled,
            "comparative_enriched_count": comparative_enriched,
        },
        "points": [extracted[c] for c in classical_codes + extraordinary_codes],
    }

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(json.dumps(output["meta"], indent=2))


if __name__ == "__main__":
    pdf = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PDF
    out = sys.argv[2] if len(sys.argv) > 2 else "Research/acupuncture/data/deadman-extract-v0.2.json"
    main(pdf, out)
