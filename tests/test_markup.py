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
        ) == "oˈla ˈɡuɡɫ ˈmũdu"

    def test_untagged_text_is_unaffected(self):
        assert G2P("pt-PT").transcribe("olá mundo") == "oˈla ˈmũdu"

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
        """English /ʉ/ and /ŋ/ are not Arabic phonemes.

        (/ɪ/ no longer serves as the donor symbol here: it is now a
        genuinely declared Najdi allophone — the AR_EMPHASIS_SPREAD_I_*
        rules back /i/ to [ɪ] next to an emphatic, Watson 2002; Davis 1995
        — so it would no longer demonstrate an undeclared symbol.)
        """
        with pytest.raises(MarkupError, match="does not declare"):
            G2P("ar-SA-x-najd").transcribe(
                '<phoneme ph="ˈmiːtʉŋ">meeting</phoneme>')

    def test_the_message_names_the_offending_symbol(self):
        with pytest.raises(MarkupError, match=r"\['ʉ'\]"):
            G2P("ar-SA-x-najd").transcribe('<phoneme ph="ʉ">x</phoneme>')

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


class TestForcingSurvivesPunctuation:
    """A forced word standing before a pause lost its forcing.

    ``_group_words`` marked the preceding word pausal by REBUILDING it from
    its surface alone — ``_Word(surface=words[-1].surface, pausal=True)`` —
    which dropped ``forced_ipa``. A ``<phoneme>`` span followed by a comma or
    a full stop was therefore silently discarded and the word was re-derived
    by the beam. ``dataclasses.replace`` keeps every other field.
    """

    LECT = "ar-SA-x-najd"
    FORCED = '<phoneme ph="ˈmiːtinɡ">meeting</phoneme>'

    def test_forced_word_before_a_comma_keeps_its_ipa(self):
        assert G2P(self.LECT).transcribe(
            self.FORCED + ", بيت").startswith("ˈmiːtinɡ ")

    def test_forced_word_at_the_end_of_a_sentence_keeps_its_ipa(self):
        assert G2P(self.LECT).transcribe(
            self.FORCED + ".") == "ˈmiːtinɡ"

    def test_forced_word_before_an_arabic_comma_keeps_its_ipa(self):
        """The widened pause set must not reintroduce the bug for a script
        whose comma only started tokenizing as punctuation with it."""
        assert G2P(self.LECT).transcribe(
            self.FORCED + "، بيت").startswith("ˈmiːtinɡ ")

    def test_the_forced_word_is_still_marked_pausal(self):
        words = G2P(self.LECT)._split_words(self.FORCED + ", بيت")
        assert words[0].forced_ipa == "ˈmiːtinɡ"
        assert words[0].pausal is True
