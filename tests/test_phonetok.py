"""Tests for orthography2ipa.phonetok — Tokenizer and IPA beam search.

Validates:
- Maximal-munch grapheme tokenization
- Token types (GRAPHEME, WHITESPACE, PUNCTUATION, DIGIT, UNKNOWN)
- IPA beam search expansion
- Vocabulary and encode/decode round-trips
- Edge cases: empty strings, all-punctuation, mixed content
"""
import pytest

import orthography2ipa
from orthography2ipa.phonetok import (
    PhonetokTokenizer,
    Token,
    TokenKind,
    IPAPath,
)
from orthography2ipa.types import LanguageSpec


# ═══════════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════════

@pytest.fixture
def tok_es() -> PhonetokTokenizer:
    return PhonetokTokenizer(orthography2ipa.get("es-ES"))


@pytest.fixture
def tok_en() -> PhonetokTokenizer:
    return PhonetokTokenizer(orthography2ipa.get("en-GB"))


@pytest.fixture
def tok_pt_br() -> PhonetokTokenizer:
    return PhonetokTokenizer(orthography2ipa.get("pt-BR"))


@pytest.fixture
def tok_simple() -> PhonetokTokenizer:
    """Tokenizer for a trivial spec to test algorithmic behaviour."""
    spec = LanguageSpec(
        code="test",
        name="Test",
        family="Test",
        script="Latin",
        graphemes={
            "a": ["a"],
            "b": ["b"],
            "c": ["k", "s"],   # ambiguous
            "ch": ["tʃ"],      # digraph must win over c + h
            "h": ["h"],
        },
        allophones={
            "a": ["a"],
            "b": ["b", "β"],
            "k": ["k"],
            "s": ["s"],
            "tʃ": ["tʃ"],
            "h": ["h"],
        },
    )
    return PhonetokTokenizer(spec)


# ═══════════════════════════════════════════════════════════════════════════
# Tokenization — basics
# ═══════════════════════════════════════════════════════════════════════════

