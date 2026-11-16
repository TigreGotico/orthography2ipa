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

def test_ch_digraph_is_the_affricate():
    """⟨ch⟩ is [t͡ʃ], not the bare palatal stop [c].

    Singh & Himmat (2013) write the phoneme as /c/ in their inventory, and
    an earlier version of this spec took that phonemic symbol as the value
    to emit. Their own phonetic description settles it the other way: the
    same paper calls /c/ "a less advanced, leaning towards alveolar,
    sometimes interdentally and affricative in nature". The zom gold is a
    narrow transcription, so it records that affricate realisation, and it
    does so in every one of its six ⟨ch⟩ headwords (chi, chil, ching,
    chivom, khutchin). Phonemic /c/ and phonetic [t͡ʃ] are not in conflict;
    the narrow value is the one this spec owes the gold.
    """
    assert ipa("cha").startswith("t͡ʃ")


def test_vowel_initial_words_take_a_glottal_onset():
    """Mortensen (2023) §2.1: Kuki-Chin syllables "tend to have a simple,
    obligatory onset", onsetless V syllables being confined to the minority
    of languages that allow them. Every one of the 33 vowel-initial
    headwords in the zom gold begins with [ʔ]."""
    for word in ("ah", "ai", "akal", "ama", "ing", "insung", "eh", "awl"):
        assert ipa(word).startswith("ʔ"), word


def test_coda_h_is_the_glottal_stop():
    """A written coda ⟨h⟩ spells [ʔ]. Singh & Himmat (2013) state that only
    p, t, k, m, n, ŋ and l occur in final position, so the letter cannot be
    standing for /h/ there; Mortensen (2023) §4.2 describes final glottal
    stop as pervasive in Kuki-Chin. Word-final and pre-consonantal ⟨h⟩ are
    both codas."""
    assert ipa("bah").endswith("ʔ")
    assert ipa("guh").endswith("ʔ")
    assert ipa("kengkoh").endswith("ʔ")
    assert "ʔp" in ipa("ahpi")
    assert "ʔs" in ipa("vohsa")


def test_onset_h_before_a_vowel_stays_h():
    """The coda rule must not swallow onset ⟨h⟩, which is a real /h/:
    Singh & Himmat list /h-/ with ha "tooth" and hoŋ "open"."""
    assert ipa("ha").startswith("h")
    assert ipa("hong").startswith("h")
    assert ipa("zumhuoi").startswith("z") and "h" in ipa("zumhuoi")


def test_mortensen_2023_is_cited_for_the_glottal_claims():
    raw = json.loads((DATA_DIR / "zom.json").read_text(encoding="utf-8"))
    sources = {s["id"]: s for s in raw["sources"]}
    assert "zom_mortensen2023" in sources
    src = sources["zom_mortensen2023"]
    assert src["author"] == "Mortensen, David R."
    assert src["url"], "citation must carry a real, fetched URL"


def test_no_encyclopedia_is_cited_as_a_source():
    """Wikipedia is a reading path, not an authority for a phonemic claim.
    It stays in the ``wikipedia`` field and out of ``sources``."""
    raw = json.loads((DATA_DIR / "zom.json").read_text(encoding="utf-8"))
    for src in raw["sources"]:
        assert "Wikipedia" not in (src.get("author") or "")
        assert "Wikipedia" not in (src.get("publisher") or "")


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
    # The measured residual once tone is folded out of both sides. This is
    # not a ceiling on the language: it moved from 0.251 to 0.156 when the
    # prosthetic glottal onset, the coda ⟨h⟩ value and the ⟨ch⟩ value were
    # corrected, all of which are recoverable from the spelling.
    assert "0.156" in notes


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
