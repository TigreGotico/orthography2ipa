"""Tests for the ``mutates_neighbor`` / ``mutates_neighbor_side`` allophone
rule fields — the "marker grapheme" pattern.

Motivation (issue #743, the Manx/Gaelic slender-vowel gap): Goidelic
orthographies use a written vowel letter (⟨i⟩/⟨e⟩) to mark that the
ADJACENT consonant is palatalized ("slender"), without the vowel itself
surfacing: Manx ``giare`` [ɡʲɛːr], ``dowin`` [daunʲ]. The existing
``allophone_rules`` vocabulary rewrites a phoneme's OWN surface form
(``surface``); it had no way for one rule to delete its own slot while
simultaneously mutating a DIFFERENT (neighbouring) slot. ``mutates_neighbor``
(the IPA feature to add, e.g. ``"ʲ"``) + ``mutates_neighbor_side``
(``"preceding"``/``"following"``, which neighbour receives it) is the
generic, language-agnostic mechanism this PR adds.

These are synthetic-spec mechanism tests, mirroring the style of
``test_allophone_rules.py``; the real-language application (Manx slender
contexts) is exercised in ``test_manx_slender_marking.py``.
"""
from orthography2ipa.allophony import compile_allophone_rescorer
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.types import AllophoneRule, LanguageSpec


def _spec(graphemes, rules):
    return LanguageSpec(
        code="xx-test", name="Test", family="Test", script="Latin",
        graphemes=graphemes, allophones={}, allophone_rules=tuple(rules),
    )


def _tok_best(spec, word):
    tok = PhonetokTokenizer(spec)
    resc = compile_allophone_rescorer(spec.allophone_rules)
    return tok.ipa_best(word, rescorer=resc)


# A minimal synthetic slender-marking spec: ⟨g⟩ = /ɡ/, a "slender" ⟨i⟩ = /i/
# that (word-medially, before a consonant) deletes and palatalizes the
# PRECEDING consonant; a "broad" ⟨a⟩ = /a/ that never triggers anything.
_SLENDER_RULE = AllophoneRule(
    id="SLENDER_I_DELETE_PALATALIZE",
    phonemes=("i",), surface="",
    mutates_neighbor="ʲ", mutates_neighbor_side="preceding",
)


def test_marker_vowel_deletes_and_palatalizes_preceding_consonant():
    spec = _spec(
        {"g": ["ɡ"], "i": ["i"], "a": ["a"], "r": ["r"]},
        (_SLENDER_RULE,),
    )
    # 'gia' -> the 'i' deletes, 'g' becomes palatalized 'ɡʲ'
    assert _tok_best(spec, "gia") == "ɡʲa"


def test_marker_vowel_alone_is_unaffected_at_word_start():
    """No preceding consonant slot to mutate: the vowel still deletes."""
    spec = _spec(
        {"g": ["ɡ"], "i": ["i"], "a": ["a"], "r": ["r"]},
        (_SLENDER_RULE,),
    )
    assert _tok_best(spec, "ia") == "a"


def test_non_triggering_vowel_leaves_consonant_plain():
    spec = _spec(
        {"g": ["ɡ"], "i": ["i"], "a": ["a"], "r": ["r"]},
        (_SLENDER_RULE,),
    )
    assert _tok_best(spec, "ga") == "ɡa"


def test_following_side_palatalizes_the_next_consonant():
    """The mirror direction: a marker vowel palatalizing what comes AFTER
    it (e.g. a preceding-marked, following-mutating orthography convention)
    — exercises ``mutates_neighbor_side="following"``."""
    rule = AllophoneRule(
        id="SLENDER_I_DELETE_PALATALIZE_NEXT",
        phonemes=("i",), surface="",
        mutates_neighbor="ʲ", mutates_neighbor_side="following",
    )
    spec = _spec({"i": ["i"], "r": ["r"], "a": ["a"]}, (rule,))
    # 'ira' -> 'i' deletes, following 'r' becomes palatalized 'rʲ'
    assert _tok_best(spec, "ira") == "rʲa"


def test_condition_gated_marker_only_fires_word_finally():
    """A conditioned marker: only deletes/palatalizes word-finally (the
    Manx ``-in`` → [-ənʲ] shape), leaving a non-final occurrence alone."""
    rule = AllophoneRule(
        id="SLENDER_I_FINAL_ONLY",
        phonemes=("i",), surface="", word_final=True,
        mutates_neighbor="ʲ", mutates_neighbor_side="preceding",
    )
    spec = _spec({"n": ["n"], "i": ["i"], "a": ["a"]}, (rule,))
    assert _tok_best(spec, "ni") == "nʲ"     # word-final: deletes + palatalizes
    assert _tok_best(spec, "nia") == "nia"   # not word-final: rule inert


def test_absent_mutates_neighbor_is_byte_identical():
    """A spec with no mutates_neighbor rules behaves exactly as before."""
    spec = _spec({"g": ["ɡ"], "i": ["i"], "a": ["a"]}, ())
    assert _tok_best(spec, "gia") == "ɡia"
