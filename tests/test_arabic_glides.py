"""A yāʾ or wāw after its homorganic short vowel is not always a long vowel.

The ⟨ِي⟩ and ⟨ُو⟩ digraphs read as /iː/ and /uː/ only when the glide is
*quiescent* — bearing no vowel of its own. A glide before another vowel "retains
its consonantal power" and syllabifies as that vowel's onset (Wright I §4;
Watson 2002 §2.6.1: onsets are obligatory, so V.GV). The grapheme table matches
the digraph greedily and swallows the consonantal glide too, which is what made
the extremely common nisba suffixes come out wrong.
"""
import pytest

from orthography2ipa.g2p import G2P

AR = G2P("ar")


# The stress mark sits where Arabic's own onset limit puts the syllable
# boundary — one consonant opens a syllable, the rest close the previous one
# (max_onset=1, the division the spec's stress block describes): mis-rijj,
# ħur-rij-ja. It is NOT onset-maximised (*mi-srijj, *ħu-rrijja); a geminate in
# particular is split across the boundary by definition.
@pytest.mark.parametrize("word,expected,why", [
    # The nisba: a shadda doubles the yāʾ, so ⟨ِيّ⟩ is /ijj/, never /ijiː/.
    ("مِصْرِيّ", "misˤˈrijj", "nisba -iyy (Ryding 2005 §5.4.1)"),
    ("عَلِيّ", "ʕaˈlijj", "nisba -iyy"),
    # The feminine nisba ⟨ِيَّة⟩ is /ijja/.
    ("حُرِّيَّة", "ħurˈrijja", "nisba -iyya"),
    ("عَرَبِيَّة", "ʕaraˈbijja", "nisba -iyya"),
])
def test_consonantal_glide_is_not_a_long_vowel(word, expected, why):
    assert AR.transcribe(word) == expected, why


@pytest.mark.parametrize("word,expected", [
    ("فِي", "ˈfiː"),          # word-final, quiescent → genuinely long
    ("فِيهِ", "ˈfiːhi"),      # preconsonantal, quiescent → genuinely long
    ("يُصَلِّي", "juˈsˤɑlliː"),  # word-final, quiescent
    ("كِتَاب", "kiˈtaːb"),
])
def test_a_quiescent_glide_stays_a_long_vowel(word, expected):
    """The rules must fire only where the glide is consonantal."""
    assert AR.transcribe(word) == expected
