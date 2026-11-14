"""The sl/vox_communis row: three measured rules, then a ceiling for what the spelling does not write.

The syllabic ⟨r⟩ is [ər], word-final obstruents are voiceless, and an
obstruent before a voiceless obstruent is voiceless; the gold agrees on 228 of
246, 123 of 126 and 176 of 181 words. The gold then marks pitch accent and
length on 6593 of 6603 words, which the spelling never writes, so the row
carries a `valid_ceiling` of 0.0712 measured by `scripts/fold_sl_notation.py`.
"""
import pytest

from orthography2ipa import G2P, json_loader


def test_vox_communis_ceiling_is_recorded_with_its_numbers():
    spec = json_loader.load_json_spec("sl")
    entry = spec.valid_ceiling["vox_communis"]
    assert entry.per == 0.0712
    for number in ("0.3451", "0.2576", "0.0819", "0.0712", "6593", "0.0158"):
        assert number in entry.citation, number
    assert "fold_sl_notation.py" in entry.citation
    assert "not predictable" in entry.citation


@pytest.mark.parametrize("word, expected", [
    ("vrh", "vərx"),
    ("srce", "sərtsɛ"),
    ("prst", "pərst"),
    ("rdeč", "ərdɛtʃ"),
    ("vrata", "vrata"),      # a vowel after the r: no schwa
    ("brez", "brɛs"),
    ("grad", "ɡrat"),
    ("mož", "mɔʃ"),
    ("odšla", "ɔtʃla"),
    ("sladko", "slatkɔ"),
    ("izpustiti", "ispustiti"),
    ("dobro", "dɔbrɔ"),      # a voiced obstruent before a sonorant stays voiced
])
def test_the_three_rules(word, expected):
    assert G2P("sl").transcribe_word(word) == expected
