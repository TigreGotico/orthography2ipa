"""⟨ü⟩ and the vowel after it are one syllable in the pt-BR spellings with the trema.

Acordo Ortográfico 1990, Base XX, 5.º: "Os digramas gu e qu, em que o u se não
pronuncia, nunca se separam da vogal ou ditongo imediato (ne-gue, ne-guei; pe-que,
pe-quei), do mesmo modo que as combinações gu e qu em que o u se pronuncia".

A word in unaccented ⟨-es⟩ stresses its penultimate syllable, so the division
decides the stress: se-tai-gües has ⟨tai⟩ as its penultimate syllable.
"""
import pytest

from orthography2ipa import G2P

LANGS = ["pt-BR", "pt-BR-x-sp", "pt-BR-x-sul"]


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word,syllables", [
    ("tranqüilas", ["tran", "qüi", "las"]),
    ("lingüistas", ["lin", "güis", "tas"]),
    ("cinqüenta", ["cin", "qüen", "ta"]),
    ("bilíngüe", ["bi", "lín", "güe"]),
    ("lingüística", ["lin", "güís", "ti", "ca"]),
    ("seqüências", ["se", "qüên", "ci", "as"]),
])
def test_u_with_the_trema_stays_with_the_next_vowel(lang, word, syllables):
    assert G2P(lang)._syllables_cached(word) == syllables


def test_the_division_places_the_stress():
    assert "ˈtaj" in G2P("pt-BR").transcribe_word("setaigües")
