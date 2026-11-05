"""A word-final coda sibilant is deleted before /ʒ/ in European Portuguese.

Cruz-Ferreira (1999: 128), Handbook of the IPA: "Syllable-final /ʃ/ occurs as
[ʒ] before a voiced consonant (except before /ʒ/ itself, where it is deleted),
and as [z] before a syllable-initial vowel both within and across word
boundaries".

So the left word of os jogos keeps its vowel and loses the sibilant, while the
left word of os dois takes [ʒ] and that of os amigos takes [z]. The expected
form of each left word comes from the same word before a voiceless consonant
(os pés), where the sibilant is the plain [ʃ], with that [ʃ] taken off.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get

#: Specs whose word-final sibilant is the plain [ʃ]. pt-AO and pt-MZ write
#: it [s], so the rule, which reads [ʃ], never applies there.
LANGS = ["pt-PT", "pt-PT-x-lisbon", "pt-PT-x-porto", "pt-PT-x-acores"]

BEFORE_ZH = [("os", "jogos"), ("as", "janelas"), ("mais", "giro"),
             ("três", "jovens"), ("dois", "gelados")]


def _words(lang: str, text: str) -> list:
    return G2P(lang).transcribe(text).split(" ")


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("left,right", BEFORE_ZH)
def test_coda_sibilant_is_deleted_before_zh(lang, left, right):
    before_voiceless = _words(lang, f"{left} pés")[0]
    assert before_voiceless.endswith("ʃ"), before_voiceless
    got = _words(lang, f"{left} {right}")
    assert got[0] == before_voiceless[:-1], got
    assert got[1] == _words(lang, right)[0], got


@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("right,sibilant", [
    ("dois", "ʒ"), ("gatos", "ʒ"), ("meus", "ʒ"), ("pés", "ʃ"),
])
def test_other_consonants_keep_the_sibilant(lang, right, sibilant):
    # Cruz-Ferreira (1999: 128): [ʒ] before a voiced consonant; the plain [ʃ]
    # stays before a voiceless consonant.
    assert _words(lang, f"os {right}")[0].endswith(sibilant)


@pytest.mark.parametrize("lang", ["pt-PT", "pt-PT-x-lisbon"])
def test_a_vowel_keeps_the_sibilant(lang):
    # Cruz-Ferreira (1999: 128): [z] before a syllable-initial vowel.
    assert _words(lang, "os amigos")[0].endswith("z")


def test_every_spec_with_the_voicing_rule_has_the_deletion_rule():
    for code in ("pt-PT", "pt-PT-x-acores", "pt-PT-x-coimbra",
                 "pt-PT-x-sao-miguel", "pt-AO"):
        rules = {r.id: r for r in get(code).sandhi_rules}
        assert "PT_CODA_S_BEFORE_ZH" in rules, code
        # The voicing class leaves /ʒ/ out, so rule order does not decide
        # between [ʒ] and deletion.
        assert "ʒ" not in rules["PT_CODA_S_VOICING"].right_context, code


def test_pt_br_is_not_changed():
    # The source describes European Portuguese; pt-BR has no such rule.
    assert "PT_CODA_S_BEFORE_ZH" not in {
        r.id for r in (get("pt-BR").sandhi_rules or ())}
