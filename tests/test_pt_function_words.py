"""The stressed vowel of pt-PT function words and frequent adverbs.

Infopédia rows give most expected values, with WikiPron pt-PT (the Portugal
pronunciations of en.wiktionary) for the forms that Infopédia does not list.
Infopédia writes the tap as [r] and the reduced vowel as [ə]; the tests write
[ɾ] and [ɨ], as the spec does. Cruz-Ferreira (1999, Handbook of the IPA, p. 130)
writes aquele [ɐˈkel], mas [mɐʃ] and todo [ˈtodu]. A native-speaker report gives
cada [ˈkɐdɐ]. Cunha & Cintra (7th ed., p. 69) list sob among the atonic
monosyllables, and p. 87 lists para, form of parar, and para, preposition, as
homographs.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get

RULE_IDS = ("PT_LEX_REDUCED_A", "PT_LEX_PARA_CANDIDATE_VERB",
            "PT_LEX_FUNCTION_CLOSE_E", "PT_LEX_FUNCTION_OPEN_E",
            "PT_LEX_FUNCTION_CLOSE_O", "PT_LEX_FUNCTION_OPEN_O",
            "PT_LEX_TODO_CLOSE", "PT_LEX_TODO_CANDIDATE_OPEN",
            "PT_LEX_VOCE_OPEN_O", "PT_LEX_SOB_CLOSE_O")
#: The rules that set a stressed mid vowel. The specs with their own stressed mid-vowel process disable them.
MID_IDS = ("PT_LEX_FUNCTION_CLOSE_E", "PT_LEX_FUNCTION_OPEN_E", "PT_LEX_FUNCTION_CLOSE_O",
           "PT_LEX_FUNCTION_OPEN_O", "PT_LEX_TODO_CLOSE", "PT_LEX_TODO_CANDIDATE_OPEN")

#: The European specs that take every rule.
EUROPE = ["pt-PT"] + [f"pt-PT-x-{d}" for d in (
    "lisbon", "coimbra", "minho", "viana", "alfena", "tras-os-montes",
    "beira", "aveiro", "alentejo", "algarve", "acores", "madeira", "sao-miguel")]
OWN_MID_VOWELS = ["pt-PT-x-porto", "pt-PT-x-braga", "pt-PT-x-terceira"]
#: Specs that keep their own value: cada, para, ela, aquele, todo, você, hoje.
NO_SOURCE = {
    "pt-AO": ("ˈkada", "ˈpaɾa", "ˈela", "aˈkɛlɨ", "ˈtɔdʊ", "voˈse", "ˈɔʒɨ"),
    "pt-CV": ("ˈkadɐ", "ˈparɐ", "ˈelɐ", "ɐˈkele", "ˈtɔdu", "vuˈse", "ˈɔʒe"),
    "pt-GW": ("ˈkadɐ", "ˈparɐ", "ˈɛlɐ", "ɐˈkɛle", "ˈtɔdu", "voˈse", "ˈɔʒe"),
    "pt-MO": ("ˈkadɐ", "ˈpaɾɐ", "ˈelɐ", "ɐˈkɛlɨ", "ˈtɔdu", "vuˈse", "ˈɔʒɨ"),
    "pt-MZ": ("ˈkadɐ", "ˈpaɾɐ", "ˈelɐ", "ɐˈkɛle", "ˈtɔdu", "voˈse", "ˈɔʒe"),
    "pt-ST": ("ˈkadɐ", "ˈparɐ", "ˈelɐ", "ɐˈkɛle", "ˈtɔdu", "voˈse", "ˈɔʒe"),
    "pt-TL": ("ˈkada", "ˈpaɾa", "ˈela", "aˈkɛle", "ˈtɔdo", "voˈse", "ˈɔʒe"),
    "ext-PT-x-barranco": ("ˈkadɐ", "ˈpaɾɐ", "ˈelɐ", "ɐˈkɛlɨ", "ˈtɔdu", "buˈse", "ˈhɔʒɨ"),
}
CREOLES = ["aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]


def _slot(word: str, grapheme: str, lang: str = "pt-PT") -> list:
    """The candidates of the slot of *word* whose grapheme is *grapheme*, first match."""
    slot = next(s for s in G2P(lang).ipa_lattice(word) if s.grapheme == grapheme)
    return [c.ipa for c in slot.candidates]


@pytest.mark.parametrize("word, ipa", [
    ("cada", "ˈkɐdɐ"),     # native-speaker report; Infopédia; WikiPron kɐdɐ
    ("para", "ˈpɐɾɐ"),     # Infopédia first reading
    ("mas", "ˈmɐʃ"),       # Infopédia; Cruz-Ferreira p. 130 [mɐʃ]
])
def test_stressed_a_of_cada_para_mas_is_reduced(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


def test_para_keeps_the_verb_reading_second():
    # Infopédia second reading [ˈparɐ], the verb form of parar.
    assert _slot("para", "a") == ["ɐ", "a"]


@pytest.mark.parametrize("word, ipa", [
    ("aquele", "ɐˈkelɨ"), ("daquele", "dɐˈkelɨ"), ("naquele", "nɐˈkelɨ"), ("àquele", "aˈkelɨ"),
    ("deste", "ˈdeʃtɨ"), ("neste", "ˈneʃtɨ"), ("desse", "ˈdesɨ"), ("dele", "ˈdelɨ"), ("nele", "ˈnelɨ"),
    ("mesmo", "ˈmeʒmu"), ("mesma", "ˈmeʒmɐ"), ("desde", "ˈdeʒdɨ"), ("menos", "ˈmenuʃ"),
    ("apenas", "ɐˈpenɐʃ"), ("cedo", "ˈsedu"),
])
def test_close_e_from_infopedia(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("aqueles", "ɐˈkelɨʃ"), ("daqueles", "dɐˈkelɨʃ"), ("naqueles", "nɐˈkelɨʃ"), ("àqueles", "aˈkelɨʃ"),
    ("destes", "ˈdeʃtɨʃ"), ("nestes", "ˈneʃtɨʃ"), ("desses", "ˈdesɨʃ"), ("nesse", "ˈnesɨ"),
    ("nesses", "ˈnesɨʃ"), ("deles", "ˈdelɨʃ"), ("neles", "ˈnelɨʃ"), ("mesmos", "ˈmeʒmuʃ"),
    ("mesmas", "ˈmeʒmɐʃ"),
])
def test_close_e_from_wikipron(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("esta", "ˈɛʃtɐ"), ("essa", "ˈɛsɐ"), ("aquela", "ɐˈkɛlɐ"), ("ela", "ˈɛlɐ"),
])
def test_open_e_from_infopedia(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("estas", "ˈɛʃtɐʃ"), ("essas", "ˈɛsɐʃ"), ("elas", "ˈɛlɐʃ"), ("desta", "ˈdɛʃtɐ"),
    ("nessa", "ˈnɛsɐ"), ("daquela", "dɐˈkɛlɐ"), ("àquela", "aˈkɛlɐ"), ("dela", "ˈdɛlɐ"),
    ("nelas", "ˈnɛlɐʃ"),
])
def test_open_e_from_wikipron(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("este", "ˈeʃtɨ"), ("estes", "ˈeʃtɨʃ"), ("esse", "ˈesɨ"), ("esses", "ˈesɨʃ"),
    ("ele", "ˈelɨ"), ("eles", "ˈelɨʃ"),
])
def test_word_initial_masculine_forms_keep_the_row(word, ipa):
    # The word-initial ⟨e⟩ row ranks [e] first. The noun este, east, keeps [ɛ] as a candidate.
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _slot(word, "e") == ["e", "i", "ɨ", "ɛ"]


@pytest.mark.parametrize("word, ipa", [
    ("connosco", "kõˈnoʃku"), ("convosco", "kõˈvoʃku"), ("hoje", "ˈoʒɨ"), ("ora", "ˈɔɾɐ"),
])
def test_stressed_o(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("todo", "ˈtodu"), ("toda", "ˈtodɐ"), ("todos", "ˈtoduʃ"), ("todas", "ˈtodɐʃ"),
])
def test_todo_is_close_and_keeps_the_noun_reading_second(word, ipa):
    # Cruz-Ferreira p. 130 [ˈtodu]; Infopédia todo [ˈtodu] then [ˈtɔdu], the noun o todo.
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _slot(word, "o") == ["o", "ɔ", "u"]


@pytest.mark.parametrize("word, ipa", [("você", "vɔˈse"), ("vocês", "vɔˈseʃ")])
def test_pretonic_o_of_voce_is_open(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


def test_sob_is_atonic_with_a_close_vowel():
    # Infopédia sob [sob], with no stress mark; Cunha & Cintra p. 69.
    assert G2P("pt-PT").transcribe("sob") == "sob"
    assert "sob" in get("pt-PT").stress.cliticless_words


def test_sequer_takes_the_open_vowel_of_quer():
    # WikiPron pt-PT sɨkɛɾ; pt.wiktionary [sɨˈkɛɾ].
    assert G2P("pt-PT").transcribe("sequer") == "sɨˈkɛɾ"


@pytest.mark.parametrize("text, ipa", [
    ("cada dia", "ˈkɐdɐ ˈdiɐ"),
    ("para casa", "ˈpɐɾɐ ˈkazɐ"),
    ("mas quanto mais soprava", "ˈmɐʃ ˈkwɐ̃tu ˈmajʃ suˈpɾavɐ"),
    ("aquele que primeiro", "ɐˈkelɨ kɨ pɾiˈmejɾu"),
    ("com todo o esplendor", "kõ ˈtodu u iʃplẽˈdoɾ"),
    ("sob a mesa", "sob ɐ ˈmezɐ"),
    ("ela e ele", "ˈɛlɐ i ˈelɨ"),
])
def test_phrases(text, ipa):
    assert G2P("pt-PT").transcribe(text) == ipa


@pytest.mark.parametrize("word, ipa", [("casa", "ˈkazɐ"), ("pato", "ˈpatu"), ("parar", "pɐˈɾaɾ")])
def test_other_stressed_a_keeps_its_reading(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [("pelo", "pɨlu"), ("pela", "pɨlɐ")])
def test_contractions_with_por_stay_atonic(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("lang", EUROPE)
def test_european_specs_take_the_rules(lang):
    g2p = G2P(lang)
    assert g2p.transcribe("cada").startswith("ˈkɐ")
    assert _slot("ela", "e", lang)[0] == "ɛ"
    assert _slot("aquele", "e", lang)[0] == "e"
    assert _slot("todo", "o", lang)[:2] == ["o", "ɔ"]


@pytest.mark.parametrize("lang", OWN_MID_VOWELS)
def test_specs_with_their_own_mid_vowels_take_only_the_other_rules(lang):
    assert G2P(lang).transcribe("cada").startswith("ˈkɐ")
    for rule_id in MID_IDS:
        rule = next(r for r in get(lang).allophone_rules if r.id == rule_id)
        assert not rule.phonemes
        assert rule.notes.startswith("DISABLED here.")


@pytest.mark.parametrize("lang, ipa", NO_SOURCE.items())
def test_specs_with_no_source_keep_their_value(lang, ipa):
    g2p = G2P(lang)
    assert tuple(g2p.transcribe(w) for w in ("cada", "para", "ela", "aquele", "todo", "você", "hoje")) == ipa


@pytest.mark.parametrize("lang", [*NO_SOURCE, *CREOLES])
@pytest.mark.parametrize("rule_id", RULE_IDS)
def test_disabled_specs_have_a_note(lang, rule_id):
    rule = next(r for r in get(lang).allophone_rules if r.id == rule_id)
    assert not rule.phonemes
    assert rule.notes.startswith("DISABLED for ")


@pytest.mark.parametrize("lang", ["pt-BR", "pt-BR-x-sp"])
def test_brazilian_specs_have_no_rule(lang):
    assert not any(r.id in RULE_IDS for r in get(lang).allophone_rules)
    g2p = G2P(lang)
    assert (g2p.transcribe("cada"), g2p.transcribe("para"), g2p.transcribe("todo")) == ("ˈkadɐ", "ˈpaɾɐ", "ˈtodu")
