"""A Dutch prefix needs a stressable rest: a schwa takes no stress.

Sources:

- M. Trommelen & W. Zonneveld, *Klemtoon en metrische fonologie*, 1989,
  p. 132: "de schwa nooit, in welke positie dan ook, klemtoon kan hebben
  in het Nederlands". P. 138 writes the schwa for final ⟨-er -el -em -en⟩:
  keln-∂r, morm-∂l, bliks-∂m, vark-∂n.
- P.C. Paardekooper, *ABN-uitspraakgids*, 1987, p. XV: "woorden op een ə
  (gespeld als en)".

The expected forms of the schwa words are the outputs of the commit before
the prefix rule, 0f4e144b^, which had no prefix test at all.
"""
import pytest

from orthography2ipa import G2P
from orthography2ipa.stress import detect_stress
from orthography2ipa.types import StressRules

CHILDREN = ["nl-NL-x-polder", "nl-NL-x-groninge", "nl-NL-x-limburg"]


@pytest.mark.parametrize("lang, word, ipa", [
    ("nl-NL", "geven", "ˈχeivən"),
    ("nl-NL", "beter", "ˈbeitəɹ"),
    ("nl-NL", "beren", "ˈbeᵊrən"),
    ("nl-NL", "bezem", "ˈbeizəm"),
    ("nl-NL", "veren", "ˈveᵊrən"),
    ("nl-NL", "verder", "ˈvɛɹdəɹ"),
    ("nl-NL", "beker", "ˈbeikəɹ"),
    ("nl-NL", "beten", "ˈbeitən"),
    ("nl-BE", "geven", "ˈɣeːvən"),
    ("nl-BE", "beter", "ˈbeːtər̥"),
    ("nl-BE", "bezem", "ˈbeːzəm"),
    ("nl-BE", "verder", "ˈvɛrdər̥"),
])
def test_schwa_rest_is_not_a_prefixed_stem(lang, word, ipa):
    assert G2P(lang).transcribe(word) == ipa


@pytest.mark.parametrize("lang", CHILDREN)
@pytest.mark.parametrize("word", ["geven", "beter", "beren", "bezem", "veren", "verder"])
def test_children_keep_initial_stress_on_schwa_rest(lang, word):
    assert G2P(lang).transcribe(word).startswith("ˈ")


@pytest.mark.parametrize("lang", ["nl-NL", "nl-BE"] + CHILDREN)
@pytest.mark.parametrize("word", [
    "geweer", "gebed", "gelijk", "bedoelen", "bewegen", "gemeen", "geleden", "vereren",
])
def test_real_prefix_keeps_stress_on_the_stem(lang, word):
    """The stress mark follows the prefix: C + [ə] + ˈ."""
    out = G2P(lang).transcribe(word)
    assert out[1:3] == "əˈ", out


@pytest.mark.parametrize("lang", ["nl-NL", "nl-BE"] + CHILDREN)
@pytest.mark.parametrize("word", ["bevel", "gestel", "gezel", "gezwel"])
def test_guide_words_with_a_full_vowel_stem_are_exceptions(lang, word):
    """Paardekooper writes bə'vɛl (p. 23), gə'stɛl (p. 73), gə'zɛl (p. 74), gə'zwɛl (p. 75)."""
    out = G2P(lang).transcribe(word)
    assert out[1:3] == "əˈ" and out.endswith("ɛl"), out


@pytest.mark.parametrize("lang, word, ipa", [
    ("nl-NL", "gezel", "χəˈzɛl"),
    ("nl-BE", "gezel", "ɣəˈzɛl"),
    ("nl-BE", "gezwel", "ɣəˈzwɛl"),
    ("nl-NL-x-limburg", "gezel", "xəˈzɛl"),
    ("nl-NL-x-limburg", "gestel", "xəˈstɛl"),
])
def test_exceptions_use_the_spec_dorsal_and_w(lang, word, ipa):
    """Each spec writes ⟨g⟩ and ⟨w⟩ with its own value: [χ], [ɣ] or [x]; [ʋ] or [w]."""
    assert G2P(lang).transcribe(word) == ipa


def test_bestel_is_a_stated_gap():
    """bestel is be+stel with a full [ɛ], but the guide does not list it."""
    assert G2P("nl-NL").transcribe("bestel") == "ˈbeistəl"


def test_schwa_rimes_block_the_prefix():
    rules = StressRules(default_position=1, unstressed_prefixes=("ge",), schwa_rimes=("en",))
    assert detect_stress("geven", rules, syllables=["ge", "ven"]) == 0
    assert detect_stress("gebed", rules, syllables=["ge", "bed"]) == 1
    assert detect_stress("geleden", rules, syllables=["ge", "le", "den"]) == 1


def test_empty_schwa_rimes_keep_the_prefix_rule():
    rules = StressRules(default_position=1, unstressed_prefixes=("ge",))
    assert detect_stress("geven", rules, syllables=["ge", "ven"]) == 1
