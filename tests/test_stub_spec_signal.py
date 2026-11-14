"""A spec with no grapheme table says so when the engine is built.

``azb`` and ``lah`` are Arabic-script stubs with zero graphemes; on dev they
transcribed كتاب to ``""`` with nothing said. The engine still builds (6219
of the 7670 registered codes are such stubs and the catalog enumerates
them), but it warns once, exposes ``is_stub``, and ``on_unmapped="raise"``
turns the per-word case into ``UnmappedScriptError``.
"""
import warnings

import pytest

from orthography2ipa import G2P
from orthography2ipa.exceptions import StubSpecWarning, UnmappedScriptError


@pytest.mark.parametrize("code", ["azb", "lah"])
def test_a_zero_grapheme_stub_warns_when_built(code):
    with pytest.warns(StubSpecWarning, match="no grapheme table"):
        g = G2P(code)
    assert g.is_stub
    assert g.transcribe("كتاب") == ""
    assert g.word_confidence("كتاب") == 0.0


@pytest.mark.parametrize("code", ["azb", "lah"])
def test_on_unmapped_raise_names_the_word(code):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", StubSpecWarning)
        g = G2P(code, on_unmapped="raise")
    with pytest.raises(UnmappedScriptError):
        g.transcribe("كتاب")


@pytest.mark.parametrize("code", ["ar", "en-US", "pt-BR"])
def test_a_spec_with_a_table_does_not_warn(code):
    with warnings.catch_warnings():
        warnings.simplefilter("error", StubSpecWarning)
        g = G2P(code)
    assert not g.is_stub
