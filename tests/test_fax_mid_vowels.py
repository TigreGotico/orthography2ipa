"""A Fala (fax) has no open-mid vowels.

Costas González (1992: 86), § 2 "Inexistencia de oposición ɛ/e, ɔ/o": "nestas
non existen os fonemas /ɛ/, /ɔ/". Page 87 gives the tonic system /i e a o u/.
Carrasco González (2024: 104) says the written accent of ⟨é ó⟩ marks the
stressed mid vowels [e] [o]; page 100 gives véllu, pórta and léiti.
Its accentuation rule 1.2 (p. 104) reads an accented ⟨ei oi⟩ as a diphthong.
"""
import pytest

from orthography2ipa import G2P, registry


@pytest.fixture(scope="module")
def fax():
    return G2P("fax")


@pytest.mark.parametrize("word, ipa", [
    # Carrasco González (2024: 100) examples of the accented tonic e and o.
    ("véllu", "beʎu"),
    ("pórta", "poɾta"),
    ("café", "kafe"),
])
def test_accented_mid_vowel_is_close_mid(fax, word, ipa):
    assert fax.transcribe(word) == ipa


@pytest.mark.xfail(strict=True, reason="⟨éi⟩ reads as a hiatus [ei]; "
                   "Carrasco González (2024: 104, Acentuación 1.2) reads "
                   "an accented ⟨ei oi⟩ as a diphthong", raises=AssertionError)
def test_accented_ei_is_a_diphthong(fax):
    assert fax.transcribe("léiti") == "lejti"


def test_letter_table_writes_no_open_mid_vowel():
    # Costas González (1992: 86): no /ɛ ɔ/ phonemes.
    spec = registry.get("fax")
    readings = {letter: spec.graphemes[letter] for letter in ("e", "é", "o", "ó")}
    assert readings == {"e": ["e"], "é": ["e"], "o": ["o"], "ó": ["o"]}


def test_inherited_open_o_rules_are_switched_off():
    # gl-ES writes [ɔ] with GL_OPEN_O and rewrites it with
    # GL_RAISE_O_BEFORE_NASAL; fax has no /ɔ/ for either to act on.
    spec = registry.get("fax")
    rules = {rule.id: rule for rule in spec.allophone_rules}
    assert rules["GL_OPEN_O"].phonemes == ()
    assert rules["GL_RAISE_O_BEFORE_NASAL"].phonemes == ()


def test_no_live_allophone_rule_writes_an_open_mid_vowel():
    spec = registry.get("fax")
    surfaces = {rule.surface for rule in spec.allophone_rules if rule.phonemes}
    assert not {s for s in surfaces if "ɛ" in s or "ɔ" in s}
