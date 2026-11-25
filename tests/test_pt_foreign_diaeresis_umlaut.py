"""Foreign names keep ⟨ä ö ü ë ï⟩, and pt-PT and pt-BR read ⟨ü ë ï⟩ as vowels.

AO1990 Base I, 3.º and the Obs. to Base XIV keep the letters of foreign proper
names (mülleriano, de Müller; hübneriano, de Hübner) and give no reading.
⟨ü⟩ is [u]. The French diaeresis ⟨ë ï⟩ after a vowel makes the vowel a nucleus
of its own (OQLF, Banque de dépannage linguistique). The expected strings are
written by hand from those readings. They are not output of the code.

The German and Nordic ⟨ö ä⟩ have no cited Portuguese reading. Their expected
values, ⟨ö⟩ [o] and ⟨ä⟩ [ɛ], are pending a citation and the tests are strict
xfails.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P

VOWELS = "aeiouɐɛɔɨ"

#: (lang, word, IPA, syllables).
CASES = [
    ("pt-PT", "Müller", "muˈleɾ", 2),
    ("pt-PT", "Hübner", "ubˈneɾ", 2),
    ("pt-PT", "Zürich", "ˈzuɾiʃ", 2),
    ("pt-PT", "Noël", "nuˈeɫ", 2),
    ("pt-PT", "Saül", "sɐˈuɫ", 2),
    ("pt-PT", "Raphaël", "ʁɐpɐˈeɫ", 3),
    ("pt-PT", "Moïse", "muˈizɨ", 3),
    ("pt-PT", "mülleriano", "mulɨɾiˈɐnu", 5),
    ("pt-PT-x-porto", "Zürich", "ˈzuɾiʃ", 2),
    ("pt-PT-x-porto", "Moïse", "muˈizɨ", 3),
    ("pt-AO", "Müller", "muˈlɛɾ", 2),
    ("pt-BR", "Hübner", "ubiˈne", 3),
    ("pt-BR", "Zürich", "ˈzuɾiʃ", 2),
    ("pt-BR", "Noël", "noˈɛw", 2),
    ("pt-BR", "Saül", "saˈuw", 2),
    ("pt-BR", "Raphaël", "ʁapaˈɛw", 3),
    ("pt-BR", "Moïse", "moˈizi", 3),
    ("pt-BR-x-sp", "Zürich", "ˈzuɾiʃ", 2),
    ("pt-BR-x-sp", "Noël", "noˈɛw", 2),
]
#: German and Nordic ⟨ö ä⟩: the nearest native vowel, pending a citation.
UMLAUT_OA = [
    ("pt-PT", "Göteborg", "ɡoˈtɛbuɾɡ"),
    ("pt-PT", "Köln", "ˈkoɫn"),
    ("pt-PT", "Bärbel", "bɛɾˈbɛɫ"),
    ("pt-AO", "Köln", "ˈkoɫn"),
    ("pt-BR", "Göteborg", "ɡoˈteboɾɡ"),
    ("pt-BR", "Köln", "ˈkow̃"),
    ("pt-BR", "Bärbel", "bɛɾˈbɛw"),
]
#: ⟨gü qü⟩ stay [ɡw kw] in pt-BR and its regional specs.
TREMA = [("lingüiça", "lĩˈɡwisɐ"), ("freqüente", "fɾeˈkwẽt͡ʃi"), ("agüentar", "aɡwẽˈta")]


@pytest.mark.parametrize("lang,word,ipa,syllables", CASES)
def test_reading(lang, word, ipa, syllables):
    assert G2P(lang).transcribe_word(word) == ipa


@pytest.mark.parametrize("lang,word,ipa,syllables", CASES)
def test_every_syllable_has_a_vowel(lang, word, ipa, syllables):
    out = G2P(lang).transcribe_word(word)
    assert sum(c in VOWELS for c in out) >= syllables


@pytest.mark.parametrize("lang", ["pt-BR", "pt-BR-x-sp", "pt-BR-x-bahia"])
@pytest.mark.parametrize("word,ipa", TREMA)
def test_brazilian_trema_stays_pronounced(lang, word, ipa):
    assert G2P(lang).transcribe_word(word) == ipa


@pytest.mark.xfail(strict=True, reason="waiting for a citation of the Portuguese reading of the German umlaut")
@pytest.mark.parametrize("lang,word,ipa", UMLAUT_OA)
def test_umlaut_o_a_reading(lang, word, ipa):
    assert G2P(lang).transcribe_word(word) == ipa
