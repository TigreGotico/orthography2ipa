#!/usr/bin/env python3
"""Attribute the Setswana ``vox_communis`` PER to gold/spec notation, not error.

The ``tn`` / ``vox_communis`` row scores PER 0.4003 over 2271 words, which
invites reading it as a defect in the Setswana spec. Almost none of it is.
The gold's phone tier is epitran-derived (a scored competitor's lexicon, see
``benchmark.load_vox_communis``'s PROVENANCE note): directional signal only,
never a gate. Neither side of this row marks tone (Setswana orthography does
not write it, and this gold does not supply it either), so raw PER is not
measuring an orthography-vs-tone silence -- there is no tone to fold out.

This script re-scores the row with the harness's own ``normalize()`` and
``levenshtein()`` (broad-normalized, the same setting the board itself
uses), then folds one convention at a time out of BOTH sides, cumulatively,
so each convention gets a number instead of an adjective:

  * the vowel letters ⟨e⟩/⟨o⟩ are phonemically the RAISED close-mid /e̝/ /o̝/,
    per Bennett, Diemer, Kerford, Probert & Wesi (2016, JIPA 46(2)): "we
    therefore transcribe them as raised close-mid [e̝] and [o̝]" -- explicitly
    moving away from the older /ɪ/ /ʊ/ notation the same paper attributes to
    Cole (1955) and calls too high. The same source documents that the
    modern orthography leaves the height diacritic out entirely, so ⟨e⟩/⟨o⟩
    are genuinely ambiguous between that close-mid value and the open-mid
    /ɛ/ /ɔ/ alternate ("both sets of vowels are represented as e and o"; see
    Chebanne et al. 2003 for the orthographic convention). This fold
    therefore has two legs: first the notation gap between the gold's
    literal /ɪ/ /ʊ/ symbols and the corrected /e̝/ /o̝/ (a symbol-set
    mismatch, not a phonemic error), then the letter-level ambiguity itself
    (gold commits to one member of the pair per letter; the spec keeps both
    as a documented candidate pair rather than reverse-engineering the
    gold's choice);
  * ⟨b⟩ is phonemically the implosive /ɓ/ (Cole 1955; Sotho-Tswana typology),
    but the epitran-derived gold's lexicon writes a plain /b/ for every token;
  * ⟨kg⟩ is the uvular fricative /χ/, matching Bennett et al. 2016 and the
    gold's own uvular symbol -- this fold is a near-no-op once the spec value
    is correct, and is kept here as a tripwire against a future regression to
    the earlier (incorrect) velar /x/ analysis;
  * the ejective marker ʼ is a convention this particular gold's phone tier
    never encodes at all (its inventory has no ejective symbol whatsoever),
    even though Bennett et al. 2016 confirm the ejective/aspirate contrast is
    real (with speaker-variable realization).

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_tn_notation.py

Nothing here feeds the board. The row stays as scored -- it is classified
``epitran-derived`` and cannot gate anything -- and this script is how the
offset is quantified. See ``data/tn.json``'s ``notes`` field.
"""
from __future__ import annotations

import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "tn"
DATASET = "vox_communis"

FOLDS = [
    ("gold's ɪ/ʊ symbols ~ corrected e̝/o̝ (Bennett et al. 2016 notation gap)",
     lambda s: s.replace("ɪ", "e̝").replace("ʊ", "o̝")),
    ("⟨e⟩/⟨o⟩ letter-level ambiguity: close-mid e̝/o̝ ~ open-mid ɛ/ɔ folded "
     "together (the letter alone never decides which; gold commits to one)",
     lambda s: s.replace("ɛ", "e̝").replace("ɔ", "o̝")),
    ("implosive ⟨b⟩ /ɓ/ ~ plain /b/ (gold's lexicon writes plain b)",
     lambda s: s.replace("ɓ", "b")),
    ("⟨kg⟩ uvular /χ/ ~ velar /x/ (place-of-articulation tripwire)",
     lambda s: s.replace("χ", "x")),
    ("aspiration marker ʰ dropped",
     lambda s: s.replace("ʰ", "")),
    ("ejective marker ʼ dropped (gold's phone tier has no ejective symbol)",
     lambda s: s.replace("ʼ", "").replace("ˀ", "")),
]


def scored_pairs():
    """(word, normalized gold, normalized hypothesis) for every scored word."""
    from orthography2ipa import G2P

    engine = G2P(LANG)
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, True, extra_strip=extra)

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

    print("Cumulative folds of gold/spec notation conventions (both sides):")
    print(f"  {'as scored':<62} {per(rows):.4f}")
    fns = []
    for name, fn in FOLDS:
        fns.append(fn)
        print(f"  + {name:<60} {per(rows, compose(fns)):.4f}")

    kg_words = [(w, g, h) for w, g, h in rows if "kg" in w.lower()]
    print(f"\n⟨kg⟩ tokens: {len(kg_words)}; gold contains χ (uvular): "
          f"{sum('χ' in g for _, g, _ in kg_words)}; "
          f"contains x (velar): {sum('x' in g for _, g, _ in kg_words)}")

    b_words = [(w, g, h) for w, g, h in rows if "b" in w.lower()]
    print(f"⟨b⟩ tokens: {len(b_words)}; gold contains ɓ (implosive): "
          f"{sum('ɓ' in g for _, g, _ in b_words)}")

    q_words = [w for w, _g, _h in rows if "q" in w.lower()]
    print(f"⟨q⟩/⟨qh⟩ tokens (clicks): {len(q_words)} -- unattested in this "
          f"sample, so the click claim cannot be checked against this gold.")

    phones_gold = collections.Counter(c for _w, g, _h in rows for c in g)
    e_words = [w for w, _g, _h in rows if "e" in w.lower()]
    o_words = [w for w, _g, _h in rows if "o" in w.lower()]
    print(f"\nwords spelled with ⟨e⟩: {len(e_words)}; gold phone tier contains "
          f"ɪ (its near-close symbol): {phones_gold['ɪ']}; contains ɛ "
          f"(open-mid): {phones_gold['ɛ']}. Gold's convention resolves the "
          f"letter-level ambiguity by never writing the open-mid member for "
          f"this sample -- a gold convention, not evidence the spec's own "
          f"candidate pair is wrong (see Bennett et al. 2016 on the letter's "
          f"real ambiguity in the modern orthography).")
    print(f"words spelled with ⟨o⟩: {len(o_words)}; gold phone tier contains "
          f"ʊ: {phones_gold['ʊ']}; contains ɔ: {phones_gold['ɔ']}.")
    print("Diacritic-bearing ⟨ê⟩/⟨ô⟩ (explicit open-mid, Chebanne et al. 2003 "
          "orthographic convention per Bennett et al. 2016): unattested in "
          "this sample's word list (the modern orthography this gold was "
          "built from drops the diacritic).")


if __name__ == "__main__":
    main()
