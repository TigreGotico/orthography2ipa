# -*- coding: utf-8 -*-
"""Standard Thai: what the spelling of a syllable does and does not say.

Every expected transcription below is the segmental content of the WikiPron
Thai (``tha_thai_broad``) entry for that headword, with the gold's tone
letters removed. The tests that ask what the LETTERS say read the
transcription through :func:`segments`, which drops the tone letters, so
that a coda or a cluster is asserted as a coda or a cluster; what the
SYLLABLE SHAPE says is asserted on its own, tone letters and all, by the
tests at the end of this module.

Sources for the facts themselves: Iwasaki, S. & Ingkaphirom, P. (2005),
*A Reference Grammar of Thai*, Cambridge University Press; Haas, M.R.
(1964), *Thai-English Student's Dictionary*, Stanford University Press.
"""
import pytest

import orthography2ipa as o2i
from orthography2ipa.tone import TONE_MARKS


@pytest.fixture(scope="module")
def th():
    return o2i.G2P("th")


def segments(th, word):
    """*word*'s reading without its tone letters — the segmental slice."""
    return "".join(ch for ch in th.transcribe_word(word)
                   if ch not in TONE_MARKS)


def test_marks_never_leak_a_placeholder_into_the_ipa(th):
    """A grapheme table entry is IPA, and ⟨็⟩ used to carry the literal
    word ``short_vowel`` straight into the transcription."""
    for word in ["เก็บ", "เป็น", "เห็น", "น็อต"]:
        ipa = th.transcribe_word(word)
        assert "short_vowel" not in ipa
        assert ipa.isprintable() and "_" not in ipa


@pytest.mark.parametrize("word,ipa", [
    # A tone mark sits on the INITIAL consonant, between it and the vowel
    # sign that is the syllable's nucleus. Reading the mark as "no vowel
    # here" surfaced the inherent vowel on a consonant that has one written.
    ("ก่อน", "kɔːn"),
    ("น้ำ", "nam"),
    # …and between the nucleus and the coda letter, which then opened a
    # syllable of its own.
    ("ยิ้ม", "jim"),
    ("ห้า", "haː"),
])
def test_a_tone_mark_is_transparent_between_a_consonant_and_its_vowel(th, word, ipa):
    assert segments(th, word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # Only /p t k m n ŋ w j/ close a Thai syllable. Every other letter
    # neutralises: to the unreleased stop of its own place…
    ("กฎ", "kot̚"),      # ⟨ฎ⟩ d → t̚
    ("เทพ", "tʰeːp̚"),   # ⟨พ⟩ pʰ → p̚
    ("ครับ", "kʰrap̚"),  # ⟨บ⟩ b → p̚
    # …or, for ⟨ร ล ฬ ญ ณ⟩, to final /n/.
    ("กงศุล", "koŋsun"),  # ⟨ล⟩ l → n
    ("กงการ", "koŋkaːn"),  # ⟨ร⟩ r → n
])
def test_a_thai_syllable_neutralises_its_coda(th, word, ipa):
    assert segments(th, word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("เก", "keː"),
    ("เทพ", "tʰeːp̚"),
    ("โต", "toː"),
])
def test_a_letter_carrying_a_preposed_vowel_is_an_onset_not_a_coda(th, word, ipa):
    """⟨เ แ โ ใ ไ⟩ are written before their consonant and pronounced after
    it, so the last LETTER of ⟨เก⟩ is the syllable's initial. A coda entry
    reaching it turned /keː/ into */k̚/."""
    assert segments(th, word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("กรุง", "kruŋ"),
    ("กลาง", "klaːŋ"),
    ("ควาย", "kʰwaːj"),
    ("ประเทศ", "pratʰeːt̚"),
    ("ทราบ", "saːp̚"),   # ⟨ทร⟩ is the lexicalised /s/ digraph
])
def test_a_true_onset_cluster_has_no_vowel_inside_it(th, word, ipa):
    assert segments(th, word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("หมา", "maː"),
    ("หนึ่ง", "nɯŋ"),
    ("ใหญ่", "jaj"),
    ("อยาก", "jaːk̚"),   # o nam: ⟨อ⟩ before ⟨ย⟩
])
def test_a_leading_ho_nam_is_a_tone_class_marker_and_is_not_pronounced(th, word, ipa):
    assert segments(th, word) == ipa


