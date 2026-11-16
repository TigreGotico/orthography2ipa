"""Italian hiatus is two syllables, and the stress mark finds the right one.

Bertinetto & Loporcaro, "The sound pattern of Standard Italian", JIPA 35(2),
2005, Table 2 (p. 138) lists the diphthongs of Standard Italian: the opening
diphthongs with [j] (je jɛ ja jɔ jo ju) and [w] (wi we wɛ wa wɔ wo), and the
closing diphthongs with [i̯] (ei ɛi ai ɔi oi ui) and [u̯] (eu ɛu au). Every
diphthong holds a high vowel, so two non-high vowels are a hiatus. Two equal
vowels are "a quickly rearticulated vowel" (p. 137: cooperare, linee). The
⟨i⟩ of ⟨ci gi sci gli⟩ before a vowel writes no sound: cacio [ˈkaːtʃo],
aglio [ˈaʎːo], ascia [ˈaʃːa] (pp. 133-134).

Without an accent mark, the spec places the stress on the penult. The tests
check where the mark falls, not the segments: each expected value is a
transcription from the source, or written by hand from the rules above, and
the test compares the number of syllabic vowels before the primary mark. A
glide ([j w], or a vowel with the non-syllabic diacritic) is not a nucleus.
"""
from __future__ import annotations

import unicodedata

import pytest

from orthography2ipa import G2P, get

_VOWELS = set("aeiouɛɔ")
_NON_SYLLABIC = "\u032f"


def _nuclei_before_mark(ipa: str) -> int:
    assert ipa.count("ˈ") == 1, ipa
    head = unicodedata.normalize("NFD", ipa.split("ˈ")[0])
    return sum(1 for i, c in enumerate(head)
               if c in _VOWELS
               and head[i + 1:i + 2] != _NON_SYLLABIC)


def _ipa(lang: str, word: str) -> str:
    return G2P(lang).transcribe_word(word)


# Two vowels that are not a Table 2 diphthong: the second one opens a
# syllable of its own. Each of these words is a paroxytone.
HIATUS = [
    ("poeta", "poˈɛːta"),         # po-E-ta; p. 138 names poeta with stressed /ɛ/
    ("teatro", "teˈaːtro"),       # te-A-tro
    ("paese", "paˈeːze"),         # pa-E-se
    ("idea", "iˈdɛːa"),           # i-DE-a
    ("reale", "reˈaːle"),         # re-A-le
    ("beato", "beˈaːto"),         # be-A-to
    ("reato", "reˈaːto"),         # re-A-to
    ("leone", "leˈoːne"),         # le-O-ne
    ("leoni", "leˈoːni"),         # le-O-ni
    ("museo", "muˈzɛːo"),         # mu-SE-o
    ("europeo", "eu̯roˈpɛːo"),     # eu-ro-PE-o
    ("maestro", "maˈestro"),      # ma-E-stro
    ("cacao", "kaˈkaːo"),         # ca-CA-o
    ("aorta", "aˈɔrta"),          # a-OR-ta
    ("idee", "iˈdɛːe"),           # i-DE-e, two equal vowels (p. 137)
]

# A high vowel between two vowels is the onset [j] of the next syllable, and
# the ⟨i⟩ of ⟨gi⟩ writes no sound, so the word keeps two syllables.
GLIDE_ONSET = [
    ("guaio", "ˈɡwaːjo"),         # GUA-io
    ("gioia", "ˈdʒɔːja"),         # GIO-ia
    ("noia", "ˈnɔːja"),           # NO-ia
]

CHILDREN = ["it-IT-x-marche", "it-IT-x-roma", "it-IT-x-toscana",
            "it-IT-x-umbria"]

# Opening diphthongs, closing diphthongs and ⟨ci gi sci gli qu gu⟩ + vowel.
# The transcriptions are the source's: pp. 133-134 and 139. These words already
# had the right stress, and the diphthong list must keep it.
CONTROL = [
    ("pieno", "ˈpjɛːno"),
    ("chiave", "ˈkjaːve"),
    ("fiore", "ˈfjoːre"),
    ("biondo", "ˈbjondo"),
    ("piuma", "ˈpjuːma"),
    ("chiodo", "ˈkjɔːdo"),
    ("miete", "ˈmjɛːte"),
    ("cuoca", "ˈkwɔːka"),
    ("guida", "ˈɡwiːda"),
    ("quindi", "ˈkwindi"),
    ("quando", "ˈkwando"),
    ("quota", "ˈkwɔːta"),
    ("acquoso", "aˈkːwoːso"),
    ("sei", "ˈsɛi̯"),
    ("baita", "ˈbai̯ta"),
    ("poi", "ˈpɔi̯"),
    ("voi", "ˈvoi̯"),
    ("lui", "ˈlui̯"),
    ("neutro", "ˈnɛu̯tro"),
    ("auto", "ˈau̯to"),
    ("Laura", "ˈlau̯ra"),
    ("cacio", "ˈkaːtʃo"),
    ("aglio", "ˈaʎːo"),
    ("ascia", "ˈaʃːa"),
    ("paglia", "ˈpaʎːa"),
    ("coscia", "ˈkɔʃːa"),
    ("meglio", "ˈmɛʎːo"),
    ("ciao", "ˈtʃaːo"),           # CIA-o
    ("giorno", "ˈdʒorno"),        # GIOR-no
    ("figlio", "ˈfiʎːo"),         # FI-glio
    ("scienza", "ˈʃɛntsa"),       # SCIEN-za
    ("lasciare", "laʃˈʃaːre"),    # la-SCIA-re
    ("può", "ˈpwɔ"),              # one syllable with a written accent
    ("più", "ˈpju"),
    ("già", "ˈdʒa"),
]


@pytest.mark.parametrize("word,expected", HIATUS + GLIDE_ONSET)
def test_it_hiatus_stress(word, expected):
    assert _nuclei_before_mark(_ipa("it-IT", word)) == \
        _nuclei_before_mark(expected)


@pytest.mark.parametrize("lang", CHILDREN)
@pytest.mark.parametrize("word,expected", HIATUS[:4])
def test_it_children_inherit_hiatus_stress(lang, word, expected):
    assert _nuclei_before_mark(_ipa(lang, word)) == \
        _nuclei_before_mark(expected)


@pytest.mark.parametrize("word,expected", CONTROL)
def test_it_diphthong_and_digraph_stress_unchanged(word, expected):
    assert _nuclei_before_mark(_ipa("it-IT", word)) == \
        _nuclei_before_mark(expected)


def test_it_declares_table_2_diphthongs():
    rules = get("it-IT").stress
    plain = {d for d in rules.diphthongs if d.isascii()}
    assert plain == {"ia", "ie", "io", "iu", "ua", "ue", "uo", "ui",
                     "ai", "ei", "oi", "au", "eu"}
    # Every diphthong holds a high vowel. A stressed high vowel next to a
    # non-high vowel is a hiatus (paura, faina; p. 139), so an accented ⟨ì ù⟩
    # is listed only beside the other high vowel (più, lùi).
    for d in rules.diphthongs:
        assert {"i", "u"} & set(unicodedata.normalize("NFD", d)), d
        if {"ì", "ù"} & set(d):
            assert set(d) <= {"i", "u", "ì", "ù"}, d
    for code in CHILDREN:
        assert get(code).stress.diphthongs == rules.diphthongs
