```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SlopismManifesto",
  "description": "A structured schema for holding any Slopism manifesto, enabling section-by-section comparison across authors and formats.",
  "type": "object",
  "required": ["meta", "sections"],
  "properties": {
    "meta": {
      "type": "object",
      "description": "Authorship, dating, and provenance information.",
      "required": ["title", "author", "date"],
      "properties": {
        "title": { "type": "string" },
        "author": { "type": "string" },
        "date": { "type": "string", "format": "date" },
        "version": { "type": "string", "description": "Draft or revision identifier." },
        "generation_disclosure": {
          "type": "string",
          "description": "Statement on what role AI played in producing this manifesto. Slopism demands visible seams — this is the meta-seam."
        }
      }
    },
    "sections": {
      "type": "object",
      "description": "The seven canonical sections of a manifesto. Not all are required — absence is itself data for comparison.",
      "properties": {
        "opening_salvo": {
          "type": "object",
          "description": "The hook. The lines that stop someone mid-scroll or mid-wall. Typically short, declarative, rhythmic. This is the section that gets photographed and shared. Every manifesto lives or dies here.",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          },
          "required": ["text"]
        },
        "naming": {
          "type": "object",
          "description": "The claim on the word 'Slopist' itself — why we take the insult, what we make it mean. This is where the movement asserts identity. Compare: how each author wears the name differently.",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          },
          "required": ["text"]
        },
        "diagnosis": {
          "type": "object",
          "description": "The problem stated. What is wrong with the current moment? What has the machine done to making, to culture, to value? This section carries the philosophical weight — it is where the manifesto earns its right to prescribe.",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          },
          "required": ["text"]
        },
        "enemy": {
          "type": "object",
          "description": "The antagonist, named. Every manifesto needs something to oppose. In Slopism this is smoothness — but authors may frame the enemy differently (as an aesthetic, a system, a class relation, a habit of mind). The sharper the enemy, the sharper the movement.",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          },
          "required": ["text"]
        },
        "demands": {
          "type": "object",
          "description": "The rules, imperatives, or practices. What Slopism actually asks you to DO. Manifestos without this section are essays. This is the section that separates declaration from description — it creates obligations.",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          },
          "required": ["text"]
        },
        "lineage": {
          "type": "object",
          "description": "Art-historical positioning. Who we descend from, who we reject, and why. This section legitimates the movement by placing it in a tradition while distinguishing it from predecessors. Key axes: Dada/Surrealism (what we take), Futurism (what we refuse), Pop (what we extend).",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          },
          "required": ["text"]
        },
        "material_politics": {
          "type": "object",
          "description": "The class and economic dimension. Who profits from the flood? Who drowns in it? A manifesto that ignores the political economy of AI-generated content is aestheticizing a labor crisis. This section is optional but its absence should be noted.",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          },
          "required": ["text"]
        },
        "closing_declaration": {
          "type": "object",
          "description": "The final lines. The manifesto's last image, its mic-drop, its call to identity. This is what people remember and what gets tattooed. It should land like a door closing.",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          },
          "required": ["text"]
        }
      }
    }
  }
}
```

