#!/usr/bin/env python3
"""Fold tone and vowel-length notation out of the Shan (``shn``) WikiPron row.

Shan writes tone with explicit, unambiguous tone-mark letters at the end of
the syllable (unlike Thai/Lao, which compute tone from consonant class and
rime shape and only place tone letters). This script checks whether the
Thai/Lao tone-PLACEMENT gap transfers to Shan by folding, cumulatively and on
BOTH sides: (1) tone identity out entirely, (2) tone placement only (move the
tone letter to a fixed position, keep order/identity), (3) vowel length.

Run from the repository root::

    PYTHONPATH=. python scripts/fold_shn_notation.py

Nothing here feeds the board; this is a measurement instrument only.
"""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "shn"
DATASET = "wikipron"

TONE = re.compile("[˥˦˧˨˩ˀ]+")


def scored_pairs():
    from orthography2ipa import G2P

    engine = G2P(LANG)
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, False, extra_strip=extra)

    out = []
    for word, gold in B.load_wikipron(LANG, 10 ** 9):
        try:
            hyp = engine.transcribe_word(word)
        except Exception:
            continue
        if hyp:
            out.append((word, norm(gold), norm(hyp)))
    return out


def per(rows, fold=lambda s: s):
    total = 0.0
    for _word, gold, hyp in rows:
        g, h = fold(gold), fold(hyp)
        total += B.levenshtein(h, g) / max(len(g), 1)
    return total / len(rows)


def fold_tone_out(s: str) -> str:
    return TONE.sub("", s)


def fold_tone_position(s: str) -> str:
    """Move every tone-letter run to the end of the string, keep identity/order."""
    marks = TONE.findall(s)
    rest = TONE.sub("", s)
    return rest + "".join(marks)


def fold_vowel_length(s: str) -> str:
    return s.replace("ː", "")


def main():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored\n")

    n_with_tone = sum(1 for _w, g, _h in rows if TONE.search(g))
    print(f"gold rows carrying a tone marker: {n_with_tone}/{len(rows)} "
          f"({n_with_tone / len(rows):.1%})")
    n_hyp_tone = sum(1 for _w, _g, h in rows if TONE.search(h))
    print(f"hypothesis rows carrying a tone marker: {n_hyp_tone}/{len(rows)} "
          f"({n_hyp_tone / len(rows):.1%})\n")

    raw = per(rows)
    print(f"as scored                          {raw:.4f}")

    tone_out = per(rows, fold_tone_out)
    print(f"+ tone folded out entirely          {tone_out:.4f}")

    tone_pos = per(rows, fold_tone_position)
    print(f"+ tone placement only (order/id kept) {tone_pos:.4f}")

    vlen = per(rows, lambda s: fold_vowel_length(fold_tone_position(s)))
    print(f"+ vowel length ⟨ː⟩ folded as well   {vlen:.4f}")

    vlen_only = per(rows, fold_vowel_length)
    print(f"(vowel length alone, no tone fold)  {vlen_only:.4f}")


if __name__ == "__main__":
    main()
