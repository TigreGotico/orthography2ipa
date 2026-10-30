"""Tests for the wikipron gold-file wiring of Spanish and Armenian
varieties in scripts/benchmark.py.

``es`` resolves (via the registry) to ``es-ES``, Castilian Spanish, which
has distinción (⟨cielo⟩ -> [θjelo]). It must be scored against the
Castilian wikipron gold, not the Latin-American one, which has seseo
(⟨cielo⟩ -> [sjelo]) and belongs to ``es-419`` instead.

``hyw`` (Western Armenian) has a spec but was never wired to its wikipron
gold; ``hy`` (Eastern Armenian) already is.

These assert the phonological fact as well as the wiring. A test that
only checked the filename would pass just as happily with the two
Spanish golds swapped back, which is exactly how the mismatch survived:
``benchmark`` rows record the tag a dataset was registered under, and the
registry resolves that tag to a different spec than the reader expects.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402

from orthography2ipa import get  # noqa: E402


def test_es_resolves_to_a_distincion_spec():
    spec = get("es")
    assert spec.code == "es-ES"
    assert spec.graphemes["z"] == ["θ"]


def test_es_is_wired_to_the_castilian_gold():
    assert benchmark._WIKIPRON_FILES["es"] == "spa_latn_ca_broad.tsv"


def test_es_419_is_wired_to_the_latin_american_gold():
    assert benchmark._WIKIPRON_FILES["es-419"] == "spa_latn_la_broad.tsv"


def test_es_419_spec_models_seseo():
    spec = get("es-419")
    assert spec.graphemes["z"] == ["s"]


def test_hyw_is_wired_to_the_western_armenian_gold():
    assert benchmark._WIKIPRON_FILES["hyw"] == "hye_armn_w_broad.tsv"


def test_hy_still_wired_to_the_eastern_armenian_gold():
    assert benchmark._WIKIPRON_FILES["hy"] == "hye_armn_e_broad.tsv"


def test_hyw_spec_voices_the_classical_voiceless_series():
    # Classical ⟨տ⟩, voiceless [t] in Eastern Armenian, is voiced [d] in
    # Western Armenian — the textbook consonant-shift correspondence.
    spec = get("hyw")
    assert spec.graphemes["տ"] == ["d"]