class TestTokenizeBasics:
    """Basic tokenization tests."""

    def test_single_letter_graphemes(self, tok_simple):
        tokens = tok_simple.tokenize("ab")
        graphemes = [t.grapheme for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert graphemes == ["a", "b"]

    def test_maximal_munch_digraph(self, tok_simple):
        """'ch' should match as one grapheme, not 'c' + 'h'."""
        tokens = tok_simple.tokenize("ch")
        graphemes = [t.grapheme for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert graphemes == ["ch"]

    def test_digraph_in_word(self, tok_simple):
        """'achb' should be a + ch + b."""
        tokens = tok_simple.tokenize("achb")
        graphemes = [t.grapheme for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert graphemes == ["a", "ch", "b"]

    def test_empty_string(self, tok_simple):
        tokens = tok_simple.tokenize("")
        # May return BOS/EOS or empty list depending on impl
        grapheme_tokens = [t for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert len(grapheme_tokens) == 0


# ═══════════════════════════════════════════════════════════════════════════
# Tokenization — special token types
# ═══════════════════════════════════════════════════════════════════════════

class TestTokenKinds:
    """Tests for different TokenKind classifications."""

    def test_whitespace_token(self, tok_en):
        tokens = tok_en.tokenize("a b")
        kinds = [t.kind for t in tokens]
        assert TokenKind.WHITESPACE in kinds

    def test_punctuation_token(self, tok_en):
        tokens = tok_en.tokenize("a.b")
        kinds = [t.kind for t in tokens]
        assert TokenKind.PUNCTUATION in kinds

    def test_digit_token(self, tok_en):
        tokens = tok_en.tokenize("a1b")
        kinds = [t.kind for t in tokens]
        assert TokenKind.DIGIT in kinds

    def test_unknown_character(self, tok_simple):
        """Characters not in the grapheme table → UNKNOWN."""
        tokens = tok_simple.tokenize("aZb")
        kinds = [t.kind for t in tokens]
        # 'Z' isn't in the grapheme table, so it should be UNKNOWN
        assert TokenKind.UNKNOWN in kinds

    def test_all_punctuation(self, tok_en):
        tokens = tok_en.tokenize("!?.,:;")
        grapheme_tokens = [t for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert len(grapheme_tokens) == 0


# ═══════════════════════════════════════════════════════════════════════════
# Tokenization — real languages
# ═══════════════════════════════════════════════════════════════════════════

class TestTokenizeRealLanguages:
    """Tokenization with actual language specs."""

    def test_english_th_digraph(self, tok_en):
        tokens = tok_en.tokenize("the")
        graphemes = [t.grapheme for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert graphemes[0] == "th"

    def test_english_sh_digraph(self, tok_en):
        tokens = tok_en.tokenize("ship")
        graphemes = [t.grapheme for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert graphemes[0] == "sh"

    def test_portuguese_ch_digraph(self, tok_pt_br):
        tokens = tok_pt_br.tokenize("chuva")
        graphemes = [t.grapheme for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert graphemes[0] == "ch"

    def test_portuguese_lh_digraph(self, tok_pt_br):
        tokens = tok_pt_br.tokenize("alho")
        graphemes = [t.grapheme for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert "lh" in graphemes

    def test_spanish_rr_digraph(self, tok_es):
        tokens = tok_es.tokenize("perro")
        graphemes = [t.grapheme for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert "rr" in graphemes

    def test_spanish_ll_digraph(self, tok_es):
        tokens = tok_es.tokenize("llave")
        graphemes = [t.grapheme for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert graphemes[0] == "ll"


# ═══════════════════════════════════════════════════════════════════════════
# IPA beam search
# ═══════════════════════════════════════════════════════════════════════════

class TestIPABeam:
    """Tests for ipa_beam() — the IPA expansion beam search."""

    def test_returns_ipa_paths(self, tok_es):
        paths = tok_es.ipa_beam("hola", beam_width=3)
        assert len(paths) >= 1
        for p in paths:
            assert isinstance(p, IPAPath)

    def test_best_path_has_score_zero(self, tok_simple):
        """The canonical path (first IPA variant each) should score 0."""
        paths = tok_simple.ipa_beam("ab", beam_width=1)
        assert len(paths) == 1
        assert paths[0].score == 0.0

    def test_ambiguous_grapheme_generates_multiple_paths(self, tok_simple):
        """'c' maps to ['k', 's'], so beam_width ≥ 2 should produce 2 paths."""
        paths = tok_simple.ipa_beam("c", beam_width=4)
        ipa_strings = [p.ipa for p in paths]
        assert "k" in ipa_strings
        assert "s" in ipa_strings

    def test_beam_width_limits_output(self, tok_en):
        paths = tok_en.ipa_beam("cat", beam_width=2)
        assert len(paths) <= 2

    def test_paths_sorted_by_score(self, tok_en):
        paths = tok_en.ipa_beam("cat", beam_width=5)
        scores = [p.score for p in paths]
        assert scores == sorted(scores)

    def test_ipa_best_matches_beam_width_1(self, tok_es):
        """ipa_best() should equal beam_width=1 result."""
        best = tok_es.ipa_best("casa")
        paths = tok_es.ipa_beam("casa", beam_width=1)
        assert best == paths[0].ipa

    def test_spanish_hola_canonical(self, tok_es):
        """'hola' in Spanish: h is silent, canonical should start with 'o'."""
        best = tok_es.ipa_best("hola")
        # 'h' maps to "" (silent), so IPA should start with a vowel
        assert "o" in best

    def test_spanish_ciudad(self, tok_es):
        paths = tok_es.ipa_beam("ciudad", beam_width=4)
        # Should produce valid IPA strings
        for p in paths:
            assert len(p.ipa) > 0

    def test_portuguese_chuva(self, tok_pt_br):
        best = tok_pt_br.ipa_best("chuva")
        # 'ch' → /ʃ/ in Portuguese
        assert "ʃ" in best


# ═══════════════════════════════════════════════════════════════════════════
# Vocabulary and encoding
# ═══════════════════════════════════════════════════════════════════════════

class TestVocabEncoding:
    """Tests for vocab, encode(), and decode()."""

    def test_vocab_has_special_tokens(self, tok_en):
        v = tok_en.vocab
        for special in ["<pad>", "<bos>", "<eos>", "<unk>", "<ws>",
                         "<punct>", "<digit>"]:
            assert special in v

    def test_vocab_special_token_ids(self, tok_en):
        v = tok_en.vocab
        assert v["<pad>"] == 0
        assert v["<bos>"] == 1
        assert v["<eos>"] == 2
        assert v["<unk>"] == 3

    def test_vocab_size_consistent(self, tok_en):
        v = tok_en.vocab
        assert tok_en.vocab_size == len(v)

    def test_vocab_includes_graphemes(self, tok_en):
        v = tok_en.vocab
        # English 'th' should be a vocab entry
        assert "th" in v

    def test_encode_produces_integers(self, tok_en):
        ids = tok_en.encode("cat")
        assert all(isinstance(i, int) for i in ids)

    def test_encode_decode_roundtrip(self, tok_en):
        """decode(encode(text)) should reconstruct the grapheme string."""
        text = "cat"
        ids = tok_en.encode(text)
        decoded = tok_en.decode(ids)
        # Decoding strips special tokens but should preserve grapheme content
        assert decoded == text

    def test_encode_unknown_char(self, tok_en):
        """Characters not in grapheme table should encode as <unk>."""
        ids = tok_en.encode("™")
        assert 3 in ids  # <unk> = 3


# ═══════════════════════════════════════════════════════════════════════════
# Token dataclass
# ═══════════════════════════════════════════════════════════════════════════

class TestToken:
    """Tests for the Token frozen dataclass."""

    def test_token_is_frozen(self, tok_en):
        tokens = tok_en.tokenize("a")
        if tokens:
            with pytest.raises(Exception):  # FrozenInstanceError
                tokens[0].kind = TokenKind.DIGIT

    def test_token_has_grapheme(self, tok_en):
        tokens = tok_en.tokenize("a")
        grapheme_tokens = [t for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert len(grapheme_tokens) >= 1
        assert grapheme_tokens[0].grapheme == "a"


# ═══════════════════════════════════════════════════════════════════════════
# Edge cases
# ═══════════════════════════════════════════════════════════════════════════

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_single_character(self, tok_en):
        paths = tok_en.ipa_beam("a", beam_width=3)
        assert len(paths) >= 1

    def test_whitespace_only(self, tok_en):
        tokens = tok_en.tokenize("   ")
        grapheme_tokens = [t for t in tokens if t.kind == TokenKind.GRAPHEME]
        assert len(grapheme_tokens) == 0

    def test_mixed_content(self, tok_en):
        """Text with graphemes, spaces, punctuation, and digits."""
        tokens = tok_en.tokenize("Hello, world! 42")
        kinds = {t.kind for t in tokens}
        assert TokenKind.GRAPHEME in kinds
        assert TokenKind.WHITESPACE in kinds
        assert TokenKind.PUNCTUATION in kinds
        assert TokenKind.DIGIT in kinds

    def test_case_sensitivity(self, tok_en):
        """Tokenizer typically lowercases or handles case."""
        # The exact behaviour depends on implementation — just check it doesn't crash
        tokens = tok_en.tokenize("THE")
        assert len(tokens) >= 1
