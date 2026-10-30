"""⟨ڭ⟩ reads [ɡ] in the Maghrebi specs whose corpus writes it, and [ŋ] where it is NG.

This letter is the one case in the Arabic specs where the Unicode name actively misleads:
U+06AD is ARABIC LETTER NG, it reads [ŋ] in the specs that own it as a letter, and its
annotation lists Moroccan Arabic among its users without giving a value for that use. No
paper in the CODA line writes it. The mapping therefore rests on a dataset — what the
corpus spells with it — under the rule that a corpus may cite where a source cannot.

⟨ݣ⟩ and ⟨ڭ⟩ are near-identical on screen, kāf with three dots above against keheh with
three dots above. Everything here is keyed on the codepoint.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import emission_inventory, phoneme_inventory
from orthography2ipa.registry import get

NG = "ڭ"          # ARABIC LETTER NG — never written as a glyph in this file
KEHEH3 = "ݣ"      # ARABIC LETTER KEHEH WITH THREE DOTS ABOVE, its look-alike

READS = ["ar-MA", "ar-DZ", "ar-TN"]        # the varieties the count covers
NOT_COUNTED = ["ar-MR", "ar-LY"]           # Maghrebi, but no occurrences counted
KEEPS_NG = [("ota", "ŋ"), ("ug", "ŋ")]     # where it is a letter in its own right
SIZES = {"ar-MA": 197, "ar-DZ": 205, "ar-TN": 225}


def _inventory(code):
    spec = get(code)
    return set(phoneme_inventory(spec)) | set(emission_inventory(spec))


@pytest.mark.parametrize("code", READS)
def test_the_ng_letter_reads_g_where_the_corpus_writes_it(code):
    assert "ɡ" in G2P(code).transcribe("ب" + NG + "ب"), code


@pytest.mark.parametrize("code", READS)
def test_g_was_already_this_specs_qaf_reflex(code):
    assert "ɡ" in _inventory(code), code


@pytest.mark.parametrize("code", NOT_COUNTED)
def test_it_does_not_spread_to_varieties_the_count_does_not_cover(code):
    """A dataset citation licenses exactly what it measured, and no further.

    Mauritania and Libya are Maghrebi and both have /ɡ/, so the mapping would be free and
    would look harmless — but the count covers Moroccan, Algerian and Tunisian rows, and
    nothing here says these two write the letter. Extending a corpus measurement past the
    labels it was taken over is the dataset-citation version of citing a paper for a
    variety it never studied.
    """
    assert NG not in get(code).graphemes, code


@pytest.mark.parametrize("code, expected", KEEPS_NG)
def test_it_still_reads_as_the_nasal_where_it_is_a_letter_in_its_own_right(code, expected):
    assert expected in get(code).graphemes[NG], code


def test_the_two_lookalike_letters_are_not_confused():
    """⟨ݣ⟩ and ⟨ڭ⟩ differ by their base letter and are near-identical on screen.

    Morocco writes /ɡ/ with both at nearly the same rate, so a spec that maps one and not
    the other reads a little over half its /ɡ/ spellings — and a spec that maps one
    *believing it is the other* looks identical in a diff. This pins that they are distinct
    codepoints handled on purpose.
    """
    assert NG != KEHEH3
    assert get("ar-MA").graphemes[NG] == ["ɡ"]


@pytest.mark.parametrize("code, size", sorted(SIZES.items()))
def test_no_inventory_grew(code, size):
    assert len(_inventory(code)) == size, code


def test_each_spec_argues_from_its_own_varietys_evidence():
    """One note pasted into three specs claims one variety's evidence for all three.

    That is what the first version of this change did: the same paragraph, byte for byte,
    in ar-MA, ar-DZ and ar-TN, citing 13 Moroccan gold rows and a Moroccan word list. The
    Moroccan claim was sound and the other two were borrowing it silently — which is the
    same error as citing a paper for a variety it never studied, committed by copy-paste
    instead of by inference.

    Pinned as distinctness plus a marker each: the two specs without gold say so in their
    own words, so a reader weighing the entry can see which evidence is theirs.
    """
    notes = {c: get(c).notes[get(c).notes.index("LOAN GRAPHEME ڭ"):] for c in READS}
    assert len(set(notes.values())) == 3, "the three notes are not distinct"
    assert "OWN SCORING GOLD" in notes["ar-MA"], "ar-MA no longer claims its gold"
    # The other two carry their OWN measured word forms, so they neither need nor may
    # borrow the Moroccan gold. Each must name the dialect label its evidence came from.
    for code, label in (("ar-DZ", "Algerian-labelled"), ("ar-TN", "Tunisian-labelled")):
        assert label in notes[code], f"{code} does not name the rows its evidence came from"
        assert "ary_arab_broad" not in notes[code], f"{code} borrows Moroccan gold"


def test_the_tunisian_entry_does_not_claim_the_moroccan_reason():
    """The reading is the same in all three and the reason is not, which is the trap.

    In Moroccan rows ⟨ڭ⟩ overwhelmingly spells the qāf reflex — ڭال، ڭلت، نڭول. In
    Tunisian rows it is almost entirely French loanwords and foreign names — الالڭوريتم,
    ڭْرَافْ, فُوتُوڭْرافْ, ديياڭنستيك, أُوڭْنُونْ — and the qāf-reflex words are essentially
    absent. Both read [ɡ], so one mapping serves and a reader checking only the output
    would see nothing wrong; an earlier draft duly claimed the Moroccan reason for the
    Tunisian entry. The distinction is only visible in the note, so it is pinned there.
    """
    tn = get("ar-TN").notes
    assert "IN IMPORTED VOCABULARY" in tn
    assert "qāf reflex goes to ‹ڨ›" in tn
