"""Tests for the structured IPA lattice API (:meth:`ipa_lattice`).

The lattice is the per-position ranked view of the beam: one
:class:`SegmentSlot` per grapheme, each carrying ranked
``Candidate(ipa, cost)`` options. These tests pin the four load-bearing
contracts:

* **structure** — slots are in surface order, spans reconstruct the
  grapheme per the B1 NFC/casefold contract, and concatenating each
  slot's top candidate reproduces ``ipa_best``;
* **costs** — real ``-log P`` for a weighted spec, rank cost for a plain
  spec, and a path's total score is the sum of its chosen per-slot costs;
* **positional** — positional overrides apply in the lattice (es-ES
  ``cena`` → θ) via the shared resolver;
* **scoring knobs** — ``length_norm``/``diversity`` are opt-in and OFF by
  default reproduce the current beam ordering byte-for-byte.
"""
import math
import unicodedata

import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.phonetok import (
    Candidate,
    PhonetokTokenizer,
    SegmentSlot,
)


# ─── Slot structure ────────────────────────────────────────────────────

def test_slots_are_in_surface_order():
    tok = PhonetokTokenizer(get("es-ES"))
    slots = tok.ipa_lattice("cena")
    assert [s.grapheme for s in slots] == ["c", "e", "n", "a"]


def test_spans_reconstruct_grapheme_per_b1_contract():
    # Upper-case + a non-grapheme separator: the span contract is defined
    # against the NFC-normalised, case-folded text, not the raw string.
    text = "Cena Azul"
    tok = PhonetokTokenizer(get("es-ES"))
    nfc = unicodedata.normalize("NFC", text)
    for slot in tok.ipa_lattice(text):
        start, end = slot.span
        assert nfc[start:end].lower() == slot.grapheme


def test_non_grapheme_tokens_produce_no_slot():
    tok = PhonetokTokenizer(get("es-ES"))
    # Two words + whitespace: only the 8 graphemes get slots.
    slots = tok.ipa_lattice("cena azul")
    assert [s.grapheme for s in slots] == list("cena") + list("azul")


def test_top_of_each_slot_concatenates_to_ipa_best():
    tok = PhonetokTokenizer(get("en-GB"))
    for word in ["weather", "cough", "through", "the", "thought"]:
        slots = tok.ipa_lattice(word)
        concat = "".join(s.top.ipa for s in slots)
        assert concat == tok.ipa_best(word), word


def test_slot_and_candidate_types():
    tok = PhonetokTokenizer(get("en-GB"))
    slots = tok.ipa_lattice("the")
    assert all(isinstance(s, SegmentSlot) for s in slots)
    assert all(isinstance(c, Candidate)
               for s in slots for c in s.candidates)
    # Candidates ranked best (lowest cost) first; top == candidates[0].
    for s in slots:
        costs = [c.cost for c in s.candidates]
        assert costs == sorted(costs)
        assert s.top is s.candidates[0]


def test_beam_width_truncates_candidates_but_keeps_top():
    tok = PhonetokTokenizer(get("en-GB"))
    full = tok.ipa_lattice("weather", beam_width=-1)
    narrow = tok.ipa_lattice("weather", beam_width=1)
    for f, n in zip(full, narrow):
        assert len(n.candidates) == 1
        assert n.candidates[0] == f.candidates[0]


# ─── Costs are real −log P / rank cost ─────────────────────────────────

def test_weighted_spec_costs_are_neg_log_p():
    # en-GB declares weights for er (0.2, 0.8) and gh (0.03, 0.12, 0.85).
    tok = PhonetokTokenizer(get("en-GB"))
    lattice = {s.grapheme: s for s in tok.ipa_lattice("gher")}

    er = lattice["er"]
    # weights normalise to themselves (sum 1.0): əɹ=0.8, ɜːɹ=0.2.
    by_ipa = {c.ipa: c.cost for c in er.candidates}
    assert by_ipa["əɹ"] == pytest.approx(-math.log(0.8))
    assert by_ipa["ɜːɹ"] == pytest.approx(-math.log(0.2))

    gh = lattice["gh"]
    by_ipa = {c.ipa: c.cost for c in gh.candidates}
    assert by_ipa[""] == pytest.approx(-math.log(0.85))
    assert by_ipa["f"] == pytest.approx(-math.log(0.12))
    assert by_ipa["ɡ"] == pytest.approx(-math.log(0.03))


