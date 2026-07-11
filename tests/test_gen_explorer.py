"""Tests for scripts/gen_explorer.py.

Covers the language-data explorer generator: every registered code must
be embedded, the embedded ``DATA`` blob must be valid JSON, the page
must not reference any external (http/https) resource in a <script src>,
<link href> or <img src> attribute (citation URLs living inside DATA are
fine — they are data, not resource loads), and output must be
byte-identical across repeated runs given the same inputs (no
timestamps/randomness).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import gen_explorer  # noqa: E402
import orthography2ipa as o2i  # noqa: E402


def _extract_data(html: str) -> dict:
    marker = "const DATA = "
    idx = html.index(marker) + len(marker)
    data, _end = json.JSONDecoder().raw_decode(html, idx)
    return data


def test_render_html_contains_every_registered_code():
    data = gen_explorer.build_data()
    html = gen_explorer.render_html(data)
    all_codes = set(o2i.available_codes())
    assert set(data["codes"]) == all_codes
    for code in all_codes:
        assert json.dumps(code) in html


def test_embedded_data_is_valid_json_and_matches_registry():
    data = gen_explorer.build_data()
    html = gen_explorer.render_html(data)
    embedded = _extract_data(html)
    assert embedded["codes"] == data["codes"]
    assert set(embedded["languages"].keys()) == set(o2i.available_codes())


def test_no_external_resource_references_in_html_tags():
    data = gen_explorer.build_data()
    html = gen_explorer.render_html(data)
    for tag_pattern in (
        r'<script[^>]*\bsrc\s*=\s*"[^"]*"',
        r'<link[^>]*\bhref\s*=\s*"[^"]*"',
        r'<img[^>]*\bsrc\s*=\s*"[^"]*"',
    ):
        for match in re.finditer(tag_pattern, html, re.IGNORECASE):
            assert "http://" not in match.group(0)
            assert "https://" not in match.group(0)


def test_no_stray_harness_tags():
    data = gen_explorer.build_data()
    html = gen_explorer.render_html(data)
    for token in ("</content>", "</invoke>", "antml:", "<function", "<parameter"):
        assert token not in html


def test_deterministic_output_across_runs():
    data1 = gen_explorer.build_data()
    html1 = gen_explorer.render_html(data1)
    data2 = gen_explorer.build_data()
    html2 = gen_explorer.render_html(data2)
    assert html1 == html2


def test_quality_tier_counts_sum_to_total_languages():
    data = gen_explorer.build_data()
    assert sum(data["counts"].values()) == len(data["codes"])


def test_benchmark_rows_joined_for_a_known_scored_language():
    data = gen_explorer.build_data()
    scored = [
        code for code, d in data["languages"].items() if d["benchmarks"]
    ]
    assert scored, "expected at least one language with joined benchmark rows"
    sample = data["languages"][scored[0]]
    row = sample["benchmarks"][0]
    assert "dataset" in row and "per" in row


def test_is_family_flags_ended_ancestor_stages_not_living_languages():
    """The tree's family/proto marker: a genetic parent whose timespan has
    ENDED is an ancestry grouping; a still-spoken language that also parents a
    sub-variety is not."""
    langs = gen_explorer.build_data()["languages"]
    # Ended proto/medieval stages that are someone's parent → family.
    assert langs["roa-x-galaicopt"]["is_family"] is True   # Galaico-Portuguese
    assert langs["pt-PT-x-medieval"]["is_family"] is True
    # Living languages (open-ended timespan) → not family, even when they
    # parent a sub-variety or their gold is keyed under a bare code.
    assert langs["gl"]["is_family"] is False
    assert langs["pt-PT"]["is_family"] is False
    assert langs["es-ES"]["is_family"] is False
    # Pure ancestry stubs ("… (family node)", proto-language nodes) carry tier
    # `stub` and often no timespan — they must still be flagged as groupings.
    assert langs["bnt"]["is_family"] is True   # Proto-Bantu (family node)
    assert langs["afa"]["is_family"] is True   # Afroasiatic (family node)


def test_explorer_ships_tree_and_graph_views():
    html = gen_explorer.render_html(gen_explorer.build_data())
    for anchor in ('id="view-tree"', 'id="view-graph"', 'id="tree-root"',
                   'buildForest', 'renderGraph', '--edge-adstrate'):
        assert anchor in html
