"""Tests for ``load_wikipron_ar_diacritized`` in scripts/benchmark.py.

The loader restores tashkeel on the INPUT side of the WikiPron Arabic
gold (same gold IPA), strips word-final harakat (pausal forms), caches
the result, and is registered with a provenance tier. ``text2tashkeel``
is mocked via ``sys.modules`` so these run offline, deterministically,
and without the optional dependency installed — mirroring
tests/test_pt_gold_loaders.py's network mocking.
"""
import os
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


_RAW = [("كتاب", "k i t aː b"), ("قمر", "q a m a r")]

#: what the fake diacritizer returns — includes a word-FINAL kasra on the
#: first word (an iʿrāb case ending the loader must strip) and a MEDIAL
#: sukun/fatha on the second (which must survive).
_DIA = {"كتاب": "كِتَابِ", "قمر": "قَمْر"}


class _FakeDiacritizer:
    def diacritize(self, word):
        return _DIA[word]


def _install_fake_text2tashkeel(monkeypatch):
    mod = types.ModuleType("text2tashkeel")
    mod.Diacritizer = _FakeDiacritizer
    monkeypatch.setitem(sys.modules, "text2tashkeel", mod)


def _patch_raw_gold(monkeypatch):
    monkeypatch.setattr(
        benchmark, "load_wikipron", lambda lang, limit: _RAW[:limit])


def test_diacritizes_input_keeps_gold_and_strips_final_harakat(
        monkeypatch, tmp_path):
    _install_fake_text2tashkeel(monkeypatch)
    _patch_raw_gold(monkeypatch)
    monkeypatch.setattr(benchmark, "CACHE_DIR", str(tmp_path))
    pairs = benchmark.load_wikipron_ar_diacritized("ar", 10)
    # final kasra stripped, medial harakat kept, gold IPA untouched
    assert pairs == [("كِتَاب", "k i t aː b"), ("قَمْر", "q a m a r")]


def test_cache_file_is_written_and_reused(monkeypatch, tmp_path):
    _install_fake_text2tashkeel(monkeypatch)
    _patch_raw_gold(monkeypatch)
    monkeypatch.setattr(benchmark, "CACHE_DIR", str(tmp_path))
    benchmark.load_wikipron_ar_diacritized("ar", 10)
    cache = tmp_path / "wikipron_ar_diacritized.tsv"
    assert cache.exists()
    # a second call must read the cache, not re-diacritize: poison the
    # diacritizer so any re-run would blow up
    bad = types.ModuleType("text2tashkeel")

    class _Boom:
        def diacritize(self, word):
            raise AssertionError("re-diacritized despite cache")
    bad.Diacritizer = _Boom
    monkeypatch.setitem(sys.modules, "text2tashkeel", bad)
    pairs = benchmark.load_wikipron_ar_diacritized("ar", 1)
    assert pairs == [("كِتَاب", "k i t aː b")]


def test_registered_with_provenance():
    loader, langs = benchmark.DATASETS["wikipron_ar_diacritized"]
    assert loader is benchmark.load_wikipron_ar_diacritized
    assert langs == ["ar"]
    # same gold tier as the raw row: the input transform adds a machine
    # noise floor but the gold itself is still crowd-scraped Wiktionary
    assert benchmark.PROVENANCE["wikipron_ar_diacritized"] == "crowd-scraped"


def test_strip_final_harakat_only_strips_trailing():
    assert benchmark._strip_final_harakat("كِتَابِ") == "كِتَاب"
    assert benchmark._strip_final_harakat("قَمْر") == "قَمْر"
    # tanwin at the end goes too
    assert benchmark._strip_final_harakat("كِتَابٌ") == "كِتَاب"
