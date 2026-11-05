"""pt-BR epenthesis after the stressed syllable, and ⟨ck⟩ as a homorganic pair.

Curioletti & Sandri (2019, PDF p. 6) give capto [kapitu] as the epenthesis
that "só se aplica em sequências não-homorgânicas". Collischonn (2004: 66)
reports Câmara Jr.: "idênticas as pautas prosódicas de rapto e rápido", so
rapto takes the stress and the syllable count of rápido. Collischonn (2004:
67, 76) counts the post-tonic vowel in 24 % of southern tokens and reads the
grammar without it as the preferred one, so the southern children keep the
cluster. The rules and their full citations are BR_EPENTHESIS_POSTTONIC and
BR_GEMINATE_C in pt-BR.json.
"""
import dataclasses

import pytest

from orthography2ipa import G2P, transcribe
from orthography2ipa.json_loader import load_json_spec


def test_capto():
    assert transcribe("capto", "pt-BR") == "ˈkapitu"


def test_rapto_has_the_prosody_of_rapido():
    rapto = transcribe("rapto", "pt-BR")
    rapido = transcribe("rápido", "pt-BR")
    assert rapto.replace("t", "d") == rapido, (rapto, rapido)


@pytest.mark.parametrize("word,stressed", [
    ("pacto", "ˈpa"),
    ("Pacto", "ˈpa"),
    ("pactos", "ˈpa"),
    ("compacto", "ˈpa"),
    ("egípcio", "ˈʒi"),
    ("helicóptero", "ˈkɔ"),
])
def test_the_inserted_vowel_does_not_move_the_stress(word, stressed):
    out = transcribe(word, "pt-BR")
    assert stressed in out, out
    assert out.count("ˈ") == 1, out


@pytest.mark.parametrize("word,expected", [
    ("chips", "ˈʃips"), ("clips", "ˈklips"), ("script", "ˈskɾipt"),
])
def test_a_word_final_cluster_stays_as_spelled(word, expected):
    # The rule reads a stop with a nucleus after it, as BR_EPENTHESIS does,
    # so a word-final cluster is outside both rules.
    assert transcribe(word, "pt-BR") == expected


@pytest.mark.parametrize("word,stressed", [
    ("corrupta", "ˈʁup"),
    ("subterrâneo", "ˈʁɐ̃"),
    ("blitzkrieg", "ˈkɾi"),
])
def test_the_mark_stands_before_the_onset_of_the_stressed_syllable(word, stressed):
    # A digraph split across two written syllables (⟨rr⟩) or a cluster the
    # spelling divides elsewhere does not move the mark into the onset.
    assert stressed in transcribe(word, "pt-BR")


def test_pretonic_epenthesis_keeps_its_stress():
    assert transcribe("advogado", "pt-BR") == "ad͡ʒivoˈɡadu"
    assert transcribe("opção", "pt-BR") == "opiˈsɐ̃w̃"


@pytest.mark.parametrize("code", ["pt-BR-x-sul", "pt-BR-x-floripa", "pt-BR-x-pr"])
def test_the_southern_children_keep_the_post_tonic_cluster(code):
    assert transcribe("capto", code) == "ˈkaptu"
    assert transcribe("opção", code).startswith("opi")


@pytest.mark.parametrize("code", ["pt-BR-x-sp", "pt-BR-x-rj"])
def test_other_children_inherit_the_rule(code):
    assert transcribe("capto", code) == "ˈkapitu"


@pytest.mark.parametrize("word", ["hockey", "jockey"])
def test_ck_takes_no_vowel(word):
    out = transcribe(word, "pt-BR")
    assert "kik" not in out.replace("ˈ", ""), out


def test_the_post_tonic_rule_is_independent_of_the_pretonic_one():
    spec = load_json_spec("pt-BR")
    rules = tuple(r for r in spec.allophone_rules if r.id != "BR_EPENTHESIS")
    g = G2P("pt-BR", spec=dataclasses.replace(spec, allophone_rules=rules))
    assert g.transcribe("capto") == "ˈkapitu"
    assert g.transcribe("advogado") == "advoˈɡadu"


def test_a_vowel_inserted_before_the_stressed_nucleus_does_not_take_the_mark():
    # The rule widened to every stop of the stressed syllable reaches the
    # onset cluster of pseudo. The inserted vowel stands before the stressed
    # nucleus, so the mark stays after it.
    spec = load_json_spec("pt-BR")
    rules = tuple(
        dataclasses.replace(r, preceded_by=None)
        if r.id == "BR_EPENTHESIS_POSTTONIC" else r
        for r in spec.allophone_rules if r.id != "BR_EPENTHESIS_ONSET")
    g = G2P("pt-BR", spec=dataclasses.replace(spec, allophone_rules=rules))
    assert g.transcribe("pseudo") == "piˈsewdu"
    assert g.transcribe("pacto") == "ˈpakitu"


@pytest.fixture
def without_syllabifier_plugin(monkeypatch):
    from orthography2ipa import registry
    monkeypatch.setattr(registry, "_syllabifiers", {})


@pytest.mark.parametrize("word,start", [
    ("capto", "ˈkapitu"), ("pacto", "ˈpakitu"), ("egípcio", "eˈʒipi"),
])
def test_without_the_syllabifier_plugin(word, start, without_syllabifier_plugin):
    out = G2P("pt-BR").transcribe_word(word)
    assert out.startswith(start), out


@pytest.mark.parametrize("word", ["hockey", "jockey"])
def test_ck_without_the_syllabifier_plugin(word, without_syllabifier_plugin):
    out = G2P("pt-BR").transcribe_word(word)
    assert "kik" not in out.replace("ˈ", ""), out


@pytest.mark.parametrize("word", ["бутербродів", "церковний", "продовжую"])
def test_a_vocalised_glide_is_not_an_inserted_nucleus(word):
    # Ukrainian ⟨в⟩ gives the non-syllabic [u̯]. It adds no syllable, so the
    # stress mark stays where the syllable count puts it.
    counted = G2P("uk")
    counted._fold_inserted_nuclei = lambda *args: None
    assert G2P("uk").transcribe(word) == counted.transcribe(word)
