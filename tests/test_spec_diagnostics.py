"""Unit coverage for the mechanical signals in ``scripts/spec_diagnostics.py``.

These are synthetic, engine-level checks: they exercise the three functions a
flagged board row is actually ranked by (gold-coverage scanning, table
twinning, cross-family inheritance) without depending on any real spec or
cached gold dataset.
"""
from __future__ import annotations

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from orthography2ipa.types import LanguageSpec  # noqa: E402
import spec_diagnostics as sd  # noqa: E402


def _spec(**kwargs) -> LanguageSpec:
    base = dict(code="xx", name="Test", family="Test", script="Latin",
                graphemes={"a": ["a"]}, allophones={})
    base.update(kwargs)
    return LanguageSpec(**base)


# --------------------------------------------------------------------------
# _scan_gold
# --------------------------------------------------------------------------

def test_scan_gold_reports_tokenizer_unknown_not_grapheme_keys():
    """A grapheme covered only through a multigraph must NOT be flagged.

    ``ch`` maps to a single phoneme, so a gold word made only of ``ch`` and
    ``a`` is fully consumed even though the grapheme table has no bare-``c``
    or bare-``h`` entry — guessing "unmapped" from the key alphabet alone
    would flag ``c`` and ``h`` here, which is exactly the false positive the
    diagnostic is built to avoid (its stated Vietnamese/Tamil validation).
    """
    spec = _spec(graphemes={"ch": ["tʃ"], "a": ["a"]})
    gold, unmapped, hits, scanned = sd._scan_gold(spec, [("cha", "tʃa")], sample=10)
    assert unmapped == []
    assert hits == 0
    assert scanned == 1
    assert gold == {"c", "h", "a"}


def test_scan_gold_flags_a_character_with_no_reading_at_any_length():
    """A character absent from the grapheme table at every length is UNKNOWN
    to the tokenizer and must show up in both the unmapped set and the
    per-word hit count."""
    spec = _spec(graphemes={"a": ["a"]})
    gold, unmapped, hits, scanned = sd._scan_gold(spec, [("az", "az")], sample=10)
    assert unmapped == ["z"]
    assert hits == 1
    assert scanned == 1


def test_scan_gold_respects_the_sample_limit():
    spec = _spec(graphemes={"a": ["a"]})
    pairs = [("az", "az")] * 5
    _, _, _, scanned = sd._scan_gold(spec, pairs, sample=2)
    assert scanned == 2


def test_scan_gold_apostrophe_is_not_treated_as_punctuation():
    """Regression for the pharyngealisation blind spot: an apostrophe-class
    character with no grapheme entry must be counted as gold and, if the
    tokenizer cannot consume it, reported as unmapped rather than silently
    stripped as punctuation."""
    spec = _spec(graphemes={"a": ["a"]})
    gold, unmapped, hits, scanned = sd._scan_gold(spec, [("a’", "aˤ")], sample=10)
    assert "’" in gold
    assert "’" in unmapped


# --------------------------------------------------------------------------
# _twin
# --------------------------------------------------------------------------

def test_twin_finds_the_closest_undeclared_match():
    raw = {
        "aa": {"code": "aa", "script": "Latin"},
        "bb": {"code": "bb", "script": "Latin"},
        "cc": {"code": "cc", "script": "Latin"},
    }
    # "aa" and "bb" share every key; "cc" shares none.
    table = {"p": ["p"], "t": ["t"], "k": ["k"], "m": ["m"],
             "n": ["n"], "s": ["s"], "l": ["l"], "r": ["r"]}
    sigs = {
        "aa": sd._signature(table),
        "bb": sd._signature(table),
        "cc": sd._signature({"x": ["x"]}),
    }
    twin = sd._twin("aa", raw, "graphemes", sigs)
    assert twin is not None
    assert twin[0] == "bb"
    assert twin[1] == 1.0


def test_twin_excludes_a_declared_base():
    """A table that matches its OWN declared base is descent, not a borrowed
    table asserted from an unrelated language, and must not be reported."""
    raw = {
        "aa": {"code": "aa", "script": "Latin", "graphemes_base": "bb"},
        "bb": {"code": "bb", "script": "Latin"},
    }
    table = {k: [k] for k in "ptkmnslr"}
    sigs = {"aa": sd._signature(table), "bb": sd._signature(table)}
    assert sd._twin("aa", raw, "graphemes", sigs) is None


def test_twin_excludes_dialect_siblings_by_primary_subtag():
    raw = {
        "pt-BR-x-sp": {"code": "pt-BR-x-sp", "script": "Latin"},
        "pt-BR-x-rj": {"code": "pt-BR-x-rj", "script": "Latin"},
    }
    table = {k: [k] for k in "ptkmnslr"}
    sigs = {"pt-BR-x-sp": sd._signature(table), "pt-BR-x-rj": sd._signature(table)}
    assert sd._twin("pt-BR-x-sp", raw, "graphemes", sigs) is None


def test_twin_none_when_table_too_small():
    raw = {"aa": {"code": "aa", "script": "Latin"},
           "bb": {"code": "bb", "script": "Latin"}}
    table = {"p": ["p"], "t": ["t"]}  # below the len(mine) < 8 floor
    sigs = {"aa": sd._signature(table), "bb": sd._signature(table)}
    assert sd._twin("aa", raw, "graphemes", sigs) is None


# --------------------------------------------------------------------------
# _chain / cross-family inheritance
# --------------------------------------------------------------------------

def test_chain_flags_a_base_from_a_different_root_family(monkeypatch):
    raw = {
        "aa": {"code": "aa", "parent": "bb"},
        "bb": {"code": "bb", "family": "Sino-Tibetan"},
    }
    monkeypatch.setattr(sd, "_family_cached", lambda code: None)
    monkeypatch.setattr(sd, "_family_path", lambda code:
                         ("Indo-European",) if code == "aa" else ("Sino-Tibetan",))
    links = sd._chain("aa", raw)
    assert len(links) == 1
    assert links[0]["field"] == "parent"
    assert links[0]["target"] == "bb"
    assert links[0]["cross_family"] is True


def test_chain_does_not_flag_a_base_within_the_same_root_family(monkeypatch):
    raw = {
        "aa": {"code": "aa", "parent": "bb"},
        "bb": {"code": "bb", "family": "Indo-European > Germanic"},
    }
    monkeypatch.setattr(sd, "_family_cached", lambda code: None)
    monkeypatch.setattr(sd, "_family_path", lambda code:
                         ("Indo-European",) if code == "aa" else
                         ("Indo-European", "Germanic"))
    links = sd._chain("aa", raw)
    assert len(links) == 1
    assert links[0]["cross_family"] is False


def test_chain_empty_when_spec_declares_no_base_field():
    raw = {"aa": {"code": "aa"}}
    assert sd._chain("aa", raw) == []
