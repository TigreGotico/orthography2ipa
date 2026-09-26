"""Tests for scripts/gold_composition.py's trivial/real classification.

The substance of the script is deciding which gold entries are alphabet-
chart noise rather than running text (see docs/gold_composition.md). These
tests exercise that decision directly, against a stub spec, so they do
not depend on any particular registered language's current grapheme
table or gold set.
"""
import os
import sys
from types import SimpleNamespace
from unittest import mock

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import gold_composition as gc  # noqa: E402


def _spec(graphemes):
    return SimpleNamespace(graphemes=graphemes)


class TestBaseForm:
    def test_casefolds(self):
        assert gc._base_form("A") == "a"

    def test_strips_combining_marks(self):
        # "A" + combining macron below (U+0331), as in the Kwak'wala
        # wikipron alphabet-chart rows.
        assert gc._base_form("A̱") == "a"

    def test_leaves_base_letters_of_multi_char_words_untouched(self):
        assert gc._base_form("Bonjour") == "bonjour"


class TestClassifyGoldAlphabetChart:
    """A gold set dominated by single/double-letter entries that cover
    most of the spec's declared alphabet is an alphabet chart: those
    entries are trivial."""

    def test_single_letters_covering_the_alphabet_are_trivial(self):
        graphemes = {c: ["x"] for c in "abcdefghij"}
        pairs = [(c, "x") for c in "abcdefghij"] + [
            ("banana", "bxnxnx"), ("garden", "gxrdxn")]
        with mock.patch.object(gc.o2i, "get",
                               return_value=_spec(graphemes)):
            trivial, real, stats = gc.classify_gold("zz", pairs)
        assert stats["is_alphabet_chart"] is True
        assert len(trivial) == 10
        assert len(real) == 2
        assert stats["n_trivial"] == 10
        assert ("banana", "bxnxnx") in real
        assert ("garden", "gxrdxn") in real

    def test_digraph_alphabet_entries_are_trivial_too(self):
        # A spec whose alphabet includes multi-character graphemes (e.g.
        # digraphs like "kw", "ch") should recognise chart rows that
        # spell those units out, not just single letters.
        graphemes = {"a": ["a"], "kw": ["kʷ"], "ch": ["tʃ"], "n": ["n"]}
        pairs = [("a", "a"), ("kw", "kʷ"), ("ch", "tʃ"), ("n", "n"),
                 ("nacho", "natʃo")]
        with mock.patch.object(gc.o2i, "get",
                               return_value=_spec(graphemes)):
            trivial, real, stats = gc.classify_gold("zz", pairs)
        assert stats["is_alphabet_chart"] is True
        assert ("kw", "kʷ") in trivial
        assert ("ch", "tʃ") in trivial
        assert ("nacho", "natʃo") in real


class TestClassifyGoldRealShortWords:
    """A handful of coincidentally short real words must NOT be flagged
    trivial: this is the case a naive length cutoff gets wrong."""

    def test_few_short_words_in_a_large_gold_are_not_trivial(self):
        graphemes = {c: ["x"] for c in "abcdefghijklmnopqrstuvwxyz"}
        # Only two short entries ("a", "y") out of a gold set that never
        # comes close to enumerating the 26-letter alphabet: coverage
        # stays far below the trivial threshold.
        pairs = [("a", "a"), ("y", "j")] + [
            (f"word{i}", "wxrd") for i in range(30)]
        with mock.patch.object(gc.o2i, "get",
                               return_value=_spec(graphemes)):
            trivial, real, stats = gc.classify_gold("zz", pairs)
        assert stats["is_alphabet_chart"] is False
        assert stats["n_trivial"] == 0
        assert trivial == []
        assert len(real) == len(pairs)

    def test_short_word_rich_language_below_threshold_stays_real(self):
        # A language whose gold happens to enumerate roughly a quarter of
        # its short alphabet as real words is still under the coverage
        # threshold and is left alone.
        graphemes = {c: ["x"] for c in "abcdefghijklmnopqrstu"}  # 21 letters
        short = [("a", "x"), ("i", "x"), ("o", "x"), ("u", "x"),
                 ("e", "x")]  # 5/21 < 0.3 threshold
        pairs = short + [(f"word{i}", "wxrd") for i in range(20)]
        with mock.patch.object(gc.o2i, "get",
                               return_value=_spec(graphemes)):
            trivial, real, stats = gc.classify_gold("zz", pairs)
        assert stats["is_alphabet_chart"] is False
        assert stats["alphabet_coverage"] < gc.ALPHABET_COVERAGE_THRESHOLD
        assert stats["n_trivial"] == 0


