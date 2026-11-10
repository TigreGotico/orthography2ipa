"""French function words and the open ⟨e⟩ before a doubled ⟨ll tt rr⟩.

The reading of each closed-class word is the value Lexique 3.83 gives in its
``phon`` column (New et al. 2004), written here in IPA. Before the entries,
⟨est⟩ was [ɛs], ⟨et⟩ [ɛ], ⟨des mes tes ses ces⟩ a bare consonant, ⟨cet⟩ [sɛ]
and ⟨sept⟩ [sɛp]. The open ⟨e⟩ rule is Féry (2001: 7-8, ex. (19) and (20b)):
only [ɛ] stands before a final consonant (elle, cette).

The counter-cases are the neighbours the rule must leave alone: ⟨ss⟩, ⟨nn⟩
and ⟨mm⟩ are not in the rule, and a schwa before a single consonant stays.
"""
import pytest

import orthography2ipa as o2i

TAGS = ["fr", "fr-FR", "fr-CA", "fr-BE", "fr-CH", "fr-CI", "fr-LU"]


@pytest.mark.parametrize("tag", TAGS)
@pytest.mark.parametrize("text, expected", [
    ("est", "ɛ"), ("es", "ɛ"), ("et", "e"), ("des", "de"), ("ces", "se"),
    ("mes", "me"), ("tes", "te"), ("ses", "se"), ("cet", "sɛt"),
    ("sept", "sɛt"), ("les", "le"),
    ("Est", "ɛ"), ("ET", "e"),
    ("c'est", "sɛ"), ("n'est", "nɛ"), ("s'est", "sɛ"), ("qu'est", "kɛ"),
    ("t'es", "tɛ"), ("n'es", "nɛ"), ("C’est", "sɛ"),
])
def test_a_function_word_has_its_lexique_reading(tag, text, expected):
    # fr-CA laxes nothing here: no high vowel stands in a final closed syllable
    assert o2i.transcribe(text, tag) == expected


@pytest.mark.parametrize("tag", TAGS)
@pytest.mark.parametrize("text, expected", [
    ("elle", "ɛl"), ("elles", "ɛl"), ("cette", "sɛt"), ("belle", "bɛl"),
    ("quelle", "kɛl"), ("nouvelle", "nuvɛl"), ("terre", "tɛʁ"),
    ("guerre", "ɡɛʁ"), ("appelle", "apɛl"),
])
def test_e_before_a_doubled_l_t_or_r_is_open(tag, text, expected):
    assert o2i.transcribe(text, tag) == expected


@pytest.mark.parametrize("text, expected", [
    ("dessus", "dəsy"),            # de- + ssus: the prefix keeps its schwa
    ("ressembler", "ʁəsɑ̃ble"),    # re- + ss
    ("ennemi", "ənəmi"),           # ⟨nn⟩ after ⟨e⟩ spells a nasal: not claimed
    ("le", "lə"),                  # a schwa before nothing stays
    ("de", "də"),
    ("ne", "nə"),
])
def test_the_open_e_rule_leaves_its_neighbours_alone(text, expected):
    assert o2i.transcribe(text, "fr-FR") == expected


def test_a_sentence_reads_est_as_the_verb():
    assert o2i.transcribe("Il est midi et elle est là", "fr-FR") == (
        "il ɛ midi e ɛl ɛ la")
    assert o2i.transcribe("c'est la belle terre", "fr-FR") == "sɛ la bɛl tɛʁ"
