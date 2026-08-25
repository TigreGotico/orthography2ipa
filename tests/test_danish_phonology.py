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
        ("uhyre", "ˈuhyɐ"),
        ("uhyggelig", "ˈuhyɡəli"),
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
        ("hyggelig", "ˈhyɡəli"),
    ])
    def test_retained_after_short_vowel(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [
        ("ligge", "ˈliɡə"),
        ("kigge", "ˈkiɡə"),
        ("tigge", "ˈtiɡə"),
    ])
    def test_igg_is_not_the_ig_digraph(self, da, word, ipa):
        """⟨ligge, kigge, tigge⟩ are ⟨li-gg-e⟩, not ⟨lig-g-e⟩. The
        longest-match tokenizer reads the first two letters as the ⟨ig⟩
        digraph, which maps to long [iː] and then loses its ⟨g⟩ to
        DA_G_ELIDE. DA_IG_BEFORE_G_NOT_A_DIGRAPH restores the short vowel
        and its consonant."""
        assert _t(da, word) == ipa


class TestFinalIg:
    """The adjectivizing suffix ⟨-ig⟩ is short unstressed [-i], not long
    [-iː] (Puggaard-Rode 2023:64, ex.(19), after Rischel 1970a)."""

    @pytest.mark.parametrize("word,ipa", [
        ("farlig", "ˈfaʁli"),
        ("heldig", "ˈhɛli"),
        ("hyggelig", "ˈhyɡəli"),
    ])
    def test_final_ig_is_short(self, da, word, ipa):
        assert _t(da, word) == ipa


class TestSchwaR:
    """Unstressed schwa next to /r/ is the single vowel [ɐ], in both the
    ⟨-er⟩ and ⟨-re⟩ orders (Puggaard-Rode 2023:40)."""

    @pytest.mark.parametrize("word,ipa", [
        ("hedder", "ˈhɛðɐ"),
        ("sanger", "ˈsaːŋɐ"),
        ("klatre", "ˈklatɐ"),
        ("store", "ˈsdoːɐ"),
    ])
    def test_schwa_r_fuses(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [("rose", "ˈʁoːsə"), ("mor", "ˈmoːʁ")])
    def test_other_r_untouched(self, da, word, ipa):
        """Guard: an /r/ not adjacent to an unstressed schwa is unchanged."""
        assert _t(da, word) == ipa


class TestHighVowelLowering:
    """/i y u/ lower to [e ø o] before a coda [ŋ] or a coda nasal +
    consonant (Puggaard-Rode 2023:46, rule (7), after Grønnum 2005:308)."""

    @pytest.mark.parametrize("word,ipa", [
        ("ting", "ˈteŋ"),
        ("kylling", "ˈkyleŋ"),
        ("synge", "ˈsøŋə"),
        ("tung", "ˈtoŋ"),
        ("vinder", "ˈvenɐ"),
        ("vinter", "ˈventɐ"),
        ("pynt", "ˈpønt"),
        ("bunde", "ˈbonə"),
    ])
    def test_lowering_fires(self, da, word, ipa):
        assert _t(da, word) == ipa

    @pytest.mark.parametrize("word,ipa", [("drikke", "ˈdʁikə"), ("hus", "ˈhuːs")])
    def test_lowering_does_not_overfire(self, da, word, ipa):
        """Guard: no nasal cluster, no lowering."""
        assert _t(da, word) == ipa

    def test_hund_family_is_a_known_miss(self, da):
        """⟨hund⟩ has a silent ⟨d⟩, so there is no coda cluster and the
        vowel should stay [u]. The rule engine reads pre-pass slot state
        and cannot see that DA_SILENT_D is about to remove the /d/, so it
        lowers anyway. Pinned so the miss is visible, not hidden."""
        assert _t(da, "hund") == "ˈhon"


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
