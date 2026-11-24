"""IPA mark order in spec inventories: a tie bar joins two letters, a
prenasal mark comes before its stop, and a length mark belongs to its
segment, before any tone letter (IPA chart, 2020: "Other symbols",
"Diacritics", "Suprasegmentals", "Tones and word accents")."""
import re
import unicodedata

import pytest

from orthography2ipa import get
from orthography2ipa.inventory import phoneme_inventory

ISSUE = "https://github.com/TigreGotico/orthography2ipa/issues/2515"
TONE_LETTERS = "˥˦˧˨˩"
PRENASAL = "ᵐⁿᵑᶬᶮ"


def misordered(token):
    for i, ch in enumerate(token):
        nxt = token[i + 1] if i + 1 < len(token) else ""
        if ch == "͡" and (not nxt or unicodedata.combining(nxt)
                               or unicodedata.category(nxt) in ("Lm", "Sk")):
            return "tie bar before a mark"
        if ch == "͡" and nxt in "wj":
            return "tie bar before a glide"
    if token[-1] in PRENASAL and len(token) > 1:
        return "prenasal mark after the stop"
    if re.search(f"[{TONE_LETTERS}]ː", token):
        return "length mark after a tone letter"
    return None


def test_checker_passes_well_formed_tokens():
    assert [misordered(t) for t in ("kʷ", "ᵐk͡p", "aː˥˥", "t͡sʲ", "o")] == [None] * 5


@pytest.mark.xfail(strict=True, reason=ISSUE)
@pytest.mark.parametrize("code", ["ted", "sef", "ank", "bo", "dz"])
def test_inventory_writes_marks_in_ipa_order(code):
    bad = {t: misordered(t) for t in phoneme_inventory(get(code)) if misordered(t)}
    assert bad == {}


@pytest.mark.xfail(strict=True, reason=ISSUE)
@pytest.mark.parametrize("letter", ["ਘ", "ਝ", "ਢ", "ਧ", "ਭ"])
def test_punjabi_tone_is_not_written_on_the_onset_consonant(letter):
    assert not any(t in e for e in get("pa").graphemes[letter] for t in TONE_LETTERS)
