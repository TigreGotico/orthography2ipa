"""Pichi (`fpe`) marks lexical tone in its own working orthography.

Yakpo, *A Grammar of Pichi* (2019: 11, sec. 1.6 Standardisation and
orthography): "Tone is marked on all Pichi words throughout this book.
H-toned syllables bear an acute accent, e.g. wét [wét] 'wait', and L-toned
syllables remain unmarked, e.g. wet [wèt] 'with'." This is directly attested
in the wikipron gold: e.g. the orthographic word "bájin" is transcribed
"b á d͡ʒ ì n" — H tone on the accented vowel, L tone (unmarked in the
orthography) on the second syllable.

Before this fix, the spec's own notes claimed the opposite (that tone is
"left unencoded"), and none of the seven accented H-tone vowel graphemes
(á é í ó ú, plus ɛ́/ɔ́ written as base vowel + combining acute, U+0301,
since Latin has no precomposed open-mid accented forms) had a table entry,
so the tokenizer silently dropped every one of them.
"""
from orthography2ipa import get, transcribe
from orthography2ipa.phonetok import PhonetokTokenizer, TokenKind


def test_fpe_h_tone_vowels_are_graphemes_not_unknown():
    """Every accented H-tone vowel must resolve to a real grapheme token,
    not UNKNOWN/PUNCTUATION (the silent-deletion failure mode)."""
    spec = get("fpe")
    tok = PhonetokTokenizer(spec)
    for word in ("bájin", "nyandá", "sidɔ́n", "sistɛlɔ́", "kwís", "smɔ́l"):
        tokens = tok.tokenize(word)
        bad = [t for t in tokens if t.kind in (TokenKind.UNKNOWN, TokenKind.PUNCTUATION)]
        assert not bad, f"{word!r} produced dropped tokens: {bad}"


def test_fpe_acute_accent_marks_high_tone_in_output():
    """The acute-accented vowel graphemes must surface their tone mark in the
    IPA output, matching the wikipron gold's own tone-marked transcriptions
    (e.g. bájin -> b á d͡ʒ ì n, gold-attested)."""
    out = transcribe("bájin", "fpe")
    assert "á" in out
    out2 = transcribe("sidɔ́n", "fpe")
    assert "ɔ́" in out2
