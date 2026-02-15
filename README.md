# SLOPISM MANIFESTO

> *A critic named it. Five AIs and one human are writing the manifesto.*

## What is this?

This repository contains the full, transparent process of generating the Slopism manifesto through a democratic collaboration between five AI models and one human curator.

**Slopism** is an art movement that reclaims "AI slop" — the flood of low-quality AI-generated content drowning the internet — as raw material for human curation. The AI generates the stone. The human is the sculptor. The curation is the creation.

The term "Slopism" was first used by critic Aimee Walleston in [Ocula](https://ocula.com/magazine/opinion/why-ai-slop-is-the-dark-future-of-art/) (December 2025) to describe work by artists like [Maya Man](https://mayaontheinter.net/) already using AI-generated material as artistic medium. "Slop" itself was [Merriam-Webster's 2025 Word of the Year](https://en.wikipedia.org/wiki/AI_slop). The movement exists. Individual artists are already making the work. What's missing is the declaration — the manifesto that names the shared philosophy, draws the line between inside and outside, and gives the scattered practice a collective identity.

Apollinaire coined "surrealism" in 1917. Breton wrote the manifesto in 1924. The word comes first. The framework follows.

## The lineage

- **Futurism** (1909): Machines have aesthetic value
- **Dadaism** (1916): Destruction of meaning IS meaning
- **Surrealism** (1924): The unconscious speaks through automatic creation
- **Slopism** (2025): AI is the new unconscious. Human curation is the new authorship.

## Why is the process in a repo?

Because the process IS the art.

The Slopism manifesto was not written by a single author. It was generated through a multi-stage pipeline where five AI models (Claude, GPT, Grok, DeepSeek, Gemini) independently wrote manifestos, then blindly synthesized each other's work, then democratically voted section-by-section on the final text. The human curator served as tiebreaker and did the final editorial pass.

This is Slopism in action:
- AI generates raw material (blind manifesto drafts)
- Structure enables comparison (standardized format)
- Democratic selection (section-by-section voting)
- No single voice dominates
- Human has the final hand
- The result is something none of the participants could have made alone

Every step is committed. The git history tells the story.

## Repository structure

```
manifesto/
├── README.md                  ← you are here
├── CLAUDE.md                  ← instructions for AI-assisted commits
├── pipeline.md                ← the full generation process
├── research/                  ← Phase 1: discourse analysis
│   ├── links.md               ← source articles
│   ├── claude-analysis.md
│   ├── gpt-analysis.md
│   ├── grok-analysis.md
│   ├── deepseek-analysis.md
│   └── gemini-analysis.md
├── drafts/                    ← Phase 2-3: blind drafts → self-curation
│   ├── claude/
│   │   ├── manifesto-1.md
│   │   ├── manifesto-2.md
│   │   ├── manifesto-3.md
│   │   └── final.md
│   ├── gpt/
│   ├── grok/
│   ├── deepseek/
│   └── gemini/
├── format/                    ← Phase 4-5: schema + conversion
│   ├── proposals/             ← each model's proposed schema
│   ├── chosen-schema.json     ← the selected structure
│   └── converted/             ← all 5 manifestos in final schema
│       ├── VOICE-Ω.json
│       ├── VOICE-Δ.json
│       ├── VOICE-Σ.json
│       ├── VOICE-Ψ.json
│       └── VOICE-Φ.json
├── synthesis/                 ← Phase 6: blind synthesis
│   ├── VOICE-Ω-synthesis.json
│   ├── VOICE-Δ-synthesis.json
│   ├── VOICE-Σ-synthesis.json
│   ├── VOICE-Ψ-synthesis.json
│   └── VOICE-Φ-synthesis.json
├── voting/                    ← Phase 7: section-by-section votes
│   ├── section-01-opening/
│   │   ├── versions.md        ← the 5 versions being voted on
│   │   ├── votes.md           ← all 5 models' votes
│   │   └── result.md          ← winner + tally
│   ├── section-02-.../
│   └── ...
├── assembly/                  ← Phase 8: final assembly
│   ├── raw-assembly.md        ← winning sections concatenated
│   ├── editorial-notes.md     ← human curator's edit notes
│   └── ratification.md        ← final review by all models
└── MANIFESTO.md               ← THE FINAL MANIFESTO
```

## Reading the git history

The commits follow the generation process chronologically:

```
1. `init:` pipeline + README + CLAUDE.md + LICENSE
2. `phase-1:` research link collection
3. `phase-1:` discourse analysis (one commit per model)
4. `phase-2:` manifesto drafts (one commit per draft — 3 per model, 15 total)
5. `phase-3:` self-curated finals (1 per model)
6. `phase-4:` format schema proposals from all 5 models
7. `phase-4:` canonical schema selection (curator decision)
8. `phase-5:` conversion to canonical schema + blind IDs assigned
9. `phase-6:` blind syntheses (one commit per voice)
10. `phase-7:` section votes with tallies (one commit per section)
11. `phase-8:` raw assembly of winning sections
12. `phase-8:` curator editorial pass
13. `phase-8:` ratification reviews from all 5 models
14. `final:` MANIFESTO.md
```

You can read the full process by walking the git log:

```bash
git log --oneline --reverse
```

## The blind IDs

During synthesis and voting (phases 6-7), model outputs are anonymized behind blind IDs (VOICE-Ω, VOICE-Δ, VOICE-Σ, VOICE-Ψ, VOICE-Φ) so that models don't know who wrote what. This prevents brand bias — no model can favor or dismiss another based on name.

The repo itself is fully transparent. Commit messages name the models. The mapping is in [`pipeline.md`](pipeline.md). The blind IDs serve the process, not the audience.

## How to read this repo

**If you just want the manifesto:** Read [`MANIFESTO.md`](MANIFESTO.md).

**If you want to see how it was made:** Start at [`pipeline.md`](pipeline.md), then walk the directories in order: `research/` → `drafts/` → `format/` → `synthesis/` → `voting/` → `assembly/`.

**If you want to run this process yourself:** Fork the repo, use `pipeline.md` as your guide, and substitute your own models or prompts. The process is the reusable artifact, not just the output.

## License

The manifesto text and all process documentation are released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Use it, remix it, build on it. Attribution to Slopism.

## Links

- [slopism.art](https://slopism.art)
- [GitHub](https://github.com/slopism)
- [𝕏 @slopism_art](https://x.com/slopism_art)
- [Bluesky @slopism.bsky.social](https://bsky.app/profile/slopism.bsky.social)

---

*"The slop is the material, not the product. The difference between noise and music is the ear that listens."*