"""French function words and the open ⟨e⟩ before a doubled ⟨ll tt rr⟩.

The reading of each closed-class word is the value Lexique 3.83 gives in its
``phon`` column (New et al. 2004), written here in IPA. Before the entries,
⟨est⟩ was [ɛs], ⟨et⟩ [ɛ], ⟨des mes tes ses ces⟩ a bare consonant, ⟨cet⟩ [sɛ]
and ⟨sept⟩ [sɛp]. The open ⟨e⟩ rule is Féry (2001: 8, ex. (19) and (20b)):
only [ɛ] stands in a word-final closed syllable (elle, cette). Lexique gives
[ɛ] for 1476 of the 1478 word types in -elle(s), -ette(s), -erre(s).

The counter-cases are the neighbours the rule must leave alone: ⟨ss⟩, ⟨nn⟩
and ⟨mm⟩ are not in the rule, a schwa before a single consonant stays, and
an earlier syllable is not claimed: there Lexique reads the ⟨e⟩ as [e] in
some words and [ɛ] in others.
"""
import pytest

import orthography2ipa as o2i

TAGS = ["fr", "fr-FR", "fr-CA", "fr-BE", "fr-CH", "fr-CI", "fr-LU"]


@pytest.mark.parametrize("tag", TAGS)
@pytest.mark.parametrize("text, expected", [
    ("est", "e"), ("es", "ɛ"), ("et", "e"), ("des", "de"), ("ces", "se"),
    ("mes", "me"), ("tes", "te"), ("ses", "se"), ("cet", "sɛt"),
    ("sept", "sɛt"), ("les", "le"),
    ("Est", "e"), ("ET", "e"),
    ("c'est", "se"), ("n'est", "ne"), ("s'est", "se"), ("qu'est", "ke"),
    ("t'es", "tɛ"), ("n'es", "nɛ"), ("C’est", "se"),
])
def test_a_function_word_has_its_lexique_reading(tag, text, expected):
    # fr-CA laxes nothing here: no high vowel stands in a final closed syllable
    assert o2i.transcribe(text, tag) == expected


@pytest.mark.parametrize("tag", TAGS)
@pytest.mark.parametrize("text, expected", [
    ("elle", "ɛl"), ("elles", "ɛl"), ("cette", "sɛt"), ("belle", "bɛl"),
    ("quelle", "kɛl"), ("nouvelle", "nuvɛl"), ("terre", "tɛʁ"),
    ("guerre", "ɡɛʁ"), ("appelle", "apɛl"),
    # Lexique 3.83 phon: vEsEl, SosEt, pjER, ZEt, bEl
    ("vaisselle", "vɛsɛl"), ("chaussette", "ʃosɛt"), ("pierre", "pjɛʁ"),
    ("jette", "ʒɛt"), ("belles", "bɛl"),
])
def test_e_before_a_doubled_l_t_or_r_is_open(tag, text, expected):
    assert o2i.transcribe(text, tag) == expected


@pytest.mark.parametrize("text, expected", [
    ("dessus", "dəsy"),            # de- + ssus: the prefix keeps its schwa
    ("ressembler", "ʁəsɑ̃ble"),    # re- + ss
    ("le", "lə"),                  # a schwa before nothing stays
    ("de", "də"),
    ("ne", "nə"),
])
def test_the_open_e_rule_leaves_its_neighbours_alone(text, expected):
    assert o2i.transcribe(text, "fr-FR") == expected


@pytest.mark.xfail(strict=True, reason="⟨e⟩ before ⟨nn⟩ is not modelled")
def test_ennemi_has_its_lexique_reading():
    # Lexique 3.83: ennemi, phon En°mi
    assert o2i.transcribe("ennemi", "fr-FR") == "ɛnəmi"


@pytest.mark.parametrize("text, open_e", [
    # The reading with the ⟨e⟩ as [ɛ]. Lexique 3.83 has [e] in each, so the
    # word-final rule must not write [ɛ] there.
    ("cellule", "sɛlyl"),          # Lexique selyl
    ("intelligent", "ɛ̃tɛliʒɑ̃"),     # Lexique 5teliZ@
    ("nettoyer", "nɛtwaje"),       # Lexique netwaje
    ("verrou", "vɛʁu"),            # Lexique veRu
    ("pellicule", "pɛlikyl"),      # Lexique pelikyl
    ("serrer", "sɛʁe"),            # Lexique seRe
])
def test_the_open_e_rule_stays_out_of_an_earlier_syllable(text, open_e):
    assert o2i.transcribe(text, "fr-FR") != open_e


def test_a_sentence_reads_est_as_the_verb():
    assert o2i.transcribe("Il est midi et elle est là", "fr-FR") == (
        "il e midi e ɛl e la")
    assert o2i.transcribe("c'est la belle terre", "fr-FR") == "se la bɛl tɛʁ"


# A hyphen compound reads from its own Lexique 3.83 entry, not from the
# standalone verb est [e]: est-ce Es°, est-ce que Es°k°, c'est-à-dire
# sEtadiR, sud-est sydEst, nord-est nOREst, est-africain EstafRik5,
# est-allemand Estal°m@, est-allemande Estal°m@d. qu'est-ce que is qu' [k]
# in front of est-ce que.
@pytest.mark.parametrize("tag", TAGS)
@pytest.mark.parametrize("text, expected", [
    ("est-ce que", "ɛsə kə"), ("Est-ce que", "ɛsə kə"),
    ("qu'est-ce que", "kɛsə kə"), ("Qu’est-ce que", "kɛsə kə"),
    ("sud-est", "sydɛst"), ("nord-est", "nɔʁɛst"),
    ("est-africain", "ɛstafʁikɛ̃"), ("est-allemand", "ɛstaləmɑ̃"),
    ("est-allemande", "ɛstaləmɑ̃d"),
])
def test_a_hyphen_compound_has_its_lexique_reading(tag, text, expected):
    assert o2i.transcribe(text, tag) == expected


@pytest.mark.parametrize("tag", [t for t in TAGS if t != "fr-CA"])
def test_c_est_a_dire_has_its_lexique_reading(tag):
    assert o2i.transcribe("c'est-à-dire", tag) == "sɛtadiʁ"


@pytest.mark.xfail(strict=True, reason="an inherited fr-FR entry bypasses "
                   "the fr-CA affrication rule")
def test_c_est_a_dire_affricates_in_fr_ca():
    # /d/ before /i/ is [d͡z], obligatory within words (Dow 2019: 1-2)
    assert o2i.transcribe("c'est-à-dire", "fr-CA") == "sɛtad͡ziʁ"


@pytest.mark.parametrize("text, second", [
    # The clitic is in the second word, so the run stays two words: d'est
    # and l'est are the noun (Lexique est NOM Est).
    ("vent-d'est", "dɛst"), ("sud-l'est", "lɛst"),
])
def test_a_clitic_inside_a_later_word_does_not_join_the_run(text, second):
    first = text.split("-")[0]
    assert o2i.transcribe(text, "fr-FR").split(" ") == [
        o2i.transcribe(first, "fr-FR"), second]


def test_a_sentence_reads_a_compound_from_its_entry_and_est_as_the_verb():
    assert o2i.transcribe("Est-ce que le vent du sud-est souffle ?",
                          "fr-FR") == "ɛsə kə lə vɑ̃ dy sydɛst sufl"
    assert o2i.transcribe("Il est midi", "fr-FR") == "il e midi"
    assert o2i.transcribe("Qu'est-ce que c'est ?", "fr-FR") == "kɛsə kə se"
