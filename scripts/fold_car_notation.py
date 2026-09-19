#!/usr/bin/env python3
"""Measure the Galibi Carib (``car``/``wold``) vowel-length-only ceiling.

The ``car``/``wold`` row is scored against a broad/phonemic lexibank gold
that marks vowel length on only 2 of its 1191 rows (checked directly:
``grep -c ':' `` over the loaded gold pairs, see ``VALID_CEILING`` in
``car.json``). ``car``'s ``stress.iambic_length`` flag realises Courtz's
Eastern Surinamese Carib footing rule (2008, *A Carib Grammar and
Dictionary*, section 2.3.2, section 2.4.1 p.31: "All vowels may be
pronounced a little longer ... when stressed"), which the wold gold's
notation cannot record. This script re-scores the row with the harness's
own ``normalize()`` and ``levenshtein()`` (the same broad-normalized
setting the board uses), then folds the IPA length mark out of BOTH sides.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_car_notation.py
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "car"
DATASET = "wold"

LENGTH_MARK = "ː"


def fold_length(s: str) -> str:
    return s.replace(LENGTH_MARK, "")


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
    for word, gold in B.load_wold(LANG, limit):
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
    n_gold_with_length = sum(
        1 for _w, golds, _h in rows if any(LENGTH_MARK in g for g in golds))
    print(f"{DATASET} / {LANG} ({label}): {len(rows)} words scored, "
          f"{n_gold_with_length} with a gold length mark")
    as_scored, as_scored_exact = per(rows)
    length_folded, length_folded_exact = per(rows, fold_length)
    print(f"  as scored          per={as_scored:.4f} exact={as_scored_exact:.4f}")
    print(f"  length folded      per={length_folded:.4f} exact={length_folded_exact:.4f}")
    print()


def main():
    report(10 ** 9, "full")


if __name__ == "__main__":
    main()
