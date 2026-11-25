"""pt-PT ⟨x⟩ is [ks] or [s] in learned words; values from Infopédia (Porto Editora)."""
import pytest

from orthography2ipa import transcribe

KS = {
    "táxi": "ˈtaksi", "sexo": "ˈsɛksu", "fixo": "ˈfiksu", "tóxico": "ˈtɔksiku",
    "anexo": "ɐˈnɛksu", "fluxo": "ˈfluksu", "paradoxo": "pɐɾɐˈdɔksu",
    "léxico": "ˈlɛksiku", "convexo": "kõˈvɛksu", "fénix": "ˈfɛniks",
}
S = {"sintaxe": "sĩˈtasɨ", "máximo": "ˈmasimu", "próximo": "ˈpɾɔsimu"}
SH = ["intoxicar", "luxação", "taxa", "taxar", "peixe", "xérox"]


@pytest.mark.parametrize("word,ipa", sorted({**KS, **S}.items()))
def test_x_value(word, ipa):
    assert transcribe(word, "pt-PT") == ipa


@pytest.mark.parametrize("word", ["complexidade", "apoplexia", "axila", "flexão", "oxigénio", "maxilar", "axioma"])
def test_x_is_ks_inside_the_word(word):
    assert "ks" in transcribe(word, "pt-PT").replace("ˈ", "").replace("ˌ", "")


@pytest.mark.parametrize("word", SH)
def test_x_stays_sh(word):
    ipa = transcribe(word, "pt-PT").replace("ˈ", "").replace("ˌ", "")
    assert "ʃ" in ipa and "ks" not in ipa


def test_x_stays_z_in_ex_before_a_vowel():
    assert transcribe("exame", "pt-PT") == "eˈzɐmɨ"
