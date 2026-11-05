"""Netherlandic Dutch coda /r/ is [ɹ]; Belgian Dutch keeps the trill, voiceless finally and before /p t k/.

Sources:

- C. Gussenhoven, "Dutch", *Journal of the International Phonetic
  Association* 22(1-2), 1992, p. 46: "/r/ is [r] in the onset, and [ɹ] in
  the coda; in careful speech, a trill may occur word-initially (the
  majority of speakers have a uvular, rather than alveolar, realization of
  /r/)."
- J. Verhoeven, "Belgian Standard Dutch", *JIPA* 35(2), 2005, p. 245: "The
  alveolar trill is most frequent and geographically most widely
  distributed", and "The alveolar/uvular trill is voiced in all positions,
  except word-finally as in [doːʀ̥] 'through' and when followed by a
  voiceless stop in consonant clusters as in [vaːʀ̥t] 'sails'."

The other segments keep the values the specs state elsewhere.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def nl():
    return G2P("nl-NL")


@pytest.fixture(scope="module")
def be():
    return G2P("nl-BE")


@pytest.mark.parametrize("word, ipa", [
    ("rat", "ˈrɑt"),
    ("raad", "ˈraːt"),
    ("haren", "ˈɦaːrən"),
    ("Aalbrecht", "ˈaːlbrɛχt"),
])
def test_nl_nl_onset_r_is_r(nl, word, ipa):
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("vaart", "ˈvaːɹt"),
    ("kaart", "ˈkaːɹt"),
    ("arm", "ˈɑɹm"),
    ("dorp", "ˈdɔɹp"),
    ("berg", "ˈbɛɹχ"),
    ("kerk", "ˈkɛɹk"),
    ("bergen", "ˈbɛɹχən"),
])
def test_nl_nl_coda_r_is_the_approximant(nl, word, ipa):
    assert nl.transcribe(word) == ipa


def test_nl_nl_word_final_r_is_the_approximant(nl):
    assert nl.transcribe("door").endswith("ɹ")
    assert nl.transcribe("bier").endswith("ɹ")


@pytest.mark.parametrize("word, ipa", [
    ("rat", "ˈrɑt"),
    ("haren", "ˈɦaːrən"),
    ("arm", "ˈɑrm"),
    ("harder", "ˈɦɑrdər̥"),
])
def test_nl_be_r_is_a_voiced_trill_elsewhere(be, word, ipa):
    assert be.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("door", "ˈdoːr̥"),
    ("vaart", "ˈvaːr̥t"),
    ("dorp", "ˈdɔr̥p"),
    ("kerk", "ˈkɛr̥k"),
])
def test_nl_be_r_is_voiceless_finally_and_before_a_voiceless_stop(be, word, ipa):
    assert be.transcribe(word) == ipa


def test_nl_be_has_no_approximant(be):
    out = "".join(be.transcribe(w) for w in ("door", "vaart", "arm", "berg", "harder", "kerk"))
    assert "ɹ" not in out


def test_af_keeps_its_own_r():
    assert "ɹ" not in G2P("af").transcribe("vaart")


@pytest.mark.parametrize("spec, word, ipa", [
    ("nl-NL-x-polder", "vaart", "ˈvaːɹt"),
    ("nl-NL-x-groninge", "vader", "ˈfaːdəɹ"),
    ("nl-NL-x-limburg", "bergen", "ˈbɛɹxən"),
    ("nl-NL-x-limburg", "tjerkgaast", "ˈtʃɛɹkxaːst"),
])
def test_netherlandic_children_take_the_coda_approximant(spec, word, ipa):
    # The children state no coda /r/ of their own, so the nl-NL value reaches them.
    assert G2P(spec).transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("acryl", "ˈɑkril"),
    ("Frysk", "ˈfrisk"),
    ("boekery", "ˈbukəri"),
])
def test_nl_nl_r_before_vowel_y_is_an_onset(nl, word, ipa):
    # ⟨y⟩ is the vowel [i] here, so the [r] before it opens the syllable.
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("spec", ["nl-NL", "nl-BE"])
def test_word_initial_r_keeps_the_trill(spec):
    # Rhenen: the [r] that starts a word is an onset in both countries.
    assert G2P(spec).transcribe("Rhenen").startswith("ˈr")
