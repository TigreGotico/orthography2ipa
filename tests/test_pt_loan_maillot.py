"""The French loan ⟨maillot⟩ reads as its Portuguese form maiô [maˈjo].

Priberam (s.v. maillot) gives the orthoepy |màiô| for pt-PT and pt-BR, with
"Origem: palavra francesa" and "Ver maiô"; à marks an open unstressed [a].
Aulete (s.v. maillot) has "pal. francesa aportuguesada em maiô". The rules
read the French spelling letter by letter, so pt-PT and pt-BR name the word
in word_exceptions. The rules already give maiô [maˈjo].
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P

SPECS = ["pt-PT", "pt-BR", "pt-AO", "pt-MZ", "pt-CV", "pt-GW", "pt-ST",
         "pt-TL", "pt-MO", "pt-PT-x-lisbon", "pt-PT-x-porto"]


@pytest.mark.parametrize("lang", SPECS)
@pytest.mark.parametrize("word", ["maillot", "Maillot"])
def test_maillot_reads_as_maio(lang, word):
    assert G2P(lang).transcribe(word) == "maˈjo"


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
def test_rules_read_maio(lang):
    assert G2P(lang).transcribe("maiô") == "maˈjo"
