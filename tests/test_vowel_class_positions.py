"""Vowel-class GraphemePosition tests.

Covers the front/back orthographic vowel predicates in ``vowels`` and the
engine's use of ``BEFORE_FRONT_VOWEL`` / ``BEFORE_BACK_VOWEL`` /
``AFTER_FRONT_VOWEL`` / ``AFTER_BACK_VOWEL`` positions, including the
resolution order exact-letter position > class position > default.
"""
from dataclasses import replace

import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.registry import get
from orthography2ipa.types import GraphemePosition
from orthography2ipa.vowels import is_back_vowel, is_front_vowel


# ═══════════════════════════════════════════════════════════════════════════
# Predicates
# ═══════════════════════════════════════════════════════════════════════════

FRONT = list("eéèêëiíìîïy") + list("üöøœæ")
BACK = list("aáàâã") + list("oóòôõ") + list("uúùû")


@pytest.mark.parametrize("ch", FRONT)
def test_front_vowels_are_front(ch):
    assert is_front_vowel(ch)
    assert not is_back_vowel(ch)


@pytest.mark.parametrize("ch", BACK)
def test_back_vowels_are_back(ch):
    assert is_back_vowel(ch)
    assert not is_front_vowel(ch)


@pytest.mark.parametrize("ch", [c.upper() for c in FRONT])
def test_front_predicate_case_insensitive(ch):
    assert is_front_vowel(ch)


@pytest.mark.parametrize("ch", [c.upper() for c in BACK])
def test_back_predicate_case_insensitive(ch):
    assert is_back_vowel(ch)


def test_classes_are_disjoint():
    assert not (set(FRONT) & set(BACK))


def test_non_vowels_are_neither():
    for ch in "bcdfg kmnpqrstvwxz.- ":
        assert not is_front_vowel(ch)
        assert not is_back_vowel(ch)


def test_empty_string_is_neither():
    assert not is_front_vowel("")
    assert not is_back_vowel("")


# ═══════════════════════════════════════════════════════════════════════════
# Engine: a single BEFORE_FRONT_VOWEL rule drives c-softening
# ═══════════════════════════════════════════════════════════════════════════

def _engine_with_spec(spec) -> G2P:
    """Build a G2P whose spec (and tokenizer) is the synthetic *spec*."""
    engine = G2P(spec.code)
    engine.spec = spec
    engine._tokenizer = PhonetokTokenizer(spec)
    return engine


def _romance_c_spec(positional):
    """A minimal spec: c→/k/ by default, plus the given positional block,
    built via dataclasses.replace on a real spec (fr-FR: no stress rules,
    keeping the test focused on positional resolution)."""
    base = get("fr-FR")
    graphemes = {
        "c": ["k"],
        "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
        "é": ["e"], "y": ["i"],
    }
    return replace(
        base,
        graphemes=graphemes,
        allophones={},
        positional_graphemes={"c": positional},
        stress=None,
        word_exceptions=None,
        sandhi_rules=(),
    )


def test_before_front_vowel_softens_c():
    spec = _romance_c_spec({GraphemePosition.BEFORE_FRONT_VOWEL: ["s"]})
    engine = _engine_with_spec(spec)

    # Front vowels (incl. accented é and y) → soft /s/
    assert engine.transcribe_word("ce") == "se"
    assert engine.transcribe_word("ci") == "si"
    assert engine.transcribe_word("cé") == "se"
    assert engine.transcribe_word("cy") == "si"

    # Back vowels → default hard /k/
    assert engine.transcribe_word("ca") == "ka"
    assert engine.transcribe_word("co") == "ko"
    assert engine.transcribe_word("cu") == "ku"


def test_before_back_vowel_class_position():
    spec = _romance_c_spec({GraphemePosition.BEFORE_BACK_VOWEL: ["ɡ"]})
    engine = _engine_with_spec(spec)

    # Back vowels hit the class rule
    assert engine.transcribe_word("ca") == "ɡa"
    assert engine.transcribe_word("co") == "ɡo"
    # Front vowels fall through to the default /k/
    assert engine.transcribe_word("ce") == "ke"
    assert engine.transcribe_word("ci") == "ki"


# ═══════════════════════════════════════════════════════════════════════════
# Precedence: exact-letter position beats class position
# ═══════════════════════════════════════════════════════════════════════════

def test_exact_before_e_beats_before_front_vowel():
    spec = _romance_c_spec({
        GraphemePosition.BEFORE_E: ["ʃ"],
        GraphemePosition.BEFORE_FRONT_VOWEL: ["s"],
    })
    engine = _engine_with_spec(spec)

    # Exact BEFORE_E wins for ⟨e⟩
    assert engine.transcribe_word("ce") == "ʃe"
    # Other front vowels still resolve via the class rule
    assert engine.transcribe_word("ci") == "si"
    assert engine.transcribe_word("cy") == "si"
    # Back vowels: default hard /k/
    assert engine.transcribe_word("ca") == "ka"


# ═══════════════════════════════════════════════════════════════════════════
# AFTER_ class positions
# ═══════════════════════════════════════════════════════════════════════════

def test_after_front_vowel_class_position():
    base = get("fr-FR")
    spec = replace(
        base,
        graphemes={
            "x": ["x"],
            "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
        },
        allophones={},
        positional_graphemes={"x": {
            GraphemePosition.AFTER_FRONT_VOWEL: ["ç"],
            GraphemePosition.AFTER_BACK_VOWEL: ["χ"],
        }},
        stress=None,
        word_exceptions=None,
        sandhi_rules=(),
    )
    engine = _engine_with_spec(spec)
    # German-ch-like: front vowel before → Ich-Laut, back vowel → Ach-Laut
    assert engine.transcribe_word("ex") == "eç"
    assert engine.transcribe_word("ix") == "iç"
    assert engine.transcribe_word("ax") == "aχ"
    assert engine.transcribe_word("ox") == "oχ"
