# -*- coding: utf-8 -*-
"""Yiddish (yi) in YIVO orthography.

Every expected value below is read off the YIVO letter table in Wikipedia's
"Yiddish orthography" or off the inventory and worked examples in Wikipedia's
"Yiddish phonology", never off the engine's output and never off a gold set.
Where the two pages give the same segment in different notation, the phonology
page's inventory symbol is the one used, because that is the page that states
the inventory.
"""

import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def yi():
    return G2P("yi")


def _bare(g2p, word):
    """Transcription without the stress mark, which these tests do not judge."""
    return g2p.transcribe_word(word).replace("ˈ", "")


class TestPointedAlefAndVov:
    """The pointing is spelling, not an optional aid: the letter table gives
    pasekh alef, komets alef and vov three different values."""

    def test_komets_alef_is_open_mid_back(self, yi):
        # Letter table: komets alef <אָ> /ɔ/. אָװנט is the phonology page's own
        # example word, transcribed there /ˈɔvn̩t/.
        assert _bare(yi, "אָװנט").startswith("ɔv")

    def test_pasekh_alef_is_open_front(self, yi):
        # Letter table: pasekh alef <אַ> /a/.
        assert _bare(yi, "אַלע").startswith("a")

    def test_vov_is_near_close_back(self, yi):
        # Letter table: vov <ו> /ʊ/, khes/khaf /χ/ per the phonology
        # consonant table's velar/uvular row.
        assert _bare(yi, "בוך") == "bʊχ"

    def test_tsvey_vovn_is_a_consonant(self, yi):
        # Letter table: tsvey vovn <וו> /v/ — a digraph, not two vowels.
        assert _bare(yi, "װאָרט") == _bare(yi, "וואָרט")
        assert _bare(yi, "וואָרט").startswith("v")


class TestDiphthongs:
    """The phonology page lists exactly three diphthongs: ɛɪ, aɪ, ɔɪ. The
    letter table names the digraph that spells each one."""

    def test_vov_yud_is_back_diphthong(self, yi):
        # Letter table: vov yud <וי> /ɔj/.
        assert "ɔɪ" in _bare(yi, "בוים")

    def test_tsvey_yudn_is_front_diphthong(self, yi):
        # Letter table: tsvey yudn <יי> /ɛj/; ligature <ײ> is the same unit.
        assert "ɛɪ" in _bare(yi, "אײזל")
        assert _bare(yi, "אײזל") == _bare(yi, "אייזל")

    def test_pasekh_tsvey_yudn_is_open_diphthong(self, yi):
        # Letter table: pasekh tsvey yudn <ײַ> /aj/, i.e. the phonology
        # page's aɪ — not the /a/ + /j/ its parts would give separately.
        assert "aɪ" in _bare(yi, "שרײַבן")


class TestYudIsVowelOrConsonant:
    """The letter table gives yud both readings, /j, i/. Which one applies is
    positional: shtumer alef exists precisely to mark that a syllable opens
    with the vocalic reading, so a bare word-initial yud is the consonant."""

    def test_bare_yud_is_the_vowel(self, yi):
        # Vocalic yud is the phonology page's /ɪ/, not /i/: /i/ is what the
        # separate khirik yud spells.
        assert _bare(yi, "קינד") == "kɪnd"

    def test_word_initial_yud_is_the_glide(self, yi):
        assert _bare(yi, "יאָר").startswith("j")

    def test_khirik_yud_blocks_the_tsvey_yudn_reading(self, yi):
        # Letter table: khirik yud <יִ> /i/. Its whole job after another yud
        # is to stop the pair being read as tsvey yudn /ɛj/, so <ייִ> is
        # /ji/ — the maximal-munch match on <יי> must not win here.
        assert _bare(yi, "ייִד") == "jid"
        assert _bare(yi, "ייִדיש").startswith("ji")


class TestAyinReduction:
    """The letter table gives ayin /ɛ, ə/. The split is stress-conditioned:
    the Jewish Language Project's Eastern Yiddish page states that stress in
    Germanic words falls on the first syllable of the root and that unstressed
    vowels are typically reduced."""

    def test_stressed_ayin_is_full(self, yi):
        assert _bare(yi, "מענטש") == "mɛntʃ"

    def test_unstressed_ayin_is_reduced(self, yi):
        assert _bare(yi, "אַלע").endswith("lə")


class TestSyllabicSonorants:
    """The phonology page: /l/ and /n/ function as syllable nuclei, with
    [m] and [ŋ] appearing as nuclei too, but only as allophones of /n/ after
    bilabial and dorsal consonants respectively."""

    def test_final_lamed_after_consonant_is_syllabic(self, yi):
        # אײזל is the page's own example, /ˈɛɪzl̩/.
        assert _bare(yi, "אײזל") == "ɛɪzl̩"

    def test_final_nun_after_consonant_is_syllabic(self, yi):
        assert _bare(yi, "העלפֿן").endswith("fn̩")

    def test_syllabic_nucleus_is_bilabial_after_a_bilabial(self, yi):
        assert _bare(yi, "לעבן").endswith("bm̩")

    def test_syllabic_nucleus_is_dorsal_after_a_dorsal(self, yi):
        assert _bare(yi, "יאָגן").endswith("ɡŋ̩")

    def test_final_nun_after_a_vowel_letter_is_a_plain_coda(self, yi):
        # The nucleus is already spelled — the ayin carries it — so the nun
        # is an ordinary coda.
        assert _bare(yi, "אָנקומען").endswith("mən")


class TestNasalAssimilation:
    """Place assimilation before a dorsal stop, with the stop retained."""

    def test_nun_before_a_dorsal_stop_is_dorsal(self, yi):
        assert _bare(yi, "אָנקומען").startswith("ɔŋk")
        assert "ŋɡ" in _bare(yi, "זינגען")
