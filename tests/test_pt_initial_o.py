"""An unstressed word-initial pt-PT ⟨o⟩ ranks [ɔ], then [u], then [o].

Cunha & Cintra (7th ed., p. 51) reduce an unstressed back vowel to [u]. On p. 53
they name "o [o] inicial absoluto de ovelha, obter, opinião" as an exception,
which is the careful-speech value. Cruz-Ferreira (1999, Handbook of the IPA,
p. 130) writes obrigar as [ɔbɾiˈgaɾ] in her Lisbon transcription. The spec reads
[ɔ] and keeps [u] and [o] as the second and third lattice candidates. A stressed
word-initial ⟨o⟩ keeps the word_initial row and the word lists. The ⟨h⟩ of a
word-initial ⟨ho⟩ has no sound, so its ⟨o⟩ takes the same ranking.

Readings without a page come from Infopédia rows.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get

RULE_IDS = ("PT_INITIAL_O_KEEP_BEFORE_CODA_NASAL", "PT_INITIAL_O_OPEN",
            "PT_INITIAL_O_CANDIDATE_U", "PT_INITIAL_O_CANDIDATE_O",
            "PT_INITIAL_HO_KEEP_BEFORE_CODA_NASAL", "PT_INITIAL_HO_OPEN",
            "PT_INITIAL_HO_CANDIDATE_U", "PT_INITIAL_HO_CANDIDATE_O")

#: The European specs. They take the pt-PT default.
EUROPE = ["pt-PT"] + [f"pt-PT-x-{d}" for d in (
    "lisbon", "coimbra", "porto", "minho", "viana", "braga", "alfena", "tras-os-montes",
    "beira", "aveiro", "alentejo", "algarve", "acores", "madeira", "sao-miguel", "terceira")]
#: Specs that keep their own value. They disable the rules with a note.
NO_SOURCE = {"pt-AO": "oˈvɛʎa", "pt-CV": "oˈveʎɐ", "pt-GW": "oˈvɛʎɐ", "pt-MO": "oˈvɛʎɐ",
             "pt-MZ": "oˈvɛʎɐ", "pt-ST": "oˈvɛʎɐ", "pt-TL": "oˈvɛla", "ext-PT-x-barranco": "oˈbɛʎɐ"}
CREOLES = ["aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]


def _first_slot(word: str, lang: str = "pt-PT") -> list:
    """The candidates of the first ⟨o⟩ slot, after a silent ⟨h⟩ when there is one."""
    slot = next(s for s in G2P(lang).ipa_lattice(word) if s.grapheme == "o")
    return [c.ipa for c in slot.candidates]


@pytest.mark.parametrize("word, ipa", [
    ("obter", "ɔbˈteɾ"), ("ovelha", "ɔˈvɛʎɐ"), ("opinião", "ɔpiniˈɐ̃w̃"),
    ("obrigado", "ɔbɾiˈɡadu"), ("oceano", "ɔsɨˈɐnu"), ("ocidental", "ɔsidẽˈtaɫ"),
    ("omitir", "ɔmiˈtiɾ"), ("oração", "ɔɾɐˈsɐ̃w̃"), ("objecto", "ɔbˈʒɛktu"),
])
def test_unstressed_initial_o_is_open(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word", ["obter", "ovelha", "opinião", "oceano"])
def test_lattice_ranks_open_then_u_then_close(word):
    assert _first_slot(word) == ["ɔ", "u", "o"]


@pytest.mark.parametrize("word, ipa, slot", [
    ("olho", "ˈoʎu", ["o", "ɔ", "u"]), ("ostra", "ˈoʃtɾɐ", ["o", "ɔ", "u"]),
    ("olhos", "ˈɔʎuʃ", ["ɔ", "ɔ", "u"]),
])
def test_stressed_initial_o_keeps_the_row_and_the_lists(word, ipa, slot):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _first_slot(word) == slot


@pytest.mark.parametrize("word, ipa", [
    ("ondular", "õduˈlaɾ"), ("ombreira", "õˈbɾejɾɐ"), ("ontologia", "õtuluˈʒiɐ"),
])
def test_initial_o_before_a_coda_nasal_stays_nasal(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _first_slot(word) == ["o", "o", "o"]


@pytest.mark.parametrize("word, ipa", [("pomar", "puˈmaɾ"), ("comer", "kuˈmeɾ"), ("votar", "vuˈtaɾ")])
def test_medial_unstressed_o_keeps_its_lattice(word, ipa):
    g2p = G2P("pt-PT")
    assert g2p.transcribe(word) == ipa
    slot = next(s for s in g2p.ipa_lattice(word) if s.grapheme == "o")
    assert [c.ipa for c in slot.candidates] == ["u", "o", "ɔ"]


@pytest.mark.parametrize("word, ipa", [("o", "u"), ("os", "uʃ")])
def test_article_keeps_the_reduced_vowel(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [("ouvir", "oˈviɾ"), ("oito", "ˈojtu"), ("hóspede", "ˈɔʃpɨdɨ")])
def test_other_graphemes_stay_out(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("hospital", "ɔʃpiˈtaɫ"), ("hotel", "ɔˈtɛɫ"), ("hostil", "ɔʃˈtiɫ"), ("horizonte", "ɔɾiˈzõtɨ"),
    ("hortelã", "ɔɾtɨˈlɐ̃"), ("horrível", "ɔˈʁivɨɫ"),
])
def test_unstressed_o_after_initial_h_is_open(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _first_slot(word) == ["ɔ", "u", "o"]


@pytest.mark.parametrize("word, ipa", [("hoje", "ˈɔʒɨ"), ("homem", "ˈɔmɐ̃j̃"), ("hora", "ˈɔɾɐ")])
def test_stressed_o_after_initial_h_keeps_its_lattice(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _first_slot(word) == ["ɔ", "o", "u"]


@pytest.mark.parametrize("word, ipa", [("honrar", "õˈɾaɾ"), ("hombridade", "õbɾiˈdadɨ")])
def test_o_after_initial_h_before_a_coda_nasal_stays_nasal(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _first_slot(word) == ["o", "o", "o"]


def test_o_after_a_medial_h_keeps_its_lattice():
    assert G2P("pt-PT").transcribe("dehoniano") == "dɨuniˈɐnu"
    assert [c.ipa for c in G2P("pt-PT").ipa_lattice("dehoniano")[3].candidates] == ["u", "o", "ɔ"]


def test_second_element_of_a_compound_takes_the_open_vowel():
    assert G2P("pt-PT").transcribe_word("água-oxigenada") == "ˌaɡwɐɔʃiʒɨˈnadɐ"


def test_sentence():
    assert G2P("pt-PT").transcribe("obter a opinião do oceano") == "ɔbˈteɾ ɐ ɔpiniˈɐ̃w̃ du ɔsɨˈɐnu"


def test_word_initial_value_of_the_o_row_is_unchanged():
    row = get("pt-PT").positional_graphemes["o"]
    assert list(row["word_initial"]) == ["o", "ɔ"]


@pytest.mark.parametrize("lang", EUROPE)
def test_european_specs_take_the_default(lang):
    assert G2P(lang).transcribe("obter").startswith("ɔb")
    assert _first_slot("obter", lang) == ["ɔ", "u", "o"]
    assert _first_slot("hospital", lang) == ["ɔ", "u", "o"]


@pytest.mark.parametrize("lang, ipa", NO_SOURCE.items())
def test_specs_with_no_source_keep_their_value(lang, ipa):
    assert G2P(lang).transcribe("ovelha") == ipa
    assert not G2P(lang).transcribe("hospital").startswith("ɔ")


@pytest.mark.parametrize("lang", [*NO_SOURCE, *CREOLES])
@pytest.mark.parametrize("rule_id", RULE_IDS)
def test_disabled_specs_have_a_note(lang, rule_id):
    rule = next(r for r in get(lang).allophone_rules if r.id == rule_id)
    assert not rule.phonemes
    assert rule.notes.startswith("DISABLED for ")


@pytest.mark.parametrize("lang", ["pt-BR", "pt-BR-x-sp", "pt-UY", "pt-PT-x-medieval"])
def test_specs_outside_the_lane_have_no_rule(lang):
    assert not any(r.id in RULE_IDS for r in get(lang).allophone_rules)
