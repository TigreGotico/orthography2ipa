"""The interpreter caches a word's result, and the cache never changes the output."""
from orthography2ipa import G2P
from orthography2ipa.ir.interpreter import Hooks


def _interpreter(code):
    return G2P(code)._interpreter


def test_a_repeated_word_gives_the_same_result_as_the_first():
    it = _interpreter("pt-PT")
    first = it.transcribe("o gato viu o gato")
    assert first.split()[1] == first.split()[4]
    assert it.transcribe("o gato viu o gato") == first
    assert ("gato", 1) in it._words


def test_a_copy_with_hooks_starts_with_an_empty_cache():
    it = _interpreter("pt-PT")
    it.transcribe("gato")
    assert not it.with_hooks(Hooks())._words
