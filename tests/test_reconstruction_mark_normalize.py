"""A leading asterisk on a gold transcription marks a form that is not
attested — one inferred rather than recorded (Graffi 2002, "The asterisk from
historical to descriptive and theoretical linguistics", Historiographia
Linguistica 29(3):329-338, doi:10.1075/hl.29.3.04gra). It is a status
annotation, not a segment. ``benchmark.normalize`` must strip it, the same way
it strips punctuation and folds ASCII "g" onto IPA "ɡ": no engine can emit it,
so scoring it as a phoneme charges an insertion error no correct transcription
can avoid.

The stripping is load-bearing for real board rows, not hypothetical. WikiPron's
Tibetan scrape carries the mark on 1538 of 3621 rows — the Old Tibetan readings
en.wiktionary's Module:bo-pron infers from the spelling, beside the Lhasa ones
— and its Old French scrape on 4. Read the ``_RECONSTRUCTION_MARK`` comment in
scripts/benchmark.py for what the fold costs: the mark can also sit on a
reconstructed pronunciation of an attested headword, and stripping lets that
reading compete as if it had been recorded.
"""
import glob
import importlib.util
import json
import os
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_spec = importlib.util.spec_from_file_location(
    "bm", _ROOT / "scripts" / "benchmark.py")
bm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bm)
normalize = bm.normalize


def _n(s: str, broad: bool = True, strip_stress: bool = True) -> str:
    return normalize(s, strip_stress=strip_stress, broad=broad)


def test_reconstruction_mark_is_not_a_segment():
    assert _n("* k a") == "ka"


def test_reconstruction_mark_stripped_in_narrow_and_stressed_modes():
    for broad in (False, True):
        for strip_stress in (False, True):
            assert "*" not in _n("*pəlykeɾ", broad=broad,
                                 strip_stress=strip_stress)


def test_starred_and_unstarred_gold_normalize_alike():
    assert _n("* k a k a r a ŋ") == _n("k a k a r a ŋ")


def test_no_registered_spec_inventory_contains_the_mark():
    """The precondition for stripping unconditionally: an asterisk is never a
    phoneme any spec claims. Guards the fold the way the ``g``/``ɡ`` comment
    says it was guarded when that one was added.
    """
    offenders = []
    for path in glob.glob(str(_ROOT / "orthography2ipa" / "data" / "*.json")):
        spec = json.load(open(path, encoding="utf-8"))
        if any("*" in str(p) for p in (spec.get("phonemes") or [])):
            offenders.append(os.path.basename(path))
    assert offenders == []
