"""Pontic Greek (pnt): accented vowels and the written stress mark.

The tonos marks only the stressed syllable, so an accented vowel has the value
of pnt's own plain letter. The stress words and their stressed syllables come
from Armostis, Voniati, Drosos & Tafiadis (2020), "Trapezountian Pontic Greek
in Etoloakarnania", JIPA 52(2): the stress section (p. 337), the broad
transcription (p. 338) and the orthographic version (p. 339) of "The North
Wind and the Sun".
"""
import pytest

import orthography2ipa

VOWELS = set("aeiou")


def _pnt(word):
    return orthography2ipa.transcribe(word, "pnt")


def _vowels_after_mark(ipa):
    """The stressed syllable, counted as the vowels from the mark to the end."""
    assert ipa.count("ˈ") == 1, ipa
    return sum(c in VOWELS for c in ipa.split("ˈ", 1)[1])


# Each accented word next to the same word with the plain letter.
ACCENTED_AND_PLAIN = [
    ("καλημέρα", "καλημερα"),
    ("θάλασσα", "θαλασσα"),
    ("σπίτι", "σπιτι"),
    ("ήλιος", "ηλιος"),
    ("νερό", "νερο"),
    ("δύο", "δυο"),
    ("ώρα", "ωρα"),
    ("είναι", "ειναι"),
    ("παίζω", "παιζω"),
    ("οίκος", "οικος"),
    ("ούτε", "ουτε"),
    ("αύριο", "αυριο"),
    ("εύκολο", "ευκολο"),
    ("ΆΝΘΡΩΠΟΣ", "ανθρωπος"),
    ("ΘΆΛΑΣΣΑ", "θαλασσα"),
]


class TestAccentedVowels:

    @pytest.mark.parametrize("accented,plain", ACCENTED_AND_PLAIN)
    def test_accented_vowel_has_plain_value(self, accented, plain):
        """No vowel drops, and each accented vowel reads as its plain letter."""
        assert _pnt(accented).replace("ˈ", "") == _pnt(plain).replace("ˈ", "")

    @pytest.mark.parametrize("word,expected", [
        # Each letter has one value in the pnt table: α a, ι i, υ i, ο o,
        # τ t, ς s, π p, ρ r, ν n, ζ z, ω o. The diaeresis keeps the vowel
        # out of the digraph, so αϊ is [ai] and not αι [e].
        ("αϊτός", "aitos"),
        ("προϊόν", "proion"),
        ("ταΐζω", "taizo"),
        ("πραΰνω", "praino"),
    ])
    def test_diaeresis_vowel_stays_out_of_digraph(self, word, expected):
        assert _pnt(word).replace("ˈ", "") == expected

    @pytest.mark.parametrize("accented,plain", list(zip("άέήίόύώϊϋΐΰ",
                                                        "αεηιουωιυιυ")))
    def test_no_accented_letter_drops(self, accented, plain):
        assert (_pnt(f"τ{accented}τ").replace("ˈ", "")
                == _pnt(f"τ{plain}τ").replace("ˈ", ""))


# (orthography p. 337/339, broad transcription p. 337/338)
ARMOSTIS_2020 = [
    ("καλά", "kaˈla"),
    ("κάλλα", "ˈkala"),
    ("έστειλανεμασεν", "ˈestilanemasen"),
    ("Βορέας", "voˈreas"),
    ("ετάβιζαν", "eˈtavizan"),
    ("ποίος", "ˈpios"),
    ("δύο", "ˈðio"),
    ("δυνατότερον", "ðinaˈtoteɾon"),
    ("μπροστά", "bɾoˈsta"),
    ("ένας", "ˈenas"),
    ("Ώσταν", "ˈostan"),
    ("Ήλον", "ˈilon"),
    ("ατός", "aˈtos"),
    ("φτάει", "ˈftai"),
    ("παιδάν", "peˈðan"),
    ("εσκάλωσεν", "eˈskalosen"),
    ("γουτουρεμένα", "ɣutuɾeˈmena"),
    ("πολλά", "poˈla"),
    ("εφύσανεν", "eˈfisanen"),
    ("ετυλίουτουν", "etiˈliutun"),
    ("ενεγκάστεν", "eneˈnɡasten"),
    ("φυσά", "fiˈsa"),
    ("σειρά", "siˈɾa"),
    ("Ήλονος", "ˈilonos"),
    ("αλήγορα", "aˈliɣoɾa"),
    ("εχουλέθεν", "exuˈleθen"),
    ("έβγαλεν", "ˈevɣalen"),
    ("παραδέχεται", "paraˈðexete"),
]


class TestStress:

    @pytest.mark.parametrize("word,source", ARMOSTIS_2020)
    def test_tonos_gives_the_stressed_syllable(self, word, source):
        assert _vowels_after_mark(_pnt(word)) == _vowels_after_mark(source)

    def test_stress_contrast_kala(self):
        """καλά 'well' and κάλλα 'better' differ in stress (p. 337)."""
        assert _vowels_after_mark(_pnt("καλά")) == 1
        assert _vowels_after_mark(_pnt("κάλλα")) == 2

    @pytest.mark.xfail(strict=True, reason=(
        "the vowel run αέ is one nucleus for the mark, so the mark goes before "
        "a; el gives ˈaeɾas for αέρας in the same way"))
    def test_hiatus_before_the_accented_vowel(self):
        assert _vowels_after_mark(_pnt("αέν")) == _vowels_after_mark("aˈen")
