#!/usr/bin/env python3
"""Fold the ipa-dict/wikipron notation split out of the Khmer (``km``) row.

The ``km``/``ipadict`` row (n=3261, PER 0.3335) scores far worse than
``km``/``wikipron`` (n=6628, PER 0.1922) against the SAME spec. Both golds
are legitimate: ``_IPADICT_PROVENANCE["km"]`` is ``lexicon-derived`` (the
Khmer-English Dictionary, aakanee.com, CC BY-NC-SA 4.0), a human
lexicographic source, not a scrape. Comparing the 1673 words attested in
both golds shows three systematic notational differences rather than a
disagreement about Khmer:

* length -- ipadict doubles the vowel letter (``kɑɑ``) where wikipron/this
  spec writes a length mark (``kɑː``);
* the labio-dental approximant -- ipadict writes ``v`` where wikipron/this
  spec writes ``ʋ``;
* a final glottal stop -- wikipron/this spec glottalises some final stops
  (``kɑːʔ``) that ipadict keeps as the plain stop (``kɑɑk``).

This script re-scores the ``km``/``ipadict`` row with the harness's own
``normalize()``/``levenshtein()`` (the same broad, stress-stripped setting
the board uses), then folds each of the three differences out of BOTH
sides, cumulatively. It also reports the two golds' per-row rate of ``ʰ``
(aspiration) marking, since that gap survives every fold and is reported,
not resolved, in ``data/km.json``'s ``audit.ipadict`` entry.

Run from the repository root::

    PYTHONPATH=. python scripts/fold_km_notation.py

Nothing here feeds the board; this is a measurement instrument only.
"""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "km"
DATASET = "ipadict"

_DOUBLED_VOWEL = re.compile(r"([aeiouɑɔɛɪʊəɤɨɯ])\1")


def scored_pairs():
    """(word, [normalized golds], normalized hypothesis), one entry per
    unique word -- matches build_scoreboard's own grouping: a word with
    several gold transcriptions is scored against whichever is closest."""
    from orthography2ipa import G2P

    engine = G2P(LANG)
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, True, extra_strip=extra)

    refs: dict = {}
    for word, gold in B.load_ipadict(LANG, 10 ** 9):
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


def fold_length(s: str) -> str:
    """Remove the length mark and collapse a doubled vowel letter to one --
    the same length contrast, written two ways."""
    s = s.replace("ː", "")
    return _DOUBLED_VOWEL.sub(r"\1", s)


def fold_glide(s: str) -> str:
    """ipadict's plain ``v`` and wikipron's ``ʋ`` for the same phoneme."""
    return s.replace("ʋ", "v")


def fold_final_glottal(s: str) -> str:
    """Drop every ``ʔ`` -- wikipron glottalises some final stops that
    ipadict keeps as the plain stop; this does not attempt to reconstruct
    which stop was lost, it only removes the symbol neither side agrees on
    the placement of."""
    return s.replace("ʔ", "")


def aspiration_rate(rows):
    n_gold = sum(1 for _w, golds, _h in rows if any("ʰ" in g for g in golds))
    n_hyp = sum(1 for _w, _g, h in rows if "ʰ" in h)
    return n_gold / len(rows), n_hyp / len(rows)


def shared_word_aspiration():
    """Aspiration rate of EACH gold, restricted to the words attested in
    BOTH -- the direct gold-vs-gold comparison, independent of this spec's
    output, that isolates whether one gold under-marks aspiration relative
    to the other on the identical word set."""
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, True, extra_strip=extra)

    ipadict: dict = {}
    for word, gold in B.load_ipadict(LANG, 10 ** 9):
        ipadict.setdefault(word, []).append(norm(gold))

    wikipron: dict = {}
    for word, gold in B.load_wikipron(LANG, 10 ** 9):
        wikipron.setdefault(word, []).append(norm(gold))

    shared = sorted(set(ipadict) & set(wikipron))
    n_ipadict = sum(1 for w in shared if any("ʰ" in g for g in ipadict[w]))
    n_wikipron = sum(1 for w in shared if any("ʰ" in g for g in wikipron[w]))
    return len(shared), n_ipadict / len(shared), n_wikipron / len(shared)


def main():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored\n")

    raw = per(rows)
    print(f"as scored                   {raw:.4f}")

    length = per(rows, fold_length)
    print(f"length only                 {length:.4f}")

    glide = per(rows, fold_glide)
    print(f"glide only                  {glide:.4f}")

    glottal = per(rows, fold_final_glottal)
    print(f"final glottal only          {glottal:.4f}")

    length_glide = per(rows, lambda s: fold_glide(fold_length(s)))
    print(f"length + glide              {length_glide:.4f}")

    all_three = per(rows, lambda s: fold_final_glottal(
        fold_glide(fold_length(s))))
    print(f"length + glide + glottal    {all_three:.4f}")

    gold_rate, hyp_rate = aspiration_rate(rows)
    print()
    print(f"ipadict/km rows: gold ʰ rate {gold_rate:.3f}, hyp ʰ rate {hyp_rate:.3f}")

    n_shared, ipadict_rate, wikipron_rate = shared_word_aspiration()
    print(f"words shared by both golds: {n_shared}")
    print(f"  ipadict ʰ rate:   {ipadict_rate:.3f}")
    print(f"  wikipron ʰ rate:  {wikipron_rate:.3f}")


if __name__ == "__main__":
    main()
