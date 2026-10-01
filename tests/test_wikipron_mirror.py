"""Tests for the pinned WikiPron mirror in scripts/wikipron_mirror.py.

The mirror's job is to make the benchmark reproducible: one upstream
commit, every row kept, and a screen verdict for every language that
survives contact with the data.
"""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import wikipron_mirror as wm  # noqa: E402


def test_schema_is_three_explicit_columns():
    assert wm.HEADER.split("\t") == [
        "orthography", "restored_orthography", "ipa"]


def test_licence_is_the_wiktionary_one_not_the_scraper_one():
    """Apache 2.0 covers WikiPron's code; the text is Wiktionary's."""
    assert wm.LICENSE == "CC BY-SA 4.0"


def test_every_screen_verdict_is_one_of_the_declared_ones():
    for code, (verdict, _, _) in wm.SCREEN.items():
        assert verdict in wm.VERDICTS, code


def test_a_confirmed_policy_the_data_contradicts_is_downgraded(monkeypatch):
    """The downgrade must fire on a verdict that went in as confirmed.

    Latin is the case it exists for, but Latin is curated
    ``not_affected`` already, so screening Latin proves nothing about the
    rule. A language whose policy says macrons never reach titles, and
    whose words carry a macron on most rows, is what the rule has to
    catch — and the rate that overturned it has to be recorded.
    """
    monkeypatch.setitem(
        wm.SCREEN, "zzz",
        ("confirmed", "Entry names do not have macrons.", ["\u0304"]))
    words = ["A\u0304ballava\u0304", "Abessa\u0304lo\u0304n",
             "Abia\u0304", "Abae"]
    record = wm.screen_language("zzz", words, "https://example.invalid")
    assert record["verdict"] == "not_affected"
    assert record["marks_found_in_gold"] == 5
    assert record["marks_per_row"] > wm.STRAY_RATE


def test_the_same_policy_stands_when_its_data_agrees(monkeypatch):
    """Same curated entry, clean data: the verdict must survive.

    Without this the downgrade could be passing by rejecting everything.
    """
    monkeypatch.setitem(
        wm.SCREEN, "zzz",
        ("confirmed", "Entry names do not have macrons.", ["\u0304"]))
    record = wm.screen_language("zzz", ["Aballava", "Abae"],
                                "https://example.invalid")
    assert record["verdict"] == "confirmed"
    assert record["marks_found_in_gold"] == 0


def test_a_confirmed_policy_the_data_supports_stands():
    record = wm.screen_language("ang", ["habban", "an", "writan"],
                                "https://example.invalid")
    assert record["verdict"] == "confirmed"
    assert record["marks_found_in_gold"] == 0


def test_a_handful_of_strays_does_not_overturn_a_policy():
    """Old English carries four macrons in eighty-five thousand rows.

    A page moved by hand, or an entry created before the rule, is not
    evidence that the rule is not followed.
    """
    words = ["w\u014drd"] + ["word"] * 999
    assert wm.screen_language(
        "ang", words, "https://example.invalid")["verdict"] == "confirmed"


def test_a_language_with_no_policy_page_is_recorded_not_skipped():
    record = wm.screen_language("zzz", ["a", "b"], None)
    assert record["verdict"] == "no_policy_page"
    assert record["rows"] == 2


def test_a_policy_page_that_says_nothing_is_inconclusive_not_negative():
    record = wm.screen_language("zzz", ["a"], "https://example.invalid")
    assert record["verdict"] == "inconclusive"


def test_every_curated_verdict_carries_its_evidence():
    """A verdict with neither a quote nor a note cannot be checked."""
    for code, (verdict, quote, _) in wm.SCREEN.items():
        assert quote or wm.NOTES.get(code), code


def test_build_keeps_every_row_and_leaves_refusals_empty(tmp_path):
    src = tmp_path / "clone" / wm.TSV_PATH
    src.mkdir(parents=True)
    (src / "ewe_latn_broad.tsv").write_text(
        "Adam\ta d a m\naba\ta b a\n", encoding="utf-8")
    restored = tmp_path / "restored"
    restored.mkdir()
    (restored / "ewe.json").write_text(
        json.dumps({"Adam": "Ádàm"}), encoding="utf-8")
    out = tmp_path / "mirror"
    monkey = wm.pin
    wm.pin = lambda clone_dir, commit=None: {
        "repo": "CUNY-CL/wikipron", "path": wm.TSV_PATH,
        "commit": "0" * 40, "commit_date": "2026-01-01"}
    try:
        manifest = wm.build(str(tmp_path / "clone"), str(restored), str(out),
                            {})
    finally:
        wm.pin = monkey
    lines = (out / "data" / "ewe_latn_broad.tsv").read_text(
        encoding="utf-8").splitlines()
    assert lines == [wm.HEADER, "Adam\tÁdàm\ta d a m",
                     "aba\t\ta b a"]
    assert manifest["files"]["ewe_latn_broad.tsv"]["rows"] == 2
    assert manifest["files"]["ewe_latn_broad.tsv"]["restored"] == 1


