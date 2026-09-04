#!/usr/bin/env python3
"""Generate educational anterior-body SVG maps for clinical protocol packs.

Point coordinates are approximate teaching positions on a simplified silhouette.
Always verify needling locations against Deadman / atlas sources.
"""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets" / "infographics"

POINTS = {
    "DU-20": (200, 42),
    "M-HN-3": (200, 78),
    "M-HN-34": (248, 90),
    "GB-20": (168, 95),
    "GB-8": (255, 88),
    "LI-4": (95, 310),
    "LI-11": (78, 250),
    "HE-7": (318, 335),
    "P-6": (305, 350),
    "LU-7": (88, 345),
    "TB-6": (320, 360),
    "REN-12": (200, 285),
    "REN-6": (200, 355),
    "REN-4": (200, 375),
    "ST-25": (168, 320),
    "ST-21": (175, 270),
    "LV-13": (145, 300),
    "ST-36": (155, 455),
    "ST-37": (150, 490),
    "SP-6": (230, 520),
    "SP-9": (235, 470),
    "SP-10": (240, 430),
    "SP-4": (245, 585),
    "KID-1": (210, 680),
    "KID-3": (225, 610),
    "KID-6": (220, 625),
    "LV-3": (185, 640),
    "LV-2": (175, 650),
    "ST-44": (160, 655),
    "ST-40": (150, 530),
    "GB-34": (140, 465),
    "GB-39": (145, 545),
    "BL-62": (255, 615),
    "SP-1": (250, 670),
    "ST-45": (155, 675),
    "BL-17": (175, 230),
    "BL-18": (170, 245),
    "BL-19": (165, 255),
    "BL-20": (175, 265),
    "BL-21": (175, 275),
    "BL-23": (175, 330),
    "BL-13": (175, 200),
    "DU-14": (200, 160),
    "HE-6": (312, 340),
    "ST-27": (185, 345),
    "LI-20": (188, 100),
}

BODY = """
  <ellipse cx="200" cy="70" rx="42" ry="50" fill="#f3ebe1" stroke="#5c4a3a" stroke-width="2"/>
  <rect x="185" y="115" width="30" height="28" fill="#f3ebe1" stroke="#5c4a3a" stroke-width="2"/>
  <path d="M140 145 L260 145 L275 360 L250 390 L150 390 L125 360 Z" fill="#f3ebe1" stroke="#5c4a3a" stroke-width="2"/>
  <path d="M140 155 L85 300 L95 310 L150 200 Z" fill="#f3ebe1" stroke="#5c4a3a" stroke-width="2"/>
  <path d="M260 155 L315 300 L305 310 L250 200 Z" fill="#f3ebe1" stroke="#5c4a3a" stroke-width="2"/>
  <path d="M150 390 L145 680 L175 680 L185 390 Z" fill="#f3ebe1" stroke="#5c4a3a" stroke-width="2"/>
  <path d="M215 390 L225 680 L255 680 L250 390 Z" fill="#f3ebe1" stroke="#5c4a3a" stroke-width="2"/>
"""


def make_svg(title: str, subtitle: str, codes: list[str], outfile: str, accent: str = "#c45c26") -> None:
    dots: list[str] = []
    for code in codes:
        if code not in POINTS:
            raise KeyError(code)
        x, y = POINTS[code]
        lx = x + 10 if x < 200 else x - 10
        anchor = "start" if x < 200 else "end"
        dots.append(
            f'<circle cx="{x}" cy="{y}" r="6" fill="{accent}" stroke="#fff" stroke-width="1.5"/>'
        )
        dots.append(
            f'<text x="{lx}" y="{y-8}" text-anchor="{anchor}" font-family="Helvetica,Arial,sans-serif" font-size="9" font-weight="700" fill="#2b2118">{code}</text>'
        )
    legend: list[str] = []
    y = 40
    for code in codes:
        legend.append(f'<circle cx="330" cy="{y}" r="5" fill="{accent}"/>')
        legend.append(
            f'<text x="342" y="{y+4}" font-family="Helvetica,Arial,sans-serif" font-size="11" fill="#2b2118">{code}</text>'
        )
        y += 18
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 760" width="420" height="760">
  <rect width="420" height="760" fill="#faf7f2"/>
  <text x="20" y="28" font-family="Helvetica,Arial,sans-serif" font-size="16" font-weight="700" fill="#2b2118">{title}</text>
  <text x="20" y="46" font-family="Helvetica,Arial,sans-serif" font-size="11" fill="#6b5a4a">{subtitle}</text>
  <g transform="translate(0,20)">{BODY}{''.join(dots)}</g>
  <rect x="310" y="55" width="95" height="{20 + 18 * len(codes)}" fill="#fff" stroke="#d9cfc3" rx="6"/>
  <text x="320" y="72" font-family="Helvetica,Arial,sans-serif" font-size="10" font-weight="700" fill="#6b5a4a">POINTS</text>
  <g transform="translate(0,40)">{''.join(legend)}</g>
  <text x="20" y="745" font-family="Helvetica,Arial,sans-serif" font-size="9" fill="#8a7a6a">Educational approximation — verify locations in Deadman / atlas before needling.</text>
