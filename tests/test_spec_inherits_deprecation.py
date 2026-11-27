"""``LanguageSpec.parent`` and the ``parent`` key of a spec file are deprecated
aliases of ``inherits``.

The removal version comes from ``version.py``, read as text, so the expected
message does not depend on the code that writes the warning.
"""
import json
import re
import warnings
from pathlib import Path

import pytest

import orthography2ipa
import orthography2ipa.json_loader as jl
from orthography2ipa import get
from orthography2ipa.json_loader import load_json_spec

DATA = Path(orthography2ipa.__file__).parent / "data"
VERSION = Path(orthography2ipa.__file__).parent / "version.py"
BASE = {"code": "zi-BASE", "name": "Base", "script": "Latn", "graphemes": {"a": ["a"]}}
KID = {"code": "zi-BASE-x-kid", "name": "Kid", "script": "Latn", "graphemes": {}}


def removal_version() -> str:
    major = re.search(r"^VERSION_MAJOR = (\d+)$", VERSION.read_text(encoding="utf-8"), re.M)
    return f"{int(major.group(1)) + 1}.0.0"


def deprecations(call):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result = call()
    return result, [w for w in caught if issubclass(w.category, DeprecationWarning)]


@pytest.fixture
def specs_in(tmp_path, monkeypatch):
    def install(*raws):
        for raw in raws:
            (tmp_path / f"{raw['code']}.json").write_text(json.dumps(raw), encoding="utf-8")
        monkeypatch.setattr(jl, "_index", {**jl._index, **{r["code"]: tmp_path / f"{r['code']}.json" for r in raws}})
        monkeypatch.setattr(jl, "_specs", {})
    return install


def test_the_parent_attribute_returns_inherits_and_warns():
    expected = json.loads((DATA / "pt-BR.json").read_text(encoding="utf-8"))["inherits"]
    spec = get("pt-BR")
    assert spec.inherits == expected
    value, caught = deprecations(lambda: spec.parent)
    assert value == expected
    assert len(caught) == 1
    assert str(caught[0].message) == (
        f"LanguageSpec.parent is deprecated and will be removed in {removal_version()}; "
        "use LanguageSpec.inherits.")
    assert caught[0].filename == __file__


def test_a_spec_file_with_the_parent_key_loads_as_inherits(specs_in):
    specs_in(BASE, {**KID, "parent": "zi-BASE"})
    spec, caught = deprecations(lambda: load_json_spec("zi-BASE-x-kid"))
    assert spec.inherits == "zi-BASE"
    assert [a.code for a in spec.ancestors] == ["zi-BASE"]
    assert len(caught) == 1
    assert str(caught[0].message) == (
        f"the 'parent' key of spec 'zi-BASE-x-kid' is deprecated and will be removed in "
        f"{removal_version()}; rename it to 'inherits'.")


def test_a_spec_file_with_the_inherits_key_does_not_warn(specs_in):
    specs_in(BASE, {**KID, "inherits": "zi-BASE"})
    spec, caught = deprecations(lambda: load_json_spec("zi-BASE-x-kid"))
    assert spec.inherits == "zi-BASE"
    assert caught == []


def test_a_spec_file_with_both_keys_is_refused_by_name(specs_in):
    specs_in(BASE, {**KID, "parent": "zi-BASE", "inherits": "zi-BASE"})
    with pytest.raises(ValueError, match="spec 'zi-BASE-x-kid' sets both 'parent' and 'inherits'"):
        load_json_spec("zi-BASE-x-kid")
