"""Tests for the gold-corrections overlay mechanism.

An overlay repairs a mechanically-derivable defect in an upstream gold without
touching the upstream file, and is registered as its own dataset so the
uncorrected row stays on the board beside the corrected one.

Two properties are load-bearing and are asserted here rather than trusted:

* the corrections are derivable from the ORTHOGRAPHY — every row of the
  Vietnamese overlay is re-derived from the spelling's Unicode combining marks
  and must reproduce the committed file byte-for-byte;
* an overlay can never gate a promotion. A gold whose readings were rewritten
  by an automated process cannot certify the engine that is scored against it,
  and the tier the overlay is registered on has to say so.
"""
import ast
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import (  # noqa: E402
    DATASETS,
    GOLD_CORRECTIONS,
    PROVENANCE,
    apply_gold_corrections,
    can_gate_promotion,
    read_gold_corrections,
)
from build_gold_corrections import (  # noqa: E402
    TONE_LETTERS,
    VI_HUYEN_READING,
    VI_NGANG_READING,
    build_vi_tone_rows,
    vi_tone_from_spelling,
)

OVERLAY_FIELDS = {"dataset", "lang", "spelling", "original_reading",
                  "corrected_reading", "reason", "authority"}


def _overlays():
    return [(d, lang) for d, langs in GOLD_CORRECTIONS.items() for lang in langs]


@pytest.mark.parametrize("dataset,lang", _overlays())
def test_overlay_rows_are_complete_and_actually_change_something(dataset, lang):
    rows = read_gold_corrections(dataset, lang)
    assert rows
    for row in rows:
        assert set(row) == OVERLAY_FIELDS
        assert row["dataset"] == dataset and row["lang"] == lang
        assert row["original_reading"] != row["corrected_reading"]
        assert row["reason"].strip() and row["authority"].strip()


@pytest.mark.parametrize("dataset,lang", _overlays())
def test_overlay_is_registered_as_its_own_dataset(dataset, lang):
    """The corrected gold is a SEPARATE board row, never a rewrite of the
    original one: the difference between the two rows is the measurement of
    the upstream defect, and it is unreadable if only one number is published.
    """
    corrected = f"{dataset}_corrected"
    assert dataset in DATASETS
    assert corrected in DATASETS
    assert lang in DATASETS[corrected][1]


@pytest.mark.parametrize("dataset,lang", _overlays())
def test_no_overlay_can_gate_a_promotion(dataset, lang):
    """Whatever tier an overlay is registered on, it must be a non-gating one.

    A corrected gold is derived twice over — from a base gold and then from an
    automated correction pass — so it can diagnose, never certify.
    """
    tier = PROVENANCE[f"{dataset}_corrected"]
    assert can_gate_promotion(tier) is False
    # and never more trustworthy than the base it was built from
    assert tier == PROVENANCE[dataset]


def test_vi_tone_read_from_combining_marks_only():
    """The Vietnamese tone is read off the spelling. Vowel-quality diacritics
    (circumflex, breve, horn) are not tone marks and must not be mistaken for
    one, and a token carrying two tone marks is undeterminable, not a guess.
    """
    assert vi_tone_from_spelling("ma") == "ngang"
    assert vi_tone_from_spelling("mà") == "huyen"
    assert vi_tone_from_spelling("má") == "sac"
    assert vi_tone_from_spelling("mả") == "hoi"
    assert vi_tone_from_spelling("mã") == "nga"
    assert vi_tone_from_spelling("mạ") == "nang"
    # circumflex / breve / horn carry no tone
    assert vi_tone_from_spelling("tôi") == "ngang"
    assert vi_tone_from_spelling("ăn") == "ngang"
    assert vi_tone_from_spelling("từ") == "huyen"
    assert vi_tone_from_spelling("buồn") == "huyen"
    # two tone marks: two syllables in one token, no single tone to assign
    assert vi_tone_from_spelling("cà-phê") == "huyen"
    assert vi_tone_from_spelling("bàn là") is None


