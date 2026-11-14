"""The shipped Arabic folded PER and omission score reproduce from the gold.

``tests/test_folded_per.py`` and ``tests/test_omission_score.py`` pin the two
helpers on synthetic pairs. Nothing pinned the values the ``ar`` spec and the
board actually ship, so a spec or gold change could move them silently. This
runs both scripts against the real ``ar`` / ``wikipron`` gold and asserts that
``ar.json``'s ``valid_ceiling`` and the board row carry what they compute.

Skips when the gold is not cached, like ``test_gawri_tone_ceiling``.
"""
import json
import os
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

SEGMENTS = ("a", "i", "u")


def _pairs():
    import benchmark as bm

    pairs = bm.load_wikipron("ar", 10 ** 9)
    if not pairs:
        pytest.skip("ar wikipron gold not available")
    return pairs


def test_shipped_folded_per_reproduces_and_is_the_ceiling():
    import folded_per as fp

    result = fp.folded_per(_pairs(), "ar", SEGMENTS)
    measured = round(result.score, 4)

    with open(ROOT / "orthography2ipa" / "data" / "ar.json", encoding="utf-8") as fh:
        spec = json.load(fh)
    assert spec["valid_ceiling"]["wikipron"]["per"] == measured

    with open(ROOT / "benchmarks" / "results.json", encoding="utf-8") as fh:
        rows = json.load(fh)
    row = next(r for r in rows if r["lang"] == "ar" and r["dataset"] == "wikipron")
    assert row["valid_ceiling"]["per"] == measured
    # the value this PR ships; a change here must be deliberate
    assert measured == 0.1656


def test_shipped_omission_score_reproduces():
    import omission_score as om

    result = om.omission_score(_pairs(), "ar", SEGMENTS)
    assert round(result.score, 4) == 0.2425
