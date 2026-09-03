"""Regression test for the Ket (ket) Cyrillic soft sign ⟨ь⟩.

``ket.json`` used to map the bare soft sign to an empty candidate, deleting it
outright: ``дэсь`` (gold ``dɛɕ``) came out ``dɛs``. The soft sign is a
palatalisation mark, not a silent letter -- the ru and uk specs already map it
to /ʲ/ and compose it onto the preceding consonant.

The northeuralex gold additionally shows that four of the resulting
palatalised consonants are not plain C+ʲ concatenations but distinct single
IPA segments: с+ь -> ɕ, т+ь -> c, д+ь -> ɟ, н+ь -> ɲ (matching the pattern
already used for л+ь -> ʎ). Those four earn Cyrillic+ь multigraph keys; the
bare soft sign otherwise composes /ʲ/ generically (e.g. р+ь -> rʲ, no key of
its own, per the ru ⟨бь⟩ precedent in AGENTS.md).
"""
from orthography2ipa.json_loader import load_json_spec

import orthography2ipa


def test_ket_spec_maps_bare_soft_sign_to_palatalisation():
    spec = load_json_spec("ket")
    assert list(spec.graphemes["ь"]) == ["ʲ"]


def test_ket_spec_maps_the_four_fused_palatalised_consonants():
    spec = load_json_spec("ket")
    assert list(spec.graphemes["сь"]) == ["ɕ"]
    assert list(spec.graphemes["ть"]) == ["c"]
    assert list(spec.graphemes["дь"]) == ["ɟ"]
    assert list(spec.graphemes["нь"]) == ["ɲ"]
    assert list(spec.graphemes["ль"]) == ["ʎ"]


def test_ket_soft_sign_palatalises_the_preceding_consonant():
    # дэсь: gold dɛɕ (northeuralex). Was dɛs when ь deleted silently.
    assert orthography2ipa.transcribe("дэсь", "ket") == "dɛɕ"
    # синь: gold ɕiɲ (northeuralex, palatal nasal).
    assert orthography2ipa.transcribe("синь", "ket") == "siɲ"


def test_ket_soft_sign_composes_generic_palatalisation_off_its_own_key():
    # семья: gold ɕɛmʲa (northeuralex) has mʲ -- м has no dedicated
    # Cyrillic+ь key, the bare soft sign composes /ʲ/ onto it directly.
    assert "mʲ" in orthography2ipa.transcribe("семья", "ket")
