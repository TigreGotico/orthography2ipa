"""pt-BR reads a coda ⟨x⟩ as the coda sibilant of the spec, and ⟨xc⟩ as one /s/.

Vasilévski (2012: 55, Table 1) gives "x |S| expor", "s |S| mosca, lesma" and
"xc /s/ exceção", and writes /ˈteS.tu/ on p. 56. The table gives the
archiphoneme, so the surface value of a coda ⟨x⟩ is the value of a coda ⟨s⟩.
"""
import pytest

from orthography2ipa import transcribe

CHIADO = ["pt-BR-x-rj", "pt-BR-x-norte", "pt-BR-x-recife", "pt-BR-x-floripa", "pt-BR-x-cuiaba"]


@pytest.mark.parametrize("word, ipa", [
    ("texto", "ˈtestu"),
    ("sexta", "ˈsestɐ"),
    ("explicar", "espliˈka"),
    ("expor", "esˈpo"),
    ("extra", "ˈestɾɐ"),
])
def test_a_coda_x_is_the_alveolar_of_the_base(word, ipa):
    assert transcribe(word, "pt-BR") == ipa


@pytest.mark.parametrize("word, ipa", [
    ("exceção", "eseˈsɐ̃w̃"),
    ("exceto", "eˈsetu"),
    ("excesso", "eˈsesu"),
])
def test_xc_before_a_front_vowel_is_one_s(word, ipa):
    assert transcribe(word, "pt-BR") == ipa


def test_x_before_a_k_is_a_coda():
    """⟨c⟩ is [k] here, so ⟨x⟩ is a coda and ⟨xc⟩ is no digraph."""
    assert transcribe("excluir", "pt-BR") == "eskluˈi"


@pytest.mark.parametrize("code", CHIADO)
def test_a_chiado_spec_gives_x_the_value_of_its_own_coda_s(code):
    """Coda ⟨x⟩ and coda ⟨s⟩ share |S|, so they agree within each spec."""
    assert transcribe("festa", code) == "ˈfeʃtɐ"
    assert transcribe("sexta", code) == "ˈseʃtɐ"


@pytest.mark.parametrize("code", CHIADO)
def test_a_chiado_x_voices_as_its_own_coda_does(code):
    assert transcribe("mesmo", code) == "ˈmeʒmu"
    assert transcribe("Vixnu", code) == "viʒˈnu"


@pytest.mark.parametrize("code", CHIADO)
@pytest.mark.parametrize("word, plain", [
    ("excesso", "ecesso"),
    ("exceto", "eceto"),
    ("exceção", "eceção"),
    ("excelente", "ecelente"),
])
def test_a_chiado_xc_is_one_s_like_a_plain_c(code, word, plain):
    """Table 1 writes ⟨xc⟩ as the phoneme /s/, not the coda |S|, so no palatal appears."""
    assert transcribe(word, code) == transcribe(plain, code)
    assert "ʃ" not in transcribe(word, code).replace("t͡ʃ", "")


def test_a_coda_x_voices_as_a_coda_s_does():
    """A coda /S/ assimilates the voicing of the next sound (Barbosa & Albano 2004: 229)."""
    assert transcribe("Vixnu", "pt-BR") == "vizˈnu"


def test_x_before_a_vowel_is_not_a_coda():
    """Vasilévski (2012: 55, Table 1): "x /z/ exato"."""
    assert transcribe("exato", "pt-BR") == "eˈzatu"
