"""Maquiritari / Ye'kwana (`mch`) — the central vowels and written vowel length.

The expected strings come from the spec's cited orthography reference
(``mch_orthography``, the Wikipedia Ye'kuana language article), never from the
engine or the gold. Its orthography section reads: "In the standard
orthography used in Venezuela, /ɨ/ is written ü, and /ə/ is written ö." and
"Long vowels are indicated by doubling the letter." Its vowel table, adapted
from Cáceres (2011), pairs each short vowel with its doubled spelling: i, ii;
e, ee; a, aa; o, oo; u, uu; ü, üü; ö, öö. The consonants in these words
(k, n, w, y, j) keep the values the spec already declares: y=[j], j=[h].
"""
import pytest

import orthography2ipa as o2i


@pytest.fixture(scope="module")
def mch():
    return o2i.G2P("mch")


@pytest.mark.parametrize("word,expected", [
    # ö is /ə/ in the Venezuelan standard, ü is /ɨ/.
    ("küwü", "kɨwɨ"),
    ("önwanno", "ənwanno"),
    ("tünwanno", "tɨnwanno"),
    # A doubled vowel letter is one long vowel, for every vowel in the table.
    ("eeka", "eːka"),
    ("yaawö", "jaːwə"),
    ("önöö", "ənəː"),
    ("öö", "əː"),
    ("wüüwa", "wɨːwa"),
    ("jüü", "hɨː"),
    ("kii", "kiː"),
    ("koo", "koː"),
    ("kuu", "kuː"),
])
def test_central_vowels_and_doubled_length(mch, word, expected):
    assert mch.transcribe_word(word) == expected


def test_o_umlaut_is_never_the_back_unrounded_vowel(mch):
    """No reading the source gives for ö is [ɤ]: the Venezuelan standard
    writes /ə/ with it and the Brazilian one writes /ɨ/."""
    for word in ("ö", "öö", "amödö", "önöö"):
        assert "ɤ" not in mch.transcribe_word(word)
