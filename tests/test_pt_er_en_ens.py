"""Portuguese word-final ⟨-er⟩, ⟨-en⟩ and ⟨-ens⟩.

Expected values come from the sources named in the rule notes of
``PT_ER_CLOSE``, ``PT_LEX_OPEN_ER``, ``PT_FINAL_EN_NUCLEUS``,
``PT_FINAL_EN_CODA`` and ``BR_FINAL_EM_GLIDE`` / ``BR_FINAL_ENS_GLIDE``:

* Infopédia (Dicionário da Língua Portuguesa) and Priberam give the stressed
  vowel of a European Portuguese infinitive in ⟨-er⟩ as close-mid [e]
  (comer [kuˈmer], ter [ˈter]) and of a few non-verbs as open-mid [ɛ]
  (mulher [muˈʎɛr], talher [tɐˈʎɛr]). Infopédia writes the learned ⟨-en⟩ as
  [ɛn] (hífen [ˈifɛn], pólen [ˈpɔlɛn]).
* Barbosa & Albano 2004 and Ciberdúvidas give Brazilian ⟨-en⟩ and ⟨-ens⟩ as
  the nasal diphthong [ẽj̃] (hífen [ˈifẽj̃]).
* The Baixo-Minho diphthongises the close stressed vowel to [je]
  (Leite de Vasconcellos 1901, §44-b), so a Porto infinitive is [kuˈmjeɾ].

Rows that must not move (African and Asian varieties, the creoles, the
Uruguayan variety, Barranquenho) pin the output they had before these rules,
because no source for them was read.
"""
import unicodedata

import pytest

from orthography2ipa import G2P

EP_STANDARD = [
    "pt-PT", "pt-PT-x-lisbon", "pt-PT-x-coimbra", "pt-PT-x-acores",
    "pt-PT-x-madeira", "pt-PT-x-alentejo", "pt-PT-x-beira", "pt-PT-x-aveiro",
    "pt-PT-x-sao-miguel", "pt-PT-x-terceira", "pt-PT-x-algarve",
    "pt-PT-x-alfena", "pt-PT-x-minho", "pt-PT-x-trasosmontes",
    "pt-PT-x-viana",
]
EP_DIPHTHONGISING = ["pt-PT-x-porto", "pt-PT-x-braga"]
EP_ALL = EP_STANDARD + EP_DIPHTHONGISING
BR_DIPHTHONG_CHILDREN = [
    "pt-BR-x-brasilia", "pt-BR-x-caipira", "pt-BR-x-fluminense",
    "pt-BR-x-pr", "pt-BR-x-rj", "pt-BR-x-sp", "pt-BR-x-sul",
]
# These five reduce a post-stressed nasal ⟨e⟩ to [ɪ̃] in ⟨-em⟩ already, so
# their ⟨-en -ens⟩ follow their own ⟨-em⟩ and carry no glide on it.
BR_REDUCING_CHILDREN = [
    "pt-BR-x-bahia", "pt-BR-x-ce", "pt-BR-x-mg", "pt-BR-x-norte",
    "pt-BR-x-recife",
]
BR_CHILDREN = BR_DIPHTHONG_CHILDREN + BR_REDUCING_CHILDREN

INFINITIVES = ["comer", "beber", "ter", "ver", "ler", "crer", "querer",
               "fazer", "haver", "entender", "escrever", "perder"]
OPEN_ER_WORDS = ["mulher", "colher", "talher", "qualquer", "quaisquer",
                 "quer", "mister", "aluguer", "chanceler", "chofer",
                 "malmequer", "mester", "cateter", "ureter", "rater"]
LEARNED_EN = {
    "hífen": "ˈifɛn",
    "pólen": "ˈpɔlɛn",
    "líquen": "ˈlikɛn",
    "sémen": "ˈsɛmɛn",
    "gérmen": "ˈʒɛɾmɛn",
}


@pytest.fixture(scope="module")
def engines():
    return {}


def ipa(engines, lang, word):
    if lang not in engines:
        engines[lang] = G2P(lang)
    return unicodedata.normalize("NFC", engines[lang].transcribe_word(word))


