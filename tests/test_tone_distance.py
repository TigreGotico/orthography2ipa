"""Tests for tone and orthographic distance."""
from orthography2ipa.distance import orthographic_distance, tone_distance
from orthography2ipa.types import LanguageSpec


def _make_spec(code, script="Latin", tone_inventory=None):
    return LanguageSpec(
        code=code, name=code, family="Test", script=script,
        graphemes={"a": ["a"]}, allophones={"a": ["a"]},
        tone_inventory=tone_inventory,
    )


class TestToneDistance:
    def test_both_non_tonal(self):
        a = _make_spec("a")
        b = _make_spec("b")
        assert tone_distance(a, b) == 0.0

    def test_one_tonal_one_not(self):
        a = _make_spec("a", tone_inventory={"˥": "high"})
        b = _make_spec("b")
        assert tone_distance(a, b) == 1.0

    def test_identical_tones(self):
        inv = {"˥": "high", "˩": "low"}
        a = _make_spec("a", tone_inventory=inv)
        b = _make_spec("b", tone_inventory=inv)
        assert tone_distance(a, b) == 0.0

    def test_partial_overlap(self):
        a = _make_spec("a", tone_inventory={"˥": "high", "˩": "low"})
        b = _make_spec("b", tone_inventory={"˥": "high", "˧": "mid"})
        d = tone_distance(a, b)
        assert 0.0 < d < 1.0


class TestOrthographicDistance:
    def test_same_script(self):
        a = _make_spec("a", script="Latin")
        b = _make_spec("b", script="Latin")
        d = orthographic_distance(a, b)
        assert 0.0 <= d <= 1.0

    def test_different_scripts(self):
        a = _make_spec("a", script="Latin")
        b = _make_spec("b", script="Arabic")
        d = orthographic_distance(a, b)
        assert d > 0.0
