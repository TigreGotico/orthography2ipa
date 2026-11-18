"""The stress position on an abugida counts the inherent vowels.

An abugida writes no letter for the inherent vowel of a consonant, so the
written division of Assamese ⟨চকু⟩ [sɔku] is one syllable. The stress
position of a spec counts syllables (``StressRules.default_position``: ``1``
the first, ``2`` the second, ``-2`` the penult), so the count runs over the
syllables of the transcription.

``as`` declares no stress block. The tests give it one in memory, with only
a default position, and check where the mark lands for each position.
"""
import dataclasses

import pytest

from orthography2ipa import G2P, registry
from orthography2ipa.types import StressRules

WORDS = ("চকু", "ৰাতি", "গহনা", "বান্দৰ")


def _assamese(position: int) -> G2P:
    spec = registry.get("as")
    rules = StressRules(default_position=position)
    return G2P("as", spec=dataclasses.replace(spec, stress=rules))


@pytest.mark.parametrize("position, expected", [
    (1, ["ˈsɔku", "ˈɹati", "ˈɡɔhɔna", "ˈbandɔɹ"]),
    (2, ["sɔˈku", "ɹaˈti", "ɡɔˈhɔna", "banˈdɔɹ"]),
    (-2, ["ˈsɔku", "ˈɹati", "ɡɔˈhɔna", "ˈbandɔɹ"]),
    (-1, ["sɔˈku", "ɹaˈti", "ɡɔhɔˈna", "banˈdɔɹ"]),
])
def test_the_default_position_counts_the_inherent_vowels(position, expected):
    g = _assamese(position)
    assert [g.transcribe(word) for word in WORDS] == expected
