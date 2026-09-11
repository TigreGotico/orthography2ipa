"""Validation tests for the Chuvash (``cv``) spec.

Chuvash is the sole surviving Oghur (Bolgar) Turkic language, written in a
37-letter Cyrillic alphabet: the 33 Russian letters plus Ӑ, Ӗ, Ҫ and Ӳ.
Every claim asserted here is grounded in a source that was read directly:

- Wikipedia, "Chuvash language" (alphabet table with per-letter IPA:
  Ӑ /ɤ̆/~/ə/, Ӗ /ɘ/, Ҫ /ɕ/, Ӳ /y/, Х /χ/, В /ʋ/~/w/; the reduced-vowel
  description; the fortis→lenis alternation and the palatalisation of
  consonants before front vowels).
- Dobrovolsky (1999), "The phonetics of Chuvash stress: implications for
  phonology", ICPhS99 San Francisco, p. 539: the full /i y e ɨ u a/ vs
  reduced /ĕ ă/ split, the latter pair corresponding phonologically to
  Turkish /œ o/ — ĕ to the front /œ/, ă to the back /o/ — and the stress
  rule "stress the last full vowel of a word; if there are no full vowels,
  stress the first vowel of the word".

The four letters unique to Chuvash carry the tests' weight: a spec whose
grapheme table omits them silently deletes the language's two most frequent
vowels, which is how a phone error rate ends up above 1.0.
"""
from __future__ import annotations

import pytest

import orthography2ipa
from orthography2ipa.g2p import G2P


@pytest.fixture(scope="module")
def spec():
    return orthography2ipa.get("cv")


@pytest.fixture(scope="module")
def g2p():
    engine = G2P("cv")

    def say(word):
        """Segments only — stress placement is asserted separately."""
        return engine.transcribe_word(word).replace("\u02c8", "")

    return say


CHUVASH_ALPHABET = "аӑбвгдеёӗжзийклмнопрсҫтуӳфхцчшщъыьэюя"


def test_alphabet_is_complete_and_cyrillic(spec):
    """All 37 letters are mapped, and no Latin look-alike stands in for a
    Cyrillic one: ⟨ӑ⟩ is U+04D1, not Latin ⟨ă⟩ U+0103."""
    assert len(CHUVASH_ALPHABET) == 37
    missing = [c for c in CHUVASH_ALPHABET if c not in spec.graphemes]
    assert not missing, f"unmapped Chuvash letters: {missing}"
    latin = [k for k in spec.graphemes if any(ch.isascii() or "Ā" <= ch <= "ɏ"
                                              for ch in k)]
    assert not latin, f"Latin keys in a Cyrillic spec: {latin}"


@pytest.mark.parametrize("letter,ipa", [
    ("ҫ", "ɕ"),      # Ҫ /ɕ/ — the letter unique to Chuvash
    ("ӳ", "y"),      # front rounded high vowel
    ("х", "χ"),      # uvular, not velar
    ("в", "ʋ"),      # approximant, [v] only in Russian loans
    ("ӑ", "ə"),      # back reduced vowel
    ("ӗ", "ɘ"),      # front reduced vowel
])
def test_letter_ipa(spec, letter, ipa):
    assert spec.graphemes[letter][0] == ipa


def test_reduced_vowels_are_distinct(spec):
    """ӑ and ӗ are the back and front members of one harmonic pair, not a
    single schwa: collapsing them erases a phonemic contrast."""
    assert spec.graphemes["ӑ"][0] != spec.graphemes["ӗ"][0]


def test_a_is_the_back_harmonic_vowel(spec):
    """а pairs with е under back~front harmony, so it is [ɑ], not [a]."""
    assert spec.graphemes["а"][0] == "ɑ"


@pytest.mark.parametrize("word,ipa", [
    ("ҫӗнӗ", "ɕɘnɘ"),        # 'new' — ҫ + both reduced vowels
    ("ӗҫ", "ɘɕ"),            # 'work'
    ("хӑнӑхса", "χənəχsɑ"),  # uvular х around reduced ӑ
    ("вӑхӑт", "ʋəχət"),      # 'time' — в as approximant
    ("ҫӳп", "ɕyp"),          # ӳ
    ("ялтан", "jɑltɑn"),     # iotated я, back ɑ
])
def test_transcriptions(g2p, word, ipa):
    assert g2p(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("епле", "jeple"),       # word-initial е is iotated
    ("ҫеҫ", "ɕeɕ"),          # е after a consonant is plain [e]
    ("еннелле", "jennelle"),  # both in one word
])
def test_e_is_iotated_only_word_initially(g2p, word, ipa):
    """Chuvash ⟨е⟩ spells [je] at the word edge and [e] elsewhere; mapping
    it to [je] everywhere injects a glide into the middle of every word
    that contains the language's second most frequent vowel letter."""
    assert g2p(word) == ipa


def test_soft_sign_palatalises(g2p, spec):
    assert spec.graphemes["ь"] == ["ʲ"]
    assert g2p("выльӑх") == "ʋɯlʲəχ"


def test_lenis_allophones_are_recorded(spec):
    """Stops, sibilants and affricates are fortis but lenis intervocalically
    and after sonorants. The alternation is realisational, so it lives in the
    allophone table rather than in the 1-best transcription."""
    for fortis, lenis in [("p", "b"), ("t", "d"), ("k", "ɡ"),
                          ("s", "z"), ("ʃ", "ʒ"), ("ɕ", "ʑ"),
                          ("tʃ", "dʒ"), ("ts", "dz")]:
        assert lenis in spec.allophones[fortis], f"{fortis} lacks lenis {lenis}"


def test_notes_record_the_unmodelled_processes(spec):
    notes = spec.notes.lower()
    assert "lenis" in notes
    assert "palatalis" in notes or "palataliz" in notes


def test_stress_notes_cite_the_last_full_vowel_rule(spec):
    notes = spec.stress.notes.lower()
    assert "last full vowel" in notes
    assert "dobrovolsky" in notes
