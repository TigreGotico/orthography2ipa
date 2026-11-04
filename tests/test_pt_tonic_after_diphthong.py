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
starts the next syllable. The Portal da Língua Portuguesa Dicionário fonético
divides and transcribes it so: bai·u·ca [baj'ukɐ].
"""
from __future__ import annotations

import dataclasses

import pytest

from orthography2ipa import G2P, get, get_syllabifier

#: European Portuguese, from the Portal da Língua Portuguesa Dicionário
#: fonético (index.php?action=pronunciation), with its ' written as ˈ.
PT_PT = [
    ("baiuca", "bajˈukɐ"),        # bai·u·ca, Base X, 4.º
    ("boiuno", "bojˈunu"),        # boi·u·no, Base X, 4.º
    ("tuiuiú", "tujujˈu"),        # tui·ui·ú, Base X, 5.º
    ("maiúscula", "majˈuʃkulɐ"),  # mai·ús·cu·la
]

#: The Portal writes ⟨ei⟩ as the Lisbon [ɐj]. pt-PT keeps [ej], and
#: pt-PT-x-lisbon gives [ɐj], so these words are read with the Lisbon spec.
PT_PT_LISBON = [
    ("cheiinho", "ʃɐjˈiɲu"),      # chei·i·nho, Base X, 4.º
    ("teiú", "tɐjˈu"),            # tei·ú, Base X, 5.º
    ("feiura", "fɐjˈuɾɐ"),        # fei·u·ra
]

#: The Base X, 4.º and 5.º examples, and the Portal words above. The Portal
#: does not list cauila, saiinha, Piauí, teiús or cauim, so their test reads
#: only the division that the clauses state: the mark follows the glide.
IN_CONTEXT = ["baiuca", "boiuno", "cauila", "cheiinho", "saiinha", "Piauí",
              "teiú", "teiús", "tuiuiú", "cauim", "maiúscula", "feiura"]

#: The ⟨i u⟩ after the diphthong is unstressed, so the clauses do not reach
#: it. Portal: a·bai·u·ca·do [ɐbaju'kadu], a·bai·u·car [ɐbaju'kaɾ],
#: pi·au·i·en·se [piawi'ẽsɨ].
CONTROLS = [
    ("abaiucado", "ɐbajuˈkadu"),
    ("abaiucar", "ɐbajuˈkaɾ"),
    ("piauiense", "piawiˈẽsɨ"),
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


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word", IN_CONTEXT)
def test_mark_follows_the_glide_of_the_diphthong(lang, word):
    ipa = G2P(lang).transcribe_word(word)
    assert _mark_after_glide(ipa), ipa


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", IN_CONTEXT)
def test_without_the_plugin_both_paths_agree(lang, word, monkeypatch):
    with_plugin = G2P(lang).transcribe_word(word)
    from orthography2ipa import registry
    monkeypatch.setattr(registry, "_syllabifiers", {})
    assert get_syllabifier(lang) is None
    ipa = G2P(lang).transcribe_word(word)
    assert _mark_after_glide(ipa), ipa
    assert ipa == with_plugin


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
