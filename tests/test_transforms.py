"""Tests for T-13 through T-16 / T-18: orthography2ipa.transforms module.

Covers:
  - T-13: Core types (IPARule, IPAChainShift, IPALexicalRule, DialectTransform)
  - T-14: debias_lisbon() — DB1–DB6 rules
  - T-15: Northern PT transforms (northern, transmontano, baixo_minhoto, porto,
           beira_alta)
  - T-16: Central-Southern, Galician, Leonese transforms
  - T-18: Integration via apply_transform()
"""
import pytest

from orthography2ipa.transforms import (
    DIALECT_PROFILES,
    VOWEL_SET,
    DialectTransform,
    IPAChainShift,
    IPALexicalRule,
    IPARule,
    apply_transform,
    available_profiles,
    debias_lisbon,
)


# ---------------------------------------------------------------------------
# T-13: Core type construction
# ---------------------------------------------------------------------------

class TestIPARule:
    def test_basic_construction(self):
        r = IPARule(id="X1", name="test", find="v", replace="b")
        assert r.id == "X1"
        assert r.find == "v"
        assert r.replace == "b"
        assert r.context is None
        assert r.requires_ortho is False

    def test_with_context(self):
        r = IPARule(id="X2", name="test", find="u", replace="y",
                    context="stressed", description="palatalize")
        assert r.context == "stressed"

    def test_deletion_rule(self):
        r = IPARule(id="X3", name="delete", find="ɨ", replace="")
        assert r.replace == ""


class TestIPAChainShift:
    def test_unconditional_shift(self):
        cs = IPAChainShift(
            id="TEST",
            name="test_shift",
            mapping={"a": "ɔ", "ɔ": "o", "o": "u"},
            context=None,
        )
        result = cs.apply("ˈkaza")
        # a → ɔ (stress does not restrict since context=None)
        assert "ɔ" in result

    def test_stressed_only(self):
        cs = IPAChainShift(
            id="TEST",
            name="test_shift",
            mapping={"a": "ɔ"},
            context="stressed",
        )
        # Stressed a → ɔ, unstressed a unchanged
        result = cs.apply("ˈkaza")
        # First a is stressed (after ˈk), second a is unstressed
        assert result == "ˈkɔza"

    def test_simultaneous_no_cascade(self):
        """Chain shift must NOT cascade: a→ɔ should not then trigger ɔ→o."""
        cs = IPAChainShift(
            id="TEST",
            name="test_shift",
            mapping={"a": "ɔ", "ɔ": "o"},
            context=None,
        )
        # 'a' in one pass → 'ɔ' (not 'o')
        result = cs.apply("pa")
        assert result == "pɔ"
        # 'ɔ' → 'o' (not 'u' if no 'u' rule)
        result2 = cs.apply("pɔ")
        assert result2 == "po"

    def test_stress_resets_after_vowel(self):
        """Only first vowel in stressed syllable should be shifted."""
        cs = IPAChainShift(
            id="TEST",
            name="test",
            mapping={"a": "ɔ"},
            context="stressed",
        )
        # ˈfaj — f is non-vowel, a is stressed vowel (shifts), j is glide
        result = cs.apply("ˈfaj")
        assert result == "ˈfɔj"


class TestIPALexicalRule:
    def test_applies_to_matching_word(self):
        rule = IPALexicalRule(id="T", word="o", find="u", replace="al")
        assert rule.applies("o") is True
        assert rule.applies("O") is True  # case-insensitive

    def test_does_not_apply_to_non_matching(self):
        rule = IPALexicalRule(id="T", word="o", find="u", replace="al")
        assert rule.applies("os") is False
        assert rule.applies(None) is False

    def test_does_not_apply_to_none(self):
        rule = IPALexicalRule(id="T", word="eu", find="ew", replace="jew")
        assert rule.applies(None) is False


