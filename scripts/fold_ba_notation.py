#!/usr/bin/env python3
"""Attribute the Bashkir ``vox_communis`` PER to this gold's vowel notation.

The ``ba`` / ``vox_communis`` row scores PER 0.4047 over 70528 words. The gold
is ``epitran-derived`` (a scored competitor's output: directional signal only,
never a gate), and it writes the Bashkir vowels and the voiced uvular in a
different symbol set from this spec's, one symbol for one symbol:

  =====  =====  ============================================
  ours   gold   letter
  =====  =====  ============================================
  a      ɑ      ⟨а⟩ (and the gold's ``a`` is our ``æ``, ⟨ә⟩)
  æ      a      ⟨ә⟩
  ɯ      ɤ      ⟨ы⟩
  e      ɘ      ⟨е⟩ ⟨э⟩
  ø      ɵ      ⟨ө⟩
  ʁ      ɣ      ⟨ғ⟩
  w      u      ⟨у⟩ ⟨ү⟩ after a vowel (a glide here, a vowel there)
  =====  =====  ============================================

Every one of these is a notation choice: both sides agree which letter is
which phoneme and disagree on the IPA symbol for it. The one reading that
is not a pure symbol swap is ⟨и⟩, which this spec reads ``i`` and the gold
reads ``ɘj`` (10419 words) — the gold analyses that letter as a diphthong.

The folds are applied to BOTH sides, cumulatively, with the harness's own
``normalize()`` (broad) and ``levenshtein()``. Because two of the swaps
chain (our ``a`` is their ``ɑ`` while their ``a`` is our ``æ``), the vowel
swap is done as one simultaneous mapping on our side, never letter by letter.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_ba_notation.py

Nothing here feeds the board. See ``data/ba.json``'s ``audit.vox_communis``.
"""
from __future__ import annotations

import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "ba"
DATASET = "vox_communis"

#: Our symbol -> the gold's symbol, applied simultaneously to OUR side only.
#: Applying it to the gold too would double-swap the chained pairs.
VOWEL_MAP = str.maketrans({"a": "ɑ", "æ": "a", "ɯ": "ɤ", "e": "ɘ", "ø": "ɵ"})


def swap_vowels(s):
    return s.translate(VOWEL_MAP)


#: (description, fold on our side, fold on the gold side)
FOLDS = [
    ("vowel symbols: our a æ ɯ e ø read as the gold's ɑ a ɤ ɘ ɵ",
     swap_vowels, lambda s: s),
    ("voiced uvular ʁ ~ ɣ", lambda s: s.replace("ʁ", "ɣ"), lambda s: s),
    ("glide w ~ vowel u after a vowel (⟨у ү⟩)", lambda s: s.replace("w", "u"), lambda s: s),
    ("⟨и⟩ i ~ ɘj, the gold's diphthong reading",
     lambda s: s, lambda s: s.replace("ɘj", "i")),
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
            hyp = engine.transcribe_word(word)
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
    print("Cumulative folds of this gold's notation:")
    print(f"  {'as scored':<58} {per(rows):.4f}")
    ours, theirs = [], []
    for name, fo, ft in FOLDS:
        ours.append(fo)
        theirs.append(ft)
        print(f"  + {name:<56} {per(rows, compose(ours), compose(theirs)):.4f}")

    exact = sum(1 for _w, golds, h in rows
                if any(compose(ours)(h) == compose(theirs)(g) for g in golds))
    print(f"\n  exact matches after all folds: {exact} of {len(rows)} "
          f"({100 * exact / len(rows):.1f}%)")
    i_words = sum(1 for w, _g, _h in rows if "и" in w)
    print(f"  words spelled with ⟨и⟩: {i_words}")


if __name__ == "__main__":
    main()
