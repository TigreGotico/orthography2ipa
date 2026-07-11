"""Regression tests for:
- ast-PT-x-guadramil (Guadramilese) — T-08
- ext-PT-x-barrancos (Barranquenho)  — T-09

Guadramilese is phonologically identical to Rionorese (inherits all rules via
graphemes_base). Tests verify registry loading and that Rionorese phonological
rules are correctly inherited, then check documented isoglosses from Paper III.

Barranquenho is Portuguese-based with Spanish adstrate influence. Tests verify
key overrides: betacism (v→b), aspirated h, alveolar rhotics, tch trigraph.
"""
import pytest

import orthography2ipa
from orthography2ipa.types import GraphemePosition
from orthography2ipa.phonetok import PhonetokTokenizer


# ═══════════════════════════════════════════════════════════════════════════
# Guadramilese (ast-PT-x-guadramil)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.fixture(scope="module")
def guadramil():
    return orthography2ipa.get("ast-PT-x-guadramil")


@pytest.fixture(scope="module")
def rionor():
    return orthography2ipa.get("ast-PT-x-rionor")


class TestGuadramilRegistry:
    def test_loads(self, guadramil):
        assert guadramil is not None
        assert guadramil.code == "ast-PT-x-guadramil"

    def test_name(self, guadramil):
        assert guadramil.name == "Guadramilese"

    def test_family(self, guadramil):
        assert guadramil.family == "Indo-European > Romance"

    def test_parent(self, guadramil):
        assert guadramil.parent == "ast-PT-x-medieval"

    def test_in_available_codes(self):
        assert "ast-PT-x-guadramil" in orthography2ipa.available_codes()

    def test_rionor_listed_as_ancestor(self, guadramil):
        """Rionorese is in the ancestor list as sister-dialect adstrate."""
        codes = [a.code for a in guadramil.ancestors]
        assert "ast-PT-x-rionor" in codes


class TestGuadramilInheritsRionorese:
    """Guadramilese shares all phonological rules with Rionorese (inherited
    via graphemes_base: ast-PT-x-rionor). Verify that the key Rionorese rules
    are present in the Guadramilese spec."""

    def test_betacism_inherited(self, guadramil):
        """v → b (full betacism, inherited from Rionorese)."""
        assert guadramil.graphemes.get("v") == ["b"]

    def test_ch_fricative_inherited(self, guadramil):
        """ch → ʃ (not tʃ, inherited from Rionorese override)."""
        assert guadramil.graphemes.get("ch") == ["ʃ"]

    def test_tch_trigraph_inherited(self, guadramil):
        """tch → tʃ (inherited from Rionorese)."""
        assert guadramil.graphemes.get("tch") == ["tʃ"]

    def test_z_dental_inherited(self, guadramil):
        """z → θ (dental fricative, inherited from Rionorese)."""
        assert guadramil.graphemes.get("z") == ["θ"]

    def test_ç_dental_inherited(self, guadramil):
        """ç → θ (inherited from Rionorese)."""
        assert guadramil.graphemes.get("ç") == ["θ"]

    def test_ie_diphthong_inherited(self, guadramil):
        """ie → je (Leonese diphthong, inherited)."""
        assert guadramil.graphemes.get("ie") == ["je"]

    def test_ua_diphthong_inherited(self, guadramil):
        """uâ → wɐ (inherited from Rionorese; Macias 2003, p. 26: timbre semelhante ao -a fechado)."""
        assert guadramil.graphemes.get("uâ") == ["wɐ"]

    def test_x_sibilant_inherited(self, guadramil):
        """x → ʃ (inherited)."""
        assert guadramil.graphemes.get("x") == ["ʃ"]

    def test_ll_lateral_inherited(self, guadramil):
        """ll → ʎ (inherited)."""
        assert guadramil.graphemes.get("ll") == ["ʎ"]

    def test_positional_c_before_e(self, guadramil):
        """c before e → θ (inherited positional rule)."""
        assert guadramil.resolve_grapheme("c", GraphemePosition.BEFORE_E) == ["θ"]

    def test_positional_g_before_e(self, guadramil):
        """g before e → x (inherited positional rule)."""
        assert guadramil.resolve_grapheme("g", GraphemePosition.BEFORE_E) == ["x"]

    def test_positional_r_word_initial_trill(self, guadramil):
        """r word-initial → r (trill, inherited)."""
        assert guadramil.resolve_grapheme("r", GraphemePosition.WORD_INITIAL) == ["r"]

    def test_positional_r_intervocalic_flap(self, guadramil):
        """r intervocalic → ɾ (flap, inherited)."""
        assert guadramil.resolve_grapheme("r", GraphemePosition.INTERVOCALIC) == ["ɾ"]

    def test_grapheme_count_similar_to_rionor(self, guadramil, rionor):
        """Guadramilese and Rionorese have the same grapheme inventory."""
        assert len(guadramil.graphemes) == len(rionor.graphemes)

    def test_v_phoneme_absent(self, guadramil):
        """/v/ is not a phoneme in Guadramilese (inherited betacism)."""
        assert guadramil.allophones.get("v") is None


