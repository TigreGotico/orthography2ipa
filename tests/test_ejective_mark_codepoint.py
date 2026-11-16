"""The IPA ejective mark is U+02BC MODIFIER LETTER APOSTROPHE.

U+2019 RIGHT SINGLE QUOTATION MARK looks the same, but it is punctuation
(category Pf), not a spacing modifier. The segmenter glues a modifier letter
to the consonant before it, so ``tsʼ`` is one ejective; with U+2019 the mark
becomes a segment of its own and ``ats’a`` syllabifies as ``ats|’a``.

The apostrophe in a grapheme KEY is spelling and is out of scope here: an
orthography may write its ejectives with either mark.
"""
import json
import os

import pytest

from orthography2ipa.allophony import segment_ipa
from orthography2ipa.registry import get
from orthography2ipa.stress import syllabify_ipa

_DATA = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")

_EJECTIVE_SPECS = ("bcq", "guk", "gwd", "har", "hdy", "irk", "kbr", "myf",
                   "nmn", "sad", "she", "ssn", "udu")

# bfa writes ⟨’b ’d ’y⟩ as ``b’ d’ j’``. Swapping the mark would claim voiced
# ejectives, so that spec needs a sourced segment fix rather than a code
# point fix. The set may only shrink.
_OPEN = {"bfa"}


def _ipa_values(spec):
    for candidates in spec.graphemes.values():
        yield from candidates
    for table in (spec.positional_graphemes or {}).values():
        for candidates in table.values():
            yield from candidates
    for surfaces in spec.allophones.values():
        yield from surfaces
    yield from spec.phonemes


@pytest.mark.parametrize("code", _EJECTIVE_SPECS)
def test_ejectives_are_written_with_the_modifier_letter(code):
    spec = get(code)
    ejectives = [v for v in _ipa_values(spec) if "ʼ" in v]
    assert ejectives, "the case only bites while the spec has ejectives"
    assert not [v for v in _ipa_values(spec) if "’" in v]
    for value in ejectives:
        assert "ʼ" not in segment_ipa(value, ()), value


def test_guk_ejective_affricate_is_one_onset():
    atoms = list(get("guk").phonemes)
    assert syllabify_ipa(get("guk").graphemes["s'"][0].join("aa"), 1, atoms) \
        == ["a", "tsʼa"]


def test_no_other_spec_writes_ipa_with_the_quotation_mark():
    offenders = set()
    for name in os.listdir(_DATA):
        if not name.endswith(".json"):
            continue
        with open(os.path.join(_DATA, name), encoding="utf-8") as handle:
            raw = json.load(handle)
        if not isinstance(raw, dict):
            continue
        values = [v for vs in (raw.get("graphemes") or {}).values() for v in vs or ()]
        values += [v for vs in (raw.get("allophones") or {}).values() for v in vs or ()]
        values += list(raw.get("phonemes") or ())
        if any(isinstance(v, str) and "’" in v for v in values):
            offenders.add(name[:-5])
    assert offenders <= _OPEN, sorted(offenders - _OPEN)
