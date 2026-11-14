"""A word_exceptions entry hits through the punctuation that clings to a raw token.

The grapheme layer never sees a trailing comma or a leading quote, so a rule
reads past them, but the exception lookup used the raw key and missed: in
the ipa_babylm gold's raw tokens 26 of the 66 words with an en-US exception
carry punctuation (#1661). The exact key is still tried first, so an entry
spelled with a mark (Afrikaans ``'n``) keeps hitting.
"""
import pytest

from orthography2ipa import G2P


@pytest.mark.parametrize("word", ["the", "the,", "the.", "(the)", "“the", "the?”"])
def test_the_exception_hits_through_edge_punctuation(word):
    # ``the`` is a declared clitic and takes no stress mark, and the comma
    # does not change that: the clitic lookup sees past the same punctuation.
    assert G2P("en-US").transcribe_word(word) == "ðə"


def test_a_key_spelled_with_a_mark_still_hits():
    g = G2P("af")
    assert g.transcribe_word("'n").replace("ˈ", "") == g.spec.word_exceptions["'n"].replace("ˈ", "")


def test_an_elision_apostrophe_is_not_clinging_punctuation():
    # Catalan d' is the elided preposition, not ⟨d⟩ with a mark on it: the
    # bare-letter exception must not capture it.
    from orthography2ipa.g2p import _EDGE_PUNCT_RE
    assert _EDGE_PUNCT_RE.sub("", "d'") == "d'"
    assert _EDGE_PUNCT_RE.sub("", "'em") == "'em"
    assert _EDGE_PUNCT_RE.sub("", "i\u2019m,") == "i\u2019m"


def test_punctuation_alone_is_not_a_word():
    assert G2P("en-US").transcribe_word("...") == ""
