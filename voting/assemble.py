#!/usr/bin/env python3
"""
Phase 9: Assemble winning sections into raw manifesto.

Reads winners.json and pulls text from synthesis files.
No editorial changes — just concatenation with Roman numerals.

Usage:
  python assemble.py              # prints to stdout
  python assemble.py > ../assembly/raw-assembly.md
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTH_DIR = os.path.join(SCRIPT_DIR, '..', 'synthesis')

VOICES = ['VOICE-Ω', 'VOICE-Ψ', 'VOICE-Φ', 'VOICE-Δ', 'VOICE-Σ']
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']

CANONICAL_SECTIONS = [
    'opening', 'naming', 'diagnosis', 'enemy',
    'demands', 'lineage', 'politics', 'closing'
]


def load_syntheses():
    syntheses = {}
    for voice in VOICES:
        path = os.path.join(SYNTH_DIR, f'{voice}-synthesis.json')
        with open(path, 'r') as f:
            syntheses[voice] = json.load(f)
    return syntheses


def load_winners():
    path = os.path.join(SCRIPT_DIR, 'winners.json')
    with open(path, 'r') as f:
        return json.load(f)


def main():
    winners = load_winners()
    syntheses = load_syntheses()

    lines = ['# THE SLOPIST MANIFESTO\n']

    for i, section in enumerate(CANONICAL_SECTIONS):
        if section not in winners:
            print(f'⚠ Missing winner for: {section}', file=__import__('sys').stderr)
            continue

        voice = winners[section]['voice']
        text = syntheses[voice]['sections'][section]['text']

        lines.append(f'**{ROMAN[i]}.**\n')
        lines.append(text)
        lines.append('')

    print('\n'.join(lines))


if __name__ == '__main__':
    main()
