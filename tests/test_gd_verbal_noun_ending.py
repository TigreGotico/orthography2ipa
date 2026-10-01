"""Scottish Gaelic ⟨adh⟩: [əɣ] at the end of a word, a hiatus vowel inside one.

The broad verbal-noun and imperfect ending ⟨-adh⟩ (⟨-eadh⟩ after a slender
consonant) keeps its fricative — Bauer (2011) gives ``glanadh`` [gLanəɣ],
``tilleadh`` [tʲiLʲəɣ] and ``bualadh`` [buəLəɣ] — while the slender endings
⟨-idh⟩, ⟨-aidh⟩ and ⟨-igh⟩ are silent, as the gold agrees: no one of its 329
rows spelled with those three endings ends in [əɣ]. Inside a word the same
spelling is a vowel in hiatus with the ⟨dh⟩ silent, ``adharc`` /ɤ.ərg/ and
``ladhar`` /Lɤ.ər/, not a fricative.
"""
from orthography2ipa import transcribe


def test_broad_verbal_noun_ending_keeps_the_fricative():
    assert transcribe("losgadh", "gd").endswith("əɣ")
    assert transcribe("fèileadh", "gd").endswith("əɣ")


def test_slender_endings_stay_silent():
    assert "ɣ" not in transcribe("pòsaidh", "gd")
    assert "ɣ" not in transcribe("nigh", "gd")


def test_non_final_adh_is_a_hiatus_vowel():
    assert transcribe("adharc", "gd") == "ˈɤəɾk"
    assert transcribe("ladhar", "gd") == "ˈl̪ˠɤəɾ"
    assert transcribe("meadhan", "gd") == "ˈmiaən"
