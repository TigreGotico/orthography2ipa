"""Ratchet: living research and production specs may not ship without stress.

A spec at ``research`` or ``production`` tier describes a living language well
enough to be benchmarked, and docs/specs/quality_tiers.md asks such a spec for a
``stress`` block when the language has word stress that the spelling lets a
rule predict. Many specs do not have one yet. This test pins that set, read
after inheritance (a dialect that inherits its base's block is covered), so
the set can only shrink:

* a spec that joins it fails the test;
* a pinned spec that gains a block also fails it until the spec is removed
  from tests/data/stress_ratchet_pinned.txt, so the pin keeps up with the data.

Clade nodes, stubs, skeletons and historical specs (a ``timespan`` with an
``end_year``) are out of scope. The schema has no field that declares "this
language has no word stress"; ``"stress": false`` only opts a spec out of an
inherited block. So tone languages stay in the pinned set, and so does a spec
that opts out. So do languages whose stress the schema cannot express, such as
Assamese (Mahanta 2012: 222); their notes say why.
"""
import pathlib
import warnings

from orthography2ipa import get
from orthography2ipa.types import QualityTier

DATA_DIR = pathlib.Path(__file__).parent.parent / "orthography2ipa" / "data"

PINNED_FILE = pathlib.Path(__file__).parent / "data" / "stress_ratchet_pinned.txt"
PINNED = frozenset(
    line.strip() for line in PINNED_FILE.read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.startswith("#"))


def _stressless_living_specs():
    """Codes of living research/production specs with no stress after inheritance."""
    found = set()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for path in sorted(DATA_DIR.glob("*.json")):
            spec = get(path.stem)
            if spec.clade or spec.quality not in (QualityTier.RESEARCH,
                                                  QualityTier.PRODUCTION):
                continue
            if spec.timespan is not None and spec.timespan.end_year is not None:
                continue
            if spec.stress is None:
                found.add(path.stem)
    return found


def test_stressless_set_only_shrinks():
    current = _stressless_living_specs()
    joined = sorted(current - PINNED)
    stale = sorted(PINNED - current)
    assert not joined, (
        f"living research/production specs with no stress block: {joined}. "
        "Give each a cited stress block, or let it inherit one from its "
        "graphemes_base or a same-language parent.")
    assert not stale, (
        f"these specs now resolve a stress block or left the scope; "
        f"remove them from tests/data/stress_ratchet_pinned.txt: {stale}")
