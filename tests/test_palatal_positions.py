"""Palatal-consonant GraphemePosition + allophone-class tests.

Covers the consonant-side mirror of the vowel-class positions:

- the :func:`orthography2ipa.vowels.is_palatal_consonant` predicate
  (``ʎ ɲ ʃ ʒ tʃ dʒ j`` yes; ``s t k`` and vowels no);
- the engine's use of ``BEFORE_PALATAL`` / ``AFTER_PALATAL`` positions,
  firing only when the neighbouring grapheme's IPA is a palatal;
- the resolution order exact-letter position > palatal class position;
- the ``"palatal"`` ``AllophoneRule`` neighbour class.

The worked example (European-Portuguese-style stressed ⟨e⟩ → [ɐ] before ⟨lh⟩
but plain [e] before ⟨t⟩) is exercised in
``test_before_palatal_fires_only_before_palatal_grapheme``.
"""
from dataclasses import replace

import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.registry import get
from orthography2ipa.types import AllophoneRule, GraphemePosition, LanguageSpec
from orthography2ipa.allophony import compile_allophone_rescorer
from orthography2ipa.vowels import is_palatal_consonant


# ═══════════════════════════════════════════════════════════════════════════
# Predicate
# ═══════════════════════════════════════════════════════════════════════════

PALATAL = ["ʎ", "ɲ", "ʃ", "ʒ", "j", "tʃ", "dʒ", "t͡ʃ", "d͡ʒ",
           "c", "ɟ", "ç", "ʝ", "ɕ", "ʑ", "tɕ", "dʑ"]
NON_PALATAL = ["s", "t", "k", "d", "z", "n", "l", "r", "p", "b", "ɡ",
               "a", "e", "i", "o", "u", "ə", "ɐ"]


@pytest.mark.parametrize("ipa", PALATAL)
def test_palatal_consonants_are_palatal(ipa):
    assert is_palatal_consonant(ipa)


@pytest.mark.parametrize("ipa", NON_PALATAL)
def test_non_palatal_segments_are_not(ipa):
    assert not is_palatal_consonant(ipa)


def test_affricate_tie_bar_equivalence():
    # Tie-bar and bare two-symbol forms classify identically.
    assert is_palatal_consonant("tʃ") == is_palatal_consonant("t͡ʃ") is True
    assert is_palatal_consonant("dʒ") == is_palatal_consonant("d͡ʒ") is True


def test_leading_segment_with_length_or_diacritic():
    # A following length mark / palatalisation diacritic does not change the head.
    assert is_palatal_consonant("ʃː")
    assert is_palatal_consonant("ɲʲ")


def test_empty_string_is_not_palatal():
    assert not is_palatal_consonant("")


def test_coronal_stop_alone_is_not_palatal():
    # Only the affricate PREFIX 'tʃ' is palatal; a bare 't' is not.
    assert not is_palatal_consonant("t")
    assert not is_palatal_consonant("d")


# ═══════════════════════════════════════════════════════════════════════════
# Engine: BEFORE_PALATAL / AFTER_PALATAL positions
# ═══════════════════════════════════════════════════════════════════════════

def _engine_with_spec(spec) -> G2P:
    """Build a G2P whose spec (and tokenizer) is the synthetic *spec*."""
    engine = G2P(spec.code)
    engine.spec = spec
    engine._tokenizer = PhonetokTokenizer(spec)
    return engine


def _palatal_spec(positional, *, extra_graphemes=None):
    """Minimal spec with the palatal digraphs ⟨lh⟩→ʎ, ⟨nh⟩→ɲ, ⟨ch⟩→ʃ and a
    plain ⟨t⟩→t, built on fr-FR (no stress rules) so the test isolates
    positional resolution."""
    base = get("fr-FR")
    graphemes = {
        "e": ["e"], "a": ["a"], "i": ["i"], "o": ["o"], "u": ["u"],
        "t": ["t"], "l": ["l"], "n": ["n"], "s": ["s"],
        "lh": ["ʎ"], "nh": ["ɲ"], "ch": ["ʃ"],
    }
    if extra_graphemes:
        graphemes.update(extra_graphemes)
    return replace(
        base,
        graphemes=graphemes,
        allophones={},
        positional_graphemes=positional,
        stress=None,
        word_exceptions=None,
        sandhi_rules=(),
    )


def test_before_palatal_fires_only_before_palatal_grapheme():
    # The worked example: stressed ⟨e⟩ → [ɐ] before a palatal (⟨lh⟩), plain
    # [e] before a non-palatal (⟨t⟩).
    spec = _palatal_spec({"e": {GraphemePosition.BEFORE_PALATAL: ["ɐ"]}})
    engine = _engine_with_spec(spec)

    assert engine.transcribe_word("elh") == "ɐʎ"   # e before ⟨lh⟩ (ʎ) → ɐ
    assert engine.transcribe_word("enh") == "ɐɲ"   # e before ⟨nh⟩ (ɲ) → ɐ
    assert engine.transcribe_word("ech") == "ɐʃ"   # e before ⟨ch⟩ (ʃ) → ɐ
    # Non-palatal following grapheme: default /e/.
    assert engine.transcribe_word("et") == "et"
    assert engine.transcribe_word("es") == "es"


