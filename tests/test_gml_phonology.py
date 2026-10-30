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


class TestScClusterNotYetAShibilant:
    """Lasch (1914) §334 (pp. 173-175): ⟨sch⟩ is a spelling variant of
    ⟨sc⟩/⟨sk⟩ that begins before the Middle Low German period and never
    displaces it inside that period -- "noch zu ende der periode sc (sk)
    nicht verdrängt" -- with the single [ʃ] a later, regionally limited
    development. All 11 ⟨sch⟩/⟨sc⟩ words in the cached gold read [sk]."""

    def test_sch_is_the_cluster(self, gml):
        out = _bare(gml, "schriven")            # gold: skriːvən
        assert out.startswith("sk")
        assert "ʃ" not in out

    def test_sc_is_the_same_cluster(self, gml):
        # (the unstressed prefix be- is a separate, unfixed limitation)
        assert "sk" in _bare(gml, "bescriven")

    def test_sch_word_finally(self, gml):
        assert _bare(gml, "versch").endswith("sk")   # gold: fersk


class TestWIsNotV:
    """Lasch keeps ⟨w⟩ (§299, pp. 155-156) and the labiodental ⟨v⟩/⟨u⟩
    (§290, p. 151) as separate sounds in separate sections; the spec had
    merged both onto [v]. The gold has [w] in all 27 ⟨w⟩ words, word
    initially, medially and finally."""

    def test_w_initial(self, gml):
        assert _bare(gml, "water").startswith("w")

    def test_w_medial(self, gml):
        assert "w" in _bare(gml, "ewich")

    def test_w_final(self, gml):
        assert _bare(gml, "juwe").startswith("juːw") or "w" in _bare(gml, "juwe")


class TestVIsVoicelessInitially:
    """Lasch (1914) §290 (p. 151): 'v, älter u, steht anlautend für den
    stimmlosen Spiranten ... v, u steht inlautend für den stimmhaften
    laut'. The gold agrees without exception."""

    def test_v_is_f_word_initially(self, gml):
        assert _bare(gml, "valsch").startswith("f")   # gold: falsk
        assert _bare(gml, "vrisch").startswith("fr")  # gold: frɪsk

    def test_v_stays_voiced_medially(self, gml):
        assert "v" in _bare(gml, "geven")             # gold: ɣɪɛvən


class TestGIsASpirant:
    """Lasch (1914) §342 (p. 180): 'auch das mnd. anlautende g ist als
    Spirant aufzufassen'; §340 (p. 179): word-final ⟨g⟩ is usually
    written ⟨ch⟩ (dag/dach, slöch), i.e. a voiceless spirant. The gold
    has [ɣ] 18 times, [x] 10 and the palatal [ʝ] twice, and no plain
    [ɡ] anywhere."""

    def test_g_is_a_spirant_word_initially(self, gml):
        out = _bare(gml, "gewolt")                    # gold: ɣəwɔlt
        assert out.startswith("ɣ")
        assert not out.startswith("ɡ")

    def test_g_devoices_word_finally(self, gml):
        assert _bare(gml, "dag").endswith("x")
