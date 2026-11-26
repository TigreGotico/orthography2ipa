"""pt equi- glide: Infopédia pt-PT readings; equino from Priberam."""
import pytest

from orthography2ipa import transcribe

# Infopédia pt-PT: [kw] in the transparent "equal" compounds.
GLIDE = ["equiangular", "equiaxial", "equidade", "equidecomponível",
         "equidiferente", "equidistante", "equidistar", "equiforme",
         "equigranular", "equilateral", "equimolal", "equinumérico",
         "equipendente", "equipolente", "equipotente", "equiprovável",
         "equisseto", "equitativo", "equivalve", "equiângulo"]
# Infopédia pt-PT: [k] in the lexicalized words.
PLAIN = ["equilíbrio", "equimose", "equinoderme", "equipa",
         "equipar", "equipamento", "equiparação", "equipartição",
         "equitação", "equivalência", "equivalente", "equivaler",
         "equívoco", "equidna", "equipo", "equipou",
         "equipos", "tequila", "ressequida", "senequiano"]


@pytest.mark.parametrize("word", GLIDE)
def test_pt_pt_equal_prefix_has_glide(word):
    assert "kw" in transcribe(word, "pt-PT")


@pytest.mark.parametrize("word", PLAIN)
def test_pt_pt_lexicalized_word_has_no_glide(word):
    assert "kw" not in transcribe(word, "pt-PT")


@pytest.mark.parametrize("lang", ["pt-PT", "pt-BR"])
def test_equino_equine_sense_has_glide(lang):
    # Priberam equino1 |qüi| 'equine' is the default; equinodermo keeps [k].
    assert "kw" in transcribe("equino", lang)
    assert "kw" in transcribe("equídeo", lang)
    assert "kw" not in transcribe("equinodermo", lang)
    assert "kw" not in transcribe("equinócio", lang)
