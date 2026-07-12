"""Tests for orthography2ipa.vowels — shared vowel-classification predicates.

Validates:
- Latin orthographic vowels (bare + accented forms)
- Greek orthographic vowels
- IPA vowel symbols
- Consonants/non-vowels return False for both predicates
- No character previously recognised by g2p._VOWEL_CHARS,
  phonetok._vowels, or stress._VOWELS was dropped
"""
import pytest

from orthography2ipa.g2p import transcribe
from orthography2ipa.vowels import is_ipa_vowel, is_orthographic_vowel


# ═══════════════════════════════════════════════════════════════════════════
# Orthographic vowels
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("ch", list("aeiouAEIOU"))
def test_bare_latin_vowels_are_orthographic(ch):
    assert is_orthographic_vowel(ch)


@pytest.mark.parametrize("ch", ["á", "ä", "ô", "é", "î", "ü", "ã", "õ", "å", "æ", "ø"])
def test_accented_latin_vowels_are_orthographic(ch):
    assert is_orthographic_vowel(ch)


@pytest.mark.parametrize("ch", ["ã", "ẽ", "ĩ", "õ", "ũ"])
def test_precomposed_nasal_vowels_are_orthographic(ch):
    # The written nasal vowels are a single orthographic-vowel source of
    # truth: ã/õ were already recognised, but the precomposed ẽ (U+1EBD),
    # ĩ (U+0129) and ũ (U+0169) must be too — Portuguese-family orthographies
    # write them and the vowel predicate must not treat them as non-vowels.
    assert is_orthographic_vowel(ch)


@pytest.mark.parametrize("ch", ["ẽ", "ĩ"])
def test_precomposed_nasal_front_vowels_axis(ch):
    # Nasalisation (combining tilde) preserves the front/back axis, so ẽ/ĩ
    # classify front by their base ⟨e⟩/⟨i⟩.
    from orthography2ipa.vowels import is_back_vowel, is_front_vowel
    assert is_front_vowel(ch)
    assert not is_back_vowel(ch)


@pytest.mark.parametrize("ch", ["ã", "õ", "ũ"])
def test_precomposed_nasal_back_vowels_axis(ch):
    # ã/õ/ũ classify back by their base ⟨a⟩/⟨o⟩/⟨u⟩ (tilde preserves the axis).
    from orthography2ipa.vowels import is_back_vowel, is_front_vowel
    assert is_back_vowel(ch)
    assert not is_front_vowel(ch)


@pytest.mark.parametrize("ch", list("αεηιουω"))
def test_greek_vowels_are_orthographic(ch):
    assert is_orthographic_vowel(ch)


@pytest.mark.parametrize("ch", ["ά", "έ", "ή", "ί", "ό", "ύ", "ώ", "ΐ", "ΰ"])
def test_accented_greek_vowels_are_orthographic(ch):
    assert is_orthographic_vowel(ch)


def test_orthographic_vowel_check_is_case_insensitive():
    assert is_orthographic_vowel("A")
    assert is_orthographic_vowel("Á")


# ═══════════════════════════════════════════════════════════════════════════
# IPA vowels
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("ch", ["ɛ", "ɔ", "ə", "ɨ", "ʉ", "ɐ", "ʌ", "ɒ", "ɪ", "ʊ", "ɤ", "ɑ"])
def test_ipa_vowel_symbols(ch):
    assert is_ipa_vowel(ch)


@pytest.mark.parametrize("ch", list("aeiou"))
def test_bare_latin_letters_are_also_ipa_vowels(ch):
    assert is_ipa_vowel(ch)


@pytest.mark.parametrize("ch", ["ã", "ẽ", "ĩ", "õ", "ũ"])
def test_precomposed_nasal_vowels_are_ipa_vowels(ch):
    assert is_ipa_vowel(ch)


# ═══════════════════════════════════════════════════════════════════════════
# Consonants / non-vowels
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("ch", list("bcdfghjklmnpqrstvwxz"))
def test_latin_consonants_are_not_vowels(ch):
    assert not is_orthographic_vowel(ch)
    assert not is_ipa_vowel(ch)


@pytest.mark.parametrize("ch", ["β", "γ", "δ", "θ", "κ", "λ", "μ", "ν", "π", "τ", "χ", "ψ"])
def test_greek_consonants_are_not_orthographic_vowels(ch):
    assert not is_orthographic_vowel(ch)


@pytest.mark.parametrize("ch", ["p", "t", "k", "s", "ʃ", "ʒ", "ʁ", "ʔ", "ŋ", "θ", "ð"])
def test_ipa_consonants_are_not_ipa_vowels(ch):
    assert not is_ipa_vowel(ch)


def test_empty_string_is_not_a_vowel():
    assert not is_orthographic_vowel("")
    assert not is_ipa_vowel("")


# ═══════════════════════════════════════════════════════════════════════════
# Regression: no coverage dropped from the three consolidated sets
# ═══════════════════════════════════════════════════════════════════════════

# Verbatim copy of the set g2p.py's `_VOWEL_CHARS` held before consolidation.
_OLD_G2P_VOWEL_CHARS = frozenset(
    "aeiouáéíóúàèìòùâêîôûãõäëïöüåæøAEIOUÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÄËÏÖÜÅÆØ"
)

