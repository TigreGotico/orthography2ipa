"""Open/closed-syllable (aperture) positional grapheme keys.

The mid-vowel alternations of Romance (the *loi de position*) and the
Germanic open-syllable length alternation are conditioned on whether the
nucleus sits in a syllable WITH a coda, not on stress and not on the
neighbouring letters. These tests cover the new
``OPEN_SYLLABLE``/``CLOSED_SYLLABLE`` positions, their stress-crossed
variants, the "aperture unknown" cases that must emit nothing, and the
French ⟨eu⟩ data that is the first consumer.
"""
from dataclasses import replace

import pytest

from orthography2ipa import G2P, get
from orthography2ipa.phonetok import flat_contexts
from orthography2ipa.positional import (_is_open_syllable,
                                        grapheme_positions,
                                        match_grammatical_ending)
from orthography2ipa.types import GraphemePosition as GP


@pytest.mark.parametrize("syllable,expected", [
    ("heu", True),      # ends in a vowel letter → open
    ("meur", False),    # ends in a consonant letter → closed
    ("le", True),
    ("lek", False),
    ("", None),         # nothing to judge
    (None, None),       # no syllabification available
    ("str", None),      # no vowel at all → undecidable, not "closed"
])
def test_is_open_syllable(syllable, expected):
    assert _is_open_syllable(syllable) is expected


def _positions(lang, word, tok_index, *, stressed=None):
    engine = G2P(lang)
    tokens = engine._tokenizer.grapheme_tokens(word)
    contexts = flat_contexts(tokens, engine.spec.vowel_graphemes)
    sylls = engine._syllables_cached(word)
    syll_for_token = engine._map_tokens_to_syllables(tokens, sylls)
    idx = syll_for_token[tok_index]
    return grapheme_positions(
        contexts[tok_index], spec=engine.spec, syll_idx=idx,
        stressed_syll_idx=stressed,
        syllable=sylls[idx] if idx is not None and idx < len(sylls) else None)


def test_aperture_positions_are_emitted_for_a_nucleus():
    # escrimeur → e·scri·meur; the ⟨eu⟩ sits in the closed final syllable.
    positions = _positions("fr", "escrimeur", 6)
    assert GP.CLOSED_SYLLABLE in positions
    assert GP.OPEN_SYLLABLE not in positions


def test_aperture_positions_precede_the_stress_only_positions():
    positions = _positions("fr", "escrimeur", 6, stressed=2)
    assert positions.index(GP.NUCLEUS_STRESSED_CLOSED) < \
        positions.index(GP.CLOSED_SYLLABLE) < \
        positions.index(GP.NUCLEUS_STRESSED)


def test_aperture_needs_no_stress_rules():
    """French declares no ``stress`` block, yet aperture is still known.

    Syllabification depends on the word, not on the stress rules; gating
    it on ``spec.stress`` is what previously hid aperture from every
    stress-less spec.
    """
    assert get("fr-FR").stress is None
    positions = _positions("fr", "heureux", 1)
    assert GP.OPEN_SYLLABLE in positions
    # …and the stress-conditioned positions stay absent, as before.
    assert GP.NUCLEUS_STRESSED not in positions
    assert GP.NUCLEUS_STRESSED_OPEN not in positions


def test_no_syllable_means_no_aperture_position():
    positions = grapheme_positions(
        flat_contexts(G2P("fr")._tokenizer.grapheme_tokens("eu"),
                      get("fr-FR").vowel_graphemes)[0],
        spec=get("fr-FR"), syllable=None)
    assert GP.OPEN_SYLLABLE not in positions
    assert GP.CLOSED_SYLLABLE not in positions


@pytest.mark.parametrize("word,expected", [
    # closed syllable → [œ]
    ("fleur", "flœʁ"),
    ("escrimeur", "ɛskʁimœʁ"),
    ("chanteur", "ʃɑ̃tœʁ"),
    # open syllable → [ø]
    ("peu", "pø"),
    ("heureux", "øʁø"),
])
def test_french_eu_follows_the_loi_de_position(word, expected):
    assert G2P("fr").transcribe_word(word) == expected


