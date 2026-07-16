"""Stress inheritance through the structural base edge.

A dialect child that overlays graphemes over a base (``graphemes_base``, or
the nearest data ancestor of ``parent``) but declares no ``stress`` block of
its own inherits the base's accentuation rules. Previously ``stress`` was
own-file-only, so every ``es-ES-x-*`` / ``an-x-*`` / ``gl-x-*`` / ``ast-x-*``
child silently emitted UNSTRESSED output — e.g. ``es-ES-x-murcia`` produced
``el θjelo`` where its ``es-ES`` parent produces ``ˈel ˈθjelo``.

Castilian accentuation is the RAE written-accent + paroxytone-default rule
(Hualde 2005, *The Sounds of Spanish*, ch. 8); a regional accent of Castilian
does not change where the stress lands, only the segmental realisation, so the
child must keep the parent's stress placement.
"""
import json
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa.json_loader import load_json_spec
from orthography2ipa.registry import get

DATA = Path(__file__).parent.parent / "orthography2ipa" / "data"


def _children_without_own_stress(base):
    codes = []
    for f in sorted(DATA.glob(f"{base}-x-*.json")):
        d = json.loads(f.read_text())
        if d.get("graphemes_base") == base and not d.get("stress"):
            codes.append(d["code"])
    return codes


class TestStressInheritance:

    @pytest.mark.parametrize("base", ["es-ES", "an", "gl", "ast"])
    def test_children_inherit_base_stress(self, base):
        parent = get(base)
        assert parent.stress is not None, base
        kids = _children_without_own_stress(base)
        assert kids, f"no stress-less x-lects found for {base}"
        for code in kids:
            child = get(code)
            assert child.stress is not None, code
            # inherited wholesale — the identical StressRules object/content
            assert child.stress.default_position == parent.stress.default_position
            assert child.stress.stress_mark == parent.stress.stress_mark
            assert child.stress.final_stress_endings == parent.stress.final_stress_endings

    def test_castilian_child_emits_primary_stress(self):
        # the reported bug: the child dropped the marks its base emits
        base = orthography2ipa.transcribe("el cielo", "es-ES")
        kid = orthography2ipa.transcribe("el cielo", "es-ES-x-murcia")
        assert "ˈ" in base
        assert "ˈ" in kid, kid

    def test_own_stress_block_wins_over_inheritance(self):
        # ca-x-valencia declares its own (Valencian/IEC) stress and must not be
        # overwritten by inheritance from ca-x-medieval
        child_raw = json.loads((DATA / "ca-x-valencia.json").read_text())
        assert child_raw.get("stress"), "fixture precondition: own stress present"
        child = get("ca-x-valencia")
        assert child.stress.marked_vowels == tuple(child_raw["stress"]["marked_vowels"])

    def test_synthetic_child_inherits_base_stress(self, tmp_path, monkeypatch):
        import orthography2ipa.json_loader as jl
        base = {"code": "zx-BASE", "name": "Base", "script": "Latn",
                "graphemes": {"a": ["a"]},
                "stress": {"default_position": -2, "stress_mark": "ˈ",
                           "final_stress_endings": ["r"]}}
        child = {"code": "zx-BASE-x-kid", "name": "Kid", "script": "Latn",
                 "parent": "zx-BASE", "graphemes_base": "zx-BASE",
                 "graphemes": {}, "stress": None}
        for d in (base, child):
            (tmp_path / f"{d['code']}.json").write_text(
                json.dumps(d), encoding="utf-8")
        index = dict(jl._index)
        index.update({d["code"]: tmp_path / f"{d['code']}.json"
                      for d in (base, child)})
        monkeypatch.setattr(jl, "_index", index)
        monkeypatch.setattr(jl, "_specs", {})
        spec = load_json_spec("zx-BASE-x-kid")
        assert spec.stress is not None
        assert spec.stress.default_position == -2
        assert spec.stress.final_stress_endings == ("r",)

    def test_no_base_edge_means_no_inherited_stress(self, tmp_path, monkeypatch):
        # a standalone spec with no base edge and no own stress stays stressless
        import orthography2ipa.json_loader as jl
        spec_raw = {"code": "zw-ALONE", "name": "Alone", "script": "Latn",
                    "graphemes": {"a": ["a"]}}
        (tmp_path / "zw-ALONE.json").write_text(json.dumps(spec_raw), encoding="utf-8")
        index = dict(jl._index)
        index["zw-ALONE"] = tmp_path / "zw-ALONE.json"
        monkeypatch.setattr(jl, "_index", index)
        monkeypatch.setattr(jl, "_specs", {})
        spec = load_json_spec("zw-ALONE")
        assert spec.stress is None
