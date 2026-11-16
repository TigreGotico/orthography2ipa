"""A stressed word-final ⟨el ol⟩ has an open vowel in pt-BR.

The citations are in the notes of BR_FINAL_EL_OPEN and BR_FINAL_OL_OPEN in
pt-BR.json. The expected values come from these sources:

* Bagno (2012: 148): mel [mɛʊ], gol [goʊ], [sɔli] for sol, [pa'pɛli] for papel.
* Bagno (2012: 191): final ⟨-el⟩ reads as ⟨-éu⟩. This covers hotel, pastel, gel.
* Battisti & Moras (2016: 100): the vowel classes of papel, aluguel, futebol,
  lençol, maleável and horrível.
* Acordo Ortográfico 1990, Base VIII, 1.º d): ⟨ói⟩ is an open diphthong. farol,
  caracol and girassol have the plurals faróis, caracóis and girassóis.

* Infopédia gives the close vowel of solto [ˈsoɫtu], feltro [ˈfeɫtru],
  amor [ɐˈmor] and vez [ˈveʃ].

The rows of the second test are controls. They pass before the rule too, and
each one fails when the rule loses one of its conditions.
"""
import pytest

from orthography2ipa import G2P
from orthography2ipa.registry import get

VOCALISING_CHILDREN = [
    "pt-BR-x-bahia", "pt-BR-x-ce", "pt-BR-x-floripa", "pt-BR-x-fluminen",
    "pt-BR-x-mg", "pt-BR-x-norte", "pt-BR-x-pr", "pt-BR-x-recife",
    "pt-BR-x-rj", "pt-BR-x-sp", "pt-BR-x-sul",
]
RETROFLEX_CHILDREN = ["pt-BR-x-caipira", "pt-BR-x-cuiaba"]


def reading(word: str, lang: str = "pt-BR") -> str:
    return G2P(lang, expose_ambiguous_endings=False).transcribe_word(word)


@pytest.mark.parametrize("word, ipa", [
    ("papel", "paˈpɛw"),
    ("mel", "ˈmɛw"),
    ("hotel", "oˈtɛw"),
    ("aluguel", "aluˈɡɛw"),
    ("pastel", "pasˈtɛw"),
    ("gel", "ˈʒɛw"),
    ("futebol", "futeˈbɔw"),
    ("farol", "faˈɾɔw"),
    ("lençol", "lẽˈsɔw"),
    ("girassol", "ʒiɾaˈsɔw"),
    ("caracol", "kaɾaˈkɔw"),
])
def test_stressed_final_el_ol_is_open(word, ipa):
    assert reading(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("gol", "ˈɡow"),      # PT_LEX_CLOSE_O
    ("nível", "ˈnivew"),
    ("móvel", "ˈmɔvew"),
    ("túnel", "ˈtũnew"),
    ("solto", "ˈsowtu"),
    ("feltro", "ˈfewtɾu"),
    ("amor", "aˈmoɾ"),
    ("vez", "ˈves"),
])
def test_other_final_laterals_keep_their_reading(word, ipa):
    assert reading(word) == ipa


def test_gol_stays_close_after_the_rule_exists():
    rules = [rule.id for rule in get("pt-BR").allophone_rules]
    assert rules.index("PT_LEX_CLOSE_O") < rules.index("BR_FINAL_OL_OPEN")


@pytest.mark.parametrize("lang", VOCALISING_CHILDREN)
@pytest.mark.parametrize("word, ending", [("papel", "ˈpɛw"), ("lençol", "ˈsɔw")])
def test_vocalising_children_read_the_open_vowel(lang, word, ending):
    assert reading(word, lang).endswith(ending)


@pytest.mark.parametrize("lang", RETROFLEX_CHILDREN)
@pytest.mark.parametrize("word, ending", [("papel", "ˈpɛɻ"), ("lençol", "ˈsɔɻ")])
def test_children_with_a_retroflex_coda_read_the_open_vowel(lang, word, ending):
    assert reading(word, lang).endswith(ending)


def test_uruguayan_portuguese_switches_both_rules_off():
    rules = {rule.id: rule for rule in get("pt-UY").allophone_rules}
    assert not rules["BR_FINAL_EL_OPEN"].phonemes
    assert not rules["BR_FINAL_OL_OPEN"].phonemes
