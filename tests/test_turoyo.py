"""Turoyo (tru) — Surayt-Aramaic in the Syriac abjad.

The spec receives unpointed letter strings: the vowel points are not part of
the input. What the bare letters still carry are the three matres lectionis
⟨ܐ ܘ ܝ⟩ and their word-edge behaviour. Every claim tested here is stated with
its source in the spec's ``notes``.
"""

from orthography2ipa import G2P, get


def _spec():
    return get("tru")


def _g(letter):
    """The ordered IPA candidate list declared for *letter*."""
    value = _spec().graphemes[letter]
    return getattr(value, "ipa", value)


class TestMatresLectionis:
    """⟨ܘ⟩ writes /u/ and ⟨ܝ⟩ writes /i/ off the word edge.

    The Surayt Orthography (Aramaic-Online Project 2017, §2a) writes every
    /u/ with waw and every /i/ with yodh, and lists ⟨ܐ ܘ ܝ⟩ as the matres
    lectionis.
    """

    def test_waw_leads_with_the_vowel(self):
        assert _g("ܘ")[0] == "u"
        assert "w" in _g("ܘ")

    def test_yodh_leads_with_the_vowel(self):
        assert _g("ܝ")[0] == "i"
        assert "j" in _g("ܝ")

    def test_non_initial_waw_is_a_vowel(self):
        # ⟨ܚܒܘܫܐ⟩ 'apple', gold ħabuʃo: the waw is the /u/, not a /w/.
        out = G2P("tru").transcribe_word("ܚܒܘܫܐ")
        assert "u" in out
        assert "w" not in out

    def test_non_initial_yodh_is_a_vowel(self):
        # ⟨ܡܣܟܝܢܐ⟩ 'poor', gold məskino: the yodh is the /i/, not a /j/.
        out = G2P("tru").transcribe_word("ܡܣܟܝܢܐ")
        assert "i" in out
        assert "j" not in out


class TestWordInitialMatresStayConsonantal:
    """Word-initial /u/ and /i/ are spelled ⟨ܐܘ⟩ and ⟨ܐܝ⟩, with a leading
    olaf, so a bare word-initial ⟨ܘ⟩ or ⟨ܝ⟩ is the consonant."""

    def test_word_initial_yodh_is_the_glide(self):
        # ⟨ܝܪܚܐ⟩ 'month', gold jarħe.
        assert G2P("tru").transcribe_word("ܝܪܚܐ").startswith("j")

    def test_word_initial_waw_is_the_consonant(self):
        assert _spec().positional_graphemes["ܘ"]["word_initial"] == ["w"]


class TestEmphaticStateEndingSurvives:
    """The word-final alaph stays the nominal ending, not a glottal stop."""

    def test_word_final_alaph_is_the_state_vowel(self):
        # ⟨ܟܠܒܐ⟩ 'dog', gold kalbo/kalbe.
        out = G2P("tru").transcribe_word("ܟܠܒܐ")
        assert not out.endswith("ʔ")
        assert out.endswith("o")
