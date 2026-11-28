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


@pytest.mark.parametrize("word, before", [
    ("imkân", "im"),
    ("derhâl", "deɾ"),
    ("kalbî", "kal"),
    ("mahkûm", "mah"),
    ("cüretkâr", "dʒyɾet"),
])
def test_a_dropped_vowel_letter_keeps_its_syllable_for_the_mark(word, before):
    # tr has no grapheme for ⟨â î û⟩ and drops the vowel; this checks only
    # where the mark goes. tr stress is word-final, so the mark opens the
    # last written syllable and a coda of the syllable before stays outside
    # it. *before* is the WikiPron (tur) transcription of the syllables
    # before the last: [imcɑːn], [deɾhal], [kalbiː], [mahcum], [dʒyɾetcaːɾ].
    out = G2P("tr").transcribe(word)
    assert out.count("ˈ") == 1 and out.split("ˈ")[0] == before


@pytest.mark.parametrize("word, after", [("kâtip", "tip"), ("kâse", "se")])
def test_a_first_syllable_without_its_vowel_still_counts(word, after):
    # The same gap in the first syllable: the mark still opens the last
    # written syllable. *after* is the WikiPron (tur) transcription of that
    # syllable: [caːtip], [cɑːse].
    out = G2P("tr").transcribe(word)
    assert out.count("ˈ") == 1 and out.split("ˈ")[1] == after
