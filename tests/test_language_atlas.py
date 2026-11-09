"""The language atlas generator: its blocks, its template and its check mode.

``scripts/gen_language_atlas.py`` owns the blocks between the atlas markers of
each language page and the four index pages. These tests hold the contract a
page author relies on: the check mode fails on a stale block, hand-written
text survives a rewrite, the template is enforced, and the values the blocks
print come from the spec, not from the generator.
"""
import importlib.util
import json
import os
import re

import pytest

import orthography2ipa

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load():
    path = os.path.join(_ROOT, "scripts", "gen_language_atlas.py")
    spec = importlib.util.spec_from_file_location("gen_language_atlas", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


atlas_gen = _load()


@pytest.fixture(scope="module")
def atlas():
    return atlas_gen.Atlas()


def _page(code):
    with open(os.path.join(_ROOT, "docs", "languages", f"{code}.md"),
              encoding="utf-8") as fh:
        return fh.read()


def test_committed_atlas_is_current():
    assert atlas_gen.main(["--check"]) == 0


def test_stale_block_fails_check(monkeypatch):
    real = atlas_gen._read
    target = os.path.join("docs", "languages", "es-ES.md")

    def stale(path):
        text = real(path)
        if path.endswith(target):
            text = text.replace("| Code | `es-ES` |", "| Code | `es-XX` |")
        return text

    monkeypatch.setattr(atlas_gen, "_read", stale)
    assert atlas_gen.main(["--check"]) == 1


def test_stale_examples_block_fails_check(monkeypatch):
    real = atlas_gen._read

    def stale(path):
        text = real(path)
        if path.endswith(os.path.join("languages", "mwl.md")):
            text = text.replace("| lhéngua | [ˈʎẽŋɡwɐ] |", "| lhéngua | [ˈlenɡwa] |")
        return text

    monkeypatch.setattr(atlas_gen, "_read", stale)
    assert atlas_gen.main(["--check"]) == 1


def test_hand_written_text_survives_a_rewrite(atlas):
    text = _page("mwl").replace(
        "## Input contract\n", "## Input contract\n\nA line only a person wrote.\n")
    assert atlas_gen.render_page(atlas, "mwl", text) == text


def test_rewrite_restores_a_tampered_block(atlas):
    original = _page("ar")
    tampered = original.replace("| Code | `ar` |", "| Code | `xx` |")
    assert tampered != original
    assert atlas_gen.render_page(atlas, "ar", tampered) == original


def test_missing_block_breaks_the_template(atlas):
    text = re.sub(r"<!-- atlas:rules begin -->.*?<!-- atlas:rules end -->\n",
                  "", _page("es-ES"), flags=re.S)
    with pytest.raises(atlas_gen.TemplateError):
        atlas_gen.render_page(atlas, "es-ES", text)


def test_blocks_out_of_order_break_the_template(atlas):
    text = _page("es-ES")
    sources = re.search(r"<!-- atlas:sources begin -->.*?<!-- atlas:sources end -->",
                        text, re.S).group(0)
    datasets = re.search(r"<!-- atlas:datasets begin -->.*?<!-- atlas:datasets end -->",
                         text, re.S).group(0)
    swapped = text.replace(sources, "\0").replace(datasets, sources).replace("\0", datasets)
    with pytest.raises(atlas_gen.TemplateError):
        atlas_gen.render_page(atlas, "es-ES", swapped)


def test_header_values_come_from_the_spec(atlas):
    spec = orthography2ipa.get("mwl")
    header = atlas_gen.block_header(atlas, spec)
    assert f"glottolog.org/resource/languoid/id/{spec.glottolog_code})" in header
    assert f"iso639-3.sil.org/code/{spec.iso639_3})" in header
    assert "| Child lects | 2, see [Related lects](#related-lects) |" in header
    lects = atlas_gen.block_lects(atlas, spec)
    for child in ("mwl-x-sendim", "mwl-x-ifanes"):
        assert f"`{child}`" in lects
        assert f"`{child}`" not in header


def test_lects_block_lists_every_child(atlas):
    data = os.path.join(os.path.dirname(orthography2ipa.__file__), "data")
    children = set()
    for name in os.listdir(data):
        if name.endswith(".json"):
            with open(os.path.join(data, name), encoding="utf-8") as fh:
                spec = json.load(fh)
            if spec.get("parent") == "es-ES" and not spec.get("clade"):
                children.add(spec["code"])
    lects = atlas_gen.block_lects(atlas, orthography2ipa.get("es-ES"))
    listed = set(re.findall(r"^- \[.*\]\(.*\) `([^`]+)`", lects, re.M))
    assert listed == children
    assert len(children) > 30


def test_historical_parent_is_an_ancestor(atlas):
    # es-ES-x-medieval ends in 1500, es-ES is living.
    header = atlas_gen.block_header(atlas, orthography2ipa.get("es-ES"))
    assert "| Ancestor | [Castilian]" in header
    assert "| Parent |" not in header
    header = atlas_gen.block_header(atlas, orthography2ipa.get("es-AR"))
    assert "| Parent | [" in header and "`es-ES` |" in header
    assert "| Ancestor |" not in header


@pytest.mark.parametrize("code, area", [
    ("es-AR", "South America"), ("es-MX", "North America"),
    ("es-GQ", "Africa"), ("es-ES", "Eurasia")])
def test_region_subtag_sets_the_macroarea(atlas, code, area):
    assert atlas.geography(code)[0] == [area]


def test_datasets_block_lists_every_board_row(atlas):
    spec = orthography2ipa.get("es-ES")
    rows = [r for r in atlas.board
            if orthography2ipa.resolves_exactly(r["lang"])
            and orthography2ipa.resolve(r["lang"]) == "es-ES"]
    block = atlas_gen.block_datasets(atlas, spec)
    table = [line for line in block.splitlines() if line.startswith("| `")]
    assert len(table) == len(rows)
    for row in rows:
        assert f"| {row['per']:.4f} |" in block


def test_examples_are_engine_output(atlas):
    spec = orthography2ipa.get("es-ES")
    block = atlas_gen.block_examples(atlas, spec, ["cabra"])
    assert f"| cabra | [{orthography2ipa.transcribe('cabra', 'es-ES')}] |" in block


@pytest.mark.parametrize("note, expected", [
    ("Coda l is the velarised [ɫ]: caldo → [ˈkaɫdu], sol → [ˈs̺oɫ].",
     "⟨caldo⟩ [ˈkaɫdu]"),
    ("a coda /n/ agrees in place, surfacing as [m].", ""),
    ("the voiced apical: asno [ˈaz̺nu] and mesmo.", "⟨asno⟩ [ˈaz̺nu]"),
    ("the broad mid nasal [ẽ] of the table.", ""),
    ("Word-final apical s is voiced: ls nius → [ɫz̺ ˈnjus̺].", "⟨ls nius⟩ [ɫz̺ ˈnjus̺]"),
])
def test_example_is_quoted_from_the_note(note, expected):
    assert atlas_gen._example(note) == expected


def test_citation_links_a_matching_source():
    spec = orthography2ipa.get("mwl")
    note = ("Leite de Vasconcellos (1900, vol. I, §13, p. 188) and "
            "Ferreira et al. (2014, §3.4) and Smith (1987).")
    cited = atlas_gen._citations(spec, note)
    assert "[Vasconcelos 1900](#src-vasconcelos1900)" in cited
    assert "[Ferreira 2014](#src-ferreira2014)" in cited
    assert "Smith 1987" in cited


@pytest.mark.parametrize("segment, base", [
    ("ç", "ç"), ("ẽ", "e"), ("s̺", "s"), ("tʃ", "tʃ"), ("t͡ʃ", "tʃ"),
    ("dˤ", "d"), ("aː", "a"),
])
def test_segment_base(segment, base):
    assert atlas_gen._base(segment) == base


def test_palatal_fricative_is_not_a_stop():
    assert atlas_gen._CONSONANTS[atlas_gen._base("ç")] == ("fricative", "palatal")


def test_dialect_without_languoid_takes_no_country(atlas):
    areas, countries = atlas.geography("mwl-x-sendim")
    assert areas == ["Eurasia"]
    assert countries == []


def test_region_subtag_names_the_country(atlas):
    assert atlas.geography("es-ES")[1] == ["ES"]


def test_primary_row_without_a_spelling_is_skipped(atlas):
    rows = atlas.primary_rows["shu-NG"]
    assert any(not (r.get("orthography") or r.get("orthography_vocalized"))
               for r in rows)
    block = atlas_gen.block_examples(atlas, orthography2ipa.get("shu-NG"), [])
    assert "| None |" not in block
    assert block.count("\n| ") > 2


def _nav():
    path = os.path.join(_ROOT, "scripts", "docs_nav.py")
    spec = importlib.util.spec_from_file_location("docs_nav", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _names_in_order(atlas, codes):
    return [f"languages/{c}.md"
            for c in sorted(codes, key=lambda c: (atlas.raw[c]["name"], c))]


def test_reading_order_takes_every_atlas_page_from_the_az_index(atlas):
    order = _nav().reading_order()
    at = order.index("languages/a-z.md") + 1
    expected = _names_in_order(atlas, atlas.pages)
    assert order[at:at + len(expected)] == expected


def test_a_new_atlas_page_gets_the_footer_of_its_az_place(monkeypatch):
    # A page on disk that is not an atlas page yet, made one by a scaffold.
    # The atlas is built here, because the test adds a page to it.
    atlas = atlas_gen.Atlas()
    code = next(c for c in sorted(atlas.raw)
                if c not in atlas.pages and not atlas.raw[c].get("clade")
                and os.path.exists(os.path.join(_ROOT, "docs", "languages",
                                                f"{c}.md")))
    atlas.pages.add(code)
    page = atlas_gen.scaffold(atlas, code)
    real = atlas_gen._read
    target = os.path.join("languages", f"{code}.md")
    monkeypatch.setattr(atlas_gen, "_read",
                        lambda p: page if p.endswith(target) else real(p))
    out = atlas_gen.outputs(atlas)[f"docs/languages/{code}.md"]
    names = _names_in_order(atlas, atlas.pages)
    at = names.index(f"languages/{code}.md")
    before = os.path.basename(names[at - 1]) if at else "a-z.md"
    assert out.splitlines()[-1].startswith("[← ")
    assert f"]({before}) · [Home](../index.md) · " in out.splitlines()[-1]
    if at + 1 < len(names):
        after = os.path.basename(names[at + 1])
        assert out.splitlines()[-1].endswith(f"]({after})")


def test_overview_block_quotes_the_opening_of_the_notes(atlas):
    spec = orthography2ipa.get("sw")
    with open(os.path.join(os.path.dirname(orthography2ipa.__file__), "data",
                           "sw.json"), encoding="utf-8") as fh:
        notes = json.load(fh)["notes"]
    first = notes.split(". ")[0] + "."
    block = atlas_gen.block_overview(atlas, spec)
    assert f"> {first}" in block
    assert "[research](../specs/quality_tiers.md#research)" in block
    assert f"It cites {len(spec.sources)} works" in block


def test_overview_block_names_the_base_of_the_letter_table(atlas):
    with open(os.path.join(os.path.dirname(orthography2ipa.__file__), "data",
                           "es-AR.json"), encoding="utf-8") as fh:
        raw = json.load(fh)
    spec = orthography2ipa.get("es-AR")
    block = atlas_gen.block_overview(atlas, spec)
    own, total = len(raw["graphemes"]), len(spec.graphemes)
    assert raw["graphemes_base"] == "es-ES" and 0 < own < total
    assert (f"writes {own} of the {total} spellings of its letter table and "
            f"takes the other {total - own} from") in block
    assert "`es-ES`" in block


def test_hand_overview_and_overview_block_break_the_template(atlas):
    text = _page("es-ES").replace(
        "<!-- atlas:header end -->\n",
        "<!-- atlas:header end -->\n\n<!-- atlas:overview begin -->\n"
        "<!-- atlas:overview end -->\n", 1)
    with pytest.raises(atlas_gen.TemplateError, match="hand-written Overview"):
        atlas_gen.render_page(atlas, "es-ES", text)


def test_scaffold_carries_every_block(atlas):
    page = atlas_gen.scaffold(atlas, "sw")
    names = re.findall(r"<!-- atlas:(\w+) begin", page)
    assert names == list(atlas_gen.BLOCKS)
    assert "## Weak points" not in page


@pytest.mark.parametrize("raw, expected", [
    ({"quality": "research"}, True),
    ({"quality": "production"}, True),
    ({"quality": "skeleton"}, False),
    ({"quality": "stub"}, False),
    ({}, True),
    ({"quality": "research", "clade": True}, False),
    ({"quality": "research", "timespan": {"start_year": 900, "end_year": 1500}}, False),
    ({"quality": "research", "timespan": {"start_year": 1500, "end_year": None}}, True),
])
def test_cut_is_living_research_and_production(raw, expected):
    assert atlas_gen.in_cut(raw) is expected


def test_az_pages_with_one_name_are_ordered_by_code(atlas, monkeypatch):
    # ks and kas are both named Kashmiri. Their order must not depend on
    # the order the page set yields them in.
    assert atlas.raw["ks"]["name"] == atlas.raw["kas"]["name"]
    monkeypatch.setattr(atlas, "pages", ["ks", "kas"])
    table = atlas_gen.index_az(atlas).split("## Pages", 1)[1].split("\n\n[A]", 1)[0]
    assert re.findall(r"^\| \[[^\]]+\]\(([^)]+)\)", table, re.M) == ["kas.md", "ks.md"]


def test_rule_change_caps_a_long_letter_list():
    rule = next(r for r in orthography2ipa.get("bo").allophone_rules
                if r.preceded_by_grapheme and len(r.preceded_by_grapheme) > 8)
    change = atlas_gen._change(rule)
    shown = rule.preceded_by_grapheme[:8]
    assert "after " + " ".join(f"⟨{g}⟩" for g in shown) in change
    assert f"⟨{shown[-1]}⟩ and {len(rule.preceded_by_grapheme) - 8} more" in change
