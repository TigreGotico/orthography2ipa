"""An elided clitic and its host are one word, and the apostrophe is silent.

French ``aujourd'hui`` and ``l'homme`` and Portuguese ``d'água`` are each
one phonological word: one stress at most, no word boundary, and no sound for
the apostrophe. Every expected value below comes from the dictionary entry
named next to it, never from the engine.

A spec that spells a sound with the apostrophe declares it in its graphemes
(Ukrainian, Guarani, Breton ⟨c'h⟩), and its reading stays as it is.
"""
import pytest

import orthography2ipa as o2i

APOSTROPHES = ["'", "’"]


@pytest.mark.parametrize("apostrophe", APOSTROPHES)
def test_aujourdhui_keeps_its_d(apostrophe):
    # Larousse French-English Dictionary, s.v. aujourd'hui: [oʒurdɥi].
    # Larousse writes the French rhotic /ʁ/ with the letter r; the fr-FR
    # spec writes it [ʁ].
    assert o2i.transcribe(f"aujourd{apostrophe}hui", "fr-FR") == "oʒuʁdɥi"


@pytest.mark.parametrize("apostrophe", APOSTROPHES)
def test_l_homme_is_one_word(apostrophe):
    # Larousse French-English Dictionary, s.v. homme: [ɔm]. The elided
    # article is the bare consonant [l] and the ⟨h⟩ is silent.
    assert o2i.transcribe(f"l{apostrophe}homme", "fr-FR") == "lɔm"


@pytest.mark.parametrize("apostrophe", APOSTROPHES)
def test_d_agua_is_one_word_with_one_stress(apostrophe):
    # Portal da Língua Portuguesa (ILTEC), phonetic dictionary, Lisbon
    # standard, s.v. água: [ˈa.gwɐ] (the portal writes ASCII g for [ɡ]).
    # The elided preposition adds the onset [d] and no stress of its own.
    assert o2i.transcribe(f"d{apostrophe}água", "pt-PT") == "ˈdaɡwɐ"


def test_copo_d_agua_keeps_the_compound_stress():
    # Portal da Língua Portuguesa, Lisbon standard: copo [kˈɔ.pu],
    # água [ˈa.gwɐ]. The pt-PT spec gives an earlier element of a hyphen
    # compound a secondary stress (compound_stress "last").
    assert o2i.transcribe("copo-d’água", "pt-PT") == "ˌkɔpu ˈdaɡwɐ"


def test_the_clitic_joins_its_host_inside_a_sentence():
    assert o2i.transcribe("um copo d'água", "pt-PT").split(" ")[-1] == "ˈdaɡwɐ"


@pytest.mark.parametrize("lang, text, sound", [
    ("uk-UA", "м'ясо", "mj"),
    ("uk-UA", "м’ясо", "mj"),
    ("gn", "ñe'ẽ", "ʔ"),
    ("br", "c'hoari", "x"),
])
def test_an_apostrophe_the_spec_spells_as_a_letter_keeps_its_reading(
        lang, text, sound):
    # These specs declare the apostrophe in their graphemes, so the
    # tokenizer reads it as a letter, not as punctuation: Ukrainian keeps
    # the plain [m] and the [j] onset, Guarani the glottal stop, Breton
    # ⟨c'h⟩ the fricative [x].
    assert sound in o2i.transcribe(text, lang)


@pytest.mark.parametrize("lang, text, words", [
    ("af", "'n man", 2),
    ("fr-FR", "l' homme", 2),
    ("pt-PT", "'água'", 1),
])
def test_an_apostrophe_at_a_word_edge_does_not_join(lang, text, words):
    assert len(o2i.transcribe(text, lang).split(" ")) == words
