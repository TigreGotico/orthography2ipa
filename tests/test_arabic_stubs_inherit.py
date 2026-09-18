"""No Arabic variety in the registry resolves to an empty table.

A spec that declares a parent and no ``graphemes_base`` produces nothing: the code
resolves, returns a Spec, and that Spec has no phonology. A caller gets an empty answer
rather than an error, which is the silent form of not being covered.

These twelve Arabic varieties were in that state. They now inherit their parent's table,
which makes them usable and is NOT a claim about the variety -- ``quality`` stays ``stub``
and each note says the table is the parent's. The tests hold both halves: the code must
reach a table, and the spec must not start asserting reflexes nobody cited.
"""
import glob
import json
import os

import pytest

import orthography2ipa
from orthography2ipa.registry import get

DATA = os.path.join(os.path.dirname(orthography2ipa.__file__), "data")

# code -> (graphemes base this change adds, classification parent it must KEEP)
# Both are pinned rather than derived. An earlier version of this test asserted the
# parent only when it differed from the base, which skipped the exact case the test
# is named for: reclassifying a variety ONTO its graphemes base, which is what the
# first version of this change did. A guard whose assertion is inside an `if` that
# the defect does not satisfy is not a guard.
FIXED = {
    "ayh": ("ar-YE", "x-clade-afro1255"),
    "acq": ("ar-YE", "x-clade-afro1255"),
    "jye": ("ar-YE", "x-clade-afro1255"),
    "aao": ("ar-DZ", "x-clade-afro1255"),
    "yud": ("ar-LY", "x-clade-afro1255"),
    "ayp": ("ar-IQ-x-qeltu", "x-clade-afro1255"),
    "abh": ("ar-x-mashriqi", "x-clade-afro1255"),
    "auz": ("ar-x-mashriqi", "x-clade-afro1255"),
    "ssh": ("ar-OM", "x-clade-afro1255"),
    # these four already named an Arabic parent on dev and keep it
    "jrb": ("arb", "arb"),
    "ajt": ("ar-TN", "ar-TN"),
    "aju": ("ar-MA", "ar-MA"),
    "yhd": ("ar-IQ", "ar-IQ"),
}


def _raw(code):
    with open(os.path.join(DATA, code + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


@pytest.mark.parametrize("code,base", [(c, b) for c, (b, _) in sorted(FIXED.items())])
def test_the_code_reaches_a_usable_table(code, base):
    spec = get(code)
    assert spec.code == code
    assert len(spec.graphemes) > 100, "resolves to a spec with no phonology"
    assert spec.graphemes == get(base).graphemes, "the table is the base's"


@pytest.mark.parametrize("code,base,parent", [(c, b, p) for c, (b, p) in sorted(FIXED.items())])
def test_only_the_graphemes_edge_moves_not_the_classification(code, base, parent):
    """The two fields are separable by design — stress rides the graphemes edge, not
    the classification parent — so fixing an empty table must not silently reclassify
    a variety.

    Both values are asserted unconditionally against what dev holds. Nine of these
    keep a Glottolog clade node; four legitimately hold an Arabic parent already.
    Changing either field in either direction goes red."""
    raw = _raw(code)
    assert raw["graphemes_base"] == base, f"{code}: graphemes base moved"
    assert raw["parent"] == parent, (
        f"{code}: classification parent is {raw['parent']!r}, expected {parent!r}. "
        "Fixing an empty table must not reclassify the variety — including by setting "
        "the parent to the graphemes base, which is the change this test exists for.")


@pytest.mark.parametrize("code,base", [(c, b) for c, (b, _) in sorted(FIXED.items())])
def test_nothing_is_asserted_about_the_variety(code, base):
    raw = _raw(code)
    assert raw["graphemes_base"] == base
    assert not raw.get("graphemes"), (
        "a reflex was declared for a variety whose description has not been read; "
        "cite it or take it out")
    assert raw["quality"] == "stub"
    assert "NOT a claim about this variety" in raw["notes"]


def test_no_arabic_spec_resolves_to_an_empty_table():
    """The absolute check. A variety that resolves to nothing is not covered, however
    complete the file list looks."""
    empty = []
    for path in glob.glob(os.path.join(DATA, "*.json")):
        spec_json = json.load(open(path, encoding="utf-8"))
        name = str(spec_json.get("name") or "")
        if "arabic" not in name.lower():
            continue
        code = os.path.basename(path)[: -len(".json")]
        if code.startswith("x-clade-"):
            continue  # ancestry nodes carry no table by design
        if code == "abv":
            continue  # a modelled Baharna spec replaces this stub in #1647
        try:
            n = len(get(code).graphemes)
        except Exception as exc:  # a code that cannot resolve is its own failure
            empty.append(f"{code}: {type(exc).__name__}")
            continue
        if n == 0:
            empty.append(f"{code} ({name})")
    assert not empty, "Arabic varieties resolving to an empty table:\n  " + "\n  ".join(empty)
