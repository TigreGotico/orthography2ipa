"""Tests for orthography2ipa.types — LanguageSpec, Ancestor, AncestorRole.

Validates the core data model: immutability, accessor methods, convenience
properties, and edge-case handling.
"""
import pytest
from dataclasses import FrozenInstanceError

from orthography2ipa.types import (
    Ancestor,
    AncestorRole,
    LanguageSpec,
    Grapheme2IPA,
    AllophoneMap,
)


# ═══════════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════════

@pytest.fixture
def minimal_spec() -> LanguageSpec:
    """A bare-minimum LanguageSpec with no ancestry."""
    return LanguageSpec(
        code="xx",
        name="Test Language",
        family="TestFamily",
        script="Latin",
        graphemes={"a": ["a"], "b": ["b"]},
        allophones={"a": ["a"], "b": ["b", "β"]},
    )


@pytest.fixture
def spec_with_parent() -> LanguageSpec:
    """A LanguageSpec with only the simple `parent` field set."""
    return LanguageSpec(
        code="xx-dialect",
        name="Test Dialect",
        family="TestFamily",
        script="Latin",
        graphemes={"a": ["a"], "b": ["b"]},
        allophones={"a": ["a"], "b": ["b"]},
        parent="xx",
    )


@pytest.fixture
def spec_with_full_ancestry() -> LanguageSpec:
    """A LanguageSpec with a rich ancestors tuple."""
    return LanguageSpec(
        code="xx-complex",
        name="Complex Test Language",
        family="TestFamily",
        script="Latin",
        graphemes={"a": ["a"], "b": ["b"]},
        allophones={"a": ["a"], "b": ["b"]},
        parent="yy-parent",
        ancestors=(
            Ancestor("yy-parent", AncestorRole.PARENT, 0.80, "Primary descent"),
            Ancestor("zz-sub", AncestorRole.SUBSTRATE, 0.10, "Substrate lang"),
            Ancestor("ww-sup", AncestorRole.SUPERSTRATE, 0.05, "Superstrate lang"),
            Ancestor("vv-ad", AncestorRole.ADSTRATE, 0.05, "Adstrate lang"),
        ),
    )


# ═══════════════════════════════════════════════════════════════════════════
# AncestorRole
# ═══════════════════════════════════════════════════════════════════════════

class TestAncestorRole:
    """Tests for the AncestorRole enum."""

    def test_all_roles_exist(self):
        expected = {"PARENT", "SUBSTRATE", "SUPERSTRATE", "ADSTRATE",
                    "LEXIFIER", "CREOLE_BASE"}
        actual = {r.name for r in AncestorRole}
        assert actual == expected

    def test_role_values(self):
        assert AncestorRole.PARENT.value == "parent"
        assert AncestorRole.SUBSTRATE.value == "substrate"
        assert AncestorRole.SUPERSTRATE.value == "superstrate"
        assert AncestorRole.ADSTRATE.value == "adstrate"
        assert AncestorRole.LEXIFIER.value == "lexifier"
        assert AncestorRole.CREOLE_BASE.value == "creole_base"


# ═══════════════════════════════════════════════════════════════════════════
# Ancestor
# ═══════════════════════════════════════════════════════════════════════════

class TestAncestor:
    """Tests for the Ancestor frozen dataclass."""

    def test_creation(self):
        a = Ancestor("la", AncestorRole.PARENT, 0.80, "Latin parent")
        assert a.code == "la"
        assert a.role == AncestorRole.PARENT
        assert a.weight == 0.80
        assert a.notes == "Latin parent"

    def test_defaults(self):
        a = Ancestor("la", AncestorRole.PARENT)
        assert a.weight == 0.5
        assert a.notes == ""

    def test_frozen(self):
        a = Ancestor("la", AncestorRole.PARENT, 0.80)
        with pytest.raises(FrozenInstanceError):
            a.code = "xx"

    def test_repr(self):
        a = Ancestor("la", AncestorRole.PARENT, 0.80)
        r = repr(a)
        assert "la" in r
        assert "parent" in r
        assert "0.80" in r

    def test_equality(self):
        a1 = Ancestor("la", AncestorRole.PARENT, 0.80, "note")
        a2 = Ancestor("la", AncestorRole.PARENT, 0.80, "note")
        assert a1 == a2

    def test_inequality(self):
        a1 = Ancestor("la", AncestorRole.PARENT, 0.80)
        a2 = Ancestor("la", AncestorRole.SUBSTRATE, 0.80)
        assert a1 != a2

    def test_hashable(self):
        """Ancestors must be hashable for use in sets and as dict keys."""
        a = Ancestor("la", AncestorRole.PARENT, 0.80)
        s = {a}
        assert a in s

    @pytest.mark.parametrize("weight", [0.0, 0.5, 1.0])
    def test_valid_weights(self, weight):
        a = Ancestor("la", AncestorRole.PARENT, weight)
        assert a.weight == weight


