"""An unstressed pt-PT ⟨e o⟩ before a stop letter and another consonant keeps a full vowel: [ɛ], [ɔ].

Cunha & Cintra (7th ed., p. 53) write "Também não se reduziram as vogais átonas
de cultismos, como o [a] de actor; o [ɛ] de director; o [ɔ] de adopção". On
p. 88 they write that Portugal kept the etymological consonant "sempre que se
seguem às vogais átonas a (aberta), e ou o (semiabertas), como forma de indicar
a abertura dessas vogais". The rules take the inference that a stop letter
before another consonant marks a learned word, whose unstressed ⟨e o⟩ do not
reduce. The reduced value stays in the lattice. ⟨a⟩, a stop before ⟨l r⟩, a
stressed vowel and a word-initial ⟨o⟩ keep their readings.

Readings without a page come from Infopédia rows.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get

RULE_IDS = ("PT_CODA_STOP_INITIAL_E_OPEN", "PT_CODA_STOP_INITIAL_E_CANDIDATE_E",
            "PT_CODA_STOP_INITIAL_E_CANDIDATE_I", "PT_CODA_STOP_INITIAL_E_CANDIDATE_REDUCED",
            "PT_CODA_STOP_E_OPEN", "PT_CODA_STOP_E_CANDIDATE_REDUCED", "PT_CODA_STOP_E_CANDIDATE_CLOSE",
            "PT_CODA_STOP_O_OPEN", "PT_CODA_STOP_O_CANDIDATE_REDUCED", "PT_CODA_STOP_O_CANDIDATE_CLOSE")

E, O, INITIAL_E = ["ɛ", "ɨ", "e"], ["ɔ", "u", "o"], ["ɛ", "e", "i", "ɨ"]

#: The European specs. They take the pt-PT default.
EUROPE = ["pt-PT"] + [f"pt-PT-x-{d}" for d in (
    "lisbon", "coimbra", "porto", "minho", "viana", "braga", "alfena", "tras-os-montes",
    "beira", "aveiro", "alentejo", "algarve", "acores", "madeira", "sao-miguel", "terceira")]
#: Specs that keep their own value. They disable the rules with a note.
NO_SOURCE = {"pt-AO": ("aspekˈtaveɫ", "nokˈtɐ̃bulʊ", "etˈnia"), "pt-CV": ("ɐspekˈtaveɫ", "nukˈtɐ̃bulu", "etˈniɐ"),
             "pt-GW": ("ɐspekˈtaveɫ", "nokˈtɐ̃bulu", "etˈniɐ"), "pt-MO": ("ɐʃpɨkˈtavɨɫ", "nukˈtɐ̃bulu", "etˈniɐ"),
             "pt-MZ": ("ɐspekˈtaveɫ", "nokˈtɐ̃bulu", "etˈniɐ"), "pt-ST": ("ɐspekˈtaveɫ", "nokˈtɐ̃bulu", "etˈniɐ"),
             "pt-TL": ("aspekˈtaveɫ", "nokˈtɐ̃bulo", "etˈnia"),
             "ext-PT-x-barranco": ("ɐhpɨkˈtabɨ", "nukˈtɐ̃bulu", "ˈetniɐ")}
CREOLES = ["aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]


def _before_stop(word: str, vowel: str, lang: str = "pt-PT") -> list:
    """The candidates of the first *vowel* slot that a stop slot and a consonant slot follow."""
    slots = G2P(lang).ipa_lattice(word)
    slot = next(s for s, n, c in zip(slots, slots[1:], slots[2:])
                if s.grapheme == vowel and n.grapheme in "pbtdcg" and c.grapheme not in "aeiouáéíóúlr")
    return [c.ipa for c in slot.candidates]


def _slot(word: str, index: int) -> list:
    """The candidates of slot *index* of *word*."""
    return [c.ipa for c in G2P("pt-PT").ipa_lattice(word)[index].candidates]


@pytest.mark.parametrize("word, vowel, value", [("director", "e", "ɛ"), ("adopção", "o", "ɔ")])
def test_the_vowels_the_source_names(word, vowel, value):
    assert _before_stop(word, vowel)[0] == value


@pytest.mark.parametrize("word, ipa", [
    ("aspectável", "ɐʃpɛkˈtavɛɫ"), ("septicemia", "sɛptisɨˈmiɐ"), ("hectare", "ɛkˈtaɾɨ"),
    ("epilepsia", "ipilɛpˈsiɐ"), ("bíceps", "ˈbisɛpʃ"), ("segmento", "sɛɡˈmẽtu"),
])
def test_e_before_a_stop_and_a_consonant_is_open(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _before_stop(word, "e") == E


@pytest.mark.parametrize("word, ipa", [
    ("noctâmbulo", "nɔkˈtɐ̃bulu"), ("cocção", "kɔkˈsɐ̃w̃"), ("dogmático", "dɔɡˈmatiku"),
    ("cognitivo", "kɔɡniˈtivu"), ("desobstruir", "dɨzɔbʃtɾuˈiɾ"),
])
def test_o_before_a_stop_and_a_consonant_is_open(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _before_stop(word, "o") == O


def test_loan_with_ck_takes_the_open_o():
    # wikipron gives cockney "k ɔ k n i". The rest of the loan stays outside the spelling rules.
    assert G2P("pt-PT").transcribe_word("cockney").replace("ˈ", "").startswith("kɔ")


@pytest.mark.parametrize("word, ipa", [("etnia", "ɛtˈniɐ"), ("ecdémico", "ɛkˈdɛmiku"), ("eczema", "ɛkˈzemɐ")])
def test_initial_e_before_a_stop_and_a_consonant_is_open(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _slot(word, 0) == INITIAL_E


@pytest.mark.parametrize("word, ipa, index, slot", [
    ("decrescer", "dɨkɾɨʃˈseɾ", 1, ["ɨ", "e", "ɛ"]),
    ("neblina", "nɨˈblinɐ", 1, ["ɨ", "e", "ɛ"]),
    ("reprovar", "ʁɨpɾuˈvaɾ", 1, ["ɨ", "e", "ɛ"]),
    ("cobrança", "kuˈbɾɐ̃sɐ", 1, ["u", "o", "ɔ"]),
    ("eclipse", "eˈklipsɨ", 0, ["e", "ɛ", "i", "ɨ"]),
])
def test_a_stop_before_l_or_r_stays_out(word, ipa, index, slot):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _slot(word, index) == slot


@pytest.mark.parametrize("word, ipa", [("captar", "kɐpˈtaɾ"), ("adaptar", "ɐdɐpˈtaɾ")])
def test_a_keeps_the_reduced_vowel(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _before_stop(word, "a") == ["ɐ", "a"]


@pytest.mark.parametrize("word, ipa", [("aspecto", "ɐʃˈpɛktu"), ("autóctone", "awˈtɔktunɨ")])
def test_stressed_vowel_keeps_its_reading(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [("optar", "ɔpˈtaɾ"), ("obter", "ɔbˈteɾ")])
def test_initial_o_keeps_the_initial_o_ranking(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa
    assert _slot(word, 0) == ["ɔ", "u", "o"]


def test_sentence():
    assert G2P("pt-PT").transcribe("o hectare de cocção") == "u ɛkˈtaɾɨ dɨ kɔkˈsɐ̃w̃"


@pytest.mark.parametrize("lang", EUROPE)
def test_european_specs_take_the_default(lang):
    assert _before_stop("aspectável", "e", lang) == E
    assert _before_stop("noctâmbulo", "o", lang) == O
    assert [c.ipa for c in G2P(lang).ipa_lattice("etnia")[0].candidates] == INITIAL_E


@pytest.mark.parametrize("lang", ["pt-PT-x-minho", "pt-PT-x-alfena", "pt-PT-x-beira", "pt-PT-x-aveiro"])
def test_apical_sibilant_after_the_stop(lang):
    assert G2P(lang).transcribe("colecção") == "kulɛkˈs̺ɐ̃w̃"


@pytest.mark.parametrize("lang, ipa", NO_SOURCE.items())
def test_specs_with_no_source_keep_their_value(lang, ipa):
    g2p = G2P(lang)
    assert (g2p.transcribe("aspectável"), g2p.transcribe("noctâmbulo"), g2p.transcribe("etnia")) == ipa


@pytest.mark.parametrize("lang", [*NO_SOURCE, *CREOLES])
@pytest.mark.parametrize("rule_id", RULE_IDS)
def test_disabled_specs_have_a_note(lang, rule_id):
    rule = next(r for r in get(lang).allophone_rules if r.id == rule_id)
    assert not rule.phonemes
    assert rule.notes.startswith("DISABLED for ")


@pytest.mark.parametrize("lang, ipa", [("pt-BR", "aspekiˈtavew"), ("pt-BR-x-sp", "aspekiˈtavew")])
def test_brazilian_specs_have_no_rule(lang, ipa):
    assert not any(r.id in RULE_IDS for r in get(lang).allophone_rules)
    assert G2P(lang).transcribe("aspectável") == ipa


@pytest.mark.parametrize("lang", ["pt-UY", "pt-PT-x-medieval"])
def test_specs_outside_the_lane_have_no_rule(lang):
    assert not any(r.id in RULE_IDS for r in get(lang).allophone_rules)
