"""Konkani (kok) phonology: schwa deletion, anusvara, murmured sonorants.

Konkani is written in Devanagari, so the same abugida machinery that serves
Hindi and Sanskrit serves it: the engine gives a consonant letter its inherent
vowel and cancels it when a matra or a virama follows, and each language's
data says what happens to that vowel afterwards. Konkani deletes it, Sanskrit
keeps it, and the two specs share a script and an ancestry link — so the
Sanskrit guards below are what break first if any of this leaks into the
engine.

Sources for the rules under test:

- Schwa deletion in modern Indo-Aryan: Masica, *The Indo-Aryan Languages*
  (1991); Ohala, *Aspects of Hindi Phonology* (1983), ch. 5;
  Narasimhan, Sproat & Kiraz, "Schwa-Deletion in Hindi Text-to-Speech
  Synthesis", *IJST* 7(4) (2004), pp. 319-333.
- Konkani vowel and consonant inventory, including the alveolar tap /ɾ/, the
  glottal fricative /h/, the mid vowels /e ɛ o ɔ/ and the murmured sonorants:
  Almeida, *A Description of Konkani* (1989) — edition not consulted, the
  inventory is quoted at second hand; Ashok & Dutta, "Syllable Structure and
  Word Stress in Central Kerala Konkani Variety: An OT Approach", *Journal of
  Universal Language* 22(1) (2021), Table 4.
- Anusvara as a homorganic nasal before a stop: Masica (1991).
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def kok() -> G2P:
    return G2P("kok")


@pytest.fixture(scope="module")
def sa() -> G2P:
    return G2P("sa")


# ── word-final schwa deletion ───────────────────────────────────────────────

@pytest.mark.parametrize("word,ipa", [
    ("भाव", "bʱaːʋ"),        # bhāv 'brother', not *bʱaːʋə
    ("नाम", "naːm"),         # nām 'name'
    ("फूल", "pʰuːl"),        # phūl 'flower'
    ("रंग", "ɾəŋɡ"),         # raṅg 'colour'
])
def test_word_final_inherent_vowel_is_deleted(kok, word, ipa):
    assert kok.transcribe_word(word) == ipa


def test_monosyllabic_one_letter_word_keeps_its_only_vowel(kok):
    """word_initial=false on the FINAL rules: न is [nə], never bare *[n].

    Over-application guard on a word class the rule must not touch — a
    one-letter word whose inherent vowel is the word's only nucleus.
    """
    assert kok.transcribe_word("न") == "nə"


def test_sanskrit_keeps_the_inherent_vowel(sa):
    """Konkani's deletion must stay in Konkani's data.

    sa shares the script, the inherent vowel and an ancestry link with kok
    (kok declares sa as its parent), so this is the leak detector.
    """
    assert sa.transcribe_word("नाम") == "n̪ɑːmɐ"


# ── medial VC_CV schwa deletion and its guard ───────────────────────────────

def test_medial_schwa_deleted_in_vc_cv(kok):
    """आयतार is [aːjt̪aːɾ] — the schwa on य is preceded by a vowel and the
    following त carries a matra of its own."""
    assert kok.transcribe_word("आयतार") == "aːjt̪aːɾ"


def test_medial_schwa_kept_after_a_cluster(kok):
    """Over-application guard, KOK_SCHWA_KEEP_*: the schwa on the second
    member of a written conjunct is preceded by a vowel-less consonant, not a
    vowel, so VC_CV does not apply. प्रकार stays [pɾəkaːɾ]."""
    assert kok.transcribe_word("प्रकार") == "pɾəkaːɾ"


def test_medial_schwa_kept_before_a_vowel_bearing_consonant(kok):
    """Second over-application guard: गावप keeps its medial schwa because the
    following प carries the word's own (deleted-final) inherent vowel rather
    than a matra — [ɡaːʋəp], not *[ɡaːʋp]."""
    assert kok.transcribe_word("गावप") == "ɡaːʋəp"


# ── anusvara ────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("word,ipa", [
    ("रंग", "ɾəŋɡ"),          # velar
    ("हिंदी", "hind̪iː"),      # dental
    ("लांब", "laːmb"),        # labial
    ("वैकुंठ", "ʋəikuɳʈʰ"),    # retroflex
    ("पांच", "paːntʃ"),       # palatal
])
def test_anusvara_before_a_stop_is_a_homorganic_nasal(kok, word, ipa):
    assert kok.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("गांव", "ɡãːʋ"),         # before a glide
    ("हांसप", "hãːsəp"),      # before a fricative
    ("गोंय", "ɡõj"),          # before a glide
])
def test_anusvara_before_a_non_stop_nasalizes_the_vowel(kok, word, ipa):
    """Over-application guard: the homorganic-nasal rules are keyed on the
    following stop GRAPHEME, so a fricative or glide leaves the anusvara as
    nasalization on the vowel."""
    assert kok.transcribe_word(word) == ipa


# ── murmured sonorants ──────────────────────────────────────────────────────

@pytest.mark.parametrize("word,ipa", [
    ("म्हस", "mʱəs"),
    ("न्हीद", "nʱiːd̪"),
    ("ल्हार", "lʱaːɾ"),
    ("व्हाण", "ʋʱaːɳ"),
])
def test_sonorant_plus_ha_is_one_murmured_segment(kok, word, ipa):
    assert kok.transcribe_word(word) == ipa


def test_plain_ha_is_a_glottal_fricative_not_a_murmur(kok):
    """Over-application guard: ⟨ह⟩ outside a sonorant conjunct is plain [h],
    and a preceding sonorant that is NOT in a conjunct with it stays plain."""
    assert kok.transcribe_word("हांव") == "hãːʋ"


# ── segment inventory ───────────────────────────────────────────────────────

def test_rhotic_is_an_alveolar_tap(kok):
    """Konkani's rhotic is /ɾ/, not a trill /r/."""
    assert kok.transcribe_word("रवो") == "ɾəʋo"