def test_vi_overlay_rederives_from_spelling_alone():
    """Re-derive every committed row from its own spelling and its own
    original reading, with no upstream file and no engine in the loop. The
    committed overlay must be exactly what the derivation produces.
    """
    committed = read_gold_corrections("vox_communis", "vi")
    rebuilt, stats = build_vi_tone_rows(
        [(r["spelling"], r["original_reading"]) for r in committed])
    assert stats["corrected"] == len(committed)
    assert rebuilt == sorted(
        committed, key=lambda r: (r["spelling"], r["original_reading"]))


def test_vi_overlay_only_touches_the_merged_tone_letter():
    for row in read_gold_corrections("vox_communis", "vi"):
        assert vi_tone_from_spelling(row["spelling"]) == "huyen"
        original, corrected = row["original_reading"], row["corrected_reading"]
        assert "".join(TONE_LETTERS.findall(original)) == VI_NGANG_READING
        assert "".join(TONE_LETTERS.findall(corrected)) == VI_HUYEN_READING
        # the segmental string is untouched
        assert (original.replace(VI_NGANG_READING, "")
                == corrected.replace(VI_HUYEN_READING, ""))


def test_uncorrectable_rows_are_left_alone():
    """Negative results are left in the gold, not guessed at: a grave-accented
    spelling whose reading is NOT the merged ˨˨, and a token whose tone cannot
    be read from the spelling, both stay uncorrected.
    """
    rows, stats = build_vi_tone_rows([
        ("mà", "maː˨˨"),           # correctable
        ("mà", "maː˨˩"),           # grave, but no merge to repair
        ("bàn là", "ɓaːn˨˨laː˨˨"),  # two tone marks, undeterminable
        ("ma", "maː˨˨"),           # ngang, not ours to touch
    ])
    assert [r["spelling"] for r in rows] == ["mà"]
    assert rows[0]["original_reading"] == "maː˨˨"
    assert stats == {"corrected": 1, "huyen_reading_not_ngang": 1,
                     "tone_undeterminable": 1, "not_huyen": 1}


def test_corrections_apply_only_on_an_exact_upstream_match():
    """A correction is keyed on the spelling AND the reading it was derived
    against. If upstream revises that reading, the correction must lapse
    rather than overwrite a row it was never inspected against.
    """
    row = read_gold_corrections("vox_communis", "vi")[0]
    pairs = [
        (row["spelling"], row["original_reading"]),
        (row["spelling"], row["original_reading"] + "ʔ"),  # upstream moved
        ("khong-in-the-overlay", "xoŋm˨˨"),
    ]
    out, applied, unmatched = apply_gold_corrections(pairs, "vox_communis", "vi")
    assert applied == 1
    assert out[0] == (row["spelling"], row["corrected_reading"])
    assert out[1:] == pairs[1:]
    assert unmatched == len(read_gold_corrections("vox_communis", "vi")) - 1


def test_overlay_never_imports_the_engine():
    """The derivation path must not be able to consult orthography2ipa. A gold
    repaired with this project's own answers would score beautifully and
    measure nothing.
    """
    path = os.path.join(os.path.dirname(__file__), "..", "scripts",
                        "build_gold_corrections.py")
    with open(path, encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.add(node.module or "")
    assert not [m for m in imported if m.split(".")[0] == "orthography2ipa"]


def test_upstream_gold_file_is_not_shipped_alongside_the_overlay():
    """The overlay repairs the upstream gold; it never replaces or vendors it.
    Nothing that looks like a copy of the cached upstream file may appear in
    the corrections directory.
    """
    directory = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa",
                             "data", "gold", "corrections")
    names = sorted(os.listdir(directory))
    assert names
    for name in names:
        assert name.endswith((".jsonl", ".md")), name
    for dataset, langs in GOLD_CORRECTIONS.items():
        for lang in langs:
            assert f"{dataset}_{lang}.jsonl" in names


def test_overlay_file_is_deterministic_jsonl():
    path = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa",
                        "data", "gold", "corrections", "vox_communis_vi.jsonl")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    keys = [(json.loads(ln)["spelling"], json.loads(ln)["original_reading"])
            for ln in lines]
    assert keys == sorted(keys)
    for line in lines:
        assert line == json.dumps(json.loads(line), ensure_ascii=False,
                                  sort_keys=True)
