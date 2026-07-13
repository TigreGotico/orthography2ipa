"""Vowel-hood is decided per script by the SPEC, not by a Latin letter list.

The engine used to answer "is this grapheme a written vowel?" from a set of
Latin and Greek letters. Every vowel-conditioned position — ``INTERVOCALIC``,
``BEFORE_VOWEL``, ``AFTER_VOWEL``, the front/back vowel classes, the exact
``BEFORE_E``/``AFTER_A`` letters — and every vowel-conditioned allophone class
therefore could not fire in Devanagari, Cyrillic, Arabic, Hebrew or any other
script: a spec could declare them and they would be inert, silently, with no
error and no unmatched-rule warning.

These tests pin the fix down at the level that matters: a positional key that a
non-Latin spec declares must actually FIRE. The unit-level tests below guard the
two ways the derivation can go wrong — under-firing (back to the old bug) and
over-firing (classifying a consonant, or a whole syllable like ⟨ال⟩ → /al/, as a
vowel, which silently corrupts its neighbours' contexts).
"""
import pytest

from orthography2ipa import G2P, get
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.positional import grapheme_positions
from orthography2ipa.types import GraphemePosition
from orthography2ipa.vowels import (
    grapheme_is_vowel,
    grapheme_vowel_axis,
    is_nucleus_only,
    is_orthographic_vowel,
)


def _positions(lang: str, word: str, grapheme: str):
    """Every position offered to any occurrence of *grapheme* inside *word*."""
    tok = PhonetokTokenizer(get(lang))
    seen = set()
    hit = False
    for ctx in tok.tokenize_with_context(word):
        if ctx.grapheme == grapheme:
            hit = True
            seen.update(grapheme_positions(ctx))
    if not hit:
        raise AssertionError(f"{grapheme!r} not tokenised out of {word!r}")
    return seen


# ── The bug: a vowel-conditioned position must FIRE outside Latin ──────────


@pytest.mark.parametrize("lang, word, grapheme, position", [
    # Devanagari: ⟨आ⟩/⟨ा⟩ must be recognised as vowels, so a consonant between
    # them is INTERVOCALIC. (hi declares no vowel-conditioned rule of its own —
    # its ⟨ड⟩ intervocalic entry was removed as a wrong analysis; the flap is the
    # separate nukta letter ⟨ड़⟩. What is asserted here is that the POSITION is
    # computed, which is the bug: before this, it never could be.)
    ("hi", "आडा", "ड", GraphemePosition.INTERVOCALIC),
    ("hi", "आडा", "ड", GraphemePosition.BEFORE_VOWEL),
    ("hi", "आडा", "ड", GraphemePosition.AFTER_VOWEL),
    # Cyrillic: ru declares ⟨я⟩ after_vowel → /ja/ (iotation).
    ("ru", "моя", "я", GraphemePosition.AFTER_VOWEL),
    ("ru", "мая", "я", GraphemePosition.AFTER_VOWEL),
    # Arabic: ar declares ⟨أ⟩ before_vowel → /ʔ/ and ⟨ة⟩ after_vowel → ∅.
    ("ar", "أنأى", "أ", GraphemePosition.BEFORE_VOWEL),
    ("ar", "امرأة", "أ", GraphemePosition.BEFORE_VOWEL),
    ("ar", "قناة", "ة", GraphemePosition.WORD_FINAL),
])
def test_vowel_conditioned_position_fires_in_non_latin_script(
        lang, word, grapheme, position):
    assert position in _positions(lang, word, grapheme)


def test_intervocalic_actually_changes_the_transcription():
    """Arabic ⟨ة⟩ (ta marbuta) elides after a vowel — a rule ar always declared
    and that could never fire, because Arabic letters were not vowels."""
    g2p = G2P("ar")
    # إحالة: the final ⟨ة⟩ follows a vowel and drops.
    assert not str(g2p.transcribe("إحالة")).lstrip("ˈˌ").endswith("t")
    # …and ⟨أ⟩ before a vowel is the glottal stop.
    assert str(g2p.transcribe("أنأى")).lstrip("ˈˌ").startswith("ʔ")