@pytest.mark.parametrize("word,expected", [
    # Word-final ⟨r⟩ is pronounced…
    ("bonjour", "bɔ̃ʒuʁ"),
    ("mer", "mɛʁ"),
    ("sur", "syʁ"),
    ("amour", "amuʁ"),
    ("loisir", "lwaziʁ"),
    ("hiver", "ivɛʁ"),
    # …except in ⟨-er⟩, which grammatical_endings owns (plural too).
    ("parler", "paʁle"),
    ("parlers", "paʁle"),
    ("boulanger", "bulɑ̃ʒe"),
])
def test_french_final_r(word, expected):
    assert G2P("fr").transcribe_word(word) == expected


@pytest.mark.parametrize("word,expected", [
    # A mute word-final ⟨h⟩ does not close the syllable: [ø], not [œ].
    ("beuh", "bø"),
    ("chleuh", "ʃlø"),
    # …while a mute ⟨s⟩ over a PRONOUNCED ⟨r⟩ leaves it closed.
    ("chanteurs", "ʃɑ̃tœʁ"),
])
def test_unconditionally_mute_graphemes_do_not_close_a_syllable(word, expected):
    """``_silent_word_finally`` must read the FLAT grapheme table too.

    French ⟨h⟩ is mute unconditionally — it has no ``word_final``
    positional entry at all — so a version that consulted only
    ``positional_graphemes`` saw *beuh* as closed and said [bœ].
    """
    assert G2P("fr").transcribe_word(word) == expected


def _ending_spec(endings):
    """A throwaway spec carrying only what the ending matcher reads."""
    return replace(get("fr-FR"), grammatical_endings=endings)


@pytest.mark.parametrize("tokens,expected_tokens", [
    # ⟨mm⟩ is ONE grapheme token, so ⟨-ment⟩ starts INSIDE it. Matching on
    # tokens alone could never see it — this is the defect: the ending is
    # plainly there in the letters. The span rounds OUTWARD to whole
    # tokens, so ⟨mm⟩+⟨e⟩+⟨n⟩+⟨t⟩ (4 tokens) are replaced, not 3.
    (["c", "o", "mm", "e", "n", "t"], 4),
    (["a", "pp", "a", "r", "e", "mm", "e", "n", "t"], 4),
    # Already token-aligned: unchanged, 4 tokens either way.
    (["a", "l", "i", "m", "e", "n", "t"], 4),
])
def test_ending_matches_when_it_starts_inside_a_digraph(tokens,
                                                        expected_tokens):
    match = match_grammatical_ending(tokens, _ending_spec({"ment": "mɑ̃"}))
    assert match is not None, "ending straddling a digraph was not seen"
    assert match.ending == "ment"
    assert match.tokens == expected_tokens


def test_ending_still_needs_a_head_token():
    """A word that IS its ending is a word, not a suffix."""
    assert match_grammatical_ending(
        ["m", "e", "n", "t"], _ending_spec({"ment": "mɑ̃"})) is None
    # …and the head may not be the straddled token's own prefix alone.
    assert match_grammatical_ending(
        ["mm", "e", "n", "t"], _ending_spec({"ment": "mɑ̃"})) is None


@pytest.mark.parametrize("word,expected", [
    # The shipped, token-aligned French endings are unaffected.
    ("parler", "paʁle"),
    ("parlers", "paʁle"),
    ("boulanger", "bulɑ̃ʒe"),
    ("mangez", "mɑ̃ʒe"),
    # ⟨-ment⟩ is NOT declared and does not need to be: the nasal ⟨en⟩ plus
    # a silent ⟨t⟩ already give the right answer.
    ("comment", "kɔmɑ̃"),
    ("apparemment", "apaʁəmɑ̃"),
    ("rapidement", "ʁapidəmɑ̃"),
])
def test_shipped_french_endings(word, expected):
    assert G2P("fr").transcribe_word(word) == expected


@pytest.mark.parametrize("word", [
    # The nominal/adjectival ⟨-ent⟩ class keeps [ɑ̃]: a grammatical_endings
    # ⟨ent⟩→[] entry wins 3844 wikipron/fr types and loses these, which are
    # far commoner in running text. Verb-vs-noun is not decidable from
    # spelling, so the rule is deliberately NOT declared.
    "vent", "dent", "cent", "argent", "accent", "talent", "absent",
    "serpent", "occident",
])
def test_nominal_ent_keeps_its_nasal_vowel(word):
    assert G2P("fr").transcribe_word(word).endswith("ɑ̃")
