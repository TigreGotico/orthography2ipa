"""Beira and Beira Litoral /l/ follow the pt-PT base.

Neither spec cites a source for a regional lateral, so neither declares its own
/l/ allophones. "ł" is not an IPA symbol, and the retroflex [ɭ] had no source.
"""
import pytest

from orthography2ipa import registry

LATERALS = {"l", "ɫ"}


@pytest.mark.parametrize("code", ["pt-PT-x-beira", "pt-PT-x-aveiro"])
def test_l_allophones_are_the_pt_pt_base(code):
    assert registry.get(code).allophones.get("l") == registry.get("pt-PT").allophones.get("l")


@pytest.mark.parametrize("code", ["pt-PT-x-beira", "pt-PT-x-aveiro"])
def test_no_uncited_lateral_in_the_inventory(code):
    variants = {v for vs in registry.get(code).allophones.values() for v in vs}
    assert "ł" not in variants and "ɭ" not in variants
    assert "ł" not in registry.get(code).allophones
