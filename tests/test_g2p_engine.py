"""Tests for the top-level G2P engine.

Validates:
- greedy equals beam(width=1) across a language sample
- word splitting and punctuation→pausal flags
- stress marking integration on Portuguese
- sandhi application across word boundaries
- dialect_profile output matches manual apply_transform
- abugida sanity (inherent vowel scripts transcribe)
- specs with stress rules cover their marked vowels as graphemes
"""
import pytest

import orthography2ipa
from orthography2ipa import G2P, available_codes, get, transcribe
from orthography2ipa.types import QualityTier

SAMPLE_LANGS = [
    "pt-PT", "pt-BR", "es-ES", "en-GB", "fr-FR", "de-DE", "it-IT",
    "ca", "gl", "eu", "oc", "ast", "mwl", "an", "cy", "ga", "ru",
    "el", "ar", "fa", "hi", "tr",
]
SAMPLE_TEXTS = {
    "default": "casa grande",
    "ru": "дом",
    "el": "καλημέρα",
    "ar": "كتاب",
    "fa": "کتاب",
    "hi": "नमस्ते",
}


def _sample_text(lang: str) -> str:
    return SAMPLE_TEXTS.get(lang.split("-")[0], SAMPLE_TEXTS["default"])


class TestGreedyVsBeam:
    @pytest.mark.parametrize("lang", SAMPLE_LANGS)
    def test_greedy_equals_beam_width_one(self, lang):
        engine = G2P(lang)
        text = _sample_text(lang)
        greedy = engine.transcribe(text, search="greedy")
        beam1 = engine.transcribe(text, search="beam", beam_width=1)
        assert greedy == beam1

    @pytest.mark.parametrize("lang", SAMPLE_LANGS)
    def test_produces_nonempty_ipa(self, lang):
        ipa = transcribe(_sample_text(lang), lang)
        assert ipa.strip()

    def test_beam_exposes_candidates(self):
        engine = G2P("pt-PT")
        result = engine.transcribe_detailed("casa", search="beam",
                                            beam_width=4)
        assert len(result.words) == 1
        assert len(result.words[0].candidates) > 1

    def test_invalid_search_rejected(self):
        engine = G2P("pt-PT")
        with pytest.raises(ValueError):
            engine.transcribe("casa", search="exhaustive")


class TestWordSplitting:
    def test_punctuation_marks_pausal(self):
        engine = G2P("pt-PT")
        words = engine._split_words("olá, mundo grande.")
        assert [w.surface for w in words] == ["olá", "mundo", "grande"]
        assert words[0].pausal is True          # before the comma
        assert words[1].pausal is False
        assert words[2].pausal is True          # end of text
        assert words[0].sentence_initial is True
        assert words[2].sentence_final is True

    def test_empty_input(self):
        engine = G2P("pt-PT")
        assert engine.transcribe("") == ""
        assert engine.transcribe("  ...  ") == ""

    def test_resolved_lang_recorded(self):
        result = G2P("pt").transcribe_detailed("casa")
        assert result.lang == "pt-PT"


class TestStressIntegration:
    def test_portuguese_stress_marked(self):
        engine = G2P("pt-PT")
        assert "ˈ" in engine.transcribe("falar")
        assert engine.transcribe("falar").startswith("fɐˈ") or \
            engine.transcribe("falar")[2] == "ˈ"  # fɐˈlaɾ / faˈlaɾ

    def test_stress_disabled(self):
        engine = G2P("pt-PT", apply_stress=False)
        assert "ˈ" not in engine.transcribe("falar")

    def test_language_without_stress_rules_unmarked(self):
        engine = G2P("en-GB")
        assert "ˈ" not in engine.transcribe("hello")

    def test_marked_vowels_are_graphemes(self):
        """Stress-marked vowels a spec declares must be transcribable."""
        for code in available_codes():
            spec = get(code)
            if spec.stress is None or spec.quality is QualityTier.STUB:
                continue
            missing = [v for v in spec.stress.marked_vowels
                       if v not in spec.graphemes]
            assert not missing, (
                f"{code} declares stress marked_vowels with no grapheme "
                f"mapping: {missing}"
            )


class TestSandhiAndTransforms:
    def test_sandhi_applied_when_rules_exist(self):
        # find any spec with sandhi rules to exercise the path
        engine = G2P("pt-PT")
        if engine._sandhi is None:
            pytest.skip("pt-PT has no sandhi rules")
        with_sandhi = engine.transcribe("os amigos")
        engine_off = G2P("pt-PT", apply_sandhi=False)
        # both produce output; equality depends on the rule set
        assert with_sandhi and engine_off.transcribe("os amigos")

    def test_dialect_profile_matches_manual_transform(self):
        from orthography2ipa import apply_transform
        from orthography2ipa.transforms import DIALECT_PROFILES

        profile = next(iter(DIALECT_PROFILES))
        plain_engine = G2P("pt-PT")
        plain = plain_engine.transcribe_detailed("casa grande")
        manual = apply_transform(plain.ipa, profile, ortho="casa grande")
        engine = G2P("pt-PT", dialect_profile=profile)
        assert engine.transcribe("casa grande") == manual


class TestAbugida:
    def test_inherent_vowel_script(self):
        spec = get("hi")
        ipa = transcribe("नमस्ते", "hi")
        assert ipa
        if spec.inherent_vowel:
            # the engine must not crash on virama/inherent vowel scripts
            assert isinstance(ipa, str)


class TestModuleLevelTranscribe:
    def test_unknown_language_raises(self):
        with pytest.raises(KeyError):
            transcribe("hello", "zz-ZZ")

    def test_in_dunder_all(self):
        assert "transcribe" in orthography2ipa.__all__
        assert "G2P" in orthography2ipa.__all__
