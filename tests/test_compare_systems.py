"""Tests for scripts/compare_systems.py.

All comparison systems are mocked — no network, no real espeak-ng,
epitran, gruut, pycotovia, or ahotts-g2p required. Covers the PER math, the
"beats espeak" tally, the "unavailable system -> n/a, never a crash"
contract, and the Catalan-dialect espeak voice discovery/fallback logic.
"""
import json
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
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_dataset": (lambda lang, limit: pairs, ["xx"])})
        monkeypatch.setitem(
            cs.LANGS, "xx",
            {"dataset": ("fake_dataset", "xx"), "espeak": "xx",
             "epitran": "xxx-Latn", "gruut": "xx"})

        # o2i: perfect on both words -> PER 0.0
        fake_o2i = FakeEngine({"ola": "ola", "kasa": "kaza"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        # espeak: gets one wrong -> PER > 0, worse than o2i
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        espeak_table = {"ola": "ola", "kasa": "kasa"}
        monkeypatch.setattr(
            cs, "espeak_transcribe",
            lambda word, voice, data_path=None: espeak_table.get(word))

        # epitran: unavailable
        monkeypatch.setattr(cs, "epitran_transcribe", lambda word, code: None)
        # gruut: unavailable
        monkeypatch.setattr(cs, "gruut_transcribe", lambda word, lang: None)

        row = cs.compare_lang("xx", limit=10)[0]

        assert row["lang"] == "xx"
        assert row["n"] == 2
        assert row["o2i_per"] == 0.0
        assert row["espeak_per"] == pytest.approx(0.25 / 2)
        assert row["epitran_per"] is None
        assert row["gruut_per"] is None

    def test_no_espeak_mapping_yields_none(self, monkeypatch):
        pairs = [("ola", "ola")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_dataset2": (lambda lang, limit: pairs, ["yy"])})
        monkeypatch.setitem(
            cs.LANGS, "yy",
            {"dataset": ("fake_dataset2", "yy"), "espeak": None,
             "epitran": None, "gruut": None})

        fake_o2i = FakeEngine({"ola": "ola"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        row = cs.compare_lang("yy", limit=10)[0]
        assert row["espeak_per"] is None
        assert row["epitran_per"] is None
        assert row["gruut_per"] is None
        assert row["o2i_per"] == 0.0

    def test_o2i_exception_excluded_gracefully(self, monkeypatch):
        pairs = [("ola", "ola")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_dataset3": (lambda lang, limit: pairs, ["zz"])})
        monkeypatch.setitem(
            cs.LANGS, "zz",
            {"dataset": ("fake_dataset3", "zz"), "espeak": None,
             "epitran": None, "gruut": None})

        class RaisingEngine:
            def transcribe_word(self, word):
                raise RuntimeError("boom")

        class FakeModule:
            G2P = staticmethod(lambda lang: RaisingEngine())
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        row = cs.compare_lang("zz", limit=10)[0]
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
             "provenance_tier": "crowd-scraped",
             "harness_version": "1.0", "limit": 10},
            {"lang": "bb", "dataset": "d", "n": 2,
             "o2i_per": 0.4, "o2i_n": 2,
             "espeak_per": 0.2, "espeak_n": 2,
             "epitran_per": 0.5, "epitran_n": 2,
             "gruut_per": None, "gruut_n": 0,
             "provenance_tier": "crowd-scraped",
             "harness_version": "1.0", "limit": 10},
            {"lang": "cc", "dataset": "d", "n": 1,
             "o2i_per": 0.2, "o2i_n": 1,
             "espeak_per": None, "espeak_n": 0,
             "epitran_per": None, "epitran_n": 0,
             "gruut_per": None, "gruut_n": 0,
             "provenance_tier": "crowd-scraped",
             "harness_version": "1.0", "limit": 10},
        ]
        for lang in ("aa", "bb", "cc"):
            monkeypatch.setitem(cs.LANGS, lang, {"dataset": ("d", lang)})
        md_path = tmp_path / "comparison.md"
        json_path = tmp_path / "comparison.json"
        monkeypatch.setattr(cs, "COMPARISON_MD", str(md_path))
        monkeypatch.setattr(cs, "COMPARISON_JSON", str(json_path))

        cs.write_comparison(rows)

        text = md_path.read_text(encoding="utf-8")
        # aa wins (0.1 < 0.3), bb loses (0.4 > 0.2); cc not comparable.
        # All three rows are each lang's own primary/only dataset and are
        # crowd-scraped (gold-tier), so they land in the gold-tier count.
        assert "Gold-tier" in text
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
             "provenance_tier": "crowd-scraped",
             "harness_version": "1.0", "limit": 10},
        ]
        monkeypatch.setitem(cs.LANGS, "aa", {"dataset": ("d", "aa")})
        md_path = tmp_path / "comparison.md"
        json_path = tmp_path / "comparison.json"
        monkeypatch.setattr(cs, "COMPARISON_MD", str(md_path))
        monkeypatch.setattr(cs, "COMPARISON_JSON", str(json_path))

        cs.write_comparison(rows)
        text = md_path.read_text(encoding="utf-8")
        assert "no language's primary gold was espeak-comparable" in text


class TestPycotoviaLazyImport:
    def test_absent_module_yields_none(self, monkeypatch):
        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **k):
            if name == "pycotovia":
                raise ImportError("no module named pycotovia")
            return real_import(name, *a, **k)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        assert cs.pycotovia_transcribe("ola", "gl") is None

    def test_present_module_phonemizes_and_converts_to_ipa(self, monkeypatch):
        class FakePycotovia:
            @staticmethod
            def phonemize(word, lang="gl"):
                assert lang == "gl"
                return "raw-cotovia-form"

            @staticmethod
            def cotovia_to_ipa(raw):
                assert raw == "raw-cotovia-form"
                return "ˈola"

        monkeypatch.setitem(sys.modules, "pycotovia", FakePycotovia)
        assert cs.pycotovia_transcribe("ola", "gl") == "ˈola"

    def test_exception_during_transcription_yields_none(self, monkeypatch):
        class FakePycotovia:
            @staticmethod
            def phonemize(word, lang="gl"):
                raise RuntimeError("boom")

            @staticmethod
            def cotovia_to_ipa(raw):
                return raw

        monkeypatch.setitem(sys.modules, "pycotovia", FakePycotovia)
        assert cs.pycotovia_transcribe("ola", "gl") is None


class TestAhottsUnfoldToIpa:
    """The StyleTTS2 single-char folds (uppercase affricates/aspirates/
    stressed vowels) MUST unfold to standard IPA before scoring, so
    ahotts-g2p is compared in the same IPA space as every other system.
    Uses a fake ``ahotts_g2p.phones`` module so no real install/network
    is required."""

    @pytest.fixture(autouse=True)
    def _fake_multi(self, monkeypatch):
        import types
        # mirrors ahotts_g2p.phones.MULTI (IPA sequence -> folded char)
        fake_phones = types.ModuleType("ahotts_g2p.phones")
        fake_phones.MULTI = {
            "tʃ": "C", "ts": "V", "tʂ": "P",
            "'i": "I", "'e": "E", "'a": "A", "'o": "O", "'u": "U",
            "pʰ": "H", "kʰ": "K", "tʰ": "T",
        }
        fake_pkg = types.ModuleType("ahotts_g2p")
        fake_pkg.phones = fake_phones
        monkeypatch.setitem(sys.modules, "ahotts_g2p", fake_pkg)
        monkeypatch.setitem(sys.modules, "ahotts_g2p.phones", fake_phones)
        cs._ahotts_unfold_cache.clear()
        yield
        cs._ahotts_unfold_cache.clear()

    def test_stressed_vowels_unfold_with_ipa_stress_mark(self):
        # 'kajʃO' -> 'kajʃˈo' (O is folded stressed /o/, not a distinct phone)
        assert cs.ahotts_unfold_to_ipa("kajʃO") == "kajʃˈo"

    def test_affricate_and_stressed_vowel_unfold(self):
        # 'eCEa' -> 'etʃˈea'
        assert cs.ahotts_unfold_to_ipa("eCEa") == "etʃˈea"

    def test_plain_ipa_chars_pass_through_unchanged(self):
        assert cs.ahotts_unfold_to_ipa("mund") == "mund"

    def test_unfold_stress_mark_is_stripped_by_shared_normalize(self):
        # end-to-end fairness: after unfold, the shared normalize strips
        # the ˈ so a folded stressed vowel scores like a plain one.
        ipa = cs.ahotts_unfold_to_ipa("mundUa")  # -> 'mundˈua'
        assert ipa == "mundˈua"
        assert cs.benchmark.normalize(ipa, True, True) == "mundua"


class TestAhottsTranscribe:
    def test_absent_module_yields_none(self, monkeypatch):
        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **k):
            if name == "ahotts_g2p":
                raise ImportError("no module named ahotts_g2p")
            return real_import(name, *a, **k)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        assert cs.ahotts_transcribe("kaixo", {"lang": "eu",
                                              "version": "classic"}) is None

    def test_present_module_phonemizes_and_unfolds(self, monkeypatch):
        import types
        fake_phones = types.ModuleType("ahotts_g2p.phones")
        fake_phones.MULTI = {"tʃ": "C", "'o": "O", "'a": "A", "'e": "E",
                             "'i": "I", "'u": "U"}
        fake_pkg = types.ModuleType("ahotts_g2p")
        fake_pkg.phones = fake_phones

        def fake_phonemize(word, lang="eu", version="modern"):
            assert (word, lang, version) == ("kaixo", "eu", "classic")
            return "kajʃO"
        fake_pkg.phonemize = fake_phonemize

        monkeypatch.setitem(sys.modules, "ahotts_g2p", fake_pkg)
        monkeypatch.setitem(sys.modules, "ahotts_g2p.phones", fake_phones)
        cs._ahotts_unfold_cache.clear()

        out = cs.ahotts_transcribe("kaixo", {"lang": "eu",
                                             "version": "classic"})
        assert out == "kajʃˈo"
        cs._ahotts_unfold_cache.clear()

    def test_exception_during_phonemize_yields_none(self, monkeypatch):
        import types
        fake_pkg = types.ModuleType("ahotts_g2p")

        def boom(word, lang="eu", version="modern"):
            raise RuntimeError("boom")
        fake_pkg.phonemize = boom
        monkeypatch.setitem(sys.modules, "ahotts_g2p", fake_pkg)
        assert cs.ahotts_transcribe("x", {"lang": "eu",
                                          "version": "classic"}) is None


