"""⟨ã⟩ writes the central nasal vowel [ɐ̃] in pt-PT and pt-BR.

Cruz-Ferreira (1999, Handbook of the IPA, p. 127) lists the European
Portuguese nasalized vowels as [ĩ ẽ ɐ̃ õ ũ]; Barbosa & Albano (2004: 230)
transcribe ímã as [ˈimɐ̃]. The coda nasal of canta already gives [ɐ̃], so a
spec's ⟨ã⟩ must be the nasal vowel of its own canta.
"""
from __future__ import annotations

import glob
import os
import re
import unicodedata

import pytest

import orthography2ipa
from orthography2ipa import G2P

DATA = os.path.join(os.path.dirname(orthography2ipa.__file__), "data")
PT = sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(DATA, "pt-*.json"))
            if not p.endswith("pt-PT-x-medieval.json")) + ["ext-PT-x-barranco"]
WORDS = ["maçã", "irmã", "lã", "fã", "afã", "maçãs", "manhã", "romã", "ímã",
         "cristãmente"]


def _nasal_a(lang: str) -> str:
    # The nasal vowel before [t] in canta, decomposed.
    ipa = unicodedata.normalize("NFD", G2P(lang).transcribe_word("canta"))
    return re.search("(\\w̃)t", ipa).group(1)


@pytest.mark.parametrize("word, ipa", [("maçã", "mɐˈsɐ̃"), ("lã", "ˈlɐ̃"),
                                       ("fã", "ˈfɐ̃"), ("afã", "ɐˈfɐ̃"),
                                       ("irmã", "iɾˈmɐ̃"), ("maçãs", "mɐˈsɐ̃ʃ")])
def test_pt_pt_reads_the_central_nasal(word, ipa):
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("word, ipa", [("maçã", "maˈsɐ̃"), ("lã", "ˈlɐ̃"),
                                       ("irmã", "iɾˈmɐ̃")])
def test_pt_br_reads_the_central_nasal(word, ipa):
    assert G2P("pt-BR").transcribe_word(word) == ipa


def test_pt_br_ima_ends_in_the_central_nasal():
    # Barbosa & Albano (2004: 230): ímã [ˈimɐ̃].
    assert G2P("pt-BR").transcribe_word("ímã").endswith("mɐ̃")


@pytest.mark.parametrize("lang", PT)
@pytest.mark.parametrize("word", WORDS)
def test_every_child_reads_its_own_nasal_a(lang, word):
    ipa = unicodedata.normalize("NFD", G2P(lang).transcribe_word(word))
    assert "a\u0303" not in ipa, ipa
    assert _nasal_a(lang) in ipa, (ipa, _nasal_a(lang))


@pytest.mark.parametrize("word, ipa", [("mãe", "ˈmɐ̃j̃"), ("pão", "ˈpɐ̃w̃"),
                                       ("cães", "ˈkɐ̃j̃ʃ"), ("cãibra", "ˈkɐ̃j̃bɾɐ")])
def test_the_nasal_diphthongs_keep_their_reading(word, ipa):
    assert G2P("pt-PT").transcribe_word(word) == ipa


def test_medieval_keeps_its_open_nasal():
    # pt-PT-x-medieval is the base the modern specs inherit from; its canta
    # has [ã], and its ⟨ã⟩ stays the same vowel.
    assert _nasal_a("pt-PT-x-medieval") == "a\u0303"
    assert G2P("pt-PT-x-medieval").transcribe_word("lã") == "ˈlã"
