"""The ba/vox_communis row is a symbol-set difference, not a defect.

The gold writes each Bashkir vowel and the voiced uvular in a different IPA
symbol; aligning the symbol sets takes 0.4047 to 0.0099 with 94.4% exact
matches. No `valid_ceiling`: Cyrillic writes every contrast the folds touch.
"""
import os
import sys

from orthography2ipa import json_loader

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))


def test_vox_communis_is_an_audit_not_a_ceiling():
    spec = json_loader.load_json_spec("ba")
    assert "vox_communis" not in (spec.valid_ceiling or {})
    entry = spec.audit["vox_communis"]
    assert entry.conclusion == "at_ceiling_documented"
    for number in ("0.4047", "0.0701", "0.0514", "0.0435", "0.0099", "94.4"):
        assert number in entry.measured, number


def test_the_vowel_swap_is_simultaneous_not_chained():
    """our a -> their ɑ and their a -> our æ chain; a letter-by-letter
    replace would turn our æ into ɑ. The mapping must be one pass."""
    import fold_ba_notation as F
    assert F.swap_vowels("aæ") == "ɑa"
    assert F.swap_vowels("ɯeø") == "ɤɘɵ"
