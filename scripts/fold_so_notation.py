#!/usr/bin/env python3
"""Measure the Somali (``so``/``kaikki``) tone-only ceiling.

The ``so``/``kaikki`` row scores PER 0.5567 over 230 words. The gold is a
narrow phonetic transcription that marks pitch accent with combining tone
diacritics (acute/grave/macron/circumflex) the 1972 Latin orthography never
writes (Mohamed 2015, *An Overview of the Interface between Aspects of
Somali Phonology and Morphology*: "Tone is not marked in the written
language..."). This script re-scores the row with the harness's own
``normalize()`` and ``levenshtein()`` (the same broad-normalized setting the
board uses), then folds ONLY the tone diacritics out of both sides -- it
deliberately does NOT touch the gold's [+/-ATR] vowel-quality letters
(ɑ ɛ ɪ ɔ ɞ), which the spec's notes and audit entry refuse to fold or model
for lack of a source (Gabbard 2010).

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_so_notation.py
"""
from __future__ import annotations

import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "so"
DATASET = "kaikki"

#: Combining tone/stress marks this gold writes on vowels: acute (high),
#: grave (low), macron (long/level), circumflex (contour). NFD-decomposed
#: first so precomposed codepoints (e.g. ú, ā) are also reached.
TONE_MARKS = "́̀̄̂"


def strip_marks(marks: str):
    def fold(s: str) -> str:
        s = unicodedata.normalize("NFD", s)
        s = "".join(c for c in s if c not in marks)
        return unicodedata.normalize("NFC", s)
    return fold


FOLD_TONE = strip_marks(TONE_MARKS)


def scored_pairs(limit=10 ** 9):
    """(word, [normalized golds], normalized hypothesis) per unique word,
    matching build_scoreboard's own grouping."""
    from orthography2ipa import G2P

    engine = G2P(LANG)
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, True, extra_strip=extra)

    refs: dict = {}
    for word, gold in B.load_kaikki(LANG, limit):
        refs.setdefault(word, []).append(gold)

    out = []
    for word, golds in refs.items():
        try:
            hyp = engine.transcribe_word(word)
        except Exception:
            continue
        if hyp:
            out.append((word, [norm(g) for g in golds], norm(hyp)))
    return out


def per(rows, fold=lambda s: s):
    """Mean per-word PER (best-of-golds) after applying *fold* to both sides."""
    total = 0.0
    for _word, golds, hyp in rows:
        h = fold(hyp)
        total += min(B.levenshtein(h, fold(g)) / max(len(fold(g)), 1)
                     for g in golds)
    return total / len(rows)


def report():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored")
    print(f"  as scored                {per(rows):.4f}")
    print(f"  tone folded only         {per(rows, FOLD_TONE):.4f}")


if __name__ == "__main__":
    report()
