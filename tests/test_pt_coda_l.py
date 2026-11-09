"""An unstressed pt-PT ⟨a e o⟩ before a coda ⟨l⟩ keeps a full vowel: [a], [ɛ], [o].

Cunha & Cintra (7th ed., p. 53) list among the unstressed vowels that do not
reduce "as vogais [a], [ɛ], [o] protegidas por l implosivo de altar, delgado,
soldado, colchão". A word-final ⟨l⟩ is in a coda, so it is implosive too. The
reduced value stays in the lattice, and ⟨o⟩ also keeps [ɔ]. A stressed vowel, a
word-initial ⟨o⟩ and a digraph ⟨lh⟩ keep their readings.

Readings without a page come from Infopédia rows.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get

RULE_IDS = ("PT_CODA_L_A_OPEN", "PT_CODA_L_A_CANDIDATE_REDUCED",
            "PT_CODA_L_E_OPEN", "PT_CODA_L_E_CANDIDATE_REDUCED",
            "PT_CODA_L_O_CLOSE", "PT_CODA_L_O_CANDIDATE_OPEN", "PT_CODA_L_O_CANDIDATE_REDUCED")

A, E, O = ["a", "ɐ"], ["ɛ", "e", "ɨ"], ["o", "ɔ", "u"]

#: The European specs. They take the pt-PT default.
EUROPE = ["pt-PT"] + [f"pt-PT-x-{d}" for d in (
    "lisbon", "coimbra", "porto", "minho", "viana", "braga", "alfena", "tras-os-montes",
    "beira", "aveiro", "alentejo", "algarve", "acores", "madeira", "sao-miguel", "terceira")]
#: Specs that keep their own value. They disable the rules with a note.
NO_SOURCE = {"pt-AO": ("aɫˈtaɾ", "deɫˈɡadʊ", "soɫˈdadʊ"), "pt-CV": ("ɐɫˈtar", "deɫˈɡadu", "suɫˈdadu"),
             "pt-GW": ("ɐɫˈtar", "deɫˈɡadu", "soɫˈdadu"), "pt-MO": ("ɐɫˈtaʁ", "dɨɫˈɡadu", "suɫˈdadu"),
             "pt-MZ": ("ɐɫˈtaɾ", "deɫˈɡadu", "soɫˈdadu"), "pt-ST": ("ɐɫˈtar", "deɫˈɡadu", "soɫˈdadu"),
             "pt-TL": ("aɫˈtaɾ", "deɫˈɡado", "soɫˈdado"),
             "ext-PT-x-barranco": ("ˈɐltɐ", "dɨlˈɡadu", "sulˈdadu")}
CREOLES = ["aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]


def _slot(word: str, index: int, lang: str = "pt-PT") -> list:
    """The candidates of slot *index* of *word*."""
    return [c.ipa for c in G2P(lang).ipa_lattice(word)[index].candidates]


def _before_l(word: str, vowel: str) -> list:
    """The candidates of the first *vowel* slot that an ⟨l⟩ slot follows."""
    slots = G2P("pt-PT").ipa_lattice(word)
    slot = next(s for s, n in zip(slots, slots[1:]) if s.grapheme == vowel and n.grapheme == "l")
    return [c.ipa for c in slot.candidates]


@pytest.mark.parametrize("word, ipa", [
    ("altar", "aɫˈtaɾ"), ("calçado", "kaɫˈsadu"), ("falcão", "faɫˈkɐ̃w̃"), ("alguém", "aɫˈɡɐ̃j̃"),
])
def test_a_before_a_coda_l_is_open(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _before_l(word, "a") == A


@pytest.mark.parametrize("word, ipa", [
    ("delgado", "dɛɫˈɡadu"), ("amável", "ɐˈmavɛɫ"), ("móvel", "ˈmɔvɛɫ"),
    ("desprazível", "dɨʃpɾɐˈzivɛɫ"), ("incomparavelmente", "ĩkõpɐɾɐvɛɫˈmẽtɨ"),
])
def test_e_before_a_coda_l_is_open(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _before_l(word, "e") == E


@pytest.mark.parametrize("word, ipa", [
    ("soldado", "soɫˈdadu"), ("colchão", "koɫˈʃɐ̃w̃"), ("soltar", "soɫˈtaɾ"), ("álcool", "ˈaɫkuoɫ"),
])
def test_o_before_a_coda_l_is_close(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _before_l(word, "o") == O


@pytest.mark.parametrize("word, ipa", [
    ("alto", "ˈaɫtu"), ("selva", "ˈsɛɫvɐ"), ("solto", "ˈsɔɫtu"), ("papel", "pɐˈpɛɫ"),
    ("faldas", "ˈfaɫdɐʃ"),
])
def test_stressed_vowel_keeps_its_reading(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [("olfato", "ɔɫˈfatu"), ("olmeiro", "ɔɫˈmejɾu")])
def test_initial_o_keeps_the_initial_o_ranking(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _slot(word, 0) == ["ɔ", "u", "o"]


def test_initial_e_keeps_the_initial_e_ranking():
    assert G2P("pt-PT").transcribe("elvense") == "ɛɫˈvẽsɨ"
    assert _slot("elvense", 0) == ["ɛ", "e", "i", "ɨ"]


@pytest.mark.parametrize("word, ipa, index, slot", [
    ("molhar", "muˈʎaɾ", 1, ["u", "o", "ɔ"]),
    ("velhice", "vɨˈʎisɨ", 1, ["ɨ", "e", "ɛ"]),
    ("calado", "kɐˈladu", 1, ["ɐ", "a"]),
])
def test_lh_and_onset_l_stay_out(word, ipa, index, slot):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _slot(word, index) == slot


def test_u_and_i_keep_their_value():
    assert G2P("pt-PT").transcribe("pulmão") == "puɫˈmɐ̃w̃"


def test_sentence():
    assert G2P("pt-PT").transcribe("o soldado deve soltar o falcão") == "u soɫˈdadu ˈdɛvɨ soɫˈtaɾ u faɫˈkɐ̃w̃"


@pytest.mark.parametrize("lang", EUROPE)
def test_european_specs_take_the_default(lang):
    assert _slot("altar", 0, lang) == A
    assert _slot("delgado", 1, lang) == E
    assert _slot("soldado", 1, lang) == O


@pytest.mark.parametrize("lang, ipa", NO_SOURCE.items())
def test_specs_with_no_source_keep_their_value(lang, ipa):
    g2p = G2P(lang)
    assert (g2p.transcribe("altar"), g2p.transcribe("delgado"), g2p.transcribe("soldado")) == ipa


@pytest.mark.parametrize("lang", [*NO_SOURCE, *CREOLES])
@pytest.mark.parametrize("rule_id", RULE_IDS)
def test_disabled_specs_have_a_note(lang, rule_id):
    rule = next(r for r in get(lang).allophone_rules if r.id == rule_id)
    assert not rule.phonemes
    assert rule.notes.startswith("DISABLED for ")


@pytest.mark.parametrize("lang, ipa", [("pt-BR", "awˈtaɾ"), ("pt-BR-x-sp", "awˈtaɾ")])
def test_brazilian_specs_have_no_rule(lang, ipa):
    assert not any(r.id in RULE_IDS for r in get(lang).allophone_rules)
    assert G2P(lang).transcribe("altar") == ipa


@pytest.mark.parametrize("lang", ["pt-UY", "pt-PT-x-medieval"])
def test_specs_outside_the_lane_have_no_rule(lang):
    assert not any(r.id in RULE_IDS for r in get(lang).allophone_rules)
