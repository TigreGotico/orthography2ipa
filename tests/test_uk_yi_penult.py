"""Ukrainian takes the penult by default ("default_position": -2), and ⟨ї⟩ after a vowel opens a syllable."""
import pytest

from orthography2ipa import transcribe

YI_FINAL_STRESS = pytest.mark.xfail(
    strict=True, reason="https://github.com/TigreGotico/orthography2ipa/issues/2538", raises=AssertionError)


@pytest.mark.parametrize("word, ipa", [
    pytest.param("Київ", "ˈkɪjiu̯", marks=YI_FINAL_STRESS),
    pytest.param("Миїв", "ˈmɪjiu̯", marks=YI_FINAL_STRESS),  # a constructed form
    pytest.param("поїзд", "ˈpɔjizd", marks=YI_FINAL_STRESS),
    ("Канів", "ˈkanʲiu̯"),
    ("Ніжин", "ˈnʲiʒen"),
])
def test_two_syllables_take_the_penult(word, ipa):
    assert transcribe(word, "uk") == ipa
