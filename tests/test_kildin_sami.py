"""Kildin Sami (`sjd`) — the palatalisation signs Ь and Ҍ.

Kildin Sami contrasts plain, half-palatalised and palatal consonants. The Kola
Saami Documentation Project (DoBeS, MPI Nijmegen,
https://dobes.mpi.nl/projects/sami/language/) gives the minimal triple
манн /manː/ 'moon', маннҍ /manːʲ/ 'egg', маннь /maɲː/ 'daughter-in-law', so the
sign is a segmental instruction on the consonant before it, not a lexical
diacritic.

Expected strings are written from that contrast plus the base letter values in
the spec's own grapheme table, not read back from the engine.

Ь and Ҍ are single graphemes reading ʲ, which the engine composes onto the
consonant before them. Only ⟨ль⟩, ⟨сь⟩, ⟨хь⟩ and ⟨нь⟩ hold keys of their own,
because their value is a palatal segment rather than the concatenation of the
letter's value with ʲ.
"""
import pytest

import orthography2ipa as o2i


@pytest.fixture(scope="module")
def sjd():
    return o2i.G2P("sjd")


def strip_stress(s):
    return s.replace("ˈ", "").replace("ˌ", "")


@pytest.mark.parametrize("spelling,ipa", [
    # ⟨ь⟩ on a consonant that has no palatal counterpart adds ʲ
    ("рь", "rʲ"),
    ("кь", "kʲ"),
    ("вь", "vʲ"),
    ("пь", "pʲ"),
    ("мь", "mʲ"),
    ("бь", "bʲ"),
    ("фь", "fʲ"),
    ("зь", "zʲ"),
    ("жь", "ʒʲ"),
    ("гь", "ɡʲ"),
    ("ӈь", "ŋʲ"),
    ("шь", "ʃʲ"),
    ("ць", "tsʲ"),
    # voiceless sonorants keep their own diacritic and take ʲ on top
    ("ӆь", "l̥ʲ"),
    ("ҏь", "r̥ʲ"),
    # ⟨ль сь хь⟩ are the palatal segments
    ("ль", "ʎ"),
    ("сь", "ɕ"),
    ("хь", "ç"),
])
def test_soft_sign_palatalises_the_preceding_consonant(sjd, spelling, ipa):
    assert strip_stress(sjd.transcribe_word(spelling)) == ipa


@pytest.mark.parametrize("spelling,ipa", [
    # Ҍ is the half-palatalisation sign, used on the dentals
    ("тҍ", "tʲ"),
    ("дҍ", "dʲ"),
    ("нҍ", "nʲ"),
])
def test_semisoft_sign_is_half_palatalisation(sjd, spelling, ipa):
    assert strip_stress(sjd.transcribe_word(spelling)) == ipa


def test_n_before_the_two_signs_is_the_dobes_minimal_pair(sjd):
    """⟨нь⟩ is the palatal nasal, ⟨нҍ⟩ only half-palatalised — DoBeS маннь ~ маннҍ."""
    assert strip_stress(sjd.transcribe_word("нь")) == "ɲ"
    assert strip_stress(sjd.transcribe_word("нҍ")) == "nʲ"
    assert strip_stress(sjd.transcribe_word("нь")) != strip_stress(
        sjd.transcribe_word("нҍ"))


def test_the_sign_is_not_a_silent_letter(sjd):
    """A sign-bearing word and its sign-less counterpart must not transcribe alike."""
    plain = strip_stress(sjd.transcribe_word("ман"))
    palatal = strip_stress(sjd.transcribe_word("мань"))
    assert plain != palatal
    assert palatal.endswith("ɲ")


@pytest.mark.parametrize("spelling,expected_segment", [
    ("а̄льп", "ʎ"),      # sign closing a cluster still palatalises its own consonant
    ("та̄ссьт", "ɕ"),
    ("а̄ббьрь", "rʲ"),
    ("ка̄ццькэ", "tsʲ"),
])
def test_sign_inside_a_word(sjd, spelling, expected_segment):
    assert expected_segment in sjd.transcribe_word(spelling)


def test_palatalisation_does_not_spread_rightward(sjd):
    """⟨а̄льп⟩ palatalises ⟨л⟩ only; ⟨п⟩ after the sign stays plain.

    Rightward spread is not regular in either shipped gold: the WikiPron gold
    writes the following consonant as palatalised in 75 of 150 sign-plus-
    consonant contexts, and NorthEuraLex in 5 of 209.
    """
    assert "pʲ" not in sjd.transcribe_word("а̄льп")


def test_hard_sign_is_not_a_palatalisation_sign(sjd):
    """⟨ъ⟩ separates rather than palatalises — ⟨куллъе⟩ keeps the ⟨е⟩ glide."""
    out = strip_stress(sjd.transcribe_word("куллъе"))
    assert "je" in out
    assert "ʎ" not in out
