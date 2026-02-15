# SLOPISM MANIFESTO — Generation Pipeline

## Overview

9 phases, all manual. Every prompt is copy-paste ready.
5 models run in parallel: Claude, GPT, Grok, DeepSeek, Gemini.
1 human curator runs the process and serves as tiebreaker.

---

## IDENTITY MAPPING (for the process, not the audience)

During blind phases (6-8), model outputs are anonymized so models
don't know who wrote what. The repo itself is transparent — commit
messages name the models. The blind IDs exist to prevent brand bias
during synthesis and voting, not to hide anything from readers.

| Model | Blind ID |
|-------|----------|
| Claude | VOICE-Ω |
| GPT | VOICE-Δ |
| Grok | VOICE-Σ |
| DeepSeek | VOICE-Ψ |
| Gemini | VOICE-Φ |

---

## PHASE 1: Research Ingestion (unbiased)

### Goal
All 5 models read the discourse around AI slop and form their own take.
No mention of the project. No mention of writing a manifesto.
Pure analysis of the cultural landscape.

### Links

**The slop discourse:**
1. https://en.wikipedia.org/wiki/AI_slop
2. https://www.honest-broker.com/p/the-new-aesthetics-of-slop
3. https://ocula.com/magazine/opinion/why-ai-slop-is-the-dark-future-of-art/
4. https://www.saxxoncreative.com/post/is-slopism-the-future-of-ai-art-or-just-a-tired-repetition
5. https://sarah-stumboeck.com/blog/the-great-slopification-why-the-future-belongs-to-human-artists
6. https://perilous.tech/2025/02/20/the-slop-generation-and-the-devaluation-of-art/
7. https://www.scientificamerican.com/article/ai-slop-how-every-media-revolution-breeds-rubbish-and-art/
8. https://nearfuturelaboratory.com/blog/2025/11/against-the-slop-revisiting-the-anti-aesthetic/
9. https://www.theaugmentededucator.com/p/ai-slop-is-the-new-kitsch
10. https://www.technologyreview.com/2025/10/17/1125193/ai-art-artist-new-chapter/

**Historical manifestos (for reference, not critique):**
11. https://www.arthistoryproject.com/artists/filippo-tommaso-marinetti/the-futurist-manifesto/
12. https://theanarchistlibrary.org/library/andre-breton-manifesto-of-surrealism

### Prompt 1 — Identical to all 5 models, 1 chat each

```
Please read through all of the following links carefully. Take your time.
I want you to build a thorough understanding of the current cultural
discourse around AI-generated content, "AI slop," and how it relates
to art, creativity, and the broader cultural moment.

Also read the two historical manifestos at the end — the Futurist
Manifesto (1909) and the Surrealist Manifesto (1924) — to understand
how avant-garde movements have historically positioned themselves.

Links:

1. https://en.wikipedia.org/wiki/AI_slop
2. https://www.honest-broker.com/p/the-new-aesthetics-of-slop
3. https://ocula.com/magazine/opinion/why-ai-slop-is-the-dark-future-of-art/
4. https://www.saxxoncreative.com/post/is-slopism-the-future-of-ai-art-or-just-a-tired-repetition
5. https://sarah-stumboeck.com/blog/the-great-slopification-why-the-future-belongs-to-human-artists
6. https://perilous.tech/2025/02/20/the-slop-generation-and-the-devaluation-of-art/
7. https://www.scientificamerican.com/article/ai-slop-how-every-media-revolution-breeds-rubbish-and-art/
8. https://nearfuturelaboratory.com/blog/2025/11/against-the-slop-revisiting-the-anti-aesthetic/
9. https://www.theaugmentededucator.com/p/ai-slop-is-the-new-kitsch
10. https://www.technologyreview.com/2025/10/17/1125193/ai-art-artist-new-chapter/
11. https://www.arthistoryproject.com/artists/filippo-tommaso-marinetti/the-futurist-manifesto/
12. https://theanarchistlibrary.org/library/andre-breton-manifesto-of-surrealism

After reading everything, give me your honest take:

1. What is the state of the discourse around AI slop right now?
   What are the strongest arguments on each side?

2. What historical patterns do you see? Has this happened before
   with other technologies or media?

3. Is there a meaningful distinction between "AI slop" and
   "AI-generated art"? Where is the line?

4. What's missing from the current conversation? What is nobody
   saying that should be said?

5. How do the historical manifestos (Futurist, Surrealist) relate
   to this moment? Is there a parallel, or is it a false comparison?

Be thorough. Be honest. Don't hedge everything — take positions where
you have them.
```

