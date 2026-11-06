"""⟨uei⟩ after a consonant is the glide [w] and the diphthong of ⟨ei⟩.

Infopédia reads bueiro [ˈbwɐjru], cueiro [ˈkwɐjru] and cajueiro [kaˈʒwɐjru]: the
stress falls on the syllable that holds ⟨ei⟩, and the vowel is the vowel of
feira [ˈfɐjrɐ], never the open [ɛ]. pt-PT-x-lisbon has that [ɐj] as its ⟨ei⟩.
Every other Portuguese spec reads the ⟨ei⟩ of its own table, so the expected
diphthong comes from the reading of feira in the same spec.

Infopédia has no row for the verb forms in ⟨-uei⟩. They take the same grapheme,
so they follow the same reading.
"""
import re

import pytest

from orthography2ipa import G2P
from orthography2ipa.registry import available_codes, get

PORTUGUESE_SPECS = sorted(
    code for code in available_codes()
    if "uei" in get(code).graphemes and not code.startswith("gl-")
)


def reading(word: str, lang: str) -> str:
    return G2P(lang, expose_ambiguous_endings=False).transcribe_word(word)


def diphthong_of_ei(lang: str) -> str:
    return re.fullmatch("ˈf(.+)[ɾr][ɐa]", reading("feira", lang)).group(1)


@pytest.mark.parametrize("lang, word, ipa", [
    ("pt-BR", "bueiro", "ˈbwejɾu"),
    ("pt-BR", "cueiro", "ˈkwejɾu"),
    ("pt-PT-x-lisbon", "bueiro", "ˈbwɐjɾu"),
    ("pt-PT-x-lisbon", "cueiro", "ˈkwɐjɾu"),
])
def test_the_reading_of_a_uei_word(lang, word, ipa):
    assert reading(word, lang) == ipa


def test_the_plural_has_the_same_segments():
    assert reading("bueiros", "pt-BR").replace("ˈ", "") == "bwejɾus"


@pytest.mark.parametrize("lang", PORTUGUESE_SPECS)
def test_uei_has_the_diphthong_of_ei(lang):
    assert reading("bueiro", lang).startswith(f"ˈbw{diphthong_of_ei(lang)}")


@pytest.mark.parametrize("lang", PORTUGUESE_SPECS)
def test_a_verb_form_in_uei_has_the_diphthong_of_ei(lang):
    assert reading("continuei", lang).endswith(f"ˈnw{diphthong_of_ei(lang)}")
