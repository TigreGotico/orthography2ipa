"""Forcing a pronunciation with ``<phoneme>``."""

import pytest

from orthography2ipa import G2P
from orthography2ipa.markup import Chunk, MarkupError, parse_markup


class TestParsing:
    def test_plain_text_is_one_chunk(self):
        """A caller who never writes a tag pays nothing."""
        assert parse_markup("olá mundo") == [Chunk("olá mundo")]

    def test_empty_input(self):
        assert parse_markup("") == [Chunk("")]

    def test_forced_span_carries_ipa_and_spelling(self):
        chunks = parse_markup('a <phoneme ph="ˈɡuɡɫ">Google</phoneme> b')
        assert chunks == [
            Chunk("a "),
            Chunk("Google", forced_ipa="ˈɡuɡɫ"),
            Chunk(" b"),
        ]

    def test_alphabet_ipa_is_accepted(self):
        chunks = parse_markup('<phoneme alphabet="ipa" ph="ˈɡuɡɫ">Google</phoneme>')
        assert chunks[0].forced_ipa == "ˈɡuɡɫ"

    def test_single_quotes(self):
        chunks = parse_markup("<phoneme ph='ˈɡuɡɫ'>Google</phoneme>")
        assert chunks[0].forced_ipa == "ˈɡuɡɫ"

    def test_several_forced_spans(self):
        chunks = parse_markup(
            '<phoneme ph="a">x</phoneme> and <phoneme ph="b">y</phoneme>')
        assert [c.forced_ipa for c in chunks] == ["a", None, "b"]

    def test_ipa_may_contain_a_stress_mark(self):
        """``ph`` is the pronunciation, mark and all."""
        assert parse_markup('<phoneme ph="ˈmiːtinɡ">meeting</phoneme>')[0].forced_ipa \
            == "ˈmiːtinɡ"


class TestMalformed:
    """Every one of these would otherwise be read aloud as letters."""

    def test_no_ph(self):
        with pytest.raises(MarkupError, match="must carry one"):
            parse_markup("<phoneme>word</phoneme>")

    def test_empty_ph(self):
        with pytest.raises(MarkupError, match="empty"):
            parse_markup('<phoneme ph="">word</phoneme>')

    def test_no_text(self):
        """The spelling is not decoration — cross-word rules read it."""
        with pytest.raises(MarkupError, match="wraps no text"):
            parse_markup('<phoneme ph="abc"></phoneme>')

    def test_foreign_alphabet_is_refused_not_guessed(self):
        with pytest.raises(MarkupError, match="only alphabet"):
            parse_markup('<phoneme alphabet="x-sampa" ph="mi:tIN">meeting</phoneme>')

    def test_unclosed_tag(self):
        with pytest.raises(MarkupError, match="unclosed"):
            parse_markup('hello <phoneme ph="abc">word')


class TestForcedPronunciation:
    def test_forced_word_bypasses_the_rules(self):
        rules = G2P("pt-PT").transcribe("Google")
        forced = G2P("pt-PT").transcribe('<phoneme ph="ˈɡuɡɫ">Google</phoneme>')
        assert forced == "ˈɡuɡɫ"
        assert forced != rules

    def test_surrounding_words_are_transcribed_normally(self):
        assert G2P("pt-PT").transcribe(
            'olá <phoneme ph="ˈɡuɡɫ">Google</phoneme> mundo'
        ) == "oˈla ˈɡuɡɫ ˈmu\u0303du"

    def test_untagged_text_is_unaffected(self):
        assert G2P("pt-PT").transcribe("olá mundo") == "oˈla ˈmu\u0303du"

    def test_forced_ipa_is_not_re_stressed(self):
        """``ph`` places the stress. A caller who wrote no mark meant none."""
        assert G2P("pt-PT").transcribe('<phoneme ph="ɡuɡɫ">Google</phoneme>') == "ɡuɡɫ"

    def test_a_forced_word_is_certain(self):
        result = G2P("pt-PT").transcribe_detailed(
            '<phoneme ph="ˈɡuɡɫ">Google</phoneme>')
        assert result.words[0].confidence == 1.0

    def test_code_switched_loanword(self):
        """A Latin-script word in Arabic text: transcribed, not dropped."""
        assert G2P("ar-SA-x-najd").transcribe(
            'عِنْدِي <phoneme ph="ˈmiːtinɡ">meeting</phoneme> السَّاعَة'
        ) == "ˈʕindiː ˈmiːtinɡ asˈsaːʕa"


class TestInventoryGuard:
    """``ph`` is held to the spec's declared inventory.

    A symbol the spec never declares has no vector in a TTS embedding table —
    it is built from the declared inventory before training — so the word
    carrying it is mispronounced permanently and silently.
    """

    def test_donor_phonology_is_refused(self):
        """English /ɪ/ and /ŋ/ are not Arabic phonemes."""
        with pytest.raises(MarkupError, match="does not declare"):
            G2P("ar-SA-x-najd").transcribe(
                '<phoneme ph="ˈmiːtɪŋ">meeting</phoneme>')

    def test_the_message_names_the_offending_symbol(self):
        with pytest.raises(MarkupError, match=r"\['ɪ'\]"):
            G2P("ar-SA-x-najd").transcribe('<phoneme ph="ɪ">x</phoneme>')

    def test_the_nativised_reading_passes(self):
        """[nɡ] for /ŋ/ — every symbol is already in the inventory."""
        assert G2P("ar-SA-x-najd").transcribe(
            '<phoneme ph="ˈmiːtinɡ">meeting</phoneme>') == "ˈmiːtinɡ"

    def test_msa_has_no_g_so_the_najdi_reading_is_refused(self):
        """/ɡ/ is a Gulf reflex of qāf; MSA declares /q/ and /dʒ/ and no /ɡ/."""
        with pytest.raises(MarkupError, match="does not declare"):
            G2P("ar").transcribe('<phoneme ph="ˈmiːtinɡ">meeting</phoneme>')

    def test_the_caller_can_say_they_mean_it(self):
        assert G2P("ar-SA-x-najd", allow_undeclared_phonemes=True).transcribe(
            '<phoneme ph="ˈmiːtɪŋ">meeting</phoneme>') == "ˈmiːtɪŋ"
