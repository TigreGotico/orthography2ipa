"""Foreign names keep ⟨ä ö ü ë ï⟩, and pt-PT and pt-BR read each as a vowel.

AO1990 Base I, 3.º and the Obs. to Base XIV keep the letters of foreign proper
names (mülleriano, de Müller; hübneriano, de Hübner) and give no reading. The
umlaut letters take the nearest native vowel: ⟨ü⟩ [u], ⟨ö⟩ [o], ⟨ä⟩ [ɛ]. The
French diaeresis ⟨ë ï⟩ after a vowel makes the vowel a nucleus of its own. The
expected strings are written by hand from those readings and from the
unchanged reading of the unmarked spelling. They are not output of the code.
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
    ("pt-PT", "Göteborg", "ɡoˈtɛbuɾɡ", 3),
    ("pt-PT", "Köln", "ˈkoɫn", 1),
    ("pt-PT", "Bärbel", "bɛɾˈbɛɫ", 2),
    ("pt-PT", "Noël", "nuˈeɫ", 2),
    ("pt-PT", "Saül", "sɐˈuɫ", 2),
    ("pt-PT", "Raphaël", "ʁɐpɐˈeɫ", 3),
    ("pt-PT", "Moïse", "muˈizɨ", 3),
    ("pt-PT", "mülleriano", "mulɨɾiˈɐnu", 5),
    ("pt-PT-x-porto", "Zürich", "ˈzuɾiʃ", 2),
    ("pt-PT-x-porto", "Moïse", "muˈizɨ", 3),
    ("pt-AO", "Müller", "muˈlɛɾ", 2),
    ("pt-AO", "Köln", "ˈkoɫn", 1),
    ("pt-BR", "Hübner", "ubiˈne", 3),
    ("pt-BR", "Zürich", "ˈzuɾiʃ", 2),
    ("pt-BR", "Göteborg", "ɡoˈteboɾɡ", 3),
    ("pt-BR", "Köln", "ˈkow̃", 1),
    ("pt-BR", "Bärbel", "bɛɾˈbɛw", 2),
    ("pt-BR", "Noël", "noˈɛw", 2),
    ("pt-BR", "Saül", "saˈuw", 2),
    ("pt-BR", "Raphaël", "ʁapaˈɛw", 3),
    ("pt-BR", "Moïse", "moˈizi", 3),
    ("pt-BR-x-sp", "Zürich", "ˈzuɾiʃ", 2),
    ("pt-BR-x-sp", "Noël", "noˈɛw", 2),
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
