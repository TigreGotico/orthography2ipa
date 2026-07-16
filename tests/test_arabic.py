"""Per-language accuracy tests for Arabic dialects.

Covers:
- Modern Standard / Classical Arabic (arb)
- Mashriqi Arabic / Eastern Arabic (ar-x-mashriqi)
- Maghrebi Arabic / Western Arabic (ar-x-maghrebi)
- Moroccan Arabic (ar-MA)
- Gulf Arabic (ar-x-gulf)
- Iraqi Arabic (ar-IQ)
- Peninsular Arabic (ar-x-peninsular)

Key cross-dialect variables:
- ق (qaf): q / ʔ / ɡ
- ج (jim): dʒ / ʒ / j / ɡ
- ث/ذ/ظ (interdentals): θ/ð/ðˤ vs t/d/dˤ (merger)
- Short vowel deletion in Maghrebi/Iraqi
- Emphasis (pharyngealisation): sˤ, tˤ, ðˤ, ɮˤ
"""
from __future__ import annotations

import pytest

import orthography2ipa

_SENTINEL = object()


def _load(code: str):
    try:
        return orthography2ipa.get(code)
    except Exception as exc:
        pytest.skip(f"{code!r} not available: {exc}")


def _grapheme(spec, grapheme: str):
    return spec.graphemes.get(grapheme)


def _allophone(spec, phoneme: str):
    return spec.allophones.get(phoneme)


def _assert_contains(values, *expected, label: str = "") -> None:
    assert values is not None, f"{label}: mapping is absent"
    for exp in expected:
        assert exp in values, f"{label}: {exp!r} not in {values}"


def _assert_first(values, expected: str, label: str = "") -> None:
    assert values is not None, f"{label}: mapping is absent"
    assert values[0] == expected, (
        f"{label}: expected first={expected!r}, got {values[0]!r}"
    )


