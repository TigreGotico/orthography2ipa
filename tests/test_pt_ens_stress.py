"""Unaccented final -ens is paroxytone in every Portuguese spec.

The Acordo Ortográfico 1990 writes an acute on every oxytone of more than
one syllable that ends in -em or -ens (Base VIII, 1.º c: "acém, detém,
deténs, entretém, entreténs, harém, haréns, porém, provém, provéns,
também"), and lists *homem* among the paroxytones that take no accent
(Base IX, 1.º). An unaccented -ens is therefore the plural of an
unaccented paroxytone -em, and keeps its stress: *homens*, *jovens*,
*viagens*. The plurals -ins, -ons, -uns of the oxytones -im, -om, -um
stay oxytone; a paroxytone in -uns is written with an accent (Base IX,
2.º b: "álbum (pl. álbuns), fórum (pl. fóruns)").
"""
import glob
import os

import pytest

import orthography2ipa
from orthography2ipa import get
from orthography2ipa.stress import _syllables_for, detect_stress

DATA = os.path.join(os.path.dirname(orthography2ipa.__file__), "data")
PT_SPECS = sorted(
    os.path.basename(p)[:-5] for p in glob.glob(os.path.join(DATA, "pt-*.json")))

# word, stressed syllable counted from the end (-1 oxytone, -2 paroxytone)
ROWS = [
    ("homens", -2), ("jovens", -2), ("viagens", -2), ("nuvens", -2),
    ("origens", -2), ("imagens", -2), ("garagens", -2),
    ("parabéns", -1), ("armazéns", -1), ("haréns", -1), ("deténs", -1),
    ("jardins", -1), ("pudins", -1), ("bombons", -1), ("batons", -1),
    ("atuns", -1), ("comuns", -1), ("alguns", -1), ("álbuns", -2),
]


def test_every_pt_spec_is_covered():
    assert len(PT_SPECS) == 39, PT_SPECS


@pytest.mark.parametrize("code", PT_SPECS)
@pytest.mark.parametrize("word,from_end", ROWS)
def test_ens_stress(code, word, from_end):
    rules = get(code).stress
    sylls = _syllables_for(word, code, rules.diphthongs)
    assert detect_stress(word, rules, syllables=sylls) == len(sylls) + from_end, sylls
