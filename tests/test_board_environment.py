"""A whole-board regeneration never drops a committed row silently, and it
records the environment that scored the board.

``wikipron_ar_diacritized/ar`` scores through the optional ``text2tashkeel``
package. ``build_scoreboard`` skips a row whose loader raises, so a
regeneration on a box without that package used to write a board one row
short and exit 0.
"""
import ast
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


def _row(lang, dataset, per=0.1):
    return {"lang": lang, "dataset": dataset, "n": 50, "per": per,
            "quality_tier": "research", "provenance": "crowd-scraped",
            "harness_version": benchmark.HARNESS_VERSION, "limit": None}


@pytest.fixture
def board(tmp_path, monkeypatch):
    """A committed board with an ar-diacritized row and a wikipron row."""
    committed = [_row("ar", "wikipron_ar_diacritized"), _row("ar", "wikipron")]
    results = tmp_path / "results.json"
    results.write_text(json.dumps(committed), encoding="utf-8")
    sample = tmp_path / "results_ci_sample.json"
    sample.write_text(json.dumps(committed), encoding="utf-8")
    monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(results))
    monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(tmp_path / "s.md"))
    monkeypatch.setattr(benchmark, "CI_SAMPLE_JSON", str(sample))
    monkeypatch.setattr(benchmark, "ENVIRONMENT_JSON",
                        str(tmp_path / "results_environment.json"),
                        raising=False)
    return results, committed


def _scorer_without_ar_diacritized(limit, oracle=False, only_langs=None,
                                   only_datasets=None, **kwargs):
    rows = [_row("ar", "wikipron", 0.2)]
    return [r for r in rows
            if not only_datasets or r["dataset"] in only_datasets]


def _run(monkeypatch, argv, scorer=_scorer_without_ar_diacritized):
    monkeypatch.setattr(benchmark, "build_scoreboard", scorer)
    monkeypatch.setattr(sys, "argv", ["benchmark.py"] + argv)
    benchmark.main()


@pytest.mark.parametrize("flag", ["--scoreboard", "--ci-sample"])
def test_whole_board_run_fails_naming_the_unscored_row(
        board, monkeypatch, capsys, flag):
    results, committed = board
    before = results.read_text(encoding="utf-8")
    with pytest.raises(SystemExit) as exc:
        _run(monkeypatch, [flag])
    assert exc.value.code not in (0, None)
    assert "wikipron_ar_diacritized/ar" in str(exc.value.code)
    assert "wikipron/ar" not in str(exc.value.code).replace(
        "wikipron_ar_diacritized/ar", "")
    assert results.read_text(encoding="utf-8") == before


def test_scoped_run_warns_and_still_merges(board, monkeypatch, capsys):
    results, committed = board
    _run(monkeypatch, ["--scoreboard", "--lang", "ar",
                       "--dataset", "wikipron_ar_diacritized"],
         scorer=lambda *a, **k: [])
    err = capsys.readouterr().err
    assert "wikipron_ar_diacritized/ar" in err
    written = json.loads(results.read_text(encoding="utf-8"))
    assert sorted(written, key=lambda r: r["dataset"]) == sorted(
        committed, key=lambda r: r["dataset"])


def test_scoped_run_ignores_committed_rows_outside_its_scope(
        board, monkeypatch, capsys):
    _run(monkeypatch, ["--scoreboard", "--dataset", "wikipron"])
    assert "wikipron_ar_diacritized" not in capsys.readouterr().err


def test_retired_row_is_not_reported_as_unscored(board, monkeypatch):
    results, committed = board
    committed.append(_row("zz", "retired_dataset"))
    results.write_text(json.dumps(committed), encoding="utf-8")
    monkeypatch.setitem(benchmark.DATASETS, "wikipron_ar_diacritized",
                        (lambda lang, limit: [], ["ar"]))

    def scorer(limit, oracle=False, only_langs=None, only_datasets=None,
               **kwargs):
        return [_row("ar", "wikipron"), _row("ar", "wikipron_ar_diacritized")]

    _run(monkeypatch, ["--scoreboard"], scorer=scorer)
    written = json.loads(results.read_text(encoding="utf-8"))
    assert [(r["dataset"], r["lang"]) for r in written] == [
        ("wikipron", "ar"), ("wikipron_ar_diacritized", "ar")]


