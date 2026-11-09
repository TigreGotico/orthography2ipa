"""The language atlas generator: its blocks, its template and its check mode.

``scripts/gen_language_atlas.py`` owns the blocks between the atlas markers of
each language page and the four index pages. These tests hold the contract a
page author relies on: the check mode fails on a stale block, hand-written
text survives a rewrite, the template is enforced, and the values the blocks
print come from the spec, not from the generator.
"""
import importlib.util
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
    for child in ("mwl-x-sendim", "mwl-x-ifanes"):
        assert f"`{child}`" in header


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
