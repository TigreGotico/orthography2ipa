"""Ancestry / distance scaffolding tests for Latin American Spanish stubs.

Every LatAm national and major regional dialect zone (Lipski 1994, as
summarised in Lipski's "Geographical and Social Varieties of Spanish: An
Overview") has at least a STUB spec wired into a weighted ancestry chain

    es-ES-x-medieval -> es-ES -> es-419 -> {country} -> {region}

plus the relevant indigenous ADSTRATE(s). The indigenous contact languages
(gn, qu, ay, nah, arn, yua, quc) are structural adstrate stubs (no invented
phonology), so the phylogenetic / distance metrics resolve without any
missing-spec KeyError.
"""
import pytest

import orthography2ipa
from orthography2ipa import get, phonological_distance
from orthography2ipa.types import QualityTier, AncestorRole
from orthography2ipa.distance import (
    ancestry_similarity,
    _get_ancestry_weights_by_code,
)

ADSTRATE_STUBS = ["gn", "qu", "ay", "nah", "arn", "yua", "quc"]

REGIONAL_STUBS = [
    "es-AR-x-cordoba", "es-AR-x-cuyo", "es-AR-x-norte", "es-AR-x-patagonia",
    "es-AR-x-litoral",
    "es-MX-x-norte", "es-MX-x-yucatan",
    "es-CO-x-santander", "es-CO-x-valluno", "es-CO-x-llanero", "es-CO-x-pacifico",
    "es-PE-x-andino", "es-PE-x-amazonico",
    "es-CL-x-andino", "es-CL-x-chilote",
    "es-VE-x-maracucho", "es-VE-x-andino", "es-VE-x-llanero",
    "es-BO-x-andino", "es-BO-x-camba",
    "es-EC-x-andino", "es-EC-x-costa",
]

NEW_NATIONALS = ["es-HN", "es-SV"]

# region code -> expected indigenous adstrate codes
REGION_ADSTRATE = {
    "es-AR-x-norte": {"qu"},
    "es-AR-x-patagonia": {"arn"},
    "es-AR-x-litoral": {"gn"},
    "es-MX-x-yucatan": {"yua"},
    "es-PE-x-andino": {"qu", "ay"},
    "es-CL-x-andino": {"ay"},
    "es-CL-x-chilote": {"arn"},
    "es-BO-x-andino": {"qu", "ay"},
    "es-BO-x-camba": {"gn"},
    "es-EC-x-andino": {"qu"},
}


# ---------------------------------------------------------------------------
# Every node resolves and is a stub with the right family
# ---------------------------------------------------------------------------
class TestNodesResolve:
    @pytest.mark.parametrize("code", ADSTRATE_STUBS + REGIONAL_STUBS + NEW_NATIONALS)
    def test_resolves(self, code):
        spec = get(code)
        assert spec is not None
        assert spec.code == code

    @pytest.mark.parametrize("code", ADSTRATE_STUBS + REGIONAL_STUBS + NEW_NATIONALS)
    def test_is_stub_tier(self, code):
        assert get(code).quality is QualityTier.STUB

    @pytest.mark.parametrize("code", REGIONAL_STUBS + NEW_NATIONALS)
    def test_spanish_is_romance(self, code):
        assert get(code).family == "Romance"

    @pytest.mark.parametrize("code", ADSTRATE_STUBS)
    def test_adstrate_nonempty_inventory(self, code):
        """Adstrate stubs carry a placeholder inventory (data-quality guard)."""
        spec = get(code)
        assert spec.graphemes
        assert spec.allophones


