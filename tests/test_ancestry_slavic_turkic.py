"""Ancestry enrichment round 1 — Slavic and Turkic strata.

Proves that the parent / substrate / superstrate / adstrate metadata added to
the Slavic and Turkic families in this round resolves cleanly:

* every referenced ancestor code is an actual registered spec file (no
  dangling references that would silently fuzzy-resolve to a wrong node), and
* the ancestry graph builds and ``ancestry_similarity`` runs without raising
  (i.e. no ancestry cycle regressions such as the ``tr`` <-> ``el`` loop).
"""
import pytest

from orthography2ipa.registry import ancestry_chain
from orthography2ipa.registry import get, available_json_codes
from orthography2ipa.distance import ancestry_similarity, _build_ancestor_graph
from orthography2ipa.types import AncestorRole

# Every spec whose ancestry was enriched in this round, plus the Proto-Turkic
# structural stub created to root the Turkic parent chain.
ENRICHED = [
    # Slavic
    "bg", "mk", "sr", "hr", "sl", "cs", "sk", "pl",
    "csb", "szl", "hsb", "dsb", "rue", "be", "uk", "ru",
    # Turkic
    "tr", "az", "tk", "uz", "kk", "ky", "tt", "ba", "cv",
    # new structural ancestry-node stub
    "trk",
]


@pytest.fixture(params=ENRICHED, ids=lambda c: c)
def spec(request):
    return request.param, get(request.param)


def test_enriched_specs_load(spec):
    code, s = spec
    assert s.code == code


def test_every_ancestor_code_is_a_real_file(spec):
    """No dangling references. The ancestor code must be an EXACT registered
    spec file, not merely something the fuzzy ``closest_lang`` resolver maps
    to a nearby node — that would corrupt the phylogenetic distance graph."""
    code, s = spec
    available = set(available_json_codes())
    for anc in s.get_ancestors():
        assert anc.code in available, (
            f"{code}: ancestor {anc.code!r} ({anc.role.value}) is not an exact "
            f"registered spec file — dangling / fuzzy-resolved reference")


def test_ancestry_graph_builds_without_cycle(spec):
    code, _ = spec
    graph = _build_ancestor_graph(code)
    assert code in graph


def test_turkic_roots_at_proto_turkic(spec):
    code, s = spec
    if code in {"tr", "az", "tk", "uz", "kk", "ky", "tt", "ba", "cv"}:
        assert s.parent == "trk"
        assert "trk" in {a.code for a in s.get_ancestors(AncestorRole.PARENT)}


def test_slavic_roots_at_proto_slavic(spec):
    code, s = spec
    if code in {"bg", "mk", "sr", "hr", "sl", "cs", "sk", "pl",
                "csb", "szl", "hsb", "dsb", "rue", "be", "uk", "ru"}:
        # Each hangs under its East/West/South Slavic clade node, which in turn
        # hangs under Proto-Slavic: `sla` stays on the chain.
        assert "sla" in ancestry_chain(code)


def test_similarity_runs_pairwise():
    """A few representative pairs — must not raise and must be in [0, 1]."""
    pairs = [("tr", "az"), ("ru", "pl"), ("bg", "tr"), ("cs", "sk"),
             ("tr", "fa"), ("uz", "kk")]
    for a, b in pairs:
        sim = ancestry_similarity(get(a), get(b))
        assert 0.0 <= sim <= 1.0
