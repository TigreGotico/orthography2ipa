#!/usr/bin/env python3
"""Measure the Dungan (``dng``/``wikipron``) tone-only ceiling.

The ``dng``/``wikipron`` row scores PER 0.4087 over 269 words. Almost all of
it is unwritten tone: the Soviet Dungan Cyrillic orthography never marks tone
in running text (Mair 1990), while the wikipron gold's IPA column carries a
Chao tone-letter digit on every syllable. This script re-scores the row with
the harness's own ``normalize()`` and ``levenshtein()`` (the same
broad-normalized setting the board uses), then folds the superscript tone
digits out of BOTH sides.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_dng_notation.py
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "dng"
DATASET = "wikipron"

#: Superscript Chao tone-letter digits (U+2070-2079 block, minus unused ones)
#: that this gold uses to mark tone contours, e.g. ²⁴, ⁵¹, ⁴⁴, ⁰.
TONE_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"


def strip_marks(marks: str):
    def fold(s: str) -> str:
        return "".join(c for c in s if c not in marks)
    return fold


FOLD_TONE = strip_marks(TONE_DIGITS)


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
    print(f"  as scored          per={as_scored:.4f} exact={as_scored_exact:.4f}")
    print(f"  tone folded        per={tone_folded:.4f} exact={tone_folded_exact:.4f}")
    print()


def main():
    report(10 ** 9, "full")


if __name__ == "__main__":
    main()
