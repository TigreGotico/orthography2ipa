"""The pa/vox_communis row: notation folds, then two counted residues.

Vowel length, ɑ for long ⟨ਾ⟩ and the tone letter are the gold's notation and
fold 0.4432 to 0.1131. The residue is medial schwa deletion (836 of 4003
words) and final devoicing of the voiced aspirates (35 words), both real
Punjabi phonology the spec's notes already cite and leave unmodelled. No
`valid_ceiling`: Gurmukhi writes every contrast the folds touch.
"""
from orthography2ipa import json_loader


def test_vox_communis_is_an_audit_not_a_ceiling():
    spec = json_loader.load_json_spec("pa")
    assert "vox_communis" not in (spec.valid_ceiling or {})
    entry = spec.audit["vox_communis"]
    assert entry.conclusion == "at_ceiling_documented"
    for number in ("0.4432", "0.2176", "0.1282", "0.1131", "836"):
        assert number in entry.measured, number


def test_the_residues_are_named_with_their_sources():
    entry = json_loader.load_json_spec("pa").audit["vox_communis"]
    assert "schwa deletion" in entry.measured
    assert "Singh & Lehal" in entry.measured
    assert "fold_pa_notation.py" in entry.measured