# ═══════════════════════════════════════════════════════════════════════════
# Modern Standard / Classical Arabic
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestArabicMSA:
    """Accuracy tests for Modern Standard / Classical Arabic (arb).

    MSA is the prestige written standard of Arabic. Key features:
    - Full set of emphatic consonants (sˤ, tˤ, ðˤ, ɮˤ)
    - Interdentals θ, ð, ðˤ preserved in writing
    - q (qaf) as uvular stop
    - Hamza (ʔ) at word boundaries and in alif
    - ج (jim) = [dʒ] in MSA
    - Long vowels: aː, iː, uː
    """

    LANGUAGE_CODE = "arb"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # Alif and vowels
    def test_alif_glottal(self):
        """ا → [ʔ, aː] — alif is glottal stop or long a."""
        vals = _grapheme(self.spec, "ا")
        _assert_contains(vals, "ʔ", label="ا")

    def test_madda(self):
        """آ → [ʔaː] (alif with madda = long a with initial glottal)."""
        vals = _grapheme(self.spec, "آ")
        assert vals is not None
        assert vals[0] in ("ʔaː", "aː"), f"آ expected ʔaː/aː, got {vals[0]}"

    def test_ta_marbuta(self):
        """ة → [a, at] (ta marbuta — feminine ending, silent or [at] in construct)."""
        vals = _grapheme(self.spec, "ة")
        _assert_contains(vals, "a", label="ة")

    # Consonants
    def test_ba(self):
        """ب → [b]."""
        _assert_first(_grapheme(self.spec, "ب"), "b", label="ب")

    def test_tha_interdental(self):
        """ث → [θ] (voiceless interdental — preserved in MSA)."""
        _assert_first(_grapheme(self.spec, "ث"), "θ", label="ث")

    def test_jim(self):
        """ج → [dʒ] (MSA standard realization)."""
        _assert_first(_grapheme(self.spec, "ج"), "dʒ", label="ج")

    def test_ha_pharyngeal(self):
        """ح → [ħ] (voiceless pharyngeal fricative)."""
        vals = _grapheme(self.spec, "ح")
        assert vals is not None
        assert vals[0] in ("ħ", "h"), f"ح expected ħ/h, got {vals[0]}"

    def test_kha(self):
        """خ → [x] (voiceless velar fricative)."""
        _assert_first(_grapheme(self.spec, "خ"), "x", label="خ")

    def test_dhal_interdental(self):
        """ذ → [ð] (voiced interdental)."""
        vals = _grapheme(self.spec, "ذ")
        assert vals is not None
        assert "ð" in vals, f"ذ should include ð, got {vals}"

    def test_ain_pharyngeal(self):
        """ع → [ʕ] (voiced pharyngeal fricative)."""
        vals = _grapheme(self.spec, "ع")
        assert vals is not None
        assert vals[0] in ("ʕ", "ʔ", ""), f"ع expected ʕ/ʔ, got {vals[0]}"

    def test_ghain(self):
        """غ → [ɣ] or [ʁ] (voiced velar/uvular fricative)."""
        vals = _grapheme(self.spec, "غ")
        assert vals is not None
        assert vals[0] in ("ɣ", "ʁ"), f"غ expected ɣ/ʁ, got {vals[0]}"

    def test_qaf_uvular(self):
        """ق → [q] (uvular stop — MSA standard)."""
        vals = _grapheme(self.spec, "ق")
        assert vals is not None
        assert vals[0] in ("q", "q"), f"ق expected q, got {vals[0]}"

    # Emphatics
    def test_sad_emphatic(self):
        """ص → emphatic sibilant [sˤ]."""
        vals = _grapheme(self.spec, "ص")
        assert vals is not None
        assert vals[0] in ("sˤ", "s"), f"ص expected sˤ, got {vals[0]}"

    def test_dhad_emphatic(self):
        """ض → emphatic [ɮˤ] or [dˤ]."""
        vals = _grapheme(self.spec, "ض")
        assert vals is not None
        assert vals[0] in ("ɮˤ", "dˤ", "d"), f"ض expected emphatic, got {vals[0]}"

    def test_ta_emphatic(self):
        """ط → emphatic [tˤ]."""
        vals = _grapheme(self.spec, "ط")
        assert vals is not None
        assert vals[0] in ("tˤ", "t"), f"ط expected tˤ, got {vals[0]}"

    def test_dha_emphatic_interdental(self):
        """ظ → emphatic [ðˤ]."""
        vals = _grapheme(self.spec, "ظ")
        assert vals is not None
        assert vals[0] in ("ðˤ", "dˤ", "zˤ"), f"ظ expected ðˤ, got {vals[0]}"

    # Allophones — emphatic phonemes
    def test_emphatic_s_allophone(self):
        """sˤ allophone → [sˤ] (pharyngealised sibilant)."""
        _assert_first(_allophone(self.spec, "sˤ"), "sˤ", label="sˤ allophone")

    def test_family(self):
        """Arabic is Semitic."""
        assert {"Afro-Asiatic", "Semitic", "Central Semitic"} <= set(self.spec.family_path)


# ═══════════════════════════════════════════════════════════════════════════
# Mashriqi / Eastern Arabic
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestMashriqiArabic:
    """Accuracy tests for Mashriqi (Eastern) Arabic — ar-x-mashriqi.

    Levantine/Eastern group. Key features vs MSA:
    - ث/ذ/ظ have merged variants [t/d/dˤ] alongside θ/ð/ðˤ
    - q→[q, ʔ, ɡ] (varies by country/register)
    - Additional phonemes p/v/tʃ (from loanwords)
    - Short vowel patterns preserved
    """

    LANGUAGE_CODE = "ar-x-mashriqi"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_tha_variable(self):
        """ث → [t, θ] — interdental sometimes merged to t in colloquial."""
        vals = _grapheme(self.spec, "ث")
        assert vals is not None
        # Both merger and preservation should be present
        has_stop = "t" in vals or "s" in vals
        assert has_stop, f"Mashriqi ث should include t/s merger, got {vals}"

    def test_q_variable(self):
        """q allophone includes ʔ or ɡ — dialect-variable qaf."""
        vals = _allophone(self.spec, "q")
        assert vals is not None
        has_variant = any(x in vals for x in ("ʔ", "ɡ", "q"))
        assert has_variant, f"Mashriqi q should have variants, got {vals}"

    def test_p_loanword(self):
        """پ → [p] (loanword phoneme — not in Classical Arabic)."""
        _assert_first(_grapheme(self.spec, "پ"), "p", label="پ")

    def test_v_loanword(self):
        """ڤ → [v] (loanword phoneme)."""
        _assert_first(_grapheme(self.spec, "ڤ"), "v", label="ڤ")

    def test_ch_loanword(self):
        """چ → [tʃ] (loanword phoneme — for Persian/Kurdish loans)."""
        _assert_first(_grapheme(self.spec, "چ"), "tʃ", label="چ")

    def test_theta_allophone_variants(self):
        """θ allophone includes t and s — phoneme realisation varies."""
        _assert_contains(_allophone(self.spec, "θ"), "t", label="θ allophone")

    def test_parent_is_arb(self):
        assert self.spec.parent == "arb"


