#!/usr/bin/env python3
"""Attribute the Punjabi ``vox_communis`` PER to gold notation, and measure
what is left.

The ``pa`` / ``vox_communis`` row scores PER 0.4454 over 4003 words. The gold
is ``epitran-derived`` (a scored competitor's output: directional signal only,
never a gate), and it writes Punjabi in epitran's conventions:

  * no vowel length at all, where this spec writes ``ː`` for the long vowel
    letters (ਾ ੀ ੂ ੇ ੋ) the Gurmukhi script distinguishes from the short ones;
  * ``ɑ`` for the long ⟨ਾ⟩ where this spec writes ``aː``;
  * no tone letter, where this spec writes ``˩`` for the low tone the voiced
    aspirate letters (ਘ ਝ ਢ ਧ ਭ) carry.

Those three are notation. Two things that survive the folds are not
notation, and this script counts them rather than folding them:

  * schwa deletion: the gold drops the inherent vowel of a medial consonant
    (ਮਸਜਦ ``məsdʒəd``, ਜਗਜੀਤ ``dʒəɡdʒit``) where this spec keeps it. That is a
    real phonological rule of Punjabi the spec does not model;
  * a word-final voiced aspirate letter surfaces voiceless in the gold
    (ਸਿੰਘ ``sɪ̃k``) where this spec writes the voiced stop plus the tone.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_pa_notation.py

Nothing here feeds the board. See ``data/pa.json``'s ``audit.vox_communis``.
"""
from __future__ import annotations

import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "pa"
DATASET = "vox_communis"

#: One fold per notation convention, both sides, cumulative, in this order.
FOLDS = [
    ("vowel length ː dropped (this gold marks none)", lambda s: s.replace("ː", "")),
    ("⟨ਾ⟩ aː ~ ɑ (after the length fold, a ~ ɑ)", lambda s: s.replace("a", "ɑ")),
    ("low tone letter ˩ dropped", lambda s: s.replace("˩", "")),
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


def main():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored\n")
    print("Cumulative folds of this gold's notation (both sides):")
    print(f"  {'as scored':<50} {per(rows):.4f}")
    fns = []
    for name, fn in FOLDS:
        fns.append(fn)
        print(f"  + {name:<48} {per(rows, compose(fns)):.4f}")
    fold = compose(fns)

    # What the folds do not touch, counted on the folded strings.
    schwa = sum(1 for _w, golds, h in rows
                if fold(h).count("ə") > min(fold(g).count("ə") for g in golds))
    devoiced = sum(1 for w, golds, h in rows
                   if w[-1] in "ਘਝਢਧਭ" and any(fold(g).endswith(("k", "tʃ", "ʈ", "t", "p")) for g in golds))
    length_ours = sum(1 for _w, _g, h in rows if "ː" in h)
    length_gold = sum(1 for _w, golds, _h in rows if any("ː" in g for g in golds))
    print(f"\n  words where we write a length mark: {length_ours}; gold words with one: {length_gold}")
    print(f"  words where we write more schwas than the gold (schwa deletion): {schwa} of {len(rows)}")
    print(f"  words ending in a voiced aspirate letter whose gold ends voiceless: {devoiced}")


if __name__ == "__main__":
    main()
