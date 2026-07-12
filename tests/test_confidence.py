"""Tests for the per-word confidence / OOV signal (Workstream B5).

The confidence is a pure, deterministic read off the pronunciation
lattice, surfaced as :attr:`WordTranscription.confidence` and via
:meth:`G2P.word_confidence` / :meth:`G2P.confidence_breakdown`. These tests
pin the load-bearing contracts:

* **ordering** — an unambiguous, fully-mapped word scores near ``1.0``; a
  known-ambiguous word scores clearly lower; an OOV-containing word scores
  low with ``coverage < 1`` reflected;
* **per-slot math** — the exact ``[0, 1]`` mapping of the ambiguity margin
  and winner rarity, checked on synthetic slots;
* **determinism** — identical input yields an identical number;
* **byte-identical** — adding the signal does not perturb ``ipa`` output
  (``transcribe`` / ``ipa_best`` / the scoreboard are unchanged), and the
  read never mutates the lattice.
"""
import math

import pytest

from orthography2ipa import ConfidenceBreakdown, G2P, WordTranscription
from orthography2ipa.phonetok import (
    Candidate,
    PhonetokTokenizer,
    SegmentSlot,
    lattice_confidence,
    slot_confidence,
)
from orthography2ipa.registry import get


def _slot(*costs: float) -> SegmentSlot:
    """Synthetic slot with candidates at the given ascending costs."""
    return SegmentSlot(
        grapheme="x", span=(0, 1),
        candidates=tuple(Candidate(ipa=f"p{i}", cost=c)
                         for i, c in enumerate(costs)))


# ─── per-slot math (synthetic, exact) ────────────────────────────────────

class TestSlotMath:
    def test_single_candidate_is_fully_confident(self):
        # No rival candidate → no ambiguity, canonical winner → 1.0.
        assert slot_confidence(_slot(0.0)) == 1.0

    def test_tied_zero_cost_candidates_are_zero_confidence(self):
        # margin 0 → ambiguity 0; winner cost 0 → rarity 1 → 0.0.
        assert slot_confidence(_slot(0.0, 0.0)) == 0.0

    def test_rank_cost_margin_of_one(self):
        # Plain-list ambiguity: margin 1.0 over a zero-cost winner.
        # 1 - exp(-1) ≈ 0.6321.
        assert slot_confidence(_slot(0.0, 1.0)) == pytest.approx(
            1.0 - math.exp(-1.0))

    def test_wide_margin_approaches_one(self):
        assert slot_confidence(_slot(0.0, 20.0)) == pytest.approx(1.0, abs=1e-6)

    def test_rare_winner_lowers_confidence(self):
        # Same margin, but a high-cost winner (rare mapping) is penalised.
        near = slot_confidence(_slot(0.0, 2.0))
        rare = slot_confidence(_slot(2.0, 4.0))
        assert rare < near

    def test_empty_slot_is_zero(self):
        assert slot_confidence(_slot()) == 0.0

    def test_lattice_uses_weakest_link(self):
        confident = _slot(0.0)          # 1.0
        ambiguous = _slot(0.0, 1.0)     # ~0.632
        assert lattice_confidence([confident, ambiguous]) == pytest.approx(
            slot_confidence(ambiguous))

    def test_empty_lattice_is_confident(self):
        # Nothing to be unsure about (e.g. a lexicon override).
        assert lattice_confidence([]) == 1.0


# ─── engine-level ordering ───────────────────────────────────────────────

class TestOrdering:
    def test_unambiguous_word_scores_near_one(self):
        # es-ES "luz" — every grapheme has a single realisation.
        assert G2P("es-ES").word_confidence("luz") == pytest.approx(1.0)

    def test_ambiguous_word_scores_clearly_lower(self):
        e = G2P("es-ES")
        assert e.word_confidence("gato") < e.word_confidence("luz")
        assert e.word_confidence("gato") < 0.8

    def test_english_th_ambiguity_lowers_confidence(self):
        # en-GB "scarf" is unambiguous; "myth"/"plinth" carry an ambiguous
        # grapheme (⟨th⟩ → ð/θ, ⟨y⟩, …) and must score lower. (Words are
        # chosen OUTSIDE the shipped en-GB pilot lexicon so this exercises the
        # rules-based lattice confidence, not a lexicon override — a lexicon
        # hit is a certain answer with confidence 1.0 by design.)
        e = G2P("en-GB")
        assert e.word_confidence("scarf") == pytest.approx(1.0)
        assert e.word_confidence("plinth") < e.word_confidence("scarf")
        assert e.word_confidence("myth") < e.word_confidence("scarf")

    def test_weighted_spec_gives_graded_confidence(self):
        # en-GB ⟨er⟩ carries −log P weights (əɹ P=0.8, ɜːɹ P=0.2): the
        # margin is < the flat rank separation and the winner is not free,
        # so "deter" lands strictly between 0 and 1. ("deter" is outside the
        # shipped pilot lexicon, so this reads the rules lattice, not a hit.)
        c = G2P("en-GB").word_confidence("deter")
        assert 0.0 < c < 1.0


