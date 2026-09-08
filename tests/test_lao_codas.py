"""Lao closes a syllable with a stop, a nasal or a glide, and nothing else.

The tokenizer may read a preposed vowel before a silent-head digraph as
putting the head in the onset and the tail in the coda. Thai wants that
reading; Lao cannot have it when the tail is a liquid, because no Lao
syllable ends in one.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest  # noqa: E402

from orthography2ipa import G2P  # noqa: E402
from orthography2ipa import registry  # noqa: E402

LAO_CODAS = ("p̚", "t̚", "k̚", "ʔ", "m", "n", "ŋ", "w", "j")


class TestTheSpecCarriesTheInventory:
    def test_lao_declares_its_codas(self):
        assert registry.get("lo").codas == LAO_CODAS

    def test_no_liquid_is_a_lao_coda(self):
        assert "l" not in registry.get("lo").codas
        assert "r" not in registry.get("lo").codas

    def test_a_spec_without_the_field_is_unconstrained(self):
        # Absent means "not stated", never "nothing may close a syllable".
        assert registry.get("th").codas == ()


class TestHoNamAfterAPreposedVowel:
    """Both spellings of one word, and both were wrong before."""

    @pytest.mark.parametrize("word", ["ອາໂຫລ", "ອາໂຫຼ"])
    def test_the_liquid_stays_the_onset(self, word):
        # Gold: ʔaː˩(˧).loː˩(˧). The reading that put the liquid in a coda
        # also invented an /h/ that no gold variant carries.
        got = G2P("lo").transcribe_word(word)
        assert got == "ʔaːloː", got

    @pytest.mark.parametrize("word", ["ອາໂຫລ", "ອາໂຫຼ"])
    def test_it_does_not_end_in_a_liquid(self, word):
        assert not G2P("lo").transcribe_word(word).endswith(("l", "r"))


class TestTheThaiReadingIsUntouched:
    """Thai declares no inventory, so the reading it relies on must stand."""

    def test_thai_still_puts_the_marker_in_the_onset(self):
        # ⟨โหม⟩ is /hoːm/ in the shipped gold; the same shape in Lao is not.
        assert G2P("th").transcribe_word("โหม").startswith("h")

    def test_a_lao_word_with_a_legal_coda_is_unchanged(self):
        assert G2P("lo").transcribe_word("ຫລຽວເຫັນ") == "liːəʋhan"
