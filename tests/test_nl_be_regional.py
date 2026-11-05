"""Regional Standard Dutch of Belgium: the ``nl-BE-x-*`` delta specs.

Antwerp (``nl-BE-x-antwerp``) is a delta over ``nl-BE``. The expected values
come from the sources the spec cites, never from the engine:

- Sebregts (2014, *The Sociophonetics and Phonology of Dutch r*, LOT 379),
  41 Antwerp speakers. Onset /r/ is the voiced alveolar tap in 65.7% of the
  word-onset and 68.6% of the intervocalic tokens (Table 3-26, p. 88). A
  schwa stands between /r/ and "a following non-coronal or nasal consonant
  in a coda cluster" (p. 236) in 95.0% of the Antwerp tokens (Table 6-2,
  p. 242), and the r there is a voiced tap in 73.3% (Table 3-27, p. 89).
- Verhoeven & Van Bael (2002, *Taal en Tongval* 54, p. 16): "twee
  Antwerpse klinkers lang zijn ... Dit betreft [i] en [u]", measured in
  stressed test words (Piet, Lies, spoed, Loes, p. 6).

A word with none of these features must come out exactly as ``nl-BE``
gives it, and a moved parent must not move the values the child states.
"""
import json
from pathlib import Path

import pytest

from orthography2ipa import G2P, json_loader
from orthography2ipa.registry import resolves_exactly

DATA = Path(__file__).parents[1] / "orthography2ipa" / "data"
ANTWERP = "nl-BE-x-antwerp"


@pytest.fixture(scope="module")
def be():
    return G2P("nl-BE")


@pytest.fixture(scope="module")
def antwerp():
    assert resolves_exactly(ANTWERP), f"{ANTWERP} names no spec"
    return G2P(ANTWERP)


def test_antwerp_resolves_to_its_own_spec():
    assert resolves_exactly(ANTWERP)


def test_antwerp_is_regional_standard_dutch(antwerp):
    assert antwerp.spec.parent == "nl-BE"
    assert antwerp.spec.iso639_3 == "nld"


@pytest.mark.parametrize("word, expected", [
    # Word-onset items of Table 3-2 (p. 53): singletons and clusters.
    ("rok", "ˈɾɔk"), ("brood", "ˈbɾoːt"), ("trein", "ˈtɾɛin"), ("kruk", "ˈkɾʏk"),
    ("schrift", "ˈsxɾɪft"), ("gras", "ˈɣɾɑs"), ("rood", "ˈɾoːt"),
    # Intervocalic items: before and after the stress.
    ("beraad", "bəˈɾaːt"), ("beroep", "bəˈɾuːp"), ("sturen", "ˈstyːɾən"),
    ("waren", "ˈwaːɾən"),
])
def test_antwerp_onset_r_is_the_voiced_tap(be, antwerp, word, expected):
    assert "r" in be.transcribe(word)
    assert antwerp.transcribe(word) == expected


@pytest.mark.parametrize("word, expected", [
    # The four schwa-insertion items of Table 3-2 (p. 53) and Table 6-2 (p. 242).
    ("harp", "ˈɦɑɾəp"), ("kerk", "ˈkɛɾək"), ("berg", "ˈbɛɾəx"), ("arm", "ˈɑɾəm"),
    # The rest of the class on p. 236 and p. 259: kern is Sebregts' own example.
    ("kern", "ˈkɛɾən"), ("hoorn", "ˈɦoːɾən"), ("durf", "ˈdʏɾəf"), ("erg", "ˈɛɾəx"),
    ("dorp", "ˈdɔɾəp"), ("sterk", "ˈstɛɾək"), ("werkt", "ˈwɛɾəkt"),
    ("kerkhof", "ˈkɛɾəkɦɔf"), ("sterkste", "ˈstɛɾəkstə"), ("dorpje", "ˈdɔɾəpjə"),
    ("armband", "ˈɑɾəmbɑnt"), ("warmwater", "ˈwɑɾəmwaːtər̥"), ("alarmnummer", "ˈaːlɑɾəmnʏmər̥"),
])
def test_antwerp_inserts_schwa_after_r_before_a_non_coronal_coda(antwerp, word, expected):
    assert antwerp.transcribe(word) == expected


