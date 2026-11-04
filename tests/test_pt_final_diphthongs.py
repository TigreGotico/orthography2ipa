"""A final ⟨iu ui⟩ after a vowel is one stressed diphthong.

Acordo Ortográfico 1990, Base X, 6.º: "Prescinde-se do acento agudo nos
ditongos tónicos/tônicos grafados iu e ui, quando precedidos de vogal:
distraiu, instruiu, pauis (pl. de paul)."

So distraiu is dis-tra-iu and pauis is pa-uis: the vowel before the diphthong
is the nucleus of the syllable before, and the stress falls on the diphthong.
The ⟨i⟩ of ⟨iu⟩ and the ⟨u⟩ of ⟨ui⟩ are full vowels, not the onset glide
[j w] of the last syllable. Cruz-Ferreira (1999: 128) lists [iu] (viu) and
[ui] (anuis) among the European Portuguese falling diphthongs, and transcribes
desistiu /dɨziʃˈtiu/ (p. 129). Barbosa & Albano (2004: 230) form the
Brazilian Portuguese diphthongs from a stressed vowel and an offglide, and
transcribe desistiu with the stress on [iʊ̯] (p. 231).
"""
from __future__ import annotations

import dataclasses
import re
import unicodedata

import pytest

from orthography2ipa import G2P, get, get_syllabifier

#: The Base X, 6.º examples and the 3rd-person preterites of ⟨-air -uir⟩
#: verbs. ⟨-air⟩ and ⟨-uir⟩ are the conjugations Base VII, 2 a) names.
FINAL_IU = ["distraiu", "instruiu", "saiu", "caiu", "atraiu", "possuiu"]
FINAL_UI = ["pauis"]

#: A vowel, the stress mark, then the full vowel and the offglide of the
#: diphthong, matched on the decomposed transcription.
_IU = re.compile("[aɐeɛəɨioɔuʊɪ]̃?ˈiw")
_UI = re.compile("[aɐeɛəɨioɔuʊɪ]̃?ˈuj")

LANGS = ["pt-PT", "pt-BR", "pt-PT-x-lisbon", "pt-BR-x-sp", "pt-AO", "pt-UY"]


def _nfd(ipa: str) -> str:
    return unicodedata.normalize("NFD", ipa)


@pytest.fixture
def without_syllabifier_plugin(monkeypatch):
    from orthography2ipa import registry
    monkeypatch.setattr(registry, "_syllabifiers", {})


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word", FINAL_IU)
def test_final_iu_after_a_vowel_is_a_stressed_diphthong(lang, word):
    ipa = G2P(lang).transcribe_word(word)
    assert _IU.search(_nfd(ipa)), ipa


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word", FINAL_UI)
def test_final_ui_after_a_vowel_is_a_stressed_diphthong(lang, word):
    ipa = G2P(lang).transcribe_word(word)
    assert _UI.search(_nfd(ipa)), ipa


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", FINAL_IU + FINAL_UI)
def test_without_the_plugin_and_paths_agree(lang, word, monkeypatch):
    with_plugin = G2P(lang).transcribe_word(word)
    from orthography2ipa import registry
    monkeypatch.setattr(registry, "_syllabifiers", {})
    assert get_syllabifier(lang) is None
    ipa = G2P(lang).transcribe_word(word)
    assert (_UI if word in FINAL_UI else _IU).search(_nfd(ipa)), ipa
    assert ipa == with_plugin


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", FINAL_IU + FINAL_UI)
def test_bundled_syllabifier_keeps_the_final_diphthong_whole(
        lang, word, without_syllabifier_plugin):
    # dis-tra-iu, pa-uis: the last syllable starts at the diphthong.
    sylls = G2P(lang)._syllables_cached(word)
    tail = "uis" if word.endswith("uis") else "iu"
    assert sylls[-1] == tail, sylls


#: European Portuguese, letter for letter. The infinitive in the Portal da
#: Língua Portuguesa Dicionário fonético gives the pretonic syllables and the
#: stressed [i] of the hiatus; the preterite ends in the falling diphthong
#: [iu] of Cruz-Ferreira (1999: 128) where the infinitive ends in [iɾ]. This
#: library writes the offglide of a diphthong as [w] (viu [ˈviw]).
PT_PT = [
    ("saiu", "sɐˈiw"),            # sair [sɐˈiɾ]
    ("caiu", "kɐˈiw"),            # cair [kɐˈiɾ]
    ("distraiu", "diʃtɾɐˈiw"),    # distrair [diʃtɾɐˈiɾ]
    ("atraiu", "ɐtɾɐˈiw"),        # atrair [ɐtɾɐˈiɾ]
    ("instruiu", "ĩʃtɾuˈiw"),     # instruir [ĩʃtɾuˈiɾ]
    ("pauis", "pɐˈujʃ"),          # paul [pɐˈuɫ]; anuis [ɐˈnuiʃ]
]


@pytest.mark.parametrize("word,expected", PT_PT)
def test_pt_pt_transcription(word, expected):
    assert G2P("pt-PT").transcribe_word(word) == expected


#: Final diphthongs the rule does not split: no vowel stands before them,
#: or the ⟨u⟩ before them belongs to the digraph ⟨gu⟩.
CONTROLS = [
    ("pt-PT", "viu", "ˈviw"),                # Cruz-Ferreira 1999: 128
    ("pt-PT", "desistiu", "dɨziʃˈtiw"),      # Cruz-Ferreira 1999: 129
    ("pt-PT", "seguiu", "sɨˈɡiw"),
    ("pt-BR", "viu", "ˈviw"),
    ("pt-BR", "seguiu", "seˈɡiw"),
]


@pytest.mark.parametrize("lang,word,expected", CONTROLS)
def test_diphthongs_outside_the_rule(lang, word, expected):
    assert G2P(lang).transcribe_word(word) == expected


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", ["baiuca", "abaiucado", "caiuá", "saiba",
                                  "animais", "rainha"])
def test_rule_does_not_reach_a_medial_or_closed_vowel(lang, word):
    # Base X, 4.º reads a medial tonic ⟨u⟩ after a diphthong (baiuca), and
    # Base X, 2.º the closed hiatus (rainha). final_diphthongs reaches only a
    # diphthong at the end of the word.
    spec = get(lang)
    undeclared = dataclasses.replace(
        spec, stress=dataclasses.replace(spec.stress, final_diphthongs=None))
    assert (G2P(lang).transcribe_word(word)
            == G2P(lang, spec=undeclared).transcribe_word(word))


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
def test_rule_holds_without_closed_hiatus(lang):
    # final_diphthongs is a field of its own: the tokenizer reads it in a
    # spec that declares no closed_hiatus.
    spec = get(lang)
    alone = dataclasses.replace(
        spec, stress=dataclasses.replace(spec.stress, closed_hiatus=None))
    assert _IU.search(_nfd(G2P(lang, spec=alone).transcribe_word("saiu")))


def test_pt_specs_declare_the_rule():
    for code in LANGS:
        rule = get(code).stress.final_diphthongs
        assert rule.diphthongs == ("iu", "ui"), code
        assert rule.finals == ("s",), code


def test_specs_outside_portuguese_do_not_declare_the_rule():
    for code in ("gl-ES", "ext-PT-x-barranco", "mwl", "pt-PT-x-medieval"):
        stress = get(code).stress
        assert stress is None or stress.final_diphthongs is None, code
