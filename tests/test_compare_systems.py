"""Tests for scripts/compare_systems.py.

All comparison systems are mocked — no network, no real espeak-ng,
epitran, or gruut required. Covers the PER math, the "beats espeak"
tally, and the "unavailable system -> n/a, never a crash" contract.
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import compare_systems as cs  # noqa: E402


class FakeEngine:
    """Stands in for orthography2ipa.G2P: deterministic word -> IPA map."""

    def __init__(self, table):
        self.table = table

    def transcribe_word(self, word):
        if word not in self.table:
            raise KeyError(word)
        return self.table[word]


class TestScoreHelper:
    def test_per_zero_on_exact_match(self):
        per, covered = cs._score([("ola", ["ola"])])
        assert per == 0.0
        assert covered == 1

    def test_per_averages_across_rows(self):
        # "ola" vs "ola" -> 0 edits / len 3 == 0.0
        # "kasa" vs "kaza" -> 1 edit / len 4 == 0.25
        per, covered = cs._score([
            ("ola", ["ola"]),
            ("kasa", ["kaza"]),
        ])
        assert covered == 2
        assert per == pytest.approx((0.0 + 0.25) / 2)

    def test_none_hypothesis_excluded_from_coverage(self):
        per, covered = cs._score([
            ("ola", ["ola"]),
            (None, ["kaza"]),
        ])
        assert covered == 1
        assert per == 0.0

    def test_all_none_yields_none_per(self):
        per, covered = cs._score([(None, ["ola"]), (None, ["kaza"])])
        assert per is None
        assert covered == 0

    def test_best_of_multiple_gold_variants(self):
        # gold has two dialect variants; the closer one wins
        per, covered = cs._score([("kasa", ["kaza", "kasa"])])
        assert per == 0.0
        assert covered == 1


class TestEspeakAvailability:
    def test_unavailable_yields_none_not_crash(self, monkeypatch):
        monkeypatch.setattr(cs.shutil, "which", lambda _: None)
        assert cs.espeak_available() is False

    def test_transcribe_returns_none_on_missing_binary(self, monkeypatch):
        def fake_run(*a, **k):
            raise FileNotFoundError("no such binary")
        monkeypatch.setattr(cs.subprocess, "run", fake_run)
        assert cs.espeak_transcribe("ola", "es") is None

    def test_transcribe_returns_none_on_nonzero_exit(self, monkeypatch):
        class Proc:
            returncode = 1
            stdout = ""
            stderr = "boom"
        monkeypatch.setattr(cs.subprocess, "run", lambda *a, **k: Proc())
        assert cs.espeak_transcribe("ola", "es") is None

    def test_transcribe_parses_stdout(self, monkeypatch):
        class Proc:
            returncode = 0
            stdout = "ˈola\n"
            stderr = ""
        monkeypatch.setattr(cs.subprocess, "run", lambda *a, **k: Proc())
        assert cs.espeak_transcribe("ola", "es") == "ˈola"


class TestEpitranLazyImport:
    def test_absent_module_yields_none(self, monkeypatch):
        # simulate epitran not being installed: importing it raises
        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **k):
            if name == "epitran":
                raise ImportError("no module named epitran")
            return real_import(name, *a, **k)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        cs._epitran_cache.clear()
        assert cs.epitran_transcribe("hola", "spa-Latn") is None


class TestGruutLazyImport:
    def test_absent_module_yields_none(self, monkeypatch):
        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **k):
            if name == "gruut":
                raise ImportError("no module named gruut")
            return real_import(name, *a, **k)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        assert cs.gruut_transcribe("hola", "es") is None


class TestCompareLang:
    def test_mocked_systems_score_correctly_and_tally_wins(
            self, monkeypatch):
        # gold: two words, one gold each
        pairs = [("ola", "ola"), ("kasa", "kaza")]
        monkeypatch.setitem(
            cs.benchmark.DATASETS, "fake_dataset",
            (lambda lang, limit: pairs, ["xx"]))
        monkeypatch.setitem(
            cs.LANGS, "xx",
            {"dataset": ("fake_dataset", "xx"), "espeak": "xx",
             "epitran": "xxx-Latn", "gruut": "xx"})

        # o2i: perfect on both words -> PER 0.0
        fake_o2i = FakeEngine({"ola": "ola", "kasa": "kaza"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        # espeak: gets one wrong -> PER > 0, worse than o2i
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        espeak_table = {"ola": "ola", "kasa": "kasa"}
        monkeypatch.setattr(
            cs, "espeak_transcribe",
            lambda word, voice: espeak_table.get(word))

        # epitran: unavailable
        monkeypatch.setattr(cs, "epitran_transcribe", lambda word, code: None)
        # gruut: unavailable
        monkeypatch.setattr(cs, "gruut_transcribe", lambda word, lang: None)

        row = cs.compare_lang("xx", limit=10)

        assert row["lang"] == "xx"
        assert row["n"] == 2
        assert row["o2i_per"] == 0.0
        assert row["espeak_per"] == pytest.approx(0.25 / 2)
        assert row["epitran_per"] is None
        assert row["gruut_per"] is None

    def test_no_espeak_mapping_yields_none(self, monkeypatch):
        pairs = [("ola", "ola")]
        monkeypatch.setitem(
            cs.benchmark.DATASETS, "fake_dataset2",
            (lambda lang, limit: pairs, ["yy"]))
        monkeypatch.setitem(
            cs.LANGS, "yy",
            {"dataset": ("fake_dataset2", "yy"), "espeak": None,
             "epitran": None, "gruut": None})

        fake_o2i = FakeEngine({"ola": "ola"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        row = cs.compare_lang("yy", limit=10)
        assert row["espeak_per"] is None
        assert row["epitran_per"] is None
        assert row["gruut_per"] is None
        assert row["o2i_per"] == 0.0

    def test_o2i_exception_excluded_gracefully(self, monkeypatch):
        pairs = [("ola", "ola")]
        monkeypatch.setitem(
            cs.benchmark.DATASETS, "fake_dataset3",
            (lambda lang, limit: pairs, ["zz"]))
        monkeypatch.setitem(
            cs.LANGS, "zz",
            {"dataset": ("fake_dataset3", "zz"), "espeak": None,
             "epitran": None, "gruut": None})

        class RaisingEngine:
            def transcribe_word(self, word):
                raise RuntimeError("boom")

        class FakeModule:
            G2P = staticmethod(lambda lang: RaisingEngine())
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        row = cs.compare_lang("zz", limit=10)
        assert row["o2i_per"] is None
        assert row["o2i_n"] == 0


class TestBuildAndWriteComparison(object):
    def test_beats_espeak_tally_and_write(self, tmp_path, monkeypatch):
        rows = [
            {"lang": "aa", "dataset": "d", "n": 2,
             "o2i_per": 0.1, "o2i_n": 2,
             "espeak_per": 0.3, "espeak_n": 2,
             "epitran_per": None, "epitran_n": 0,
             "gruut_per": None, "gruut_n": 0,
             "harness_version": "1.0", "limit": 10},
            {"lang": "bb", "dataset": "d", "n": 2,
             "o2i_per": 0.4, "o2i_n": 2,
             "espeak_per": 0.2, "espeak_n": 2,
             "epitran_per": 0.5, "epitran_n": 2,
             "gruut_per": None, "gruut_n": 0,
             "harness_version": "1.0", "limit": 10},
            {"lang": "cc", "dataset": "d", "n": 1,
             "o2i_per": 0.2, "o2i_n": 1,
             "espeak_per": None, "espeak_n": 0,
             "epitran_per": None, "epitran_n": 0,
             "gruut_per": None, "gruut_n": 0,
             "harness_version": "1.0", "limit": 10},
        ]
        md_path = tmp_path / "comparison.md"
        json_path = tmp_path / "comparison.json"
        monkeypatch.setattr(cs, "COMPARISON_MD", str(md_path))
        monkeypatch.setattr(cs, "COMPARISON_JSON", str(json_path))

        cs.write_comparison(rows)

        text = md_path.read_text(encoding="utf-8")
        # aa wins (0.1 < 0.3), bb loses (0.4 > 0.2); cc not comparable
        assert "o2i beats espeak on 1 of 2 comparable languages" in text
        assert "| bb |" in text  # honest: the losing row is still listed
        assert "n/a" in text  # missing systems reported as n/a

        data = json_path.read_text(encoding="utf-8")
        assert '"lang": "aa"' in data

    def test_no_comparable_languages_does_not_crash(self, tmp_path,
                                                      monkeypatch):
        rows = [
            {"lang": "aa", "dataset": "d", "n": 1,
             "o2i_per": 0.1, "o2i_n": 1,
             "espeak_per": None, "espeak_n": 0,
             "epitran_per": None, "epitran_n": 0,
             "gruut_per": None, "gruut_n": 0,
             "harness_version": "1.0", "limit": 10},
        ]
        md_path = tmp_path / "comparison.md"
        json_path = tmp_path / "comparison.json"
        monkeypatch.setattr(cs, "COMPARISON_MD", str(md_path))
        monkeypatch.setattr(cs, "COMPARISON_JSON", str(json_path))

        cs.write_comparison(rows)
        text = md_path.read_text(encoding="utf-8")
        assert "No languages were comparable" in text
