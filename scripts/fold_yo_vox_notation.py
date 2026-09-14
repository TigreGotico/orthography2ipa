#!/usr/bin/env python3
"""Measure the Yoruba (``yo``/``vox_communis``) tone-and-nasal fold ceiling.

The ``yo``/``vox_communis`` row scores PER 0.6392: the engine emits Yoruba
tone marks (the spec is verified to 0.0288 on wikipron, #1541) while this
gold's epitran-derived phone tier writes NONE — the reverse of the wikipron
defect. This script folds tone accents and the nasalisation tilde out of
BOTH sides with the harness's own ``normalize()``/``levenshtein()``; the
result bounds how much of the row is notation disagreement the script cannot
record (see th and tn, which carry valid_ceiling on this same dataset).

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_yo_vox_notation.py
"""
from __future__ import annotations

import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "yo"
DATASET = "vox_communis"

# NFC composes combining tone marks into precomposed vowel codepoints,
# so the fold must decompose before filtering.
TONE_MARKS = "̀́̂̄"
NASAL_MARK = "̃"


def fold_tone(s: str) -> str:
    return unicodedata.normalize(
        "NFC", "".join(c for c in unicodedata.normalize("NFD", s)
                       if c not in TONE_MARKS))


def fold_nasal(s: str) -> str:
    return unicodedata.normalize(
        "NFC", "".join(c for c in unicodedata.normalize("NFD", s)
                       if c != NASAL_MARK))


def scored_pairs(limit=10 ** 9):
    from orthography2ipa import G2P

    engine = G2P(LANG)
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, True, extra_strip=extra)

    refs: dict = {}
    for word, gold in B.load_vox_communis(LANG, limit):
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
    total = 0.0
    exact = 0
    for _word, golds, hyp in rows:
        h = fold(hyp)
        folded_golds = [fold(g) for g in golds]
        total += min(B.levenshtein(h, g) / max(len(g), 1) for g in folded_golds)
        if h in folded_golds:
            exact += 1
    return total / len(rows), exact / len(rows)


def char_counts(rows):
    """Mark counts per side, computed AFTER normalization (the scored
    surface), so the citation's numbers match what the scorer sees."""
    import collections
    gold_tone = collections.Counter()
    gold_nasal = 0
    for _word, golds, _hyp in rows:
        for s in golds:
            for c in unicodedata.normalize("NFD", s):
                if c in TONE_MARKS:
                    gold_tone[c] += 1
                elif c == NASAL_MARK:
                    gold_nasal += 1
    return gold_tone, gold_nasal


def main():
    rows = scored_pairs()
    tone, nasal = char_counts(rows)
    n_gold_tone = sum(1 for _w, golds, _h in rows
                      if any(any(c in TONE_MARKS
                                 for c in unicodedata.normalize("NFD", g))
                             for g in golds))
    print(f"{DATASET} / {LANG} (full): {len(rows)} words scored")
    print(f"  gold-side tone marks by accent: {dict(tone)}, nasal: {nasal}")
    print(f"  words with any gold tone mark: {n_gold_tone}")
    a, ae = per(rows)
    print(f"  as scored           per={a:.4f} exact={ae:.4f}")
    t, te = per(rows, fold_tone)
    print(f"  tone folded         per={t:.4f} exact={te:.4f}")
    n_, ne = per(rows, fold_nasal)
    print(f"  nasal folded        per={n_:.4f} exact={ne:.4f}")
    tn, tne = per(rows, lambda s: fold_nasal(fold_tone(s)))
    print(f"  tone+nasal folded   per={tn:.4f} exact={tne:.4f}")


if __name__ == "__main__":
    main()
