"""Behaviour tests for the Xhosa (``xh``) spec.

The click table, the implosive/plosive ⟨b⟩–⟨bh⟩ split, post-nasal hardening,
the lateral obstruents and penultimate lengthening are all cited in the
spec's ``notes``; the sources are listed in its ``sources`` block.
"""
import pytest

from orthography2ipa import get, transcribe
from orthography2ipa.types import QualityTier


def tr(word):
    return transcribe(word, "xh")


def test_quality_and_sources():
    spec = get("xh")
    assert spec.quality is QualityTier.RESEARCH
    ids = {s.id for s in spec.sources}
    assert {"xhosa_wiki", "hyman2013_penult", "jessen_roux2002"} <= ids


# --- clicks -----------------------------------------------------------------
# Three click types x six series. Every click carries a rear velar closure, so
# the segment is the two-symbol sequence kǀ / ŋǀ, not a bare click letter.

@pytest.mark.parametrize("grapheme,ipa", [
    ("c", "kǀ"), ("ch", "kǀʰ"), ("gc", "ɡǀ"),
    ("nc", "ŋǀ"), ("ngc", "ŋǀ"), ("nkc", "ŋkǀ"),
    ("x", "kǁ"), ("xh", "kǁʰ"), ("gx", "ɡǁ"),
    ("nx", "ŋǁ"), ("ngx", "ŋǁ"), ("nkx", "ŋkǁ"),
    ("q", "kǃ"), ("qh", "kǃʰ"), ("gq", "ɡǃ"),
    ("nq", "ŋǃ"), ("ngq", "ŋǃ"), ("nkq", "ŋkǃ"),
])
def test_click_table_is_complete(grapheme, ipa):
    assert get("xh").graphemes[grapheme][0] == ipa


def test_plain_click_carries_its_velar_closure():
    """⟨caca⟩ is [kǀaːkǀa] — a bare ǀ would drop the rear articulation."""
    assert tr("caca") == "kǀaːkǀa"


def test_breathy_nasal_click_is_not_ng_plus_click():
    """⟨ingca⟩ is [iːŋǀa]: ⟨ngc⟩ is one nasal click, not ⟨ng⟩ + ⟨c⟩."""
    assert tr("ingca") == "iːŋǀa"


def test_nasal_velar_click_series():
    assert tr("nkqo") == "ŋkǃo"


# --- stops ------------------------------------------------------------------

def test_b_is_implosive_and_bh_is_the_plosive():
    assert tr("abo") == "aːɓo"
    assert tr("ibhasi") == "ibaːsi"


def test_v_is_transcribed():
    """⟨v⟩ was absent from the grapheme table and silently vanished."""
    assert tr("isilevu") == "isileːvu"
    assert "v" in tr("imvubu")


# --- palatals, laterals, dorsals -------------------------------------------

def test_palatal_stops():
    assert tr("tya") == "ca"
    assert tr("ukutya") == "ukuːca"
    assert tr("indyebo") == "iɲɟeːɓo"


def test_lateral_obstruents():
    assert tr("ihlathi") == "iɬaːtʰi"
    assert tr("indlu") == "iːndɮu"
    assert tr("intloko") == "intɬoːko"


def test_rh_is_a_velar_fricative_and_kr_a_velar_affricate():
    assert tr("urhulumente") == "uxulumeːnte"
    assert tr("ukrebe") == "ukxeːɓe"


def test_post_nasal_hardening_of_z():
    assert tr("amanzi") == "amaːndzi"


def test_nasal_is_homorganic_before_a_palatal():
    assert tr("intshonalanga") == "iɲtʃonalaːŋɡa"
    assert tr("njalo") == "ɲdʒaːlo"
    assert tr("injongo") == "iɲdʒoːŋɡo"


def test_hh_is_the_breathy_glottal():
    assert get("xh").graphemes["hh"][0] == "ɦ"
    assert get("xh").graphemes["h"][0] == "h"


# --- prosody ----------------------------------------------------------------

def test_penultimate_vowel_is_long():
    assert tr("molo") == "moːlo"
    assert tr("thina") == "tʰiːna"
    assert tr("kancinci") == "kaŋǀiːŋǀi"


def test_monosyllables_are_not_lengthened():
    """Penultimate lengthening needs a penult; ⟨fa⟩ and ⟨lo⟩ have none."""
    assert tr("fa") == "fa"
    assert tr("lo") == "lo"


@pytest.mark.parametrize("word,ipa", [
    ("moya", "moːja"),
    ("ikhaya", "ikʰaːja"),
    ("hayi", "haːji"),
    ("fuya", "fuːja"),
    ("leyo", "leːjo"),
    ("isithunywa", "isitʰuːɲʷa"),
    ("loo", "loːo"),
])
def test_length_lands_on_the_penult_across_a_glide(word, ipa):
    """⟨y⟩ and ⟨w⟩ are consonants: they open a syllable, they are not part of
    the nucleus. Counting them as vowels merges ⟨oya⟩ into one nucleus and the
    length lands on the wrong vowel, or on two at once."""
    assert tr(word) == ipa


def test_no_word_ends_in_a_long_vowel():
    """The penult is never the last syllable."""
    for word in ["molo", "moya", "loo", "hayi", "fa", "isithunywa", "caca"]:
        assert not tr(word).endswith("ː"), word


def test_no_word_carries_two_length_marks():
    for word in ["moya", "ikhaya", "loo", "isithunywa", "kancinci"]:
        assert tr(word).count("ː") <= 1, word


def test_vowel_letters_is_declared():
    assert get("xh").stress.vowel_letters == ("a", "e", "i", "o", "u")


def test_w_after_a_consonant_is_labialisation():
    assert tr("incwadi") == "iŋǀʷaːdi"
