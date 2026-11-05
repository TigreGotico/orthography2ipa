"""A word that is only a sibilant reduces with the next sibilant.

Bonet & Lloret, *OCP Effects in Catalan Cliticization* (UAB GGT-01-9): "In
Catalan, sequences of sibilants are never pronounced as such" (p. 1, p. 2),
and "only reduction of the two sibilants to one (fusion or deletion) is found
... when the sibilants belong to different words" (p. 2). A clitic with no
vowel takes part too: *Ens sent* has one [s] (p. 4, example 4a).

So when the left word is only the sibilant, such as the letter name ⟨x⟩ [ˈʃ]
or ⟨ç⟩ [ˈs], the phrase keeps one sibilant and no word made only of a stress
mark. The phrase then reads as the right word alone, which the rule does not
change. The expected strings below are those right words, read alone.
"""
import pytest

from orthography2ipa import transcribe

#: Every spec whose resolved sandhi rules carry CA_DEGEM_S and CA_DEGEM_SH.
DEGEMINATING = ["ca", "ca-x-nord", "ca-x-alguer", "ca-x-occident",
                "ca-x-valencia"]


@pytest.mark.parametrize("lang,phrase,expected", [
    ("ca", "x xocolata", "ʃukuˈlatə"),
    ("ca", "X xarxa", "ˈʃarʃə"),
    ("ca", "ç sopa", "ˈsɔpə"),
    ("ca-x-nord", "x xocolata", "ʃukuˈlatə"),
    ("ca-x-nord", "ç sopa", "ˈsɔpə"),
    ("ca-x-alguer", "x xocolata", "ʃukuˈɾata"),
    ("ca-x-alguer", "X xarxa", "ˈʃarʃa"),
    ("ca-x-alguer", "ç sopa", "ˈsɔpa"),
    ("ca-x-occident", "ç sopa", "ˈsopɛ"),
    ("ca-x-valencia", "ç sopa", "ˈsopa"),
])
def test_a_lone_sibilant_reduces_with_its_mark(lang, phrase, expected):
    assert transcribe(phrase, lang) == expected


@pytest.mark.parametrize("lang", DEGEMINATING)
@pytest.mark.parametrize("phrase", [
    "x xocolata", "X xarxa", "ç sopa", "ç sa", "x xinès", "ç sense",
])
def test_no_word_is_only_a_stress_mark(lang, phrase):
    words = transcribe(phrase, lang).split()
    assert all(w.strip("ˈˌ") for w in words), words


@pytest.mark.parametrize("lang,expected", [
    ("ca", "ˈpɛ ʃiˈnɛs"),
    ("ca-x-nord", "ˈpɛ ʃiˈnɛs"),
    ("ca-x-alguer", "ˈpe ʃiˈnɛs"),
])
def test_a_word_with_a_vowel_keeps_its_mark(lang, expected):
    # The mark of peix stands before the vowel, never right before the final
    # sibilant, so only the [ʃ] is deleted.
    assert transcribe("peix xinès", lang) == expected


@pytest.mark.parametrize("lang,expected", [
    ("ca", "ˈsɔpə"),
    ("ca-x-nord", "ˈsɔpə"),
    ("ca-x-alguer", "ˈsɔpa"),
    ("ca-x-occident", "ˈsopɛ"),
    ("ca-x-valencia", "ˈsopa"),
])
def test_an_unstressed_lone_s_stays_one_sibilant(lang, expected):
    assert transcribe("s sopa", lang) == expected


@pytest.mark.parametrize("lang", ["ca", "ca-x-nord", "ca-x-alguer"])
def test_a_pause_blocks_the_reduction(lang):
    # Sandhi acts inside the phrase. After a full stop the letter keeps its
    # sibilant and its mark.
    assert transcribe("x. xocolata", lang).split()[0] == "ˈʃ"

