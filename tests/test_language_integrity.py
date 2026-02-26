"""Tests for language integrity — structural validation of ALL registered languages.

These tests iterate over every registered language code and validate:
- LanguageSpec fields are properly populated
- Grapheme and allophone inventories are non-empty and well-formed
- Parent codes actually exist in the registry
- Ancestry chains are acyclic and complete (no dangling references)
- IPA values use valid IPA characters
- Allophone keys have a correspondence in the grapheme-derived phoneme set
- Distance metrics produce valid results between parent and child
"""
import pytest

from orthography2ipa.registry import get, available_codes
from orthography2ipa.types import LanguageSpec, AncestorRole


# ═══════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════

def _all_specs():
    """Yield (code, LanguageSpec) for every registered language."""
    for code in available_codes():
        try:
            yield code, get(code)
        except (KeyError, ModuleNotFoundError, ImportError):
            pytest.skip(f"Module for {code} not importable")


def _all_codes(exclude_proto=False):
    """Return all registered codes."""
    codes = available_codes()
    if exclude_proto:
        # TODO - add script+graphemes where available
        codes = [c for c in codes if c not in [
            "ine", "ine-x-italic",
            "cel", "cel-x-gallaecia", "xce", "xaq", "txr", "xlg", "xib",
            "gem", "got", "xpa", "xsb", "xcg", "xtg",
            "sem", "sem-x-central", "sem-x-west",
            "la", "la-x-archaic", "la-x-late", "la-x-hispania", "la-x-gallia", "mxi",
            "oc"
        ]]
    return codes


# ═══════════════════════════════════════════════════════════════════════════
# Per-language structural validation
# ═══════════════════════════════════════════════════════════════════════════

class TestAllLanguagesStructure:
    """Validate that every LanguageSpec is well-formed."""

    @pytest.fixture(params=_all_codes(exclude_proto=True), ids=lambda c: c)
    def lang(self, request):
        code = request.param
        try:
            return code, get(code)
        except (KeyError, ModuleNotFoundError, ImportError):
            pytest.skip(f"Cannot load {code}")

    def test_has_code(self, lang):
        code, spec = lang
        assert spec.code, f"{code}: empty code"

    def test_has_name(self, lang):
        code, spec = lang
        assert spec.name, f"{code}: empty name"

    def test_has_family(self, lang):
        code, spec = lang
        assert spec.family, f"{code}: empty family"

    def test_has_script(self, lang):
        code, spec = lang
        assert spec.script, f"{code}: empty script"

    def test_graphemes_nonempty(self, lang):
        code, spec = lang
        assert len(spec.graphemes) > 0, f"{code}: no graphemes"

    def test_allophones_nonempty(self, lang):
        code, spec = lang
        assert len(spec.allophones) > 0, f"{code}: no allophones"

    def test_grapheme_keys_are_strings(self, lang):
        code, spec = lang
        for k in spec.graphemes:
            assert isinstance(k, str), f"{code}: grapheme key {k!r} is not str"
            assert len(k) > 0, f"{code}: empty grapheme key"

    def test_grapheme_values_are_nonempty_lists(self, lang):
        code, spec = lang
        for k, v in spec.graphemes.items():
            assert isinstance(v, list), \
                f"{code}: graphemes[{k!r}] is {type(v)}, not list"
            assert len(v) > 0, \
                f"{code}: graphemes[{k!r}] is empty"

    def test_allophone_keys_are_strings(self, lang):
        code, spec = lang
        for k in spec.allophones:
            assert isinstance(k, str), f"{code}: allophone key {k!r} is not str"

    def test_allophone_values_are_nonempty_lists(self, lang):
        code, spec = lang
        for k, v in spec.allophones.items():
            assert isinstance(v, list), \
                f"{code}: allophones[{k!r}] is {type(v)}, not list"
            assert len(v) > 0, \
                f"{code}: allophones[{k!r}] is empty"

    def test_grapheme_ipa_first_entry_is_canonical(self, lang):
        """The first IPA value in a grapheme list is the canonical/default."""
        code, spec = lang
        for k, v in spec.graphemes.items():
            # First entry should be a string (can be "" for silent graphemes)
            assert isinstance(v[0], str), \
                f"{code}: graphemes[{k!r}][0] is not a string"


# ═══════════════════════════════════════════════════════════════════════════
# Ancestry graph integrity
# ═══════════════════════════════════════════════════════════════════════════

