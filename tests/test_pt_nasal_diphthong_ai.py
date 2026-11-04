"""⟨ãi⟩ is one nasal diphthong, the same as ⟨ãe⟩.

Acordo Ortográfico 1990, Base VII, 3 a): "Os ditongos representados por vogal
com til e semivogal são quatro, considerando-se apenas a língua padrão
contemporânea: ãe (usado em vocábulos oxítonos e derivados), ãi (usado em
vocábulos anoxítonos e derivados), ão e õe. Exemplos: cães, Guimarães, mãe,
mãezinha; cãibas, cãibeiro, cãibra, zãibo; [...]"

So the ⟨ãi⟩ of cãibra is one syllable nucleus, and the stress of the
paroxytone falls on it. Cruz-Ferreira (1999: 128) lists one nasal diphthong
[ɐ̃i] for European Portuguese (cem), and the Portal da Língua Portuguesa
Dicionário fonético writes cãibra [ˈkɐ̃jbɾɐ] and zãibo [ˈzɐ̃jbu], with the
nucleus of mãe [ˈmɐ̃j]. Barbosa & Albano (2004: 230) form the Brazilian
Portuguese nasalised diphthongs from [ẽ ɐ̃ õ ũ] and the offglide [ɪ̯̃].
This library writes that offglide [j̃] (mãe [ˈmɐ̃j̃]).
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get, get_syllabifier

AO_BASE_VII_3A = ["cãibas", "cãibra", "zãibo"]

#: The transcription each example starts with: the stress mark, the onset
#: and the nasal diphthong, then the [b] of the next syllable.
_ONSET = {"c": "k", "z": "z"}


def _head(word: str) -> str:
    return "ˈ" + _ONSET[word[0]] + "ɐ̃j̃b"


LANGS = ["pt-PT", "pt-BR", "pt-PT-x-lisbon", "pt-BR-x-sp", "pt-AO", "pt-UY"]


@pytest.fixture
def without_syllabifier_plugin(monkeypatch):
    from orthography2ipa import registry
    monkeypatch.setattr(registry, "_syllabifiers", {})


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word", AO_BASE_VII_3A)
def test_ai_is_one_stressed_nasal_diphthong(lang, word):
    # The paroxytone stresses the first syllable, and its nucleus is the
    # nasal diphthong: no stress mark and no syllable break inside it.
    ipa = G2P(lang).transcribe_word(word)
    assert ipa.startswith(_head(word)), ipa


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", AO_BASE_VII_3A)
def test_without_the_plugin_and_paths_agree(lang, word, monkeypatch):
    with_plugin = G2P(lang).transcribe_word(word)
    from orthography2ipa import registry
    monkeypatch.setattr(registry, "_syllabifiers", {})
    assert get_syllabifier(lang) is None
    ipa = G2P(lang).transcribe_word(word)
    assert ipa.startswith(_head(word)), ipa
    assert ipa == with_plugin


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
def test_bundled_syllabifier_keeps_ai_in_one_syllable(
        lang, without_syllabifier_plugin):
    assert G2P(lang)._syllables_cached("cãibra") == ["cãi", "bra"]


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
def test_ai_reads_as_ae(lang):
    # Base VII, 3 a) puts ⟨ãi⟩ and ⟨ãe⟩ in one class, and every source above
    # gives the two one nucleus.
    graphemes = get(lang).graphemes
    assert graphemes["ãi"] == graphemes["ãe"]


#: European Portuguese, letter for letter: the Portal da Língua Portuguesa
#: Dicionário fonético, with the offglide written [j̃]. The plural ⟨s⟩ is
#: syllable-final [ʃ] (Cruz-Ferreira 1999: 128).
PT_PT = [
    ("cãibra", "ˈkɐ̃j̃bɾɐ"),
    ("cãibras", "ˈkɐ̃j̃bɾɐʃ"),
    ("zãibo", "ˈzɐ̃j̃bu"),
]


@pytest.mark.parametrize("word,expected", PT_PT)
def test_pt_pt_transcription(word, expected):
    assert G2P("pt-PT").transcribe_word(word) == expected


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word,head", [("mãe", "ˈmɐ̃j̃"), ("cães", "ˈkɐ̃j̃")])
def test_ae_is_unchanged(lang, word, head):
    ipa = G2P(lang).transcribe_word(word)
    assert ipa.startswith(head), ipa


def test_specs_outside_the_standard_do_not_read_ai():
    # Base VII, 3 a) speaks of "a língua padrão contemporânea".
    for code in ("pt-PT-x-medieval", "gl-ES", "mwl"):
        assert "ãi" not in get(code).graphemes, code
