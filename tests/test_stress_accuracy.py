"""The stress column: does the primary stress land on the gold's syllable.

PER strips stress marks, so it cannot see a stress error. The definition the
column implements is in docs/benchmarks.md ("Stress accuracy"). Every expected
value below is worked out by hand from the transcriptions in the test: which
syllable the gold marks, which one the hypothesis marks, and which segments
the edit-distance alignment pairs.
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import (  # noqa: E402
    THIN_ROW_N,
    StressTally,
    evaluate_words_oracle,
    normalize,
    stress_eligible,
    stress_matches,
    stress_reading,
)


def _reading(ipa):
    return stress_reading(ipa, broad=True)


def _scores(gold, hyp, word="w"):
    """``None`` when the gold is ineligible, else hit (True) or miss."""
    g = _reading(gold)
    if not stress_eligible(word, g):
        return None
    return stress_matches(g, _reading(hyp))


class TestDefinitionRegressionRows:
    """The rows the definition requires every implementation to carry."""

    @pytest.mark.parametrize("hyp", ["ˈsajdɐ", "ˈsaidɐ"])
    def test_saida_hiatus_read_as_diphthong_is_a_miss(self, hyp):
        # Gold sɐ-ˈi-dɐ stresses the i of the hiatus; both hypotheses stress
        # the a. The alignment pairs s-s, ɐ-a, i-j (or i-i), d-d, ɐ-ɐ, so
        # the gold's stressed i meets the hypothesis's third segment, not
        # its stressed a at index 1: a miss.
        assert _scores("sɐˈidɐ", hyp) is False

    def test_saida_right_stress_is_a_hit(self):
        assert _scores("sɐˈidɐ", "sɐˈidɐ") is True

    def test_texto_lost_glide_is_a_segment_error_not_a_stress_error(self):
        # Gold ˈtɐjʃtu, hypothesis ˈtɐʃtu: the j is deleted, the stressed ɐ
        # aligns with the stressed ɐ.
        assert _scores("ˈtɐjʃtu", "ˈtɐʃtu") is True

    def test_california_final_glide_read_as_vowel_keeps_the_stress(self):
        # Gold ka-li-ˈfɔr-nja has 4 syllables, the hypothesis ka-li-ˈfɔr-ni-a
        # has 5. Counted from the end the stressed ɔ moves from penultimate
        # to antepenultimate; aligned, ɔ still pairs with ɔ.
        assert _scores("kɐliˈfɔɾnjɐ", "kɐliˈfɔɾniɐ") is True

    def test_california_stress_on_the_glide_vowel_is_a_miss(self):
        assert _scores("kɐliˈfɔɾnjɐ", "kɐlifɔɾˈniɐ") is False

    def test_monosyllable_is_ineligible(self):
        # pão: ɐ̃ is the one nucleus, w̃ is a glide.
        assert _reading("ˈpɐ̃w̃").syllables == 1
        assert _scores("ˈpɐ̃w̃", "ˈpɐ̃w̃") is None

    def test_gold_with_no_mark_is_ineligible(self):
        assert _scores("kazɐ", "ˈkazɐ") is None

    def test_hypothesis_with_two_primary_marks_is_a_miss(self):
        assert _scores("ˈkazɐ", "ˈkaˈzɐ") is False

    def test_compound_secondary_mark_is_ignored(self):
        # guarda-chuva: secondary on gwar, primary on chu. Only the primary
        # is compared, so the hypothesis without the secondary is a hit.
        assert _scores("ˌɡwaɾdɐˈʃuvɐ", "ɡwaɾdɐˈʃuvɐ") is True
        assert _scores("ˌɡwaɾdɐˈʃuvɐ", "ˌɡwaɾdɐˈʃuvɐ") is True

    def test_compound_primary_on_the_first_element_is_a_miss(self):
        assert _scores("ˌɡwaɾdɐˈʃuvɐ", "ˈɡwaɾdɐˌʃuvɐ") is False


class TestEligibility:
    def test_ascii_apostrophe_is_folded_to_the_primary_mark(self):
        g = _reading("'kaza")
        assert g.primaries == 1
        assert stress_eligible("casa", g)
        assert stress_matches(g, _reading("ˈkazɐ")) is True

    def test_two_primary_marks_in_the_gold_is_ineligible(self):
        assert _scores("ˈkazɐˈkazɐ", "ˈkazɐkazɐ") is None

    def test_multiword_entry_is_ineligible(self):
        assert _scores("ˈkazɐ", "ˈkazɐ", word="a casa") is None

    def test_mark_with_no_nucleus_after_it_is_ineligible(self):
        # A mark at the end leaves no stressed syllable to compare.
        assert _scores("kazɐˈ", "ˈkazɐ") is None

    def test_non_syllabic_vowel_is_not_a_syllable(self):
        # pai̯: one nucleus, so ineligible as a monosyllable.
        assert _reading("ˈpai̯").syllables == 1

    def test_syllabic_consonant_is_a_nucleus(self):
        # Czech trhu ˈtr̩ɦu: the stressed nucleus is the syllabic r.
        g = _reading("ˈtr̩ɦu")
        assert g.syllables == 2
        assert g.segments[g.nucleus] == "r\u0329"

    def test_near_close_rounded_vowel_is_a_nucleus(self):
        # German Hütte ˈhʏtə: ʏ is an IPA chart vowel, so two syllables and
        # the stressed nucleus is ʏ at index 1 of "hʏtə".
        g = _reading("ˈhʏtə")
        assert g.syllables == 2
        assert g.segments[g.nucleus] == "ʏ"

    def test_dotted_gold_counts_a_syllable_once_per_dot_chunk(self):
        # Two vowel letters inside one dot-bounded syllable are one syllable.
        assert _reading("ˈsai.dɐ").syllables == 2
        # Without dots every nucleus is a syllable.
        assert _reading("ˈsaidɐ").syllables == 3

    def test_dotted_gold_aligns_like_the_undotted_one(self):
        assert _scores("kɐ.liˈfɔɾ.njɐ", "kɐliˈfɔɾniɐ") is True


class TestSegmentsAndTieBreaks:
    """The four details that keep this column comparable with tugaphone's."""

    def test_melhor_cost_tie_pairs_vowel_with_vowel(self):
        # Gold me-ˈʎɒɹ, hypothesis me-ˈʎɔ: one edit either way. Deleting ɹ
        # pairs ɒ with ɔ; deleting ɒ pairs ɹ with ɔ. Both cost 1; only the
        # first pairs vowel with vowel, and it puts the stressed ɒ on the
        # stressed ɔ: a hit.
        assert _scores("meˈʎɒɹ", "meˈʎɔ") is True

    def test_exigencia_tie_bar_joins_the_diphthong_into_one_segment(self):
        # Gold ˌe-zi-ˈʒe͡ɪŋ-sjæ: e͡ɪ is one stressed segment, so the gold has
        # 9 segments and the stressed one is index 4. The hypothesis
        # e-zi-ˈʒẽ-sjɐ stresses ẽ, also index 4, and ẽ pairs with e͡ɪ.
        g = _reading("ˌeziʒˈe͡ɪŋsjæ")
        assert len(g.segments) == 9
        assert g.segments[g.nucleus] == "eɪ"
        assert _scores("ˌeziʒˈe͡ɪŋsjæ", "eziˈʒẽsjɐ") is True

    def test_tied_affricate_is_one_segment(self):
        # ˈt͡ʃa.ta: t͡ʃ is one segment, so the stressed a is index 1.
        g = _reading("ˈt͡ʃa.ta")
        assert g.segments == ("tʃ", "a", "t", "a")
        assert g.nucleus == 1

    def test_hyphenated_compound_with_a_primary_on_each_element_is_a_miss(
            self):
        # guarda-chuva is one word, so it is eligible; a primary mark on
        # both elements is two primary marks.
        assert _scores("ˌɡwaɾdɐˈʃuvɐ", "ˈɡwaɾdɐˈʃuvɐ",
                       word="guarda-chuva") is False

    def test_multiword_entry_is_ineligible_when_its_gold_has_no_space(self):
        assert _scores("ɐˈkazɐ", "ɐˈkazɐ", word="a casa") is None

    @pytest.mark.parametrize("ipa", ["sɐˈidɐ", "ˈpʼã.ka", "ŋǃaˈkǀa",
                                     "a ˈbe"])
    def test_segments_carry_the_per_folds(self, ipa):
        # Without length marks or tie bars, the segments joined are exactly
        # the string PER compares.
        assert "".join(_reading(ipa).segments) == normalize(
            ipa, strip_stress=True, broad=True)


