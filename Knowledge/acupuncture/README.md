# Acupuncture Knowledge Branch

## Purpose

Atomic knowledge objects about acupuncture points — one leaf per confirmed point or concept.

## What Belongs Here

- Confirmed point records (after Research validation)
- One file per point: `What-Is-LU-1-Zhongfu.md` or `LU-1-Zhongfu.md`
- Links to [Research/acupuncture/](../../Research/acupuncture/README.md) source evidence

## Naming Rules

- `{CODE}-{Pinyin-Or-English}.md` (e.g. `LU-1-Zhongfu.md`)
- Only add leaves after Validate stage confirms the record

## Confidence

Correctness is an evolving property, not a binary (Constitution Article VI). Every leaf carries a `Confidence` rung that can only rise as evidence accrues, and is re-audited by [`qa_check.py`](../../Research/acupuncture/scripts/qa_check.py):

| Rung | Meaning |
|------|---------|
| `proposed` | Extracted by tooling; not yet checked against a source. |
| `source-verified` | Each clinical field read directly from a gold-standard source (Deadman) and confirmed present on the cited page; the point also appears in ≥1 comparison source. |
| `cross-confirmed` | Identity and **location** additionally agree with an independent source (Bencaodian); clinical actions/indications remain Deadman-sourced (Bencaodian supplies location, not actions). Low automated overlap requires a documented reconciliation note. |
| `contested` | Sources are present but disagree; the disagreement is documented rather than hidden. |

Run the audit any time: `python3 Research/acupuncture/scripts/qa_check.py`.

## Related Folders

- [Research/acupuncture/](../../Research/acupuncture/README.md) — Raw comparison and extraction data
- [Constitution/Living-Tree/03-Branches.md](../../Constitution/Living-Tree/03-Branches.md) — Branch rules

## Confirmed Leaves

### Lung channel (LU)

Graduated after [Lung Channel Validation](../../Research/acupuncture/lung-channel-validation-v0.1.md), source-verified against Deadman pp. 76–91 — **the complete channel (11/11)**:

| Code | Leaf | Point class |
|------|------|-------------|
| LU-1 | [Zhongfu 中府](LU-1-Zhongfu.md) | Front-Mu of the Lung |
| LU-2 | [Yunmen 雲門](LU-2-Yunmen.md) | — |
| LU-3 | [Tianfu 天府](LU-3-Tianfu.md) | Window of Heaven |
| LU-4 | [Xiabai 俠白](LU-4-Xiabai.md) | — |
| LU-5 | [Chize 尺澤](LU-5-Chize.md) | He-Sea / Water |
| LU-6 | [Kongzui 孔最](LU-6-Kongzui.md) | Xi-Cleft |
| LU-7 | [Lieque 列缺](LU-7-Lieque.md) | Luo-Connecting; Confluent of Ren Mai |
| LU-8 | [Jingqu 經渠](LU-8-Jingqu.md) | Jing-River / Metal |
| LU-9 | [Taiyuan 太淵](LU-9-Taiyuan.md) | Shu-Stream / Yuan-Source / Earth; Hui-Meeting of vessels |
| LU-10 | [Yuji 魚際](LU-10-Yuji.md) | Ying-Spring / Fire |
| LU-11 | [Shaoshang 少商](LU-11-Shaoshang.md) | Jing-Well / Wood |

### Large Intestine channel (LI)

Graduated after [Large Intestine Channel Validation v0.1](../../Research/acupuncture/large-intestine-channel-validation-v0.1.md), source-verified against Deadman pp. 100–120 — **the complete channel (20/20)**:

| Code | Leaf | Point class |
|------|------|-------------|
| LI-1 | [Shangyang 商陽](LI-1-Shangyang.md) | Jing-Well / Metal |
| LI-2 | [Erjian 二間](LI-2-Erjian.md) | Ying-Spring / Water |
| LI-3 | [Sanjian 三間](LI-3-Sanjian.md) | Shu-Stream / Wood |
| LI-4 | [Hegu 合谷](LI-4-Hegu.md) | Yuan-Source; command (face/mouth) |
| LI-5 | [Yangxi 陽谿](LI-5-Yangxi.md) | Jing-River / Fire |
| LI-6 | [Pianli 偏歷](LI-6-Pianli.md) | Luo-Connecting |
| LI-7 | [Wenliu 溫溜](LI-7-Wenliu.md) | Xi-Cleft |
| LI-8 | [Xialian 下廉](LI-8-Xialian.md) | — |
| LI-9 | [Shanglian 上廉](LI-9-Shanglian.md) | — |
| LI-10 | [Shousanli 手三里](LI-10-Shousanli.md) | — |
| LI-11 | [Quchi 曲池](LI-11-Quchi.md) | He-Sea / Earth; Heavenly Star |
| LI-12 | [Zhouliao 肘髎](LI-12-Zhouliao.md) | — |
| LI-13 | [Shouwuli 手五里](LI-13-Shouwuli.md) | — |
| LI-14 | [Binao 臂臑](LI-14-Binao.md) | Meeting (LI/SI/BL) |
| LI-15 | [Jianyu 肩髃](LI-15-Jianyu.md) | Meeting with Yangqiao Mai |
| LI-16 | [Jugu 巨骨](LI-16-Jugu.md) | Meeting with Yangqiao Mai |
| LI-17 | [Tianding 天鼎](LI-17-Tianding.md) | — |
| LI-18 | [Futu 扶突](LI-18-Futu.md) | Window of Heaven |
| LI-19 | [Kouheliao 口禾髎](LI-19-Kouheliao.md) | — |
| LI-20 | [Yingxiang 迎香](LI-20-Yingxiang.md) | Meeting (LI/ST) |

## Status

Branch **growing**. Two complete channels source-verified: Lung (11/11) and Large Intestine (20/20) — 31 confirmed leaves. Other channels not yet started.
