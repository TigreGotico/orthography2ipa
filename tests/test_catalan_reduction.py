"""Catalan vowel reduction, spirantization and dialectal vocalism.

These tests pin the corrected Catalan vowel system:

* **Stress-conditioned reduction** (Central/Eastern block): unstressed
  /a e ɛ/ → [ə] and /o ɔ/ → [u], while STRESSED vowels keep full quality
  (Wheeler 2005 §2.3). The bug this guards against was unconditional
  reduction of every nucleus (``gos`` → *[ˈɡus]* instead of [ˈɡɔs]).
* **Western varieties do NOT reduce** — Valencian and Northwestern
  (Occidental) keep the 7-vowel inventory in atonic position
  (Recasens 1996; Veny 1982). Occidental previously inherited the Central
  reduction by mistake.
* **Intervocalic spirantization** /b d ɡ/ → [β ð ɣ] between vowels only
  (Wheeler 2005 §5.2), modelled as a post-lexical allophone rule.
"""
import pytest

from orthography2ipa import transcribe


# ── Bug 1: stressed vowels keep full quality; unstressed reduce (Central) ──

@pytest.mark.parametrize("word,expected", [
    ("gos", "ˈɡɔs"),     # stressed o → [ɔ], NOT reduced to [u]
    ("dona", "ˈdɔnə"),   # stressed o → [ɔ]; unstressed final a → [ə]
    ("porta", "ˈpɔɾtə"),  # stressed o → [ɔ]; unstressed a → [ə]
    ("fred", "ˈfɾɛt"),   # stressed e → [ɛ] (+ final devoicing d→t)
    ("pare", "ˈpaɾə"),   # stressed a → [a]; unstressed e → [ə]
])
def test_central_stressed_vowel_keeps_quality(word, expected):
    assert transcribe(word, "ca") == expected


@pytest.mark.parametrize("word,expected", [
    ("casa", "ˈkazə"),   # unstressed a → [ə]
    ("tenir", "təˈniɾ"),  # pretonic e → [ə]
])
def test_central_unstressed_vowel_reduces(word, expected):
    assert transcribe(word, "ca") == expected


def test_central_monosyllable_is_stressed():
    """A monosyllable is treated as stressed, so its vowel is not reduced."""
    assert transcribe("gos", "ca") == "ˈɡɔs"
    assert transcribe("sol", "ca") == "ˈsɔl"


# ── Bug 2: Western varieties do NOT apply Central reduction ──

@pytest.mark.parametrize("code", ["ca-x-occidental", "ca-x-valencia"])
@pytest.mark.parametrize("word", ["casa", "dona", "tenir", "porta", "gos"])
def test_western_varieties_do_not_reduce(code, word):
    out = transcribe(word, code)
    assert "ə" not in out, f"{code} {word!r}: {out!r} unexpectedly has schwa"


def test_occidental_full_vowels():
    assert transcribe("casa", "ca-x-occidental") == "kaza"
    assert transcribe("dona", "ca-x-occidental") == "dɔna"


def test_valencia_full_vowels():
    assert transcribe("casa", "ca-x-valencia") == "kaza"
    assert transcribe("dona", "ca-x-valencia") == "dona"


def test_balear_reduces_but_keeps_stress_quality():
    """Balearic (Eastern) reduces unstressed vowels but keeps stressed."""
    assert transcribe("casa", "ca-x-balear") == "ˈkazə"   # unstressed a → ə
    assert transcribe("gos", "ca-x-balear") == "ˈɡos"     # stressed o kept


# ── Bug 3: intervocalic spirantization only between vowels ──

@pytest.mark.parametrize("word,seg", [
    ("roba", "β"),
    ("cada", "ð"),
    ("pagar", "ɣ"),
])
def test_spirantization_intervocalic(word, seg):
    assert seg in transcribe(word, "ca")


def test_no_spirantization_after_consonant():
    """/b/ after a consonant (not intervocalic) stays a stop."""
    out = transcribe("poble", "ca")   # b is preceded by vowel but followed by l
    assert "β" not in out
    assert "b" in out


@pytest.mark.parametrize("code", ["ca", "ca-x-occidental", "ca-x-valencia",
                                  "ca-x-balear"])
def test_spirantization_all_varieties(code):
    """Spirantization is on the shared base, so every variety inherits it."""
    assert "ð" in transcribe("cada", code)
