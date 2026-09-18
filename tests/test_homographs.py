"""Letters borrowed from other Arabic-script keyboards read what they stand in for.

Writers of Arabic reach for Urdu, Sindhi, Pashto and Kurdish letters that look almost
identical to an Arabic one. That is a keyboard or a font, not a phonological choice —
and an undeclared letter is deleted in silence, taking its consonant and stranding any
haraka it carried.

The substitution is measured: every form carrying one of these in the judged corpus was
respelled with the Arabic lookalike and looked for in the same variety. ⟨ۏ⟩ and ⟨ۅ⟩
reach 100% — every form written with them also occurs written with ⟨و⟩.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import phoneme_inventory

# letter, the Arabic letter it stands in for
PAIRS = [("ۃ", "ة"), ("ٳ", "إ"), ("ہ", "ه"), ("ڠ", "غ"), ("ۉ", "و"), ("ە", "ه"),
         ("ے", "ي"), ("ټ", "ت"), ("ړ", "ر"), ("ۏ", "و"), ("ۅ", "و"), ("ݜ", "ش"),
         ("ں", "ن"), ("ۆ", "و"), ("ې", "ي"), ("ڕ", "ر"), ("ڜ", "ش"), ("ٽ", "ت"),
         ("ۋ", "و"), ("ٹ", "ت"), ("ۈ", "و"), ("ډ", "د")]


@pytest.mark.parametrize("letter,base", PAIRS)
def test_it_reads_exactly_what_it_stands_in_for(letter, base):
    g = get("arb").graphemes
    assert g[letter] == g[base], f"{letter} reads {g[letter]}, {base} reads {g[base]}"


@pytest.mark.parametrize("letter,base", PAIRS)
def test_the_dialect_leaves_inherit_it(letter, base):
    """Declared on the shared dialectal ancestor, so every Arabic dialect gets it."""
    for code in ("ar-EG", "ar-MA", "ar-SA-x-najd", "ar-DZ"):
        assert letter in get(code).graphemes, f"{code} does not inherit {letter}"


@pytest.mark.parametrize("letter,base", PAIRS)
def test_no_phone_is_added(letter, base):
    """It reads an existing letter's reading, so the inventory cannot grow."""
    inv = phoneme_inventory(get("arb"))
    for p in get("arb").graphemes[letter]:
        assert p in inv, f"{letter} introduced {p}"


def test_the_consonant_is_no_longer_dropped():
    """What the silence cost, on a real corpus form: الۏقت for الوقت."""
    out = G2P("ar-MA").transcribe("الۏقت")
    assert "w" in out or "uː" in out, out


def test_the_letter_refused_for_thin_evidence_stays_refused():
    """⟨ڊ⟩ was measured at 2 of 8 forms twinned — too thin to tell a substitution from
    a coincidence. Pinned so it is not swept in later with the rest."""
    assert "ڊ" not in get("arb").graphemes


def test_this_does_not_touch_the_languages_these_letters_belong_to():
    """An orthographic claim about Arabic text, not a claim on Urdu or Pashto."""
    ur = get("ur").graphemes
    assert ur.get("ٹ") and ur["ٹ"] != get("arb").graphemes["ٹ"], (
        "Urdu's own reading of its retroflex ṭ was overwritten")
