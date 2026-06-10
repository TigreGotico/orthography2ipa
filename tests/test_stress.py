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


class TestSyllabifierPlugins:
    """Per-language syllabifier plugins supersede the naive splitter."""

    class _FakeSyllabifier:
        def syllabify(self, word, lang=None):
            # hiatus-aware: the naive splitter cannot separate 'i-a'
            if word == "viagem":
                return ["vi", "a", "gem"]
            return [word]

        @property
        def language_codes(self):
            return ["pt-PT"]

        @property
        def priority(self):
            return 50

    def _install(self, monkeypatch):
        from orthography2ipa import registry
        monkeypatch.setattr(
            registry, "_syllabifiers", {"pt-PT": self._FakeSyllabifier()})

    def test_plugin_used_for_lang(self, monkeypatch):
        from orthography2ipa import get
        self._install(monkeypatch)
        rules = get("pt-PT").stress
        # with the hiatus-aware plugin, viagem is correctly paroxytone
        # over three syllables (vi-A-gem)
        assert detect_stress("viagem", rules, lang="pt-PT") == 1

    def test_no_plugin_falls_back_to_naive(self, monkeypatch):
        from orthography2ipa import get
        self._install(monkeypatch)
        rules = get("pt-PT").stress
        assert detect_stress("viagem", rules, lang="en-GB") == 0

    def test_explicit_syllables_beat_plugin(self, monkeypatch):
        from orthography2ipa import get
        self._install(monkeypatch)
        rules = get("pt-PT").stress
        assert detect_stress(
            "viagem", rules, syllables=["via", "gem"], lang="pt-PT") == 0

    def test_get_syllabifier_unknown_lang(self):
        from orthography2ipa import get_syllabifier
        assert get_syllabifier("zz-ZZ") is None

    def test_broken_plugin_output_rejected(self, monkeypatch):
        """A plugin whose syllables don't rebuild the word is ignored."""
        from orthography2ipa import get, registry

        class Broken:
            def syllabify(self, word, lang=None):
                return ["xxx"]

            @property
            def language_codes(self):
                return ["pt-PT"]

            @property
            def priority(self):
                return 50

        monkeypatch.setattr(registry, "_syllabifiers", {"pt-PT": Broken()})
        rules = get("pt-PT").stress
        # falls back to the naive splitter instead of trusting garbage
        assert detect_stress("casa", rules, lang="pt-PT") == 0


class TestGalicianStress:
    """Gold stress placements for Galician (gl) — Cotovia/GTM rules."""

    @pytest.fixture(scope="class")
    def rules(self):
        return get("gl").stress

    def test_gl_carries_stress_block(self, rules):
        assert rules is not None
        assert rules.default_position == -2
        assert rules.stress_mark == "ˈ"

    @pytest.mark.parametrize("word,expected", [
        # paroxytone default (vowel-final)
        ("casa",   0),   # ca-sa → syll 0
        ("galego", 1),   # ga-le-go → syll 1 (middle)
        # penult_stress_endings: -n and -s stay paroxytone
        ("casas",  0),   # ca-sas → syll 0
        ("cantan", 0),   # ca-ntan → syll 0
        # oxytone endings
        ("falar",  1),   # fa-lar → final
        ("azul",   1),   # a-zul → final
        ("rapaz",  1),   # ra-paz → final
        # written accent overrides
        ("café",   1),   # ca-fé → accent on last
        ("médico", 0),   # mé-di-co → accent on first
        ("nación", 1),   # na-ción → accent on last
    ])
    def test_galician_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestMirandeseStress:
    """Gold stress placements for Mirandese (mwl).

    Convenção Ortográfica da Língua Mirandesa (1999): Portuguese-based
    accentuation, but Mirandese orthography writes final nasals with -n
    (Asturleonese trait: camin, naçon, un) and has word-final ⟨ç⟩
    (rapaç, lhuç) where Portuguese writes -z.
    """

    @pytest.fixture(scope="class")
    def rules(self):
        return get("mwl").stress

    def test_mwl_carries_stress_block(self, rules):
        assert rules is not None
        assert rules.default_position == -2
        assert "á" in rules.marked_vowels
        assert "r" in rules.final_stress_endings
        # Mirandese nasal endings are -n, never the Portuguese -m
        assert "in" in rules.final_stress_endings
        assert "on" in rules.final_stress_endings
        assert "im" not in rules.final_stress_endings
        assert "um" not in rules.final_stress_endings

    def test_mwl_j_is_postalveolar(self):
        """Mirandese ⟨j⟩ is /ʒ/ (western Iberian), never the Asturian ʝ."""
        spec = get("mwl")
        assert spec.graphemes["j"] == ["ʒ"], (
            f"mwl j should be ʒ; got {spec.graphemes['j']}"
        )

    def test_mwl_cedilla_is_voiceless_laminal(self):
        """Mirandese keeps the six-sibilant contrast (apical s̺/z̺,
        laminal s̻/z̻, postalveolar ʃ/ʒ): ⟨ç⟩ is the voiceless laminal
        fricative /s̻/ — not the Asturian affricate t͡s, and not the
        voiced z̻, which is the value of ⟨z⟩."""
        spec = get("mwl")
        assert spec.graphemes["ç"] == ["s̻"], (
            f"mwl ç should be s̻; got {spec.graphemes['ç']}"
        )

    @pytest.mark.parametrize("word,expected", [
        # paroxytone default (vowel-final)
        ("casa",     0),   # ca-sa → syll 0
        ("lhéngua",  0),   # lhé-ngua → accent on first
        # oxytone endings: consonant-final, incl. word-final ç
        ("falar",    1),   # fa-lar → final
        ("rapaç",    1),   # ra-paç → final (Mirandese -ç where pt has -z)
        # final nasals written -n (Asturleonese), not -m
        ("camin",    1),   # ca-min → -in oxytone
        ("naçon",    1),   # na-çon → -on (< Lat. -ōnem) oxytone
        # written accents win
        ("mirandés", 2),   # mi-ra-ndés (3 sylls) → accent on last
        # tilde vowel as accent-bearer
        ("irmã",     1),   # ir-mã → accent on last (ã in marked_vowels)
    ])
    def test_mirandese_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestBarranquenhoStress:
    """Gold stress placements for Barranquenho (ext-PT-x-barrancos)."""

    @pytest.fixture(scope="class")
    def rules(self):
        return get("ext-PT-x-barrancos").stress

    def test_barrancos_carries_stress_block(self, rules):
        assert rules is not None
        assert rules.default_position == -2
        assert "á" in rules.marked_vowels
        assert "r" in rules.final_stress_endings

    @pytest.mark.parametrize("word,expected", [
        # paroxytone default (vowel-final)
        ("casa",   0),   # ca-sa → syll 0
        ("casas",  0),   # ca-sas → vowel+s penult (not in final_stress_endings)
        # unmarked -em/-am stay paroxytone, as in Portuguese norms
        ("homem",  0),   # ho-mem → penult
        ("falam",  0),   # fa-lam → penult
        # oxytone endings
        ("falar",  1),   # fa-lar → final
        ("caju",   1),   # ca-ju → -u oxytone
        # written accent overrides
        ("café",   1),   # ca-fé → accent on last
        ("médico", 0),   # mé-di-co → accent on first
    ])
    def test_barranquenho_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected
