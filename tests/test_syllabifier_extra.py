"""The bundled Portuguese syllabifier plugin.

A plugin supplies **syllables**. A caller passes it to one engine, and installing
the package changes no transcription.
"""

import pytest

from orthography2ipa import Pipeline
from orthography2ipa.g2p import G2P

silabificador = pytest.importorskip("silabificador")

from orthography2ipa.syllabifiers import SilabificadorSyllabifier  # noqa: E402


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
def test_it_does_not_change_the_transcription(word):
    """The bundled splitter is right on its own — pt-PT declares its diphthongs —
    so a better splitter draws better boundaries without moving the answer."""
    pipeline = Pipeline(syllabifier=SilabificadorSyllabifier())
    with_plugin = G2P("pt-PT-x-lisbon", pipeline=pipeline).transcribe_word(word)
    without_plugin = G2P("pt-PT-x-lisbon").transcribe_word(word)

    assert with_plugin == without_plugin


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
def test_installing_it_leaves_the_stress_of_a_plain_engine(lang):
    """⟨asteríida⟩ carries its stress on the written ⟨í⟩. The package is installed
    in this test environment, and the plugin puts the stress on the ⟨i⟩ after it,
    so a plain engine that reads it fails here."""
    assert "ˈɾi" in G2P(lang).transcribe_word("asteríida")
