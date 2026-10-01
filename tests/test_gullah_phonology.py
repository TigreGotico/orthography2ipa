"""Gullah / Sea Island Creole English (`gul`): the rules that separate a
Gullah transcription from a plain-English-with-accent one.

Klein (2013, APiCS Online chapter 13, synthesising Turner [1949] 2002,
Jones-Jackson 1978 and Weldon 2004) gives:

* a 12-monophthong vowel system with a close/back member and a lax/central
  member at each height (i/ɪ, u/ʊ, e/ə/o, ɛ/ʌ/ɔ, a/ɑ);
* an approximant rhotic /ɹ/, not a trill;
* categorical th-stopping: English [θ] -> [t], English [ð] -> [d].

The plain-letter orthography cannot mark which member of a vowel pair, or
which of θ/ð, a given "th" spelling intends, so the spec picks the value
that the wikipron gold consistently realises for a bare vowel letter (a
measured, not a sourced, choice) and handles the θ/ð split through a closed
list of English function words where ð is categorical.
"""
from orthography2ipa import get, transcribe


def test_gul_is_not_an_english_clone():
    # A "light accent" spec would leave the single-letter vowels at English
    # lax defaults (ɪ, ɛ, ɔ, ʌ) and the rhotic at a trill. Gullah's own
    # single-letter vowel readings sit at the close/back member of each pair
    # per Klein (2013) Table 1, and the rhotic is the approximant ɹ per
    # Table 2, not a trill.
    spec = get("gul")
    assert list(spec.graphemes["a"]) == ["ɑ"]
    assert list(spec.graphemes["e"]) == ["e"]
    assert list(spec.graphemes["i"]) == ["i"]
    assert list(spec.graphemes["o"]) == ["o"]
    assert list(spec.graphemes["u"]) == ["u"]
    assert list(spec.graphemes["r"]) == ["ɹ"]


def test_gul_th_stops_to_voiceless_by_default():
    # Klein (2013): "English [θ] and [ð] appear categorically as [t] and
    # [d], respectively." Content words with etymological theta stop to [t].
    assert transcribe("thik", "gul") == "tik"


def test_gul_th_stops_to_voiced_in_function_words():
    # The closed set of English function words that have ð (the, this,
    # that, ...) is not distinguishable from a theta-word by spelling alone,
    # so it is listed explicitly rather than guessed at from "th".
    assert transcribe("the", "gul") == "də"
    assert transcribe("that", "gul") == "dat"


def test_gul_rhotic_is_an_approximant_not_a_trill():
    assert transcribe("run", "gul") == "ɹun"
    assert "r" not in transcribe("run", "gul")
