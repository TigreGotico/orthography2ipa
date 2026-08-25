# -*- coding: utf-8 -*-
"""Middle Low German (gml).

Every expectation below is read off Lasch (1914) *Mittelniederdeutsche
Grammatik* (archive.org/details/mittelniederdeut00lasc), never off the
engine's own output, or measured directly against the cached wikipron
gold to document a distribution the spec cannot fully reproduce.
"""

import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def gml():
    return G2P("gml")


def _bare(g2p, word):
    return g2p.transcribe_word(word).replace("ˈ", "")


class TestUnstressedVowelReduction:
    """Lasch (1914) §§211-212 (pp. 116-117): the short vowels of Old Saxon
    unstressed medial/final syllables merged in Middle Low German to a
    single sound normally spelled <e> ('Die im as. noch vorhandene
    Mannigfaltigkeit der kurzen Vokale in den unbetonten Silben hat sich
    mnd. auf einen meist durch e wiedergegebenen Laut reduziert')."""

    def test_unstressed_final_en_is_schwa(self, gml):
        # Polysyllabic -en: root-initial stress (§1) leaves -en unstressed.
        assert _bare(gml, "achten").endswith("ən")
        assert _bare(gml, "binden").endswith("ən")

    def test_unstressed_final_e_is_schwa(self, gml):
        assert _bare(gml, "koke").endswith("ə")
        assert _bare(gml, "asche").endswith("ə")

    def test_unstressed_medial_e_before_r_is_schwa(self, gml):
        # water, ridder: unstressed medial e before a final -er also
        # merges to the reduced sound (§212's "gedeckte Silbe" cases).
        assert "ər" in _bare(gml, "water")
        assert "ər" in _bare(gml, "ridder")

    def test_monosyllable_e_is_not_reduced(self, gml):
        # Monosyllables are always stressed (root-initial stress rule),
        # so a bare -e word keeps its full vowel rather than reducing.
        assert _bare(gml, "he") != "h" + "ə"
        assert _bare(gml, "he").startswith("he")


class TestNoSilentGraphemeDeletion:
    """Every character actually attested in the wikipron gold must map to
    something; a character with no entry silently drops from the word."""

    @pytest.mark.parametrize("letter", list("abcdefghijklmnoprstuvwz"))
    def test_letter_is_mapped(self, letter):
        from orthography2ipa import get
        assert letter in get("gml").graphemes, letter
