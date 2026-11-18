"""Engine forms that the language pages quote in their prose.

A page that says "the spec gives `ˈɡʁap` for `Grab`" makes a claim about the
engine. Each row below names the page, the code, the word and the form, and the
test checks both halves: the page carries the sentence, and the engine gives the
form. A spec change that moves one of these forms then fails here until the page
follows.
"""
from pathlib import Path

import pytest

from orthography2ipa import G2P, transcribe

DOCS = Path(__file__).resolve().parent.parent / "docs" / "languages"

WORD_FORMS = [
    ("de-DE.md", "de-DE", "Grab", "ˈɡʁap"),
    ("de-DE.md", "de-DE", "Tag", "ˈtak"),
    ("de-DE.md", "de-DE", "brav", "ˈbʁaf"),
    ("de-DE.md", "de-DE", "Buch", "ˈbʊx"),
    ("de-DE.md", "de-DE", "Chor", "ˈkɔʁ"),
    ("de-DE.md", "de-DE", "Wespe", "ˈveːspə"),
    ("de-DE.md", "de-DE", "voll", "ˈvɔl"),
    ("de-DE.md", "de-DE", "Mädchen", "ˈmɛdçən"),
    ("pt-UY.md", "pt-UY", "mesmo", "ˈmesmu"),
    ("pt-UY.md", "pt-BR", "mesmo", "ˈmezmu"),
]


@pytest.mark.parametrize("page, code, word, form", WORD_FORMS)
def test_page_quotes_the_form_the_engine_gives(page, code, word, form):
    text = (DOCS / page).read_text(encoding="utf-8")
    assert f"`{form}`" in text and f"`{word}`" in text
    assert G2P(code).transcribe_word(word) == form


def test_an_valleys_quotes_both_entry_points_on_the_middle_dot():
    """transcribe_word reads one word; transcribe reads a text and, under `an`,
    splits it at the middle dot, which no `an` grapheme contains."""
    text = (DOCS / "an-valleys.md").read_text(encoding="utf-8")
    assert '`G2P("an").transcribe_word` gives `ˈbella`' in text
    assert '`transcribe("bel·la", "an")` gives the two words `ˈbel la`' in text
    assert '`transcribe("col·legi", "an")` gives `ˈkol ˈlexi`' in text
    assert G2P("an").transcribe_word("bel·la") == "ˈbella"
    assert transcribe("bel·la", "an") == "ˈbel la"
    assert transcribe("col·legi", "an") == "ˈkol ˈlexi"
