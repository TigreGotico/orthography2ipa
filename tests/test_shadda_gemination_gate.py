"""A spec that declares the shadda geminates it, whatever its ``script`` label.

The dialect specs ``acq`` (script ``Zyyy``) and the Judeo-Arabic specs (script
``Hebrew``) write Arabic letters and map ``ّ`` to ``ː`` in their grapheme
tables. A letter with a vowel mark plus shadda must double the consonant, as it
does in ``ar`` (Ryding 2005, ch. 2, pp. 15-16; Watson 2002, as cited in
``ar.json``), and never lengthen the vowel. Stress is not asserted.
"""
import pytest

from orthography2ipa import registry
from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import _expands_shadda
from orthography2ipa.phonetok import _AR_SHADDA

# word, doubled consonant the shadda must produce
WORDS = (("سِتَّة", "tt"), ("قُوَّة", "uww"), ("كَتَّبَ", "tt"))
SPECS = ("acq", "aao", "ssh", "aeb-x-judeo", "jrb", "yud")


@pytest.mark.parametrize("code", SPECS)
@pytest.mark.parametrize("word, geminate", WORDS)
def test_shadda_doubles_the_consonant(code, word, geminate):
    out = G2P(code).transcribe(word)
    assert geminate in out, out
    assert "ː" not in out, out


@pytest.mark.parametrize("word, geminate", WORDS)
def test_ar_keeps_its_geminate(word, geminate):
    assert geminate in G2P("ar").transcribe(word)


def test_gate_is_the_declared_grapheme_not_the_script_label():
    scripts = {registry.get(c).script for c in SPECS}
    assert scripts - {"Arabic"}, "the affected specs must not carry script Arabic"
    for code in SPECS:
        assert _AR_SHADDA in registry.get(code).graphemes
        assert _expands_shadda(registry.get(code))


def test_a_spec_without_a_shadda_grapheme_does_not_expand():
    assert not _expands_shadda(registry.get("fa"))
