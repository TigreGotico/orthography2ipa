"""European Portuguese stressed ⟨e⟩ and ⟨o⟩ in suffix endings.

Expected values are the Infopédia (Dicionário da Língua Portuguesa, Porto
Editora) readings of the portuguese-unified lexicon, region pt-PT, written
in the spec's notation: Infopédia [ə] is [ɨ], its flap [r] is [ɾ] and its
trill [ʀ] is [ʁ]. The rules and their sources are ``PT_SUFFIX_*_CLOSE``,
``PT_LEX_OPEN_E_SUFFIX`` and ``PT_LEX_OPEN_O_SUFFIX`` in ``pt-PT.json``.

The pre-lexical default for an unmarked stressed ⟨e⟩ or ⟨o⟩ stays open, so
words outside the suffix classes keep [ɛ] and [ɔ].

Porto, Braga and Terceira own their stressed mid vowels (diphthongisation
and the Terceira crescent diphthong), and no source for the African and
Asian varieties, Barranquenho or the creoles was read, so those lects pin the
output they had before the rules.
"""
import unicodedata

import pytest

from orthography2ipa import G2P

EP_INHERITING = [
    "pt-PT", "pt-PT-x-lisbon", "pt-PT-x-coimbra", "pt-PT-x-acores",
    "pt-PT-x-madeira", "pt-PT-x-alentejo", "pt-PT-x-beira", "pt-PT-x-aveiro",
    "pt-PT-x-sao-miguel", "pt-PT-x-algarve", "pt-PT-x-alfena",
    "pt-PT-x-minho", "pt-PT-x-trasosmontes", "pt-PT-x-viana",
]