class TestCompareLangWithPycotoviaAndAhotts:
    def test_gl_row_scores_pycotovia_and_leaves_ahotts_absent(
            self, monkeypatch):
        pairs = [("ola", "ola")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_gl_dataset": (lambda lang, limit: pairs, ["gl"])})
        monkeypatch.setitem(
            cs.LANGS, "gl",
            {"dataset": ("fake_gl_dataset", "gl"), "espeak": None,
             "epitran": None, "gruut": None, "pycotovia": "gl"})

        fake_o2i = FakeEngine({"ola": "ola"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(
            cs, "pycotovia_transcribe", lambda word, lang: "ola")

        row = cs.compare_lang("gl", limit=10)[0]
        assert row["pycotovia_per"] == 0.0
        assert row["pycotovia_n"] == 1
        assert row["ahotts_per"] is None
        assert row["ahotts_n"] == 0

    def test_eu_row_scores_ahotts_and_records_version(self, monkeypatch):
        # gold 'kaiʃo'; ahotts (mocked) returns unfolded 'kajʃˈo' ->
        # normalize -> 'kajʃo' vs 'kaiʃo' == 1 edit / 5 == 0.2
        pairs = [("kaixo", "kaiʃo")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_eu_dataset": (lambda lang, limit: pairs, ["eu"])})
        monkeypatch.setitem(
            cs.LANGS, "eu",
            {"dataset": ("fake_eu_dataset", "eu"), "espeak": None,
             "epitran": None, "gruut": None,
             "ahotts": {"lang": "eu", "version": "classic"}})

        fake_o2i = FakeEngine({"kaixo": "kaiʃo"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(
            cs, "ahotts_transcribe", lambda word, cfg: "kajʃˈo")

        row = cs.compare_lang("eu", limit=10)[0]
        assert row["o2i_per"] == 0.0
        assert row["ahotts_per"] == pytest.approx(0.2)
        assert row["ahotts_n"] == 1
        assert row["ahotts_version"] == "classic"
        assert row["pycotovia_per"] is None

    def test_g2p_override_drives_named_spec_for_alt_dataset_row(
            self, monkeypatch):
        # eu-wikipron-style row: distinct key, but g2p override selects
        # the real "eu" spec.
        pairs = [("bat", "bat")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_euw_dataset": (lambda lang, limit: pairs, ["eu"])})
        monkeypatch.setitem(
            cs.LANGS, "eu-wikipron",
            {"dataset": ("fake_euw_dataset", "eu"), "g2p": "eu",
             "espeak": None, "epitran": None, "gruut": None})

        seen = {}

        class FakeModule:
            @staticmethod
            def G2P(lang):
                seen["lang"] = lang
                return FakeEngine({"bat": "bat"})
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        row = cs.compare_lang("eu-wikipron", limit=10)[0]
        assert seen["lang"] == "eu"  # g2p override, not the row key
        assert row["lang"] == "eu-wikipron"
        assert row["o2i_per"] == 0.0


class TestAfricaG2pLazyImport:
    def test_absent_module_yields_none(self, monkeypatch):
        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **k):
            if name == "africa_g2p":
                raise ImportError("no module named africa_g2p")
            return real_import(name, *a, **k)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        cs._africa_pipeline_cache.clear()
        assert cs.africa_g2p_transcribe("azul", "kab") is None

    def test_present_module_runs_pipeline(self, monkeypatch):
        class FakePipeline:
            def __init__(self, lang, output):
                assert output == "ipa"
                self.lang = lang

            def run(self, word):
                return f"ipa-{word}-{self.lang}"

        fake_pkg = type(sys)("africa_g2p")
        fake_pkg.AfricaPipeline = FakePipeline
        monkeypatch.setitem(sys.modules, "africa_g2p", fake_pkg)
        cs._africa_pipeline_cache.clear()

        assert cs.africa_g2p_transcribe("azul", "kab") == "ipa-azul-kab"
        cs._africa_pipeline_cache.clear()

    def test_unknown_lang_construction_failure_yields_none(self, monkeypatch):
        class FailingPipeline:
            def __init__(self, lang, output):
                raise KeyError(lang)

        fake_pkg = type(sys)("africa_g2p")
        fake_pkg.AfricaPipeline = FailingPipeline
        monkeypatch.setitem(sys.modules, "africa_g2p", fake_pkg)
        cs._africa_pipeline_cache.clear()

        assert cs.africa_g2p_transcribe("x", "zzz") is None
        cs._africa_pipeline_cache.clear()

    def test_exception_during_run_yields_none(self, monkeypatch):
        class BoomPipeline:
            def __init__(self, lang, output):
                pass

            def run(self, word):
                raise RuntimeError("boom")

        fake_pkg = type(sys)("africa_g2p")
        fake_pkg.AfricaPipeline = BoomPipeline
        monkeypatch.setitem(sys.modules, "africa_g2p", fake_pkg)
        cs._africa_pipeline_cache.clear()

        assert cs.africa_g2p_transcribe("x", "kab") is None
        cs._africa_pipeline_cache.clear()


class TestCompareLangWithAfricaG2p:
    def test_kab_row_scores_africa_g2p(self, monkeypatch):
        pairs = [("azul", "azul")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_kab_dataset": (lambda lang, limit: pairs, ["kab"])})
        monkeypatch.setitem(
            cs.LANGS, "kab",
            {"dataset": ("fake_kab_dataset", "kab"), "espeak": None,
             "epitran": None, "gruut": None, "africa_g2p": "kab"})

        fake_o2i = FakeEngine({"azul": "azul"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(
            cs, "africa_g2p_transcribe", lambda word, lang: "azul")

        row = cs.compare_lang("kab", limit=10)[0]
        assert row["africa_g2p_per"] == 0.0
        assert row["africa_g2p_n"] == 1

    def test_no_africa_g2p_mapping_yields_none(self, monkeypatch):
        pairs = [("ola", "ola")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_no_afg2p_dataset": (lambda lang, limit: pairs, ["ww"])})
        monkeypatch.setitem(
            cs.LANGS, "ww",
            {"dataset": ("fake_no_afg2p_dataset", "ww"), "espeak": None,
             "epitran": None, "gruut": None})

        fake_o2i = FakeEngine({"ola": "ola"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        row = cs.compare_lang("ww", limit=10)[0]
        assert row["africa_g2p_per"] is None
        assert row["africa_g2p_n"] == 0


class TestDiscoverCatalanDialectVoices:
    def test_all_bsc_dialect_voices_present(self, monkeypatch):
        monkeypatch.setattr(cs, "espeak_available", lambda: True)

        class Proc:
            returncode = 0
            stderr = ""
            stdout = (
                "Pty Language       Age/Gender VoiceName          File\n"
                " 5  ca              --/M      Catalan            roa/ca\n"
                " 5  ca-ba           --/M      Catalan_(Balearic) roa/ca-ba\n"
                " 5  ca-nw           --/M      Catalan_(NW)       roa/ca-nw\n"
                " 5  ca-va           --/M      Catalan_(Valencian) roa/ca-va\n"
            )
        monkeypatch.setattr(cs.subprocess, "run", lambda *a, **k: Proc())

        voices = cs.discover_catalan_dialect_voices()
        assert voices == {
            "ca": "ca", "ca-x-balear": "ca-ba",
            "ca-x-occidental": "ca-nw", "ca-x-valencia": "ca-va",
        }

    def test_missing_dialect_voices_fall_back_to_generic_ca(
            self, monkeypatch):
        monkeypatch.setattr(cs, "espeak_available", lambda: True)

        class Proc:
            returncode = 0
            stderr = ""
            stdout = (
                "Pty Language       Age/Gender VoiceName          File\n"
                " 5  ca              --/M      Catalan            roa/ca\n"
            )
        monkeypatch.setattr(cs.subprocess, "run", lambda *a, **k: Proc())

        voices = cs.discover_catalan_dialect_voices()
        assert voices["ca"] == "ca"
        assert voices["ca-x-balear"] == "ca"
        assert voices["ca-x-occidental"] == "ca"
        assert voices["ca-x-valencia"] == "ca"

    def test_no_catalan_voice_at_all_yields_none(self, monkeypatch):
        monkeypatch.setattr(cs, "espeak_available", lambda: True)

        class Proc:
            returncode = 0
            stderr = ""
            stdout = "Pty Language       Age/Gender VoiceName          File\n"
        monkeypatch.setattr(cs.subprocess, "run", lambda *a, **k: Proc())

        voices = cs.discover_catalan_dialect_voices()
        assert all(v is None for v in voices.values())

    def test_espeak_unavailable_yields_all_none(self, monkeypatch):
        monkeypatch.setattr(cs, "espeak_available", lambda: False)
        voices = cs.discover_catalan_dialect_voices()
        assert all(v is None for v in voices.values())

    def test_apply_catalan_dialect_voices_mutates_langs_espeak_field(
            self, monkeypatch):
        monkeypatch.setattr(
            cs, "discover_catalan_dialect_voices",
            lambda: {"ca": "ca", "ca-x-balear": "ca",
                     "ca-x-occidental": None, "ca-x-valencia": "ca-va"})
        langs = {
            "ca": {"espeak": "placeholder"},
            "ca-x-balear": {"espeak": "placeholder"},
            "ca-x-occidental": {"espeak": "placeholder"},
            "ca-x-valencia": {"espeak": "placeholder"},
        }
        voices = cs.apply_catalan_dialect_voices(langs)
        assert langs["ca"]["espeak"] == "ca"
        assert langs["ca-x-balear"]["espeak"] == "ca"
        assert langs["ca-x-occidental"]["espeak"] is None
        assert langs["ca-x-valencia"]["espeak"] == "ca-va"
        assert voices["ca-x-valencia"] == "ca-va"


class TestCatalanDialectTableSection:
    def test_lines_report_dialect_specific_voices_when_all_found(self):
        rows = [
            {"lang": "ca", "dataset": "4catac", "n": 160,
             "o2i_per": 0.41, "espeak_per": 0.18},
            {"lang": "ca-x-balear", "dataset": "4catac", "n": 160,
             "o2i_per": 0.38, "espeak_per": 0.21},
            {"lang": "ca-x-occidental", "dataset": "4catac", "n": 160,
             "o2i_per": 0.56, "espeak_per": 0.19},
            {"lang": "ca-x-valencia", "dataset": "4catac", "n": 160,
             "o2i_per": 0.30, "espeak_per": 0.18},
        ]
        voices = {"ca": "ca", "ca-x-balear": "ca-ba",
                  "ca-x-occidental": "ca-nw", "ca-x-valencia": "ca-va"}
        lines = cs._catalan_dialect_table_lines(rows, voices)
        text = "\n".join(lines)
        assert "All three BSC dialect voices" in text
        assert "| balear | ca-x-balear | ca-ba | 160 | 0.3800 | 0.2100 |" in text
        assert "fallback" not in text

    def test_lines_report_fallback_honestly_when_voice_missing(self):
        rows = [
            {"lang": "ca", "dataset": "4catac", "n": 160,
             "o2i_per": 0.41, "espeak_per": 0.18},
            {"lang": "ca-x-balear", "dataset": "4catac", "n": 160,
             "o2i_per": 0.38, "espeak_per": 0.25},
        ]
        voices = {"ca": "ca", "ca-x-balear": "ca",
                  "ca-x-occidental": None, "ca-x-valencia": None}
        lines = cs._catalan_dialect_table_lines(rows, voices)
        text = "\n".join(lines)
        assert "not** found" in text
        assert "ca (fallback, no dialect voice found)" in text
        assert "| occidental (nord-occidental) | ca-x-occidental | n/a | 0 | n/a | n/a |" in text


class TestEspeakBatchTranscribe:
    """The batched espeak path must never mis-attribute output to the
    wrong word: alignment is positional, checked per chunk, and any
    surprise degrades to the per-word path instead of misaligning."""

    def test_aligned_chunk_maps_words_positionally(self, monkeypatch):
        class P:
            returncode = 0
            stdout = "kasa\n\nporta\n"   # middle word: espeak emitted nothing

        monkeypatch.setattr(cs.subprocess, "run", lambda *a, **k: P())
        out = cs.espeak_batch_transcribe(["casa", "xyz", "porta"], "es")
        assert out == {"casa": "kasa", "xyz": None, "porta": "porta"}

    def test_line_count_mismatch_falls_back_to_per_word(self, monkeypatch):
        class P:
            returncode = 0
            stdout = "only-one-line\n"   # 3 words in, 1 line out

        monkeypatch.setattr(cs.subprocess, "run", lambda *a, **k: P())
        calls = []

        def per_word(word, voice, data_path=None):
            calls.append(word)
            return f"ipa-{word}"

        monkeypatch.setattr(cs, "espeak_transcribe", per_word)
        out = cs.espeak_batch_transcribe(["a", "b", "c"], "es")
        assert calls == ["a", "b", "c"]
        assert out == {"a": "ipa-a", "b": "ipa-b", "c": "ipa-c"}

    def test_subprocess_failure_falls_back_to_per_word(self, monkeypatch):
        def boom(*a, **k):
            raise OSError("espeak exploded")

        monkeypatch.setattr(cs.subprocess, "run", boom)
        monkeypatch.setattr(cs, "espeak_transcribe",
                            lambda w, v, data_path=None: f"ipa-{w}")
        out = cs.espeak_batch_transcribe(["a", "b"], "es")
        assert out == {"a": "ipa-a", "b": "ipa-b"}

    def test_words_are_chunked(self, monkeypatch):
        monkeypatch.setattr(cs, "_ESPEAK_CHUNK", 2)
        inputs = []

        class P:
            returncode = 0

        def fake_run(cmd, *, input, **k):
            words = input.strip().split("\n")
            inputs.append(words)
            p = P()
            p.stdout = "".join(f"ipa-{w}\n" for w in words)
            return p

        monkeypatch.setattr(cs.subprocess, "run", fake_run)
        out = cs.espeak_batch_transcribe(["a", "b", "c"], "es")
        assert inputs == [["a", "b"], ["c"]]
        assert out == {"a": "ipa-a", "b": "ipa-b", "c": "ipa-c"}


class TestMultiwordDispatch:
    """Sentence-level gold (4catac) must go through the utterance API —
    the same rule benchmark.evaluate_words applies since the sentence
    datasets were mis-scored by the word-level call."""

    def test_multiword_entry_uses_transcribe(self, monkeypatch):
        calls = {}

        class FakeG2P:
            def __init__(self, lang): pass
            def transcribe(self, s):
                calls.setdefault("transcribe", []).append(s)
                return "ipa"
            def transcribe_word(self, w):
                calls.setdefault("transcribe_word", []).append(w)
                return "ipa"

        import orthography2ipa
        monkeypatch.setattr(orthography2ipa, "G2P", FakeG2P)
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake": (lambda lang, limit: [("una frase curta", "ipa"),
                                           ("mot", "ipa")], ["xx"])})
        monkeypatch.setitem(
            cs.LANGS, "xx",
            {"dataset": ("fake", "xx"), "espeak": None,
             "epitran": None, "gruut": None})
        try:
            cs.compare_lang("xx", 10)
        finally:
            cs.LANGS.pop("xx", None)
        assert calls["transcribe"] == ["una frase curta"]
        assert calls["transcribe_word"] == ["mot"]


class TestEspeakRulesAvailability:
    def test_unavailable_without_env_var(self, monkeypatch):
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", None)
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        assert cs.espeak_rules_available() is False

    def test_unavailable_when_path_missing(self, monkeypatch, tmp_path):
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH",
                            str(tmp_path / "does-not-exist"))
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        assert cs.espeak_rules_available() is False

    def test_unavailable_when_espeak_missing(self, monkeypatch, tmp_path):
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(tmp_path))
        monkeypatch.setattr(cs, "espeak_available", lambda: False)
        assert cs.espeak_rules_available() is False

    def test_available_when_env_set_and_dir_exists(self, monkeypatch, tmp_path):
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(tmp_path))
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        assert cs.espeak_rules_available() is True


class TestEspeakDataPathPlumbing:
    """The espeak_rules column reuses espeak_transcribe/espeak_batch_transcribe
    with an extra --path=<data_path> flag; these tests assert the flag is
    actually threaded through to the subprocess command, never silently
    dropped (which would make espeak_rules identical to plain espeak)."""

    def test_transcribe_passes_path_flag(self, monkeypatch):
        seen_cmd = {}

        class Proc:
            returncode = 0
            stdout = "ˈɔla\n"

        def fake_run(cmd, **kwargs):
            seen_cmd["cmd"] = cmd
            return Proc()

        monkeypatch.setattr(cs.subprocess, "run", fake_run)
        cs.espeak_transcribe("ola", "es", data_path="/rules/only/data")
        assert "--path=/rules/only/data" in seen_cmd["cmd"]

    def test_transcribe_omits_path_flag_when_none(self, monkeypatch):
        seen_cmd = {}

        class Proc:
            returncode = 0
            stdout = "ˈɔla\n"

        def fake_run(cmd, **kwargs):
            seen_cmd["cmd"] = cmd
            return Proc()

        monkeypatch.setattr(cs.subprocess, "run", fake_run)
        cs.espeak_transcribe("ola", "es")
        assert not any(str(c).startswith("--path=") for c in seen_cmd["cmd"])

    def test_batch_transcribe_passes_path_flag(self, monkeypatch):
        seen_cmd = {}

        class Proc:
            returncode = 0
            stdout = "ˈɔla\n"

        def fake_run(cmd, **kwargs):
            seen_cmd["cmd"] = cmd
            return Proc()

        monkeypatch.setattr(cs.subprocess, "run", fake_run)
        cs.espeak_batch_transcribe(["ola"], "es", data_path="/rules/only/data")
        assert "--path=/rules/only/data" in seen_cmd["cmd"]


class TestParseEspeakWordlistWords:
    def test_extracts_plain_words_skips_directives_and_comments(self, tmp_path):
        (tmp_path / "en_list").write_text(
            "// a comment line\n"
            "\n"
            "b\tbi:\n"                # single-letter "spell it out" entry: skip
            "_lig\tl,Iga#tS3_\n"      # helper directive: skip
            "?3 z\tzi:\n"             # conditional directive: skip
            "the\tD@2\t$only $nounf\n"  # real function word: keep
            "one\tw02n\t$nounf\n"       # real word: keep
            "à\t$accent $atend\n",     # accented single char + directive only: skip
            encoding="utf-8",
        )
        words = cs._parse_espeak_wordlist_words(str(tmp_path), "en")
        assert words == ["one", "the"]

    def test_merges_list_listx_and_extra(self, tmp_path):
        (tmp_path / "fr_list").write_text("bonjour\tb..\n", encoding="utf-8")
        (tmp_path / "fr_listx").write_text("monsieur\tm..\n", encoding="utf-8")
        (tmp_path / "fr_extra").write_text("madame\tm..\n", encoding="utf-8")
        words = cs._parse_espeak_wordlist_words(str(tmp_path), "fr")
        assert words == ["bonjour", "madame", "monsieur"]

    def test_missing_files_yield_empty_list(self, tmp_path):
        assert cs._parse_espeak_wordlist_words(str(tmp_path), "zz") == []


class TestBuildEspeakLexiconTsv:
    def test_returns_none_without_dictsource_path(self, monkeypatch):
        monkeypatch.setattr(cs, "ESPEAK_DICTSOURCE_PATH", None)
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        assert cs.build_espeak_lexicon_tsv("en") is None

    def test_returns_none_for_unmapped_language(self, monkeypatch, tmp_path):
        monkeypatch.setattr(cs, "ESPEAK_DICTSOURCE_PATH", str(tmp_path))
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        assert cs.build_espeak_lexicon_tsv("zz-not-mapped") is None

    def test_builds_and_caches_tsv(self, monkeypatch, tmp_path):
        dictsource = tmp_path / "dictsource"
        dictsource.mkdir()
        (dictsource / "en_list").write_text(
            "the\tD@2\t$only\nof\t02v\t$only\n", encoding="utf-8")
        cache_dir = tmp_path / "cache"
        monkeypatch.setattr(cs, "ESPEAK_DICTSOURCE_PATH", str(dictsource))
        monkeypatch.setattr(cs, "O2I_LEX_CACHE_DIR", str(cache_dir))
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        monkeypatch.setitem(
            cs.LANGS, "en-US-test",
            {"dataset": ("wikipron", "en-US"), "espeak": "en-us"})
        monkeypatch.setitem(cs.DICTSOURCE_LANG, "en-US-test", "en")

        calls = []

        def fake_batch(words, voice, data_path=None):
            calls.append(list(words))
            return {"the": "ð", "of": "ʌv"}

        monkeypatch.setattr(cs, "espeak_batch_transcribe", fake_batch)

        path = cs.build_espeak_lexicon_tsv("en-US-test")
        assert path == str(cache_dir / "en-US-test.tsv")
        content = (cache_dir / "en-US-test.tsv").read_text(encoding="utf-8")
        assert "of\tʌv" in content
        assert "the\tð" in content
        assert len(calls) == 1

        # second call reuses the cache — no second espeak invocation
        path2 = cs.build_espeak_lexicon_tsv("en-US-test")
        assert path2 == path
        assert len(calls) == 1

    def test_no_words_yields_none_and_no_empty_cache_file(self, monkeypatch, tmp_path):
        dictsource = tmp_path / "dictsource"
        dictsource.mkdir()
        (dictsource / "en_list").write_text("// nothing but comments\n",
                                            encoding="utf-8")
        cache_dir = tmp_path / "cache"
        monkeypatch.setattr(cs, "ESPEAK_DICTSOURCE_PATH", str(dictsource))
        monkeypatch.setattr(cs, "O2I_LEX_CACHE_DIR", str(cache_dir))
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        monkeypatch.setitem(
            cs.LANGS, "en-US-test2",
            {"dataset": ("wikipron", "en-US"), "espeak": "en-us"})
        monkeypatch.setitem(cs.DICTSOURCE_LANG, "en-US-test2", "en")
        assert cs.build_espeak_lexicon_tsv("en-US-test2") is None
        assert not (cache_dir / "en-US-test2.tsv").exists()


class TestCompareLangFairComparison2x2:
    def test_espeak_rules_and_o2i_lex_columns_scored(self, monkeypatch, tmp_path):
        pairs = [("bat", "bato")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_2x2": (lambda lang, limit: pairs, ["yy"])})
        monkeypatch.setitem(
            cs.LANGS, "yy",
            {"dataset": ("fake_2x2", "yy"), "espeak": "yy-voice",
             "epitran": None, "gruut": None})
        monkeypatch.setitem(cs.DICTSOURCE_LANG, "yy", "yy")

        class FakeEngine:
            def transcribe_word(self, word):
                return "bato"  # exact o2i hit, PER 0

        class FakeModule:
            G2P = staticmethod(lambda lang: FakeEngine())
            registered = {}

            @staticmethod
            def register_lexicon(code, src):
                FakeModule.registered[code] = src

            @staticmethod
            def clear_lexicons():
                FakeModule.registered.clear()

        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        monkeypatch.setattr(cs, "espeak_rules_available", lambda: True)
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", "/fake/rules/data")
        monkeypatch.setattr(
            cs, "build_espeak_lexicon_tsv",
            lambda lang: str(tmp_path / "lex.tsv") if lang == "yy" else None)

        def fake_batch(words, voice, data_path=None):
            if data_path == "/fake/rules/data":
                return {w: "wrong" for w in words}  # rules-only is worse
            return {w: "bato" for w in words}

        monkeypatch.setattr(cs, "espeak_batch_transcribe", fake_batch)

        try:
            row = cs.compare_lang("yy", limit=10)[0]
        finally:
            cs.LANGS.pop("yy", None)
            cs.DICTSOURCE_LANG.pop("yy", None)

        assert row["espeak_per"] == 0.0
        assert row["espeak_rules_per"] > 0.0
        assert row["o2i_lex_per"] == 0.0
        assert FakeModule.registered == {}  # cleared after o2i_lex scoring

    def test_missing_env_vars_yield_n_a_for_both_new_columns(self, monkeypatch):
        pairs = [("bat", "bato")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_2x2b": (lambda lang, limit: pairs, ["zz2"])})
        monkeypatch.setitem(
            cs.LANGS, "zz2",
            {"dataset": ("fake_2x2b", "zz2"), "espeak": "zz2-voice",
             "epitran": None, "gruut": None})

        class FakeEngine:
            def transcribe_word(self, word):
                return "bato"

        class FakeModule:
            G2P = staticmethod(lambda lang: FakeEngine())
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)

        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        monkeypatch.setattr(cs, "espeak_rules_available", lambda: False)
        monkeypatch.setattr(cs, "ESPEAK_DICTSOURCE_PATH", None)
        monkeypatch.setattr(cs, "espeak_batch_transcribe",
                            lambda words, voice, data_path=None:
                            {w: "bato" for w in words})

        try:
            row = cs.compare_lang("zz2", limit=10)[0]
        finally:
            cs.LANGS.pop("zz2", None)

        assert row["espeak_rules_per"] is None
        assert row["espeak_rules_n"] == 0
        assert row["o2i_lex_per"] is None
        assert row["o2i_lex_n"] == 0


class TestCompareLangMultiDataset:
    """compare_lang must score EVERY benchmark.DATASETS entry that covers
    the language's loader_lang, not just the one dataset picked as the
    LANGS config's primary — the whole point of the comparison-matrix
    redesign (one row per (lang, dataset), not one battleground row)."""

    def test_iterates_every_matching_dataset(self, monkeypatch):
        pairs_a = [("ola", "ola")]
        pairs_b = [("kasa", "kaza")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {
                "fake_primary": (lambda lang, limit: pairs_a, ["mm"]),
                "fake_secondary": (lambda lang, limit: pairs_b, ["mm"]),
                "fake_unrelated": (lambda lang, limit: pairs_a, ["nn"]),
            },
        )
        monkeypatch.setitem(
            cs.LANGS, "mm",
            {"dataset": ("fake_primary", "mm"), "espeak": None,
             "epitran": None, "gruut": None})

        fake_o2i = FakeEngine({"ola": "ola", "kasa": "kaza"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        try:
            rows = cs.compare_lang("mm", limit=10)
        finally:
            cs.LANGS.pop("mm", None)

        datasets = {r["dataset"] for r in rows}
        assert datasets == {"fake_primary", "fake_secondary"}
        assert "fake_unrelated" not in datasets  # different loader_lang
        # the configured primary dataset stays first, existing consumers
        # that only look at row [0] keep seeing the same dataset as before
        assert rows[0]["dataset"] == "fake_primary"
        assert all(r["lang"] == "mm" for r in rows)

    def test_single_dataset_language_yields_one_row(self, monkeypatch):
        pairs = [("ola", "ola")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_only": (lambda lang, limit: pairs, ["oo"])})
        monkeypatch.setitem(
            cs.LANGS, "oo",
            {"dataset": ("fake_only", "oo"), "espeak": None,
             "epitran": None, "gruut": None})

        fake_o2i = FakeEngine({"ola": "ola"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        try:
            rows = cs.compare_lang("oo", limit=10)
        finally:
            cs.LANGS.pop("oo", None)

        assert len(rows) == 1
        assert rows[0]["dataset"] == "fake_only"


class TestSameSourceExclusion:
    """A system scored against a gold dataset that IS that system's own
    output is tautological — near-zero PER by construction, not accuracy.
    Such cells must be refused (flagged same_source, per left None) rather
    than silently reported as a real number."""

    def test_espeak_excluded_on_espeak_derived_gold(self, monkeypatch):
        pairs = [("ola", "ola")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"ipa_babylm": (lambda lang, limit: pairs, ["pp"])})
        monkeypatch.setattr(
            cs.benchmark, "PROVENANCE",
            {**cs.benchmark.PROVENANCE, "ipa_babylm": "espeak-derived"})
        monkeypatch.setitem(
            cs.LANGS, "pp",
            {"dataset": ("ipa_babylm", "pp"), "espeak": "pp-voice",
             "epitran": None, "gruut": None})

        fake_o2i = FakeEngine({"ola": "ola"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        # If espeak were actually invoked, this would return a "perfect"
        # score, proving the exclusion is what keeps the cell empty.
        monkeypatch.setattr(
            cs, "espeak_batch_transcribe",
            lambda words, voice, data_path=None: {w: "ola" for w in words})

        try:
            row = cs.compare_lang("pp", limit=10)[0]
        finally:
            cs.LANGS.pop("pp", None)

        assert row["espeak_per"] is None
        assert row["espeak_n"] == 0
        assert row["espeak_same_source"] is True
        assert cs._cell(row, "espeak") == "same-source"

    def test_epitran_excluded_on_epitran_derived_gold(self, monkeypatch):
        pairs = [("ola", "ola")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"vox_communis": (lambda lang, limit: pairs, ["qq"])})
        monkeypatch.setattr(
            cs.benchmark, "PROVENANCE",
            {**cs.benchmark.PROVENANCE, "vox_communis": "epitran-derived"})
        monkeypatch.setitem(
            cs.LANGS, "qq",
            {"dataset": ("vox_communis", "qq"), "espeak": None,
             "epitran": "qqq-Latn", "gruut": None})

        fake_o2i = FakeEngine({"ola": "ola"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(
            cs, "epitran_transcribe", lambda word, code: "ola")

        try:
            row = cs.compare_lang("qq", limit=10)[0]
        finally:
            cs.LANGS.pop("qq", None)

        assert row["epitran_per"] is None
        assert row["epitran_same_source"] is True
        assert cs._cell(row, "epitran") == "same-source"

    def test_ahotts_excluded_on_hitz_basque_ipa(self, monkeypatch):
        pairs = [("kaixo", "kaiʃo")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"hitz_basque_ipa": (lambda lang, limit: pairs, ["eu"])})
        monkeypatch.setitem(
            cs.LANGS, "eu",
            {"dataset": ("hitz_basque_ipa", "eu"), "espeak": None,
             "epitran": None, "gruut": None,
             "ahotts": {"lang": "eu", "version": "classic"}})

        fake_o2i = FakeEngine({"kaixo": "kaiʃo"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(
            cs, "ahotts_transcribe", lambda word, cfg: "kajʃˈo")

        row = cs.compare_lang("eu", limit=10)[0]

        assert row["ahotts_per"] is None
        assert row["ahotts_n"] == 0
        assert row["ahotts_same_source"] is True
        assert cs._cell(row, "ahotts") == "same-source"

    def test_non_same_source_dataset_still_scores_normally(self, monkeypatch):
        # Sanity check: an unrelated (non-derived) dataset for the SAME
        # espeak-mapped language is NOT excluded — only the specific
        # (dataset, lang) pair flagged derived is refused.
        pairs = [("ola", "ola")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_expert_gold": (lambda lang, limit: pairs, ["rr"])})
        monkeypatch.setitem(
            cs.LANGS, "rr",
            {"dataset": ("fake_expert_gold", "rr"), "espeak": "rr-voice",
             "epitran": None, "gruut": None})

        fake_o2i = FakeEngine({"ola": "ola"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        monkeypatch.setattr(
            cs, "espeak_batch_transcribe",
            lambda words, voice, data_path=None: {w: "ola" for w in words})

        try:
            row = cs.compare_lang("rr", limit=10)[0]
        finally:
            cs.LANGS.pop("rr", None)

        assert row["espeak_same_source"] is False
        assert row["espeak_per"] == 0.0


class TestCellFormatting:
    def test_cell_shows_same_source_not_na(self):
        row = {"espeak_per": None, "espeak_same_source": True}
        assert cs._cell(row, "espeak") == "same-source"

    def test_cell_shows_na_when_unavailable_not_same_source(self):
        row = {"espeak_per": None, "espeak_same_source": False}
        assert cs._cell(row, "espeak") == "n/a"

    def test_cell_shows_formatted_number(self):
        row = {"espeak_per": 0.1234, "espeak_same_source": False}
        assert cs._cell(row, "espeak") == "0.1234"


class TestWriteComparisonSameSourceRendering:
    def test_same_source_cell_rendered_in_docs(self, tmp_path, monkeypatch):
        rows = [
            {"lang": "aa", "dataset": "d", "n": 2,
             "o2i_per": 0.1, "o2i_n": 2,
             "espeak_per": None, "espeak_n": 0, "espeak_same_source": True,
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
        assert "same-source" in text
        assert "| aa | d | 2 | 0.1000 | same-source |" in text


class TestO2iSameSourceExclusion:
    """o2i itself is scored against gold that shares its own spec-authoring
    Claude lineage (arabic_tts, portuguese_tts, gold20_arabic) — a
    tautological self-agreement, not a real accuracy signal, so those
    cells must render same-source too (see _O2I_SAME_SOURCE_DATASETS)."""

    def test_o2i_flagged_same_source_on_arabic_tts(self, monkeypatch):
        pairs = [("kaifa", "kajfa")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"arabic_tts": (lambda lang, limit: pairs, ["ar-EG"])})
        monkeypatch.setattr(
            cs.benchmark, "PROVENANCE",
            {**cs.benchmark.PROVENANCE, "arabic_tts": "llm-generated"})
        monkeypatch.setitem(
            cs.LANGS, "ar-EG",
            {"dataset": ("arabic_tts", "ar-EG"), "espeak": None,
             "epitran": None, "gruut": None})

        fake_o2i = FakeEngine({"kaifa": "kajfa"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        try:
            row = cs.compare_lang("ar-EG", limit=10)[0]
        finally:
            cs.LANGS.pop("ar-EG", None)

        # o2i is still scored (it's the system under test) ...
        assert row["o2i_per"] == 0.0
        # ... but flagged, so the docs table refuses to present it as a
        # real accuracy number.
        assert row["o2i_same_source"] is True
        assert cs._cell(row, "o2i") == "same-source"

    def test_o2i_not_flagged_on_unrelated_llm_generated_dataset(self, monkeypatch):
        # mirandese_dict is llm-generated (Claude, same as the datasets
        # that ARE excluded) but its loader's own docstring documents it
        # was NOT produced by orthography2ipa or any downstream o2i
        # consumer, so scoring o2i against it is not circular — the
        # blanket llm-generated tier must not be used as the o2i
        # same-source condition; only the curated, documented-circular
        # dataset names in _O2I_SAME_SOURCE_DATASETS are.
        pairs = [("ola", "ola")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"mirandese_dict": (lambda lang, limit: pairs, ["mwl"])})
        monkeypatch.setattr(
            cs.benchmark, "PROVENANCE",
            {**cs.benchmark.PROVENANCE, "mirandese_dict": "llm-generated"})
        monkeypatch.setitem(
            cs.LANGS, "mwl",
            {"dataset": ("mirandese_dict", "mwl"), "espeak": None,
             "epitran": None, "gruut": None})

        fake_o2i = FakeEngine({"ola": "ola"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
            clear_lexicons = staticmethod(lambda: None)
            register_lexicon = staticmethod(lambda code, src: None)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        try:
            row = cs.compare_lang("mwl", limit=10)[0]
        finally:
            cs.LANGS.pop("mwl", None)

        assert row["o2i_same_source"] is False
        assert cs._cell(row, "o2i") == "0.0000"


class TestRobustnessSection:
    """_robustness_section is consumed by write_comparison but was
    previously untested — pin the win/loss split, the verdict labels, the
    >=-counts-as-loss tie convention, and the <2-datasets skip."""

    def _row(self, lang, dataset, o2i, espeak, tier="crowd-scraped",
             espeak_same_source=False, o2i_same_source=False):
        return {
            "lang": lang, "dataset": dataset, "n": 10,
            "o2i_per": o2i, "espeak_per": espeak,
            "espeak_same_source": espeak_same_source,
            "o2i_same_source": o2i_same_source,
            "provenance_tier": tier,
        }

    def test_mixed_wins_and_losses_reported(self):
        rows = [
            self._row("xx", "gold_a", 0.1, 0.2),   # o2i wins
            self._row("xx", "gold_b", 0.3, 0.1),   # o2i loses
        ]
        lines = cs._robustness_section(rows)
        text = "\n".join(lines)
        assert "**`xx`** (MIXED — wins on some golds, loses on others)" in text
        assert "gold_a" in text and "o2i wins" in text
        assert "gold_b" in text and "o2i loses" in text

    def test_wins_on_all_golds(self):
        rows = [
            self._row("yy", "gold_a", 0.1, 0.2),
            self._row("yy", "gold_b", 0.05, 0.3),
        ]
        text = "\n".join(cs._robustness_section(rows))
        assert "**`yy`** (wins on all golds)" in text

    def test_loses_on_all_golds(self):
        rows = [
            self._row("zz", "gold_a", 0.3, 0.1),
            self._row("zz", "gold_b", 0.4, 0.2),
        ]
        text = "\n".join(cs._robustness_section(rows))
        assert "**`zz`** (loses on all golds)" in text

    def test_tie_counts_as_loss(self):
        # o2i_per == espeak_per is NOT a win — the >= convention.
        rows = [
            self._row("tt", "gold_a", 0.2, 0.2),
            self._row("tt", "gold_b", 0.3, 0.1),
        ]
        text = "\n".join(cs._robustness_section(rows))
        assert "**`tt`** (loses on all golds)" in text
        assert "`gold_a`" in text

    def test_language_with_fewer_than_two_datasets_skipped(self):
        rows = [self._row("single", "gold_a", 0.1, 0.2)]
        text = "\n".join(cs._robustness_section(rows))
        assert "single" not in text
        assert "No language in this run had 2+" in text

    def test_same_source_rows_excluded_from_the_split(self):
        # An espeak-same-source or o2i-same-source row is never a real
        # win/loss data point and must not count toward the 2+ threshold.
        rows = [
            self._row("uu", "gold_a", 0.1, 0.2),
            self._row("uu", "gold_b", 0.0, None, espeak_same_source=True),
            self._row("uu", "gold_c", 0.0, 0.5, o2i_same_source=True),
        ]
        text = "\n".join(cs._robustness_section(rows))
        # Only one real espeak-comparable dataset remains for "uu" — below
        # the 2+ threshold, so it must be skipped entirely.
        assert "**`uu`**" not in text


class TestCommittedDocsMatchesFreshStalenessNote:
    """Mechanical guard against exactly the bug this class is named for:
    docs/comparison.md's scoreboard-staleness paragraph was generated
    BEFORE a rebase moved benchmarks/results.json out from under it, so
    the committed prose named the wrong stale rows (14 rows, wrong set)
    instead of the true count against the tree it actually shipped with
    (21 rows). A regeneration that runs write_comparison() before its
    final rebase/JSON update is exactly what this would have caught: the
    committed doc's note must equal _scoreboard_staleness_note() computed
    fresh, right now, from the COMMITTED comparison.json against the
    COMMITTED results.json — if they differ, the doc was generated
    against a different tree than the one that got committed."""

    def test_committed_staleness_note_matches_fresh_computation(self):
        with open(cs.COMPARISON_JSON, encoding="utf-8") as fh:
            committed_rows = json.load(fh)
        with open(cs.COMPARISON_MD, encoding="utf-8") as fh:
            committed_docs = fh.read()

        fresh_note = cs._scoreboard_staleness_note(committed_rows)

        assert fresh_note in committed_docs, (
            "docs/comparison.md's scoreboard-staleness paragraph does not "
            "match a fresh _scoreboard_staleness_note() computed from the "
            "COMMITTED benchmarks/comparison.json against the COMMITTED "
            "benchmarks/results.json — the doc was regenerated against a "
            "different tree than what actually got committed (e.g. before "
            "a later rebase changed results.json). Re-run "
            "scripts/compare_systems.py's writer on the current tree "
            "before committing.\n\nFresh note:\n" + fresh_note
        )


class TestCommittedComparisonJsonCompleteness:
    """Mechanical guard against a partial regeneration: every row actually
    committed to benchmarks/comparison.json must carry a provenance_tier
    and the *_same_source keys its tier requires. This is exactly the
    check that would have caught both the 13/44-rows partial regen and
    the kab/vox_communis stale-row mislabel (epitran cell rendered n/a
    instead of same-source) before they reached the PR."""

    def test_every_committed_row_has_required_fields(self):
        with open(cs.COMPARISON_JSON, encoding="utf-8") as fh:
            committed_rows = json.load(fh)

        assert committed_rows, "benchmarks/comparison.json must not be empty"

        required_same_source_keys = {
            "espeak_same_source", "espeak_rules_same_source",
            "epitran_same_source", "ahotts_same_source", "o2i_same_source",
        }
        missing = []
        for row in committed_rows:
            label = f"{row.get('lang')}/{row.get('dataset')}"
            if "provenance_tier" not in row:
                missing.append(f"{label}: missing provenance_tier")
                continue
            absent_keys = required_same_source_keys - row.keys()
            if absent_keys:
                missing.append(f"{label}: missing {sorted(absent_keys)}")

        assert not missing, (
            "rows below are stale/partially-regenerated leftovers "
            "(missing the current schema's fields) — regenerate the full "
            "matrix, do not hand-patch:\n" + "\n".join(missing)
        )

    def test_epitran_derived_rows_are_never_silently_na(self):
        # The specific bug this guards: a competitor-derived row whose
        # exclusion flag is False/absent renders "n/a" instead of
        # "same-source", silently hiding the tautology instead of
        # refusing it.
        with open(cs.COMPARISON_JSON, encoding="utf-8") as fh:
            committed_rows = json.load(fh)

        wrong = []
        for row in committed_rows:
            dataset = row.get("dataset")
            lang = row.get("lang")
            # Use the row's OWN recorded provenance_tier (computed at scoring
            # time from the dataset's real loader_lang) rather than
            # recomputing from the LANGS key, which for aliased entries
            # (e.g. "eu-wikipron") differs from the loader_lang and would
            # look up the wrong tier.
            tier = row.get("provenance_tier")
            if tier == "epitran-derived" and not row.get("epitran_same_source"):
                wrong.append(f"{lang}/{dataset}")
            if tier == "espeak-derived" and not row.get("espeak_same_source"):
                wrong.append(f"{lang}/{dataset} (espeak)")

        assert not wrong, (
            "these committed rows are competitor-derived but not flagged "
            "same-source — a stale/hand-edited row, not a live rescore: "
            + ", ".join(wrong)
        )


class TestScoreboardLangScoping:
    """``--scoreboard --lang X`` must rebuild ONLY X and keep every other
    language's committed row.

    Regression guard for a real defect: ``build_comparison`` took no
    language filter and ``main()`` called it as ``build_comparison(
    args.limit)``, so ``--scoreboard --lang nl`` silently rescored all 33
    mapped languages — every external system over every gold row, hours of
    espeak-ng and epitran subprocesses. The practical effect was that a
    one-language refresh was never run at all and the board's rows went
    stale instead (the staleness note in ``docs/comparison.md`` was
    carrying 20 such rows).
    """

    def test_build_comparison_only_langs_restricts_the_run(self, monkeypatch):
        called = []

        def fake_compare_lang(lang, limit):
            called.append(lang)
            return [{"lang": lang, "dataset": "d", "o2i_per": 0.1}]

        monkeypatch.setattr(cs, "compare_lang", fake_compare_lang)
        rows = cs.build_comparison(None, only_langs=["nl"])

        assert called == ["nl"], (
            f"only_langs=['nl'] must score nl alone, scored: {called}"
        )
        assert [r["lang"] for r in rows] == ["nl"]

    def test_build_comparison_without_only_langs_runs_everything(
            self, monkeypatch):
        called = []
        monkeypatch.setattr(
            cs, "compare_lang",
            lambda lang, limit: called.append(lang) or [])

        cs.build_comparison(None)

        assert set(called) == set(cs.LANGS), (
            "omitting only_langs must still rebuild the whole board"
        )

    def test_merge_keeps_every_other_language_untouched(self):
        old = [
            {"lang": "nl", "dataset": "wikipron", "o2i_per": 0.1262},
            {"lang": "de", "dataset": "wikipron", "o2i_per": 0.2092},
            {"lang": "fr", "dataset": "wikipron", "o2i_per": 0.1189},
        ]
        new = [{"lang": "nl", "dataset": "wikipron", "o2i_per": 0.0902}]

        merged = cs.merge_comparison_rows(old, new)

        by_key = {(r["lang"], r["dataset"]): r for r in merged}
        assert by_key[("nl", "wikipron")]["o2i_per"] == 0.0902
        assert by_key[("de", "wikipron")]["o2i_per"] == 0.2092
        assert by_key[("fr", "wikipron")]["o2i_per"] == 0.1189
        assert len(merged) == 3

    def test_merge_appends_a_language_with_no_committed_row(self):
        merged = cs.merge_comparison_rows(
            [{"lang": "de", "dataset": "wikipron", "o2i_per": 0.2}],
            [{"lang": "nl", "dataset": "wikipron", "o2i_per": 0.09}],
        )
        assert [(r["lang"], r["dataset"]) for r in merged] == [
            ("de", "wikipron"), ("nl", "wikipron")]

    def test_merge_replaces_a_row_wholesale_not_field_by_field(self):
        """Half-refreshing a row would mix two live runs' numbers."""
        old = [{"lang": "nl", "dataset": "wikipron",
                "o2i_per": 0.1262, "espeak_per": 0.1099, "stale_key": 1}]
        new = [{"lang": "nl", "dataset": "wikipron",
                "o2i_per": 0.0902, "espeak_per": 0.1099}]

        merged = cs.merge_comparison_rows(old, new)

        assert merged == new
        assert "stale_key" not in merged[0]
