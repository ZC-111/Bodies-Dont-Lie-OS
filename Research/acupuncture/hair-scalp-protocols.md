# Hair & Scalp — Acupuncture Protocols

Clinical quick reference for pattern-based hair thinning, shedding, and scalp symptoms. **Differential first** (labs / derm) — AP supports Blood, Jing, Heat, and stress terrain; it does not replace iron, thyroid, androgen, or autoimmune workups.

Structured data: [data/hair-scalp-protocols-v0.1.json](data/hair-scalp-protocols-v0.1.json)

**System:** `clinical_protocol` — pattern prescriptions + local scalp adjuncts. Cross-reference Deadman for location/needling.  
**Integrative rule:** build a **hair theme hub** that links nutrition/endocrine/immune leaves; keep AP as one fork.

---

## When This Pack Applies

| Presentation | Lead | AP role |
|---|---|---|
| Diffuse shedding + fatigue / pale | Labs (ferritin, TSH, etc.) | Blood Xu protocols |
| Vertex / aging / postpartum | Labs + history | KI Jing Xu protocols |
| Itchy red scalp, rapid loss | Derm if severe | Blood Heat / Wind |
| Stress telogen | History | LV Qi yu + shen |
| Patchy alopecia areata | Derm / autoimmune | Cautious local + systemic Xu/Heat pattern |
| Androgenetic pattern | Endocrine / derm | Adjunct only — don’t oversell |

**Red flags:** scarring alopecia, severe infection, sudden patchy loss with systemic illness — refer.

---

## Anchor Points

| Code | Name | Role |
|------|------|------|
| **ST-36** | Zusanli | Tonify qi/blood; systemic rebuild |
| **SP-6** | Sanyinjiao | Nourish Blood/Yin; SP/LV/KI meeting |
| **SP-10** | Xuehai | Move and cool Blood; Blood Heat / stasis adjunct |
| **BL-17** | Geshu | Influential point of Blood; Blood Xu patterns |
| **BL-20** | Pishu | SP back-shu; generate Blood |
| **BL-23** | Shenshu | KI back-shu; Jing / aging / vertex |
| **KID-3** | Taixi | Tonify KI Yin/Yang root |
| **REN-4** | Guanyuan | Root qi/Jing; postpartum / depletion |
| **LV-3** | Taichong | Spread LV qi; stress hair-fall |
| **LI-11** | Quchi | Clear Heat; itchy hot scalp |
| **DU-20** | Baihui | Local vertex; lift clear yang / focus treatment |
| **GB-20** | Fengchi | Wind / stress neck–occiput; tension telogen |

### Local scalp adjuncts (always with a systemic pattern)

| Point / group | Role |
|---|---|
| **DU-20**, Si Shen Cong | Vertex focus |
| **GB-8** | Temporal / side thinning adjunct |
| **Ah-shi** along thinning tracts | Local microcirculation / stimulation |
| **GB-15 / BL-7 region** (as trained) | Forehead / coronal thinning zones |

Needle direction, depth, and electrical stimulation only per training and patient tolerance.

---

## Combinations by Pattern

### Blood Deficiency (diffuse thinning, dull hair, pale, fatigue)

**Points:** ST-36, SP-6, BL-17, BL-20, SP-10, REN-4  
**Local:** DU-20 ± Ah-shi  
**Intent:** nourish and generate Blood; anchor hair “surplus of Blood”  
**Integrative echo:** ferritin / B12 / postpartum; nutrition leaves

### Kidney Jing Deficiency (vertex, premature greying, aging, postpartum Jing drain)

**Points:** KID-3, BL-23, REN-4, GB-39, ST-36, SP-6  
**Local:** DU-20, Si Shen Cong  
**Intent:** tonify Jing and marrow; support root of hair  
**Integrative echo:** age-related / endocrine; don’t skip thyroid labs

### Kidney Yin Deficiency with Empty Heat (night sweat, dry, restless, thinning)

**Points:** KID-3, KID-6, SP-6, HE-6, BL-23  
**Local:** DU-20 light stimulation  
**Intent:** nourish Yin, clear empty Heat  
**Integrative echo:** peri-menopause / HRT context nights

### Blood Heat / Wind in the Skin (itchy, red, greasy-inflamed scalp, rapid shed)

**Points:** SP-10, LI-11, LV-2, DU-14, LI-4  
**Local:** gentle Ah-shi; avoid aggressive trauma on inflamed plaques  
**Intent:** cool Blood, extinguish Wind, clear Heat  
**Integrative echo:** seborrheic / inflammatory derm — refer if scarring

### Liver Qi Constraint (stress telogen, tight neck/jaw, PMS stress)

**Points:** LV-3, LI-4, GB-20, SP-6, HE-7 or Yintang  
**Local:** GB-8 / DU-20 as needed  
**Intent:** spread LV qi, settle shen, reduce stress-shed drive  
**Cross-link:** [sleep-spirit-protocols.md](sleep-spirit-protocols.md)

### Qi and Blood Stagnation (stubborn local patches, dark complexion, history of trauma)

**Points:** SP-10, SP-6, LV-3, LI-4, BL-17  
**Local:** denser Ah-shi around patch borders (trained practitioners)  
**Intent:** move Blood, open local luo  
**Caution:** alopecia areata / scarring — coordinate with derm

### Damp-Heat Scalp (oily, itchy, foul dandruff)

**Points:** SP-9, LI-11, ST-40, GB-34, REN-12  
**Local:** light local only  
**Intent:** resolve Damp-Heat  
**Integrative echo:** fungal / seborrheic pathways — AP adjunct

### Lung Wei-Qi / Exterior (hair fall after febrile illness — classical “Blood dried by Heat”)

**Points:** LI-4, LU-7, ST-36, SP-6, BL-13  
**Intent:** regulate Wei-qi, rebuild post-illness  
**Integrative echo:** post-viral / post-partum / post-antibiotic shed timelines

---

## Suggested Intake Fork (integrative)

```text
Hair complaint
  ├─ Red flags / scarring → derm
  ├─ Labs: ferritin, CBC, TSH±Abs, vitamin D, androgens if indicated
  ├─ Pattern: Blood Xu | KI Jing | Blood Heat | LV Qi | Damp-Heat | mixed
  ├─ AP: systemic pattern + local scalp
  └─ Parallel: nutrition / endocrine / immune leaves + content kit later
```

---

## Code Notes

| Notation | Notes |
|----------|-------|
| Si Shen Cong | Extra points around DU-20 — confirm location per atlas |
| GB-39 | Influential of marrow — Jing/marrow support in KI Xu sets |
| HE-6 | Yin Xi — empty Heat / night sweat adjunct |

---

## Related Files

- [gut-sibo-protocols.md](gut-sibo-protocols.md) — shared SP/ST rebuild points
- [sleep-spirit-protocols.md](sleep-spirit-protocols.md) — stress / shen telogen
- [deadman-extract-v0.2.json](data/deadman-extract-v0.2.json)
- Theme hub (to create): `Research/themes/hair/` when ready

---

*v0.1 draft for integrative hair theme. Expand with clinic-preferred local maps and Kiiko strategies after validation.*