class _Dist:
    def __init__(self, name, version):
        self.metadata = {"Name": name}
        self.version = version


class _EntryPoint:
    def __init__(self, name, value, dist):
        self.name, self.value, self.dist = name, value, dist


def test_environment_records_plugin_and_scorer_versions(monkeypatch):
    eps = {"orthography2ipa.syllabify": [_EntryPoint(
        "silabificador", "orthography2ipa.syllabifiers:SilabificadorSyllabifier",
        _Dist("silabificador", "2.1.1a1"))]}
    monkeypatch.setattr(benchmark, "entry_points",
                        lambda group: eps.get(group, []))
    installed = {"text2tashkeel": "0.3.0a2"}

    def fake_version(name):
        if name in installed:
            return installed[name]
        raise benchmark.PackageNotFoundError(name)

    monkeypatch.setattr(benchmark, "package_version", fake_version)
    env = benchmark.board_environment()
    assert env["plugins"]["orthography2ipa.syllabify"] == {
        "silabificador": {
            "target": "orthography2ipa.syllabifiers:SilabificadorSyllabifier",
            "distribution": "silabificador", "version": "2.1.1a1"}}
    assert env["scorers"]["text2tashkeel"] == "0.3.0a2"
    assert env["scorers"]["rarfile"] is None
    assert set(env["plugins"]) == {
        f"orthography2ipa.{s}" for s in
        ("normalize", "syllabify", "stress", "rescore", "sandhi")}


def test_whole_board_run_writes_environment_beside_the_board(
        board, monkeypatch):
    results, committed = board
    monkeypatch.setattr(benchmark, "board_environment",
                        lambda: {"plugins": {}, "scorers": {"x": "1"}})
    _run(monkeypatch, ["--scoreboard"], scorer=lambda *a, **k: [
        _row("ar", "wikipron_ar_diacritized"), _row("ar", "wikipron")])
    written = json.loads(open(benchmark.ENVIRONMENT_JSON,
                              encoding="utf-8").read())
    assert written == {"plugins": {}, "scorers": {"x": "1"}}
    assert isinstance(json.loads(results.read_text(encoding="utf-8")), list)


def test_every_optional_import_in_the_harness_is_a_recorded_scorer():
    """A scorer package the harness imports but does not record would move
    rows with nothing on the board to explain it."""
    tree = ast.parse(open(benchmark.__file__, encoding="utf-8").read())
    local = {"orthography2ipa", "docs_nav", "check_board_not_reverting"}
    imported = set()
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for node in ast.walk(fn):
            if isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
            elif isinstance(node, ast.Import):
                imported.update(a.name.split(".")[0] for a in node.names)
    third_party = {m for m in imported
                   if m not in local and m not in sys.stdlib_module_names}
    assert third_party, "the scan found no function-level imports at all"
    assert third_party <= set(benchmark.OPTIONAL_SCORER_PACKAGES)


def test_ci_unreproducible_row_is_marked_in_row_and_scoreboard(
        tmp_path, monkeypatch):
    monkeypatch.setattr(benchmark, "SCOREBOARD_JSON",
                        str(tmp_path / "results.json"))
    monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(tmp_path / "s.md"))
    marked = _row("ar", "wikipron_ar_diacritized")
    marked["ci_reproducible"] = False
    benchmark.write_scoreboard([marked, _row("ar", "wikipron")])
    lines = [l for l in (tmp_path / "s.md").read_text(
        encoding="utf-8").splitlines() if l.startswith("| ar |")]
    flagged = [l for l in lines if "not CI-reproducible" in l]
    assert len(lines) == 2 and len(flagged) == 1
    assert "wikipron_ar_diacritized" in flagged[0]


def test_scorer_no_ci_job_installs_is_flagged_not_reproducible():
    assert benchmark.NOT_CI_REPRODUCIBLE == {
        "wikipron_ar_diacritized": "text2tashkeel"}
