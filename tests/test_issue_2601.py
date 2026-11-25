"""A Basque word with an acute vowel keeps that vowel, and no grapheme goes unmapped.

Basque text carries ⟨á é í ó ú⟩ in Spanish and French names and in Souletin
forms written with a stress acute. The acute marks stress and does not change
the vowel, so ⟨kát⟩ reads like ⟨kat⟩.
"""
import warnings

import pytest

from orthography2ipa import transcribe
from orthography2ipa.exceptions import UnmappedGraphemeWarning

ACUTE_TO_BASE = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}


@pytest.mark.xfail(
    strict=True,
    reason="https://github.com/TigreGotico/orthography2ipa/issues/2601")
@pytest.mark.parametrize("acute, base", ACUTE_TO_BASE.items())
def test_acute_vowel_is_mapped_and_kept(acute, base):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        ipa = transcribe(f"k{acute}t", "eu")
    assert not [w for w in caught if issubclass(w.category, UnmappedGraphemeWarning)]
    assert base in ipa
