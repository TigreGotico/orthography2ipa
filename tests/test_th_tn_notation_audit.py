"""th and tn notation folds are audit entries, not valid_ceiling.

A valid_ceiling is only for a contrast the orthography does not write.
Thai spells tone, and the tn vox_communis gap is the gold's symbol
set, so each fold is recorded as an audit entry and the board carries no
ceiling for these rows.
"""
import json
import os
import sys

import pytest

from orthography2ipa import json_loader

ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "scripts"))

ROWS = [
    ("th", "wikipron", "0.1710"),
    ("th", "vox_communis", "0.2294"),
    ("tn", "vox_communis", "0.2066"),
]


@pytest.mark.parametrize("lang,dataset,folded", ROWS)
def test_fold_is_an_audit_not_a_ceiling(lang, dataset, folded):
    spec = json_loader.load_json_spec(lang)
    assert dataset not in (spec.valid_ceiling or {})
    assert spec.audit[dataset].conclusion == "at_ceiling_documented"
    assert folded in spec.audit[dataset].measured


@pytest.mark.parametrize("board", ["results.json", "results_ci_sample.json"])
def test_board_rows_carry_no_ceiling(board):
    with open(os.path.join(ROOT, "benchmarks", board), encoding="utf-8") as fh:
        rows = json.load(fh)
    keys = {(lang, dataset) for lang, dataset, _ in ROWS}
    hits = [r for r in rows if (r["lang"], r["dataset"]) in keys]
    assert hits
    assert not [r for r in hits if "valid_ceiling" in r]


def test_tone_to_end_moves_placement_and_keeps_tone_order():
    fold = pytest.importorskip("fold_th_notation")
    # Nucleus placement (vox_communis) and syllable-final placement
    # (wikipron) of the same two tones fold to one string.
    nucleus = "ka˧n.di˥ŋ"
    final = "kan˧.diŋ˥"
    assert fold.tone_to_end(nucleus) == fold.tone_to_end(final) == "kan.diŋ˧˥"
    assert fold.tone_to_end("ka˥n.di˧ŋ") != fold.tone_to_end(nucleus)
