"""Engine capability: SECONDARY STRESS — a second prominence level.

Language-agnostic tests over a synthetic spec. Word prominence is a metrical
grid with levels, not a stressed/unstressed switch: syllables group into feet,
each foot has a head, and one head is promoted to the word accent while the
others stay metrically strong (Liberman & Prince 1977, *On Stress and
Linguistic Rhythm*, LI 8; Hayes 1995, *Metrical Stress Theory*, ch. 2-3).

What the level does, and the reason it exists: a secondary foot head is NOT
unstressed, so it stops matching a spec's ``nucleus_unstressed`` entry and the
reduction written there no longer reaches it.
"""
import dataclasses

import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.positional import grapheme_positions
from orthography2ipa.phonetok import flat_contexts, PhonetokTokenizer
from orthography2ipa.stress import (
    SECONDARY_ALTERNATING, apply_stress_mark, secondary_stress_positions,
)
from orthography2ipa.types import GraphemePosition, StressRules


PLAIN = StressRules(default_position=1)
ALTERNATING = StressRules(default_position=1,
                          secondary_stress=SECONDARY_ALTERNATING)


# ── placement ───────────────────────────────────────────────────────────

def test_no_secondary_level_without_the_declaration():
    """The default is the binary system every existing spec has: no spec
    that omits ``secondary_stress`` gains a level."""
    assert PLAIN.secondary_stress == ""
    assert secondary_stress_positions(5, 3, PLAIN) == frozenset()


@pytest.mark.parametrize("n,primary,expected", [
    (4, 2, {0}),      # ˌcombiˈnation — com-bi-na-tion
    (5, 3, {1}),      # reˌpreseˈntative shape: heads at 1 and 3
    (5, 4, {0, 2}),   # two feet built leftward
    (6, 4, {0, 2}),
    (3, 2, {0}),
])
def test_alternating_builds_binary_feet_leftward(n, primary, expected):
    """Binary, quantity-insensitive feet built leftward from the main stress
    (Hayes 1995 ch. 3): every second syllable before it is a foot head."""
    assert secondary_stress_positions(n, primary, ALTERNATING) == expected


@pytest.mark.parametrize("n,primary", [(2, 0), (2, 1), (3, 0), (4, 1), (5, 0)])
def test_no_room_for_a_foot_marks_nothing(n, primary):
    """A main stress on the first or second syllable leaves no syllable two
    positions to its left, so there is no foot head to promote."""
    assert secondary_stress_positions(n, primary, ALTERNATING) == frozenset()


def test_unplaceable_main_stress_defines_no_level_below_it():
    """A level below the main accent is only definable relative to a known
    main accent — a clitic (negative sentinel) or an end-anchored index
    yields nothing rather than a guess."""
    assert secondary_stress_positions(5, -1, ALTERNATING) == frozenset()
    assert secondary_stress_positions(5, -99, ALTERNATING) == frozenset()


def test_a_syllable_never_carries_two_levels():
    """The main-stress syllable is never in the secondary set."""
    for n in range(1, 9):
        for primary in range(n):
            assert primary not in secondary_stress_positions(
                n, primary, ALTERNATING)


# ── the positional consequence (this is the point) ──────────────────────

def _positions(word, spec, tok_index, syll_idx, primary, secondary):
    """Positions emitted for the *tok_index*-th grapheme that carries a
    nucleus (a vowel token), under the given prominence assignment."""
    tokenizer = PhonetokTokenizer(spec)
    tokens = tokenizer.grapheme_tokens(word)
    contexts = flat_contexts(tokens, spec.vowel_graphemes)
    vowels = [c for c in contexts if c.is_vowel]
    return grapheme_positions(
        vowels[tok_index], spec=spec, syll_idx=syll_idx,
        stressed_syll_idx=primary, secondary_syll_idxs=frozenset(secondary))


@pytest.fixture(scope="module")
def spec():
    from orthography2ipa import get
    return get("en-GB")


def test_secondary_nucleus_replaces_the_unstressed_position(spec):
    """A secondary foot head gets ``nucleus_secondary`` and NOT
    ``nucleus_unstressed`` — the reduction entry can no longer reach it."""
    pos = _positions("combination", spec, 0, 0, 2, {0})
    assert GraphemePosition.NUCLEUS_SECONDARY in pos
    assert GraphemePosition.NUCLEUS_UNSTRESSED not in pos
    assert GraphemePosition.NUCLEUS_UNSTRESSED_OPEN not in pos
    assert GraphemePosition.NUCLEUS_UNSTRESSED_CLOSED not in pos