# Infopédia readings, spec notation.
CLOSE = {
    "rapidez": "ʁɐpiˈdeʃ",
    "beleza": "bɨˈlezɐ", "certeza": "sɨɾˈtezɐ", "mesa": "ˈmezɐ",
    "tema": "ˈtemɐ", "sistema": "siʃˈtemɐ", "fonema": "fuˈnemɐ",
    "dantesco": "dɐ̃ˈteʃku", "pitoresco": "pituˈɾeʃku", "fresca": "ˈfɾeʃkɐ",
    "trabalhador": "tɾɐbɐʎɐˈdoɾ", "professor": "pɾufɨˈsoɾ", "amor": "ɐˈmoɾ",
    "senhor": "sɨˈɲoɾ", "flor": "ˈfloɾ", "dor": "ˈdoɾ",
    "famoso": "fɐˈmozu", "brioso": "bɾiˈozu",
    "risonho": "ʁiˈzoɲu", "medonho": "mɨˈdoɲu",
}
# Infopédia open readings inside the suffix classes: the exception lists.
OPEN_EXCEPTIONS = {
    "melhor": "mɨˈʎɔɾ", "menor": "mɨˈnɔɾ",
    "pormenor": "puɾmɨˈnɔɾ", "suor": "suˈɔɾ", "redor": "ʁɨˈdɔɾ",
    "reza": "ˈʁɛzɐ", "fresa": "ˈfɾɛzɐ", "pesca": "ˈpɛʃkɐ", "dez": "ˈdɛʃ",
}
# Infopédia readings where the engine differs elsewhere in the word (the
# pretonic ⟨al⟩ of altivez, the glide of ⟨ai⟩ ⟨io⟩); only the stressed
# vowel is compared.
VOWEL_ONLY = {"altivez": "aɫtiˈveʃ", "maior": "mɐjˈɔɾ", "pior": "ˈpjɔɾ"}
# Infopédia open readings next to the suffix classes; no rule may reach them.
OPEN_NEIGHBOURS = {
    "janela": "ʒɐˈnɛlɐ", "papel": "pɐˈpɛɫ", "moda": "ˈmɔdɐ", "roda": "ˈʁɔdɐ",
    "porta": "ˈpɔɾtɐ", "sol": "ˈsɔɫ", "formosa": "fuɾˈmɔzɐ",
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
def test_pt_pt_suffix_class_has_close_stressed_vowel(engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


@pytest.mark.parametrize("word,expected", sorted(OPEN_EXCEPTIONS.items()))
def test_pt_pt_listed_exceptions_keep_open_vowel(engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


@pytest.mark.parametrize("word,expected", sorted(VOWEL_ONLY.items()))
def test_pt_pt_stressed_vowel_of_words_with_other_differences(
        engines, word, expected):
    assert stressed_vowel(ipa(engines, "pt-PT", word)) == stressed_vowel(expected)


@pytest.mark.parametrize("word,expected", sorted(OPEN_NEIGHBOURS.items()))
def test_pt_pt_open_neighbours_do_not_move(engines, word, expected):
    assert ipa(engines, "pt-PT", word) == expected


@pytest.mark.parametrize("word", ["pesa", "preza", "despreza", "pesco", "rema", "crema"])
def test_pt_pt_verb_forms_in_the_suffix_endings_keep_open_vowel(engines, word):
    # Ciberdúvidas 7872: the verb form of a homograph has the open vowel.
    # WikiPron pt-PT: rema 'ʁ ɛ m ɐ', crema 'k ɾ ɛ m ɐ'.
    assert stressed_vowel(ipa(engines, "pt-PT", word)) == "ɛ"


# WikiPron pt-PT readings of -enar and -onar verb forms. They are open, so no
# rule closes the stressed vowel of -eno, -ena or -ona.
VERB_FORMS_OPEN = {
    "ordena": "ɛ", "ordeno": "ɛ", "condena": "ɛ", "acena": "ɛ", "envenena": "ɛ",
    "funciona": "ɔ", "menciona": "ɔ", "telefona": "ɔ", "abandona": "ɔ", "questiona": "ɔ",
}


@pytest.mark.parametrize("word,expected", sorted(VERB_FORMS_OPEN.items()))
def test_pt_pt_enar_and_onar_verb_forms_keep_open_vowel(engines, word, expected):
    assert stressed_vowel(ipa(engines, "pt-PT", word)) == expected


@pytest.mark.parametrize("word", ["famosa", "famosos", "gostosas"])
def test_oso_feminine_and_plural_keep_the_open_vowel(engines, word):
    # The feminine and the plural of -oso open the vowel by metaphony
    # (Cunha & Cintra p. 266: brioso briosa, formoso formosa).
    assert stressed_vowel(ipa(engines, "pt-PT", word)) == "ɔ"


@pytest.mark.parametrize("lang", EP_INHERITING)
@pytest.mark.parametrize("word", sorted(CLOSE) + ["altivez"])
def test_ep_lects_inherit_the_close_vowel(engines, lang, word):
    expected = stressed_vowel({**CLOSE, **VOWEL_ONLY}[word])
    assert stressed_vowel(ipa(engines, lang, word)) == expected


@pytest.mark.parametrize("lang", EP_INHERITING)
@pytest.mark.parametrize("word", sorted(OPEN_EXCEPTIONS) + ["maior", "pior"])
def test_ep_lects_inherit_the_open_exceptions(engines, lang, word):
    expected = stressed_vowel({**OPEN_EXCEPTIONS, **VOWEL_ONLY}[word])
    assert stressed_vowel(ipa(engines, lang, word)) == expected


# Output before the rules; these lects disable them.
PINNED = {
    "pt-PT-x-porto": {"rapidez": "ʁɐpiˈdjɛʃ", "beleza": "bɨˈljɛzɐ", "mesa": "ˈmjɛzɐ", "tema": "ˈtjɛmɐ", "chileno": "ʃiˈljɛnu", "pena": "ˈpjɛnɐ", "dantesco": "dɐ̃ˈtjɛʃku", "trabalhador": "tɾɐbɐʎɐˈdwɔɾ", "amor": "ɐˈmwɔɾ", "senhor": "sɨˈɲwɔɾ", "famoso": "fɐˈmwɔzu", "zona": "ˈzwɔnɐ", "risonho": "ʁiˈzwɔɲu", "melhor": "mɨˈʎwɔɾ", "pior": "piˈwɔɾ", "reza": "ˈʁjɛzɐ"},
    "pt-PT-x-braga": {"rapidez": "ʁɐpiˈdjɛʃ", "beleza": "bɨˈljɛzɐ", "mesa": "ˈmjɛzɐ", "tema": "ˈtjɛmɐ", "chileno": "ʃiˈljɛnu", "pena": "ˈpjɛnɐ", "dantesco": "dɐ̃ˈtjɛʃku", "trabalhador": "tɾɐbɐʎɐˈdwɔɾ", "amor": "ɐˈmwɔɾ", "senhor": "sɨˈɲwɔɾ", "famoso": "fɐˈmwɔzu", "zona": "ˈzwɔnɐ", "risonho": "ʁiˈzwɔɲu", "melhor": "mɨˈʎwɔɾ", "pior": "piˈwɔɾ", "reza": "ˈʁjɛzɐ"},
    "pt-PT-x-terceira": {"rapidez": "ʁɐpiˈdɛʃ", "beleza": "bɨˈlɛzɐ", "mesa": "ˈmɛzɐ", "tema": "ˈtɛmɐ", "chileno": "ʃiˈlɛnu", "pena": "ˈpɛnɐ", "dantesco": "dɐ̃ˈtɛʃku", "trabalhador": "tɾɐbɐʎɐˈdɔɾ", "amor": "ɐˈmwɔɾ", "senhor": "sɨˈɲɔɾ", "famoso": "fɐˈmwɔzu", "zona": "ˈzɔnɐ", "risonho": "ʁiˈzɔɲu", "melhor": "mɨˈʎɔɾ", "pior": "piˈɔɾ", "reza": "ˈʁɛzɐ"},
    "pt-AO": {"rapidez": "ɾapiˈdɛz", "beleza": "beˈlɛza", "mesa": "ˈmɛza", "tema": "ˈtɛma", "chileno": "ʃiˈlɛnʊ", "pena": "ˈpɛna", "dantesco": "dɐ̃ˈtɛskʊ", "trabalhador": "tʁabaʎaˈdɔɾ", "amor": "aˈmɔɾ", "senhor": "seˈɲɔɾ", "famoso": "faˈmozʊ", "zona": "ˈzɔna", "risonho": "ɾiˈzɔɲʊ", "melhor": "meˈʎɔɾ", "pior": "piˈɔɾ", "reza": "ˈɾɛza"},
    "pt-CV": {"rapidez": "rɐpiˈdes", "beleza": "beˈlezɐ", "mesa": "ˈmezɐ", "tema": "ˈtemɐ", "chileno": "ʃiˈlenu", "pena": "ˈpenɐ", "dantesco": "dɐ̃ˈtesku", "trabalhador": "trɐbɐʎɐˈdɔr", "amor": "ɐˈmɔr", "senhor": "seˈɲɔr", "famoso": "fɐˈmozu", "zona": "ˈzɔnɐ", "risonho": "riˈzɔɲu", "melhor": "meˈʎɔr", "pior": "piˈɔr", "reza": "ˈrezɐ"},
    "pt-GW": {"rapidez": "ʁɐpiˈdɛs", "beleza": "beˈlɛzɐ", "mesa": "ˈmɛsɐ", "tema": "ˈtɛmɐ", "chileno": "ʃiˈlɛnu", "pena": "ˈpɛnɐ", "dantesco": "dɐ̃ˈtɛsku", "trabalhador": "trɐbɐʎɐˈdɔr", "amor": "ɐˈmɔr", "senhor": "seˈɲɔr", "famoso": "fɐˈmosu", "zona": "ˈzɔnɐ", "risonho": "ʁiˈsɔɲu", "melhor": "meˈʎɔr", "pior": "piˈɔr", "reza": "ˈʁɛzɐ"},
    "pt-MO": {"rapidez": "ʁɐpiˈdɛʃ", "beleza": "bɨˈlɛzɐ", "mesa": "ˈmɛzɐ", "tema": "ˈtɛmɐ", "chileno": "ʃiˈlɛnu", "pena": "ˈpɛnɐ", "dantesco": "dɐ̃ˈtɛʃku", "trabalhador": "tʁɐbɐʎɐˈdɔʁ", "amor": "ɐˈmɔʁ", "senhor": "sɨˈɲɔʁ", "famoso": "fɐˈmozu", "zona": "ˈzɔnɐ", "risonho": "ʁiˈzɔɲu", "melhor": "mɨˈʎɔʁ", "pior": "piˈɔʁ", "reza": "ˈʁɛzɐ"},
    "pt-MZ": {"rapidez": "rɐpiˈdɛz", "beleza": "beˈlɛzɐ", "mesa": "ˈmɛzɐ", "tema": "ˈtɛmɐ", "chileno": "ʃiˈlɛnu", "pena": "ˈpɛnɐ", "dantesco": "dɐ̃ˈtɛsku", "trabalhador": "trɐbɐʎɐˈdɔɾ", "amor": "ɐˈmɔɾ", "senhor": "seˈɲɔɾ", "famoso": "fɐˈmozu", "zona": "ˈzɔnɐ", "risonho": "riˈzɔɲu", "melhor": "meˈʎɔɾ", "pior": "piˈɔɾ", "reza": "ˈrɛzɐ"},
    "pt-ST": {"rapidez": "ʁɐpiˈdɛs", "beleza": "beˈlɛzɐ", "mesa": "ˈmɛsɐ", "tema": "ˈtɛmɐ", "chileno": "ʃiˈlɛnu", "pena": "ˈpɛnɐ", "dantesco": "dɐ̃ˈtɛsku", "trabalhador": "trɐbɐʎɐˈdɔr", "amor": "ɐˈmɔr", "senhor": "seˈɲɔr", "famoso": "fɐˈmosu", "zona": "ˈzɔnɐ", "risonho": "ʁiˈsɔɲu", "melhor": "meˈʎɔr", "pior": "piˈɔr", "reza": "ˈʁɛzɐ"},
    "pt-TL": {"rapidez": "rapiˈdɛz", "beleza": "beˈlɛza", "mesa": "ˈmɛza", "tema": "ˈtɛma", "chileno": "ʃiˈlɛno", "pena": "ˈpɛna", "dantesco": "dɐ̃ˈtɛsko", "trabalhador": "trabalaˈdɔɾ", "amor": "aˈmɔɾ", "senhor": "seˈnɔɾ", "famoso": "faˈmozo", "zona": "ˈzɔna", "risonho": "riˈzɔno", "melhor": "meˈlɔɾ", "pior": "piˈɔɾ", "reza": "ˈrɛza"},
    "ext-PT-x-barrancos": {"rapidez": "rɐpiˈdɛʃ", "beleza": "bɨˈlɛzɐ", "mesa": "ˈmɛzɐ", "tema": "ˈtemɐ", "chileno": "ʃiˈlenu", "pena": "ˈpenɐ", "dantesco": "dɐ̃ˈtɛhku", "trabalhador": "tɾɐbɐˈʎadu", "amor": "ˈɐmu", "senhor": "ˈsɛɲu", "famoso": "fɐˈmozu", "zona": "ˈzɔnɐ", "risonho": "riˈzɔɲu", "melhor": "ˈmɛʎu", "pior": "ˈpiɔ", "reza": "ˈrɛzɐ"},
    "kea": {"rapidez": "ʀaˈpideʒ", "beleza": "beˈleza", "mesa": "ˈmesa", "tema": "ˈtema", "chileno": "iˈleno", "pena": "ˈpena", "dantesco": "dãˈteso", "trabalhador": "tɾabaˈʎadoɾ", "amor": "ˈamoɾ", "senhor": "ˈseɲoɾ", "famoso": "faˈmoso", "zona": "ˈzona", "risonho": "ʀiˈsoɲo", "melhor": "ˈmeʎoɾ", "pior": "ˈpioɾ", "reza": "ˈʀeza"},
    "pap": {"rapidez": "rapideʒ", "beleza": "beleza", "mesa": "mesa", "tema": "tema", "chileno": "tʃileno", "pena": "pena", "dantesco": "danteso", "trabalhador": "trabaɫhador", "amor": "amor", "senhor": "senhor", "famoso": "famoso", "zona": "zona", "risonho": "risonho", "melhor": "meɫhor", "pior": "pior", "reza": "reza"},
    "cri": {"rapidez": "ɾapidɛz", "beleza": "bɛlɛza", "mesa": "mɛsa", "tema": "tɛma", "chileno": "ilɛnɔ", "pena": "pɛna", "dantesco": "dãtɛsɔ", "trabalhador": "tɾabaʎadɔɾ", "amor": "amɔɾ", "senhor": "sɛɲɔɾ", "famoso": "famɔsɔ", "zona": "zɔna", "risonho": "ɾisɔɲɔ", "melhor": "mɛʎɔɾ", "pior": "piɔɾ", "reza": "ɾɛza"},
    "aoa": {"rapidez": "rapideʒ", "beleza": "beleza", "mesa": "mesa", "tema": "tema", "chileno": "hileno", "pena": "pena", "dantesco": "danteso", "trabalhador": "trabaɫhador", "amor": "amor", "senhor": "seɲor", "famoso": "famoso", "zona": "zona", "risonho": "risoɲo", "melhor": "meɫhor", "pior": "pior", "reza": "reza"},
    "mzs": {"rapidez": "rapideʒ", "beleza": "beleza", "mesa": "mesa", "tema": "tema", "chileno": "tʃileno", "pena": "pena", "dantesco": "danteso", "trabalhador": "trabaʎador", "amor": "amor", "senhor": "seɲor", "famoso": "famoso", "zona": "zona", "risonho": "risoɲo", "melhor": "meʎor", "pior": "pior", "reza": "reza"},
    "pov": {"rapidez": "rapideʒ", "beleza": "beleza", "mesa": "mesa", "tema": "tema", "chileno": "ileno", "pena": "pena", "dantesco": "danteso", "trabalhador": "trabalador", "amor": "amor", "senhor": "seɲor", "famoso": "famoso", "zona": "zona", "risonho": "risoɲo", "melhor": "melor", "pior": "pior", "reza": "reza"},
    "pre": {"rapidez": "rapideʒ", "beleza": "beleza", "mesa": "mesa", "tema": "tema", "chileno": "hileno", "pena": "pena", "dantesco": "dãteso", "trabalhador": "trabaɫhador", "amor": "amor", "senhor": "seɲor", "famoso": "famoso", "zona": "zona", "risonho": "risoɲo", "melhor": "meɫhor", "pior": "pior", "reza": "reza"},
    "vkp": {"rapidez": "ɾapidez", "beleza": "beleza", "mesa": "mesa", "tema": "tema", "chileno": "tʃileno", "pena": "pena", "dantesco": "danteso", "trabalhador": "tɾabalhadoɾ", "amor": "amoɾ", "senhor": "senhoɾ", "famoso": "famoso", "zona": "zona", "risonho": "ɾisonho", "melhor": "melhoɾ", "pior": "pioɾ", "reza": "ɾeza"},
    "idb": {"rapidez": "ˈrapidez", "beleza": "ˈbeleza", "mesa": "ˈmesa", "tema": "ˈtema", "chileno": "ˈtʃileno", "pena": "ˈpena", "dantesco": "ˈdaɳteso", "trabalhador": "ˈtrabaɭador", "amor": "ˈamor", "senhor": "ˈseɲor", "famoso": "ˈfamoso", "zona": "ˈzoɳa", "risonho": "ˈrisoɲo", "melhor": "ˈmelor", "pior": "ˈpior", "reza": "ˈreza"},
    "mcm": {"rapidez": "raˈpidez", "beleza": "beˈleza", "mesa": "ˈmesa", "tema": "ˈtema", "chileno": "tʃiˈleno", "pena": "ˈpena", "dantesco": "danˈteso", "trabalhador": "trabaˈlador", "amor": "ˈamor", "senhor": "ˈsenor", "famoso": "faˈmoso", "zona": "ˈzona", "risonho": "riˈsono", "melhor": "ˈmelor", "pior": "ˈpior", "reza": "ˈreza"},
}


@pytest.mark.parametrize("lang,word,expected", [
    (lang, word, out) for lang, row in sorted(PINNED.items())
    for word, out in sorted(row.items())
])
def test_lects_that_disable_the_rules_keep_their_output(
        engines, lang, word, expected):
    assert ipa(engines, lang, word) == expected