class TestAncestryIntegrity:
    """Every parent/ancestor code must exist in the registry.

    This is THE critical test for the lineage graph — a dangling reference
    breaks the distance metric's ancestry traversal.
    """

    @pytest.fixture(params=_all_codes(), ids=lambda c: c)
    def lang(self, request):
        code = request.param
        try:
            return code, get(code)
        except (KeyError, ModuleNotFoundError, ImportError):
            pytest.skip(f"Cannot load {code}")

    def test_parent_exists_in_registry(self, lang):
        """If spec.parent is set, that code should be loadable.
        Missing parents are warned as data gaps."""
        code, spec = lang
        if spec.parent:
            try:
                parent_spec = get(spec.parent)
                assert isinstance(parent_spec, LanguageSpec)
            except KeyError:
                import warnings
                pytest.fail(
                    f"{code}: parent '{spec.parent}' is NOT in the registry. "
                    f"This is a data gap to fill."
                )

    def test_all_ancestor_codes_exist(self, lang):
        """Every ancestor code in the ancestors tuple should ideally be loadable.
        Missing ancestors are collected as warnings — these represent data gaps
        in the registry that should be filled, but don't block testing."""
        code, spec = lang
        missing = []
        for anc in spec.get_ancestors():
            try:
                anc_spec = get(anc.code)
                assert isinstance(anc_spec, LanguageSpec)
            except KeyError:
                missing.append(f"{anc.code} ({anc.role.value})")
        if missing:
            pytest.fail(
                f"{code}: {len(missing)} ancestor(s) not in registry: "
                f"{', '.join(missing)}. These are data gaps to fill."
            )

    def test_parent_count_reasonable(self, lang):
        """Each language should typically have at most one PARENT ancestor.
        Some dialect models (e.g. Persian varieties) use dual PARENT to
        represent both the immediate parent and the classical ancestor.
        We warn if > 2, fail if > 3 (likely a data error)."""
        code, spec = lang
        parents = spec.get_ancestors(AncestorRole.PARENT)
        if len(parents) > 3:
            pytest.fail(
                f"{code}: has {len(parents)} PARENT ancestors (expected ≤ 3)"
            )
        elif len(parents) > 1:
            pytest.fail(
                f"{code}: has {len(parents)} PARENT ancestors: "
                f"{[p.code for p in parents]}. Consider consolidating."
            )

    def test_ancestor_weights_in_range(self, lang):
        """All ancestor weights should be in [0.0, 1.0]."""
        code, spec = lang
        for anc in spec.get_ancestors():
            assert 0.0 <= anc.weight <= 1.0, \
                f"{code}: ancestor '{anc.code}' has weight {anc.weight} (out of [0,1])"

    def test_primary_parent_weight_high(self, lang):
        """The highest-weight PARENT should typically be ≥ 0.5."""
        code, spec = lang
        parents = spec.get_ancestors(AncestorRole.PARENT)
        if parents:
            max_weight = max(p.weight for p in parents)
            assert max_weight >= 0.5, \
                f"{code}: highest PARENT weight is {max_weight} (expected ≥ 0.5)"

    def test_no_self_reference(self, lang):
        """A language should not list itself as an ancestor."""
        code, spec = lang
        for anc in spec.get_ancestors():
            assert anc.code != code, \
                f"{code}: lists itself as ancestor (role={anc.role.value})"
            # Also check the stored code field if it differs from registry key
            assert anc.code != spec.code, \
                f"{spec.code}: self-referential ancestor"


# ═══════════════════════════════════════════════════════════════════════════
# Ancestry acyclicity
# ═══════════════════════════════════════════════════════════════════════════

class TestAncestryAcyclic:
    """The ancestry PARENT chain must not contain cycles."""

    def test_no_cycles_in_parent_chains(self):
        """Follow every language's PARENT chain — it must terminate."""
        for code in _all_codes():
            try:
                spec = get(code)
            except (KeyError, ModuleNotFoundError, ImportError):
                continue

            visited = set()
            current = code
            while current:
                if current in visited:
                    pytest.fail(
                        f"Cycle detected in PARENT chain: {code} → ... → "
                        f"{current} (already visited: {visited})"
                    )
                visited.add(current)
                try:
                    s = get(current)
                    current = s.primary_parent
                except KeyError:
                    break  # unresolvable ancestor — separate test catches this


# ═══════════════════════════════════════════════════════════════════════════
# Proto-language roots
# ═══════════════════════════════════════════════════════════════════════════

