# -*- coding: utf-8 -*-
"""Standard Thai: what the spelling of a syllable does and does not say.

Every expected transcription below is the segmental content of the WikiPron
Thai (``tha_thai_broad``) entry for that headword, with the gold's tone
letters removed — the spec emits no tone (see ``test_tone_is_not_emitted``
and the DECLARED GAPS paragraph of ``th.json``'s notes).

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
    assert th.transcribe_word(word) == ipa


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
    assert th.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("เก", "keː"),
    ("เทพ", "tʰeːp̚"),
    ("โต", "toː"),
])
def test_a_letter_carrying_a_preposed_vowel_is_an_onset_not_a_coda(th, word, ipa):
    """⟨เ แ โ ใ ไ⟩ are written before their consonant and pronounced after
    it, so the last LETTER of ⟨เก⟩ is the syllable's initial. A coda entry
    reaching it turned /keː/ into */k̚/."""
    assert th.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("กรุง", "kruŋ"),
    ("กลาง", "klaːŋ"),
    ("ควาย", "kʰwaːj"),
    ("ประเทศ", "pratʰeːt̚"),
    ("ทราบ", "saːp̚"),   # ⟨ทร⟩ is the lexicalised /s/ digraph
])
def test_a_true_onset_cluster_has_no_vowel_inside_it(th, word, ipa):
    assert th.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("หมา", "maː"),
    ("หนึ่ง", "nɯŋ"),
    ("ใหญ่", "jaj"),
    ("อยาก", "jaːk̚"),   # o nam: ⟨อ⟩ before ⟨ย⟩
])
def test_a_leading_ho_nam_is_a_tone_class_marker_and_is_not_pronounced(th, word, ipa):
    assert th.transcribe_word(word) == ipa


def test_ho_nam_is_only_silent_before_a_sonorant(th):
    """⟨ห⟩ is a tone-class marker only in front of ⟨ง ญ ณ น ม ย ร ล ฬ ว⟩;
    everywhere else it is an ordinary /h/ and must survive."""
    assert th.transcribe_word("ห้า") == "haː"
    assert th.transcribe_word("หก") == "hok̚"


@pytest.mark.parametrize("word,ipa", [
    ("อ่าน", "ʔaːn"),    # word-initial ⟨อ⟩ is the glottal onset
    ("ขอ", "kʰɔː"),      # after a consonant it is the vowel /ɔː/
    ("ก่อน", "kɔːn"),
    ("เอกชน", "ʔeːktɕʰon"),
])
def test_o_ang_is_a_vowel_letter_except_as_a_syllable_onset(th, word, ipa):
    assert th.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("สัตว์", "sat̚"),    # ⟨ว⟩ cancelled
    ("จันทร์", "tɕan"),  # the whole final ⟨ทร⟩ cancelled
])
def test_thanthakhat_cancels_the_letter_it_stands_on(th, word, ipa):
    assert th.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("ธง", "tʰoŋ"),
    ("ฆ่า", "kʰaː"),
    ("ฉัน", "tɕʰan"),
])
def test_the_letters_the_table_used_to_omit_are_read(th, word, ipa):
    """⟨ฃ ฅ ฆ ฉ ฌ ฒ ธ⟩ were absent from the grapheme table, so a word
    spelled with one lost that consonant entirely."""
    assert th.transcribe_word(word) == ipa


def test_tone_is_not_emitted(th):
    """A pin on the DECLARED GAP, not an endorsement of it.

    Thai tone is recoverable from the spelling, but the computation needs
    a syllable analysis of the written word that this library has no
    mechanism for. Nothing in the spec may quietly start emitting a
    half-computed tone: against a tone-marked gold a wrong tone costs more
    than no tone, and the gap belongs in the notes until the engine can
    state consonant class × syllable type × vowel length × tone mark.
    """
    for word in ["กา", "ข่า", "ค้า", "หมา", "กฎ"]:
        assert not (set(th.transcribe_word(word)) & TONE_MARKS)


def test_the_spec_declares_the_tone_system_it_cannot_yet_compute(th):
    spec = o2i.get("th")
    assert spec.tone_inventory
    assert set(spec.tone_inventory.values()) == {
        "mid", "low", "falling", "high", "rising"}


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
    assert th.transcribe_word(word) == ipa


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
    assert th.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("คลอโรฟอร์ม", "kʰlɔːroːfɔːm"),
    ("คอร์นวอลล์", "kʰɔːnwɔːl"),
])
def test_a_thanthakhat_killed_cluster_leaves_no_inherent_vowel(th, word, ipa):
    """A letter+thanthakhat sequence spells nothing, so it cannot stand
    between a consonant and the vowel that consonant reads."""
    assert th.transcribe_word(word) == ipa
