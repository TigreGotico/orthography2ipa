"""Ancestry enrichment round 2 — Indo-European strata.

Round 2 fills the remaining un-enriched *standard* Indo-European specs with a
weighted ``ancestors`` tuple (proto -> historical -> modern parent chain plus
textbook contact strata) and roots them consistently at the shared IE proto
nodes.  It also adds three metadata-only structural nodes referenced as
substrate/adstrate: Old Tupi (tpw), Kimbundu (kmb) and Proto-Dravidian (dra).

The test proves the added metadata resolves cleanly:

* every referenced ancestor code is an actual registered spec file (no
  dangling references that would silently fuzzy-resolve to a wrong node), and
* the ancestry graph builds and ``ancestry_similarity`` runs without raising
  (i.e. no ancestry cycle regressions).
"""
import pytest

from orthography2ipa.registry import get, available_json_codes
from orthography2ipa.distance import ancestry_similarity, _build_ancestor_graph

# Specs enriched in this round plus the new structural stubs.
ENRICHED = [
    # Romance
    "es-ES", "ca", "pt-BR",
    # Germanic
    "nb",
    # Indo-Aryan / Iranian
    "hi", "fa",
    # new metadata-only structural nodes
    "tpw", "kmb", "dra",
]


@pytest.fixture(params=ENRICHED, ids=lambda c: c)
def spec(request):
    return request.param, get(request.param)


def test_enriched_specs_load(spec):
    code, s = spec
    assert s.code == code


def test_every_ancestor_code_is_a_real_file(spec):
    """No dangling references. Each ancestor code must be an EXACT registered
    spec file, not merely something the fuzzy resolver maps to a nearby node."""
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


def test_similarity_runs_pairwise():
    """Representative pairs — must not raise and must be in [0, 1]."""
    pairs = [
        ("es-ES", "ca"), ("es-ES", "pt-BR"), ("hi", "fa"),
        ("hi", "ur"), ("nb", "da"), ("fa", "ar"), ("ca", "oc"),
    ]
    for a, b in pairs:
        sim = ancestry_similarity(get(a), get(b))
        assert 0.0 <= sim <= 1.0