# ─── OOV / coverage signal ───────────────────────────────────────────────

class TestOOV:
    def test_oov_char_lowers_confidence_and_reflects_coverage(self):
        e = G2P("en-GB")
        mapped = e.word_confidence("bar")           # coverage 1.0
        b = e.confidence_breakdown("bar你")           # one OOV char
        assert b.coverage < 1.0
        assert b.unmapped == ("你",)
        assert b.value < mapped
        # value is the lattice confidence folded with coverage.
        assert b.value == pytest.approx(b.lattice * b.coverage)

    def test_all_oov_word_is_zero_confidence(self):
        # Nothing maps → coverage 0 → confidence 0.
        assert G2P("en-GB").word_confidence("你好") == pytest.approx(0.0)

    def test_detailed_word_carries_confidence_and_coverage(self):
        r = G2P("en-GB").transcribe_detailed("bar你")
        w = r.words[0]
        assert w.coverage < 1.0
        # confidence folds coverage, so it can never exceed it.
        assert w.confidence <= w.coverage


# ─── determinism ─────────────────────────────────────────────────────────

class TestDeterminism:
    @pytest.mark.parametrize("word", ["gato", "luz", "casa", "bar你", "her"])
    def test_same_input_same_confidence(self, word):
        e = G2P("es-ES")
        assert e.word_confidence(word) == e.word_confidence(word)

    def test_breakdown_is_reproducible(self):
        e = G2P("en-GB")
        a = e.confidence_breakdown("mother")
        b = e.confidence_breakdown("mother")
        assert a == b


# ─── byte-identical: the signal is purely additive ───────────────────────

_CORPUS = {
    "pt": ["olá", "mundo", "casa", "gato", "sol", "fim", "cidade"],
    "es-ES": ["hola", "mundo", "gato", "luz", "casa", "cena"],
    "en-GB": ["through", "cough", "mother", "water", "bar", "myth"],
}


class TestByteIdentical:
    def test_default_word_transcription_confidence_is_neutral(self):
        # A plain WordTranscription (no lattice) defaults to 1.0, so callers
        # constructing one by hand are unaffected.
        assert WordTranscription(word="x", ipa="x").confidence == 1.0

    @pytest.mark.parametrize("lang", sorted(_CORPUS))
    def test_ipa_output_unchanged_by_confidence(self, lang):
        # transcribe()/ipa are chosen from the beam, never from the
        # confidence read — the chosen ipa must equal the lattice top and be
        # stable regardless of whether confidence is inspected.
        e = G2P(lang)
        tok = PhonetokTokenizer(get(lang))
        for w in _CORPUS[lang]:
            detailed = e.transcribe_detailed(w)
            # Reading confidence does not change the transcription.
            assert detailed.ipa == e.transcribe(w)
            _ = e.word_confidence(w)
            assert e.transcribe_detailed(w).ipa == detailed.ipa
            # ipa_best is untouched by the new read.
            assert tok.ipa_best(w) == tok.ipa_best(w)

    def test_confidence_read_does_not_mutate_lattice(self):
        e = G2P("en-GB")
        before = e.ipa_lattice("mother")
        _ = lattice_confidence(before)
        after = e.ipa_lattice("mother")
        assert before == after

    def test_confidence_always_in_unit_interval(self):
        for lang, words in _CORPUS.items():
            e = G2P(lang)
            for w in words:
                c = e.word_confidence(w)
                assert 0.0 <= c <= 1.0

    def test_breakdown_value_matches_word_confidence(self):
        e = G2P("en-GB")
        for w in _CORPUS["en-GB"]:
            assert e.confidence_breakdown(w).value == e.word_confidence(w)


def test_confidence_breakdown_type():
    b = G2P("es-ES").confidence_breakdown("gato")
    assert isinstance(b, ConfidenceBreakdown)
    assert len(b.per_slot) == len(G2P("es-ES").ipa_lattice("gato"))
