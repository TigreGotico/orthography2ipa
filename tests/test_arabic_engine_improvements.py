"""Arabic engine-improvement regression tests.

Covers three fixes to the flagship ``ar`` engine surfaced by the arbtok
downstream migration:

1. Presentation-form / lam-alif ligature normalization (engine-level,
   Arabic-script-scoped) — a bare ﻻ must not yield an empty transcription.
2. Gemination (shadda ّ) modelled as a doubled/geminate consonant for ALL
   consonants including the glides ي/و (Wright 1896 Vol. I §7 rem., p. 15;
   Ryding 2005 §2.3, p. 15).
3. ``ar.json`` spec-data fixes: يَ/وَ onsets (not diphthongs), أ/إ bare
   glottal + harakat vowel (no baked doubling vowel), word-final ي/و long
   reading, ة pausal reading.

All transcriptions assume the documented fully-diacritized input contract
(see ``docs/languages/ar.md``); the WikiPron gold is undiacritized and is
scored separately by ``scripts/benchmark.py``.
"""
from __future__ import annotations

import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.phonetok import (
    _decompose_arabic_presentation_forms,
    _expand_arabic_gemination,
)

# Combining marks, named to keep the geminate unit test unambiguous.
_MEEM = "م"
_FATHA = "َ"
_SHADDA = "ّ"


@pytest.fixture(scope="module")
def ar():
    return G2P("ar")


# ─── 1. Presentation forms / ligatures ─────────────────────────────────────

def test_lam_alif_ligature_transcribes(ar):
    # ﻻ (U+FEFB, lam-alif isolated form) must decompose to ل + ا and
    # transcribe as [laː], never the empty string.
    assert ar.transcribe_word("ﻻ") == "laː"


def test_lam_alif_ligatures_all_forms():
    # All four lam-alif ligature codepoints decompose to lam + an alif form.
    for lig in ("ﻻ", "ﻷ", "ﻵ", "ﻹ"):
        out = _decompose_arabic_presentation_forms(lig)
        assert out != lig
        assert out[0] == "ل"  # lam


def test_presentation_form_letter_decomposes():
    # An Arabic Presentation Forms-B isolated letter (ﺏ U+FE8F, beh)
    # decomposes to its canonical letter ب (U+0628).
    assert _decompose_arabic_presentation_forms("ﺏ") == "ب"


def test_presentation_form_normalization_is_arabic_scoped():
    # A Latin ligature (ﬁ U+FB01) sits outside the Arabic presentation-form
    # ranges and must be left untouched (no global NFKC folding).
    assert _decompose_arabic_presentation_forms("ﬁ") == "ﬁ"


# ─── 2. Gemination (shadda) ────────────────────────────────────────────────

def test_gemination_plain_consonant(ar):
    # عَمَّ → [ʕamma]: the shadda-carrying mim geminates (doubles), it is not
    # a length mark stranded on the preceding vowel.
    assert ar.transcribe_word("عَمَّ") == "ʕamma"


def test_gemination_glide_yaa(ar):
    # عُيِّنَ → [ʕujjina]: the glide ي geminates like any other consonant.
    assert ar.transcribe_word("عُيِّنَ") == "ʕujjina"


def test_gemination_glide_waw(ar):
    # قَوَّاس → [qawwaːs]: geminate و before the long-ā digraph.
    assert ar.transcribe_word("قَوَّاس") == "qawwaːs"


def test_gemination_expander_doubles_consonant():
    # Unit-level: both mark orderings expand to the same doubled consonant
    # (meem + meem + fatha).
    expected = _MEEM + _MEEM + _FATHA
    # canonical order: consonant + shadda + harakat
    assert _expand_arabic_gemination(_MEEM + _SHADDA + _FATHA) == expected
    # equally-valid rendered order: consonant + harakat + shadda
    assert _expand_arabic_gemination(_MEEM + _FATHA + _SHADDA) == expected


# ─── 3. ar.json spec-data fixes ────────────────────────────────────────────

def test_yaa_fatha_is_onset_not_diphthong(ar):
    # يَ is the onset /ja/, not the diphthong [aj].
    assert ar.transcribe_word("يَ") == "ja"


def test_waw_fatha_is_onset_not_diphthong(ar):
    # وَ is the onset /wa/, not the diphthong [aw].
    assert ar.transcribe_word("وَ") == "wa"


def test_yaw_word_onset(ar):
    # يَوم → [jawm]: initial يَ is onset /ja/, medial و is coda /w/.
    assert ar.transcribe_word("يَوم") == "jawm"


def test_hamza_alif_no_baked_vowel(ar):
    # أَكَلَ → [ʔakala]: أ contributes a bare /ʔ/, its vowel comes from the
    # explicit fatha — no doubled a from a baked ʔa.
    assert ar.transcribe_word("أَكَلَ") == "ʔakala"


def test_hamza_kasra_no_doubling_on_iman(ar):
    # إِيْمَان → [ʔiːmaːn]: إ is bare /ʔ/ + the long ī from ـِي, never the
    # ʔiiː double the old baked-vowel mapping produced.
    assert ar.transcribe_word("إِيْمَان") == "ʔiːmaːn"


def test_hamza_bare_fallback_vowel_undiacritized(ar):
    # With no following harakat (out-of-contract undiacritized input) أ/إ
    # fall back to their default hamza+vowel reading so bare skeletons still
    # carry a vowel (this is what keeps the WikiPron gold PER from
    # regressing).
    assert ar.transcribe_word("أخ") == "ʔax"
    assert ar.transcribe_word("إسلام") == "ʔislaːm"


def test_word_final_yaa_is_long_vowel(ar):
    # يُصَلِّي → […iː]: word-final ي prefers the long-vowel reading and the
    # geminate ل doubles. (The [ɑ] is pre-existing emphatic backing after
    # /sˤ/.)
    out = ar.transcribe_word("يُصَلِّي")
    assert out.endswith("iː")
    assert "ll" in out


def test_ta_marbuta_pausal_no_double_vowel(ar):
    # مَدْرَسَة → [madrasa]: word-final ة after a harakat is the pausal /a/
    # already supplied by the preceding fatha — not a second a.
    assert ar.transcribe_word("مَدْرَسَة") == "madrasa"
