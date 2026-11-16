# -*- coding: utf-8 -*-
"""Standard Tibetan: the written syllable resolves to onset + rhyme + tone.

Every case here is a claim about the language, cited in ``bo.json``'s own
rules and sources. The gold is the reading the sources predict, computed
from the spelling by hand, never read back from the engine.
"""
import pytest

import orthography2ipa as o2i


@pytest.fixture(scope="module")
def bo():
    return o2i.G2P("bo")


@pytest.mark.parametrize("word,ipa", [
    # A vowel sign is read. The four signs never matched before, because
    # every key carried the U+25CC placeholder, and every word came out
    # with the inherent /a/.
    ("ཀི", "ki˥˥"),
    ("ཀུ", "ku˥˥"),
    ("ཀེ", "ke˥˥"),
    ("ཀོ", "ko˥˥"),
])
def test_vowel_signs_are_read(bo, word, ipa):
    assert bo.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # A stack is one onset, not its letters in sequence.
    ("ཁྱ", "cʰa˥˥"),      # khya
    ("ཁྲ", "ʈʂʰa˥˥"),     # khra
    ("ལྷ", "l̥a˥˥"),       # lha
    ("སྤྱ", "tɕa˥˥"),      # spya
    ("རྒྱ", "ca˩˨"),       # rgya
    ("གཡ", "ja˥˥"),       # g.ya
    ("དབ", "wa˩˨"),       # dba
])
def test_onset_stacks(bo, word, ipa):
    assert bo.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # The register is the written onset's: voiceless root high, voiced low.
    ("ཀ", "ka˥˥"),
    ("ག", "kʰa˩˨"),
    ("ང", "ŋa˩˨"),
    ("རྔ", "ŋa˥˥"),       # superscribed ⟨ར⟩ raises the sonorant
    ("མ", "ma˩˨"),
    ("སྨ", "ma˥˥"),
])
def test_register_comes_from_the_written_onset(bo, word, ipa):
    assert bo.transcribe_word(word) == ipa


def test_prefix_is_silent_and_deaspirates(bo):
    # ⟨དགོན⟩ dgon: the prefix ⟨ད⟩ is not pronounced and leaves the low
    # ⟨ག⟩ kʰ unaspirated, and ⟨ན⟩ nasalises the nucleus.
    assert bo.transcribe_word("དགོན") == "kø̃˩˨"
    # The high-register aspirates keep their aspiration under a prefix.
    assert bo.transcribe_word("འཁོར") == "kʰoː˥˥"


@pytest.mark.parametrize("word,ipa", [
    ("ཁྱོད", "cʰøː˥˨"),    # khyod: ⟨ད⟩ umlauts and lengthens, no coda
    ("སྤོས", "pøː˥˨"),     # spos: ⟨ས⟩ does the same
    ("ཀུན", "kỹ˥˥"),       # kun: ⟨ན⟩ nasalises, no coda
    ("ཁུལ", "kʰyː˥˥"),     # khul: ⟨ལ⟩ lengthens the umlauted vowel
    ("ནོར", "noː˩˨"),      # nor: ⟨ར⟩ lengthens
    ("ལག", "laʔ˩˧˨"),     # lag: ⟨ག⟩ is the only stop coda left
    ("ཁང", "kʰaŋ˥˥"),     # khang
    ("གསུམ", "sum˥˥"),    # gsum: prefix silent, ⟨མ⟩ is a coda
])
def test_suffix_fixes_the_rhyme(bo, word, ipa):
    assert bo.transcribe_word(word) == ipa


def test_post_suffix_s_is_silent_and_only_changes_the_contour():
    # ⟨ཁམ⟩ kham and ⟨ཁམས⟩ khams are a minimal pair for the contour alone:
    # the post-suffix ⟨ས⟩ is not pronounced.
    bo = o2i.G2P("bo")
    assert bo.transcribe_word("ཁམ") == "kʰam˥˥"
    assert bo.transcribe_word("ཁམས") == "kʰam˥˨"


def test_a_root_after_its_own_prefix_is_not_a_post_suffix(bo):
    # ⟨གསུམ⟩ and ⟨བསམ⟩ open with a prefix, so their ⟨ས⟩ is the ROOT and
    # keeps its /s/ — the letter two back is what tells the two apart.
    assert bo.transcribe_word("བསམ") == "sam˥˥"


def test_medial_ba_is_a_semivowel(bo):
    # ⟨་བ⟩ is wa: ⟨བ⟩ opening a non-initial syllable lenites.
    assert bo.transcribe_word("གཙོ་བོ") == "tso˥˥wo˩˨"


def test_achung_opens_a_syllable_with_a_glottal_stop(bo):
    assert bo.transcribe_word("འོག") == "ʔoʔ˩˧˨"
