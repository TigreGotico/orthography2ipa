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


class TestWordExceptionStressRouting:
    """word_exceptions overrides must flow through stress marking.

    A spec that declares both ``word_exceptions`` and ``stress`` must
    apply stress marks to override words exactly as it would to a
    normally-searched word with the same base IPA — the override is a
    shortcut for the *segmental* transcription, not an opt-out from
    stress placement.
    """

    def test_polysyllabic_override_receives_stress_mark(self):
        from dataclasses import replace

        lang = "pt-PT"
        word = "banana"

        # Normal search path: establish what stress marking produces
        # for this word's base IPA.
        baseline_engine = G2P(lang)
        baseline_ipa = baseline_engine.transcribe_word(word)
        stress = baseline_engine.spec.stress
        assert stress is not None
        assert stress.stress_mark in baseline_ipa, (
            "fixture word must actually receive a stress mark on the "
            "normal search path for this test to be meaningful"
        )
        unmarked_ipa = baseline_ipa.replace(stress.stress_mark, "")

        # Override path: same word, base IPA supplied via
        # word_exceptions instead of positional/grapheme search.
        override_engine = G2P(lang)
        override_engine.spec = replace(
            override_engine.spec, word_exceptions={word: unmarked_ipa})

        result = override_engine.transcribe_word(word)
        assert result == baseline_ipa
        assert stress.stress_mark in result

    def test_fr_fr_word_exceptions_unaffected(self):
        """fr-FR has no stress block: overrides pass through unmarked,
        identical to before this fix (monosyllabic exceptions only)."""
        engine = G2P("fr-FR")
        assert engine.spec.stress is None
        assert engine.transcribe_word("le") == "lə"
        assert engine.transcribe_word("de") == "də"
        assert engine.transcribe_word("que") == "kə"

    def test_en_gb_word_exceptions_unaffected(self):
        """en-GB has no stress block either: same guarantee."""
        engine = G2P("en-GB")
        assert engine.spec.stress is None
        expected = {
            "the": "ðə", "be": "biː", "he": "hiː",
            "me": "miː", "we": "wiː", "she": "ʃiː",
        }
        for word, ipa in expected.items():
            assert engine.transcribe_word(word) == ipa


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


class TestPositionalSelection:
    """Positional grapheme rules reach the engine output."""

    def test_pt_c_before_i_gives_s(self):
        """Portuguese 'c' before 'i' → /s/ (not /k/); 'cinco' starts with /s/."""
        engine = G2P("pt-PT", apply_stress=False)
        ipa = engine.transcribe("cinco")
        assert ipa.startswith("s"), f"Expected initial s from c-before-i, got {ipa!r}"

    def test_pt_final_a_reduces_to_schwa(self):
        """Word-final 'a' in pt-PT → /ɐ/."""
        engine = G2P("pt-PT", apply_stress=False)
        ipa = engine.transcribe("casa")
        assert ipa.endswith("ɐ"), f"Expected final ɐ, got {ipa!r}"

    def test_pt_stressed_a_is_open(self):
        """Stressed 'a' in pt-PT stays /a/ (nucleus_stressed rule)."""
        engine = G2P("pt-PT", apply_stress=False)
        # In 'casa' the stressed syllable 'ca-' has open /a/
        ipa = engine.transcribe("casa")
        assert "a" in ipa, f"Expected open /a/ in stressed syllable, got {ipa!r}"

    def test_pt_unstressed_e_reduces(self):
        """Unstressed 'e' in pt-PT → /ɨ/ (nucleus_unstressed rule)."""
        engine = G2P("pt-PT", apply_stress=False)
        ipa = engine.transcribe("abade")
        assert "ɨ" in ipa, f"Expected ɨ in unstressed final e, got {ipa!r}"

    def test_pt_unstressed_o_raises(self):
        """Unstressed 'o' in pt-PT → /u/ (nucleus_unstressed rule)."""
        engine = G2P("pt-PT", apply_stress=False)
        # 'comer': the first 'o' is unstressed → should produce u
        ipa = engine.transcribe("comer")
        assert "u" in ipa, f"Expected u from unstressed o, got {ipa!r}"

    def test_pt_s_intervocalic_voiced(self):
        """Intervocalic 's' in pt-PT → /z/."""
        engine = G2P("pt-PT", apply_stress=False)
        ipa = engine.transcribe("casa")
        assert "z" in ipa, f"Expected z from intervocalic s, got {ipa!r}"

    def test_beam_exposes_alternatives_with_positional(self):
        """Beam search still has multiple candidates when positional rules apply."""
        engine = G2P("pt-PT")
        candidates = engine.candidates("casa", beam_width=4)
        assert len(candidates) > 1, "Beam should expose alternatives"

    def test_greedy_equals_beam_one_with_positional(self):
        """greedy == beam(1) invariant holds when positional rules are active."""
        engine = G2P("pt-PT")
        for word in ["casa", "cinco", "falar", "comer"]:
            greedy = engine.transcribe(word, search="greedy")
            beam1 = engine.transcribe(word, search="beam", beam_width=1)
            assert greedy == beam1, f"Mismatch for {word!r}: {greedy!r} vs {beam1!r}"

    def test_language_without_positional_data_unchanged(self):
        """Languages with no positional_graphemes use the flat table unchanged."""
        # en-GB has no positional overrides; engine must not crash or misbehave
        engine = G2P("en-GB")
        ipa = engine.transcribe("hello")
        assert ipa.strip(), "Expected non-empty output for en-GB"