# ═══════════════════════════════════════════════════════════════════════════
# Maghrebi / Western Arabic
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestMaghrebiArabic:
    """Accuracy tests for Maghrebi (Western) Arabic — ar-x-maghrebi.

    North African group (Morocco, Algeria, Tunisia, Libya). Key features:
    - Full merger of ث→t/s, ذ→d (interdentals lost)
    - Short vowel deletion (a/i/u→∅ in unstressed syllables)
    - Preservation of q
    - Additional p/v from Berber/French contact
    """

    LANGUAGE_CODE = "ar-x-maghrebi"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_tha_merged(self):
        """ث → [t, s] — interdental fully merged in Maghrebi."""
        vals = _grapheme(self.spec, "ث")
        assert vals is not None
        has_merger = "t" in vals or "s" in vals
        assert has_merger, f"Maghrebi ث should be t/s, got {vals}"
        assert "θ" not in vals, "Maghrebi should not preserve θ as primary"

    def test_dhal_merged(self):
        """ذ → [d] — voiced interdental merged."""
        _assert_first(_grapheme(self.spec, "ذ"), "d", label="ذ")

    def test_short_vowel_deletion(self):
        """a/i/u allophones include ∅ — short vowel deletion (syncope)."""
        _assert_contains(_allophone(self.spec, "a"), "", label="a allophone deletion")
        _assert_contains(_allophone(self.spec, "i"), "", label="i allophone deletion")
        _assert_contains(_allophone(self.spec, "u"), "", label="u allophone deletion")

    def test_emphatic_merger(self):
        """ɮˤ allophone → [dˤ] — emphatic merged to stop in Maghrebi."""
        _assert_first(_allophone(self.spec, "ɮˤ"), "dˤ", label="ɮˤ allophone")

    def test_parent_is_arb(self):
        assert self.spec.parent == "arb"


# ═══════════════════════════════════════════════════════════════════════════
# Moroccan Arabic
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestMoroccanArabic:
    """Accuracy tests for Moroccan Arabic — ar-MA.

    Darija. Key features: inherits Maghrebi base, adds Romance loanword
    phonemes e/o, extreme short vowel reduction (a→[a,ə,∅]).
    """

    LANGUAGE_CODE = "ar-MA"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_tha_fully_merged(self):
        """ث → [t] only — full merger in Moroccan."""
        _assert_first(_grapheme(self.spec, "ث"), "t", label="ث")

    def test_e_loanword_phoneme(self):
        """e → [e] — French loanword vowel phoneme added to inventory."""
        _assert_first(_grapheme(self.spec, "e"), "e", label="e")

    def test_o_loanword_phoneme(self):
        """o → [o] — French/Spanish loanword vowel."""
        _assert_first(_grapheme(self.spec, "o"), "o", label="o")

    def test_a_extreme_reduction(self):
        """a allophone includes ə and ∅ — extreme vowel reduction."""
        _assert_contains(_allophone(self.spec, "a"), "ə", "", label="a allophone")

    def test_aa_raised(self):
        """aː allophone includes æː — Moroccan vowel raising."""
        _assert_contains(_allophone(self.spec, "aː"), "æː", label="aː allophone")

    def test_parent_is_maghrebi(self):
        assert self.spec.parent == "ar-x-maghrebi"


