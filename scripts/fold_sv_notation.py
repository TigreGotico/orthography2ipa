#!/usr/bin/env python3
"""Attribute the Swedish ``vox_communis`` PER to this gold's notation choices.

The ``sv`` / ``vox_communis`` row scores PER 0.3717 over 19492 words, the
worst Swedish row on the board, which invites reading it as a defect in the
Swedish spec. Most of it is not one. The gold is ``epitran-derived`` and it
writes Swedish in epitran's own conventions:

  * every vowel in an open syllable is long, stressed or not (``inte`` →
    ``ɪnteː``, ``vara`` → ``vɑːrɑː``), where this spec writes length only
    under stress (Riad 2014);
  * a consonant after a short vowel is written single: the gold carries 12
    geminates in 19492 words, where this spec writes the Swedish long
    consonant (``kappsäck`` → ``kappsɛkk``);
  * ⟨r⟩ + dental is written as two segments (``rn rs rt``) where this spec
    writes the retroflex the assimilation gives (``ɳ ʂ ʈ``);
  * ⟨sk⟩ is ``ɧ`` before any vowel, and ``sɕ`` in a few words, where this spec
    writes ``ɧ`` before a front vowel and ``sk`` elsewhere;
  * vowel quality follows length: ``ɛ ɐ ɑ ɪ ʊ ʏ œ ɵ ɔ`` here against
    ``e a ɑː i u y ø ʉ o`` there.

This script re-scores the row with the harness's own ``normalize()`` (broad,
the setting the board uses) and ``levenshtein()``, then folds one convention
at a time out of BOTH sides, cumulatively, so each gets a number instead of
an adjective. It then counts what the folds leave, which this gold can
measure: the three spelling rules this row fixed (⟨c⟩ before a front vowel is
[s], ⟨gn⟩ inside a word is [ŋn], ⟨hj⟩ is [j]), and the gold's own misreadings
(⟨ng⟩ as ``nj``, ⟨nk⟩ with no velar, ⟨ck⟩ as ``kɕ``).

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_sv_notation.py
"""
from __future__ import annotations

import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "sv"
DATASET = "vox_communis"

_VOWELS = "aeiouyøæœɛɪʊʏɐɑɵɔ"
_QUALITY = str.maketrans({"ɛ": "e", "æ": "e", "ɐ": "a", "ɑ": "a", "ɪ": "i",
                          "ʊ": "u", "ʏ": "y", "œ": "ø", "ɵ": "ʉ", "ɔ": "o"})
_RETROFLEX = {"ɳ": "rn", "ɭ": "rl", "ʂ": "rs", "ʈ": "rt", "ɖ": "rd"}


def _retroflex(s: str) -> str:
    for k, v in _RETROFLEX.items():
        s = s.replace(k, v)
    return s


#: One fold per notation convention, both sides, cumulative, in this order.
FOLDS = [
    ("vowel length ː dropped (the gold lengthens every open syllable)",
     lambda s: s.replace("ː", "")),
    ("geminate consonants written single",
     lambda s: re.sub(rf"([^{_VOWELS}])\1", r"\1", s)),
    ("retroflex ɳ ɭ ʂ ʈ ɖ ~ rn rl rs rt rd", _retroflex),
    ("⟨sk⟩: ɧ ~ sk ~ sɕ", lambda s: s.replace("sɕ", "ɧ").replace("ɧ", "sk")),
    ("vowel quality pairs merged: ɛ æ~e, ɐ ɑ~a, ɪ~i, ʊ~u, ʏ~y, œ~ø, ɵ~ʉ, ɔ~o",
     lambda s: s.translate(_QUALITY)),
]


def scored_pairs():
    """(word, normalized golds, normalized hypothesis) per scored word."""
    from orthography2ipa import G2P

    engine = G2P(LANG)
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, True, extra_strip=extra)

    refs: "collections.OrderedDict[str, list]" = collections.OrderedDict()
    for word, gold in B.DATASETS[DATASET][0](LANG, 10 ** 9):
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
    for _word, golds, hyp in rows:
        h = fold(hyp)
        total += min(B.levenshtein(h, fold(g)) / max(len(fold(g)), 1)
                     for g in golds)
    return total / len(rows)


def compose(fns):
    def folded(s):
        for fn in fns:
            s = fn(s)
        return s
    return folded


def count(rows, pattern, gold_has, ours_has):
    """(words matching *pattern*, gold words with *gold_has*, ours with *ours_has*)."""
    sel = [(w, golds, h) for w, golds, h in rows if re.search(pattern, w.lower())]
    return (len(sel),
            sum(1 for _w, golds, _h in sel if any(gold_has(g) for g in golds)),
            sum(1 for _w, _g, h in sel if ours_has(h)))


def main():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored\n")
    print("Cumulative folds of this gold's notation (both sides):")
    print(f"  {'as scored':<70} {per(rows):.4f}")
    fns = []
    for name, fn in FOLDS:
        fns.append(fn)
        print(f"  + {name:<68} {per(rows, compose(fns)):.4f}")
    fold = compose(fns)
    exact = sum(1 for _w, golds, h in rows if any(fold(h) == fold(g) for g in golds))
    print(f"  exact matches after all folds: {exact} of {len(rows)} ({100 * exact / len(rows):.1f}%)")

    length_ours = sum(1 for _w, _g, h in rows if "ː" in h)
    length_gold = sum(1 for _w, golds, _h in rows if any("ː" in g for g in golds))
    final_e = [(golds, h) for w, golds, h in rows if w.lower().endswith("e") and len(w) > 3]
    final_e_long = sum(1 for golds, _h in final_e if any(g.endswith("eː") for g in golds))
    print(f"  words where we write a length mark: {length_ours}; gold words with one: {length_gold}")
    print(f"  words ending in ⟨-e⟩: {len(final_e)}; gold ends them long eː: {final_e_long}")

    print("\nSpelling rules this gold measures (words; gold has it; we have it):")
    for name, pattern, gold_has, ours_has in [
        ("⟨c⟩ before e i y ä ö is [s]", r"c[eiyäö]", lambda g: "s" in g, lambda h: "s" in h),
        ("⟨gn⟩ inside a word is [ŋn]", r".gn", lambda g: "ŋn" in g, lambda h: "ŋn" in h),
        ("word-initial ⟨gn⟩ stays [ɡn]", r"^gn", lambda g: g.startswith("ɡn"), lambda h: h.startswith("ɡn")),
        ("⟨hj⟩ is [j]", r"hj", lambda g: "hj" not in g, lambda h: "hj" not in h),
        ("⟨sc⟩ before a front vowel is [s]", r"sc[eiyäö]", lambda g: "sk" not in g, lambda h: "sk" not in h),
    ]:
        n, g, o = count(rows, pattern, gold_has, ours_has)
        print(f"  {name:<40} {n:>5} {g:>5} {o:>5}")

    print("\nGold misreadings the folds leave (words; gold has it):")
    for name, pattern, gold_has in [
        ("⟨ng⟩ written nj", r"ng", lambda g: "nj" in g),
        ("⟨nk⟩ with no velar nasal", r"nk", lambda g: "ŋ" not in g),
        ("⟨ck⟩ written kɕ", r"ck", lambda g: "kɕ" in g),
    ]:
        n, g, _o = count(rows, pattern, gold_has, lambda h: False)
        print(f"  {name:<40} {n:>5} {g:>5}")


if __name__ == "__main__":
    main()
