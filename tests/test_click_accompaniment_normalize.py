"""Superscript vs full-letter click-accompaniment notation is a
transcription-convention choice, not a phonemic contrast (IPA Chart 2015,
superscript-modifier convention; Ladefoged & Maddieson 1996, ch.8 "Clicks",
pp.246-260). ``benchmark.normalize`` must fold the two conventions together
for the five click letters (ǀ ǁ ǃ ǂ ʘ) the same way it already folds tie
bars, WITHOUT touching superscripts that are not adjacent to a click letter
(e.g. prenasalized-stop notation ᵑg) and WITHOUT merging different click
TYPES or clicks with non-click consonants.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "bm", Path(__file__).parent.parent / "scripts" / "benchmark.py")
bm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bm)
normalize = bm.normalize


def _n(s: str, broad: bool = False) -> str:
    return normalize(s, strip_stress=True, broad=broad)


# ── MUST fold: same segment, different notation ──────────────────────────

def test_superscript_velar_accompaniment_folds_to_full_letter():
    assert _n("ᵏǀ") == _n("kǀ")


def test_superscript_nasal_accompaniment_folds_to_full_letter():
    assert _n("ᵑǃ") == _n("ŋǃ")


def test_tie_barred_accompaniment_already_matches_superscript():
    # Tie bars are already stripped unconditionally, so this pair must also
    # match once the superscript fold is in place.
    assert _n("ᵑǀ") == _n("ŋ͜ǀ")


def test_superscript_accompaniment_folds_with_trailing_glottal():
    assert _n("ᵑǀʔ") == _n("ŋǀʔ")


def test_ligature_lateral_affricate_letter_folds():
    # U+1DF06 (𝼆) is NOT a click letter: it is a ligature-style shorthand
    # for the voiceless palatal lateral fricative ʎ̥˔ (Unicode 13.0, 2021).
    # The Hadza wikipron alphabet-table rows write the "tl" lateral
    # affricate as bare 𝼆; the corresponding word rows write the SAME
    # segment tie-barred as c͜ʎ̥˔.
    assert _n("𝼆") == _n("ʎ̥˔")
    assert _n("c͜𝼆") == _n("cʎ̥˔")


def test_ligature_lateral_affricate_never_merges_with_lateral_click():
    # 𝼆 must never fold to ǁ (the lateral CLICK) -- that is a different
    # segment (a fricative, not a click).
    assert _n("𝼆") != _n("ǁ")


def test_full_word_notational_variants_match():
    # Hadza gold's two attested conventions for the same alphabet-table
    # entries (see data/hts.json / scripts/benchmark.py hts comment).
    assert _n("ᵏǀ") == _n("k͜ǀ")
    assert _n("ᵑǀʔ") == _n("ŋ͜ǀʔ")


def test_combining_mark_on_modifier_still_folds():
    # A combining mark (e.g. a combining ring below for voicelessness, as
    # in ktz gold's ᵑ̊) rides along with the modifier letter it decorates
    # and must not block the fold.
    assert _n("ᵑ̊ǃ") == _n("ŋ̊ǃ")


def test_space_separated_accompaniment_still_folds():
    # Some gold sets (e.g. ngh) space-separate phonemes, putting the
    # modifier and its click letter on opposite sides of a space. The fold
    # must survive the later whitespace-join.
    assert _n("ᵑ ǂ") == _n("ŋǂ")


# ── MUST NOT fold: different segments ─────────────────────────────────────

def test_different_click_types_stay_distinct():
    assert _n("ǀ") != _n("ǃ")
    assert _n("kǀ") != _n("kǃ")


def test_bilabial_click_never_merges_with_dental_click():
    assert _n("ʘ") != _n("ǀ")
    assert _n("ᵏʘ") != _n("ᵏǀ")


def test_click_vs_plain_velar_stays_distinct():
    assert _n("kǀ") != _n("k")
    assert _n("ǀ") != _n("k")


def test_superscript_before_non_click_is_not_folded():
    # ᵏ/ᵑ before a non-click letter is unrelated notation (e.g. a
    # prenasalized-stop marker like ᵑg) and must be left alone.
    assert _n("ᵑg") == "ᵑɡ"
    assert _n("ᵏt") == "ᵏt"


def test_superscript_accompaniment_distinct_from_bare_click():
    assert _n("ᵏǀ") != _n("ǀ")
