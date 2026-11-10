"""European Portuguese ⟨-oide⟩: the stressed diphthong is the open [ɔj].

Expected values are the Infopédia (Dicionário da Língua Portuguesa, Porto
Editora) readings of the portuguese-unified lexicon, region pt-PT, written in
the spec's notation: Infopédia [ə] is [ɨ], its optional final (ə) is [ɨ], its
flap [r] is [ɾ] and its trill [ʀ] is [ʁ]. The rules and their sources are
``PT_SUFFIX_OIDE_OPEN`` and ``PT_LEX_OIDAR_CLOSE`` in ``pt-PT.json``.

São Miguel spells ⟨oi⟩ as its own monophthong [ø] in the grapheme table, so
the rule does not reach it there.

Terceira disables the rule, because its crescent diphthong after a labial
(foi [ˈfwoj], ovoide [ɔˈvwojdɨ]) owns the stressed vowel there. The African
and Asian varieties, Barranquenho and the creoles disable the rule, because
no source for their vowel in this ending was read. These lects pin the output
they had before the rule.
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
    "asteroide": "ɐʃtɨˈɾɔjdɨ", "alcaloide": "aɫkɐˈlɔjdɨ", "humanoide": "umɐˈnɔjdɨ",
    "cristaloide": "kɾiʃtɐˈlɔjdɨ", "tiroide": "tiˈɾɔjdɨ", "mastoide": "mɐʃˈtɔjdɨ",
    "sinusoide": "sinuˈzɔjdɨ", "celuloide": "sɨluˈlɔjdɨ", "planetoide": "plɐnɨˈtɔjdɨ",
    "metaloide": "mɨtɐˈlɔjdɨ", "xifoide": "ʃiˈfɔjdɨ", "blastoides": "blɐʃˈtɔjdɨʃ",
    "gadoides": "ɡɐˈdɔjdɨʃ",
}
# Infopédia words that also differ outside the diphthong: only the diphthong
# after the stress mark is compared.
DIPHTHONG_ONLY = {
    "androide": "ɐ̃ˈdɾɔjdɨ", "tabloide": "tɐˈblɔjdɨ", "lambdoide": "lɐ̃ˈbdɔjdɨ",
    "hominoides": "ɔmiˈnɔjdɨ", "cicloide": "siˈklɔjdɨ", "ovoide": "ɔˈvɔjdɨ",
}
# The present-subjunctive forms of adoidar and endoidar keep the close [oj] of
# doido (Cunha & Cintra, 7.ª ed., p. 431, obs. 3.ª a: pernoito "sempre com [o]").
OIDAR = ["adoide", "adoides", "adoidem", "endoide", "endoides", "endoidem"]
# Other ⟨oi⟩ words: the rule needs the ⟨d⟩ and a front vowel after a stressed
# ⟨oi⟩, so these keep the [oj] of the grapheme table.
NEIGHBOURS = ["boia", "joia", "heroico", "dezoito", "oito", "noite", "coice", "foice",
              "doido", "doida", "sinusoidal", "doideira"]

PINNED = {
    "pt-PT-x-terceira": {"asteroide": "ɐʃtɨˈɾojdɨ", "alcaloide": "aɫkɐˈlojdɨ", "androides": "ɐ̃ˈdɾojdɨʃ", "humanoide": "umɐˈnojdɨ", "ovoide": "ɔˈvwojdɨ", "foi": "ˈfwoj", "depois": "dɨˈpwojʃ"},
    "pt-PT-x-sao-miguel": {"asteroide": "ɐʃtɨˈɾødɨ", "androides": "ɐ̃ˈdɾødɨʃ", "endoide": "ẽˈdødɨ", "boia": "ˈbøɐ"},
    "pt-AO": {"asteroide": "asteˈɾojdɨ", "alcaloide": "aɫkaˈlojdɨ", "androides": "ɐ̃ˈdʁojdes", "humanoide": "umaˈnojdɨ"},
    "pt-CV": {"asteroide": "ɐsteˈrojde", "alcaloide": "ɐɫkɐˈlojde", "androides": "ɐ̃ˈdrojdes", "humanoide": "umɐˈnojde"},
    "pt-GW": {"asteroide": "ɐsteˈrojde", "alcaloide": "ɐɫkɐˈlojde", "androides": "ɐ̃ˈdrojdes", "humanoide": "umɐˈnojde"},
    "pt-MO": {"asteroide": "ɐʃtɨˈɾojdɨ", "alcaloide": "ɐɫkɐˈlojdɨ", "androides": "ɐ̃ˈdʁojdɨʃ", "humanoide": "umɐˈnojdɨ"},
    "pt-MZ": {"asteroide": "ɐsteˈɾojde", "alcaloide": "ɐɫkɐˈlojde", "androides": "ɐ̃ˈdrojdes", "humanoide": "umɐˈnojde"},
    "pt-ST": {"asteroide": "ɐsteˈrojde", "alcaloide": "ɐɫkɐˈlojde", "androides": "ɐ̃ˈdrojdes", "humanoide": "umɐˈnojde"},
    "pt-TL": {"asteroide": "asteˈɾojde", "alcaloide": "aɫkaˈlojde", "androides": "ɐ̃ˈdrojdes", "humanoide": "umaˈnojde"},
    "ext-PT-x-barranco": {"asteroide": "ɐhtɨˈɾojdɨ", "alcaloide": "ɐlkɐˈlojdɨ", "androides": "ɐ̃ˈdɾojdɨ", "humanoide": "humɐˈnojdɨ"},
    "aoa": {"asteroide": "aʃteroide", "alcaloide": "alaloide", "androides": "androideʃ", "humanoide": "humanoide"},
    "cri": {"asteroide": "aʃtɛɾɔidɛ", "alcaloide": "alalɔidɛ", "androides": "ãndɾɔidɛʃ", "humanoide": "umanɔidɛ"},
    "idb": {"asteroide": "asteˈroide", "alcaloide": "aɭaˈɭoide", "androides": "aɳdˈroides", "humanoide": "umaˈɳoide"},
    "kea": {"asteroide": "aʃteˈɾoide", "alcaloide": "alaˈloide", "androides": "ãˈdɾoideʃ", "humanoide": "umaˈnoide"},
    "mcm": {"asteroide": "asteˈroide", "alcaloide": "alaˈloide", "androides": "anˈdroides", "humanoide": "umaˈnoide"},
    "mzs": {"asteroide": "aʃteroide", "alcaloide": "alaloide", "androides": "androideʃ", "humanoide": "humanoide"},
    "pap": {"asteroide": "aʃterojde", "alcaloide": "alalojde", "androides": "androjdeʃ", "humanoide": "humanojde"},
    "pov": {"asteroide": "aʃteroide", "alcaloide": "alaloide", "androides": "androideʃ", "humanoide": "umanoide"},
    "pre": {"asteroide": "aʃteroide", "alcaloide": "alaloide", "androides": "ãdroideʃ", "humanoide": "humãoide"},
    "vkp": {"asteroide": "asteɾoide", "alcaloide": "alaloide", "androides": "andɾoides", "humanoide": "humanoide"},
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
def test_pt_pt_oide_has_the_open_diphthong(engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


@pytest.mark.parametrize("word,expected", sorted(DIPHTHONG_ONLY.items()))
def test_pt_pt_oide_diphthong_of_words_with_other_differences(engines, word, expected):
    assert stressed_diphthong(ipa(engines, "pt-PT", word)) == stressed_diphthong(expected)


@pytest.mark.parametrize("word", OIDAR)
def test_pt_pt_oidar_verb_forms_keep_the_close_diphthong(engines, word):
    assert stressed_diphthong(ipa(engines, "pt-PT", word)) == "oj"


@pytest.mark.parametrize("word", NEIGHBOURS)
def test_pt_pt_other_oi_words_keep_the_close_diphthong(engines, word):
    assert "ɔj" not in ipa(engines, "pt-PT", word)


@pytest.mark.parametrize("lang", EP_INHERITING)
@pytest.mark.parametrize("word", ["asteroide", "alcaloide", "androides", "humanoide"])
def test_ep_lects_inherit_the_open_diphthong(engines, lang, word):
    assert stressed_diphthong(ipa(engines, lang, word)) == "ɔj"


@pytest.mark.parametrize("lang", EP_INHERITING)
@pytest.mark.parametrize("word", ["endoide", "boia"])
def test_ep_lects_keep_the_close_diphthong_outside_the_ending(engines, lang, word):
    assert stressed_diphthong(ipa(engines, lang, word)) == "oj"


@pytest.mark.parametrize("lang,word,expected", [
    (lang, word, out) for lang, row in sorted(PINNED.items())
    for word, out in sorted(row.items())
])
def test_lects_outside_the_rule_keep_their_output(engines, lang, word, expected):
    assert ipa(engines, lang, word) == expected
