"""Tests for the context-aware grapheme-token model (phonetok B1).

Validates :class:`GraphemeContext` / :class:`TokenSequence`:
- word-local neighbour access (prev/next/at/neighbors) incl. boundaries
- character spans
- phonological-class predicates delegating to vowels.py
- additivity: tokenize()/grapheme_tokens()/ipa_best() unchanged
"""
import pytest

import orthography2ipa
from orthography2ipa.phonetok import (
    GraphemeContext,
    PhonetokTokenizer,
    TokenKind,
    TokenSequence,
)
from orthography2ipa.types import LanguageSpec
from orthography2ipa.vowels import (
    is_back_vowel,
    is_front_vowel,
    is_orthographic_vowel,
)


# ═══════════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════════

@pytest.fixture
def tok_pt() -> PhonetokTokenizer:
    return PhonetokTokenizer(orthography2ipa.get("pt-PT"))


@pytest.fixture
def tok_digraph() -> PhonetokTokenizer:
    """Spec with a vowel digraph and consonant digraphs to exercise the
    leading-character predicate rule."""
    spec = LanguageSpec(
        code="tst-ctx",
        name="Test",
        family="Test",
        script="Latin",
        graphemes={
            "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
            "y": ["j"],
            "c": ["k", "s"], "g": ["g"], "n": ["n"], "s": ["s"], "t": ["t"],
            "ch": ["ʃ"], "qu": ["k"], "ai": ["aj"],
            "é": ["ɛ"], "á": ["a"], "ü": ["y"],
        },
        allophones={},
    )
    return PhonetokTokenizer(spec)


# ═══════════════════════════════════════════════════════════════════════════
# Neighbour correctness + boundaries
# ═══════════════════════════════════════════════════════════════════════════

def test_prev_next_within_word(tok_digraph):
    seq = tok_digraph.tokenize_with_context("cat")
    assert [c.grapheme for c in seq] == ["c", "a", "t"]
    c, a, t = seq[0], seq[1], seq[2]
    # first grapheme: no prev; last: no next
    assert c.prev is None
    assert c.next is a
    assert a.prev is c
    assert a.next is t
    assert t.next is None
    assert t.prev is a


def test_at_relative_offset_and_clamp(tok_digraph):
    seq = tok_digraph.tokenize_with_context("cats")
    c, a, t, s = list(seq)
    assert c.at(0) is c
    assert c.at(2) is t
    assert c.at(3) is s
    assert c.at(4) is None       # past the end -> None
    assert s.at(-3) is c
    assert s.at(-4) is None      # before the start -> None
    assert t.at(-2) is c


def test_neighbors_window_and_edge_clamp(tok_digraph):
    seq = tok_digraph.tokenize_with_context("cats")
    c, a, t, s = list(seq)
    # interior grapheme, full +/-1 window
    assert [x.grapheme for x in a.neighbors(1)] == ["c", "t"]
    # +/-2 window, ordered left-to-right, self excluded
    assert [x.grapheme for x in t.neighbors(2)] == ["c", "a", "s"]
    # word-edge grapheme returns fewer than 2n
    assert [x.grapheme for x in c.neighbors(2)] == ["a", "t"]
    assert s.neighbors(1)[0].grapheme == "t"
    assert c.neighbors(0) == []


def test_neighbours_are_word_local(tok_digraph):
    seq = tok_digraph.tokenize_with_context("cat sun")
    graphs = [c.grapheme for c in seq]
    assert graphs == ["c", "a", "t", "s", "u", "n"]
    t = seq[2]   # last grapheme of "cat"
    s = seq[3]   # first grapheme of "sun"
    # neighbours never cross the whitespace boundary
    assert t.next is None
    assert s.prev is None
    assert t.neighbors(2) == [seq[0], seq[1]]
    assert s.neighbors(1) == [seq[4]]


def test_punctuation_ends_a_word_run(tok_digraph):
    seq = tok_digraph.tokenize_with_context("ca-ni")
    # hyphen is punctuation, splitting the run
    assert [c.grapheme for c in seq] == ["c", "a", "n", "i"]
    a = seq[1]
    n = seq[2]
    assert a.next is None
    assert n.prev is None


# ═══════════════════════════════════════════════════════════════════════════
# Spans
# ═══════════════════════════════════════════════════════════════════════════

def test_span_maps_back_to_input(tok_digraph):
    text = "chai"
    seq = tok_digraph.tokenize_with_context(text)
    # maximal munch: "ch" then "ai"
    assert [c.grapheme for c in seq] == ["ch", "ai"]
    for c in seq:
        start, end = c.span
        assert text[start:end] == c.grapheme


