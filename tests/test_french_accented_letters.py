"""Every letter of the French alphabet has a value in fr-FR.

French writes ⟨à⟩, ⟨æ⟩, ⟨œ⟩ and ⟨ÿ⟩ as letters of its own alphabet, beside the
accented vowels ⟨â é è ê ë î ï ô ù û ü⟩ and ⟨ç⟩. A letter with no grapheme key is
dropped from the transcription without a trace, so ⟨déjà⟩ came out *[deʒ] and
⟨à⟩ came out empty. The expected values come from the letter tables the spec
cites in its ``notes`` (French orthography; Prononciation du français), never
from the engine:

* ⟨à⟩ is /a/, the same vowel as ⟨a⟩: its grave only separates homophones
  (à "to" against a "has", là against la).
* ⟨æ⟩ is /e/, like ⟨é⟩ (cæcum, ex æquo).
* ⟨œ⟩ outside ⟨œu⟩ and ⟨œil⟩ is the Latin rendering of Greek ⟨οι⟩ and is /e/,
  with the spelling pronunciation /ø/ as the second reading (œsophage, fœtus).
* ⟨il⟩ and ⟨ill⟩ after ⟨œ⟩ are /j/, as after ⟨eu⟩ and ⟨ue⟩ (œil, œillet).
* ⟨ÿ⟩ is /i/; it occurs only in proper names (Aÿ /ai/).
* ⟨œ⟩ is a vowel letter, so an ⟨s⟩ after it is intervocalic (œsophage
  /ezɔfaʒ/).
"""
import pytest

from orthography2ipa import G2P, transcribe


def _t(word):
    return transcribe(word, "fr-FR")


@pytest.mark.parametrize("word,expected", [
    ("à", "a"),
    ("À", "a"),
    ("là", "la"),
    ("déjà", "deʒa"),
    ("voilà", "vwala"),
    ("delà", "dəla"),
])
def test_a_grave_is_a(word, expected):
    assert _t(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("æ", "e"),
    ("Æ", "e"),
    ("œ", "e"),
    ("Œ", "e"),
    ("ÿ", "i"),
    ("Ÿ", "i"),
])
def test_the_ligatures_and_y_diaeresis_have_a_value(word, expected):
    assert _t(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("fœtal", "fetal"),
    ("œsophage", "ezɔfaʒ"),
    ("Aÿ", "ai"),
])
def test_the_ligatures_and_y_diaeresis_inside_a_word(word, expected):
    assert _t(word) == expected


def test_learned_oe_keeps_the_spelling_pronunciation_as_second_reading():
    assert G2P("fr-FR").word_candidates("œ", k=2) == ["e", "ø"]


@pytest.mark.parametrize("word,expected", [
    ("œil", "œj"),
    ("œillet", "œjɛ"),
])
def test_il_after_oe_is_yod(word, expected):
    assert _t(word) == expected


ALL_FRENCH_LETTERS = "àâæçéèêëîïôœùûüÿ"


@pytest.mark.parametrize("letter", list(ALL_FRENCH_LETTERS + ALL_FRENCH_LETTERS.upper()))
def test_no_french_letter_is_dropped(letter):
    assert _t(letter) != ""
    assert _t("t" + letter + "l") != "tl"


# ── ⟨œu⟩: a hard ⟨c⟩ before it, a vowel after ⟨n⟩, and the loi de position ──
# Expected values are the headword pronunciations of the French Wiktionary
# entries (fr.wiktionary.org), syllable dots removed.

@pytest.mark.parametrize("word,expected", [
    ("cœur", "kœʁ"),
    ("sœur", "sœʁ"),
    ("œuvre", "œvʁ"),
    ("manœuvre", "manœvʁ"),
    ("cœlacanthe", "selakɑ̃t"),
    ("vœu", "vø"),
    ("nœud", "nø"),
    ("bœuf", "bœf"),
])
def test_oe_u_digraph(word, expected):
    assert _t(word) == expected
