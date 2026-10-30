"""Unstressed nasal ⟨e⟩ in Mirandese, by word position and dialect.

Expected vowels come from Leite de Vasconcellos, Estudos de Philologia
Mirandesa I (1900): §76 (p. 238) gives medial -en- as the "e surdo" nasal ẽ̥
[ɨ̃] (antẽ̥dér, lhẽ̥mbrar, bẽ̥ntura); §77 (p. 239) gives final -em as the
intermediate ḙ̃ in "mirandês normal" (amḙ̃, debḙ̃), which p. 178 likens to
German final e and to [ə], and as ẽ̥ [ɨ̃] in Sendinês (amẽ̥, debẽ̥).
"""
import unicodedata

import pytest

from orthography2ipa import G2P

TILDE = "̃"


def nasal_vowels(ipa: str) -> list:
    """The nasalised vowels of *ipa*, in order."""
    ipa = unicodedata.normalize("NFD", ipa)
    return [unicodedata.normalize("NFC", ipa[i - 1] + TILDE)
            for i, c in enumerate(ipa) if c == TILDE]


@pytest.mark.parametrize("dialect", ["mwl", "mwl-x-sendim", "mwl-x-ifanes"])
@pytest.mark.parametrize("word, expected", [
    ("antender", ["ɐ̃", "ɨ̃"]),
    ("lhembrar", ["ɨ̃"]),
    ("bentura", ["ɨ̃"]),
])
def test_medial_unstressed_en_is_central(dialect, word, expected):
    assert nasal_vowels(G2P(dialect).transcribe(word)) == expected


@pytest.mark.parametrize("dialect, expected", [
    ("mwl", ["ə̃"]),
    ("mwl-x-ifanes", ["ə̃"]),
    ("mwl-x-sendim", ["ɨ̃"]),
])
@pytest.mark.parametrize("word", ["deben", "amen"])
def test_final_unstressed_en_by_dialect(dialect, expected, word):
    assert nasal_vowels(G2P(dialect).transcribe(word)) == expected


@pytest.mark.parametrize("dialect", ["mwl", "mwl-x-sendim", "mwl-x-ifanes"])
@pytest.mark.parametrize("word, expected", [
    ("cento", ["ẽ"]),
    ("ben", ["ẽ"]),
])
def test_stressed_en_stays_close_mid(dialect, word, expected):
    assert nasal_vowels(G2P(dialect).transcribe(word)) == expected
