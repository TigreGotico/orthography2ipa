"""Tests for the declarative stress system.

Validates:
- StressRules schema round-trip through json_loader and pydantic
- detect_stress precedence: marked vowels > oxytone endings >
  penult endings > default position
- Portuguese gold stress placements on pt-PT/pt-BR seed data
- apply_stress_mark insertion (orthographic and end-anchored indices)
- Specs without a stress block are unaffected
"""
import pytest

from orthography2ipa import get
from orthography2ipa.schema import StressRulesModel
from orthography2ipa.stress import apply_stress_mark, detect_stress, syllabify
from orthography2ipa.types import StressRules


class TestSchema:
    def test_pt_specs_carry_stress(self):
        for code in ("pt-PT", "pt-BR"):
            rules = get(code).stress
            assert isinstance(rules, StressRules)
            assert rules.default_position == -2
            assert "r" in rules.final_stress_endings
            assert "á" in rules.marked_vowels
            assert rules.stress_mark == "ˈ"

    def test_specs_without_stress_are_none(self):
        assert get("en-GB").stress is None
        assert get("ar").stress is None

    def test_pydantic_model_validates(self):
        model = StressRulesModel(
            default_position=-1,
            final_stress_endings=["r"],
            marked_vowels=["á"],
        )
        assert model.default_position == -1

    def test_pydantic_rejects_bad_position(self):
        with pytest.raises(Exception):
            StressRulesModel(default_position=2)

    def test_pydantic_rejects_empty_entries(self):
        with pytest.raises(Exception):
            StressRulesModel(final_stress_endings=[""])


class TestSyllabify:
    @pytest.mark.parametrize("word,count", [
        ("casa", 2), ("falar", 2), ("abacaxi", 4), ("sol", 1),
        ("lâmpada", 3), ("médico", 3), ("", 0),
    ])
    def test_counts(self, word, count):
        assert len(syllabify(word)) == count

    def test_round_trip(self):
        for word in ("casa", "falar", "abacaxi", "lâmpada", "atuns"):
            assert "".join(syllabify(word)) == word


class TestDetectStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("pt-PT").stress

    @pytest.mark.parametrize("word,expected", [
        # paroxytone default
        ("casa", 0), ("livro", 0), ("homem", 0), ("falam", 0),
        ("rapazes", 1),
        # hiatus 'ia' counts as one nucleus for the naive syllabifier;
        # the stressed vowel still falls inside the returned syllable
        ("viagem", 0),
        # oxytone endings
        ("falar", 1), ("azul", 1), ("rapaz", 1), ("jardim", 1),
        ("caju", 1), ("abacaxi", 3), ("atuns", 1),
        # written accents win
        ("médico", 0), ("lâmpada", 0), ("café", 1), ("túnel", 0),
        ("órgão", 0), ("manhã", 1), ("amável", 1),
        # monosyllables inherently stressed
        ("sol", 0), ("pé", 0),
    ])
    def test_portuguese_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected

    def test_explicit_syllables_override(self, rules):
        assert detect_stress("falar", rules, syllables=["fa", "lar"]) == 1

    def test_penult_endings(self):
        rules = StressRules(default_position=-1,
                            penult_stress_endings=("os",))
        assert detect_stress("santos", rules) == 0
        assert detect_stress("santo", rules) == 1

    def test_default_clamped_on_short_words(self):
        rules = StressRules(default_position=-3)
        assert detect_stress("casa", rules) == 0


class TestApplyStressMark:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("pt-PT").stress

    def test_end_anchored_index(self, rules):
        assert apply_stress_mark("fɐlaɾ", rules, -1) == "fɐˈlaɾ"
        assert apply_stress_mark("kazɐ", rules, -2) == "ˈkazɐ"

    def test_orthographic_index_converted(self, rules):
        assert apply_stress_mark(
            "kazɐ", rules, 0, syllables=["ca", "sa"]) == "ˈkazɐ"
        assert apply_stress_mark(
            "fɐlaɾ", rules, 1, syllables=["fa", "lar"]) == "fɐˈlaɾ"

    def test_already_marked_unchanged(self, rules):
        assert apply_stress_mark("fɐˈlaɾ", rules, -1) == "fɐˈlaɾ"

    def test_empty_input(self, rules):
        assert apply_stress_mark("", rules, -1) == ""
