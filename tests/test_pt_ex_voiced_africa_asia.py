"""Word-initial ⟨ex-⟩ + vowel is [z] in pt-AO, pt-MZ and pt-TL (``PT_INITIAL_EX_VOICED``).

Each table row is the Portal da Língua Portuguesa Dicionário fonético entry for the variety
(Luanda ``lda``, Maputo standard ``mpx``, Díli ``dli``). The expected consonant after the
initial vowel is read off the Portal string, not off the engine. ``exu``, the Yoruba loan, is
[ˈeʃu] in the Infopédia row of the unified pronunciation lexicon (pt-PT).
"""
import re

import pytest

from orthography2ipa import transcribe

PORTAL = {
    "pt-AO": {
        "exame": "e.zˈa.mɨ", "existir": "e.ziʃ.tˈiɾ", "exato": "e.zˈa.tʊ",
        "êxito": "ˈe.zi.tʊ", "exótico": "e.zˈɔ.ti.kʊ", "exemplo": "e.zˈẽjm.plʊ",
    },
    "pt-MZ": {
        "exame": "e.zˈɐ.mɨ", "existir": "e.ziʃ.tˈiɾ", "exato": "e.zˈa.tu",
        "êxito": "ˈe.zi.tu", "exótico": "e.zˈɔ.ti.ku", "exemplo": "e.zˈẽ.plu",
    },
    "pt-TL": {
        "exame": "zˈa.mɨ", "existir": "ziʃ.tˈiɾ", "exato": "zˈak.tʊ",
        "êxito": "ˈe.zi.tʊ", "exótico": "zˈɔ.ti.kʊ", "exemplo": "zˈẽm.plʊ",
    },
}

CASES = [(lang, word, portal) for lang, rows in PORTAL.items() for word, portal in rows.items()]


def consonant_after_initial_vowel(ipa: str) -> str:
    """The first consonant of *ipa* after an optional initial vowel; the Díli entries have none."""
    bare = re.sub(r"[ˈˌ.]", "", ipa)
    return re.sub(r"^[eɛɐi]", "", bare)[0]


@pytest.mark.parametrize("lang, word, portal", CASES)
def test_initial_ex_vowel_has_the_portal_consonant(lang, word, portal):
    assert consonant_after_initial_vowel(portal) == "z"
    assert consonant_after_initial_vowel(transcribe(word, lang)) == "z"


@pytest.mark.parametrize("lang", PORTAL)
@pytest.mark.parametrize("word", ["texto", "extra", "explicar", "excelente"])
def test_the_rule_does_not_fire_outside_initial_ex_vowel(lang, word):
    ipa = transcribe(word, lang)
    assert "ʃ" in ipa
    assert "z" not in ipa


@pytest.mark.parametrize("lang", ["pt-PT", "pt-PT-x-lisbon", "pt-PT-x-coimbra", "pt-AO", "pt-MZ", "pt-TL"])
@pytest.mark.parametrize("word", ["exu", "Exu"])
def test_exu_keeps_sh(lang, word):
    assert transcribe(word, lang) == "ˈeʃu"
