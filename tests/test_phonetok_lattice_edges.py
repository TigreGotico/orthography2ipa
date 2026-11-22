from orthography2ipa.phonetok import PhonetokTokenizer, _lower
from orthography2ipa.registry import get


def test_width_zero_lattice_without_a_rescorer_has_no_slots():
    assert PhonetokTokenizer(get("pt-PT")).ipa_lattice("casa", beam_width=0) == []


def test_lowercasing_with_no_language_is_plain_lowercasing():
    assert _lower("I", None) == "i"
    assert _lower("I", "tr") == "ı"
