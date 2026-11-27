"""The syllable part of a plugin fragment (docs/ir/o2i-ir-v1.md, 3.7.6).

The expected splits are those of silabificador 1.x (``syllabify``) and of the
dictionaries it cites; this file never reads them back from the interpreter.
"""
import copy
import json
from pathlib import Path

import pytest

from orthography2ipa.ir import layout
from orthography2ipa.ir.compiler import build_ir
from orthography2ipa.ir.interpreter import Interpreter

FRAGMENT = json.loads((Path(__file__).parent / "data" / "ir_fragment_syllable.json").read_text(encoding="utf-8"))


def splitter(*fragments):
    return Interpreter(layout.encode(build_ir("pt-PT", fragments=list(fragments))))


def without(table):
    fragment = copy.deepcopy(FRAGMENT)
    del fragment["syllable"][table]
    return fragment


FULL = splitter(FRAGMENT)

# (table, word, split): the split needs the table.
CASES = [
    ("glides", "neymar", "ney.mar"),
    ("glides", "playground", "play.ground"),
    ("hiatus", "ao", "ao"),
    ("hiatus", "aos", "aos"),
    ("stem_cuts", "arruinar", "ar.ru.i.nar"),
    ("stem_cuts", "adleriano", "ad.le.ri.a.no"),
    ("prefix_boundaries", "sublinhar", "sub.li.nhar"),
    ("prefix_boundaries", "sublocar", "sub.lo.car"),
    ("seams", "distribuidor", "dis.tri.bu.i.dor"),
    ("seams", "ingenuidade", "in.ge.nu.i.da.de"),
    ("onsets", "pacto", "pac.to"),
    ("onsets", "abstrair", "abs.tra.ir"),
    ("foreign", "kubitschek", "ku.bi.tschek"),
    ("foreign", "facebookiano", "fa.ce.boo.ki.a.no"),
    ("foreign", "bureau", "bu.reau"),
    ("foreign", "boxeur", "bo.xeur"),
    ("foreign", "gourmet", "gour.met"),
]


@pytest.mark.parametrize("table,word,split", CASES)
def test_the_table_gives_the_split(table, word, split):
    assert ".".join(FULL.syllables(word)) == split
    assert ".".join(splitter(without(table)).syllables(word)) != split


@pytest.mark.parametrize("word,split", [("sublime", "su.bli.me"), ("cuidado", "cui.da.do"),
                                        ("contiguidade", "con.ti.gui.da.de"), ("aorta", "a.or.ta"),
                                        ("atleta", "a.tle.ta"), ("marathon", "ma.ra.thon")])
def test_the_tables_leave_these_splits(word, split):
    assert ".".join(FULL.syllables(word)) == split


def test_a_pair_cuts_without_an_onset_table():
    pairs = {"ir_version": 1, "syllable": {"heterosyllabic_pairs": FRAGMENT["syllable"]["heterosyllabic_pairs"]}}
    assert splitter().syllables("carro") == ["ca", "rro"]
    assert splitter(pairs).syllables("carro") == ["car", "ro"]
    assert splitter(pairs).syllables("nascer") == ["nas", "cer"]


def test_a_pair_inside_a_unit_does_not_cut():
    assert ".".join(splitter(without("heterosyllabic_pairs")).syllables("kubitschek")) == "ku.bi.tschek"
    assert ".".join(FULL.syllables("kubitschek")) == "ku.bi.tschek"


def test_the_glide_hiatus_does_not_depend_on_stress():
    hiatus = {"ir_version": 1, "syllable": {"hiatus": FRAGMENT["syllable"]["hiatus"],
                                            "onsets": FRAGMENT["syllable"]["onsets"]}}
    assert ".".join(splitter(hiatus).syllables("ainda")) == "a.in.da"
    assert ".".join(splitter(hiatus).syllables("bairro")) == "bair.ro"
    assert ".".join(splitter(hiatus).syllables("rainha")) == "ra.i.nha"


@pytest.mark.parametrize("fragment", [{"ir_version": 1}, {"ir_version": 1, "syllable": {}}])
def test_no_syllable_tables_change_nothing(fragment):
    assert build_ir("pt-PT", fragments=[fragment]) == build_ir("pt-PT")
    assert layout.spec_revision(build_ir("pt-PT", fragments=[fragment])) == layout.spec_revision(build_ir("pt-PT"))


def test_the_tables_add_their_semantics_versions():
    manifest = layout.manifest(build_ir("pt-PT", fragments=[FRAGMENT])).split(";")
    for name in ("cut_pairs", "glide_hiatus", "stem_cuts", "prefix_cuts", "seams", "foreign_nuclei"):
        assert f"{name}=1" in manifest
    assert not {m.split("=")[0] for m in layout.manifest(build_ir("pt-PT")).split(";")} & {
        "cut_pairs", "glide_hiatus", "stem_cuts", "prefix_cuts", "seams", "foreign_nuclei"}


def test_a_later_fragment_replaces_a_table():
    later = {"ir_version": 1, "syllable": {"stem_cuts": {"adleriano": [2]}}}
    ir = build_ir("pt-PT", fragments=[FRAGMENT, later])
    assert [list(pair) for pair in ir["syllable"]["stem_cuts"]] == [["adleriano", [2]]]


@pytest.mark.parametrize("part,message", [
    ({"stress": {}}, "key 'stress' is not allowed"),
    ({"glides": ["yy"]}, "each glide must be one char"),
    ({"hiatus": {"vowels": []}}, "key 'vowels' is not allowed"),
    ({"heterosyllabic_pairs": ["rrr"]}, "each pair must have 2 chars"),
    ({"heterosyllabic_pairs": ["RR"]}, "must be lowercase NFC"),
    ({"stem_cuts": {"ruin": [4]}}, "offsets inside the stem"),
    ({"seams": {"suffixes": [{"pattern": "(?<=ab)c", "cut": 0}]}}, "seams.suffixes"),
    ({"onsets": {"max_onset": 0}}, "max_onset"),
    ({"foreign": {"nuclei": ["ee"]}}, "nuclei need a pattern"),
    ({"prefix_boundaries": [{"prefix": 3}]}, "prefix_boundaries.prefix"),
])
def test_a_malformed_table_is_refused(part, message):
    with pytest.raises(ValueError, match=message.replace("(", r"\(").replace(")", r"\)")):
        build_ir("pt-PT", fragments=[{"ir_version": 1, "syllable": part}])
