"""Pontic Greek (pnt): accented vowels and the written stress mark.

The tonos marks only the stressed syllable, so an accented vowel has the value
of pnt's own plain letter. The stress words and their stressed syllables come
from Armostis, Voniati, Drosos & Tafiadis (2020), "Trapezountian Pontic Greek
in Etoloakarnania", JIPA 52(2): the stress section (p. 337), the broad
transcription (p. 338) and the orthographic version (p. 339) of "The North
Wind and the Sun".
"""
import unicodedata

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


def _segments(word):
    return _pnt(word).replace("ˈ", "")


class TestDoubledConsonantLetters:
    """A doubled consonant letter reads as one consonant.

    Oeconomides (1908), Lautlehre des Pontischen, p. 175 (addendum to p. 9):
    forms such as ἄλλο, ἄλλος "die mit Doppelkonsonant geschrieben sind, sind
    trotzdem so auszusprechen, als ob sie mit einfachem Konsonant geschrieben
    wären". Armostis et al. (2020) transcribe κάλλα [ˈkala] (p. 337) and
    πολλά [poˈla] (pp. 338-339).
    """

    @pytest.mark.parametrize("word,source", [
        ("κάλλα", "ˈkala"),
        ("πολλά", "poˈla"),
    ])
    def test_armostis_single_consonant(self, word, source):
        assert _pnt(word) == source

    @pytest.mark.parametrize("letter", list("βκλμνπρστ"))
    def test_doubled_letter_reads_as_the_single_letter(self, letter):
        assert _segments(f"α{letter}{letter}α") == _segments(f"α{letter}α")

    @pytest.mark.parametrize("doubled,single", [
        ("ἄλλο", "ἄλο"),
        ("ἄλλος", "ἄλος"),
    ])
    def test_oeconomides_forms(self, doubled, single):
        assert _segments(doubled) == _segments(single)


class TestGammaKappa:
    """⟨γκ⟩ is [ɡ] at the start of a word and [ŋɡ] inside it.

    Armostis et al. (2020): γκαρίζ’ [ɡaˈɾiz] (pp. 331, 334); the narrow
    transcription (p. 339) has [eneˈŋɡasten] ενεγκάστεν and [anaˈŋɡasten]
    αναγκάστεν, and p. 335 states that /n/ takes the place of a following
    dorsal.
    """

    @pytest.mark.parametrize("word,source", [
        ("ενεγκάστεν", "eneˈŋɡasten"),
        ("αναγκάστεν", "anaˈŋɡasten"),
    ])
    def test_word_internal(self, word, source):
        assert _pnt(word) == source

    def test_word_initial(self):
        ipa = _segments("γκαρίζ’")
        assert ipa.startswith("ɡa"), ipa
        assert "ŋ" not in ipa and "k" not in ipa, ipa


def _with(base, *marks):
    return unicodedata.normalize("NFC", base + "".join(marks))


PSILI, DASIA = "̓", "̔"
ACUTE, GRAVE, PERISPOMENI = "́", "̀", "͂"


class TestPolytonic:
    """Oeconomides (1908) writes Pontic in polytonic spelling.

    The rough breathing is no longer spoken (p. 34), the smooth breathing
    follows the etymology (p. 84), each vowel letter has one value (p. 2), and
    the accent marks the stressed syllable (p. 125).
    """

    @pytest.mark.parametrize("vowel,breathing,accent", [
        (vowel, breathing, accent)
        for vowel in "αεηιουω"
        for breathing in (PSILI, DASIA)
        for accent in ("", ACUTE, GRAVE, PERISPOMENI)
        # Greek has no ε or ο with the circumflex.
        if not (accent == PERISPOMENI and vowel in "εο")
    ])
    def test_letter_reads_as_the_plain_vowel(self, vowel, breathing, accent):
        letter = _with(vowel, breathing, accent)
        assert len(letter) == 1, letter
        assert _segments(f"τ{letter}τ") == _segments(f"τ{vowel}τ")

    @pytest.mark.parametrize("vowel", list("αηιυω"))
    def test_circumflex_without_breathing(self, vowel):
        assert _segments(f"τ{_with(vowel, PERISPOMENI)}τ") == _segments(
            f"τ{vowel}τ")

    @pytest.mark.parametrize("digraph", ["αι", "ει", "οι", "ου", "αυ", "ευ"])
    @pytest.mark.parametrize("accent", [GRAVE, PERISPOMENI])
    def test_accented_digraph_reads_as_the_plain_digraph(self, digraph, accent):
        accented = digraph[0] + _with(digraph[1], accent)
        assert _segments(f"τ{accented}τ") == _segments(f"τ{digraph}τ")

    def test_upsilon_iota_is_one_vowel(self):
        """p. 2, note: "η, ει, οι, υι wie i"; ο is o and ς is s (pp. 2-3)."""
        assert _segments("υιός") == "ios"

    @pytest.mark.parametrize("polytonic,monotonic", [
        ("ἄλλο", "άλλο"),
        ("ἔχει", "έχει"),
        ("ἔρται", "έρται"),
        ("ἄνθρωπος", "άνθρωπος"),
        ("υἱός", "υιός"),
    ])
    def test_breathing_writes_no_sound(self, polytonic, monotonic):
        assert _pnt(polytonic) == _pnt(monotonic)

    @pytest.mark.parametrize("word,plain,vowels_after", [
        # p. 125: "Der Accent wird zurückgezogen ... im Vocativ": μῶρε
        # (st. μωρὲ); in the adjectives in -ικος: Τούρκικον (st. Τουρκικὸν).
        ("μῶρε", "μωρε", 2),
        ("μωρὲ", "μωρε", 1),
        ("Τουρκικὸν", "τουρκικον", 1),
    ])
    def test_grave_and_circumflex_mark_the_stress(self, word, plain,
                                                   vowels_after):
        assert _segments(word) == _segments(plain)
        assert _vowels_after_mark(_pnt(word)) == vowels_after
