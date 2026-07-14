"""Quantity-sensitive stress: placement by syllable weight, not by spelling.

The end-anchored systems (Portuguese, Spanish, Italian) pick the stressed
syllable from an orthographic ending. Arabic and Latin do not: stress falls on a
syllable because that syllable is **heavy**, and weight is a property of the
transcription — a long vowel, a coda — not of the spelling. No ending table can
express it, which is exactly why the Arabic spec used to declare no stress at
all.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.stress import (
    HEAVY, LIGHT, SUPERHEAVY, detect_stress_by_weight, syllabify_ipa,
    syllable_weight,
)
from orthography2ipa.types import StressRules

ARABIC = StressRules(
    default_position=-3,
    quantity_sensitive=True,
    superheavy_final_attracts=True,
    max_onset=1,
)


# ─── the syllabifier: weight depends on where the boundary falls ────────

@pytest.mark.parametrize("ipa,expected", [
    ("kitaːb", ["ki", "taːb"]),
    # The load-bearing case. Onset-maximising gives mu-da-rris, whose penult is
    # LIGHT, and the stress would land on the antepenult. Arabic takes exactly
    # one consonant as an onset, so the cluster splits: mu-dar-ris, the penult
    # is heavy, and the stress lands there.
    ("mudarris", ["mu", "dar", "ris"]),
    ("madrasa", ["mad", "ra", "sa"]),
    ("qahwa", ["qah", "wa"]),
    ("kataba", ["ka", "ta", "ba"]),
])
def test_syllabify_ipa_divides_clusters_by_onset_limit(ipa, expected):
    assert syllabify_ipa(ipa, max_onset=1) == expected


def test_onset_limit_changes_the_division():
    """A larger onset limit hands the whole cluster forward, emptying the coda.

    With both consonants of ⟨rr⟩ allowed as an onset the penult keeps no coda
    and is light — which is precisely the mis-division that would put Arabic's
    stress on the wrong syllable.
    """
    assert syllabify_ipa("mudarris", max_onset=2) == ["mu", "da", "rris"]
    assert syllable_weight("da") == LIGHT


# ─── weight ─────────────────────────────────────────────────────────────

@pytest.mark.parametrize("syllable,weight", [
    ("ki", LIGHT),          # CV
    ("taː", HEAVY),         # CVː
    ("dar", HEAVY),         # CVC
    ("taːb", SUPERHEAVY),   # CVːC
    ("bint", SUPERHEAVY),   # CVCC
    ("bajt", SUPERHEAVY),   # diphthong + coda
])
def test_syllable_weight(syllable, weight):
    assert syllable_weight(syllable) == weight


# ─── the cascade ────────────────────────────────────────────────────────

@pytest.mark.parametrize("ipa,index,why", [
    ("kitaːb", -1, "superheavy final takes the stress"),
    ("mudarris", -2, "heavy penult takes it when the final is not superheavy"),
    ("madrasa", -3, "otherwise the antepenult"),
    ("kataba", -3, "all light → antepenult"),
    ("qahwa", -2, "two syllables: the heavy penult is also the first"),
])
def test_detect_stress_by_weight(ipa, index, why):
    assert detect_stress_by_weight(ipa, ARABIC) == index, why


def test_a_language_that_never_stresses_the_final_syllable():
    """Latin's rule: a superheavy final does NOT attract stress."""
    latin = StressRules(
        default_position=-3, quantity_sensitive=True,
        superheavy_final_attracts=False, max_onset=1,
    )
    assert detect_stress_by_weight("kitaːb", latin) == -2
    assert detect_stress_by_weight("kitaːb", ARABIC) == -1


def test_monosyllable():
    assert detect_stress_by_weight("bajt", ARABIC) == -1


# ─── end to end, through the G2P ────────────────────────────────────────

