"""Tests for script_distance module."""
from orthography2ipa.script_distance import (
    SCRIPT_REGISTRY,
    ScriptFeatures,
    script_distance,
    script_distance_by_name,
)
from orthography2ipa.types import ScriptType


class TestScriptRegistry:
    def test_registry_has_major_scripts(self):
        expected = {"Latin", "Cyrillic", "Arabic", "Devanagari", "Greek",
                    "Hangul", "Hanzi", "Kana", "Hebrew"}
        assert expected.issubset(set(SCRIPT_REGISTRY.keys()))

    def test_registry_entries_are_script_features(self):
        for name, feat in SCRIPT_REGISTRY.items():
            assert isinstance(feat, ScriptFeatures)
            assert feat.name == name or feat.name in name


class TestScriptDistance:
    def test_same_script_zero(self):
        assert script_distance_by_name("Latin", "Latin") == 0.0

    def test_latin_cyrillic_close(self):
        """Latin and Cyrillic share Greek ancestor → relatively close."""
        d = script_distance_by_name("Latin", "Cyrillic")
        assert 0.0 < d < 0.3

    def test_latin_arabic_moderate(self):
        d = script_distance_by_name("Latin", "Arabic")
        assert 0.3 < d < 0.7

    def test_latin_hanzi_far(self):
        d = script_distance_by_name("Latin", "Hanzi")
        assert d > 0.7

    def test_arabic_hebrew_close(self):
        """Both abjads, shared Phoenician ancestor."""
        d = script_distance_by_name("Arabic", "Hebrew")
        assert d < 0.3

    def test_devanagari_bengali_close(self):
        """Both Brahmic abugidas."""
        d = script_distance_by_name("Devanagari", "Bengali")
        assert d < 0.2

    def test_ordering_latin_cyrillic_vs_latin_arabic(self):
        d_lc = script_distance_by_name("Latin", "Cyrillic")
        d_la = script_distance_by_name("Latin", "Arabic")
        assert d_lc < d_la

    def test_ordering_latin_cyrillic_vs_latin_hangul(self):
        d_lc = script_distance_by_name("Latin", "Cyrillic")
        d_lh = script_distance_by_name("Latin", "Hangul")
        assert d_lc < d_lh

    def test_symmetry(self):
        d1 = script_distance_by_name("Arabic", "Latin")
        d2 = script_distance_by_name("Latin", "Arabic")
        assert abs(d1 - d2) < 1e-10

    def test_range_zero_to_one(self):
        for a in SCRIPT_REGISTRY:
            for b in SCRIPT_REGISTRY:
                d = script_distance_by_name(a, b)
                assert 0.0 <= d <= 1.0, f"{a} vs {b}: {d}"


class TestReconstructionScript:
    """Tests for the IPA-reconstruction meta-script."""

    def test_reconstruction_in_registry(self):
        assert "IPA-reconstruction" in SCRIPT_REGISTRY
        feat = SCRIPT_REGISTRY["IPA-reconstruction"]
        assert feat.script_type == ScriptType.RECONSTRUCTION

    def test_reconstruction_self_zero(self):
        assert script_distance_by_name("IPA-reconstruction", "IPA-reconstruction") == 0.0

    def test_reconstruction_close_to_alphabet(self):
        """Reconstruction (segmental IPA) is closest to alphabets."""
        d = script_distance_by_name("IPA-reconstruction", "Latin")
        assert d < 0.4

    def test_reconstruction_far_from_logographic(self):
        d = script_distance_by_name("IPA-reconstruction", "Hanzi")
        assert d > 0.6

    def test_reconstruction_ordering(self):
        """Reconstruction closer to Latin than to Hanzi."""
        d_lat = script_distance_by_name("IPA-reconstruction", "Latin")
        d_han = script_distance_by_name("IPA-reconstruction", "Hanzi")
        assert d_lat < d_han

    def test_proto_languages_use_reconstruction(self):
        """Proto-language specs should have script_type RECONSTRUCTION."""
        from orthography2ipa.registry import get
        for code in ["ine", "gem", "sem", "cel"]:
            try:
                spec = get(code)
                assert spec.script_type == ScriptType.RECONSTRUCTION, \
                    f"{code} should be RECONSTRUCTION, got {spec.script_type}"
                assert spec.script == "IPA-reconstruction", \
                    f"{code} should have script='IPA-reconstruction'"
            except KeyError:
                pass  # skip if not loaded
