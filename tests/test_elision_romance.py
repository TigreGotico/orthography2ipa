"""Italian and Portuguese write an elided clitic with its host.

Italian (Romito 2010, Enciclopedia dell'Italiano, "Elisione"): the elided
clitic and its host are one phonological word with one stress mark, written
with an apostrophe: l'astrazione [lastraˈʦjone], un'ora [uˈnora], d'essere
[ˈdesːere], senz'altro [senˈʦaltro].

Portuguese (Acordo Ortográfico de 1990, Base XVIII, pp. 18-19 of the APEL
text): the apostrophe splits a contraction in writing, d'Os Lusíadas, n'Os
Lusíadas, pel'Os Lusíadas (1º a), p. 18), d'Ele, n'Ela, pel'A, lh'O (1º b),
p. 19), and marks an elision, Sant'Ana, Nun'Álvares (1º c), p. 19). The
split 'nunca impede na leitura a combinação fonética' (p. 18): d'Os reads as
the contraction dos.

The expected IPA is written here. Before the field was set, the clitic was a
word of its own with a stress mark on a bare consonant (it-IT ``l'amico`` was
``ˈl aˈmiko``).
"""
import pytest

import orthography2ipa as o2i
from orthography2ipa import G2P, Pipeline

@pytest.mark.parametrize("text, expected", [
    ("l'amico", "laˈmiko"),
    ("un'amica", "unaˈmika"),
    ("dell'uomo", "deˈlːwomo"),
    ("nell'aria", "neˈlːarja"),
    ("un'altra", "uˈnaltra"),
    ("senz'altro", "senˈtsaltro"),     # Romito 2010: [senˈʦaltro]
    ("l’amico", "laˈmiko"),            # U+2019
])
def test_an_italian_elision_is_one_word_with_one_stress(text, expected):
    assert o2i.transcribe(text, "it-IT") == expected


@pytest.mark.parametrize("tag", ["it-IT-x-toscana", "it-IT-x-roma"])
def test_an_italian_regional_spec_inherits_the_elision(tag):
    assert " " not in o2i.transcribe("l'amico", tag)


def test_an_italian_apostrophe_at_a_word_edge_is_not_an_elision():
    assert o2i.transcribe("po'", "it-IT") == o2i.transcribe("po", "it-IT")


@pytest.mark.parametrize("tag", ["pt-PT", "pt-BR"])
def test_a_portuguese_contraction_or_elision_is_one_word(tag):
    for text in ("d'Ele", "Sant'Ana", "Nun'Álvares", "pel'A", "lh'O"):
        assert " " not in o2i.transcribe(text, tag), text


def test_a_portuguese_elision_reads_like_the_spelling_without_the_mark():
    for text in ("Sant'Ana", "Nun'Álvares", "d'Ele"):
        assert o2i.transcribe(text, "pt-PT") == o2i.transcribe(
            text.replace("'", ""), "pt-PT"), text


@pytest.mark.parametrize("text, clitic", [
    ("l'home", "l"), ("d'aigua", "d"), ("s'ha", "s"), ("n'hi", "n"),
    ("m'agrada", "m"),
])
def test_a_catalan_elision_keeps_its_clitic(text, clitic):
    # Catalan already read these as one word; the clitic must stay.
    spoken = o2i.transcribe(text, "ca").lstrip("ˈ")
    assert " " not in spoken
    assert spoken.startswith(clitic)


@pytest.mark.parametrize("tag, text, expected", [
    # The contraction is an unstressed function word: European Portuguese
    # reads its ⟨o⟩ as [u], ⟨e⟩ as [ɨ] and final ⟨s⟩ as [ʃ]; Brazilian
    # Portuguese keeps [e] and [s].
    ("pt-PT", "d'Os", "duʃ"),        # = dos (1º a))
    ("pt-PT", "n'Os", "nuʃ"),        # = nos
    ("pt-PT", "pel'Os", "pɨluʃ"),    # = pelos
    ("pt-PT", "pel'A", "pɨlɐ"),      # = pela (1º b))
    ("pt-PT", "lh'O", "ʎu"),         # = lho
    ("pt-PT", "D'OS", "duʃ"),
    ("pt-PT", "d’Os", "duʃ"),        # U+2019
    ("pt-BR", "d'Os", "dus"),
    ("pt-BR", "pel'A", "pelɐ"),
])
def test_a_portuguese_split_contraction_reads_as_the_contraction(
        tag, text, expected):
    assert o2i.transcribe(text, tag) == expected
    assert o2i.transcribe(text.replace("'", "").replace("’", ""),
                          tag) == expected


def test_an_italian_elision_keeps_the_host_lexicon_entry():
    # uomo is [ˈwɔmo] with an open ⟨o⟩; the rules write a close [o]. The
    # clitic's last consonant opens the host's stressed syllable.
    engine = G2P("it-IT", pipeline=Pipeline(lexicon={"uomo": "ˈwɔmo"}))
    assert engine.transcribe("l'uomo") == "ˈlwɔmo"
    assert engine.transcribe("dell'uomo") == "deˈlːwɔmo"
    assert engine.transcribe("quell'uomo") == "kweˈlːwɔmo"


def test_a_vowel_before_the_apostrophe_is_no_elided_clitic():
    # tu'A (Acordo, Base XVIII 1º b)) is tua with a capital: the part
    # before the mark keeps its vowel, so the article a after it does not
    # make the word a clitic.
    assert o2i.transcribe("tu'A", "pt-PT") == o2i.transcribe("tua", "pt-PT")
    assert "ˈ" in o2i.transcribe("tu'A", "pt-PT")


def test_a_consonant_after_the_apostrophe_is_no_host():
    # N'Djamena holds no elision: an entry for djamena does not apply.
    plain = G2P("pt-PT")
    with_entry = G2P("pt-PT", pipeline=Pipeline(lexicon={"djamena": "dʒaˈmenɐ"}))
    assert with_entry.transcribe("N'Djamena") == plain.transcribe("N'Djamena")