def test_span_offsets_after_whitespace(tok_digraph):
    text = "at un"
    seq = tok_digraph.tokenize_with_context(text)
    spans = {c.grapheme: c.span for c in seq}
    assert spans["u"] == (3, 4)
    assert text[3:4] == "u"


# ═══════════════════════════════════════════════════════════════════════════
# Predicate delegation to vowels.py
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("grapheme", ["a", "e", "i", "o", "u", "é", "á", "ü", "y"])
def test_is_vowel_matches_vowels_module(tok_digraph, grapheme):
    seq = tok_digraph.tokenize_with_context(grapheme)
    c = seq[0]
    assert c.is_vowel is is_orthographic_vowel(grapheme[0])
    assert c.is_consonant is (not c.is_vowel)


@pytest.mark.parametrize("grapheme", ["e", "i", "y", "é", "ü"])
def test_front_predicate_matches_vowels_module(tok_digraph, grapheme):
    seq = tok_digraph.tokenize_with_context(grapheme)
    c = seq[0]
    assert c.is_front is is_front_vowel(grapheme[0])
    assert c.is_front is True


@pytest.mark.parametrize("grapheme", ["a", "o", "u", "á"])
def test_back_predicate_matches_vowels_module(tok_digraph, grapheme):
    seq = tok_digraph.tokenize_with_context(grapheme)
    c = seq[0]
    assert c.is_back is is_back_vowel(grapheme[0])
    assert c.is_back is True


def test_consonant_digraph_predicates(tok_digraph):
    seq = tok_digraph.tokenize_with_context("chuqu")
    ch = seq[0]
    assert ch.grapheme == "ch"
    assert ch.is_consonant is True
    assert ch.is_vowel is False
    assert ch.is_front is False


def test_vowel_digraph_classified_by_leading_char(tok_digraph):
    seq = tok_digraph.tokenize_with_context("ai")
    ai = seq[0]
    assert ai.grapheme == "ai"
    assert ai.is_vowel is True         # leading 'a' is a vowel
    assert ai.is_back is True          # 'a' is back
    assert ai.is_front is False


def test_softening_context_use_case(tok_digraph):
    """The class-predicate replacement for `next_char in 'ei'` softening."""
    seq = tok_digraph.tokenize_with_context("ce")
    c, e = seq[0], seq[1]
    # a downstream author writes: c.next.is_front  -> soft realisation
    assert c.next.is_front is True
    seq2 = tok_digraph.tokenize_with_context("ca")
    assert seq2[0].next.is_front is False
    assert seq2[0].next.is_back is True


# ═══════════════════════════════════════════════════════════════════════════
# Sequence container behaviour
# ═══════════════════════════════════════════════════════════════════════════

def test_sequence_indices_are_global(tok_digraph):
    seq = tok_digraph.tokenize_with_context("cat sun")
    assert [c.index for c in seq] == [0, 1, 2, 3, 4, 5]
    assert len(seq) == 6
    assert isinstance(seq, TokenSequence)
    assert all(isinstance(c, GraphemeContext) for c in seq)


def test_sequence_retains_full_token_stream(tok_digraph):
    seq = tok_digraph.tokenize_with_context("at un")
    kinds = [t.kind for t in seq.tokens]
    assert TokenKind.WHITESPACE in kinds
    # grapheme contexts exclude whitespace
    assert len(seq) == 4


# ═══════════════════════════════════════════════════════════════════════════
# Additivity — existing outputs must be byte-identical
# ═══════════════════════════════════════════════════════════════════════════

_CORPUS = ["chuva", "cha", "gato", "aquilo", "the cat", "peixe", "casa", "olho"]


def test_tokenize_output_unchanged(tok_pt):
    for w in _CORPUS:
        base = tok_pt.tokenize(w)
        via_ctx = tok_pt.tokenize_with_context(w).tokens
        assert base == via_ctx


def test_grapheme_tokens_and_ipa_best_unchanged(tok_pt):
    # snapshot a few known transcriptions and confirm the context layer
    # neither changes them nor is required to obtain them.
    for w in _CORPUS:
        gt_before = tok_pt.grapheme_tokens(w)
        ipa_before = tok_pt.ipa_best(w)
        seq = tok_pt.tokenize_with_context(w)  # build context view
        gt_after = tok_pt.grapheme_tokens(w)
        ipa_after = tok_pt.ipa_best(w)
        assert gt_before == gt_after
        assert ipa_before == ipa_after
        # the context view wraps exactly the grapheme tokens
        assert [c.token for c in seq] == gt_before


def test_context_wraps_same_token_objects(tok_pt):
    seq = tok_pt.tokenize_with_context("chuva")
    for c in seq:
        assert c.token.kind == TokenKind.GRAPHEME
        assert c.grapheme == c.token.grapheme
        assert c.ipa == c.token.ipa
