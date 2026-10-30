"""Cited-claim tests for the Gawri (``gwc``) tone ceiling.

Gawri has five contrastive tones, and its 1995 Perso-Arabic spelling makes
tone diacritics available but leaves them off most words (Baart & Sagar,
"The Gawri Language of Kalam and Dir Kohistan", p. 7 and p. 10, quoted in
``gwc.json``'s ``valid_ceiling`` citation). The gwc/wikipron gold marks tone
with acute, grave, circumflex and caron accents on the vowel; the spelling
column carries none of them.

These tests pin the measurement behind ``valid_ceiling.wikipron``: with tone
folded out of both hypothesis and gold, the row drops from 0.4170 to 0.2626.
The ceiling stays above 0.25, so the row is not declared input-limited; the
remaining gap is segmental. Vowel length is not folded, because the same
source says Jazm marks shortness where necessary.
"""
from __future__ import annotations

import json
import pathlib
import sys
import unicodedata

import pytest

DATA_DIR = (pathlib.Path(__file__).parent.parent
            / "orthography2ipa" / "data")

_TONE_MARKS = {"̀", "́", "̂", "̌"}  # grave, acute, circumflex, caron


def _fold_tone(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if c not in _TONE_MARKS)
    return unicodedata.normalize("NFC", s)


def _benchmark():
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm
    return bm


def _evaluate(fold=None):
    bm = _benchmark()
    pairs = bm.load_wikipron("gwc", 10 ** 9)
    if not pairs:
        pytest.skip("gwc wikipron gold not available")
    orig_normalize = bm.normalize

    def folded_normalize(ipa, strip_stress, broad, extra_strip=""):
        out = orig_normalize(ipa, strip_stress, broad, extra_strip=extra_strip)
        return fold(out)

    try:
        if fold is not None:
            bm.normalize = folded_normalize
        _, covered, per, _ = bm.evaluate(pairs, "gwc", strip_stress=True,
                                          broad=True)
    finally:
        bm.normalize = orig_normalize
    return covered, per


def test_spec_declares_the_measured_tone_ceiling():
    """The spec's ``valid_ceiling`` names the fold measured below and carries
    the same PER, so spec and board agree."""
    raw = json.loads((DATA_DIR / "gwc.json").read_text(encoding="utf-8"))
    ceiling = raw["valid_ceiling"]["wikipron"]
    assert ceiling["folded"] == "tone"
    assert ceiling["per"] == pytest.approx(0.2626, abs=1e-4)
    assert "on most words the tone marks would not need to be used" in (
        ceiling["citation"])
    assert raw["audit"]["wikipron"]["conclusion"] == "input_limited"


def test_gold_marks_tone_that_the_spelling_does_not():
    bm = _benchmark()
    pairs = bm.load_wikipron("gwc", 10 ** 9)
    if not pairs:
        pytest.skip("gwc wikipron gold not available")
    toned = sum(1 for _w, g in pairs
                if any(c in _TONE_MARKS
                       for c in unicodedata.normalize("NFD", g)))
    spelled = sum(1 for w, _g in pairs
                  if any(c in _TONE_MARKS
                         for c in unicodedata.normalize("NFD", w)))
    # measured against the cached gold: 204 of 208 pairs carry a tone mark
    assert toned >= 200
    assert spelled == 0


def test_tone_folded_scoring_matches_the_ceiling():
    """Fold tone out of both sides and rescore through the harness. This runs
    the shipped engine, so a segmental regression shows up here even with
    tone folded out."""
    covered, raw_per = _evaluate()
    assert covered == 165
    # measured 0.4170 as scored
    assert raw_per > 0.35

    covered, per = _evaluate(_fold_tone)
    assert covered == 165
    # measured 0.2626; the margin allows harness float noise and still fails
    # if a change reopens the tone gap or breaks the segments.
    assert 0.20 < per < 0.30, (
        f"expected tone-folded PER near 0.2626, got {per:.4f}")
