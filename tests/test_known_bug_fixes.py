"""Regressions for bugs where a language silently mangled its own words."""

from orthography2ipa import G2P


class TestMalayIsNotFiveVowels:
    """ms shipped only ⟨a e i o u⟩, so every consonant was dropped: makan → aa.
    It now inherits Indonesian's grapheme table (the 1972 unified orthography)."""

    def test_consonants_survive(self):
        assert G2P("ms").transcribe_word("makan") == "ˈmakan"

    def test_the_malay_digraphs(self):
        g = G2P("ms")
        assert g.transcribe_word("nyanyi") == "ˈɲaɲi"   # ⟨ny⟩ = /ɲ/
        assert g.transcribe_word("bunga") == "ˈbuŋa"     # ⟨ng⟩ = /ŋ/
        assert g.transcribe_word("khabar") == "ˈxabar"   # ⟨kh⟩ = /x/


class TestGreekAccentsDoNotEatTheVowel:
    """A precomposed accented vowel ⟨ό⟩ was an unknown character, so the vowel
    under it vanished: λόγος → lɡos. The pitch/length marks are now folded."""

    def test_accented_vowel_is_read(self):
        assert "o" in G2P("grc").transcribe_word("λόγος")   # was lɡos

    def test_the_word_keeps_all_its_vowels(self):
        # λόγος has two vowels; both must survive the accent-folding.
        ipa = G2P("grc").transcribe_word("λόγος")
        assert ipa.count("o") == 2


class TestLatinDoesNotRhotacise:
    """Classical Latin /s/ is voiceless everywhere; rhotacism was prehistoric and
    already complete (honōs → honor is spelled with ⟨r⟩). Intervocalic ⟨s⟩ is /s/,
    not /r/ — the spec had it backwards (rosa → rora), against its own cited note
    '(9) /s/ always voiceless' (Allen 1965)."""

    def test_intervocalic_s_stays_s(self):
        assert G2P("la").transcribe_word("rosa") == "rosa"
        assert G2P("la").transcribe_word("casa") == "kasa"

    def test_archaic_latin_is_unchanged(self):
        # la-x-archaic keeps its own (pre-rhotacism) reading.
        assert G2P("la-x-archaic").transcribe_word("rosa") == "rosa"


class TestEnglishDoublingIsNotGemination:
    """⟨tt nn pp mm⟩ spell a single consonant; the engine read two (summer →
    sʌmmə). collapse_geminates fixes it, without touching a real long vowel."""

    def test_doubled_consonants_collapse(self):
        g = G2P("en-GB")
        assert g.transcribe_word("summer") == "sʌməɹ"
        assert g.transcribe_word("running") == "ɹʌnɪŋ"
        assert g.transcribe_word("happy") == "hæpi"

    def test_a_real_long_vowel_is_kept(self):
        # ⟨ee⟩/⟨oo⟩ are long vowels, not doubled letters — must not collapse.
        assert G2P("en-GB").transcribe_word("see") == "siː"
        assert G2P("en-GB").transcribe_word("food") == "fuːd"


class TestEnglishFinalYIsAVowel:
    """Word-final ⟨y⟩ is /i/ (happy, city), not the consonant /j/ (happy → hæppj)."""

    def test_final_y(self):
        assert G2P("en-GB").transcribe_word("city") == "sɪti"

    def test_initial_y_is_still_the_glide(self):
        assert G2P("en-GB").transcribe_word("yes") == "jɛs"


class TestWordFinalSeesThroughSilentLetters:
    """A word-final rule must fire on the last PRONOUNCED consonant, even when a
    silent letter follows it. is_word_final was computed on the grapheme chain,
    so a mute final ⟨e⟩ hid final devoicing — Walloon ⟨rodje⟩ stayed [ʀɔdʒ]."""

    def test_devoicing_fires_behind_a_mute_e(self):
        from orthography2ipa import G2P
        assert G2P("wa").transcribe_word("rodje") == "ʀɔtʃ"
        assert G2P("wa").transcribe_word("rodje") == G2P("wa").transcribe_word("rotche")

    def test_a_language_without_final_devoicing_is_unaffected(self):
        # French has no final devoicing; ⟨grande⟩ keeps its [d] behind the mute ⟨e⟩.
        from orthography2ipa import G2P
        assert G2P("fr-FR").transcribe_word("grande") == "ɡʁɑ̃d"


class TestSpanishFinalYIsAVowel:
    """Word-final ⟨y⟩ is the vowel /i/ (soy, rey, y 'and'), not the consonant /ʝ/
    — which stays only before a vowel (yo, playa). soy was /soʝ/."""

    def test_final_y(self):
        from orthography2ipa import G2P
        assert G2P("es").transcribe_word("soy") == "ˈsoi"
        # ⟨y⟩ 'and' is the vowel /i/, not the consonant /ʝ/. As the atonic
        # conjunction it is a declared prosodic clitic (stress.cliticless_words),
        # so it surfaces unstressed — the vowel quality [i] is what this asserts.
        assert G2P("es").transcribe_word("y") == "i"

    def test_prevocalic_y_is_the_consonant(self):
        from orthography2ipa import G2P
        assert G2P("es").transcribe_word("yo") == "ˈʝo"
        assert G2P("es").transcribe_word("playa") == "plaˈʝa"


class TestPolishRzDoesNotVoiceThePrecedingStop:
    """⟨rz⟩ /ʐ/ progressively DEVOICES after a voiceless obstruent (przy [pʂɨ]); it
    does not trigger regressive voicing of the stop, as the rule's own note says
    ('v and ʐ do not trigger'). przy was /bʂɨ/, także /taɡʂɛ/."""

    def test_rz_after_voiceless_stop(self):
        from orthography2ipa import G2P
        g = G2P("pl")
        assert g.transcribe_word("przy") == "ˈpʂɨ"
        assert g.transcribe_word("trzy") == "ˈtʂɨ"
        assert g.transcribe_word("także") == "ˈtakʂɛ"

    def test_a_real_voiced_obstruent_still_triggers(self):
        # prośba: ⟨ś⟩ voices to [ʑ] before /b/ — regressive voicing is intact.
        from orthography2ipa import G2P
        assert G2P("pl").transcribe_word("prośba") == "ˈprɔʑba"

    def test_final_affricate_devoices(self):
        from orthography2ipa import G2P
        assert G2P("pl").transcribe_word("łódź") == "ˈwutɕ"
