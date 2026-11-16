"""A stressed pt-PT ⟨e⟩ before ⟨lh nh j ch⟩ is [e], with [ɐ] and [ɛ] as candidates.

Cunha & Cintra (7th ed., p. 431, obs. 1.ª b and c) give a stressed stem ⟨e⟩ before a
palatal consonant "no português de Portugal, com [e] ou [ɐ]" (fecho, desejo, aparelho,
empenho), and [ɛ] only for invejar, embrechar, frechar and vexar. On p. 49 they place the
[ɐ] in Lisbon speech (rei, tenho, telha), so pt-PT-x-lisbon keeps LX_STRESSED_E_PREPALATAL.
Porto and Braga keep their diphthongisation of the tonic mid vowels.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get

RULE_IDS = ("PT_STRESSED_E_PREPALATAL_CLOSE", "PT_STRESSED_E_PREPALATAL_CANDIDATE_LISBON",
            "PT_STRESSED_E_PREPALATAL_CANDIDATE_OPEN")

LATTICE = ["e", "ɐ", "ɛ"]

#: The European specs that take the pt-PT default.
EUROPE = ["pt-PT"] + [f"pt-PT-x-{d}" for d in (
    "coimbra", "minho", "viana", "alfena", "tras-os-montes", "beira", "aveiro", "alentejo",
    "algarve", "acores", "madeira", "sao-miguel", "terceira")]
#: Specs that keep their own value. They disable the rules with a note.
NO_SOURCE = {"pt-AO": ("ˈfɛʃʊ", "ˈtɛʎa"), "pt-CV": ("ˈfeʃu", "ˈteʎɐ"), "pt-GW": ("ˈfɛʃu", "ˈtɛʎɐ"),
             "pt-MO": ("ˈfɛʃu", "ˈtɛʎɐ"), "pt-MZ": ("ˈfɛʃu", "ˈtɛʎɐ"), "pt-ST": ("ˈfɛʃu", "ˈtɛʎɐ"),
             "pt-TL": ("ˈfɛʃo", "ˈtɛla"), "ext-PT-x-barranco": ("ˈfɛʃu", "ˈtɛʎɐ")}
CREOLES = ["aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]


def _stressed_e(word: str, lang: str = "pt-PT") -> list:
    """The candidates of the last ⟨e⟩ slot of *word*, which the tests place under stress."""
    slots = [s for s in G2P(lang).ipa_lattice(word) if s.grapheme == "e"]
    return [c.ipa for c in slots[-1].candidates]


@pytest.mark.parametrize("word, ipa", [
    ("fecho", "ˈfeʃu"), ("desejo", "dɨˈzeʒu"), ("aparelho", "ɐpɐˈɾeʎu"), ("empenho", "ẽˈpeɲu"),
    ("tenho", "ˈteɲu"), ("seja", "ˈseʒɐ"),
])
def test_verb_forms_take_the_close_vowel(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _stressed_e(word) == LATTICE


@pytest.mark.parametrize("word, ipa", [
    ("espelho", "iʃˈpeʎu"), ("telha", "ˈteʎɐ"), ("coelho", "kuˈeʎu"), ("abelha", "ɐˈbeʎɐ"),
    ("igreja", "iˈɡɾeʒɐ"), ("flecha", "ˈfleʃɐ"),
])
def test_nouns_take_the_close_vowel(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _stressed_e(word) == LATTICE


@pytest.mark.parametrize("word, ipa, slot", [
    ("fechar", "fɨˈʃaɾ", ["ɨ", "e", "ɛ"]),
    ("espelhinho", "iʃpɨˈʎiɲu", ["ɨ", "e", "ɛ"]),
    ("velhice", "vɨˈʎisɨ", ["ɨ", "e", "ɛ"]),
])
def test_unstressed_e_keeps_its_reduction(word, ipa, slot):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _stressed_e(word) == slot


@pytest.mark.parametrize("word, ipa", [("complexo", "kõˈplɛʃu"), ("sexo", "ˈsɛʃu"), ("bege", "ˈbɛʒɨ")])
def test_x_and_g_stay_out(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    slots = [s for s in G2P("pt-PT").ipa_lattice(word) if s.grapheme == "e"]
    assert [c.ipa for c in slots[0].candidates] == ["ɛ", "e", "ɨ"]


@pytest.mark.parametrize("word, ipa", [("feixe", "ˈfejʃɨ"), ("eixo", "ˈejʃu")])
def test_the_diphthong_ei_stays_out(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


def test_sentence():
    assert G2P("pt-PT").transcribe("o coelho fecha o espelho velho") == "u kuˈeʎu ˈfeʃɐ u iʃˈpeʎu ˈveʎu"


@pytest.mark.parametrize("word, ipa", [
    ("fecho", "ˈfɐʃu"), ("espelho", "iʃˈpɐʎu"), ("telha", "ˈtɐʎɐ"), ("tenho", "ˈtɐɲu"), ("coelho", "kuˈɐʎu"),
])
def test_lisbon_keeps_its_centralised_vowel(word, ipa):
    assert G2P("pt-PT-x-lisbon").transcribe(word) == ipa


def test_lisbon_disables_the_rules_and_keeps_its_own():
    rules = {r.id: r for r in get("pt-PT-x-lisbon").allophone_rules}
    for rule_id in RULE_IDS:
        assert not rules[rule_id].phonemes
        assert rules[rule_id].notes.startswith("DISABLED for Lisbon")
    assert rules["LX_STRESSED_E_PREPALATAL"].surface == "ɐ"
    assert rules["LX_STRESSED_E_PREPALATAL"].phonemes


@pytest.mark.parametrize("lang", ["pt-PT-x-porto", "pt-PT-x-braga"])
def test_the_north_keeps_its_diphthong(lang):
    g2p = G2P(lang)
    assert (g2p.transcribe("fecho"), g2p.transcribe("telha"), g2p.transcribe("mês")) == ("ˈfjɛʃu", "ˈtjɛʎɐ", "ˈmjeʃ")
    assert all(not r.phonemes for r in get(lang).allophone_rules if r.id in RULE_IDS)


@pytest.mark.parametrize("lang", EUROPE)
def test_european_specs_take_the_default(lang):
    assert _stressed_e("fecho", lang) == LATTICE
    assert _stressed_e("telha", lang) == LATTICE


@pytest.mark.parametrize("lang, ipa", NO_SOURCE.items())
def test_specs_with_no_source_keep_their_value(lang, ipa):
    g2p = G2P(lang)
    assert (g2p.transcribe("fecho"), g2p.transcribe("telha")) == ipa


@pytest.mark.parametrize("lang", [*NO_SOURCE, *CREOLES])
@pytest.mark.parametrize("rule_id", RULE_IDS)
def test_disabled_specs_have_a_note(lang, rule_id):
    rule = next(r for r in get(lang).allophone_rules if r.id == rule_id)
    assert not rule.phonemes
    assert rule.notes.startswith("DISABLED for ")


@pytest.mark.parametrize("lang", ["pt-BR", "pt-BR-x-sp"])
def test_brazilian_specs_have_no_rule(lang):
    assert not any(r.id in RULE_IDS for r in get(lang).allophone_rules)
    assert G2P(lang).transcribe("fecho") == "ˈfeʃu"


@pytest.mark.parametrize("lang", ["pt-UY", "pt-PT-x-medieval"])
def test_specs_outside_the_lane_have_no_rule(lang):
    assert not any(r.id in RULE_IDS for r in get(lang).allophone_rules)
