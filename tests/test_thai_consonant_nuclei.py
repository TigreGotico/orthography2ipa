"""A bare Thai ⟨ว⟩ between an unvowelled onset and a closing consonant is the nucleus.

The expected strings are the WikiPron gold (``k r u a̯ t̚ ˨˩`` for ⟨กรวด⟩)
with the gold's offglide mark ⟨a̯⟩ written ⟨a⟩ after ⟨uː⟩, which is how
this spec already writes the open-syllable nucleus ⟨ัว⟩ (⟨ตัว⟩ /tuːa/).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest  # noqa: E402

from orthography2ipa import G2P  # noqa: E402
from orthography2ipa import registry  # noqa: E402


@pytest.fixture(scope="module")
def th():
    return G2P("th")


@pytest.mark.parametrize("word, expected", [
    ("กรวด", "kruːat̚˨˩"),
    ("ขวด", "kʰuːat̚˨˩"),
    ("รวน", "ruːan˧"),
    ("ควร", "kʰuːan˧"),
    ("กวน", "kuːan˧"),
    ("บวก", "buːak̚˨˩"),
    ("ด้วย", "duːaj˥˩"),
])
def test_bare_wo_between_consonants_is_the_nucleus(th, word, expected):
    assert th.transcribe_word(word) == expected


@pytest.mark.parametrize("word, expected", [
    ("วน", "won˧"),
    ("กังวล", "kaŋ˧won˧"),
    ("ขวา", "kʰwaː˩˩˦"),
    ("กวาง", "kwaːŋ˧"),
    ("ควาย", "kʰwaːj˧"),
    ("ตัว", "tuːa˧"),
])
def test_wo_that_is_an_onset_or_has_its_own_vowel_is_unchanged(
        th, word, expected):
    assert th.transcribe_word(word) == expected


def test_only_thai_declares_the_field():
    declared = {
        code for code in registry.available_codes()
        if registry.get(code).consonant_nuclei
    }
    assert declared == {"th"}
