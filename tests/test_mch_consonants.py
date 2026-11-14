"""Maquiritari / Ye'kwana (`mch`) — ⟨d⟩ and the digraphs ⟨sh⟩ and ⟨jh⟩.

The expected strings come from the spec's cited orthography reference
(``mch_orthography``, the Wikipedia Ye'kuana language article), never from the
engine or the gold. Its consonant table, adapted from Cáceres (2011), lists
the rhotic /ɾ̠/ with the spelling d, /ʃ/ with "s, sh" and /ç/ with "j/jh". Its
phonology section reads: "At the beginning of a word, and after a glottal
stop, /ɾ̠/ becomes [d]", and "/ɾ̠ɾ̠/ [dd] in Yeꞌkwana". Its orthography list
reads "[ɾ̠]~[d] - d", "[ʃ] - sh, s" and "[ç] - j (Venezuelan standard), jh
(Brazil and Amazonas)".

The words avoid the processes the spec does not encode: vowel lengthening
(bisyllables, closed syllables, or written long vowels only), palatalization
after /i/ and /j/, and the allophones of /h/ and /j/ at the start of a word
or after /o/, /u/, /w/ and the glottal stop. Other consonants keep the values
the spec already declares: ch=[tʃ], ñ=[ɲ], '=[ʔ], j=[h].
"""
import warnings

import pytest

import orthography2ipa as o2i
from orthography2ipa.exceptions import UnmappedGraphemeWarning


@pytest.fixture(scope="module")
def mch():
    return o2i.G2P("mch")


@pytest.mark.parametrize("word,expected", [
    # ⟨d⟩ is the rhotic /ɾ̠/ between vowels and after a consonant.
    ("adö", "aɾ̠ə"),
    ("edenna", "eɾ̠enna"),
    ("ashiichadu", "aʃiːtʃaɾ̠u"),
    # /ɾ̠/ is [d] at the start of a word ...
    ("danñe", "danɲe"),
    ("dü", "dɨ"),
    # ... after a glottal stop ...
    ("'dötö", "ʔdətə"),
    ("a'de'ta", "aʔdeʔta"),
    # ... and as the geminate /ɾ̠ɾ̠/.
    ("addö", "addə"),
    ("saddu", "saddu"),
])
def test_d_is_the_rhotic(mch, word, expected):
    assert mch.transcribe_word(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("a'sha", "aʔʃa"),
    ("ashiichadu", "aʃiːtʃaɾ̠u"),
    ("jhunu", "çunu"),
    ("jhumma", "çumma"),
])
def test_sh_and_jh_are_one_consonant(mch, word, expected):
    assert mch.transcribe_word(word) == expected


@pytest.mark.parametrize("word", ["a'sha", "ashiichadu", "jhunu", "jhumma"])
def test_sh_and_jh_drop_no_letter(word):
    # A fresh engine: the module fixture caches words the other tests read.
    with warnings.catch_warnings():
        warnings.simplefilter("error", UnmappedGraphemeWarning)
        o2i.G2P("mch").transcribe_word(word)


@pytest.mark.parametrize("word,expected", [
    # Words with no ⟨d⟩, ⟨sh⟩ or ⟨jh⟩ keep their readings.
    ("chaka", "tʃaka"),
    ("chökkö", "tʃəkkə"),
    ("a'sa", "aʔsa"),
    ("eese", "eːse"),
    ("aja", "aha"),
])
def test_other_consonants_keep_their_values(mch, word, expected):
    assert mch.transcribe_word(word) == expected


def test_d_is_never_implosive(mch):
    """No reading the source gives for ⟨d⟩ is the implosive [ɗ]."""
    for word in ("adö", "danñe", "'dötö", "addö", "amödö"):
        assert "ɗ" not in mch.transcribe_word(word)