</svg>
"""
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / outfile).write_text(svg)
    print("wrote", outfile)


def main() -> None:
    make_svg("Sleep & Spirit — Classic Trio", "Yintang + HE-7 + SP-6", ["M-HN-3", "HE-7", "SP-6"], "sleep_classic_trio_body.svg")
    make_svg("Sleep & Spirit — Anchor Map", "Primary anchors from sleep-spirit protocols", ["HE-7", "SP-6", "M-HN-3", "M-HN-34", "KID-1", "P-6", "BL-62", "KID-6"], "sleep_anchors_body.svg", "#2f6f6a")
    make_svg("Sleep — HT/SP Deficiency", "Nourish blood & anchor spirit", ["HE-7", "SP-6", "ST-36", "M-HN-3"], "sleep_pattern_ht_sp_xu_body.svg")
    make_svg("Sleep — HT–KI Disharmony", "Nourish KI yin / cool deficiency fire", ["HE-7", "SP-6", "KID-3", "KID-6"], "sleep_pattern_ht_ki_body.svg")
    make_svg("Sleep — Liver Fire", "Drain excess fire & settle LV (+ Anmian)", ["HE-7", "SP-6", "M-HN-34", "BL-18", "BL-19"], "sleep_pattern_lv_fire_body.svg")

    make_svg("Gut & SIBO — Middle-Jiao Duo", "ST-36 + SP-6 + REN-12", ["ST-36", "SP-6", "REN-12"], "gut_classic_middle_jiao_body.svg", "#3d6b4f")
    make_svg("Gut & SIBO — Anchor Map", "Adjunct points for Hill three-phase pairing", ["ST-36", "SP-6", "REN-12", "ST-25", "ST-37", "SP-9", "LV-13", "LV-3", "P-6", "HE-7"], "gut_anchors_body.svg", "#3d6b4f")
    make_svg("Gut — SP Qi Deficiency", "Tonify SP / Phase 2–3 terrain", ["ST-36", "SP-6", "REN-12", "BL-20", "BL-21"], "gut_pattern_sp_qi_xu_body.svg", "#3d6b4f")
    make_svg("Gut — LV Invading SP", "Stress relapse / sympathetic tone", ["LV-3", "LV-13", "ST-36", "SP-6", "REN-12"], "gut_pattern_lv_sp_body.svg", "#3d6b4f")
    make_svg("Gut — Move the Fu", "Motility / distension adjunct", ["ST-25", "ST-37", "TB-6", "ST-36", "LV-3"], "gut_pattern_move_fu_body.svg", "#3d6b4f")

    make_svg("Hair & Scalp — Blood-Nourish Core", "ST-36 + SP-6 + BL-17 + DU-20", ["ST-36", "SP-6", "BL-17", "DU-20"], "hair_classic_blood_nourish_body.svg", "#7a4a6b")
    make_svg("Hair & Scalp — Anchor Map", "Systemic + local vertex focus", ["ST-36", "SP-6", "SP-10", "BL-17", "BL-20", "BL-23", "KID-3", "REN-4", "LV-3", "LI-11", "DU-20", "GB-20"], "hair_anchors_body.svg", "#7a4a6b")
    make_svg("Hair — Blood Deficiency", "Diffuse thinning / pale / fatigue", ["ST-36", "SP-6", "BL-17", "BL-20", "SP-10", "REN-4", "DU-20"], "hair_pattern_blood_xu_body.svg", "#7a4a6b")
    make_svg("Hair — KI Jing Deficiency", "Vertex / aging / postpartum", ["KID-3", "BL-23", "REN-4", "GB-39", "ST-36", "SP-6", "DU-20"], "hair_pattern_ki_jing_body.svg", "#7a4a6b")
    make_svg("Hair — LV Qi Constraint", "Stress telogen", ["LV-3", "LI-4", "GB-20", "SP-6", "HE-7", "DU-20"], "hair_pattern_lv_qi_body.svg", "#7a4a6b")


if __name__ == "__main__":
    main()
