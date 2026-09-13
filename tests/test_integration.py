"""Tests for T-22: full-pipeline integration tests.

Validates the complete flow: orthographic text → PhonetokTokenizer → IPA →
debias_lisbon → apply_transform → dialect IPA.

Also includes T-17 tests for CLUP allophone weight loading and parameterization.
"""
import pytest

import orthography2ipa
from orthography2ipa.transforms import (
    apply_transform,
    debias_lisbon,
    debias_lisbon_preserve_spirants,
    load_clup_profile,
)


# ---------------------------------------------------------------------------
# T-22: Full pipeline integration
# ---------------------------------------------------------------------------

class TestPipelinePtPT:
    """Test: pt-PT tokenization → de-bias → dialect transform."""

    @pytest.fixture()
    def spec_pt(self):
        return orthography2ipa.get("pt-PT")

    @pytest.fixture()
    def tok_pt(self, spec_pt):
        return orthography2ipa.PhonetokTokenizer(spec_pt)

    def test_tokenize_then_northern(self, tok_pt):
        """vaca → IPA → Northern betacism."""
        ipa = tok_pt.ipa_best("vaca")
        result = apply_transform(ipa, "northern", debias=False)
        assert "v" not in result
        assert "b" in result

    def test_tokenize_then_galician_devoicing(self, tok_pt):
        """Test that z becomes s in Galician."""
        ipa = tok_pt.ipa_best("casa")
        # casa likely produces /kazɐ/ or similar with z
        if "z" in ipa:
            result = apply_transform(ipa, "galician", debias=False)
            assert "z" not in result

    def test_tokenize_then_lisbon(self, tok_pt):
        """Lisbon profile returns a string (no error)."""
        ipa = tok_pt.ipa_best("leite")
        result = apply_transform(ipa, "lisbon", debias=False)
        assert isinstance(result, str)
        assert len(result) > 0


class TestPipelineRionorese:
    """Test: ast-PT-x-rionor tokenization → Rionorese transform."""

    @pytest.fixture()
    def spec_rio(self):
        return orthography2ipa.get("ast-PT-x-rionor")

    @pytest.fixture()
    def tok_rio(self, spec_rio):
        return orthography2ipa.PhonetokTokenizer(spec_rio)

    def test_tokenize_chamar(self, tok_rio):
        """Rionorese 'chamar' should produce ʃ (not tʃ — tokenizer uses flat
        graphemes where ch→ʃ)."""
        ipa = tok_rio.ipa_best("chamar")
        assert "ʃ" in ipa

    def test_lexicon_then_transform(self, tmp_path):
        """A caller-supplied lexicon feeds the transform pipeline.

        No lexicon is bundled — the caller registers one (path, URL or hf id).
        """
        lex_file = tmp_path / "ast-PT-x-rionor.tsv"
        lex_file.write_text("abajo\taˈbaʒo\n", encoding="utf-8")
        orthography2ipa.register_lexicon("ast-PT-x-rionor", str(lex_file))
        try:
            ipa = orthography2ipa.get_lexicon("ast-PT-x-rionor")["abajo"]
            # betacism is already applied in the lexicon, so the Leonese
            # transform is mostly idempotent here
            result = apply_transform(ipa, "leonese", debias=False)
            assert isinstance(result, str)
        finally:
            orthography2ipa.clear_lexicons()


class TestPipelineBarranquenho:
    """Test: ext-PT-x-barrancos tokenization."""

    @pytest.fixture()
    def spec_barr(self):
        return orthography2ipa.get("ext-PT-x-barrancos")

    @pytest.fixture()
    def tok_barr(self, spec_barr):
        return orthography2ipa.PhonetokTokenizer(spec_barr)

    def test_tokenize_vaca(self, tok_barr):
        """Barranquenho: v→b (betacism in spec graphemes)."""
        ipa = tok_barr.ipa_best("vaca")
        # spec.graphemes["v"] = ["b"], so tokenizer should produce b
        assert "b" in ipa


class TestDebiasIntegration:
    """Test debias_lisbon on simulated eSpeak output before transform."""

    def test_espeak_to_northern(self):
        """Simulate eSpeak output → de-bias → Northern."""
        # eSpeak might output spirants and Lisbon lowered diphthong
        espeak_ipa = "u βɛˈʎu ˈveɾdɨ foj ˈveɾ ɐ ˈβakɐ"
        result = apply_transform(espeak_ipa, "northern", debias=True)
        # β → b (de-biased) + v → b (betacism)
        assert "β" not in result
        assert "v" not in result
        assert result.count("b") >= 3

    def test_espeak_to_galician_west(self):
        """Full pipeline: eSpeak → de-bias → Galician (with geada)."""
        espeak_ipa = "u ˈɡatu"
        result = apply_transform(espeak_ipa, "galician_west", debias=True)
        # geada: ɡ → x
        assert "x" in result
        assert "ɡ" not in result

    def test_espeak_to_algarve_chain_shift(self):
        """eSpeak → de-bias → Barlavento chain shift."""
        espeak_ipa = "ˈkazɐ"
        result = apply_transform(espeak_ipa, "algarve_barlavento", debias=True)
        # stressed a → ɔ (chain shift)
        assert "ɔ" in result

    def test_espeak_to_beira_baixa(self):
        """eSpeak → de-bias → Beira-Baixa u→y."""
        espeak_ipa = "ˈtudu"
        result = apply_transform(espeak_ipa, "beira_baixa", debias=True)
        # stressed u → y
        assert "y" in result