def test_plain_spec_costs_are_rank_cost():
    # es-ES 'e' is a plain list [e, ɛ]: rank cost 0.0, 1.0.
    tok = PhonetokTokenizer(get("es-ES"))
    e_slot = next(s for s in tok.ipa_lattice("cena") if s.grapheme == "e")
    assert [c.cost for c in e_slot.candidates] == [0.0, 1.0]


def test_path_total_score_equals_sum_of_chosen_slot_costs():
    tok = PhonetokTokenizer(get("en-GB"))
    word = "gher"
    slots = tok.ipa_lattice(word)
    # The best path picks the top of each slot; its cost is the sum.
    best_path = tok.ipa_beam(word, beam_width=1)[0]
    assert best_path.score == pytest.approx(
        sum(s.top.cost for s in slots))
    assert best_path.ipa == "".join(s.top.ipa for s in slots)


# ─── Positional slots (B2 in the lattice) ──────────────────────────────

def test_positional_softening_applies_in_lattice_es_cena():
    # c before a front vowel (e) softens to θ in es-ES — the positional
    # override must fire in the lattice, not just the full engine.
    tok = PhonetokTokenizer(get("es-ES"))
    c_slot = next(s for s in tok.ipa_lattice("cena") if s.grapheme == "c")
    assert c_slot.top.ipa == "θ"
    # And before a back vowel it stays /k/.
    c_slot = next(s for s in tok.ipa_lattice("casa") if s.grapheme == "c")
    assert c_slot.top.ipa == "k"


def test_engine_lattice_also_softens_cena():
    g = G2P("es-ES")
    c_slot = next(s for s in g.ipa_lattice("cena") if s.grapheme == "c")
    assert c_slot.top.ipa == "θ"


def test_engine_lattice_top_matches_positional_best():
    # Concatenating engine slot tops == the engine's pre-stress positional
    # best (transcribe_word only adds stress marks on top).
    g = G2P("es-ES")
    slots = g.ipa_lattice("cena")
    concat = "".join(s.top.ipa for s in slots)
    stripped = g.transcribe_word("cena").replace("ˈ", "").replace("ˌ", "")
    assert concat == stripped


# ─── length_norm / diversity are opt-in ────────────────────────────────

@pytest.mark.parametrize("word", ["weather", "through", "thought"])
def test_default_beam_order_unchanged_by_new_params(word):
    tok = PhonetokTokenizer(get("en-GB"))
    base = tok.ipa_beam(word, beam_width=8)
    explicit_off = tok.ipa_beam(
        word, beam_width=8, length_norm=False, diversity=0.0)
    assert [p.ipa for p in base] == [p.ipa for p in explicit_off]
    assert [p.score for p in base] == [p.score for p in explicit_off]


def test_length_norm_divides_score_by_segment_count():
    tok = PhonetokTokenizer(get("en-GB"))
    base = tok.ipa_beam("weather", beam_width=8)
    norm = tok.ipa_beam("weather", beam_width=8, length_norm=True)
    n = len(base[0].segments)  # every path shares this count
    # Same order (single word → equal lengths), scores scaled by 1/n.
    assert [p.ipa for p in norm] == [p.ipa for p in base]
    for b, m in zip(base, norm):
        assert m.score == pytest.approx(b.score / n)


def test_diversity_demotes_near_duplicates_of_top():
    tok = PhonetokTokenizer(get("en-GB"))
    base = tok.ipa_beam("weather", beam_width=8)
    div = tok.ipa_beam("weather", beam_width=8, diversity=5.0)
    # Top-1 never changes.
    assert div[0].ipa == base[0].ipa
    # A strong diversity penalty pushes a path differing from the top in
    # two positions ahead of the single-segment near-duplicates.
    def n_diff(ipa):
        segs = next(p.segments for p in base if p.ipa == ipa)
        top = base[0].segments
        return sum(1 for a, b in zip(segs, top) if a != b)
    assert n_diff(base[1].ipa) == 1          # baseline: nearest neighbour
    assert n_diff(div[1].ipa) >= 2           # diversified: more different
    # The result is a permutation of the same path set.
    assert sorted(p.ipa for p in div) == sorted(p.ipa for p in base)


def test_ipa_best_still_matches_default_beam_head():
    # Guard: the additive lattice/scoring work must not perturb ipa_best.
    tok = PhonetokTokenizer(get("en-GB"))
    for word in ["weather", "the", "cough"]:
        assert tok.ipa_best(word) == tok.ipa_beam(word, beam_width=1)[0].ipa
