"""A pt-PT ⟨r⟩ after a coda consonant or a nasal vowel is the strong rhotic.

Pereira (2020: 11), citing Mateus e Andrade (2000: 15) and Mateus, Falé &
Freitas (2016: 135-136), lists the strong rhotic [ʀ] in a simple onset after a
coda consonant (melro [ˈmɛɫʀu], Israel [iʒʀɐˈɛɫ]) and after a nasal vowel
(genro [ˈʒẽʀu]), and the tap in a branching onset (prato [ˈpɾatu]). The other
readings are Infopédia's pt-PT rows. Infopédia writes the tap as [r] and the
strong rhotic as [ʀ]; the spec writes them [ɾ] and [ʁ], so the test maps the
symbols before it compares.
"""
from __future__ import annotations

import unicodedata

import pytest

from orthography2ipa import G2P, get

#: Word and its published reading, in the source's own symbols.
STRONG = {
    "honra": "ˈõʀɐ", "genro": "ˈʒẽʀu", "Israel": "iʒʀɐˈɛɫ", "melro": "ˈmɛɫʀu",
    "guelra": "ˈɡɛɫʀɐ", "bilro": "ˈbiɫʀu", "honrar": "õˈʀar", "palrar": "paɫˈʀar",
    "desrespeito": "dəʒʀəʃˈpɐjtu", "enredo": "ẽˈʀedu", "tenro": "ˈtẽʀu",
}
#: The tap of a branching onset and the tap after a diphthong stay.
TAP = {"prato": "ˈpratu", "abraço": "ɐˈbrasu", "feira": "ˈfɐjrɐ", "Europa": "ewˈrɔpɐ"}
#: Words whose whole published reading is in the spec's vowel notation.
WHOLE = ["honra", "genro", "Israel", "melro", "guelra", "bilro", "honrar", "palrar", "tenro"]

EUROPE = ["pt-PT"] + [f"pt-PT-x-{d}" for d in (
    "lisbon", "coimbra", "porto", "minho", "viana", "braga", "alfena", "tras-os-montes",
    "beira", "aveiro", "alentejo", "algarve", "acores", "madeira", "sao-miguel", "terceira")]
#: Specs whose strong rhotic is not [ʁ], or that have no source for the context.
DISABLED = ["pt-CV", "pt-GW", "pt-MZ", "pt-ST", "pt-TL", "ext-PT-x-barranco",
            "aoa", "cri", "idb", "kea", "mcm", "mzs", "pap", "pov", "pre", "vkp"]
#: Specs whose own map reads an ⟨r⟩ after a coda as [ʁ]. They keep the rule.
OWN_STRONG = ["pt-AO", "pt-MO"]


def _spec_symbols(reading: str) -> str:
    return reading.replace("ʀ", "ʁ").replace("r", "ɾ")


def _ipa(lang: str, word: str) -> str:
    return unicodedata.normalize("NFC", G2P(lang).transcribe_word(word))


def _rhotic_context(reading: str) -> tuple[str, str]:
    """The segment before the first rhotic of *reading*, and that rhotic.

    The segment is empty when the rhotic starts the word.
    """
    reading = unicodedata.normalize("NFC", reading)
    i = next(i for i, ch in enumerate(reading) if ch in "ɾʁ")
    return reading[:i].rstrip("ˈˌ")[-1:], reading[i]


@pytest.mark.parametrize("word", WHOLE)
def test_pt_pt_reads_the_whole_word(word):
    assert _ipa("pt-PT", word) == unicodedata.normalize("NFC", _spec_symbols(STRONG[word]))


@pytest.mark.parametrize("lang", EUROPE)
@pytest.mark.parametrize("word", [*STRONG, *TAP])
def test_european_specs_read_the_rhotic_after_the_coda(lang, word):
    expected = _rhotic_context(_spec_symbols({**STRONG, **TAP}[word]))
    got = _rhotic_context(_ipa(lang, word))
    if word in STRONG:
        assert got == expected, (lang, word, got)
    else:
        assert got[1] == expected[1], (lang, word, got)


@pytest.mark.parametrize("word", ["carro", "rato"])
def test_the_rule_writes_the_rhotic_of_rr_and_initial_r(word):
    assert _rhotic_context(_ipa("pt-PT", word))[1] == "ʁ"


@pytest.mark.parametrize("word", ["caro", "mar", "torta"])
def test_the_tap_between_vowels_and_in_the_coda_stays(word):
    assert _rhotic_context(_ipa("pt-PT", word))[1] == "ɾ"


@pytest.mark.parametrize("lang", EUROPE)
def test_the_nasal_m_takes_the_strong_rhotic(lang):
    # wikipron (Wiktionary) pt-PT: amrinona ɐ̃ʁiˈnɔnɐ
    assert _rhotic_context(_ipa(lang, "amrinona")) == ("̃", "ʁ"), lang


@pytest.mark.parametrize("lang", EUROPE)
@pytest.mark.parametrize("word", ["Christo", "Cochran", "chrétienne"])
def test_the_tap_after_ch_stays(lang, word):
    # ⟨ch⟩ spells [ʃ] but never closes a syllable, so the ⟨r⟩ after it is no
    # onset after a coda consonant
    assert _rhotic_context(_ipa(lang, word))[1] == "ɾ", (lang, word)


@pytest.mark.parametrize("lang", DISABLED)
def test_disabled_specs_have_a_note(lang):
    rule = next(r for r in get(lang).allophone_rules if r.id == "PT_STRONG_R_AFTER_CODA")
    assert not rule.phonemes
    assert rule.notes.startswith("DISABLED for ")


@pytest.mark.parametrize("lang", DISABLED)
@pytest.mark.parametrize("word", ["honra", "guelra", "Israel"])
def test_disabled_specs_write_no_uvular_rhotic(lang, word):
    assert "ʁ" not in _ipa(lang, word)


@pytest.mark.parametrize("lang", OWN_STRONG)
@pytest.mark.parametrize("word", ["honra", "guelra", "Israel"])
def test_specs_with_a_uvular_strong_rhotic_read_it_after_the_coda(lang, word):
    assert _rhotic_context(_ipa(lang, word))[1] == "ʁ"


@pytest.mark.parametrize("lang", ["pt-PT-x-medieval", "pt-UY", "pt-BR"])
def test_specs_outside_european_portuguese_have_no_rule(lang):
    assert not any(r.id == "PT_STRONG_R_AFTER_CODA" for r in get(lang).allophone_rules)
