"""The nasal-carrier constraint must not depend on the search width.

A slot whose only reading is the bare combining tilde (a coda nasal that
nasalises the preceding vowel) needs an oral vowel or a glide in front of
it. That is a bigram constraint, and evaluating it only after the previous
slot has been chosen made it width-dependent: a greedy (width-1) search
committed to a non-carrier reading and then had no legal continuation,
while a width-8 beam kept the carrier alive and returned a different —
legal — string. ``G2P.transcribe_word`` (greedy) and
``G2P.word_candidates()[0]`` (beam) therefore disagreed, which is the
identity ``scripts/benchmark.py`` asserts on every scoreboard run.

Urdu's hamza-on-waw plurals are the shape that exposed it: ⟨ؤ⟩ resolves to
/ʔ/ at cost 0 and to /o/ at cost 1, and ⟨ں⟩ is a tilde-only slot, so greedy
produced the impossible *xzəʔ̃* where the beam produced *xzəõ*.

The fix walks back through the preceding slot's readings and drops the
non-carrier ones, using the segment's BASE character (stripping trailing
length marks and other non-tilde combining diacritics first) — a long
oral vowel like ``aː`` is a valid carrier, and must not be rejected just
because the raw last character of the string is the length mark ``ː``.
It also walks back past any number of chained DELETABLE slots (graphemes
with an empty reading, e.g. a silent hamza/ain) rather than only the
immediate predecessor, since the actual carrier segment can land on
whichever slot precedes the last one that resolves to nothing.

Finally, a valid tilde is no longer appended as its own trailing
segment: it is spliced into the carrier segment right after the base
vowel, so a long nasalised vowel comes out in IPA normal form (``ũː``,
tilde on the vowel, length mark after) instead of ``uː̃`` (tilde
trailing the length mark) — the latter is what plain segment
concatenation produced, and it is not the notation any gold or citation
this engine is measured against uses.
"""
from __future__ import annotations

import pytest

import orthography2ipa
from orthography2ipa import G2P

# The words --scoreboard reported as diverging for wikipron lang=ur.
HAMZA_WAW_PLURALS = {
    "آنساؤں": "aːnsəõ",
    "اہلیاؤں": "əɦljəõ",
    "بواؤں": "bʋəõ",
    "تمناؤں": "t̪mnəõ",
    "خزاؤں": "xzəõ",
}

# Languages whose grapheme table has at least one tilde-only slot, i.e.
# every language the constraint can act on.
TILDE_ONLY_LANGS = (
    "as", "awa", "bal", "bgc", "bho", "bn", "doi", "gom", "gu", "gwc",
    "hi", "hne", "hno", "kas", "kok", "kru", "mag", "mai", "mr", "ne",
    "new", "or", "pa", "pa-PK", "sa", "skr", "ur",
)


def _engine(code: str) -> G2P:
    try:
        return G2P(code)
    except Exception as exc:  # pragma: no cover - spec missing
        pytest.skip(f"{code!r} not available: {exc}")


@pytest.mark.parametrize("word,expected", sorted(HAMZA_WAW_PLURALS.items()))
def test_hamza_waw_plural_is_nasalised_not_glottal(word, expected):
    """⟨ؤں⟩ is a nasalised /õ/, never a glottal stop carrying a tilde."""
    ur = _engine("ur")
    assert ur.transcribe_word(word) == expected
    assert "ʔ̃" not in ur.transcribe_word(word)


@pytest.mark.parametrize("word", sorted(HAMZA_WAW_PLURALS))
def test_greedy_equals_best_beam_candidate(word):
    """The invariant the benchmark harness aborts on."""
    ur = _engine("ur")
    assert ur.word_candidates(word)[0] == ur.transcribe_word(word)


# ⟨ماں⟩ "mother": a LONG oral vowel (aː) immediately before the tilde-only
# nasalisation sign. The constraint must recognise ``aː`` as a carrier by
# its base vowel ``a``, not reject it because the raw last character of
# the segment string is the length mark ``ː`` (which looks unrelated to
# any vowel and previously deleted the long-vowel reading outright). The
# expected output is IPA normal form: the tilde marks the base VOWEL and
# the length mark follows it (``mãː``), never the other way round
# (``maː̃``, tilde trailing the length mark) — every gold this engine is
# measured against writes long nasalised vowels the first way.
LONG_VOWEL_CARRIERS = {
    "bal": ("ماں", "mãː"),
    "kas": ("ماں", "mãː"),
}


@pytest.mark.parametrize("code,word,expected",
                          [(c, w, e) for c, (w, e) in
                           sorted(LONG_VOWEL_CARRIERS.items())])
def test_long_vowel_survives_as_nasal_carrier(code, word, expected):
    """A long oral vowel must carry the tilde in IPA normal form."""
    engine = _engine(code)
    assert engine.transcribe_word(word) == expected
    assert engine.word_candidates(word)[0] == expected
    assert "aː̃" not in engine.transcribe_word(word), (
        "tilde must land on the base vowel before the length mark, "
        "not trail it")


# ⟨ؤ/ئ⟩ (waw/yeh hamza, deletable to a glottal reading) stacked behind a
# SILENT ⟨ع/ء⟩ (ain/hamza, deletable to nothing) before the tilde-only
# ⟨ں⟩. Two deletable slots in a row: the actual carrier the tilde needs
# sits two slots back, not one, so the fix has to walk the whole
# deletable chain, not just the immediate predecessor.
DELETABLE_CHAIN_WORDS = ("پؤعں", "پؤءں", "پئعں", "پئءں", "پًؤءں")


@pytest.mark.parametrize("word", sorted(DELETABLE_CHAIN_WORDS))
def test_greedy_equals_beam_across_deletable_chains(word):
    """Two stacked deletable slots must not defeat the carrier lookback."""
    ur = _engine("ur")
    best = ur.word_candidates(word, k=8)
    assert best and best[0] == ur.transcribe_word(word)


@pytest.mark.parametrize("code", TILDE_ONLY_LANGS)
def test_tilde_only_slot_languages_keep_the_identity(code):
    """No tilde-only-slot language may break greedy == beam-best.

    A single hand-built word per language is enough: the constraint is a
    property of the slot pair, not of the word, and the words below all
    end in that language's nasalisation sign after a vowel sign.
    """
    engine = _engine(code)
    spec = orthography2ipa.get(code)
    tilde_signs = [g for g, v in spec.graphemes.items()
                   if v and all(x == "̃" for x in v)]
    assert tilde_signs, f"{code} has no tilde-only grapheme any more"
    carriers = "aeiouɛɔəɨʉɯæɐʌɒœøɪʊɤɵɞɑɘɚɜɝɶywjɥɰ"
    vowels = sorted(g for g, v in spec.graphemes.items()
                    if v and v[0] and v[0][-1] in carriers)
    if not vowels:
        pytest.skip(f"{code} has no vowel-final grapheme")
    for sign in tilde_signs:
        for vowel in vowels[:5]:
            word = vowel + sign
            best = engine.word_candidates(word)
            if not best:
                continue
            assert best[0] == engine.transcribe_word(word), (
                f"{code}: {word!r} greedy != beam-best")
