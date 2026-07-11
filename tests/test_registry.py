"""Tests for orthography2ipa.registry — Language loading, aliases, families.

Validates:
- Lazy loading via get()
- ISO 639-3 alias resolution
- available_codes() and available_families()
- Error handling for unknown codes
- Cache consistency
"""
import pytest

import orthography2ipa
from orthography2ipa.registry import (
    get,
    available_codes,
    available_families,
    get_syllabifier,
)
from orthography2ipa.types import LanguageSpec


# ═══════════════════════════════════════════════════════════════════════════
# Basic loading
# ═══════════════════════════════════════════════════════════════════════════

class TestRegistryGet:
    """Tests for get() — the main entry point."""

    @pytest.mark.parametrize("code", ["pt-PT"])
    def test_core_languages_load(self, code):
        spec = get(code)
        assert isinstance(spec, LanguageSpec)
        assert spec.name  # non-empty name
        assert spec.family  # non-empty family

    def test_spec_fields_populated(self):
        en = get("pt-PT")
        assert en.family == "Indo-European > Romance"
        assert en.script == "Latin"
        assert len(en.graphemes) > 20  # English has many grapheme entries
        assert len(en.allophones) > 10

    def test_returns_same_object_on_second_call(self):
        """Verify caching: same object returned for repeated calls."""
        spec1 = get("pt-PT")
        spec2 = get("pt-PT")
        assert spec1 is spec2

    def test_unknown_code_raises_keyerror(self):
        with pytest.raises(KeyError, match="unsupported language:"):
            get("xx-nonexistent-code")

    def test_keyerror_message_lists_available(self):
        with pytest.raises(KeyError) as exc_info:
            get("zzzz")
        assert "Available" in str(exc_info.value)


# ═══════════════════════════════════════════════════════════════════════════
# ISO 639-3 alias resolution
# ═══════════════════════════════════════════════════════════════════════════

class TestAliases:
    """ISO 639-3 and other aliases should resolve correctly."""

    @pytest.mark.parametrize("alias,canonical", [
        ("por", "pt-PT"),
    ])
    def test_iso639_3_aliases(self, alias, canonical):
        spec_alias = get(alias)
        spec_canon = get(canonical)
        assert spec_alias.code == spec_canon.code

    def test_alias_and_canonical_return_same_object(self):
        """After loading, both should point to same cached object."""
        spec_por = get("por")
        spec_pt = get("pt-PT")
        assert spec_por is spec_pt


# ═══════════════════════════════════════════════════════════════════════════
# available_codes
# ═══════════════════════════════════════════════════════════════════════════

class TestAvailableCodes:
    """Tests for available_codes()."""

    def test_returns_sorted_list(self):
        codes = available_codes()
        assert isinstance(codes, list)
        assert codes == sorted(codes)

    def test_core_languages_present(self):
        codes = available_codes()
        for c in ["pt-PT"]:
            assert c in codes, f"{c} should be in available codes"

    def test_returns_many_codes(self):
        """ensure reasonable count."""
        codes = available_codes()
        assert len(codes) >= 3

    def test_no_duplicates(self):
        codes = available_codes()
        assert len(codes) == len(set(codes))


# ═══════════════════════════════════════════════════════════════════════════
# available_families
# ═══════════════════════════════════════════════════════════════════════════

class TestAvailableFamilies:
    """Tests for available_families()."""

    def test_returns_dict(self):
        fam = available_families()
        assert isinstance(fam, dict)

    def test_expected_families_present(self):
        fam = available_families()
        for family in ["Indo-European > Romance"]:
            assert family in fam, f"Family '{family}' should be present"

    def test_family_values_are_code_lists(self):
        fam = available_families()
        for family, codes in fam.items():
            assert isinstance(codes, list)
            assert len(codes) > 0
            for c in codes:
                assert isinstance(c, str)

    def test_romance_has_many_members(self):
        fam = available_families()
        romance = fam.get("Indo-European > Romance", [])
        assert len(romance) >= 3  # many Spanish/Portuguese dialects


# ═══════════════════════════════════════════════════════════════════════════
# Top-level convenience functions
# ═══════════════════════════════════════════════════════════════════════════

class TestTopLevelAPI:
    """Verify that the top-level orthography2ipa.* functions work."""

    def test_top_level_get(self):
        spec = orthography2ipa.get("pt-PT")
        assert isinstance(spec, LanguageSpec)

    def test_top_level_available_codes(self):
        codes = orthography2ipa.available_codes()
        assert "pt-PT" in codes

    def test_top_level_available_families(self):
        fam = orthography2ipa.available_families()
        assert isinstance(fam, dict)

    def test_version_string(self):
        assert hasattr(orthography2ipa, "__version__")
        assert isinstance(orthography2ipa.__version__, str)


# ═══════════════════════════════════════════════════════════════════════════
# Syllabifier plugin discovery
# ═══════════════════════════════════════════════════════════════════════════

class TestSyllabifierDiscovery:
    """get_syllabifier() dispatches to entry-point plugins.

    No third-party syllabifier package is installed in this environment,
    so discovery must handle the zero-plugins case without crashing and
    simply report that no syllabifier is registered.
    """

    def test_no_plugins_installed_returns_none(self):
        assert get_syllabifier("pt-PT") is None

    def test_unknown_code_returns_none(self):
        assert get_syllabifier("xx-nonexistent-code") is None

    def test_repeated_calls_are_stable(self):
        """Discovery is cached; repeated lookups don't re-scan or raise."""
        first = get_syllabifier("pt-PT")
        second = get_syllabifier("pt-PT")
        assert first is second is None
