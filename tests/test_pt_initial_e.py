"""An unstressed word-initial pt-PT ⟨e⟩ takes its value from the first syllable.

Mateus & d'Andrade (1998, D.E.L.T.A. 14(1), p. 26) write that word-initial
/e/ and /ɛ/ are [ɛ] before a coda /L/ (Elvira), [i] when the rhyme has no coda
(elefante), vary between [i], [e] and [ɛ] before a coda /R/ (ermida) and drop
before a coda /S/. Cunha & Cintra (7th ed., p. 53) write "o [e] inicial absoluto
de enorme, erguer, que se pronuncia geralmente [i]".

The spec ranks the slot [i], [e], [ɛ] in an open first syllable and [ɛ], [e],
[i] before a coda ⟨l⟩ or ⟨r⟩, where Infopédia decides the order. Before
another coda consonant, which no source read names, it keeps [e] and ranks
[ɛ] second. A stop before another consonant takes the coda-stop rules
(tests/test_pt_coda_stop.py). Initial ⟨ex⟩, ⟨e⟩ before a vowel, ⟨e⟩ before a coda nasal and
initial ⟨es⟩ before a consonant keep their own readings.

Readings without a page come from Infopédia rows.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get

RULE_IDS = ("PT_INITIAL_E_OPEN", "PT_INITIAL_E_OPEN_CANDIDATE_E",
            "PT_INITIAL_E_OPEN_CANDIDATE_OPEN", "PT_INITIAL_E_OPEN_CANDIDATE_REDUCED",
            "PT_INITIAL_E_LIQUID_CODA", "PT_INITIAL_E_LIQUID_CODA_CANDIDATE_E",
            "PT_INITIAL_E_LIQUID_CODA_CANDIDATE_I", "PT_INITIAL_E_LIQUID_CODA_CANDIDATE_REDUCED",
            "PT_INITIAL_E_CODA_CANDIDATE_OPEN", "PT_INITIAL_E_CODA_CANDIDATE_I",
            "PT_INITIAL_E_CODA_CANDIDATE_REDUCED")

OPEN = ["i", "e", "ɛ", "ɨ"]
LIQUID_CODA = ["ɛ", "e", "i", "ɨ"]
OTHER_CODA = ["e", "ɛ", "i", "ɨ"]
ROW = ["e", "i", "ɨ", "ɛ"]

#: The European specs. They take the pt-PT default.
EUROPE = ["pt-PT"] + [f"pt-PT-x-{d}" for d in (
    "lisbon", "coimbra", "porto", "minho", "viana", "braga", "alfena", "tras-os-montes",
    "beira", "aveiro", "alentejo", "algarve", "acores", "madeira", "sao-miguel", "terceira")]
#: Specs that keep their own value. They disable the rules with a note.
NO_SOURCE = {"pt-AO": ("eleˈfɐ̃tɨ", "eʁˈmida"), "pt-CV": ("eleˈfɐ̃te", "erˈmidɐ"),
             "pt-GW": ("eleˈfɐ̃te", "erˈmidɐ"), "pt-MO": ("elɨˈfɐ̃tɨ", "eʁˈmidɐ"),
             "pt-MZ": ("eleˈfɐ̃te", "erˈmidɐ"), "pt-ST": ("eleˈfɐ̃te", "erˈmidɐ"),
             "pt-TL": ("eleˈfɐ̃te", "erˈmida"), "ext-PT-x-barranco": ("elɨˈfɐ̃tɨ", "eɾˈmidɐ")}
CREOLES = ["aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]


def _first_slot(word: str, lang: str = "pt-PT") -> list:
    """The candidates of the first slot of *word*."""
    return [c.ipa for c in G2P(lang).ipa_lattice(word)[0].candidates]


@pytest.mark.parametrize("word, ipa", [
    ("enorme", "iˈnɔɾmɨ"), ("educar", "iduˈkaɾ"), ("emitir", "imiˈtiɾ"),
    ("elefante", "ilɨˈfɐ̃tɨ"), ("edifício", "idiˈfisiu"), ("enigma", "iˈniɡmɐ"),
    ("errado", "iˈʁadu"), ("esófago", "iˈzɔfɐɡu"), ("essencial", "isẽsiˈaɫ"),
])
def test_initial_e_in_an_open_syllable_is_i(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _first_slot(word) == OPEN


@pytest.mark.parametrize("word, ipa", [
    ("elvense", "ɛɫˈvẽsɨ"), ("elzevir", "ɛɫzɨˈviɾ"),
    ("ermida", "ɛɾˈmidɐ"), ("erguer", "ɛɾˈɡeɾ"), ("erguido", "ɛɾˈɡidu"),
])
def test_initial_e_before_a_coda_l_or_r_is_open(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _first_slot(word) == LIQUID_CODA


@pytest.mark.parametrize("word, ipa", [
    ("eclipse", "eˈklipsɨ"), ("eclosão", "ekluˈzɐ̃w̃"), ("ecler", "eˈklɛɾ"),
])
def test_initial_e_before_another_coda_keeps_e(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _first_slot(word) == OTHER_CODA


@pytest.mark.parametrize("word, ipa", [
    ("ecto", "ˈektu"), ("elmo", "ˈeɫmu"), ("efe", "ˈefɨ"), ("esse", "ˈesɨ"),
])
def test_stressed_initial_e_keeps_the_row(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _first_slot(word) == ROW


@pytest.mark.parametrize("word, ipa, slot", [
    ("estar", "iʃˈtaɾ", ["i", "i", "ɨ", "ɛ"]),
    ("exemplo", "eˈʃẽplu", ROW),
    ("explicar", "eʃpliˈkaɾ", ROW),
    ("eólico", "eˈɔliku", ROW),
    ("entrar", "ẽˈtɾaɾ", ["e", "i", "e", "e"]),
    ("enfim", "ẽˈfĩ", ["e", "i", "e", "e"]),
])
def test_other_initial_contexts_stay_out(word, ipa, slot):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _first_slot(word) == slot


def test_conjunction_keeps_its_reading():
    assert G2P("pt-PT").transcribe("e") == "i"


@pytest.mark.parametrize("word, ipa", [("pesado", "pɨˈzadu"), ("selar", "sɨˈlaɾ"), ("medida", "mɨˈdidɐ")])
def test_medial_unstressed_e_keeps_its_lattice(word, ipa):
    g2p = G2P("pt-PT")
    assert g2p.transcribe(word) == ipa
    assert [c.ipa for c in g2p.ipa_lattice(word)[1].candidates] == ["ɨ", "e", "ɛ"]


def test_second_element_of_a_compound_takes_the_rule():
    assert G2P("pt-PT").transcribe_word("bem-educado") == "ˌbɐ̃j̃iduˈkadu"


def test_sentence():
    assert G2P("pt-PT").transcribe("vi a ermida e o elefante") == "ˈvi ɐ ɛɾˈmidɐ i u ilɨˈfɐ̃tɨ"


def test_word_initial_value_of_the_e_row_is_unchanged():
    row = get("pt-PT").positional_graphemes["e"]
    assert list(row["word_initial"]) == ["e", "i"]


@pytest.mark.parametrize("lang", EUROPE)
def test_european_specs_take_the_default(lang):
    assert G2P(lang).transcribe("elefante").startswith("il")
    assert _first_slot("elefante", lang) == OPEN
    assert _first_slot("ermida", lang) == LIQUID_CODA
    assert _first_slot("eclipse", lang) == OTHER_CODA


@pytest.mark.parametrize("lang, ipa", NO_SOURCE.items())
def test_specs_with_no_source_keep_their_value(lang, ipa):
    assert (G2P(lang).transcribe("elefante"), G2P(lang).transcribe("ermida")) == ipa


@pytest.mark.parametrize("lang", [*NO_SOURCE, *CREOLES])
@pytest.mark.parametrize("rule_id", RULE_IDS)
def test_disabled_specs_have_a_note(lang, rule_id):
    rule = next(r for r in get(lang).allophone_rules if r.id == rule_id)
    assert not rule.phonemes
    assert rule.notes.startswith("DISABLED for ")


@pytest.mark.parametrize("lang", ["pt-BR", "pt-BR-x-sp", "pt-UY", "pt-PT-x-medieval"])
def test_specs_outside_the_lane_have_no_rule(lang):
    assert not any(r.id in RULE_IDS for r in get(lang).allophone_rules)
