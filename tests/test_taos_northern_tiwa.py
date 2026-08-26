# -*- coding: utf-8 -*-
"""Taos (``twf``, Northern Tiwa, Kiowa-Tanoan) — Trager's practical orthography.

Taos is written in the Americanist orthography of Trager (1948), whose
letters routinely disagree with their IPA namesakes: ⟨a⟩ is /æ/, ⟨o⟩ is
/ɑ/, ⟨ə⟩ is /ɤ/, ⟨c⟩ is /tʃ/, ⟨ł⟩ is /ɬ/, ⟨y⟩ is /j/, and the ogonek
letters ⟨į ę ą ǫ ų⟩ are the nasal vowels /ĩ ẽ æ̃ ɑ̃ ũ/. Under the same
1948 analysis the aspirates, ejectives and labialised consonants are
consonant CLUSTERS, so ⟨ph th⟩ are /ph th/, ⟨p' t' k' c'⟩ are /pʔ tʔ kʔ
tʃʔ/ and ⟨kw xw⟩ are /kw xw/.

Every vowel letter carries one of six diacritics that jointly encode
stress and tone. Only the tone is recoverable from a single grapheme:
acute and grave are mid tone (macron), double acute and caron are high
tone (acute), circumflex and double grave are low tone (grave), and a
bare vowel is unstressed and toneless. In a mid-tone vowel cluster the
macron is written on both components. Vowel-initial words begin with a
glottal stop that the orthography does not write.

Every word expectation below is a worked orthography/phonemic pair
printed in the Wikipedia *Taos phonology* article, quoted unchanged
except for dropping the stress marks the spec does not emit. The two
tables the spec is built from live in the "Transcription" section of
the Wikipedia *Taos language* article; the spec's own note carries the
full citation, and these tests only exercise it.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def twf():
    return G2P("twf")


@pytest.mark.parametrize("word,ipa", [
    # Trager's letters against their IPA namesakes.
    ("xónemą", "xɑ̄nemæ̃"),        # <o> is /ɑ/, <ą> is /æ̃/
    ("kə̀nénemą", "kɤ̄nēnemæ̃"),   # <ə> is /ɤ/
    ("łòxóyna", "ɬɑ̄xɑ̄jnæ"),       # <ł> is /ɬ/, <y> is /j/
    ("łùłiʼína", "ɬūɬiʔīnæ"),      # the apostrophe is /ʔ/
    ("łòwatúną", "ɬɑ̄wætūnæ̃"),    # unmarked <a> is /æ/, not /a/
])
def test_americanist_letter_values(twf, word, ipa):
    assert twf.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # The 1948 cluster analysis: no ʰ, no ejective ʼ, no labialisation ʷ.
    ("tʼáwaną", "tʔǣwænæ̃"),
    ("mą̏cʼélena", "mæ̃̀tʃʔēlenæ"),
    ("kʼə́onemą", "kʔɤ̄ɑ̄nemæ̃"),
    ("pʼȍkʼúowoną", "pʔɑ̀kʔūɑ̄wɑnæ̃"),
    ("kwę̀mų́na", "kwẽ̄mũ̄næ"),
])
def test_glottalised_and_labialised_are_clusters(twf, word, ipa):
    assert twf.transcribe(word) == ipa


def test_phr_is_the_marginal_labial_fricative(twf):
    """⟨phr⟩ is /fɾ/, not ⟨ph⟩ + ⟨r⟩.

    Trager 1946 wrote this cluster ⟨fr⟩ and 1948 respells it ⟨phr⟩, so
    reading it as an aspirate plus a flap gives [phɾ] for a sequence
    whose first segment is /f/. No word in the benchmark gold contains
    it, which is why only a test can hold the letter value in place.
    """
    assert twf.transcribe("phráne") == "fɾǣne"


@pytest.mark.parametrize("word,ipa", [
    # The five ogonek letters, phonemically.
    ("mą́kuna", "mæ̃̄kunæ"),        # ą = /æ̃/
    ("mę̀sotuʼúna", "mẽ̄sɑtuʔūnæ"),  # ę = /ẽ/, not /ɛ̃/ and not /æ̃/
    ("hǫ́luma", "hɑ̃̄lumæ"),        # ǫ = /ɑ̃/
    ("yų́na", "jũ̄næ"),             # ų = /ũ/
    ("thį̀ęʼéna", "thĩ̄ẽ̄ʔēnæ"),   # į = /ĩ/, and <th> is a cluster
])
def test_ogonek_nasal_vowels(twf, word, ipa):
    assert twf.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # Acute and grave are both MID tone and surface as a macron; they
    # differ only in stress, which a grapheme-local mapping cannot place.
    ("cìatúną", "tʃīǣtūnæ̃"),
    # Double acute is HIGH tone.
    ("wa̋mą", "wǽmæ̃"),
    # Circumflex and double grave are both LOW tone.
    ("mą̂tʼemą", "mæ̃̀tʔemæ̃"),
    ("łȉwéna", "ɬìwēnæ"),
    # A bare vowel is unstressed and carries no tone mark at all.
    ("híʼąngą", "hīʔæ̃nɡæ̃"),
])
def test_stress_tone_diacritics_resolve_to_tone(twf, word, ipa):
    assert twf.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # Under a mid tone the macron is written on BOTH cluster components.
    ("kʼə́onemą", "kʔɤ̄ɑ̄nemæ̃"),   # ə́o = /ɤ̄ɑ̄/
    ("cìatúną", "tʃīǣtūnæ̃"),      # ìa = /īǣ/
    ("thį̀ęʼéna", "thĩ̄ẽ̄ʔēnæ"),   # į̀ę = /ĩ̄ẽ̄/
    # Under a low tone only the first component carries the mark.
    ("pʼȍkʼúowoną", "pʔɑ̀kʔūɑ̄wɑnæ̃"),
])
def test_mid_tone_spreads_across_a_vowel_cluster(twf, word, ipa):
    assert twf.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # Vowel-initial words open with a glottal stop the orthography omits.
    ("íałona", "ʔīǣɬɑnæ"),
    ("ȍdénemą", "ʔɑ̀dēnemæ̃"),
    ("pʼȍʼǫ́yona", "pʔɑ̀ʔɑ̃̄jɑnæ"),  # word-internal ʼ is written as usual
])
def test_word_initial_glottal_stop_is_restored(twf, word, ipa):
    assert twf.transcribe(word) == ipa