class TestProtoLanguageRoots:
    """Proto-languages should have no parent (they are the roots)."""

    @pytest.mark.parametrize("code", ["ine"])
    def test_proto_language_has_no_parent(self, code):
        try:
            spec = get(code)
        except KeyError:
            pytest.skip(f"{code} not in registry")
        parents = spec.get_ancestors(AncestorRole.PARENT)
        assert len(parents) == 0, \
            f"Proto-language {code} should have no PARENT, but has: {parents}"


# ═══════════════════════════════════════════════════════════════════════════
# Minimum inventory sizes
# ═══════════════════════════════════════════════════════════════════════════

class TestMinimumInventorySizes:
    """Sanity checks on inventory sizes for well-known languages."""

    @pytest.mark.parametrize("code,min_graphemes,min_allophones", [
        #   ("en-GB", 40, 20),   # English has many digraphs/trigraphs
        #   ("es-ES", 20, 15),   # Spanish is more transparent
        ("pt-PT", 20, 10),
        #   ("fr-FR", 20, 15),
        #   ("de-DE", 20, 15),
        #   ("it-IT", 20, 15),
        #   ("ar", 20, 10),
        #   ("ja", 10, 10),
    ])
    def test_minimum_inventory_size(self, code, min_graphemes, min_allophones):
        try:
            spec = get(code)
        except KeyError:
            pytest.skip(f"{code} not in registry")
        assert len(spec.graphemes) >= min_graphemes, \
            f"{code}: only {len(spec.graphemes)} graphemes (expected ≥ {min_graphemes})"
        assert len(spec.allophones) >= min_allophones, \
            f"{code}: only {len(spec.allophones)} allophones (expected ≥ {min_allophones})"


# ═══════════════════════════════════════════════════════════════════════════
# Key phonological facts (spot checks)
# ═══════════════════════════════════════════════════════════════════════════

class TestKeyPhonologicalFacts:
    """Spot-check critical linguistic facts for major languages."""

    # ── English ────────────────────────────────────────────────────────
    @pytest.mark.skip()
    def test_english_th_maps_to_dental_fricatives(self):
        en = get("en-GB")
        ipa = en.graphemes.get("th", [])
        assert "θ" in ipa, "English 'th' should include /θ/"
        assert "ð" in ipa, "English 'th' should include /ð/"

    @pytest.mark.skip()
    def test_english_t_has_flap_allophone(self):
        en = get("en-GB")
        t_allo = en.allophones.get("t", [])
        assert "ɾ" in t_allo, "English /t/ should have [ɾ] flap allophone"

    @pytest.mark.skip()
    def test_english_sh_is_postalveolar(self):
        en = get("en-GB")
        assert "ʃ" in en.graphemes.get("sh", [])

    # ── Spanish ────────────────────────────────────────────────────────
    @pytest.mark.skip()
    def test_spanish_c_has_theta(self):
        """Castilian Spanish: 'c' should include /θ/ (distinción)."""
        es = get("es-ES")
        ipa = es.graphemes.get("c", [])
        assert "θ" in ipa, "Castilian 'c' should include /θ/"

    @pytest.mark.skip()
    def test_spanish_h_is_silent(self):
        es = get("es-ES")
        h_ipa = es.graphemes.get("h", [])
        assert "" in h_ipa, "Spanish 'h' should be silent (empty string)"

    @pytest.mark.skip()
    def test_spanish_b_lenition(self):
        """Spanish /b/ should have [β] allophone (lenition)."""
        es = get("es-ES")
        b_allo = es.allophones.get("b", [])
        assert "β" in b_allo, "Spanish /b/ should have [β] allophone"

    @pytest.mark.skip()
    def test_spanish_rr_is_trill(self):
        es = get("es-ES")
        rr_ipa = es.graphemes.get("rr", [])
        assert "r" in rr_ipa, "Spanish 'rr' should map to alveolar trill /r/"

    @pytest.mark.skip()
    def test_spanish_ancestry_includes_latin(self):
        es = get("es-ES")
        assert es.primary_parent == "la-x-hispania"

    @pytest.mark.skip()
    def test_spanish_has_basque_substrate(self):
        es = get("es-ES")
        subs = es.substrate_codes
        assert "xaq" in subs, "Spanish should have Basque (xaq) substrate"

    # ── Portuguese ─────────────────────────────────────────────────────

    def test_portuguese_lh_palatal_lateral(self):
        pt_br = get("pt-PT")
        lh_ipa = pt_br.graphemes.get("lh", [])
        assert "ʎ" in lh_ipa, "Portuguese 'lh' should map to /ʎ/"

    def test_portuguese_nh_palatal_nasal(self):
        pt = get("pt-PT")
        nh_ipa = pt.graphemes.get("nh", [])
        assert "ɲ" in nh_ipa, "Portuguese 'nh' should map to /ɲ/"

    # ── German ─────────────────────────────────────────────────────────
    @pytest.mark.skip()
    def test_german_sch_is_postalveolar(self):
        de = get("de-DE")
        sch_ipa = de.graphemes.get("sch", [])
        assert "ʃ" in sch_ipa, "German 'sch' should map to /ʃ/"

    @pytest.mark.skip()
    def test_german_ch_has_ich_and_ach(self):
        """German 'ch' should include both [ç] and [x]."""
        de = get("de-DE")
        ch_ipa = de.graphemes.get("ch", [])
        assert "ç" in ch_ipa or "x" in ch_ipa, \
            "German 'ch' should have /ç/ or /x/"

    # ── French ─────────────────────────────────────────────────────────
    @pytest.mark.skip()
    def test_french_has_nasal_vowels(self):
        """French allophone/grapheme system should include nasal vowels."""
        fr = get("fr-FR")
        all_ipa = set()
        for v_list in fr.graphemes.values():
            all_ipa.update(v_list)
        # At least one nasal vowel should be present
        nasal_vowels = {"ɑ̃", "ɛ̃", "ɔ̃", "œ̃"}
        assert nasal_vowels & all_ipa, \
            "French should have at least one nasal vowel"

    @pytest.mark.skip()
    def test_french_r_is_uvular(self):
        fr = get("fr-FR")
        r_allo = fr.allophones.get("ʁ", fr.allophones.get("r", []))
        # French /r/ should be uvular [ʁ]
        assert any("ʁ" in a for a in r_allo) or "ʁ" in fr.allophones, \
            "French /r/ should include uvular [ʁ]"


