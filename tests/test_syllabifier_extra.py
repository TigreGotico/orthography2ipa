"""The bundled Portuguese syllabifier plugin.

A plugin supplies **syllables**. It must not change the transcription — because
if it did, installing an optional package would change the answer, and the same
word would have two of them depending on what happened to be in the environment.
That is the bug this library just had, and the syllable count was how it got in.
"""
import pytest

from orthography2ipa import get_syllabifier
from orthography2ipa.g2p import G2P
from orthography2ipa import registry

silabificador = pytest.importorskip("silabificador")

from orthography2ipa.syllabifiers import SilabificadorSyllabifier  # noqa: E402


def test_it_is_discovered():
    plugin = get_syllabifier("pt-PT")
    assert plugin is not None
    assert hasattr(plugin, "syllabify")


@pytest.mark.parametrize("word,expected", [
    ("coelho", ["co", "e", "lho"]),   # hiatus, not a diphthong
    ("viagem", ["vi", "a", "gem"]),
    ("mãe", ["mãe"]),                 # a real diphthong stays whole
])
def test_it_splits_hiatus(word, expected):
    assert SilabificadorSyllabifier().syllabify(word) == expected


def test_joining_the_syllables_reproduces_the_word():
    """The plugin contract: a split, not a rewrite."""
    plugin = SilabificadorSyllabifier()
    for word in ["coelho", "viagem", "paralelepípedo", "saudade", "mãe"]:
        assert "".join(plugin.syllabify(word)) == word


@pytest.mark.parametrize("word", ["coelho", "viagem", "moeda", "poeta", "espelho"])
def test_installing_it_does_not_change_the_transcription(word, monkeypatch):
    """The whole point. The bundled splitter is right on its own — pt-PT declares
    its diphthongs — so a better splitter draws better boundaries without moving
    the answer."""
    with_plugin = G2P("pt-PT-x-lisbon").transcribe_word(word)

    monkeypatch.setattr(registry, "_syllabifiers", {})
    without_plugin = G2P("pt-PT-x-lisbon").transcribe_word(word)

    assert with_plugin == without_plugin
