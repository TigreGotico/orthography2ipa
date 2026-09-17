#!/usr/bin/env python3
"""Attribute the German ``ipa_childes`` PER to this gold's notation, and
count the one place the gold is wrong about German.

The ``de-DE`` / ``ipa_childes`` row scores PER 0.3948 over 24857 words. The
gold is ``epitran-derived`` (a scored competitor's output: directional signal
only, never a gate), and it writes German in epitran's conventions:

  * every voiceless stop is aspirated (``kʰ tʰ pʰ``), which this broad spec
    does not write;
  * the rhotic is ``ʀ`` where this spec writes ``ʁ``, and after a vowel the
    gold keeps a full ``ʀ`` where this spec writes the vocalised ``ɐ``;
  * vowels in open syllables are written long (``jaː`` ``duː`` ``maːn``) where
    this spec, following Duden, writes ⟨a⟩ ⟨u⟩ in ``ja`` ``du`` ``man`` short;
  * the lax vowels ``ʊ ʏ ɔ`` are written as their tense counterparts.

One thing is not notation. The gold reads an unstressed ⟨e⟩, above all the
word-final ⟨-e⟩ of ``heute`` ``rote`` ``eine``, as ``ɛː``, a long open-mid
vowel. German has no such reading: that letter is the schwa [ə] (Duden, Wiese
1996). This spec writes ``ə``. The script folds that difference out like the
others so the size of the notation offset is stated honestly, but it counts
those words separately and the audit entry names it as a gold error, not a
convention.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_de_notation.py

Nothing here feeds the board. See ``data/de-DE.json``'s ``audit.ipa_childes``.
"""
from __future__ import annotations

import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "de-DE"
DATASET = "ipa_childes"

#: (description, fold on our side, fold on the gold side)
FOLDS = [
    ("aspiration ʰ dropped (this gold aspirates every voiceless stop)",
     lambda s: s, lambda s: s.replace("ʰ", "")),
    ("rhotic ʁ ~ ʀ, and vocalised ɐ ~ ʀ",
     lambda s: s.replace("ʁ", "ʀ").replace("ɐ", "ʀ"), lambda s: s),
    ("vowel length ː dropped (open-syllable long vowels)",
     lambda s: s.replace("ː", ""), lambda s: s.replace("ː", "")),
    ("lax ʊ ʏ ɔ ɪ ~ tense u y o i",
     lambda s: s.translate(str.maketrans({"ʊ": "u", "ʏ": "y", "ɔ": "o", "ɪ": "i"})),
     lambda s: s.translate(str.maketrans({"ʊ": "u", "ʏ": "y", "ɔ": "o", "ɪ": "i"}))),
    ("unstressed ⟨e⟩: our ə ~ the gold's ɛ (a gold error, counted below)",
     lambda s: s.replace("ə", "ɛ"), lambda s: s),
]


def scored_pairs():
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
            transcribe = (engine.transcribe if B._is_multiword(word)
                          else engine.transcribe_word)
            hyp = transcribe(word)
        except Exception:
            continue
        if hyp:
            out.append((word, [norm(g) for g in golds], norm(hyp)))
    return out


def per(rows, ours=lambda s: s, theirs=lambda s: s):
    total = 0.0
    for _word, golds, hyp in rows:
        h = ours(hyp)
        total += min(B.levenshtein(h, theirs(g)) / max(len(theirs(g)), 1)
                     for g in golds)
    return total / len(rows)


def compose(fns):
    def folded(s):
        for fn in fns:
            s = fn(s)
        return s
    return folded


def main():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored\n")
    print("Cumulative folds (our side / gold side):")
    print(f"  {'as scored':<66} {per(rows):.4f}")
    ours, theirs = [], []
    for name, fo, ft in FOLDS:
        ours.append(fo)
        theirs.append(ft)
        print(f"  + {name:<64} {per(rows, compose(ours), compose(theirs)):.4f}")

    final_e = [(w, golds) for w, golds, _h in rows if w.lower().endswith("e") and w.isalpha()]
    gold_long = sum(1 for _w, golds in final_e if any(g.endswith("ɛː") for g in golds))
    gold_schwa = sum(1 for _w, golds in final_e if any(g.endswith("ə") for g in golds))
    print(f"\n  words ending in ⟨-e⟩: {len(final_e)}; gold ends ɛː: {gold_long}; "
          f"gold ends ə: {gold_schwa}")
    asp = sum(1 for _w, golds, _h in rows if any("ʰ" in g for g in golds))
    print(f"  gold words with an aspiration mark: {asp} of {len(rows)}")


if __name__ == "__main__":
    main()
