#!/usr/bin/env python3
"""Measure the Kikuyu (``ki``/``wikipron``) tone-and-length ceiling.

The ``ki``/``wikipron`` row scores PER 0.3914 over 1025 words. Almost all of
it is unwritten tone: standard Gĩkũyũ orthography marks neither lexical tone
(including downstep) nor vowel length, while the wikipron gold's IPA column
carries both. This script re-scores the row with the harness's own
``normalize()`` and ``levenshtein()`` (the same broad-normalized setting the
board uses), then folds tone and length out of BOTH sides, one at a time and
combined, so each contribution gets its own number instead of an adjective.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_ki_notation.py
"""
from __future__ import annotations

import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "ki"
DATASET = "wikipron"

#: Combining/spacing tone marks: acute (high), grave (low), caron (rising),
#: circumflex (falling), and the modifier-letter downstep (U+A71C ꜜ).
TONE_MARKS = "́̀̌̂ꜜ"

#: Vowel length mark.
LENGTH_MARK = "ː"  # ː


def strip_marks(marks: str):
    def fold(s: str) -> str:
        s = unicodedata.normalize("NFD", s)
        s = "".join(c for c in s if c not in marks)
        return unicodedata.normalize("NFC", s)
    return fold


FOLD_TONE = strip_marks(TONE_MARKS)
FOLD_LENGTH = strip_marks(LENGTH_MARK)
FOLD_BOTH = strip_marks(TONE_MARKS + LENGTH_MARK)


def scored_pairs(limit=10 ** 9):
    """(word, [normalized golds], normalized hypothesis) per unique word,
    matching build_scoreboard's own grouping — a word with several gold
    transcriptions is scored against whichever is closest."""
    from orthography2ipa import G2P

    engine = G2P(LANG)
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, True, extra_strip=extra)

    refs: dict = {}
    for word, gold in B.load_wikipron(LANG, limit):
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


def report(limit, label):
    rows = scored_pairs(limit)
    print(f"{DATASET} / {LANG} ({label}): {len(rows)} words scored")
    print(f"  as scored                {per(rows):.4f}")
    print(f"  tone folded only         {per(rows, FOLD_TONE):.4f}")
    print(f"  length folded only       {per(rows, FOLD_LENGTH):.4f}")
    print(f"  tone + length folded     {per(rows, FOLD_BOTH):.4f}")
    print()


def main():
    report(10 ** 9, "full, n=1025")
    report(1000, "CI sample, limit=1000")


if __name__ == "__main__":
    main()
