"""Stress inheritance through the structural base edge.

A dialect child that overlays graphemes over a base (``graphemes_base``, or
the nearest data ancestor of ``parent``) but declares no ``stress`` block of
its own inherits the base's accentuation rules. Previously ``stress`` was
own-file-only, so every ``es-ES-x-*`` / ``an-x-*`` / ``gl-ES-x-*`` / ``ast-x-*``
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

    @pytest.mark.parametrize("base", ["es-ES", "an", "gl-ES", "ast"])
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
        # gl-ES-x-eonavia declares its own block. The Eonavian norm (§1.5.2)
        # writes the accent on an oxytone final diphthong (baxóu, cantéi), so an
        # unaccented one is paroxytone, and the block drops the gl-ES endings
        # that make it oxytone. The block stays whole, never merged with gl-ES.
        child_raw = json.loads((DATA / "gl-ES-x-eonavia.json").read_text())
        assert child_raw.get("stress"), "fixture precondition: own stress present"
        child, base = get("gl-ES-x-eonavia"), get("gl-ES")
        own_endings = tuple(child_raw["stress"]["final_stress_endings"])
        assert child.stress.final_stress_endings == own_endings
        assert child.stress.final_stress_endings != base.stress.final_stress_endings

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


# The stressed syllable is counted from the end of the transcription: the
# number of vowel nuclei from the stress mark to the end of the word.
_IPA_VOWELS = set("aeiouɛɔəɐɨɯʊɪyøœæɑɒʌ")


def _syllables_from_mark(ipa):
    assert ipa.count("ˈ") == 1, ipa
    tail = ipa.split("ˈ")[1]
    return sum(1 for i, ch in enumerate(tail)
               if ch in _IPA_VOWELS and (i == 0 or tail[i - 1] not in _IPA_VOWELS))


class TestSameLanguageParent:
    """A spec with ``parent`` but no ``graphemes_base`` and no stress block
    takes its parent's block when the parent is the same language: the spec's
    ``iso639_3`` is unset or equal to the parent's (InheritanceMode.BASE_BLOCK).
    """

    # Modern Greek monotonic orthography: the tonos is "used to mark the
    # stressed syllable in polysyllabic words" (Wikipedia, Greek orthography).
    # el-CY has no ISO 639-3 code of its own; its parent is el.
    @pytest.mark.parametrize("word, from_end", [
        ("καλημέρα", 2), ("θάλασσα", 3), ("ουρανός", 1), ("νερό", 1),
        ("γράμμα", 2),
    ])
    def test_cypriot_greek_stresses_the_accented_syllable(self, word, from_end):
        ipa = orthography2ipa.transcribe(word, "el-CY")
        assert _syllables_from_mark(ipa) == from_end, ipa

    # Italian orthography: accents are "generally mandatory only to indicate
    # stress on a word-final vowel" (Wikipedia, Italian orthography).
    # it-IT-x-toscana shares iso639_3 ita with its parent it-IT.
    @pytest.mark.parametrize("code", ["it-IT-x-toscana", "it-IT-x-roma",
                                      "it-IT-x-marche", "it-IT-x-umbria"])
    @pytest.mark.parametrize("word", ["città", "perché", "caffè", "però"])
    def test_italian_variety_stresses_the_written_final_accent(self, code, word):
        ipa = orthography2ipa.transcribe(word, code)
        assert _syllables_from_mark(ipa) == 1, ipa

    def test_variety_takes_the_parent_block(self):
        assert get("el-CY").stress == get("el").stress
        assert get("it-IT-x-toscana").stress == get("it-IT").stress

    # A language with its own ISO 639-3 code keeps parent for its genealogy
    # only. Angolar (aoa) is a creole under pt-PT; A Fala (fax) is a language
    # of the Galician branch (Glottolog fala1241) under gl-ES.
    @pytest.mark.parametrize("code", ["aoa", "fax"])
    def test_other_language_does_not_take_the_parent_block(self, code):
        raw = json.loads((DATA / f"{code}.json").read_text())
        assert not raw.get("stress") and not raw.get("graphemes_base")
        assert raw["iso639_3"] != get(raw["parent"]).iso639_3
        assert get(code).stress is None


class TestCopiedBlockRemoved:
    """A child that copied its base's block now takes the block from the
    base, and its stress placement does not change."""

    # RAE rules as es-ES states them: a written accent wins; an unaccented
    # word that ends in a vowel, -n or -s is paroxytone, and one that ends in
    # another consonant is oxytone (Hualde 2005, ch. 8).
    @pytest.mark.parametrize("code", ["es-419", "es-AR", "es-MX"])
    @pytest.mark.parametrize("word, from_end", [
        ("canción", 1), ("ciudad", 1), ("árbol", 2), ("papel", 1),
        ("comer", 1), ("joven", 2), ("casas", 2),
    ])
    def test_spanish_variety_keeps_its_placement(self, code, word, from_end):
        ipa = orthography2ipa.transcribe(word, code)
        assert _syllables_from_mark(ipa) == from_end, ipa

    @pytest.mark.parametrize("code, base", [
        ("es-AR", "es-ES"), ("pt-PT-x-lisbon", "pt-PT"), ("pt-BR-x-sp", "pt-BR"),
    ])
    def test_child_takes_the_base_block(self, code, base):
        raw = json.loads((DATA / f"{code}.json").read_text())
        assert "stress" not in raw
        assert get(code).stress == get(base).stress


def _load_synthetic(tmp_path, monkeypatch, specs, code):
    import orthography2ipa.json_loader as jl
    index = dict(jl._index)
    for d in specs:
        path = tmp_path / f"{d['code']}.json"
        path.write_text(json.dumps(d), encoding="utf-8")
        index[d["code"]] = path
    monkeypatch.setattr(jl, "_index", index)
    monkeypatch.setattr(jl, "_specs", {})
    return load_json_spec(code)


_PARENT = {"code": "zq-PAR", "name": "Parent", "script": "Latn",
           "iso639_3": "zqp", "graphemes": {"a": ["a"]},
           "stress": {"default_position": 1, "final_stress_endings": ["r"]}}


class TestSyntheticParentEdge:

    @pytest.mark.parametrize("iso", [None, "zqp"])
    def test_same_language_child_takes_the_block(self, tmp_path, monkeypatch, iso):
        child = {"code": "zq-PAR-x-kid", "name": "Kid", "script": "Latn",
                 "parent": "zq-PAR", "iso639_3": iso, "graphemes": {"a": ["a"]}}
        spec = _load_synthetic(tmp_path, monkeypatch, [_PARENT, child], child["code"])
        assert spec.stress is not None
        assert spec.stress.default_position == 1
        assert spec.stress.final_stress_endings == ("r",)

    def test_other_language_child_takes_nothing(self, tmp_path, monkeypatch):
        child = {"code": "zqk", "name": "Other", "script": "Latn",
                 "parent": "zq-PAR", "iso639_3": "zqk", "graphemes": {"a": ["a"]}}
        spec = _load_synthetic(tmp_path, monkeypatch, [_PARENT, child], "zqk")
        assert spec.stress is None

    def test_edge_passes_through_a_clade(self, tmp_path, monkeypatch):
        clade = {"code": "x-clade-zq", "name": "Zq branch", "script": "Zyyy",
                 "clade": True, "quality": "stub", "graphemes": {},
                 "allophones": {}, "parent": "zq-PAR"}
        child = {"code": "zq-PAR-x-far", "name": "Far", "script": "Latn",
                 "parent": "x-clade-zq", "graphemes": {"a": ["a"]}}
        spec = _load_synthetic(tmp_path, monkeypatch, [_PARENT, clade, child],
                               child["code"])
        assert spec.stress is not None
        assert spec.stress.default_position == 1

    def test_own_block_is_kept_whole(self, tmp_path, monkeypatch):
        child = {"code": "zq-PAR-x-own", "name": "Own", "script": "Latn",
                 "parent": "zq-PAR", "graphemes": {"a": ["a"]},
                 "stress": {"default_position": -1}}
        spec = _load_synthetic(tmp_path, monkeypatch, [_PARENT, child], child["code"])
        assert spec.stress.default_position == -1
        assert spec.stress.final_stress_endings == ()


class TestOptOut:
    """``"stress": false`` takes no block; ``{}`` and ``null`` inherit."""

    @pytest.mark.parametrize("edge", ["graphemes_base", "parent"])
    def test_false_takes_no_block(self, tmp_path, monkeypatch, edge):
        child = {"code": "zq-PAR-x-out", "name": "Out", "script": "Latn",
                 "parent": "zq-PAR", "graphemes": {"a": ["a"]}, "stress": False}
        if edge == "graphemes_base":
            child["graphemes_base"] = "zq-PAR"
        spec = _load_synthetic(tmp_path, monkeypatch, [_PARENT, child], child["code"])
        assert spec.stress is None

    @pytest.mark.parametrize("value", [{}, None])
    def test_empty_or_null_still_inherits(self, tmp_path, monkeypatch, value):
        child = {"code": "zq-PAR-x-in", "name": "In", "script": "Latn",
                 "parent": "zq-PAR", "graphemes": {"a": ["a"]}, "stress": value}
        spec = _load_synthetic(tmp_path, monkeypatch, [_PARENT, child], child["code"])
        assert spec.stress is not None
        assert spec.stress.default_position == 1

    def test_schema_accepts_false_and_rejects_true(self, tmp_path):
        from orthography2ipa.schema import validate_spec_file
        base = {"code": "zq-PAR-x-out", "name": "Out", "script": "Latn",
                "graphemes": {"a": ["a"]}}
        ok, bad = tmp_path / "ok.json", tmp_path / "bad.json"
        ok.write_text(json.dumps({**base, "stress": False}), encoding="utf-8")
        bad.write_text(json.dumps({**base, "stress": True}), encoding="utf-8")
        assert validate_spec_file(ok).stress is False
        with pytest.raises(Exception):
            validate_spec_file(bad)
