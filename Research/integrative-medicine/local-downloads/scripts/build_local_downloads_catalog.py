#!/usr/bin/env python3
"""Catalog medical lecture packs from /Users/nuu/Downloads into Living Tree tags."""

from __future__ import annotations

import json
import os
import re
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"
OUT_PATH = DATA_DIR / "local-downloads-catalog.json"

DOWNLOADS = Path("/Users/nuu/Downloads")

# Primary docs only — screenshots summarized as counts.
DOC_EXTS = {
    ".pdf",
    ".ppt",
    ".pptx",
    ".doc",
    ".docx",
    ".txt",
    ".rtf",
    ".md",
    ".json",
    ".xlsx",
    ".xls",
    ".csv",
    ".mp3",
    ".m4a",
    ".mp4",
    ".mov",
    ".zip",
}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".heic"}
SKIP_NAMES = {".ds_store"}

# Curated packs: name under Downloads, or exact filename for loose files.
PACKS: list[dict] = [
    {
        "id": "acu-resource",
        "title": "Acupuncture resource",
        "path": "Acupuncture resource",
        "kind": "folder",
        "speaker": None,
        "approx_date": "2026-09",
        "primary_branch": "acupuncture",
        "related_branches": [],
        "themes": ["acupuncture"],
        "medical_terms": ["acupuncture", "kiiko", "deadman", "microsystems", "ear_ap"],
        "notes": "Deadman/Kiiko books + NotebookLM exports; many items already imported under Research/acupuncture/.",
        "already_in_repo": True,
    },
    {
        "id": "peptides-bpc-kpv-2026-05",
        "title": "Peptides BPC-157, KPV, and lorazotide — gut repair / barrier",
        "path": " peptides BPC 157, KPV, and lorazotide for gut repair, inflammation, and barrier control slides 5 5 2026",
        "kind": "folder",
        "speaker": None,
        "approx_date": "2026-05-05",
        "primary_branch": "nutrition",
        "related_branches": ["immune"],
        "themes": ["nutrition", "gi_metabolic", "peptides", "inflammation"],
        "medical_terms": ["peptides", "gi_metabolic", "inflammation", "vitamin_supplement"],
        "notes": "Slide deck PDF + transcript + screenshot sequence.",
    },
    {
        "id": "ivermectin-ayurveda-2026-05",
        "title": "Ivermectin for longevity, cancer, neurodegeneration & quantum Ayurveda",
        "path": "Ivermectin for longevity, cancer, neurodegenerative diseases, & potential of quantum Ayurveda technology 5 19 2026",
        "kind": "folder",
        "speaker": None,
        "approx_date": "2026-05-19",
        "primary_branch": "integrative-medicine",
        "related_branches": ["immune", "materia-medica"],
        "themes": ["longevity", "cancer_onco", "neuro", "infection", "ayurveda"],
        "medical_terms": ["cancer_onco", "neuro", "infection_covid", "herbal_botanical", "longevity"],
        "notes": "Audio + zip + transcript; 99 slide screenshots in nested slides folder. Lecture packet: Research/lectures/ivermectin-ayurveda-2026-05/.",
    },
    {
        "id": "dna-repair-andrews-2026-04",
        "title": "DNA repair healing with Dr. Bill Andrews",
        "path": "DNA repair healing with Dr. Bill Andrews 4 28 2026",
        "kind": "folder",
        "speaker": "Bill Andrews",
        "approx_date": "2026-04-28",
        "primary_branch": "integrative-medicine",
        "related_branches": ["nutrition"],
        "themes": ["longevity", "regenerative", "dna_repair"],
        "medical_terms": ["regenerative", "longevity"],
        "notes": "Large PDF + transcript + 90 slide screenshots. Lecture packet: Research/lectures/dna-repair-andrews-2026-04/.",
    },
    {
        "id": "hashimoto-tano",
        "title": "Hashimoto thyroiditis with Dr Benoit Tano",
        "path": "Hashimoto thyroididtis with Dr Benoit Tano ",
        "kind": "folder",
        "speaker": "Benoit Tano",
        "approx_date": None,
        "primary_branch": "immune",
        "related_branches": ["nutrition"],
        "themes": ["autoimmune", "endocrine_hormone"],
        "medical_terms": ["autoimmune", "endocrine_hormone", "immune"],
        "notes": "Zip + mp3 + transcript. Filename typo: thyroididtis.",
    },
    {
        "id": "emily-autoimmune-2026-04",
        "title": "Insights On Emily — a case of Autoimmune Origin",
        "path": "Insights On Emily:a case of Autoimmune Origin 4 2026",
        "kind": "folder",
        "speaker": None,
        "approx_date": "2026-04",
        "primary_branch": "immune",
        "related_branches": [],
        "themes": ["autoimmune", "case_study"],
        "medical_terms": ["autoimmune", "immune"],
        "notes": "Case-based autoimmune lecture PDF + transcript + screenshots.",
    },
    {
        "id": "integrative-immuno-carbon60",
        "title": "Integrative Immunology — Nutritional Cofactors / Carbon60",
        "path": "Integrative Immunology Nutritional Cofactors in Tissue Using Repair Carbon60",
        "kind": "folder",
        "speaker": None,
        "approx_date": None,
        "primary_branch": "immune",
        "related_branches": ["nutrition"],
        "themes": ["immune", "nutrition", "nutraceutical"],
        "medical_terms": ["immune", "vitamin_supplement", "regenerative"],
        "notes": "Zip + mp3 + transcript.",
    },
    {
        "id": "dpc-hartman-2026-05",
        "title": "Stefan Hartman — starting a DPC practice (LLC / S-corp)",
        "path": "Stefan Hartman presented on starting a DPC practice, emphasizing the benefits of an LLC, S corporation 512 2026",
        "kind": "folder",
        "speaker": "Stefan Hartman",
        "approx_date": "2026-05-12",
        "primary_branch": "integrative-medicine",
        "related_branches": [],
        "themes": ["practice_systems"],
        "medical_terms": ["ethics_systems"],
        "research_priority": "low",
        "notes": "Practice/business ops — low clinical priority. 20 slide screenshots. Lecture packet: Research/lectures/dpc-hartman-2026-05/.",
    },
    {
        "id": "colchicine-cv-prevention",
        "title": "Low-dose colchicine — CV prevention / anti-inflammatory",
        "path": "low-dose colchicine as a cost-effective anti-inflammatory therapy for cardiovascular prevention",
        "kind": "folder",
        "speaker": None,
        "approx_date": None,
        "primary_branch": "integrative-medicine",
        "related_branches": ["immune"],
        "themes": ["cardiometabolic", "inflammation"],
        "medical_terms": ["cardio", "inflammation"],
        "notes": "Zip + mp3 + transcript. Related single: Colchicine uses.pdf.",
    },
    {
        "id": "morgellons-lyme-syphilis",
        "title": "Overlap between Morgellons, Lyme disease, and syphilis",
        "path": "overlap between Morgellons Lyme disease and syphilis",
        "kind": "folder",
        "speaker": None,
        "approx_date": None,
        "primary_branch": "immune",
        "related_branches": [],
        "themes": ["infection", "derm", "chronic_infection"],
        "medical_terms": ["infection_covid", "derm", "immune"],
        "notes": "Zip + mp3 + transcript.",
    },
    {
        "id": "campbell-mold-aosrd-2021",
        "title": "Dr Andrew Campbell — Mold and Mycotoxins (AOSRD 2021)",
        "path": "DR andrew Campbell Mold-and-Mycotoxins-AOSRD 2021.pdf",
        "kind": "file",
        "speaker": "Andrew Campbell",
        "approx_date": "2021",
        "primary_branch": "immune",
        "related_branches": ["integrative-medicine"],
        "themes": ["mold_mycotoxin", "immune"],
        "medical_terms": ["mold_mycotoxin", "immune"],
        "notes": "AOSRD 2021 mold lecture PDF (local copy; 2022 AOSRD pack is on external drive).",
    },
    {
        "id": "brain-and-mycotoxins",
        "title": "Brain and Mycotoxins",
        "path": "BrainandMycotoxins.pdf",
        "kind": "file",
        "speaker": None,
        "approx_date": None,
        "primary_branch": "immune",
        "related_branches": [],
        "themes": ["mold_mycotoxin", "neuro"],
        "medical_terms": ["mold_mycotoxin", "neuro"],
        "notes": None,
    },
    {
        "id": "burton-hormones-2026-04",
        "title": "Dr Lindsay Burton — everything hormones lecture",
        "path": "Dr Lindsay Burton everything hormones lecture 4 2026.txt",
        "kind": "file",
        "speaker": "Lindsay Burton",
        "approx_date": "2026-04",
        "primary_branch": "integrative-medicine",
        "related_branches": ["nutrition"],
        "themes": ["endocrine_hormone"],
        "medical_terms": ["endocrine_hormone"],
        "notes": "Transcript only in Downloads.",
    },
    {
        "id": "integrative-medicine-lecture-notes",
        "title": "Integrative medicine lecture notes",
        "path": "integrative_medicine_lecture_notes.docx",
        "kind": "file",
        "speaker": None,
        "approx_date": None,
        "primary_branch": "integrative-medicine",
        "related_branches": [],
        "themes": ["integrative-medicine"],
        "medical_terms": [],
        "notes": None,
    },
    {
        "id": "colchicine-uses",
        "title": "Colchicine uses",
        "path": "Colchicine uses.pdf",
        "kind": "file",
        "speaker": None,
        "approx_date": None,
        "primary_branch": "integrative-medicine",
        "related_branches": ["immune"],
        "themes": ["cardiometabolic", "inflammation"],
        "medical_terms": ["cardio", "inflammation"],
        "notes": "Companion to low-dose colchicine pack.",
    },
    {
        "id": "deadman-purple-cover",
        "title": "A Manual of Acupuncture (purple cover)",
        "path": "a-manual-of-acupuncture-purple cover.pdf",
        "kind": "file",
        "speaker": "Peter Deadman",
        "approx_date": None,
        "primary_branch": "acupuncture",
        "related_branches": [],
        "themes": ["acupuncture"],
        "medical_terms": ["acupuncture", "deadman"],
        "notes": "Small PDF; fuller Deadman PDF lives in Acupuncture resource folder.",
    },
    {
        "id": "insomnia-reference-guide",
        "title": "Insomnia reference guide",
        "path": "insomnia_reference_guide.pdf",
        "kind": "file",
        "speaker": None,
        "approx_date": None,
        "primary_branch": "acupuncture",
        "related_branches": [],
        "themes": ["acupuncture", "sleep"],
        "medical_terms": ["acupuncture", "psych_behavioral"],
        "notes": "Also present under Acupuncture resource.",
    },
    {
        "id": "hidden-geography-channels-m4a",
        "title": "The hidden geography of acupuncture channels (audio)",
        "path": "The_hidden_geography_of_acupuncture_channels.m4a",
        "kind": "file",
        "speaker": None,
        "approx_date": None,
        "primary_branch": "acupuncture",
        "related_branches": [],
        "themes": ["acupuncture"],
        "medical_terms": ["acupuncture"],
        "notes": "Duplicate of file inside Acupuncture resource.",
    },
    {
        "id": "hair-follicle-optimization",
        "title": "Hair Follicle Optimization Master Research v0.2",
        "path": "Hair_Follicle_Optimization_Master_Research_v0.2.docx",
        "kind": "file",
        "speaker": None,
        "approx_date": None,
        "primary_branch": "integrative-medicine",
        "related_branches": ["nutrition"],
        "themes": ["derm", "regenerative"],
        "medical_terms": ["derm", "regenerative"],
        "notes": None,
    },
]


