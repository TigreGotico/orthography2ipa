"""A vowel that an ``append`` rule inserts is matched in its own syllable.

The inserted vowel and the consonant before it make a syllable that the
spelling does not write, and that syllable takes no stress. Collischonn
(2004: 66) reports Câmara Jr.: "na posição postônica a vogal se reduz [...]
sendo, portanto, idênticas as pautas prosódicas de rapto e rápido", so the
[i] of pt-BR pacto is post-tonic, and she counts egípcios among the
post-tonic contexts (p. 67). Her tableau for the pretonic magnata gives
"ma.gi.(ná.ta)" (p. 75), and Nascimento (2015: 62-63) reports Collischonn
(1996: 151) for a word-initial cluster: "pneu [pi'new]".

Three probe rules stand before the pt-BR rules and rewrite an inserted [i]
by its stress position, so each test reads that position from the output.
"""
import dataclasses

import pytest

from orthography2ipa import G2P
from orthography2ipa.json_loader import load_json_spec
from orthography2ipa.types import AllophoneRule

_AFTER = ("p", "b", "t", "d", "k", "ɡ", "f", "v")


def _probe(stress, surface):
    return AllophoneRule(id=f"PROBE_{stress.upper()}", phonemes=("i",), surface=surface,
                         stress=stress, preceded_by_phoneme=_AFTER)


@pytest.fixture(scope="module")
def probed():
    spec = load_json_spec("pt-BR")
    probes = (_probe("stressed", "ɪ"), _probe("pretonic", "ɨ"), _probe("posttonic", "ə"))
    return G2P("pt-BR", spec=dataclasses.replace(
        spec, allophone_rules=probes + tuple(spec.allophone_rules)))


@pytest.mark.parametrize("word, ipa", [
    ("pneu", "pɨˈnew"),
    ("advogado", "ad͡ʒɨvoˈɡadu"),
    ("pacto", "ˈpakətu"),
])
def test_an_inserted_vowel_takes_the_stress_position_of_its_own_syllable(probed, word, ipa):
    assert probed.transcribe(word) == ipa


def test_the_nearest_earlier_vowel_places_the_syllable(probed):
    """Collischonn (2004: 67) counts egípcios among the post-tonic contexts:
    the [i] stands after the stressed syllable, not after the first one."""
    assert probed.transcribe("egípcio").startswith("eˈʒipə")


def test_pneu_has_an_oral_pretonic_vowel():
    """Collischonn (1996: 151), reported by Nascimento (2015: 62-63): "pneu [pi'new]"."""
    assert G2P("pt-BR").transcribe("pneu") == "piˈnew"


@pytest.mark.parametrize("word, start", [("gnomo", "ɡiˈn"), ("tmese", "t͡ʃiˈm")])
def test_the_inserted_vowel_before_a_stressed_nasal_onset_is_oral(word, start):
    """Barbosa & Albano (2004: 227): "The epenthetic vowel is always [i] or
    [ɪ]", and a /t/ before it is the affricate (p. 228)."""
    assert G2P("pt-BR").transcribe(word).startswith(start)


def test_a_written_stressed_i_before_a_nasal_stays_nasal():
    """Barbosa & Albano (2004: 229): "(em) cima sĩmɐ"."""
    assert G2P("pt-BR").transcribe("cima") == "ˈsĩmɐ"


def test_a_vowel_from_a_positional_value_keeps_the_stress_of_its_slot():
    """Engine contract, not phonology: pt-BR reads ⟨qu⟩ as [ku] only in a
    positional value (word-final), so that [u] is written, not inserted, and
    keeps the stress of its slot. The nonce word taqu ends in ⟨u⟩, so the
    stress is final."""
    spec = load_json_spec("pt-BR")
    probe = AllophoneRule(id="PROBE_STRESSED_U", phonemes=("u",), surface="ʉ",
                          stress="stressed", preceded_by_phoneme=("k",))
    g2p = G2P("pt-BR", spec=dataclasses.replace(
        spec, allophone_rules=(probe,) + tuple(spec.allophone_rules)))
    assert g2p.transcribe("taqu") == "taˈkʉ"
