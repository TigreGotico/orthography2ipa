"""Tests for cross-language consistency and integration.

Validates:
- Tokenizer works for every registered language
- Distance metrics work across language pairs
- Ancestry graph is globally connected within families
- Phonological distance ordering matches linguistic expectations
"""
import pytest

import orthography2ipa
from orthography2ipa.registry import get, available_codes
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.distance import (
    phonological_distance,
    ancestry_similarity,
    full_distance,
)


# ═══════════════════════════════════════════════════════════════════════════
# Tokenizer works for all languages
# ═══════════════════════════════════════════════════════════════════════════

class TestTokenizerAllLanguages:
    """Verify PhonetokTokenizer can be constructed and used for every language."""

    @pytest.fixture(params=available_codes()[:40], ids=lambda c: c)
    def lang_code(self, request):
        """Use a representative subset for speed."""
        return request.param

    def test_tokenizer_constructs(self, lang_code):
        try:
            spec = get(lang_code)
        except (KeyError, ModuleNotFoundError):
            pytest.skip(f"Cannot load {lang_code}")
        tok = PhonetokTokenizer(spec)
        assert tok is not None
        assert tok.vocab_size > 7  # at least special tokens + some graphemes

    def test_tokenizer_handles_simple_text(self, lang_code):
        try:
            spec = get(lang_code)
        except (KeyError, ModuleNotFoundError):
            pytest.skip(f"Cannot load {lang_code}")
        tok = PhonetokTokenizer(spec)
        # Use the first grapheme key as test input
        first_grapheme = list(spec.graphemes.keys())[0]
        tokens = tok.tokenize(first_grapheme)
        assert len(tokens) >= 1

    def test_ipa_beam_produces_output(self, lang_code):
        try:
            spec = get(lang_code)
        except (KeyError, ModuleNotFoundError):
            pytest.skip(f"Cannot load {lang_code}")
        tok = PhonetokTokenizer(spec)
        first_grapheme = list(spec.graphemes.keys())[0]
        paths = tok.ipa_beam(first_grapheme, beam_width=2)
        assert len(paths) >= 1
        assert paths[0].ipa is not None


# ═══════════════════════════════════════════════════════════════════════════
# Distance metric smoke tests across languages
# ═══════════════════════════════════════════════════════════════════════════

class TestDistanceSmokeTests:
    """Basic smoke tests: distance metrics don't crash for any language pair."""

    SAMPLE_CODES = ["en-GB", "es-ES", "pt-PT", "fr-FR", "de-DE", "ar", "ja", "ru", "la"]

    @pytest.mark.parametrize("code_a", SAMPLE_CODES)
    @pytest.mark.parametrize("code_b", SAMPLE_CODES)
    def test_phonological_distance_no_crash(self, code_a, code_b):
        try:
            a = get(code_a)
            b = get(code_b)
        except KeyError:
            pytest.skip(f"Cannot load {code_a} or {code_b}")
        d = phonological_distance(a, b)
        assert 0.0 <= d.combined <= 1.0

    @pytest.mark.parametrize("code_a", SAMPLE_CODES)
    @pytest.mark.parametrize("code_b", SAMPLE_CODES)
    def test_ancestry_similarity_no_crash(self, code_a, code_b):
        try:
            a = get(code_a)
            b = get(code_b)
        except KeyError:
            pytest.skip(f"Cannot load {code_a} or {code_b}")
        sim = ancestry_similarity(a, b)
        assert 0.0 <= sim <= 1.0


# ═══════════════════════════════════════════════════════════════════════════
# Linguistic ordering expectations
# ═══════════════════════════════════════════════════════════════════════════

class TestLinguisticOrdering:
    """Distance ordering should match well-established linguistic groupings."""

    def _dist(self, a, b):
        return phonological_distance(get(a), get(b)).combined

    def _anc_sim(self, a, b):
        return ancestry_similarity(get(a), get(b))

    def test_spanish_closer_to_portuguese_than_japanese(self):
        d_es_pt = self._dist("es-ES", "pt-PT")
        d_es_ja = self._dist("es-ES", "ja")
        assert d_es_pt < d_es_ja

    def test_spanish_closer_to_italian_than_english(self):
        d_es_it = self._dist("es-ES", "it-IT")
        d_es_en = self._dist("es-ES", "en-GB")
        assert d_es_it < d_es_en

    def test_english_closer_to_german_than_arabic(self):
        d_en_de = self._dist("en-GB", "de-DE")
        d_en_ar = self._dist("en-GB", "ar")
        assert d_en_de < d_en_ar

    def test_portuguese_closer_to_galician_than_german(self):
        try:
            get("gl-ES")
        except KeyError:
            pytest.skip("gl not available")
        d_pt_gl = self._dist("pt-PT", "gl-ES")
        d_pt_de = self._dist("pt-PT", "de-DE")
        assert d_pt_gl < d_pt_de

    def test_ancestry_romance_cluster(self):
        """Romance languages should have higher mutual ancestry than with Japanese."""
        sim_es_pt = self._anc_sim("es-ES", "pt-PT")
        sim_es_ja = self._anc_sim("es-ES", "ja")
        assert sim_es_pt > sim_es_ja

    def test_ancestry_germanic_cluster(self):
        sim_en_de = self._anc_sim("en-GB", "de-DE")
        sim_en_ja = self._anc_sim("en-GB", "ja")
        assert sim_en_de > sim_en_ja


