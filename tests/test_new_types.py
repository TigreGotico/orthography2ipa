"""Tests for Phase 0 type system extensions."""
from orthography2ipa.types import (
    LanguageSpec,
    QualityTier,
    SandhiRule,
    ScriptType,
)


class TestQualityTier:
    def test_enum_values(self):
        assert QualityTier.STUB.value == "stub"
        assert QualityTier.SKELETON.value == "skeleton"
        assert QualityTier.RESEARCH.value == "research"
        assert QualityTier.PRODUCTION.value == "production"

    def test_from_string(self):
        assert QualityTier("stub") == QualityTier.STUB

    def test_is_str(self):
        assert isinstance(QualityTier.STUB, str)


class TestScriptType:
    def test_enum_values(self):
        assert ScriptType.ALPHABET.value == "alphabet"
        assert ScriptType.ABJAD.value == "abjad"
        assert ScriptType.ABUGIDA.value == "abugida"
        assert ScriptType.SYLLABARY.value == "syllabary"
        assert ScriptType.LOGOGRAPHIC.value == "logographic"
        assert ScriptType.FEATURAL.value == "featural"
        assert ScriptType.MIXED.value == "mixed"
        assert ScriptType.RECONSTRUCTION.value == "reconstruction"

    def test_reconstruction_for_proto_languages(self):
        """Proto-languages use RECONSTRUCTION script type."""
        assert ScriptType("reconstruction") == ScriptType.RECONSTRUCTION


class TestSandhiRule:
    def test_frozen(self):
        rule = SandhiRule(
            id="TEST", name="test", left_context="a$",
            right_context="^b", transform="x",
        )
        assert rule.obligatory is True
        assert rule.notes == ""


class TestLanguageSpecNewFields:
    def test_default_quality(self):
        spec = LanguageSpec(
            code="test", name="Test", family="Test", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
        )
        assert spec.quality == QualityTier.RESEARCH

    def test_default_script_type(self):
        spec = LanguageSpec(
            code="test", name="Test", family="Test", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
        )
        assert spec.script_type == ScriptType.ALPHABET

    def test_custom_quality(self):
        spec = LanguageSpec(
            code="test", name="Test", family="Test", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
            quality=QualityTier.PRODUCTION,
        )
        assert spec.quality == QualityTier.PRODUCTION

    def test_quality_from_string(self):
        spec = LanguageSpec(
            code="test", name="Test", family="Test", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
            quality="stub",
        )
        assert spec.quality == QualityTier.STUB

    def test_script_type_from_string(self):
        spec = LanguageSpec(
            code="test", name="Test", family="Test", script="Arabic",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
            script_type="abjad",
        )
        assert spec.script_type == ScriptType.ABJAD

    def test_inherent_vowel_default_none(self):
        spec = LanguageSpec(
            code="test", name="Test", family="Test", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
        )
        assert spec.inherent_vowel is None

    def test_iso639_3_default_none(self):
        spec = LanguageSpec(
            code="test", name="Test", family="Test", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
        )
        assert spec.iso639_3 is None

    def test_sandhi_rules_default_empty(self):
        spec = LanguageSpec(
            code="test", name="Test", family="Test", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
        )
        assert spec.sandhi_rules == ()

    def test_tone_inventory_default_none(self):
        spec = LanguageSpec(
            code="test", name="Test", family="Test", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
        )
        assert spec.tone_inventory is None

    def test_backward_compatibility_existing_specs(self):
        """Existing specs should work with no new fields specified."""
        spec = LanguageSpec(
            code="pt-BR", name="Brazilian Portuguese", family="Romance",
            script="Latin",
            graphemes={"a": ["a"], "lh": ["ʎ"]},
            allophones={"a": ["a"], "ʎ": ["ʎ", "lj"]},
            parent="pt-PT",
        )
        assert spec.quality == QualityTier.RESEARCH
        assert spec.script_type == ScriptType.ALPHABET
        assert spec.inherent_vowel is None
        assert spec.sandhi_rules == ()
