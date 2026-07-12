"""Tests for broad-mode normalization folding place-of-articulation
diacritics in scripts/benchmark.py's normalize().

Broad transcription conventions never encode articulatory place detail
(dental/apical/laminal); broad mode already folded dental (U+032A) and
must also fold apical (U+033A) and laminal (U+033C) so dialects that
correctly emit e.g. apico-alveolar [s̺]/[z̺] aren't penalized against
gold sets that write plain [s]/[z].
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import normalize  # noqa: E402


def test_broad_mode_folds_apical_diacritic():
    assert normalize("s̺", strip_stress=True, broad=True) == "s"
    assert normalize("z̺", strip_stress=True, broad=True) == "z"


def test_broad_mode_folds_laminal_diacritic():
    assert normalize("s̼", strip_stress=True, broad=True) == "s"


def test_broad_mode_still_folds_dental_diacritic():
    assert normalize("t̪", strip_stress=True, broad=True) == "t"


def test_narrow_mode_does_not_strip_apical_or_laminal():
    assert normalize("s̺", strip_stress=True, broad=False) == "s̺"
    assert normalize("s̼", strip_stress=True, broad=False) == "s̼"


def test_non_apical_string_unchanged_by_broad_mode():
    assert normalize("kat", strip_stress=True, broad=True) == "kat"
    assert normalize("aˈbc", strip_stress=True, broad=True) == "abc"
