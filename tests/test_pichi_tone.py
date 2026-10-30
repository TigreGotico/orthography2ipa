"""Pichi (`fpe`) writes both of its level tones, and both must reach the IPA.

Pichi contrasts a high (H) and a low (L) level tone. The transcription
convention the gold material follows marks H with an acute accent and leaves
L unmarked, so the spec declares seven accented H-tone vowel graphemes and
maps the seven plain vowel letters to grave-marked L-tone IPA vowels. The
citation for both halves lives in the `fpe` spec's notes and its
`fpe_yakpo2019` source entry; this file only guards the behaviour.

Unmarked in the orthography is not untoned in the phonology: in the wikipron
fpe gold every one of the 261 words is fully toned, and of its 391 vowel
tokens 259 are H and 132 are L, with no untoned vowel anywhere.
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
    IPA output, matching the tone-marked gold transcriptions
    (e.g. bájin -> b á d͡ʒ ì n, gold-attested)."""
    out = transcribe("bájin", "fpe")
    assert "á" in out
    out2 = transcribe("sidɔ́n", "fpe")
    assert "ɔ́" in out2


def test_fpe_unaccented_vowels_carry_low_tone():
    """A vowel letter written bare is L-toned, not toneless. Gold-attested:
    bájin -> b á d͡ʒ ì n and torí -> t ò ʁ í."""
    assert "ì" in transcribe("bájin", "fpe")
    assert "ò" in transcribe("torí", "fpe")


def test_fpe_open_mid_vowels_carry_low_tone():
    """The open-mid pair takes the same treatment, with a combining grave
    (U+0300) since Latin has no precomposed ɛ̀/ɔ̀. Gold-attested:
    síryɔs -> s í ʁ j ɔ̀ s."""
    assert "ɔ̀" in transcribe("síryɔs", "fpe")
    assert "ɛ̀" in transcribe("sistɛlɔ́", "fpe")


def test_fpe_no_vowel_reaches_the_output_untoned():
    """No bare vowel may survive to the IPA: every vowel in the gold carries
    a tone, so an untoned output vowel is always an error."""
    for word in ("bájin", "torí", "síryɔs", "gbogbogbo", "sistɛlɔ́"):
        out = transcribe(word, "fpe")
        for i, ch in enumerate(out):
            if ch in "aeiouɛɔ":
                following = out[i + 1 : i + 2]
                assert following in ("́", "̀"), (
                    f"{word!r} -> {out!r}: untoned vowel {ch!r} at {i}"
                )