@pytest.mark.parametrize("word,expected,why", [
    ("كِتَاب", "kiˈtaːb", "superheavy final CVːC"),
    ("مُدَرِّس", "muˈdarris", "heavy penult CVC"),
    ("مَدْرَسَة", "ˈmadrasa", "all-light tail → antepenult"),
    ("قَهْوَة", "ˈqahwa", "heavy penult, two syllables"),
    ("كَتَبَ", "ˈkataba", "all light → antepenult"),
])
def test_arabic_is_stressed_end_to_end(word, expected, why):
    """The system this was built for, through the real shipped spec."""
    assert G2P("ar").transcribe(word) == expected, why


@pytest.mark.parametrize("lang", ["ar-SA-x-najd", "ar-SA-x-hejaz", "ar-EG"])
def test_the_varieties_are_stressed_too(lang):
    assert G2P(lang).transcribe("كِتَاب").endswith("ˈtaːb")


def test_end_anchored_languages_are_untouched():
    """The existing systems must not move."""
    assert G2P("pt").transcribe("palavra") == "pɐˈlavɾɐ"
    assert not get("pt").stress.quantity_sensitive


def test_the_arabic_specs_opt_in():
    """Arabic is the system this was built for, and it now declares the block."""
    from orthography2ipa import available_codes
    opted_in = {
        code for code in available_codes()
        if (get(code).stress and get(code).stress.quantity_sensitive)
    }
    assert {"ar", "arb", "ar-SA-x-najd", "ar-SA-x-hejaz", "ar-EG"} <= opted_in
    # Nothing outside Arabic opted in, so no other language moved.
    assert all(c.startswith("ar") for c in opted_in), sorted(opted_in)


# ─── weight is counted in SEGMENTS, not characters ──────────────────────
#
# A modifier letter (pharyngealization ˤ, aspiration ʰ, length ː) rides on the
# consonant it modifies, and an affricate is one consonant, not a cluster.
# Counting characters made a CVC coda look like CVCC, called the syllable
# superheavy and pulled the stress onto it: /ɣalatˤ/ came out ɣaˈlɑtˤ and
# /xaradʒ/ xaˈradʒ, both wrong.

@pytest.mark.parametrize("syllable,weight,why", [
    ("latˤ", HEAVY, "tˤ is ONE pharyngealized consonant — CVC, not CVCC"),
    ("radʒ", HEAVY, "dʒ is ONE affricate — CVC"),
    ("lidz", HEAVY, "so is the Najdi affricate dz"),
    ("lit͡s", HEAVY, "tie-barred spelling likewise"),
    ("bakʰt", SUPERHEAVY, "a real two-consonant coda is still superheavy"),
])
def test_syllable_weight_counts_segments(syllable, weight, why):
    assert syllable_weight(syllable) == weight, why


@pytest.mark.parametrize("ipa,index,why", [
    ("ɣalatˤ", -2, "final CVC is only heavy, so it does not attract"),
    ("xaradʒ", -2, "same, with an affricate coda"),
    ("saːlidz", -2, "heavy penult saː keeps the stress"),
])
def test_detect_stress_by_weight_counts_segments(ipa, index, why):
    assert detect_stress_by_weight(ipa, ARABIC) == index, why


def test_an_affricate_is_never_split_across_a_syllable_boundary():
    assert syllabify_ipa("katsib", max_onset=1) == ["ka", "tsib"]
    assert syllabify_ipa("matˤɑr", max_onset=1) == ["ma", "tˤɑr"]


def test_the_stress_mark_never_lands_inside_a_long_vowel():
    """The mark is placed against the weight syllabifier's own division.

    The naive `syllabify` cuts `saːliq` as sa|ːliq, so marking the final
    syllable there produced `saˈːliq` — a stress mark inside a long vowel,
    which is not well-formed IPA.
    """
    from orthography2ipa.stress import apply_stress_mark
    marked = apply_stress_mark(
        "saːliq", ARABIC, -1,
        ipa_syllables=syllabify_ipa("saːliq", ARABIC.max_onset),
    )
    assert marked == "saːˈliq"
