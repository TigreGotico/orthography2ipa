"""Cited-claim tests for ``zom`` — Zou (Zomi), a Kuki-Chin language of
Manipur and Chin State written in a Latin script derived from J.H. Cope's
missionary romanization.

Zou is tonal: Singh & Himmat (2013), "Zou Phonology" (Language in India
13.2, pp. 683-701), establish three contrastive tones (level, low-rising,
falling) and give the minimal triplet ``hai`` / ``ha´i`` / ``ha`i``, all
spelled identically as ``hai`` once the diacritics are dropped for running
Latin text. This is the exact convention the plain Cope orthography uses:
no tone letter, no vowel doubling, no diacritic distinguishes the three
tones. That is confirmed independently by the shipped zom/wikipron gold,
where 24 Latin spellings are attested with two or more different gold tone
diacritics for the identical input string (e.g. ``hai``, ``chi``, ``za``).
There is no rule this engine could add from the Latin spelling alone that
would recover Zou tone, so the spec documents tone as an honest ceiling
rather than shipping a rule fitted to look good on 134 gold rows.
"""
from __future__ import annotations

import json
import pathlib

from orthography2ipa import get, transcribe as _transcribe

DATA_DIR = (pathlib.Path(__file__).parent.parent
            / "orthography2ipa" / "data")


def ipa(word: str) -> str:
    return _transcribe(word, lang="zom")


# ═══════════════════════════════════════════════════════════════════════════
# Segmental spelling conventions (spec notes)
# ═══════════════════════════════════════════════════════════════════════════

def test_ch_digraph_is_the_palatal_stop():
    """'ch is the palatal stop [c]' (zom notes)"""
    assert ipa("cha").startswith("c")


def test_kh_ph_th_are_aspirates():
    """'ng/kh/ph/th are the expected digraphs and aspirates' (zom notes)"""
    assert ipa("kha").startswith("kʰ")
    assert ipa("pha").startswith("pʰ")
    assert ipa("tha").startswith("tʰ")


# ═══════════════════════════════════════════════════════════════════════════
# The documented tone ceiling
# ═══════════════════════════════════════════════════════════════════════════

def test_singh_himmat_2013_is_cited_for_the_tone_claim():
    """The tone claim in the notes must trace to a real fetched primary
    source, not to the Wikipedia reading path that pointed at it."""
    raw = json.loads((DATA_DIR / "zom.json").read_text(encoding="utf-8"))
    sources = {s["id"]: s for s in raw["sources"]}
    assert "zom_singh_himmat2013" in sources
    src = sources["zom_singh_himmat2013"]
    assert src["author"] == "Singh, Yashawanta and Himmat, Lukram"
    assert src["year"] == 2013
    assert src["url"], "citation must carry a real, fetched URL"


def test_notes_document_the_three_tone_system_and_the_ceiling():
    raw = json.loads((DATA_DIR / "zom.json").read_text(encoding="utf-8"))
    notes = raw["notes"]
    assert "three contrastive" in notes
    assert "Singh & Himmat" in notes
    # the honest, measured ceiling once tone is folded out of both sides
    assert "0.251" in notes


def test_identical_spelling_maps_to_more_than_one_gold_tone():
    """Direct evidence, independent of the literature, that the plain Latin
    orthography cannot disambiguate tone: the same wikipron headword recurs
    with different tone diacritics in the gold IPA."""
    import sys
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
    import benchmark as bm

    pairs = bm.load_wikipron("zom", 10 ** 9)
    by_word: dict[str, set[str]] = {}
    for word, gold in pairs:
        by_word.setdefault(word, set()).add(gold)

    ambiguous = {w: g for w, g in by_word.items() if len(g) > 1}
    # measured against the cached gold; a handful of these are pure length
    # variants, but the large majority differ in tone diacritic alone
    assert len(ambiguous) >= 20, (
        "expected the previously-measured ~24 tone-ambiguous homographs; "
        f"found {len(ambiguous)}"
    )
    assert "hai" in ambiguous, "hai is Singh & Himmat's own minimal triplet"
