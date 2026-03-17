"""Tests for feature vector accuracy — spot-checks on phone_features.

Validates that the feature system has the correct dimensionality and that
specific phone classes (clicks, nasalized vowels, ejectives, plain vowels,
plain consonants) carry the expected feature values.
"""
import pytest

from orthography2ipa.feats import phone_features, NUM_FEATURES


# ═══════════════════════════════════════════════════════════════════════════
# Dimensionality
# ═══════════════════════════════════════════════════════════════════════════

class TestDimensionality:
    """Feature system should have exactly 23 features."""

    def test_num_features_constant(self):
        assert NUM_FEATURES == 23

    def test_all_vectors_length_23(self):
        for phone, vec in phone_features.items():
            assert len(vec) == 23, f"{phone}: has {len(vec)} features, expected 23"


# ═══════════════════════════════════════════════════════════════════════════
# Clicks — index 21
# ═══════════════════════════════════════════════════════════════════════════

class TestClicks:
    """Click consonants should have click=True at index 21."""

    @pytest.mark.parametrize("click", ["ǃ", "ǀ", "ǁ", "ǂ", "ʘ"])
    def test_click_feature_true(self, click):
        assert click in phone_features, f"{click} missing from phone_features"
        assert phone_features[click][21] is True

    @pytest.mark.parametrize("vowel", ["a", "e", "i", "o", "u"])
    def test_vowels_not_clicks(self, vowel):
        assert phone_features[vowel][21] is False


# ═══════════════════════════════════════════════════════════════════════════
# Nasalized vowels — index 22
# ═══════════════════════════════════════════════════════════════════════════

class TestNasalizedVowels:
    """Nasalized vowels should have nasal_vowel=True at index 22."""

    @pytest.mark.parametrize("nv", ["ã", "ẽ", "ĩ", "õ", "ũ"])
    def test_nasal_vowel_feature_true(self, nv):
        assert nv in phone_features, f"{nv} missing from phone_features"
        assert phone_features[nv][22] is True

    @pytest.mark.parametrize("vowel", ["a", "e", "i", "o", "u"])
    def test_oral_vowels_not_nasal(self, vowel):
        assert phone_features[vowel][22] is False

    @pytest.mark.parametrize("cons", ["p", "t", "k"])
    def test_consonants_not_nasal_vowel(self, cons):
        assert phone_features[cons][22] is False


# ═══════════════════════════════════════════════════════════════════════════
# Ejectives
# ═══════════════════════════════════════════════════════════════════════════

class TestEjectives:
    """Ejective consonants should be present in phone_features."""

    @pytest.mark.parametrize("ej", ["pʼ", "tʼ", "kʼ"])
    def test_ejective_exists(self, ej):
        assert ej in phone_features, f"{ej} missing from phone_features"