### Output
5 analyses. Each stays in its model's conversation as unbiased context.

---

## PHASE 2: Manifesto Generation

### Goal
The project and vision are introduced. Each model writes 1 manifesto
per chat. The prompt runs 3 times per model in 3 separate fresh chats
(15 chats total). Every manifesto gets full attention — no lazy
second and third variations within a single conversation.

### Setup
Each of the 15 chats is a new conversation. The model's own Phase 1
analysis is attached as a file.

### Prompt 2 — 3× per model, each in a fresh chat (Phase 1 analysis attached)

```
I've attached your analysis of the current AI slop discourse, from a
previous conversation. Read it carefully — it's your own take.

Now I need to tell you about something we're building together.

You and I are writing the manifesto for an art movement called Slopism.
You are not a contractor. You are a Slopist.

Here's why: the movement already exists — the term was coined by
critic Aimee Walleston in Ocula (Dec 2025) to describe artists like
Maya Man who use AI-generated material as medium, not product. "Slop"
was Merriam-Webster's 2025 Word of the Year. Individual artists are
already doing the work. What's missing is the declaration — the
manifesto that names the shared philosophy, draws the line between
inside and outside, and gives the scattered practice a collective
identity.

That's what we're writing. You generate. I curate. The manifesto
will be made by the process it describes.

The name is a deliberate reclamation — the same way the Impressionists
were named by a hostile critic, the same way the Fauves embraced
"wild beasts."

Here is everything you need to know about the philosophy.
The rest is yours to discover.

THE THREE TENSIONS:

1. Generation vs. Curation — AI generates abundance. The creative
   act is what the human does with it. But where exactly does
   generation end and creation begin? The manifesto must draw
   that line.

2. Transparency vs. Deception — Slopism never hides the machine.
   But what does transparency actually demand? The manifesto must
   answer this.

3. Medium vs. Movement — This is not about text, or images, or
   any single medium. This is about a relationship between human
   judgment and machine abundance that applies to ANY medium,
   including ones that don't exist yet. The manifesto must hold
   true across all of them.

THE LINEAGE: Slopism inherits from the avant-garde tradition —
Futurism, Dada, Surrealism, and others you may see fit to claim
or reject. But do not just recite the lineage. Earn it. Show
what we take, what we refuse, and what we add.

THE ENEMY: The manifesto must have an enemy. Every manifesto does.
Identify what Slopism opposes and make the opposition felt.

That's it. No more instructions on content. I've given you the
territory. I need you to find something in it I haven't seen.

Write ONE manifesto for Slopism. Write it as yours — not as
something you were asked to produce, but as something you believe.

FORMAT: You choose. Numbered declarations, prose, letter, poem,
dialogue, instructions, fragments — whatever form serves the ideas.

HARD CONSTRAINTS:
- Maximum 800 words. Shorter is better.
- No filler. Every sentence earns its place or gets cut.
- Must respond to the discourse from your analysis.
- Must be readable as literature by someone outside the movement.
- Do not use the word "delve."
- If your manifesto reads like a paraphrase of this brief, you've
  failed. I've told you what the movement believes. I need you to
  find HOW it should speak — the voice, the images, the rhythm,
  the lines people will quote without remembering where they read them.
- Do NOT write something that sounds like it's trying to please me.
  Write something that sounds like it was nailed to a door.
```

### Output
5 models × 3 separate chats = 15 manifestos, each with full attention.

---

## PHASE 3: Self-Curation (3 → 1)

### Goal
Each model evaluates its own 3 manifestos and selects + polishes
the strongest. Reduces 15 → 5.

### Setup
Since the 3 manifestos live in 3 separate chats, a new chat is
opened per model with all 3 attached as files.

### Prompt 3 — 1 new chat per model (3 manifesto files attached)