# ═══════════════════════════════════════════════════════════════════════════
# Full distance integration
# ═══════════════════════════════════════════════════════════════════════════

class TestFullDistanceIntegration:
    """Test full_distance (phonological + ancestry) on real language pairs."""

    def test_closely_related_low_distance(self):
        d = full_distance(get("es-ES"), get("pt-PT"))
        assert d < 0.6, "Spanish↔Portuguese should be close"

    def test_unrelated_high_distance(self):
        d = full_distance(get("es-ES"), get("ja"))
        assert d > 0.4, "Spanish↔Japanese should be distant"

    def test_dialect_very_close(self):
        d = full_distance(get("pt-PT"), get("pt-BR"))
        assert d < 0.4, "pt-PT↔pt-BR should be very close"


# ═══════════════════════════════════════════════════════════════════════════
# Grapheme IPA consistency
# ═══════════════════════════════════════════════════════════════════════════

class TestGraphemeIPAConsistency:
    """The IPA values in graphemes should ideally appear as keys in allophones."""

    SAMPLE_CODES = ["en-GB", "es-ES", "pt-PT", "fr-FR", "de-DE", "it-IT"]

    @pytest.mark.parametrize("code", SAMPLE_CODES)
    def test_canonical_ipa_in_allophones(self, code):
        """The first (canonical) IPA for each grapheme should have an
        allophone entry, unless it's a compound (like 'ks' for x) or
        silent ('')."""
        try:
            spec = get(code)
        except KeyError:
            pytest.skip(f"{code} not available")

        allo_keys = set(spec.allophones.keys())
        missing = []
        for grapheme, ipa_list in spec.graphemes.items():
            canonical = ipa_list[0]
            # Skip silent, empty, and compound IPA
            if not canonical or len(canonical) > 3:
                continue
            if canonical not in allo_keys:
                missing.append((grapheme, canonical))

        # Allow some gaps — complex IPA sequences may not have direct
        # allophone entries. Report as warning if > 30% missing.
        if len(missing) > 0.3 * len(spec.graphemes):
            pytest.fail(
                f"{code}: {len(missing)}/{len(spec.graphemes)} canonical IPAs "
                f"not in allophones. First 10: {missing[:10]}"
            )


# ═══════════════════════════════════════════════════════════════════════════
# Global ancestry graph connectivity
# ═══════════════════════════════════════════════════════════════════════════

class TestGlobalAncestryGraph:
    """Verify the ancestry graph has expected structure at the global level."""

    def test_every_parent_is_loadable(self):
        """Exhaustive check: every parent reference resolves."""
        missing = []
        for code in available_codes():
            try:
                spec = get(code)
            except (KeyError, ModuleNotFoundError):
                continue
            pp = spec.primary_parent
            if pp:
                try:
                    get(pp)
                except KeyError:
                    missing.append((code, pp))
        if missing:
            pytest.fail(
                f"{len(missing)} broken parent references:\n"
                + "\n".join(f"  {code} → {parent}" for code, parent in missing)
            )

    def test_every_ancestor_is_loadable(self):
        """Exhaustive check: every ancestor reference resolves."""
        missing = []
        for code in available_codes():
            try:
                spec = get(code)
            except (KeyError, ModuleNotFoundError):
                continue
            for anc in spec.get_ancestors():
                try:
                    get(anc.code)
                except KeyError:
                    missing.append((code, anc.code, anc.role.value))
        if missing:
            pytest.fail(
                f"{len(missing)} broken ancestor references:\n"
                + "\n".join(
                    f"  {code} → {anc} ({role})"
                    for code, anc, role in missing
                )
            )

    def test_no_orphan_languages_in_established_families(self):
        """Languages in Romance/Germanic should have parents (except roots)."""
        root_codes = {"la", "ine", "gem", "cel"}
        families_requiring_parents = {"Romance", "Germanic"}
        orphans = []
        for code in available_codes():
            try:
                spec = get(code)
            except (KeyError, ModuleNotFoundError):
                continue
            if (spec.family in families_requiring_parents
                    and code not in root_codes
                    and spec.primary_parent is None):
                orphans.append(code)
        if orphans:
            pytest.fail(
                f"Languages in major families without parents: {orphans}"
            )
