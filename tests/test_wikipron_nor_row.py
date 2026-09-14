"""Tests for the ``wikipron_nor`` row wiring in scripts/benchmark.py.

WikiPron files a pronunciation by the code inside the Wiktionary
``{{IPA|…}}`` template, so Nynorsk entries tagged with the Norwegian
macrolanguage code land in ``nor_latn_broad.tsv``. That file is scored
against ``nn`` under its own dataset id, and must NOT be reachable
through the plain ``wikipron`` dataset under any code.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


def test_macro_file_is_registered_against_nynorsk():
    loader, langs = benchmark.DATASETS["wikipron_nor"]
    assert loader is benchmark.load_wikipron_nor
    assert langs == ["nn"]
    assert benchmark._WIKIPRON_FILES_MACRO["nn"] == "nor_latn_broad.tsv"


def test_macro_file_is_not_scored_as_a_plain_wikipron_row():
    # The row used to sit under the macrolanguage code "no", whose spec
    # models Bokmal. Nothing may reintroduce it there.
    assert "no" not in benchmark._WIKIPRON_FILES
    assert "nor_latn_broad.tsv" not in benchmark._WIKIPRON_FILES.values()


def test_provenance_is_declared():
    assert benchmark.PROVENANCE["wikipron_nor"] == "crowd-scraped"


def test_loader_parses_pairs_and_honours_limit(monkeypatch):
    monkeypatch.setattr(
        benchmark, "_fetch",
        lambda url, name: "namn\tn ɑ m n\ntydeleg\t² t yː d l ɛ\nfrå\tf r oː\n")
    assert benchmark.load_wikipron_nor("nn", sys.maxsize) == [
        ("namn", "n ɑ m n"), ("tydeleg", "² t yː d l ɛ"), ("frå", "f r oː")]
    assert benchmark.load_wikipron_nor("nn", 2) == [
        ("namn", "n ɑ m n"), ("tydeleg", "² t yː d l ɛ")]


def test_scoring_spec_strips_the_pitch_accent_digits():
    # The gold marks accent 2 with U+00B2 on roughly half its rows. Those
    # digits are word prosody, not segments, and the harness only unscores
    # them for a spec that declares a pitch accent. The Bokmal-flavoured
    # macrolanguage spec declares none, so scoring this gold there charged
    # every accent mark as an error.
    assert benchmark._prosody_marks("nn") == "¹²"
    assert benchmark._prosody_marks("no") == ""