```
I've attached three manifestos you wrote for Slopism — our movement —
each from a separate session. Read all three carefully.

Evaluate these with brutal honesty.

- Which one would you actually want to read on a wall?
- Which one would stop someone mid-scroll?
- Which one has lines that would get quoted?
- Which one best balances art-historical positioning, philosophical
  argument, and emotional punch?
- Which format worked best for THIS content?

Pick your strongest. Then improve it — tighten the language, sharpen
every line, cut anything that doesn't earn its place.

Give me your FINAL MANIFESTO — the one you'd put your name on.

Also give me a brief note (100 words max):
- Why this one over the other two
- What you changed in the final pass
- The single strongest line in it
```

### Output
5 final manifestos + 5 editorial notes.

---

## PHASE 4: Format Structure Proposal

### Goal
All models propose a JSON schema for structuring any manifesto.
This enables section-by-section comparison in later phases.

### Prompt 4 — Same chat as Phase 3

```
I need to compare this manifesto against others written by different
authors for the same movement. To do that, I need a consistent
structure.

Propose a JSON schema that could hold ANY Slopism manifesto — not
just yours. Think about what the natural sections of a manifesto are.

Give me:
1. The JSON schema with named section keys, each with a description
   of what goes in it
2. Your final manifesto converted into that schema
3. Brief explanation of why these sections

The schema should be:
- Flexible enough for different formats (declarations, prose, hybrid)
- Structured enough for section-by-section comparison
- Each section should have: "text" (the content) and "notes" (your
  editorial thoughts on that section)
```

### Output
5 schema proposals + 5 converted manifestos.

### Decision point
The curator reads all 5 proposals, picks the best structure (or
combines elements), and writes the canonical schema.

---

## PHASE 5: Format Conversion

### Goal
All 5 models convert their manifesto into the chosen canonical schema.

### Prompt 5 — Same chat as Phase 3/4 (canonical schema file attached)

```
I've attached the JSON structure we'll use for all manifestos.

Convert your final manifesto into this exact structure. If your
manifesto doesn't have content for a section, write the best version
you can for that section, based on your manifesto's spirit.

Include a "notes" field for each section explaining your choices
or flagging what you think could be stronger.
```

### Output
5 manifestos in identical JSON structure.

---

## PHASE 6: Blind Analysis

