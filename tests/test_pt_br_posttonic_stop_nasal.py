"""pt-BR breaks a post-tonic [t] before a nasal and a post-tonic [k] before [n].

Bisol (1999: 730), read only through Nascimento (2015: 59): "O resultado é
ri.ti.mo". Collischonn (2004: 67) names étnico and ritmo as post-tonic words.
Cagliari (1981: 107), read only through Nascimento (2015: 56), lists "técnica",
and gives "acne". The vowel is [i] (Barbosa & Albano 2004: 227), a /t/ before
it is the affricate (p. 228), and a final ⟨o⟩ is [u].
"""
import pytest

from orthography2ipa import transcribe


@pytest.mark.parametrize("word, ipa", [
    ("ritmo", "ˈʁit͡ʃimu"),
    ("étnico", "ˈɛt͡ʃiniku"),
    ("técnico", "ˈtɛkiniku"),
    ("técnica", "ˈtɛkinikɐ"),
    ("acne", "ˈakini"),
])
def test_the_vowel_breaks_the_cluster_the_sources_name(word, ipa):
    assert transcribe(word, "pt-BR") == ipa


@pytest.mark.parametrize("word, cluster", [
    ("dogma", "ɡm"),
    ("digno", "ɡn"),
    ("mogno", "ɡn"),
    ("dracma", "km"),
])
def test_clusters_no_source_gives_a_vowel_stay(word, cluster):
    """No source gives a value for these words, so the rule does not reach them."""
    assert cluster in transcribe(word, "pt-BR")


@pytest.mark.parametrize("code", ["pt-BR-x-sul", "pt-BR-x-floripa", "pt-BR-x-pr", "pt-UY"])
def test_the_specs_without_post_tonic_epenthesis_keep_the_cluster(code):
    """Collischonn (2004: 67) counts 24 % after the stressed syllable in the south."""
    assert "tm" in transcribe("ritmo", code)
    assert "kn" in transcribe("técnico", code)


def test_a_child_with_the_rule_keeps_its_own_coda_and_rhotic():
    assert transcribe("ritmo", "pt-BR-x-rj").endswith("it͡ʃimu")
