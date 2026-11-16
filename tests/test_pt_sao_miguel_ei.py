"""São Miguel reduces the falling diphthong ⟨ei⟩ to [e].

Cunha & Cintra (7th ed., p. 31) write of the Atlantic islands that the
reduction of [ej] to [e] "só ocorre como norma na ilha de São Miguel". The
other island specs and generic pt-PT keep [ej]. Before a vowel the glide
begins the next syllable, and the source does not cover that position, so
there the spec keeps the pt-PT value [ej]. A nasal ⟨ei⟩ before a coda nasal
keeps it too.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P

SPEC = "pt-PT-x-sao-miguel"

#: The pt-PT reading with the glide removed. The words hold no ⟨u⟩, ⟨oi⟩,
#: ⟨ou⟩ or ⟨il⟩, so no other São Miguel rule touches them.
MONOPHTHONG = {
    "leite": "ˈletɨ",
    "peixe": "ˈpeʃɨ",
    "primeiro": "pɾiˈmeɾu",
    "feira": "ˈfeɾɐ",
    "lei": "ˈle",
    "queijo": "ˈkeʒu",
    "seis": "ˈseʃ",
    "madeira": "mɐˈdeɾɐ",
    "reino": "ˈʁenu",
    "deixar": "deˈʃaɾ",
    "beijinho": "beˈʒiɲu",
    "enxaguei": "ẽʃɐˈɡe",
    "cajueiro": "kɐˈʒweɾu",
    "atueira": "ɐˈtweɾɐ",
    "continuei": "kõtiˈnwe",
    "sei": "ˈse",
    "amêijoa": "ɐˈmeʒuɐ",
    "gêiser": "ˈʒezɨɾ",
}

#: ⟨ei⟩ before a vowel keeps the glide, as in pt-PT.
HIATUS = {
    "cheia": "ˈʃejɐ",
    "ideia": "iˈdejɐ",
    "veia": "ˈvejɐ",
    "meio": "ˈmeju",
}

#: The specs that keep the pt-PT diphthong.
KEEP_EJ = ["pt-PT", "pt-PT-x-acores", "pt-PT-x-terceira", "pt-PT-x-madeira"]


@pytest.mark.parametrize("word,ipa", sorted(MONOPHTHONG.items()))
def test_falling_ei_is_a_monophthong(word: str, ipa: str) -> None:
    assert G2P(SPEC).transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", sorted(MONOPHTHONG.items()))
def test_monophthong_is_the_standard_without_the_glide(word: str, ipa: str) -> None:
    standard = G2P("pt-PT").transcribe_word(word)
    assert "ej" in standard
    assert standard.replace("ej", "e") == ipa


@pytest.mark.parametrize("word,ipa", sorted(HIATUS.items()))
def test_ei_before_a_vowel_keeps_the_glide(word: str, ipa: str) -> None:
    assert G2P(SPEC).transcribe_word(word) == ipa
    assert G2P("pt-PT").transcribe_word(word) == ipa


#: A plain ⟨e⟩ before a vowel is not the diphthong, so it takes no glide.
PLAIN_E_BEFORE_VOWEL = {
    "eolítico": "euˈlitiku",
    "eanismo": "eɐˈniʒmu",
    "Eoceno": "euˈsɛnu",
}


@pytest.mark.parametrize("word,ipa", sorted(PLAIN_E_BEFORE_VOWEL.items()))
def test_plain_e_before_a_vowel_takes_no_glide(word: str, ipa: str) -> None:
    assert G2P(SPEC).transcribe_word(word) == ipa
    assert G2P("pt-PT").transcribe_word(word) == ipa


#: A nasal ⟨ei⟩ before a coda nasal is not the oral diphthong of the source.
NASAL_EI = ["hein", "holstein", "reimplantar", "reincidente"]


@pytest.mark.parametrize("word", NASAL_EI)
def test_nasal_ei_keeps_the_standard_reading(word: str) -> None:
    ipa = G2P(SPEC).transcribe_word(word)
    assert ipa == G2P("pt-PT").transcribe_word(word)
    assert "ej̃" in ipa


def test_open_ei_keeps_its_glide() -> None:
    assert G2P(SPEC).transcribe_word("papéis") == "pɐˈpɛjʃ"


@pytest.mark.parametrize("spec", KEEP_EJ)
@pytest.mark.parametrize("word", ["leite", "peixe", "primeiro", "lei"])
def test_other_specs_keep_the_diphthong(spec: str, word: str) -> None:
    assert "ej" in G2P(spec).transcribe_word(word)


def test_lisbon_keeps_its_centralised_diphthong() -> None:
    assert G2P("pt-PT-x-lisbon").transcribe_word("leite") == "ˈlɐjtɨ"


@pytest.mark.parametrize("sentence,ipa", [
    ("o leite do primeiro queijo", "u ˈletɨ du pɾiˈmeɾu ˈkeʒu"),
    ("a feira de seis de maio", "ɐ ˈfeɾɐ dɨ ˈseʒ dɨ ˈmaju"),
])
def test_sentence(sentence: str, ipa: str) -> None:
    assert G2P(SPEC).transcribe(sentence) == ipa