class TestDialectTransform:
    def test_construction(self):
        dt = DialectTransform(
            profile_code="test",
            name="Test",
            cintra_zone="none",
            rules=[],
        )
        assert dt.profile_code == "test"
        assert dt.requires_debiasing is True

    def test_lisbon_no_debiasing(self):
        assert DIALECT_PROFILES["lisbon"].requires_debiasing is False


class TestDialectProfilesRegistry:
    def test_all_expected_profiles_present(self):
        expected = {
            "estremenho", "lisbon", "ribatejano", "beira_baixa",
            "algarve_barlavento", "northern", "transmontano",
            "baixo_minhoto", "porto", "beira_alta",
            "galician", "galician_west", "leonese", "rionorese", "guadramilese",
        }
        assert expected.issubset(set(DIALECT_PROFILES.keys()))

    def test_available_profiles_sorted(self):
        profiles = available_profiles()
        assert profiles == sorted(profiles)

    def test_all_profiles_have_codes(self):
        for code, dt in DIALECT_PROFILES.items():
            assert dt.profile_code == code, \
                f"Mismatch: key={code!r} but profile_code={dt.profile_code!r}"

    def test_all_profiles_have_cintra_zone(self):
        for code, dt in DIALECT_PROFILES.items():
            assert dt.cintra_zone, f"{code} missing cintra_zone"


# ---------------------------------------------------------------------------
# T-14: debias_lisbon()
# ---------------------------------------------------------------------------

class TestDebiasLisbon:
    def test_db4_beta_to_b(self):
        """DB4: β → b (allophonic spirantization normalize)."""
        assert debias_lisbon("ˈβɐzu") == "ˈbɐzu"

    def test_db5_eth_to_d(self):
        """DB5: ð → d."""
        assert debias_lisbon("ˈkaðɐ") == "ˈkadɐ"

    def test_db6_gamma_to_g(self):
        """DB6: ɣ → ɡ."""
        assert debias_lisbon("ˈaɣwɐ") == "ˈaɡwɐ"

    def test_db6b_velarized_l(self):
        """DB6b: ɫ → l."""
        assert debias_lisbon("ˈsaɫ") == "ˈsal"

    def test_db1_ej_restoration_with_ortho(self):
        """DB1: ɐj → ej when ortho contains 'ei'."""
        result = debias_lisbon("ˈlɐjtɨ", ortho="leite")
        assert result == "ˈlejtɨ"

    def test_db1_no_change_without_ei(self):
        """DB1: ɐj should NOT change if ortho doesn't have 'ei'."""
        result = debias_lisbon("ˈmɐj", ortho="mai")
        assert result == "ˈmɐj"

    def test_db2_ou_restoration_with_ortho(self):
        """DB2: restore /ow/ diphthong from ‹ou›."""
        result = debias_lisbon("ˈfol", ortho="foul")
        assert "ow" in result

    def test_idempotent_on_clean_input(self):
        """De-biasing a clean IPA string should not change it (no β/ð/ɣ/ɫ)."""
        clean = "ˈveɾdɨ"
        assert debias_lisbon(clean) == clean

    def test_db7_uvular_preserved(self):
        """DB7: ʁ is preserved (not changed)."""
        ipa = "ˈʁiu"
        assert debias_lisbon(ipa) == "ˈʁiu"

    def test_combined_debiasing(self):
        """Multiple corrections in one string."""
        result = debias_lisbon("βɐˈzɐl ðɨ ˈsɫ", ortho=None)
        assert "β" not in result
        assert "ð" not in result
        assert "ɫ" not in result


# ---------------------------------------------------------------------------
# T-15: Northern PT transforms
# ---------------------------------------------------------------------------

class TestNorthernCommon:
    def test_betacism_v_to_b(self):
        """N1: /v/ → /b/ — the canonical Northern feature."""
        result = apply_transform("ˈvakɐ", "northern", debias=False)
        assert result == "ˈbakɐ"

    def test_betacism_multiple(self):
        result = apply_transform("ˈvɛʎu ˈveɾdɨ ˈvakɐ", "northern", debias=False)
        assert "v" not in result
        assert result.count("b") >= 3

    def test_no_other_changes(self):
        """Northern common should not change consonants other than v."""
        ipa = "ˈpeʃɨ"
        result = apply_transform(ipa, "northern", debias=False)
        assert result == ipa  # no v in input


