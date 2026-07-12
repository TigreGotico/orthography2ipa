"""Clade nodes and the derived ``family`` field.

A clade (``Romance``, ``West Germanic``) is a classification-only node in the
ancestry graph: no phonology, never a data-inheritance source. ``family`` is
read off the clade nodes on a spec's parent chain rather than hand-maintained
in every JSON file.
"""
import json
import pathlib

import pytest

from orthography2ipa import get
from orthography2ipa.json_loader import load_all_json_specs
from orthography2ipa.registry import (
    ancestry_chain,
    available_codes,
    available_families,
)
from orthography2ipa.types import QualityTier

DATA_DIR = (pathlib.Path(__file__).parent.parent
            / "orthography2ipa" / "data")
ALL_SPECS = load_all_json_specs()
CLADES = sorted(code for code, spec in ALL_SPECS.items() if spec.clade)


# ═══════════════════════════════════════════════════════════════════════════
# Clade nodes are classification-only
# ═══════════════════════════════════════════════════════════════════════════

def test_clade_nodes_exist():
    assert len(CLADES) >= 50, "the classification backbone should be populated"


@pytest.mark.parametrize("code", CLADES)
def test_clade_carries_no_phonology(code):
    """A clade is not a language: it has nothing to transcribe with."""
    spec = get(code)
    assert not spec.graphemes, f"{code}: clade nodes carry no graphemes"
    assert not spec.allophones, f"{code}: clade nodes carry no allophones"
    assert not spec.sandhi_rules
    assert not spec.allophone_rules
    assert spec.quality is QualityTier.STUB


@pytest.mark.parametrize("code", CLADES)
def test_clade_is_cited(code):
    """Never fabricate a branch: every clade cites Wikipedia, and its
    Glottolog languoid whenever one with that membership exists."""
    raw = json.loads((DATA_DIR / f"{code}.json").read_text(encoding="utf-8"))
    assert raw["wikipedia"], f"{code}: no Wikipedia citation"
    assert raw["sources"], f"{code}: no source"
    if raw.get("glottolog_code") is None:
        # A glue node Glottolog does not carve the same way must say so.
        assert "Glottolog" in raw["notes"], (
            f"{code}: no glottolog_code and no note explaining why")


@pytest.mark.parametrize("code", CLADES)
def test_clade_is_never_a_data_base(code):
    """No spec may inherit data from a clade."""
    for other, raw_path in ((p.stem, p) for p in DATA_DIR.glob("*.json")):
        raw = json.loads(raw_path.read_text(encoding="utf-8"))
        for field in ("graphemes_base", "allophones_base",
                      "positional_graphemes_base"):
            assert raw.get(field) != code, (
                f"{other} inherits {field} from clade {code}")


def test_clades_are_not_listed_as_languages():
    assert not set(available_codes()) & set(CLADES)
    assert set(CLADES) <= set(available_codes(include_clades=True))


# ═══════════════════════════════════════════════════════════════════════════
# family is derived from the chain
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("code,expected", [
    ("pt-PT", ("Indo-European", "Italic", "Romance", "Ibero-Romance")),
    ("es-ES", ("Indo-European", "Italic", "Romance", "Ibero-Romance")),
    ("mwl", ("Indo-European", "Italic", "Romance", "Ibero-Romance",
             "Asturleonese")),
    ("it-IT", ("Indo-European", "Italic", "Romance", "Italo-Romance")),
    ("en-GB", ("Indo-European", "Germanic", "Northwest Germanic",
               "West Germanic")),
    ("ru", ("Indo-European", "Balto-Slavic", "Slavic", "East Slavic")),
    ("fi", ("Uralic", "Finnic")),
    ("zh", ("Sino-Tibetan", "Sinitic")),
    ("ga", ("Indo-European", "Celtic", "Goidelic")),
    ("hi", ("Indo-European", "Indo-Iranian", "Indo-Aryan")),
    ("ar-EG", ("Afro-Asiatic", "Semitic", "Central Semitic")),
    ("sw", ("Atlantic-Congo", "Bantu")),
    ("tr", ("Turkic",)),
])
def test_family_path_is_derived_from_the_clade_chain(code, expected):
    spec = get(code)
    assert spec.family_path == expected
    assert spec.family == " > ".join(expected)


def test_family_is_not_authored_in_json():
    """The burden is gone: no genetic spec hand-maintains a family string.

    The only files that still carry one are the groupings that are not clades
    at all — creoles, constructed languages, isolates, unclassified languages.
    """
    authored = {}
    for path in sorted(DATA_DIR.glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        if raw.get("family"):
            authored[path.stem] = raw["family"]
    assert set(authored.values()) <= {
        "Constructed", "Isolate", "Unclassifiable", "Khoe-Kwadi",
        # A creole does not descend from a single parent — that is what makes it
        # a creole. The family tree cannot classify one, so these keep an
        # authored label rather than deriving a descent that does not exist.
        "English Creole", "French Creole", "Portuguese Creole",
        "Spanish Creole", "Creole",
    }, authored


def test_explicit_family_overrides_the_derived_path():
    """No clade covers a constructed language or an unclassified one, so those
    specs keep the hand-written string — the only escape hatch left."""
    assert get("eo").family == "Constructed"
    assert get("eo").family_path == ()
    assert get("xib").family == "Isolate"


def test_every_language_has_a_family():
    for code in available_codes():
        assert get(code).family, f"{code}: no family"


def test_available_families_is_keyed_by_the_derived_path():
    fams = available_families()
    assert "pt-PT" in fams[
        "Indo-European > Italic > Romance > Ibero-Romance"]
    # every depth is a usable filter: the CLI matches any step of the path
    steps = {step for key in fams for step in key.split(" > ")}
    assert {"Indo-European", "Italic", "Romance", "Ibero-Romance"} <= steps


def test_orphan_lisbon_is_wired_into_the_graph():
    """pt-PT-x-lisbon is a scored benchmark row that had no parent."""
    spec = get("pt-PT-x-lisbon")
    assert spec.parent == "pt-PT"
    assert "Ibero-Romance" in spec.family_path


# ═══════════════════════════════════════════════════════════════════════════
# Splicing a clade in changes nothing about inheritance
# ═══════════════════════════════════════════════════════════════════════════

def test_clade_parent_does_not_break_rule_inheritance():
    """A spec whose parent chain passes through clades still resolves its
    overlay fields against the nearest data-bearing ancestor."""
    # ast hangs under the Asturleonese clade, above which sits la-x-hispania.
    chain = ancestry_chain("ast")
    assert chain[0].startswith("x-clade-")
    assert "la-x-hispania" in chain
    # Old Catalan's own rules survive a clade parent (its parent is the
    # Romance clade, spliced above Late Latin) — and modern Catalan, which
    # hangs under it, still resolves its overlay fields through it.
    assert get("ca-x-medieval").parent.startswith("x-clade-")
    assert get("ca-x-medieval").allophone_rules
    assert get("ca").parent == "ca-x-medieval"
    assert get("ca").allophone_rules


def test_ancestry_graph_is_acyclic_through_clades():
    for code in available_codes(include_clades=True):
        chain = ancestry_chain(code)
        assert len(chain) == len(set(chain)), f"{code}: cyclic chain {chain}"
