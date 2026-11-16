# -*- coding: utf-8 -*-
"""Low German (nds) — the SASS orthography of Northern Low Saxon.

Every expectation below is read off a spelling rule in the SASS
Schrievregeln or a phonetic value in the SASS Grammatik / Prehn (2012),
never off the engine's own output. The words are the rules' own worked
examples wherever the rule supplies one.
"""

import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def nds():
    return G2P("nds")


def _bare(g2p, word):
    """Transcription without the stress mark, which these tests do not judge."""
    return g2p.transcribe_word(word).replace("ˈ", "")


class TestVowelLength:
    """SASS §§3–5, §9, §12 — the three ways length is written, and the
    open syllable where it is not written at all."""

    def test_doubled_vowel_is_long(self, nds):
        # SASS §5 I lists <aa ää ee oo öö uu üü yy> as the closed-syllable
        # length spelling; Aal, gröön, Schüün are its own examples.
        assert _bare(nds, "Aal").startswith("ɔː")     # [ɔːl]
        assert "yː" in _bare(nds, "Schüün")       # üü → [yː]
        assert "øː" in _bare(nds, "gröön")   # öö → [øː]
        assert "uː" in _bare(nds, "Bruun")                  # uu → [uː]

    def test_dehnungs_h_lengthens_and_is_not_a_consonant(self, nds):
        # SASS §3: the h stands only where the High German cognate has one
        # (gahn, Ohr, mehr) and marks length; it is not spoken.
        assert "h" not in _bare(nds, "gahn")
        assert "h" not in _bare(nds, "Ohr")
        assert _bare(nds, "Ohr").startswith("oː")

    def test_ie_is_long_i(self, nds):
        # SASS §12: Ies, hier, frie.
        assert "iː" in _bare(nds, "Ies")
        assert "iː" in _bare(nds, "hier")

    def test_open_syllable_length_is_unwritten(self, nds):
        # SASS §4 I: "Grundsätzlich wird die Vokallänge ... nicht
        # bezeichnet" — sche-ten, gro-ne, Se-len, and the monosyllables
        # bi, du, he, se, na, to, so, wo.
        assert "eː" in _bare(nds, "eten")
        assert "iː" in _bare(nds, "bi")
        assert "uː" in _bare(nds, "du")

    def test_long_a_is_dark(self, nds):
        # SASS §9 / SASS-Grammatik 1.1.4.1 "Langes a": the long a runs
        # from [ɔː] to [oː]; kamen, Straat, Hahn are its own examples.
        assert _bare(nds, "laten").startswith("lɔː")
        assert _bare(nds, "gahn").startswith("ɡɔː")


class TestShortnessAndGeminates:
    """SASS §6 — a doubled consonant marks the VOWEL as short. It is a
    spelling device, not a long consonant, so nothing doubles in the IPA."""

    def test_doubled_consonant_is_one_segment(self, nds):
        for word, seq in [("Katt", "tt"), ("Kopp", "pp"),
                          ("seggen", "ɡɡ"), ("swemmen", "mm")]:
            assert seq not in _bare(nds, word), word

    def test_doubled_consonant_blocks_lengthening(self, nds):
        # Katt and Kopp keep the short vowel the doubling marks.
        assert "aː" not in _bare(nds, "Katt")
        assert "ɔː" not in _bare(nds, "Kopp")


class TestUnstressedSyllables:
    """SASS §§23/27 and SASS-Grammatik 1.1.4.5 — the unstressed e reduces;
    stress is word-initial (Lindow et al. 1998:30 via Prehn 2012 §4.1)."""

    def test_unstressed_e_is_schwa(self, nds):
        # SASS-Grammatik 1.1.4.5: "In der Silbe -en fällt im
        # Niederdeutschen das e stets aus, es wird ein silbisches [ṇ]
        # gesprochen" — the syllabic nasal is the prescribed reading, but
        # the crowd-scraped gold overwhelmingly writes [ən] (95 of 96
        # word-final occurrences), so [ən] stays rank 1 and the syllabic
        # form is carried as a lattice alternative.
        assert _bare(nds, "eten").endswith("ən")
        assert _bare(nds, "Aven").endswith("ən")
        assert any(c.endswith("n̩") for c in nds.word_candidates("eten"))

    def test_stress_is_word_initial(self, nds):
        assert nds.transcribe_word("Water").startswith("ˈ")
        assert nds.transcribe_word("gemeen").startswith("ˈ")


class TestConsonants:
    """SASS §§16, 18, 20, 21 and Prehn (2012) on r and on final lenis."""

    def test_onset_r_is_apical_not_uvular(self, nds):
        # Uvular [ʁ] is a German-contact variant, not the first reading.
        assert "ʁ" not in _bare(nds, "Regen")
        assert _bare(nds, "Regen").startswith("r")

    def test_final_lenis_obstruent_is_voiceless(self, nds):
        # Prehn 2012 ch. 6: the lenis series is laryngeally unspecified and
        # surfaces voiceless word-finally.
        assert _bare(nds, "Deev").endswith("f")
        assert _bare(nds, "Avend").endswith("t")
        assert _bare(nds, "old").endswith("t")

    def test_v_is_voiced_between_vowels(self, nds):
        # SASS §18: the intervocalic v/b sound spelt <v> is [v] (Gloven).
        assert "v" in _bare(nds, "Gloven")
        assert "v" in _bare(nds, "Aven")

    def test_g_positions(self, nds):
        # SASS §16 II/III: final <g> is [ç/x] (Dag), intervocalic is [ɡ]
        # (negen, stiegen).
        assert _bare(nds, "Dag").endswith(("x", "ç"))
        assert "ɡ" in _bare(nds, "negen")

    def test_s_cluster_onsets_keep_both_readings(self, nds):
        # SASS §20: <st> <sp> are written with s whether [s] or [ʃ] is
        # spoken, so both must be reachable in the lattice.
        cands = nds.word_candidates("Straat", k=8)
        assert any(c.startswith(("ˈs", "s")) for c in cands)
        assert any("ʃ" in c for c in cands)


class TestNoHighGermanShift:
    """Low German did not undergo the High German consonant shift, so the
    <pf> of the shift has no place in the spec (SASS §1 admits only High
    German LETTERS, which is not the same claim)."""

    def test_no_pf_grapheme(self):
        from orthography2ipa import get
        assert "pf" not in get("nds").graphemes


class TestNoSilentGraphemeDeletion:
    """Every letter the gold's Low German writing traditions use must map to
    something. A letter with no entry is dropped in silence, which turns a
    word into a different word."""

    @pytest.mark.parametrize("letter", list(
        "abcdefghijklmnopqrstuvwxyzäöüß"
        "àâåæëęœ"))
    def test_letter_is_mapped(self, letter):
        from orthography2ipa import get
        assert letter in get("nds").graphemes, letter