# Verbatim copy of the set phonetok.py's inherent-vowel heuristic held
# before consolidation.
_OLD_PHONETOK_VOWELS = set("aeiouɛɔəɨʉɯæɐʌɒœøɪʊɤɵɞɑ")

# Verbatim copy of the set stress.py's `_VOWELS` held before consolidation.
_OLD_STRESS_VOWELS = set(
    "aeiou"
    "áéíóúàèìòùâêîôûãõäëïöüåæø"
    "ąęėįųūīāēőűýěůŏŭıå"
    "ɐɑɒɔəɘɚɛɜɝɞɪɨɵøœɶʊʉʌyɤeiou̯ãẽĩõũɐ̃"
    "αεηιουωάέήίόύώΐΰ"
)


def test_new_orthographic_predicate_is_superset_of_old_g2p_set():
    for ch in _OLD_G2P_VOWEL_CHARS:
        assert is_orthographic_vowel(ch), f"dropped {ch!r} from g2p._VOWEL_CHARS"


def test_new_ipa_predicate_is_superset_of_old_phonetok_set():
    for ch in _OLD_PHONETOK_VOWELS:
        assert is_ipa_vowel(ch), f"dropped {ch!r} from phonetok._vowels"


def test_new_predicates_are_superset_of_old_stress_set():
    for ch in _OLD_STRESS_VOWELS:
        assert is_orthographic_vowel(ch) or is_ipa_vowel(ch), \
            f"dropped {ch!r} from stress._VOWELS"


# ═══════════════════════════════════════════════════════════════════════════
# Integration: Malayalam abugida inherent-vowel heuristic
# ═══════════════════════════════════════════════════════════════════════════

def test_malayalam_anusvara_keeps_inherent_vowel_matra_replaces_it():
    # \u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02 exercises both halves of the abugida inherent-vowel rule:
    #
    #   \u0d2f + \u0d3e  a dependent vowel sign SUPPLIES the syllable's vowel, so the
    #          inherent vowel is cancelled rather than added to \u2192 "ja\u02d0",
    #          not "jaa\u02d0".
    #   \u0d33 + \u0d02  the anusvara's IPA opens with a combining tilde, a diacritic
    #          that MODIFIES a vowel without supplying one \u2014 so \u0d33 keeps its
    #          inherent vowel for the tilde to attach to \u2192 "\u026da\u0303m".
    #
    # The pipeline emits NFD (bare "a" + combining tilde U+0303); build the
    # expected string from escapes to keep the combining char unambiguous.
    expected = "malaja\u02d0\u026da\u0303m"
    assert transcribe("\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02", "ml") == expected


# ═══════════════════════════════════════════════════════════════════════════
# Greek front/back axis (velar palatalization depends on it)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("ch", list("εηιυ") + ["έ", "ή", "ί", "ύ", "ϊ", "ϋ", "ΐ", "ΰ"])
def test_greek_front_vowels_axis(ch):
    # Modern Greek ε η ι υ are all front (υ by iotacism; Holton,
    # Mackridge & Philippaki-Warburton ch. 1.1); the acute and the
    # dialytika preserve the axis.
    from orthography2ipa.vowels import is_back_vowel, is_front_vowel
    assert is_front_vowel(ch)
    assert not is_back_vowel(ch)


@pytest.mark.parametrize("ch", list("αοω") + ["ά", "ό", "ώ"])
def test_greek_back_vowels_axis(ch):
    from orthography2ipa.vowels import is_back_vowel, is_front_vowel
    assert is_back_vowel(ch)
    assert not is_front_vowel(ch)


class TestGreekPhonology:
    """Modern Greek spec behaviors that ride on the axis fix + the el
    spec overhaul (Arvaniti 2007, JIPA Illustrations: Standard Modern
    Greek; Holton, Mackridge & Philippaki-Warburton ch. 1)."""

    @staticmethod
    def _t(w):
        from orthography2ipa.g2p import transcribe as _tr
        return _tr(w, "el").replace("ˈ", "")

    def test_velar_palatalization_before_front_vowel(self):
        assert self._t("Άκης") == "acis"          # κ → [c]
        assert self._t("χέρι") == "çeɾi"           # χ → [ç]
        assert self._t("Αγγελική") == "aŋɟelici"   # γγ → [ŋɟ]

    def test_velars_stay_plain_before_back_vowels(self):
        assert self._t("καλός") == "kalos"
        assert self._t("γάτα") == "ɣata"

    def test_accented_digraph_is_one_vowel(self):
        assert self._t("αίμα") == "ema"            # αί = /e/
        assert self._t("Αδριανούπολη") == "aðɾianupoli"  # ού = /u/

    def test_s_voices_before_voiced_consonant(self):
        assert self._t("κόσμος") == "kozmos"

    def test_double_consonants_degeminate(self):
        assert self._t("Έλλην") == "elin"

    def test_nasal_stop_digraphs_positional(self):
        assert self._t("Όλυμπος") == "olimbos"     # medial μπ = [mb]
        assert self._t("μπάλα").startswith("b")    # initial μπ = [b]

    def test_rho_is_a_tap(self):
        assert self._t("ρόδα") == "ɾoða"