class TestTransmontano:
    def test_betacism(self):
        result = apply_transform("ˈvɛʎu", "transmontano", debias=False)
        assert "b" in result and "v" not in result

    def test_sibilant_apico_fallback_no_ortho(self):
        """TM1_fallback: s → s̺ when no ortho provided."""
        result = apply_transform("ˈsɛku", "transmontano", ortho=None, debias=False)
        # TM1_fallback (s→s̺) applies when ortho is None
        assert "s̺" in result

    def test_nasal_diphthong_reduction_word_final(self):
        """TM3: ɐ̃w̃ → õ at word end."""
        result = apply_transform("kɐ̃ˈsɐ̃w̃", "transmontano", debias=False)
        assert "õ" in result

    def test_ch_affrication_with_ortho(self):
        """TM2: ʃ → tʃ when ortho contains 'ch'."""
        result = apply_transform("ˈʃa", "transmontano", ortho="chá", debias=False)
        assert "tʃ" in result


class TestBaixoMinhoto:
    def test_all_s_apicoalveolar(self):
        """BMD1a: unconditional s → s̺."""
        result = apply_transform("ˈsɛku", "baixo_minhoto", debias=False)
        assert "s̺" in result

    def test_all_z_apicoalveolar(self):
        """BMD1b: unconditional z → z̺."""
        result = apply_transform("ˈkazɐ", "baixo_minhoto", debias=False)
        assert "z̺" in result

    def test_betacism(self):
        result = apply_transform("ˈvinu", "baixo_minhoto", debias=False)
        assert "b" in result


class TestPorto:
    def test_betacism(self):
        result = apply_transform("ˈvakɐ", "porto", debias=False)
        assert "b" in result and "v" not in result

    def test_sibilants_apicoalveolar(self):
        result = apply_transform("ˈsɛku", "porto", debias=False)
        assert "s̺" in result


class TestBeiraAlta:
    def test_sibilants_apicoalveolar(self):
        result = apply_transform("ˈsɛku", "beira_alta", debias=False)
        assert "s̺" in result

    def test_betacism(self):
        result = apply_transform("ˈvinu", "beira_alta", debias=False)
        assert "b" in result


# ---------------------------------------------------------------------------
# T-16: Central-Southern transforms
# ---------------------------------------------------------------------------

class TestEstremenho:
    def test_no_change(self):
        """Estremenho = neutral dialect. After de-biasing, no further change."""
        ipa = "ˈveɾdɨ"
        result = apply_transform(ipa, "estremenho", debias=False)
        assert result == ipa


class TestLisbon:
    def test_ei_lowering(self):
        """LX1: /ej/ → [ɐj] (Lisbon diphthong lowering)."""
        result = apply_transform("ˈlejtɨ", "lisbon", debias=False)
        assert "ɐj" in result

    def test_ou_monophthong(self):
        """LX2: /ow/ → [o]."""
        result = apply_transform("ˈlowku", "lisbon", debias=False)
        assert "ow" not in result and "o" in result

    def test_lisbon_no_debiasing_flag(self):
        """Lisbon profile has requires_debiasing=False."""
        assert DIALECT_PROFILES["lisbon"].requires_debiasing is False


class TestRibatejano:
    def test_ei_monophthong(self):
        """RA1: /ej/ → [e]."""
        result = apply_transform("ˈlejtɨ", "ribatejano", debias=False)
        assert "ej" not in result
        assert "e" in result

    def test_sample_words(self):
        # primeiro → pɾiˈmeɾu
        result = apply_transform("pɾiˈmejɾu", "ribatejano", debias=False)
        assert "ej" not in result


