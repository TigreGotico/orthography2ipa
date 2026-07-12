"""Tests for scripts/benchmark.py's load_hitz_basque loader (the
HiTZ/wikipedia_basque_ipa gold source for the ``eu`` benchmark).

Network access is mocked out via benchmark._fetch so these run offline
and deterministically, mirroring how the other loaders would be tested.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


def _rows_page(rows):
    return json.dumps({
        "rows": [{"row": row} for row in rows],
    })


def test_load_hitz_basque_extracts_word_ipa_pairs(monkeypatch):
    page = _rows_page([
        {
            "text": "Historiako lehenengo zientzia izan da astronomia.",
            "phonemes": "'istoɾiako le'enenɡo ʂi'entʂia iʂ'an da astr'onomia.",
        },
    ])
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: page)

    pairs = benchmark.load_hitz_basque("eu", 10)

    assert ("Historiako", "ˈistoɾiako") in pairs
    assert ("da", "da") in pairs
    words = [w for w, _ in pairs]
    assert "." not in "".join(w for _, w in pairs)


def test_load_hitz_basque_normalizes_apostrophe_stress(monkeypatch):
    page = _rows_page([
        {"text": "izan", "phonemes": "iʂ'an"},
    ])
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: page)

    pairs = benchmark.load_hitz_basque("eu", 5)

    assert pairs == [("izan", "iʂˈan")]


def test_load_hitz_basque_deduplicates_and_respects_limit(monkeypatch):
    page = _rows_page([
        {"text": "eta eta eta", "phonemes": "eta eta eta"},
        {"text": "beste", "phonemes": "b'este"},
    ])
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: page)

    pairs = benchmark.load_hitz_basque("eu", 1)

    assert pairs == [("eta", "eta")]


def test_load_hitz_basque_skips_misaligned_paragraphs(monkeypatch):
    page = _rows_page([
        # word/phoneme token counts differ -> paragraph is skipped
        {"text": "bat bi hiru", "phonemes": "bat bi"},
        {"text": "lau", "phonemes": "law"},
    ])
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: page)

    pairs = benchmark.load_hitz_basque("eu", 5)

    assert pairs == [("lau", "law")]


def test_hitz_basque_registered_in_datasets():
    assert "hitz_basque_ipa" in benchmark.DATASETS
    loader, langs = benchmark.DATASETS["hitz_basque_ipa"]
    assert loader is benchmark.load_hitz_basque
    assert langs == ["eu"]
    # additive to, not a replacement of, the existing eu wikipron gold
    wikipron_loader, wikipron_langs = benchmark.DATASETS["wikipron"]
    assert "eu" in wikipron_langs
