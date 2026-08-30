"""Cited-claim tests for the Limburgish (``li``) benchmark ceiling.

Limburgish is a pitch-accent language whose orthography (Spelling 2003,
the "Veldekespelling") does not write the sleeptoon/stoottoon contrast.
The natural hypothesis is that tone marking in the li/wikipron gold is
the dominant driver of the shipped PER, the way it was for Hausa and
Kikuyu (see ``test_kikuyu_tone_ceiling.py``). That hypothesis does NOT
hold here: only a small share of gold lines carry a tone letter, and
folding tone out of both sides barely moves the score. This file checks
that measured (negative) result plus the larger, documented driver: the
li/wikipron gold set mixes Wiktionary's competing Limburgish spelling
conventions (Veldeke/Spelling 2003, German-based spelling, Rheinische
Dokumenta, Eupen dialect) rather than the single Spelling-2003 convention
this spec's INPUT CONTRACT targets (see ``wiktionary_li_orthography_mix``
in ``li.json``'s ``sources``).
"""
from __future__ import annotations

import json
import pathlib
import sys

DATA_DIR = (pathlib.Path(__file__).parent.parent
            / "orthography2ipa" / "data")

_TONE_LETTERS = {"˨", "˧", "˦", "˥", "˩"}


def _load_gold():
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm
    return bm.load_wikipron("li", 10 ** 9)


def test_notes_document_the_measured_ceiling():
    raw = json.loads((DATA_DIR / "li.json").read_text(encoding="utf-8"))
    notes = raw["notes"]
    assert "0.3819" in notes
    assert "0.3771" in notes
    assert "33.4%" in notes or "330/989" in notes
    source_ids = {s["id"] for s in raw["sources"]}
    assert "wiktionary_li_orthography_mix" in source_ids


def test_tone_marking_is_rare_and_not_the_dominant_driver():
    """Negative result: unlike Hausa/Kikuyu, tone-folding barely moves PER."""
    pairs = _load_gold()
    tone_lines = [g for _, g in pairs if any(c in _TONE_LETTERS for c in g)]
    # measured: 90/1128 gold lines carry a tone letter
    assert 70 <= len(tone_lines) <= 110, (
        f"expected ~90 tone-marked gold lines, found {len(tone_lines)}"
    )

    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm

    orig_normalize = bm.normalize

    def folded_normalize(ipa, strip_stress, broad, extra_strip=""):
        out = orig_normalize(ipa, strip_stress, broad, extra_strip=extra_strip)
        return "".join(c for c in out if c not in _TONE_LETTERS)

    try:
        bm.normalize = folded_normalize
        _, _, per_folded, _ = bm.evaluate(pairs, "li", strip_stress=True,
                                           broad=True)
    finally:
        bm.normalize = orig_normalize

    _, _, per_baseline, _ = bm.evaluate(pairs, "li", strip_stress=True,
                                         broad=True)

    # tone folding should move PER by well under 0.02 (measured: ~0.005),
    # far less than the >0.3 collapse seen for Hausa/Kikuyu
    assert per_baseline - per_folded < 0.02, (
        "tone folding moved PER more than expected; li may in fact have a "
        "recoverable tone ceiling like Hausa/Kikuyu -- re-examine before "
        "reasserting the 'not dominant' claim in li.json's notes"
    )


def test_gold_headwords_mix_out_of_scope_spelling_conventions():
    """330/989 gold headwords carry a character absent from the Spelling
    2003 grapheme table (ä, é, ï, ë, ǫ, ą, ṣ, or a syllabic mark), which the
    tokenizer silently drops as UNKNOWN -- evidence the gold draws from
    Wiktionary's German-based/Rheinische-Dokumenta/Eupen spelling variants,
    not exclusively the Veldeke/Spelling-2003 form this spec targets."""
    from orthography2ipa import get
    from orthography2ipa.phonetok import PhonetokTokenizer, TokenKind

    spec = get("li")
    tok = PhonetokTokenizer(spec)
    pairs = _load_gold()
    words = {w for w, _ in pairs}

    def has_unknown(w: str) -> bool:
        return any(t.kind == TokenKind.UNKNOWN for t in tok.tokenize(w.lower()))

    out_of_scope = {w for w in words if has_unknown(w)}
    # measured: 330/989
    assert len(out_of_scope) >= 280, (
        f"expected >= ~330 out-of-scope-spelling headwords, found "
        f"{len(out_of_scope)}"
    )
    assert "Bäcker" in out_of_scope or "Aap" in out_of_scope
