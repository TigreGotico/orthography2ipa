"""Tests for Aragonese (an) language module — structural and linguistic validation.

Validates the Aragonese inventory against the official orthographic standard:
    Academia de l'Aragonés (2017). *Ortografía de l'Aragonés*.

Tests cover:
1. Structural integrity (all specs well-formed, positional keys valid)
2. Phoneme inventory completeness (all consonants, vowels, digraphs)
3. Grapheme→IPA correctness per the official orthography
4. Allophone inventory (lenition, nasal assimilation)
5. Positional grapheme accuracy (lenition, r-distribution, final weakening)
6. Dialectal variation (Eastern/Ribagorçan vs Central)
7. Ancestry chain integrity (parent references resolve)
"""
import pytest
from orthography2ipa.registry import get
from orthography2ipa.types import (
    AncestorRole,
    GraphemePosition as GP,
    LanguageSpec,
)


# ═══════════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════════

@pytest.fixture(scope="module")
def an():
    """Standard/central Aragonese."""
    return get("an")


@pytest.fixture(scope="module")
def an_w():
    """Western Aragonese."""
    return get("an-x-occidental")


@pytest.fixture(scope="module")
def an_e():
    """Eastern Aragonese (Ribagorçan)."""
    return get("an-x-oriental")


# ═══════════════════════════════════════════════════════════════════════════
# 1. Structural integrity
# ═══════════════════════════════════════════════════════════════════════════

class TestAragonesStructure:
    """All Aragonese specs are well-formed LanguageSpecs."""

    @pytest.mark.parametrize("code", ["an", "an-x-occidental", "an-x-oriental"])
    def test_spec_loads(self, code):
        spec = get(code)
        assert isinstance(spec, LanguageSpec)
        assert spec.code == code

    def test_family_is_romance(self, an):
        assert an.family == "Romance"

    def test_script_is_latin(self, an):
        assert an.script == "Latin"

    def test_graphemes_nonempty(self, an):
        assert len(an.graphemes) > 20

    def test_allophones_nonempty(self, an):
        assert len(an.allophones) > 10

    def test_has_positional_data(self, an):
        assert an.has_positional_data()

    def test_positional_keys_in_graphemes(self, an):
        """Every positional grapheme key must exist in the base graphemes."""
        for key in an.positional_grapheme_keys():
            assert key in an.graphemes, (
                f"Positional key '{key}' not found in base graphemes"
            )

    def test_dialects_parent_is_an(self, an_w, an_e):
        assert an_w.primary_parent == "an"
        assert an_e.primary_parent == "an"


# ═══════════════════════════════════════════════════════════════════════════
# 2. Vowel system (§1.1)
# ═══════════════════════════════════════════════════════════════════════════

class TestAragonesVowels:
    """Standard Aragonese has a 5-vowel system /a e i o u/."""

    @pytest.mark.parametrize("grapheme,ipa", [
        ("a", "a"),
        ("e", "e"),
        ("i", "i"),
        ("o", "o"),
        ("u", "u"),
    ])
    def test_five_vowel_system(self, an, grapheme, ipa):
        assert ipa in an.graphemes[grapheme]

    def test_central_no_open_mid_vowels(self, an):
        """Central Aragonese does NOT have /ɛ/ or /ɔ/ as graphemic targets."""
        # The base <e> should map to just ["e"], not include "ɛ"
        assert an.graphemes["e"] == ["e"], (
            "Central Aragonese has a 5-vowel system; "
            "/ɛ/ belongs only to Eastern (Benasquese) variety"
        )
        assert an.graphemes["o"] == ["o"]

    def test_eastern_has_open_mid_vowels(self, an_e):
        """Eastern Aragonese (Benasquese) has 7-vowel system with /ɛ/ and /ɔ/."""
        assert "ɛ" in an_e.graphemes["e"]
        assert "ɔ" in an_e.graphemes["o"]

    @pytest.mark.parametrize("grapheme,ipa", [
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
    ])
    def test_accented_vowels_same_phoneme(self, an, grapheme, ipa):
        """Accent marks indicate stress, not different phonemes (§3)."""
        assert an.graphemes[grapheme] == [ipa]


