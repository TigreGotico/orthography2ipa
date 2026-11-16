"""Hmong Daw (mww): RPA word-final consonant letters spell tone.

RPA (Smalley, Barney & Bertrais 1953) writes every syllable as
(onset)(rhyme)(tone letter): the seven letters b/j/v/s/g/m/d that can
follow the rhyme spell one of eight tones rather than a coda consonant,
and a rhyme with none of them is the mid tone, unmarked (Smalley 1976;
Ratliff 2010, *Hmong-Mien Language History*, ch. 4). Three of those seven
letters (b/j/g) never spell an onset consonant, so they carry their tone
mark unconditionally; the other four (s/v/m/d) are homographs of onset
consonants and only spell tone in the rhyme-final slot the engine's
``positional_graphemes: after_vowel`` matches.

These expectations are read directly off the WikiPron gold
(``.benchmark_cache/mww_latn_broad.tsv``), which is itself checked
against the RPA tone letter table in the spec's own ``tone_inventory``.
"""
import pytest

from orthography2ipa.g2p import G2P


@pytest.fixture(scope="module")
def mww():
    return G2P("mww")


def say(g2p, word):
    return g2p.transcribe_word(word)


@pytest.mark.parametrize("word,expected", [
    # b/j/g never spell an onset: their tone mark is unconditional.
    ("Hmoob", "m̥ɒ̃˥"),        # -b high
    # s/v/m/d are onset homographs: after_vowel is the tone slot.
    ("Fav", "fa˧˦"),          # -v mid-rising
    ("Hinplus", "hi˧ᵐbˡu˩"),  # -s low, mid-tone syllable before it
    # An unmarked rhyme (no final tone letter) carries the mid tone ˧
    # on every syllable, including polysyllabic loanwords.
    ("Amelika", "a˧me˧li˧ka˧"),
])
def test_tone_letters_resolve_to_chao_marks(mww, word, expected):
    assert say(mww, word) == expected


def test_onset_homograph_still_reads_as_a_consonant_intervocalically(mww):
    # The same letters (s/m/v/d) keep their plain consonant value when
    # they open a following syllable rather than closing the one before,
    # which `positional_graphemes: intervocalic` disambiguates from the
    # tone-bearing after_vowel slot.
    assert say(mww, "Amelika") == "a˧me˧li˧ka˧"
