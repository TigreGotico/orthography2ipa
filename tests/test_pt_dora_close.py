"""European Portuguese ⟨-dora -tora -sora⟩: the stressed vowel is close [o].

Expected values are the Infopédia (Dicionário da Língua Portuguesa, Porto
Editora) readings of the portuguese-unified lexicon, region pt-PT, written in
the spec's notation: Infopédia [ə] is [ɨ], its flap [r] is [ɾ] and its trill
[ʀ] is [ʁ]. The rules and their sources are ``PT_SUFFIX_DORA_CLOSE``,
``PT_SUFFIX_DORA_CANDIDATE_OPEN`` and ``PT_LEX_OPEN_O_SUFFIX`` in
``pt-PT.json``.

Porto, Braga and Terceira own their stressed mid vowels, and no source for the
African and Asian varieties, Barranquenho or the creoles was read, so those
lects pin the output they had before the rule.
"""
import unicodedata

import pytest

from orthography2ipa import G2P

EP_INHERITING = [
    "pt-PT", "pt-PT-x-lisbon", "pt-PT-x-coimbra", "pt-PT-x-acores",
    "pt-PT-x-madeira", "pt-PT-x-alentejo", "pt-PT-x-beira", "pt-PT-x-aveiro",
    "pt-PT-x-sao-miguel", "pt-PT-x-algarve", "pt-PT-x-alfena",
    "pt-PT-x-minho", "pt-PT-x-tras-os-montes", "pt-PT-x-viana",
]

# Infopédia readings, spec notation.
CLOSE = {
    "calculadora": "kaɫkulɐˈdoɾɐ", "depiladora": "dɨpilɐˈdoɾɐ", "embaixadora": "ẽbajʃɐˈdoɾɐ",
    "metralhadora": "mɨtɾɐʎɐˈdoɾɐ", "lavadora": "lɐvɐˈdoɾɐ", "incubadora": "ĩkubɐˈdoɾɐ",
    "editora": "idiˈtoɾɐ", "pastora": "pɐʃˈtoɾɐ", "construtora": "kõʃtɾuˈtoɾɐ",
    "adutora": "ɐduˈtoɾɐ", "impressora": "ĩpɾɨˈsoɾɐ", "emissora": "imiˈsoɾɐ",
}
# Infopédia words that also differ outside the stressed vowel.
VOWEL_ONLY = {
    "aceleradora": "ɐsɨlɨɾɐˈdoɾɐ", "copiadora": "kupjɐˈdoɾɐ", "distribuidora": "dɨʃtɾibwiˈdoɾɐ",
    "operadora": "ɔpɨɾɐˈdoɾɐ", "automotora": "awtɔmuˈtoɾɐ",
}
# Infopédia [ɔ] in the ending: not agent nouns, and the rhizotonic forms of
# adorar (lograr model, Cunha & Cintra pp. 430-431), and desoras (des- and
# horas). PT_LEX_OPEN_O_SUFFIX.
OPEN_EXCEPTIONS = {
    "fedora": "fɨˈdɔɾɐ", "pandora": "pɐ̃ˈdɔɾɐ", "bandora": "bɐ̃ˈdɔɾɐ", "mandora": "mɐ̃ˈdɔɾɐ",
    "pletora": "plɨˈtɔɾɐ", "pitora": "piˈtɔɾɐ", "atora": "ɐˈtɔɾɐ", "nessora": "nɨˈsɔɾɐ",
    "adora": "ɐˈdɔɾɐ", "adoras": "ɐˈdɔɾɐʃ", "adoram": "ɐˈdɔɾɐ̃w̃", "desoras": "dɨˈzɔɾɐʃ",
}
# Neighbours the rule must not reach: the monosyllabic stems, another consonant
# before the ⟨o⟩, another consonant after it, or another vowel after the ⟨r⟩
# (adoro, adore: the lograr model, Cunha & Cintra pp. 430-431).
OPEN_NEIGHBOURS = ["tora", "sora", "dora", "senhora", "agora", "embora", "aurora", "devora",
                   "explora", "demora", "idosa", "pistola", "histórico", "vitória", "adoro", "adore"]