def slugify(*parts: str) -> str:
    raw = "-".join(p for p in parts if p)
    raw = re.sub(r"[^a-zA-Z0-9]+", "-", raw.lower()).strip("-")
    return raw[:120] or "item"


def classify_kind(ext: str) -> str:
    if ext in {".mp4", ".m4v", ".mov"}:
        return "video"
    if ext in {".m4a", ".mp3"}:
        return "audio"
    if ext in {".ppt", ".pptx"}:
        return "slides"
    if ext == ".zip":
        return "archive"
    if ext in IMAGE_EXTS:
        return "image"
    return "document"


def scan_path(abs_path: Path, kind: str) -> tuple[list[dict], int, int]:
    """Return (documents, screenshot_count, total_bytes including images)."""
    docs: list[dict] = []
    screenshots = 0
    total_bytes = 0

    def add_file(full: Path, rel: str) -> None:
        nonlocal screenshots, total_bytes
        try:
            st = full.stat()
        except OSError:
            return
        total_bytes += st.st_size
        ext = full.suffix.lower()
        if ext in IMAGE_EXTS or full.name.lower().startswith("screenshot"):
            if ext in IMAGE_EXTS:
                screenshots += 1
            return
        if ext not in DOC_EXTS:
            return
        docs.append(
            {
                "filename": full.name,
                "relative_path": rel,
                "source_path": str(full),
                "size_bytes": st.st_size,
                "format": ext.lstrip(".") or "unknown",
                "kind": classify_kind(ext),
            }
        )

    if kind == "file":
        if abs_path.is_file():
            add_file(abs_path, abs_path.name)
        return docs, screenshots, total_bytes

    if not abs_path.is_dir():
        return docs, screenshots, total_bytes

    for dirpath, dirnames, filenames in os.walk(abs_path):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fname in filenames:
            if fname.lower() in SKIP_NAMES:
                continue
            full = Path(dirpath) / fname
            rel = full.relative_to(abs_path).as_posix()
            add_file(full, rel)

    docs.sort(key=lambda d: (-d["size_bytes"], d["relative_path"]))
    return docs, screenshots, total_bytes