# ---------------------------------------------------------------------------
# Ancestry chains: parent role + es-419 + indigenous adstrate, no dangling refs
# ---------------------------------------------------------------------------
class TestRegionalAncestry:
    @pytest.mark.parametrize("code", REGIONAL_STUBS)
    def test_single_parent_is_country(self, code):
        spec = get(code)
        parents = spec.get_ancestors(AncestorRole.PARENT)
        assert len(parents) == 1
        # parent code is the national variety (e.g. es-AR for es-AR-x-norte)
        assert code.startswith(parents[0].code + "-x-")

    @pytest.mark.parametrize("code", REGIONAL_STUBS + NEW_NATIONALS)
    def test_es419_in_chain(self, code):
        weights = _get_ancestry_weights_by_code(code)
        assert "es-419" in weights

    @pytest.mark.parametrize("code", REGIONAL_STUBS + NEW_NATIONALS)
    def test_chain_reaches_medieval_castilian(self, code):
        """The full es-ES-x-medieval -> es-ES chain resolves transitively."""
        weights = _get_ancestry_weights_by_code(code)
        assert "es-ES" in weights
        assert "es-ES-x-medieval" in weights

    @pytest.mark.parametrize("code,expected", sorted(REGION_ADSTRATE.items()))
    def test_indigenous_adstrate_present(self, code, expected):
        adstrates = {a.code for a in get(code).get_ancestors(AncestorRole.ADSTRATE)}
        assert expected.issubset(adstrates)

    @pytest.mark.parametrize("code", REGIONAL_STUBS + NEW_NATIONALS)
    def test_no_dangling_ancestor(self, code):
        """Every ancestor code must resolve — no missing-spec KeyError."""
        for anc in get(code).get_ancestors():
            assert get(anc.code) is not None


# ---------------------------------------------------------------------------
# Augmented existing nationals keep their parent field but gain adstrates
# ---------------------------------------------------------------------------
class TestNationalAugmentation:
    def test_es_mx_parent_field_preserved(self):
        # test_iberian_extended asserts es-MX/es-CL/es-VE/es-419 parent == es-ES
        assert get("es-MX").parent == "es-ES"
        assert get("es-CL").parent == "es-ES"

    @pytest.mark.parametrize("code,expected", [
        ("es-MX", {"nah", "yua"}),
        ("es-PE", {"qu", "ay"}),
        ("es-BO", {"qu", "ay"}),
        ("es-CL", {"arn"}),
        ("es-PY", {"gn"}),
        ("es-GT", {"quc"}),
    ])
    def test_national_indigenous_adstrate(self, code, expected):
        adstrates = {a.code for a in get(code).get_ancestors(AncestorRole.ADSTRATE)}
        assert expected.issubset(adstrates)

    def test_paraguay_guarani_weight_is_strong(self):
        gn = [a for a in get("es-PY").get_ancestors(AncestorRole.ADSTRATE)
              if a.code == "gn"][0]
        assert gn.weight >= 0.15


# ---------------------------------------------------------------------------
# Distance metrics run on the new stubs
# ---------------------------------------------------------------------------
class TestDistanceMetrics:
    def test_national_vs_castilian(self):
        d = phonological_distance(get("es-AR"), get("es-ES"))
        assert isinstance(d.combined, float)
        assert 0.0 <= d.combined <= 1.0

    def test_stub_vs_stub(self):
        d = phonological_distance(get("es-PE-x-andino"), get("es-BO-x-andino"))
        assert isinstance(d.combined, float)
        assert 0.0 <= d.combined <= 1.0

    def test_region_shares_adstrate_ancestry(self):
        """es-AR-x-litoral is ancestrally connected to Guaraní via adstrate."""
        assert ancestry_similarity(get("es-AR-x-litoral"), get("gn")) > 0.0

    def test_andean_regions_closer_than_to_unrelated(self):
        """Two Andean stubs (shared es-419 + Quechua/Aymara) are closer to each
        other than a highland stub is to an unrelated language (Basque)."""
        andean = ancestry_similarity(get("es-PE-x-andino"), get("es-BO-x-andino"))
        unrelated = ancestry_similarity(get("es-PE-x-andino"), get("eu"))
        assert andean > unrelated
