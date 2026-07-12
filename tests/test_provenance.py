"""Tests for the per-dataset reliability/provenance classification added
to scripts/benchmark.py.

Reliable G2P "gold" barely exists: most benchmark datasets are
semi-automated, dictionary-extracted, community-scraped, or a
phonemizer's own output reused as a reference. Every registered dataset
must therefore carry an explicit reliability tier so the caveat travels
with the numbers (docs/scoreboard.md column + benchmarks/results.json
field). These tests are a forcing function: a new dataset cannot be
registered without classifying it, and the scoreboard must keep emitting
the provenance column/field.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import (  # noqa: E402
    DATASETS,
    PROVENANCE,
    RELIABILITY_TIERS,
    build_scoreboard,
    write_scoreboard,
)


def test_every_dataset_has_a_reliability_tier():
    """Forcing function: adding a dataset to DATASETS without an explicit,
    evidence-based reliability classification fails CI."""
    missing = sorted(set(DATASETS) - set(PROVENANCE))
    assert not missing, f"datasets without a provenance tier: {missing}"


def test_provenance_tiers_are_known_values():
    for dataset, tier in PROVENANCE.items():
        assert tier in RELIABILITY_TIERS, (
            f"{dataset} has unknown tier {tier!r}; "
            f"expected one of {RELIABILITY_TIERS}"
        )


def test_no_orphan_provenance_entries():
    """Every classified dataset must actually be registered."""
    orphan = sorted(set(PROVENANCE) - set(DATASETS))
    assert not orphan, f"provenance entries for unregistered datasets: {orphan}"


def test_every_tier_is_in_use():
    """The taxonomy is not aspirational: each tier classifies at least one
    real registered dataset (so the docs table is grounded)."""
    used = set(PROVENANCE.values())
    assert used == set(RELIABILITY_TIERS)


def test_write_scoreboard_emits_provenance_column_and_field(tmp_path, monkeypatch):
    """write_scoreboard must surface provenance both as a scoreboard column
    and as a results.json field, so regeneration can never silently drop
    the reliability signal."""
    import benchmark

    md = tmp_path / "scoreboard.md"
    js = tmp_path / "results.json"
    monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(md))
    monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(js))

    rows = [
        {
            "lang": "xx",
            "dataset": "wikipron",
            "n": 3,
            "per": 0.1,
            "per_ci_low": 0.0,
            "per_ci_high": 0.2,
            "exact_match": 0.9,
            "quality_tier": "research",
            "provenance": "crowd-scraped",
            "harness_version": benchmark.HARNESS_VERSION,
            "limit": 300,
        }
    ]
    write_scoreboard(rows)

    md_text = md.read_text(encoding="utf-8")
    assert "Provenance" in md_text  # column header
    assert "crowd-scraped" in md_text  # cell value
    # grain-of-salt banner survives regeneration
    assert "Grain of salt" in md_text

    import json

    data = json.loads(js.read_text(encoding="utf-8"))
    assert data[0]["provenance"] == "crowd-scraped"


def test_build_scoreboard_row_shape_includes_provenance():
    """build_scoreboard tags each row with its dataset's tier. Uses a tiny
    fake dataset so the test needs no network."""
    import benchmark

    def _fake_loader(lang, limit):
        return [("cat", "kat"), ("dog", "dog")]

    monkey_datasets = {"wikipron": (_fake_loader, ["en"])}
    orig = benchmark.DATASETS
    try:
        benchmark.DATASETS = monkey_datasets
        rows = build_scoreboard(limit=10)
    finally:
        benchmark.DATASETS = orig

    assert rows, "expected at least one scored row"
    assert rows[0]["provenance"] == PROVENANCE["wikipron"] == "crowd-scraped"
