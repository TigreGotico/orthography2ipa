"""Standard Yoruba: the three level tones and the five nasal vowels.

Yoruba writes tone on the vowel — acute for high, grave for low, nothing
for mid — and writes vowel nasalisation with a following ⟨n⟩. Both are
therefore recoverable from the spelling, and the spec is expected to emit
both. The expectations below follow the standard descriptions of the
language (Bamgboṣe, A. (1966) *A Grammar of Yoruba*, Cambridge University
Press; Akinlabi, A. (2004) "Yoruba"): three level tones with mid
unmarked in the orthography, seven oral vowels /i e ɛ a ɔ o u/, and five
nasal vowels /ĩ ɛ̃ ã ɔ̃ ũ/ with no nasal counterparts of /e/ and /o/.

Every string here is NFC-normalised before comparison because a tone mark
that follows a nasalisation tilde composes differently from one that
precedes it, and only the tilde-first order is the standard notation.
"""
import unicodedata

import pytest

from orthography2ipa.g2p import G2P


@pytest.fixture(scope="module")
def yo():
    return G2P("yo")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def say(yo, word):
    return nfc(yo.transcribe_word(word))


# ── Tone is emitted, and mid is a mark of its own ─────────────────────
# The classic minimal triple on ⟨ọkọ⟩: mid-mid "hoe", mid-low "vehicle",
# low-low "spear". A transcription that drops tone collapses all three.
@pytest.mark.parametrize("word,expected", [
    ("ọkọ", "ɔ̄kɔ̄"),
    ("ọkọ̀", "ɔ̄kɔ̀"),
    ("ọ̀kọ̀", "ɔ̀kɔ̀"),
])
def test_tone_is_emitted_on_every_vowel(yo, word, expected):
    assert say(yo, word) == nfc(expected)


def test_the_three_okọ_readings_stay_distinct(yo):
    forms = {say(yo, w) for w in ("ọkọ", "ọkọ̀", "ọ̀kọ̀")}
    assert len(forms) == 3


@pytest.mark.parametrize("word,expected", [
    ("bá", "bá"), ("bà", "bà"), ("ba", "bā"),
    ("dé", "dé"), ("dè", "dè"), ("de", "dē"),
    ("ẹ́", "ɛ́"), ("ẹ̀", "ɛ̀"), ("ẹ", "ɛ̄"),
])
def test_each_tone_mark_maps_to_its_own_ipa_diacritic(yo, word, expected):
    assert say(yo, word) == nfc(expected)


def test_an_unmarked_vowel_is_mid_not_toneless(yo):
    """Mid is a specified tone, so ⟨ba⟩ is /bā/, never bare /ba/."""
    assert say(yo, "ba") != "ba"


# ── Nasal vowels ──────────────────────────────────────────────────────
# ⟨n⟩ after a nasalisable vowel, not itself before a vowel, spells
# nasalisation of that vowel and is not a consonant of its own.
@pytest.mark.parametrize("word,expected", [
    ("Abiọdun", "ābīɔ̄dũ̄"),
    ("Agbaakin", "āɡ͡bāākĩ̄"),
    ("Adediran", "ādēdīɾã̄"),
    ("Agbọnmiregun", "āɡ͡bɔ̃̄mīɾēɡũ̄"),
])
def test_final_n_nasalises_the_vowel(yo, word, expected):
    assert say(yo, word) == nfc(expected)


@pytest.mark.parametrize("word", ["Abiọdun", "Agbaakin", "Adediran"])
def test_the_nasalising_n_is_not_a_separate_consonant(yo, word):
    assert not say(yo, word).endswith("n")


@pytest.mark.parametrize("word,expected", [
    ("ana", "ānā"),
    ("ẹni", "ɛ̄nī"),
    ("Aarinọla", "āāɾīnɔ̄lā"),
])
def test_n_before_a_vowel_stays_an_onset(yo, word, expected):
    """The before_vowel positional override: ⟨ana⟩ is /ānā/, not */ãā/."""
    out = say(yo, word)
    assert out == nfc(expected)
    assert "̃" not in unicodedata.normalize("NFD", out)


@pytest.mark.parametrize("word", ["kenbu", "onta"])
def test_e_and_o_have_no_nasal_counterpart(yo, word):
    """Yoruba nasalises only /i ɛ a ɔ u/; ⟨en⟩ and ⟨on⟩ are not nasal
    vowel spellings, so the ⟨n⟩ must survive as a consonant."""
    assert "n" in say(yo, word)
    assert "̃" not in unicodedata.normalize("NFD", say(yo, word))


# ── Notation order: tilde before tone ─────────────────────────────────
@pytest.mark.parametrize("word,expected", [
    ("ún", "ṹ"),
    ("ùn", "ũ̀"),
    ("un", "ũ̄"),
    ("ín", "ĩ́"),
    ("ọ́n", "ɔ̃́"),
    ("ẹ̀n", "ɛ̃̀"),
])
def test_nasal_and_tone_compose_in_the_standard_order(yo, word, expected):
    assert say(yo, word) == nfc(expected)


def test_tilde_precedes_the_tone_mark(yo):
    """u + tilde + acute composes to ṹ; the reverse order does not."""
    decomposed = unicodedata.normalize("NFD", say(yo, "ún"))
    assert decomposed.index("̃") < decomposed.index("́")
