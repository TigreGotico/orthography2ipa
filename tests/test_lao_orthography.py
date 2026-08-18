# -*- coding: utf-8 -*-
"""What the Lao spec claims about the Lao writing system, pinned as values.

Lao writes its vowels with signs that surround the consonant, closes its
syllables on a small permitted set, and uses ⟨ຫ⟩ before a sonorant as a
tone-class marker rather than as an /h/. Each group below pins the reading
the spec asserts AND a case where the same rule must not fire, because a
Lao rule that over-applies looks exactly like a correct one on the words it
was written for.

Source: Enfield, N.J. (2007), *A Grammar of Lao*, Mouton de Gruyter.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def lo():
    return G2P("lo")


# ═══════════════════════════════════════════════════════════════════════════
# Vowel signs the spec had not encoded at all
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,ipa", [
    ("ສະ", "saʔ"),        # ⟨ະ⟩ short /a/, glottal-checked in an open syllable
    ("ວັດ", "ʋat̚"),       # ⟨ັ⟩ short /a/ in a closed syllable
    ("ລົດ", "lot̚"),       # ⟨ົ⟩ short /o/ in a closed syllable
    ("ນ້ຳ", "nam"),   # ⟨ຳ⟩ /am/
    ("ນຳ", "nam"),        # same nucleus with no tone mark in the way
    ("ປຽບ", "piːəp̚"),     # ⟨ຽ⟩ /iːə/
    ("ຫໍ", "hɔː"),        # ⟨ໍ⟩ /ɔː/
])
def test_a_written_vowel_sign_is_read(lo, word, ipa):
    assert lo.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("ເສືອ", "sɯːə"),      # ⟨ເ◌ືອ⟩ the long ua-type diphthong
    ("ເມືອງ", "mɯːəŋ"),
    ("ເຮົາ", "haw"),       # ⟨ເ◌ົາ⟩ /aw/
    ("ຫົວ", "huːə"),       # ⟨◌ົວ⟩ /uːə/
    ("ເກາະ", "kɔʔ"),       # ⟨ເ◌າະ⟩ short /ɔ/, glottal-checked
])
def test_a_circumfix_vowel_is_read_as_one_nucleus(lo, word, ipa):
    assert lo.transcribe(word) == ipa


# ═══════════════════════════════════════════════════════════════════════════
# Coda phonotactics: only /p t k m n ŋ w j/ may close a Lao syllable
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,ipa", [
    ("ລົດ", "lot̚"),        # ⟨ດ⟩ coda → unreleased [t̚]
    ("ດອກ", "dɔːk̚"),       # ⟨ກ⟩ coda → [k̚]
    ("ຂອຍ", "kʰɔːj"),       # ⟨ຍ⟩ onset /ɲ/ but coda /j/
    ("ຂ້ອຍ", "kʰɔːj"),
    ("ລາວ", "laːw"),        # ⟨ວ⟩ onset /ʋ/ but coda /w/
    ("ພຸດທະ", "pʰut̚tʰaʔ"),  # coda neutralisation inside the word, not only finally
])
def test_a_coda_consonant_neutralises(lo, word, ipa):
    assert lo.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("ດີ", "diː"),      # onset ⟨ດ⟩ stays /d/ — the coda rule must not reach it
    ("ວັດ", "ʋat̚"),     # onset ⟨ວ⟩ stays /ʋ/
    ("ບານ", "baːn"),    # onset ⟨ບ⟩ stays /b/
    ("ບ້ານ", "baːn"),
])
def test_an_onset_consonant_is_not_neutralised(lo, word, ipa):
    assert lo.transcribe(word) == ipa


# ═══════════════════════════════════════════════════════════════════════════
# ho nam: ⟨ຫ⟩ before a sonorant is a tone-class marker, not an /h/
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,ipa", [
    ("ຫລອດ", "lɔːt̚"),    # ⟨ຫລ⟩
    ("ຫຼາຍ", "laːj"),     # ⟨ຫຼ⟩ with the subscript lo ⟨ຼ⟩
    ("ຫມາ", "maː"),      # ⟨ຫມ⟩
    ("ຫວານ", "ʋaːn"),    # ⟨ຫວ⟩ — the sonorant keeps its onset /ʋ/
    ("ໝາກ", "maːk̚"),     # ⟨ໝ⟩, the single-codepoint ligature of ⟨ຫ⟩+⟨ມ⟩
    ("ໜັງສື", "naŋsɯː"),  # ⟨ໜ⟩
])
def test_ho_nam_leaves_the_sonorant_as_the_onset(lo, word, ipa):
    assert lo.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("ຫໍ", "hɔː"),      # ⟨ຫ⟩ before a vowel is a real /h/
    ("ຫ້າ", "haː"),
    ("ຫົວ", "huːə"),
])
def test_ho_before_a_vowel_is_still_an_h(lo, word, ipa):
    assert lo.transcribe(word) == ipa


# ═══════════════════════════════════════════════════════════════════════════
# ⟨ອ⟩ has two jobs, and the following vowel is what tells them apart
# ═══════════════════════════════════════════════════════════════════════════

def test_o_after_an_onset_is_the_vowel(lo):
    assert lo.transcribe("ດອກ") == "dɔːk̚"
    assert lo.transcribe("ອອດ") == "ʔɔːt̚"


def test_o_opening_a_syllable_is_the_zero_onset_carrier(lo):
    assert lo.transcribe("ອິດ") == "ʔit̚"
    assert lo.transcribe("ອາ") == "ʔaː"


# ═══════════════════════════════════════════════════════════════════════════
# ⟨ຣ⟩ merged with /l/ in the modern language
# ═══════════════════════════════════════════════════════════════════════════

def test_ro_is_read_as_l(lo):
    assert lo.transcribe("ໂຣດ") == "loːt̚"


def test_a_tone_mark_spells_no_segment(lo):
    # The tone marks are recorded in tone_inventory and contribute nothing
    # to the segmental string; ⟨ຫ້າ⟩ and ⟨ຫາ⟩ differ only in tone.
    assert lo.transcribe("ຫ້າ") == lo.transcribe("ຫາ") == "haː"


# ═══════════════════════════════════════════════════════════════════════════
# A preposed vowel sign attaches to an onset, never to a vowel letter
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,ipa", [
    ("ເອກ", "ʔeːk̚"),
    ("ແອກ", "ʔɛːk̚"),
    ("ໂອ", "ʔoː"),
    ("ໄອ", "ʔaj"),
])
def test_o_after_a_preposed_sign_is_the_carrier(lo, word, ipa):
    # ⟨ອ⟩ is the vowel /ɔː/ after an onset, but a preposed sign IS its
    # syllable's nucleus, so what follows it is the onset slot: the carrier.
    assert lo.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("ເຫຼົ້າ", "law"),
    ("ແຫຼມ", "lɛːm"),
    ("ໂຫຼດ", "loːt̚"),
])
def test_a_preposed_sign_is_silenced_before_the_subscript_lo_digraph(lo, word,
                                                                    ipa):
    # ⟨ຫຼ⟩ ends in a combining mark but spells the consonant /l/, so it takes
    # the preposed sign's reading exactly as the full ⟨ຫລ⟩ spelling does.
    assert lo.transcribe(word) == lo.transcribe(word.replace("ຫຼ", "ຫລ"))
    assert lo.transcribe(word) == ipa


def test_the_ho_nam_onset_is_not_read_as_a_coda(lo):
    # ⟨ຫຼວງ⟩ opens on /l/; nothing in the coda phonotactics reaches an onset.
    assert lo.transcribe("ຫຼວງ")[0] == "l"


@pytest.mark.parametrize("word", [
    "ຟ້າ", "ບ່າ", "ຊ້າ", "ແກ້ວ", "ນ້ຳ",
    # Circumfix vowels whose postposed half a tone mark interrupts in the
    # writing (Lao ⟨ເ◌ົ້າ⟩ = ⟨ເ⟩ + C + ⟨ົ⟩ + tone mark + ⟨າ⟩): the mark
    # must stay transparent to the multigraph match the way it already
    # is to ``_syllable_position``, or the postposed half never completes
    # and ⟨ເຂົ້າ⟩ reads as */kʰoaː/ instead of /kʰaw/.
    "ເຂົ້າ", "ເຈົ້າ", "ເຫຼົ້າ", "ເບື້ອງ",
])
def test_a_tone_mark_does_not_change_the_segments(lo, word):
    bare = word.translate({ord(c): None for c in "່້໊໋"})
    assert lo.transcribe(word) == lo.transcribe(bare)


# ═══════════════════════════════════════════════════════════════════════════
# Known gaps — documented in the spec notes, not encoded around
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.xfail(
    reason="the ho-nam digraph ⟨ຫຼ⟩ does not form word-finally: a preposed "
           "vowel attaches to the single grapheme before it, not the "
           "longest digraph match, so a trailing subscript lo surfaces as "
           "a stray coda /l/ instead of completing the ho-nam reading",
    strict=True,
)
def test_the_ho_nam_digraph_forms_word_finally(lo):
    # Gold: ʔaː˩˧loː˩˧ (tone letters aside, ʔaːloː segmentally).
    assert lo.transcribe("ອາໂຫຼ") == "ʔaːloː"


@pytest.mark.xfail(
    reason="⟨ເ...ອ⟩ is a preposed-sign/⟨ອ⟩ circumfix, like ⟨ເ◌ີ⟩, and is "
           "not encoded for the same reason: the vowel key cannot see "
           "which preposed sign it belongs to",
    strict=True,
)
def test_the_e_o_circumfix_keeps_its_preposed_nucleus(lo):
    assert lo.transcribe("ເສອ") == "seːɔː"


@pytest.mark.xfail(
    reason="bare ⟨◌ວ◌⟩ — the letter ⟨ວ⟩ between two other consonant "
           "letters with no vowel sign anywhere in the word — is itself "
           "the nucleus /uːə/ (12/12 kaikki gold words with no vowel sign "
           "at all agree: ⟨ພວກ⟩ /pʰuːə̯k̚/, ⟨ຫຼວງ⟩ /luːə̯ŋ/...; ignoring that "
           "condition and only requiring the C-⟨ວ⟩-C letters widens the "
           "set to 36/40, the 4 exceptions all carrying a preposed vowel "
           "sign elsewhere in the word that turns ⟨ວ⟩ into that vowel's "
           "own onset or coda instead, e.g. ⟨ແຫວນ⟩ /ʋɛːn/). The spec "
           "currently gives ⟨ວ⟩ only its onset "
           "/ʋ/ and coda /w/ readings; a positional entry needs a joint "
           "after-consonant-AND-before-consonant condition the engine's "
           "positional lookup does not expose as a single key, so this is "
           "tracked as a known gap rather than encoded around.",
    strict=True,
)
def test_bare_wa_between_consonants_is_the_nucleus(lo):
    assert lo.transcribe("ຫຼວງ") == "luːə̯ŋ"