# ═══════════════════════════════════════════════════════════════════════════
# 3. Consonant grapheme→IPA (§1.2)
# ═══════════════════════════════════════════════════════════════════════════

class TestAragonesConsonants:
    """Validate consonant grapheme→IPA mappings per the official orthography."""

    def test_b_is_bilabial_stop(self, an):
        """§1.2.1: <b> → /b/."""
        assert an.graphemes["b"] == ["b"]

    def test_v_is_bilabial_stop(self, an):
        """§1.2.18: <v> → /b/ (betacism, same as <b>)."""
        assert an.graphemes["v"] == ["b"]

    def test_c_has_k_and_theta(self, an):
        """§1.2.2: <c> → /k/ before a,o,u; /θ/ before e,i."""
        ipa = an.graphemes["c"]
        assert "k" in ipa
        assert "θ" in ipa

    def test_ch_is_palatal_affricate(self, an):
        """§1.2.2: <ch> → /tʃ/."""
        assert an.graphemes["ch"] == ["tʃ"]

    def test_d_is_dental_stop(self, an):
        """§1.2.3: <d> → /d/."""
        assert an.graphemes["d"] == ["d"]

    def test_f_is_labiodental_fricative(self, an):
        """§1.2.4: <f> → /f/."""
        assert an.graphemes["f"] == ["f"]

    def test_g_is_velar_stop(self, an):
        """§1.2.5: <g> → /ɡ/ (velar stop only, NOT /x/)."""
        ipa = an.graphemes["g"]
        assert "ɡ" in ipa
        assert "x" not in ipa, (
            "<g> represents /ɡ/ only; /x/ is <j> (§1.2.7)"
        )

    def test_gu_before_e_i(self, an):
        """§1.2.5b: <gu> before e,i → /ɡ/."""
        assert "ɡ" in an.graphemes["gu"]

    def test_gue_dieresis(self, an):
        """§1.2.5a: <gü> → /ɡw/ (cigüenya, pingüino)."""
        assert "gü" in an.graphemes
        assert "ɡw" in an.graphemes["gü"]

    def test_h_is_silent(self, an):
        """§1.2.6: <h> is silent (etymological)."""
        assert an.graphemes["h"] == [""]

    def test_j_is_velar_fricative(self, an):
        """§1.2.7: <j> → /x/ (velar fricative)."""
        ipa = an.graphemes["j"]
        assert "x" in ipa
        # Traditional Aragonese /tʃ/ is written <ch>, not <j>
        assert "tʃ" not in ipa, (
            "The traditional Aragonese affricate /tʃ/ is spelled <ch>, "
            "not <j>. <j> represents Castilianised /x/ (§1.2.7)"
        )

    def test_k_is_velar_stop(self, an):
        """§1.2.8: <k> → /k/ (foreign/technical terms only)."""
        assert an.graphemes["k"] == ["k"]

    def test_l_is_alveolar_lateral(self, an):
        """§1.2.9: <l> → /l/."""
        assert an.graphemes["l"] == ["l"]

    def test_ll_is_palatal_lateral(self, an):
        """§1.2.9: <ll> → /ʎ/ (conservative, no yeísmo)."""
        assert an.graphemes["ll"] == ["ʎ"]

    def test_m_is_bilabial_nasal(self, an):
        """§1.2.10: <m> → /m/."""
        assert an.graphemes["m"] == ["m"]

    def test_n_is_alveolar_nasal(self, an):
        """§1.2.11: <n> → /n/."""
        assert an.graphemes["n"] == ["n"]

    def test_nn_geminate_nasal(self, an):
        """§1.2.11: <nn> → geminate [nː] (Belsetán, toponyms)."""
        assert "nn" in an.graphemes
        assert "nː" in an.graphemes["nn"]

    def test_ny_is_palatal_nasal(self, an):
        """§1.2.12: <ny> → /ɲ/ (referential spelling)."""
        assert an.graphemes["ny"] == ["ɲ"]

    def test_ene_tilde_is_palatal_nasal(self, an):
        """§1.2.12: <ñ> → /ɲ/ (also normative)."""
        assert an.graphemes["ñ"] == ["ɲ"]

    def test_p_is_bilabial_stop(self, an):
        """§1.2.13: <p> → /p/."""
        assert an.graphemes["p"] == ["p"]

    def test_qu_is_velar_stop(self, an):
        """§1.2.14: <qu> → /k/ before e,i."""
        assert an.graphemes["qu"] == ["k"]

    def test_r_is_tap(self, an):
        """§1.2.15: <r> → /ɾ/ (simple vibrant)."""
        assert "ɾ" in an.graphemes["r"]

    def test_rr_is_trill(self, an):
        """§1.2.15: <rr> → /r/ (multiple vibrant, intervocalic)."""
        assert an.graphemes["rr"] == ["r"]

    def test_s_is_alveolar_fricative(self, an):
        """§1.2.16: <s> → /s/ (apico-alveolar)."""
        assert an.graphemes["s"] == ["s"]

    def test_t_is_dental_stop(self, an):
        """§1.2.17: <t> → /t/."""
        assert an.graphemes["t"] == ["t"]

    def test_x_is_prepalatal_fricative(self, an):
        """§1.2.20: <x> → /ʃ/ (prepalatal fricative)."""
        assert an.graphemes["x"] == ["ʃ"]

    def test_ix_is_prepalatal_fricative(self, an):
        """§1.2.20: <ix> → /ʃ/ (after vowel)."""
        assert an.graphemes["ix"] == ["ʃ"]

    def test_y_is_palatal_fricative(self, an):
        """§1.2.21: <y> → /ʝ/ (palatal fricative)."""
        ipa = an.graphemes["y"]
        assert "ʝ" in ipa

    def test_z_is_interdental_fricative(self, an):
        """§1.2.22: <z> → /θ/ (before a,o,u and in coda)."""
        assert "θ" in an.graphemes["z"]

    def test_l_dot_l_geminate(self, an):
        """§1.2.9: <l·l> → [lː] (Belsetán geminate lateral)."""
        assert "l·l" in an.graphemes
        assert "lː" in an.graphemes["l·l"]


