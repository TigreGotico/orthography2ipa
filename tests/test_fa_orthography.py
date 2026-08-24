"""Tests for the Persian (fa) reading of the Perso-Arabic abjad.

Perso-Arabic writes only the long vowels, and it writes them with the
three matres lectionis ⟨ا و ی⟩. A grapheme table that gives those three
letters their consonantal value everywhere turns every long vowel in the
language into a spurious consonant — ⟨آرارات⟩ "Ararat" comes out as
*ʔɒːɾʔɾʔt instead of ʔɒːɾɒːɾɒːt. These tests pin the positional reading
of the matres, of word-final ⟨ه⟩, and of the silent wāw in ⟨خوا⟩.

The claims are standard descriptions of the writing system (Mahootian
1997 "Persian", Routledge; Windfuhr & Perry 2009 "Persian and Tajik", in
Windfuhr ed. "The Iranian Languages", Routledge). No page locator is
claimed for either.

The phoneme values themselves (long ā = /ɒː/, rhotic = /ɾ/) follow the
Tehran standard and are pinned separately in tests/test_fa_convention.py.
"""
from orthography2ipa import G2P


def tr(word: str) -> str:
    drop = "ˈˌ.·‿()"
    return "".join(c for c in G2P("fa").transcribe(word) if c not in drop)


class TestAlefIsLongAExceptWordInitially:
    """Non-initial ⟨ا⟩ is the mater lectionis for long ā, not a glottal
    stop. Word-initially it is the carrier of a vowel onset instead."""

    def test_medial_alef_is_long_a(self):
        result = tr("آرارات")  # Ararat
        assert result.count("ɒː") == 3, result
        assert result.count("ʔ") == 1, (
            f"only the word-initial onset may be ʔ, got {result!r}"
        )

    def test_word_initial_alef_keeps_glottal_onset(self):
        assert tr("این").startswith("ʔ")

    def test_initial_alef_plus_ye_is_long_i(self):
        assert tr("ایران") == "ʔiːɾɒːn", tr("ایران")


class TestYeAndWawAreVocalicOffInitially:
    """⟨ی⟩ and ⟨و⟩ are consonantal /j/ and /v/ word-initially and vocalic
    /iː/ and /uː/ elsewhere, where the vocalic reading is the frequent
    one in running text."""

    def test_non_initial_ye_is_long_i(self):
        result = tr("بینی")  # nose
        assert "j" not in result, result
        assert result.count("iː") == 2, result

    def test_word_initial_ye_is_a_glide(self):
        assert tr("یار").startswith("j")

    def test_non_initial_waw_is_long_u(self):
        assert tr("نوروز") == "nuːɾuːz", tr("نوروز")

    def test_word_initial_waw_is_a_consonant(self):
        assert tr("ورزش").startswith("v")


class TestFinalHe:
    """Word-final ⟨ه⟩ after a consonant spells the vowel /e/; after long
    ā it stays the consonant /h/."""

    def test_final_he_after_consonant_is_e(self):
        assert tr("خانه") == "xɒːne", tr("خانه")

    def test_final_he_after_long_a_is_h(self):
        assert tr("ماه") == "mɒːh", tr("ماه")


class TestSilentWawInKhwa:
    """⟨خوا⟩ carries the historical silent wāw (wāw-i maʿdūla): the ⟨و⟩
    is not pronounced and the sequence reads /xɒː/."""

    def test_khab(self):
        assert tr("خواب") == "xɒːb", tr("خواب")

    def test_khahar(self):
        assert tr("خواهر").startswith("xɒːh")
