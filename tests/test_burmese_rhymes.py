# -*- coding: utf-8 -*-
"""Burmese (``my``) — syllable rhymes, medials and tone.

Burmese permits exactly two codas, [ʔ] and nasalisation, so a written final
consonant never surfaces as itself: every final stop letter neutralises to
[ʔ] and every final nasal letter to a nasalised rhyme, with the nucleus
shifting by the final's place. The rhyme is therefore not decomposable into
its written parts, and the spec lists it as one grapheme. Tone is
orthographic — unmarked low, ⟨့⟩ creaky, ⟨း⟩ high, or carried by the choice
of vowel sign in the open ⟨a i u⟩ series.

Sources: Watkins 2001 (*Burmese*, Illustrations of the IPA, JIPA 31(2));
Wheatley 1990 (*Burmese*, in Comrie ed., The World's Major Languages).
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def my():
    return G2P("my")


@pytest.mark.parametrize("word,ipa", [
    # Final stops all neutralise to [ʔ]; the nucleus tracks the final's place.
    ("ကက်", "kɛʔ"),      # velar final
    ("ကစ်", "kɪʔ"),      # palatal-sibilant final
    ("ကတ်", "kaʔ"),      # alveolar final
    ("ကပ်", "kaʔ"),      # labial final — same rhyme as the alveolar
    ("ကိတ်", "keɪʔ"),
    ("ကုတ်", "koʊʔ"),
    ("ကောက်", "kaʊʔ"),
    ("ကိုက်", "kaɪʔ"),
])
def test_checked_rhymes(my, word, ipa):
    assert my.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # Final nasals nasalise the rhyme instead of surfacing as a nasal.
    ("ကင်", "kɪ̀ɴ"),
    ("ကန်", "kàɴ"),
    ("ကမ်", "kàɴ"),
    ("ကံ", "kàɴ"),        # anusvara spells the same rhyme as ⟨န်⟩/⟨မ်⟩
    ("ကိန်", "kèɪɴ"),
    ("ကုန်", "kòʊɴ"),
    ("ကောင်", "kàʊɴ"),
    ("ကိုင်", "kàɪɴ"),
    ("ကွန်", "kʊ̀ɴ"),     # the ⟨ွ⟩ medial reshapes the rhyme, not just the onset
])
def test_nasal_rhymes(my, word, ipa):
    assert my.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # Tone: bare = low, ⟨့⟩ = creaky, ⟨း⟩ = high.
    ("ကန်", "kàɴ"),
    ("ကန့်", "ka̰ɴ"),
    ("ကန်း", "káɴ"),
    ("ကင်", "kɪ̀ɴ"),
    ("ကင့်", "kɪ̰ɴ"),
    ("ကင်း", "kɪ́ɴ"),
    # …and in the open series the vowel sign carries it instead.
    ("က", "ka̰"),
    ("ကာ", "kà"),
    ("ကား", "ká"),
    ("ကိ", "kḭ"),
    ("ကီ", "kì"),
    ("ကီး", "kí"),
    ("ကု", "kṵ"),
    ("ကူ", "kù"),
    ("ကူး", "kú"),
])
def test_tone_is_orthographic(my, word, ipa):
    assert my.transcribe(word) == ipa


def test_creaky_mark_precedes_the_asat(my):
    """⟨့⟩ (U+1037) sorts before the asat ⟨်⟩ (U+103A) by combining class.

    The rhyme graphemes must be spelled in that canonical order or they never
    match the text, and the creaky rhymes silently decay into a sequence of
    bare letters.
    """
    assert "ကန့်" == "ကန့်"
    assert my.transcribe("ကန့်") == "ka̰ɴ"


@pytest.mark.parametrize("word,ipa", [
    # The palatal medial affricates the velars and glides the labials.
    ("ကျ", "tɕa̰"),
    ("ကြ", "tɕa̰"),        # ⟨ျ⟩ and ⟨ြ⟩ have merged in the standard language
    ("ချ", "tɕʰa̰"),
    ("ဂျ", "dʑa̰"),
    ("မျ", "mja̰"),
    ("ပျ", "pja̰"),
    # ha-hto devoices the sonorant it attaches to.
    ("မှ", "m̥a̰"),
    ("နှ", "n̥a̰"),
    ("လှ", "l̥a̰"),
    ("ရှ", "ʃa̰"),
    # ⟨ရ⟩ has merged with ⟨ယ⟩ to /j/.
    ("ရာ", "jà"),
    ("ယာ", "jà"),
])
def test_medials_and_onsets(my, word, ipa):
    assert my.transcribe(word) == ipa


def test_nnya_rhyme_keeps_its_three_readings(my):
    """⟨ည်⟩ has no settled standard value — /ì/ ~ /è/ ~ /ɛ̀/ are all attested."""
    spec = my.spec
    assert list(spec.graphemes["ည်"]) == ["ì", "è", "ɛ̀"]


@pytest.mark.parametrize("word,ipa", [
    ("ကင်ပွန်း", "kɪ̀ɴpʊ́ɴ"),
    ("ကင်းပုံ", "kɪ́ɴpòʊɴ"),
    ("ကကတစ်", "ka̰ka̰tɪʔ"),
    ("ကျောက်", "tɕaʊʔ"),
])
def test_polysyllables(my, word, ipa):
    """Whole words, onset by onset.

    The remaining distance to a native transcription is the two things the
    orthography does not record — minor-syllable reduction (⟨ကစား⟩ is [ɡəzá],
    not [ka̰sá]) and the lexically conditioned word-internal voicing sandhi
    (⟨ကင်ပွန်း⟩ is [kɪ̀ɴbʊ́ɴ]). Neither is written, so neither is modelled.
    """
    assert my.transcribe(word) == ipa
