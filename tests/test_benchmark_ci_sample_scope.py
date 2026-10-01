"""``benchmark.py --ci-sample`` honours ``--lang`` and ``--dataset``.

A scoped CI-sample refresh must rescore only the requested rows and carry
every other committed row through byte-for-byte, exactly as the
``--scoreboard`` path already does. Without that, ``--ci-sample --lang X``
silently rescores the whole board and downloads every registered dataset.
"""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


def _row(lang, dataset, per):
    return {"lang": lang, "dataset": dataset, "n": 10, "per": per,
            "harness_version": benchmark.HARNESS_VERSION}


@pytest.fixture
def ci_sample(tmp_path, monkeypatch):
    path = tmp_path / "results_ci_sample.json"
    committed = [_row("ar", "wikipron", 0.5), _row("pt-PT", "wikipron", 0.2),
                 _row("pt-PT", "portuguese_tts", 0.3)]
    path.write_text(json.dumps(committed, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    monkeypatch.setattr(benchmark, "CI_SAMPLE_JSON", str(path))
    return path, committed


def _fake_build_scoreboard(limit, oracle=False, only_langs=None,
                           only_datasets=None, **kwargs):
    """Stand-in scorer: every row it is asked for comes back with per=0.0,
    so any row it touches is visibly changed."""
    assert oracle is False
    assert limit == benchmark.CI_SAMPLE_LIMIT
    rows = []
    for lang, dataset in (("ar", "wikipron"), ("pt-PT", "wikipron"),
                          ("pt-PT", "portuguese_tts")):
        if only_langs and lang not in only_langs:
            continue
        if only_datasets and dataset not in only_datasets:
            continue
        rows.append(_row(lang, dataset, 0.0))
    return rows


def _run(monkeypatch, argv):
    monkeypatch.setattr(benchmark, "build_scoreboard", _fake_build_scoreboard)
    monkeypatch.setattr(sys, "argv", ["benchmark.py"] + argv)
    benchmark.main()


def test_ci_sample_lang_rescores_only_that_language(ci_sample, monkeypatch):
    path, committed = ci_sample
    _run(monkeypatch, ["--ci-sample", "--lang", "pt-PT"])
    written = json.loads(path.read_text(encoding="utf-8"))
    by_key = {(r["lang"], r["dataset"]): r for r in written}
    assert by_key[("ar", "wikipron")] == committed[0]
    assert by_key[("pt-PT", "wikipron")]["per"] == 0.0
    assert by_key[("pt-PT", "portuguese_tts")]["per"] == 0.0
    assert len(written) == 3


def test_ci_sample_dataset_rescores_only_that_dataset(ci_sample, monkeypatch):
    path, committed = ci_sample
    _run(monkeypatch, ["--ci-sample", "--dataset", "wikipron"])
    written = json.loads(path.read_text(encoding="utf-8"))
    by_key = {(r["lang"], r["dataset"]): r for r in written}
    assert by_key[("pt-PT", "portuguese_tts")] == committed[2]
    assert by_key[("ar", "wikipron")]["per"] == 0.0
    assert by_key[("pt-PT", "wikipron")]["per"] == 0.0


def test_ci_sample_without_scope_rescores_everything(ci_sample, monkeypatch):
    path, _ = ci_sample
    _run(monkeypatch, ["--ci-sample"])
    written = json.loads(path.read_text(encoding="utf-8"))
    assert {r["per"] for r in written} == {0.0}
    assert len(written) == 3
