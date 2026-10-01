"""Central Dagaare (dga): the map read from the IPA Illustration (T-2696).

Every expected string is the phonemic form Angsongna & Akinbo (2022) print for
that spelling, on page 343 or 345. The same examples are the dga
``primary_sources`` gold rows.
"""
import pytest

from orthography2ipa.g2p import G2P

DGA = G2P("dga")


@pytest.mark.parametrize("word, expected", [
    ("bíé", "bíí"),          # p.343 prints bíé; see the known-miss test below
    ("dɔ́ɔ́", "dɔ́ː"),         # doubled letter is one long vowel
    ("gàà", "ɡàː"),
    ("gbágá", "ɡ͡báɡá"),      # digraph reads one unit
    ("kpɛ́ré", "k͡pɛ́ɹí"),
    ("ŋmáné", "ŋ͡mání"),
    ("yírì", "jíɹì"),
    ("lúgó", "lúɡó"),
    ("dì", "dì"),            # p.345, i
    ("wà", "wà"),
    ("dú", "dú"),
])
def test_illustration_examples(word, expected):
    assert DGA.transcribe_word(word).lstrip("ˈ") == expected


@pytest.mark.parametrize("word, expected", [
    ("kógó", "kʰóɡó"),
    ("tègè", "tʰìɡì"),
    ("pɛ́gé", "pʰɛ́ɡí"),
])
def test_word_initial_voiceless_stops_are_aspirated(word, expected):
    # p.343: "all initial voiceless stops in this work are transcribed as
    # /pʰ tʰ kʰ/". Word-internally they are plain.
    assert DGA.transcribe_word(word).lstrip("ˈ") == expected


def test_the_tap_after_g():
    # p.344: /ɹ/ is realized as a tap [ɾ] after a /g/.
    assert DGA.transcribe_word("pɛ́gré").lstrip("ˈ") == "pʰɛ́ɡɾí"
    assert DGA.transcribe_word("yírì").lstrip("ˈ") == "jíɹì"


def test_dot_below_a_is_schwa():
    # The source spells ə with a dot-below letter: vạ /və́/.
    assert DGA.transcribe_word("vạ").lstrip("ˈ").startswith("və")


def test_candidate_lists_carry_the_unwritten_atr_member():
    # ⟨o⟩ stands for both o and ʊ; the second reading must stay reachable even
    # though the first is what the 1-best emits (fò /fʊ̀/ on p.345).
    cands = [c.lstrip("ˈ") for c in DGA.word_candidates("fò", k=8)]
    assert "fʊ̀" in cands, cands


@pytest.mark.parametrize("word, one_best, printed, why", [
    ("bíé", "bíí", "bíé", "⟨e⟩ reads i in 11 of 15 example tokens; this word is one of the 3 with e"),
    ("yèlé", "jìlí", "jèlé", "same candidate order"),
    ("fò", "fò", "fʊ̀", "⟨o⟩ reads o in 4 of 6 example tokens; this word is one of the 2 with ʊ"),
    ("váábó", "váːbó", "váːbʊ́", "same candidate order"),
    ("dê", "dî", "dɪ̂", "⟨e⟩ reads ɪ in 1 of 15 tokens"),
    ("ŋáà", "ŋâː", "ŋáː", "the source reads ⟨áà⟩ as falling twice and as high here"),
    ("è", "ì", "ʔì", "the orthography has no letter for the glottal stop"),
    ("vạ", "və", "və́", "the source leaves the tone unwritten in this word"),
    ("hạạri", "həːɹi", "hə́ːɹì", "the source leaves the tone unwritten in this word"),
])
def test_known_misses_are_pinned(word, one_best, printed, why):
    """The 9 words the 1-best does not reproduce, and why.

    Pinned so a later change to the map shows up here instead of moving a
    board number silently. `printed` is what the Illustration prints.
    """
    assert DGA.transcribe_word(word).lstrip("ˈ") == one_best, why
    assert DGA.transcribe_word(word).lstrip("ˈ") != printed or one_best == printed
