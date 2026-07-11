"""Ancestry-chain tests for kab (Kabyle) and its Berber ancestor stubs.

kab is wired into the Glottolog Berber tree so the phylogenetic /
ancestry-weighted distance metrics have a chain to traverse:

    kab -> ber-x-kabyle-atlas -> ber -> afa   (+ ar adstrate)

(Afro-Asiatic afro1255 > Berber berb1260 > Kabyle-Atlas Berber kaby1244 >
Kabyle kaby1243). The intermediate/top nodes ber-x-kabyle-atlas and afa are
structural STUB specs (no invented phonology).
"""
import pytest

import orthography2ipa
from orthography2ipa import phonological_distance
from orthography2ipa.types import QualityTier, AncestorRole
from orthography2ipa.distance import (
    ancestry_similarity,
    _build_ancestor_graph,
    _get_ancestry_weights_by_code,
)


@pytest.fixture(scope="module")
def kab():
    return orthography2ipa.get("kab")


# ---------------------------------------------------------------------------
# Every node in kab's chain resolves as a registered spec
# ---------------------------------------------------------------------------

class TestChainResolves:
    @pytest.mark.parametrize("code", ["kab", "ber-x-kabyle-atlas", "ber", "afa"])
    def test_node_resolves(self, code):
        spec = orthography2ipa.get(code)
        assert spec is not None
        assert spec.code == code

    @pytest.mark.parametrize("code", ["ber-x-kabyle-atlas", "afa"])
    def test_stub_tier(self, code):
        assert orthography2ipa.get(code).quality is QualityTier.STUB

    def test_stub_glottocodes(self):
        assert orthography2ipa.get("afa").glottolog_code == "afro1255"
        assert orthography2ipa.get("ber-x-kabyle-atlas").glottolog_code == "kaby1244"

    def test_stubs_are_afroasiatic(self):
        assert orthography2ipa.get("afa").family == "Afro-Asiatic"
        assert orthography2ipa.get("ber-x-kabyle-atlas").family == "Afro-Asiatic > Berber"


# ---------------------------------------------------------------------------
# kab's parent + weighted ancestors
# ---------------------------------------------------------------------------

class TestKabAncestry:
    def test_parent(self, kab):
        assert kab.parent == "ber-x-kabyle-atlas"

    def test_ancestors_present(self, kab):
        codes = {a.code for a in kab.get_ancestors()}
        assert "ber-x-kabyle-atlas" in codes
        assert "ar" in codes

    def test_primary_parent_role(self, kab):
        parents = kab.get_ancestors(AncestorRole.PARENT)
        assert [a.code for a in parents] == ["ber-x-kabyle-atlas"]

    def test_arabic_is_adstrate(self, kab):
        adstrates = {a.code for a in kab.get_ancestors(AncestorRole.ADSTRATE)}
        assert "ar" in adstrates

    def test_intermediate_links_up(self):
        assert orthography2ipa.get("ber-x-kabyle-atlas").parent == "ber"
        assert orthography2ipa.get("ber").parent == "afa"
        assert orthography2ipa.get("afa").parent is None


# ---------------------------------------------------------------------------
# The ancestry graph traverses the full chain (no missing-spec / KeyError)
# ---------------------------------------------------------------------------

class TestAncestryGraph:
    def test_graph_covers_full_chain(self):
        graph = _build_ancestor_graph("kab")
        for node in ("kab", "ber-x-kabyle-atlas", "ber", "afa", "ar"):
            assert node in graph
        assert ("ber-x-kabyle-atlas", 0.85) in graph["kab"]
        assert ("ber", 0.9) in graph["ber-x-kabyle-atlas"]
        assert ("afa", 0.85) in graph["ber"]
        assert graph["afa"] == []

    def test_weights_propagate_transitively(self):
        weights = _get_ancestry_weights_by_code("kab")
        # direct parent
        assert weights["ber-x-kabyle-atlas"] == pytest.approx(0.85)
        # transitive: 0.85 * 0.9
        assert weights["ber"] == pytest.approx(0.765)
        # transitive: 0.765 * 0.85
        assert weights["afa"] == pytest.approx(0.65025)
        assert weights["ar"] == pytest.approx(0.12)


# ---------------------------------------------------------------------------
# Distance metrics run on kab and reflect the ancestry chain
# ---------------------------------------------------------------------------

class TestDistanceMetrics:
    def test_phonological_distance_returns_valid_result(self, kab):
        d = phonological_distance(kab, orthography2ipa.get("ar"))
        assert isinstance(d.combined, float)
        assert 0.0 <= d.combined <= 1.0
        # a non-trivial multi-component result was produced
        assert d.inventory is not None
        assert isinstance(d.allophone_sim, float)

    def test_ancestry_similarity_immediate_parent(self, kab):
        sim = ancestry_similarity(kab, orthography2ipa.get("ber-x-kabyle-atlas"))
        assert sim == pytest.approx(0.85)

    def test_ancestry_similarity_transitive_grandparent(self, kab):
        sim = ancestry_similarity(kab, orthography2ipa.get("ber"))
        assert sim == pytest.approx(0.765)

    def test_ancestry_similarity_adstrate(self, kab):
        sim = ancestry_similarity(kab, orthography2ipa.get("ar"))
        assert sim == pytest.approx(0.12)

    def test_unrelated_language_zero_ancestry(self, kab):
        """A genetically unrelated language with no shared contact stratum has
        zero ancestry overlap with Kabyle. Finnish (Uralic) is used as the
        control: unlike Basque — which since round-2 enrichment carries a
        Romance/Andalusi-Arabic adstrate that faintly touches the Semitic node
        shared with Kabyle's Arabic adstrate — Finnish's ancestry tree
        (Proto-Uralic, Russian) never intersects Kabyle's."""
        assert ancestry_similarity(kab, orthography2ipa.get("fi")) == pytest.approx(0.0)

    def test_closer_ancestry_than_unrelated(self, kab):
        """kab is ancestrally closer to Berber than to Basque."""
        to_ber = ancestry_similarity(kab, orthography2ipa.get("ber"))
        to_eu = ancestry_similarity(kab, orthography2ipa.get("eu"))
        assert to_ber > to_eu
