"""The article and clitic pronoun ⟨o os⟩ have the reduced vowel [u] in pt-PT.

Cruz-Ferreira (1999, Handbook of the IPA, p. 130) transcribes O vento norte e
o sol as [u ˈvẽtu ˈnɔɾt i u sɔl]; p. 128 gives dos [duʒ]. The rules gave the
word-initial ⟨o⟩ [o], so pt-PT read o [o] and os [oʃ]. PT_LEX_CLITIC_O names
the two words and changes only the vowel. A spec that keeps an unstressed ⟨o⟩
as [o] disables the rule; so do the creoles that inherit it.
"""
from __future__ import annotations

from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import G2P, get

#: Specs whose rule is active and whose word_exceptions do not pin o and os.
REDUCED = ["pt-PT", "pt-PT-x-lisbon", "pt-PT-x-porto", "pt-PT-x-braga",
           "pt-PT-x-coimbra", "pt-PT-x-minho", "pt-PT-x-viana",
           "pt-PT-x-tras-os-montes", "pt-PT-x-aveiro", "pt-PT-x-alfena",
           "pt-PT-x-madeira", "pt-PT-x-terceira", "pt-MO", "pt-CV",
           "ext-PT-x-barranco"]
#: Specs that keep an unstressed ⟨o⟩ as [o] and have no word exception for os.
DISABLED = ["pt-AO", "pt-MZ", "pt-TL", "pt-GW", "pt-ST"]

DATA = Path(orthography2ipa.__file__).parent / "data"


def _rule(lang):
    return next((r for r in get(lang).allophone_rules
                 if r.id == "PT_LEX_CLITIC_O"), None)


@pytest.mark.parametrize("word, ipa", [("o", "u"), ("os", "uʃ"),
                                       ("O", "u"), ("Os", "uʃ")])
def test_pt_pt_reads_the_reduced_vowel(word, ipa):
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("lang", REDUCED)
def test_the_article_matches_the_contraction_with_de(lang):
    # do and dos already read the reduced vowel, so o and os are do and dos
    # without the [d].
    g = G2P(lang)
    assert g.transcribe_word("o") == g.transcribe_word("do")[1:]
    assert g.transcribe_word("os") == g.transcribe_word("dos")[1:]


@pytest.mark.parametrize("phrase, ipa", [("os amigos", "uz ɐˈmiɡuʃ"),
                                         ("os gatos", "uʒ ˈɡatuʃ"),
                                         ("os jogos", "u ˈʒɔɡuʃ"),
                                         ("o gato", "u ˈɡatu")])
def test_pt_pt_sandhi_keeps_working(phrase, ipa):
    assert G2P("pt-PT").transcribe(phrase) == ipa


@pytest.mark.parametrize("word", ["osso", "ovo", "olho", "ontem"])
def test_other_words_with_o_keep_their_vowel(word):
    assert not G2P("pt-PT").transcribe_word(word).lstrip("ˈ").startswith("u")


@pytest.mark.parametrize("lang", sorted(p.stem for p in DATA.glob("*.json")))
def test_the_rule_follows_unstressed_o_reduction(lang):
    # The rule is active exactly where the spec's own rules reduce the
    # pretonic ⟨o⟩ of bonito to [u].
    rule = _rule(lang)
    if rule is None:
        return
    reduces = G2P(lang).transcribe_word("bonito")[1:].startswith("u")
    assert bool(rule.phonemes) == reduces, (lang, rule.phonemes)


@pytest.mark.parametrize("lang", DISABLED)
def test_specs_without_reduction_keep_their_reading(lang):
    assert _rule(lang) is not None and not _rule(lang).phonemes
    assert G2P(lang).transcribe_word("os").startswith("o")


def test_pt_br_is_not_changed():
    assert _rule("pt-BR") is None
