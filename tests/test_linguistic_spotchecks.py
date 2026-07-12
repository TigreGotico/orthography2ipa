"""Tests for linguistic accuracy — spot-checks on grapheme→IPA mappings.

Validates that specific languages produce correct IPA outputs for
well-known grapheme→phoneme correspondences, and that sandhi rules
are populated for languages that require them.
"""
import pytest

from orthography2ipa.registry import get


# ═══════════════════════════════════════════════════════════════════════════
# Helper
# ═══════════════════════════════════════════════════════════════════════════

def _load_or_skip(code):
    """Load a LanguageSpec by code, skipping the test if unavailable."""
    try:
        return get(code)
    except Exception:
        pytest.skip(f"{code} not available in registry")


# ═══════════════════════════════════════════════════════════════════════════
# Spanish (es-ES)
# ═══════════════════════════════════════════════════════════════════════════

class TestSpanish:
    """Spot-checks for Spanish grapheme→IPA mappings."""

    @pytest.fixture(autouse=True)
    def load_spec(self):
        self.spec = _load_or_skip("es-ES")

    def test_ch_maps_to_affricate(self):
        ipas = self.spec.graphemes.get("ch", [])
        assert any("tʃ" in ipa for ipa in ipas), f"ch → {ipas}, expected tʃ"

    def test_enye_maps_to_palatal_nasal(self):
        ipas = self.spec.graphemes.get("ñ", [])
        assert any("ɲ" in ipa for ipa in ipas), f"ñ → {ipas}, expected ɲ"

    def test_ll_maps_to_palatal(self):
        ipas = self.spec.graphemes.get("ll", [])
        assert any("ʎ" in ipa or "ʝ" in ipa for ipa in ipas), (
            f"ll → {ipas}, expected ʎ or ʝ"
        )


# ═══════════════════════════════════════════════════════════════════════════
# Portuguese (pt-PT)
# ═══════════════════════════════════════════════════════════════════════════

class TestPortuguese:
    """Spot-checks for Portuguese grapheme→IPA mappings."""

    @pytest.fixture(autouse=True)
    def load_spec(self):
        self.spec = _load_or_skip("pt-PT")

    def test_lh_maps_to_palatal_lateral(self):
        ipas = self.spec.graphemes.get("lh", [])
        assert any("ʎ" in ipa for ipa in ipas), f"lh → {ipas}, expected ʎ"

    def test_nh_maps_to_palatal_nasal(self):
        ipas = self.spec.graphemes.get("nh", [])
        assert any("ɲ" in ipa for ipa in ipas), f"nh → {ipas}, expected ɲ"


# ═══════════════════════════════════════════════════════════════════════════
# Rionorese (ast-PT-x-rionor)
# ═══════════════════════════════════════════════════════════════════════════

class TestRionorese:
    """Spot-checks for Rionorese Asturian-Leonese grapheme→IPA mappings."""

    @pytest.fixture(autouse=True)
    def load_spec(self):
        self.spec = _load_or_skip("ast-PT-x-rionor")

    def test_ch_contains_postalveolar_fricative(self):
        ipas = self.spec.resolve_grapheme("ch")
        assert any("ʃ" in ipa for ipa in ipas), f"ch → {ipas}, expected ʃ"


# ═══════════════════════════════════════════════════════════════════════════
# Arabic (arb)
# ═══════════════════════════════════════════════════════════════════════════

class TestArabic:
    """Spot-checks for Classical Arabic grapheme→IPA mappings."""

    @pytest.fixture(autouse=True)
    def load_spec(self):
        self.spec = _load_or_skip("arb")

    def test_has_arabic_letter_graphemes(self):
        graphemes = self.spec.graphemes
        arabic_graphemes = [g for g in graphemes if any(
            "\u0600" <= ch <= "\u06FF" for ch in g
        )]
        assert len(arabic_graphemes) > 0, "Expected Arabic letter graphemes"


# ═══════════════════════════════════════════════════════════════════════════
# Sandhi rules
# ═══════════════════════════════════════════════════════════════════════════

class TestSandhiRules:
    """Languages with sandhi should have non-empty sandhi_rules."""

    @pytest.mark.parametrize("code", ["fr-FR", "pt-PT", "arb"])
    def test_sandhi_rules_populated(self, code):
        spec = _load_or_skip(code)
        assert len(spec.sandhi_rules) > 0, (
            f"{code} should have sandhi_rules, got empty"
        )
