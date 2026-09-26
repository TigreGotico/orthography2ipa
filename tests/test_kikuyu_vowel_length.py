"""Cited-claim tests for Gĩkũyũ (``ki``) orthographic vowel length.

Vowel length is phonemic in Gĩkũyũ, and where the standard orthography
writes it at all it writes it by doubling the vowel letter: "Vowel length
is phonemic in Gĩkũyũ. It is often indicated orthographically by means of
a sequence of two identical vowels. However, this is not consistent,
especially across morpheme boundaries, and so the orthography cannot be
taken as a reliable indicator of whether a vowel is long or short"
(Englebretson, ed., 2015, *A Basic Sketch Grammar of Gĩkũyũ*, Orthography,
https://www.ruf.rice.edu/~reng/kik/sketch.pdf).

The unreliability runs one way. A doubled vowel letter is evidence of
length; a single vowel letter is no evidence of shortness. This file pins
both halves against the shipped ki/wikipron gold, so that the doubled
graphemes cannot be dropped again and the under-writing is not mistaken
for a rule the engine could learn.
"""
from __future__ import annotations

import pathlib
import re
import sys

from orthography2ipa import G2P

SCRIPTS_DIR = pathlib.Path(__file__).parent.parent / "scripts"

_VOWEL_LETTERS = "aeiouĩũ"
_DOUBLED = re.compile("([" + _VOWEL_LETTERS + r"])\1")


def _load_gold():
    sys.path.insert(0, str(SCRIPTS_DIR))
    import benchmark as bm
    return bm.load_wikipron("ki", 10 ** 9)


def test_doubled_vowel_letters_transcribe_long():
    engine = G2P("ki")
    for word, expected in [
        ("baara", "βaːɾa"),
        ("cuuka", "ʃuːka"),
        ("mbaage", "ᵐbaːɣɛ"),
        ("gĩthũũri", "ɣeðoːɾi"),
        ("nyee", "ɲɛː"),
    ]:
        assert engine.transcribe_word(word) == expected, word


def test_single_vowel_letters_stay_short():
    """The doubled graphemes must not leak into single-letter spellings."""
    engine = G2P("ki")
    assert "ː" not in engine.transcribe_word("mũgate")
    assert "ː" not in engine.transcribe_word("njamba")


def test_doubling_is_evidence_of_length_and_single_letters_are_not():
    """The asymmetry Englebretson (2015) states, measured on the gold.

    Doubled spellings are transcribed long in the clear majority of the
    gold rows that use them; but most gold rows that carry a length mark
    are spelled with a single vowel letter, so length is under-written and
    those rows are out of reach for any orthography-driven rule.
    """
    pairs = _load_gold()
    doubled_rows = [(w, g) for w, g in pairs if _DOUBLED.search(w.lower())]
    long_rows = [(w, g) for w, g in pairs if "ː" in g]

    assert len(doubled_rows) == 94
    assert len(long_rows) == 269

    doubled_and_long = [g for w, g in doubled_rows if "ː" in g]
    assert len(doubled_and_long) == 56

    # the other 38 doubled spellings are written as two tone-bearing vowel
    # symbols -- the gold's notation for a long vowel whose two moras carry
    # different tones, not a segmental disagreement
    assert len(doubled_rows) - len(doubled_and_long) == 38

    long_without_doubling = [w for w, g in long_rows
                             if not _DOUBLED.search(w.lower())]
    assert len(long_without_doubling) == 213
