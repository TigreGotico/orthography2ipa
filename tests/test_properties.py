"""Property-based / fuzz tests for the core g2p, registry and tokenizer APIs.

Uses hypothesis to generate arbitrary unicode inputs and asserts the
totality invariants documented by each function's own contract:
  - transcribe() returns a string for any language code / text, never
    raising for well-formed inputs (only ValueError for a malformed
    ``search`` argument, which these tests never pass).
  - PhonetokTokenizer.encode/decode round-trips text built purely from
    its own known vocabulary.
  - registry.get() either resolves a spec or raises exactly KeyError;
    no other exception type is allowed to leak from internals.
"""
from __future__ import annotations

import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

import orthography2ipa
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.registry import get

_ALL_CODES = orthography2ipa.available_codes()


@pytest.mark.slow
@settings(deadline=None, max_examples=200,
          suppress_health_check=[HealthCheck.too_slow])
@given(text=st.text(max_size=50), lang=st.sampled_from(_ALL_CODES))
def test_transcribe_never_raises_on_arbitrary_unicode(text, lang):
    """transcribe() returns a string for any unicode input and lang code."""
    result = orthography2ipa.transcribe(text, lang)
    assert isinstance(result, str)


class TestTokenizerRoundTrip:
    """encode/decode round-trips text built from the tokenizer's own vocab."""

    @settings(deadline=None, max_examples=100)
    @given(data=st.data())
    def test_encode_decode_roundtrip(self, data):
        lang = data.draw(st.sampled_from(_ALL_CODES))
        spec = get(lang)
        tokenizer = PhonetokTokenizer(spec)
        graphemes = sorted(tokenizer._grapheme_ipa)
        if not graphemes:
            return
        words = data.draw(
            st.lists(st.sampled_from(graphemes), min_size=1, max_size=8))
        text = " ".join(words)

        ids = tokenizer.encode(text)
        decoded = tokenizer.decode(ids)

        assert decoded == text


class TestRegistryResolutionTotality:
    """registry.get() either succeeds or raises exactly KeyError."""

    @settings(deadline=None, max_examples=300)
    @given(code=st.text(max_size=30))
    def test_get_raises_only_keyerror(self, code):
        try:
            spec = get(code)
        except KeyError:
            return
        assert spec is not None
