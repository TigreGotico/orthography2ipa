"""Tests for the primary-source gold set and its benchmark loader.

The rows are transcriptions copied out of the grammars, monographs and theses
the language specs cite. Their whole value is provenance: a row that cannot say
which source and which PRINTED page it came from is worthless, and a row whose
notation was silently coerced is worse than worthless. These tests police that.
"""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import (  # noqa: E402
    DATASETS,
    PROVENANCE,
    _PRIMARY_SOURCES_DIR,
    load_primary_sources,
    read_primary_source_rows,
)

from orthography2ipa import registry  # noqa: E402

LEVELS = {"broad", "narrow"}
CONFIDENCES = {"high", "medium", "low"}
NOTATIONS = {"ipa", "arabicist-transliteration"}
PROVENANCES = {"as-printed", "editor-supplied"}

ROWS = read_primary_source_rows()

with open(os.path.join(_PRIMARY_SOURCES_DIR, "sources.json"), encoding="utf-8") as _fh:
    SOURCES = json.load(_fh)


def test_rows_are_not_empty():
    assert len(ROWS) >= 60


@pytest.mark.parametrize("row", ROWS, ids=[r["id"] for r in ROWS])
def test_row_shape(row):
    assert row["level"] in LEVELS
    assert row["confidence"] in CONFIDENCES
    assert row["notation_system"] in NOTATIONS
    assert row["orthography_provenance"] in PROVENANCES
    assert row["ipa"], "a row with no IPA is not gold"
    assert row["gloss"]
    assert row["source_notation"], "the source's own notation must be kept verbatim"


@pytest.mark.parametrize("row", ROWS, ids=[r["id"] for r in ROWS])
def test_row_cites_a_known_source_and_a_printed_page(row):
    assert row["source"] in SOURCES
    page = str(row["page"])
    assert page.isdigit(), "page must be the printed folio, not a range or an index"


def test_row_ids_are_unique_and_prefixed_by_their_source():
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids))
    for row in ROWS:
        assert row["id"].startswith(row["source"] + "-")


@pytest.mark.parametrize("row", ROWS, ids=[r["id"] for r in ROWS])
def test_lang_is_a_real_spec_code_or_explicitly_null(row):
    """Null beats wrong: a row may decline to map to a spec, but it may not
    invent a code."""
    lang = row.get("lang")
    if lang is None:
        return
    assert registry.get(lang) is not None


@pytest.mark.parametrize(
    "row",
    [r for r in ROWS if r["notation_system"] != "ipa"],
    ids=[r["id"] for r in ROWS if r["notation_system"] != "ipa"],
)
def test_transliterated_rows_are_never_high_confidence(row):
    """A transliteration→IPA conversion is our inference, not the source's
    claim, so it may not masquerade as certainty."""
    assert row["confidence"] in {"medium", "low"}


@pytest.mark.parametrize(
    "row",
    [r for r in ROWS if r["orthography_provenance"] == "editor-supplied"],
    ids=[r["id"] for r in ROWS if r["orthography_provenance"] == "editor-supplied"],
)
def test_editor_supplied_orthography_is_explained(row):
    assert row["notes"], "an editor-supplied spelling must carry a note"


def test_sources_document_their_folio_offset():
    """pdftotext's page index is not the printed page. Each source must say how
    the two relate, so a later editor can check a citation."""
    for key, src in SOURCES.items():
        assert src["pagination"], key
        assert src["url"], key
        assert src["access"] == "open", f"{key}: only open sources can be re-checked"


def test_loader_is_registered_and_classified():
    assert "primary_sources" in DATASETS
    assert PROVENANCE["primary_sources"] == "expert-human"


def test_loader_returns_word_ipa_pairs_for_a_registered_language():
    loader, langs = DATASETS["primary_sources"]
    assert "ar-IQ" in langs
    pairs = loader("ar-IQ", 100)
    assert pairs
    assert ("قَلْب", "ɡalˤʊb") in pairs


def test_loader_prefers_the_vocalized_arabic_orthography():
    """o2i's Arabic input contract is diacritized text; the bare printed form
    would score the engine on input it cannot vowelize."""
    word, _ipa = load_primary_sources("ar-SY", 1)[0]
    assert word == "فِيد"


def test_loader_respects_the_limit_and_filters_by_language():
    assert len(load_primary_sources("ar-IQ", 3)) == 3
    assert load_primary_sources("ar-IQ", 100) != load_primary_sources("ar-JO", 100)


def test_loader_returns_nothing_for_an_unrepresented_language():
    assert load_primary_sources("en-GB", 10) == []


def test_registered_langs_are_exactly_the_langs_present_in_the_rows():
    _loader, langs = DATASETS["primary_sources"]
    assert set(langs) == {r["lang"] for r in ROWS if r.get("lang")}
    for lang in langs:
        assert load_primary_sources(lang, 100), f"{lang} registered but yields no pairs"