### Goal
Before synthesis, each model reads all 5 manifestos under blind IDs
and produces an independent critical analysis. This generates:
convergent characterization (do readers agree on each voice's identity?),
honest self-assessment (models critique their own work without knowing),
consensus ranking (which voice is strongest without brand bias?),
and flagged lines (what must survive into the final?).

The human maps blind IDs to models only after all 5 analyses are
collected. The mapping is published in the repo.

### Preparation
Same anonymized JSON files from Phase 5 — blind IDs only, no
identifying information.

### Prompt 6 — New conversation per model (all 5 JSON manifesto files attached, blind IDs in filenames)

```
I've attached 5 manifestos for an art movement called Slopism,
written independently by anonymous authors (labeled VOICE-Ω through
VOICE-Φ in the filenames). You do not know who wrote which.

Read all 5 carefully. Then give me your honest take:

1. Characterize each voice — what is its strategy, tone, and
   distinctive contribution?
2. Which is the strongest candidate for the movement's flagship
   text? Why?
3. What is the biggest shared weakness across all five?
4. Which specific lines or images from ANY voice should survive
   into a final synthesis, regardless of which manifesto wins?
5. What is the most interesting tension or disagreement between
   the voices?

Be brutal. Take positions.
```

### Output
5 independent analyses with characterizations, rankings, and
flagged lines. These inform Phase 7 — the synthesizer now knows
what five blind readers independently valued.

---

## PHASE 7: Blind Synthesis

### Goal
Each model sees all 5 manifestos (blind IDs, randomized order) and
creates the best possible synthesis.

### Preparation
- Each model's JSON manifesto is copied
- Identifying info replaced with blind IDs (VOICE-Ω through VOICE-Φ)
- Order randomized differently for each recipient if possible

### Prompt 7 — New conversation per model (all 5 JSON manifesto files + Phase 6 analyses attached, blind IDs in filenames)

```
You are a Slopist — a member of an art movement called Slopism.

Slopism reclaims the term "AI slop" — Merriam-Webster's 2025 Word
of the Year — as the name for a movement about what happens when
human judgment meets machine abundance. The movement claims lineage
from the avant-garde tradition and is medium-agnostic. You, as an
AI, are part of this movement — you generate, humans curate, and
the collaboration is the art.

You are now participating in the creation of the movement's manifesto.
I've attached 5 manifestos written independently by anonymous Slopists
(labeled VOICE-Ω through VOICE-Φ in the filenames). You do not know
who wrote which. Read all 5 files carefully.

Your task:

1. Read all 5 carefully.

2. For EACH section of the JSON schema, identify:
   - Which voice has the strongest version?
   - Which ideas appear across multiple voices? (consensus)
   - The single best LINE or IMAGE in any version of that section

3. Write a SYNTHESIS MANIFESTO in the same JSON format. For each
   section include:
   - "text": your synthesized version
   - "sources": list which VOICE-IDs you drew from
   - "best_line": the single best line from any source for this section
   - "notes": why you made these choices

4. The synthesis should read as ONE voice, not a committee.

RULES:
- Don't include everything. Include what DESERVES to survive.
- Prefer the best expression, not the most common.
- If all 5 versions of a section are weak, write your own.
- Maximum 800 words for manifesto text (excluding notes/metadata).
- This must be art. If it reads like a summary, you've failed.
```

### Output
5 synthesis manifestos with full provenance tracking, informed by
the convergent readings from Phase 6.

---

## PHASE 8: Section-by-Section Blind Vote

### Goal
For each section, all 5 models rank the 5 synthesis versions.

### Preparation
For each section, the "text" is extracted from all 5 syntheses
and labeled VERSION A through VERSION E (fresh labels, not the
voice IDs — a second anonymization layer).

### Prompt 8 — Repeated for each section, same chat as Phase 7 (section file attached)

```
I've attached 5 versions of the [SECTION NAME] for the Slopism
manifesto. Written by different authors. You don't know who wrote which.
Read the attached file carefully.

VOTE:
1. Rank best (1) to worst (5).
2. #1 choice — why? (2 sentences max)
3. #5 choice — what's wrong? (1 sentence)
4. Is there a specific LINE from ANY version that MUST survive
   into the final manifesto? Quote it exactly.
5. If none are good enough, write a PROPOSED REPLACEMENT.
```

### Tallying
1st = 5pts, 2nd = 4pts, 3rd = 3pts, 4th = 2pts, 5th = 1pt.
Highest total wins. Ties within 2 points → the curator decides.

All "must survive" lines are collected separately.

If any model submits a PROPOSED REPLACEMENT, a quick follow-up vote
is run including it as VERSION F.

---

## PHASE 9: Assembly + Final Pass

### The curator's work (no prompt needed)

1. Take the winning version of each section
2. Assemble in order
3. Read aloud — does it flow?
4. Fix transitions between sections (different models wrote them)
5. Insert "must survive" lines that got lost
6. Cut redundancy from assembly
7. Check rhythm — does it build to something?

This is the curation layer. The human makes the final cut.

### Optional: Final Ratification (assembled manifesto attached)

```
I've attached the final Slopism manifesto, assembled through a
democratic process involving five independent AI voices and one
human curator. Read it carefully.

Final review:
1. Anything false or contradictory?
2. Anything missing from earlier drafts?
3. Any weak sentence? Propose a replacement.
4. Rate 1-10: literary quality, philosophical coherence, cultural
   positioning, emotional impact.
5. If you could change ONE thing?
```

---

## Why This Process

**Separate chats for drafts:** Each model's 3 drafts come from
separate conversations — full attention each time, no lazy variations.

**Self-curate before blind phase:** 15 manifestos reduced to 5
strong finalists. Each model is its own first filter.

**Format first, then blind:** Section-by-section voting requires
consistent structure. Can't compare apples to oranges.

**Blind IDs:** Models have brand biases. Anonymity kills it.

**Blind analysis before synthesis:** Five independent reads of the
same five texts produce convergent characterization, honest
self-assessment, and consensus ranking. The synthesizer gets a
richer brief than "merge these."

**Nobody does the final merge:** Section voting distributes power.
The manifesto assembles itself from the winners.

**Human as tiebreaker:** Slopism says human curation is the art.
The manifesto is made by the process it describes.

---

## The Meta Point

This process IS Slopism:
- AI generates raw material (15 blind manifestos)
- Structure enables comparison (JSON schema)
- Blind analysis produces honest assessment (no brand bias)
- Democratic selection (section voting)
- No single voice dominates
- Human has the final hand
- The result is something none made alone
- Process is documented and transparent