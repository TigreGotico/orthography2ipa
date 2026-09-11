"""Tests for scripts/check_board_row_counts.py.

The regression gate is one-sided — it only fires when a row gets worse —
so a board row left behind by a change to its own gold loader can publish
a stale number indefinitely with CI green. That is exactly what happened
when the ``vox_communis`` loader started dropping the aligner's ``spn``
coverage-hole marker: 26 rows kept scoring a gold set a quarter larger
than the one the code produced, and several published a PER above 1.0.

These cover the impossibility the check tests for (a row scoring more
words than its gold holds), the healthy case it must NOT flag (a row
scoring fewer, which is what an uncoverable-word language looks like),
and the fossil case (a row no loader will serve).
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import check_board_row_counts as cbrc  # noqa: E402


def _row(lang="it", dataset="vox_communis", n=48570, per=0.1031):
    return {"lang": lang, "dataset": dataset, "n": n, "per": per}


@pytest.fixture
def gold(monkeypatch):
    """Stub the loaders with a ``{(dataset, lang): pair_count}`` table."""
    sizes = {}

    def fake_gold_size(dataset, lang):
        value = sizes[(dataset, lang)]
        if isinstance(value, Exception):
            raise value
        return value

    monkeypatch.setattr(cbrc, "DATASETS", {"vox_communis": (None, [])})
    monkeypatch.setattr(cbrc, "gold_size", fake_gold_size)
    return sizes


class TestStaleRows:
    def test_row_scoring_more_words_than_the_gold_holds_is_stale(self, gold):
        """The `it` row as committed before the spn fix: n=90332 against a
        gold that now yields 48570 pairs."""
        gold[("vox_communis", "it")] = 48570
        stale, unreachable, skipped = cbrc.check_rows([_row(n=90332)], 0.01)
        assert [r["lang"] for r, _ in stale] == ["it"]
        assert stale[0][1] == 48570
        assert not unreachable and not skipped

    def test_row_matching_its_gold_is_clean(self, gold):
        gold[("vox_communis", "it")] = 48570
        stale, _, _ = cbrc.check_rows([_row(n=48570)], 0.01)
        assert stale == []

    def test_row_scoring_fewer_words_is_never_flagged(self, gold):
        """`ja` scores 42549 of 48607 pairs because the kana spec gives a
        kanji-only word no hypothesis. A lower bound would fire on it."""
        gold[("vox_communis", "ja")] = 48607
        stale, _, _ = cbrc.check_rows([_row("ja", n=42549)], 0.01)
        assert stale == []

    def test_tolerance_absorbs_snapshot_drift(self, gold):
        """A re-fetch moves a live-snapshot gold by a handful of words, so
        an `n` a few above the pair count is noise, not staleness."""
        gold[("vox_communis", "ca")] = 141623
        stale, _, _ = cbrc.check_rows([_row("ca", n=141624)], 0.01)
        assert stale == []

    def test_drift_past_the_tolerance_is_stale(self, gold):
        gold[("vox_communis", "eu")] = 63415
        stale, _, _ = cbrc.check_rows([_row("eu", n=64075)], 0.01)
        assert [r["lang"] for r, _ in stale] == ["eu"]


class TestUnreachableRows:
    def test_row_whose_loader_refuses_the_language(self, gold):
        """The `zh` fossil: the row survived the spec's de-registration, so
        no code path can reproduce it."""
        gold[("vox_communis", "zh")] = KeyError("zh")
        stale, unreachable, _ = cbrc.check_rows([_row("zh", n=121)], 0.01)
        assert not stale
        assert unreachable[0][0]["lang"] == "zh"
        assert "KeyError" in unreachable[0][1]

    def test_row_naming_an_unregistered_dataset(self, gold):
        stale, unreachable, _ = cbrc.check_rows(
            [_row(dataset="retired_gold")], 0.01)
        assert not stale
        assert "retired_gold" in unreachable[0][1]

    def test_zero_pair_gold_is_unreachable_not_a_zero_division(self, gold):
        """A gold that now yields 0 pairs is a fossil, not drift: the ratio
        `n / gold_n` is undefined, so the row must land in `unreachable`
        rather than crash the report."""
        gold[("vox_communis", "km")] = 0
        stale, unreachable, _ = cbrc.check_rows([_row("km", n=121)], 0.01)
        assert not stale
        assert unreachable[0][0]["lang"] == "km"


class TestOfflineRuns:
    def test_unfetchable_gold_is_skipped_not_failed(self, gold):
        """A run with no network must report the rows it could not check
        rather than declaring every one of them broken."""
        gold[("vox_communis", "it")] = OSError("Name or service not known")
        stale, unreachable, skipped = cbrc.check_rows([_row()], 0.01)
        assert not stale and not unreachable
        assert skipped[0][0]["lang"] == "it"

    def test_missing_optional_dependency_is_skipped_not_unreachable(self, gold):
        """A loader that needs an uninstalled optional package (e.g.
        `rarfile`) raises ModuleNotFoundError, not a network error. That is
        an environment gap, not proof the row is a fossil no code path can
        reproduce, so it must land in `skipped`."""
        gold[("vox_communis", "co")] = ModuleNotFoundError(
            "No module named 'rarfile'")
        stale, unreachable, skipped = cbrc.check_rows([_row("co")], 0.01)
        assert not stale and not unreachable
        assert skipped[0][0]["lang"] == "co"
        assert "rarfile" in skipped[0][1]


class TestRealDatasetsRegistry:
    def test_gold_size_against_the_real_registry(self):
        """The stubbed `gold` fixture replaces `DATASETS` wholesale. Exercise
        the real `coruss_ru` loader, which needs the optional `rarfile`
        package: where it is not installed, the loader must raise
        `ModuleNotFoundError`, land in `_OFFLINE_ERRORS`, and bucket the row
        as skipped rather than unreachable. Runners that do have `rarfile`
        installed can't exercise that precondition, so this skips itself
        rather than asserting on whatever the loader does with the package
        present (a live network fetch, most likely)."""
        try:
            import rarfile  # noqa: F401
        except ImportError:
            pass
        else:
            pytest.skip("rarfile is installed here; cannot exercise the "
                        "missing-dependency skip path")

        stale, unreachable, skipped = cbrc.check_rows(
            [_row("ru", dataset="coruss_ru", n=1)], 0.01)
        assert not stale
        assert unreachable == []
        assert skipped, "expected the coruss_ru row to be skipped"
        row, reason = skipped[0]
        assert row["lang"] == "ru"
        assert "rarfile" in reason
