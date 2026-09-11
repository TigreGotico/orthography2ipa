"""Regression test for the Nivkh (niv) Cyrillic soft sign ⟨ь⟩.

``niv.json`` used to map the bare soft sign to an empty candidate, deleting it
outright, except for the single ⟨нь⟩ multigraph key. The soft sign is a
palatalisation mark, not a silent letter -- the ru and uk specs already map it
to /ʲ/ and compose it onto the preceding consonant.

The northeuralex and wikipron golds agree that two more of the resulting
sequences are not plain C+ʲ concatenations but distinct single IPA segments:
д+ь -> ɟ, т+ь -> c (matching the already-present н+ь -> ɲ). Those two earn
Cyrillic+ь multigraph keys; the bare soft sign otherwise composes /ʲ/
generically for Russian loanwords (e.g. р+ь -> rʲ in "сентябрь", л+ь -> lʲ in
"учитель"), no key of their own, per the ru ⟨бь⟩ precedent in AGENTS.md.
"""
from orthography2ipa.json_loader import load_json_spec

import orthography2ipa


def test_niv_spec_maps_bare_soft_sign_to_palatalisation():
    spec = load_json_spec("niv")
    assert list(spec.graphemes["ь"]) == ["ʲ"]


def test_niv_spec_maps_the_fused_palatalised_consonants():
    spec = load_json_spec("niv")
    assert list(spec.graphemes["нь"]) == ["ɲ"]
    assert list(spec.graphemes["дь"]) == ["ɟ"]
    assert list(spec.graphemes["ть"]) == ["c"]


def test_niv_soft_sign_palatalises_the_preceding_consonant():
    # видь: gold v i ɟ (wikipron). Was v i d when ь deleted silently.
    assert orthography2ipa.transcribe("видь", "niv") == "viɟ"
    # выть: gold v ɤ c (wikipron).
    assert orthography2ipa.transcribe("выть", "niv") == "vɨc"
    # ань: gold a ɲ (wikipron).
    assert orthography2ipa.transcribe("ань", "niv") == "æɲ"


def test_niv_soft_sign_composes_generic_palatalisation_off_its_own_key():
    # сентябрь: gold sɪentjæbrʲ (northeuralex) has rʲ -- р has no dedicated
    # Cyrillic+ь key, the bare soft sign composes /ʲ/ onto it directly.
    assert "rʲ" in orthography2ipa.transcribe("сентябрь", "niv")
