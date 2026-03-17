"""Tests for Phase 0B feature system extensions."""
from orthography2ipa.feats import (
    NUM_FEATURES,
    feature_weights,
    modifiers,
    phone_features,
    vectorize_phones,
)
from orthography2ipa.distance import segment_distance


class TestFeatureSystemExtension:
    def test_num_features_23(self):
        assert NUM_FEATURES == 23

    def test_all_phones_have_23_features(self):
        for phone, vec in phone_features.items():
            assert len(vec) == 23, f"{phone}: has {len(vec)} features"

    def test_feature_weights_sum_to_one(self):
        assert abs(sum(feature_weights) - 1.0) < 1e-10

    def test_feature_weights_count(self):
        assert len(feature_weights) == 23


class TestClickPhones:
    def test_clicks_exist(self):
        for click in ["ǀ", "ǁ", "ǂ", "ǃ", "ʘ"]:
            assert click in phone_features

    def test_clicks_have_click_feature(self):
        for click in ["ǀ", "ǁ", "ǂ", "ǃ", "ʘ"]:
            assert phone_features[click][21] is True  # click feature

    def test_non_clicks_dont_have_click_feature(self):
        for phone in ["p", "t", "k", "a", "i"]:
            assert phone_features[phone][21] is False

    def test_clicks_closer_to_each_other_than_to_vowels(self):
        d_click_click = segment_distance("ǃ", "ǀ")
        d_click_vowel = segment_distance("ǃ", "a")
        assert d_click_click < d_click_vowel


class TestEjectives:
    def test_ejectives_exist(self):
        for ej in ["pʼ", "tʼ", "kʼ", "qʼ"]:
            assert ej in phone_features

    def test_ejectives_constricted_glottis(self):
        for ej in ["pʼ", "tʼ", "kʼ", "qʼ"]:
            assert phone_features[ej][10] is True  # constricted_glottis


class TestPrenasalizedStops:
    def test_prenasalized_exist(self):
        for pn in ["ᵐb", "ⁿd", "ᵑɡ"]:
            assert pn in phone_features

    def test_prenasalized_are_nasal(self):
        for pn in ["ᵐb", "ⁿd", "ᵑɡ"]:
            assert phone_features[pn][6] is True  # nasal


class TestNasalizedVowels:
    def test_nasalized_vowels_exist(self):
        for nv in ["ã", "ẽ", "ĩ", "õ", "ũ"]:
            assert nv in phone_features

    def test_nasalized_vowels_have_nasal_vowel_feature(self):
        for nv in ["ã", "ẽ", "ĩ", "õ", "ũ"]:
            assert phone_features[nv][22] is True  # nasal_vowel

    def test_oral_vowels_dont_have_nasal_vowel_feature(self):
        for v in ["a", "e", "i", "o", "u"]:
            assert phone_features[v][22] is False

    def test_nasalized_vowels_are_nasal(self):
        for nv in ["ã", "ẽ", "ĩ", "õ", "ũ"]:
            assert phone_features[nv][6] is True  # nasal


class TestNewModifiers:
    def test_nasalization_modifier(self):
        assert "̃" in modifiers
        assert modifiers["̃"][6] is True  # nasal
        assert modifiers["̃"][22] is True  # nasal_vowel

    def test_voicelessness_modifier(self):
        assert "̥" in modifiers
        assert modifiers["̥"][8] is False  # voice

    def test_palatalization_modifier(self):
        assert "ʲ" in modifiers
        assert modifiers["ʲ"][15] is True  # high

    def test_labialization_modifier(self):
        assert "ʷ" in modifiers
        assert modifiers["ʷ"][14] is True  # labial

    def test_ejective_modifier(self):
        assert "ʼ" in modifiers
        assert modifiers["ʼ"][10] is True  # constricted_glottis
