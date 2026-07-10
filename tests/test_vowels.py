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
