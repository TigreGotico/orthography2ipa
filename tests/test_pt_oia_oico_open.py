"""European Portuguese ⟨-oia⟩ and ⟨-oico⟩: the stressed diphthong is the open [ɔj].

Expected values are the Infopédia (Dicionário da Língua Portuguesa, Porto
Editora) readings of the portuguese-unified lexicon, region pt-PT, written in
the spec's notation: Infopédia [ə] is [ɨ], its optional final (ə) is [ɨ], its
flap [r] is [ɾ] and its trill [ʀ] is [ʁ]. The rules and their sources are
``PT_SUFFIX_OIA_OPEN``, ``PT_SUFFIX_OICO_OPEN`` and ``PT_LEX_OIA_CLOSE`` in
``pt-PT.json``.

São Miguel spells ⟨oi⟩ as its own monophthong [ø] in the grapheme table, so
the rules do not reach it there. Terceira, the African and Asian varieties,
Barranquenho and the creoles disable the rules, as they disable
``PT_SUFFIX_OIDE_OPEN``. These lects pin the output they had before the rules.
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

# Infopédia readings, spec notation.
OPEN = {
    "boia": "ˈbɔjɐ", "joia": "ˈʒɔjɐ", "jiboia": "ʒiˈbɔjɐ", "paranoia": "pɐɾɐˈnɔjɐ",
    "tramoia": "tɾɐˈmɔjɐ", "semijoia": "sɨmiˈʒɔjɐ", "metanoia": "mɨtɐˈnɔjɐ",
    "chirimoia": "ʃiɾiˈmɔjɐ", "tipoia": "tiˈpɔjɐ", "troia": "ˈtɾɔjɐ", "soia": "ˈsɔjɐ",
    "paranoico": "pɐɾɐˈnɔjku", "benzoico": "bẽˈzɔjku", "azoico": "ɐˈzɔjku",
    "anecoico": "ɐnɨˈkɔjku", "dicroico": "diˈkɾɔjku", "minoico": "miˈnɔjku",
    "monoico": "muˈnɔjku", "zoico": "ˈzɔjku", "troica": "ˈtɾɔjkɐ",
}
# Infopédia words that also differ outside the diphthong: only the diphthong
# after the stress mark is compared.
DIPHTHONG_ONLY = {
    "heroico": "iˈɾɔjku", "estoico": "(i)ʃˈtɔjku", "claraboia": "klaɾɐˈbɔjɐ",
    "sequoia": "sɨˈkɔjɐ", "mesozoico": "mɛzɔˈzɔjku", "paleozoico": "paljɔˈzɔjku",
    "epiploico": "epiˈplɔjku", "etanoico": "etɐˈnɔjku",
}
# Words whose European spelling before 1990 had no acute keep the close [oj].
# poia is [ˈpojɐ] in Infopédia.
CLOSE = ["apoia", "apoias", "apoiam", "desapoia", "desapoias", "desapoiam",
         "saloia", "saloias", "poia", "poias", "arroia", "arroias", "arroiam"]
# Other ⟨oi⟩ words: the rules need ⟨a⟩, or ⟨c⟩ and a back vowel, after a
# stressed ⟨oi⟩, so these keep the [oj] of the grapheme table. Infopédia gives
# [oj] in the unstressed ⟨oi⟩ of boicote [bojˈkɔt(ə)], boicotar and moicano.
NEIGHBOURS = ["apoio", "comboio", "boina", "dezoito", "foice", "coice", "oiço",
              "boiada", "noite", "apoiado", "apoiamos", "aboiar",
              "boicote", "boicotar", "moicano"]

PINNED = {
    "pt-PT-x-terceira": {"boia": "ˈbwojɐ", "jiboia": "ʒiˈbwojɐ", "heroico": "ɨˈɾojku", "paranoico": "pɐɾɐˈnojku",
        "apoia": "ɐˈpwojɐ", "poia": "ˈpwojɐ", "saloia": "sɐˈlojɐ"},
    "pt-PT-x-sao-miguel": {"boia": "ˈbøɐ", "jiboia": "ʒiˈbøɐ", "heroico": "ɨˈɾøku", "paranoico": "pɐɾɐˈnøku",
        "apoia": "ɐˈpøɐ", "poia": "ˈpøɐ", "saloia": "sɐˈløɐ"},
    "pt-AO": {"boia": "ˈboja", "jiboia": "ʒiˈboja", "heroico": "eˈɾojkʊ", "paranoico": "paɾaˈnojkʊ",
        "apoia": "aˈpoja", "poia": "ˈpoja", "saloia": "saˈloja"},
    "pt-CV": {"boia": "ˈbojɐ", "jiboia": "ʒiˈbojɐ", "heroico": "eˈrojku", "paranoico": "pɐrɐˈnojku",
        "apoia": "ɐˈpojɐ", "poia": "ˈpojɐ", "saloia": "sɐˈlojɐ"},
    "pt-GW": {"boia": "ˈbojɐ", "jiboia": "ʒiˈbojɐ", "heroico": "eˈrojku", "paranoico": "pɐrɐˈnojku",
        "apoia": "ɐˈpojɐ", "poia": "ˈpojɐ", "saloia": "sɐˈlojɐ"},
    "pt-MO": {"boia": "ˈbojɐ", "jiboia": "ʒiˈbojɐ", "heroico": "ɨˈɾojku", "paranoico": "pɐɾɐˈnojku",
        "apoia": "ɐˈpojɐ", "poia": "ˈpojɐ", "saloia": "sɐˈlojɐ"},
    "pt-MZ": {"boia": "ˈbojɐ", "jiboia": "ʒiˈbojɐ", "heroico": "eˈɾojku", "paranoico": "pɐɾɐˈnojku",
        "apoia": "ɐˈpojɐ", "poia": "ˈpojɐ", "saloia": "sɐˈlojɐ"},
    "pt-ST": {"boia": "ˈbojɐ", "jiboia": "ʒiˈbojɐ", "heroico": "eˈrojku", "paranoico": "pɐrɐˈnojku",
        "apoia": "ɐˈpojɐ", "poia": "ˈpojɐ", "saloia": "sɐˈlojɐ"},
    "pt-TL": {"boia": "ˈboja", "jiboia": "ʒiˈboja", "heroico": "eˈɾojko", "paranoico": "paɾaˈnojko",
        "apoia": "aˈpoja", "poia": "ˈpoja", "saloia": "saˈloja"},
    "ext-PT-x-barranco": {"boia": "boˈjɐ", "jiboia": "ʒiˈbojɐ", "heroico": "hɨˈɾojku", "paranoico": "pɐɾɐˈnojku",
        "apoia": "ɐˈpojɐ", "poia": "poˈjɐ", "saloia": "saˈlojɐ"},
    "aoa": {"boia": "boia", "jiboia": "dʒiboia", "heroico": "heroio", "paranoico": "paranoio",
        "apoia": "apoia", "poia": "poia", "saloia": "saloia"},
    "cri": {"boia": "bɔia", "jiboia": "ʒibɔia", "heroico": "ɛɾɔiɔ", "paranoico": "paɾanɔiɔ",
        "apoia": "apɔia", "poia": "pɔia", "saloia": "salɔia"},
    "idb": {"boia": "ˈboia", "jiboia": "ˈdʒiboia", "heroico": "ˈeroio", "paranoico": "ˈparaɳoio",
        "apoia": "ˈapoia", "poia": "ˈpoia", "saloia": "ˈsaɭoia"},
    "kea": {"boia": "ˈboia", "jiboia": "ʒiˈboia", "heroico": "eˈɾoio", "paranoico": "paɾaˈnoio",
        "apoia": "aˈpoia", "poia": "ˈpoia", "saloia": "saˈloia"},
    "mcm": {"boia": "ˈboia", "jiboia": "dʒiˈboia", "heroico": "eˈroio", "paranoico": "paraˈnoio",
        "apoia": "aˈpoia", "poia": "ˈpoia", "saloia": "saˈloia"},
    "mzs": {"boia": "boia", "jiboia": "ʒiboia", "heroico": "heroio", "paranoico": "paranoio",
        "apoia": "apoia", "poia": "poia", "saloia": "saloia"},
    "pap": {"boia": "boja", "jiboia": "iboja", "heroico": "herojo", "paranoico": "paranojo",
        "apoia": "apoja", "poia": "poja", "saloia": "saloja"},
    "pov": {"boia": "boia", "jiboia": "dʒiboia", "heroico": "eroio", "paranoico": "paranoio",
        "apoia": "apoia", "poia": "poia", "saloia": "saloia"},
    "pre": {"boia": "boia", "jiboia": "dʒiboia", "heroico": "heroio", "paranoico": "parãoio",
        "apoia": "apoia", "poia": "poia", "saloia": "saloia"},
    "vkp": {"boia": "boia", "jiboia": "dʒiboia", "heroico": "heɾoio", "paranoico": "paɾanoio",
        "apoia": "apoia", "poia": "poia", "saloia": "saloia"},
}


@pytest.fixture(scope="module")
def engines():
    return {}


def ipa(engines, lang, word):
    if lang not in engines:
        engines[lang] = G2P(lang)
    return unicodedata.normalize("NFC", engines[lang].transcribe_word(word))


def stressed_diphthong(transcription):
    """The two symbols after the primary stress mark that follow its onset."""
    tail = transcription[transcription.index("ˈ") + 1:]
    start = next(i for i, c in enumerate(tail) if c in "aɐeɛiɨoɔuə")
    return tail[start:start + 2]


@pytest.mark.parametrize("word,expected", sorted(OPEN.items()))
def test_pt_pt_oia_oico_have_the_open_diphthong(engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


@pytest.mark.parametrize("word,expected", sorted(DIPHTHONG_ONLY.items()))
def test_pt_pt_oia_oico_diphthong_of_words_with_other_differences(engines, word, expected):
    assert stressed_diphthong(ipa(engines, "pt-PT", word)) == stressed_diphthong(expected)


def test_pt_pt_poia_keeps_the_infopedia_reading(engines):
    assert ipa(engines, "pt-PT", "poia") == "ˈpojɐ"


@pytest.mark.parametrize("word", CLOSE)
def test_pt_pt_oia_words_without_a_pre_1990_acute_keep_the_close_diphthong(engines, word):
    assert stressed_diphthong(ipa(engines, "pt-PT", word)) == "oj"


@pytest.mark.parametrize("word", NEIGHBOURS)
def test_pt_pt_other_oi_words_keep_the_close_diphthong(engines, word):
    assert "ɔj" not in ipa(engines, "pt-PT", word).replace("ˈ", "").replace("ˌ", "")


@pytest.mark.parametrize("lang", EP_INHERITING)
@pytest.mark.parametrize("word", ["boia", "jiboia", "heroico", "paranoico"])
def test_ep_lects_inherit_the_open_diphthong(engines, lang, word):
    assert stressed_diphthong(ipa(engines, lang, word)) == "ɔj"


@pytest.mark.parametrize("lang", EP_INHERITING)
@pytest.mark.parametrize("word", ["saloia", "apoia", "comboio"])
def test_ep_lects_keep_the_close_diphthong_of_listed_and_other_words(engines, lang, word):
    assert stressed_diphthong(ipa(engines, lang, word)) == "oj"


@pytest.mark.parametrize("lang,word,expected", [
    (lang, word, out) for lang, row in sorted(PINNED.items())
    for word, out in sorted(row.items())
])
def test_lects_outside_the_rules_keep_their_output(engines, lang, word, expected):
    assert ipa(engines, lang, word) == expected
