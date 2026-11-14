"""Assyrian Neo-Aramaic (aii) — unpointed East Syriac spelling.

The spec receives bare letter strings: vowel pointing, the qushshaya/rukkakha
dots and the majliana mark are not part of the input. What survives is the
matres lectionis and the word-edge behaviour of the letters that carry them.
Every claim tested here is stated with its source in the spec's ``notes``.
"""

from orthography2ipa import G2P, get


def _spec():
    return get("aii")


def _g(letter):
    """The ordered IPA candidate list declared for *letter*."""
    value = _spec().graphemes[letter]
    return getattr(value, "ipa", value)


class TestMatresLectionis:
    """Alaph, waw and yudh double as vowel letters."""

    def test_word_final_alaph_is_the_determined_state_vowel(self):
        # ⟨ܒܝܬܐ⟩ 'house': the final alaph writes -a, it is not a glottal stop.
        out = G2P("aii").transcribe_word("ܒܝܬܐ")
        assert not out.endswith("ʔ")
        assert out.endswith("ɑː")

    def test_word_initial_alaph_stays_a_glottal_stop(self):
        assert G2P("aii").transcribe_word("ܐܒܐ").startswith("ʔ")

    def test_medial_alaph_keeps_both_readings_in_the_lattice(self):
        ipa = _g("ܐ")
        assert ipa[0] == "ʔ"
        assert "ɑː" in ipa

    def test_waw_is_a_back_vowel_letter_by_default(self):
        assert _g("ܘ")[0] == "uː"

    def test_waw_is_consonantal_word_initially(self):
        assert G2P("aii").transcribe_word("ܘܪܕܐ").startswith("w")

    def test_yudh_is_a_front_vowel_letter_by_default(self):
        assert _g("ܝ")[0] == "iː"

    def test_yudh_is_consonantal_word_initially(self):
        assert G2P("aii").transcribe_word("ܝܘܡܐ").startswith("j")


class TestBegadkepat:
    """Word-final position leads with the fricative reflex — except pe."""

    def test_word_final_taw_leads_with_the_fricative(self):
        assert G2P("aii").transcribe_word("ܒܝܬ").endswith("θ")

    def test_word_final_kaph_leads_with_the_fricative(self):
        assert G2P("aii").transcribe_word("ܡܠܟ").endswith("x")

    def test_word_final_dalath_leads_with_the_fricative(self):
        assert G2P("aii").transcribe_word("ܝܕ").endswith("ð")

    def test_pe_never_spirantizes(self):
        # *p is merged into /p/ outside Tyari, Barwari and Chaldean.
        assert "ܦ" not in _spec().positional_graphemes
        assert _g("ܦ")[0] == "p"

    def test_medial_position_keeps_the_plosive_first(self):
        # No medial spirantization is declared: the plosive still leads.
        assert G2P("aii").transcribe_word("ܟܬܒܐ").count("θ") == 0


class TestConsonantValues:
    def test_heth_is_velar_not_pharyngeal(self):
        ipa = _g("ܚ")
        assert ipa[0] == "x"
        assert "ħ" in ipa

    def test_ayin_is_retained_as_a_pharyngeal(self):
        assert _g("ܥ")[0] == "ʕ"

    def test_emphatics_are_pharyngealized(self):
        assert _g("ܛ")[0] == "tˤ"
        assert _g("ܨ")[0] == "sˤ"

    def test_majliana_affricates_are_reachable_without_the_mark(self):
        # The mark is absent from unpointed text, so the affricate stays in
        # the lattice as a minority reading of the plain letter.
        assert "t͡ʃ" in _g("ܟ")
        assert "d͡ʒ" in _g("ܓ")
        assert "ʒ" in _g("ܙ")


class TestDoubledWaw:
    """A written ⟨ܘܘ⟩ digraph is not a doubled vowel letter.

    Measured on the shipped gold: of the 18 headwords containing the
    digraph, 16 have it word-medially and no gold reading of any of them
    repeats [uː]. The digraph reading is confined to non-initial position,
    because word-initial waw is consonantal.
    """

    def test_doubled_waw_is_not_a_double_long_vowel(self):
        out = G2P("aii").transcribe_word("ܙܘܘܓܐ")  # gold: zuwwɑːɣɑː
        assert "uːuː" not in out
        assert "w" in out

    def test_doubled_waw_general_grapheme_leads_with_a_short_vowel(self):
        ipa = _g("ܘܘ")
        assert ipa[0] == "uw"

    def test_word_initial_doubled_waw_opens_with_the_consonant(self):
        # Word-initial waw is consonantal /w/, so a word that opens with the
        # digraph opens with /w/ too — gold ⟨ܘܘ⟩ [waw], ⟨ܘܘܐ⟩ [wawwa].
        engine = G2P("aii")
        assert engine.transcribe_word("ܘܘ").startswith("w")
        assert engine.transcribe_word("ܘܘܐ").startswith("w")

    def test_the_digraph_reading_still_applies_off_the_word_edge(self):
        # The same digraph, one letter in from the edge, keeps [uw].
        assert "uw" in G2P("aii").transcribe_word("ܡܩܘܘܡܐ")


class TestSpecIntegrity:
    def test_every_source_is_cited_without_an_unverified_locator(self):
        for src in _spec().sources:
            assert src.pages is None

    def test_quality_tier_is_research(self):
        assert _spec().quality.value == "research"
