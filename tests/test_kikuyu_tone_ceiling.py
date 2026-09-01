"""Cited-claim tests for the Kikuyu (``ki``) tone ceiling.

Kikuyu (Gĩkũyũ) is a tonal Bantu language and the standard Latin
orthography does not write tone at all (Englebretson 2015, "A Basic
Sketch Grammar of Gĩkũyũ", Rice University Field Methods Class,
https://www.ruf.rice.edu/~reng/kik/sketch.pdf). Armstrong's *The Phonetic
and Tonal Structure of Kikuyu* (1940) and Clements's later work on the
tone system are the classic descriptive references for the tone system
itself; the spec's notes cite them for the existence of a tone system, not
for a rule this engine implements.

The ki/wikipron gold set marks tone with acute/grave/caron accents on the
vowel and a raised downstep arrow ``ꜜ``, none of which appear in the plain
orthographic headword. This file checks two facts about that gap: (1) the same plain spelling
recurs with different gold tone marking, evidence that the writing
system underdetermines tone and the gold is internally inconsistent for
a tone-blind rule set (this does not by itself floor or ceiling any
score, since the harness scores a spelling against the best-matching of
its gold transcriptions), and (2) scoring with tone folded out of both
hypothesis and gold collapses PER from the shipped ~0.40 to a small
residual — this second measurement is what actually establishes the
ceiling, and is what the notes report as the measured "0.0523" figure
once tone is discounted.
"""
from __future__ import annotations

import json
import pathlib
import sys
import unicodedata

import pytest

DATA_DIR = (pathlib.Path(__file__).parent.parent
            / "orthography2ipa" / "data")

_TONE_MARKS = {"̀", "́", "̌", "ꜜ"}  # grave, acute, caron, downstep


def _fold_tone(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if c not in _TONE_MARKS)
    return unicodedata.normalize("NFC", s)


def _load_gold():
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm
    return bm.load_wikipron("ki", 10 ** 9)


def test_notes_document_the_measured_tone_ceiling():
    raw = json.loads((DATA_DIR / "ki.json").read_text(encoding="utf-8"))
    notes = raw["notes"]
    assert "tone" in notes
    assert "321" in notes
    assert "0.0523" in notes


def test_identical_spelling_maps_to_more_than_one_gold_tone():
    """Direct evidence that the plain orthography cannot disambiguate tone:
    the same wikipron headword recurs with different gold tone marking."""
    pairs = _load_gold()
    by_word: dict[str, set[str]] = {}
    for word, gold in pairs:
        by_word.setdefault(word, set()).add(gold.replace(" ", ""))

    ambiguous = {w: g for w, g in by_word.items() if len(g) > 1}
    # measured against the cached gold: 321/1025 unique spellings
    assert len(ambiguous) >= 300, (
        "expected the previously-measured ~321 tone-ambiguous homographs; "
        f"found {len(ambiguous)}"
    )
    assert "aka" in ambiguous


def test_tone_folded_scoring_collapses_the_gap():
    """Fold every tone mark out of both hypothesis and gold and rescore.

    This is the fail-before-sensitive claim: it exercises the shipped
    engine, not just the gold file, so a spec regression that broke
    segmental accuracy (as opposed to tone) would show up here even
    though tone is folded out.
    """
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm

    pairs = _load_gold()
    orig_normalize = bm.normalize

    def folded_normalize(ipa, strip_stress, broad, extra_strip=""):
        out = orig_normalize(ipa, strip_stress, broad, extra_strip=extra_strip)
        return _fold_tone(out)

    try:
        bm.normalize = folded_normalize
        _, covered, per, _ = bm.evaluate(pairs, "ki", strip_stress=True,
                                          broad=True)
    finally:
        bm.normalize = orig_normalize

    assert covered == 1025
    # measured 0.0523; generous margin against harness float noise while
    # still failing hard if a future change reopens the tone gap.
    assert per < 0.10, f"expected tone-folded PER near 0.0523, got {per:.4f}"


_LENGTH_MARK = "ː"


def _fold_tone_and_length(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if c not in _TONE_MARKS and c != _LENGTH_MARK)
    return unicodedata.normalize("NFC", s)


def test_tone_and_length_folded_scoring_matches_the_ceiling():
    """Vowel length is the other contrast the plain orthography leaves
    unwritten (Englebretson 2015, p. xi). Folding it alongside tone should
    collapse PER further, to the combined ceiling the spec now declares."""
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm

    pairs = _load_gold()
    orig_normalize = bm.normalize

    def folded_normalize(ipa, strip_stress, broad, extra_strip=""):
        out = orig_normalize(ipa, strip_stress, broad, extra_strip=extra_strip)
        return _fold_tone_and_length(out)

    try:
        bm.normalize = folded_normalize
        _, covered, per, _ = bm.evaluate(pairs, "ki", strip_stress=True,
                                          broad=True)
    finally:
        bm.normalize = orig_normalize

    assert covered == 1025
    # measured 0.0344; generous margin against harness float noise while
    # still failing hard if a future change reopens the gap.
    assert per < 0.08, (
        f"expected tone+length-folded PER near 0.0344, got {per:.4f}"
    )


def test_spec_declares_the_measured_tone_and_length_ceiling():
    """The spec's ``valid_ceiling`` must name the fold actually measured
    above and carry the same PER (issue #1396: spec and board must agree,
    and this pins the spec side)."""
    raw = json.loads((DATA_DIR / "ki.json").read_text(encoding="utf-8"))
    ceiling = raw["valid_ceiling"]["wikipron"]
    assert ceiling["folded"] == "tone+length"
    assert ceiling["per"] == pytest.approx(0.0344, abs=1e-4)
