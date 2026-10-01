"""Turkmen letter values that separate the 1993 Latin alphabet from Turkish.

Every assertion here is read off the orthography-to-IPA table in David Gray,
*A Short Descriptive Grammar of the Turkmen Language* (SIL-NEG, 2004), §2.2,
and the vowel-harmony and vowel-length notes in §2.3
(https://archive.org/details/032-turkmen).

The Turkish alphabet uses several of the same letters for different phonemes,
so a Turkic spec that copies Turkish letter values is wrong for Turkmen in
exactly the places these tests probe.
"""

import pytest

from orthography2ipa import G2P


def _bare(code: str, word: str) -> str:
    return G2P(code).transcribe(word).replace("ˈ", "").replace("ˌ", "")


def test_y_is_the_close_back_unrounded_vowel_not_a_glide():
    """⟨y⟩ = /ɯ/, ⟨ý⟩ = /j/ (Gray §2.2).

    Turkish assigns ⟨y⟩ to /j/; Turkmen writes that glide ⟨ý⟩ and uses plain
    ⟨y⟩ for the back unrounded vowel, "further back than the Russian ы".
    """
    assert _bare("tk", "gyz") == "ɡɯð"
    assert _bare("tk", "ýol").startswith("j")


def test_s_and_z_are_interdental_fricatives():
    """⟨s⟩ = /θ/, ⟨z⟩ = /ð/ (Gray §2.2, the Teke readings).

    Gray lists the alveolar [s z] as the Charjew-dialect variants; the Teke
    interdentals are the standard-language values and are what distinguishes
    Turkmen from the rest of Turkic.
    """
    assert _bare("tk", "asal").startswith("aθ")
    assert _bare("tk", "az") == "að"


def test_r_is_a_flap_and_doubles_to_a_trill():
    """⟨r⟩ = /ɾ/, ⟨rr⟩ = /r/ (Gray §2.2: "when there are two 'r's the flap
    becomes a trill e.g. garry")."""
    assert "ɾ" in _bare("tk", "arpa")
    assert "r" in _bare("tk", "garry")
    assert "ɾ" not in _bare("tk", "garry")


def test_g_is_a_stop_word_initially_and_a_fricative_elsewhere():
    """⟨g⟩ = [ɡ] initially, [ɣ] "mid-utterance" (Gray §2.2)."""
    assert _bare("tk", "gel").startswith("ɡ")
    assert "ɣ" in _bare("tk", "aglamak")


def test_ae_is_always_long():
    """⟨ä⟩ = /æː/ (Gray §2.3: e and ä "are always short and always long
    respectively"), the one vowel length the orthography encodes."""
    assert _bare("tk", "äri").startswith("æː")


def test_unwritten_vowel_length_is_not_predicted():
    """Length is phonemic but unwritten (Gray §2.3), so no length mark may be
    invented for a plain vowel letter: ot 'grass' and ot 'fire' are spelled
    alike and this spec must return one reading for both."""
    assert _bare("tk", "ot") == "ot"
