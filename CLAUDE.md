# CLAUDE.md — AI-Assisted Commit Guide

This file instructs Claude (via Claude Code or similar) on how to help
manage the git history of this repository. The git history is part of
the artwork — each commit tells a chapter of the story.

## Context

This repo documents the democratic generation of the Slopism manifesto
across 5 AI models. The human curator runs the process manually and
uses Claude Code to commit each step with meaningful messages. The
commit history should be readable as a narrative.

## Commit conventions

### Format

```
phase-N: <descriptive message>

<optional body explaining what happened and why>
```

### Phase prefixes

| Prefix | Phase |
|--------|-------|
| `init` | Initial repo setup |
| `phase-1` | Research ingestion |
| `phase-2` | Blind manifesto drafts |
| `phase-3` | Self-curation (3→1) |
| `phase-4` | Format schema proposals |
| `phase-5` | Format conversion |
| `phase-6` | Blind synthesis |
| `phase-7` | Section-by-section voting |
| `phase-8` | Assembly + editorial |
| `final` | Manifesto complete |

### Example commits (in chronological order)

```
init: add pipeline, README, and CLAUDE.md

The manifesto generation process begins. This commit contains
the full pipeline specification, the public README explaining
the process, and this file — instructions for AI-assisted commits.

The process itself is Slopism in action: AI generates raw material,
humans curate, and the result is transparent.
```

```
phase-1: add research link collection

10 articles on the AI slop discourse + 2 historical manifestos
(Futurist 1909, Surrealist 1924). These will be sent to all 5
models for unbiased analysis before any mention of the project.
```

```
phase-1: add Claude's discourse analysis

Claude reads all 12 sources and provides unbiased analysis of
the AI slop discourse. No knowledge of the Slopism project yet.
```

```
phase-1: add GPT's discourse analysis
phase-1: add Grok's discourse analysis
phase-1: add DeepSeek's discourse analysis
phase-1: add Gemini's discourse analysis
```

```
phase-2: add Claude's manifesto draft 1 of 3

Fresh chat. Claude receives its Phase 1 analysis as context and
the generation prompt: three tensions, an enemy, no handed
metaphors or checklists. Each of the 3 drafts is written in a
separate conversation to avoid lazy variations.
```

```
phase-2: add Claude's manifesto draft 2 of 3
phase-2: add Claude's manifesto draft 3 of 3
phase-2: add GPT's manifesto draft 1 of 3
...
```

```
phase-3: add self-curated finals (5 models × 1 manifesto each)

Each model evaluated their own 3 drafts and selected + polished
their strongest. 15 manifestos reduced to 5 finalists.
```

```
phase-4: add format schema proposals from all 5 models

Each model proposes a JSON structure for decomposing any manifesto
into comparable sections. The curator will choose the best schema.
```

```
phase-4: select canonical JSON schema

The curator reviewed all 5 proposals and chose [brief rationale].
This structure will be used for all subsequent comparison.
```

```
phase-5: convert all 5 manifestos to canonical schema

Blind IDs assigned: VOICE-Ω through VOICE-Φ. From this point
forward, no model knows which voice belongs to which model.
The repo itself stays transparent — blind IDs are for the
models, not the readers.
```

```
phase-6: add blind synthesis from VOICE-Ω

VOICE-Ω reads all 5 anonymous manifestos and creates a synthesis —
the strongest possible manifesto from all voices combined.
Provenance tracked per section.
```

```
phase-6: add blind synthesis from VOICE-Δ
phase-6: add blind synthesis from VOICE-Σ
phase-6: add blind synthesis from VOICE-Ψ
phase-6: add blind synthesis from VOICE-Φ
```

```
phase-7: vote on section "opening" — VOICE-Σ wins (21 pts)

5 models ranked 5 versions blind. Tally:
VOICE-Σ: 21, VOICE-Ω: 18, VOICE-Δ: 15, VOICE-Φ: 12, VOICE-Ψ: 9
Must-survive line: "[quoted line]"
```

```
phase-7: vote on section "historical positioning" — VOICE-Ω wins (19 pts)
phase-7: vote on section "core declarations" — tie, curator breaks for VOICE-Δ
...
```

```
phase-8: assemble winning sections into raw draft

Winning sections concatenated in order. No editorial changes yet.
This is the democratic output before human curation.
```

```
phase-8: curator editorial pass

Transitions smoothed, must-survive lines inserted, redundancy cut,
rhythm adjusted. This is the curation layer — the human making the
final cut through the machine-generated material.

Changes documented in assembly/editorial-notes.md.
```

```
phase-8: add ratification reviews from all 5 models

All models review the assembled manifesto. Scores and feedback
recorded. Minor fixes incorporated.
```

```
final: add MANIFESTO.md

The Slopism manifesto is complete. Generated through democratic
collaboration between 5 AI models and 1 human curator. No single
voice dominates. The process is documented and transparent.
```

## Rules for Claude Code

1. **One commit per meaningful step.** Don't batch unrelated work.
   Each commit should be a chapter, not a dump.

2. **Commit messages tell the story.** Someone reading `git log`
   should understand the full process without opening any files.

3. **Include tallies in vote commits.** The commit message for each
   section vote should show the point totals. This makes the git
   log itself a record of the democratic process.

4. **Commit the pipeline first.** The very first commit should contain
   `pipeline.md`, `README.md`, and `CLAUDE.md`. This establishes the
   rules before the game begins.

5. **Don't amend phase commits.** Once a phase is committed, it stays.
   If something needs fixing, commit the fix as a new commit with
   explanation. The history should show the real process, not a
   cleaned-up version.

6. **Use conventional branch strategy.** Work on `main`. No feature
   branches needed — this is a linear process, not parallel development.

## File naming conventions

- Model outputs in `drafts/`: use model name (public, pre-anonymization)
- Converted files in `format/converted/`: use blind IDs (VOICE-Ω etc.)
- Synthesis files: use blind IDs
- Voting files: use VERSION A-E labels (fresh anonymization layer)
- Final manifesto: `MANIFESTO.md` at repo root

## Directory creation

Create directories as needed when committing each phase. Don't
pre-create empty directories. The structure grows with the process.

## This file is part of the art

Yes, you're reading instructions written for an AI, committed to a
public repo, as part of a manifesto generation process for an art
movement about AI-human collaboration. The transparency is the point.
The process is visible. The tools are visible. Nothing is hidden.

That's Slopism.