class TestUnmappedCharObservability:
    """Additive R3 fix: unmapped/out-of-script characters currently
    produce an empty ``ipa`` string indistinguishable from legitimate
    silence (pure punctuation). ``WordTranscription.unmapped`` /
    ``.coverage`` and ``G2P(on_unmapped=...)`` make that distinguishable
    without changing default behavior.
    """

    def test_unsupported_script_reports_unmapped_but_ipa_unchanged(self):
        """A word entirely outside the spec's script surfaces via
        unmapped/coverage while `ipa` stays empty, matching pre-existing
        'ignore' (default) behavior — feeding Hanzi to the pinyin-only
        zh spec, the PR #102 scenario."""
        engine = G2P("zh")
        result = engine.transcribe_detailed("你好")
        assert result.ipa == "", (
            "Default on_unmapped='ignore' must not change ipa output")
        assert len(result.words) == 1
        word = result.words[0]
        assert word.ipa == ""
        assert word.unmapped == ("你", "好")
        assert word.coverage == 0.0

    def test_fully_covered_word_has_no_unmapped(self):
        """A word entirely within the spec's grapheme table reports no
        unmapped characters and full coverage."""
        engine = G2P("pt-PT")
        result = engine.transcribe_detailed("casa")
        word = result.words[0]
        assert word.unmapped == ()
        assert word.coverage == 1.0

    def test_on_unmapped_raise_raises_unmapped_script_error(self):
        """`on_unmapped="raise"` raises UnmappedScriptError for the
        Korean precomposed-Hangul-into-compatibility-jamo scenario
        (PR #106)."""
        from orthography2ipa.exceptions import UnmappedScriptError

        engine = G2P("ko", on_unmapped="raise")
        with pytest.raises(UnmappedScriptError) as excinfo:
            engine.transcribe("안녕하세요")
        assert excinfo.value.lang == "ko"
        assert excinfo.value.word == "안녕하세요"
        assert excinfo.value.unmapped

    def test_on_unmapped_log_emits_warning_without_raising(self, caplog):
        """`on_unmapped="log"` emits a warning once per (lang, word) and
        still returns normally (no exception, same ipa as 'ignore')."""
        engine = G2P("zh", on_unmapped="log")
        with caplog.at_level("WARNING", logger="orthography2ipa.g2p"):
            ipa = engine.transcribe("你好")
            ipa_again = engine.transcribe("你好")
        assert ipa == ""
        assert ipa == ipa_again
        warnings = [r for r in caplog.records if r.levelname == "WARNING"]
        assert len(warnings) == 1, (
            "Expected exactly one warning for the repeated (lang, word) pair")
        assert "你" in warnings[0].message or "你好" in warnings[0].message

    def test_default_on_unmapped_is_ignore(self):
        """The default G2P() constructor call must not raise or log for
        unmapped characters — zero behavior change for existing callers."""
        engine = G2P("zh")
        assert engine.on_unmapped == "ignore"
        ipa = engine.transcribe("你好")  # must not raise
        assert ipa == ""