def test_mid_vowels_are_short(kok):
    """Devanagari writes no length on ⟨े⟩/⟨ो⟩ and Konkani's mid vowels are
    /e ɛ o ɔ/, so the plain matras read short."""
    assert kok.transcribe_word("ओडप") == "oɖəp"
    assert kok.transcribe_word("धर्चे") == "d̪ʱəɾtʃe"


def test_low_and_high_vowel_length_is_still_written(kok):
    """Guard on the mid-vowel change: it must not strip length from ⟨ा⟩/⟨ी⟩/⟨ू⟩,
    which the script does distinguish from ⟨अ⟩/⟨ि⟩/⟨ु⟩."""
    assert kok.transcribe_word("बारीक") == "baːɾiːk"


def test_both_affricate_series_are_reachable(kok):
    """Konkani contrasts /ts dz/ with /tʃ dʒ/ and Devanagari writes both with
    ⟨च⟩/⟨ज⟩, so both readings must be in the lattice."""
    readings = kok.word_candidates("चूक")
    assert "tʃuːk" in readings
    assert "tsuːk" in readings


# ── vocalic r and candra vowels ─────────────────────────────────────────────

@pytest.mark.parametrize("word,ipa", [
    ("कृपेन", "kɾɪpen"),
    ("संस्कृताय", "sə̃skɾɪt̪aːj"),
])
def test_vocalic_r_is_a_tap_plus_vowel(kok, word, ipa):
    """⟨ृ⟩/⟨ऋ⟩ (vocalic r) are not in the grapheme table, so the segment is
    silently dropped instead of read as the Indo-Aryan tap-plus-vowel reflex
    (Masica 1991, ch. 6)."""
    assert kok.transcribe_word(word) == ipa


def test_vocalic_r_word_still_has_a_final_consonant(kok):
    """Regression guard for the reported symptom: dropping ⟨ृ⟩ left no vowel
    between the tap and the following coda, so schwa deletion misfired and
    kept a schwa word-finally instead (संस्कृत -> sə̃skt̪ə)."""
    assert kok.transcribe_word("संस्कृत") == "sə̃skɾɪt̪"


@pytest.mark.parametrize("word,ipa", [
    ("ऑगस्ट", "æɡsʈ"),
    ("मॅरी", "mæɾiː"),
])
def test_candra_vowels_are_the_english_loan_class(kok, word, ipa):
    """⟨ऑ⟩/⟨ॉ⟩ (candra o) and ⟨ॅ⟩ (candra e) mark the loan vowels Devanagari
    has no native letter for; the kaikki gold reads both as /æ/ in these
    words."""
    assert kok.transcribe_word(word) == ipa


def test_candra_o_offers_the_documented_open_mid_reading(kok):
    """/ɔ/ is the value the broader Indo-Aryan candra-o convention documents
    (and the one Marathi's spec carries); it is kept as a second candidate
    alongside the gold-attested /æ/."""
    assert "ɔɡsʈ" in kok.word_candidates("ऑगस्ट")
