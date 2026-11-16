"""Behaviour tests for the Ewe (``ee``) spec.

Full-transcription pins for the three phenomena the spec encodes beyond the
flat letter table — nasal vowels written with a tilde, tone written with an
accent where the orthography marks it, and the liquid ⟨r⟩ — plus guards on
the letter classes those changes must leave alone. Every pinned form is a
headword of the WikiPron ``ewe_latn_broad`` gold, read with its gold
transcription; the citations are in ``data/ee.json``'s ``notes``.
"""
import pytest

from orthography2ipa import get, transcribe


def t(word):
    return transcribe(word, "ee")


# --- nasal vowels: the tilde is part of the grapheme -------------------------

@pytest.mark.parametrize("word,ipa", [
    ("afã", "afã"),
    ("alẽ", "alẽ"),
    ("dzĩ", "d͡zĩ"),
    ("atɔ̃", "atɔ̃"),
    ("Gɛ̃", "ɡɛ̃"),
    ("ŋusẽ", "ŋusẽ"),
    ("agbalẽ", "aɡ͡balẽ"),
    ("anyĩtsi", "aɲĩt͡si"),
])
def test_tilde_marks_a_nasal_vowel(word, ipa):
    assert t(word) == ipa


def test_nasal_vowel_survives_inside_a_word():
    assert t("ʋɔnudrɔ̃la") == "βɔnudlɔ̃la"


def test_nasal_tone_combination_is_codepoint_order_agnostic():
    """Both Unicode orderings of a combined tilde+accent are ccc=230, so
    accent-then-tilde is equally canonical and must not silently drop the
    nasal tilde.
    """
    tilde_then_accent = "ã́"  # ã́
    accent_then_tilde = "á̃"  # á̃
    assert t(tilde_then_accent) == t(accent_then_tilde) == "ã́"


def test_plain_vowel_is_untouched_by_the_nasal_entries():
    """Guard: adding tilde graphemes must not nasalise a bare vowel."""
    assert t("alẽnɔ") == "alẽnɔ"
    assert t("ade") == "ade"


def test_coda_n_stays_a_consonant():
    """Guard: Ewe does not absorb a written ⟨n⟩ into the vowel here.

    The sister Gbe spec (``gun``) does; the Ewe gold writes ⟨n⟩ as a segment
    in every position, so no such rule is encoded.
    """
    assert t("wein") == "ɰein"
    assert t("nyɔnu") == "ɲɔnu"


# --- tone: carried through where the spelling marks it ----------------------

def test_written_high_tone_reaches_the_ipa():
    assert t("mí") == "mí"


def test_written_low_tone_reaches_the_ipa():
    assert t("wò") == "ɰò"


def test_unmarked_vowels_get_no_invented_tone():
    """Only the vowel the spelling accents carries a tone mark."""
    assert t("míawo") == "míaɰo"


def test_bare_spelling_is_toneless():
    assert t("aba") == "aba"


# --- the liquid ⟨r⟩ ---------------------------------------------------------

@pytest.mark.parametrize("word,ipa", [
    ("adre", "adle"),
    ("aŋutrɔ", "aŋutlɔ"),
    ("dzamatre", "d͡zamatle"),
    ("blaadre", "blaadle"),
    ("Abraham", "ablaham"),
    ("ʋɔnudrɔ̃la", "βɔnudlɔ̃la"),
])
def test_r_in_a_cluster_is_the_liquid_phoneme(word, ipa):
    assert t(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("Mars", "mars"),
    ("Hagar", "haɡar"),
    ("Yanuar", "januar"),
])
def test_r_outside_a_cluster_stays_r(word, ipa):
    assert t(word) == ipa


def test_written_l_is_never_touched():
    """Guard: the ⟨r⟩ rule is one-directional."""
    assert t("koklolã") == "koklolã"
    assert t("abable") == "abable"


# --- guards on the letter classes the change must not disturb ---------------

@pytest.mark.parametrize("word,ipa", [
    ("Eʋegbe", "eβeɡ͡be"),
    ("agbaƒuti", "aɡ͡baɸuti"),
    ("afɔkpa", "afɔk͡pa"),
    ("anyitsi", "aɲit͡si"),
    ("Dzodze", "d͡zod͡ze"),
    ("Xawa", "xaɰa"),
    ("aɖaba", "aɖaba"),
    ("ŋaneŋane", "ŋaneŋane"),
])
def test_consonant_letters_and_digraphs_unchanged(word, ipa):
    assert t(word) == ipa


def test_gamma_keeps_its_fricative_value():
    """⟨ɣ⟩ is not folded into ⟨w⟩ — see the spec notes for the gold mismatch."""
    assert t("ɣ") == "ɣ"


def test_spec_documents_its_rules():
    notes = get("ee").notes
    for key in ("NASAL VOWELS", "TONE", "LIQUID", "⟨w⟩", "⟨ɣ⟩"):
        assert key in notes
