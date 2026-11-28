import re

import pytest

from orthography2ipa import G2P

SEPARATORS = [c for c in map(chr, range(0x110000)) if re.match(r"\s", c)]


@pytest.mark.parametrize("code, words", [("pt-PT", ["sim", "rui", "vem"]), ("en-GB", ["sim", "rue", "vim"]),
                                         ("es-ES", ["sin", "rui", "ven"])])
def test_every_whitespace_character_splits_words_like_a_space(code, words):
    g = G2P(code)
    spaced = g.transcribe(" ".join(words))
    assert spaced.count(" ") == len(words) - 1
    wrong = {hex(ord(s)): out for s in SEPARATORS if (out := g.transcribe(s.join(words))) != spaced}
    assert not wrong, wrong
