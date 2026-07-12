"""Tests for the canonical-decomposition tokenizer fallback (step d2) and
the segment-aware allophone pass that together make Hangul transcribable.

The engine side is script-agnostic: step d2 is pure Unicode canonical
equivalence (an unmapped character whose NFD pieces are ALL mapped
graphemes becomes one token), and the segment pass matches allophone
rules against phoneme-sized segments inside a multi-phoneme slot. All
Korean specifics live in ko.json (conjoining jamo + lax-voicing rules).
"""
import pytest

from orthography2ipa import G2P
from orthography2ipa.allophony import segment_ipa


class TestCanonicalDecompositionFallback:
    @pytest.fixture(scope="class")
    def ko(self):
        return G2P("ko")

    def test_hangul_syllable_blocks_transcribe(self, ko):
        # Sohn (1999) citation forms; coda neutralization on jongseong.
        assert ko.transcribe_word("안녕") == "annjʌŋ"
        assert ko.transcribe_word("김치") == "kimtɕʰi"
        assert ko.transcribe_word("서울") == "sʌuɭ"

    def test_unmapped_pieces_stay_unknown(self, ko):
        # Han characters have no canonical decomposition into mapped
        # graphemes — a partial or absent match must NOT half-transcribe.
        assert ko.transcribe_word("韓國") == ""

    def test_silent_initial_ieung_contributes_nothing(self, ko):
        # ᄋ (choseong ieung) maps to '' — 아 is just [a].
        assert ko.transcribe_word("아") == "a"


class TestSegmentAwareAllophony:
    @pytest.fixture(scope="class")
    def ko(self):
        return G2P("ko")

    def test_lax_voicing_within_word(self, ko):
        # /k t p tɕ/ voice between voiced sounds (Sohn 1999 §6.3); the
        # context crosses syllable-token boundaries (바+다 → pada).
        assert ko.transcribe_word("바다") == "pada"
        assert ko.transcribe_word("한국") == "hanɡuk̚"
        assert ko.transcribe_word("아버지") == "abʌdʑi"

    def test_word_initial_lax_stop_stays_voiceless(self, ko):
        assert ko.transcribe_word("바다").startswith("p")

    def test_tense_and_aspirated_never_voice(self, ko):
        # 김치: tɕʰ intervocalic but aspirated — must stay tɕʰ, which also
        # pins that segmentation treats tɕʰ as ONE atom (never t + ɕʰ).
        assert "tɕʰ" in ko.transcribe_word("김치")

    def test_neighbourless_rules_keep_whole_slot_semantics(self):
        # Braga diphthongisation [o]→[wo] has no phoneme-neighbour
        # context: it was written against whole slots and must not fire
        # on the 'o' INSIDE the diphthong slot 'ow' (vou is one syllable).
        g = G2P("pt-PT-x-braga")
        assert g.transcribe_word("vou") == "ˈbow"


class TestSegmentIpa:
    def test_modifiers_attach_to_base(self):
        assert segment_ipa("kʰak̚") == ["kʰ", "a", "k̚"]

    def test_atoms_match_longest_first(self):
        assert segment_ipa("tɕʰi", atoms=("tɕʰ", "tɕ")) == ["tɕʰ", "i"]

    def test_atom_must_not_steal_a_modified_base(self):
        # 'k' as an atom must not split 'k͈' (tense k, base+combining).
        assert segment_ipa("k͈a", atoms=("k",)) == ["k͈", "a"]

    def test_single_phoneme_roundtrips(self):
        assert segment_ipa("ʝ") == ["ʝ"]
