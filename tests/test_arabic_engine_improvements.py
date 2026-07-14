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
    assert ar.transcribe_word("ﻻ") == "ˈlaː"


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
    assert ar.transcribe_word("عَمَّ") == "ˈʕamma"


def test_gemination_glide_yaa(ar):
    # عُيِّنَ → [ʕujjina]: the glide ي geminates like any other consonant.
    assert ar.transcribe_word("عُيِّنَ") == "ˈʕujjina"


def test_gemination_glide_waw(ar):
    # قَوَّاس → [qawwaːs]: geminate و before the long-ā digraph. The geminate
    # splits across the syllable boundary (qaw-waːs), so the mark goes before
    # the SECOND half of it.
    assert ar.transcribe_word("قَوَّاس") == "qawˈwaːs"


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
    assert ar.transcribe_word("يَ") == "ˈja"


def test_waw_fatha_is_onset_not_diphthong(ar):
    # وَ is the onset /wa/, not the diphthong [aw].
    assert ar.transcribe_word("وَ") == "ˈwa"


def test_yaw_word_onset(ar):
    # يَوم → [jawm]: initial يَ is onset /ja/, medial و is coda /w/.
    assert ar.transcribe_word("يَوم") == "ˈjawm"


def test_hamza_alif_no_baked_vowel(ar):
    # أَكَلَ → [ʔakala]: أ contributes a bare /ʔ/, its vowel comes from the
    # explicit fatha — no doubled a from a baked ʔa.
    assert ar.transcribe_word("أَكَلَ") == "ˈʔakala"


def test_hamza_kasra_no_doubling_on_iman(ar):
    # إِيْمَان → [ʔiːmaːn]: إ is bare /ʔ/ + the long ī from ـِي, never the
    # ʔiiː double the old baked-vowel mapping produced. Stress falls on the
    # superheavy final -maːn; the mark precedes the syllable, never landing
    # inside the long vowel of the previous one (*ʔiˈːmaːn is not IPA).
    assert ar.transcribe_word("إِيْمَان") == "ʔiːˈmaːn"


def test_hamza_bare_fallback_vowel_undiacritized(ar):
    # With no following harakat (out-of-contract undiacritized input) أ/إ
    # fall back to their default hamza+vowel reading so bare skeletons still
    # carry a vowel (this is what keeps the WikiPron gold PER from
    # regressing).
    assert ar.transcribe_word("أخ") == "ˈʔax"
    assert ar.transcribe_word("إسلام") == "ʔisˈlaːm"  # ʔis-laːm, onset limit 1


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
    assert ar.transcribe_word("مَدْرَسَة") == "ˈmadrasa"


# ─── 4. Fatḥa + standalone alif-maksūra ⟨ـَى⟩ merges to a single [aː] ───────


def test_fatha_alif_maksura_merges_to_single_long_a(ar):
    # حَتَّى → [ħattaː]: word-final fatḥa + alif maksūra ⟨ـَى⟩ is one long /aː/,
    # exactly like fatḥa + alif ⟨ـَا⟩ — not the fatḥa's /a/ followed by a
    # second /aː/ from ى (the old ħattaaː). Ryding 2005, "Phonology and
    # script", long vowels spelled with the matres (pp. 25–27); Wright 1896
    # Vol. I §5, alif maqṣūra as a spelling of final /aː/.
    assert ar.transcribe_word("حَتَّى") == "ˈħattaː"


def test_fatha_alif_maksura_ramaa(ar):
    # رَمَى → [ramaː]: same fatḥa + alif-maksūra merge, no emphatic context so
    # the vowel stays plain /aː/.
    assert ar.transcribe_word("رَمَى") == "ˈramaː"


# ─── 5. Word-final glide after a coda consonant (sukūn) stays a glide ───────


def test_word_final_yaa_after_sukun_stays_glide(ar):
    # رَمْي → [ramj]: word-final ي after a sukūn-bearing coda consonant ⟨ـْي⟩ is
    # the glide /j/, NOT a long /iː/ — a long vowel would be written with the
    # homorganic kasra (ـِي). Wright 1896 Vol. I §4 (a quiescent/coda
    # consonant carries no vowel); Ryding 2005 pp. 25–27, 29–30.
    assert ar.transcribe_word("رَمْي") == "ˈramj"


def test_word_final_waw_after_sukun_stays_glide(ar):
    # ظَبْي parallels رَمْي for ي; the ⟨ـْو⟩ coda glide is /w/ (here shown on a
    # word whose emphatic ظ /ðˤ/ backs the /a/ to [ɑ] — pre-existing, and
    # orthogonal to the glide fix): the tail must be /j/, never /iː/.
    out = ar.transcribe_word("ظَبْي")
    assert out.endswith("j")
    assert not out.endswith("iː")


def test_sukun_glide_medial_is_onset_glide(ar):
    # دُنْيَا → [dunjaː]: the same ⟨ـْي⟩ coda→glide rule word-medially yields the
    # /j/ onset of the following syllable, not a spurious long vowel.
    assert ar.transcribe_word("دُنْيَا") == "ˈdunjaː"


def test_diacritized_glide_diphthong_unaffected(ar):
    # بَيْت → [bajt]: ⟨يْ⟩ (ya THEN sukūn, i.e. the /j/ offglide of a diphthong)
    # is untouched by the ⟨ـْي⟩ (sukūn THEN ya) coda-glide digraph.
    assert ar.transcribe_word("بَيْت") == "ˈbajt"


def test_undiacritized_final_glide_keeps_long_fallback(ar):
    # في (out-of-contract undiacritized skeleton, no sukūn) keeps the
    # graceful word-final long-vowel fallback [fiː]: the coda-glide guard is
    # keyed on an explicit sukūn, so it does not disturb bare skeletons.
    assert ar.transcribe_word("في") == "ˈfiː"
