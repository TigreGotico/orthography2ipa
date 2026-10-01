"""Ancient Egyptian (`egy`) — the Egyptological reading convention.

The written form of Egyptian in every dictionary, corpus and gold set is the
Egyptological TRANSLITERATION of the hieroglyphs (ꜣ ꜥ j y w ḥ ḫ ẖ z š q ṯ ḏ),
and the pronunciation attached to it is the conventional reading Egyptologists
use to say the words aloud: weak consonants read as vowels, a conventional ⟨e⟩
supplied where the script writes no vowel. That convention is what `egy`
encodes, and these tests state it letter by letter.

The reconstructed phonology of the living language is a different object
(Loprieno 1995; Allen 2013): it needs vowels the orthography never wrote and
differs by stage, so no orthography→IPA map can produce it. Nothing here
asserts it.
"""
import pytest

from orthography2ipa import G2P
from orthography2ipa.types import AllophoneRule


@pytest.fixture(scope="module")
def egy():
    return G2P("egy")


@pytest.mark.parametrize("letter,ipa", [
    ("ꜣ", "ɑ"), ("ꜥ", "ɑː"), ("j", "i"), ("y", "iː"),
    ("ḥ", "h"), ("ḫ", "x"), ("ẖ", "ç"), ("š", "ʃ"),
    ("ṯ", "t͡ʃ"), ("ḏ", "d͡ʒ"), ("q", "k"), ("z", "z"),
])
def test_letter_values(egy, letter, ipa):
    """Each transliteration letter takes its conventional reading value.

    Read between two other consonants so the letter is neither word-initial
    nor word-final and no edge rule can supply the value instead.
    """
    assert ipa in egy.transcribe_word(f"b{letter}t")


def test_weak_consonants_are_read_as_vowels(egy):
    """⟨j⟩ and ⟨ꜣ⟩ are nuclei in the convention, not glides."""
    assert egy.transcribe_word("bjn") == "bin"
    assert egy.transcribe_word("bjꜣ") == "biɑ"


def test_w_is_consonantal_only_word_initially(egy):
    """⟨w⟩ opens a word as [w] and is the vowel [uː] anywhere else."""
    assert egy.transcribe_word("wbnw") == "wɛbnuː"
    assert egy.transcribe_word("bntwt") == "bɛntuːt"


def test_epenthetic_vowel_opens_a_word_initial_cluster(egy):
    """nfr is read 'nefer' — the convention's best-known example."""
    assert egy.transcribe_word("nfr") == "nɛfɛr"


def test_the_pairing_continues_to_the_third_consonant(egy):
    """A word-initial run pairs off from the left, so position three vowels too."""
    assert egy.transcribe_word("mnmnt") == "mɛnmɛnɛt"
    assert egy.transcribe_word("nḫbḫb") == "nɛxbɛxɛb"


def test_epenthetic_vowel_closes_the_final_syllable(egy):
    assert egy.transcribe_word("bḥdt") == "bɛhdɛt"
    assert egy.transcribe_word("wbnt") == "wɛbnɛt"


def test_doubled_letter_is_two_radicals_not_a_geminate(egy):
    """A doubled letter in a consonantal skeleton is two root consonants.

    ⟨bbr⟩ is the three-radical root b-b-r and the convention puts its vowel
    between the two ⟨b⟩; treating the doubling as one long segment would
    protect it from the epenthesis rule and leave an unpronounceable cluster.
    """
    assert egy.transcribe_word("bbr") == "bɛbɛr"
    assert egy.transcribe_word("gbb") == "ɡɛbɛb"
    assert egy.transcribe_word("nḥḥ") == "nɛhɛh"


def test_hiatus_between_two_weak_radicals(egy):
    """Two adjacent weak consonants keep both radicals audible."""
    assert egy.transcribe_word("ꜣꜣ") == "ɑʔɑ"
    assert egy.transcribe_word("jj") == "iʔi"


def test_a_word_of_one_consonant_takes_the_conventional_vowel(egy):
    assert egy.transcribe_word("s") == "sɛ"
    assert egy.transcribe_word("t") == "tɛ"


def test_coptic_does_not_inherit_the_reading_convention():
    """Coptic writes its own vowels; the Egyptian reading rules must not fire.

    The inheritance edge from `egy` is genealogical, and the epenthesis rules
    would otherwise insert a vowel into every Coptic onset cluster.
    """
    cop = G2P("cop")
    assert cop.transcribe_word("ⲡⲣⲱⲙⲉ") == "pɾoːmɛ"
    assert cop.transcribe_word("ⲧⲡⲉ") == "tpɛ"
    # Three- and four-consonant onsets, which the run rules reach and a
    # two-consonant onset does not.
    assert cop.transcribe_word("ⲙⲡϥⲥⲱⲧⲙ") == "mpfsoːtm"
    assert cop.transcribe_word("ⲙⲛⲧⲣⲙⲛⲕⲏⲙⲉ") == "mntɾmnkeːmɛ"


def test_append_inserts_instead_of_replacing():
    """The generic capability the epenthesis rules use.

    One rule states an insertion for a whole class of target phonemes, which
    a fixed `surface` string cannot do: it can only name one of them.
    """
    rule = AllophoneRule(id="X", phonemes=("b", "d"), append="ɛ")
    assert rule.surface == ""
    assert rule.append == "ɛ"


def test_append_and_surface_are_mutually_exclusive():
    with pytest.raises(ValueError, match="mutually exclusive"):
        AllophoneRule(id="X", phonemes=("b",), surface="p", append="ɛ")
