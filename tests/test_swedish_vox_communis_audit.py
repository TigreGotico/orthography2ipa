"""The sv/vox_communis row: three spelling rules measured, five notation folds.

⟨c⟩ before a front vowel is [s], ⟨gn⟩ inside a word is [ŋn] and ⟨hj⟩ is [j];
the gold agrees on every word it holds (309, 154, 54). The rest of the row
is epitran's notation (length on every open syllable, no geminates, no
retroflex assimilation), folded 0.3695 to 0.0200. No `valid_ceiling`: the
spelling writes every contrast the folds touch.
"""
import pytest

from orthography2ipa import G2P, json_loader


def test_vox_communis_is_an_audit_not_a_ceiling():
    spec = json_loader.load_json_spec("sv")
    assert "vox_communis" not in (spec.valid_ceiling or {})
    entry = spec.audit["vox_communis"]
    assert entry.conclusion == "at_ceiling_documented"
    for number in ("0.3695", "0.0200", "17144", "309", "154", "54"):
        assert number in entry.measured, number
    assert "fold_sv_notation.py" in entry.measured


@pytest.mark.parametrize("word, expected", [
    ("centimeter", "ˈsɛntɪmɛtɛr"),
    ("cykel", "ˈsʏɕɛl"),
    ("cancer", "ˈkansɛr"),      # ⟨c⟩ before a back vowel stays [k]
    ("scen", "ˈseːn"),
    ("lögn", "ˈlœŋn"),
    ("regn", "ˈrɛŋn"),
    ("vagn", "ˈvaŋn"),
    ("gnista", "²ɡnɪsta"),      # word-initial ⟨gn⟩ stays [ɡn]
    ("hjälp", "ˈjɛlp"),
    ("hjärna", "²jæɳa"),
])
def test_the_three_spelling_rules(word, expected):
    assert G2P("sv").transcribe_word(word) == expected
