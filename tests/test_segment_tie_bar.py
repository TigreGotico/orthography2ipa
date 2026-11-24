"""A tie bar joins two letters into one segment. IPA chart (2020), "Other
symbols": "Affricates and double articulations can be represented by two
symbols joined by a tie bar if necessary." Marks after the second letter
belong to the whole segment."""
import pytest

from orthography2ipa import get
from orthography2ipa.allophony import segment_ipa
from orthography2ipa.inventory import phoneme_inventory

TIE_BAR_ISSUE = "https://github.com/TigreGotico/orthography2ipa/issues/2514"


def test_bare_affricate_is_one_segment_with_its_atom():
    assert segment_ipa("t͡s", ["t͡s"]) == ["t͡s"]


@pytest.mark.xfail(strict=True, reason=TIE_BAR_ISSUE)
@pytest.mark.parametrize("ipa, segments", [
    ("t͡s", ["t͡s"]),
    ("t͡sʲ", ["t͡sʲ"]),
    ("t͡ɕː", ["t͡ɕː"]),
    ("at͡ʃʰa", ["a", "t͡ʃʰ", "a"]),
])
def test_tie_bar_keeps_the_second_letter_and_its_marks(ipa, segments):
    assert segment_ipa(ipa) == segments


@pytest.mark.xfail(strict=True, reason=TIE_BAR_ISSUE)
def test_no_inventory_token_ends_in_a_tie_bar():
    assert [t for t in phoneme_inventory(get("av")) if t.endswith("͡")] == []
