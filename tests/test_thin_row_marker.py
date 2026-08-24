"""Tests for the thin-row statistical-weight marker in the scoreboard.

A bootstrap CI is computed by resampling a row's per-word PER list with
replacement. Below a handful of scored words the resample can only ever
reproduce the values it started with, so the interval collapses toward
the point estimate instead of widening the way it would on a real
sample: a row scored on a single word gets a `[x, x]` "confidence
interval" that looks perfectly precise despite being the least reliable
row on the board. write_scoreboard must flag such rows in the rendered
`N` column so a reader cannot mistake a degenerate interval for a
narrow, trustworthy one.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import THIN_ROW_MARK, THIN_ROW_N, write_scoreboard  # noqa: E402


def _row(n, **overrides):
    row = {
        "lang": "xx",
        "dataset": "wikipron",
        "n": n,
        "per": 0.1,
        "per_ci_low": 0.1,
        "per_ci_high": 0.1,
        "exact_match": 0.9,
        "quality_tier": "research",
        "provenance": "crowd-scraped",
        "harness_version": "1.1",
        "limit": None,
    }
    row.update(overrides)
    return row


def test_thin_row_is_marked_in_n_column(tmp_path, monkeypatch):
    import benchmark

    md = tmp_path / "scoreboard.md"
    js = tmp_path / "results.json"
    monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(md))
    monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(js))

    thin = _row(1, lang="xx", dataset="thin_ds")
    write_scoreboard([thin])

    md_text = md.read_text(encoding="utf-8")
    assert f"| xx | thin_ds | 1{THIN_ROW_MARK} |" in md_text


def test_well_sampled_row_is_not_marked(tmp_path, monkeypatch):
    import benchmark

    md = tmp_path / "scoreboard.md"
    js = tmp_path / "results.json"
    monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(md))
    monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(js))

    thick = _row(1713, lang="xx", dataset="thick_ds")
    write_scoreboard([thick])

    md_text = md.read_text(encoding="utf-8")
    assert f"| xx | thick_ds | 1713 |" in md_text
    assert THIN_ROW_MARK not in md_text.split("thick_ds")[1].split("|")[1]


def test_thin_row_threshold_is_documented_in_the_legend(tmp_path, monkeypatch):
    """The legend paragraph explaining the marker must actually mention
    both the marker glyph and the threshold, so the two never drift
    apart if THIN_ROW_N is tuned later."""
    import benchmark

    md = tmp_path / "scoreboard.md"
    js = tmp_path / "results.json"
    monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(md))
    monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(js))

    write_scoreboard([_row(5)])

    md_text = md.read_text(encoding="utf-8")
    assert THIN_ROW_MARK in md_text
    assert str(THIN_ROW_N) in md_text


def test_results_json_values_are_unaffected_by_the_marker(tmp_path, monkeypatch):
    """The marker is a rendering-only annotation: results.json keeps the
    raw integer n, per, and CI bounds untouched."""
    import benchmark
    import json

    md = tmp_path / "scoreboard.md"
    js = tmp_path / "results.json"
    monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(md))
    monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(js))

    row = _row(1, per=0.7143, per_ci_low=0.7143, per_ci_high=0.7143)
    write_scoreboard([row])

    data = json.loads(js.read_text(encoding="utf-8"))
    assert data[0]["n"] == 1
    assert data[0]["per"] == 0.7143
    assert data[0]["per_ci_low"] == 0.7143
    assert data[0]["per_ci_high"] == 0.7143


def test_committed_scoreboard_is_in_sync_with_generator(tmp_path, monkeypatch):
    """The committed docs/scoreboard.md must be byte-identical to what
    write_scoreboard(read_scoreboard_rows()) produces. This catches drift
    where the generator changes but the output file is not regenerated.

    (If this test fails, run: `PYTHONPATH=$PWD python -c
    "import sys; sys.path.insert(0,'scripts'); import benchmark as bm;
    bm.write_scoreboard(bm.read_scoreboard_rows())"` and commit the result.)
    """
    import benchmark
    import json

    # Load the committed scoreboard rows.
    repo_root = os.path.dirname(os.path.dirname(__file__))
    results_json = os.path.join(repo_root, "benchmarks", "results.json")
    committed_md = os.path.join(repo_root, "docs", "scoreboard.md")

    if not os.path.exists(results_json) or not os.path.exists(committed_md):
        # Skip if not running in the repo (e.g., on a minimal test install).
        return

    with open(results_json, encoding="utf-8") as fh:
        rows = json.load(fh)

    # Regenerate the scoreboard in a temp location.
    regen_md = tmp_path / "scoreboard_regenerated.md"
    regen_js = tmp_path / "results_regen.json"
    monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(regen_md))
    monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(regen_js))

    write_scoreboard(rows)

    # Compare the regenerated file to the committed file.
    with open(committed_md, encoding="utf-8") as fh:
        committed_text = fh.read()
    regenerated_text = regen_md.read_text(encoding="utf-8")

    if committed_text != regenerated_text:
        # Provide a helpful error message with the first few differing lines.
        committed_lines = committed_text.splitlines()
        regen_lines = regenerated_text.splitlines()
        for i, (c, r) in enumerate(zip(committed_lines, regen_lines)):
            if c != r:
                raise AssertionError(
                    f"Scoreboard drift detected at line {i + 1}. "
                    f"Run: PYTHONPATH=$PWD python -c \"import sys; "
                    f"sys.path.insert(0,'scripts'); import benchmark as bm; "
                    f"bm.write_scoreboard(bm.read_scoreboard_rows())\" "
                    f"and commit the changes."
                )
        # If all line-by-line comparisons match but the full text doesn't,
        # it's a line-ending or final-newline difference.
        raise AssertionError(
            "Scoreboard drift detected (line-ending or final-newline). "
            "Run the regeneration command above and commit the changes."
        )
