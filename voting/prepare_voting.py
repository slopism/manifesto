#!/usr/bin/env python3
"""
Prepare voting files for Phase 8: section-by-section blind vote.

Usage:
  python prepare_voting.py                      # Generate mapping.json only
  python prepare_voting.py opening              # First section (no context)
  python prepare_voting.py naming               # Subsequent (reads winners.json)

Each section gets its own folder:
  voting/01-opening/
    ballot.md           <- copy-paste into fresh chat per model
    claude.json         <- paste vote here
    gpt.json
    grok.json
    deepseek.json
    gemini.json

winners.json stores coordinates, not content:
{
  "opening": {
    "version": "B",
    "voice": "VOICE-Ψ",
    "points": 25,
    "must_survive_line": "..."
  }
}

The script resolves winning text from synthesis files via the voice ID.
"""

import json
import random
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTH_DIR = os.path.join(SCRIPT_DIR, '..', 'synthesis')
OUT_DIR = SCRIPT_DIR

VOICES = ['VOICE-Ω', 'VOICE-Ψ', 'VOICE-Φ', 'VOICE-Δ', 'VOICE-Σ']
MODELS = ['claude', 'gpt', 'grok', 'deepseek', 'gemini']
LABELS = ['A', 'B', 'C', 'D', 'E']

CANONICAL_SECTIONS = [
    'opening', 'naming', 'diagnosis', 'enemy',
    'demands', 'lineage', 'politics', 'closing'
]

# Number prefix for folder ordering
SECTION_NUM = {s: f'{i+1:02d}' for i, s in enumerate(CANONICAL_SECTIONS)}

# Seed for reproducibility (same mappings every run)
random.seed(42)


def load_syntheses():
    syntheses = {}
    for voice in VOICES:
        path = os.path.join(SYNTH_DIR, f'{voice}-synthesis.json')
        with open(path, 'r') as f:
            syntheses[voice] = json.load(f)
    return syntheses


def generate_all_mappings():
    """Pre-generate all randomized A-E mappings (deterministic via seed)."""
    master = {}
    for section in CANONICAL_SECTIONS:
        shuffled = VOICES.copy()
        random.shuffle(shuffled)
        master[section] = {LABELS[i]: shuffled[i] for i in range(5)}
    return master


def load_winners():
    """Load winners.json if it exists."""
    path = os.path.join(OUT_DIR, 'winners.json')
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}


def resolve_winning_text(section, winners, syntheses):
    """Look up winning text from synthesis files via coordinates in winners.json."""
    entry = winners[section]
    voice = entry['voice']
    return syntheses[voice]['sections'][section]['text']


def build_ballot(section, mapping, syntheses, winners):
    """Build a self-contained ballot .md file for one section."""
    lines = []
    is_first = section == CANONICAL_SECTIONS[0]

    if is_first:
        # First section: introduce the context
        lines.append('You are voting on sections for the Slopism manifesto — an art')
        lines.append('movement about human judgment meeting machine abundance.\n')
    else:
        # Subsequent sections: show accumulated manifesto
        lines.append('You are voting on sections for the Slopism manifesto.')
        lines.append('Here is the manifesto so far:\n')
        lines.append('---\n')
        roman = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
        prev_texts = []
        for i, prev_section in enumerate(CANONICAL_SECTIONS):
            if prev_section == section:
                break
            if prev_section in winners:
                numeral = roman[i]
                text = resolve_winning_text(prev_section, winners, syntheses)
                prev_texts.append(f'**{numeral}.**\n\n{text}')
        lines.append('\n\n'.join(prev_texts))
        lines.append('\n\n---\n')

    # Section versions
    lines.append(f'5 versions of the **{section.upper()}** section. You don\'t know who wrote which.\n')

    for label in LABELS:
        voice = mapping[label]
        text = syntheses[voice]['sections'].get(section, {}).get('text', '[SECTION NOT PRESENT]')
        lines.append(f'## VERSION {label}\n')
        lines.append(text)
        lines.append('\n')

    # Continuity instruction (after opening)
    if not is_first:
        lines.append('Which one best **continues** this manifesto? Consider voice,')
        lines.append('rhythm, and flow — not just standalone quality.\n')

    # JSON format spec
    lines.append('Reply in this exact JSON format:\n')
    lines.append('```json')
    lines.append('{')
    lines.append(f'  "section": "{section}",')
    lines.append('  "ranking": ["X", "X", "X", "X", "X"],')
    lines.append('  "best": { "version": "X", "why": "..." },')
    lines.append('  "worst": { "version": "X", "why": "..." },')
    lines.append('  "must_survive_line": "...",')
    lines.append('  "proposed_replacement": null')
    lines.append('}')
    lines.append('```\n')
    lines.append('`ranking` is best-to-worst (first entry = your #1 pick).')
    lines.append('`proposed_replacement` is null unless you think none are good enough.')

    return '\n'.join(lines)


def main():
    syntheses = load_syntheses()
    master_mapping = generate_all_mappings()

    # Always write mapping
    mapping_path = os.path.join(OUT_DIR, 'mapping.json')
    with open(mapping_path, 'w') as f:
        json.dump(master_mapping, f, indent=2, ensure_ascii=False)
    print(f'  ✓ mapping.json')

    if len(sys.argv) < 2:
        print('\nUsage: python prepare_voting.py <section>')
        print(f'Sections: {", ".join(CANONICAL_SECTIONS)}')
        return

    section = sys.argv[1]
    if section not in CANONICAL_SECTIONS:
        print(f'Unknown section: {section}')
        print(f'Valid: {", ".join(CANONICAL_SECTIONS)}')
        sys.exit(1)

    winners = load_winners()

    # Check prerequisites (all prior sections should have winners)
    idx = CANONICAL_SECTIONS.index(section)
    missing = [s for s in CANONICAL_SECTIONS[:idx] if s not in winners]
    if missing:
        print(f'  ⚠ Missing winners for: {", ".join(missing)}')
        print(f'    Update winners.json before generating this ballot.')
        sys.exit(1)

    # Create section folder
    folder_name = f'{SECTION_NUM[section]}-{section}'
    folder_path = os.path.join(OUT_DIR, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Write ballot
    content = build_ballot(section, master_mapping[section], syntheses, winners)
    ballot_path = os.path.join(folder_path, 'ballot.md')
    with open(ballot_path, 'w') as f:
        f.write(content)

    # Create empty vote files for each model
    for model in MODELS:
        vote_path = os.path.join(folder_path, f'{model}.json')
        if not os.path.exists(vote_path):
            with open(vote_path, 'w') as f:
                f.write('')

    print(f'  ✓ {folder_name}/')
    print(f'    ballot.md')
    for model in MODELS:
        print(f'    {model}.json  (paste vote here)')

    if idx > 0:
        print(f'    ({idx} winning section(s) included as context)')


if __name__ == '__main__':
    main()
