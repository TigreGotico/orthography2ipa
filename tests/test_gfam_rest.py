"""The rest of the /ɡ/-family letters, in the varieties whose corpus attests them.

Arabic writers use five different codepoints for the same sound — ⟨گ ڨ ݣ ڭ ګ⟩ — and
which one a variety reaches for is a fact about its keyboards and its printers, not
about its phonology. A spec that declares one and drops the others deletes a consonant
in silence, and when it carries a haraka the vowel survives, so the word comes out
well-formed and wrong.

None of these adds a phone: every spec below already reads [ɡ] from some letter.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P

CASES = [
    ("ar-DZ", "ݣ"), ("ar-DZ", "ګ"),
    ("ar-TN", "ݣ"), ("ar-TN", "ګ"),
    ("ar-LB", "ڭ"), ("ar-MA", "ګ"), ("ar-LY", "ڭ"),
]

#: Attested and deliberately still unmapped. ⟨ڨ⟩ occurs outside the Maghreb in Sudanese,
#: Palestinian, Libyan, Najdi and Yemeni rows — all qāf words — and that is the evidence
#: test_qaf_three_dots.py exists to refuse: the cited source names Algerian, Moroccan and
#: Tunisian and nothing beyond. Six rows in 52,406 Najdi ones, for a letter one dot away
#: from ⟨ق⟩, is as well explained by a typo as by a usage.
STILL_REFUSED = [("ar-SD", "ڨ"), ("ar-PS", "ڨ"), ("ar-LY", "ڨ"),
                 ("ar-SA-x-najd", "ڨ"), ("ar-YE", "ڨ")]


@pytest.mark.parametrize("code,letter", CASES)
def test_the_letter_is_declared(code, letter):
    assert get(code).graphemes.get(letter) == ["ɡ"], f"{code} {letter}"


@pytest.mark.parametrize("code,letter", CASES)
def test_the_letter_reaches_the_output(code, letter):
    assert "ɡ" in G2P(code).transcribe(f"ب{letter}ب"), f"{code} {letter}"


@pytest.mark.parametrize("code,letter", CASES)
def test_the_vowel_is_no_longer_orphaned(code, letter):
    """What the silence cost: the consonant went and its haraka stayed."""
    out = G2P(code).transcribe(f"ت{letter}ُول")
    assert "ɡ" in out, f"{code} {letter}: {out!r}"


@pytest.mark.parametrize("code", sorted({c for c, _ in CASES}))
def test_no_phone_is_added(code):
    """Each spec already made this sound before this change.

    The claim is about the inventory, not about which letter carries it. In ar-MA and
    ar-LB [ɡ] arrives only through the gaf family, licensed letter by letter in earlier
    work with its own sources — so another member of that family is another spelling of
    a phone the spec already has, which is the same argument. A spec with no [ɡ] at all
    would be an inventory claim needing its own source, and fails here rather than
    passing quietly.
    """
    g = get(code).graphemes or {}
    added_here = {letter for c, letter in CASES if c == code}
    before = {p for letter, v in g.items() if letter not in added_here for p in v}
    assert any("ɡ" in p for p in before), (
        f"{code}: nothing outside {sorted(added_here)} offers [ɡ], so this change would "
        "add a phone rather than a spelling and needs an inventory citation")


@pytest.mark.parametrize("code,letter", STILL_REFUSED)
def test_attestation_alone_does_not_carry_the_three_dot_qaf(code, letter):
    """Corpus frequency is not a source, and this is where that line is drawn.

    These are attested, in qāf words, and still refused: the counts are noise-level for
    a letter a single dot away from ⟨ق⟩, and the cited orthographic source for ⟨ڨ⟩ names
    the Maghreb only. Pinned so the absence cannot erode quietly the next time somebody
    counts rows.
    """
    assert letter not in get(code).graphemes, f"{code} gained {letter} on frequency alone"


def test_a_variety_with_no_attestation_does_not_gain_them():
    """The negative control. ar-JO has no rows in the corpus at all."""
    g = get("ar-JO").graphemes or {}
    assert not ({"گ", "ݣ", "ڭ", "ګ"} & set(g)), (
        "ar-JO gained a gaf-family letter with nothing attesting it")
