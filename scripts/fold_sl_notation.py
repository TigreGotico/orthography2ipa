#!/usr/bin/env python3
"""Split the Slovene ``vox_communis`` PER into what the spelling cannot say and what the gold writes differently.

The ``sl`` / ``vox_communis`` row is the worst Slovene row on the board. The
gold is ``epitran-derived`` and marks, on every stressed vowel, a pitch accent
(acute, grave or circumflex) and vowel length. Standard Slovene spelling writes
none of that, and the same source the spec's ``wikipron`` ceiling cites says
stress placement is not predictable from the spelling (Šuštaršič, Komar &
Petek 1995). The spelling also does not say whether ⟨e o⟩ are close-mid or
open-mid, nor when ⟨e⟩ is the schwa. Those are the unwritten contrasts, and
folding them out of BOTH sides gives the ``valid_ceiling``.

After that come two notation choices of the gold, folded so the row's
remainder can be seen: ``ʋ`` for this spec's ``v``, and ``lj nj`` for ``ʎ ɲ``.

The script also prints the counts behind the three rules this row measured:
the syllabic ⟨r⟩ is [ər], word-final obstruents are voiceless, and an
obstruent before a voiceless obstruent is voiceless.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_sl_notation.py
"""
from __future__ import annotations

import collections
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "sl"
DATASET = "vox_communis"

_ACCENTS = "̀́̂̌"


def _strip_accents(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if c not in _ACCENTS)


#: Contrasts the spelling does not write: these give the ceiling.
UNWRITTEN = [
    ("pitch accent and stress marks dropped", _strip_accents),
    ("vowel length ː dropped", lambda s: s.replace("ː", "")),
    ("mid-vowel quality: e ~ ɛ, o ~ ɔ", lambda s: s.replace("e", "ɛ").replace("o", "ɔ")),
    ("schwa for ⟨e⟩: ə ~ ɛ", lambda s: s.replace("ə", "ɛ")),
]

#: The gold's notation, folded after the ceiling so the remainder is visible.
NOTATION = [
    ("ʋ ~ v", lambda s: s.replace("ʋ", "v")),
    ("lj nj ~ ʎ ɲ", lambda s: s.replace("ʎ", "lj").replace("ɲ", "nj")),
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
    print(f"  {'as scored':<56} {per(rows):.4f}")
    fns = []
    print("Unwritten contrasts (both sides, cumulative):")
    for name, fn in UNWRITTEN:
        fns.append(fn)
        print(f"  + {name:<54} {per(rows, compose(fns)):.4f}")
    print(f"  = valid_ceiling")
    print("Gold notation, on top:")
    for name, fn in NOTATION:
        fns.append(fn)
        print(f"  + {name:<54} {per(rows, compose(fns)):.4f}")
    fold = compose(fns)
    exact = sum(1 for _w, golds, h in rows if any(fold(h) == fold(g) for g in golds))
    print(f"  exact matches after all folds: {exact} of {len(rows)} ({100 * exact / len(rows):.1f}%)")
    accented = sum(1 for _w, golds, _h in rows
                   if any(c in _ACCENTS for g in golds for c in unicodedata.normalize("NFD", g)))
    print(f"  gold words carrying a pitch-accent mark: {accented} of {len(rows)}")

    print("\nThe rules this row measured (words; gold has it; we have it):")
    strip = _strip_accents
    for name, pattern, gold_has, ours_has in [
        ("syllabic ⟨r⟩ is [ər]", r"(^|[^aeiou])r([^aeiou]|$)",
         lambda g: "ər" in strip(g), lambda h: "ər" in h),
        ("word-final voiced obstruent letter is voiceless", r"[zdbgž]$",
         lambda g: g[-1] in "stpkʃ", lambda h: h[-1] in "stpkʃ"),
        ("voiced obstruent before a voiceless one is voiceless", r"[zdbgž][ptkscšhfč]",
         lambda g: re.search(r"[zdbɡʒ](?=[ptksʃxf]|ts|tʃ)", g) is None,
         lambda h: re.search(r"[zdbɡʒ](?=[ptksʃxf]|ts|tʃ)", h) is None),
    ]:
        n, g, o = count(rows, pattern, gold_has, ours_has)
        print(f"  {name:<52} {n:>5} {g:>5} {o:>5}")

    print("\nGold misreadings the folds leave (words; gold has it):")
    for name, pattern, gold_has in [
        ("word-initial ⟨r⟩ written ʐ or z", r"^r", lambda g: g[:1] in "ʐz"),
        ("word-initial ⟨d⟩ written z", r"^d[aeiou]", lambda g: g[:1] == "z"),
        ("final ⟨-l⟩ written ʋ", r"[aeiou]l$", lambda g: g.endswith("ʋ")),
    ]:
        n, g, _o = count(rows, pattern, gold_has, lambda h: False)
        print(f"  {name:<52} {n:>5} {g:>5}")


if __name__ == "__main__":
    main()
