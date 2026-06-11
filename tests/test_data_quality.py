"""Permanent data-quality guards over the language spec library.

Validates:
- Every spec declares an explicit quality tier in its JSON file
- Every non-stub spec for a living language resolves (after ancestry
  inheritance) to a non-empty grapheme AND allophone inventory
- Stub tier is reserved for placeholders: a stub may be empty, anything
  else may not
"""
import json
import pathlib

import pytest

from orthography2ipa import get
from orthography2ipa.types import QualityTier

DATA_DIR = (pathlib.Path(__file__).parent.parent
            / "orthography2ipa" / "data")
ALL_CODES = sorted(p.stem for p in DATA_DIR.glob("*.json"))


@pytest.mark.parametrize("code", ALL_CODES)
def test_explicit_quality_tier(code):
    """The quality tier is part of the contract — never left implicit."""
    raw = json.loads((DATA_DIR / f"{code}.json").read_text(encoding="utf-8"))
    assert raw.get("quality") in ("stub", "skeleton", "research",
                                  "production"), (
        f"{code}.json has no explicit quality tier"
    )


@pytest.mark.parametrize("code", ALL_CODES)
def test_non_stub_resolves_to_content(code):
    """A spec above stub tier must resolve to usable G2P data.

    Empty inventories are only acceptable on stubs; a living language
    advertised as skeleton or better must transcribe something.
    """
    spec = get(code)
    if spec.quality is QualityTier.STUB:
        return
    is_extinct = (spec.timespan is not None
                  and spec.timespan.end_year is not None)
    if is_extinct and not spec.graphemes and not spec.allophones:
        pytest.fail(
            f"{code} is an extinct metadata-only placeholder — its quality "
            f"tier should be 'stub', not '{spec.quality.value}'"
        )
    assert spec.graphemes, f"{code} ({spec.quality.value}) has no graphemes"
    assert spec.allophones, f"{code} ({spec.quality.value}) has no allophones"
