"""A stressed ⟨i u⟩ after a diphthong is a syllable of its own.

Acordo Ortográfico 1990, Base X, 4.º: "Prescinde-se do acento agudo nas
vogais tónicas/tônicas grafadas i e u das palavras paroxítonas, quando elas
estão precedidas de ditongo: baiuca, boiuno, cauila (var. cauira), cheiinho
(de cheio), saiinha (de saia)."

Base X, 5.º: "Levam, porém, acento agudo as vogais tónicas/tônicas grafadas i
e u quando, precedidas de ditongo, pertencem a palavras oxítonas e estão em
posição final ou seguidas de s: Piauí, teiú, teiús, tuiuiú, tuiuiús. Obs.: Se,
neste caso, a consoante final for diferente de s, tais vogais dispensam o
acento agudo: cauim."

So baiuca is bai-u-ca: the diphthong keeps its glide, and the stressed vowel
starts the next syllable. Infopédia divides and transcribes it so: bai.u.ca
[bɐjˈukɐ].
"""
from __future__ import annotations

import dataclasses

import pytest

from orthography2ipa import G2P, get

#: European Portuguese, letter for letter: the Infopédia rows.
PT_PT = [
    ("boiuno", "bojˈunu"),        # boi.u.no, Base X, 4.º
    ("maiúscula", "majˈuʃkulɐ"),  # mai.ús.cu.la
]

#: Infopédia writes ⟨ei⟩ as the Lisbon [ɐj], and its ⟨r⟩ is [ɾ] here. pt-PT
#: keeps [ej], and pt-PT-x-lisbon gives [ɐj], so these words are read with the
#: Lisbon spec.
PT_PT_LISBON = [
    ("teiú", "tɐjˈu"),            # tei.ú, Base X, 5.º
    ("feiura", "fɐjˈuɾɐ"),        # fei.u.ra
]

#: The Base X, 4.º and 5.º examples, and the words above. Their test reads only
#: the division that the clauses state: the mark follows the glide. The rows
#: above leave out the others. Infopédia has no row for cauila, cheiinho,
#: saiinha, Piauí or teiús. It writes baiuca [bɐjˈukɐ], with [ɐj] where this
#: library has [aj]. It writes tuiuiú [tujuˈju] and cauim [kɐˈwĩ], with the mark
#: before the glide, although it divides them tui.ui.ú and cau.im.
IN_CONTEXT = ["baiuca", "boiuno", "cauila", "cheiinho", "saiinha", "Piauí",
              "teiú", "teiús", "tuiuiú", "cauim", "maiúscula", "feiura"]

#: The ⟨i u⟩ after the diphthong is unstressed, so the clauses do not reach
#: it. Infopédia: a.bai.u.ca.do [ɐbajuˈkadu], a.bai.u.car [ɐbajuˈkar].
CONTROLS = [
    ("abaiucado", "ɐbajuˈkadu"),
    ("abaiucar", "ɐbajuˈkaɾ"),
]

LANGS = ["pt-PT", "pt-BR", "pt-PT-x-lisbon", "pt-BR-x-sp", "pt-AO"]


def _mark_after_glide(ipa: str) -> bool:
    head, _, tail = ipa.partition("ˈ")
    return head[-1:] in ("j", "w") and tail[:1] not in ("", "j", "w")


@pytest.mark.parametrize("word,expected", PT_PT)
def test_pt_pt_transcription(word, expected):
    assert G2P("pt-PT").transcribe_word(word) == expected


@pytest.mark.parametrize("word,expected", PT_PT_LISBON)
def test_pt_pt_lisbon_transcription(word, expected):
    assert G2P("pt-PT-x-lisbon").transcribe_word(word) == expected


def test_tuiuiu_keeps_the_segments_of_infopedia():
    assert G2P("pt-PT").transcribe_word("tuiuiú").replace("ˈ", "") == "tujuju"


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word", IN_CONTEXT)
def test_mark_follows_the_glide_of_the_diphthong(lang, word):
    ipa = G2P(lang).transcribe_word(word)
    assert _mark_after_glide(ipa), ipa


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", IN_CONTEXT)
def test_plugin_and_bundled_paths_agree(lang, word, plugin_engine):
    ipa = plugin_engine(lang).transcribe_word(word)
    assert _mark_after_glide(ipa), ipa
    assert ipa == G2P(lang).transcribe_word(word)


@pytest.mark.parametrize("word,expected", CONTROLS)
def test_unstressed_vowel_after_a_diphthong(word, expected):
    assert G2P("pt-PT").transcribe_word(word) == expected


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", ["abaiucado", "piauiense", "goiaba", "maior",
                                  "baiano", "rainha", "distraiu", "saiu",
                                  "pauis", "baú"])
def test_rule_reaches_only_a_stressed_i_or_u_after_a_diphthong(lang, word):
    # goiaba, maior, baiano: the stressed vowel after the diphthong is not
    # ⟨i u⟩. rainha, baú: no diphthong stands before it. distraiu, saiu,
    # pauis: Base X, 6.º, the stressed syllable is the diphthong itself.
    spec = get(lang)
    undeclared = dataclasses.replace(
        spec, stress=dataclasses.replace(spec.stress, tonic_after_diphthong=()))
    assert (G2P(lang).transcribe_word(word)
            == G2P(lang, spec=undeclared).transcribe_word(word))


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
def test_undeclared_rule_puts_the_glide_in_the_onset(lang):
    spec = get(lang)
    undeclared = dataclasses.replace(
        spec, stress=dataclasses.replace(spec.stress, tonic_after_diphthong=()))
    assert G2P(lang, spec=undeclared).transcribe_word("baiuca").startswith(
        "baˈju")


def test_pt_specs_declare_the_rule():
    for code in LANGS + ["pt-UY"]:
        assert get(code).stress.tonic_after_diphthong == (
            "i", "u", "í", "ú"), code


def test_specs_outside_portuguese_do_not_declare_the_rule():
    for code in ("gl-ES", "ext-PT-x-barranco", "mwl", "pt-PT-x-medieval",
                 "es-ES"):
        stress = get(code).stress
        assert stress is None or not stress.tonic_after_diphthong, code


def test_only_a_glide_after_a_listed_diphthong_moves():
    from orthography2ipa.stress import _glide_to_diphthong
    rules = get("pt-PT").stress
    assert _glide_to_diphthong(["bai", "u", "ca"], ["ba", "ju", "kɐ"], 1,
                               rules) == ["baj", "u", "kɐ"]
    # No listed diphthong ends the syllable before the stressed ⟨u⟩.
    assert _glide_to_diphthong(["bra", "u", "ca"], ["bɾa", "ju", "kɐ"], 1,
                               rules) == ["bɾa", "ju", "kɐ"]
    # The stressed IPA syllable starts with a vowel, not a glide: a nucleus
    # never moves.
    assert _glide_to_diphthong(["bai", "ia"], ["ba", "ia"], 1,
                               rules) == ["ba", "ia"]
    # The two divisions differ in length, so the syllables do not line up.
    assert _glide_to_diphthong(["bai", "u", "ca"], ["ba", "jukɐ"], 1,
                               rules) == ["ba", "jukɐ"]