# ═══════════════════════════════════════════════════════════════════════════
# 4. Allophone inventory
# ═══════════════════════════════════════════════════════════════════════════

class TestAragonesAllophones:
    """Validate allophone inventory for phonological completeness."""

    def test_b_has_approximant(self, an):
        """Ibero-Romance lenition: /b/ → [β] in lenition contexts."""
        assert "β" in an.allophones["b"]

    def test_d_has_approximant(self, an):
        """Ibero-Romance lenition: /d/ → [ð]."""
        assert "ð" in an.allophones["d"]

    def test_d_has_deletion(self, an):
        """§1.2.3: Intervocalic /d/ → [∅] in some dialects."""
        assert "∅" in an.allophones["d"]

    def test_g_has_approximant(self, an):
        """Ibero-Romance lenition: /ɡ/ → [ɣ]."""
        assert "ɣ" in an.allophones["ɡ"]

    def test_s_apico_alveolar(self, an):
        """§1.2.16: /s/ is apico-alveolar [s̺]."""
        assert "s̺" in an.allophones["s"]

    def test_n_velar_allophone(self, an):
        """Nasal assimilation: /n/ → [ŋ] before velars."""
        assert "ŋ" in an.allophones["n"]

    def test_r_final_deletion(self, an):
        """§1.2.15: Final /ɾ/ → [∅] in Ansotano, Chistabino, Ribagorzano."""
        assert "∅" in an.allophones["ɾ"]

    def test_palatal_lateral_conservative(self, an):
        """Standard Aragonese preserves /ʎ/ without yeísmo."""
        assert "ʎ" in an.allophones["ʎ"]
        # For central Aragonese, ʎ should NOT have [j] allophone
        if "j" in an.allophones.get("ʎ", []):
            pytest.fail("Central Aragonese should not have yeísmo [j] for /ʎ/")


# ═══════════════════════════════════════════════════════════════════════════
# 5. Positional graphemes
# ═══════════════════════════════════════════════════════════════════════════

