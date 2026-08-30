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
    A gml-style schwa rule on a vowel grapheme would be a regression here,
    so no vowel grapheme may carry a reduced candidate and the spec ships
    no `stress` block. The consonant lenition positions the spec does
    declare (⟨g⟩, ⟨h⟩, sourced to Gallée §186) are a different phenomenon
    and are not covered by Holthausen's statement about unstressed vowels."""

    def test_final_a_keeps_a_full_vowel(self, osx):
        out = _bare(osx, "geva")
        assert not out.endswith("ə")

    def test_no_vowel_grapheme_declares_a_reduced_candidate(self):
        spec = get("osx")
        for letter, positions in (spec.positional_graphemes or {}).items():
            if letter in "aeiouāēīōū":
                for candidates in positions.values():
                    assert "ə" not in candidates, (letter, candidates)

    def test_spec_ships_no_stress_block(self):
        assert get("osx").stress is None


class TestDentalFricativeDigraph:
    """Gallée (1910) §175 (p. 134): the voiceless and the voiced dental
    spirant are written ⟨th⟩, ⟨ð⟩, ⟨dh⟩ and ⟨d⟩, and word-initial ⟨th⟩ is
    regular in all the older monuments; §184.5 (p. 146) gives ⟨th⟩ the
    value of English ⟨th⟩. The manuscript spelling this gold uses is
    ⟨th⟩ throughout -- ⟨þ⟩ does not occur in a single one of its 244
    headwords -- and without a ⟨th⟩ entry the engine read it as [t]+[h]
    in the 46 rows that contain it."""

    def test_th_is_one_dental_fricative_not_t_plus_h(self, osx):
        out = _bare(osx, "ertha")           # gold: ɛrθɑ
        assert "θ" in out
        assert "th" not in out

    def test_th_word_initially(self, osx):
        assert _bare(osx, "thiu").startswith("θ")


class TestVelarSpirants:
    """Gallée (1910) §186.3 (p. 148): ⟨g⟩ is usually a voiced velar
    spirant, and word-finally the voicing is lost so it becomes the
    voiceless spirant. §186.4: ⟨h⟩ writes the breath sound before a
    vowel, but medially before a consonant and word-finally it is the
    voiceless velar spirant."""

    def test_g_is_a_spirant_between_vowels(self, osx):
        assert "ɣ" in _bare(osx, "egitha")   # gold: eɣiθɑ

    def test_g_devoices_word_finally(self, osx):
        assert _bare(osx, "almahtig").endswith("x")

    def test_h_is_the_breath_sound_before_a_vowel(self, osx):
        assert "h" in _bare(osx, "friohon")  # gold: friːɔhɔn

    def test_h_is_a_spirant_before_a_consonant(self, osx):
        assert "x" in _bare(osx, "ahto")     # gold: ɑxto

    def test_h_is_a_spirant_word_finally(self, osx):
        assert _bare(osx, "burh").endswith("x")   # gold: burx


class TestBarredB:
    """Gallée (1910) §183.6 (p. 146): ⟨b⟩, ⟨v⟩, ⟨u⟩ and ⟨ƀ⟩ all write the
    labiodental spirant, 'wie franz. v, ndl. v'. ⟨ƀ⟩ had no entry, so it
    was silently deleted."""

    def test_barred_b_is_the_labiodental_spirant(self, osx):
        out = _bare(osx, "ƀ")
        assert out and out[0] in "vf"


class TestNoSilentGraphemeDeletion:
    """Every letter attested in the wikipron gold must map to something,
    the Latin-loan ⟨c⟩ and the barred ⟨ƀ⟩ included."""

    @pytest.mark.parametrize(
        "letter", list("abcdefghijklmnoprstuwƀ")
    )
    def test_letter_is_mapped(self, letter):
        assert letter in get("osx").graphemes, letter
