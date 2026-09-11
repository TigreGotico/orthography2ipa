"""Gold forensics for the Nupe (``nup``) coda-nasal contexts.

The spec resolves a spelled vowel + ⟨n⟩/⟨m⟩ + oral consonant to a
tone-bearing syllabic nasal [ŋ] with an oral vowel before it (Kawu 2002 on
the Nupe syllabic/moraic nasal; Banfield & Macintyre 1915, *A Grammar of
the Nupe Language*, "The Alphabet", pp. 14-15, which writes the nasal as a
distinct letter with "a strong nasal n sound as in the French word mon").

The shipped wikipron/nup gold is split on that context, and this file pins
the split so it is not mistaken for a rule the engine could condition on.
The two sets are not separated by anything in the spelling: ``enangi``
carries both a nasalised vowel and the syllabic nasal, while the
near-identical ``eyangici`` carries neither. Choosing branch (3) follows
the majority of the gold and the cited description; the minority is
documented in the spec notes, not fitted.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

DATA_DIR = (pathlib.Path(__file__).parent.parent
            / "orthography2ipa" / "data")
SCRIPTS_DIR = pathlib.Path(__file__).parent.parent / "scripts"

_VNC = re.compile(r"(?=([aeiou])([nm])([bcdfgjklprstvzh]))")


def _load_gold():
    sys.path.insert(0, str(SCRIPTS_DIR))
    import benchmark as bm
    return bm.load_wikipron("nup", 10 ** 9)


def test_notes_record_the_measured_split():
    notes = json.loads(
        (DATA_DIR / "nup.json").read_text(encoding="utf-8"))["notes"]
    assert "MAJORITY reading of a gold that is split" in notes
    assert "54 gold rows" in notes
    assert "44 of those 48" in notes


def test_gold_is_split_thirty_to_twentyfour_on_the_coda_nasal():
    rows = [(w, g.replace(" ", "")) for w, g in _load_gold()
            if _VNC.search(w.lower())]
    assert len(rows) == 54

    with_eng = [w for w, g in rows if g.count("ŋ") >= len(
        _VNC.findall(w.lower()))]
    without_eng = [w for w, g in rows if "ŋ" not in g]

    assert len(with_eng) == 30
    assert len(without_eng) == 24
    # no row is partially resolved: every row goes one way or the other
    assert len(with_eng) + len(without_eng) == len(rows)

    assert "dangi" in with_eng
    assert "gbingan" in without_eng


def test_the_split_has_no_orthographic_conditioning():
    """The minimal near-pair that refutes any spelling-driven conditioning:
    both spell ⟨ang⟩ between vowels, and the gold resolves them oppositely.
    """
    gold = {w: g.replace(" ", "") for w, g in _load_gold()}
    assert "ŋ" in gold["enangi"]
    assert "ŋ" not in gold["eyangici"]
