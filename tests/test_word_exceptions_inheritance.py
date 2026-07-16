"""word_exceptions BASE_MERGE inheritance.

A dialect child that declares ``word_exceptions_base`` sees the base
spec's word-level exception overrides, with its own entries winning per
word. Previously ``word_exceptions`` was own-file-only, so every
``pt-PT-x-*`` child silently dropped the parent's exceptions.
"""
import json
from pathlib import Path

import pytest

from orthography2ipa.json_loader import load_json_spec
from orthography2ipa.registry import get

DATA = Path(__file__).parent.parent / "orthography2ipa" / "data"


def _pt_pt_children():
    codes = []
    for f in DATA.glob("pt-PT-x-*.json"):
        d = json.loads(f.read_text())
        if d.get("word_exceptions_base") == "pt-PT":
            codes.append(d["code"])
    return sorted(codes)


class TestWordExceptionsInheritance:

    def test_all_pt_pt_children_declare_the_base(self):
        # every dialect child that pulls graphemes from pt-PT must pull its
        # word exceptions too — a new child can't silently opt out
        for f in DATA.glob("pt-PT-x-*.json"):
            d = json.loads(f.read_text())
            if d.get("graphemes_base") == "pt-PT":
                assert d.get("word_exceptions_base") == "pt-PT", d["code"]

    @pytest.mark.parametrize("code", _pt_pt_children())
    def test_child_sees_parent_exceptions(self, code):
        parent = get("pt-PT")
        child = get(code)
        parent_exc = parent.word_exceptions or {}
        child_raw = json.loads((DATA / f"{code}.json").read_text())
        own = child_raw.get("word_exceptions") or {}
        merged = child.word_exceptions or {}
        for word, ipa in parent_exc.items():
            expected = own.get(word, ipa)  # own entries win
            assert merged.get(word) == expected, (code, word)
        for word, ipa in own.items():
            assert merged.get(word) == ipa, (code, word)

    def test_own_entries_override_base(self, tmp_path, monkeypatch):
        # synthetic: base defines two exceptions, child overrides one and
        # adds one — merged view is {**base, **own}
        import orthography2ipa.json_loader as jl
        base = {"code": "zz-BASE", "name": "Base", "script": "Latn",
                "graphemes": {"a": ["a"]},
                "word_exceptions": {"foo": "fu", "bar": "ba"}}
        child = {"code": "zz-BASE-x-kid", "name": "Kid", "script": "Latn",
                 "parent": "zz-BASE",
                 "graphemes_base": "zz-BASE",
                 "word_exceptions_base": "zz-BASE",
                 "graphemes": {},
                 "word_exceptions": {"bar": "BA", "baz": "bz"}}
        for d in (base, child):
            (tmp_path / f"{d['code']}.json").write_text(
                json.dumps(d), encoding="utf-8")
        index = dict(jl._index)
        index.update({d["code"]: tmp_path / f"{d['code']}.json"
                      for d in (base, child)})
        monkeypatch.setattr(jl, "_index", index)
        monkeypatch.setattr(jl, "_specs", {})
        spec = load_json_spec("zz-BASE-x-kid")
        assert spec.word_exceptions == {"foo": "fu", "bar": "BA", "baz": "bz"}

    def test_no_base_key_means_own_only(self, tmp_path, monkeypatch):
        # without word_exceptions_base nothing is inherited (opt-in)
        import orthography2ipa.json_loader as jl
        base = {"code": "zy-BASE", "name": "Base", "script": "Latn",
                "graphemes": {"a": ["a"]},
                "word_exceptions": {"foo": "fu"}}
        child = {"code": "zy-BASE-x-kid", "name": "Kid", "script": "Latn",
                 "parent": "zy-BASE",
                 "graphemes_base": "zy-BASE",
                 "graphemes": {}}
        for d in (base, child):
            (tmp_path / f"{d['code']}.json").write_text(
                json.dumps(d), encoding="utf-8")
        index = dict(jl._index)
        index.update({d["code"]: tmp_path / f"{d['code']}.json"
                      for d in (base, child)})
        monkeypatch.setattr(jl, "_index", index)
        monkeypatch.setattr(jl, "_specs", {})
        spec = load_json_spec("zy-BASE-x-kid")
        assert not spec.word_exceptions