class TestBeiraBaixa:
    def test_ei_monophthong(self):
        result = apply_transform("ˈlejtɨ", "beira_baixa", debias=False)
        assert "ej" not in result

    def test_u_palatalization_stressed(self):
        """BB1: tonic /u/ → [y]."""
        result = apply_transform("ˈtudu", "beira_baixa", debias=False)
        assert "y" in result

    def test_final_schwa_deletion(self):
        """BB5b: final ɨ → Ø."""
        result = apply_transform("ˈɡɾɐ̃dɨ", "beira_baixa", debias=False)
        assert not result.endswith("ɨ")

    def test_open_e_labialization(self):
        """BB4: tonic /ɛ/ → [œ]."""
        result = apply_transform("ˈpɛ", "beira_baixa", debias=False)
        assert "œ" in result


class TestBarlaventoAlgarve:
    def test_chain_shift_a_to_o(self):
        """ALG: stressed /a/ → [ɔ]."""
        result = apply_transform("ˈkazɐ", "algarve_barlavento", debias=False)
        # stressed a → ɔ
        assert "ɔ" in result

    def test_chain_shift_no_cascade(self):
        """Chain shift must be simultaneous: ɔ→o but the ɔ from a→ɔ should
        NOT then go to o in the same pass."""
        # In a single word with stressed /a/ only, we should get ɔ, not o
        result = apply_transform("ˈka", "algarve_barlavento", debias=False)
        assert "ɔ" in result and result != "ˈko"

    def test_ei_monophthong(self):
        result = apply_transform("ˈlejtu", "algarve_barlavento", debias=False)
        assert "ej" not in result


# ---------------------------------------------------------------------------
# T-16: Galician transforms
# ---------------------------------------------------------------------------

class TestGalicianCommon:
    def test_betacism(self):
        result = apply_transform("ˈvakɐ", "galician", debias=False)
        assert "b" in result

    def test_sibilant_devoicing_palatal(self):
        """G2a: ʒ → ʃ."""
        result = apply_transform("ˈʒa", "galician", debias=False)
        assert "ʃ" in result and "ʒ" not in result

    def test_sibilant_devoicing_alveolar(self):
        """G2b: z → s."""
        result = apply_transform("ˈkazɐ", "galician", debias=False)
        assert "z" not in result

    def test_unstressed_reduction_undo(self):
        """G3a: unstressed ɨ → e."""
        result = apply_transform("ˈɡɾɐ̃dɨ", "galician", debias=False)
        # final ɨ is unstressed → e
        assert result.endswith("e")

    def test_unstressed_a_reduction_undo(self):
        """G3c: unstressed ɐ → a."""
        result = apply_transform("ˈkazɐ", "galician", debias=False)
        # final ɐ → a
        assert result.endswith("a")


class TestGalicianWest:
    def test_geada(self):
        """GW1: /ɡ/ → [x] (geada)."""
        result = apply_transform("ˈɡatu", "galician_west", debias=False)
        assert "x" in result and "ɡ" not in result

    def test_betacism_also_applies(self):
        result = apply_transform("ˈvakɐ", "galician_west", debias=False)
        assert "b" in result

    def test_sibilant_devoicing(self):
        result = apply_transform("ˈʒa", "galician_west", debias=False)
        assert "ʃ" in result


# ---------------------------------------------------------------------------
# T-16: Leonese enclave transforms
# ---------------------------------------------------------------------------

class TestLeoneseCOmmon:
    def test_betacism(self):
        result = apply_transform("ˈvakɐ", "leonese", debias=False)
        assert "b" in result

    def test_lh_yodization(self):
        """LEO3: ʎ → j."""
        result = apply_transform("ˈfiʎu", "leonese", debias=False)
        assert "j" in result and "ʎ" not in result

    def test_palatal_devoicing(self):
        """LEO4: ʒ → ʃ."""
        result = apply_transform("ˈʒa", "leonese", debias=False)
        assert "ʃ" in result and "ʒ" not in result

    def test_participle_syncope_word_final(self):
        """LEO5: word-final adu → aw."""
        result = apply_transform("fɐˈladu", "leonese", debias=False)
        assert "aw" in result or result.endswith("aw")


