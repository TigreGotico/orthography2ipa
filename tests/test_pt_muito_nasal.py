"""muito, its inflections and muitíssimo have the nasal diphthong [ũj̃].

No nasal letter is written. Cruz-Ferreira (1999, Handbook of the IPA, p. 128)
lists the European Portuguese nasal diphthong [ũi] with muita [ˈmũitɐ], and
Infopédia gives muito [ˈmũj̃tu] and muitíssimo [mũj̃ˈtisimu]. Barbosa & Albano
(2004, JIPA 34, p. 231) transcribe Brazilian com muita as [kõ ˈmũĩ̯ta].
Infopédia gives pt-PT mui an oral [ˈmuj], so only pt-BR, where pt.wiktionary
gives /ˈmũj/, lists mui. PT_LEX_NASAL_UI and PT_LEX_NASAL_UI_GLIDE change only
the vowel and the glide, so each child keeps its own consonants and final vowel.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get

WORDS = ["muito", "muita", "muitos", "muitas", "muitíssimo"]
BR_WORDS = WORDS + ["mui"]

#: Every spec that inherits the rules from pt-PT or pt-BR.
NASAL = [
    "pt-PT", "pt-PT-x-lisbon", "pt-PT-x-porto", "pt-PT-x-braga",
    "pt-PT-x-coimbra", "pt-PT-x-minho", "pt-PT-x-viana",
    "pt-PT-x-tras-os-montes", "pt-PT-x-aveiro", "pt-PT-x-alfena",
    "pt-PT-x-beira", "pt-PT-x-alentejo", "pt-PT-x-algarve",
    "pt-PT-x-madeira", "pt-PT-x-acores", "pt-PT-x-sao-miguel",
    "pt-PT-x-terceira", "pt-AO", "pt-CV", "pt-GW", "pt-MO", "pt-MZ",
    "pt-ST", "pt-TL", "ext-PT-x-barranco",
    "pt-BR", "pt-BR-x-bahia", "pt-BR-x-caipira", "pt-BR-x-ce",
    "pt-BR-x-cuiaba", "pt-BR-x-floripa", "pt-BR-x-fluminen", "pt-BR-x-mg",
    "pt-BR-x-norte", "pt-BR-x-pr", "pt-BR-x-recife", "pt-BR-x-rj",
    "pt-BR-x-sp", "pt-BR-x-sul", "pt-UY",
]


@pytest.mark.parametrize("word, ipa", [
    ("muito", "ˈmũj̃tu"), ("muita", "ˈmũj̃tɐ"), ("muitos", "ˈmũj̃tuʃ"),
    ("muitas", "ˈmũj̃tɐʃ"), ("muitíssimo", "mũj̃ˈtisimu"), ("Muito", "ˈmũj̃tu"),
    ("mui", "ˈmuj"),
])
def test_pt_pt_reads_the_nasal_diphthong(word, ipa):
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("muito", "ˈmũj̃tu"), ("muita", "ˈmũj̃tɐ"), ("muitos", "ˈmũj̃tus"),
    ("muitas", "ˈmũj̃tɐs"), ("mui", "ˈmũj̃"), ("muitíssimo", "mũj̃ˈt͡ʃisimu"),
])
def test_pt_br_reads_the_nasal_diphthong(word, ipa):
    assert G2P("pt-BR").transcribe_word(word) == ipa


@pytest.mark.parametrize("lang", NASAL)
@pytest.mark.parametrize("word", WORDS)
def test_every_inheriting_spec_reads_the_nasal_diphthong(lang, word):
    ipa = G2P(lang).transcribe_word(word)
    assert "mũj̃" in ipa, (lang, word, ipa)
    assert "muj" not in ipa, (lang, word, ipa)


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR", "pt-PT-x-porto", "pt-MZ"])
@pytest.mark.parametrize("word", ["fortuito", "circuito", "gratuito",
                                  "cuidado", "mudo", "fui", "muitíssima"])
def test_other_words_keep_an_oral_vowel(lang, word):
    ipa = G2P(lang).transcribe_word(word)
    assert "ũ" not in ipa and "j̃" not in ipa, (lang, word, ipa)


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
def test_the_final_vowel_and_sibilant_are_the_spec_s_own(lang):
    # The rules change only the diphthong: the rest of muitos is what the spec
    # gives the same letters in a word without the rules (mudos).
    g = G2P(lang)
    assert g.transcribe_word("muitos")[-2:] == g.transcribe_word("mudos")[-2:]


def test_the_phrase_keeps_its_sandhi():
    assert G2P("pt-PT").transcribe("muitos amigos") == "ˈmũj̃tuz ɐˈmiɡuʃ"
    assert G2P("pt-BR").transcribe("muito bem") == "ˈmũj̃tu ˈbẽj̃"


CREOLES = ["aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]


@pytest.mark.parametrize("lang", CREOLES)
def test_the_creoles_disable_the_rules(lang):
    rules = {r.id: r for r in get(lang).allophone_rules}
    for rid in ("PT_LEX_NASAL_UI", "PT_LEX_NASAL_UI_GLIDE"):
        assert rules[rid].phonemes == (), (lang, rid)


@pytest.mark.parametrize("lang", CREOLES + ["pt-PT-x-medieval"])
def test_specs_outside_the_rules_do_not_change(lang):
    assert "ũ" not in G2P(lang).transcribe_word("muito")


@pytest.mark.parametrize("lang, words", [("pt-PT", WORDS), ("pt-BR", BR_WORDS)])
def test_the_rules_name_their_words(lang, words):
    rules = {r.id: r for r in get(lang).allophone_rules}
    for rid in ("PT_LEX_NASAL_UI", "PT_LEX_NASAL_UI_GLIDE"):
        assert sorted(rules[rid].word) == sorted(words)
