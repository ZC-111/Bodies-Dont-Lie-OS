#!/usr/bin/env python3
"""Apply gap-fill and comparative-database enrichments to an existing Deadman extract."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from deadman_extract import apply_gap_fill, enrich_from_comparative  # noqa: E402


def main(in_path: str, out_path: str | None = None) -> None:
    in_file = Path(in_path)
    out_file = Path(out_path or in_path)
    data_dir = in_file.parent

    payload = json.loads(in_file.read_text(encoding="utf-8"))
    extracted = {p["code"]: p for p in payload["points"]}

    gap_filled = apply_gap_fill(extracted, data_dir / "deadman-gap-fill.json")
    comparative_enriched = enrich_from_comparative(
        extracted, data_dir / "acupuncture-comparative-database.json"
    )

    classical = [c for c in extracted if extracted[c]["type"] == "classical"]
    extraordinary = [c for c in extracted if extracted[c]["type"] == "extraordinary"]
    missing_loc_classical = [c for c in classical if not extracted[c].get("location_en")]
    missing_loc_extra = [c for c in extraordinary if not extracted[c].get("location_en")]

    def sort_key(code: str):
        import re
        if code.startswith(("M-", "N-", "MN-")):
            return (1, code)
        m = re.match(r"^([A-Z]+)-(\d+)$", code)
        return (0, m.group(1), int(m.group(2))) if m else (0, code, 0)

    ordered = sorted(classical, key=sort_key) + sorted(extraordinary, key=sort_key)
    payload["points"] = [extracted[c] for c in ordered]
    payload["meta"]["gap_filled_count"] = gap_filled
    payload["meta"]["comparative_enriched_count"] = comparative_enriched
    payload["meta"]["classical_with_full_text"] = len(classical) - len(missing_loc_classical)
    payload["meta"]["extraordinary_with_full_text"] = len(extraordinary) - len(missing_loc_extra)

    out_file.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Gap-filled locations: {gap_filled}")
    print(f"Comparative i18n enriched: {comparative_enriched}")
    print(f"Classical missing location_en: {len(missing_loc_classical)} {missing_loc_classical}")
    print(f"Extraordinary missing location_en: {len(missing_loc_extra)} {missing_loc_extra}")
    print(f"Wrote {out_file}")


if __name__ == "__main__":
    inp = sys.argv[1] if len(sys.argv) > 1 else "Research/acupuncture/data/deadman-extract-v0.2.json"
    out = sys.argv[2] if len(sys.argv) > 2 else inp
    main(inp, out)