# ─── European Portuguese ⟨-er⟩ ──────────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("comer", "kuˈmeɾ"), ("ter", "ˈteɾ"), ("ver", "ˈveɾ"), ("ler", "ˈleɾ"),
    ("crer", "ˈkɾeɾ"), ("fazer", "fɐˈzeɾ"), ("haver", "ɐˈveɾ"),
    ("entender", "ẽtẽˈdeɾ"), ("querer", "kɨˈɾeɾ"),
])
def test_pt_pt_infinitive_has_close_mid_vowel(engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


@pytest.mark.parametrize("lang", EP_STANDARD)
@pytest.mark.parametrize("word", INFINITIVES)
def test_ep_lects_infinitive_stressed_vowel_is_close_mid(engines, lang, word):
    out = ipa(engines, lang, word)
    assert out.endswith("eɾ"), out
    assert not out.endswith("ɛɾ"), out


@pytest.mark.parametrize("word,expected", [
    ("comer", "kuˈmjeɾ"), ("ter", "ˈtjeɾ"), ("perder", "pɨɾˈdjeɾ"),
])
@pytest.mark.parametrize("lang", EP_DIPHTHONGISING)
def test_baixo_minho_diphthongises_the_close_infinitive_vowel(
        engines, lang, word, expected):
    assert ipa(engines, lang, word) == expected


@pytest.mark.parametrize("lang", EP_STANDARD)
@pytest.mark.parametrize("word", OPEN_ER_WORDS)
def test_ep_lects_lexically_open_er_words_stay_open(engines, lang, word):
    assert ipa(engines, lang, word).endswith("ɛɾ")


@pytest.mark.parametrize("word,expected", [
    ("mulher", "muˈʎɛɾ"), ("colher", "kuˈʎɛɾ"), ("talher", "tɐˈʎɛɾ"),
    ("mister", "miʃˈtɛɾ"), ("quer", "ˈkɛɾ"),
])
def test_pt_pt_open_er_nouns_exact(engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


@pytest.mark.parametrize("word,expected", [
    ("mulher", "muˈʎjɛɾ"), ("talher", "tɐˈʎjɛɾ"),
])
@pytest.mark.parametrize("lang", EP_DIPHTHONGISING)
def test_baixo_minho_diphthongises_the_open_er_noun_vowel(
        engines, lang, word, expected):
    assert ipa(engines, lang, word) == expected


@pytest.mark.parametrize("word,expected", [
    ("tem", "ˈtɐ̃j̃"), ("porém", "puˈɾɐ̃j̃"), ("ninguém", "nĩˈɡɐ̃j̃"),
    ("homens", "ˈɔmɐ̃j̃ʃ"), ("bens", "ˈbɐ̃j̃ʃ"), ("também", "tɐ̃ˈbɐ̃j̃"),
    ("mulheres", "muˈʎɛɾɨʃ"),
])
def test_pt_pt_neighbours_do_not_move(engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


@pytest.mark.parametrize("word", ["caráter", "carácter", "revólver", "líder"])
def test_unstressed_final_er_is_untouched(engines, word):
    assert ipa(engines, "pt-PT", word).endswith("ɨɾ")


# ─── European Portuguese ⟨-en⟩ ──────────────────────────────────────────

@pytest.mark.parametrize("word,expected", sorted(LEARNED_EN.items()))
def test_pt_pt_learned_en_keeps_open_vowel_and_final_n(
        engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


def test_pt_pt_abdomen_ends_in_open_e_and_n(engines):
    assert ipa(engines, "pt-PT", "abdómen") == "ɐbˈdɔmɛn"


@pytest.mark.parametrize("lang", EP_ALL)
@pytest.mark.parametrize("word", sorted(LEARNED_EN))
def test_ep_lects_learned_en_ends_in_open_e_and_n(engines, lang, word):
    assert ipa(engines, lang, word).endswith("ɛn")


@pytest.mark.parametrize("word,expected", [
    ("hífenes", "ˈifɨnɨʃ"), ("líquenes", "ˈlikɨnɨʃ"),
])
def test_pt_pt_en_plural_is_not_a_final_n(engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


# ─── Brazilian ⟨-en⟩ and ⟨-ens⟩ ─────────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("hífen", "ˈifẽj̃"), ("pólen", "ˈpɔlẽj̃"), ("líquen", "ˈlikẽj̃"),
    ("bens", "ˈbẽj̃s"), ("homens", "ˈomẽj̃s"), ("jovens", "ˈʒovẽj̃s"),
    ("parabéns", "paɾaˈbẽj̃s"), ("viagens", "viˈaʒẽj̃s"),
])
def test_pt_br_final_en_and_ens_end_in_the_nasal_diphthong(
        engines, word, expected):
    assert ipa(engines, "pt-BR", word) == expected


@pytest.mark.parametrize("lang", BR_DIPHTHONG_CHILDREN)
@pytest.mark.parametrize("word", ["bens", "homens", "jovens", "hífen"])
def test_pt_br_lects_carry_the_glide_on_en_and_ens(engines, lang, word):
    out = ipa(engines, lang, word)
    assert "j̃" in out, out
    assert out.rstrip("sʃ").endswith("j̃"), out


@pytest.mark.parametrize("lang", ["pt-BR"] + BR_CHILDREN)
def test_pt_br_ens_matches_its_singular_em(engines, lang):
    em = ipa(engines, lang, "homem")
    ens = ipa(engines, lang, "homens")
    assert ens.startswith(em), (em, ens)


@pytest.mark.parametrize("word,expected", [
    ("bem", "ˈbẽj̃"), ("homem", "ˈomẽj̃"), ("também", "tɐ̃ˈbẽj̃"),
    ("bom", "ˈbõ"), ("sons", "ˈsõs"), ("jardins", "ʒaɾˈd͡ʒĩs"),
])
def test_pt_br_other_nasal_endings_do_not_move(engines, word, expected):
    assert ipa(engines, "pt-BR", word) == expected


# ─── rows that keep their output ─────────────────────────────────────────

UNCHANGED = {
    "pt-AO": {"comer": "koˈmɛɾ", "mulher": "muˈʎɛɾ", "hífen": "ˈifẽ",
              "pólen": "ˈpɔlẽ", "homens": "ˈɔmẽj̃s", "bens": "ˈbẽj̃s"},
    "pt-CV": {"comer": "kuˈmer", "mulher": "muˈʎer", "hífen": "ˈifẽ",
              "pólen": "ˈpɔlẽ", "homens": "ˈɔmẽj̃s", "bens": "ˈbẽj̃s"},
    "pt-GW": {"comer": "koˈmɛr", "mulher": "muˈʎɛr", "hífen": "ˈifẽ",
              "pólen": "ˈpɔlẽ", "homens": "ˈɔmẽj̃s", "bens": "ˈbẽj̃s"},
    "pt-MO": {"comer": "kuˈmɛʁ", "mulher": "muˈʎɛʁ", "hífen": "ˈifẽ",
              "pólen": "ˈpɔlẽ", "homens": "ˈɔmẽj̃ʃ", "bens": "ˈbẽj̃ʃ"},
    "pt-MZ": {"comer": "koˈmɛɾ", "mulher": "muˈʎɛɾ", "hífen": "ˈifẽ",
              "pólen": "ˈpɔlẽ", "homens": "ˈɔmẽs", "bens": "ˈbẽs"},
    "pt-ST": {"comer": "koˈmɛr", "mulher": "muˈʎɛr", "hífen": "ˈifẽ",
              "pólen": "ˈpɔlẽ", "homens": "ˈɔmẽj̃s", "bens": "ˈbẽj̃s"},
    "pt-TL": {"comer": "koˈmɛɾ", "mulher": "muˈlɛɾ", "hífen": "ˈifẽ",
              "pólen": "ˈpɔlẽ", "homens": "ˈɔmẽj̃s", "bens": "ˈbẽj̃s"},
    "pt-UY": {"comer": "koˈmeɾ", "mulher": "muˈjeɾ", "hífen": "ˈifẽ",
              "pólen": "ˈpɔlẽ", "homens": "ˈomẽs", "bens": "ˈbẽs"},
    "ext-PT-x-barrancos": {"comer": "ˈkɔmɨ", "mulher": "ˈmuʎɨ",
                           "hífen": "ˈhifɨ̃", "pólen": "ˈpɔlɨ̃",
                           "homens": "huˈmẽ", "bens": "ˈbẽ"},
    "kea": {"comer": "ˈomeɾ", "mulher": "ˈmuʎeɾ", "hífen": "ˈifẽ",
            "pólen": "ˈpɔlẽ", "homens": "ˈomẽʃ", "bens": "ˈbẽʃ"},
    "cri": {"comer": "ɔmɛɾ", "mulher": "muʎɛɾ", "hífen": "fẽ",
            "pólen": "plẽ", "homens": "ɔmẽʃ", "bens": "bẽʃ"},
    "pre": {"comer": "omer", "mulher": "muɫher", "hífen": "hfẽ",
            "pólen": "plẽ", "homens": "homẽʃ", "bens": "bẽʃ"},
}


@pytest.mark.parametrize("lang,word", [
    (lang, word) for lang, rows in sorted(UNCHANGED.items()) for word in rows
])
def test_varieties_without_a_source_keep_their_output(engines, lang, word):
    assert ipa(engines, lang, word) == UNCHANGED[lang][word]
