"""Tests for the ``wikipron_restored`` row wiring in scripts/benchmark.py.

The row republishes an affected WikiPron gold with the Wiktionary
DISPLAY headword in the input column instead of the page title. It is a
second row beside the original, never a replacement: the point is the
comparison between the two.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


def test_registered_for_the_affected_languages():
    loader, langs = benchmark.DATASETS["wikipron_restored"]
    assert loader is benchmark.load_wikipron_restored
    assert langs == ["ee", "gmh", "he", "yo"]


def test_the_original_rows_are_still_registered():
    # comparability with the untouched gold is the whole point
    for lang in ("ee", "gmh", "he", "yo"):
        assert lang in benchmark._WIKIPRON_FILES
        assert lang in benchmark.DATASETS["wikipron"][1]


def test_middle_high_german_is_not_repointed_at_the_title_form_spec():
    """``gmh-x-wikt`` models the TITLE spelling, which this row replaces.

    Scoring the restored display form against the title-form spec would
    measure a spelling convention neither side uses.
    """
    assert "gmh-x-wikt" not in benchmark.DATASETS["wikipron_restored"][1]
    assert "gmh" in benchmark.DATASETS["wikipron_restored"][1]


def test_provenance_is_declared():
    assert benchmark.PROVENANCE["wikipron_restored"] == "crowd-scraped"


def test_loader_parses_pairs_and_honours_limit(monkeypatch):
    monkeypatch.setattr(
        benchmark, "_fetch",
        lambda url, name: "Ádàm\ta d a m\nhëlfen\th ɛ l f ə n\n")
    assert benchmark.load_wikipron_restored("ee", sys.maxsize) == [
        ("Ádàm", "a d a m"), ("hëlfen", "h ɛ l f ə n")]
    assert benchmark.load_wikipron_restored("ee", 1) == [("Ádàm", "a d a m")]


def test_header_row_is_not_scored_as_a_word(monkeypatch):
    """The published files carry a header so the HF viewer renders them."""
    monkeypatch.setattr(
        benchmark, "_fetch",
        lambda url, name: "orthography\tipa\nÁdàm\ta d a m\n")
    assert benchmark.load_wikipron_restored("ee", sys.maxsize) == [
        ("Ádàm", "a d a m")]


def test_unregistered_language_returns_empty_not_an_error(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: "x\tx\n")
    assert benchmark.load_wikipron_restored("pt-PT", 10) == []


def test_each_language_reads_its_own_file(monkeypatch):
    seen = []

    def fake_fetch(url, name):
        seen.append((url, name))
        return ""

    monkeypatch.setattr(benchmark, "_fetch", fake_fetch)
    for lang in ("ee", "gmh", "he", "yo"):
        benchmark.load_wikipron_restored(lang, 10)
    assert [n for _, n in seen] == [
        "wikipron_restored_ee.tsv", "wikipron_restored_gmh.tsv",
        "wikipron_restored_he.tsv", "wikipron_restored_yo.tsv"]
    assert all(u.endswith(f"/{lang}.tsv")
               for (u, _), lang in zip(seen, ("ee", "gmh", "he", "yo")))