def test_ho_nam_is_only_silent_before_a_sonorant(th):
    """⟨ห⟩ is a tone-class marker only in front of ⟨ง ญ ณ น ม ย ร ล ฬ ว⟩;
    everywhere else it is an ordinary /h/ and must survive."""
    assert segments(th, "ห้า") == "haː"
    assert segments(th, "หก") == "hok̚"


@pytest.mark.parametrize("word,ipa", [
    ("อ่าน", "ʔaːn"),    # word-initial ⟨อ⟩ is the glottal onset
    ("ขอ", "kʰɔː"),      # after a consonant it is the vowel /ɔː/
    ("ก่อน", "kɔːn"),
    ("เอกชน", "ʔeːktɕʰon"),
])
def test_o_ang_is_a_vowel_letter_except_as_a_syllable_onset(th, word, ipa):
    assert segments(th, word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("สัตว์", "sat̚"),    # ⟨ว⟩ cancelled
    ("จันทร์", "tɕan"),  # the whole final ⟨ทร⟩ cancelled
])
def test_thanthakhat_cancels_the_letter_it_stands_on(th, word, ipa):
    assert segments(th, word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("ธง", "tʰoŋ"),
    ("ฆ่า", "kʰaː"),
    ("ฉัน", "tɕʰan"),
])
def test_the_letters_the_table_used_to_omit_are_read(th, word, ipa):
    """⟨ฃ ฅ ฆ ฉ ฌ ฒ ธ⟩ were absent from the grapheme table, so a word
    spelled with one lost that consonant entirely."""
    assert segments(th, word) == ipa


def test_the_spec_declares_its_tone_inventory(th):
    spec = o2i.get("th")
    assert spec.tone_inventory
    assert set(spec.tone_inventory.values()) == {
        "mid", "low", "falling", "high", "rising"}
    assert set(spec.tone_inventory) == {"˧", "˨˩", "˥˩", "˦˥", "˩˩˦"}


@pytest.mark.parametrize("word,ipa", [
    ("โหม", "hoːm"),        # ⟨ห⟩ is the onset, ⟨ม⟩ the coda
    ("กลาโหม", "klaːhoːm"),
    ("กำแหง", "kamhɛːŋ"),
    ("ข่มเหง", "kʰomheːŋ"),
])
def test_a_preposed_vowel_makes_ho_nam_its_own_onset(th, word, ipa):
    """⟨ห⟩ before a sonorant is a silent tone-class marker only when the
    sonorant OPENS the syllable. A preposed vowel written before ⟨ห⟩ takes
    ⟨ห⟩ as its consonant, which leaves the sonorant as the coda: reading
    the digraph there deletes a real /h/ and reorders the syllable."""
    assert segments(th, word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("หมา", "maː"),      # no preposed vowel
    ("ใหญ่", "jaj"),     # ⟨ใ⟩ spells its own final glide
    ("ไหม", "maj"),
    ("แหวน", "wɛːn"),    # ⟨น⟩ takes the coda slot
    ("โหมด", "moːt̚"),
    ("แหล่", "lɛː"),     # the tone mark rides the syllable initial
])
def test_ho_nam_still_reads_the_sonorant_alone_where_it_opens_the_syllable(
        th, word, ipa):
    assert segments(th, word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("คลอโรฟอร์ม", "kʰlɔːroːfɔːm"),
    ("คอร์นวอลล์", "kʰɔːnwɔːl"),
])
def test_a_thanthakhat_killed_cluster_leaves_no_inherent_vowel(th, word, ipa):
    """A letter+thanthakhat sequence spells nothing, so it cannot stand
    between a consonant and the vowel that consonant reads."""
    assert segments(th, word) == ipa