PINNED = {
    "pt-PT-x-porto": {"calculadora": "kaɫkulɐˈdwɔɾɐ", "professora": "pɾufɨˈs̺wɔɾɐ", "autoras": "awˈtwɔɾɐʃ", "vendedora": "bẽdɨˈdwɔɾɐ"},
    "pt-PT-x-braga": {"calculadora": "kaɫkulɐˈdwɔɾɐ", "professora": "pɾufɨˈs̺wɔɾɐ", "autoras": "awˈtwɔɾɐʃ", "vendedora": "bɨ̃dɨˈdwɔɾɐ"},
    "pt-PT-x-terceira": {"calculadora": "kaɫkulɐˈdɔɾɐ", "professora": "pɾufɨˈsɔɾɐ", "autoras": "awˈtɔɾɐʃ", "vendedora": "vẽdɨˈdɔɾɐ"},
    "pt-AO": {"calculadora": "kaɫkulaˈdɔɾa", "professora": "pʁofeˈsɔɾa", "autoras": "awˈtɔɾas", "vendedora": "vẽdeˈdɔɾa"},
    "pt-CV": {"calculadora": "kɐɫkulɐˈdɔrɐ", "professora": "prufeˈsɔrɐ", "autoras": "awˈtɔrɐs", "vendedora": "vẽdeˈdɔrɐ"},
    "pt-GW": {"calculadora": "kɐɫkulɐˈdɔrɐ", "professora": "profeˈsɔrɐ", "autoras": "awˈtɔrɐs", "vendedora": "vẽdeˈdɔrɐ"},
    "pt-MO": {"calculadora": "kɐɫkulɐˈdɔɾɐ", "professora": "pʁufɨˈsɔɾɐ", "autoras": "awˈtɔɾɐʃ", "vendedora": "vẽdɨˈdɔɾɐ"},
    "pt-MZ": {"calculadora": "kɐɫkulɐˈdɔɾɐ", "professora": "profeˈsɔɾɐ", "autoras": "awˈtɔɾɐs", "vendedora": "vẽdeˈdɔɾɐ"},
    "pt-ST": {"calculadora": "kɐɫkulɐˈdɔrɐ", "professora": "profeˈsɔrɐ", "autoras": "awˈtɔrɐs", "vendedora": "vẽdeˈdɔrɐ"},
    "pt-TL": {"calculadora": "kaɫkulaˈdɔɾa", "professora": "profeˈsɔɾa", "autoras": "awˈtɔɾas", "vendedora": "vẽdeˈdɔɾa"},
    "ext-PT-x-barranco": {"calculadora": "kɐlkulɐˈdɔɾɐ", "professora": "pɾufɨˈsɔɾɐ", "autoras": "awˈtɔɾɐ", "vendedora": "bɨ̃dɨˈdɔɾɐ"},
    "aoa": {"calculadora": "aluladora", "professora": "professora", "autoras": "autoraʃ", "vendedora": "vendedora"},
    "cri": {"calculadora": "aluladɔɾa", "professora": "pɾɔfɛssɔɾa", "autoras": "autɔɾaʃ", "vendedora": "vɛndɛdɔɾa"},
    "idb": {"calculadora": "ˈaɭuladora", "professora": "ˈprofessora", "autoras": "ˈautoras", "vendedora": "ˈʋendedora"},
    "kea": {"calculadora": "alulaˈdoɾa", "professora": "pɾofesˈsoɾa", "autoras": "auˈtoɾaʃ", "vendedora": "vẽdeˈdoɾa"},
    "mcm": {"calculadora": "alulaˈdora", "professora": "profesˈsora", "autoras": "auˈtoras", "vendedora": "vendeˈdora"},
    "mzs": {"calculadora": "aluladora", "professora": "professora", "autoras": "awtoraʃ", "vendedora": "vendedora"},
    "pap": {"calculadora": "aluladora", "professora": "professora", "autoras": "awtoraʃ", "vendedora": "vendedora"},
    "pov": {"calculadora": "aluladora", "professora": "professora", "autoras": "autoraʃ", "vendedora": "vendedora"},
    "pre": {"calculadora": "aluladora", "professora": "professora", "autoras": "autoraʃ", "vendedora": "vendedora"},
    "vkp": {"calculadora": "aluladoɾa", "professora": "pɾofessoɾa", "autoras": "autoɾas", "vendedora": "ʋendedoɾa"},
}


@pytest.fixture(scope="module")
def engines():
    return {}


def ipa(engines, lang, word):
    if lang not in engines:
        engines[lang] = G2P(lang)
    return unicodedata.normalize("NFC", engines[lang].transcribe_word(word))


def stressed_vowel(transcription):
    """The first vowel symbol after the primary stress mark."""
    tail = transcription[transcription.index("ˈ") + 1:]
    return next(c for c in tail if c in "aɐeɛiɨoɔuə")


@pytest.mark.parametrize("word,expected", sorted(CLOSE.items()))
def test_pt_pt_dora_has_the_close_vowel(engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


@pytest.mark.parametrize("word,expected", sorted(VOWEL_ONLY.items()))
def test_pt_pt_dora_vowel_of_words_with_other_differences(engines, word, expected):
    assert stressed_vowel(ipa(engines, "pt-PT", word)) == stressed_vowel(expected)


@pytest.mark.parametrize("word,expected", sorted(OPEN_EXCEPTIONS.items()))
def test_pt_pt_listed_open_words_keep_the_open_vowel(engines, word, expected):
    assert stressed_vowel(ipa(engines, "pt-PT", word)) == stressed_vowel(expected)


@pytest.mark.parametrize("word", OPEN_NEIGHBOURS)
def test_pt_pt_open_neighbours_do_not_move(engines, word):
    assert stressed_vowel(ipa(engines, "pt-PT", word)) == "ɔ"


@pytest.mark.parametrize("word", ["calculadora", "professora", "trabalhadoras"])
def test_pt_pt_open_vowel_stays_a_lattice_candidate(engines, word):
    if "pt-PT" not in engines:
        engines["pt-PT"] = G2P("pt-PT")
    cands = [unicodedata.normalize("NFC", c) for c in engines["pt-PT"].word_candidates(word, k=20)]
    assert stressed_vowel(cands[0]) == "o"
    assert any(stressed_vowel(c) == "ɔ" for c in cands)


@pytest.mark.parametrize("lang", EP_INHERITING)
@pytest.mark.parametrize("word", ["calculadora", "professora", "autoras", "vendedora"])
def test_ep_lects_inherit_the_close_vowel(engines, lang, word):
    assert stressed_vowel(ipa(engines, lang, word)) == "o"


@pytest.mark.parametrize("lang,word,expected", [
    (lang, word, out) for lang, row in sorted(PINNED.items())
    for word, out in sorted(row.items())
])
def test_lects_that_disable_the_rule_keep_their_output(engines, lang, word, expected):
    assert ipa(engines, lang, word) == expected