def test_a_restoration_map_is_not_applied_across_languages(tmp_path):
    """``ade`` is an Ewe entry and a Yoruba one, and they differ.

    The maps are keyed by language, and the build must key its lookup the
    same way or one language's headword lands in the other's file.
    """
    src = tmp_path / "clone" / wm.TSV_PATH
    src.mkdir(parents=True)
    (src / "ewe_latn_broad.tsv").write_text("ade\ta d e\n", encoding="utf-8")
    (src / "yor_latn_broad.tsv").write_text("ade\ta d e\n", encoding="utf-8")
    restored = tmp_path / "restored"
    restored.mkdir()
    (restored / "ewe.json").write_text(json.dumps({"ade": "adè"}),
                                       encoding="utf-8")
    out = tmp_path / "mirror"
    monkey = wm.pin
    wm.pin = lambda clone_dir, commit=None: {
        "repo": "x", "path": wm.TSV_PATH, "commit": "0" * 40,
        "commit_date": "2026-01-01"}
    try:
        wm.build(str(tmp_path / "clone"), str(restored), str(out), {})
    finally:
        wm.pin = monkey
    assert (out / "data" / "yor_latn_broad.tsv").read_text(
        encoding="utf-8").splitlines()[1] == "ade\t\ta d e"


def test_diff_reports_a_changed_file(tmp_path, capsys):
    def manifest(sha, digest):
        return {"upstream": {"commit": sha, "commit_date": "2026-01-01"},
                "files": {"ewe_latn_broad.tsv":
                          {"rows": 2, "sha256_upstream": digest}}}

    old = tmp_path / "old.json"
    new = tmp_path / "new.json"
    old.write_text(json.dumps(manifest("a" * 40, "1" * 64)))
    new.write_text(json.dumps(manifest("b" * 40, "2" * 64)))
    wm.diff(str(old), str(new))
    assert "changed ewe_latn_broad.tsv" in capsys.readouterr().out


def _fake_pin(monkeypatch):
    monkeypatch.setattr(wm, "pin", lambda clone_dir, commit=None: {
        "repo": "CUNY-CL/wikipron", "path": wm.TSV_PATH,
        "commit": "0" * 40, "commit_date": "2026-01-01"})


def _scrape(tmp_path, name, text, maps=None):
    src = tmp_path / "clone" / wm.TSV_PATH
    src.mkdir(parents=True, exist_ok=True)
    (src / name).write_text(text, encoding="utf-8")
    restored = tmp_path / "restored"
    restored.mkdir(exist_ok=True)
    for code, mapping in (maps or {}).items():
        (restored / f"{code}.json").write_text(json.dumps(mapping),
                                               encoding="utf-8")
    return str(tmp_path / "clone"), str(restored), str(tmp_path / "mirror")


def test_a_language_nobody_ran_is_marked_not_attempted(tmp_path, monkeypatch):
    """Zero restored rows is ambiguous unless the manifest says why.

    ``ang`` and ``grc`` are screened, confirmed and unrestored because
    nobody has run them. That has to be distinguishable from a run that
    recovered nothing, which would be a defect.
    """
    _fake_pin(monkeypatch)
    args = _scrape(tmp_path, "ang_latn_broad.tsv", "habban\th a b a n\n")
    manifest = wm.build(*args, {})
    record = manifest["screen"]["ang"]
    assert record["restoration_attempted"] is False
    assert record["restored_rows"] == 0


def test_a_language_that_ran_is_marked_attempted(tmp_path, monkeypatch):
    _fake_pin(monkeypatch)
    args = _scrape(tmp_path, "ewe_latn_broad.tsv", "Adam\ta d a m\n",
                   {"ewe": {"Adam": "Ádàm"}})
    manifest = wm.build(*args, {})
    record = manifest["screen"]["ewe"]
    assert record["restoration_attempted"] is True
    assert record["restored_rows"] == 1


def test_a_run_that_recovered_nothing_refuses_to_publish(tmp_path,
                                                         monkeypatch):
    """The Tundra Nenets failure, as a gate instead of a printed count.

    Reading ``yrk`` where Wiktionary tags headwords ``yrk-tun`` rendered
    every page, matched none, and reported a clean run. Found nothing is
    never success.
    """
    _fake_pin(monkeypatch)
    args = _scrape(tmp_path, "yrk_cyrl_narrow.tsv", "вада\tv a d a\n",
                   {"yrk": {}})
    with pytest.raises(SystemExit) as excinfo:
        wm.build(*args, {})
    assert "yrk" in str(excinfo.value)


def test_the_card_says_not_attempted_rather_than_zero(tmp_path, monkeypatch):
    _fake_pin(monkeypatch)
    args = _scrape(tmp_path, "ang_latn_broad.tsv", "habban\th a b a n\n")
    wm.build(*args, {})
    card = (tmp_path / "mirror" / "README.md").read_text(encoding="utf-8")
    row = [line for line in card.splitlines() if line.startswith("| `ang`")]
    assert row and "not attempted" in row[0]
