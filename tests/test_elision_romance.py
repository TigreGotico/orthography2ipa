"""Italian and Portuguese write an elided clitic with its host.

Italian (Romito 2010, Enciclopedia dell'Italiano, "Elisione"): the elided
clitic and its host are one phonological word with one stress mark, written
with an apostrophe: l'astrazione [lastraˈʦjone], un'ora [uˈnora], d'essere
[ˈdesːere], senz'altro [senˈʦaltro].

Portuguese (Acordo Ortográfico de 1990, Base XVIII, p. 18 of the APEL text):
the apostrophe splits a contraction or marks an elision in writing, and the
split 'nunca impede na leitura a combinação fonética': d'Ele, n'Ela, pel'A,
Sant'Ana, Nun'Álvares.

The expected IPA is written here. Before the field was set, the clitic was a
word of its own with a stress mark on a bare consonant (it-IT ``l'amico`` was
``ˈl aˈmiko``).
"""
import pytest

import orthography2ipa as o2i

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
