"""Regression test for the Southern Yukaghir (yux) Cyrillic soft sign ⟨ь⟩.

``yux.json`` used to map the bare soft sign to an empty candidate, deleting it
outright, and its one existing ⟨дь⟩ multigraph key produced the wrong value:
``dʲ``, a plain concatenation of д (d) and the generic palatalisation ʲ, fails
the AGENTS.md test that a multigraph key's value is not the concatenation of
its parts -- and disagrees with the gold, which shows the affricate ``d͡ʑ``.

The wikipron gold (46 of 255 rows contain ⟨ь⟩, all showing a palatal segment)
gives three fused sequences: д+ь -> d͡ʑ (22 words, e.g. "абудьэ" -> a w u d͡ʑ ə),
л+ь -> ʎ (19 words, e.g. "пиполь" -> p ɪ p o ʎ) and н+ь -> ɲ (9 words,
e.g. "ньаадэ" -> ɲ aː d ə, already correct before this fix). No occurrence of
a bare ⟨ь⟩ outside of these three digraphs appears in the gold, so the generic
ь -> ʲ mapping is untested by this corpus but is added for correctness and
parity with ru/uk, matching the ket/yrk/niv siblings in this defect class.
"""
from orthography2ipa.json_loader import load_json_spec

import orthography2ipa


def test_yux_spec_maps_bare_soft_sign_to_palatalisation():
    spec = load_json_spec("yux")
    assert list(spec.graphemes["ь"]) == ["ʲ"]


def test_yux_spec_maps_the_fused_palatalised_consonants():
    spec = load_json_spec("yux")
    assert list(spec.graphemes["нь"]) == ["ɲ"]
    assert list(spec.graphemes["дь"]) == ["d͡ʑ"]
    assert list(spec.graphemes["ль"]) == ["ʎ"]


def test_yux_soft_sign_fuses_the_preceding_consonant():
    # абудьэ: gold a w u d͡ʑ ə (wikipron); the spec does not model the
    # б -> w allophony or vowel reduction, so it composes "abud͡ʑe". Was
    # "abudʲe" when дь -> dʲ.
    assert orthography2ipa.transcribe("абудьэ", "yux") == "abud͡ʑe"
    # пиполь: gold p ɪ p o ʎ (wikipron). Was "pipol" when ь deleted silently.
    assert orthography2ipa.transcribe("пиполь", "yux") == "pipoʎ"
    # ньаадэ: gold ɲ aː d ə (wikipron), already correct; the spec does not
    # model vowel length or reduction.
    assert orthography2ipa.transcribe("ньаадэ", "yux") == "ɲaade"
