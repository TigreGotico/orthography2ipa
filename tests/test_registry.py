"""Tests for orthography2ipa.registry — Language loading, aliases, families.

Validates:
- Lazy loading via get()
- ISO 639-3 alias resolution
- available_codes() and available_families()
- Error handling for unknown codes
- Cache consistency
"""
import pytest

from orthography2ipa import registry

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
        assert {"Indo-European", "Romance", "Ibero-Romance"} <= set(en.family_path)
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
        for family in ["Indo-European > Italic > Romance"]:
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
        romance = fam.get("Indo-European > Italic > Romance", [])
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

    These assert BEHAVIOUR, not the contents of the environment. Whether a
    syllabifier is installed is not a property of this library: tugaphone ships
    one, and it is a normal — indeed the intended — downstream configuration. A
    test that asserts "nothing is installed" passes only where nothing is, which
    means it fails for exactly the users who wired the plugin system up correctly.
    So the zero-plugin case is *constructed* here rather than assumed.
    """

    def test_zero_plugins_returns_none(self, monkeypatch):
        """The zero-plugin case must not crash — it must simply report nothing."""
        monkeypatch.setattr(registry, "_syllabifiers", {})
        assert registry.get_syllabifier("pt-PT") is None

    def test_unknown_code_returns_none(self):
        """A code no plugin claims resolves to nothing, installed or not."""
        assert get_syllabifier("xx-nonexistent-code") is None

    def test_repeated_calls_are_stable(self):
        """Discovery is cached: repeated lookups return the same object and do
        not re-scan the entry points."""
        first = get_syllabifier("pt-PT")
        second = get_syllabifier("pt-PT")
        assert first is second

    def test_an_installed_plugin_is_discovered(self):
        """When a plugin IS installed, it is found and it is a syllabifier.

        Skipped where none is installed, because that is a fact about the
        environment and not about this code.
        """
        plugin = get_syllabifier("pt-PT")
        if plugin is None:
            pytest.skip("no syllabifier plugin installed in this environment")
        assert hasattr(plugin, "syllabify")


# ═══════════════════════════════════════════════════════════════════════════
# Cache immutability — a spec handed out by get() cannot be mutated
# ═══════════════════════════════════════════════════════════════════════════

class TestCachedSpecIsImmutable:
    """get() returns the single cached spec shared by every caller.

    A mutation of that shared instance would silently corrupt every subsequent
    caller in the process — this actually happened and poisoned a measurement
    run. The mapping fields are frozen (:class:`FrozenDict`) so the shared
    instance cannot be mutated in place, while identity is preserved (get() is
    cheap: no per-call copy) and reads/replace/asdict/deepcopy keep working.
    """

    def test_grapheme_key_assignment_is_blocked(self):
        spec = get("ext-PT-x-barrancos")
        with pytest.raises(TypeError):
            spec.graphemes["aqui"] = ["x"]

    def test_grapheme_pop_and_update_are_blocked(self):
        spec = get("pt-PT")
        with pytest.raises(TypeError):
            spec.graphemes.pop(next(iter(spec.graphemes)))
        with pytest.raises(TypeError):
            spec.graphemes.update({"zzz": ["z"]})

    def test_plugins_mapping_is_blocked(self):
        spec = get("pt-PT")
        with pytest.raises(TypeError):
            spec.plugins["stress"] = ("bogus",)

    def test_attribute_rebinding_is_blocked(self):
        spec = get("pt-PT")
        with pytest.raises(Exception):  # FrozenInstanceError
            spec.graphemes = {}

    def test_a_failed_mutation_leaves_a_fresh_get_pristine(self):
        """The regression: mutate a fetched spec, then a fresh get() is
        unaffected. Even a mutation that slips past the guard must not leak
        into the next caller's spec."""
        first = get("ext-PT-x-barrancos")
        before = dict(first.graphemes)
        # attempts to corrupt the shared instance
        for attempt in (
            lambda: first.graphemes.__setitem__("aqui", ["CORRUPT"]),
            lambda: first.graphemes.update({"aqui": ["CORRUPT"]}),
        ):
            try:
                attempt()
            except TypeError:
                pass
        second = get("ext-PT-x-barrancos")
        assert second is first          # identity: shared cached instance
        assert dict(second.graphemes) == before
        assert "aqui" not in second.graphemes

    def test_identity_is_preserved_for_aliases(self):
        """Freezing must not turn get() into a copy: alias and canonical code
        still resolve to the SAME cached object."""
        assert get("por") is get("pt-PT")

    def test_replace_and_asdict_still_work(self):
        from dataclasses import replace, asdict
        spec = get("pt-PT")
        assert replace(spec, notes="x").notes == "x"
        assert isinstance(asdict(spec)["graphemes"], dict)
