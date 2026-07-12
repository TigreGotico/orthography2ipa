"""Tests for the feature-export API (Workstream F1).

``G2P.features`` is a pure, additive read: it exposes o2i's per-grapheme
structure as CRF/neural-model features and must never change ``transcribe``.
These tests pin the record shape and values on a known word, determinism, the
no-op parity guarantee, JSON/CRF-consumability of ``as_dict``, and multi-word
handling.
"""
import json

import pytest

from orthography2ipa import G2P, GraphemeFeatures, WordFeatures


@pytest.fixture
def en():
    return G2P("en-GB")


def test_features_shape_on_cough(en):
    """en-GB "cough" has two grapheme slots; ⟨ough⟩ exposes its ranked
    candidates, margin and vowel class straight off the shared lattice."""
    words = en.features("cough")
    assert len(words) == 1
    wf = words[0]
    assert isinstance(wf, WordFeatures)
    assert wf.word == "cough"
    assert wf.code == "en-GB"
    assert wf.script == "Latin"
    assert len(wf.graphemes) == 2

    c, ough = wf.graphemes
    assert all(isinstance(g, GraphemeFeatures) for g in wf.graphemes)

    # Leading consonant ⟨c⟩.
    assert c.grapheme == "c"
    assert c.index == 0
    assert c.position == "initial"
    assert c.prev is None
    assert c.next == "ough"
    assert c.is_consonant is True
    assert c.is_vowel is False

    # The ambiguous vowel digraph ⟨ough⟩.
    assert ough.grapheme == "ough"
    assert ough.index == 1
    assert ough.position == "final"
    assert ough.prev == "c"
    assert ough.next is None
    assert ough.is_vowel is True
    assert ough.is_back is True
    assert ough.top1_ipa == "ɔː"
    assert ough.top1_cost == 0.0
    assert ough.n_candidates == 6
    assert ough.margin == 1.0  # cost2 (1.0) - cost1 (0.0)


def test_candidates_ranked_best_first(en):
    ough = en.features("cough")[0].graphemes[1]
    costs = [cost for _ipa, cost in ough.candidates]
    assert costs == sorted(costs)
    assert ough.candidates[0] == ("ɔː", 0.0)
    for ipa, cost in ough.candidates:
        assert isinstance(ipa, str)
        assert isinstance(cost, float)


def test_confidence_matches_word_confidence(en):
    wf = en.features("cough")[0]
    assert wf.confidence == pytest.approx(en.word_confidence("cough"))
    # Denormalised onto every grapheme record.
    for g in wf.graphemes:
        assert g.confidence == wf.confidence


def test_margin_none_for_single_candidate():
    """A slot with a single candidate has no rival, so margin is None
    (kept out of ``inf`` so ``as_dict`` stays strict-JSON safe)."""
    pt = G2P("pt-PT")
    for wf in pt.features("a"):
        for g in wf.graphemes:
            if g.n_candidates < 2:
                assert g.margin is None
            else:
                assert isinstance(g.margin, float)


def test_determinism(en):
    assert en.features("cough") == en.features("cough")


def test_features_is_a_noop_on_transcribe(en):
    """Reading features must not perturb transcribe / transcribe_detailed."""
    baseline = en.transcribe("the cough")
    baseline_detailed = en.transcribe_detailed("the cough").ipa
    en.features("the cough")
    en.features("cough")
    assert en.transcribe("the cough") == baseline
    assert en.transcribe_detailed("the cough").ipa == baseline_detailed


def test_as_dict_is_json_and_crf_consumable(en):
    """Every ``as_dict`` value is a scalar (str/int/float/bool/None), so it
    is ``json.dumps``-clean and directly a python-crfsuite item."""
    wf = en.features("cough")[0]
    scalar = (str, int, float, bool, type(None))
    for g in wf.graphemes:
        d = g.as_dict()
        assert isinstance(d, dict)
        for key, value in d.items():
            assert isinstance(key, str)
            assert isinstance(value, scalar), (key, value)
        # Round-trips through strict JSON (no inf / NaN).
        assert json.loads(json.dumps(d)) == d
    seq = wf.as_dicts()
    assert isinstance(seq, list)
    assert len(seq) == len(wf.graphemes)
    json.dumps(seq)


def test_multi_word_indices_reset_per_word(en):
    words = en.features("the cough")
    assert [w.word for w in words] == ["the", "cough"]
    for wf in words:
        assert wf.graphemes[0].index == 0
        assert wf.graphemes[0].position == "initial"
        assert wf.graphemes[-1].position == "final"
        assert [g.index for g in wf.graphemes] == list(range(len(wf.graphemes)))


def test_medial_position(en):
    """A three-plus grapheme word exposes a medial grapheme."""
    wf = en.features("cat")[0]
    positions = [g.position for g in wf.graphemes]
    assert positions[0] == "initial"
    assert positions[-1] == "final"
    assert "medial" in positions
    mid = wf.graphemes[1]
    assert mid.prev == "c"
    assert mid.next == "t"


def test_empty_text(en):
    assert en.features("") == []
    assert en.features("   ") == []
