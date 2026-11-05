"""Inside a word, a pt-PT coda sibilant is voiced to [ʒ] before a voiced
consonant and deleted before /ʒ/.

Cruz-Ferreira (1999, Handbook of the IPA, p. 128): "Syllable-final /ʃ/ occurs
as [ʒ] before a voiced consonant (except before /ʒ/ itself, where it is
deleted)". Infopédia writes asno ˈaʒnu, cisne ˈsiʒn(ə), mesmo ˈmeʒmu, desgelo
dəˈʒelu and desjejum dəʒəˈʒũ. A spec whose coda /s/ is not [ʃ] disables both
rules.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import G2P, get

#: Specs whose coda /s/ is [ʃ] and that take the rule.
HUSHED = ["pt-PT", "pt-PT-x-acores", "pt-PT-x-alentejo", "pt-PT-x-alfena",
          "pt-PT-x-algarve", "pt-PT-x-aveiro", "pt-PT-x-beira", "pt-PT-x-braga",
          "pt-PT-x-coimbra", "pt-PT-x-lisbon", "pt-PT-x-madeira",
          "pt-PT-x-minho", "pt-PT-x-porto", "pt-PT-x-sao-miguel",
          "pt-PT-x-terceira", "pt-PT-x-tras-os-montes", "pt-PT-x-viana",
          "pt-MO"]
#: Specs whose coda /s/ is [s] or [h] and that disable the rule.
DISABLED = ["pt-AO", "pt-CV", "pt-GW", "pt-MZ", "pt-ST", "pt-TL",
            "ext-PT-x-barranco", "idb", "mcm", "vkp"]
#: Creoles whose coda /s/ is [ʃ]. The rules have no source for them, so they
#: disable both rules and keep their own reading.
CREOLES = ["aoa", "cri", "kea", "mzs", "pap", "pov", "pre"]

#: Word, and the consonant after the coda sibilant. Infopédia writes [ʒ] there.
VOICED = [("esbelto", "b"), ("desdém", "d"), ("musgo", "ɡ"), ("desligar", "l"),
          ("mesmo", "m"), ("abismo", "m"), ("lesma", "m"), ("desmaio", "m"),
          ("desregrado", "ɾ"), ("asno", "n"), ("cisne", "n"), ("desnível", "n"),
          ("esnobe", "n"), ("desnudar", "n")]
#: Word, and the Infopédia reading of the syllable around the deleted coda.
BEFORE_ZH = [("desgelo", "dɨˈʒ"), ("desjejum", "dɨʒɨˈʒ"), ("disjunto", "diˈʒ"),
             ("desjeito", "dɨˈʒ")]
VOICELESS = [("pasta", "t"), ("mesquita", "k"), ("esfera", "f")]

DATA = Path(orthography2ipa.__file__).parent / "data"
RULE_IDS = ["PT_CODA_S_VOICING_INTERNAL", "PT_CODA_S_BEFORE_ZH_INTERNAL"]


def _sibilant_before(ipa: str, consonant: str) -> str:
    # The segment right before the consonant, skipping a stress mark.
    m = re.search(r"([ʃʒszh]|s̺)[ˈˌ]?" + consonant, ipa)
    assert m, (ipa, consonant)
    return m.group(1)


def _rule(lang, rule_id="PT_CODA_S_VOICING_INTERNAL"):
    return next((r for r in get(lang).allophone_rules if r.id == rule_id), None)


@pytest.mark.parametrize("word, consonant", VOICED)
def test_pt_pt_voices_before_a_voiced_consonant(word, consonant):
    ipa = G2P("pt-PT").transcribe_word(word)
    assert _sibilant_before(ipa, consonant) == "ʒ", ipa


@pytest.mark.parametrize("lang", HUSHED)
@pytest.mark.parametrize("word", ["mesmo", "desdém", "musgo"])
def test_every_hushing_spec_voices(lang, word):
    consonant = dict(VOICED)[word]
    ipa = G2P(lang).transcribe_word(word)
    assert _sibilant_before(ipa, consonant) == "ʒ", ipa


@pytest.mark.parametrize("word, start", BEFORE_ZH)
def test_the_sibilant_is_deleted_before_zh(word, start):
    ipa = G2P("pt-PT").transcribe_word(word)
    assert ipa.startswith(start), ipa
    assert "ʃʒ" not in ipa and "ʒʒ" not in ipa, ipa


@pytest.mark.parametrize("word", ["snobe", "slogan", "smoking", "sbirro"])
def test_a_word_initial_sibilant_is_not_voiced(word):
    # Infopédia writes [s] here (snobe ˈsnɔb(ə), slogan ˈsloɡan); the rule is
    # for a coda inside the word.
    assert not G2P("pt-PT").transcribe_word(word).lstrip("ˈˌ").startswith("ʒ")


@pytest.mark.parametrize("word, consonant", VOICELESS)
def test_the_sibilant_stays_voiceless_before_a_voiceless_consonant(word, consonant):
    ipa = G2P("pt-PT").transcribe_word(word)
    assert _sibilant_before(ipa, consonant) == "ʃ", ipa


def test_an_onset_sibilant_is_not_voiced():
    assert G2P("pt-PT").transcribe_word("chmm").startswith("ˈʃ")


@pytest.mark.parametrize("lang", HUSHED + DISABLED)
@pytest.mark.parametrize("rule_id", RULE_IDS)
def test_the_rule_follows_the_coda_sibilant(lang, rule_id):
    # The rule is active exactly where the spec's own coda /s/ in pasta is [ʃ].
    rule = _rule(lang, rule_id)
    coda = _sibilant_before(G2P(lang).transcribe_word("pasta"), "t")
    assert bool(rule.phonemes) == (coda == "ʃ"), (lang, coda, rule.phonemes)


@pytest.mark.parametrize("lang", CREOLES)
@pytest.mark.parametrize("rule_id", RULE_IDS)
def test_the_creoles_disable_the_rule(lang, rule_id):
    assert not _rule(lang, rule_id).phonemes


def test_no_other_spec_carries_the_rules():
    # A new child of pt-PT inherits both rules, so it fails here until it is
    # sorted into one of the lists above.
    carriers = {p.stem for p in DATA.glob("*.json")
                if any(_rule(p.stem, rule_id) for rule_id in RULE_IDS)}
    assert carriers == set(HUSHED + DISABLED + CREOLES)


@pytest.mark.parametrize("lang", DISABLED + CREOLES)
def test_disabled_specs_keep_their_coda(lang):
    for rule_id in RULE_IDS:
        assert _rule(lang, rule_id) is not None and not _rule(lang, rule_id).phonemes
    g = G2P(lang)
    coda = _sibilant_before(g.transcribe_word("pasta"), "t")
    assert _sibilant_before(g.transcribe_word("mesmo"), "m") == coda


def test_pt_br_is_not_changed():
    assert _rule("pt-BR") is None
    assert _rule("pt-BR", "PT_CODA_S_BEFORE_ZH_INTERNAL") is None
