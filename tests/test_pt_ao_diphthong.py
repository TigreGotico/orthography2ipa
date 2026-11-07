"""The contraction ao (a + o) is the falling diphthong [aw] in pt-PT.

Cruz-Ferreira (1999, Handbook of the IPA, p. 130) transcribes Ao vê-lo as
[au ˈvelu], and p. 128 states that diphthong end-points are transcribed [i]
and [u]. Infopédia gives ao [aw]. The rules reduced the unstressed ⟨a⟩ to [ɐ]
and read ⟨o⟩ as a separate [u], so pt-PT read ao as [ɐu]. PT_LEX_AO_A and
PT_LEX_AO_GLIDE name the word and change only its two segments.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get

#: Specs that inherit the rules and read ao [aw].
DIPHTHONG = ["pt-PT", "pt-PT-x-lisbon", "pt-PT-x-porto", "pt-PT-x-braga",
             "pt-PT-x-coimbra", "pt-PT-x-minho", "pt-PT-x-viana",
             "pt-PT-x-tras-os-montes", "pt-PT-x-aveiro", "pt-PT-x-alfena",
             "pt-PT-x-madeira", "pt-PT-x-terceira", "pt-PT-x-sao-miguel",
             "pt-MO", "pt-CV", "pt-MZ", "pt-GW", "pt-ST", "ext-PT-x-barranco"]
#: Specs with their own word exception for ao, which the rules do not reach.
OWN_EXCEPTION = {"pt-PT-x-beira": "ɐu", "pt-PT-x-algarve": "aw",
                 "pt-PT-x-acores": "aw", "pt-PT-x-alentejo": "aw"}
CREOLES = ["aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]


@pytest.mark.parametrize("word", ["ao", "Ao", "AO"])
def test_pt_pt_reads_the_diphthong(word):
    assert G2P("pt-PT").transcribe_word(word) == "aw"


def test_the_phrase_from_the_source():
    assert G2P("pt-PT").transcribe("ao vê-lo").startswith("aw ")


@pytest.mark.parametrize("lang", DIPHTHONG)
def test_every_inheriting_spec_reads_the_diphthong(lang):
    assert G2P(lang).transcribe_word("ao") == "aw"


@pytest.mark.parametrize("lang, ipa", sorted(OWN_EXCEPTION.items()))
def test_a_spec_s_own_exception_wins(lang, ipa):
    assert G2P(lang).transcribe_word("ao") == ipa


@pytest.mark.parametrize("word, ipa", [("aos", "ɐuʃ"), ("caos", "ˈkauʃ"),
                                       ("pau", "ˈpaw"), ("mau", "ˈmaw")])
def test_other_words_keep_their_reading(word, ipa):
    # aos has no source reading, so it keeps the hiatus; the others never
    # matched the rules.
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("lang, ipa", [("pt-BR", "au"), ("pt-AO", "aʊ"),
                                       ("pt-TL", "ao"), ("pt-PT-x-medieval", "ɐo")])
def test_specs_without_the_reduced_reading_keep_theirs(lang, ipa):
    assert G2P(lang).transcribe_word("ao") == ipa


@pytest.mark.parametrize("lang", CREOLES)
def test_the_creoles_disable_the_rules(lang):
    rules = {r.id: r for r in get(lang).allophone_rules}
    for rid in ("PT_LEX_AO_A", "PT_LEX_AO_GLIDE"):
        assert rules[rid].phonemes == (), (lang, rid)


def test_the_rules_name_only_ao():
    rules = {r.id: r for r in get("pt-PT").allophone_rules}
    for rid in ("PT_LEX_AO_A", "PT_LEX_AO_GLIDE"):
        assert tuple(rules[rid].word) == ("ao",)
