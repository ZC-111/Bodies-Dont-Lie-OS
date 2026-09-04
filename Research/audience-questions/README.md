# Audience Questions — Content Intake

Hybrid inbox for **answerable** audience questions → blog/vlog briefs.

**Pilot theme:** SIBO / gut  
**v1 intake:** Google People Also Ask (PAA) + curated YouTube comment paraphrases  
**Deferred:** Reddit API; YouTube Data API automation; live publish

## Safety rules

- Store **paraphrases only** — never usernames, handles, or verbatim personal medical stories.
- Educational framing only — not personal medical advice.
- Inherit claim tags + disclaimer from lecture content kits / pathways.
- Do **not** invent protocols when assets are thin — mark `gap`.

## Pipeline

```text
PAA seeds + curated YT comment themes
  → inbox/*.json   (schema/question.json)
  → clusters/<theme>-v0.1.md
  → Research/themes/<theme>/briefs/...
```

## Folders

| Path | Role |
|---|---|
| `schema/question.json` | JSON Schema for inbox items |
| `inbox/` | Anonymized curated questions |
| `clusters/` | Grouped answerable questions + asset coverage |

## Source types (v1)

| `source_type` | What to put in `source_ref` |
|---|---|
| `paa` | Seed search query (e.g. `SIBO breath test`) |
| `youtube_comment` | Video URL only (no username) |
| `reddit` | Deferred — reserved for later |
| `manual` / `inbox` / `quora` | Reserved |

## Matching doctrine (integrative)

When both layers apply:

- **Clearfield / biomed** — measure / treat  
- **TCM / acupuncture** — pattern / how hard to push  

Prefer questions coverable by existing pathway + content kit + AP pack. Coverage tags: `pathway` | `kit` | `ap` | `infographic` | `gap`.

## Next steps (out of v1 scope)

1. YouTube Data API `commentThreads` for a fixed playlist of educational SIBO videos (quota-aware; still paraphrase).
2. Reddit API for subreddit clusters (`r/SIBO`, etc.) — volume layer after briefs prove useful.
3. Wire publish destinations (Substack / YT) only after briefs ship.

## Pilot pointers

- Theme hub: [`../themes/sibo/README.md`](../themes/sibo/README.md)
- Cluster: [`clusters/sibo-v0.1.md`](clusters/sibo-v0.1.md)
- Brief templates: [`../lectures/templates/blog-brief.md`](../lectures/templates/blog-brief.md), [`../lectures/templates/vlog-brief.md`](../lectures/templates/vlog-brief.md)
