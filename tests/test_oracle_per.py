"""Top-k oracle PER in the benchmark harness.

Oracle PER@k is the per-word minimum PER over the engine's top-k
readings. It separates RANKING error (right answer in the beam, ranked
wrong — recoverable by a downstream rescorer) from MODEL error (right
answer absent from the lattice at any k). It is a lattice-quality
diagnostic for this engine ONLY and is never valid input to a
cross-system comparison; these tests pin that boundary too.
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402
from benchmark import (  # noqa: E402
    ORACLE_KS,
    ORACLE_REPORT_KS,
    OracleResult,
    assert_oracle_self_check,
    evaluate_words,
    evaluate_words_oracle,
)


class _FakeEngine:
    """Stand-in G2P: fixed 1-best and candidate list per word.

    Lets the oracle arithmetic be tested against transcriptions chosen to
    exercise the edge cases, instead of against whatever a real language
    spec happens to produce today (which would make the test a change
    detector for the spec data).
    """

    def __init__(self, best, cands, raise_on=()):
        self._best = best
        self._cands = cands
        self._raise_on = set(raise_on)

    def transcribe_word(self, word):
        return self._best[word]

    def transcribe(self, text):
        return self._best[text]

    def word_candidates(self, word, *, k=5):
        if word in self._raise_on:
            raise RuntimeError("no lattice for this word")
        return self._cands[word][:k]


@pytest.fixture
def fake_engine(monkeypatch):
    """Install a _FakeEngine as the G2P the harness constructs."""
    def _install(best, cands, raise_on=()):
        import orthography2ipa

        engine = _FakeEngine(best, cands, raise_on)
        monkeypatch.setattr(orthography2ipa, "G2P",
                            lambda lang, **kw: engine, raising=True)
        return engine
    return _install


def _run(pairs, oracle_ks=ORACLE_KS):
    # 'xx' never reaches a real spec: the engine is faked.
    return evaluate_words_oracle(pairs, "xx", strip_stress=True, broad=True,
                                 oracle_ks=oracle_ks)


class TestOracleArithmetic:
    def test_oracle_at_3_beats_top1_when_beam_holds_the_answer(
            self, fake_engine):
        # top-1 is 2 substitutions away from gold; candidate 3 is exact.
        fake_engine(best={"w": "aXY"},
                    cands={"w": ["aXY", "aXb", "abc"]})
        *_, oracle = _run([("w", "abc")])
        assert oracle.oracle_per[1] == pytest.approx(2 / 3)
        assert oracle.oracle_per[3] == 0.0
        assert oracle.oracle_per[3] < oracle.oracle_per[1]

    def test_oracle_at_1_equals_the_1_best_per(self, fake_engine):
        # The identity the whole metric rests on: candidate 0 IS the
        # 1-best answer, so oracle@1 must reproduce the PER column.
        fake_engine(best={"a": "xbc", "b": "de"},
                    cands={"a": ["xbc", "abc"], "b": ["de", "df"]})
        *_, per, _wer, oracle = _run([("a", "abc"), ("b", "df")])
        assert oracle.oracle_per[1] == pytest.approx(per)

    def test_oracle_is_monotone_non_increasing_in_k(self, fake_engine):
        fake_engine(best={"w": "zzz"},
                    cands={"w": ["zzz", "azz", "abz", "abc", "abc"]})
        *_, oracle = _run([("w", "abc")])
        vals = [oracle.oracle_per[k] for k in sorted(ORACLE_KS)]
        assert vals == sorted(vals, reverse=True)
        assert oracle.oracle_per[5] == 0.0

    def test_deeper_candidates_beyond_k_are_not_counted(self, fake_engine):
        # The exact answer sits at rank 6 — outside every reported k.
        fake_engine(best={"w": "zzz"},
                    cands={"w": ["zzz"] * 5 + ["abc"]})
        *_, oracle = _run([("w", "abc")])
        assert oracle.oracle_per[5] == pytest.approx(1.0)

    def test_multiple_golds_take_the_best_gold_per_candidate(
            self, fake_engine):
        # Dialect variants: a candidate matching ANY gold scores 0, the
        # same rule the 1-best column uses.
        fake_engine(best={"w": "zzz"}, cands={"w": ["zzz", "def"]})
        *_, oracle = _run([("w", "abc"), ("w", "def")])
        assert oracle.oracle_per[3] == 0.0


class TestGracefulFallback:
    def test_missing_candidates_fall_back_to_top1_and_are_counted(
            self, fake_engine):
        fake_engine(best={"w": "abd"}, cands={"w": []})
        *_, per, _wer, oracle = _run([("w", "abc")])
        assert oracle.fallback_words == 1
        assert oracle.oracle_per[5] == pytest.approx(per)

    def test_raising_candidates_never_crash_the_run(self, fake_engine):
        fake_engine(best={"w": "abd"}, cands={"w": ["abd", "abc"]},
                    raise_on={"w"})
        *_, per, _wer, oracle = _run([("w", "abc")])
        assert oracle.fallback_words == 1
        assert oracle.oracle_per[3] == pytest.approx(per)

    def test_sentence_entries_fall_back_without_calling_the_beam(
            self, fake_engine):
        # The beam is per WORD. A sentence gold entry gets no oracle
        # rather than a composed one the engine would never rank.
        fake_engine(best={"a b": "xy"}, cands={}, raise_on={"a b"})
        *_, per, _wer, oracle = _run([("a b", "ab")])
        assert oracle.fallback_words == 1
        assert oracle.oracle_per[3] == pytest.approx(per)

    def test_top1_mismatch_is_counted_not_hidden(self, fake_engine):
        # candidate 0 disagreeing with transcribe_word is an engine bug;
        # the harness must surface it, and oracle@1 then no longer
        # equals PER — which is exactly the signal.
        fake_engine(best={"w": "abd"}, cands={"w": ["abc", "abd"]})
        *_, per, _wer, oracle = _run([("w", "abc")])
        assert oracle.top1_mismatch == 1
        assert oracle.oracle_per[1] != pytest.approx(per)


class TestHarnessIntegration:
    def test_disabling_the_oracle_leaves_the_1_best_numbers_untouched(
            self, fake_engine):
        fake_engine(best={"a": "xbc", "b": "de"},
                    cands={"a": ["xbc", "abc"], "b": ["de", "df"]})
        pairs = [("a", "abc"), ("b", "df")]
        off = _run(pairs, oracle_ks=())
        on = _run(pairs)
        assert off[5] is None
        assert off[:5] == on[:5]

    def test_evaluate_words_still_returns_the_legacy_five_tuple(
            self, fake_engine):
        fake_engine(best={"a": "abc"}, cands={"a": ["abc"]})
        result = evaluate_words([("a", "abc")], "xx",
                                strip_stress=True, broad=True)
        assert len(result) == 5
        assert result[3] == 0.0

    def test_reported_ks_are_a_subset_of_computed_ks(self):
        assert set(ORACLE_REPORT_KS) <= set(ORACLE_KS)
        assert 1 in ORACLE_KS, "k=1 is the oracle-vs-PER self-check"


class TestAgainstTheRealEngine:
    """No fakes: the identity must hold for the shipped G2P too.

    If it ever fails, ``G2P.word_candidates`` and ``G2P.transcribe_word``
    have drifted apart and the oracle columns describe a different engine
    than the PER column. That is an engine bug, not a metric quirk.
    """

    @pytest.mark.parametrize("lang,words", [
        ("fr", ["bonjour", "femme", "oiseau", "chien", "chateau"]),
        ("pt-PT", ["olá", "mundo", "carro", "cidade"]),
        ("en-GB", ["nation", "through", "the", "night"]),
    ])
    def test_oracle_at_1_equals_per_and_candidate_0_is_the_1_best(
            self, lang, words):
        from orthography2ipa import G2P

        engine = G2P(lang)
        # Gold is irrelevant to the identity — any fixed target works.
        pairs = [(w, engine.transcribe_word(w)) for w in words]
        *_, per, _wer, oracle = evaluate_words_oracle(
            pairs, lang, strip_stress=True, broad=True)
        assert oracle.top1_mismatch == 0
        assert oracle.fallback_words == 0
        assert oracle.oracle_per[1] == pytest.approx(per)

    def test_oracle_never_exceeds_the_1_best_per(self):
        from orthography2ipa import G2P

        engine = G2P("fr")
        words = ["bonjour", "femme", "oiseau", "chien", "maison", "eau"]
        pairs = [(w, engine.transcribe_word(w)[::-1]) for w in words]
        *_, per, _wer, oracle = evaluate_words_oracle(
            pairs, "fr", strip_stress=True, broad=True)
        for k in ORACLE_KS:
            assert oracle.oracle_per[k] <= per + 1e-12


class TestOracleIsDiagnosticOnly:
    """The semantics guard: oracle@k must not leak into comparisons."""

    def test_compare_systems_does_not_read_oracle_fields(self):
        path = os.path.join(os.path.dirname(__file__), "..", "scripts",
                            "compare_systems.py")
        with open(path, encoding="utf-8") as fh:
            source = fh.read()
        assert "oracle" not in source.lower(), (
            "compare_systems.py must never consume oracle@k: every system "
            "it compares against emits ONE pronunciation")

    def test_ci_regression_sample_stays_1_best(self):
        path = os.path.join(os.path.dirname(__file__), "..", "benchmarks",
                            "results_ci_sample.json")
        with open(path, encoding="utf-8") as fh:
            source = fh.read()
        assert "oracle" not in source, (
            "the CI regression gate is 1-best by design")

    def test_docstring_states_the_diagnostic_only_rule(self):
        doc = OracleResult.__doc__ or ""
        assert "never" in doc.lower() and "cross-system" in doc.lower()


class TestExactMatchOracle:
    """OracleX@k: some top-k candidate EQUALS a gold, not merely nears it."""

    def test_a_closer_but_wrong_candidate_does_not_count_as_exact(
            self, fake_engine):
        # PER oracle improves (abz is nearer than zzz) but nothing is right.
        fake_engine(best={"w": "zzz"}, cands={"w": ["zzz", "abz"]})
        *_, oracle = _run([("w", "abc")])
        assert oracle.oracle_per[3] < oracle.oracle_per[1]
        assert oracle.oracle_exact[3] == 0.0

    def test_an_exact_candidate_counts(self, fake_engine):
        fake_engine(best={"w": "zzz"}, cands={"w": ["zzz", "abz", "abc"]})
        *_, oracle = _run([("w", "abc")])
        assert oracle.oracle_exact[3] == 1.0
        assert oracle.oracle_per[3] == 0.0

    def test_exact_at_1_is_the_exact_match_column(self, fake_engine):
        fake_engine(best={"a": "abc", "b": "zz"},
                    cands={"a": ["abc"], "b": ["zz", "de"]})
        *_, _per, wer, oracle = _run([("a", "abc"), ("b", "de")])
        assert oracle.oracle_exact[1] == pytest.approx(1.0 - wer)

    def test_exact_is_monotone_non_decreasing_in_k(self, fake_engine):
        fake_engine(best={"w": "zzz"},
                    cands={"w": ["zzz", "zza", "zab", "abc", "abc"]})
        *_, oracle = _run([("w", "abc")])
        vals = [oracle.oracle_exact[k] for k in sorted(ORACLE_KS)]
        assert vals == sorted(vals)
        assert oracle.oracle_exact[3] == 0.0
        assert oracle.oracle_exact[5] == 1.0

    def test_any_gold_variant_counts_as_exact(self, fake_engine):
        fake_engine(best={"w": "zzz"}, cands={"w": ["zzz", "def"]})
        *_, oracle = _run([("w", "abc"), ("w", "def")])
        assert oracle.oracle_exact[3] == 1.0


class TestSelfCheckIsFatal:
    """A disagreeing oracle must abort, never warn above exit 0."""

    def _ok(self, **kw):
        base = dict(oracle_per={1: 0.5, 3: 0.4, 5: 0.3},
                    oracle_exact={1: 0.0, 3: 0.0, 5: 0.0},
                    fallback_words=0, scored_words=10, top1_mismatch=0)
        base.update(kw)
        return OracleResult(**base)

    def test_agreeing_oracle_passes_silently(self):
        assert_oracle_self_check("ds", "xx", 0.5, 10, self._ok()) is None

    def test_top1_mismatch_exits_non_zero(self, capsys):
        with pytest.raises(SystemExit) as exc:
            assert_oracle_self_check("ds", "xx", 0.5, 10,
                                     self._ok(top1_mismatch=3))
        assert exc.value.code != 0
        assert "ENGINE BUG" in capsys.readouterr().err

    def test_oracle_at_1_diverging_from_per_exits_non_zero(self, capsys):
        with pytest.raises(SystemExit) as exc:
            assert_oracle_self_check("ds", "xx", 0.7, 10, self._ok())
        assert exc.value.code != 0
        assert "ENGINE BUG" in capsys.readouterr().err

    def test_float_noise_within_epsilon_is_not_an_abort(self):
        assert_oracle_self_check("ds", "xx", 0.5 + 1e-12, 10, self._ok())

    def test_build_scoreboard_writes_nothing_when_the_check_fails(
            self, monkeypatch, fake_engine):
        # candidate 0 != 1-best => the scoreboard would be corrupt.
        fake_engine(best={"a": "abd"}, cands={"a": ["abc", "abd"]})
        monkeypatch.setattr(benchmark, "DATASETS",
                            {"ds": (lambda lang, limit: [("a", "abc")],
                                    ["xx"])})
        monkeypatch.setattr(benchmark, "PROVENANCE", {"ds": "llm-generated"})
        with pytest.raises(SystemExit) as exc:
            benchmark.build_scoreboard(5, oracle=True)
        assert exc.value.code != 0


class TestTheCIGateStays1Best:
    """The regression gate must not pay 1.6x for columns it never reads."""

    def test_build_scoreboard_defaults_to_oracle_off(self, monkeypatch,
                                                    fake_engine):
        fake_engine(best={"a": "abc"}, cands={"a": ["abc", "abd"]})
        monkeypatch.setattr(benchmark, "DATASETS",
                            {"ds": (lambda lang, limit: [("a", "abc")],
                                    ["xx"])})
        monkeypatch.setattr(benchmark, "PROVENANCE", {"ds": "llm-generated"})
        rows = benchmark.build_scoreboard(5)
        assert rows and "oracle_per_top3" not in rows[0], (
            "oracle must be opt-in: a defaulted-on oracle silently taxes "
            "every call site, including the CI regression gate")

    def test_the_regression_script_does_not_opt_in(self):
        import inspect

        import check_benchmark_regression as cbr

        src = inspect.getsource(cbr)
        calls = [line for line in src.splitlines()
                 if "build_scoreboard(" in line]
        assert calls, "expected the gate to build a scoreboard"
        for line in calls:
            assert "oracle" not in line, (
                f"the CI gate must stay 1-best, got: {line.strip()}")

    def test_ci_sample_path_passes_oracle_false(self):
        import inspect

        src = inspect.getsource(benchmark.main)
        assert "build_scoreboard(CI_SAMPLE_LIMIT, oracle=False)" in src


_ORACLE_HEADERS = ("Oracle@3", "Oracle@5", "OracleX@3", "OracleX@5")


class TestScoreboardMarkers:
    """`·` (unrescored) and `-` (sentence-level) are different states.

    These assertions read only the four ORACLE cells (`Oracle@3`,
    `Oracle@5`, `OracleX@3`, `OracleX@5`), located by HEADER NAME — the
    same technique scripts/check_board_not_reverting.py's
    `_read_markdown` uses to key a row's cells regardless of column
    order — not by a hardcoded position. They used to scan the whole
    line for a bare `-`, which was a safe proxy for "no oracle cell
    reads as sentence-level" back when the oracle columns were the only
    ones a `-` could appear in. The `Ceiling` column legitimately
    renders `-` for a row with no measured `valid_ceiling` (see
    scripts/benchmark.py's `_valid_ceiling`), which is an unrelated
    state and would trip the old whole-line proxy on every ordinary
    row, and a hardcoded oracle-cell index would just as silently break
    the NEXT time a column is inserted ahead of the oracle block.
    Locating cells by header name is immune to both.
    """

    def _row(self, **kw):
        base = dict(lang="xx", dataset="ds", n=10, per=0.5, per_ci_low=0.4,
                    per_ci_high=0.6, exact_match=0.5, quality_tier="research",
                    provenance="crowd-scraped", harness_version="1.1",
                    limit=None)
        base.update(kw)
        return base

    def _render(self, tmp_path, monkeypatch, row):
        monkeypatch.setattr(benchmark, "SCOREBOARD_JSON",
                            str(tmp_path / "r.json"))
        monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(tmp_path / "s.md"))
        benchmark.write_scoreboard([row])
        text = (tmp_path / "s.md").read_text(encoding="utf-8")
        lines = text.splitlines()
        header_line = next(ln for ln in lines if ln.startswith("| Lang |"))
        data_line = next(ln for ln in lines if ln.startswith("| xx |"))
        return header_line, data_line

    @classmethod
    def _oracle_cells(cls, header_line, data_line):
        """The four oracle cells for *data_line*, keyed by the header
        names in *header_line* — never by position."""
        headers = [c.strip() for c in header_line.strip().strip("|").split("|")]
        cells = [c.strip() for c in data_line.strip().strip("|").split("|")]
        by_header = dict(zip(headers, cells))
        missing = [h for h in _ORACLE_HEADERS if h not in by_header]
        assert not missing, (
            f"expected oracle headers {_ORACLE_HEADERS} in the rendered "
            f"table, missing {missing} — got headers {headers}. A rename "
            "here must fail loudly rather than let an empty/short slice "
            "make the marker assertions vacuously true."
        )
        return [by_header[h] for h in _ORACLE_HEADERS]

    def test_unrescored_row_reads_dot_not_dash(self, tmp_path, monkeypatch):
        header_line, data_line = self._render(tmp_path, monkeypatch, self._row())
        oracle_cells = self._oracle_cells(header_line, data_line)
        assert all(c == "·" for c in oracle_cells), (
            "an unrescored row must not read as a sentence-level row, "
            f"which would look like zero ranking error: {oracle_cells}")

    def test_sentence_level_row_reads_dash(self, tmp_path, monkeypatch):
        row = self._row(oracle_per_top3=0.5, oracle_per_top5=0.5,
                        oracle_exact_top3=0.0, oracle_exact_top5=0.0,
                        oracle_fallback_words=10, oracle_scored_words=0)
        header_line, data_line = self._render(tmp_path, monkeypatch, row)
        oracle_cells = self._oracle_cells(header_line, data_line)
        assert all(c == "-" for c in oracle_cells), oracle_cells

    def test_measured_row_prints_numbers(self, tmp_path, monkeypatch):
        row = self._row(oracle_per_top3=0.3, oracle_per_top5=0.2,
                        oracle_exact_top3=0.1, oracle_exact_top5=0.15,
                        oracle_fallback_words=0, oracle_scored_words=10)
        _, data_line = self._render(tmp_path, monkeypatch, row)
        assert ("0.3000" in data_line and "0.2000" in data_line
                and "0.1500" in data_line)

    def test_scored_words_not_n_decides_the_marker(self, tmp_path,
                                                   monkeypatch):
        # A row whose fallback count happens not to equal `n` must still
        # be judged on whether ANY word got a real candidate list.
        row = self._row(n=99, oracle_per_top3=0.5, oracle_per_top5=0.5,
                        oracle_exact_top3=0.0, oracle_exact_top5=0.0,
                        oracle_fallback_words=10, oracle_scored_words=0)
        header_line, data_line = self._render(tmp_path, monkeypatch, row)
        assert all(c == "-" for c in self._oracle_cells(header_line, data_line))


class TestScoredWordCount:
    def test_scored_words_excludes_fallbacks(self, fake_engine):
        fake_engine(best={"a": "abc", "b": "de"},
                    cands={"a": ["abc"], "b": []})
        *_, oracle = _run([("a", "abc"), ("b", "de")])
        assert oracle.fallback_words == 1
        assert oracle.scored_words == 1
