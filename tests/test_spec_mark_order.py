"""Mark order in spec inventories. A tie bar joins two letters: IPA chart,
"Other symbols": "Affricates and double articulations can be represented by
two symbols joined by a tie bar if necessary." A glide after a stop is
labialization or palatalization (``kʷ``), not a tie. A length mark belongs to
its segment, so it stands before the tone letters of the syllable."""
import re

import pytest

from orthography2ipa import get
from orthography2ipa.inventory import phoneme_inventory

ISSUE = "https://github.com/TigreGotico/orthography2ipa/issues/2515"
TONE_LETTERS = "˥˦˧˨˩"


def misordered(token):
    for before, after in zip(token, token[1:]):
        if before == "͡" and after in "ːˑ":
            return "tie bar before a length mark"
        if before == "͡" and after in "wj":
            return "tie bar before a glide"
    if re.search(f"[{TONE_LETTERS}][ːˑ]", token):
        return "length mark after a tone letter"
    return None


def test_checker_passes_well_formed_tokens():
    assert [misordered(t) for t in ("kʷ", "k͡p", "aː˥˥", "t͡sʲ", "o˥")] == [None] * 5


@pytest.mark.xfail(strict=True, reason=ISSUE, raises=AssertionError)
@pytest.mark.parametrize("code", ["ted", "ank", "eto", "god"])
def test_spec_writes_no_tie_bar_before_a_glide_or_a_length_mark(code):
    bad = {t: misordered(t) for t in phoneme_inventory(get(code)) if misordered(t)}
    assert bad == {}


@pytest.mark.xfail(strict=True, reason=ISSUE, raises=AssertionError)
@pytest.mark.parametrize("code", ["bo", "dz"])
def test_inventory_puts_the_length_mark_before_the_tone_letters(code):
    bad = sorted(t for t in phoneme_inventory(get(code)) if misordered(t))
    assert bad == []


@pytest.mark.xfail(strict=True, reason=ISSUE, raises=AssertionError)
@pytest.mark.parametrize("letter", ["ਘ", "ਝ", "ਢ", "ਧ", "ਭ"])
def test_punjabi_tone_is_not_written_on_the_onset_consonant(letter):
    assert not any(t in e for e in get("pa").graphemes[letter] for t in TONE_LETTERS)
