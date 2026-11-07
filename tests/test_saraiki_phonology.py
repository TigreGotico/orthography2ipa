"""Saraiki (skr) Shahmukhi orthography — full-transcription pins.

Every expectation is a real Saraiki word whose reading follows from the
Saraiki Shahmukhi alphabet and the phonology described in Shackle (1976)
and Bashir & Conners (2019). Short vowels and gemination are unwritten in
this abjad, so they are absent from the expected forms by construction.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def skr():
    return G2P("skr")


@pytest.mark.parametrize("word,expected", [
    # ݨ (U+0768) is the Saraiki retroflex nasal letter, carrier of the
    # productive infinitive suffix -ݨ.
    ("آوݨ", "aːvɳ"),
    ("آکھݨ", "aːkʰɳ"),
    # ݙ (U+0759) is the Saraiki implosive dal, not the Sindhi ڏ.
    ("اݙݨ", "əɗɳ"),
    ("ݙاہ", "ɗaːh"),
    # The other three implosives keep their dedicated letters.
    ("اڄ", "əʄ"),
    ("ٻاوی", "ɓaːviː"),
])
def test_saraiki_letters(skr, word, expected):
    assert skr.transcribe(word) == expected


@pytest.mark.parametrize("word,expected", [
    # Word-initial ا is a bare carrier for an unwritten short vowel;
    # initial /aː/ is spelt with the madda, آ.
    ("انگل", "əŋɡl"),
    ("اسی", "əsiː"),
    ("آنا", "aːnaː"),
])
def test_initial_alef_carrier_versus_madda(skr, word, expected):
    assert skr.transcribe(word) == expected


@pytest.mark.parametrize("word,expected", [
    # After a consonant و and ی spell the long vowel...
    ("ویچݨ", "veːtʃɳ"),
    ("بھیݨ", "bʰeːɳ"),
    # ...word-finally they are /iː/ and /uː/...
    ("تریوی", "tɾiːviː"),
    # ...and in the second slot of a doubled mater they are the glide.
    ("رووݨ", "ɾoːvɳ"),
    ("دھووݨ", "dʰoːvɳ"),
    ("پیوݨ", "piːvɳ"),
    ("ٹھیک", "ʈʰeːk"),
    # Word-initial و is the consonant.
    ("ولݨ", "vlɳ"),
])
def test_mater_lectionis_positions(skr, word, expected):
    assert skr.transcribe(word) == expected


@pytest.mark.parametrize("word,expected", [
    # ر is a tap, distinct from the retroflex flap ڑ.
    ("رووݨ", "ɾoːvɳ"),
    ("تریوی", "tɾiːviː"),
])
def test_rhotic_is_a_tap(skr, word, expected):
    assert skr.transcribe(word) == expected


def test_nasal_assimilates_before_gaf(skr):
    assert skr.transcribe("انگل") == "əŋɡl"


def test_hamza_seats_are_silent(skr):
    assert skr.transcribe("سرائیکی") == "sɾaːeːkiː"


@pytest.mark.parametrize("word,expected", [
    # Guards: letters this wave does not touch keep their readings.
    ("شام", "ʃaːm"),
    ("خالص", "xaːls"),
    ("ڑ", "ɽ"),
    ("قلم", "qlm"),
])
def test_untouched_classes_are_stable(skr, word, expected):
    assert skr.transcribe(word) == expected
