"""The Dutch prefixes be-, ge-, ver- and ont- take no stress.

Source:

- J. Schultink, "Over de accentuering van Nederlandse afleidingen",
  *Spektator* 6, 1976, p. 475: "Van een tweede categorie maken prefixen
  deel uit die altijd accentloos zijn en de accentuering van de afleiding
  niet beïnvloeden: be-, er-, ge-, ont- en ver-, bijv. in be'zien,
  er'kennen, ge'sar, ont'kennen en ver'vuilen".

The spec lists the spellings be, ge, ver and ont. It leaves er- out,
because the spelling er- also starts ere-, ereburger and eren. A prefix
does not take the stress when the syllable after it is a final open
syllable, as in bede and beste. The segments are the values the specs
state elsewhere; these tests check where the stress falls.
"""
import json
from importlib import resources

import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def nl():
    return G2P("nl-NL")


@pytest.mark.parametrize("word, ipa", [
    ("bezien", "bəˈzin"),
    ("ontkennen", "ɔntˈkɛnən"),
    ("vervuilen", "vəɹˈvœylən"),
])
def test_schultink_examples(nl, word, ipa):
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("betalen", "bəˈtaːlən"),
    ("bedoelen", "bəˈdulən"),
    ("beroemd", "bəˈrumt"),
    ("gebeuren", "χəˈbøᵊrən"),
    ("geloven", "χəˈlouvən"),
    ("verkopen", "vəɹˈkoupən"),
])
def test_prefix_is_unstressed(nl, word, ipa):
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("bede", "ˈbeidə"),
    ("beste", "ˈbeistə"),
])
def test_final_open_syllable_keeps_initial_stress(nl, word, ipa):
    assert nl.transcribe(word) == ipa


def test_listed_spellings():
    spec = json.loads(
        resources.files("orthography2ipa").joinpath("data/nl-NL.json").read_text("utf-8"))
    assert spec["stress"]["unstressed_prefixes"] == ["be", "ge", "ver", "ont"]


@pytest.mark.parametrize("lang, word, ipa", [
    ("nl-BE", "betalen", "bəˈtaːlən"),
    ("nl-BE", "geloven", "ɣəˈloːvən"),
    ("nl-BE", "verkopen", "vər̥ˈkoːpən"),
    ("nl-NL-x-polder", "betalen", "bəˈtaːlən"),
    ("nl-NL-x-polder", "verkopen", "vəɹˈkoupən"),
    ("nl-NL-x-limburg", "geloven", "xəˈlouvən"),
    ("nl-NL-x-groninge", "verkopen", "fəɹˈkoupən"),
])
def test_inheriting_specs(lang, word, ipa):
    assert G2P(lang).transcribe(word) == ipa



@pytest.mark.xfail(strict=True, reason="known gap: the root reads as the unstressed prefix")
@pytest.mark.parametrize("word, ipa", [
    ("beter", "ˈbeitəɹ"),
    ("beker", "ˈbeikəɹ"),
    ("gelen", "ˈχeilən"),
    ("geven", "ˈχeivən"),
    ("beten", "ˈbeitən"),
    ("veren", "ˈveᵊrən"),
    ("verder", "ˈvɛɹdəɹ"),
    ("verkoop", "ˈvɛɹkoup"),
])
def test_known_gap_roots_with_the_prefix_spelling(nl, word, ipa):
    assert nl.transcribe(word) == ipa
