"""A tonic ⟨i u⟩ after a vowel, closed by the next consonant, is a hiatus.

Acordo Ortográfico 1990, Base X, 2.º: "As vogais tónicas/tônicas grafadas i e
u das palavras oxítonas e paroxítonas não levam acento agudo quando,
antecedidas de vogal com que não formam ditongo, constituem sílaba com a
consoante seguinte, como é o caso de nh, l, m, n, r e z: bainha, moinho,
rainha; adail, paul, Raul; Aboim, Coimbra, ruim; ainda, constituinte,
oriundo, ruins, triunfo; atrair, demiurgo, influir, influirmos; juiz, raiz,
etc."

So in each example word the ⟨i u⟩ is the stressed vowel of its own syllable,
and the vowel before it is the nucleus of the syllable before. The
transcription carries the stress mark between the two vowels, and the ⟨i u⟩
is a full vowel, not the glide [j w]. Vowel quality is each variety's own and
is not checked here.

Base X, 1.º excludes a following ⟨s⟩ ("excetuando o caso de s"), so a plural
in ⟨-ais⟩ keeps its diphthong. An ⟨i u⟩ followed by a consonant that opens the
next syllable stays a glide (muito, leite, saiba), and so does one before
⟨rr⟩, which spells one consonant (bairro).
"""
from __future__ import annotations

import re
import unicodedata

import pytest

from orthography2ipa import G2P, get_syllabifier

AO_BASE_X_2 = [
    "bainha", "moinho", "rainha",
    "adail", "paul", "Raul",
    "Aboim", "Coimbra", "ruim",
    "ainda", "constituinte", "oriundo", "ruins", "triunfo",
    "atrair", "demiurgo", "influir", "influirmos",
    "juiz", "raiz",
]

#: A vowel, the stress mark, then a full [i] or [u], oral or nasal, matched
#: on the decomposed transcription. The glide readings [j w j̃ w̃] do not
#: match, and neither does a mark placed on an earlier syllable.
_HIATUS_STRESS = re.compile("[aɐeɛəɨioɔuʊɪ]̃?ˈ[iu]")


def _hiatus_stressed(ipa: str) -> bool:
    return bool(_HIATUS_STRESS.search(unicodedata.normalize("NFD", ipa)))

LANGS = ["pt-PT", "pt-BR", "pt-PT-x-lisbon", "pt-BR-x-sp", "pt-AO", "pt-UY"]


@pytest.fixture
def without_syllabifier_plugin(monkeypatch):
    from orthography2ipa import registry
    monkeypatch.setattr(registry, "_syllabifiers", {})


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word", AO_BASE_X_2)
def test_closed_hiatus_vowel_is_stressed(lang, word):
    ipa = G2P(lang).transcribe_word(word)
    assert _hiatus_stressed(ipa), ipa


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", AO_BASE_X_2)
def test_closed_hiatus_without_the_plugin(lang, word,
                                          without_syllabifier_plugin):
    assert get_syllabifier(lang) is None
    ipa = G2P(lang).transcribe_word(word)
    assert _hiatus_stressed(ipa), ipa


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", AO_BASE_X_2)
def test_bundled_syllabifier_splits_the_hiatus(lang, word,
                                               without_syllabifier_plugin):
    # The ⟨i u⟩ after the vowel opens a syllable of its own: ra-i-nha, ra-ul.
    g2p = G2P(lang)
    sylls = g2p._syllables_cached(word.lower())
    vowel = next(k for k in range(1, len(word))
                 if word[k] in "iu" and word[k - 1].lower() in "aeiou")
    starts, at = set(), 0
    for syll in sylls:
        starts.add(at)
        at += len(syll)
    assert vowel in starts, sylls


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", AO_BASE_X_2)
def test_plugin_and_bundled_paths_agree(lang, word, monkeypatch):
    with_plugin = G2P(lang).transcribe_word(word)
    from orthography2ipa import registry
    monkeypatch.setattr(registry, "_syllabifiers", {})
    assert G2P(lang).transcribe_word(word) == with_plugin


#: Falling diphthongs the rule does not reach, with the stressed syllable
#: that holds the glide.
CONTROLS = [
    ("animais", r"ˈmaj"),   # ⟨i⟩ + ⟨s⟩: Base X, 1.º excepts s
    ("muito", r"ˈm[uũ]j"),  # ⟨t⟩ opens the next syllable
    ("leite", r"ˈlej"),
    ("pai", r"paj"),
    ("saiba", r"ˈsaj"),     # ⟨b⟩ opens the next syllable
    ("bairro", r"ˈbaj"),    # ⟨rr⟩ spells one consonant
    ("jaime", r"ˈʒaj"),     # ⟨m⟩ before a vowel opens the next syllable
    ("quinze", r"ˈk"),      # the ⟨u⟩ of ⟨qu⟩ is no vowel
]


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word,stressed", CONTROLS)
def test_diphthongs_outside_the_rule_keep_the_glide(lang, word, stressed):
    assert re.search(stressed, G2P(lang).transcribe_word(word))


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word,stressed", CONTROLS)
def test_controls_without_the_plugin(lang, word, stressed,
                                     without_syllabifier_plugin):
    assert re.search(stressed, G2P(lang).transcribe_word(word))


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", ["lourdes", "gourmet"])
def test_ou_is_outside_the_rule(lang, word, without_syllabifier_plugin):
    # Base X, 2.º gives no ⟨ou⟩ example, and the words of this shape are
    # loans and foreign names. The bundled path keeps ⟨ou⟩ one nucleus and
    # stresses it. The silabificador plugin divides lo-ur-des, which is why
    # this control runs without it.
    ipa = G2P(lang).transcribe_word(word)
    assert re.match(r"ˈ(l|ɡ)o", ipa), ipa


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
def test_unstressed_closed_vowel_is_left_as_it_was(lang):
    # Base X, 2.º speaks of tonic vowels only, and Base XIV, 1.º says the
    # spelling does not tell an atonic ⟨i u⟩ in hiatus from a diphthong
    # (arruinar, faiscar). An atonic ⟨i u⟩ therefore keeps the glide reading.
    ipa = G2P(lang).transcribe_word("ruindade")
    assert "uj̃" in ipa and "ˈda" in ipa, ipa


def test_ext_barrancos_and_galician_do_not_declare_the_rule():
    from orthography2ipa import get
    for code in ("gl-ES", "ext-PT-x-barrancos", "mwl", "pt-PT-x-medieval"):
        stress = get(code).stress
        assert stress is None or stress.closed_hiatus is None, code


def test_pt_specs_declare_the_rule():
    from orthography2ipa import get
    for code in ("pt-PT", "pt-BR", "pt-PT-x-lisbon", "pt-BR-x-sp", "pt-UY"):
        rule = get(code).stress.closed_hiatus
        assert rule.pairs == ("ai", "au", "ei", "eu", "iu", "oi", "ui")
        assert rule.onsets == ("nh",)
        assert rule.codas == ("l", "m", "n", "r", "z")