def test_after_vowel_actually_changes_the_transcription():
    """Russian ⟨я⟩ after a vowel is /ja/, not /a/."""
    assert "ja" in str(G2P("ru").transcribe("моя"))


# ── Non-Latin vowel letters and their front/back axis ──────────────────────


@pytest.mark.parametrize("lang, grapheme", [
    ("hi", "आ"), ("hi", "ि"), ("hi", "ौ"), ("hi", "ऋ"),   # Devanagari
    ("ru", "а"), ("ru", "ы"), ("ru", "я"),                 # Cyrillic
    ("ar", "ى"), ("ar", "ِ"),                              # Arabic
])
def test_non_latin_vowel_graphemes_are_vowels(lang, grapheme):
    spec = get(lang)
    assert grapheme_is_vowel(grapheme, spec.graphemes[grapheme])


@pytest.mark.parametrize("lang, grapheme", [
    ("hi", "क"),    # abugida consonant: /kə/ carries a vowel but is not one
    ("hi", "य"),    # bare glide /j/
    ("ru", "б"), ("ru", "й"),
    ("ar", "ال"),   # a whole syllable /al/ — not a vowel grapheme
    ("he", "ב"),
])
def test_non_latin_consonant_graphemes_are_not_vowels(lang, grapheme):
    spec = get(lang)
    assert not grapheme_is_vowel(grapheme, spec.graphemes[grapheme])


def test_front_back_axis_derives_from_the_ipa_outside_latin():
    spec = get("hi")
    assert grapheme_vowel_axis("ि", spec.graphemes["ि"]) == "front"   # /ɪ/
    assert grapheme_vowel_axis("ु", spec.graphemes["ु"]) == "back"    # /ʊ/
    # A central vowel belongs to neither axis, exactly as ⟨å⟩ does.
    assert grapheme_vowel_axis("अ", spec.graphemes["अ"]) is None      # /ə/


# ── The nucleus test the derivation rests on ──────────────────────────────


@pytest.mark.parametrize("ipa, expected", [
    ("a", True), ("aː", True), ("ɛː", True), ("ẽ", True),
    ("r̩", True),        # syllabic consonant: a nucleus
    ("ja", True),        # iotated vowel letter: on-glide + nucleus
    ("j", False),        # bare glide
    ("kə", False),       # abugida consonant + inherent vowel
    ("al", False),       # a syllable, not a vowel
    ("b", False), ("ʔ", False), ("", False),
    ("̃", False),         # a bare mark is no nucleus (Devanagari anusvāra)
])
def test_is_nucleus_only(ipa, expected):
    assert is_nucleus_only(ipa) is expected


# ── Latin and Greek must be untouched by all of the above ─────────────────


@pytest.mark.parametrize("grapheme, ipa", [
    ("y", ["i"]),      # ⟨y⟩ is not in the Latin vowel-letter set: still not one
    ("w", ["u"]),      # even when a spec maps it to a vowel
    ("r", ["r̩"]),      # Czech syllabic ⟨r⟩: a consonant letter all the same
    ("b", ["b"]),
])
def test_latin_letters_keep_the_letter_set_answer(grapheme, ipa):
    """The letter set closes the Latin inventory: a spec's IPA cannot promote a
    Latin consonant letter to a vowel (that would change existing languages)."""
    assert grapheme_is_vowel(grapheme, ipa) is is_orthographic_vowel(grapheme)


@pytest.mark.parametrize("grapheme", list("aeiouáéíóúäöüαεηιουω"))
def test_latin_and_greek_vowels_stay_vowels_without_any_ipa(grapheme):
    assert grapheme_is_vowel(grapheme, [])


def test_transliteration_symbols_are_never_vowels():
    """Buckwalter presses ASCII symbols into service (⟨>⟩ = hamza). A symbol is
    neither a letter nor a mark, so it can never be a written vowel."""
    spec = get("ar-Latn-buckwalter")
    for grapheme, ipa in spec.graphemes.items():
        if not grapheme[0].isalpha():
            assert not grapheme_is_vowel(grapheme, ipa), grapheme
