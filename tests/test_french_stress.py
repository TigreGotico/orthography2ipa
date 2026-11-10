"""Opt-in French stress marks: ``fr-FR-x-stress``.

French has no stress block in ``fr-FR``, so the standard tags stay unmarked.
The notation variant ``fr-FR-x-stress`` states a block that marks the last
full syllable of a word that is not a function word. The sources are the ones
the English Wikipedia article "French phonology" (section Stress) reports:
Hirst & Di Cristo (1998: 196-197), Anderson (1982: 537), Tranel (1987:
194-200) and Walker (2001: 181-182). Function words are unmarked: the same
article reports a stress group made of a content word and its clitics
(Tranel 1987: 197).

The expected IPA is written here by the rule (mark before the onset of the
last full syllable). The function-word list was checked against
``espeak-ng -v fr --ipa -q`` 1.52 in sentence frames.
"""
import pytest

import orthography2ipa as o2i

TAG = "fr-FR-x-stress"


@pytest.mark.parametrize("text, expected", [
    ("lumière", "lyˈmjɛʁ"),
    ("salon", "saˈlɔ̃"),
    ("bonjour", "bɔ̃ˈʒuʁ"),
    ("minuteur", "minyˈtœʁ"),
    ("question", "kɛˈstjɔ̃"),
    ("maison", "mɛˈzɔ̃"),
    ("dentiste", "dɑ̃ˈtist"),
    ("d'accord", "daˈkɔʁ"),
    ("sept", "ˈsɛt"),
])
def test_a_content_word_is_marked_on_its_last_full_syllable(text, expected):
    assert o2i.transcribe(text, TAG) == expected


@pytest.mark.parametrize("text, expected", [
    ("le", "lə"), ("la", "la"), ("les", "le"), ("un", "œ̃"), ("une", "yn"),
    ("du", "dy"), ("de", "də"), ("des", "de"), ("ce", "sə"), ("se", "sə"),
    ("ne", "nə"), ("que", "kə"), ("qui", "ki"), ("en", "ɑ̃"),
    ("dans", "dɑ̃"), ("sur", "syʁ"), ("pour", "puʁ"), ("par", "paʁ"),
    ("est", "ɛ"), ("et", "e"), ("mes", "me"), ("il", "il"), ("je", "ʒə"),
    ("à", "a"), ("où", "u"), ("mais", "mɛ"), ("pas", "pa"), ("très", "tʁɛ"),
    ("tout", "tu"), ("plus", "ply"), ("c'est", "sɛ"),
])
def test_a_function_word_has_no_mark(text, expected):
    assert o2i.transcribe(text, TAG) == expected


def test_a_sentence_marks_the_content_words_only():
    assert (o2i.transcribe("la lumière du salon est allumée", TAG)
            == "la lyˈmjɛʁ dy saˈlɔ̃ ɛ alyˈme")


@pytest.mark.parametrize("tag", ["fr", "fr-FR", "fr-CA", "fr-BE", "fr-CH",
                                 "fr-LU"])
def test_the_standard_french_tags_stay_unmarked(tag):
    assert "ˈ" not in o2i.transcribe("la lumière du salon", tag)


def test_the_variant_keeps_the_fr_fr_segments():
    for text in ("lumière", "d'accord", "rouge orange", "les amis"):
        plain = o2i.transcribe(text, "fr-FR")
        marked = o2i.transcribe(text, TAG).replace("ˈ", "")
        assert marked == plain
