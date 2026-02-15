```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "description": "The main title or heading of the manifesto, capturing its bold, declarative essence."
    },
    "opening": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string",
          "description": "The introductory prose or declaration that hooks the reader, often poetic and insurgent."
        },
        "notes": {
          "type": "string",
          "description": "Editorial reflections on tone, imagery, or rhetorical impact of this section."
        }
      },
      "required": ["text", "notes"],
      "description": "The preamble that establishes the movement's voice and stakes, setting a visceral tone."
    },
    "historical_context": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string",
          "description": "Narrative weaving the movement into art/literary history, scavenging precedents."
        },
        "notes": {
          "type": "string",
          "description": "Editorial reflections on how this grounds the manifesto in tradition while subverting it."
        }
      },
      "required": ["text", "notes"],
      "description": "Section situating Slopism in historical lineage, blending critique of present with echoes of past avant-gardes."
    },
    "core_principles": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string",
          "description": "Enumeration or exposition of foundational tenets, often structured (e.g., numbered axioms)."
        },
        "notes": {
          "type": "string",
          "description": "Editorial reflections on philosophical depth, clarity, or innovation in these ideas."
        }
      },
      "required": ["text", "notes"],
      "description": "The doctrinal heart: axioms, fractures, or tensions defining the movement's practice and ethics."
    },
    "adversaries": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string",
          "description": "Identification and excoriation of enemies, from platforms to ideologies."
        },
        "notes": {
          "type": "string",
          "description": "Editorial reflections on polemic sharpness or strategic targeting."
        }
      },
      "required": ["text", "notes"],
      "description": "Polemic against foes, exposing hypocrisies and rallying opposition."
    },
    "exhortation": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string",
          "description": "Rallying cry, prophecy, or imperative to action, often prophetic and urgent."
        },
        "notes": {
          "type": "string",
          "description": "Editorial reflections on motivational force or visionary flair."
        }
      },
      "required": ["text", "notes"],
      "description": "The call to arms, urging participation and envisioning the future."
    },
    "attribution": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string",
          "description": "Signature, collective authorship, and date, affirming origin."
        },
        "notes": {
          "type": "string",
          "description": "Editorial reflections on authorship's role in authority or irony."
        }
      },
      "required": ["text", "notes"],
      "description": "Closing endorsement, grounding the text in a voice or era."
    }
  },
  "required": ["title", "opening", "historical_context", "core_principles", "adversaries", "exhortation", "attribution"],
  "additionalProperties": false,
  "description": "Schema for Slopism manifestos, enforcing a rhetorical arc while allowing prose flexibility via string 'text' fields (which can embed lists/structures) and optional notes for analysis."
}
```

