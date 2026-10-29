"""A Portuguese hyphenated compound is one prosodic word with one main stress.

Each element of a compound by juxtaposition keeps its own stress and the
last is the strongest (Bechara, *Moderna Gramática Portuguesa*, p. 340,
quoted in Ciberdúvidas, resposta 28042). The engine reads a hyphen as a
word break, so it used to write a primary mark on every element. With
``stress.compound_stress = "last"`` the last marked element of a
hyphen-joined group keeps ``ˈ`` and every earlier one takes ``ˌ``. A
clitic (``stress.cliticless_words``) carries no mark, as before: *chamo-me*
is one stress, on the verb. An enclitic leans on its host, and *fala-se* is
one prosodic word (Toneli 2011, citing Vigário 2003).

Expected rows give one entry per hyphen element, read from the Portal da
Língua Portuguesa or Infopédia transcription named beside it, or from the
Acordo Ortográfico 1990, Base VIII, 1.º b for the enclisis forms.
"""
import glob
import os

import pytest

import orthography2ipa
from orthography2ipa import G2P, get

P, S = "ˈ", "ˌ"
DATA = os.path.join(os.path.dirname(orthography2ipa.__file__), "data")
PT_SPECS = sorted(
    os.path.basename(p)[:-5] for p in glob.glob(os.path.join(DATA, "pt-*.json")))

ROWS = [
    ("guarda-chuva", [S, P]),             # Portal gwˌaɾdɐʃˈuvɐ
    ("pisca-pisca", [S, P]),              # Portal pˌiʃkɐpˈiʃkɐ
    ("segunda-feira", [S, P]),            # Portal sɨgˌũdɐfˈɐjɾɐ
    ("norte-americano", [S, P]),          # Portal nˌɔɾtɨɐmɨɾikˈɐnu
    ("pé-de-meia", [S, None, P]),         # Portal pˌɛdɨmˈɐjɐ
    ("bem-me-quer", [S, None, P]),        # Portal bˌɐ̃jmɨkˈɛɾ
    ("vê-lo-emos", [S, None, P]),         # Portal vˌeluˈemuʃ
    ("lobo-da-alsácia", [S, None, P]),    # Infopédia lobudaɫˈsasjɐ
    ("amancebar-se", [P, None]),          # Infopédia ɐmɐ̃səˈbars
    ("chamo-me", [P, None]),
    ("dá-lo", [P, None]),
    ("fá-lo-ia", [S, None, P]),
    # Mesoclisis has the shape of vê-lo-emos: the ending after the atonic
    # pronoun is the last stressed element.
    ("dir-se-ia", [S, None, P]),
    # Bechara's rule, with the article an atonic clitic as in lobo-da-alsácia.
    ("Trás-os-Montes", [S, None, P]),
    # Not a compound: one word, one primary.
    ("casa", [P]),
]


def element_marks(ipa):
    out = []
    for element in ipa.split():
        marks = [ch for ch in element if ch in (P, S)]
        assert len(marks) <= 1, f"{element!r} carries two marks"
        out.append(marks[0] if marks else None)
    return out


def test_every_pt_spec_is_covered():
    assert len(PT_SPECS) == 39, PT_SPECS


@pytest.mark.parametrize("code", PT_SPECS)
def test_pt_specs_opt_in(code):
    assert get(code).stress.compound_stress == "last"


@pytest.mark.parametrize("code", PT_SPECS)
@pytest.mark.parametrize("word,expected", ROWS)
def test_compound_marks(code, word, expected):
    ipa = G2P(code).transcribe(word)
    assert element_marks(ipa) == expected, ipa


@pytest.mark.parametrize("code", ["pt-PT", "pt-BR"])
def test_space_separated_words_keep_their_own_primary(code):
    assert element_marks(G2P(code).transcribe("guarda chuva")) == [P, P]


@pytest.mark.parametrize("code", ["pt-PT", "pt-BR"])
def test_compound_inside_a_sentence(code):
    ipa = G2P(code).transcribe("guarda-chuva amarelo, pisca-pisca")
    assert element_marks(ipa) == [S, P, P, S, P], ipa


def test_default_is_off():
    """A spec that does not opt in keeps one primary per hyphen element."""
    assert get("es").stress.compound_stress == ""
    assert element_marks(G2P("es").transcribe("teórico-práctico")) == [P, P]


# The word API (transcribe_word, word_candidates) reads a compound element by
# element, as transcribe does, and returns one token. The board scores every
# one-word gold entry through it.

@pytest.mark.parametrize("code", PT_SPECS)
@pytest.mark.parametrize("word,expected", ROWS)
def test_word_api_marks(code, word, expected):
    ipa = G2P(code).transcribe_word(word)
    assert " " not in ipa, ipa
    assert [ch for ch in ipa if ch in (P, S)] == [m for m in expected if m], ipa


@pytest.mark.parametrize("code", PT_SPECS)
@pytest.mark.parametrize("word,_", ROWS)
def test_word_api_matches_sentence_api(code, word, _):
    """The word API runs no cross-word sandhi, so it is compared with
    transcribe with sandhi off (pt-AO norte-americano elides a vowel
    across the hyphen only in a sentence)."""
    sentence = G2P(code, apply_sandhi=False).transcribe(word)
    assert G2P(code).transcribe_word(word) == "".join(sentence.split())


@pytest.mark.parametrize("code", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word,first", [
    ("chamo-me", P),       # chamo is paroxytone: the first syllable
    ("guarda-chuva", S),   # Portal gwˌaɾdɐʃˈuvɐ
    ("pé-de-meia", S),     # Portal pˌɛdɨmˈɐjɐ
    ("fá-lo-ia", S),       # the accent on fá marks its stress
])
def test_word_api_mark_opens_the_first_syllable(code, word, first):
    assert G2P(code).transcribe_word(word).startswith(first)


@pytest.mark.parametrize("code", ["pt-PT", "pt-BR"])
@pytest.mark.parametrize("word", ["guarda-chuva", "chamo-me", "fá-lo-ia"])
def test_word_candidates_agree_with_transcribe_word(code, word):
    """The board's oracle check needs candidate 0 to be transcribe_word."""
    g2p = G2P(code)
    assert g2p.word_candidates(word, k=5) == [g2p.transcribe_word(word)]


def test_word_api_default_is_off():
    """A spec that does not opt in keeps the hyphen-blind word reading."""
    g2p = G2P("es")
    assert g2p.transcribe_word("teórico-práctico") == g2p.transcribe_word(
        "teóricopráctico")
