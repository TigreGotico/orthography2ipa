"""Tests for typological distance ordering — cross-language comparisons.

Validates that phonological distance metrics produce linguistically
sensible orderings: related languages closer than unrelated ones,
same-script distance zero, and script family distances ordered correctly.
"""
import pytest

from orthography2ipa.registry import get
from orthography2ipa.distance import full_distance, inventory_distance
from orthography2ipa import script_distance_by_name


# ═══════════════════════════════════════════════════════════════════════════
# Fixtures — skip if language not available
# ═══════════════════════════════════════════════════════════════════════════

@pytest.fixture
def es():
    try:
        return get("es-ES")
    except Exception:
        pytest.skip("es-ES not available in registry")


@pytest.fixture
def pt():
    try:
        return get("pt-PT")
    except Exception:
        pytest.skip("pt-PT not available in registry")


@pytest.fixture
def arb():
    try:
        return get("arb")
    except Exception:
        pytest.skip("arb not available in registry")


@pytest.fixture
def de():
    try:
        return get("de-DE")
    except Exception:
        pytest.skip("de-DE not available in registry")


@pytest.fixture
def nl():
    try:
        return get("nl")
    except Exception:
        pytest.skip("nl not available in registry")


# ═══════════════════════════════════════════════════════════════════════════
# Cross-language distance ordering
# ═══════════════════════════════════════════════════════════════════════════

class TestRomanceCloser:
    """Romance languages should be closer to each other than to Arabic."""

    def test_es_pt_closer_than_es_arb(self, es, pt, arb):
        d_romance = full_distance(es, pt)
        d_cross = full_distance(es, arb)
        assert d_romance < d_cross


class TestGermanicCloser:
    """Germanic languages should be closer to each other than to Arabic."""

    def test_de_nl_closer_than_de_arb(self, de, nl, arb):
        d_germanic = full_distance(de, nl)
        d_cross = full_distance(de, arb)
        assert d_germanic < d_cross


# ═══════════════════════════════════════════════════════════════════════════
# Script distance ordering
# ═══════════════════════════════════════════════════════════════════════════

class TestScriptDistance:
    """Script distance should reflect typological script relationships."""

    def test_same_script_zero(self):
        assert script_distance_by_name("Latin", "Latin") == 0.0

    def test_latin_cyrillic_closer_than_latin_hangul(self):
        d_lc = script_distance_by_name("Latin", "Cyrillic")
        d_lh = script_distance_by_name("Latin", "Hangul")
        assert d_lc < d_lh

    def test_arabic_hebrew_closer_than_arabic_hangul(self):
        d_ah = script_distance_by_name("Arabic", "Hebrew")
        d_ak = script_distance_by_name("Arabic", "Hangul")
        assert d_ah < d_ak
