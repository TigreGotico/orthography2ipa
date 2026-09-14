#!/usr/bin/env python3
"""Attribute the Brazilian Portuguese ``vox_communis`` PER to the gold.

The ``pt-BR`` / ``vox_communis`` row is the worst Portuguese row on the board
(PER 0.3896 over 33,957 words), which invites reading it as a defect in the
Brazilian spec. It is not one. The row's phone tier is Epitran output over the
region-untagged Common Voice ``pt`` locale, and it is European Portuguese:
measured over the cached TSV, NONE of the four features that define Brazilian
Portuguese appear in it, while the European coda sibilant appears in all of
them.

This script re-scores the row with the harness's own ``normalize()`` and
``levenshtein()``, then folds one gold convention at a time out of BOTH sides
and re-scores, so each convention gets a number instead of an adjective. It
also counts the two ways the gold is not merely a different notation but wrong
about Portuguese of any variety: it has no palatal lateral and no palatal
nasal, so every ``lh`` and ``nh`` word loses its digraph, and it writes the
``ss`` digraph as two segments with the first one palatalised.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_pt_br_notation.py

Nothing here feeds the board. The row stays as scored — it is classified
``epitran-derived`` and cannot gate anything — and this script is how the
offset is quantified. See docs/languages/pt-BR.md.
"""
from __future__ import annotations

import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "pt-BR"
DATASET = "vox_communis"

#: One fold per gold convention, applied to gold and hypothesis alike and
#: CUMULATIVELY, in the order listed. Each entry is (description, function).
#: Every fold removes a distinction the gold cannot express, so folding always
#: loses information: these numbers bound the row's notation offset, they do
#: not improve the spec.
FOLDS = [
    ("coda ⟨s⟩ as [ʃ] (EP chiado, Mateus & d'Andrade 2000: ch.2)",
     lambda s: re.sub(r"ʃ$", "s", s)),
    ("palatal lateral ⟨lh⟩ absent from the gold inventory",
     lambda s: s.replace("ʎ", "l")),
    ("palatal nasal ⟨nh⟩ absent from the gold inventory",
     lambda s: s.replace("ɲ", "n")),
    ("dental affrication before /i/ (Barbosa & Albano 2004: 228)",
     lambda s: s.replace("t͡ʃ", "t").replace("d͡ʒ", "d")),
    ("final unstressed ⟨e o⟩ raising to [i u] (Câmara 1970)",
     lambda s: re.sub(r"i$", "e", re.sub(r"u$", "o", s))),
    ("mid-vowel height ⟨ɛ ɔ⟩ ~ ⟨e o⟩",
     lambda s: s.replace("ɛ", "e").replace("ɔ", "o")),
    ("coda ⟨l⟩ vocalisation to [w] (Barbosa & Albano 2004: 228, /L/)",
     lambda s: re.sub(r"w$", "l", s)),
]

#: Features that define Brazilian Portuguese against European Portuguese, as
#: (description, does the orthography select the word, does the gold show it).
BR_FEATURES = [
    ("final ⟨-l⟩ vocalised to [w]",
     lambda w: w.endswith("l") and len(w) > 3, lambda g: g.endswith("w")),
    ("⟨t⟩ affricated before /i/",
     lambda w: "ti" in w, lambda g: "tʃ" in g),
    ("⟨d⟩ affricated before /i/",
     lambda w: "di" in w, lambda g: "dʒ" in g),
    ("final unstressed ⟨-e⟩ raised to [i]",
     lambda w: w.endswith("e") and len(w) > 3, lambda g: g.endswith("i")),
    ("final unstressed ⟨-o⟩ raised to [u]",
     lambda w: w.endswith("o") and len(w) > 3, lambda g: g.endswith("u")),
    ("final ⟨-s⟩ as alveolar [s], not the EP [ʃ]",
     lambda w: w.endswith("s") and len(w) > 3, lambda g: g.endswith("s")),
]


def scored_pairs():
    """(word, normalized gold, normalized hypothesis) for every scored word."""
    from orthography2ipa import G2P

    engine = G2P(LANG)
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, False, extra_strip=extra)

    out = []
    for word, gold in B.load_vox_communis(LANG, 10 ** 9):
        try:
            hyp = engine.transcribe_word(word)
        except Exception:
            continue
        if hyp:
            out.append((word, norm(gold), norm(hyp)))
    return out


def per(rows, fold=lambda s: s):
    """Mean per-word PER after applying *fold* to both sides."""
    total = 0.0
    for _word, gold, hyp in rows:
        g, h = fold(gold), fold(hyp)
        total += B.levenshtein(h, g) / max(len(g), 1)
    return total / len(rows)


def compose(fns):
    """Apply *fns* left to right."""
    def folded(s):
        for fn in fns:
            s = fn(s)
        return s
    return folded


def main():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored\n")

    print("Cumulative folds of gold conventions (both sides):")
    print(f"  {'as scored':<58} {per(rows):.4f}")
    fns = []
    for name, fn in FOLDS:
        fns.append(fn)
        print(f"  + {name:<56} {per(rows, compose(fns)):.4f}")

    print("\nDefining Brazilian features, as attested in this gold:")
    for name, selects, shows in BR_FEATURES:
        sel = [g for w, g, _h in rows if selects(w.lower())]
        hit = sum(1 for g in sel if shows(g))
        pct = 100 * hit / max(len(sel), 1)
        print(f"  {name:<46} {hit:>6}/{len(sel):<6} {pct:5.1f}%")

    phones = collections.Counter(c for _w, g, _h in rows for c in g)
    print(f"\n  Gold phone inventory: {len(phones)} symbols, "
          f"⟨ʎ⟩ ×{phones['ʎ']}, ⟨ɲ⟩ ×{phones['ɲ']}.")
    lh = sum(1 for w, _g, _h in rows if "lh" in w.lower())
    nh = sum(1 for w, _g, _h in rows if "nh" in w.lower())
    print(f"  Words spelled with ⟨lh⟩: {lh}; with ⟨nh⟩: {nh}. Both digraphs "
          f"lose their ⟨h⟩\n  in the gold, which has neither palatal.")

    ss = [(w, g) for w, g, _h in rows if "ss" in w.lower()]
    split = sum(1 for _w, g in ss if "ʃs" in g)
    print(f"\n  Words spelled with ⟨ss⟩: {len(ss)}; written [ʃs] rather than "
          f"[s]: {split}.\n  The gold applies the EP coda rule inside the "
          f"digraph (isso → [iʃso]).")

    rr = [(w, g) for w, g, _h in rows if "rr" in w.lower()]
    doubled = sum(1 for _w, g in rr if "ʁʁ" in g or "rr" in g)
    print(f"  Words spelled with ⟨rr⟩: {len(rr)}; transcribed with a doubled "
          f"rhotic: {doubled}.\n  ⟨rr⟩ is a digraph for the strong rhotic, "
          f"not a geminate, in gold and spec alike.")


if __name__ == "__main__":
    main()