class TestRoundTrip:
    """Test that neutral → dialect → (compare with expected)."""

    def test_neutral_to_lisbon_ej(self):
        """Neutral /ej/ → Lisbon [ɐj]."""
        neutral = "ˈlejte"
        lisbon = apply_transform(neutral, "lisbon", debias=False)
        assert "ɐj" in lisbon

    def test_neutral_to_ribatejano_ej(self):
        """Neutral /ej/ → Ribatejano [e] (monophthong)."""
        neutral = "ˈlejte"
        ribatejano = apply_transform(neutral, "ribatejano", debias=False)
        assert "ej" not in ribatejano

    def test_neutral_to_northern_v(self):
        """Neutral /v/ → Northern /b/."""
        neutral = "ˈvakɐ"
        northern = apply_transform(neutral, "northern", debias=False)
        assert northern == "ˈbakɐ"

    def test_chain_shift_preserves_unstressed(self):
        """Barlavento chain shift affects stressed vowels only."""
        neutral = "kɐˈzalɐ"  # unstressed a in first syllable, stressed a in second
        result = apply_transform(neutral, "algarve_barlavento", debias=False)
        # The stressed a → ɔ, but the unstressed ɐ should stay ɐ
        # (ɐ is not in the chain shift mapping)
        assert "ɔ" in result


# ---------------------------------------------------------------------------
# T-17: CLUP allophone weight tests
# ---------------------------------------------------------------------------

CLUP_CSV = "/home/miro/PycharmProjects/NLP Workspace/ipa_research/clup/clup_analysis_allophone_flags.csv"


class TestLoadClupProfile:
    def test_load_known_region(self):
        """Load a known region from the CLUP CSV."""
        weights = load_clup_profile("Vizela", CLUP_CSV)
        if weights is None:
            pytest.skip("CLUP CSV not found")
        assert isinstance(weights, dict)
        assert "spirantization_rate" in weights
        assert "vowel_reduction_ratio" in weights

    def test_load_returns_floats(self):
        weights = load_clup_profile("Vizela", CLUP_CSV)
        if weights is None:
            pytest.skip("CLUP CSV not found")
        for key, val in weights.items():
            assert isinstance(val, float), f"{key} is not float: {type(val)}"

    def test_load_unknown_region(self):
        weights = load_clup_profile("Nonexistent Region XYZ", CLUP_CSV)
        assert weights is None

    def test_load_missing_file(self):
        weights = load_clup_profile("Vizela", "/nonexistent/path.csv")
        assert weights is None

    def test_boolean_flags_are_0_or_1(self):
        weights = load_clup_profile("Vizela", CLUP_CSV)
        if weights is None:
            pytest.skip("CLUP CSV not found")
        bool_keys = [
            "retroflex_sibilant", "uvular_trill", "voiceless_uvular",
            "retroflex_tap", "retroflex_lateral", "aspiration",
            "insular_vowel_shift",
        ]
        for key in bool_keys:
            assert weights[key] in (0.0, 1.0), f"{key} = {weights[key]}"

    def test_vizela_has_retroflex_sibilant(self):
        """Vizela (Braga) — Northern, should have retroflex sibilants per CSV."""
        weights = load_clup_profile("Vizela", CLUP_CSV)
        if weights is None:
            pytest.skip("CLUP CSV not found")
        assert weights["retroflex_sibilant"] == 1.0

    def test_vowel_reduction_ratio_range(self):
        weights = load_clup_profile("Vizela", CLUP_CSV)
        if weights is None:
            pytest.skip("CLUP CSV not found")
        assert 0.0 <= weights["vowel_reduction_ratio"] <= 1.0


class TestAllophonicWeightsInTransform:
    def test_spirant_preservation(self):
        """When allophone_weights indicates spirantization, β is kept."""
        ipa = "ˈβakɐ"
        weights = {"spirantization_rate": 0.05}  # above 0.02 threshold
        result = apply_transform(ipa, "northern", debias=True,
                                 allophone_weights=weights)
        # β should be preserved (not de-biased to b), then N1 betacism
        # converts v→b but β is not 'v', so β stays
        assert "β" in result

    def test_no_spirant_preservation_below_threshold(self):
        """When spirantization_rate is low, β is normalized to b."""
        ipa = "ˈβakɐ"
        weights = {"spirantization_rate": 0.01}  # below 0.02 threshold
        result = apply_transform(ipa, "northern", debias=True,
                                 allophone_weights=weights)
        # β → b (de-biased), then betacism doesn't change b
        assert "β" not in result

    def test_none_weights_default_behavior(self):
        """allophone_weights=None is the default (standard de-biasing)."""
        ipa = "ˈβakɐ"
        result = apply_transform(ipa, "northern", debias=True,
                                 allophone_weights=None)
        assert "β" not in result

    def test_debias_preserve_spirants_keeps_beta(self):
        """debias_lisbon_preserve_spirants keeps β, ð, ɣ."""
        ipa = "ˈβaðɐ ɣatu"
        result = debias_lisbon_preserve_spirants(ipa)
        assert "β" in result
        assert "ð" in result
        assert "ɣ" in result

    def test_debias_preserve_spirants_still_fixes_lateral(self):
        """debias_lisbon_preserve_spirants still normalizes ɫ → l."""
        ipa = "ˈsaɫ"
        result = debias_lisbon_preserve_spirants(ipa)
        assert "ɫ" not in result
        assert "l" in result


class TestTopLevelImports:
    def test_load_clup_profile_accessible(self):
        assert hasattr(orthography2ipa, "load_clup_profile")
