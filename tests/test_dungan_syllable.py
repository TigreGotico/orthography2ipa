# -*- coding: utf-8 -*-
"""Dungan (``dng``) — initials, compound finals and the two conditioned series.

Dungan spells a Sinitic syllable as an initial plus a final, and the final is
a fixed letter sequence rather than a string of independent vowel and
consonant letters. The letter н is the clearest case: it never stands for a
coda /n/, and which nasal outcome it produces — a nasalised vowel or [ŋ] —
depends on the whole final, so the finals are keyed as multigraphs and win by
maximal munch.

Two initial series alternate. җ and ч are retroflex before back and apical
finals and alveolo-palatal before finals that begin with a front high vowel;
ы is an apical vowel, retroflex after the retroflex sibilants and dental
after з, ц, с. The remaining sibilants do not alternate, because щ carries
the alveolo-palatal fricative on its own.

Source: the correspondence chart in Wikipedia, "Dungan alphabets" (IPA column
attributed there to Lin Tao 2012; edition not consulted).
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def dng():
    return G2P("dng")


@pytest.mark.parametrize("word,ipa", [
    # Mandarin -n finals: the nasal is a nasalised vowel, with no [n] and no [ŋ].
    ("сан", "sæ̃"),
    ("чян", "tɕʰiæ̃"),
    ("гуан", "kuæ̃"),
    ("йүан", "yæ̃"),
    # Mandarin -ng finals: a real [ŋ], and the nucleus is not the bare vowel
    # letter's value (он is [ɑŋ], not [ɔŋ]; ын is [əŋ], not the apical vowel).
    ("вон", "vɑŋ"),
    ("бин", "piŋ"),
    ("фын", "fəŋ"),
    ("гун", "kuŋ"),
    ("гуон", "kuɑŋ"),
    ("җүн", "tɕyŋ"),
])
def test_nasal_finals_split_by_rhyme(dng, word, ipa):
    assert dng.transcribe(word) == ipa


def test_eng_letter_is_an_initial_not_a_coda(dng):
    """ң spells an initial [ŋ]; a syllable-final nasal is always spelled н.

    The chart records ң only in the syllable ңә, but the gold has ңыйлу too,
    so the letter is mapped as a general initial rather than a fixed syllable.
    """
    assert dng.transcribe("ңә") == "ŋə"
    assert dng.transcribe("ңыйлу") == "ŋeilou"


@pytest.mark.parametrize("word,ipa", [
    ("бый", "pei"),      # ый is [ei], not the apical vowel plus a glide
    ("гуй", "kuei"),
    ("хуэй", "xuei"),    # the -уэй spelling of the same final, used after х
    ("куә", "kʰuə"),
    ("щүә", "ɕyə"),
    ("хуа", "xua"),
])
def test_compound_finals_beat_their_component_letters(dng, word, ipa):
    assert dng.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # у is the nucleus [ou]; ў is [u]; a prevocalic medial u is spelled у and
    # only ever appears inside a compound final.
    ("ву", "vou"),
    ("лўфу", "lufou"),
    ("бохў", "pɔxu"),
])
def test_u_letters_are_nucleus_versus_medial(dng, word, ipa):
    assert dng.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # й is a zero initial. The on-glide of е, ё, ю, я belongs to the final, so
    # a ⟨j⟩ is never emitted for any of them.
    ("йи", "i"),
    ("йү", "y"),
    ("йинйү", "iŋy"),
    ("ще", "ɕiə"),
    ("щеҗя", "ɕiətɕia"),
    ("җю", "tɕiou"),
    ("баҗё", "patɕiɔ"),
])
def test_zero_initial_and_rising_finals(dng, word, ipa):
    assert dng.transcribe(word) == ipa
    assert "j" not in dng.transcribe(word)


@pytest.mark.parametrize("word,ipa", [
    # retroflex before back and apical finals
    ("җў", "ʈʂu"),
    ("җошы", "ʈʂɔʂʐ̩"),
    ("чў", "ʈʂʰu"),
    ("чын", "ʈʂʰəŋ"),
    ("чончын", "ʈʂʰɑŋʈʂʰəŋ"),
    # alveolo-palatal before front high finals, including the nasal ones
    ("җидан", "tɕitæ̃"),
    ("Быйҗин", "peitɕiŋ"),
    ("чи", "tɕʰi"),
    ("чютян", "tɕʰioutʰiæ̃"),
    ("дёчён", "tiɔtɕʰiɑŋ"),
])
def test_dzh_and_ch_alternate_by_following_final(dng, word, ipa):
    assert dng.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("җы", "ʈʂʐ̩"),      # apical retroflex after the retroflex series
    ("шы", "ʂʐ̩"),
    ("чы", "ʈʂʰʐ̩"),
    ("зы", "tsz̩"),      # apical dental after the dental series
    ("цы", "tsʰz̩"),
    ("сы", "sz̩"),
])
def test_apical_vowel_tracks_the_preceding_sibilant(dng, word, ipa):
    assert dng.transcribe(word) == ipa


def test_zhy_is_one_syllabic_retroflex(dng):
    """жы is a single held articulation, not [ʐ] followed by a vowel."""
    assert dng.transcribe("жы") == "ʐ̩"
    assert dng.transcribe("сынжы") == "səŋʐ̩"
    # ж elsewhere keeps its onset
    assert dng.transcribe("жын") == "ʐəŋ"
    assert dng.transcribe("гунжин") == "kuŋʐiŋ"


def test_sh_and_zh_never_palatalise(dng):
    """Only җ and ч alternate: щ already carries the alveolo-palatal fricative."""
    assert dng.transcribe("люшын") == "liouʂəŋ"
    assert dng.transcribe("гунжин") == "kuŋʐiŋ"
    assert dng.transcribe("щинщю") == "ɕiŋɕiou"


def test_tone_is_not_emitted(dng):
    """Dungan tone is lexical and unwritten; nothing in the output encodes it."""
    out = dng.transcribe("җонгуйди")
    assert out == "ʈʂɑŋkueiti"
    assert not any(c in out for c in "⁰¹²³⁴⁵˥˦˧˨˩")


def test_short_u_is_a_vowel_letter():
    """ў spells the nucleus [u], so the engine must class it as a vowel letter.

    The engine treats Cyrillic as a closed vowel inventory and refuses ⟨ў⟩ by
    name, because in Belarusian the same letter writes the glide /w/. Dungan
    uses it for a plain high back vowel — у is the nucleus [ou] and ў is [u] —
    so the spec declares it in ``vowel_graphemes`` and any positional rule
    that asks whether the following letter is a vowel gets the right answer.
    """
    from orthography2ipa import get
    from orthography2ipa.vowels import grapheme_is_vowel

    spec = get("dng")
    assert list(spec.graphemes["ў"]) == ["u"]
    assert grapheme_is_vowel("ў", list(spec.graphemes["ў"]),
                             frozenset(spec.vowel_graphemes))