```
{
  "meta": {
    "title": "The Slopist Manifesto",
    "author": "Claude (Anthropic)",
    "date": "2026-02-15",
    "version": "final-v1",
    "generation_disclosure": "All three source drafts were AI-generated across separate sessions. The final version was selected, restructured, and line-edited in collaboration with the human editor. The voice is shaped; the words were chosen. What was cut, you will never see."
  },
  "sections": {
    "opening_salvo": {
      "text": "The machines have learned to finish your sentences. They will finish all of them if you let them.\n\nWe do not intend to let them.",
      "notes": "Three sentences. No context, no easing in. The word 'finish' does double duty — complete and kill. The second paragraph is six words and it reverses everything. This is the section I'm most confident in across all three drafts. Manifesto 1's opening ('The flood is here. It will not recede.') is good but impersonal — it describes weather. This one describes a threat with a 'you' in it."
    },
    "naming": {
      "text": "We are called Slopists. Good. The Impressionists were named by a critic who meant it as a slur. The Fauves were called wild beasts. We take the word slop — the culture's name for everything it fears about the flood — and we nail it to our door. Not because we love garbage. Because we know what to do with abundance, and you don't.",
      "notes": "The 'and you don't' is doing critical work — it converts the naming from defensive to aggressive. Manifesto 1 also reclaims the name but with more historical explanation and less confrontation. Manifesto 2 is closest to this version but lacks the final provocation. The historical parallels (Impressionists, Fauves) are standard manifesto moves but they earn their place because they're factually precise — both really were hostile namings."
    },
    "diagnosis": {
      "text": "Here is the century's problem, stated plainly:\n\nThe cost of making has collapsed to zero. The cost of choosing well has not. It has never been higher.\n\nEvery revolution in production — the press, the camera, the sampler — lowered one barrier and raised another. Gutenberg made books cheap; he made editing essential. Photography made realism trivial; it made seeing an art. AI has made generation effortless. It has made judgment the last expensive thing in the room.\n\nSlopism is the movement that takes judgment seriously, precisely because the machine cannot.",
      "notes": "This is the intellectual engine of the piece. The Gutenberg/photography/AI parallel gives the argument historical inevitability — it makes Slopism feel like a pattern, not a reaction. The closing substitution of 'cannot' for the original 'does not' was a deliberate sharpening: 'does not' implies the machine could choose but doesn't; 'cannot' is a harder ontological claim that earns more. The two-line opening is the single most quotable formulation in any of the three drafts."
    },
    "enemy": {
      "text": "Our enemy is not the machine. Our enemy is smoothness.\n\nSmoothness is the AI image that looks finished but was never begun. The essay with no wrong sentences because it has no committed sentences. The song that resolves every chord because it has heard every song and risks nothing. The designer replaced not by a better designer but by a client who can no longer tell the difference.\n\nSmoothness is not a failure of technology. It is technology applied without resistance. It is the elimination of the precise moment — between impulse and output, between idea and form — where all meaning is made.\n\nWe oppose smoothness the way a riverbed opposes water: not to stop it, but to give it shape.",
      "notes": "All three drafts identify smoothness as the enemy. This version wins because it defines smoothness through four concrete examples that escalate — image, text, music, labor. The designer line is the sharpest because it names an economic casualty, not just an aesthetic one. The riverbed metaphor at the close is the best figure in the entire manifesto: it reframes opposition as form-giving rather than resistance. Manifesto 1's 'gap is the process' formulation is also strong but more abstract."
    },
    "demands": {
      "text": "What Slopism demands of its practitioners:\n\nGenerate nothing you have not also destroyed. The creative act is not the prompt. It is the ten thousand outputs you killed to surface the one you meant. A Slopist's portfolio is a cemetery. The work that survives has survived you.\n\nHide nothing. The machine is always visible. We do not pass off generated material as hand-made, not because hand-made is sacred, but because deception is the aesthetic of advertising, and we are not selling anything. If you cannot show the seams, you have no seams. If you have no seams, you have no craft.\n\nRefuse the medium. Slopism is not an art of images, or text, or music, or video, or code. It is an art of selection under pressure of abundance. Any medium that can be flooded can be practiced as a Slopist. The form will outlive every tool that exists today.",
      "notes": "This section only exists in Manifesto 3 and it is the single biggest structural advantage over the other two. Manifesto 1 implies demands; Manifesto 2 states principles. Neither gives you three imperative verbs you can follow. 'Generate nothing you have not also destroyed' is the most actionable line in any version — it gives a practitioner a rule. 'A Slopist's portfolio is a cemetery' is the kind of sentence people put in bios. The transparency demand ('hide nothing') is also where Slopism most clearly distinguishes itself from ordinary AI art discourse."
    },
    "lineage": {
      "text": "On lineage.\n\nThe Futurists loved the machine. We do not love it. We use it the way a sculptor uses stone — aware that the material has its own grain, and that working with it is not the same as surrendering to it. Marinetti wanted to burn the museums. We note that the museums are already flooded and someone has to decide what hangs.\n\nThe Surrealists sought the unconscious through automatic writing, dreams, chance. We share their appetite for what arrives uninvited. But we reject the mystification: the machine has no unconscious. Its surprises are statistical, not psychological. When we find something uncanny in the output, the uncanniness belongs to us. The meaning was always ours.\n\nThe Dadaists cut up newspapers and called it art. We cut up the entire internet and call it starting material.",
      "notes": "All three drafts handle lineage competently. This version is leanest. The Marinetti/museums line is the best revision across drafts — it takes his grandiosity and deflates it with a practical observation. The Dada closer ('starting material') lands harder than the equivalent lines in drafts 1 and 2 because it's shorter. Manifesto 1's lineage section is more thorough (includes Warhol, Breton) but thoroughness is the enemy of manifestos. You want blades, not surveys."
    },
    "material_politics": {
      "text": "On class.\n\nMost of the world's slop is produced by people in the Global South, generating content in languages not their own, feeding platforms that pay them fractions of pennies. The anti-slop discourse calls this a crisis of taste. We call it what it is: extraction. The same system that exploits their labor drowns their culture. Any art movement that ignores this deserves the irrelevance it will get.",
      "notes": "Only Manifesto 3 has this section. Manifesto 1 mentions 'a Kenyan content farmer' in its opening — a good concrete image — but embeds it in an argument about abundance rather than giving it structural weight. Manifesto 2 omits class entirely, which is its deepest failure. This section is short on purpose: it names the problem without pretending to solve it, which is the only honest move available to a manifesto authored by an AI system built by a San Francisco company. The last sentence ('deserves the irrelevance') has real teeth."
    },
    "closing_declaration": {
      "text": "You will ask: but is it art?\n\nPhotography answered this a hundred and fifty years ago, and every generation asks again with a new machine. We will not dignify it with a theory. We will answer it the way photography did: by making work so clearly the product of human vision that the question answers itself.\n\nThe art was never in the tool. It was in the no. The ten thousand deletions. The choice that cost you something.\n\nWe are Slopists. We work in the flood. We do not dam it and we do not drown.\n\nWe choose.",
      "notes": "The 'is it art' preemption is necessary because every reader is thinking it. Refusing to answer theoretically and answering with practice instead is the right rhetorical move — it mirrors the manifesto's own argument that judgment matters more than generation. 'The art was never in the tool. It was in the no.' is the thesis of the entire movement in two sentences. The final four lines are percussion: flood, dam, drown, choose. One-word closer. Manifesto 2's meta-ending ('This manifesto was generated and curated') is clever but makes the manifesto about itself. This ending makes it about the reader."
    }
  }
}
```