class TestGuadramilDistance:
    """Guadramilese is very close to Rionorese and both are close to pt-PT."""

    def test_closer_to_rionor_than_to_arb(self, guadramil):
        from orthography2ipa.distance import full_distance
        rionor = orthography2ipa.get("ast-PT-x-rionor")
        arb = orthography2ipa.get("arb")
        assert full_distance(guadramil, rionor) < full_distance(guadramil, arb)

    def test_very_close_to_rionor(self, guadramil, rionor):
        """Guadramilese and Rionorese are sister dialects — phonologically near-identical."""
        from orthography2ipa.distance import phonological_distance
        d = phonological_distance(guadramil, rionor)
        assert d.combined < 0.15, f"Expected near-zero distance, got {d.combined}"

    def test_ancestry_high_with_rionor(self, guadramil, rionor):
        from orthography2ipa.distance import ancestry_similarity
        sim = ancestry_similarity(guadramil, rionor)
        assert sim > 0.3


# ═══════════════════════════════════════════════════════════════════════════
# Barranquenho (ext-PT-x-barrancos)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.fixture(scope="module")
def barrancos():
    return orthography2ipa.get("ext-PT-x-barrancos")


@pytest.fixture(scope="module")
def barrancos_tok(barrancos):
    return PhonetokTokenizer(barrancos)


class TestBarrancosRegistry:
    def test_loads(self, barrancos):
        assert barrancos is not None
        assert barrancos.code == "ext-PT-x-barrancos"

    def test_name(self, barrancos):
        assert barrancos.name == "Barranquenho"

    def test_parent(self, barrancos):
        assert barrancos.parent == "pt-PT"

    def test_in_available_codes(self):
        assert "ext-PT-x-barrancos" in orthography2ipa.available_codes()

    def test_has_graphemes(self, barrancos):
        assert len(barrancos.graphemes) > 0

    def test_spanish_ancestor(self, barrancos):
        codes = [a.code for a in barrancos.ancestors]
        assert "es-ES" in codes


class TestBarrancosGraphemes:
    """Key Barranquenho phonological rules from the 2025 Convenção Ortográfica."""

    def test_betacism(self, barrancos):
        """v → b (betacism — comment in source: 'NOT USED in barranquenho')."""
        assert barrancos.graphemes.get("v") == ["b"]

    def test_b_maps_to_b(self, barrancos):
        """b → b (explicit)."""
        assert barrancos.graphemes.get("b") == ["b"]

    def test_h_is_aspirated(self, barrancos):
        """h → h (NOT silent — Spanish/Andalusian influence)."""
        result = barrancos.graphemes.get("h")
        assert result == ["h"]

    def test_tch_affricate(self, barrancos):
        """tch → tʃ (new trigraph absent from standard Portuguese)."""
        assert barrancos.graphemes.get("tch") == ["tʃ"]

    def test_rr_alveolar_trill(self, barrancos):
        """rr → r (alveolar trill, NOT uvular ʁ as in pt-PT)."""
        assert barrancos.graphemes.get("rr") == ["r"]

    def test_ch_sibilant_inherited(self, barrancos):
        """ch → ʃ (inherited from pt-PT)."""
        assert barrancos.graphemes.get("ch") == ["ʃ"]

    def test_nh_nasal_inherited(self, barrancos):
        """nh → ɲ (inherited from pt-PT)."""
        assert barrancos.graphemes.get("nh") == ["ɲ"]

    def test_lh_lateral_inherited(self, barrancos):
        """lh → ʎ (inherited from pt-PT)."""
        assert barrancos.graphemes.get("lh") == ["ʎ"]


class TestBarrancosAllophones:
    def test_v_phoneme_absent(self, barrancos):
        """/v/ not a phoneme in Barranquenho (betacism)."""
        assert barrancos.allophones.get("v") is None

    def test_uvular_absent(self, barrancos):
        """/ʁ/ not a phoneme in Barranquenho (alveolar trill used instead)."""
        assert barrancos.allophones.get("ʁ") is None

    def test_b_has_fricative_allophone(self, barrancos):
        """/b/ → [β] intervocalically (Ibero-Romance allophony)."""
        assert "β" in barrancos.allophones.get("b", [])

    def test_r_trill(self, barrancos):
        """/r/ trill is a distinct phoneme."""
        assert barrancos.allophones.get("r") == ["r"]


