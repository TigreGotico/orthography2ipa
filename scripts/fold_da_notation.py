#!/usr/bin/env python3
"""Attribute the Danish ``ipa_childes`` PER to this gold's notation choices.

The ``da`` / ``ipa_childes`` row scores PER 0.4476 over 2233 words, the worst
Danish row on the board, which invites reading it as a defect in the Danish
spec. Most of it is not one. The gold is ``espeak-derived`` (a scored
competitor's output: directional signal only, never a gate), and it writes
Danish in espeak-ng's own conventions:

  * stød is written as a pharyngealisation mark ``ˤ`` on the vowel. Danish
    orthography does not write stød at all (see ``da.json`` notes and
    ``audit.wikipron``), so no grapheme rule can place it;
  * vowel length is not marked, while this spec writes ``ː`` from the
    quantity rules the orthography does support;
  * the rhotic is written ``r`` where this spec writes the uvular ``ʁ``;
  * ⟨v⟩ is written ``ʋ`` rather than ``v``;
  * ⟨ø⟩ is written ``œ`` rather than ``ø``;
  * a post-vocalic ⟨r⟩ is written as a full ``r`` after a vowel letter, where
    this spec writes the r-coloured ``ɐ``;
  * stops after ⟨s⟩ are written voiceless (``sk st sp``) where this spec
    writes ``sɡ sd sb`` — the same convention ``audit.wikipron`` records.

This script re-scores the row with the harness's own ``normalize()`` (broad,
the setting the board uses) and ``levenshtein()``, then folds one convention
at a time out of BOTH sides, cumulatively, so each gets a number instead of
an adjective.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_da_notation.py

Nothing here feeds the board. The row stays as scored, and this script is how
the offset is quantified. See ``data/da.json``'s ``audit.ipa_childes``.
"""
from __future__ import annotations

import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "da"
DATASET = "ipa_childes"

#: One fold per convention, applied to gold and hypothesis alike and
#: CUMULATIVELY, in the order listed. Each entry is (description, function).
FOLDS = [
    ("stød mark ˤ dropped (unwritten in the orthography)",
     lambda s: s.replace("ˤ", "")),
    ("vowel length ː dropped (this gold marks none)",
     lambda s: s.replace("ː", "")),
    ("rhotic ʁ ~ r", lambda s: s.replace("ʁ", "r")),
    ("⟨v⟩ ʋ ~ v", lambda s: s.replace("ʋ", "v")),
    ("⟨ø⟩ œ ~ ø", lambda s: s.replace("œ", "ø")),
    ("r-coloured schwa ɐ ~ ɔr", lambda s: s.replace("ɐ", "ɔr")),
    # the same post-s convention audit.wikipron already documents
    ("post-s stops sɡ sd sb ~ sk st sp",
     lambda s: s.replace("sɡ", "sk").replace("sd", "st").replace("sb", "sp")),
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
            transcribe = (engine.transcribe if B._is_multiword(word)
                          else engine.transcribe_word)
            hyp = transcribe(word)
        except Exception:
            continue
        if hyp:
            out.append((word, [norm(g) for g in golds], norm(hyp)))
    return out


def per(rows, fold=lambda s: s):
    """Mean per-word PER after applying *fold* to both sides."""
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


def main():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored\n")
    print("Cumulative folds of this gold's notation (both sides):")
    print(f"  {'as scored':<56} {per(rows):.4f}")
    fns = []
    for name, fn in FOLDS:
        fns.append(fn)
        print(f"  + {name:<54} {per(rows, compose(fns)):.4f}")

    stod = sum(1 for _w, golds, _h in rows if any("ˤ" in g for g in golds))
    length = sum(1 for _w, _g, h in rows if "ː" in h)
    gold_length = sum(1 for _w, golds, _h in rows if any("ː" in g for g in golds))
    print(f"\n  gold words marking stød: {stod} of {len(rows)}")
    print(f"  words where we write a length mark: {length}; "
          f"gold words with one: {gold_length}")


if __name__ == "__main__":
    main()
