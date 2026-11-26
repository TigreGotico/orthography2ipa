"""pt equi- glide: Infopédia pt-PT readings; pt-BR equino from Michaelis."""
import pytest

from orthography2ipa import transcribe

# Infopédia pt-PT: [kw] in the transparent "equal" compounds.
GLIDE = ["equiangular", "equiaxial", "equidade", "equidecomponível",
         "equidiferente", "equidistante", "equidistar", "equiforme",
         "equigranular", "equilateral", "equimolal", "equinumérico",
         "equipendente", "equipolente", "equipotente", "equiprovável",
         "equisseto", "equitativo", "equivalve", "equiângulo"]
# Infopédia pt-PT: [k] in the lexicalized words.
PLAIN = ["equilíbrio", "equimose", "equino", "equinoderme", "equipa",
         "equipar", "equipamento", "equiparação", "equipartição",
         "equitação", "equivalência", "equivalente", "equivaler",
         "equívoco", "equidna"]


@pytest.mark.parametrize("word", GLIDE)
def test_pt_pt_equal_prefix_has_glide(word):
    assert "kw" in transcribe(word, "pt-PT")


@pytest.mark.parametrize("word", PLAIN)
def test_pt_pt_lexicalized_word_has_no_glide(word):
    assert "kw" not in transcribe(word, "pt-PT")


def test_equino_glide_is_pt_br_only():
    assert transcribe("equino", "pt-PT") == "iˈkinu"
    assert "kw" in transcribe("equino", "pt-BR")
    assert "kw" not in transcribe("equinócio", "pt-BR")
