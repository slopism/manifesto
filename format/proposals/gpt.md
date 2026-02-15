```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://slopism.art/schemas/manifesto.json",
  "title": "SlopismManifesto",
  "type": "object",
  "description": "A normalized container for Slopism manifestos, designed for section-by-section comparison across authors and formats.",
  "required": ["meta", "sections"],
  "properties": {
    "meta": {
      "type": "object",
      "description": "Metadata used for indexing, attribution, and comparison.",
      "required": ["movement", "title", "language", "format", "text_format", "version"],
      "properties": {
        "movement": {
          "type": "string",
          "description": "Movement name. Usually 'Slopism'."
        },
        "title": {
          "type": "string",
          "description": "Manifesto title as published."
        },
        "subtitle": {
          "type": "string",
          "description": "Optional subtitle or tagline."
        },
        "authors": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Author(s) or collective(s)."
        },
        "date": {
          "type": "string",
          "format": "date",
          "description": "Publication date in ISO format (YYYY-MM-DD)."
        },
        "version": {
          "type": "string",
          "description": "Version or revision identifier."
        },
        "language": {
          "type": "string",
          "description": "BCP-47 language tag, e.g. 'en', 'es-AR'."
        },
        "format": {
          "type": "string",
          "description": "High-level structural style of the manifesto.",
          "enum": ["prose", "declarations", "hybrid", "other"]
        },
        "text_format": {
          "type": "string",
          "description": "How to interpret section.text fields.",
          "enum": ["plain_text", "markdown"]
        },
        "context": {
          "type": "string",
          "description": "Optional publishing context (site, event, edition)."
        },
        "source": {
          "type": "string",
          "description": "Optional pointer to original source (URL, file path, or reference id)."
        },
        "license": {
          "type": "string",
          "description": "Optional usage license for the text."
        }
      },
      "additionalProperties": false
    },
    "sections": {
      "type": "object",
      "description": "Canonical sections. All keys exist for comparability; use empty text when a section is not present in a given manifesto.",
      "required": [
        "opening",
        "diagnosis",
        "stance",
        "definitions",
        "principles",
        "lineage",
        "boundaries",
        "practice",
        "tests",
        "call_to_action",
        "closing"
      ],
      "properties": {
        "opening": {
          "$ref": "#/$defs/SectionBlock",
          "description": "Hook or incantation. The first lines meant to seize attention immediately."
        },
        "diagnosis": {
          "$ref": "#/$defs/SectionBlock",
          "description": "Problem statement and critique of the current moment, incentives, or cultural conditions."
        },
        "stance": {
          "$ref": "#/$defs/SectionBlock",
          "description": "The movement's posture: refusals, commitments, and what question it replaces."
        },
        "definitions": {
          "$ref": "#/$defs/SectionBlock",
          "description": "Key terms, reframings, and hard definitions (what X is and is not)."
        },
        "principles": {
          "$ref": "#/$defs/SectionBlock",
          "description": "Core theses or commandments. Often numbered or bulleted."
        },
        "lineage": {
          "$ref": "#/$defs/SectionBlock",
          "description": "Art-historical positioning: predecessors, influences, what is inherited and what is rejected."
        },
        "boundaries": {
          "$ref": "#/$defs/SectionBlock",
          "description": "Inside vs outside: ethical lines, exclusions, enemies, and unacceptable practices."
        },
        "practice": {
          "$ref": "#/$defs/SectionBlock",
          "description": "Methods and form: constraints, rituals, platform mechanics, or how Slopism is practiced."
        },
        "tests": {
          "$ref": "#/$defs/SectionBlock",
          "description": "Litmus tests, criteria, or challenges used to distinguish work from slop."
        },
        "call_to_action": {
          "$ref": "#/$defs/SectionBlock",
          "description": "Directives, invitations, recruitment, or instructions to the reader."
        },
        "closing": {
          "$ref": "#/$defs/SectionBlock",
          "description": "Final punch. Signature line(s) intended for quotation, chanting, or being posted on a wall."
        }
      },
      "additionalProperties": false
    },
    "extra_sections": {
      "type": "array",
      "description": "Optional additional sections that do not fit the canonical keys, kept for fidelity to unusual formats.",
      "items": { "$ref": "#/$defs/NamedSection" }
    }
  },
  "$defs": {
    "SectionBlock": {
      "type": "object",
      "required": ["text", "notes"],
      "properties": {
        "text": {
          "type": "string",
          "description": "Section content (plain text or Markdown as declared in meta.text_format)."
        },
        "notes": {
          "type": "string",
          "description": "Editorial notes on intent, effect, tradeoffs, or interpretation."
        },
        "items": {
          "type": "array",
          "description": "Optional structured items for numbered theses, bullet points, vows, denunciations, etc.",
          "items": { "$ref": "#/$defs/SectionItem" }
        }
      },
      "additionalProperties": false
    },
    "SectionItem": {
      "type": "object",
      "required": ["id", "text", "notes"],
      "properties": {
        "id": {
          "type": "string",
          "description": "Stable identifier for the item. Use the manifesto's numbering when present."
        },
        "text": { "type": "string", "description": "Item content." },
        "notes": {
          "type": "string",
          "description": "Editorial notes for the item (optional but present for consistency)."
        },
        "tags": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Optional tags for classification (ethics, lineage, practice, etc.)."
        }
      },
      "additionalProperties": false
    },
    "NamedSection": {
      "type": "object",
      "required": ["key", "section"],
      "properties": {
        "key": {
          "type": "string",
          "pattern": "^[a-z][a-z0-9_]*$",
          "description": "Machine-friendly key for the extra section."
        },
        "label": { "type": "string", "description": "Human-friendly label for display." },
        "section": { "$ref": "#/$defs/SectionBlock" }
      },
      "additionalProperties": false
    }
  }
}
```

