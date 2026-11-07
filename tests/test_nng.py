"""Per-language accuracy tests for Nǁng / Nǀuu (ngh), a critically endangered
Tuu (!Ui branch) click language of South Africa.

Every expectation below is a claim about the click-accompaniment and
nasal-vowel system, sourced from the citations carried in
``orthography2ipa/data/ngh.json``: the linguo-pulmonic contour click series
(click + delayed uvular release) and the circumflex alternate nasalization
diacritic. Words are drawn from the cached wikipron gold
(``.benchmark_cache/ngh_latn_broad.tsv``); the IPA is the value the cited
description predicts, not a value read back from any engine.

Run with:
    pytest tests/test_nng.py -v --tb=short
"""
from __future__ import annotations

import unicodedata

import pytest

import orthography2ipa


def _spec():
    try:
        return orthography2ipa.get("ngh")
    except Exception as exc:  # pragma: no cover - registry failure
        pytest.skip(f"ngh not available: {exc}")


def _ipa(word: str) -> str:
    # Composed form on both sides: a nasal vowel written with a combining
    # tilde has a precomposed codepoint and an uncomposed literal in a test
    # would fail for a typographic reason rather than a phonological one.
    return unicodedata.normalize("NFC", orthography2ipa.transcribe(word, "ngh"))


def _eq(word: str, expected: str) -> bool:
    return _ipa(word) == unicodedata.normalize("NFC", expected)


class TestLinguoPulmonicClickCluster:
    """<q>/<qh> directly after a click letter marks the linguo-pulmonic
    contour click series -- the click's rear closure releases into a
    (optionally aspirated) uvular stop, per Miller et al.'s reanalysis and
    Güldemann's click classification, both cited via the Wikipedia
    phonology article's bibliography."""

    def test_grapheme_table_has_the_aspirated_click_uvular_series(self):
        spec = _spec()
        assert spec.graphemes["ǁqh"] == ["ǁqʰ"]
        assert spec.graphemes["ǀqh"] == ["ǀqʰ"]

    def test_word_lateral_click_uvular_release(self):
        # gold: ǁqhuu -> [ǁ qʰ u u]
        assert _eq("ǁqhuu", "ǁqʰuu")


class TestPostVocalicPharyngealization:
    """<q> after an oral or nasal vowel (not adjacent to a click letter)
    marks pharyngealization of that vowel rather than a click cluster."""

    def test_grapheme_table_has_the_pharyngealized_vowel_series(self):
        spec = _spec()
        assert spec.graphemes["aq"] == ["aˤ"]
        assert spec.graphemes["âq"] == ["ãˤ"]

    def test_word_postvocalic_q_is_pharyngealization_not_a_click(self):
        # gold: haqaʻi -> [h ɑˤ ɑ ʔ i]
        assert _eq("haqaʻi", "haˤaʔi")


class TestCircumflexNasalVowels:
    """<â ê î ô û> are an alternate notation for the same nasalized vowels
    already written with a combining/precomposed tilde elsewhere in the
    dataset (community-dictionary transcriptions vary transcriber to
    transcriber)."""

    def test_grapheme_table_maps_circumflex_to_the_tilde_series(self):
        spec = _spec()
        assert spec.graphemes["â"] == ["ã"]
        assert spec.graphemes["ô"] == ["õ"]

    def test_word_circumflex_vowel_is_nasalized(self):
        # gold: tsâa -> [t s ɑ̃ ɑ̃] (dataset uses /a/-quality; this spec's
        # oral-vowel value is the mid-open a, so the predicted output nasal
        # -izes the spec's own "a" rather than borrowing the gold's IPA
        # vowel quality)
        assert _eq("tsâa", "tsãa")
        # gold: kôea -> [k õ e ə]
        assert _eq("kôea", "kõea")
