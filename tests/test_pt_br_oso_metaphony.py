"""The stressed ⟨o⟩ of the pt-BR adjective suffix ⟨-oso⟩ opens in its inflected forms.

Belando, Seara & Agostinho (2019, Gradus 4.2, p. 35), after Cavacas (1920):
the suffix has a close vowel in the masculine singular, the metaphony opens it
in the feminine ('o fenômeno metafônico se observa, portanto, na forma
feminina, tornando mais aberto o timbre da vogal tônica'), and the masculine
plural 'sofreu influência analógica das formas femininas'. The expected vowels
come from that description, not from the engine.

The close singular passes before the rules exist. It fails when
BR_SUFFIX_OSOS_OPEN loses the consonant after the final ⟨o⟩.
"""
import re

import pytest

from orthography2ipa import G2P


def stressed_vowel(word: str) -> str:
    ipa = G2P("pt-BR", expose_ambiguous_endings=False).transcribe_word(word)
    return re.search(r"ˈ[^aeiouɛɔɐɪʊ]*([aeiouɛɔɐɪʊ])", ipa).group(1)


@pytest.mark.parametrize("word", [
    "gostosa", "gostosas", "famosas", "gostosos", "caprichosos",
])
def test_inflected_suffix_is_open(word):
    assert stressed_vowel(word) == "ɔ"


@pytest.mark.parametrize("word", ["gostoso", "famoso", "caprichoso"])
def test_masculine_singular_stays_close(word):
    assert stressed_vowel(word) == "o"
