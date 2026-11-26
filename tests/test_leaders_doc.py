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
        if row["lang"] == "nl-NL" and row["dataset"] == "wikipron":
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


def _rows(page):
    return {line.split("|")[1].strip().strip("`"): [c.strip() for c in line.split("|")[1:-1]]
            for line in page.splitlines() if line.startswith("| `")}


def test_trusted_tier_beats_a_larger_n():
    rows = [
        {"dataset": "big", "n": 900, "provenance": "machine-generated"},
        {"dataset": "wiki", "n": 50, "provenance": "crowd-scraped"},
        {"dataset": "lex", "n": 10, "provenance": "lexicon-derived"},
        {"dataset": "lex2", "n": 20, "provenance": "lexicon-derived"},
    ]
    assert leaders.best_row(rows)["dataset"] == "lex2"
    assert leaders.best_row([]) is None


def test_small_expert_row_loses_to_a_large_lexicon_row():
    rows = [
        {"dataset": "ep_dialects", "n": 30, "provenance": "expert-human"},
        {"dataset": "portuguese_unified", "n": 105553, "provenance": "lexicon-derived"},
    ]
    assert leaders.best_row(rows)["dataset"] == "portuguese_unified"
    assert leaders.best_row(rows[:1])["dataset"] == "ep_dialects"


def test_gating_rows_pick_the_trusted_tier():
    rows = _rows(leaders.render())
    assert rows["nl-NL"][3:5] == ["`wikipron`", "45872"]
    assert rows["nl-NL"][7] == "crowd-scraped"
    assert rows["pt-BR"][3] == "`portuguese_unified`"
    assert rows["pt-PT"][3] == "`portuguese_unified`"


def test_non_gating_row_is_marked():
    rows = _rows(leaders.render())
    assert rows["kab"][3] == "`vox_communis`"
    assert rows["kab"][7] == "epitran-derived (does not gate)"


def test_mwr_is_unsupported():
    row = _rows(leaders.render())["mwr"]
    assert row[1] == ("unsupported: resolves to the `dhd` stub "
                      "(a member of the mwr macrolanguage), no phonology")
    assert row[3] == "not measured"
