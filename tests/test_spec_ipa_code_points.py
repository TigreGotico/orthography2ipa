"""Rule contexts and phoneme lists match the code points the engine emits.

ASCII ⟨g⟩ (U+0067) and the IPA voiced velar plosive ⟨ɡ⟩ (U+0261) look the
same in most fonts. The engine emits U+0261, so a sandhi context or an
allophone phoneme list that writes U+0067 never matches and the rule is
silently dead. The scorer folds the two (``scripts/benchmark.py``
``normalize``), which hides the dead rule from the board.
"""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "orthography2ipa" / "data"

_SANDHI_FIELDS = ("left_context", "right_context", "transform", "right_transform")
_ALLOPHONE_FIELDS = (
    "phonemes", "surface", "append", "mutates_neighbor",
    "preceded_by_phoneme", "followed_by_phoneme",
    "preceded_by_phoneme_2", "followed_by_phoneme_2",
    "preceded_by_surface_phoneme_2",
)

#: FR_ENCHAÎNEMENT replaces the matched consonant with ‿, which deletes it.
#: A ɡ in its class would be deleted the same way, so the class and the
#: transform must change together.
_KNOWN = {("fr-FR", "FR_ENCHAÎNEMENT", "left_context")}


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _strings(item)


def _ascii_g_fields():
    found = set()
    specs = sorted(DATA.glob("*.json"))
    for path in specs:
        spec = json.loads(path.read_text(encoding="utf-8"))
        rules = [(r, _SANDHI_FIELDS) for r in spec.get("sandhi_rules") or []]
        rules += [(r, _ALLOPHONE_FIELDS) for r in spec.get("allophone_rules") or []]
        for rule, fields in rules:
            for field in fields:
                if any("g" in s for s in _strings(rule.get(field))):
                    found.add((path.stem, rule["id"], field))
    return found, len(specs)


def test_no_ascii_g_in_rule_ipa_fields():
    found, scanned = _ascii_g_fields()
    assert scanned > 7000
    assert found - _KNOWN == set()