class TestRionorese:
    def test_betacism(self):
        result = apply_transform("ˈvakɐ", "rionorese", debias=False)
        assert "b" in result and "v" not in result

    def test_lh_yodization(self):
        result = apply_transform("ˈfiʎu", "rionorese", debias=False)
        assert "ʎ" not in result

    def test_article_substitution_with_ortho(self):
        """RIO_ART: orthographic 'o' → IPA 'al'."""
        result = apply_transform("u", "rionorese", ortho="o", debias=False)
        assert result == "al"

    def test_pronoun_substitution_with_ortho(self):
        """RIO_PRON: orthographic 'eu' → 'jew'."""
        result = apply_transform("ew", "rionorese", ortho="eu", debias=False)
        assert result == "jew"


class TestGuadramilese:
    def test_betacism(self):
        result = apply_transform("ˈvakɐ", "guadramilese", debias=False)
        assert "b" in result

    def test_pronoun_substitution(self):
        """GUA_PRON: 'eu' → 'jow'."""
        result = apply_transform("ew", "guadramilese", ortho="eu", debias=False)
        assert result == "jow"


# ---------------------------------------------------------------------------
# T-18: Integration — apply_transform() with debias pipeline
# ---------------------------------------------------------------------------

class TestApplyTransformAPI:
    def test_unknown_profile_raises(self):
        with pytest.raises(KeyError):
            apply_transform("ˈtɛstu", "nonexistent_profile")

    def test_returns_string(self):
        result = apply_transform("ˈveɾdɨ", "northern")
        assert isinstance(result, str)

    def test_debias_then_northern(self):
        """Pipeline: eSpeak Lisbon output → de-bias → Northern transform."""
        # Simulate eSpeak output with β and v
        espeak_out = "u βɛˈʎu ˈveɾdɨ"
        result = apply_transform(espeak_out, "northern", debias=True)
        # β → b (de-biased), v → b (betacism)
        assert "β" not in result
        assert "v" not in result

    def test_debias_skipped_for_lisbon(self):
        """Lisbon profile has requires_debiasing=False — debias not applied
        even when debias=True is passed."""
        # Input already in Lisbon form with ɐj
        ipa = "ˈlɐjtɨ"
        result = apply_transform(ipa, "lisbon", debias=True)
        # Lisbon profile re-applies LX1 (ej→ɐj) but ɐj is already there
        # so result should still contain ɐj (not changed to ej by debias)
        assert "ɐj" in result

    def test_neutral_passthrough_estremenho(self):
        """Estremenho is the neutral dialect — no phonological changes."""
        ipa = "ˈveɾdɨ"
        result = apply_transform(ipa, "estremenho", debias=False)
        assert result == ipa

    def test_multiword_betacism(self):
        result = apply_transform("u ˈvɛʎu ˈveɾdɨ", "northern", debias=False)
        assert "v" not in result

    def test_available_profiles_returns_list(self):
        profiles = available_profiles()
        assert isinstance(profiles, list)
        assert len(profiles) >= 13

    def test_top_level_import(self):
        """apply_transform, debias_lisbon, DIALECT_PROFILES accessible from top."""
        import orthography2ipa
        assert hasattr(orthography2ipa, "apply_transform")
        assert hasattr(orthography2ipa, "debias_lisbon")
        assert hasattr(orthography2ipa, "DIALECT_PROFILES")


class TestVowelSet:
    def test_vowels_in_set(self):
        for v in "aeɛɐiɨoɔu":
            assert v in VOWEL_SET

    def test_consonants_not_in_set(self):
        for c in "bdfɡkmnpstvʃʒ":
            assert c not in VOWEL_SET
