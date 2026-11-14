"""A digit that no grapheme key covers is reported like an unmapped letter.

The transcription drops such a digit, so ``on_unmapped`` covers it in every
mode: ``warn`` warns once per (spec, character), ``raise`` raises, and the
word's ``unmapped`` and ``coverage`` count it. The transcription string does
not change. A spec that spells a segment with a digit, such as numbered
Pinyin, maps that digit as a grapheme and stays silent.

Expected values are written by hand: ``3`` is one character with no mapping,
so the word ``3`` has coverage 0/1 and ``a3b`` has coverage 2/3.
"""
import warnings

import pytest

from orthography2ipa import G2P
from orthography2ipa.exceptions import UnmappedGraphemeWarning, UnmappedScriptError


def _digit_warnings(record):
    return [str(w.message).split(" ")[1] for w in record
            if issubclass(w.category, UnmappedGraphemeWarning)]


def test_raise_mode_raises_on_a_digit():
    with pytest.raises(UnmappedScriptError):
        G2P("pt-PT", on_unmapped="raise").transcribe("tenho 3 gatos")


def test_each_digit_warns_once():
    engine = G2P("en-GB")
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        engine.transcribe("room 101 a3b")
        engine.transcribe("room 101")
    assert sorted(_digit_warnings(record)) == ["U+0030", "U+0031", "U+0033"]


def test_ignore_mode_stays_silent():
    with warnings.catch_warnings():
        warnings.simplefilter("error", UnmappedGraphemeWarning)
        G2P("pt-PT", on_unmapped="ignore").transcribe("tenho 3 gatos")


def test_the_transcription_does_not_change():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UnmappedGraphemeWarning)
        engine = G2P("pt-PT")
        assert engine.transcribe("tenho 3 gatos") == engine.transcribe("tenho gatos")


def test_unmapped_and_coverage_count_the_digit():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UnmappedGraphemeWarning)
        words = G2P("en-GB").transcribe_detailed("3 a3b").words
    assert [(w.unmapped, w.coverage) for w in words] == [(("3",), 0.0), (("3",), 2 / 3)]


def test_a_spec_that_spells_with_a_digit_stays_silent():
    with warnings.catch_warnings():
        warnings.simplefilter("error", UnmappedGraphemeWarning)
        result = G2P("zh").transcribe_detailed("ma3")
    assert result.words[0].unmapped == ()


def test_the_docs_say_what_the_engine_does_with_a_digit():
    """The engine warns for a digit (#2183), so no doc may say it never does."""
    from pathlib import Path
    import orthography2ipa
    root = Path(orthography2ipa.__file__).parent
    texts = {
        "g2p.py": (root / "g2p.py").read_text(encoding="utf-8"),
        "exceptions.py": (root / "exceptions.py").read_text(encoding="utf-8"),
        "api_stability.md": (root.parent / "docs" / "reference"
                             / "api_stability.md").read_text(encoding="utf-8"),
    }
    for name, text in texts.items():
        flat = " ".join(text.split())
        assert "digits, symbols and spaces do not warn" not in flat, name
        assert "digits, symbols and spaces never do" not in flat, name
    with pytest.warns(UnmappedGraphemeWarning):
        G2P("fr-FR").transcribe("3")
