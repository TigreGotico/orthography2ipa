"""Generic allophony primitives added for PR #856's ⟨-ed⟩ fix round.

Two engine-generic capabilities, tested here with a synthetic language so
they stand on their own outside en-GB:

* ``"any"`` neighbour class — matches any existing neighbour grapheme
  regardless of what class it is (as opposed to ``"word_boundary"``, which
  tests the ABSENCE of a neighbour). Closes a documented gap: before this,
  a rule that only cared *whether* a grapheme stood N away — not what kind
  — had to be declared as a redundant vowel/consonant pair.
* ``preceded_by_3`` — the ``preceded_by``/``preceded_by_2`` neighbour-class
  family, extended one grapheme further back. Combined with ``"any"`` this
  is the "is there a real stem in front of this ending" gate that English
  ⟨-ed⟩ needs (see ``tests/test_cited_rules_germanic.py`` for the live
  en-GB case: monosyllables like ``fed``/``ted`` whose ⟨ed⟩ IS the stem,
  not the past-tense suffix).
* ``preceded_by_surface_phoneme_2`` — like ``preceded_by_phoneme_2`` but
  reads the resolved SURFACE candidate of the slot two positions back,
  not the grapheme's first declared candidate. Needed whenever the
  declared candidate order disagrees with what actually gets selected —
  en-GB ⟨-ed⟩ devoicing must see the stem's actual (already-resolved)
  final consonant, not its citation-form voicing.
"""
from __future__ import annotations

from orthography2ipa.allophony import compile_allophone_rescorer
from orthography2ipa.phonetok import Candidate, PhonetokTokenizer
from orthography2ipa.rescorer import LatticeRescorer
from orthography2ipa.types import AllophoneRule, LanguageSpec


def _spec(graphemes, rules=(), *, code="xx-surf2"):
    return LanguageSpec(
        code=code, name="Test", family="Test", script="Latin",
        graphemes=graphemes, allophones={}, allophone_rules=tuple(rules),
    )


def _tok_best(spec, word, extra_rescorers=()):
    tok = PhonetokTokenizer(spec)
    resc = compile_allophone_rescorer(spec.allophone_rules)
    chain = list(extra_rescorers) + ([resc] if resc else [])
    return tok.ipa_best(word, rescorer=chain)


class _PromoteIPA(LatticeRescorer):
    """Reorders a specific grapheme's slot so *ipa* becomes the resolved
    top candidate — stands in for the positional/weight resolution stage
    (E2.1), which runs BEFORE allophone rescoring in the real pipeline and
    is what actually decides "s" is voiced intervocalically in a word like
    ``used`` long before any allophone rule sees it."""

    def __init__(self, grapheme: str, ipa: str) -> None:
        self.grapheme = grapheme
        self.ipa = ipa

    def rescore(self, slot, context):
        if slot.grapheme != self.grapheme:
            return slot.candidates
        best = min(c.cost for c in slot.candidates)
        return [Candidate(self.ipa, best - 1.0)] + [
            c for c in slot.candidates if c.ipa != self.ipa
        ]


# ─── "any" neighbour class ──────────────────────────────────────────────

def test_any_matches_an_existing_neighbour_of_either_class():
    """``preceded_by_2="any"`` fires whether the neighbour is a vowel or a
    consonant — only the presence of A grapheme matters, not its class."""
    rule = AllophoneRule(
        id="ANY2", phonemes=("x",), surface="y", preceded_by_2="any")
    spec = _spec({"a": ["a"], "b": ["b"], "x": ["x"]}, (rule,))
    # "a" (vowel) two back from "x": ax? need 3 graphemes so "x" is 3rd.
    assert _tok_best(spec, "bax") == "bay"   # preceded_by_2 sees "b" (consonant)
    assert _tok_best(spec, "aax") == "aay"   # preceded_by_2 sees "a" (vowel)


def test_any_does_not_match_a_word_boundary():
    """``"any"`` requires an actual neighbour — it is not a wildcard that
    also accepts the word edge (that's what distinguishes it from simply
    omitting the condition)."""
    rule = AllophoneRule(
        id="ANY2_EDGE", phonemes=("x",), surface="y", preceded_by_2="any")
    spec = _spec({"a": ["a"], "x": ["x"]}, (rule,))
    # Only one grapheme before "x" -> no grapheme two back -> must not fire.
    assert _tok_best(spec, "ax") == "ax"


