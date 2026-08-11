"""A zero-coverage evaluation must never be recorded as a scoreboard row.

Regression guard for the silent-fabrication failure that produced stale
``n=0, per=1.0`` rows (tn/ug/yue): ``build_scoreboard`` must refuse to
append a row when ``covered == 0`` and say so on stderr.
"""
import io
import sys
import contextlib

sys.path.insert(0, "scripts")
import benchmark  # noqa: E402


def test_zero_coverage_row_is_refused(monkeypatch):
    def dead_loader(lang, limit):
        return [("word-with-no-scorable-graphemes", "ipa")]

    def zero_eval(pairs, lang, strip_stress, broad, oracle_ks=(),
                  expose_ambiguous_endings=False):
        # The board's measurement convention must reach the scorer:
        # a stub that silently swallowed it would let build_scoreboard
        # stop threading the flag with nothing noticing.
        assert expose_ambiguous_endings is False
        return len(pairs), 0, [], 1.0, 1.0, None

    monkeypatch.setattr(benchmark, "DATASETS",
                        {"deadset": (dead_loader, ["xx-dead"])})
    monkeypatch.setattr(benchmark, "PROVENANCE",
                        {"deadset": "llm-generated"})
    monkeypatch.setattr(benchmark, "evaluate_words_oracle", zero_eval)

    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        rows = [r for r in benchmark.build_scoreboard(5)
                if r["dataset"] == "deadset"]

    assert rows == [], "zero-coverage row must not be recorded"
    assert "REFUSING" in err.getvalue()


def test_nonzero_coverage_row_is_recorded(monkeypatch):
    def loader(lang, limit):
        return [("a", "a")]

    def one_eval(pairs, lang, strip_stress, broad, oracle_ks=(),
                  expose_ambiguous_endings=False):
        # The board's measurement convention must reach the scorer:
        # a stub that silently swallowed it would let build_scoreboard
        # stop threading the flag with nothing noticing.
        assert expose_ambiguous_endings is False
        return 1, 1, [0.0], 0.0, 0.0, None

    monkeypatch.setattr(benchmark, "DATASETS",
                        {"liveset": (loader, ["xx-live"])})
    monkeypatch.setattr(benchmark, "PROVENANCE",
                        {"liveset": "llm-generated"})
    monkeypatch.setattr(benchmark, "evaluate_words_oracle", one_eval)

    rows = [r for r in benchmark.build_scoreboard(5)
            if r["dataset"] == "liveset"]
    assert len(rows) == 1 and rows[0]["n"] == 1
