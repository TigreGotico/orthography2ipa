"""Cited-claim tests for the Kapampangan (``pam``) valid_ceiling.

Kapampangan stress is phonemic and lexical, and ordinary Sulat Wawa
spelling never marks it (Forman 1971, *Kapampangan Grammar Notes*;
summarised at https://en.wikipedia.org/wiki/Kapampangan_language, which
cites Forman 1971 pp.28-29 for the stress facts). The wikipron gold
shows this directly: the identical spelling recurs with mutually
incompatible readings (e.g. "Guagua" -> ɡwaɡwə vs wawəʔ), so the vowel
quality alternation the gold marks (/a/ ~ [ə], /i/ ~ [ɪ], /u/ ~ [ʊ]
under the unwritten unstressed condition) cannot be recovered from the
spelling. The word-final glottal stop is a second, independent unwritten
phenomenon (the spec's own notes already record it as "usually
unwritten"). This file keeps the sourced, measured ceiling that proves
the row is input-limited from silently drifting.
"""
from __future__ import annotations

import json
import pathlib
import sys

DATA_DIR = (pathlib.Path(__file__).parent.parent
            / "orthography2ipa" / "data")


def _load_gold():
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm
    return bm.load_wikipron("pam", 10 ** 9)


def _fold(s: str) -> str:
    return (s.replace("ʔ", "")
             .replace("ə", "a")
             .replace("ɪ", "i")
             .replace("ʊ", "u"))


def test_notes_document_glottal_stop_as_unwritten():
    raw = json.loads((DATA_DIR / "pam.json").read_text(encoding="utf-8"))
    assert "usually unwritten" in raw["notes"]
    ceiling = raw["valid_ceiling"]["wikipron"]
    assert ceiling["per"] == 0.0843
    assert "0.2861" in ceiling["citation"]
    assert "0.0843" in ceiling["citation"]


def test_identical_spelling_maps_to_incompatible_readings():
    """Direct evidence stress/vowel-quality is lexical, not recoverable
    from the spelling: the same headword recurs with conflicting gold
    vowel realizations."""
    pairs = _load_gold()
    by_word: dict[str, set[str]] = {}
    for word, gold in pairs:
        by_word.setdefault(word, set()).add(gold.replace(" ", ""))

    ambiguous = {w: g for w, g in by_word.items() if len(g) > 1}
    # measured against the cached gold: 48 conflicting headwords
    assert len(ambiguous) >= 40, (
        "expected the previously-measured ~48 conflicting-reading "
        f"headwords; found {len(ambiguous)}"
    )


def test_orthography_never_marks_the_glottal_stop():
    """Negative-recoverability check: Sulat Wawa spelling carries no
    apostrophe or other glottal-stop mark anywhere in this gold's input
    column, while the gold pronunciation frequently carries ʔ."""
    pairs = _load_gold()
    assert not any("'" in word or "’" in word for word, _ in pairs)
    with_glottal = sum(1 for _, gold in pairs if "ʔ" in gold)
    assert with_glottal >= 90  # measured: 108/926


def test_ceiling_fold_narrows_the_gap():
    """Fail-before-sensitive: fold glottal stop + a/ə + i/ɪ + u/ʊ out of
    both hypothesis and gold and rescore against the shipped engine, not
    just the gold file, so a real segmental regression would still show
    up here even though the unwritten-stress alternation is folded."""
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm

    pairs = _load_gold()
    orig_normalize = bm.normalize

    def folded_normalize(ipa, strip_stress, broad, extra_strip=""):
        out = orig_normalize(ipa, strip_stress, broad, extra_strip=extra_strip)
        return _fold(out)

    try:
        bm.normalize = folded_normalize
        _, covered, per, _ = bm.evaluate(pairs, "pam", strip_stress=True,
                                          broad=True)
    finally:
        bm.normalize = orig_normalize

    assert covered == 860
    # measured 0.0843; generous margin against harness float noise while
    # still failing hard if a future change reopens or widens the gap.
    assert per < 0.12, f"expected folded PER near 0.0843, got {per:.4f}"


def test_positional_stress_heuristic_does_not_hold():
    """Negative result: treating only the word-final vowel as stressed
    (the rest reduced) only narrows raw PER to ~0.2351, far short of the
    0.0843 ceiling -- confirming the alternation is lexical, not
    positional, so no such rule was added to the spec."""
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm
    from orthography2ipa import G2P

    pairs = _load_gold()
    engine = G2P("pam")
    refs: dict[str, list[str]] = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)

    def heuristic(hyp: str) -> str:
        chars = list(hyp)
        vowel_idxs = [i for i, c in enumerate(chars) if c in "aəiɪuʊeo"]
        if not vowel_idxs:
            return hyp
        last_v = vowel_idxs[-1]
        for i in vowel_idxs:
            if chars[i] == "a" and i != last_v:
                chars[i] = "ə"
        return "".join(chars)

    pers = []
    for word, golds in refs.items():
        try:
            hyp = bm.normalize(engine.transcribe_word(word), True, True)
        except Exception:
            continue
        if not hyp:
            continue
        hyp_t = heuristic(hyp)
        golds_norm = [bm.normalize(g, True, True) for g in golds]
        per = min(bm.levenshtein(hyp_t, g) / max(len(g), 1) for g in golds_norm)
        pers.append(per)

    result = sum(pers) / len(pers)
    assert 0.20 < result < 0.27, (
        f"expected the heuristic to land near 0.2351 (a partial, "
        f"non-clearing narrowing), got {result:.4f}"
    )