@pytest.mark.parametrize("word", [
    # The consonant opens the next syllable, so it is not in the coda cluster.
    "kerken", "bergen", "werken", "Antwerpen", "sterke", "armen", "kernen",
    # A coronal after /r/: 'only to a limited extent in the coda context' (p. 88).
    "worst", "paard", "kers", "kaars", "bord",
    # Word-final /r/ and /l/ + consonant are outside the measured class.
    "door", "melk", "film",
    # A consonant before /l/ or /r/ opens an onset cluster: 'in a coda cluster' (p. 236).
    "verblijf", "verflauwen", "verbergen",
    # An obstruent before /n w/ can open the next syllable (knal, kwartier).
    "deurknop", "verknallen", "Kloosterkwartier",
])
def test_antwerp_keeps_the_parent_r_outside_the_schwa_context(be, antwerp, word):
    assert antwerp.transcribe(word) == be.transcribe(word)


@pytest.mark.parametrize("word, expected", [
    ("Piet", "ˈpiːt"), ("Lies", "ˈliːs"), ("spoed", "ˈspuːt"), ("Loes", "ˈluːs"),
    ("riem", "ˈɾiːm"), ("boek", "ˈbuːk"),
])
def test_antwerp_stressed_i_and_u_are_long(be, antwerp, word, expected):
    # 'twee Antwerpse klinkers lang zijn ... Dit betreft [i] en [u]' (p. 16).
    assert "ː" not in be.transcribe(word)
    assert antwerp.transcribe(word) == expected


@pytest.mark.parametrize("word", ["taxi", "lelie", "sorry"])
def test_antwerp_unstressed_i_keeps_the_parent_value(be, antwerp, word):
    # The source measures stressed vowels only. The words carry their stress on
    # the first syllable, which the inherited stress block gets right.
    assert antwerp.transcribe(word) == be.transcribe(word)


@pytest.mark.parametrize("word", [
    "gaan", "dag", "acht", "huis", "tijd", "zitten", "lachen", "fee", "boot", "melk",
])
def test_antwerp_words_without_r_or_stressed_i_u_equal_the_parent(be, antwerp, word):
    assert antwerp.transcribe(word) == be.transcribe(word)


@pytest.mark.parametrize("word, expected", [
    ("verbranden", "vərˈbɾɑndən"), ("vergraven", "vərˈɣɾaːvən"),
    # ⟨berg⟩ is one slot that holds a vowel, so it is no coda consonant.
    ("verberg", "vərˈbɛɾəx"),
])
def test_antwerp_r_before_an_onset_cluster_takes_no_schwa(word, expected):
    # The /r/ of ver- stays in its coda; only the onset /r/ after b or g is the tap.
    assert G2P(ANTWERP).transcribe(word) == expected


def test_antwerp_restates_the_parent_voiceless_stop_devoicing():
    # The schwa rules must fire before the devoicing, so the child switches the
    # inherited rule off in place and restates it after its own rule.
    parent = json.loads((DATA / "nl-BE.json").read_text(encoding="utf-8"))
    child = json.loads((DATA / f"{ANTWERP}.json").read_text(encoding="utf-8"))

    def bare(rule):
        return {k: v for k, v in rule.items() if k not in ("id", "notes")}

    inherited = next(r for r in parent["allophone_rules"]
                     if r["id"] == "NL_BE_R_DEVOICE_BEFORE_VOICELESS_STOP")
    restated = next(r for r in child["allophone_rules"]
                    if r["id"] == "NL_BE_X_ANTWERP_R_DEVOICE_BEFORE_VOICELESS_STOP")
    assert bare(restated) == bare(inherited)


def test_antwerp_keeps_its_values_when_nl_be_moves(antwerp, tmp_path, monkeypatch):
    # An nl-BE whose ⟨kerk⟩ and ⟨berg⟩ keys lose the parent values. The child
    # states both keys itself, so its output must not follow.
    raw = json.loads((DATA / "nl-BE.json").read_text(encoding="utf-8"))
    raw["graphemes"]["kerk"] = ["kɛrk"]
    raw["positional_graphemes"]["berg"] = {"word_final": ["bɛrk"], "default": ["bɛrk"]}
    moved_file = tmp_path / "nl-BE.json"
    moved_file.write_text(json.dumps(raw, ensure_ascii=False), encoding="utf-8")
    index = dict(json_loader._index, **{"nl-BE": moved_file})
    specs = {k: v for k, v in json_loader._specs.items() if k not in ("nl-BE", ANTWERP)}
    monkeypatch.setattr(json_loader, "_index", index)
    monkeypatch.setattr(json_loader, "_specs", specs)

    moved = G2P("nl-BE", spec=json_loader.load_json_spec("nl-BE"))
    child = G2P(ANTWERP, spec=json_loader.load_json_spec(ANTWERP))
    assert moved.transcribe("berg") == "ˈbɛr̥k"
    for word in ("kerk", "berg", "kerken", "bergen", "bergtop"):
        assert child.transcribe(word) == antwerp.transcribe(word)
