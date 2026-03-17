"""Tests that non-stub languages have at least one source.

Every language with quality != "stub" must have a populated sources array
so that phonological decisions are traceable to published literature.
"""
import glob
import json
import os

import pytest

STUB_QUALITY = {"stub"}

_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")


def _non_stub_codes():
    """Return a list of (code, path) tuples for all non-stub languages."""
    result = []
    for path in sorted(glob.glob(os.path.join(_DATA_DIR, "*.json"))):
        with open(path) as f:
            data = json.load(f)
        quality = data.get("quality", "stub")
        if quality not in STUB_QUALITY:
            code = data.get("code", os.path.basename(path).replace(".json", ""))
            result.append((code, path))
    return result


_NON_STUB = _non_stub_codes()


@pytest.mark.linguistic
@pytest.mark.parametrize("code,path", _NON_STUB, ids=[c for c, _ in _NON_STUB])
def test_non_stub_has_sources(code: str, path: str) -> None:
    """Every non-stub language must have at least one bibliographic source entry.

    This is a ``@pytest.mark.linguistic`` test — it is part of the ongoing
    linguistic reference audit and will fail for languages not yet covered.
    Run with: ``pytest -m linguistic tests/test_sources.py``

    Phase coverage: Phase 1 (Germanic) is complete. Other families are TODO.
    See ``TODO.md`` and ``PLAN.md`` for the full audit roadmap.
    """
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
    """Each source entry must have id, author, year, and title."""
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
