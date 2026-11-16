#!/usr/bin/env python3
"""Attribute the Norwegian ``ipa_childes`` PER to this gold's notation choices.

The ``nb`` / ``ipa_childes`` row scores PER 0.3587 over 3176 words, the worst
Norwegian row on the board. The gold is ``espeak-derived`` (a scored
competitor's output: directional signal only, never a gate), and it writes
Norwegian in espeak-ng's own conventions:

  * every voiceless stop carries an aspiration mark;
  * vowel length is marked where espeak puts it, not where the quantity
    rules of Kristoffersen (2000) do;
  * ⟨r⟩ is a tap ``ɾ`` where this spec writes ``r``;
  * short ⟨å o⟩ are ``ɒ``, short ⟨a⟩ is ``a``, and the lax/tense pairs
    ``ɛ ɪ ʏ ʊ`` are written tense;
  * an unstressed word-final ⟨-e⟩ is ``a`` (599 of the 612 words ending in
    ⟨-e⟩), which is no Norwegian reading of the letter: it is the schwa
    (Kristoffersen 2000), as this spec writes it. That one is folded only
    to size it.

This script re-scores the row with the harness's own ``normalize()`` (broad,
the setting the board uses) and ``levenshtein()``, then folds one convention
at a time out of BOTH sides, cumulatively, so each gets a number instead of
an adjective. It then prints the counts behind the two rules this row
measured: ⟨k⟩ and ⟨g⟩ before a front vowel are palatal only word-initially.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_nb_notation.py
"""
from __future__ import annotations

import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "nb"
DATASET = "ipa_childes"

_QUALITY = str.maketrans({"ɛ": "e", "ɪ": "i", "ʏ": "y", "ʊ": "u", "ɔ": "o"})

#: One fold per notation convention, both sides, cumulative, in this order.
FOLDS = [
    ("aspiration ʰ dropped (espeak aspirates every voiceless stop)", lambda s: s.replace("ʰ", "")),
    ("vowel length ː dropped", lambda s: s.replace("ː", "")),
    ("tap ɾ ~ r", lambda s: s.replace("ɾ", "r")),
    ("short ⟨å o⟩: ɒ ~ ɔ", lambda s: s.replace("ɒ", "ɔ")),
    ("short ⟨a⟩: a ~ ɑ", lambda s: s.replace("ɑ", "a")),
    ("lax ɛ ɪ ʏ ʊ ɔ ~ tense e i y u o", lambda s: s.translate(_QUALITY)),
    ("unstressed ⟨-e⟩: ə ~ a (a gold error, sized here)", lambda s: s.replace("ə", "a")),
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
    sel = [(w, golds, h) for w, golds, h in rows if re.search(pattern, w.lower())]
    return (len(sel),
            sum(1 for _w, golds, _h in sel if any(gold_has(g) for g in golds)),
            sum(1 for _w, _g, h in sel if ours_has(h)))


def main():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored\n")
    print("Cumulative folds of this gold's notation (both sides):")
    print(f"  {'as scored':<62} {per(rows):.4f}")
    fns = []
    for name, fn in FOLDS:
        fns.append(fn)
        print(f"  + {name:<60} {per(rows, compose(fns)):.4f}")
    fold = compose(fns)
    exact = sum(1 for _w, golds, h in rows if any(fold(h) == fold(g) for g in golds))
    print(f"  exact matches after all folds: {exact} of {len(rows)} ({100 * exact / len(rows):.1f}%)")

    final_e = [(golds, h) for w, golds, h in rows if w.lower().endswith("e") and len(w) > 2]
    gold_a = sum(1 for golds, _h in final_e if any(g.endswith("a") for g in golds))
    ours_schwa = sum(1 for _g, h in final_e if h.endswith("ə"))
    print(f"  words ending in ⟨-e⟩: {len(final_e)}; gold ends a: {gold_a}; we end ə: {ours_schwa}")
    asp = sum(1 for _w, golds, _h in rows if any("ʰ" in g for g in golds))
    print(f"  gold words with an aspiration mark: {asp} of {len(rows)}")

    print("\nThe rules this row measured (words; gold has it; we have it):")
    front = "[eiyæø]"
    for name, pattern, gold_has, ours_has in [
        ("medial ⟨k⟩ before a front vowel is [k]", rf"[aeiouyæøå]k{front}",
         lambda g: "k" in g, lambda h: "ç" not in h),
        ("word-initial ⟨k⟩ before a front vowel is [ç]", rf"^k{front}",
         lambda g: g.startswith("ç"), lambda h: h.startswith("ç")),
        ("medial ⟨g⟩ before a front vowel is [ɡ]", rf"[aeiouyæøå]g{front}",
         lambda g: "ɡ" in g, lambda h: "ɡ" in h),
        ("word-initial ⟨g⟩ before a front vowel is [j]", rf"^g{front}",
         lambda g: g.startswith("j"), lambda h: h.startswith("j")),
    ]:
        n, g, o = count(rows, pattern, gold_has, ours_has)
        print(f"  {name:<48} {n:>5} {g:>5} {o:>5}")


if __name__ == "__main__":
    main()
