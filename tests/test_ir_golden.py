"""G2P gives the recorded output on a fixed sample of the gold words.

``tests/data/ir_golden_ci.json`` maps a code to ``[word, ipa]`` rows: at
most 300 WikiPron words of every 15th code with a WikiPron set, plus pt-PT,
as ``scripts/ir_parity.py --write-golden`` recorded them from the rules
engine. ``scripts/ir_parity.py --golden`` runs the full set.
"""
import json
from pathlib import Path

import pytest

from orthography2ipa import G2P

GOLDEN = json.loads((Path(__file__).parent / "data" / "ir_golden_ci.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("code", sorted(GOLDEN))
def test_output_equals_the_recorded_output(code):
    g = G2P(code)
    rows = GOLDEN[code]
    assert [g.transcribe(word) for word, _ in rows] == [ipa for _, ipa in rows]
