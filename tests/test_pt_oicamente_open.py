"""European Portuguese ⟨-oicamente⟩: the adverb keeps the open [ɔj] of its adjective.

The source is the Acordo Ortográfico de 1945, Bases Analíticas, Base XXIII:
the adverbs in mente "que provêm de formas marcadas com acento agudo" take the
grave accent before the suffix (heròicamente), the mark of the open vowel. The
adjectives in ⟨-oico -oica⟩ took the acute before 1990 (heróico, estóico).
Cunha & Cintra (Nova Gramática do Português Contemporâneo, p. 53) state that
the stressed vowel of a simple word is in general not reduced in its derivatives,
mostly in -mente and -inho.
Infopédia (Dicionário da Língua Portuguesa, Porto Editora) gives [ɔj] in
heroicamente and estoicamente, written here in the spec's notation: its [ə]
and optional final (ə) are [ɨ]. The rule is ``PT_DERIV_OICAMENTE_OPEN`` in
``pt-PT.json``.

Base XXIII names only the adverbs in mente and the derivatives with an infix
⟨z⟩, so other derivatives keep the [oj] of the grapheme table. Terceira, São
Miguel, the African and Asian varieties, Barranquenho and the creoles keep the
output they had before the rule.
"""
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

# Infopédia gives estoicamente [iʃtɔjkɐˈmẽtə].
ESTOICAMENTE = "iʃtɔjkɐˈmẽtɨ"
# Adverbs of adjectives in ⟨-oico⟩. Infopédia gives heroicamente
# [irɔjkɐˈmẽt(ə)]; its initial vowel is another class, so only the diphthong
# is compared. paranoicamente is not an Infopédia headword; paranóico had the
# acute before 1990, so Base XXIII gives its adverb the open vowel.
OPEN_ADVERBS = ["heroicamente", "estoicamente", "paranoicamente"]
# Infopédia gives [oj] in estoicismo, boicote and moicano, and Base XXIII does
# not name a derivative in ⟨-ismo⟩ or a word whose base has no acute.
CLOSE = ["estoicismo", "boicote", "boicotar", "moicano", "boicotamente"]

PINNED = {
    "pt-PT-x-terceira": {"heroicamente": "ɨɾojkɐˈmẽtɨ", "estoicamente": "iʃtojkɐˈmẽtɨ"},
    "pt-PT-x-sao-miguel": {"heroicamente": "ɨɾøkɐˈmẽtɨ", "estoicamente": "iʃtøkɐˈmẽtɨ"},
    "pt-AO": {"heroicamente": "eɾojkaˈmẽtɨ", "estoicamente": "estojkaˈmẽtɨ"},
    "pt-CV": {"heroicamente": "erojkɐˈmẽte", "estoicamente": "estojkɐˈmẽte"},
    "pt-GW": {"heroicamente": "erojkɐˈmẽte", "estoicamente": "estojkɐˈmẽte"},
    "pt-MO": {"heroicamente": "ɨɾojkɐˈmẽtɨ", "estoicamente": "eʃtojkɐˈmẽtɨ"},
    "pt-MZ": {"heroicamente": "eɾojkɐˈmẽte", "estoicamente": "estojkɐˈmẽte"},
    "pt-ST": {"heroicamente": "erojkɐˈmẽte", "estoicamente": "estojkɐˈmẽte"},
    "pt-TL": {"heroicamente": "eɾojkaˈmẽte", "estoicamente": "estojkaˈmẽte"},
    "ext-PT-x-barranco": {"heroicamente": "hɨɾojkɐˈmẽtɨ", "estoicamente": "ehtojkɐˈmẽtɨ"},
}


@pytest.fixture(scope="module")
def engines():
    return {}


def ipa(engines, lang, word):
    if lang not in engines:
        engines[lang] = G2P(lang)
    return unicodedata.normalize("NFC", engines[lang].transcribe_word(word))


def oi_vowel(transcription):
    """The vowel of the ⟨oi⟩ diphthong before the [k] of ⟨-oicamente⟩."""
    plain = transcription.replace("ˈ", "").replace("ˌ", "")
    return plain[plain.index("jk") - 1]


def test_pt_pt_estoicamente_is_the_infopedia_reading(engines):
    assert ipa(engines, "pt-PT", "estoicamente") == ESTOICAMENTE


@pytest.mark.parametrize("word", OPEN_ADVERBS)
def test_pt_pt_oicamente_has_the_open_diphthong(engines, word):
    assert oi_vowel(ipa(engines, "pt-PT", word)) == "ɔ"


@pytest.mark.parametrize("word", CLOSE)
def test_pt_pt_other_oi_derivatives_keep_the_close_diphthong(engines, word):
    assert "ɔj" not in ipa(engines, "pt-PT", word).replace("ˈ", "").replace("ˌ", "")


@pytest.mark.parametrize("lang", EP_INHERITING)
@pytest.mark.parametrize("word", ["heroicamente", "estoicamente"])
def test_ep_lects_inherit_the_open_diphthong(engines, lang, word):
    assert oi_vowel(ipa(engines, lang, word)) == "ɔ"


@pytest.mark.parametrize("lang,word,expected", [
    (lang, word, out) for lang, row in sorted(PINNED.items())
    for word, out in sorted(row.items())
])
def test_lects_outside_the_rule_keep_their_output(engines, lang, word, expected):
    assert ipa(engines, lang, word) == expected
