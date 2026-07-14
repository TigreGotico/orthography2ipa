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
* **Post-continuant spirantization** /b d ɡ/ → [β ð ɣ] after a vowel or
  other continuant (Wheeler 2005 §5.2), modelled as a post-lexical
  allophone rule — and BLOCKED before a lateral, where the stop geminates
  instead (⟨poble⟩ [ˈpɔbːlə]).

A word on the mid vowels: which of [e]/[ɛ] or [o]/[ɔ] a STRESSED unaccented
⟨e⟩/⟨o⟩ takes is not recoverable from the spelling — it continues a Latin
distinction the orthography stopped writing (⟨gos⟩ is [ˈɡos] but ⟨dona⟩ is
[ˈdɔnə]; only the written accents ⟨è é ò ó⟩ disambiguate). The spec therefore
carries a frequency prior, and these tests assert the vowel quality only where
the orthography actually determines it.
"""
import pytest

from orthography2ipa import transcribe


# ── Bug 1: stressed vowels keep full quality; unstressed reduce (Central) ──

@pytest.mark.parametrize("word,expected", [
    ("pare", "ˈpaɾə"),    # stressed a → [a]; unstressed e → [ə]
    ("porta", "ˈpɔrtə"),  # stressed ⟨o⟩ keeps its OPEN-mid quality, never [u]
    ("casa", "ˈkazə"),    # stressed a → [a]; unstressed a → [ə]
])
def test_central_stressed_vowel_keeps_quality(word, expected):
    """A stressed nucleus is never reduced (Wheeler 2005 §2.3).

    The bug this guards is unconditional reduction of every nucleus —
    ⟨porta⟩ → *[ˈpuɾtə⟩, ⟨casa⟩ → *[ˈkəzə]. Reduction is stress-conditioned,
    so the stressed vowel keeps a full quality even where the *choice*
    between [o] and [ɔ] is a lexical coin-flip the spelling does not make.
    """
    assert transcribe(word, "ca") == expected


@pytest.mark.parametrize("word,expected", [
    ("cafè", "kəˈfɛ"),     # ⟨è⟩ = [ɛ]; the accents DO fix the mid quality
    ("però", "pəˈɾɔ"),     # ⟨ò⟩ = [ɔ]
    ("avió", "əβiˈo"),     # ⟨ó⟩ = [o]; oxytone a-vi-Ó (the ⟨io⟩ is hiatus)
    ("cafés", "kəˈfes"),   # ⟨é⟩ = [e]
])
def test_central_written_accent_fixes_mid_vowel_quality(word, expected):
    assert transcribe(word, "ca") == expected


@pytest.mark.parametrize("word,expected", [
    ("casa", "ˈkazə"),    # unstressed a → [ə]
    ("tenir", "təˈni"),   # pretonic e → [ə] (and final -r is deleted)
    ("comú", "kuˈmu"),    # pretonic o → [u]
])
def test_central_unstressed_vowel_reduces(word, expected):
    assert transcribe(word, "ca") == expected


def test_central_monosyllable_is_stressed():
    """A monosyllable is treated as stressed, so its vowel is not reduced."""
    assert "ə" not in transcribe("gos", "ca")
    assert "u" not in transcribe("gos", "ca")
    assert "ə" not in transcribe("sol", "ca")


# ── Bug 2: Western varieties do NOT apply Central reduction ──

@pytest.mark.parametrize("code", ["ca-x-occidental", "ca-x-valencia"])
@pytest.mark.parametrize("word", ["casa", "dona", "tenir", "porta", "gos"])
def test_western_varieties_do_not_reduce(code, word):
    out = transcribe(word, code)
    assert "ə" not in out, f"{code} {word!r}: {out!r} unexpectedly has schwa"


def test_occidental_full_vowels():
    """North-Western keeps full vowels — and opens a word-final ⟨-a⟩ to [ɛ].

    The lleidatà final ⟨-a⟩ is [ɛ] (⟨una porta⟩ [ˈunɛ ˈpɔɾtɛ]) — neither the
    Central [ə] nor the Valencian [a] (Veny 1982 ch. 3; Recasens 1996).
    """
    assert transcribe("casa", "ca-x-occidental") == "ˈkazɛ"
    assert transcribe("tenir", "ca-x-occidental") == "teˈni"


def test_valencia_full_vowels():
    assert transcribe("casa", "ca-x-valencia") == "ˈkaza"
    assert transcribe("tenir", "ca-x-valencia") == "teˈniɾ"


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


def test_no_spirantization_before_a_lateral():
    """/b ɡ/ before a lateral GEMINATE rather than lenite.

    ⟨poble⟩ is [ˈpɔbːlə] and ⟨regla⟩ [ˈreɡːlə], not *[ˈpɔβlə] / *[ˈreɣlə]
    (Wheeler 2005 §5.2, §10.2) — the pre-lateral context is the one place a
    post-vocalic /b ɡ/ survives as a stop.
    """
    out = transcribe("poble", "ca")
    assert "β" not in out and "b" in out
    out = transcribe("regla", "ca")
    assert "ɣ" not in out and "ɡ" in out


def test_spirantization_after_a_non_vowel_continuant():
    """Lenition is not restricted to the strictly intervocalic context.

    /b d ɡ/ lenite after ANY continuant — ⟨arbre⟩ [ˈaɾβɾə], ⟨serveix⟩
    [sərˈβɛʃ] — so conditioning the rule on "between two vowels" alone
    misses the post-liquid and post-fricative cases (Wheeler 2005 §5.2).
    """
    assert "β" in transcribe("arbre", "ca")


@pytest.mark.parametrize("code", ["ca", "ca-x-occidental", "ca-x-valencia",
                                  "ca-x-balear"])
def test_spirantization_all_varieties(code):
    """Spirantization is on the shared base, so every variety inherits it."""
    assert "ð" in transcribe("cada", code)
