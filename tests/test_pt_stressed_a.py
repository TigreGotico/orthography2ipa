"""A stressed pt-PT ⟨a⟩ is [a], and it is [ɐ] before an onset /m n ɲ/.

Cunha & Cintra (Nova Gramática do Português Contemporâneo, 7th ed., p. 49): "No
português europeu normal, [ɑ], quando tônico, também aparece, na maioria dos
casos, antes de consoante nasal, a exemplo de cama, cana e sanha". Their [ɑ] is
the spec's [ɐ]. The same page sets present amamos against preterite amámos.

Lao, Rodrigues & Brissos (2020, Revista da APL 7, p. 308) give the regions:
"o Noroeste possui [a] e [ã]", Trás-os-Montes, Beira Alta, Beira Litoral and
Estremadura "preferem [ɐ]", and "de resto, o que predomina é [ɐ̃]".

Readings without a page come from Infopédia rows.
"""
from __future__ import annotations

from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import G2P, get

RULE_ID = "PT_STRESSED_A_BEFORE_NASAL"
DATA = Path(orthography2ipa.__file__).parent / "data"

#: Specs that take the [ɐ] of the standard.
RAISED = ["pt-PT", "pt-PT-x-lisbon", "pt-PT-x-tras-os-montes", "pt-PT-x-beira",
          "pt-PT-x-coimbra", "pt-PT-x-aveiro"]
#: Northwest specs, where the source gives an open vowel.
NORTHWEST = ["pt-PT-x-minho", "pt-PT-x-braga", "pt-PT-x-viana", "pt-PT-x-porto",
             "pt-PT-x-alfena"]
#: Specs where the source gives the raised nasal vowel.
NASAL = ["pt-PT-x-alentejo", "pt-PT-x-algarve"]
#: Specs with no source for the rule. They disable it with a note.
NO_SOURCE = ["pt-AO", "pt-CV", "pt-GW", "pt-MZ", "pt-ST", "pt-TL", "ext-PT-x-barranco",
             "pt-MO", "pt-PT-x-acores", "pt-PT-x-madeira", "pt-PT-x-sao-miguel",
             "pt-PT-x-terceira"]
CREOLES = ["aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]


def _rule(lang: str):
    return next((r for r in get(lang).allophone_rules if r.id == RULE_ID), None)


@pytest.mark.parametrize("word, ipa", [
    ("ar", "ˈaɾ"), ("arte", "ˈaɾtɨ"), ("ato", "ˈatu"), ("água", "ˈaɡwɐ"),
    ("cama", "ˈkɐmɐ"), ("ramo", "ˈʁɐmu"), ("banho", "ˈbɐɲu"),
    ("ano", "ˈɐnu"), ("amo", "ˈɐmu"), ("ama", "ˈɐmɐ"), ("anho", "ˈɐɲu"),
])
@pytest.mark.parametrize("lang", ["pt-PT", "pt-PT-x-lisbon"])
def test_stressed_a(lang, word, ipa):
    assert G2P(lang).transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("falamos", "fɐˈlɐmuʃ"), ("falámos", "fɐˈlamuʃ"), ("amámos", "ɐˈmamuʃ"),
])
def test_written_a_acute_stays_open(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("amar", "ɐˈmaɾ"), ("abrir", "ɐˈbɾiɾ"), ("manhã", "mɐˈɲɐ̃"), ("a", "ɐ"), ("as", "ɐʃ"),
])
def test_unstressed_a_stays_reduced(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [("campo", "ˈkɐ̃pu"), ("ambos", "ˈɐ̃buʃ")])
def test_coda_nasal_keeps_its_nasal_vowel(word, ipa):
    assert G2P("pt-PT").transcribe(word) == ipa


@pytest.mark.parametrize("lang", RAISED)
def test_raised_specs(lang):
    assert G2P(lang).transcribe("cama") == "ˈkɐmɐ"


@pytest.mark.parametrize("lang", ["pt-CV", "pt-GW", "pt-MZ", "pt-ST", "pt-MO", "pt-PT-x-acores",
                                  "pt-PT-x-madeira", "pt-PT-x-sao-miguel"])
def test_specs_with_no_source_keep_open_a(lang):
    assert "ˈkamɐ" in G2P(lang).transcribe("cama")


@pytest.mark.parametrize("lang", NORTHWEST)
@pytest.mark.parametrize("word, ipa", [("cama", "ˈkamɐ"), ("ano", "ˈanu")])
def test_northwest_keeps_open_a(lang, word, ipa):
    assert G2P(lang).transcribe(word) == ipa


@pytest.mark.parametrize("lang", NASAL)
def test_south_gives_the_nasal_vowel(lang):
    assert G2P(lang).transcribe("cama") == "ˈkɐ̃mɐ"


@pytest.mark.parametrize("word, ipa", [("ramo", "ˈʁɔmu"), ("banho", "ˈbɔɲu"), ("gato", "ˈɡɔtu")])
def test_terceira_keeps_its_metaphony(word, ipa):
    # Mikołajczak (2014: 423): pato "[ˈpɔtu]", gato "[ˈɡɔtu]".
    assert G2P("pt-PT-x-terceira").transcribe(word) == ipa


def test_barranquenho_keeps_its_initial_a():
    assert G2P("ext-PT-x-barranco").transcribe("areia") == "ɐˈɾejɐ"


@pytest.mark.parametrize("lang", NORTHWEST + NO_SOURCE + CREOLES)
def test_disabled_specs_have_a_note(lang):
    rule = _rule(lang)
    assert rule is not None and not rule.phonemes
    assert rule.notes.startswith("DISABLED for ")


@pytest.mark.parametrize("lang", ["pt-BR", "pt-BR-x-sp", "pt-UY"])
def test_pt_br_lane_has_no_rule(lang):
    assert _rule(lang) is None


def test_no_other_spec_carries_the_rule():
    # A new child of pt-PT inherits the rule, so it fails here until it is
    # sorted into one of the lists above.
    carriers = {p.stem for p in DATA.glob("*.json") if _rule(p.stem)}
    assert carriers == set(RAISED + NORTHWEST + NASAL + NO_SOURCE + CREOLES)
