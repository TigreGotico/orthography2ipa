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


class TestNasalBeforeGammaKappa:
    """⟨νγκ⟩ is one nasal and the stop, and the nasal takes the stop's place.

    Armostis et al. (2020: 335): "the nasal /n/ assimilates to their place of
    articulation, as mentioned above, e.g. [ˈeŋga] ένγκα 'I brought', but
    [ˈeɲɟen] ένγκεν 's/he brought'"; p. 334: [eneˈŋgasta] ενενγκάστα.
    """

    @pytest.mark.parametrize("word,source", [
        ("ένγκα", "ˈeŋɡa"),
        ("ένγκεν", "ˈeɲɟen"),
        ("ενενγκάστα", "eneˈŋɡasta"),
        ("ΕΝΓΚΑ", "ˈeŋɡa"),
    ])
    def test_armostis(self, word, source):
        assert _pnt(word) == source


class TestPalatalDorsals:
    """The dorsals are palatal before a front vowel phoneme.

    Armostis et al. (2020: 335): the velar [k g x ɣ] and the palatal
    [c ɟ ç ʝ] are in complementary distribution; "the palatals appear before
    front vowels /i e/, while velars appear everywhere else, e.g. [ˈlikon]
    λύκον 'wolf.NOM' vs. [ˈlice] λύκε 'wolf.VOC'", and [ˈçile] χείλε 'lips'.
    The narrow transcription (p. 339) has [paraˈðeçete] παραδέχεται and [ce]
    for και, where ⟨αι⟩ is the front vowel [e].
    """

    def test_lykon_against_lyke(self):
        assert (_pnt("λύκον"), _pnt("λύκε")) == ("ˈlikon", "ˈlice")

    @pytest.mark.parametrize("word,source", [
        ("χείλε", "ˈçile"),
        ("παραδέχεται", "paraˈðeçete"),
        ("ένγκεν", "ˈeɲɟen"),
    ])
    def test_armostis(self, word, source):
        assert _pnt(word) == source

    def test_digraph_front_vowel(self):
        """και is [ce] in the narrow transcription (p. 339)."""
        assert _segments("και") == "ce"


class TestNasalStopWordInitial:
    """⟨μπ ντ⟩ are [b d] at the start of a word and [mb nd] inside it.

    Armostis et al. (2020): μπαλόν’ [baˈlon], ντολμάδε [dolˈmaðe] and ζαντόν
    [zanˈdon] (p. 331); [do] ντο 'what' with "a word-initial voiced [d] with
    substantial prevoicing" (p. 332). ⟨ντζ⟩ keeps the nasal: [ˈnd͡zid͡zifa]
    ντζίτζιφα has "a fully-fledged word-initial nasal" (p. 332).
    """

    @pytest.mark.parametrize("word,source", [
        ("μπαλόν’", "balon"),
        ("ντολμάδε", "dolmaðe"),
        ("ντο", "do"),
        ("Ντο", "do"),
    ])
    def test_word_initial(self, word, source):
        assert _segments(word) == source

    def test_word_internal_keeps_the_nasal(self):
        assert (_segments("ντο"), _segments("ζαντόν")) == ("do", "zandon")

    def test_nasal_before_affricate(self):
        assert (_segments("ντο"), _segments("ντζίτζιφα")) == ("do",
                                                             "ndzidzifa")


DOT_ABOVE, DIAERESIS = "\u0307", "\u0308"


class TestUpsilonOfAuEu:
    """The υ of ⟨αυ ευ⟩ is [v] before a vowel and a soft consonant, else [f].

    Oeconomides (1908: 25, § 13): "Vor den Vocalen und den weichen
    Consonanten β, γ, δ, ζ, λ, μ, ν, ρ wird das υ des Diphthonges αυ wie β
    (= w), sonst wie φ (= f) gesprochen. Dasselbe gilt auch für ευ." The
    expected value of each word is the diphthong's value by that rule and the
    letter's value in the pnt table.
    """

    @pytest.mark.parametrize("letter,value", [
        ("κ", "k"), ("π", "p"), ("τ", "t"), ("θ", "θ"),
        ("σ", "s"), ("ξ", "ks"), ("ψ", "ps"),
    ])
    @pytest.mark.parametrize("diphthong,vowel", [("αυ", "a"), ("ευ", "e")])
    def test_voiceless_consonant(self, diphthong, vowel, letter, value):
        assert _segments(f"{diphthong}{letter}α") == f"{vowel}f{value}a"

    @pytest.mark.parametrize("word,source", [
        ("εὐχή", "efxi"),
        ("εύκολα", "efkola"),
        ("αὐτός", "aftos"),
    ])
    def test_words(self, word, source):
        """χ before ⟨η⟩ is the palatal of p. 335 in εὐχή."""
        assert _segments(word) == source.replace("xi", "çi")

    @pytest.mark.parametrize("word,source", [("ταυ", "taf"), ("τευ", "tef")])
    def test_word_final(self, word, source):
        """"sonst wie φ": no vowel and no soft consonant follows."""
        assert _segments(word) == source

    def test_soft_consonant_and_vowel_against_voiceless(self):
        soft = [_segments(f"ευ{c}α")[:2] for c in "βγδζλμνρ"]
        assert soft == ["ev"] * 8
        # Oeconomides' β̇ and δ̇ (p. 3) are β and δ with a dot.
        assert _segments(f"ευβ{DOT_ABOVE}α")[:2] == "ev"
        assert _segments(f"ευδ{DOT_ABOVE}α")[:2] == "ev"
        assert _segments("ευα")[:2] == "ev"
        assert _segments("ευτα")[:2] == "ef"


class TestOeconomidesLetters:
    """Oeconomides' own letters (1908: 2-3).

    p. 2: "α̈ = deutsches ä", "ο̈, ω̈ = deutsches ö", "α̈υ = äw", and
    "κ̇ velar. = g". p. 3: τ̇ and δ̇ = d, π̇ and β̇ = b, σ̇ and χ̇ = sch,
    ψ̇ = psch, τσ̇ = tsch, τ̇σ̇ = dsch.
    """

    @pytest.mark.parametrize("letter,value", [
        ("α" + DIAERESIS, "æ"),
        ("ο" + DIAERESIS, "ø"),
        ("ω" + DIAERESIS, "ø"),
    ])
    def test_vowel(self, letter, value):
        assert _segments(f"τ{letter}τ") == f"t{value}t"

    def test_a_umlaut_upsilon(self):
        assert _segments(f"τα{DIAERESIS}υτ")[:3] == "tæv"

    @pytest.mark.parametrize("letter,value", [
        ("κ" + DOT_ABOVE, "ɡ"),
        ("τ" + DOT_ABOVE, "d"),
        ("δ" + DOT_ABOVE, "d"),
        ("π" + DOT_ABOVE, "b"),
        ("β" + DOT_ABOVE, "b"),
        ("σ" + DOT_ABOVE, "ʃ"),
        ("χ" + DOT_ABOVE, "ʃ"),
        ("ψ" + DOT_ABOVE, "pʃ"),
        ("τσ" + DOT_ABOVE, "tʃ"),
        ("τ" + DOT_ABOVE + "σ" + DOT_ABOVE, "dʒ"),
    ])
    def test_dotted_consonant(self, letter, value):
        assert _segments(f"α{letter}α") == f"a{value}a"

    def test_dotted_kappa_stays_velar(self):
        """p. 2 writes the palatal κ̇ with a second mark, so κ̇ε is [ɡe]."""
        assert _segments(f"κ{DOT_ABOVE}ε") == "ɡe"
