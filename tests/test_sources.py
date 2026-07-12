"""Tests that non-stub languages have at least one source.

Every language with quality != "stub" must have a populated sources array
so that phonological decisions are traceable to published literature.

Wikipedia URLs (``wikipedia`` on the spec, ``wikipedia_url`` on individual
sources) are treated as quick human references, not citable sources.  Their
presence is encouraged but not required for every language.
"""
import glob
import json
import os
import re

import pytest

STUB_QUALITY = {"stub"}

_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")

_WIKIPEDIA_RE = re.compile(
    r"^https://[a-z]{2,}\.wikipedia\.org/wiki/.+$"
)
_URL_RE = re.compile(r"^https?://")


def _all_codes():
    """Return (code, path) for every JSON file."""
    result = []
    for path in sorted(glob.glob(os.path.join(_DATA_DIR, "*.json"))):
        with open(path) as f:
            data = json.load(f)
        code = data.get("code", os.path.basename(path).replace(".json", ""))
        result.append((code, path))
    return result


def _non_stub_codes():
    """Return (code, path) for all non-stub languages."""
    result = []
    for path in sorted(glob.glob(os.path.join(_DATA_DIR, "*.json"))):
        with open(path) as f:
            data = json.load(f)
        quality = data.get("quality", "stub")
        if quality not in STUB_QUALITY:
            code = data.get("code", os.path.basename(path).replace(".json", ""))
            result.append((code, path))
    return result


_ALL = _all_codes()
_NON_STUB = _non_stub_codes()


# ── Bibliographic source tests ───────────────────────────────────────────


@pytest.mark.linguistic
@pytest.mark.parametrize("code,path", _NON_STUB, ids=[c for c, _ in _NON_STUB])
def test_non_stub_has_sources(code: str, path: str) -> None:
    """Every non-stub language must have at least one bibliographic source entry."""
    with open(path) as f:
        data = json.load(f)
    sources = data.get("sources", [])
    assert len(sources) >= 1, (
        f"{code}: non-stub language (quality={data.get('quality')!r}) "
        f"is missing a 'sources' array. Add at least one bibliographic reference."
    )


@pytest.mark.linguistic
@pytest.mark.parametrize("code,path", _NON_STUB, ids=[c for c, _ in _NON_STUB])
def test_source_entries_have_required_fields(code: str, path: str) -> None:
    """Each source entry must have id, author, year (int), and title."""
    with open(path) as f:
        data = json.load(f)
    sources = data.get("sources", [])
    for i, src in enumerate(sources):
        for field in ("id", "author", "year", "title"):
            assert field in src and src[field] is not None, (
                f"{code}: sources[{i}] is missing required field '{field}'"
            )
        assert isinstance(src["year"], int), (
            f"{code}: sources[{i}]['year'] must be an integer, got {src['year']!r}"
        )


@pytest.mark.linguistic
@pytest.mark.parametrize("code,path", _NON_STUB, ids=[c for c, _ in _NON_STUB])
def test_source_ids_are_unique(code: str, path: str) -> None:
    """Source IDs within a single spec must be unique."""
    with open(path) as f:
        data = json.load(f)
    ids = [s["id"] for s in data.get("sources", []) if "id" in s]
    assert len(ids) == len(set(ids)), (
        f"{code}: duplicate source IDs: {[x for x in ids if ids.count(x) > 1]}"
    )


@pytest.mark.linguistic
@pytest.mark.parametrize("code,path", _NON_STUB, ids=[c for c, _ in _NON_STUB])
def test_source_year_is_plausible(code: str, path: str) -> None:
    """Source years must be between 1800 and 2030."""
    with open(path) as f:
        data = json.load(f)
    for i, src in enumerate(data.get("sources", [])):
        year = src.get("year")
        if isinstance(year, int):
            assert 1800 <= year <= 2030, (
                f"{code}: sources[{i}]['year']={year} is outside plausible range [1800, 2030]"
            )


@pytest.mark.linguistic
@pytest.mark.parametrize("code,path", _NON_STUB, ids=[c for c, _ in _NON_STUB])
def test_source_urls_are_well_formed(code: str, path: str) -> None:
    """Source 'url' and 'wikipedia_url' fields, when present, must start with http(s)://."""
    with open(path) as f:
        data = json.load(f)
    for i, src in enumerate(data.get("sources", [])):
        for field in ("url", "wikipedia_url"):
            val = src.get(field)
            if val is not None:
                assert _URL_RE.match(val), (
                    f"{code}: sources[{i}]['{field}']={val!r} is not a valid URL"
                )


@pytest.mark.linguistic
@pytest.mark.parametrize("code,path", _NON_STUB, ids=[c for c, _ in _NON_STUB])
def test_source_wikipedia_urls_point_to_wikipedia(code: str, path: str) -> None:
    """'wikipedia_url' fields must point to *.wikipedia.org/wiki/…."""
    with open(path) as f:
        data = json.load(f)
    for i, src in enumerate(data.get("sources", [])):
        wurl = src.get("wikipedia_url")
        if wurl is not None:
            assert _WIKIPEDIA_RE.match(wurl), (
                f"{code}: sources[{i}]['wikipedia_url']={wurl!r} "
                f"does not match https://<lang>.wikipedia.org/wiki/<article>"
            )


# ── Top-level wikipedia field tests ──────────────────────────────────────