def branch_path(name: str) -> str:
    return f"Research/{name}/"


def build() -> dict:
    lectures: list[dict] = []
    missing: list[str] = []
    by_branch: dict[str, int] = {}
    by_theme: dict[str, int] = {}
    total_docs = 0
    total_shots = 0

    for pack in PACKS:
        abs_path = DOWNLOADS / pack["path"]
        if not abs_path.exists():
            missing.append(pack["path"])
            continue

        docs, shots, total_bytes = scan_path(abs_path, pack["kind"])
        total_docs += len(docs)
        total_shots += shots

        primary = pack["primary_branch"]
        by_branch[primary] = by_branch.get(primary, 0) + 1
        for t in pack.get("themes") or []:
            by_theme[t] = by_theme.get(t, 0) + 1

        primary_file = docs[0]["relative_path"] if docs else None
        formats = sorted({d["format"] for d in docs})
        kinds = sorted({d["kind"] for d in docs})

        entry = {
            "id": pack["id"],
            "title": pack["title"],
            "speaker": pack.get("speaker"),
            "approx_date": pack.get("approx_date"),
            "source_root": str(abs_path),
            "kind": pack["kind"],
            "primary_branch": primary,
            "branches": [branch_path(primary)]
            + [branch_path(b) for b in pack.get("related_branches") or []],
            "themes": pack.get("themes") or [],
            "medical_terms": pack.get("medical_terms") or [],
            "research_priority": pack.get("research_priority", "normal"),
            "already_in_repo": pack.get("already_in_repo", False),
            "notes": pack.get("notes"),
            "primary_file": primary_file,
            "formats": formats,
            "kinds": kinds,
            "document_count": len(docs),
            "screenshot_count": shots,
            "total_bytes": total_bytes,
            "files": docs,
        }
        lectures.append(entry)

    lectures.sort(key=lambda L: (L["primary_branch"], L["title"].lower()))

    return {
        "meta": {
            "version": "0.1",
            "cataloged_at": date.today().isoformat(),
            "source": str(DOWNLOADS),
            "machine_user": "nuu",
            "catalog_script": (
                "Research/integrative-medicine/local-downloads/scripts/"
                "build_local_downloads_catalog.py"
            ),
            "local_path": (
                "Research/integrative-medicine/local-downloads/data/"
                "local-downloads-catalog.json"
            ),
            "notes": (
                "Local Downloads medical lecture packs (not external-drive archives). "
                "Screenshots summarized by count; documents/audio/zips listed. "
                "Branch tags follow Research/BRANCH-TAXONOMY.md. Catalog only — no file moves."
            ),
            "branch_taxonomy": {
                "immune": "autoimmune, mold/mycotoxins, infection, immuno",
                "nutrition": "peptides, nutraceuticals, gut barrier, vitamins",
                "acupuncture": "Deadman, Kiiko, channel/point materials",
                "integrative-medicine": "multi-topic / longevity / cardio / hormones / practice",
                "materia-medica": "Ayurveda-adjacent cross-link only when herbal focus",
            },
        },
        "summary": {
            "packs": len(lectures),
            "expected_packs": len(PACKS),
            "missing": missing,
            "documents": total_docs,
            "screenshots": total_shots,
            "by_primary_branch": dict(sorted(by_branch.items())),
            "by_theme": dict(sorted(by_theme.items())),
        },
        "lectures": lectures,
    }


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    catalog = build()
    OUT_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    s = catalog["summary"]
    print(f"Wrote {OUT_PATH}")
    print(
        f"packs={s['packs']} docs={s['documents']} screenshots={s['screenshots']} "
        f"missing={len(s['missing'])}"
    )
    print("by_branch:", s["by_primary_branch"])
    if s["missing"]:
        print("MISSING:", s["missing"])


if __name__ == "__main__":
    main()
