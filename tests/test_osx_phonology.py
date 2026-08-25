# -*- coding: utf-8 -*-
"""Old Saxon (osx).

Every expectation below is read off the cached wikipron gold
(.benchmark_cache/osx_latn_broad.tsv) or Gallée (1910) *Altsächsische
Grammatik* (archive.org/details/altschsischegram00gall), never off the
engine's own output.
"""

import pytest

from orthography2ipa import G2P, get


@pytest.fixture(scope="module")
def osx():
    return G2P("osx")


def _bare(g2p, word):
    return g2p.transcribe_word(word).replace("ˈ", "")


class TestVGrapheme:
    """Gallée (1910) pp. 126-128, 161: manuscript orthography interchanges
    b/ƀ/u/v/f for the single labiodental fricative phoneme that ⟨f⟩ also
    spells (e.g. `sivon` beside `sibun` 'seven'). Before this fix ⟨v⟩ had
    no grapheme entry at all, so it was silently dropped from every word
    that contained it -- 21 of the 273 rows (7.7%) in the cached gold."""

    def test_v_is_not_silently_dropped(self, osx):
        assert "v" not in _bare(osx, "avand") or "f" in _bare(osx, "avand")
        assert len(_bare(osx, "avand")) == len("avand")

    def test_v_words_transcribe_with_the_f_phoneme(self, osx):
        # geva 'gives': gold is ɣɛfɑ -- <v> realises as the same fricative
        # <f> does, not as a distinct [v] sound.
        out = _bare(osx, "geva")
        assert "f" in out
        assert "v" not in out


class TestNoUnwarrantedScwhaReduction:
    """Unlike its Middle Low German descendant (gml), Old Saxon itself does
    not reduce unstressed final vowels to schwa: final -a stays [ɑ]/[a] in
    19 of 21 -a-final words in the cached gold (Holthausen 1921 §147).
    A gml-style positional_graphemes.e/a schwa rule would be a regression
    here, so this spec intentionally ships no `positional_graphemes` or
    `stress` block."""

    def test_final_a_keeps_a_full_vowel(self, osx):
        out = _bare(osx, "geva")
        assert not out.endswith("ə")

    def test_spec_ships_no_schwa_reduction_rule(self):
        spec = get("osx")
        assert spec.positional_graphemes in (None, {})


class TestNoSilentGraphemeDeletion:
    """Every plain Latin letter attested in the wikipron gold (besides the
    rare loanword-only ⟨c⟩, attested in a single ambiguous word) must map
    to something."""

    @pytest.mark.parametrize(
        "letter", list("abdefghijklmnoprstuw")
    )
    def test_letter_is_mapped(self, letter):
        assert letter in get("osx").graphemes, letter