class TestTally:
    def test_thin_row_is_null(self):
        assert StressTally(eligible=THIN_ROW_N - 1,
                           hits=THIN_ROW_N - 1).accuracy is None

    def test_row_at_the_floor_reports_the_share(self):
        assert StressTally(eligible=THIN_ROW_N, hits=15).accuracy == (
            15 / THIN_ROW_N)

    def test_unmarked_gold_is_null_with_zero_count(self):
        t = StressTally()
        assert t.eligible == 0 and t.accuracy is None


class _FakeEngine:
    def __init__(self, best):
        self._best = best

    def transcribe_word(self, word):
        return self._best[word]

    def transcribe(self, text):
        return self._best[text]


@pytest.fixture
def fake_engine(monkeypatch):
    import orthography2ipa

    def _install(best):
        monkeypatch.setattr(orthography2ipa, "G2P",
                            lambda lang, **kw: _FakeEngine(best))
    return _install


class TestScoringLoop:
    def _run(self, pairs, stress):
        return evaluate_words_oracle(pairs, "xx", strip_stress=True,
                                     broad=True, oracle_ks=(), stress=stress)

    def test_counts_from_the_same_transcriptions_as_per(self, fake_engine):
        fake_engine({"saída": "ˈsajdɐ", "texto": "ˈtɐʃtu", "pão": "ˈpɐ̃w̃",
                     "casa": "kazɐ"})
        pairs = [("saída", "sɐˈidɐ"), ("texto", "ˈtɐjʃtu"),
                 ("pão", "ˈpɐ̃w̃"), ("casa", "ˈkazɐ")]
        tally = StressTally()
        with_stress = self._run(pairs, tally)
        # saída miss, texto hit, pão ineligible, casa miss (no mark).
        assert (tally.eligible, tally.hits) == (3, 1)
        # PER is the same with the tally on or off.
        assert with_stress == self._run(pairs, None)

    def test_word_with_several_golds_counts_once_and_hits_any(
            self, fake_engine):
        fake_engine({"w": "paˈta"})
        tally = StressTally()
        self._run([("w", "ˈpata"), ("w", "paˈta")], tally)
        assert (tally.eligible, tally.hits) == (1, 1)

    def test_uncovered_word_is_not_counted(self, fake_engine):
        fake_engine({"w": ""})
        tally = StressTally()
        self._run([("w", "ˈpata")], tally)
        assert tally.eligible == 0


def test_scoreboard_renders_the_stress_cell(tmp_path, monkeypatch):
    import benchmark

    monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(tmp_path / "s.md"))
    monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(tmp_path / "r.json"))
    base = {"dataset": "wikipron", "n": 500, "per": 0.1, "per_ci_low": 0.09,
            "per_ci_high": 0.11, "exact_match": 0.9, "quality_tier": "research",
            "provenance": "crowd-scraped", "harness_version": "1.1",
            "limit": None}
    benchmark.write_scoreboard([
        {**base, "lang": "aa", "stress_acc": 0.9123, "n_stress": 400},
        {**base, "lang": "bb", "stress_acc": None, "n_stress": 0},
        {**base, "lang": "cc"},
    ])
    table = [line for line in (tmp_path / "s.md").read_text(
        encoding="utf-8").splitlines() if line.startswith("| ")]
    header = [c.strip() for c in table[0].strip("|").split("|")]
    col = header.index("Stress")
    assert header[col - 1] == "PER"
    cells = {}
    for line in table[1:]:
        parts = [c.strip() for c in line.strip("|").split("|")]
        cells[parts[0]] = parts[col]
    assert cells == {"aa": "0.9123", "bb": "-", "cc": "·"}