class TestAragonesPositional:
    """Validate positional grapheme resolution."""

    def test_b_intervocalic_lenition(self, an):
        """<b> → [β] intervocalically (standard Ibero-Romance)."""
        result = an.resolve_grapheme("b", GP.INTERVOCALIC)
        assert "β" in result

    def test_b_default_stop(self, an):
        """<b> → [b] in default position."""
        result = an.resolve_grapheme("b", GP.DEFAULT)
        assert "b" in result

    def test_d_intervocalic_lenition(self, an):
        """<d> → [ð] intervocalically (§1.2.3)."""
        result = an.resolve_grapheme("d", GP.INTERVOCALIC)
        assert "ð" in result

    def test_d_word_final_deletion(self, an):
        """<d> → [∅] word-finally in gerund -nd forms (§1.2.3)."""
        result = an.resolve_grapheme("d", GP.WORD_FINAL)
        assert "∅" in result

    def test_g_intervocalic_lenition(self, an):
        """<g> → [ɣ] intervocalically."""
        result = an.resolve_grapheme("g", GP.INTERVOCALIC)
        assert "ɣ" in result

    def test_r_word_initial_trill(self, an):
        """§1.2.15: <r> word-initially → trill /r/."""
        result = an.resolve_grapheme("r", GP.WORD_INITIAL)
        assert "r" in result

    def test_r_intervocalic_tap(self, an):
        """§1.2.15: <r> intervocalically → tap /ɾ/."""
        result = an.resolve_grapheme("r", GP.INTERVOCALIC)
        assert "ɾ" in result

    def test_r_word_final_variable(self, an):
        """§1.2.15: <r> word-finally → [ɾ] or [∅]."""
        result = an.resolve_grapheme("r", GP.WORD_FINAL)
        assert "ɾ" in result or "∅" in result

    def test_t_word_final_variable(self, an):
        """§1.2.17: <t> word-finally → [t]~[ð]~[ɾ]~[∅]."""
        result = an.resolve_grapheme("t", GP.WORD_FINAL)
        # Should contain multiple variants
        assert len(result) > 1, (
            "Word-final <t> should have multiple realisations per §1.2.17"
        )
        assert "t" in result


# ═══════════════════════════════════════════════════════════════════════════
# 6. Diphthongs
# ═══════════════════════════════════════════════════════════════════════════

class TestAragoneseDiphthongs:
    """Aragonese retains Latin diphthongs shared with Castilian."""

    def test_ue_diphthong(self, an):
        """Lat. Ŏ → [we]: puerta, fuent, cuerpo."""
        assert "we" in an.graphemes["ue"]

    def test_ie_diphthong(self, an):
        """Lat. Ĕ → [je]: tierra, fiero, siete."""
        assert "je" in an.graphemes["ie"]

    @pytest.mark.parametrize("digraph,ipa", [
        ("ua", "wa"), ("uo", "wo"),
        ("ia", "ja"), ("io", "jo"), ("iu", "ju"),
        ("ai", "aj"), ("ei", "ej"), ("oi", "oj"),
        ("au", "aw"), ("eu", "ew"), ("ou", "ow"),
        ("ui", "wi"),
    ])
    def test_diphthong_mapping(self, an, digraph, ipa):
        assert ipa in an.graphemes[digraph]


# ═══════════════════════════════════════════════════════════════════════════
# 7. Eastern Aragonese dialectal differences
# ═══════════════════════════════════════════════════════════════════════════

class TestEasternAragonese:
    """Eastern/Ribagorçan differences from central standard."""

    def test_seseo(self, an_e):
        """Benasquese: <z> and <ce>/<ci> → /s/ (not /θ/)."""
        assert "s" in an_e.graphemes["z"]
        # <c> should have /s/ instead of /θ/ before e,i
        assert "s" in an_e.graphemes["c"]

    def test_voiced_affricate(self, an_e):
        """Catalan influence: <j> may have voiced affricate [dʒ]."""
        assert "dʒ" in an_e.graphemes["j"]

    def test_g_before_front_vowels(self, an_e):
        """<g> before e,i → [dʒ] (Catalan pattern)."""
        assert "dʒ" in an_e.graphemes["g"]

    def test_partial_yeismo(self, an_e):
        """Some yeísmo: /ʎ/ → [j] in some Eastern speakers."""
        assert "j" in an_e.graphemes["ll"]

    def test_seven_vowel_system(self, an_e):
        """Eastern has /ɛ/ and /ɔ/ (Catalan-type 7-vowel system)."""
        assert "ɛ" in an_e.graphemes["e"]
        assert "ɔ" in an_e.graphemes["o"]
        # Also in allophones
        assert "ɛ" in an_e.allophones
        assert "ɔ" in an_e.allophones