def test_same_syllable_is_unstressed_without_the_level(spec):
    """Fail-before control: with no secondary set the SAME grapheme is
    unstressed, so the difference is the capability and nothing else."""
    pos = _positions("combination", spec, 0, 0, 2, set())
    assert GraphemePosition.NUCLEUS_UNSTRESSED in pos
    assert GraphemePosition.NUCLEUS_SECONDARY not in pos


def test_position_relative_to_the_main_stress_is_kept(spec):
    """``pretonic``/``posttonic`` state WHERE a syllable is, not how strong
    it is; a secondary head keeps them."""
    pos = _positions("combination", spec, 0, 0, 2, {0})
    assert GraphemePosition.PRETONIC in pos


def test_main_stress_outranks_a_stray_secondary_claim(spec):
    """A syllable claimed by both levels is the main stress: nothing else."""
    pos = _positions("combination", spec, 0, 0, 0, {0})
    assert GraphemePosition.NUCLEUS_STRESSED in pos
    assert GraphemePosition.NUCLEUS_SECONDARY not in pos


# ── the IPA mark ────────────────────────────────────────────────────────

def test_secondary_mark_is_written_before_its_foot_head():
    marked = apply_stress_mark("kombineiʃon", ALTERNATING, 2,
                               syllables=["kom", "bi", "na", "tion"],
                               secondary_indices=[0])
    assert marked.startswith("ˌ")
    assert marked.count("ˌ") == 1 and marked.count("ˈ") == 1
    assert marked.index("ˌ") < marked.index("ˈ")
    assert marked.replace("ˌ", "").replace("ˈ", "") == "kombineiʃon"


def test_a_mark_is_never_written_inside_a_long_vowel():
    """The bundled splitter is a vowel-group splitter over the IPA, so it can
    cut a long vowel in half (``sɜː`` → ``sɜ|ː…``). A length mark at the head
    of a syllable belongs to the vowel BEFORE it, so the stress mark goes
    after it — never ``sɜˌːkʌm``, which claims a syllable starts with half a
    nucleus."""
    out = apply_stress_mark("sɜːkʌmləkjuːʃən", ALTERNATING, 3,
                            syllables=["cir", "cum", "lo", "cu", "tion"],
                            secondary_indices=[1])
    assert "ˌː" not in out and "ˈː" not in out
    assert out.replace("ˌ", "").replace("ˈ", "") == "sɜːkʌmləkjuːʃən"


def test_english_marks_never_land_inside_a_long_vowel():
    """End to end, on the word that exposed it."""
    out = G2P("en-GB").transcribe_word("circumlocution")
    assert "ˌː" not in out and "ˈː" not in out
    assert out.startswith("sɜː")


def test_no_secondary_indices_leaves_the_transcription_as_before():
    assert apply_stress_mark("kombineiʃon", ALTERNATING, 2,
                             syllables=["kom", "bi", "na", "tion"]) == (
        apply_stress_mark("kombineiʃon", PLAIN, 2,
                          syllables=["kom", "bi", "na", "tion"]))


def test_a_secondary_index_on_the_main_stress_is_dropped():
    """One syllable, one mark — never ``ˌˈ``."""
    out = apply_stress_mark("kombineiʃon", ALTERNATING, 2,
                            syllables=["kom", "bi", "na", "tion"],
                            secondary_indices=[2])
    assert "ˌ" not in out
    assert out.count("ˈ") == 1


def test_two_secondary_indices_collapsing_onto_one_slot_mark_once():
    """The IPA can have fewer syllables than the spelling; two orthographic
    heads that land on the same IPA syllable must not double-mark it."""
    out = apply_stress_mark("kombina", ALTERNATING, 4,
                            syllables=["ko", "m", "bi", "n", "a"],
                            secondary_indices=[0, 2])
    assert out.count("ˌ") <= 2
    assert "ˌˌ" not in out


# ── blast radius ────────────────────────────────────────────────────────

def test_declaring_nothing_changes_nothing_end_to_end():
    """A spec without the declaration keeps ONE stress mark and no ``ˌ`` — the
    values are pinned, so a future prominence change that leaked outside the
    opted-in specs breaks this test instead of passing it."""
    g = G2P("pt-PT")
    assert g.spec.stress.secondary_stress == ""
    assert g.transcribe_word("combinação") == "kõbinɐˈsɐ̃w̃"
    assert g.transcribe_word("responsabilidade") == "ʁɨʃpõsɐbiliˈdadɨ"


def test_stressrules_default_keeps_the_binary_system():
    assert StressRules().secondary_stress == ""
    assert dataclasses.replace(
        StressRules(), secondary_stress=SECONDARY_ALTERNATING
    ).secondary_stress == "alternating"
