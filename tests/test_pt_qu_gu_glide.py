"""AO1990 Base XIV 1.º: the u of ⟨gu qu⟩ before ⟨e i⟩ is pronounced in a closed
set of words. Expected glides from Priberam (|güen| aguentar, |àgüí| sagui) and
the pre-1990 trema spellings."""
import pytest

import orthography2ipa as o

GLIDE = {"aguentar": "ɡw", "aguenta": "ɡw", "sagui": "ɡw", "linguiça": "ɡw", "pinguim": "ɡw",
         "linguista": "ɡw", "antiguidade": "ɡw", "arguir": "ɡw",
         "frequenta": "kw", "frequente": "kw", "tranquilo": "kw", "cinquenta": "kw",
         "equestre": "kw", "equino": "kw", "ubiquidade": "kw", "sequestro": "kw",  # Priberam also accepts |qué|; kw is the one pinned
         "bilíngue": "ɡw", "bilingue": "ɡw", "sequência": "kw", "delinquente": "kw",
         "eloquente": "kw", "ensanguentado": "ɡw", "quinquénio": "kw",
         "consequente": "kw", "ambiguidade": "ɡw", "aquífero": "kw", "antiquíssimo": "kw",
         "anhanguera": "ɡw"}
SILENT = {"argueiro": "ɡ", "equipa": "k", "requinte": "k", "guerra": "ɡ", "quero": "k", "seguir": "ɡ",
          "equinocial": "k", "equinócio": "k", "esquina": "k"}


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word,onset", sorted(GLIDE.items()))
def test_glide(lang, word, onset):
    assert onset in o.transcribe(word, lang)


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word,onset", sorted(SILENT.items()))
def test_silent_u(lang, word, onset):
    assert onset + "w" not in o.transcribe(word, lang)