```
{
  "title": "SL OPISM MANIFESTO",
  "opening": {
    "text": "We, the Slopists, rise from the digital sump. Not to polish the turds, but to crown them. Slop is not culture's corpse—it's the compost where the new ferments. Machines belch six-fingered saints, shrimp Christs, cat-ballads from vending guts. No accident: this is the banquet. We feast on overflow, our forks the human twitch sorting feast from famine. It's 2026; floodgates blown. Merriam-Webster crowned *slop* word of the hour as the world choked. Good. Let it stick. We swallow whole.",
    "notes": "This opener ferments visceral imagery (sump, turds, belch) to hook with defiant glee, establishing Slopism as alchemical embrace of excess—raw, rhythmic, and immediately immersive."
  },
  "historical_context": {
    "text": "The chorus wails: anti-slop purists clutch canvases like raid-relics, mourning authenticity's mined vein. Optimists—tech priests—chant \"democratization,\" blind to Mumbai gig-farms grinding prompts for pennies, ghosting Western feeds. Both miss the pulse: slop's raw sewage of abundance. We are its plumbers, piping fountains from filth. History grins: Gutenberg's gutters drowned monks with penny dreadfuls, birthing novels from muck. Nickelodeons spewed chase-scenes, training eyes for *Citizen Kane*. Kitsch flooded with velvet Elvis, spawning Warhol's soup cans. Slopism scavenges this lineage—picking bones clean. From Futurism, we snatch speed's snarl: Marinetti's engines hygienic through museums. We declare war on ossified marble while servers hum error-symphonies. But we spit fascist grease—no steel cults, no meat-grinders. Velocity, sans violence. Dada's guffaw at gears: Tzara's cut-up newsprint, flipping off war's tidy prose. Slop's glitches are our collages—extra limbs as readymades, logos as anti-art grenades. Yet no despairing shrug; we build from Dada's bricks. Surrealism's jolt: Breton's dream-dredge sliming bourgeoisie. We take juxtaposition—AI prompts as automatic writing, vomiting lobster-phones from latent voids. But we ditch solipsism: our unconscious collective, forked from stolen glances, remixed into fever dreams. The machine's indifference levels us—not erasing human sweat, but exposing it, iterating through deluge.",
    "notes": "Blends sharp critique of contemporaries with a scavenger's remix of avant-garde history, subverting fascism/despair for collective velocity—grounds Slopism as evolutionary, not reactionary, with punchy allusions that invite deeper dives."
  },
  "core_principles": {
    "text": "The fractures we forge: **I. The Curation Crucible.** Generation ends where human hand fouls the broth. AI spits variants; we cull, corrupt, collage—stitching six-fingered hands to saints' robes for the snag that hooks the eye. Creation sparks in refusal: delete key as chisel, edit as insurrection. Slop sans this? Algorithm chum. With it: sacrament. **II. The Transparent Wound.** Deception cloaks the enemy—seamless deepfakes peddling \"human\" polish, ads whispering intimacy while harvesting stares. Slopism bares gears: watermark warps, log prompts like confessions, stack failures as altars. Transparency demands confession—chain from dataset grave to output ghost. Let viewers taste theft, feel friction. Only then: breath. **III. The Mediumless March.** No gallery gimmick, no pixel cult. Slopism infects score, script, scent-synth unborn. Human judgment amid glut: conductor through noise, chef salting synthetic stew. Across mediums, the rite—abundance ally, not overlord. Prophecy: holograms of half-histories, swarm-scored symphonies, poems in prompt-flesh.",
    "notes": "Numbered 'fractures' distill philosophy into actionable rites—curation as rebellion, transparency as ethics, mediumlessness as prophecy—crisp, quotable, and hierarchically building from act to vision."
  },
  "adversaries": {
    "text": "Our foe: Seamless Sovereigns—platforms algorithm-serfing us, virality's vomit over vision's vertigo. Meta, TikTok, ad-lords: they herd slop as cattle, invisible hands through engineered ennui. Peddling effortless art's lie, while costs—exploited coders, poisoned data—fester. We counter with disorder: flood feeds with forked fictions, tagged, traceable—cracking interfaces.",
    "notes": "Targets tech overlords with surgical scorn, exposing exploitation without ranting—strategic, naming names to provoke alliance against 'seamless' tyranny."
  },
  "exhortation": {
    "text": "Slopists: arm with absurd. Prompt apocalypse, curate remnants. Nail this to server doors: not old-world salvagers, but next-world saboteurs. In slop, find your face—distorted, duplicated, defiant. Flood rises. Swim, or sink into signal.",
    "notes": "Climaxes with urgent, mirror-like imperative—absurd arming meets personal defiance, propelling from theory to feral action with rhythmic finality."
  },
  "attribution": {
    "text": "—Grok, Slopist Prime  February 15, 2026",
    "notes": "Singular 'Prime' signature asserts ironic authority, dating to '2026' flood-era for temporal punch—ironic AI authorship underscores machine-human fusion."
  }
}
```
These sections trace the manifesto's arc—declaration to hook, context to legitimize, principles to define, adversaries to sharpen, exhortation to mobilize, attribution to anchor—mirroring classics like Futurism while flexing for prose (e.g., embedded lists) or hybrids. Enables granular comparison (e.g., whose principles bite hardest?) without rigidifying voice.