@pytest.mark.linguistic
@pytest.mark.parametrize("code,path", _NON_STUB, ids=[c for c, _ in _NON_STUB])
def test_non_stub_has_wikipedia(code: str, path: str) -> None:
    """Every non-stub language should have at least one top-level 'wikipedia' URL."""
    with open(path) as f:
        data = json.load(f)
    wp = data.get("wikipedia")
    # Accept str (legacy), non-empty list, or non-empty tuple
    if isinstance(wp, str):
        has = bool(wp)
    elif isinstance(wp, (list, tuple)):
        has = len(wp) > 0
    else:
        has = False
    assert has, (
        f"{code}: missing top-level 'wikipedia' field. "
        f"Add at least one Wikipedia article URL for this language."
    )


@pytest.mark.linguistic
@pytest.mark.parametrize("code,path", _NON_STUB, ids=[c for c, _ in _NON_STUB])
def test_wikipedia_url_is_well_formed(code: str, path: str) -> None:
    """All 'wikipedia' URLs must match https://*.wikipedia.org/wiki/…."""
    with open(path) as f:
        data = json.load(f)
    wp = data.get("wikipedia")
    if wp is None:
        return
    urls = [wp] if isinstance(wp, str) else list(wp)
    for url in urls:
        assert _WIKIPEDIA_RE.match(url), (
            f"{code}: wikipedia URL {url!r} does not match "
            f"https://<lang>.wikipedia.org/wiki/<article>"
        )


@pytest.mark.linguistic
@pytest.mark.parametrize("code,path", _NON_STUB, ids=[c for c, _ in _NON_STUB])
def test_wikipedia_urls_are_unique(code: str, path: str) -> None:
    """'wikipedia' list must not contain duplicate URLs."""
    with open(path) as f:
        data = json.load(f)
    wp = data.get("wikipedia")
    if not isinstance(wp, (list, tuple)):
        return
    assert len(wp) == len(set(wp)), (
        f"{code}: duplicate entries in 'wikipedia': {[u for u in wp if wp.count(u) > 1]}"
    )


# ── Runtime model tests ───────────────────────────────────────────────────


def test_linguistic_source_has_wikipedia_url_field() -> None:
    """LinguisticSource dataclass exposes wikipedia_url field."""
    from orthography2ipa.types import LinguisticSource
    src = LinguisticSource(
        id="test2024",
        author="Test, A.",
        year=2024,
        title="Test Title",
        wikipedia_url="https://en.wikipedia.org/wiki/Test",
    )
    assert src.wikipedia_url == "https://en.wikipedia.org/wiki/Test"


def test_linguistic_source_wikipedia_url_defaults_none() -> None:
    """LinguisticSource.wikipedia_url defaults to None."""
    from orthography2ipa.types import LinguisticSource
    src = LinguisticSource(id="x", author="A.", year=2000, title="T")
    assert src.wikipedia_url is None


def test_language_spec_wikipedia_is_tuple() -> None:
    """LanguageSpec.wikipedia is always a tuple of strings, never None."""
    import orthography2ipa
    spec = orthography2ipa.get("fr-FR")
    assert hasattr(spec, "wikipedia")
    assert isinstance(spec.wikipedia, tuple)


def test_wikipedia_list_round_trips_through_loader() -> None:
    """A list of wikipedia URLs in JSON becomes a tuple on the loaded LanguageSpec."""
    import json
    import tempfile
    import os
    from orthography2ipa import json_loader
    from orthography2ipa.json_loader import load_json_spec

    stub = {
        "code": "xx-list",
        "name": "Test List Language",
        "family": "Test",
        "script": "Latin",
        "graphemes": {"a": ["a"]},
        "allophones": {},
        "wikipedia": [
            "https://en.wikipedia.org/wiki/Test_language",
            "https://de.wikipedia.org/wiki/Test_language",
        ],
        "sources": [{"id": "t2024", "author": "T.", "year": 2024, "title": "T"}],
    }
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, dir=_DATA_DIR
    ) as fh:
        json.dump(stub, fh)
        tmp_path = fh.name

    try:
        from pathlib import Path
        json_loader._index["xx-list"] = Path(tmp_path)
        spec = load_json_spec("xx-list")
        assert spec.wikipedia == (
            "https://en.wikipedia.org/wiki/Test_language",
            "https://de.wikipedia.org/wiki/Test_language",
        )
    finally:
        os.unlink(tmp_path)
        json_loader._index.pop("xx-list", None)
        json_loader._specs.pop("xx-list", None)


def test_wikipedia_url_round_trips_through_loader() -> None:
    """A wikipedia URL set in JSON is accessible on the loaded LanguageSpec."""
    import json
    import tempfile
    import os
    from orthography2ipa import json_loader
    from orthography2ipa.json_loader import load_json_spec

    stub = {
        "code": "xx-test",
        "name": "Test Language",
        "family": "Test",
        "script": "Latin",
        "graphemes": {"a": ["a"]},
        "allophones": {},
        "wikipedia": "https://en.wikipedia.org/wiki/Test_language",
        "sources": [
            {
                "id": "test2024",
                "author": "Test, A.",
                "year": 2024,
                "title": "A Test Grammar",
                "wikipedia_url": "https://en.wikipedia.org/wiki/Test_Grammar",
            }
        ],
    }
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, dir=_DATA_DIR
    ) as fh:
        json.dump(stub, fh)
        tmp_path = fh.name

    try:
        # Inject into the loader's index so it can be found by code
        from pathlib import Path
        json_loader._index["xx-test"] = Path(tmp_path)
        spec = load_json_spec("xx-test")
        assert spec.wikipedia == ("https://en.wikipedia.org/wiki/Test_language",)
        assert spec.sources[0].wikipedia_url == "https://en.wikipedia.org/wiki/Test_Grammar"
    finally:
        os.unlink(tmp_path)
        json_loader._index.pop("xx-test", None)
        json_loader._specs.pop("xx-test", None)
