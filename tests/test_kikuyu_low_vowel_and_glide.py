"""Kikuyu (Gĩkũyũ, ``ki``): the low central vowel and post-consonantal ⟨w⟩.

Two facts from the Rice field-methods sketch grammar (Englebretson 2015,
Figures 2 and 4, and the diphthong discussion in the vowel chapter):

* the single low vowel, written ⟨a⟩, is the low CENTRAL /a/, not a back
  /ɑ/ — it is the only low vowel of the seven-vowel system;
* Gĩkũyũ has no consonant clusters, so an orthographic ⟨w⟩ that follows a
  consonant is not the approximant but the first vowel of a diphthong,
  pronounced like ⟨ũ⟩ = /o/. Word-initial and intervocalic ⟨w⟩ is the
  approximant.

Whole transcriptions are pinned rather than substrings: the two rules
change vowels in the middle of words, and a substring assertion would pass
on an output that got the rest of the word wrong.
"""
from orthography2ipa import G2P


def _ipa(word: str) -> str:
    return G2P("ki").transcribe_word(word)


def test_low_vowel_is_central():
    """⟨a⟩ is /a/, the low central vowel of the seven-vowel inventory."""
    assert _ipa("aka") == "aka"
    assert _ipa("atha") == "aða"


def test_no_back_low_vowel_anywhere():
    """Guard: /ɑ/ is not in the inventory, so no ⟨a⟩ may surface as one."""
    for word in ("aka", "atha", "mwaka", "watho", "ndawa", "gĩcanjama"):
        assert "ɑ" not in _ipa(word), word


def test_post_consonantal_w_is_the_close_mid_back_vowel():
    """⟨Cw⟩ is a consonant plus the diphthong-initial vowel /o/."""
    assert _ipa("mwaka") == "moaka"
    assert _ipa("mwana") == "moana"
    assert _ipa("gwata") == "ɣoata"


def test_initial_and_intervocalic_w_stay_approximant():
    """The vowel reading is confined to the post-consonantal slot."""
    assert _ipa("watho") == "waðɔ"
    assert _ipa("wendo") == "wɛⁿdɔ"
    assert _ipa("ndawa") == "ⁿdawa"


def test_seven_vowel_orthography_unchanged():
    """The tilde vowels and the prenasalised series are untouched."""
    assert _ipa("Gĩkũyũ") == "ɣekojo"
    assert _ipa("mũthũngũ") == "moðoᵑɡo"
    assert _ipa("ng'ombe") == "ŋɔᵐbɛ"
