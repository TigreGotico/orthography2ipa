"""Word-initial ⟨ex-⟩ before a vowel voices its ⟨x⟩ to [z] in pt-PT (``PT_INITIAL_EX_VOICED``).

The European values come from the Portal da Língua Portuguesa Dicionário fonético (ILTEC /
CLUL, Lisbon variety), which writes the unstressed initial vowel [i] and the ⟨x⟩ as [z]: exame
[i.zˈɐ.mɨ], exausto [i.zˈawʃ.tu], existir [i.ziʃ.tˈiɾ], exótico [i.zˈɔ.ti.ku], exato [i.zˈa.tu].
The Portal vowel is not asserted: the engine's initial vowel is [e] in pt-PT and [ɐ] in Lisbon, a separate question. Each test
compares the output after that vowel with the Portal string after its vowel.
"""
import pytest

from orthography2ipa import transcribe

# word -> Portal transcription with its initial vowel removed
PORTAL_AFTER_VOWEL = {
    "exame": "ˈzɐmɨ",
    "exato": "ˈzatu",
    "exausto": "ˈzawʃtu",
    "existir": "ziʃˈtiɾ",
    "exótico": "ˈzɔtiku",
}

LANGS = ["pt-PT", "pt-PT-x-lisbon", "pt-PT-x-coimbra"]


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word, rest", PORTAL_AFTER_VOWEL.items())
def test_initial_ex_vowel_is_z_after_the_initial_vowel(lang, word, rest):
    assert transcribe(word, lang)[1:] == rest


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word", ["exato", "exibir", "êxito", "êxodo", "exumar", "exemplo"])
def test_x_is_z_for_every_initial_ex_vowel_word(lang, word):
    ipa = transcribe(word, lang)
    assert ipa.replace("ˈ", "")[1:].startswith("z")
    assert "ʃ" not in ipa


# ⟨ex⟩ before a consonant keeps [ʃ] and the glide of PT_EX_CONSONANT_GLIDE.
@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("word", [
    "texto", "extra", "explicar", "excelente", "exterior", "xadrez"])
def test_the_rule_does_not_fire_outside_initial_ex_vowel(lang, word):
    ipa = transcribe(word, lang)
    assert "ʃ" in ipa
    assert "z" not in ipa


@pytest.mark.parametrize("lang, start", [
    ("pt-PT", "ˌeʃ"), ("pt-PT-x-lisbon", "ˌɐʃ"), ("pt-PT-x-coimbra", "ˌeʃ")])
def test_the_hyphenated_prefix_is_not_matched(lang, start):
    assert transcribe("ex-presidente", lang).startswith(start)
