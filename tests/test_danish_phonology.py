"""Danish (da) phonology pins.

Each class covers one cited generalisation in ``da.json``. Every assertion is
a full transcription, so a rule that fires in the wrong place shows up here
rather than being averaged away by the benchmark.

Run with:
    pytest tests/test_danish_phonology.py -v --tb=short
"""
from __future__ import annotations

import pytest

import orthography2ipa


@pytest.fixture(scope="module")
def da():
    try:
        return orthography2ipa.G2P("da")
    except Exception as exc:  # pragma: no cover - spec always ships
        pytest.skip(f"da not available: {exc}")


def _t(engine, word):
    return engine.transcribe_word(word)


class TestSilentH:
    """/h/ is syllable-initial only (Basbøll 2005), so ⟨hv hj⟩ open with the
    approximant and a coda ⟨h⟩ is silent."""

    @pytest.mark.parametrize("word,ipa", [
        ("hvor", "ˈvoːʁ"),
        ("hvad", "ˈvaːð"),
        ("hvem", "ˈveːm"),
        ("hjem", "ˈjeːm"),
        ("hjælp", "ˈjɛlp"),
    ])
    def test_hv_hj(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [("øh", "ˈøː"), ("åh", "ˈɔː")])
    def test_coda_h_is_silent(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [
        ("hus", "ˈhuːs"),
        ("hytte", "ˈhytə"),
        ("har", "ˈhɑːʁ"),
    ])
    def test_onset_h_survives(self, da, word, ipa):
        """Guard: the deletion must not reach a syllable-initial /h/."""
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [
        ("uhyre", "ˈuhyʁə"),
        ("uhyggelig", "ˈuhyɡəliː"),
    ])
    def test_onset_h_before_y_survives(self, da, word, ipa):
        """Guard: a non-initial ⟨h⟩ before ⟨y⟩ is syllable-initial, not a
        coda, so it must not be deleted (the syllabifier misclassifies it
        as coda — engine defect, task #79 — narrowed out spec-side)."""
        assert _t(da, word) == ipa


class TestARetraction:
    """/a/ is retracted to [ɑ] next to /r/; [a] and [ɑ] are in
    near-complementary distribution (Grønnum 2005; Basbøll 2005)."""

    @pytest.mark.parametrize("word,ipa", [
        ("har", "ˈhɑːʁ"),
        ("par", "ˈpɑːʁ"),
        ("rar", "ˈʁɑːʁ"),
        ("fra", "ˈfʁɑː"),
    ])
    def test_retraction(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [
        ("nat", "ˈnaːt"),
        ("tak", "ˈtaːk"),
        ("kaffe", "ˈkafə"),
        ("mand", "ˈman"),
    ])
    def test_front_a_elsewhere(self, da, word, ipa):
        """Guard: /a/ away from /r/ stays front."""
        assert _t(da, word) == ipa


class TestGElision:
    """Single intervocalic ⟨g⟩ after a long vowel is elided; after a short
    vowel it is retained."""

    @pytest.mark.parametrize("word,ipa", [("tage", "ˈtaːə"), ("sige", "ˈsiːə")])
    def test_elided_after_long_vowel(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [
        ("bygge", "ˈbyɡə"),
        ("hyggelig", "ˈhyɡəliː"),
    ])
    def test_retained_after_short_vowel(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [
        ("ligge", "ˈliːə"),
        ("kigge", "ˈkiːə"),
        ("tigge", "ˈtiːə"),
    ])
    def test_igg_class_known_gap(self, da, word, ipa):
        """Known gap: word-final ⟨ig(g)⟩ before a vowel still over-lengthens
        and elides ⟨g⟩ (gold: lʔeɡə, kikə/kʔiɡə, tekər), because the ⟨ig⟩
        digraph maps to long [iː] and DA_G_ELIDE then fires on it. A
        word-final ⟨ig⟩ constraint would fix this without an ad-hoc ⟨igg⟩
        grapheme entry; tracked as o2i task #80 (45/65 non-final ⟨ig⟩ words
        over-lengthen)."""
        assert _t(da, word) == ipa


class TestSoftD:
    """⟨d⟩ and ⟨dd⟩ after a vowel are both the approximant [ð]."""

    @pytest.mark.parametrize("word,ipa", [
        ("sidde", "ˈsiðə"),
        ("gade", "ˈɡaːðə"),
        ("mad", "ˈmaːð"),
    ])
    def test_soft_d(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [("mand", "ˈman"), ("guld", "ˈɡul")])
    def test_silent_d_after_sonorant(self, da, word, ipa):
        """Guard: the ⟨nd ld⟩ deletion still wins over the lenition."""
        assert _t(da, word) == ipa


class TestCBeforeFrontVowel:
    """⟨c⟩ is [s] before a front vowel and [k] elsewhere."""

    @pytest.mark.parametrize("word,ipa", [
        ("recept", "ˈʁeːsəpt"),
        ("citron", "ˈsitʁɔn"),
        ("cykel", "ˈsyːkəl"),
    ])
    def test_c_is_s_before_front_vowel(self, da, word, ipa):
        assert _t(da, word) == ipa


class TestUntouchedClasses:
    """Guards for the parts of the spec this wave did not change."""

    @pytest.mark.parametrize("word,ipa", [
        ("skal", "ˈsɡaːl"),
        ("stor", "ˈsdoːʁ"),
    ])
    def test_no_aspiration_after_s(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [("ikke", "ˈikə"), ("vand", "ˈvan")])
    def test_degemination_and_schwa(self, da, word, ipa):
        assert _t(da, word) == ipa


class TestLexicalLowering:
    """Seed-list pins for the four DA_LEXICAL_LOWER_* entries: a stressed
    short high/mid vowel lowers while keeping the spelling of its historical
    higher vowel. Each entry pins a frequent member of a much larger,
    partly-conditioned class (o2i task #80 tracks the rest)."""

    @pytest.mark.parametrize("word,ipa", [
        ("til", "ˈtel"),
        ("nul", "ˈnol"),
        ("kys", "ˈkøs"),
        ("søn", "ˈsœn"),
    ])
    def test_seed_list_lowering(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [("kysse", "ˈkysə")])
    def test_untreated_class_member_does_not_lower(self, da, word, ipa):
        """Guard: kysse is in the same stressed-⟨y⟩ class as kys but is not
        one of the four pinned words, so it keeps the unlowered [y]. This
        documents the seed-list boundary — it is not evidence the class
        member is correctly transcribed."""
        assert _t(da, word) == ipa
