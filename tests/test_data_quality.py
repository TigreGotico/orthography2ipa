"""Permanent data-quality guards over the language spec library.

Validates:
- Every spec declares an explicit quality tier in its JSON file
- Every non-stub spec for a living language resolves (after ancestry
  inheritance) to a non-empty grapheme AND allophone inventory
- Stub tier is reserved for placeholders: a stub may be empty, anything
  else may not
"""
import json
import os
import pathlib
import sys

import pytest

from orthography2ipa import get
from orthography2ipa.types import QualityTier

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from benchmark import can_gate_promotion  # noqa: E402

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


# Deep-orthography PER ceiling, applied uniformly below because
# LanguageSpec carries no orthographic-depth field to key a per-language
# threshold off. See docs/quality_tiers.md for the shallow (0.15) / deep
# (0.25) rationale, and for why the shallow threshold is reviewer- rather
# than machine-enforced.
_PRODUCTION_MIN_N = 500
_PRODUCTION_DEEP_PER_CEILING = 0.25

RESULTS_JSON = (pathlib.Path(__file__).parent.parent
                 / "benchmarks" / "results.json")


def _gate_eligible(tier) -> bool:
    if not isinstance(tier, str):
        return False
    try:
        return can_gate_promotion(tier)
    except ValueError:
        return False


def _benchmark_rows():
    if not RESULTS_JSON.exists():
        return []
    return json.loads(RESULTS_JSON.read_text(encoding="utf-8"))


@pytest.mark.parametrize("code", ALL_CODES)
def test_production_tier_has_qualifying_benchmark(code):
    """A spec claiming `production` must have a benchmarks/results.json
    row for one of its language tags meeting the tier threshold
    documented in docs/quality_tiers.md (n >= 500, PER <= ceiling).

    This guard enforces the deep-orthography ceiling (0.25) uniformly,
    since LanguageSpec has no orthographic-depth field to derive a
    per-language threshold from. The tighter shallow-orthography target
    (0.15) documented for languages like Spanish, Finnish, and Esperanto
    is a reviewer-enforced convention checked against the spec's
    docs/languages/ page during promotion review, not by this test.

    No spec is currently at production tier, so this test is presently
    vacuous for every code — that is expected: tier promotion is a
    test-gated act, not a label change.
    """
    spec = get(code)
    if spec.quality is not QualityTier.PRODUCTION:
        return

    rows = _benchmark_rows()

    def _matches(row_lang: str) -> bool:
        # docs/quality_tiers.md: the gold may be registered under "one of
        # the spec's language tags" — benchmark rows record the tag the
        # dataset was registered with (wikipron "es"), which the registry
        # resolves to the reference variety's spec ("es-ES"). Resolve the
        # row tag the same way the engine would before comparing.
        if row_lang == spec.code:
            return True
        try:
            return get(row_lang).code == spec.code
        except Exception:
            return False

    qualifying = [
        row for row in rows
        if _matches(row.get("lang", ""))
        and row.get("n", 0) >= _PRODUCTION_MIN_N
        and row.get("per", 1.0) <= _PRODUCTION_DEEP_PER_CEILING
        # a row on a competitor-derived or LLM tier can never qualify a
        # promotion (docs/quality_tiers.md); rows without a provenance
        # field predate the tier system and cannot vouch either
        and _gate_eligible(row.get("provenance"))
    ]
    assert qualifying, (
        f"{code} claims production tier but has no benchmarks/results.json "
        f"row with n >= {_PRODUCTION_MIN_N} and "
        f"per <= {_PRODUCTION_DEEP_PER_CEILING}"
    )
