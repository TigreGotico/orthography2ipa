"""The word-final tap of a Brazilian Portuguese infinitive drops.

Barbosa & Albano (2004: 228-229): "The tap is the preferred realisation for
/R/ in the variety presented here. In infinitives, however, this sound usually
drops word-finally except if followed by a vowel." Callou, Moraes & Leite
(1998: 66) name the cue in the spelling: the infinitive and the future
subjunctive carry the final R and the stress on its syllable (comer versus
come), and the R of a non-verb carries no morphological information.

Expected forms combine the drop with the other values of the same source: the
oral vowels [a e i o] in the stressed syllable, the coda tap inside the word
and /t/ affricated before [i] (p. 228).
"""
import json
import re
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import transcribe
from orthography2ipa.json_loader import load_json_spec

DATA = Path(orthography2ipa.__file__).parent / "data"
RULE_IDS = ("BR_FINAL_R_NONVERB", "BR_INFINITIVE_R_DROP", "BR_INFINITIVE_R_DROP_POR")


def _own_rules(code):
    spec = json.loads((DATA / f"{code}.json").read_text(encoding="utf-8"))
    return {r["id"]: r for r in spec.get("allophone_rules", [])}


@pytest.mark.parametrize("word,expected", [
    ("falar", "faˈla"),
    ("comer", "koˈme"),
    ("partir", "paɾˈt͡ʃi"),
    ("sair", "saˈi"),
    ("ser", "ˈse"),
    ("pôr", "ˈpo"),
    ("compor", "kõˈpo"),
    ("fizer", "fiˈze"),
    ("Falar", "faˈla"),
])
def test_infinitive_and_future_subjunctive_drop_the_tap(word, expected):
    assert transcribe(word, "pt-BR") == expected


@pytest.mark.parametrize("word,expected", [
    ("mar", "ˈmaɾ"),
    ("lugar", "luˈɡaɾ"),
    ("mulher", "muˈʎeɾ"),
    ("amor", "aˈmoɾ"),
    ("quer", "ˈkeɾ"),
])
def test_a_non_verb_keeps_the_tap(word, expected):
    assert transcribe(word, "pt-BR") == expected


@pytest.mark.parametrize("word", ["açúcar", "revólver", "caráter"])
def test_an_unstressed_final_syllable_keeps_the_tap(word):
    assert transcribe(word, "pt-BR").endswith("ɾ")


def test_the_tap_list_stands_before_the_drop():
    ids = [r.id for r in load_json_spec("pt-BR").allophone_rules]
    assert ids.index("BR_FINAL_R_NONVERB") < ids.index("BR_INFINITIVE_R_DROP")
    assert ids.index("BR_FINAL_R_NONVERB") < ids.index("BR_INFINITIVE_R_DROP_POR")


def test_every_listed_non_verb_is_in_the_domain_of_the_drop():
    words = _own_rules("pt-BR")["BR_FINAL_R_NONVERB"]["word"]
    assert len(words) == len(set(words))
    bad = [w for w in words
           if not re.fullmatch(r"[a-zçãõàü]*[aei]r", w)]
    assert bad == []


def test_every_listed_por_word_ends_in_or():
    words = _own_rules("pt-BR")["BR_INFINITIVE_R_DROP_POR"]["word"]
    assert "pôr" in words and "for" in words
    assert [w for w in words if not re.search(r"[oô]r$", w)] == []
    assert not {"amor", "maior", "vapor"} & set(words)


@pytest.mark.parametrize("code", ["pt-BR-x-sp", "pt-BR-x-sul", "pt-BR-x-pr", "pt-BR-x-floripa"])
def test_children_with_the_tap_inherit_the_drop(code):
    assert transcribe("falar", code) == "faˈla"
    assert transcribe("mar", code) == "ˈmaɾ"


@pytest.mark.parametrize("code,final", [
    ("pt-BR-x-rj", "h"),
    ("pt-BR-x-fluminen", "h"),
    ("pt-UY", "ɾ"),
])
def test_specs_that_switch_the_rules_off_keep_their_final_r(code, final):
    for rule_id in RULE_IDS:
        assert _own_rules(code)[rule_id]["phonemes"] == []
    assert transcribe("falar", code).endswith(final)
    assert transcribe("mar", code).endswith(final)
