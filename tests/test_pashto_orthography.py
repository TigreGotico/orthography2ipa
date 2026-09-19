"""Pashto letter values that the plain Perso-Arabic reading gets wrong.

Pashto writes with a modified Perso-Arabic abjad, and three of its letters
carry values that a Persian- or Arabic-shaped reading misses. Alef is a
vowel carrier at the start of a word rather than the long back vowel it
spells medially, so ⟨ا⟩ opens a word on a short vowel and the sequence
⟨او⟩ opens it on the rounded vowel that Waw supplies. He at the end of a
word spells the final vowel, not /h/. Waw and the Ye letters are matres
lectionis after a consonant and glides next to a vowel.

Two consonant values follow the descriptive literature rather than a
Persian default: ⟨ر⟩ is the alveolar trill /r/, with the tap [ɾ] kept as
a registered allophone per the gold's notation convention rather than a
positional rule, and /n/ is velar [ŋ] before a velar stop.

Sources are Tegey & Robson, *A Reference Grammar of Pashto* (1996),
Penzl, *A Grammar of Pashto* (1955), and David, *Descriptive Grammar of
Pashto and its Dialects* (2014), all cited in the ``ps`` spec.
"""
import pytest

from orthography2ipa.g2p import G2P

PS = G2P("ps")


# Word-initial alef is a carrier defaulting to a short vowel; ɑ is a
# low-priority fallback in that same slot, and آ is the letter dedicated
# to spelling /ɑ/. Medial alef keeps the back vowel.
@pytest.mark.parametrize("word,expected", [
    ("اته", "ata"),
    ("انار", "anɑr"),
    ("آر", "ɑr"),
])
def test_initial_alef_is_a_vowel_carrier(word, expected):
    assert PS.transcribe(word) == expected


# ⟨او⟩ word-initially is carrier + Waw-as-nucleus, so the word opens on a
# rounded vowel, not on /ɑw/.
@pytest.mark.parametrize("word,expected", [
    ("اوبه", "oba"),
    ("اور", "or"),
    ("اوم", "om"),
])
def test_initial_alef_waw_is_a_rounded_vowel(word, expected):
    assert PS.transcribe(word) == expected
    assert not PS.transcribe(word).startswith("ɑ")


# Final He spells the vowel that ends the word (the feminine -a above all),
# never the consonant /h/.
@pytest.mark.parametrize("word,expected", [
    ("ښځه", "ʂdza"),
    ("ښه", "ʂa"),
    ("ژبه", "ʒba"),
])
def test_final_he_is_a_vowel(word, expected):
    assert PS.transcribe(word) == expected
    assert not PS.transcribe(word).endswith("h")


# Waw and Ye after a consonant are matres lectionis, not glides.
# "زموږ" is a direct gold match. "ماشوم" is not attested in the gold set;
# the pin is the engine's own candidate-ranking output, recorded here as
# a regression pin rather than a gold-verified value. "دی" likewise has
# no direct gold entry (the gold's transcription is d̪aɪ); the corpus
# split on final ⟨ی⟩ is i 67 / aɪ 56 tokens, so an i-first ranking is
# defensible, but "di" is the spec's candidate choice, not gold. "وريژې"
# is a direct gold match.
@pytest.mark.parametrize("word,expected", [
    ("ماشوم", "mɑʃom"),
    ("زموږ", "zmoʐ"),
    ("دی", "di"),
    ("وريژې", "wriʒe"),
])
def test_waw_and_ye_are_matres_after_a_consonant(word, expected):
    assert PS.transcribe(word) == expected


# Vowel length is not written into the phonemes: the seven-vowel system
# contrasts by quality, so no transcription carries a length mark.
@pytest.mark.parametrize("word", ["انار", "آر", "ماشوم", "کتاب", "پښتو"])
def test_no_length_marks(word):
    assert "ː" not in PS.transcribe(word)


# ر is the trill in onset position; the tap stays available as a
# registered positional allophone. The r/ɾ choice follows the gold's
# notation convention (356 r vs 1 ɾ tokens), not a positional claim, so
# this test does not assert anything about the tap's own distribution.
def test_rhotic_is_the_trill():
    assert PS.transcribe("وريژې") == "wriʒe"
    assert "ɾ" in PS.spec.allophones["r"]


# /n/ before a velar stop is [ŋ].
def test_nasal_assimilates_to_velar():
    assert PS.transcribe("انګور") == "aŋɡor"


# The Kandahari (Southwestern) retroflex values for ښ ږ are the spec's
# declared dialect target; the Yusufzai x/ɡ and Central ç/ʝ readings of the
# same letters are not what this spec emits.
def test_kandahari_retroflex_sibilants():
    assert PS.transcribe("پښتو") == "pʂto"
    assert PS.transcribe("زموږ") == "zmoʐ"
