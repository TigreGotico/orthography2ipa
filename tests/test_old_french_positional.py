"""Old French (``fro``) positional consonant readings.

Old French spells /k/ and /ɡ/ before ⟨e i⟩ as ⟨qu⟩ and ⟨gu⟩ precisely
because plain ⟨c⟩ and ⟨g⟩ were taken in that position: Schwan & Behrens,
*Grammaire de l'ancien français* (trans. Bloch, 1913), §13 — "Il était
d'autant plus nécessaire de conserver l'orthographe qu et gu pour
représenter les sons k et g devant e, i, que c et g dans la même position
servaient à rendre les sons ts, dž." Word-internal intervocalic ⟨s⟩ is
voiced while the spelling stays ⟨s⟩ (§126.1), and geminate ⟨ss⟩ is not
(§127).

These readings are declared on ``fro`` itself. They are NOT inherited from
``la-x-gallia``: that spec's positional table describes Gallo-Romance
lenition in progress, whose other entries are wrong for Old French
orthography — intervocalic ⟨v⟩ is /v/, not [β] or [w] (§105), and
intervocalic /d/ survived as [ð] only to about the end of the 11th century
before falling (§116.1).
"""
import json
import pathlib

import pytest

from orthography2ipa import G2P

SPEC = json.loads(
    (pathlib.Path(__file__).parent.parent / "orthography2ipa" / "data"
     / "fro.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def fro():
    return G2P("fro")


@pytest.mark.parametrize("word, expected", [
    ("cent", "ts"),       # c before e
    ("cité", "ts"),       # c before i
    ("gent", "dʒ"),       # g before e
    ("gitier", "dʒ"),     # g before i
    ("rose", "z"),        # intervocalic s
])
def test_positional_reading_fires(fro, word, expected):
    assert expected in fro.transcribe_word(word), (
        f"{word!r} -> {fro.transcribe_word(word)!r} lacks {expected!r}")


@pytest.mark.parametrize("word, forbidden", [
    ("quel", "ts"),       # qu keeps /k/ before e — the reason the digraph exists
    ("guerre", "dʒ"),     # gu keeps /ɡ/ before e
    ("car", "ts"),        # c before a is /k/, not the Gallo-Romance /tʃ/
    ("passer", "z"),      # geminate ss stays voiceless (§127)
])
def test_positional_reading_does_not_overfire(fro, word, forbidden):
    assert forbidden not in fro.transcribe_word(word), (
        f"{word!r} -> {fro.transcribe_word(word)!r} should not contain "
        f"{forbidden!r}")


def test_editorial_diaeresis_is_not_dropped(fro):
    """⟨ü⟩ is ⟨u⟩ = /y/ under the editors' hiatus diaeresis.

    With no key for it the letter has no reading at any length and the
    tokenizer discards it silently, which is a wrong transcription that
    costs almost nothing in PER and so hides in the aggregate.
    """
    assert fro.transcribe_word("armeüre") == "aɾməyɾə"


def test_fro_declares_no_grapheme_base(fro):
    """Old French does not take la-x-gallia's table.

    Wiring ``graphemes_base: la-x-gallia`` was measured against the 663-word
    WikiPron gold: it moves PER from 0.2738 to 0.2610, but the movement is a
    sum of three entries that are true of Old French and eight that are not,
    and it also imports the Gallo-Romance ``ca`` = /t͡ʃa/ key. The three true
    entries are declared here instead.
    """
    assert SPEC.get("graphemes_base") is None
    assert SPEC.get("positional_graphemes_base") is None
