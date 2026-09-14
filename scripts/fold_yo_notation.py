#!/usr/bin/env python3
"""Measure the Yoruba (``yo``/``wikipron``) tone-and-nasalisation notation ceiling.

The ``yo``/``wikipron`` row is scored against a wikipron gold whose IPA
carries the Yoruba tone accents and the nasalisation tilde, which the
orthography writes only on the vowel letters the gold restores (documented
in ``yo.md``: the three tone levels of the gold as the acute, the grave
and a mid macron, plus the combining tilde on nasal vowels). This script
re-scores the row with the harness's own ``normalize()`` and
``levenshtein()`` (the same broad-normalized setting the board uses),
then folds tone and nasalisation notation out of BOTH sides.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_yo_notation.py
"""
from __future__ import annotations

import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "yo"
DATASET = "wikipron"

# NFC composes combining tone marks into precomposed vowel codepoints
# (a + U+0301 -> U+00E1), so the fold must decompose before filtering.
TONE_MARKS = "\u0300\u0301\u0302\u0304"
NASAL_MARK = "\u0303"

def fold_tone(s: str) -> str:
    return unicodedata.normalize(
        "NFC", "".join(c for c in unicodedata.normalize("NFD", s)
                       if c not in TONE_MARKS))

def fold_nasal(s: str) -> str:
    return unicodedata.normalize(
        "NFC", "".join(c for c in unicodedata.normalize("NFD", s)
                       if c != NASAL_MARK))

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
    n_gold_tone = sum(1 for _w, golds, _h in rows
                      if any(any(c in TONE_MARKS
                                 for c in unicodedata.normalize("NFD", g))
                             for g in golds))
    n_gold_nasal = sum(1 for _w, golds, _h in rows
                        if any(NASAL_MARK in g for g in golds))
    print(f"{DATASET} / {LANG} ({label}): {len(rows)} words scored, "
          f"{n_gold_tone} with a gold tone mark, "
          f"{n_gold_nasal} with a gold nasalisation mark")
    as_scored, as_exact = per(rows)
    tone_only, tone_only_exact = per(rows, fold_tone)
    nasal_only, nasal_only_exact = per(rows, fold_nasal)
    tone_nasal, tone_nasal_exact = per(rows, lambda s: fold_nasal(fold_tone(s)))
    print(f"  as scored          per={as_scored:.4f} exact={as_exact:.4f}")
    print(f"  tone folded        per={tone_only:.4f} exact={tone_only_exact:.4f}")
    print(f"  nasal folded       per={nasal_only:.4f} exact={nasal_only_exact:.4f}")
    print(f"  tone+nasal folded  per={tone_nasal:.4f} exact={tone_nasal_exact:.4f}")
    print()

def main():
    report(10 ** 9, "full")

if __name__ == "__main__":
    main()
