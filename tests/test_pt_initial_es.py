"""A word-initial unstressed pt-PT ⟨e⟩ before a coda sibilant is [i].

Vázquez Diéguez (2015, Anuario de Estudios Filológicos 38) gives "estar [i] / —"
for Europe on p. 242, the series "esc- [(i)ʃk]", "est- [(i)ʃt]" and their sisters
on p. 250, and "pode desaparecer, p. ex. [iʃˈtaɾ / ʃˈtaɾ]" on p. 265. The spec
writes the vowel. The drop stays unmodelled.

Albuquerque (2010, ReVEL 8(15)) writes espelho [es.ˈpe.lu] on p. 276 and lists
escola [is.ˈkɔ.la] ~ [iʃ.kɔ.la] among traits shared with the Asian creoles on
p. 277, so pt-TL keeps [e].

Readings without a page come from Infopédia rows, with its optional (i) written.
"""
from __future__ import annotations

from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import G2P, get

RULE_ID = "PT_INITIAL_ES_RAISE"
DATA = Path(orthography2ipa.__file__).parent / "data"

#: The European specs. The source speaks for Europe, so they inherit the rule.
EUROPE = ["pt-PT"] + [f"pt-PT-x-{d}" for d in (
    "lisbon", "coimbra", "porto", "minho", "viana", "braga", "alfena", "tras-os-montes",
    "beira", "aveiro", "alentejo", "algarve", "acores", "madeira", "sao-miguel", "terceira")]
#: Specs that keep their own value. They disable the rule with a note.
NO_SOURCE = {"pt-AO": "esˈkɔla", "pt-TL": "esˈkɔla", "pt-CV": "esˈkɔlɐ", "pt-GW": "esˈkɔlɐ", "pt-MO": "eʃˈkɔlɐ",
             "pt-MZ": "esˈkɔlɐ", "pt-ST": "esˈkɔlɐ", "ext-PT-x-barranco": "ehˈkɔlɐ"}
CREOLES = ["aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]


def _rule(lang: str):
    return next((r for r in get(lang).allophone_rules if r.id == RULE_ID), None)


@pytest.mark.parametrize("word, ipa", [
    ("estar", "iʃˈtaɾ"), ("escola", "iʃˈkɔlɐ"), ("esmola", "iʒˈmɔlɐ"),
    ("esbelto", "iʒˈbɛɫtu"), ("esplendor", "iʃplẽˈdoɾ"), ("escrever", "iʃkɾɨˈveɾ"),
])
def test_initial_es(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, start", [
    ("esbaforir", "iʒb"), ("escabeche", "iʃk"), ("esdrúxulo", "iʒˈd"), ("esfacelar", "iʃf"),
    ("esgaçar", "iʒɡ"), ("eslavo", "iʒˈl"), ("esmagar", "iʒm"), ("espaçar", "iʃp"),
    ("esquadra", "iʃˈk"), ("estabelecer", "iʃt"), ("esvaziar", "iʒv"),
])
def test_every_series_of_vazquez_p250(word, start):
    assert G2P("pt-PT").transcribe(word).startswith(start)


@pytest.mark.parametrize("word, ipa", [
    ("este", "ˈeʃtɨ"), ("esse", "ˈesɨ"), ("esmo", "ˈeʒmu"),
])
def test_stressed_e_stays_out(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word", ["esta", "essa", "esca", "esto", "estro"])
def test_stressed_e_keeps_the_stress_mark(word):
    assert G2P("pt-PT").transcribe(word).startswith("ˈe")


@pytest.mark.parametrize("word, ipa", [
    ("essência", "eˈsẽsiɐ"), ("essoutro", "eˈsotɾu"), ("essonite", "esuˈnitɨ"),
])
def test_double_s_stays_out(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word", ["explicar", "exterior", "extensão"])
def test_initial_ex_stays_with_its_own_rule(word):
    assert not G2P("pt-PT").transcribe(word).startswith("i")


@pytest.mark.parametrize("word, ipa", [
    ("esotérico", "ezuˈtɛɾiku"), ("esófago", "eˈzɔfɐɡu"),
])
def test_initial_es_before_a_vowel_stays_out(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("desde", "ˈdɛʒdɨ"), ("pesca", "ˈpɛʃkɐ"), ("pescar", "pɨʃˈkaɾ"), ("mesquinho", "mɨʃˈkiɲu"),
    ("gestão", "ʒɨʃˈtɐ̃w̃"),
])
def test_medial_es_stays_out(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("elefante", "elɨˈfɐ̃tɨ"), ("edifício", "ediˈfisiu"), ("ermida", "eɾˈmidɐ"),
])
def test_other_initial_e_keeps_its_value(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


def test_word_initial_value_of_the_e_row_is_unchanged():
    row = get("pt-PT").positional_graphemes["e"]
    assert list(row["word_initial"]) == ["e", "i"]


@pytest.mark.parametrize("lang", EUROPE)
def test_european_specs_take_the_vowel_and_keep_their_coda(lang):
    assert G2P(lang).transcribe("estar") == "iʃˈtaɾ"
    assert G2P(lang).transcribe("esbelto").startswith("iʒ")


def test_algarve_takes_the_pt_pt_pretonic_row():
    assert G2P("pt-PT-x-algarve").transcribe("menino") == "mɨˈninu"


@pytest.mark.parametrize("lang, ipa", [("pt-PT-x-algarve", "pɨʃˈkaɾ"), ("pt-TL", "pesˈkaɾ")])
def test_medial_es_stays_out_of_algarve_and_timor(lang, ipa):
    assert G2P(lang).transcribe("pescar") == ipa


def test_terceira_keeps_its_metaphony():
    assert G2P("pt-PT-x-terceira").transcribe("estado") == "iʃˈtɔdu"


@pytest.mark.parametrize("lang, ipa", NO_SOURCE.items())
def test_specs_with_no_source_keep_their_value(lang, ipa):
    assert G2P(lang).transcribe("escola") == ipa


@pytest.mark.parametrize("lang", [*NO_SOURCE, *CREOLES])
def test_disabled_specs_have_a_note(lang):
    rule = _rule(lang)
    assert rule is not None and not rule.phonemes
    assert rule.notes.startswith("DISABLED for ")


@pytest.mark.parametrize("lang", ["pt-BR", "pt-BR-x-sp", "pt-UY", "pt-PT-x-medieval"])
def test_specs_outside_the_lane_have_no_rule(lang):
    assert _rule(lang) is None


def test_no_other_spec_carries_the_rule():
    # A new child of pt-PT inherits the rule, so it fails here until it is
    # sorted into one of the lists above.
    carriers = {p.stem for p in DATA.glob("*.json") if _rule(p.stem)}
    assert carriers == {*EUROPE, *NO_SOURCE, *CREOLES}