class TestBarrancosPositional:
    def test_r_word_initial_alveolar(self, barrancos):
        """r word-initial → r (alveolar trill, not uvular ʁ)."""
        result = barrancos.resolve_grapheme("r", GraphemePosition.WORD_INITIAL)
        assert result == ["r"]

    def test_r_intervocalic_flap(self, barrancos):
        """r intervocalic → ɾ (flap)."""
        result = barrancos.resolve_grapheme("r", GraphemePosition.INTERVOCALIC)
        assert result == ["ɾ"]

    def test_c_before_e_is_s(self, barrancos):
        """c before e → s (Portuguese sibilant, not θ as in Rionorese)."""
        result = barrancos.resolve_grapheme("c", GraphemePosition.BEFORE_E)
        assert result == ["s"]

    def test_g_before_e_is_voiced_fricative(self, barrancos):
        """g before e → ʒ (like Portuguese, not velar x as in Rionorese/Spanish)."""
        result = barrancos.resolve_grapheme("g", GraphemePosition.BEFORE_E)
        assert result == ["ʒ"]

    def test_s_word_initial_voiceless(self, barrancos):
        """s word-initial → s (voiceless)."""
        result = barrancos.resolve_grapheme("s", GraphemePosition.WORD_INITIAL)
        assert result == ["s"]

    def test_s_intervocalic_voiced(self, barrancos):
        """s intervocalic → z (voiced, like Portuguese)."""
        result = barrancos.resolve_grapheme("s", GraphemePosition.INTERVOCALIC)
        assert result == ["z"]

    def test_qu_before_e_is_k(self, barrancos):
        """qu before e → k (u silent)."""
        result = barrancos.resolve_grapheme("qu", GraphemePosition.BEFORE_E)
        assert result == ["k"]


class TestBarrancosTokenizer:
    def test_tch_trigraph_matched(self, barrancos_tok):
        """Tokenizer matches tch as a single trigraph."""
        from orthography2ipa.phonetok import TokenKind
        tokens = barrancos_tok.tokenize("tcha")
        grapheme_tokens = [t for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert grapheme_tokens[0].grapheme == "tch"
        assert "tʃ" in grapheme_tokens[0].ipa

    def test_rr_produces_trill(self, barrancos_tok):
        """rr → r (not ʁ as in standard pt-PT)."""
        result = barrancos_tok.ipa_best("rra")
        assert "r" in result
        assert "ʁ" not in result

    def test_v_produces_b(self, barrancos_tok):
        """v → b (betacism)."""
        from orthography2ipa.phonetok import TokenKind
        tokens = barrancos_tok.tokenize("vaca")
        g_tokens = [t for t in tokens if t.kind == TokenKind.GRAPHEME]
        v_token = g_tokens[0]
        assert v_token.grapheme == "v"
        assert "b" in v_token.ipa

    def test_h_produces_phoneme(self, barrancos_tok):
        """h → h (NOT empty/silent as in standard Portuguese)."""
        from orthography2ipa.phonetok import TokenKind
        tokens = barrancos_tok.tokenize("hasta")
        g_tokens = [t for t in tokens if t.kind == TokenKind.GRAPHEME]
        h_token = g_tokens[0]
        assert h_token.grapheme == "h"
        assert len(h_token.ipa) > 0


class TestBarrancosDistance:
    def test_closer_to_pt_than_to_arb(self, barrancos):
        from orthography2ipa.distance import full_distance
        pt = orthography2ipa.get("pt-PT")
        arb = orthography2ipa.get("arb")
        assert full_distance(barrancos, pt) < full_distance(barrancos, arb)

    def test_barrancos_not_identical_to_pt(self, barrancos):
        from orthography2ipa.distance import phonological_distance
        pt = orthography2ipa.get("pt-PT")
        d = phonological_distance(barrancos, pt)
        assert d.combined > 0.01, "Barranquenho should differ from pt-PT"

    def test_barrancos_closer_to_pt_than_rionor(self, barrancos):
        """Barranquenho is a Portuguese-base variety; Rionorese is Leonese-base."""
        from orthography2ipa.distance import full_distance
        pt = orthography2ipa.get("pt-PT")
        rionor = orthography2ipa.get("ast-PT-x-rionor")
        d_barrancos_pt = full_distance(barrancos, pt)
        d_barrancos_rionor = full_distance(barrancos, rionor)
        assert d_barrancos_pt < d_barrancos_rionor
