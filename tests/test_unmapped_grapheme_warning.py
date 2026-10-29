"""A letter or combining mark that no grapheme key covers is never dropped in silence.

The tokenizer emits such a character as an ``UNKNOWN`` token, and the
transcription carries nothing for it: ``ar`` reads ⟨بڨب⟩ as ``ˈbb``, the same
string a word without the ⟨ڨ⟩ gives. The engine now emits
:class:`~orthography2ipa.exceptions.UnmappedGraphemeWarning` once per
(spec, character), and the transcription string does not change.

Only Unicode letters (``L*``) and marks (``M*``) warn. Punctuation, digits,
symbols and spaces are not part of a spelling the spec has to cover.

⟨ڨ⟩ U+06A8 is the issue #1644 case: ``ar-MA`` declares it (Saadane & Habash
2015, quoted in that spec's notes) and ``ar`` does not.
"""
import warnings

import pytest

from orthography2ipa import G2P
from orthography2ipa.exceptions import (
    StubSpecWarning,
    UnmappedGraphemeWarning,
    UnmappedScriptError,
)

QAF_THREE_DOTS = "ڨ"
WORD = "ب" + QAF_THREE_DOTS + "ب"


def _unmapped_warnings(record):
    return [w for w in record if issubclass(w.category, UnmappedGraphemeWarning)]


def test_unmapped_letter_warns_and_names_code_point_and_spec():
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        ipa = G2P("ar").transcribe(WORD)
    hits = _unmapped_warnings(record)
    assert len(hits) == 1
    message = str(hits[0].message)
    assert "U+06A8" in message
    assert message.startswith("ar:")
    assert QAF_THREE_DOTS in message
    # The output string is the one the explicit silent mode returns.
    assert ipa == G2P("ar", on_unmapped="ignore").transcribe(WORD)


def test_spec_that_maps_the_letter_does_not_warn():
    with warnings.catch_warnings():
        warnings.simplefilter("error", UnmappedGraphemeWarning)
        ipa = G2P("ar-MA").transcribe(WORD)
    # ar-MA cites Saadane & Habash (2015) for ⟨ڨ⟩ = /ɡ/.
    assert "ɡ" in ipa


def test_warns_once_per_spec_and_character():
    engine = G2P("ar")
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        engine.transcribe(WORD)
        engine.transcribe(WORD + " " + QAF_THREE_DOTS + "ا")
        engine.transcribe_detailed(WORD)
    assert len(_unmapped_warnings(record)) == 1


def test_each_distinct_character_warns():
    # U+06A8 and U+06A5 ARABIC LETTER FEH WITH THREE DOTS BELOW are both
    # absent from ar.
    silent = G2P("ar", on_unmapped="ignore")
    assert silent.transcribe_detailed("ڥ").words[0].unmapped == ("ڥ",)
    engine = G2P("ar")
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        engine.transcribe(WORD + " " + "بڥب")
    messages = sorted(str(w.message) for w in _unmapped_warnings(record))
    assert len(messages) == 2
    assert "U+06A5" in messages[0] and "U+06A8" in messages[1]


def test_unmapped_combining_mark_warns():
    # U+0331 COMBINING MACRON BELOW is category Mn and absent from en-US.
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        G2P("en-US").transcribe("be̱d")
    hits = _unmapped_warnings(record)
    assert len(hits) == 1
    assert "U+0331" in str(hits[0].message)


@pytest.mark.parametrize("lang, word", [
    ("en-US", "cat"),
    ("pt-PT", "casa"),
    ("fi", "talo"),
    ("ru", "дом"),
    ("hi", "कमल"),
])
def test_mapped_word_in_unrelated_languages_does_not_warn(lang, word):
    with warnings.catch_warnings():
        warnings.simplefilter("error", UnmappedGraphemeWarning)
        result = G2P(lang).transcribe_detailed(word)
    assert result.words[0].unmapped == ()


@pytest.mark.parametrize("text", [
    "ب€ب",    # U+20AC, category Sc
    "ب😀ب",   # U+1F600, category So
    "بب، ١٢٣ !",
])
def test_symbols_digits_punctuation_and_spaces_do_not_warn(text):
    with warnings.catch_warnings():
        warnings.simplefilter("error", UnmappedGraphemeWarning)
        G2P("ar").transcribe(text)


def test_ignore_mode_stays_silent():
    with warnings.catch_warnings():
        warnings.simplefilter("error", UnmappedGraphemeWarning)
        G2P("ar", on_unmapped="ignore").transcribe(WORD)


def test_raise_mode_still_raises():
    with pytest.raises(UnmappedScriptError):
        G2P("ar", on_unmapped="raise").transcribe(WORD)


def test_stub_spec_warns_once_for_the_spec_not_per_letter():
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        G2P("azb").transcribe("كتاب")
    assert [w for w in record if issubclass(w.category, StubSpecWarning)]
    assert _unmapped_warnings(record) == []