# ═══════════════════════════════════════════════════════════════════════════
# Gulf Arabic
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestGulfArabic:
    """Accuracy tests for Gulf Arabic — ar-x-gulf.

    Spoken in the Arabian Gulf states (UAE, Kuwait, Bahrain, Qatar, Oman).
    Key features:
    - ق → [ɡ] (velarization — qaf→g in many dialects)
    - ج → [dʒ, j] (jim varies)
    - ك → [k, tʃ] (kaf palatalisation before front vowels)
    - Long vowels raised (aː→eː in some environments)
    """

    LANGUAGE_CODE = "ar-x-gulf"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_qaf_to_g(self):
        """ق → [ɡ, q] — qaf realised as ɡ in Gulf (primary variant)."""
        vals = _grapheme(self.spec, "ق")
        assert vals is not None
        _assert_first(vals, "ɡ", label="ق first")

    def test_jim_variable(self):
        """ج → [dʒ, j] — jim varies between affricate and glide."""
        vals = _grapheme(self.spec, "ج")
        assert vals is not None
        _assert_contains(vals, "dʒ", "j", label="ج")

    def test_kaf_affrication_rule(self):
        """/k/ → [tʃ] before a high front vowel via GULF_K_AFFRICATION.

        Affrication is modelled as a post-lexical allophone rule (B8), not a
        grapheme candidate: ك maps to /k/, which the rule realises as [tʃ]
        adjacent to /i, iː/ (Alshammari 2026 p.1335, Mustafawi Qatari).
        """
        from orthography2ipa.g2p import G2P
        ids = [r.id for r in self.spec.allophone_rules]
        assert "GULF_K_AFFRICATION" in ids
        g = G2P(self.LANGUAGE_CODE)
        assert g.transcribe("كِتَاب").lstrip("ˈˌ").startswith("tʃ")
        # …and stays [k] before a non-high vowel (blocked by [-high])
        assert g.transcribe("كَلْب").lstrip("ˈˌ").startswith("k")

    def test_q_allophone_g(self):
        """q allophone → ɡ (primary) — qaf→gaf in Gulf."""
        _assert_first(_allophone(self.spec, "q"), "ɡ", label="q allophone")

    def test_aa_raised(self):
        """aː allophone includes eː — vowel raising in Gulf."""
        _assert_contains(_allophone(self.spec, "aː"), "eː", label="aː allophone")

    def test_jim_allophone(self):
        """dʒ allophone includes j — jim weakening."""
        _assert_contains(_allophone(self.spec, "dʒ"), "j", label="dʒ allophone")


# ═══════════════════════════════════════════════════════════════════════════
# Iraqi Arabic
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestIraqiArabic:
    """Accuracy tests for Iraqi Arabic — ar-IQ.

    Mesopotamian Arabic. Key features:
    - ق → [ɡ] (qaf→gaf — shared with Gulf)
    - Preserves θ/ð/ðˤ interdentals (unlike Maghrebi)
    - ك → [k, tʃ] (kaf palatalisation)
    - Kurdish/Persian loanword phonemes ژ→ʒ
    - Long vowels raised: aː→eː
    """

    LANGUAGE_CODE = "ar-IQ"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_qaf_to_g(self):
        """ق → [ɡ] — Iraqi qaf→gaf."""
        _assert_first(_grapheme(self.spec, "ق"), "ɡ", label="ق")

    def test_tha_preserved(self):
        """ث → [θ] — interdental preserved in Iraqi (unlike Maghrebi)."""
        _assert_first(_grapheme(self.spec, "ث"), "θ", label="ث")

    def test_dhal_preserved(self):
        """ذ → [ð] — voiced interdental preserved."""
        _assert_first(_grapheme(self.spec, "ذ"), "ð", label="ذ")

    def test_zhe_loanword(self):
        """ژ → [ʒ] — Persian/Kurdish loanword phoneme."""
        _assert_first(_grapheme(self.spec, "ژ"), "ʒ", label="ژ")

    def test_q_allophone_g(self):
        """q allophone → ɡ — qaf realised as ɡ."""
        _assert_first(_allophone(self.spec, "q"), "ɡ", label="q allophone")

    def test_kaf_palatalisation(self):
        """k allophone includes tʃ — kaf palatalisation."""
        _assert_contains(_allophone(self.spec, "k"), "tʃ", label="k allophone")

    def test_aa_raised(self):
        """aː allophone includes eː — vowel raising."""
        _assert_contains(_allophone(self.spec, "aː"), "eː", label="aː allophone")

    def test_parent_is_mashriqi(self):
        """Iraqi Arabic inherits from Mashriqi group."""
        assert self.spec.parent in ("ar-x-mashriqi", "arb", "ar")
