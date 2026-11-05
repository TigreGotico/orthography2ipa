"""The pt-BR conventions sheet writes what the pt-BR spec writes.

Expected values come from docs/languages/pt-BR.md and the rule notes of
orthography2ipa/data/pt-BR.json, not from the engine alone.
"""
from pathlib import Path

import pytest

from orthography2ipa import G2P

SHEET = Path(__file__).resolve().parent.parent / "orthography2ipa/data/gold/conventions/pt-BR.md"


@pytest.mark.parametrize("word, ipa", [
    ("mar", "ˈmaɾ"),              # the base keeps the coda tap
    ("irmão", "iɾˈmɐ̃w̃"),
    ("falar", "faˈla"),            # BR_INFINITIVE_R_DROP
    ("estar", "isˈta"),            # BR_INITIAL_ES_RAISE and the infinitive drop
    ("desligar", "dezliˈɡa"),      # ⟨des⟩ has no raising rule
    ("outro", "ˈowtɾu"),           # the spec keeps the diphthong
    ("vou", "ˈvow"),
    ("menino", "meˈnĩnu"),         # BR_NASAL_STRESSED_I
    ("número", "ˈnũmeɾu"),         # BR_NASAL_STRESSED_U
    ("vinho", "ˈvĩɲu"),
    ("homem", "ˈõmẽj̃"),
])
def test_the_sheet_and_the_spec_give_one_reading(word, ipa):
    assert f"{word} [{ipa}]" in SHEET.read_text(encoding="utf-8")
    assert G2P("pt-BR", expose_ambiguous_endings=False).transcribe_word(word) == ipa


@pytest.mark.parametrize("stale", ["[ˈmaʁ]", "[faˈlaʁ]", "[ˈotɾu]", "[d͡ʒizliˈɡaʁ]", "⟨es-, ex-⟩"])
def test_the_sheet_drops_what_the_spec_does_not_write(stale):
    assert stale not in SHEET.read_text(encoding="utf-8")
