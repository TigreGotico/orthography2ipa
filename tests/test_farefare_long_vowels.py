"""Farefare (gur): doubled vowel letters are long vowels, ⟨ɣ⟩ is [ɣ].

The words and their IPA are the examples in the ``farefare_wiki`` source
(Wikipedia, "Farefare language", vowel table), with the source's ⟨ɹ⟩ written
as this spec's tap [ɾ]. The gold counts are in the ``gur`` spec notes and PR.
"""
import pytest

from orthography2ipa import G2P

GUR = G2P("gur")


@pytest.mark.parametrize("word, expected", [
    ("piika", "piːka"),
    ("buulika", "buːlika"),
    ("ɔɔrɔ", "ɔːɾɔ"),
    ("taablɩ", "taːblɪ"),
    ("teebʋl", "teːbʊl"),
])
def test_doubled_vowel_letter_is_one_long_vowel(word, expected):
    assert GUR.transcribe_word(word).lstrip("ˈ") == expected


def test_ghain_letter_is_read():
    assert GUR.transcribe_word("dɔɣɔta").lstrip("ˈ") == "dɔɣɔta"


@pytest.mark.parametrize("word, expected", [
    ("ya", "ja"),          # the source's /a/ row: ya /ja/ 'houses'
    ("gaarɛ", "ɡaːɾɛ"),    # its /aː/ row: gaarɛ /gaːɹɛ/, long then short
])
def test_single_vowel_letters_stay_short(word, expected):
    # The earlier guard used ⟨toma⟩, which the same table writes
    # /to:.ma.to:.ma/ with a LONG o, so it never guarded anything.
    assert GUR.transcribe_word(word).lstrip("ˈ") == expected
