#!/usr/bin/env python3
"""Attribute the American English ``ipa_babylm`` PER to this gold's notation, then count the rest.

The ``en-US`` / ``ipa_babylm`` row scores PER 0.3602 over 20103 words, the
worst English row on the board. The gold is ``espeak-derived`` (a scored
competitor's output: directional signal only, never a gate), and it writes
English in espeak-ng's own conventions:

  * tense vowels carry a length mark (``siː``, ``niːd``) that this spec, which
    follows Ladefoged's American convention, does not write;
  * ``d̠ʒ`` and ``t̠ʃ`` carry a retraction mark;
  * the NURSE and LETTER vowels are ``ɜː`` and ``əɹ`` where this spec writes
    the r-coloured ``ɝ`` and ``ɚ``;
  * a doubled ``ɹɹ`` appears across some morpheme boundaries;
  * STRUT is ``ʌ`` in words this spec reduces to ``ə``.

This script re-scores the row with the harness's own ``normalize()`` (broad,
the setting the board uses) and ``levenshtein()``, then folds one convention
at a time out of BOTH sides, cumulatively, so each gets a number instead of
an adjective. What the folds leave is English spelling itself: the letter
⟨a e i o u⟩ does not say which of its readings a word takes, and that is
counted below by residue class, not folded.

It also prints the counts behind the three rules this row measured:
word-final ⟨s⟩ after a tense vowel or an r-coloured vowel is [z], word-final
⟨y⟩ in a monosyllable is [aɪ], and the pronoun I and the five verb forms
is/as/was/has/his are whole-word exceptions.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_en_us_notation.py
"""
from __future__ import annotations

import collections
import difflib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "en-US"
DATASET = "ipa_babylm"

#: One fold per notation convention, both sides, cumulative, in this order.
FOLDS = [
    ("vowel length ː dropped (espeak marks tense vowels long)", lambda s: s.replace("ː", "")),
    ("retraction mark dropped (espeak's d̠ʒ t̠ʃ)", lambda s: s.replace("̠", "")),
    ("r-coloured vowels: ɝ ɚ ~ ɜ ~ əɹ",
     lambda s: s.replace("ɝ", "əɹ").replace("ɚ", "əɹ").replace("ɜɹ", "əɹ").replace("ɜ", "əɹ")),
    ("doubled ɹɹ written once", lambda s: s.replace("ɹɹ", "ɹ")),
    ("ʌ ~ ə", lambda s: s.replace("ʌ", "ə")),
    ("word-final i ~ ɪ", lambda s: re.sub(r"i$", "ɪ", s)),
]

_VOWEL = set("aeiouæɑɒɔəɛɜɝɚɪʊʌ")


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


def residue_classes(rows, fold):
    """Edit operations left after *fold*, grouped as vowel or consonant."""
    kinds = collections.Counter()
    for _w, golds, h in rows:
        fh = fold(h)
        fg = min((fold(g) for g in golds), key=lambda g: B.levenshtein(fh, g))
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, fh, fg, autojunk=False).get_opcodes():
            if op == "equal":
                continue
            seg = fh[i1:i2] + fg[j1:j2]
            kinds["vowel" if seg and all(c in _VOWEL for c in seg) else "consonant or mixed"] += 1
    return kinds


def strip_punct(w):
    return re.sub(r"[^A-Za-z']", "", w)


def main():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored\n")
    print("Cumulative folds of this gold's notation (both sides):")
    print(f"  {'as scored':<58} {per(rows):.4f}")
    fns = []
    for name, fn in FOLDS:
        fns.append(fn)
        print(f"  + {name:<56} {per(rows, compose(fns)):.4f}")
    fold = compose(fns)
    exact = sum(1 for _w, golds, h in rows if any(fold(h) == fold(g) for g in golds))
    print(f"  exact matches after all folds: {exact} of {len(rows)} ({100 * exact / len(rows):.1f}%)")

    kinds = residue_classes(rows, fold)
    total = sum(kinds.values())
    print("\nWhat the folds leave, by edit operation:")
    for k, n in kinds.most_common():
        print(f"  {k:<22} {n:>6} ({100 * n / total:.1f}%)")

    print("\nThe rules this row measured (words; gold has it; we have it):")
    def count(pred, gold_has, ours_has):
        sel = [(w, golds, h) for w, golds, h in rows if pred(strip_punct(w).lower())]
        return (len(sel), sum(1 for _w, golds, _h in sel if any(gold_has(g) for g in golds)),
                sum(1 for _w, _g, h in sel if ours_has(h)))
    for name, pred, gold_has, ours_has in [
        ("final ⟨s⟩ after a vowel digraph (days, goes, sees)",
         lambda w: re.search(r"([aeiou]{2}|[aeiou][yw])s$", w) is not None,
         lambda g: g.endswith("z"), lambda h: h.endswith("z")),
        ("final ⟨s⟩ after vowel + ⟨r⟩ (cars, years)",
         lambda w: re.search(r"[aeiou]rs$", w) is not None,
         lambda g: g.endswith("z"), lambda h: h.endswith("z")),
        ("monosyllable ending in consonant + ⟨y⟩ (my, why, try)",
         lambda w: re.search(r"^[^aeiou]+y$", w) is not None and len(w) <= 4,
         lambda g: g.endswith("aɪ"), lambda h: h.endswith("aɪ")),
        ("the pronoun I and its contractions",
         lambda w: w in ("i", "i'm", "i'll", "i'd", "i've"),
         lambda g: g.startswith("aɪ"), lambda h: h.startswith("aɪ")),
        ("is, as, was, has, his",
         lambda w: w in ("is", "as", "was", "has", "his"),
         lambda g: g.endswith("z"), lambda h: h.endswith("z")),
    ]:
        n, g, o = count(pred, gold_has, ours_has)
        print(f"  {name:<52} {n:>5} {g:>5} {o:>5}")


if __name__ == "__main__":
    main()
