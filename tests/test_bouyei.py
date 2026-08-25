"""Bouyei (pcc) — the 1985 Latin orthography.

The scheme spells TONE with a syllable-final consonant letter, exactly as
the cognate Zhuang orthography does, so the same letters are onsets before
a vowel and tones elsewhere. These tests pin that split, the rime
inventory (vowel quality and length depend on the coda) and the glottal
onset on a vowel-initial spelling.
"""
import pytest

from orthography2ipa.g2p import G2P


@pytest.fixture(scope="module")
def pcc():
    return G2P("pcc")


@pytest.mark.parametrize("word,ipa", [
    # native tone letters: l=24, z=11, c=53, x=31, s=35, h=33
    ("bil", "pi˨˦"),
    ("faz", "fa˩"),
    ("gac", "ka˥˧"),
    ("bix", "pi˧˩"),
    ("baus", "pɐu˧˥"),
    ("boh", "po˧"),
    # loanword tone letters: q=24, j=53, f=31, y=33
    ("dianq", "tiən˨˦"),
    ("dinc", "tin˥˧"),
    ("Zungyhuaf", "tsuŋ˧xua˧˩"),
    # checked tone 7 is ⟨t⟩; checked tone 8 is spelled by no letter at all
    ("bidt", "pit̚˧˥"),
    ("byagt", "pʲɐk̚˧˥"),
    ("rog", "zɔk̚˧"),
    ("nyib", "ɲip̚˧"),
])
def test_tone_letters(pcc, word, ipa):
    assert pcc.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # a tone letter also occurs syllable-finally inside a compound, where it
    # stands before the next syllable's onset
    ("cangjzangj", "tsʰɐŋ˥˧tsɐŋ˥˧"),
    ("hocrauz", "xo˥˧zɐu˩"),
    ("danglngonz", "tɐŋ˨˦ŋɔn˩"),
    ("Yinfnanf", "jin˧˩nɐn˧˩"),
    ("ndaaulndis", "ɗaːu˨˦ɗi˧˥"),
])
def test_tone_letter_before_onset(pcc, word, ipa):
    assert pcc.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # the same letters are ordinary onsets in front of a vowel
    ("laail", "laːi˨˦"),
    ("dufzej", "tu˧˩tsɯ˥˧"),
    ("jaucsoiz", "tɕɐu˥˧soːi˩"),
    ("xib", "ɕip̚˧"),
    ("saaml", "saːm˨˦"),
    ("hac", "xa˥˧"),
    ("yianh", "jiən˧"),
    ("hocsul", "xo˥˧su˨˦"),
])
def test_tone_letters_are_onsets_before_a_vowel(pcc, word, ipa):
    assert pcc.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("dal", "ta˨˦"),        # open ⟨a⟩ is a
    ("dams", "tɐm˧˥"),      # ⟨a⟩ before a coda is ɐ
    ("daail", "taːi˨˦"),    # ⟨aa⟩ is long
    ("hoc", "xo˥˧"),        # open ⟨o⟩ is o
    ("ngonz", "ŋɔn˩"),      # ⟨o⟩ before a coda is ɔ
    ("doongl", "toːŋ˨˦"),   # ⟨oo⟩ is long
    ("deel", "te˨˦"),       # open ⟨ee⟩ is e
    ("beedt", "peːt̚˧˥"),   # ⟨ee⟩ before a coda is long
    ("deh", "tɯ˧"),         # ⟨e⟩ is ɯ
    ("beangz", "pɯəŋ˩"),
    ("diangz", "tiəŋ˩"),
    ("guec", "kuə˥˧"),
    ("haec", "xɐɯ˥˧"),
    ("joic", "tɕoːi˥˧"),
])
def test_rimes(pcc, word, ipa):
    assert pcc.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("iel", "ʔiə˨˦"),
    ("oix", "ʔoːi˧˩"),
    ("iadt", "ʔiət̚˧˥"),
])
def test_vowel_initial_spelling_takes_a_glottal_onset(pcc, word, ipa):
    assert pcc.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("mbael", "ɓɐɯ˨˦"),
    ("ndingl", "ɗiŋ˨˦"),
    ("byal", "pʲa˨˦"),
    ("myaus", "mʲɐu˧˥"),
    ("gvaz", "kʷa˩"),
    ("bail", "pɐi˨˦"),      # ⟨b d g⟩ are the plain voiceless stops
    ("dungx", "tuŋ˧˩"),
    ("gul", "ku˨˦"),
    ("kuangq", "kʰuəŋ˨˦"),  # ⟨p t k⟩ are aspirated
    ("dufpinj", "tu˧˩pʰin˥˧"),
    ("ramx", "zɐm˧˩"),      # ⟨r⟩ is z
])
def test_initials(pcc, word, ipa):
    assert pcc.transcribe_word(word) == ipa