class TestClassifyGoldBoundAffix:
    """Some wikipron scrapes carry inflection-table cells as entries: a
    bound suffix form prefixed with U+0640 TATWEEL rather than a
    free-standing word (the ``tru/wikipron`` case). These are trivial
    independent of length or alphabet coverage."""

    def test_tatweel_prefixed_entry_is_trivial(self):
        graphemes = {c: ["x"] for c in "ab"}  # tiny alphabet: never charts
        pairs = [("ـܢܐ", "a n o"), ("real_word", "rxrl")]
        with mock.patch.object(gc.o2i, "get", return_value=_spec(graphemes)):
            trivial, real, stats = gc.classify_gold("tru", pairs)
        assert stats["n_bound_affix"] == 1
        assert ("ـܢܐ", "a n o") in trivial
        assert ("real_word", "rxrl") in real

    def test_apostrophe_is_never_treated_as_ignorable(self):
        # A phonemic apostrophe-class marker (e.g. Tarifit pharyngealisation,
        # Kwak'wala glottalization/ejective marks) must never be stripped by
        # the base-form fold: it changes the character, not the length
        # bucket, of an otherwise ordinary real word.
        graphemes = {c: ["x"] for c in "ab"}
        pairs = [("k'op", "k'op")]
        with mock.patch.object(gc.o2i, "get", return_value=_spec(graphemes)):
            trivial, real, stats = gc.classify_gold("zz", pairs)
        assert gc._base_form("k'op") == "k'op"
        assert ("k'op", "k'op") in real


class TestClassifyGoldStats:
    def test_single_and_two_char_counts_are_reported_independent_of_chart(self):
        # Composition counts (n_single_char / n_two_char) are raw length
        # stats and must be reported even when the coverage test does not
        # flag the row as an alphabet chart -- they are a separate signal
        # from the trivial/real split.
        # A large declared alphabet that these two short entries barely
        # dent, so coverage stays far below the trivial threshold.
        graphemes = {c: ["x"] for c in "abcdefghijklmnopqrstuvwxyz0123456789"}
        pairs = [("a", "a"), ("bo", "bo")] + [
            (f"word{i}", "wxrd") for i in range(10)]
        with mock.patch.object(gc.o2i, "get", return_value=_spec(graphemes)):
            trivial, real, stats = gc.classify_gold("zz", pairs)
        assert stats["n_single_char"] == 1
        assert stats["n_two_char"] == 1
        assert stats["is_alphabet_chart"] is False
        assert stats["n_trivial"] == 0

    def test_multiword_entries_are_never_trivial(self):
        # A sentence-level gold entry can be short in word count but is
        # never an alphabet-chart row: an alphabet chart is word-level.
        graphemes = {c: ["x"] for c in "ab"}
        pairs = [("a", "x"), ("b", "x"), ("a b", "x x")]
        with mock.patch.object(gc.o2i, "get", return_value=_spec(graphemes)):
            trivial, real, stats = gc.classify_gold("zz", pairs)
        assert ("a b", "x x") in real
        assert ("a b", "x x") not in trivial

    def test_spec_lookup_failure_degrades_to_no_trivial_split(self):
        # If the spec cannot be resolved (e.g. a stale board row for a
        # deregistered code) the alphabet inventory is empty, coverage is
        # always 0, and nothing is misclassified as trivial.
        pairs = [("a", "x"), ("b", "x")]
        with mock.patch.object(gc.o2i, "get", side_effect=KeyError("nope")):
            trivial, real, stats = gc.classify_gold("nonexistent-lang", pairs)
        assert stats["alphabet_size"] == 0
        assert stats["n_trivial"] == 0
        assert real == pairs


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
