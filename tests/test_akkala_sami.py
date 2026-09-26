"""Akkala Sami (`sia`) — the two ways the orthography spells palatalisation.

Akkala Sami is the Kola Saami language of the Babino area; the last fluent
speaker died in 2003, so the record is elicited fieldwork. Zajkov's monograph
on the Babino dialect (Zajkov 1987) describes almost every consonant as having
a palatalised counterpart, and separates the 'soft' nasal /ń/ from the
'half-soft' /n·/ with a minimal pair from Akkala itself: mańń
'daughter-in-law' against mɛn·n· 'egg' (p. 56). For the lateral he gives only a
two-way contrast, velarised /l/ against palatalised /ĺ/; the further
opposition to a lateral palatal /ʎ/ is stated by the Kola Saami Documentation
Project (https://dobes.mpi.nl/projects/sami/language/) for Kola Saami as a
whole, and is what the gold's own counts support here.

The orthography spells palatalisation twice over: with the signs Ь and ҍ,
and with an iotated vowel letter after the consonant. Both are
grapheme-conditioned alternations, not lexical diacritics.

Expected strings are written from those descriptions plus the base letter
values in the spec's own grapheme table, never read back from the engine.
"""
import pytest

import orthography2ipa as o2i


@pytest.fixture(scope="module")
def sia():
    return o2i.G2P("sia")


def strip_stress(s):
    return s.replace("ˈ", "").replace("ˌ", "")


@pytest.mark.parametrize("spelling,segment", [
    ("рь", "rʲ"),
    ("кь", "kʲ"),
    ("вь", "vʲ"),
    ("пь", "pʲ"),
    ("мь", "mʲ"),
    ("ць", "tsʲ"),
    ("гь", "ɡʲ"),
    ("ть", "tʲ"),
])
def test_soft_sign_composes_onto_the_consonant(sia, spelling, segment):
    """Ь reads ʲ and the engine composes it onto the letter before it, so no
    consonant-plus-sign key is needed for the compositional cases."""
    assert strip_stress(sia.transcribe_word(spelling)) == segment


@pytest.mark.parametrize("spelling,segment", [
    ("ль", "ʎ"),
    ("нь", "ɲ"),
])
def test_the_two_palatal_segments_hold_keys_of_their_own(sia, spelling, segment):
    """⟨ль⟩ and ⟨нь⟩ are the lateral and nasal palatals, not the letter's value
    plus ʲ. The gold writes ⟨ль⟩ ʎ in 23 occurrences against lʲ in 7, and ⟨нь⟩
    ɲ in 2 against nʲ in 0."""
    assert strip_stress(sia.transcribe_word(spelling)) == segment


def test_semisoft_sign_stays_compositional_on_the_nasal(sia):
    """⟨нҍ⟩ is the half-soft nʲ, not the soft ɲ. Zajkov draws the contrast
    inside Akkala — mańń 'daughter-in-law' against mɛn·n· 'egg' (p. 56) — and
    the gold writes ⟨нҍ⟩ nʲ in 5 occurrences against ɲ in 0."""
    assert strip_stress(sia.transcribe_word("нҍ")) == "nʲ"
    assert strip_stress(sia.transcribe_word("нь")) != \
        strip_stress(sia.transcribe_word("нҍ"))


def test_palatalised_sibilant_is_single_focus(sia):
    """⟨сь⟩ is sʲ, not the alveolo-palatal ɕ. Zajkov's palatalised /ś/ is
    explicitly single-focus (однофокусный), opposed to the two-focus
    (двухфокусный) /š/ (p. 52), and a single-focus palatalised sibilant is sʲ.
    The gold agrees, writing sʲ in 13 occurrences and ɕ in none."""
    out = strip_stress(sia.transcribe_word("сь"))
    assert out == "sʲ"
    assert "ɕ" not in out


@pytest.mark.parametrize("spelling,expected", [
    ("няппь", "ɲɑppʲ"),
    ("Фелькь", "fʲɛʎkʲ"),
    ("тӓт", "tʲat"),
    ("вилль", "vʲiʎʎ"),
])
def test_iotated_vowel_palatalises_the_consonant_before_it(sia, spelling, expected):
    """After a consonant ⟨е ё ю я⟩ and ⟨и ӓ⟩ mark that consonant palatal and
    contribute a plain vowel; they do not add a glide.

    A written geminate stays two identical slots in the engine's output, which
    is the same string as the gold's length mark once both are normalised.
    """
    assert strip_stress(sia.transcribe_word(spelling)) == expected


@pytest.mark.parametrize("spelling,prefix", [
    ("ённ", "jo"),
    ("еййль", "jɛ"),
])
def test_the_glide_reading_survives_word_initially(sia, spelling, prefix):
    """Word-initially there is no consonant to palatalise, so the iotated
    letter keeps its glide-plus-vowel reading."""
    assert strip_stress(sia.transcribe_word(spelling)).startswith(prefix)


@pytest.mark.parametrize("spelling,segment", [
    ("а̄", "ɑː"),
    ("о̄", "oː"),
    ("э̄", "ɛː"),
    ("ы̄", "ɨː"),
    ("ӣ", "iː"),
    ("ӯ", "uː"),
])
def test_vowel_length_is_written_and_read(sia, spelling, segment):
    """Length is spelt with a combining macron on the base vowel, or with the
    dedicated letters Ӣ and Ӯ. Without these keys the macron is a character
    with no spec entry and is deleted in silence."""
    assert strip_stress(sia.transcribe_word(spelling)) == segment


@pytest.mark.parametrize("spelling,segment", [
    ("к̌", "c"),
    ("а̊", "ɔ"),
    ("ӹ", "ɪ"),
])
def test_the_three_extra_letters_carry_zajkovs_extra_phonemes(sia, spelling, segment):
    """This Cyrillic extends the Kildin conventions with three letters for
    phonemes Kildin does not spell: the palatal stop, the low back vowel and
    the high central vowel (Zajkov 1987, pp. 33, 43)."""
    assert strip_stress(sia.transcribe_word(spelling)) == segment


def test_plain_lateral_is_velarised(sia):
    """Zajkov calls the plain lateral 'переднеязычный боковой велЯризованный
    звонкий сонант' and reports it as characteristic of every Kola Saami
    dialect, occurring neither before /i/ nor next to a palatalised consonant
    (p. 56). The gold writes ɫ in 26 occurrences against plain l in 2."""
    assert "ɫ" in sia.transcribe_word("аллт")


def test_palatalisation_is_not_lexical(sia):
    """The signs are a segmental instruction, so the same base letter reads
    three ways depending only on what follows it."""
    forms = {strip_stress(sia.transcribe_word(w)) for w in ("нэ", "нҍэ", "нье")}
    assert len(forms) == 3
