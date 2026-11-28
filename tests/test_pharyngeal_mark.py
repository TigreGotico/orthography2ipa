"""Pharyngealization is U+02E4 MODIFIER LETTER SMALL REVERSED GLOTTAL STOP (ˤ),
as on the IPA chart (2020), "Diacritics". U+02C1 MODIFIER LETTER REVERSED
GLOTTAL STOP (ˁ) looks alike but is a different symbol."""
import json
from pathlib import Path

import orthography2ipa

DATA = Path(orthography2ipa.__file__).parent / "data"
IPA_FIELDS = ("graphemes", "positional_graphemes", "phonemes", "allophones")


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from _strings(item)


def test_no_spec_writes_pharyngealization_with_u02c1():
    bad = {}
    for path in sorted(DATA.glob("*.json")):
        spec = json.loads(path.read_text(encoding="utf-8"))
        hits = sorted({s for field in IPA_FIELDS for s in _strings(spec.get(field)) if "ˁ" in s})
        if hits:
            bad[path.stem] = hits
    assert bad == {}


def test_gho_reads_its_emphatic_stop_with_the_ipa_mark():
    from orthography2ipa import get
    assert "dˤ" in get("gho").graphemes["ḍ"]


def test_gud_open_e_is_pharyngealized_like_its_sister_vowels():
    # The Omniglot Yocoboué Dida chart prints ɛ as [ɛˤ], with the mark it prints on ɔ.
    from orthography2ipa import get
    graphemes = get("gud").graphemes
    assert graphemes["ɛ"] == ["ɛˤ"]
    assert graphemes["ɔ"] == ["ɔˤ"]
