"""Newar (Nepal Bhasa) written in Devanagari.

Newar borrows the Devanagari script from Indo-Aryan practice without
borrowing its values, so these cases pin the readings where the two
orthographies say different things with the same letters.

Most expected strings below are gold rows from
`new_deva_narrow.tsv` with spaces stripped: they pin the fix against the
benchmark but cannot by themselves show the reading was derived from the
orthography rather than fitted to the gold. Four cases are derived
independently instead, composed by hand from the rules in the spec's
`notes` (Ishida's visarga/candrabindu/anusvara description and the
`ाय्` vowel-letter key) for words that do not occur in the gold at all:
`आः` (⟨ा⟩ is a, the visarga lengthens it to aː), `आँ` (candrabindu writes
a short nasal, so आ+candrabindu is ã), `बं` (anusvara writes a long
nasal on the inherent vowel, so ब+anusvara is bə̃ː), and `काय्` (the
`ाय्` dependent vowel is æː, so क+ाय् is kæː). Each of the four flips
from a different, wrong reading to the one above when the pre-fix
`new.json` (commit 7ac16794) is swapped in, so they are not vacuous.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def g2p():
    return G2P("new")


class TestVowelLength:
    """The ā/e/o matras are short; the visarga is the length mark."""

    @pytest.mark.parametrize("word,expected", [
        ("आलु", "alu"),          # ⟨ा⟩ alone is short a, not aː
        ("नेवाः", "newaː"),      # ⟨ाः⟩ is the long one, and ⟨े⟩ is short e
        ("कःनि", "kəːni"),       # on a bare letter the visarga lengthens ə
        ("आखः", "akʰəː"),
        # source-derived: ⟨ा⟩ is a, the visarga lengthens it to aː (not in gold)
        ("आः", "aː"),
    ])
    def test_length_is_written_with_the_visarga(self, g2p, word, expected):
        assert g2p.transcribe_word(word) == expected

    @pytest.mark.parametrize("word,expected", [
        ("हि", "hi"),            # ⟨ि⟩ is i, not a laxed ɪ
        ("आलु", "alu"),          # ⟨ु⟩ is u, not a laxed ʊ
        ("अर्थपूर्ण", "əɾtʰəpuːɾnə"),   # ⟨ू⟩ carries its own length
    ])
    def test_the_i_and_u_signs_carry_their_own_length(self, g2p, word,
                                                      expected):
        assert g2p.transcribe_word(word) == expected


class TestNasalisation:
    """Candrabindu writes a short nasal vowel, anusvara a long one."""

    @pytest.mark.parametrize("word,expected", [
        ("कुँ", "kũ"),
        ("सिँ", "sĩ"),
        ("अं", "ə̃ː"),
        ("आम्पां", "ampãː"),
        # source-derived: candrabindu writes a short nasal, so आ+candrabindu
        # is ã (not in gold)
        ("आँ", "ã"),
        # source-derived: anusvara writes a long nasal on the inherent
        # vowel, so ब+anusvara is bə̃ː (not in gold)
        ("बं", "bə̃ː"),
    ])
    def test_the_two_marks_differ_in_length(self, g2p, word, expected):
        assert g2p.transcribe_word(word) == expected


class TestYaWithVirama:
    """⟨य्⟩ spells a vowel, not a glide."""

    @pytest.mark.parametrize("word,expected", [
        ("अय्", "ɛː"),
        ("आय्", "æː"),
        ("थाय्", "tʰæː"),
        ("फय्", "pʰɛː"),
        ("कँय्", "kɛ̃ː"),
        ("घाँय्", "ɡʱæ̃ː"),
        # source-derived: the ⟨ाय्⟩ dependent vowel is æː, so क+ाय् is
        # kæː (not in gold)
        ("काय्", "kæː"),
    ])
    def test_ya_virama_is_a_vowel_letter(self, g2p, word, expected):
        assert g2p.transcribe_word(word) == expected

    def test_the_zero_width_non_joiner_spells_nothing(self, g2p):
        assert g2p.transcribe_word("अय्‌लाः") == "ɛːlaː"

    @pytest.mark.parametrize("word,expected", [
        ("मतैक्य", "mətəikjə"),   # ⟨य⟩ without the virama is still a glide
        ("घौ", "ɡʱəu"),
    ])
    def test_a_bare_ya_and_the_diphthong_signs(self, g2p, word, expected):
        assert g2p.transcribe_word(word) == expected


class TestConsonants:
    @pytest.mark.parametrize("word,expected", [
        ("चा", "t͡ɕa"),           # the affricates are alveolo-palatal
        ("खिचा", "kʰit͡ɕa"),
        ("अजा", "əd͡ʑa"),
        ("वा", "wa"),            # ⟨व⟩ is the approximant
        ("हेरा", "heɾa"),        # ⟨ह⟩ is plain h
        ("भाषा", "bʱasa"),       # one sibilant only
        ("म्हुतु", "mʱutu"),      # murmured sonorant
    ])
    def test_newar_consonant_readings(self, g2p, word, expected):
        assert g2p.transcribe_word(word) == expected


class TestInherentVowel:
    @pytest.mark.parametrize("word,expected", [
        ("अउल", "əulə"),
        ("धर्म", "dʱəɾmə"),
    ])
    def test_the_inherent_vowel_is_not_deleted(self, g2p, word, expected):
        assert g2p.transcribe_word(word) == expected
