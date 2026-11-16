"""Tests for the primary-source gold set and its benchmark loader.

The rows are transcriptions copied out of the grammars, monographs and theses
the language specs cite. Their whole value is provenance: a row that cannot say
which source and which PRINTED page it came from is worthless, and a row whose
notation was silently coerced is worse than worthless. These tests police that.
"""
import json
import os
import re
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


DOI = re.compile(r"^10\.\d{4,9}/\S+$")


def _isbn13_is_valid(isbn):
    digits = isbn.replace("-", "")
    if len(digits) != 13 or not digits.isdigit():
        return False
    return sum(int(d) * (3 if i % 2 else 1) for i, d in enumerate(digits)) % 10 == 0


def source_defects(src, rows):
    """Why a reader could not find each of ``rows`` in ``src``.

    An open source links a copy anybody can read. A closed source has no such
    copy, so it is cited by its DOI or ISBN, and each row must name the printed
    page that a reader of the book turns to."""
    defects = []
    if not src.get("pagination"):
        defects.append("no pagination note")
    if src.get("access") == "open":
        if not src.get("url", "").startswith(("https://", "http://")):
            defects.append("an open source needs the URL of a copy")
    elif src.get("access") == "closed":
        if src.get("url"):
            defects.append("a closed source is cited by DOI or ISBN, not by a link to a copy")
        doi, isbn = src.get("doi"), src.get("isbn")
        if not (doi and DOI.match(doi)) and not (isbn and _isbn13_is_valid(isbn)):
            defects.append("a closed source needs a DOI or a valid ISBN-13")
        defects += [f"{row['id']}: no printed page" for row in rows
                    if not str(row.get("page") or "").isdigit()]
    else:
        defects.append(f"access must be open or closed, not {src.get('access')!r}")
    return defects


@pytest.mark.parametrize("key", sorted(SOURCES))
def test_every_source_can_be_found_by_a_reader(key):
    rows = [r for r in ROWS if r["source"] == key]
    assert source_defects(SOURCES[key], rows) == []


_CLOSED = {"pagination": "printed page", "access": "closed",
           "doi": "10.1093/oso/9780199257591.001.0001"}
_ROW = {"id": "x-001", "page": "17"}


@pytest.mark.parametrize("src, rows, defect", [
    (_CLOSED, [{"id": "x-001", "page": ""}], "x-001: no printed page"),
    (_CLOSED, [{"id": "x-001"}], "x-001: no printed page"),
    (_CLOSED, [{"id": "x-001", "page": "17-18"}], "x-001: no printed page"),
    ({**_CLOSED, "doi": None}, [_ROW], "a closed source needs a DOI or a valid ISBN-13"),
    ({**_CLOSED, "doi": None, "isbn": "9780199257592"}, [_ROW],
     "a closed source needs a DOI or a valid ISBN-13"),
    ({**_CLOSED, "url": "https://example.org/copy.pdf"}, [_ROW],
     "a closed source is cited by DOI or ISBN, not by a link to a copy"),
    ({"pagination": "p", "access": "open"}, [_ROW], "an open source needs the URL of a copy"),
    ({"pagination": "p", "access": "paywalled", "url": "https://x"}, [_ROW],
     "access must be open or closed, not 'paywalled'"),
])
def test_an_unfindable_source_is_refused(src, rows, defect):
    assert defect in source_defects(src, rows)


@pytest.mark.parametrize("src", [
    _CLOSED,
    {**_CLOSED, "doi": None, "isbn": "978-0-19-925759-1"},
    {"pagination": "p", "access": "open", "url": "https://example.org/a.pdf"},
])
def test_a_findable_source_passes(src):
    assert source_defects(src, [_ROW]) == []


def test_loader_is_registered_and_classified():
    assert "primary_sources" in DATASETS
    assert PROVENANCE["primary_sources"] == "expert-human"


def test_loader_returns_word_ipa_pairs_for_a_registered_language():
    loader, langs = DATASETS["primary_sources"]
    assert "acm-IQ" in langs
    pairs = loader("acm-IQ", 100)
    assert pairs
    assert ("قَلْب", "ɡalˤʊb") in pairs


def test_loader_prefers_the_vocalized_arabic_orthography():
    """o2i's Arabic input contract is diacritized text; the bare printed form
    would score the engine on input it cannot vowelize."""
    word, _ipa = load_primary_sources("apc-SY", 1)[0]
    assert word == "فِيد"


def test_loader_respects_the_limit_and_filters_by_language():
    assert len(load_primary_sources("acm-IQ", 3)) == 3
    assert load_primary_sources("acm-IQ", 100) != load_primary_sources("apc-JO", 100)


def test_loader_returns_nothing_for_an_unrepresented_language():
    assert load_primary_sources("en-GB", 10) == []


def test_registered_langs_are_exactly_the_langs_present_in_the_rows():
    _loader, langs = DATASETS["primary_sources"]
    assert set(langs) == {r["lang"] for r in ROWS if r.get("lang")}
    for lang in langs:
        assert load_primary_sources(lang, 100), f"{lang} registered but yields no pairs"
