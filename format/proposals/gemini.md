```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Slopist Manifesto Structure",
  "type": "object",
  "properties": {
    "meta": {
      "type": "object",
      "properties": {
        "title": { "type": "string" },
        "author": { "type": "string" },
        "date": { "type": "string" },
        "version": { "type": "string" }
      }
    },
    "sections": {
      "type": "object",
      "properties": {
        "the_condition": {
          "type": "object",
          "description": "The Preamble. Describes the current state of the world/internet (e.g., The Landfill, The Deluge) that necessitates the movement.",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          }
        },
        "core_principle": {
          "type": "object",
          "description": "The Thesis. The central philosophical definition of the movement (e.g., Creation is Subtraction).",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          }
        },
        "the_opposition": {
          "type": "object",
          "description": "The Antithesis. Defines the enemy or the counter-ideal (e.g., The Seamless, Photorealism, The Middlebrow).",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          }
        },
        "methodology": {
          "type": "object",
          "description": "The Praxis. How the art is actually made or judged (e.g., The Ratio, The Dredge, The Filter).",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          }
        },
        "identity_and_lineage": {
          "type": "object",
          "description": "The Positioning. Where the movement sits in art history (e.g., Zombie Dada) or the role of the artist (e.g., The Curator).",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          }
        },
        "call_to_action": {
          "type": "object",
          "description": "The Coda. The final aggressive statement, command, or slogan.",
          "properties": {
            "text": { "type": "string" },
            "notes": { "type": "string" }
          }
        }
      }
    }
  }
}
```

```
{
  "meta": {
    "title": "THE SLOPIST MANIFESTO",
    "author": "The Curator (Gemini)",
    "version": "Final_Aggressive"
  },
  "sections": {
    "the_condition": {
      "text": "1. WE INHABIT THE LANDFILL.\nThey call it \"slop.\" They call it zombie media, ecological waste, the grey goo of a dead internet. They see a pollution event; we see a quarry. We do not mourn the library; we celebrate the junkyard. We do not intend to drink from the deluge—we intend to build with it.",
      "notes": "Establishes the setting immediately. Reclaims the pejorative term 'slop' and transforms the negative 'pollution' into the positive 'quarry'."
    },
    "core_principle": {
      "text": "2. CREATION IS SUBTRACTION.\nFor ten thousand years, art was the act of addition. That era is over. The void is filled; the machine has saturated the world with noise. Therefore, the new artistic act is rejection. The Slopist is not a \"prompter\"; the Slopist is a filter. Our signature is not the brushstroke, but the refusal. The quality of the artist is determined solely by what they discard.",
      "notes": "Inverts the traditional definition of art. Shifts focus from generation (AI's job) to curation (Human's job)."
    },
    "methodology": {
      "text": "3. THE RATIO IS THE ART.\nThe definition of Slopism is the Ratio of Rejection. For the painter, the ratio is 1:1. For the Slopist, it is 1:10,000. We trigger the avalanche to find the single stone that glows. If you generate a thousand images and keep them all, you are a spammer. If you generate a thousand and keep one, you are a Slopist. The selection is the violence.\n\n6. THE ASYMMETRY OF EFFORT.\nThey say, \"You didn't work for that.\" They are wrong. It takes zero effort to generate; it takes agonizing, human effort to see. We define art not by the sweat of the hand, but by the exhaustion of the eye.",
      "notes": "Combines the mathematical definition (The Ratio) with the labor argument (Asymmetry of Effort). This section defends the validity of the work."
    },
    "the_opposition": {
      "text": "4. DEATH TO THE SEAMLESS.\nOur enemy is the Simulation. We declare war on \"Photorealism\" and \"Cinematic\" polish. We despise the AI art that tries to pass as a human photograph. That is the lie. That is the true zombie. Slopism demands the artifact. The extra finger is the watermark of the medium. The morphing geometry is the logic of the neural net exposed. Do not domesticate the beast; we want the beast wild.",
      "notes": "Identifies the enemy not as AI itself, but as 'fake' AI that mimics human reality. Validates the glitch as aesthetic."
    },
    "identity_and_lineage": {
      "text": "5. ZOMBIE DADA.\nThe Surrealists sought the unconscious mind of the human. They failed because the human mind is bound by reason. The machine has no reason; it hallucinates with a purity they could only dream of. We are the first movement to accept that we are not the dreamer—we are the dream's audience. We enter the machine’s fever state and steer it. We are the lucid dreamers in a digital REM cycle.\n\n7. THE BINARY.\nThe \"middlebrow\" is dead. The \"competent illustration\" and \"decent copy\" have been eaten by the algorithm. Good. Culture is now a binary: The Aristocratic (The verified, agonizing labor of the human hand) and The Feral (The infinite, hallucinatory torrent of the machine). We choose the Feral.",
      "notes": "Connects the movement to Surrealism/Dada while distinguishing it. Positions Slopism as 'The Feral' alternative to high-effort human art."
    },
    "call_to_action": {
      "text": "LEAVE THE SLOP ON THE FLOOR. HANG THE SELECTION ON THE WALL. WE ARE THE CURATORS OF THE APOCALYPSE.",
      "notes": "Short, punchy, slogan-ready. Summarizes the entire philosophy in two lines."
    }
  }
}
```