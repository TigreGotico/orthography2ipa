"""``docs/languages/leaders.md`` matches what ``scripts/gen_leaders_doc.py``
builds from the board and the spec files."""
import importlib.util
import json
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load():
    path = os.path.join(_ROOT, "scripts", "gen_leaders_doc.py")
    spec = importlib.util.spec_from_file_location("gen_leaders_doc", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


leaders = _load()


def _committed():
    with open(leaders.PATH, encoding="utf-8") as f:
        return f.read()


def test_committed_page_is_current():
    assert _committed() == leaders.render()


def test_one_changed_cell_is_stale(monkeypatch, tmp_path):
    with open(leaders.RESULTS, encoding="utf-8") as f:
        rows = json.load(f)
    for row in rows:
        if row["lang"] == "pt-PT" and row["dataset"] == "portuguese_unified":
            row["per"] += 0.01
    bumped = tmp_path / "results.json"
    bumped.write_text(json.dumps(rows), encoding="utf-8")
    monkeypatch.setattr(leaders, "RESULTS", str(bumped))
    assert _committed() != leaders.render()


def test_rows_follow_the_leader_order():
    tags = [line.split("|")[1].strip().strip("`")
            for line in leaders.render().splitlines()
            if line.startswith("| `")]
    assert tags == ["pt-PT", "pt-BR", "es-CO", "fr-FR", "it-IT", "de-DE",
                    "nl-NL", "da-DK", "kab", "hi-IN", "bn-IN", "mwr"]


def test_best_gold_row_is_the_largest_gating_row():
    rows = [
        {"dataset": "a", "n": 10, "gating": True},
        {"dataset": "b", "n": 900, "gating": False},
        {"dataset": "c", "n": 50, "gating": True},
    ]
    assert leaders.best_gold_row(rows)["dataset"] == "c"
    assert leaders.best_gold_row([rows[1]]) is None
