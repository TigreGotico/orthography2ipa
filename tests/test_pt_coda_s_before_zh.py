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


#: Every spec that resolves PT_CODA_S_BEFORE_ZH: pt-PT, its regional
#: children, the other national varieties and the creoles that inherit it.
RULE_SPECS = [
    "aoa", "cri", "ext-PT-x-barranco", "idb", "kea", "mcm", "mzs", "pap",
    "pov", "pre", "pt-AO", "pt-CV", "pt-GW", "pt-MO", "pt-MZ", "pt-PT",
    "pt-PT-x-acores", "pt-PT-x-alentejo", "pt-PT-x-alfena",
    "pt-PT-x-algarve", "pt-PT-x-aveiro", "pt-PT-x-beira", "pt-PT-x-braga",
    "pt-PT-x-coimbra", "pt-PT-x-lisbon", "pt-PT-x-madeira", "pt-PT-x-minho",
    "pt-PT-x-porto", "pt-PT-x-sao-miguel", "pt-PT-x-terceira",
    "pt-PT-x-tras-os-montes", "pt-PT-x-viana", "pt-ST", "pt-TL", "vkp",
]

#: The specs where the letter s is the plain [ʃ] and jogos starts with [ʒ],
#: so the rule's two contexts both meet a lone sibilant.
LONE_SIBILANT_SPECS = [
    "cri", "kea", "mzs", "pt-MO", "pt-PT", "pt-PT-x-acores",
    "pt-PT-x-alentejo", "pt-PT-x-algarve", "pt-PT-x-braga",
    "pt-PT-x-coimbra", "pt-PT-x-lisbon", "pt-PT-x-madeira",
    "pt-PT-x-porto", "pt-PT-x-sao-miguel", "pt-PT-x-terceira",
]

LONE_SIBILANT_PHRASES = [("s", "jogos"), ("S", "João"), ("x", "jogos")]

MARKS = set("ˈˌ")


def test_rule_specs_are_every_spec_with_the_rule():
    from orthography2ipa.registry import available_codes
    found = set()
    for code in available_codes():
        try:
            rules = get(code).sandhi_rules or ()
        except Exception:
            continue
        if any(r.id == "PT_CODA_S_BEFORE_ZH" for r in rules):
            found.add(code)
    assert found == set(RULE_SPECS)


@pytest.mark.parametrize("lang", LONE_SIBILANT_SPECS)
@pytest.mark.parametrize("left,right", LONE_SIBILANT_PHRASES)
def test_a_word_that_is_only_the_sibilant_keeps_it(lang, left, right):
    # Cruz-Ferreira (1999: 128) deletes a SYLLABLE-FINAL /ʃ/. A word that is
    # only [ʃ] has no syllable, so the rule does not apply, and the word keeps
    # the form it has before a voiceless consonant.
    before_voiceless = _words(lang, f"{left} pés")[0]
    assert before_voiceless.lstrip("ˈˌ") == "ʃ", before_voiceless
    got = _words(lang, f"{left} {right}")
    assert got[0] == before_voiceless, got
    assert got[1] == _words(lang, right)[0], got


@pytest.mark.parametrize("lang", RULE_SPECS)
@pytest.mark.parametrize("left,right", [("s", "jogos"), ("S", "João")])
def test_no_word_is_left_without_a_segment(lang, left, right):
    got = _words(lang, f"{left} {right}")
    assert len(got) == 2 and all(set(w) - MARKS for w in got), got


@pytest.mark.parametrize("lang", ["pt-PT", "pt-PT-x-lisbon", "pt-PT-x-porto"])
@pytest.mark.parametrize("left,right", [("bíceps", "jogam"),
                                        ("tens", "jeito"),
                                        ("fórceps", "gelados")])
def test_a_consonant_before_the_sibilant_does_not_block_the_deletion(
        lang, left, right):
    # The nucleus may stand earlier in the word than the segment before [ʃ]:
    # the coda of bíceps is [pʃ] and that of tens is a nasal glide.
    before_voiceless = _words(lang, f"{left} pés")[0]
    assert before_voiceless.endswith("ʃ"), before_voiceless
    got = _words(lang, f"{left} {right}")
    assert got[0] == before_voiceless[:-1], got
