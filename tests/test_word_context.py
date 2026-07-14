"""WordContext — what a word can see of its neighbours.

The type survived the removal of `G2PPlugin`; the abstract base class did not.
Nothing in orthography2ipa ever discovered or called a `G2PPlugin`: the engines
that implemented it (arbtok, tugaphone) are not plugins TO this library, they are
engines built ON it. The base class asserted a relationship that did not exist.

The *type* is real — it is shared vocabulary for cross-word context, which is
what `orthography2ipa.sentence` is about, and where it now lives.
"""
from orthography2ipa import WordContext


def test_every_field_defaults():
    """An engine populates as much as it knows, and no more."""
    ctx = WordContext()
    assert ctx.prev_word is None
    assert ctx.next_word is None
    assert ctx.is_pausal is False
    assert ctx.word_index == 0
    assert ctx.word_count == 1
    assert ctx.lang is None


def test_it_carries_the_neighbours():
    ctx = WordContext(prev_word="فِي", next_word="الْبَيْت", lang="ar")
    assert ctx.prev_word == "فِي"
    assert ctx.next_word == "الْبَيْت"
    assert ctx.lang == "ar"


def test_it_is_frozen():
    """A word's context is a fact about the sentence, not a scratchpad."""
    import pytest
    ctx = WordContext()
    with pytest.raises(Exception):
        ctx.lang = "pt"


def test_it_is_importable_from_the_package_root():
    """Downstream engines import it from here; that is the whole point of keeping it."""
    import orthography2ipa
    assert orthography2ipa.WordContext is WordContext
    assert not hasattr(orthography2ipa, "G2PPlugin")
