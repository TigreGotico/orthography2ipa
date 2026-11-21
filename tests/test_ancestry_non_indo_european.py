"""Ancestry enrichment round 2 — NON-Indo-European families.

Proves that the parent / substrate / superstrate / adstrate metadata added to the
non-Indo-European families in this round (Afro-Asiatic, Uralic, Dravidian,
Sino-Tibetan, Japonic, Koreanic, Austronesian, Kartvelian, Mongolic,
Austroasiatic, Tai-Kadai, Niger-Congo and the Basque isolate) resolves cleanly:

* every referenced ancestor code is an actual registered spec file (no dangling
  references that would silently fuzzy-resolve to a wrong node), and
* the ancestry graph builds and ``ancestry_similarity`` runs without raising
  (i.e. no ancestry cycle was introduced — e.g. the ``th`` <-> ``km`` and
  ``fi`` <-> ``sv`` mutual-adstrate loops that were explicitly avoided).
"""
import pytest

from orthography2ipa.registry import get, available_json_codes
from orthography2ipa.distance import ancestry_similarity, _build_ancestor_graph
from orthography2ipa.types import AncestorRole

# Modern specs whose ancestry was enriched this round.
ENRICHED = [
    # Afro-Asiatic (Semitic / Berber / Egyptian-Coptic / Chadic)
    "ar", "he", "am", "ti", "mt", "ber", "cop", "ha",
    # Uralic
    "fi", "et", "hu", "se",
    # Dravidian (parent field set)
    "ta", "te", "kn", "ml",
    # Sino-Tibetan
    "zh", "bo", "my",
    # Japonic / Koreanic
    "ja", "ko",
    # Austronesian
    "id", "ms", "tl", "jv",
    # Kartvelian / Mongolic
    "ka", "mn",
    # Austroasiatic / Tai-Kadai
    "vi", "km", "th", "lo",
    # Niger-Congo / isolate
    "sw", "zu", "yo", "ig", "eu",
]

# Structural proto / contact stubs created this round.
STUBS = [
    "urj", "sit", "och", "ltc", "jpx", "ojp", "ain", "pko", "poz", "ccs",
    "xgn", "tai", "nic", "bnt", "khi", "cdc", "cus", "egy", "gez",
    "sem-x-ethiopic", "arc",
]


@pytest.fixture(params=ENRICHED + STUBS, ids=lambda c: c)
def spec(request):
    return request.param, get(request.param)


def test_spec_loads(spec):
    code, s = spec
    assert s.code == code


def test_every_ancestor_code_is_a_real_file(spec):
    """No dangling references — each ancestor code must be an EXACT registered
    spec file, not a fuzzy ``closest_lang`` match that would corrupt the
    phylogenetic distance graph."""
    code, s = spec
    available = set(available_json_codes())
    for anc in s.get_ancestors():
        assert anc.code in available, (
            f"{code}: ancestor {anc.code!r} ({anc.role.value}) is not an exact "
            f"registered spec file — dangling / fuzzy-resolved reference")


def test_ancestry_graph_builds_without_cycle(spec):
    code, _ = spec
    graph = _build_ancestor_graph(code)  # raises ValueError on a cycle
    assert code in graph


def test_enriched_modern_specs_have_a_parent(spec):
    code, s = spec
    if code in ENRICHED:
        assert s.parent, f"{code}: enriched modern spec must set a parent"


def test_similarity_runs_pairwise():
    """Representative cross-family pairs — must not raise and stay in [0, 1]."""
    pairs = [
        ("ja", "ko"), ("sw", "zu"), ("th", "lo"), ("am", "ti"),
        ("fi", "et"), ("vi", "km"), ("id", "ms"), ("ja", "sw"),
        ("eu", "ka"), ("ar", "he"), ("bo", "my"), ("zh", "ja"),
    ]
    for a, b in pairs:
        sim = ancestry_similarity(get(a), get(b))
        assert 0.0 <= sim <= 1.0


def test_textbook_strata_present():
    """A few load-bearing contact strata are actually encoded."""
    # Coptic substrate is referenced by Egyptian Arabic; Greek adstrate on Coptic.
    assert "grc" in {a.code for a in get("cop").get_ancestors(AncestorRole.ADSTRATE)}
    # Khoisan click substrate in Zulu.
    assert "khi" in {a.code for a in get("zu").get_ancestors(AncestorRole.SUBSTRATE)}
    # Cushitic substrate in Amharic.
    assert "cus" in {a.code for a in get("am").get_ancestors(AncestorRole.SUBSTRATE)}
    # Middle Chinese (Sino-Xenic) adstrate on Japanese, Korean and Vietnamese.
    for code in ("ja", "ko", "vi"):
        assert "ltc" in {a.code for a in get(code).get_ancestors(AncestorRole.ADSTRATE)}
