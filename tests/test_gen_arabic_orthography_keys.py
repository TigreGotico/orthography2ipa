"""Tests for scripts/gen_arabic_orthography_keys.py.

The script's docstring promises "Idempotent: re-running produces the same
specs". It stopped being true, in the worst possible way: it assigned
``spec["allophone_rules"] = ALLOPHONE_RULES`` wholesale, and twelve
``AR_EMPHASIS_SPREAD_*`` rules had been added to ``arb.json`` after that
constant was last touched. A plain run deleted all twelve, with their Watson
2002 and Davis 1995 citations, and said nothing. Nobody re-reads a 3000-line
data file after running a generator, so the loss was invisible and the
citations are the part that cannot be reconstructed from the code.

These tests hold the promise to the wall:

* the generator writes every spec byte-identical on a clean tree;
* it preserves a rule it does not own, and still updates the ones it does;
* a lect with no ``graphemes_base`` gets the whole derived key set, from its
  own letter values, not a difference from an ancestor it does not inherit
  from.
"""
import json
import os
import shutil
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import gen_arabic_orthography_keys as gen  # noqa: E402


@pytest.fixture
def data_copy(tmp_path, monkeypatch):
    """Point the generator's output directory at a copy of the real data.

    Reads still resolve through the installed package, which is what the
    generator uses to compute effective letter values; only the writes are
    redirected, so the test can diff what it wrote against what is committed
    without ever touching the working tree.
    """
    dest = tmp_path / "data"
    shutil.copytree(gen.DATA, dest)
    monkeypatch.setattr(gen, "DATA", dest)
    return dest


def _load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class TestIdempotent:
    def test_a_plain_run_changes_no_spec(self, data_copy, capsys):
        """The headline promise: run it on a clean tree, get an empty diff."""
        gen.main()
        capsys.readouterr()

        drifted = []
        for code in gen.LECTS:
            written = data_copy / f"{code}.json"
            committed = (gen.REPO_ROOT / "orthography2ipa" / "data"
                         / f"{code}.json")
            if _load(written) != _load(committed):
                drifted.append(code)
        assert drifted == [], (
            "the generator rewrote these specs on a clean tree: "
            + ", ".join(drifted)
            + ". Either a constant in the script has fallen behind the "
              "committed spec, or the script is overwriting a field it does "
              "not own."
        )

    def test_two_runs_agree(self, data_copy, capsys):
        gen.main()
        first = {c: _load(data_copy / f"{c}.json") for c in gen.LECTS}
        gen.main()
        capsys.readouterr()
        second = {c: _load(data_copy / f"{c}.json") for c in gen.LECTS}
        assert first == second


class TestOwnedRulesMergeNotReplace:
    """The regression that lost arb's emphasis spread."""

    def test_a_rule_the_script_does_not_own_survives(self):
        kept = {"id": "HAND_WRITTEN", "phonemes": ["a"], "surface": "ɑ",
                "notes": "added to the spec by hand, with a citation"}
        owned = [{"id": "AR_WASL_EPENTHESIS", "phonemes": ["ʔ"],
                  "surface": "ʔi"}]
        out = gen.merge_rules_by_id([owned[0], kept], owned)
        assert kept in out

    def test_an_owned_rule_is_updated_in_place(self):
        stale = {"id": "AR_WASL_EPENTHESIS", "surface": "OLD"}
        other = {"id": "HAND_WRITTEN", "surface": "ɑ"}
        fresh = {"id": "AR_WASL_EPENTHESIS", "surface": "NEW"}
        out = gen.merge_rules_by_id([stale, other], [fresh])
        assert out == [fresh, other], "order must not move either"

    def test_an_owned_rule_the_spec_lacks_is_appended(self):
        other = {"id": "HAND_WRITTEN", "surface": "ɑ"}
        fresh = {"id": "AR_WASL_EPENTHESIS", "surface": "NEW"}
        assert gen.merge_rules_by_id([other], [fresh]) == [other, fresh]

    def test_an_empty_spec_field_takes_the_owned_rules(self):
        fresh = {"id": "AR_WASL_EPENTHESIS", "surface": "NEW"}
        assert gen.merge_rules_by_id(None, [fresh]) == [fresh]

    def test_arb_keeps_its_emphasis_spread_rules(self, data_copy, capsys):
        """The exact rules the old code deleted."""
        gen.main()
        capsys.readouterr()
        ids = [r.get("id")
               for r in _load(data_copy / "arb.json")["allophone_rules"]]
        emphasis = [i for i in ids if i.startswith("AR_EMPHASIS_SPREAD_")]
        assert len(emphasis) == 12, ids
        assert "AR_WASL_EPENTHESIS" in ids


class TestLectWithNoGraphemesBase:
    """``ayl`` is such a spec: it declares its own orthography and inherits no
    keys, so "the difference from my ancestor" is the wrong question to ask."""

    def test_base_keys_carry_the_whole_derived_set(self):
        import orthography2ipa

        letters = {s: list(orthography2ipa.get("ayl").graphemes[s])
                   for s in gen.SUN if s in orthography2ipa.get("ayl").graphemes}
        keys = gen.base_keys(letters)
        for k in gen.ARB_ADDITIONS:
            assert k in keys
        for k in gen.ARB_FIXES:
            assert k in keys
        assert "اَلضض" in keys, "the assimilated-article keys must be there"

    def test_what_base_keys_does_not_cover_is_stated(self):
        """The derived set is not the whole vocalised set, and the docstring
        says so. This pins the gap so it cannot widen unnoticed."""
        import unicodedata

        import orthography2ipa

        g = orthography2ipa.get("ayl").graphemes
        letters = {s: list(g[s]) for s in gen.SUN if s in g}
        produced = set(gen.base_keys(letters))
        arb = orthography2ipa.get("arb").graphemes
        haraka = {k for k in arb
                  if any(unicodedata.category(c) == "Mn" for c in k)}
        missing = haraka - produced
        assert len(haraka) == 182 and len(missing) == 16, (
            len(haraka), sorted(missing))
        # the primitive vowel-sign layer: bare marks and the matres digraphs
        assert missing == {"َ", "ُ", "ِ", "ً", "ٌ", "ٍ", "ّ", "ْ",
                           "ُو", "ِي", "َا", "َى", "َو", "َي", "ْو", "ْي"}

    def test_sun_keys_use_the_lects_own_letter_values(self):
        """A lect that reads ض as [dˤ] must not get Classical [ɮˤ]."""
        keys = gen.base_keys({"ض": ["dˤ"]})
        assert keys["اَلضض"] == ["adˤdˤ"]
        assert not any("ɮ" in v for vs in keys.values() for v in vs)

    def test_every_current_lect_still_declares_a_base(self):
        """Guards the branch above: while this holds, no committed spec takes
        it, so the fix cannot move any existing data file."""
        without = [c for c in gen.LECTS
                   if c != "arb"
                   and not _load(gen.DATA / f"{c}.json").get("graphemes_base")]
        assert without == [], without
