"""Word-final ⟨-em -ens⟩ and the unstressed nasal ⟨e⟩, per European lect.

European Portuguese has five nasal monophthongs, /ĩ ẽ ɐ̃ õ ũ/, and the
reduced vowel [ɨ] "occurs only in unstressed syllables" with no nasal
counterpart (Cruz-Ferreira 1999, Handbook of the IPA, p. 127, Lisbon
accent). Her diphthong table gives cem as [sɐ̃j] (p. 128) and her passage
transcribes the unstressed preposition em as [ɐ̃j] (p. 130). Ciberdúvidas
(Viana & Rocha 2006) gives -em and -en(s) as [ɐ̃j̃] in European Portuguese
and [ẽj̃] in some of its dialects; Wikipedia ("Portuguese phonology") puts
the merger of [ẽj̃] with [ɐ̃j̃] in Greater Lisbon.

Leite de Vasconcellos (Esquisse, 1901, §44n, p. 93) gives the Algarve and
Baixo-Alentejo [ẽj] in an open syllable and [ẽ] in a closed one. For the
Alto- and Baixo-Minho he records the pretonic ⟨en em⟩ as a reduced nasal,
"e surdo nasal": lembrar, pensamento, vender, tendência (Estudos de
Philologia Mirandesa I, 1900, §76, p. 238, and table b, p. 201).

The rows assert only the segment each source describes: the word ending,
or the nucleus of the pretonic nasal syllable.
"""
import unicodedata

import pytest

from orthography2ipa import G2P

LISBON_TYPE = ["pt-PT", "pt-PT-x-lisbon", "pt-PT-x-coimbra", "pt-PT-x-acores",
               "pt-PT-x-madeira", "pt-PT-x-alentejo"]
NORTH = ["pt-PT-x-porto", "pt-PT-x-alfena", "pt-PT-x-trasosmontes",
         "pt-PT-x-minho", "pt-PT-x-braga", "pt-PT-x-viana"]
MINHO = ["pt-PT-x-minho", "pt-PT-x-braga", "pt-PT-x-viana"]
NOT_MINHO = LISBON_TYPE + ["pt-PT-x-porto", "pt-PT-x-alfena",
                           "pt-PT-x-trasosmontes", "pt-PT-x-algarve",
                           "pt-PT-x-beira", "pt-PT-x-aveiro"]

FINAL_EM = ["homem", "viagem", "bem", "cem", "também", "vendem", "nuvem"]
FINAL_ENS = ["homens", "viagens", "jovens", "parabéns", "bens"]
PRETONIC_EN = ["pensar", "lembrar", "vender", "tendência", "pensamento"]


@pytest.fixture(scope="module")
def engines():
    return {}


def _ipa(engines, lang, word):
    if lang not in engines:
        engines[lang] = G2P(lang)
    return unicodedata.normalize("NFC", engines[lang].transcribe_word(word))


@pytest.mark.parametrize("lang", LISBON_TYPE)
@pytest.mark.parametrize("word", FINAL_EM)
def test_lisbon_type_final_em_is_central_diphthong(engines, lang, word):
    assert _ipa(engines, lang, word).endswith("ɐ̃j̃")


@pytest.mark.parametrize("lang", LISBON_TYPE)
@pytest.mark.parametrize("word", FINAL_ENS)
def test_lisbon_type_final_ens_is_central_diphthong(engines, lang, word):
    assert _ipa(engines, lang, word)[-len("ɐ̃j̃ʃ"):] == "ɐ̃j̃ʃ"


@pytest.mark.parametrize("lang", NORTH)
@pytest.mark.parametrize("word", FINAL_EM)
def test_north_final_em_keeps_close_mid_nucleus(engines, lang, word):
    assert _ipa(engines, lang, word).endswith("ẽj̃")


@pytest.mark.parametrize("lang", NORTH)
@pytest.mark.parametrize("word", FINAL_ENS)
def test_north_final_ens_keeps_close_mid_nucleus(engines, lang, word):
    ipa = _ipa(engines, lang, word)
    assert ipa.removesuffix("s̺").removesuffix("ʃ").endswith("ẽj̃"), ipa
    assert ipa.endswith(("ʃ", "s̺")), ipa


@pytest.mark.parametrize("word", FINAL_EM)
def test_algarve_open_final_em_is_close_mid_diphthong(engines, word):
    assert _ipa(engines, "pt-PT-x-algarve", word).endswith("ẽj̃")


@pytest.mark.parametrize("word", ["homens", "viagens", "jovens", "bens"])
def test_algarve_closed_final_ens_is_monophthong(engines, word):
    assert _ipa(engines, "pt-PT-x-algarve", word).endswith("ẽʒ")


@pytest.mark.parametrize("lang", NOT_MINHO)
@pytest.mark.parametrize("word", PRETONIC_EN + ["entender"])
def test_no_nasal_central_vowel_outside_the_minho(engines, lang, word):
    assert "ɨ̃" not in _ipa(engines, lang, word)


@pytest.mark.parametrize("lang", NOT_MINHO)
@pytest.mark.parametrize("word", ["pensar", "lembrar", "tendência"])
def test_pretonic_nasal_e_is_close_mid_outside_the_minho(engines, lang, word):
    ipa = _ipa(engines, lang, word)
    assert ipa[1:].startswith("ẽ"), ipa


@pytest.mark.parametrize("lang", MINHO)
@pytest.mark.parametrize("word", PRETONIC_EN)
def test_minho_pretonic_nasal_e_is_reduced(engines, lang, word):
    ipa = _ipa(engines, lang, word)
    assert ipa[1:].startswith("ɨ̃"), ipa


@pytest.mark.parametrize("lang", MINHO)
def test_minho_reduces_only_the_pretonic_syllable(engines, lang):
    """entender: word-initial ⟨en⟩ keeps [ẽ], the medial pretonic one reduces."""
    ipa = _ipa(engines, lang, "entender")
    assert ipa.startswith("ẽt") and "ɨ̃" in ipa, ipa


def test_medial_ens_is_not_the_plural_ending(engines):
    """menstruação: ⟨ens⟩ before a consonant inside the word stays [ẽ]."""
    ipa = _ipa(engines, "pt-PT", "menstruação")
    assert "ɐ̃j̃" not in ipa and ipa[1:].startswith("ẽ"), ipa


@pytest.mark.parametrize("word", ["jardins", "bombons", "atuns"])
def test_other_nasal_plurals_take_no_glide(engines, word):
    assert "j̃" not in _ipa(engines, "pt-PT", word)


def test_unstressed_preposition_em(engines):
    """Cruz-Ferreira 1999, p. 130: 'de acordo em como' has [ɐ̃j] for em."""
    assert _ipa(engines, "pt-PT", "em") == "ɐ̃j̃"
