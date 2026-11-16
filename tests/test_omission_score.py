"""The omission-score helper, checked against arithmetic done by hand.

Every expected number here is derived on paper from the definition —
character-level edit distance to the gold, divided by the gold length,
averaged over words — and never read back out of the helper.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import pytest  # noqa: E402

from omission_score import (  # noqa: E402
    OmissionResult,
    omission_score,
    segment_clusters,
    strip_segments,
)

SHORT_VOWELS = ("a", "i", "u")


class TestSegmentClusters:
    def test_a_length_mark_joins_the_vowel_before_it(self):
        assert segment_clusters("kaːtib") == ["k", "aː", "t", "i", "b"]

    def test_a_combining_mark_joins_its_base(self):
        # Syllabic s has no precomposed form, so the ring below stays a
        # separate code point and still has to ride with its base.
        assert segment_clusters("s\u0329t") == ["s\u0329", "t"]

    def test_a_leading_modifier_starts_its_own_segment(self):
        assert segment_clusters("ːa") == ["ː", "a"]


class TestStripSegments:
    def test_it_removes_every_listed_segment(self):
        assert strip_segments("kataba", SHORT_VOWELS) == "ktb"

    def test_a_long_vowel_survives_when_only_the_short_one_is_listed(self):
        # An abjad writes the long vowels. Removing "a" must leave "aː"
        # standing, or the score describes a script nobody reads.
        assert strip_segments("kaːtib", ("a", "i")) == "kaːtb"

    def test_a_long_vowel_goes_when_it_is_listed_itself(self):
        assert strip_segments("kaːtib", ("aː", "i")) == "ktb"

    def test_a_modifier_stays_with_the_consonant_it_modifies(self):
        assert strip_segments("sˤadaqa", ("a",)) == "sˤdq"

    def test_a_bare_length_mark_is_stripped_off_its_vowel(self):
        # A script that writes the vowel but not its length leaves a spec
        # able to emit the vowel short.
        assert strip_segments("kaːtib", ("ː",)) == "katib"

    def test_a_stripped_mark_can_expose_a_segment_that_also_goes(self):
        assert strip_segments("kaːtib", ("ː", "a", "i")) == "ktb"

    def test_an_unlisted_segment_survives(self):
        assert strip_segments("kataba", ("i",)) == "kataba"


class TestTheOmissionScore:
    def test_one_word_score_is_deleted_chars_over_gold_length(self):
        # "kataba" -> "ktb": three deletions over six gold characters.
        res = omission_score([("w", "kataba")], "acm", SHORT_VOWELS)
        assert res == OmissionResult(score=0.5, words=1, gold_chars=6,
                                  removed_chars=3)

    def test_it_averages_per_word_not_over_pooled_chars(self):
        # By hand: "kataba" 3/6 = 0.5, "bi" 1/2 = 0.5, mean 0.5.
        # Pooled characters would give 4/8 = 0.5 as well, so this pair is
        # chosen so the two agree; the next test separates them.
        res = omission_score([("w1", "kataba"), ("w2", "bi")], "acm", SHORT_VOWELS)
        assert res.score == pytest.approx(0.5)
        assert res.words == 2

    def test_share_and_score_are_different_numbers(self):
        # "aaab" loses 3 of 4 = 0.75; "kb" loses nothing = 0.0.
        # The score is the mean of the two words: 0.375.
        # Pooled share is 3 of 6 characters: 0.5. Quoting the share
        # instead is the error this helper exists to stop.
        res = omission_score([("w1", "aaab"), ("w2", "kb")], "acm", SHORT_VOWELS)
        assert res.score == pytest.approx(0.375)
        assert res.removed_share == pytest.approx(0.5)

    def test_a_word_scores_against_its_kindest_gold(self):
        # The scorer takes the minimum over a word's golds, so an
        # unvowelled variant puts this word's score at zero.
        res = omission_score([("w", "tu"), ("w", "t")], "acm", SHORT_VOWELS)
        assert res.score == 0.0
        assert res.words == 1

    def test_a_spec_that_loses_nothing_scores_zero(self):
        res = omission_score([("w", "ktb")], "acm", SHORT_VOWELS)
        assert res.score == 0.0
        assert res.removed_chars == 0

    def test_empty_gold_contributes_no_word(self):
        assert omission_score([("w", "")], "acm", SHORT_VOWELS).words == 0


class TestItIsWhatTheScorerWouldReport:
    """The score must be a PER the harness itself would print.

    A number computed by any other arithmetic is not comparable with the
    board row it is quoted against, which is the whole reason for
    quoting it.
    """

    def test_it_equals_scoring_the_best_hypothesis_through_the_harness(
            self, monkeypatch):
        import benchmark
        import orthography2ipa
        from benchmark import levenshtein, normalize

        vowels = ("a", "i", "u")
        pairs = [("kataba", "kataba"), ("kitaːb", "kitaːb"),
                 ("bint", "bint"), ("ʃams", "ʃamsu"), ("ʃams", "ʃams"),
                 ("qalb", "qalbu"), ("daras", "darasa")]

        refs = {}
        for word, gold in pairs:
            refs.setdefault(word, []).append(gold)
        best = {}
        for word, golds in refs.items():
            golds_norm = [normalize(g, True, True) for g in golds]
            cands = [normalize(strip_segments(g, vowels), True, True)
                     for g in golds]
            best[word] = min(
                cands,
                key=lambda h: min(levenshtein(h, r) / len(r)
                                  for r in golds_norm))

        class _BestPossibleSpec:
            """Emits the gold minus the segments, and nothing else wrong."""

            def transcribe_word(self, word):
                return best[word]

            transcribe = transcribe_word

            def word_candidates(self, word, k=1):
                return [best[word]]

        monkeypatch.setattr(orthography2ipa, "G2P",
                            lambda *a, **k: _BestPossibleSpec())
        _n, _covered, _pers, scored, _wer = benchmark.evaluate_words(
            pairs, "acm", strip_stress=True, broad=True)

        assert omission_score(pairs, "acm", vowels).score == pytest.approx(scored)
