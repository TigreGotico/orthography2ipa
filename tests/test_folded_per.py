"""The folded-PER helper, checked against arithmetic done by hand.

Every expected number here is derived on paper from the definition —
fold the segments out of BOTH sides, take the character-level edit
distance, divide by the folded gold length, average over covered words —
and never read back out of the helper.

The distinction this file defends is the one the Arabic specs kept
losing: the omission score folds the HYPOTHESIS only and needs no
engine, while the folded PER folds both sides and needs the spec's own
output. Numbers from one are not numbers from the other.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import pytest  # noqa: E402

import folded_per as fp  # noqa: E402

SHORT_VOWELS = ("a", "i", "u")


class _Spec:
    """A stand-in engine returning a fixed reading per word."""

    def __init__(self, lang, **kwargs):
        self.readings = _Spec.readings

    def transcribe_word(self, word):
        return self.readings[word]

    transcribe = transcribe_word


@pytest.fixture
def engine(monkeypatch):
    def install(readings):
        _Spec.readings = readings
        import orthography2ipa
        monkeypatch.setattr(orthography2ipa, "G2P", _Spec, raising=False)
    return install


class TestFoldedPer:
    def test_a_spec_that_matches_the_gold_scores_zero(self, engine):
        engine({"ktb": "kataba"})
        res = fp.folded_per([("ktb", "kataba")], "ar", SHORT_VOWELS)
        assert res.score == 0.0
        assert res.covered == 1

    def test_a_consonant_error_survives_the_fold(self, engine):
        # gold kataba -> ktb, hypothesis kaTaba -> kTb: one substitution
        # over a folded gold of length 3.
        engine({"ktb": "kaTaba"})
        res = fp.folded_per([("ktb", "kataba")], "ar", SHORT_VOWELS)
        assert res.score == pytest.approx(1 / 3)

    def test_a_vowel_only_error_is_folded_away(self, engine):
        # Both sides lose every short vowel, so guessing them wrong
        # cannot cost anything. This is the whole point of the measure,
        # and it is what separates it from the omission score.
        engine({"ktb": "kutibu"})
        res = fp.folded_per([("ktb", "kataba")], "ar", SHORT_VOWELS)
        assert res.score == 0.0

    def test_it_folds_the_reference_too(self, engine):
        # Folding only the hypothesis would leave the gold at length 6
        # and score 3/6; folding both sides scores 0. A helper that
        # forgot the reference passes every test above and fails here.
        engine({"ktb": "kataba"})
        res = fp.folded_per([("ktb", "kataba")], "ar", SHORT_VOWELS)
        assert res.score != pytest.approx(0.5)
        assert res.gold_chars == 3
        assert res.removed_chars == 3

    def test_a_word_scores_against_the_kindest_gold(self, engine):
        # Two golds, one reachable. The scorer credits the better, so
        # this helper must too.
        engine({"ktb": "katiba"})
        res = fp.folded_per(
            [("ktb", "kataba"), ("ktb", "katiba")], "ar", SHORT_VOWELS)
        assert res.score == 0.0
        assert res.words == 1

    def test_an_empty_reading_is_not_counted_as_covered(self, engine):
        engine({"ktb": ""})
        res = fp.folded_per([("ktb", "kataba")], "ar", SHORT_VOWELS)
        assert res.covered == 0
        assert res.score == 0.0