# ── the tone a syllable's shape spells ──────────────────────────────────
#
# Thai writes no tone letter. It writes the class of the initial consonant,
# whether the rime is live or dead, how long the vowel is, and which of the
# four tone marks (if any) rides the initial — and those four together name
# one of the five tones. Each expectation below is the full WikiPron entry
# for its headword, tone letters included; the cell of the system each one
# exercises is named beside it.


@pytest.mark.parametrize("word,ipa", [
    ("กา", "kaː˧"),           # mid   × live        → mid
    ("จุด", "tɕut̚˨˩"),        # mid   × dead short  → low
    ("จอด", "tɕɔːt̚˨˩"),       # mid   × dead long   → low
    ("ของ", "kʰɔːŋ˩˩˦"),      # high  × live        → rising
    ("ผัด", "pʰat̚˨˩"),        # high  × dead short  → low
    ("ขาด", "kʰaːt̚˨˩"),       # high  × dead long   → low
    ("มา", "maː˧"),           # low   × live        → mid
    ("นก", "nok̚˦˥"),          # low   × dead short  → high
    ("เทพ", "tʰeːp̚˥˩"),       # low   × dead long   → falling
])
def test_an_unmarked_syllable_takes_the_tone_of_its_class_and_shape(
        th, word, ipa):
    assert th.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("ก่อน", "kɔːn˨˩"),        # mai ek  on mid   → low
    ("ห่าง", "haːŋ˨˩"),        # mai ek  on high  → low
    ("พ่อ", "pʰɔː˥˩"),         # mai ek  on low   → falling
    ("อ้าง", "ʔaːŋ˥˩"),        # mai tho on mid   → falling
    ("ห้า", "haː˥˩"),          # mai tho on high  → falling
    ("นี้", "niː˦˥"),          # mai tho on low   → high
    ("ก๊อก", "kɔːk̚˦˥"),       # mai tri on mid   → high
])
def test_a_tone_mark_names_the_tone_together_with_the_class(th, word, ipa):
    assert th.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("หมา", "maː˩˩˦"),   # ho nam: ⟨ห⟩ lends ⟨ม⟩ its high class
    ("ไหม", "maj˩˩˦"),   # the gold also holds the colloquial /maj˦˥/
    ("ใหม่", "maj˨˩"),   # …and the mark then reads off that class
    ("ไหม้", "maj˥˩"),   # mai tho on the same high-class ⟨หม⟩
    ("ม้า", "maː˦˥"),    # bare low-class ⟨ม⟩ with mai tho → high
])
def test_a_leading_ho_nam_lends_its_class_to_the_syllable(th, word, ipa):
    """The silent ⟨ห⟩ is written for exactly this: it makes a low-class
    sonorant read as a high-class initial, which is a different tone."""
    assert th.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("กรุง", "kruŋ˧"),      # the cluster's FIRST letter carries the class
    ("ทราบ", "saːp̚˥˩"),    # ⟨ทร⟩ reads /s/, but its class is ⟨ท⟩'s
])
def test_a_cluster_takes_the_class_of_the_letter_that_opens_it(th, word, ipa):
    assert th.transcribe_word(word) == ipa


def test_every_syllable_of_a_word_is_toned_separately(th):
    """Tone is a property of the syllable, not of the word: ⟨บันทึก⟩ is a
    live mid-class first syllable and a dead-short low-class second one."""
    assert th.transcribe_word("บันทึก") == "ban˧tʰɯk̚˦˥"


def test_a_bare_consonant_letter_is_left_alone(th):
    """A spelling with no nucleus has no syllable to carry a tone, and
    must come back as it was rather than as nothing."""
    assert th.transcribe_word("ก") == "k̚"
