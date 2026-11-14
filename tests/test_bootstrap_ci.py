"""Tests for the bootstrap confidence interval added to
scripts/benchmark.py's scoreboard (Workstream M, task M1).

Covers: determinism given the fixed seed (hand-precomputed fixture),
and that refactoring evaluate() to expose the per-word PER list left
the point-estimate PER unchanged.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import (  # noqa: E402
    BOOTSTRAP_REPS,
    BOOTSTRAP_SEED,
    THIN_ROW_N,
    bootstrap_per_ci,
    evaluate,
    evaluate_words,
)


def _percentile_interval(pers):
    """The 2.5th/97.5th percentile of the resampled means, written out
    independently of the function under test."""
    import random

    rng = random.Random(BOOTSTRAP_SEED)
    n = len(pers)
    means = sorted(
        sum(pers[rng.randrange(n)] for _ in range(n)) / n
        for _ in range(BOOTSTRAP_REPS))
    top = len(means) - 1

    def at(p):
        i = int(p * top)
        j = min(i + 1, top)
        return means[i] + (means[j] - means[i]) * (p * top - i)

    return at(0.025), at(0.975)


def test_bootstrap_ci_matches_an_independent_resampling():
    pers = [0.0, 0.5, 1.0, 0.25] * (THIN_ROW_N // 4)
    low, high = bootstrap_per_ci(pers)
    expected_low, expected_high = _percentile_interval(pers)
    assert low == expected_low
    assert high == expected_high


def test_bootstrap_ci_deterministic_across_calls():
    pers = [i / 10 % 1 for i in range(THIN_ROW_N + 3)]
    first = bootstrap_per_ci(pers)
    second = bootstrap_per_ci(pers)
    assert first == second


def test_bootstrap_ci_is_null_below_the_minimum_sample():
    """A sample too small to resample has no interval; reporting its point
    as [x, x] claims perfect certainty."""
    assert bootstrap_per_ci([]) == (None, None)
    assert bootstrap_per_ci([0.7143]) == (None, None)
    assert bootstrap_per_ci([0.5, 0.0]) == (None, None)
    assert bootstrap_per_ci([0.5] * (THIN_ROW_N - 1)) == (None, None)


def test_bootstrap_ci_has_positive_width_at_the_minimum_sample():
    pers = [i / THIN_ROW_N for i in range(THIN_ROW_N)]
    low, high = bootstrap_per_ci(pers)
    mean = sum(pers) / len(pers)
    assert low < mean < high


def test_evaluate_words_mean_equals_sum_over_len_of_per_word_list():
    pairs = [("cat", "kat"), ("dog", "dog"), ("fox", "foks")]
    n, covered, pers, per, wer = evaluate_words(
        pairs, "en", strip_stress=True, broad=True,
    )
    assert covered == len(pers)
    if pers:
        assert per == sum(pers) / len(pers)


def test_evaluate_point_estimate_unchanged_by_refactor():
    pairs = [("cat", "kat"), ("dog", "dog"), ("fox", "foks")]
    n1, covered1, per1, wer1 = evaluate(
        pairs, "en", strip_stress=True, broad=True,
    )
    n2, covered2, pers2, per2, wer2 = evaluate_words(
        pairs, "en", strip_stress=True, broad=True,
    )
    assert (n1, covered1, per1, wer1) == (n2, covered2, per2, wer2)
    if pers2:
        assert per1 == sum(pers2) / len(pers2)
