"""European Portuguese ⟨-oicidade⟩: the noun keeps the open [ɔj] of its adjective.

Cunha & Cintra (Nova Gramática do Português Contemporâneo, p. 53) state as a
general clause, with the hedge "em geral", that the stressed vowel of a simple
word is not reduced in its derivatives. Their examples are derivatives in
-mente and -inho. The adjectives in ⟨-oico -oica⟩ have a stressed [ɔj].
Infopédia (Dicionário da Língua Portuguesa, Porto Editora) gives [ɔj] in all
3 of its headwords in ⟨-oicidade⟩, written here in the spec's notation: its
optional final (ə) is [ɨ]. The rule is ``PT_DERIV_OICIDADE_OPEN`` in
``pt-PT.json``.

The rule needs ⟨-oicidade⟩ in the word. Infopédia gives [oj] in estoicismo, a
derivative of the same adjective, and in boicote and moicano. Terceira, São
Miguel, the African and Asian varieties, Barranquenho and the creoles keep the
output they had before the rule.
"""
import re
import unicodedata

import pytest

from orthography2ipa import G2P

EP_INHERITING = [
    "pt-PT", "pt-PT-x-lisbon", "pt-PT-x-coimbra", "pt-PT-x-acores",
    "pt-PT-x-madeira", "pt-PT-x-alentejo", "pt-PT-x-beira", "pt-PT-x-aveiro",
    "pt-PT-x-algarve", "pt-PT-x-alfena",
    "pt-PT-x-minho", "pt-PT-x-tras-os-montes", "pt-PT-x-viana",
    "pt-PT-x-porto", "pt-PT-x-braga",
]

# Infopédia gives estoicidade [(i)ʃtɔjsiˈdad(ə)].
ESTOICIDADE = "iʃtɔjsiˈdadɨ"
# Infopédia gives heroicidade [irɔjsiˈdad(ə)] and monozoicidade
# [mɔnɔzɔjsiˈdad(ə)]; their other vowels are other classes, so only the
# diphthong is compared.
OPEN_NOUNS = ["heroicidade", "estoicidade", "monozoicidade", "heroicidades"]
# Infopédia gives estoicismo [iʃtojˈsiʒmu], boicote [bojˈkɔtə] and moicano
# [mojˈkanu].
CLOSE = ["estoicismo", "boicote", "moicano"]

PINNED = {
    "pt-PT-x-terceira": {"estoicidade": "iʃtojsiˈdadɨ", "heroicidade": "ɨɾojsiˈdadɨ"},
    "pt-PT-x-sao-miguel": {"estoicidade": "iʃtøsiˈdadɨ", "heroicidade": "ɨɾøsiˈdadɨ"},
    "pt-AO": {"estoicidade": "estojsiˈdadɨ", "heroicidade": "eɾojsiˈdadɨ"},
    "pt-CV": {"estoicidade": "estojsiˈdade", "heroicidade": "erojsiˈdade"},
    "pt-GW": {"estoicidade": "estojsiˈdade", "heroicidade": "erojsiˈdade"},
    "pt-MO": {"estoicidade": "eʃtojsiˈdadɨ", "heroicidade": "ɨɾojsiˈdadɨ"},
    "pt-MZ": {"estoicidade": "estojsiˈdade", "heroicidade": "eɾojsiˈdade"},
    "pt-ST": {"estoicidade": "estojsiˈdade", "heroicidade": "erojsiˈdade"},
    "pt-TL": {"estoicidade": "estojsiˈdade", "heroicidade": "eɾojsiˈdade"},
    "ext-PT-x-barranco": {"estoicidade": "ehtojsiˈdadɨ", "heroicidade": "hɨɾojsiˈdadɨ"},
}


@pytest.fixture(scope="module")
def engines():
    return {}


def ipa(engines, lang, word):
    if lang not in engines:
        engines[lang] = G2P(lang)
    return unicodedata.normalize("NFC", engines[lang].transcribe_word(word))


def plain(transcription):
    return transcription.replace("ˈ", "").replace("ˌ", "")


def oi_vowel(transcription):
    """The vowel of the ⟨oi⟩ diphthong before the [s] of ⟨-oicidade⟩.

    The northern lects write an apical [s̺], so only the [j] and the [s] are matched.
    """
    return re.search(r"(.)js", plain(transcription)).group(1)


def test_pt_pt_estoicidade_is_the_infopedia_reading(engines):
    assert ipa(engines, "pt-PT", "estoicidade") == ESTOICIDADE


@pytest.mark.parametrize("word", OPEN_NOUNS)
def test_pt_pt_oicidade_has_the_open_diphthong(engines, word):
    assert oi_vowel(ipa(engines, "pt-PT", word)) == "ɔ"


@pytest.mark.parametrize("word", CLOSE)
def test_pt_pt_other_oi_words_keep_the_close_diphthong(engines, word):
    text = plain(ipa(engines, "pt-PT", word))
    assert "oj" in text and "ɔj" not in text


@pytest.mark.parametrize("lang", EP_INHERITING)
@pytest.mark.parametrize("word", ["heroicidade", "estoicidade"])
def test_ep_lects_inherit_the_open_diphthong(engines, lang, word):
    assert oi_vowel(ipa(engines, lang, word)) == "ɔ"


@pytest.mark.parametrize("lang,word,expected", [
    (lang, word, out) for lang, row in sorted(PINNED.items())
    for word, out in sorted(row.items())
])
def test_lects_outside_the_rule_keep_their_output(engines, lang, word, expected):
    assert ipa(engines, lang, word) == expected
