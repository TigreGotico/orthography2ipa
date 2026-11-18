"""A Fala (fax) has no open-mid vowels.

Costas González (1992: 86), § 2 "Inexistencia de oposición ɛ/e, ɔ/o": "nestas
non existen os fonemas /ɛ/, /ɔ/". Page 87 gives the tonic system /i e a o u/.
Carrasco González (2024: 104) says the written accent of ⟨é ó⟩ marks the
stressed mid vowels [e] [o]; page 100 gives véllu, pórta and léiti.
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
    ("léiti", "leiti"),
    ("café", "kafe"),
])
def test_accented_mid_vowel_is_close_mid(fax, word, ipa):
    assert fax.transcribe(word) == ipa


def test_letter_table_writes_no_open_mid_vowel():
    # Costas González (1992: 86): no /ɛ ɔ/ phonemes.
    spec = registry.get("fax")
    readings = {letter: spec.graphemes[letter] for letter in ("e", "é", "o", "ó")}
    assert readings == {"e": ["e"], "é": ["e"], "o": ["o"], "ó": ["o"]}


def test_no_allophone_rule_writes_an_open_mid_vowel():
    # Covers GL_OPEN_O, which fax inherits from gl-ES.
    spec = registry.get("fax")
    surfaces = {rule.id: rule.surface for rule in spec.allophone_rules}
    assert surfaces["GL_OPEN_O"] == "o"
    assert not {s for s in surfaces.values() if "ɛ" in s or "ɔ" in s}