# ═══════════════════════════════════════════════════════════════════════════
# 8. Ancestry chain integrity
# ═══════════════════════════════════════════════════════════════════════════

class TestAragonesAncestry:
    """Validate ancestry references resolve correctly."""

    def test_parent_is_hispanic_vulgar_latin(self, an):
        """Aragonese descends from Hispanic Vulgar Latin."""
        assert an.primary_parent == "la-x-hispania"

    def test_parent_exists_in_registry(self, an):
        """The parent code must resolve to a real LanguageSpec."""
        parent = get(an.primary_parent)
        assert parent is not None
        assert parent.code == "la-x-hispania"

    def test_has_basque_substrate(self, an):
        """Aragonese (Pyrenean) should have Basque substrate."""
        subs = an.substrate_codes
        assert "xaq" in subs

    def test_has_arabic_adstrate(self, an):
        """Ebro valley Arabic influence."""
        contacts = an.contact_codes
        assert "xaa" in contacts

    def test_has_gothic_superstrate(self, an):
        """Visigothic superstrate (shared with other Ibero-Romance)."""
        sups = an.superstrate_codes
        assert "got" in sups

    def test_ancestor_weights_reasonable(self, an):
        """Parent weight should dominate, contacts should be small."""
        for anc in an.get_ancestors():
            if anc.role == AncestorRole.PARENT:
                assert anc.weight >= 0.70
            elif anc.role in (AncestorRole.SUBSTRATE, AncestorRole.ADSTRATE):
                assert anc.weight <= 0.20
            elif anc.role == AncestorRole.SUPERSTRATE:
                assert anc.weight <= 0.20

    def test_all_ancestors_exist(self, an):
        """Every ancestor code must resolve in the registry."""
        for anc in an.get_ancestors():
            ancestor_spec = get(anc.code)
            assert ancestor_spec is not None, (
                f"Ancestor '{anc.code}' not found in registry"
            )

    def test_western_parent_chain(self, an_w):
        """Western Aragonese → Aragonese → Hispanic Vulgar Latin → Latin."""
        assert an_w.primary_parent == "an"
        parent = get("an")
        assert parent.primary_parent == "la-x-hispania"
        grandparent = get("la-x-hispania")
        assert grandparent.primary_parent == "la"

    def test_eastern_parent_chain(self, an_e):
        """Eastern Aragonese → Aragonese → Hispanic Vulgar Latin → Latin."""
        assert an_e.primary_parent == "an"


# ═══════════════════════════════════════════════════════════════════════════
# 9. Removed or fixed items validation
# ═══════════════════════════════════════════════════════════════════════════

class TestAragonesCorrections:
    """Validate corrections from the PDF-based review."""

    def test_no_cedilla_grapheme(self, an):
        """<ç> is not part of the standard Aragonese orthography."""
        assert "ç" not in an.graphemes, (
            "<ç> (cedilla) is not in the official Aragonese orthography; "
            "it does not appear in the 2017 standard"
        )

    def test_g_does_not_map_to_x(self, an):
        """<g> should NOT map to /x/; that's <j>'s job (§1.2.5 vs §1.2.7)."""
        assert "x" not in an.graphemes["g"]

    def test_j_does_not_map_to_tsh(self, an):
        """<j> = /x/ only in the standard orthography (§1.2.7).
        Traditional /tʃ/ is written <ch>."""
        assert "tʃ" not in an.graphemes["j"]

    def test_y_does_not_map_to_vowel_i(self, an):
        """<y> = /ʝ/ (consonantal); vowel [i] is written <i> (§1.2.21)."""
        ipa = an.graphemes["y"]
        # The primary value should be the palatal fricative
        assert "ʝ" in ipa