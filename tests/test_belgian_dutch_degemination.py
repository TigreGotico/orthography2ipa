"""Belgian Dutch reads a doubled consonant letter as one consonant.

Source:

- J. Verhoeven, "Belgian Standard Dutch", *Journal of the International
  Phonetic Association* 35(2), 2005, p. 247. The broad transcription of the
  reading passage writes one consonant for each doubled letter: uittrekken
  [ʔœytrɛkə], induffelde [ɪndʏfəldə], onmiddellijk [ɔmɪdələk].

``collapse_geminates`` is not inherited, so ``nl-BE`` states it, as
``nl-NL`` does. The other segments keep the values the spec states
elsewhere; these tests check that each doubled letter gives one consonant.
"""
import json
from importlib import resources

import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def be():
    return G2P("nl-BE")


@pytest.mark.parametrize("word, ipa", [
    ("kennen", "ˈkɛnən"),
    ("zitten", "ˈzɪtən"),
    ("hebben", "ˈɦɛbən"),
    ("zeggen", "ˈzɛɣən"),
    ("bakken", "ˈbɑkən"),
    ("uittrekken", "ˈœytrəkən"),
    ("induffelde", "ˈɪndʏfəldə"),
])
def test_doubled_consonant_letter_is_one_consonant(be, word, ipa):
    assert be.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("zee", "ˈzeː"),
    ("kaas", "ˈkaːs"),
    ("boot", "ˈboːt"),
])
def test_doubled_vowel_letter_stays_long(be, word, ipa):
    assert be.transcribe(word) == ipa


def test_spec_states_the_flag():
    raw = json.loads(
        resources.files("orthography2ipa").joinpath("data/nl-BE.json").read_text("utf-8"))
    assert raw["collapse_geminates"] is True