# ─── preceded_by_3 ───────────────────────────────────────────────────────

def test_preceded_by_3_reads_three_graphemes_back():
    rule = AllophoneRule(
        id="P3", phonemes=("x",), surface="y", preceded_by_3="vowel")
    spec = _spec({"a": ["a"], "b": ["b"], "x": ["x"]}, (rule,))
    assert _tok_best(spec, "abbx") == "abby"   # "a" sits 3 graphemes back
    assert _tok_best(spec, "bbbx") == "bbbx"   # no vowel 3 back -> no-op


def test_preceded_by_3_any_is_a_stem_existence_gate():
    """The ``"any"`` + ``preceded_by_3`` combination used by en-GB ⟨-ed⟩:
    fires only when a real grapheme (of whatever class) stands three back,
    i.e. only when there is a stem in front of a short C-e-C-shaped tail."""
    rule = AllophoneRule(
        id="P3_ANY", phonemes=("x",), surface="y", preceded_by_3="any")
    spec = _spec({"a": ["a"], "b": ["b"], "x": ["x"]}, (rule,))
    assert _tok_best(spec, "abbx") == "abby"   # 4 graphemes: "a" exists at -3
    assert _tok_best(spec, "bbx") == "bbx"     # only 3 graphemes: -3 is out of bounds


# ─── preceded_by_surface_phoneme_2 ──────────────────────────────────────

def test_preceded_by_surface_phoneme_2_reads_the_resolved_slot_not_the_declared_candidate():
    """The declared candidate order for ``s`` lists the voiceless member
    first, but between two vowels it should resolve to voiced ``z`` before
    this rule ever runs (modelled here with an explicit low-cost voiced
    candidate). A rule keyed on ``preceded_by_phoneme_2`` (declared-candidate
    reading) would see the wrong (voiceless) phoneme two graphemes back;
    ``preceded_by_surface_phoneme_2`` must see the resolved surface one."""
    devoice = AllophoneRule(
        id="DEVOICE_SURF", phonemes=("d",), surface="t", grapheme=("d",),
        word_final=True, preceded_by_grapheme=("e",),
        preceded_by_surface_phoneme_2=("s",),
    )
    spec = _spec(
        {
            "u": ["u"],
            # Declared order lists "s" (voiceless, citation form) first.
            "s": ["s", "z"],
            "e": ["", "e"],
            "d": ["d"],
        },
        (devoice,),
    )
    # The positional/weight stage resolves stem-final "s" to voiced [z]
    # (modelled here by promoting it before the allophone pass runs) ->
    # devoicing must NOT fire.
    assert _tok_best(spec, "used", [_PromoteIPA("s", "z")]) == "uzd"


def test_preceded_by_surface_phoneme_2_fires_when_the_resolved_stem_is_voiceless():
    devoice = AllophoneRule(
        id="DEVOICE_SURF2", phonemes=("d",), surface="t", grapheme=("d",),
        word_final=True, preceded_by_grapheme=("e",),
        preceded_by_surface_phoneme_2=("s",),
    )
    spec = _spec(
        {
            "m": ["m"],
            "s": ["s"],
            "e": ["", "e"],
            "d": ["d"],
        },
        (devoice,),
    )
    assert _tok_best(spec, "msed") == "mst"


# ─── affricate atoms register for preceded_by_phoneme_2 families ───────

def test_preceded_by_surface_phoneme_2_sees_a_multichar_affricate_whole():
    """A stem ending in an affricate (declared as a single multi-character
    phoneme, e.g. ``tʃ``) must be matched as ONE segment two graphemes
    back, not split into its component letters by generic segmentation —
    the ``_rule_atoms`` collection must include ``preceded_by_surface_phoneme_2``
    (and ``preceded_by_phoneme_2``/``followed_by_phoneme_2``) values."""
    devoice = AllophoneRule(
        id="DEVOICE_AFFR", phonemes=("d",), surface="t", grapheme=("d",),
        word_final=True, preceded_by_grapheme=("e",),
        preceded_by_surface_phoneme_2=("tʃ",),
    )
    spec = _spec(
        {
            "w": ["w"],
            "c": ["tʃ"],
            "e": ["", "e"],
            "d": ["d"],
        },
        (devoice,),
    )
    assert _tok_best(spec, "wced") == "wtʃt"
