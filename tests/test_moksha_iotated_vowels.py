"""Cited-rule tests for the Moksha (``mdf``) iotated vowel letters ⟨е ё ю я⟩.

Moksha writes palatalisation the Russian way, so each of the four letters has
two values: after a consonant letter it is the vowel and palatalises that
consonant, and elsewhere it is /j/ plus the vowel. The spec cites the
description of the modern Mordvin alphabet for both values. Every test word is
in the WikiPron Moksha gold, and the expected glide is the one the gold writes.
"""

from orthography2ipa.g2p import G2P


def mdf(word: str) -> str:
    return G2P("mdf").transcribe_word(word)


def test_an_iotated_letter_at_the_start_of_a_word_is_j_plus_vowel():
    """Gold ⟨ялга⟩ [j a l ɡ a], ⟨юр⟩ [j u r], ⟨ёр⟩ [j o r]."""
    assert mdf("ялга") == "jalɡa"
    assert mdf("юр") == "jur"
    assert mdf("ёр") == "jor"


def test_an_iotated_letter_after_a_vowel_is_j_plus_vowel():
    """Gold ⟨лия⟩ [lʲ i j æ], ⟨уемс⟩ [u j ə m s]: the glide sits between the
    two vowels, and no palatalisation mark follows the vowel."""
    for word in ("лия", "уемс"):
        assert "ʲ" not in mdf(word)
    assert mdf("лия").startswith("lij")
    assert mdf("уемс").startswith("uj")


def test_an_iotated_letter_after_a_consonant_palatalises_it():
    """Gold ⟨пеель⟩ [pʲ e j e lʲ] and ⟨шяярь⟩ [ʃʲ æ j æ rʲ] carry both
    values in one word: the first letter palatalises the consonant, and the
    second, after a vowel, is j plus the vowel."""
    assert mdf("пеель") == "pʲejelʲ"
    assert mdf("шяярь").startswith("ʃʲaj")


def test_an_iotated_letter_after_the_soft_sign_is_j_plus_vowel():
    """⟨ь⟩ palatalises the consonant before it, so the iotated letter after
    it has no consonant to palatalise: gold ⟨кундья⟩ [k u nʲ dʲ j ɑ]."""
    assert mdf("кундья").endswith("dʲja")
