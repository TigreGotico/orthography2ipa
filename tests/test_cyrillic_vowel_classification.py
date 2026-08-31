"""Cyrillic and Greek vowel-letter classification.

``_ORTHOGRAPHIC_VOWELS`` closes the inventories of the scripts it names:
:func:`grapheme_is_vowel` refuses to consult a spec's own IPA for a
character whose script the sets claim to enumerate exhaustively. Cyrillic
and Greek are two such scripts, so any vowel letter missing from the sets
is not merely unclassified — it is positively classified as a consonant,
and no spec can override that through its grapheme table.

Two distinct classes of letter were missing.
"""

import unicodedata

import pytest

from orthography2ipa.vowels import (
    grapheme_is_vowel,
    is_orthographic_vowel,
)


# Atomic Cyrillic vowel letters — these have no canonical decomposition, so
# no NFD-base rule can reach them; they must be named.
ATOMIC_CYRILLIC_VOWELS = "әөүұӕ"

# Cyrillic and Greek vowel letters that DO decompose to a vowel letter the
# sets already name, under marks that are pure diacritics.
DECOMPOSING_VOWELS = "ӓӑӗӥӣӧӱӯӳӭӹϊϋᾱῑῡἀἐἰὀὐἠὠ"


@pytest.mark.parametrize("ch", ATOMIC_CYRILLIC_VOWELS)
def test_atomic_cyrillic_vowel_letters(ch):
    assert is_orthographic_vowel(ch)
    assert is_orthographic_vowel(ch.upper())


@pytest.mark.parametrize("ch", DECOMPOSING_VOWELS)
def test_decomposing_vowel_letters_classify_by_nfd_base(ch):
    assert unicodedata.normalize("NFD", ch) != ch, "test premise: ch decomposes"
    assert is_orthographic_vowel(ch)


@pytest.mark.parametrize("ch", ATOMIC_CYRILLIC_VOWELS + DECOMPOSING_VOWELS)
def test_closed_inventory_no_longer_calls_them_consonants(ch):
    """The live consequence: with the letter absent, ``grapheme_is_vowel``
    early-outs on the closed Cyrillic/Greek inventory and never reaches the
    spec's own IPA, so the letter cannot be a syllable nucleus."""
    assert grapheme_is_vowel(ch, ["a"])


@pytest.mark.parametrize("ch", "йў")
def test_cyrillic_glides_stay_consonants(ch):
    """⟨й⟩ decomposes to ⟨и⟩ plus a breve and ⟨ў⟩ to ⟨у⟩ plus a breve, but
    both are glides. A base-character rule must not readmit them."""
    assert not is_orthographic_vowel(ch)
    assert not is_orthographic_vowel(ch.upper())


@pytest.mark.parametrize("ch", "ъь")
def test_cyrillic_signs_stay_non_vowels(ch):
    """The yer signs remain outside the vowel sets, as before. Bulgarian
    ⟨ъ⟩ = /ɤ/ is a genuine vowel and is reached through a spec's
    ``vowel_graphemes`` declaration, not through the shared letter sets."""
    assert not is_orthographic_vowel(ch)


def test_kazakh_alphabet_vowels_all_classify():
    """Every vowel letter of the Kazakh Cyrillic alphabet."""
    for ch in "аәеёиоөуұүыіэюя":
        assert is_orthographic_vowel(ch), ch
