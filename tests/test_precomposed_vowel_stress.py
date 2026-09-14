# -*- coding: utf-8 -*-
"""A precomposed accented vowel is a vowel, so it can carry stress.

⟨ē⟩ and ⟨ō⟩ are /e/ and /o/ with a length mark, not new vocoids. Testing
membership against the base symbol table without decomposing them first
classified them as consonants, and a stress rule that counts syllables
counted them as none: the stress mark landed on the wrong syllable in every
language whose orthography writes a long vowel precomposed.

The languages below are the ones the fleet differential found — the stress
mark MOVES, the segments do not, which is why the committed board rows are
unchanged (the benchmark normalizer strips stress by default).
"""
import pytest

from orthography2ipa import G2P


@pytest.mark.parametrize("lang,word,ipa,rule", [
    # Livonian stress is word-initial.
    ("liv", "Dēņmō", "ˈdeːɲmoː", "initial"),
    # Silesian stress is penultimate.
    ("szl", "Gabōn", "ˈɡaboːn", "penultimate"),
    # Bahnar stress is word-final.
    ("bdq", "hơmơ̆l", "həˈməl", "final"),
])
def test_precomposed_vowel_counts_as_a_syllable(lang, word, ipa, rule):
    assert G2P(lang).transcribe(word) == ipa
