"""Tests for scripts/compare_systems.py.

All comparison systems are mocked — no network, no real espeak-ng,
epitran, gruut, pycotovia, or ahotts-g2p required. Covers the PER math, the
"beats espeak" tally, the "unavailable system -> n/a, never a crash"
contract, and the Catalan-dialect espeak voice discovery/fallback logic.
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
        monkeypatch.setitem(
            cs.benchmark.DATASETS, "fake_gl_dataset",
            (lambda lang, limit: pairs, ["gl"]))
        monkeypatch.setitem(
            cs.LANGS, "gl",
            {"dataset": ("fake_gl_dataset", "gl"), "espeak": None,
             "epitran": None, "gruut": None, "pycotovia": "gl"})

        fake_o2i = FakeEngine({"ola": "ola"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(
            cs, "pycotovia_transcribe", lambda word, lang: "ola")

        row = cs.compare_lang("gl", limit=10)
        assert row["pycotovia_per"] == 0.0
        assert row["pycotovia_n"] == 1
        assert row["ahotts_per"] is None
        assert row["ahotts_n"] == 0

    def test_eu_row_scores_ahotts_and_records_version(self, monkeypatch):
        # gold 'kaiʃo'; ahotts (mocked) returns unfolded 'kajʃˈo' ->
        # normalize -> 'kajʃo' vs 'kaiʃo' == 1 edit / 5 == 0.2
        pairs = [("kaixo", "kaiʃo")]
        monkeypatch.setitem(
            cs.benchmark.DATASETS, "fake_eu_dataset",
            (lambda lang, limit: pairs, ["eu"]))
        monkeypatch.setitem(
            cs.LANGS, "eu",
            {"dataset": ("fake_eu_dataset", "eu"), "espeak": None,
             "epitran": None, "gruut": None,
             "ahotts": {"lang": "eu", "version": "classic"}})

        fake_o2i = FakeEngine({"kaixo": "kaiʃo"})

        class FakeModule:
            G2P = staticmethod(lambda lang: fake_o2i)
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
        monkeypatch.setattr(
            cs, "ahotts_transcribe", lambda word, cfg: "kajʃˈo")

        row = cs.compare_lang("eu", limit=10)
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
        monkeypatch.setitem(
            cs.benchmark.DATASETS, "fake_euw_dataset",
            (lambda lang, limit: pairs, ["eu"]))
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
        monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)

        row = cs.compare_lang("eu-wikipron", limit=10)
        assert seen["lang"] == "eu"  # g2p override, not the row key
        assert row["lang"] == "eu-wikipron"
        assert row["o2i_per"] == 0.0


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

        def per_word(word, voice):
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
                            lambda w, v: f"ipa-{w}")
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