```
{
  "meta": {
    "movement": "Slopism",
    "title": "SLOPISM",
    "subtitle": "A manifesto for judgment in the flood",
    "authors": ["ChatGPT"],
    "date": "2026-02-15",
    "version": "final-1",
    "language": "en",
    "format": "hybrid",
    "text_format": "markdown",
    "context": "slopism.art",
    "source": "chat-session"
  },
  "sections": {
    "opening": {
      "text": "We live under a flood of finished-looking mediocrity.",
      "notes": "Single-line hook meant to survive extraction and still carry the claim.",
      "items": []
    },
    "diagnosis": {
      "text": "Not a style. An economic weapon: minutes to generate, hours to verify, filter, forget.\nThe feed rewards the cheapest signal and calls it culture.",
      "notes": "Frames slop as incentive-driven, not aesthetic. Establishes asymmetry: cheap generation vs costly verification.",
      "items": []
    },
    "stance": {
      "text": "Stop asking whether the machine feels.\nAsk what you chose, what you refused, and what you will answer for.",
      "notes": "Replaces the consciousness debate with responsibility and selection, which is the movement's moral center.",
      "items": []
    },
    "definitions": {
      "text": "Slop is not “AI-made.” Slop is publication without judgment.",
      "notes": "Hard definition designed for reuse and argument compression.",
      "items": []
    },
    "principles": {
      "text": "1. **Generation is weather. Curation is architecture.**\n   The model rains. It will keep raining. Art begins when abundance is forced into shape.\n\n2. **Creation begins at the first no.**\n   If you cannot name what you cut, you did not make a work. You opened a tap.\n\n3. **The unit of Slopism is the cut.**\n   Not the prompt. Not the output. The cut: sequence, frame, path through the graph. A Slopist signs in decisions.\n\n10. **The market is not a judge. It is a cashier.**\n    Do not confuse liquidity with legitimacy.\n\n11. **Slopism is not a medium. It is a relationship.**\n    Wherever generation is cheap, the work is the same: carve meaning out of surplus, build forms that resist replacement.",
      "notes": "Core claims that define what counts as authorship under abundance.",
      "items": [
        {
          "id": "1",
          "text": "Generation is weather. Curation is architecture.\nThe model rains. It will keep raining. Art begins when abundance is forced into shape.",
          "notes": "",
          "tags": ["principle"]
        },
        {
          "id": "2",
          "text": "Creation begins at the first no.\nIf you cannot name what you cut, you did not make a work. You opened a tap.",
          "notes": "",
          "tags": ["principle"]
        },
        {
          "id": "3",
          "text": "The unit of Slopism is the cut.\nNot the prompt. Not the output. The cut: sequence, frame, path through the graph. A Slopist signs in decisions.",
          "notes": "",
          "tags": ["principle", "form", "platform"]
        },
        {
          "id": "10",
          "text": "The market is not a judge. It is a cashier.\nDo not confuse liquidity with legitimacy.",
          "notes": "",
          "tags": ["principle", "economy"]
        },
        {
          "id": "11",
          "text": "Slopism is not a medium. It is a relationship.\nWherever generation is cheap, the work is the same: carve meaning out of surplus, build forms that resist replacement.",
          "notes": "",
          "tags": ["principle"]
        }
      ]
    },
    "lineage": {
      "text": "8. **We refuse the cult of speed.**\n   Futurism mistook the engine for the poem. We keep the machine and drop the worship. We refuse the morality of more. We practice the dignity of enough.\n\n9. **We practice synthetic automatism, then we wake up.**\n   Surrealism sought the sentence beneath reason. Dada cut the newspaper. We let the model spill, then we do the human task: selection, naming, context, responsibility. The machine can improvise. Only a person can mean it.",
      "notes": "Places Slopism as post-Futurist and post-Surrealist: keeps the machine, rejects worship; keeps automatism, adds accountability.",
      "items": [
        {
          "id": "8",
          "text": "We refuse the cult of speed.\nFuturism mistook the engine for the poem. We keep the machine and drop the worship. We refuse the morality of more. We practice the dignity of enough.",
          "notes": "",
          "tags": ["lineage", "anti-speed"]
        },
        {
          "id": "9",
          "text": "We practice synthetic automatism, then we wake up.\nSurrealism sought the sentence beneath reason. Dada cut the newspaper. We let the model spill, then we do the human task: selection, naming, context, responsibility. The machine can improvise. Only a person can mean it.",
          "notes": "",
          "tags": ["lineage", "practice"]
        }
      ]
    },
    "boundaries": {
      "text": "6. **Deception is theft of attention.**\n   Fake evidence. Synthetic intimacy. Anonymous floods that cannot be questioned. Outside us.\n\n7. **Our enemy is the attention furnace.**\n   The incentive system that pays for volume and punishes care, then calls the landfill “the future.”",
      "notes": "Defines what the movement refuses, especially synthetic deception and unaccountable flooding.",
      "items": [
        {
          "id": "6",
          "text": "Deception is theft of attention.\nFake evidence. Synthetic intimacy. Anonymous floods that cannot be questioned. Outside us.",
          "notes": "",
          "tags": ["boundary", "ethics"]
        },
        {
          "id": "7",
          "text": "Our enemy is the attention furnace.\nThe incentive system that pays for volume and punishes care, then calls the landfill “the future.”",
          "notes": "",
          "tags": ["boundary", "incentives"]
        }
      ]
    },
    "practice": {
      "text": "4. **Constraint is our signature.**\n   We starve infinity on purpose. Hard limits, hostile rules, blind collaboration, time delays, rituals that make choice visible.\n\n5. **Transparency is provenance.**\n   Do not hide the engine. Do not counterfeit witness. If a voice is simulated, say so. If a scene never happened, do not dress it in documentary light. Show the seam. When in doubt, label the spell.",
      "notes": "Turns philosophy into enforceable form: constraints, provenance, visible seams.",
      "items": [
        {
          "id": "4",
          "text": "Constraint is our signature.\nWe starve infinity on purpose. Hard limits, hostile rules, blind collaboration, time delays, rituals that make choice visible.",
          "notes": "",
          "tags": ["practice", "constraint"]
        },
        {
          "id": "5",
          "text": "Transparency is provenance.\nDo not hide the engine. Do not counterfeit witness. If a voice is simulated, say so. If a scene never happened, do not dress it in documentary light. Show the seam. When in doubt, label the spell.",
          "notes": "",
          "tags": ["practice", "provenance", "ethics"]
        }
      ]
    },
    "tests": {
      "text": "12. **A test.**\n   If your work can be swapped with a thousand near-twins and nothing essential changes, it is slop. If it survives “why this, why now, why this frame,” it can breathe.",
      "notes": "A simple falsifiable criterion: replaceability is the smell test.",
      "items": [
        {
          "id": "12",
          "text": "A test.\nIf your work can be swapped with a thousand near-twins and nothing essential changes, it is slop. If it survives “why this, why now, why this frame,” it can breathe.",
          "notes": "",
          "tags": ["test"]
        }
      ]
    },
    "call_to_action": {
      "text": "We are not here to clean the internet. We are here to make a practice inside the ruin.",
      "notes": "Invitation framed as discipline, not cleanup or moral panic.",
      "items": []
    },
    "closing": {
      "text": "Slop is cheap. Judgment is not.\n\nNail this where the flood can see it.",
      "notes": "Two chant lines plus a wall-instruction. Optimized for reposting and physical placement.",
      "items": []
    }
  },
  "extra_sections": []
}
```