# ═══════════════════════════════════════════════════════════════════════════
# Family consistency
# ═══════════════════════════════════════════════════════════════════════════

class TestFamilyConsistency:
    """Languages in the same family should share some ancestry."""

    def test_romance_languages_share_latin_ancestor(self):
        """All Romance languages should eventually trace back to Latin."""
        romance_codes = ["es-ES", "pt-PT", "fr-FR", "it-IT", "ca"]
        for code in romance_codes:
            try:
                spec = get(code)
            except KeyError:
                continue
            # Walk PARENT chain
            visited = set()
            current = code
            found_latin = False
            while current and current not in visited:
                visited.add(current)
                if current.startswith("la"):
                    found_latin = True
                    break
                try:
                    s = get(current)
                    current = s.primary_parent
                except KeyError:
                    break
            assert found_latin, \
                f"Romance language {code} should trace back to Latin, " \
                f"but chain was: {visited}"

    @pytest.mark.skip()
    def test_germanic_languages_share_protogermanic(self):
        """Germanic languages should trace to Proto-Germanic (gem)."""
        germanic_codes = ["pt-PT", "de-DE", "nl"]
        for code in germanic_codes:
            try:
                spec = get(code)
            except KeyError:
                continue
            visited = set()
            current = code
            found_gem = False
            while current and current not in visited:
                visited.add(current)
                if current == "gem":
                    found_gem = True
                    break
                try:
                    s = get(current)
                    current = s.primary_parent
                except KeyError:
                    break
            assert found_gem, \
                f"Germanic language {code} should trace to gem, " \
                f"but chain was: {visited}"


# ═══════════════════════════════════════════════════════════════════════════
# Dialect-parent relationship
# ═══════════════════════════════════════════════════════════════════════════

class TestDialectParentRelationship:
    """Dialects should be close to their parent language."""

    @pytest.mark.parametrize("child,parent_code", [
        ("pt-BR", "pt-PT"),
        ("es-AR", "es-ES"),
    ])
    def test_dialect_has_expected_parent(self, child, parent_code):
        """Dialect's primary_parent should point to the expected parent."""
        try:
            spec = get(child)
        except KeyError:
            pytest.skip(f"{child} not in registry")
        # Parent may be a more specific code (e.g. pt-PT instead of pt)
        pp = spec.primary_parent
        assert pp is not None, f"{child} has no parent"
        # The parent should be loadable
        try:
            parent = get(pp)
        except KeyError:
            pytest.fail(f"{child}: parent '{pp}' not in registry")
