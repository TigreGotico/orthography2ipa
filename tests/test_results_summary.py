"""``benchmarks/results_summary.json`` and the headline row of a language."""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402
from benchmark import headline_row, report_row_changes, results_summary  # noqa: E402


def _row(dataset, n, tier, gating, lang="xx", per=0.1):
    return {"lang": lang, "dataset": dataset, "n": n, "per": per,
            "provenance": tier, "gating": gating}


def test_gating_row_beats_a_better_tier_that_does_not_gate():
    rows = [_row("a", 5000, "expert-human", False),
            _row("b", 5000, "crowd-scraped", True)]
    assert headline_row(rows)["dataset"] == "b"


def test_row_below_min_n_loses_to_a_worse_tier_above_it():
    rows = [_row("a", 999, "expert-human", True),
            _row("b", 1000, "crowd-scraped", True)]
    assert headline_row(rows)["dataset"] == "b"


def test_small_rows_compete_when_no_row_reaches_min_n():
    rows = [_row("a", 600, "crowd-scraped", True),
            _row("b", 500, "lexicon-derived", True)]
    assert headline_row(rows)["dataset"] == "b"


def test_same_tier_takes_the_largest_n_then_the_first_name():
    rows = [_row("b", 2000, "crowd-scraped", True),
            _row("c", 3000, "crowd-scraped", True),
            _row("a", 3000, "crowd-scraped", True)]
    assert headline_row(rows)["dataset"] == "a"


def test_language_with_no_gating_row_takes_its_best_other_row():
    rows = [_row("a", 4000, "epitran-derived", False),
            _row("b", 4000, "espeak-derived", False)]
    assert headline_row(rows)["dataset"] == "b"
    assert headline_row([]) is None


def test_summary_rows_carry_gold_fold_and_headline_values():
    rows = [_row("wikipron", 2000, "crowd-scraped", True, "pt-BR", 0.2),
            _row("portuguese_unified", 23000, "lexicon-derived", True,
                 "pt-BR", 0.1421),
            _row("vox_communis", 900, "epitran-derived", False, "ab", 0.3)]
    folded = [{"lang": "pt-BR", "dataset": "portuguese_unified",
               "folded_per": 0.0679, "folds": ["michaelis_ã"]}]
    out = results_summary(rows, folded, "1.2.3a4", "abc")
    assert (out["o2i_version"], out["o2i_git_sha"], out["min_n"]) == \
        ("1.2.3a4", "abc", 1000)
    by = {(r["lang"], r["dataset"]): r for r in out["rows"]}
    assert [(r["lang"], r["dataset"]) for r in out["rows"]] == [
        ("ab", "vox_communis"), ("pt-BR", "portuguese_unified"),
        ("pt-BR", "wikipron")]
    pu = by[("pt-BR", "portuguese_unified")]
    assert pu == {
        "dataset": "portuguese_unified", "lang": "pt-BR",
        "gold_source": "Infopedia, Michaelis and pt.wiktionary "
                       "pronunciation lexicon",
        "gold_provenance": benchmark.GOLD_SOURCES["portuguese_unified"][
            "provenance"],
        "reliability_tier": "lexicon-derived", "gating": True,
        "headline": True, "n": 23000, "strict_per": 0.1421,
        "folded_per": 0.0679, "folds": ["michaelis_ã"]}
    assert by[("pt-BR", "wikipron")]["headline"] is False
    assert by[("pt-BR", "wikipron")]["folded_per"] is None
    assert by[("pt-BR", "wikipron")]["folds"] == []
    assert by[("ab", "vox_communis")]["headline"] is True


def test_gold_sources_table_covers_every_dataset():
    assert set(benchmark.GOLD_SOURCES) == set(benchmark.DATASETS)
    for entry in benchmark.GOLD_SOURCES.values():
        assert entry["tier"] in benchmark.RELIABILITY_TIERS
        assert entry["source"] and entry["provenance"]


def test_every_applied_fold_has_a_label():
    with open(benchmark.FOLD_LABELS_JSON, encoding="utf-8") as fh:
        labels = json.load(fh)
    with open(benchmark.NOTATION_FOLDS_JSON, encoding="utf-8") as fh:
        applied = {f for r in json.load(fh) for f in r["folds"]}
    assert applied == {"michaelis_ã", "michaelis_no_palatal", "michaelis_final_r"}
    assert applied <= set(labels)


def test_committed_summary_matches_the_committed_board():
    with open(benchmark.RESULTS_SUMMARY_JSON, encoding="utf-8") as fh:
        committed = json.load(fh)
    with open(benchmark.NOTATION_FOLDS_JSON, encoding="utf-8") as fh:
        folded = json.load(fh)
    expected = results_summary(benchmark.read_scoreboard_rows(), folded,
                               committed["o2i_version"],
                               committed["o2i_git_sha"])
    assert committed == expected, (
        "run: python scripts/benchmark.py --results-summary")


def test_row_changes_count_rows_and_diff_fields():
    old = [{"lang": "a", "dataset": "d", "per": 0.5},
           {"lang": "b", "dataset": "d", "per": 0.2}]
    new = [{"lang": "a", "dataset": "d", "per": 0.4},
           {"lang": "b", "dataset": "d", "per": 0.2},
           {"lang": "c", "dataset": "d", "per": 0.1}]
    written = benchmark.merge_scoreboard_rows(old, new)
    assert report_row_changes(old, new, written) == [
        "rows in: 2 committed, 3 rescored; rows out: 3",
        "rows changed: 2",
        "  ~ d/a: per 0.5 -> 0.4",
        "  + d/c: new row",
    ]


@pytest.fixture
def ci_sample(tmp_path, monkeypatch):
    path = tmp_path / "results_ci_sample.json"
    committed = [{"lang": "ar", "dataset": "wikipron", "n": 10, "per": 0.5},
                 {"lang": "pt-PT", "dataset": "wikipron", "n": 10, "per": 0.2}]
    path.write_text(json.dumps(committed), encoding="utf-8")
    monkeypatch.setattr(benchmark, "CI_SAMPLE_JSON", str(path))

    def fake(limit, oracle=False, only_langs=None, only_datasets=None, **kw):
        return [{"lang": r["lang"], "dataset": r["dataset"], "n": 10,
                 "per": 0.0} for r in committed
                if (not only_langs or r["lang"] in only_langs)
                and (not only_datasets or r["dataset"] in only_datasets)]
    monkeypatch.setattr(benchmark, "build_scoreboard", fake)
    return path


def _main(monkeypatch, argv):
    monkeypatch.setattr(sys, "argv", ["benchmark.py"] + argv)
    benchmark.main()


def test_scoped_ci_sample_prints_rows_in_out_and_the_diff(
        ci_sample, monkeypatch, capsys):
    _main(monkeypatch, ["--ci-sample", "--lang", "pt-PT",
                        "--dataset", "wikipron"])
    out = capsys.readouterr().out.splitlines()
    assert out[:3] == ["rows in: 2 committed, 1 rescored; rows out: 2",
                       "rows changed: 1",
                       "  ~ wikipron/pt-PT: per 0.2 -> 0.0"]
    written = json.loads(ci_sample.read_text(encoding="utf-8"))
    assert [r["per"] for r in written] == [0.5, 0.0]


def test_whole_ci_sample_prints_the_same_summary(ci_sample, monkeypatch, capsys):
    _main(monkeypatch, ["--ci-sample"])
    out = capsys.readouterr().out.splitlines()
    assert out[:2] == ["rows in: 2 committed, 2 rescored; rows out: 2",
                       "rows changed: 2"]
