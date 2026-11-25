"""The trema of ⟨gü qü⟩ marks a pronounced ⟨u⟩, so pt-PT reads it [ɡw kw].

Spellings written before the AO1990 keep the trema: lingüiça, freqüente. The
unmarked spelling is read the same way in pt-PT, and the expected values are
the Infopédia pt-PT readings of the unmarked forms, from o2i-lexicons
data/pt-PT/infopedia.tsv. ⟨ü⟩ and the vowel after it are one syllable, so the
stress mark stands before the onset: fɾɨˈkwẽtɨ.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P

#: (trema spelling, Infopédia pt-PT reading of the unmarked spelling).
TREMA_WORDS = [
    ("agüentar", "ɐɡwẽˈtaɾ"),            # aguentar
    ("cinqüenta", "sĩˈkwẽtɐ"),           # cinquenta
    ("conseqüente", "kõsɨˈkwẽtɨ"),       # consequente
    ("argüir", "ɐɾˈɡwiɾ"),               # arguir
    ("argüido", "ɐɾˈɡwidu"),             # arguido
    ("antigüidade", "ɐ̃tiɡwiˈdadɨ"),     # antiguidade
    ("ambigüidade", "ɐ̃biɡwiˈdadɨ"),     # ambiguidade
    ("bilingüismo", "bilĩˈɡwiʒmu"),      # bilinguismo
    ("aqüífero", "ɐˈkwifɨɾu"),           # aquífero
    ("antiqüíssimo", "ɐ̃tiˈkwisimu"),    # antiquíssimo
    ("argüente", "ɐɾˈɡwẽtɨ"),            # arguente
    ("anhangüera", "ɐɲɐ̃ˈɡwɛɾɐ"),        # anhanguera
    ("tranqüilo", "tɾɐ̃ˈkwilu"),         # tranquilo
    ("freqüente", "fɾɨˈkwẽtɨ"),          # frequente
    ("lingüiça", "lĩˈɡwisɐ"),            # linguiça
]
UNMARKED = [
    ("aguentar", "ɐɡẽˈtaɾ"), ("cinquenta", "sĩˈkẽtɐ"), ("frequente", "fɾɨˈkẽtɨ"),
    ("tranquilo", "tɾɐ̃ˈkilu"), ("linguiça", "lĩˈɡisɐ"), ("arguir", "ɐɾˈɡiɾ"),
]


@pytest.mark.parametrize("word,ipa", TREMA_WORDS)
def test_pt_pt_reads_the_trema(word, ipa):
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", UNMARKED)
def test_unmarked_spelling_is_unchanged(word, ipa):
    assert G2P("pt-PT").transcribe_word(word) == ipa


def test_porto_reads_the_trema():
    assert G2P("pt-PT-x-porto").transcribe_word("agüentar") == "ɐɡwẽˈtaɾ"


def test_angola_reads_the_trema():
    assert G2P("pt-AO").transcribe_word("lingüiça").startswith("lĩˈɡwi")