def test_after_palatal_fires_only_after_palatal_grapheme():
    spec = _palatal_spec({"e": {GraphemePosition.AFTER_PALATAL: ["ɐ"]}})
    engine = _engine_with_spec(spec)

    assert engine.transcribe_word("lhe") == "ʎɐ"   # e after ⟨lh⟩ (ʎ) → ɐ
    assert engine.transcribe_word("che") == "ʃɐ"   # e after ⟨ch⟩ (ʃ) → ɐ
    # Non-palatal preceding grapheme: default /e/.
    assert engine.transcribe_word("te") == "te"
    assert engine.transcribe_word("le") == "le"


def test_after_palatal_fires_after_vowel_letter_glide():
    # A vowel *letter* realised as the palatal glide /j/ (⟨i⟩→/j/) is palatal
    # too, so AFTER_PALATAL must fire for it — mirroring BEFORE_PALATAL.
    spec = _palatal_spec(
        {"e": {GraphemePosition.AFTER_PALATAL: ["ɐ"]}},
        extra_graphemes={"i": ["j"]},
    )
    engine = _engine_with_spec(spec)
    assert engine.transcribe_word("ie") == "jɐ"   # e after ⟨i⟩→/j/ (palatal)
    assert engine.transcribe_word("ae") == "ae"   # e after ⟨a⟩ (non-palatal)


def test_before_palatal_inert_on_tokenizer_path():
    # Standalone tokenizer resolves positions too (no stress needed here).
    spec = _palatal_spec({"e": {GraphemePosition.BEFORE_PALATAL: ["ɐ"]}})
    tok = PhonetokTokenizer(spec)
    assert tok.ipa_best("elh") == "ɐʎ"
    assert tok.ipa_best("et") == "et"


# ═══════════════════════════════════════════════════════════════════════════
# Precedence: exact-letter position beats palatal class position
# ═══════════════════════════════════════════════════════════════════════════

def test_exact_before_i_beats_before_palatal():
    # ⟨i⟩ mapped to the palatal glide /j/ is BOTH the exact letter ⟨i⟩ and a
    # palatal, so a grapheme before it triggers BEFORE_I *and* BEFORE_PALATAL.
    # The exact-letter position must win.
    spec = _palatal_spec(
        {"e": {
            GraphemePosition.BEFORE_I: ["ɛ"],
            GraphemePosition.BEFORE_PALATAL: ["ɐ"],
        }},
        extra_graphemes={"i": ["j"]},
    )
    engine = _engine_with_spec(spec)
    # next ⟨i⟩→/j/ is palatal AND the exact letter i → exact BEFORE_I wins.
    assert engine.transcribe_word("ei") == "ɛj"
    # next ⟨lh⟩ is palatal but not letter i → palatal class fires.
    assert engine.transcribe_word("elh") == "ɐʎ"


# ═══════════════════════════════════════════════════════════════════════════
# AllophoneRule "palatal" neighbour class
# ═══════════════════════════════════════════════════════════════════════════

def _spec(graphemes, rules=(), *, code="xx-test"):
    return LanguageSpec(
        code=code, name="Test", family="Test", script="Latin",
        graphemes=graphemes, allophones={}, allophone_rules=tuple(rules),
    )


def _tok_best(spec, word):
    tok = PhonetokTokenizer(spec)
    resc = compile_allophone_rescorer(spec.allophone_rules)
    return tok.ipa_best(word, rescorer=resc)


def test_followed_by_palatal_class_fires_only_before_palatal():
    # /e/ → [ɐ] when the NEXT grapheme is a palatal consonant.
    rule = AllophoneRule(id="RED_E_PAL", phonemes=("e",), surface="ɐ",
                         followed_by="palatal")
    spec = _spec({"e": ["e"], "t": ["t"], "lh": ["ʎ"], "ch": ["ʃ"]}, (rule,))
    assert _tok_best(spec, "elh") == "ɐʎ"   # before ⟨lh⟩ (ʎ) → ɐ
    assert _tok_best(spec, "ech") == "ɐʃ"   # before ⟨ch⟩ (ʃ) → ɐ
    assert _tok_best(spec, "et") == "et"     # before ⟨t⟩ → unchanged


def test_preceded_by_palatal_class():
    rule = AllophoneRule(id="RED_E_PAL2", phonemes=("e",), surface="ɐ",
                         preceded_by="palatal")
    spec = _spec({"e": ["e"], "t": ["t"], "lh": ["ʎ"]}, (rule,))
    assert _tok_best(spec, "lhe") == "ʎɐ"   # after ⟨lh⟩ (ʎ) → ɐ
    assert _tok_best(spec, "te") == "te"     # after ⟨t⟩ → unchanged


def test_palatal_class_accepted_by_allophone_rule_validation():
    # "palatal" is a valid preceded_by/followed_by class (no ValueError).
    AllophoneRule(id="OK", phonemes=("e",), surface="ɐ", followed_by="palatal")
    AllophoneRule(id="OK2", phonemes=("e",), surface="ɐ", preceded_by="palatal")
    with pytest.raises(ValueError):
        AllophoneRule(id="BAD", phonemes=("e",), surface="ɐ",
                      followed_by="not_a_class")
