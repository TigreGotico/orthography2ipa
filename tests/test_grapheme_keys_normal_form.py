"""Every grapheme key is written the way the tokenizer sees the text.

The tokenizer matches NFC text with the spec's ``fold_diacritics`` removed.
A key in any other form can never match, so it is dead data, and an edit
made to it changes nothing.
"""
import json
import unicodedata
from pathlib import Path

import pytest

DATA = Path(__file__).resolve().parent.parent / "orthography2ipa" / "data"


def _normal_form(key, fold):
    decomposed = unicodedata.normalize("NFD", key)
    return unicodedata.normalize("NFC", "".join(c for c in decomposed if c not in fold))


def _keys_not_in_normal_form():
    found = []
    for path in sorted(DATA.glob("*.json")):
        spec = json.loads(path.read_text(encoding="utf-8"))
        graphemes = spec.get("graphemes")
        if not isinstance(graphemes, dict):
            continue
        fold = spec.get("fold_diacritics") or []
        found += [(path.stem, key, _normal_form(key, fold))
                  for key in graphemes if _normal_form(key, fold) != key]
    return found


def test_every_grapheme_key_is_in_normal_form():
    assert _keys_not_in_normal_form() == []


@pytest.mark.parametrize("key, fold, expected", [
    ("ņ", [], "ņ"),
    ("ἀ", ["̓"], "α"),
    ("ά", ["̓"], "ά"),
])
def test_normal_form_matches_the_tokenizer_rule(key, fold, expected):
    assert _normal_form(key, fold) == expected
