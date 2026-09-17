"""Two letters the Maghrib writes that every Maghrebi spec was dropping.

⟨ݣ⟩ is a borrowed-sound letter and ⟨ڢ⟩ is not one at all — it is fāʾ in the Maghribi hand
— so they are cited separately and scoped differently. ⟨ݣ⟩ goes only where Kew 2003 puts
it, Morocco and Mauritania; ⟨ڢ⟩ goes on the ar-x-maghrebi node because its sources describe
the script tradition and name the region rather than a country.

The absences matter as much as the readings. ⟨ݣ⟩ must NOT spread to the Maghrebi specs Kew
does not name, and U+06AD ARABIC LETTER NG must stay unmapped — the proposal itself warns
that the two are visually identical in initial and medial joined forms, so a reader who
assumes they are interchangeable will map the wrong one.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import emission_inventory, phoneme_inventory
from orthography2ipa.registry import get

GAF_READS = ["ar-MA", "ar-MR"]          # Kew 2003 §3 p.5 (Morocco), p.6 (Mauritania)
GAF_REFUSES = ["ar-DZ", "ar-TN", "ar-LY", "ar-x-maghrebi"]
FEH_READS = ["ar-MA", "ar-DZ", "ar-TN", "ar-MR", "ar-LY", "ar-x-maghrebi"]

# Sizes before this change: neither letter may introduce a phone.
SIZES = {"ar-MA": 197, "ar-DZ": 205, "ar-TN": 225, "ar-MR": 225,
         "ar-LY": 227, "ar-x-maghrebi": 193}


def _inventory(code):
    spec = get(code)
    return set(phoneme_inventory(spec)) | set(emission_inventory(spec))


@pytest.mark.parametrize("code", GAF_READS)
def test_moroccan_gaf_reads_g(code):
    assert "ɡ" in G2P(code).transcribe("بݣب"), code


@pytest.mark.parametrize("code", GAF_REFUSES)
def test_moroccan_gaf_does_not_spread_past_its_source(code):
    """Unmapped in Algeria, Tunisia and Libya — pinning a DEFECT that has a price.

    Kew names Morocco and Mauritania; those three are not in it, and they all have /ɡ/,
    so mapping there would be free and would look harmless. That is why the absence is
    tested rather than left as a decision nobody wrote down.

    But it is not costless. The data lane counts ⟨ݣ⟩ 3,448 times in lahgtna's judged
    tree — ma 3,042, dz 328, tn 61, ly 2 — so refusing it here drops **391 occurrences**
    in silence. Those varieties more usually write ⟨ڨ⟩ for the same sound and #1592 maps
    that, which is why the loss is tolerable for now and not why it is acceptable
    permanently. Citation-blocked, on the defect list, not settled.
    """
    assert "ݣ" not in get(code).graphemes, code


@pytest.mark.parametrize("code", FEH_READS)
def test_maghribi_feh_reads_f(code):
    assert "f" in G2P(code).transcribe("بڢب"), code


def test_maghribi_feh_is_not_a_borrowed_consonant():
    """It is fāʾ in the Maghribi hand, so it reads what ⟨ف⟩ reads, not a foreign phone."""
    assert get("ar-x-maghrebi").graphemes["ڢ"] == get("ar-x-maghrebi").graphemes.get(
        "ف", ["f"]
    ) or get("ar-x-maghrebi").graphemes["ڢ"] == ["f"]


def test_the_confusable_ng_letter_stays_unmapped():
    """U+06AD is visually identical to ⟨ݣ⟩ in initial and medial joined forms.

    Kew 2003 says so in the proposal that encoded ⟨ݣ⟩, and both letters occur in real
    text. Mapping U+06AD by assuming it is the same letter is the specific mistake that
    warning exists to prevent, so the absence is pinned until it gets its own source.

    The cost is not small and an earlier draft badly understated it as "one occurrence".
    That was the Saudi-oriented pool's count. Over lahgtna's judged tree the data lane
    counts U+06AD **3,250 times** — ma 2,742, dz 391, tn 80 — against 3,042 Moroccan
    occurrences of ⟨ݣ⟩. Morocco writes /ɡ/ with both letters at about the same rate, so
    this PR adds a /ɡ/ letter to ar-MA while the spec still drops the other one. It is
    the largest unmapped letter counted so far.
    """
    for code in GAF_READS:
        assert "ڭ" not in get(code).graphemes, code


@pytest.mark.parametrize("code, size", sorted(SIZES.items()))
def test_the_inventory_did_not_grow(code, size):
    assert len(_inventory(code)) == size, code
