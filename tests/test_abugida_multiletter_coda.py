# -*- coding: utf-8 -*-
"""A written coda may be several letters, and only the spec says which.

``coda_no_inherent_vowel`` looks back past a coda letter to find the nucleus
its syllable already has, which is what lets the Tibetan post-suffix ⟨ས⟩ be
silent in ⟨ཁམས⟩. The search is bounded by the letters the spec itself
describes post-vocalically. Thai and Lao describe none, because in those
scripts a bare consonant is routinely the ONSET of a syllable whose vowel is
not written at all — an unbounded search deletes that vowel and leaves a
consonant run the phonotactics forbid.
"""
import pytest

import orthography2ipa as o2i


@pytest.mark.parametrize("lang,word,ipa", [
    # ⟨ພຸດທະ⟩ buddha: ⟨ທ⟩ opens the second syllable and keeps its vowel.
    ("lo", "ພຸດທະ", "pʰut̚tʰaʔ"),
    # ⟨เอกชน⟩ private sector: ⟨ช⟩ opens ⟨ชน⟩ and keeps its implicit vowel.
    # (Thai writes its tone: /ʔèːk/ is a dead-long mid-class syllable.)
    ("th", "เอกชน", "ʔeːk˨˩tɕʰon˧"),
])
def test_an_onset_consonant_keeps_its_implicit_vowel(lang, word, ipa):
    assert o2i.G2P(lang).transcribe_word(word) == ipa


@pytest.mark.parametrize("lang,words", [
    ("lo", ["ພຸດທະ", "ພຸດທະສາສະໜາ"]),
    ("th", ["เอกชน", "เอกสาร", "อุปกรณ์"]),
])
def test_no_syllable_loses_its_nucleus_wholesale(lang, words):
    """Neither language allows a three-consonant run; a spike in them is the
    signature of nuclei being deleted, and it is what an unbounded look-back
    produces. Counted over segments rather than characters, and over a word
    list rather than one spot-check, so a future widening of the search
    cannot pass by getting the two words above right."""
    from orthography2ipa.allophony import segment_ipa

    g = o2i.G2P(lang)
    atoms = tuple(sorted(o2i.phoneme_inventory(o2i.get(lang)),
                         key=len, reverse=True))
    vowels = set("aeiouɛɔəɨʉɯøœyɐɤʌæɑɒ")
    for word in words:
        ipa = g.transcribe_word(word)
        run = best = 0
        for seg in segment_ipa(ipa, atoms):
            # A CV atom (Thai ⟨เอ⟩ /ʔeː/) carries the syllable's nucleus even
            # though it opens with a consonant, so the run ends at it: the
            # thing this test hunts is a DELETED nucleus.
            if seg and any(ch in vowels for ch in seg):
                run = 0
            else:
                run += 1
                best = max(best, run)
        assert best < 3, f"{lang} {word} -> {ipa}: {best}-consonant run"


def test_tibetan_post_suffix_still_reaches_its_nucleus():
    """The bound must not cost Tibetan the thing it was added for."""
    bo = o2i.G2P("bo")
    assert bo.transcribe_word("ཁམས") == "kʰam˥˨"
    assert bo.transcribe_word("ཁོགས") == "kʰoʔ˥˨"


def test_dzongkha_post_suffix_surfaces_its_coda():
    """Dzongkha's ⟨ས⟩ took an inherent vowel of its own and spelled the coda
    away: ⟨མཚམས⟩ came out with a trailing [sɑ] instead of the [m] the gold
    and van Driem's description both give."""
    dz = o2i.G2P("dz")
    assert dz.transcribe_word("མཚམས") == "t͡sʰɑ˥m"
    assert dz.transcribe_word("ཞབས") == "ʑɑ˩p"


def test_tsheg_is_a_syllable_boundary_not_a_transparent_mark():
    """⟨་⟩ (tsheg) SEPARATES Tibetan/Dzongkha syllables; the spec maps it to
    ``[""]`` because it spells no segment of its own, but that is not the
    same thing as being transparent to a look-back the way a combining tone
    mark is. A look-back that walks across the tsheg reaches into the
    PREVIOUS syllable and deletes the next syllable's own inherent vowel:
    ⟨ཀ་ཀ་ནི⟩ (k a k a n i) collapses ⟨ཀ⟩+⟨ནི⟩ into one syllable and drops the
    second ⟨ཀ⟩'s vowel, and ⟨ཀ་ཀོ་ལ⟩ (k a k o l a) drops the final ⟨ལ⟩'s
    vowel outright."""
    bo = o2i.G2P("bo")
    assert bo.transcribe_word("ཀ་ཀ་ནི") == "ka˥˥ka˥˥ni˩˨"
    assert bo.transcribe_word("ཀ་ཀོ་ལ") == "ka˥˥ko˥˥la˩˨"
