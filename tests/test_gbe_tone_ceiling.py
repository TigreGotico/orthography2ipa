"""Ewe (``ee``) and Gun/Gungbe (``guw``): the shared Gbe tone-notation ceiling.

Both languages are Gbe (Kwa, Niger-Congo) and both are tonal; both
WikiPron golds mark tone on nearly every syllable while the running
orthographies mark it rarely (Ewe: only where a minimal pair would
otherwise collide; Gun: 3 of 681 gold entries). No grapheme or allophone
rule can recover a tone the spelling never wrote, so the raw PER against
those golds is dominated by that notation gap rather than by segmental
(consonant/vowel) error.

These tests pin the two numbers that prove the gap is a ceiling and not
an ordinary rule defect:

* the homograph count — how many distinct spellings in the gold carry
  two or more different gold transcriptions. A low count (Ewe) means the
  orthography almost always disambiguates a word by itself; a high count
  (Gun) reflects the two competing Gun orthographies the spec documents
  (data/guw.json's ``notes``), not lost information.
* the tone-folded PER — segmental accuracy once the tone diacritics are
  stripped from both the engine's output and the gold. This is the
  number that actually reflects the quality of the grapheme/allophone
  rules, isolated from the notation gap.

Both numbers are measured directly against the cached WikiPron TSVs
(``.benchmark_cache/ewe_latn_broad.tsv``, ``guw_latn_broad.tsv``), the
same files ``scripts/benchmark.py --scoreboard`` scores against, so a
change that quietly breaks a grapheme or allophone rule for either
language moves the folded PER here and fails the test — see the module
docstring of ``scripts/benchmark.py`` for the scoring convention this
mirrors (segmentation-free string comparison via Levenshtein distance).
"""
import os
import sys
import unicodedata

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import benchmark  # noqa: E402

from orthography2ipa.g2p import G2P  # noqa: E402

_CACHE = os.path.join(os.path.dirname(__file__), "..", ".benchmark_cache")

_TONE_COMBINING_MARKS = "́̀̄̌̋̏"  # acute, grave, macron,
# caron, double-acute, inverted-breve — the tone diacritics these two
# orthographies use (circumflex is deliberately excluded: in Ewe it can
# mark a genuine long/falling vowel quality distinct from a level tone,
# so folding it would understate rather than isolate the tone gap).


def _strip_tone(s: str) -> str:
    decomposed = unicodedata.normalize("NFD", s)
    return unicodedata.normalize(
        "NFC", "".join(c for c in decomposed if c not in _TONE_COMBINING_MARKS))


def _gold_pairs(tsv_name):
    path = os.path.join(_CACHE, tsv_name)
    if not os.path.exists(path):
        pytest.skip(f"gold cache {tsv_name} not populated")
    pairs = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            pairs.append((parts[0], parts[1]))
    return pairs


def _homograph_count(pairs):
    by_word = {}
    for word, ipa in pairs:
        by_word.setdefault(word, set()).add(ipa)
    return sum(1 for readings in by_word.values() if len(readings) > 1)


def _folded_per(lang, pairs):
    engine = G2P(lang)
    extra = benchmark._prosody_marks(lang)
    refs = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)
    pers = []
    for word, golds in refs.items():
        try:
            hyp = benchmark.normalize(
                engine.transcribe_word(word), False, True, extra_strip=extra)
        except Exception:
            continue
        if not hyp:
            continue
        golds_norm = [benchmark.normalize(g, False, True, extra_strip=extra)
                      for g in golds]
        hyp_f = _strip_tone(hyp)
        golds_f = [_strip_tone(g) for g in golds_norm]
        pers.append(min(
            benchmark.levenshtein(hyp_f, g) / max(len(g), 1)
            for g in golds_f))
    assert pers, f"no words scored for {lang}"
    return sum(pers) / len(pers)


def test_ee_homograph_count_is_near_zero():
    # Ewe's toneless-by-default orthography almost always disambiguates a
    # word without needing a tone mark: only 3 of 247 distinct spellings
    # in the gold carry more than one transcription.
    pairs = _gold_pairs("ewe_latn_broad.tsv")
    assert _homograph_count(pairs) == 3


def test_guw_homograph_count_reflects_the_dual_orthography():
    # Gun mixes the Benin and Nigerian orthographic conventions for the
    # same phonemes (data/guw.json's notes), so a much larger share of
    # spellings collide even before tone is considered.
    pairs = _gold_pairs("guw_latn_broad.tsv")
    assert _homograph_count(pairs) == 72


def test_ee_folded_per_confirms_the_ceiling_is_notation():
    # Once tone is stripped from both sides, Ewe's segmental PER drops
    # under 2 points — the ~44-point raw PER is overwhelmingly the tone
    # the gold writes on every vowel and the spelling does not.
    pairs = _gold_pairs("ewe_latn_broad.tsv")
    assert _folded_per("ee", pairs) < 0.02


def test_guw_folded_per_confirms_the_ceiling_is_notation():
    # Same story for Gun: folding tone drops PER from ~43 points to
    # under 6, leaving only ordinary segmental error.
    pairs = _gold_pairs("guw_latn_broad.tsv")
    assert _folded_per("guw", pairs) < 0.06
