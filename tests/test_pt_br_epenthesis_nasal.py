"""pt-BR breaks a stop and a following nasal with the epenthetic [i].

Collischonn (2004: 68, Tabela 2) counts the vowel in "Oclusiva Nasal (mogno)
116/151 77", against "Oclusiva não nasal (rapto) 34/78 44", and her p. 66
names hipnose. She lists the sequences "acne, signo, magma, abnegado, patmos,
admitir, etnia, Edna" (p. 68). Barbosa & Albano (2004: 227): "The epenthetic
vowel is always [i] or [ɪ]". The rule is BR_EPENTHESIS in pt-BR.json.

Each expected substring is the stop, [i] and the nasal. A /t d/ before the
inserted [i] is the affricate (Barbosa & Albano 2004: 228).
"""
import pytest

from orthography2ipa import transcribe


def _bare(word, code="pt-BR"):
    return transcribe(word, code).replace("ˈ", "")


@pytest.mark.parametrize("word, part", [
    ("hipnose", "pin"), ("abnegado", "bin"), ("admitir", "d͡ʒim"),
    ("etnia", "t͡ʃin"),
])
def test_a_pretonic_stop_before_a_nasal_takes_the_vowel(word, part):
    assert part in _bare(word)


@pytest.mark.parametrize("code", ["pt-BR-x-sul", "pt-BR-x-floripa", "pt-BR-x-pr"])
def test_the_southern_specs_inherit_it(code):
    """Collischonn's data are from Porto Alegre, Florianópolis and Curitiba."""
    assert "pin" in _bare("hipnose", code)


@pytest.mark.parametrize("code", ["pt-BR-x-sul", "pt-BR-x-floripa", "pt-BR-x-pr"])
def test_the_southern_specs_keep_the_post_tonic_cluster(code):
    """Collischonn (2004: 75): the optimum for mogno has the syllables g.no,
    without the vowel, and the optimum for the pretonic magnata is
    "ma.gi.(ná.ta)"."""
    assert "ɡn" in _bare("mogno", code)
    assert "ɡin" in _bare("magnata", code)


def test_two_nasals_keep_the_cluster():
    """Collischonn (2004: 69, note 7) found no token with a nasal before the nasal."""
    assert _bare("amnésia") == "ɐ̃nɛziɐ"