# ═══════════════════════════════════════════════════════════════════════════
# LanguageSpec — Basic properties
# ═══════════════════════════════════════════════════════════════════════════

class TestLanguageSpecBasic:
    """Basic LanguageSpec creation and field access."""

    def test_minimal_creation(self, minimal_spec):
        assert minimal_spec.code == "xx"
        assert minimal_spec.name == "Test Language"
        assert minimal_spec.family == "TestFamily"
        assert minimal_spec.script == "Latin"
        assert len(minimal_spec.graphemes) == 2
        assert len(minimal_spec.allophones) == 2

    def test_defaults(self, minimal_spec):
        assert minimal_spec.parent is None
        assert minimal_spec.ancestors == ()
        assert minimal_spec.notes == ""

    def test_frozen(self, minimal_spec):
        with pytest.raises(FrozenInstanceError):
            minimal_spec.code = "yy"

    def test_graphemes_type(self, minimal_spec):
        assert isinstance(minimal_spec.graphemes, dict)
        for k, v in minimal_spec.graphemes.items():
            assert isinstance(k, str)
            assert isinstance(v, list)
            for ipa in v:
                assert isinstance(ipa, str)

    def test_allophones_type(self, minimal_spec):
        assert isinstance(minimal_spec.allophones, dict)
        for k, v in minimal_spec.allophones.items():
            assert isinstance(k, str)
            assert isinstance(v, list)


# ═══════════════════════════════════════════════════════════════════════════
# LanguageSpec — Ancestry accessors
# ═══════════════════════════════════════════════════════════════════════════

class TestLanguageSpecAncestry:
    """Ancestry accessor methods and properties."""

    def test_no_ancestry(self, minimal_spec):
        assert minimal_spec.primary_parent is None
        assert minimal_spec.get_ancestors() == ()
        assert minimal_spec.substrate_codes == ()
        assert minimal_spec.superstrate_codes == ()
        assert minimal_spec.contact_codes == ()

    def test_parent_only_synthesises_ancestor(self, spec_with_parent):
        """When only `parent` is set, get_ancestors() synthesises a PARENT."""
        ancs = spec_with_parent.get_ancestors()
        assert len(ancs) == 1
        assert ancs[0].code == "xx"
        assert ancs[0].role == AncestorRole.PARENT
        assert ancs[0].weight == 1.0

    def test_primary_parent_from_parent_field(self, spec_with_parent):
        assert spec_with_parent.primary_parent == "xx"

    def test_primary_parent_from_ancestors(self, spec_with_full_ancestry):
        assert spec_with_full_ancestry.primary_parent == "yy-parent"

    def test_get_ancestors_all(self, spec_with_full_ancestry):
        ancs = spec_with_full_ancestry.get_ancestors()
        assert len(ancs) == 4

    def test_get_ancestors_by_role(self, spec_with_full_ancestry):
        parents = spec_with_full_ancestry.get_ancestors(AncestorRole.PARENT)
        assert len(parents) == 1
        assert parents[0].code == "yy-parent"

        subs = spec_with_full_ancestry.get_ancestors(AncestorRole.SUBSTRATE)
        assert len(subs) == 1
        assert subs[0].code == "zz-sub"

    def test_substrate_codes(self, spec_with_full_ancestry):
        assert spec_with_full_ancestry.substrate_codes == ("zz-sub",)

    def test_superstrate_codes(self, spec_with_full_ancestry):
        assert spec_with_full_ancestry.superstrate_codes == ("ww-sup",)

    def test_contact_codes(self, spec_with_full_ancestry):
        """contact_codes = all non-PARENT ancestor codes."""
        contact = spec_with_full_ancestry.contact_codes
        assert "zz-sub" in contact
        assert "ww-sup" in contact
        assert "vv-ad" in contact
        assert "yy-parent" not in contact

    def test_get_ancestors_empty_role(self, spec_with_full_ancestry):
        """Filtering by LEXIFIER should return empty tuple."""
        lexifiers = spec_with_full_ancestry.get_ancestors(AncestorRole.LEXIFIER)
        assert lexifiers == ()
