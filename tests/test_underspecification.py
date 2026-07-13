"""An abjad does not write its vowels — say so, instead of guessing silently.

The engine must produce *something* for ⟨كتب⟩, so it falls back on a default
reading. That is the only sensible behaviour and it is also a guess dressed as
an answer: the caller gets a confident IPA string with no signal that its vowels
were invented. These tests pin the honesty layer that makes the silence visible.

They assert nothing about *what* the transcription is — this changes no
transcription. Restoring the marks is a statistical, morphosyntactic problem
that belongs to a diacritizer, not to a grapheme table.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.underspecification import (
    is_underdetermined, mark_density, underdetermined_positions,
)

AR = get("ar")


# ─── a bare skeleton is a guess ─────────────────────────────────────────

@pytest.mark.parametrize("word", ["كتب", "كتاب", "مدرسة", "قهوة"])
def test_undiacritized_is_underdetermined(word):
    """⟨كتب⟩ is kataba / kutiba / kutub / kattaba — the letters say none of it."""
    assert is_underdetermined(word, AR)
    assert mark_density(word, AR) < 1.0


# ─── a diacritized word is not ──────────────────────────────────────────

@pytest.mark.parametrize("word", ["كَتَبَ", "كِتَاب", "مَدْرَسَة", "قَهْوَة"])
def test_diacritized_is_fully_determined(word):
    """This is the engine's input contract, so it must read as determined."""
    assert not is_underdetermined(word, AR)
    assert mark_density(word, AR) == 1.0
    assert underdetermined_positions(word, AR) == ()


def test_a_mater_lectionis_needs_no_mark():
    """⟨ا⟩ after a fatḥa is the long vowel that fatḥa opened, not a bare consonant.

    The mark *before* it licenses it. Requiring a mark of its own would report
    كِتَاب — a correctly and fully written word — as a guess.
    """
    assert underdetermined_positions("كِتَاب", AR) == ()


def test_a_word_final_letter_needs_no_mark():
    """In the pausal form that is actually spoken, a final consonant has no ending."""
    assert underdetermined_positions("مَدْرَسَة", AR) == ()


def test_partial_marking_is_a_spectrum():
    """Real text marks only the words it thinks are ambiguous."""
    assert 0.0 < mark_density("كتب", AR) < 1.0


# ─── scope: this is an abjad property ───────────────────────────────────

@pytest.mark.parametrize("code", ["en", "pt", "es"])
def test_an_orthography_that_writes_its_vowels_is_never_underdetermined(code):
    spec = get(code)
    assert not spec.optional_marks
    assert not is_underdetermined("hello", spec)
    assert mark_density("hello", spec) == 1.0


@pytest.mark.parametrize("code", [
    "ar", "arb", "ar-SA-x-najd", "ar-SA-x-hejaz", "ar-EG", "ar-x-gulf",
])
def test_every_arabic_spec_declares_its_omissible_marks(code):
    """script_type: abjad recorded that vowels are optional; this says which."""
    spec = get(code)
    assert spec.script_type.value == "abjad"
    assert "َ" in spec.optional_marks   # fatḥa
    assert "ُ" in spec.optional_marks   # ḍamma
    assert "ِ" in spec.optional_marks   # kasra
    assert "ْ" in spec.optional_marks   # sukūn
    assert "ّ" in spec.optional_marks   # shadda


def test_empty_input():
    assert underdetermined_positions("", AR) == ()
    assert mark_density("", AR) == 1.0
