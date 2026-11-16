#!/usr/bin/env python3
"""Measure the Gawri (``gwc``/``wikipron``) tone ceiling.

The ``gwc``/``wikipron`` row scores the Perso-Arabic spelling against a gold
that marks tone on nearly every word. Baart & Sagar (The Gawri Language of
Kalam and Dir Kohistan, p. 10, "The writing of tone in Gawri") say the 1995
spelling committee made tone diacritics available, but "on most words the
tone marks would not need to be used". This script re-scores the row with the
harness's own ``normalize()`` and ``levenshtein()`` (the same broad-normalized
setting the board uses), then folds the gold's combining tone diacritics out
of BOTH sides. Tone+length is printed as well, for comparison only: the same
source says Jazm marks vowel shortness "where necessary", so length is partly
written and is not recorded as a ceiling.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_gwc_notation.py
"""
from __future__ import annotations

import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "gwc"
DATASET = "wikipron"

#: Combining tone diacritics this gold uses: acute, grave, circumflex, caron.
#: The text is NFD-decomposed first, so precomposed letters such as á reach
#: the fold too.
TONE_MARKS = "́̀̂̌"
LENGTH_MARKS = "ː"


def strip_marks(marks: str):
    # Recompose after stripping, so a mark that is not folded (such as the
    # nasal tilde) counts as one symbol, the way normalize() returns it.
    def fold(s: str) -> str:
        kept = "".join(c for c in unicodedata.normalize("NFD", s)
                       if c not in marks)
        return unicodedata.normalize("NFC", kept)
    return fold


FOLD_TONE = strip_marks(TONE_MARKS)
FOLD_TONE_LENGTH = strip_marks(TONE_MARKS + LENGTH_MARKS)


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
    exact = 0
    for _word, golds, hyp in rows:
        h = fold(hyp)
        folded_golds = [fold(g) for g in golds]
        total += min(B.levenshtein(h, g) / max(len(g), 1) for g in folded_golds)
        if h in folded_golds:
            exact += 1
    return total / len(rows), exact / len(rows)


def report(limit, label):
    rows = scored_pairs(limit)
    print(f"{DATASET} / {LANG} ({label}): {len(rows)} words scored")
    as_scored, as_scored_exact = per(rows)
    tone_folded, tone_folded_exact = per(rows, FOLD_TONE)
    both, both_exact = per(rows, FOLD_TONE_LENGTH)
    print(f"  as scored          per={as_scored:.4f} exact={as_scored_exact:.4f}")
    print(f"  tone folded        per={tone_folded:.4f} exact={tone_folded_exact:.4f}")
    print(f"  tone+length folded per={both:.4f} exact={both_exact:.4f}"
          "  (comparison only)")
    print()


def main():
    report(10 ** 9, "full")


if __name__ == "__main__":
    main()
