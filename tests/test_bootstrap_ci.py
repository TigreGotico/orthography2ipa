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
    bootstrap_per_ci,
    evaluate,
    evaluate_words,
)


def test_bootstrap_ci_matches_hand_precomputed_fixture():
    # Hand-precomputed once via bootstrap_per_ci([0.0, 0.5, 1.0, 0.25])
    # with BOOTSTRAP_SEED/BOOTSTRAP_REPS at their current values.
    pers = [0.0, 0.5, 1.0, 0.25]
    low, high = bootstrap_per_ci(pers)
    assert round(low, 6) == round(0.125, 6)
    assert round(high, 6) == round(0.7515624999999986, 6)


def test_bootstrap_ci_deterministic_across_calls():
    pers = [0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 1.0]
    first = bootstrap_per_ci(pers)
    second = bootstrap_per_ci(pers)
    assert first == second


def test_bootstrap_ci_uses_fixed_module_seed_and_rep_count():
    pers = [0.0, 1.0]
    import random

    rng = random.Random(BOOTSTRAP_SEED)
    n = len(pers)
    means = []
    for _ in range(BOOTSTRAP_REPS):
        sample = [pers[rng.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()
    expected_low = means[0]
    expected_high = means[-1]
    low, high = bootstrap_per_ci(pers)
    assert low == expected_low
    assert high == expected_high


def test_bootstrap_ci_empty_input_is_zero():
    assert bootstrap_per_ci([]) == (0.0, 0.0)


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
