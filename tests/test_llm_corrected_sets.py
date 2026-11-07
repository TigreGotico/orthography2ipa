"""Format and validation checks for the llm-corrected silver sets.

``scripts/correct_silver_ipa.py`` writes one
``orthography2ipa/data/gold/<set>.llm-corrected.jsonl`` per LLM-generated set
(docs/contributing/silver_correction.md). The rows are silver, tier
``llm-corrected``, and gate nothing. These tests check the shape of each row,
that each file holds exactly the rows of its source set, and that each label
has one IPA word for each word of the engine split it was written against.
They do not compare a row with the engine: a silver label is not engine
output, and nothing here pins one.
"""
import csv
import json
import os
import sys
from collections import Counter
from pathlib import Path

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402
import correct_silver_ipa as csi  # noqa: E402

GOLD = Path(__file__).resolve().parent.parent / "orthography2ipa" / "data" / "gold"
FIELDS = {"dataset", "lect", "id", "sentence", "ipa", "ipa_llm_original",
          "ipa_engine", "model", "passes", "flag", "reason", "note_conflict",
          "word_count", "tier", "source_row"}
FLAGS = {"agreed", "adjudicated", "uncertain"}
C_FIELDS = {"ipa", "flag", "reason", "note_conflict"}
LOCAL = ("arabic_tts", "iberian_creole_tts", "kabyle_tts", "portuguese_tts",
         "spain_romance_tts")
REMOTE = ("barranquenho_dict", "gold20_arabic", "mirandese_dict")


def _rows(dataset):
    path = GOLD / f"{dataset}.llm-corrected.jsonl"
    return [json.loads(line) for line in path.read_text("utf-8").splitlines()]


def _source(dataset):
    """``(lect, id, sentence)`` of every row the correction tool reads, from
    the source files themselves for the local sets."""
    if dataset in LOCAL:
        rows = []
        for path in sorted((GOLD / dataset).glob("*.tsv")):
            with open(path, encoding="utf-8") as fh:
                for record in csv.DictReader(fh, delimiter="\t"):
                    sentence = (record.get("sentence") or "").strip()
                    if sentence and (record.get("ipa") or "").strip():
                        rows.append((path.stem, record["id"], sentence))
        return rows
    loader = csi.REMOTE_LOADERS[dataset]
    return [(lect, f"{lect}-{n:04d}", text)
            for lect in benchmark.DATASETS[dataset][1]
            for n, (text, _) in enumerate(loader(lect, sys.maxsize), 1)]


def test_the_tool_and_these_tests_cover_the_same_sets():
    assert set(csi.SILVER_SETS) == set(LOCAL) | set(REMOTE)
    assert set(benchmark.LLM_CORRECTED_DATASETS) <= set(csi.SILVER_SETS)


@pytest.mark.parametrize("dataset", LOCAL + REMOTE)
def test_rows_have_the_documented_shape(dataset):
    for row in _rows(dataset):
        assert set(row) == FIELDS, row["id"]
        assert row["dataset"] == dataset
        assert row["tier"] == "llm-corrected"
        assert row["flag"] in FLAGS
        for name in ("ipa", "ipa_engine", "sentence", "reason"):
            assert isinstance(row[name], str) and row[name].strip(), (
                row["id"], name)
        assert isinstance(row["note_conflict"], str)
        assert isinstance(row["source_row"], dict)
        passes = row["passes"]
        assert set(passes) == {"A", "B", "C"}
        assert isinstance(passes["A"], str) and passes["A"].strip()
        assert isinstance(passes["B"], str) and passes["B"].strip()
        if passes["C"] is None:
            # No adjudication: the label is pass A, in canonical form.
            assert row["flag"] == "agreed"
            assert row["ipa"] == csi.canonical_ipa(passes["A"])
            assert row["note_conflict"] == ""
        else:
            assert set(passes["C"]) == C_FIELDS
            assert row["flag"] == passes["C"]["flag"]
            assert row["ipa"] == csi.canonical_ipa(passes["C"]["ipa"])
            assert row["note_conflict"] == passes["C"]["note_conflict"]


@pytest.mark.parametrize("dataset", LOCAL + REMOTE)
def test_ipa_writes_the_ipa_letter_for_the_velar_stop(dataset):
    for row in _rows(dataset):
        assert "g" not in row["ipa"], row["id"]


@pytest.mark.parametrize("dataset", LOCAL + REMOTE)
def test_rows_are_the_rows_of_the_source_set(dataset):
    rows = _rows(dataset)
    got = [(r["lect"], r["id"], r["sentence"]) for r in rows]
    source = _source(dataset)
    assert len(got) == len(source)
    assert Counter(got) == Counter(source)
    assert len(set((r["lect"], r["id"]) for r in rows)) == len(rows)
    assert [(r["lect"], r["id"]) for r in rows] == sorted(
        (r["lect"], r["id"]) for r in rows)


@pytest.mark.parametrize("dataset", LOCAL + REMOTE)
def test_each_label_has_one_word_per_engine_word(dataset):
    for row in _rows(dataset):
        count = row["word_count"]
        assert count == {"ipa": len(row["ipa"].split()),
                         "engine": len(row["ipa_engine"].split()),
                         "ok": True}, row["id"]


@pytest.mark.parametrize("dataset", benchmark.LLM_CORRECTED_DATASETS)
def test_the_board_scores_the_llm_corrected_file_as_silver(dataset):
    assert benchmark.PROVENANCE[dataset] == "llm-corrected"
    assert not benchmark.can_gate_promotion("llm-corrected")
    loader, langs = benchmark.DATASETS[dataset]
    rows = _rows(dataset)
    assert {r["lect"] for r in rows} == set(langs)
    for lang in langs:
        assert loader(lang, sys.maxsize) == [
            (r["sentence"], r["ipa"]) for r in rows if r["lect"] == lang]
