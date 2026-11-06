"""⟨porque⟩ is [ˈpuɾkɨ] in European Portuguese.

The CLUP dialect transcriptions, which are speech data, write ˈpuɾkɨ in all
13 tokens. pt.wiktionary gives Portugal /ˈpuɾ.kɨ/. The WikiPron pt-PT gold
has p u ɾ k ɨ, the en.wiktionary {{pt-IPA}} output from the respelling
pt=purque. The Portal da Língua Portuguesa Dicionário fonético agrees
('puɾkɨ), but it has no documented provenance. The rules alone give the
default stressed ⟨o⟩ [ɔ], so PT_LEX_REDUCED_O names the word. It changes
only the vowel, so each spec keeps its own consonants. The [u] is the vowel
an unstressed ⟨o⟩ reduces to, so a spec that keeps an unstressed ⟨o⟩ as [o]
disables the rule.
"""
from __future__ import annotations

from pathlib import Path

import pytest

import orthography2ipa

from orthography2ipa import G2P, get

#: pt-PT and the pt-PT dialects whose stressed vowel the rule sets.
PT_PT = ["pt-PT", "pt-PT-x-lisbon", "pt-PT-x-porto", "pt-PT-x-braga",
         "pt-PT-x-acores", "pt-PT-x-beira", "pt-PT-x-minho"]


@pytest.mark.parametrize("word", ["porque", "Porque"])
def test_pt_pt_reads_the_dictionary_form(word):
    assert G2P("pt-PT").transcribe_word(word) == "ˈpuɾkɨ"


@pytest.mark.parametrize("lang", PT_PT)
def test_the_stressed_vowel_is_u(lang):
    ipa = G2P(lang).transcribe_word("porque")
    assert ipa.startswith("ˈpu"), ipa


#: Specs that inherit the rule and keep it, outside pt-PT and its dialects.
KEEP = ["pt-MO", "pt-CV", "ext-PT-x-barranco"]
#: Specs that keep an unstressed ⟨o⟩ as [o] and disable the rule.
DISABLED = ["pt-AO", "pt-MZ", "pt-TL", "pt-GW", "pt-ST"]

DATA = Path(orthography2ipa.__file__).parent / "data"


@pytest.mark.parametrize("lang", PT_PT + KEEP)
def test_only_the_vowel_changes(lang):
    # The coda and the final syllable are the same as in porco, whose stressed
    # ⟨o⟩ the rule does not touch: only [ɔ o wɔ] before the coda becomes [u].
    porque = G2P(lang).transcribe_word("porque")
    porco = G2P(lang).transcribe_word("porco")
    coda = porco[porco.index("p") + 1:].lstrip("wɔo")[0]
    assert porque.startswith("ˈpu" + coda), (porque, porco)


@pytest.mark.parametrize("lang", PT_PT)
def test_porque_stays_a_different_word(lang):
    # porquê is stressed on the last syllable: pt.wiktionary /puɾ.ˈke/,
    # WikiPron pt-PT p u ɾ k e.
    ipa = G2P(lang).transcribe_word("porquê")
    assert ipa.startswith("puɾˈk"), ipa


def test_pt_pt_porque_with_circumflex():
    assert G2P("pt-PT").transcribe_word("porquê") == "puɾˈke"


@pytest.mark.parametrize("word", ["porco", "porta", "forte"])
def test_other_stressed_o_words_keep_their_vowel(word):
    assert G2P("pt-PT").transcribe_word(word).startswith(
        "ˈ" + word[0] + "ɔ")


def test_pt_br_is_not_changed():
    rules = {r.id for r in get("pt-BR").allophone_rules}
    assert "PT_LEX_REDUCED_O" not in rules


def _rule(lang):
    return next((r for r in get(lang).allophone_rules
                 if r.id == "PT_LEX_REDUCED_O"), None)


@pytest.mark.parametrize("lang", sorted(p.stem for p in DATA.glob("*.json")))
def test_the_rule_follows_unstressed_o_reduction(lang):
    # The rule is active exactly where the spec's own rules reduce the
    # pretonic ⟨o⟩ of bonito to [u]. The creoles that inherit it have no ⟨q⟩
    # in their spelling, so they never read porque and are left out.
    rule = _rule(lang)
    if rule is None or "k" not in G2P(lang).transcribe_word("porque"):
        return
    reduces = G2P(lang).transcribe_word("bonito")[1:].startswith("u")
    assert bool(rule.phonemes) == reduces, (lang, rule.phonemes)


@pytest.mark.parametrize("lang", DISABLED)
def test_specs_without_reduction_keep_the_stressed_vowel(lang):
    assert not _rule(lang).phonemes
    porque = G2P(lang).transcribe_word("porque")
    porco = G2P(lang).transcribe_word("porco")
    assert porque[:3] == porco[:3] and porque[2] != "u", (porque, porco)
