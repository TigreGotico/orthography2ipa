"""Where the "free variation" of velar affrication lives in the engine.

The notes of ar-OM, ar-SA-x-najd and ar-SA-x-shamali call the affrication free
variation. The engine carries it in two places, and this file pins both so
the notes and the lattice cannot drift apart again: the allophone rule
rewrites the slot, so ``transcribe_word`` gives the affricate; ``candidates``
is the pre-rule beam and gives the plain velar; and the pair is an entry of
the ``allophones`` table, so both arcs are in ``candidates`` under
``expand_allophones=True``.
"""
import pytest

from orthography2ipa import G2P

CASES = [
    ("ar-OM", "كِتَاب", "tʃ", "kitaːb", "tʃitaːb"),
    ("ar-SA-x-najd", "كِتَاب", "ts", "kitaːb", "tsitaːb"),
    ("ar-SA-x-qassim", "كِتَاب", "ts", "kitaːb", "tsitaːb"),
    ("ar-SA-x-shamali", "كَلْب", "ts", "kalb", "tsalb"),
]


@pytest.mark.parametrize("lang, word, affricate, plain, affricated", CASES)
def test_the_rule_rewrites_and_the_beam_keeps_the_plain_velar(lang, word, affricate, plain, affricated):
    g = G2P(lang)
    assert g.transcribe_word(word).lstrip("ˈ").startswith(affricate) or affricate in g.transcribe_word(word)
    paths = [p.ipa for p in g.candidates(word)]
    assert paths == [plain], paths


@pytest.mark.parametrize("lang, word, affricate, plain, affricated", CASES)
def test_both_arcs_are_reachable_with_expand_allophones(lang, word, affricate, plain, affricated):
    g = G2P(lang, expand_allophones=True)
    paths = [p.ipa for p in g.candidates(word)]
    assert plain in paths and affricated in paths, paths


@pytest.mark.parametrize("lang, key, pair", [
    ("ar-OM", "k", ["k", "tʃ"]),
    ("ar-SA-x-najd", "k", ["k", "ts"]),
    ("ar-SA-x-shamali", "k", ["k", "ts"]),
])
def test_the_pair_is_an_allophones_entry(lang, key, pair):
    assert list(G2P(lang).spec.allophones[key]) == pair
