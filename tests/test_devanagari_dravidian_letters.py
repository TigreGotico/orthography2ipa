"""Devanagari ऩ ऱ ऴ read as their base letters.

NamesList.txt (Unicode 16.0.0) names three precomposed letters that NFC keeps
as one code point, because none is a composition exclusion:

- U+0929 NNNA, "for transcribing Dravidian alveolar n", equivalent to
  U+0928 + U+093C.
- U+0931 RRA, "for transcribing Dravidian alveolar r", whose half form is
  described as "Eyelash RA", equivalent to U+0930 + U+093C.
- U+0934 LLLA, "for transcribing Dravidian l", equivalent to U+0933 + U+093C.

The Unicode Standard (ch. 12, rule R5) says of the eyelash RA: "This form of RA
is commonly used in writing Marathi and Newari." No source states a reading for
ऩ or ऴ in these languages. The specs read each of the three letters as its base
letter, which is a choice of the specs. Wikipedia, "Marathi phonology", gives
दर्या [d̪əɾ.jaː] against दऱ्या [d̪əɾʲaː]; the spec does not write the palatalised
release.

The expected reading of each word is the reading of the same word written with
the base letter. That word passes through no new key, so it does not depend on
the keys under test. The base of ऴ is ⟨ळ⟩ where the spec has that letter, and
⟨ल⟩ where it has none, because the spec's inventory then has no retroflex
lateral to give it.
"""
import unicodedata
import warnings

import pytest

from orthography2ipa import G2P
from orthography2ipa.json_loader import load_json_spec

#: Specs with their own letter table, then the specs that inherit hi's table.
OWN = ["awa", "bho", "hi", "kok", "kru", "mai", "mr", "ne", "sa", "vsn"]
INHERITED = ["bgc", "doi", "gom", "hne", "mag", "new"]
LANGS = OWN + INHERITED

#: letter -> (base letter, word with the letter, word with the base letter)
ROWS = {
    "ऩ": ("न", "ऩम", "नम"),
    "ऱ": ("र", "कऱम", "करम"),
    "ऴ": (None, "कऴम", None),
}


@pytest.fixture(scope="module")
def engines():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return {lang: G2P(lang) for lang in LANGS}


def base_word(engine, letter):
    base, word, plain = ROWS[letter]
    if letter == "ऴ":
        base = "ळ" if "ळ" in engine.spec.graphemes else "ल"
        plain = word.replace("ऴ", base)
    return base, word, plain


@pytest.mark.parametrize("letter", sorted(ROWS))
@pytest.mark.parametrize("lang", LANGS)
def test_letter_reads_as_its_base_letter(engines, lang, letter):
    engine = engines[lang]
    _, word, plain = base_word(engine, letter)
    assert engine.transcribe_word(word) == engine.transcribe_word(plain)


@pytest.mark.parametrize("letter", sorted(ROWS))
@pytest.mark.parametrize("lang", LANGS)
def test_letter_is_not_dropped_with_a_warning(lang, letter):
    _, word, _ = ROWS[letter]
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        G2P(lang).transcribe_word(word)


@pytest.mark.parametrize("letter", sorted(ROWS))
def test_letter_survives_nfc(letter):
    decomposed = unicodedata.normalize("NFD", letter)
    assert len(decomposed) == 2 and decomposed[1] == "़"
    assert unicodedata.normalize("NFC", decomposed) == letter


def test_marathi_eyelash_ra_rows():
    mr = G2P("mr")
    # दऱ्या against दर्या `d̪əɾja`: the plain word is the issue's own row.
    assert mr.transcribe_word("दऱ्या") == "d̪əɾja"
    assert mr.transcribe_word("दऱ्या") == mr.transcribe_word("दर्या")
    assert mr.transcribe_word("वाऱ्या") == mr.transcribe_word("वार्या")
    assert mr.transcribe_word("ऱ्हास") == "ɾʱas"


def test_eyelash_ra_before_ha_is_the_murmured_tap_where_the_spec_has_the_cluster():
    # ⟨र्ह⟩ is a conjunct key of mr and kok, so ⟨ऱ्ह⟩ is the same cluster.
    for lang in ("mr", "kok"):
        engine = G2P(lang)
        assert engine.transcribe_word("ऱ्हास") == engine.transcribe_word("र्हास")


def test_hindi_nnna_row():
    hi = G2P("hi")
    assert hi.transcribe_word("ऩम") == "nəm"


@pytest.mark.parametrize("lang", OWN)
def test_spec_cites_unicode_for_the_three_letters(lang):
    ids = {s["id"] if isinstance(s, dict) else s.id for s in load_json_spec(lang).sources}
    assert {"unicode16_ch12", "unicode16_nameslist"} <= ids
