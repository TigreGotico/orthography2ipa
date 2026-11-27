"""Seselwa (crs) inherits the fr-FR sandhi rules by id and switches off the French ones.

The French rules that read the spelling (the obligatory liaisons, vingt, neuf
ans, est, verbal -ent, the h aspiré stems) read French words, and no source
states them for Seselwa, whose spelling writes the consonants it pronounces.
crs.json therefore overrides each of them by id.
"""
import json
from pathlib import Path

import pytest

import orthography2ipa as o2i

DATA = Path(o2i.__file__).parent / "data"


def _own_ids(code):
    return {r["id"] for r in json.loads((DATA / f"{code}.json").read_text(encoding="utf-8"))["sandhi_rules"]}


def test_every_french_spelling_rule_is_overridden_in_crs():
    spelled = {r.id for r in o2i.get("fr-FR").sandhi_rules
               if r.left_spelling is not None or r.right_spelling is not None}
    assert spelled
    assert spelled <= _own_ids("crs")
    assert not any(r.left_spelling or r.right_spelling for r in o2i.get("crs").sandhi_rules)


@pytest.mark.parametrize("text, expected", [
    # en is the article a: the French [n] liaison of en does not apply.
    ("en ansyen lakaz", "ɛ̃ ɑ̃sjɛ̃ lakaz"),
    # onz is eleven, not an h aspiré word: the enchaînement stays as it was.
    ("zot onz zanfan", "zot‿ ɔ̃z zɑ̃fɑ̃"),
])
def test_seselwa_keeps_its_sandhi(text, expected):
    assert o2i.transcribe(text, "crs") == expected
