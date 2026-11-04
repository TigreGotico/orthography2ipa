"""Cavite (cbk-PH-x-cavite) and Ternate (cbk-x-ternate) Chabacano transcribe.

Both specs take the Spanish-based cbk-PH table over ``graphemes_base``.
Every expected value below comes from Sippola's APiCS survey chapters, not
from engine output:

- Sippola, Eeva. 2013. Cavite Chabacano. APiCS survey chapter 45, §4
  Phonology: "The usual orthography is based on Spanish and uses <c, qu> for
  /k/, <j> for /h/, <y> for /j/, <ch> for /tʃ/", and casa [kása] 'house'.
- Sippola, Eeva. 2013. Ternate Chabacano. APiCS survey chapter 44, §4
  Phonology, Table 2: ŋ <ng>, tʃ <ch>, j <y>, and hénte [hénte] 'people'.

The acute in Sippola's forms marks stress. Neither spec encodes stress, so the
expected strings are the segments without it.
"""

import warnings

import pytest

from orthography2ipa.g2p import transcribe


def _transcribe(word: str, code: str) -> str:
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        return transcribe(word, code)


# Cavite forms are the chapter's own spellings: casa (§4), aquel 'that' (§5),
# ya 'already' (§6), quilaya 'how' (§8).
CAVITE = [
    ("casa", "kasa"),       # [kása]; <c> = /k/
    ("aquel", "akel"),      # <qu> = /k/
    ("quilaya", "kilaja"),  # <qu> = /k/, <y> = /j/
    ("ya", "ja"),           # <y> = /j/
]

# Ternate forms are Sippola's transcriptions: hénte (§4), kása, tay 'father',
# nay 'mother', mánga plural marker (§5), kayá 'so, therefore' (§9).
TERNATE = [
    ("kása", "kasa"),
    ("hénte", "hente"),     # [hénte]
    ("mánga", "maŋa"),      # <ng> = /ŋ/
    ("kayá", "kaja"),       # <y> = /j/
    ("tay", "taj"),
    ("nay", "naj"),
]


@pytest.mark.parametrize("word,expected", CAVITE)
def test_cavite_reads_its_spanish_based_spelling(word, expected):
    assert _transcribe(word, "cbk-PH-x-cavite") == expected


@pytest.mark.parametrize("word,expected", TERNATE)
def test_ternate_reads_sippola_transcription(word, expected):
    assert _transcribe(word, "cbk-x-ternate") == expected


@pytest.mark.parametrize("code,word", [("cbk-PH-x-cavite", "mujer"),
                                       ("cbk-x-ternate", "muhér")])
def test_woman_has_glottal_fricative(code, word):
    # Cavite writes /h/ as <j> (mujer), Ternate as <h> (muhér). The rhotic
    # value is not stated by either chapter, so only the /h/ is checked.
    assert _transcribe(word, code).startswith("muhe")
