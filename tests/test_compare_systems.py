"""Tests for scripts/compare_systems.py.

All comparison systems are mocked — no network, no real espeak-ng,
epitran, gruut, pycotovia, or ahotts-g2p required. Covers the PER math, the
"beats espeak" tally, the "unavailable system -> n/a, never a crash"
contract, and the Catalan-dialect espeak voice discovery/fallback logic.

Two shared doubles do most of the work; reach for these before writing a
new one:

:class:`FakeEngine`
    Stands in for ``orthography2ipa.G2P`` with a fixed word -> IPA table, so
    o2i's PER on a test row is an exact, hand-computable number.
:func:`install_fake_o2i`
    Puts a ``FakeEngine`` (or any stub engine) into ``sys.modules`` as the
    ``orthography2ipa`` module, which is what ``compare_lang`` actually
    imports. Its ``on_register``/``on_clear`` hooks observe the
    process-global lexicon registry for the contamination-ordering tests.

The remaining hand-rolled fake modules are the cases those hooks cannot
express — capturing the language code ``G2P`` was constructed with, and
accumulating registered lexicons on the class itself.

Individual comparison engines are stubbed by monkeypatching the module-level
``cs.<engine>_transcribe`` function. That works because
:data:`compare_systems.PER_WORD_ENGINES` resolves engines BY NAME at call
time rather than holding function objects.
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


def install_fake_o2i(monkeypatch, engine, *, on_register=None, on_clear=None):
    """Swap the real ``orthography2ipa`` module for a stub whose ``G2P``
    returns *engine*.

    Almost every ``compare_lang`` test needs this. ``_compare_lang_dataset``
    imports ``orthography2ipa`` itself rather than taking it as an argument,
    so replacing the entry in ``sys.modules`` is the only way to pin o2i to a
    known, fixed set of hypotheses and get a PER we can assert exactly.

    *on_register* / *on_clear* observe the process-global lexicon registry
    calls. Tests use them to assert the ORDER of operations — notably the
    tugaphone contamination regression, where the bug was not a wrong number
    but a lexicon being registered too early.
    """
    class FakeModule:
        G2P = staticmethod(lambda lang: engine)
        clear_lexicons = staticmethod(on_clear or (lambda: None))
        register_lexicon = staticmethod(
            on_register or (lambda code, src: None))

    monkeypatch.setitem(sys.modules, "orthography2ipa", FakeModule)
    return FakeModule


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

        install_fake_o2i(monkeypatch, fake_o2i)

        # espeak: gets one wrong -> PER > 0, worse than o2i
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        # A local $ESPEAK_RULES_DATA_PATH build (as used by the board-regen
        # skill) would otherwise be probed for this mock language "xx" and
        # raise, since no real rules-only manifest lists it.
        monkeypatch.setattr(cs, "espeak_rules_available", lambda: False)
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

        install_fake_o2i(monkeypatch, fake_o2i)

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

        install_fake_o2i(monkeypatch, RaisingEngine())

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
        assert "### bb" in text  # honest: the losing row is still listed
        assert "n/a" in text  # missing systems reported as n/a

        data = json_path.read_text(encoding="utf-8")
        assert '"lang": "aa"' in data

    def test_partial_regen_keeps_the_catalan_section(self, tmp_path,
                                                       monkeypatch):
        """A single-language refresh rewrites the WHOLE document, so a
        section it did not rescore must survive it.

        ``write_comparison`` defaults ``catalan_voices`` to the resolved
        module constant precisely so a caller that never thought about
        Catalan cannot delete the committed "Catalan dialects vs espeak
        (BSC)" section — which is exactly what a ``--lang en`` regen did
        while the default was ``None``.
        """
        def row(lang, per):
            return {"lang": lang, "dataset": "4catac", "n": 2,
                    "o2i_per": per, "o2i_n": 2,
                    "espeak_per": 0.2, "espeak_n": 2,
                    "epitran_per": None, "epitran_n": 0,
                    "gruut_per": None, "gruut_n": 0,
                    "provenance_tier": "expert-human",
                    "harness_version": "1.0", "limit": 10}

        rows = [row(t, 0.1) for t in cs._CATALAN_DIALECT_LABELS]
        rows.append({"lang": "en", "dataset": "wikipron", "n": 2,
                     "o2i_per": 0.3, "o2i_n": 2,
                     "espeak_per": 0.2, "espeak_n": 2,
                     "epitran_per": None, "epitran_n": 0,
                     "gruut_per": None, "gruut_n": 0,
                     "provenance_tier": "crowd-scraped",
                     "harness_version": "1.0", "limit": 10})
        for r in rows:
            monkeypatch.setitem(cs.LANGS, r["lang"],
                                {"dataset": (r["dataset"], r["lang"])})
        md_path = tmp_path / "comparison.md"
        monkeypatch.setattr(cs, "COMPARISON_MD", str(md_path))
        monkeypatch.setattr(cs, "COMPARISON_JSON",
                            str(tmp_path / "comparison.json"))

        # the shape of a partial refresh: no catalan_voices argument at all
        cs.write_comparison(rows)

        assert "## Catalan dialects vs espeak (BSC)" in md_path.read_text(
            encoding="utf-8")

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

        install_fake_o2i(monkeypatch, fake_o2i)
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

        install_fake_o2i(monkeypatch, fake_o2i)
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

        install_fake_o2i(monkeypatch, fake_o2i)
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

        install_fake_o2i(monkeypatch, fake_o2i)

        row = cs.compare_lang("ww", limit=10)[0]
        assert row["africa_g2p_per"] is None
        assert row["africa_g2p_n"] == 0


class TestArbtokLazyImport:
    def test_absent_module_yields_none(self, monkeypatch):
        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **k):
            if name == "arbtok.plugin":
                raise ImportError("no module named arbtok.plugin")
            return real_import(name, *a, **k)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        cs._arbtok_plugin_cache.clear()
        assert cs.arbtok_transcribe("كتاب", "arb") is None

    def test_present_module_transcribes(self, monkeypatch):
        class FakePlugin:
            def __init__(self, lang, lexicon=None, dialect_lexicon=True):
                self.lang = lang
                # arbtok_transcribe (the RANKED column) must construct
                # with both bundled lexicons off — see
                # test_arbtok_transcribe_constructs_plugin_lexicon_free
                # for the dedicated audit of this.
                assert lexicon is None
                assert dialect_lexicon is False

            def transcribe(self, word):
                return f"ipa-{word}-{self.lang}"

        fake_pkg = type(sys)("arbtok.plugin")
        fake_pkg.ArbtokG2PPlugin = FakePlugin
        monkeypatch.setitem(sys.modules, "arbtok.plugin", fake_pkg)
        cs._arbtok_plugin_cache.clear()

        assert cs.arbtok_transcribe("كتاب", "arb") == "ipa-كتاب-arb"
        cs._arbtok_plugin_cache.clear()

    def test_exception_during_transcribe_yields_none(self, monkeypatch):
        class BoomPlugin:
            def __init__(self, lang, lexicon=None, dialect_lexicon=True):
                pass

            def transcribe(self, word):
                raise RuntimeError("boom")

        fake_pkg = type(sys)("arbtok.plugin")
        fake_pkg.ArbtokG2PPlugin = BoomPlugin
        monkeypatch.setitem(sys.modules, "arbtok.plugin", fake_pkg)
        cs._arbtok_plugin_cache.clear()

        assert cs.arbtok_transcribe("x", "arb") is None
        cs._arbtok_plugin_cache.clear()


class TestTugaphoneLazyImport:
    def test_absent_module_yields_none(self, monkeypatch):
        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **k):
            if name == "tugaphone":
                raise ImportError("no module named tugaphone")
            return real_import(name, *a, **k)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        cs._tugaphone_instance = None
        assert cs.tugaphone_transcribe("casa", "pt-PT") is None

    def test_present_module_phonemizes(self, monkeypatch):
        class FakeTugaPhonemizer:
            def phonemize_sentence(self, sentence, lang="pt-PT"):
                return f"ipa-{sentence}-{lang}"

        fake_pkg = type(sys)("tugaphone")
        fake_pkg.TugaPhonemizer = FakeTugaPhonemizer
        monkeypatch.setitem(sys.modules, "tugaphone", fake_pkg)
        cs._tugaphone_instance = None

        assert cs.tugaphone_transcribe("casa", "pt-PT") == "ipa-casa-pt-PT"
        cs._tugaphone_instance = None

    def test_exception_during_phonemize_yields_none(self, monkeypatch):
        class BoomTugaPhonemizer:
            def phonemize_sentence(self, sentence, lang="pt-PT"):
                raise RuntimeError("boom")

        fake_pkg = type(sys)("tugaphone")
        fake_pkg.TugaPhonemizer = BoomTugaPhonemizer
        monkeypatch.setitem(sys.modules, "tugaphone", fake_pkg)
        cs._tugaphone_instance = None

        assert cs.tugaphone_transcribe("x", "pt-PT") is None
        cs._tugaphone_instance = None


class TestBarranquenhoLazyImport:
    def test_absent_module_yields_none(self, monkeypatch):
        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **k):
            if name == "g2p_barranquenho":
                raise ImportError("no module named g2p_barranquenho")
            return real_import(name, *a, **k)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        assert cs.barranquenho_transcribe("casa", "ext-PT-x-barrancos") is None

    def test_present_module_transcribes(self, monkeypatch):
        fake_pkg = type(sys)("g2p_barranquenho")
        fake_pkg.transcribe = lambda word: ["k", "a", "z", "ɐ"]
        monkeypatch.setitem(sys.modules, "g2p_barranquenho", fake_pkg)

        assert (cs.barranquenho_transcribe("casa", "ext-PT-x-barrancos")
                == "kazɐ")

    def test_exception_during_transcribe_yields_none(self, monkeypatch):
        def boom(word):
            raise RuntimeError("boom")

        fake_pkg = type(sys)("g2p_barranquenho")
        fake_pkg.transcribe = boom
        monkeypatch.setitem(sys.modules, "g2p_barranquenho", fake_pkg)

        assert cs.barranquenho_transcribe("x", "ext-PT-x-barrancos") is None


class TestMwlPhonemizerLazyImport:
    def test_absent_module_yields_none(self, monkeypatch):
        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **k):
            if name == "mwl_phonemizer":
                raise ImportError("no module named mwl_phonemizer")
            return real_import(name, *a, **k)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        assert cs.mwl_transcribe("siempre", "mwl") is None

    def test_present_module_phonemizes(self, monkeypatch):
        fake_pkg = type(sys)("mwl_phonemizer")
        fake_pkg.phonemize = lambda word, dialect="mwl": f"ipa-{word}-{dialect}"
        monkeypatch.setitem(sys.modules, "mwl_phonemizer", fake_pkg)

        assert cs.mwl_transcribe("siempre", "mwl") == "ipa-siempre-mwl"

    def test_exception_during_phonemize_yields_none(self, monkeypatch):
        def boom(word, dialect="mwl"):
            raise RuntimeError("boom")

        fake_pkg = type(sys)("mwl_phonemizer")
        fake_pkg.phonemize = boom
        monkeypatch.setitem(sys.modules, "mwl_phonemizer", fake_pkg)

        assert cs.mwl_transcribe("x", "mwl") is None


class TestTugaphoneLexiconContaminationRegression:
    """C1 regression: ``tugaphone_transcribe`` -> ``TugaPhonemizer.
    phonemize_sentence`` -> ``tugaphone.lattice_core._ensure_lexicon()``
    calls ``orthography2ipa.register_lexicon()`` — a PROCESS-GLOBAL
    mutation keyed on the SAME lect code o2i's own engine uses. Before the
    fix, tugaphone was scored INSIDE the same per-word loop as o2i, so
    from word 2 onward o2i's own column was secretly o2i+tugalex, not
    bare o2i.

    Uses REAL ``tugaphone`` and REAL ``orthography2ipa`` (skipped, not
    mocked, if either is unavailable) — the bug lives one layer BELOW
    ``compare_systems.py``'s own code, in tugaphone's global lexicon
    registration, so a mocked ``tugaphone_transcribe`` cannot exercise it
    at all; every other test in this file mocks the family transcribe
    functions and is structurally blind to this class of bug."""

    def test_o2i_per_identical_with_and_without_tugaphone_wired(
            self, monkeypatch):
        pytest.importorskip("tugaphone")
        import orthography2ipa
        orthography2ipa.clear_lexicons()

        # Words picked to include cases tugalex covers (so the pre-fix
        # bug actually changes o2i's transcription, not just risks it).
        words = ["esquisito", "campanário", "obrigado", "cristão", "gato"]
        engine = orthography2ipa.G2P("pt-PT")
        gold_pairs = [(w, engine.transcribe_word(w)) for w in words]
        orthography2ipa.clear_lexicons()

        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_pt_dataset": (lambda lang, limit: gold_pairs,
                                  ["pt-PT"])})

        base_cfg = {"dataset": ("fake_pt_dataset", "pt-PT"), "espeak": None,
                    "epitran": None, "gruut": None}
        monkeypatch.setitem(cs.LANGS, "pt-PT", dict(base_cfg))
        clean_row = cs.compare_lang("pt-PT", limit=10)[0]

        monkeypatch.setitem(
            cs.LANGS, "pt-PT",
            dict(base_cfg, tugaphone="pt-PT"))
        wired_row = cs.compare_lang("pt-PT", limit=10)[0]

        # The bug this guards: with tugaphone wired, o2i's own column
        # measurably changed (0.0 clean -> nonzero contaminated) because
        # tugaphone's global register_lexicon() call leaked into o2i's
        # own engine mid-loop.
        assert clean_row["o2i_per"] == 0.0
        assert wired_row["o2i_per"] == clean_row["o2i_per"], (
            f"o2i_per changed from {clean_row['o2i_per']} (no tugaphone) "
            f"to {wired_row['o2i_per']} (tugaphone wired) — tugaphone's "
            f"register_lexicon() call is leaking into o2i's own scoring")
        orthography2ipa.clear_lexicons()


class TestCompareLangWithFamilySystems:
    """The family systems' same-source discipline: they are built directly
    on o2i's own lattice, so they inherit o2i's exact same-source exposure
    on the o2i-lineage-gold datasets (``_O2I_SAME_SOURCE_DATASETS``) — this
    is what distinguishes them from a genuinely independent competitor like
    epitran/gruut."""

    def _install_o2i(self, monkeypatch, table):
        """Pin o2i to a fixed word -> IPA *table* for this test."""
        return install_fake_o2i(monkeypatch, FakeEngine(table))

    def test_arbtok_scores_on_independent_gold(self, monkeypatch):
        pairs = [("كتاب", "kitaːb")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_indep_ar": (lambda lang, limit: pairs, ["arb"])})
        monkeypatch.setitem(
            cs.LANGS, "arb",
            {"dataset": ("fake_indep_ar", "arb"), "espeak": None,
             "epitran": None, "gruut": None, "arbtok": "arb"})
        self._install_o2i(monkeypatch, {"كتاب": "kitaːb"})
        monkeypatch.setattr(cs, "arbtok_transcribe",
                             lambda word, lang: "kitaːb")
        monkeypatch.setattr(cs, "arbtok_stock_transcribe",
                             lambda word, lang: "kitaːb")

        row = cs.compare_lang("arb", limit=10)[0]
        assert row["arbtok_per"] == 0.0
        assert row["arbtok_same_source"] is False

    def test_arbtok_refuses_o2i_lineage_gold_as_same_source(self, monkeypatch):
        pairs = [("كتاب", "kitaːb")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"arabic_tts": (lambda lang, limit: pairs, ["arb"])})
        monkeypatch.setitem(
            cs.LANGS, "arb",
            {"dataset": ("arabic_tts", "arb"), "espeak": None,
             "epitran": None, "gruut": None, "arbtok": "arb"})
        self._install_o2i(monkeypatch, {"كتاب": "kitaːb"})
        monkeypatch.setattr(cs, "arbtok_transcribe",
                             lambda word, lang: "kitaːb")

        row = cs.compare_lang("arb", limit=10)[0]
        assert row["arbtok_per"] is None
        assert row["arbtok_same_source"] is True

    def test_tugaphone_refuses_o2i_lineage_gold_as_same_source(
            self, monkeypatch):
        pairs = [("casa", "ˈkazɐ")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"portuguese_tts": (lambda lang, limit: pairs, ["pt-PT"])})
        monkeypatch.setitem(
            cs.LANGS, "pt-PT",
            {"dataset": ("portuguese_tts", "pt-PT"), "espeak": None,
             "epitran": None, "gruut": None, "tugaphone": "pt-PT"})
        self._install_o2i(monkeypatch, {"casa": "ˈkazɐ"})
        monkeypatch.setattr(cs, "tugaphone_transcribe",
                             lambda word, lang: "ˈkazɐ")

        row = cs.compare_lang("pt-PT", limit=10)[0]
        # Bug this guards: tugaphone wraps o2i's own lattice, so scoring it
        # against o2i-lineage gold (portuguese_tts) must be refused exactly
        # like o2i itself is, not silently scored as a real 0.0.
        assert row["tugaphone_per"] is None
        assert row["tugaphone_same_source"] is True

    def test_mwl_phonemizer_refuses_o2i_lineage_gold_as_same_source(
            self, monkeypatch):
        pairs = [("siempre", "ˈsjẽpɾɨ")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"portuguese_tts": (lambda lang, limit: pairs, ["mwl"])})
        monkeypatch.setitem(
            cs.LANGS, "mwl",
            {"dataset": ("portuguese_tts", "mwl"), "espeak": None,
             "epitran": None, "gruut": None, "mwl_phonemizer": "mwl"})
        self._install_o2i(monkeypatch, {"siempre": "ˈsjẽpɾɨ"})
        monkeypatch.setattr(cs, "mwl_transcribe",
                             lambda word, lang: "ˈsjẽpɾɨ")

        row = cs.compare_lang("mwl", limit=10)[0]
        assert row["mwl_phonemizer_per"] is None
        assert row["mwl_phonemizer_same_source"] is True

    def test_mwl_phonemizer_scores_on_independent_gold(self, monkeypatch):
        pairs = [("siempre", "ˈsjẽpɾɨ")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"mirandese_g2p": (lambda lang, limit: pairs, ["mwl"])})
        monkeypatch.setitem(
            cs.LANGS, "mwl",
            {"dataset": ("mirandese_g2p", "mwl"), "espeak": None,
             "epitran": None, "gruut": None, "mwl_phonemizer": "mwl"})
        self._install_o2i(monkeypatch, {"siempre": "ˈsjẽpɾɨ"})
        monkeypatch.setattr(cs, "mwl_transcribe",
                             lambda word, lang: "ˈsjẽpɾɨ")

        row = cs.compare_lang("mwl", limit=10)[0]
        assert row["mwl_phonemizer_per"] == 0.0
        assert row["mwl_phonemizer_same_source"] is False

    def test_barranquenho_refuses_o2i_lineage_gold_as_same_source(
            self, monkeypatch):
        pairs = [("casa", "ˈkazɐ")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"barranquenho_dict": (lambda lang, limit: pairs,
                                    ["ext-PT-x-barrancos"])})
        monkeypatch.setitem(
            cs.LANGS, "ext-PT-x-barrancos",
            {"dataset": ("barranquenho_dict", "ext-PT-x-barrancos"),
             "espeak": None, "epitran": None, "gruut": None,
             "barranquenho": "ext-PT-x-barrancos"})
        self._install_o2i(monkeypatch, {"casa": "ˈkazɐ"})
        monkeypatch.setattr(cs, "barranquenho_transcribe",
                             lambda word, lang: "ˈkazɐ")

        row = cs.compare_lang("ext-PT-x-barrancos", limit=10)[0]
        assert row["barranquenho_per"] is None
        assert row["barranquenho_same_source"] is True

    def test_tugaphone_excluded_from_lexicon_free_ranking(self):
        # tugaphone's tugalex lexicon has no public disable toggle (see the
        # module note by tugaphone_transcribe), so — the espeak discipline —
        # it must never contribute to the lexicon-free Winner/leaderboard
        # ranking even when it has a real, non-same-source PER.
        row = {"o2i_per": 0.20, "tugaphone_per": 0.05,
               "tugaphone_same_source": False}
        values = cs._rules_only_values(row)
        assert "tugaphone" not in values

    def test_barranquenho_is_ranked_lexicon_free(self):
        # g2p_barranquenho carries no per-word lexicon at all, so — unlike
        # tugaphone — it contributes to the lexicon-free ranking when not
        # same-source.
        row = {"o2i_per": 0.20,
               "barranquenho_per": 0.10, "barranquenho_same_source": False}
        values = cs._rules_only_values(row)
        assert values["barranquenho"] == 0.10

    def test_arbtok_ranked_column_included_stock_column_excluded(self):
        # C2/C7 fix: arbtok's DEFAULT configuration is lexicon-backed
        # (145,890-entry stem lexicon + dialect lexicon), so the RANKED
        # "arbtok" column and the informational "arbtok_stock" column are
        # now two DIFFERENT numbers from two different plugin configs
        # (see arbtok_transcribe/arbtok_stock_transcribe). Only the
        # ranked, lexicon-free one may contribute to the ranking.
        row = {"o2i_per": 0.20,
               "arbtok_per": 0.05, "arbtok_same_source": False,
               "arbtok_stock_per": 0.01, "arbtok_stock_same_source": False}
        values = cs._rules_only_values(row)
        assert values["arbtok"] == 0.05
        assert "arbtok_stock" not in values

    def test_arbtok_transcribe_constructs_plugin_lexicon_free(
            self, monkeypatch):
        # Real-config audit: arbtok_transcribe must construct
        # ArbtokG2PPlugin with BOTH bundled lexicons explicitly disabled,
        # not rely on (wrong) defaults. Captures the actual constructor
        # kwargs rather than asserting on compare_systems.py's own
        # documentation, which is exactly the gap that let C2 (arbtok
        # scored lexicon-backed while documented/labeled lexicon-free)
        # ship undetected.
        captured = {}

        class FakePlugin:
            def __init__(self, lang, lexicon, dialect_lexicon):
                captured["lang"] = lang
                captured["lexicon"] = lexicon
                captured["dialect_lexicon"] = dialect_lexicon

            def transcribe(self, word):
                return "ipa"

        fake_pkg = type(sys)("arbtok.plugin")
        fake_pkg.ArbtokG2PPlugin = FakePlugin
        monkeypatch.setitem(sys.modules, "arbtok.plugin", fake_pkg)
        cs._arbtok_plugin_cache.clear()

        cs.arbtok_transcribe("كتاب", "arb")

        assert captured["lexicon"] is None
        assert captured["dialect_lexicon"] is False
        cs._arbtok_plugin_cache.clear()

    def test_arbtok_stock_transcribe_uses_default_plugin_config(
            self, monkeypatch):
        # The informational stock column must use arbtok's UNMODIFIED
        # defaults (whatever they are) — it exists specifically to show
        # the full-featured, lexicon-backed number, so it must not
        # secretly strip the lexicon like the ranked column does.
        captured = {}

        class FakePlugin:
            def __init__(self, lang):
                captured["lang"] = lang
                captured["called_with_only_lang"] = True

            def transcribe(self, word):
                return "ipa"

        fake_pkg = type(sys)("arbtok.plugin")
        fake_pkg.ArbtokG2PPlugin = FakePlugin
        fake_lexicon_pkg = type(sys)("arbtok.lexicon")

        class LexiconUnavailable(RuntimeError):
            pass

        class FakeStemLexicon:
            @property
            def entries(self):
                return {"fake": "entry"}  # pre-flight succeeds

        fake_lexicon_pkg.LexiconUnavailable = LexiconUnavailable
        fake_lexicon_pkg.StemLexicon = FakeStemLexicon
        monkeypatch.setitem(sys.modules, "arbtok.plugin", fake_pkg)
        monkeypatch.setitem(sys.modules, "arbtok.lexicon", fake_lexicon_pkg)
        cs._arbtok_stock_plugin_cache.clear()

        result = cs.arbtok_stock_transcribe("كتاب", "arb")

        assert captured["called_with_only_lang"] is True
        assert result == "ipa"
        cs._arbtok_stock_plugin_cache.clear()

    def test_arbtok_stock_transcribe_lets_lexicon_unavailable_propagate(
            self, monkeypatch):
        # C3 round 2: a fake ArbtokG2PPlugin peer that raises
        # LexiconUnavailable directly from transcribe() is FALSE GREEN —
        # the REAL arbtok swallows every diacritizer exception internally
        # (arbtok/plugin.py's _diacritize: blanket
        # ``except Exception: return text``), so LexiconUnavailable never
        # actually reaches transcribe()'s caller; a mock that raises
        # there doesn't exercise the real failure path at all. This test
        # uses the REAL arbtok package (skipped if unavailable) and
        # forces a REAL fetch failure by breaking
        # ``arbtok.lexicon.resolve_source`` — the actual function
        # ``StemLexicon.entries`` calls — so the pre-flight in
        # ``arbtok_stock_transcribe`` (which calls
        # ``StemLexicon().entries`` directly, bypassing arbtok's own
        # swallow-everything diacritizer path entirely) is what must
        # catch this, not arbtok itself.
        pytest.importorskip("arbtok")
        import arbtok.lexicon as real_lexicon

        def broken_resolve_source(source):
            raise OSError("simulated lexicon fetch failure")

        monkeypatch.setattr(real_lexicon, "resolve_source",
                             broken_resolve_source)
        cs._arbtok_stock_plugin_cache.clear()

        with pytest.raises(real_lexicon.LexiconUnavailable):
            cs.arbtok_stock_transcribe("كتاب", "arb")
        cs._arbtok_stock_plugin_cache.clear()

    def test_arbtok_transcribe_ranked_column_survives_broken_stock_lexicon(
            self, monkeypatch):
        # Sanity: the RANKED column (lexicon=None) must be unaffected by
        # a broken stem lexicon — it never touches StemLexicon at all.
        pytest.importorskip("arbtok")
        import arbtok.lexicon as real_lexicon

        def broken_resolve_source(source):
            raise OSError("simulated lexicon fetch failure")

        monkeypatch.setattr(real_lexicon, "resolve_source",
                             broken_resolve_source)
        cs._arbtok_plugin_cache.clear()

        result = cs.arbtok_transcribe("كتاب", "arb")

        assert result is not None
        cs._arbtok_plugin_cache.clear()


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


class TestEspeakRulesBuildVerification:
    """The espeak_rules column must never silently score STOCK espeak-ng.

    build_espeak_rules_only.sh copies espeak-ng's stock compiled data for
    EVERY language and recompiles only the ones it was asked for, so the
    directory existing says nothing about the language being scored. These
    gates exist because a real published board row was fabricated that way:
    the es row read 'espeak 0.1071 / espeak_rules 0.1071' when both numbers
    were stock, because the build's default language list has no es.
    """

    def _manifest(self, tmp_path, body):
        root = tmp_path / "rules"
        (root / "espeak-ng-data").mkdir(parents=True)
        if body is not None:
            (root / cs.ESPEAK_RULES_MANIFEST).write_text(body, encoding="utf-8")
        return root

    def test_no_manifest_at_all_raises(self, monkeypatch, tmp_path):
        root = self._manifest(tmp_path, None)
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(root))
        with pytest.raises(RuntimeError, match="no rules_only_manifest"):
            cs.assert_espeak_rules_built_for("es", "es")

    def test_language_absent_from_manifest_raises(self, monkeypatch, tmp_path):
        root = self._manifest(tmp_path, "# lang\tn\nfr\t100\n")
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(root))
        with pytest.raises(RuntimeError, match="did NOT strip"):
            cs.assert_espeak_rules_built_for("es", "es")

    def test_stripped_but_dict_identical_to_stock_raises(
            self, monkeypatch, tmp_path):
        root = self._manifest(tmp_path, "# lang\tn\nes\t424\n")
        built = root / "espeak-ng-data" / "es_dict"
        built.write_bytes(b"IDENTICAL")
        stock = tmp_path / "stock_es_dict"
        stock.write_bytes(b"IDENTICAL")
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(root))
        monkeypatch.setattr(cs, "_stock_espeak_dict", lambda lang: str(stock))
        with pytest.raises(RuntimeError, match="byte-identical"):
            cs.assert_espeak_rules_built_for("es", "es")

    def test_stripped_and_dict_differs_passes(self, monkeypatch, tmp_path):
        root = self._manifest(tmp_path, "# lang\tn\nes\t424\n")
        (root / "espeak-ng-data" / "es_dict").write_bytes(b"RULES ONLY")
        stock = tmp_path / "stock_es_dict"
        stock.write_bytes(b"STOCK WITH LIST")
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(root))
        monkeypatch.setattr(cs, "_stock_espeak_dict", lambda lang: str(stock))
        assert cs.assert_espeak_rules_built_for("es", "es") == "es"

    def test_zero_stripped_lines_is_a_legitimate_no_op(
            self, monkeypatch, tmp_path):
        """A language shipping no _list/_listx/_extra has nothing to strip, so
        an identical dict is honest there and must NOT raise."""
        root = self._manifest(tmp_path, "# lang\tn\nes\t0\n")
        (root / "espeak-ng-data" / "es_dict").write_bytes(b"SAME")
        stock = tmp_path / "stock_es_dict"
        stock.write_bytes(b"SAME")
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(root))
        monkeypatch.setattr(cs, "_stock_espeak_dict", lambda lang: str(stock))
        assert cs.assert_espeak_rules_built_for("es", "es") == "es"

    def test_unresolvable_stock_path_warns_instead_of_passing_silently(
            self, monkeypatch, tmp_path, capsys):
        """Gate 2 is INCONCLUSIVE when no stock dict can be located. It must
        say so; a check that quietly proves nothing is what let the
        fabricated es row through."""
        root = self._manifest(tmp_path, "# lang\tn\nes\t424\n")
        (root / "espeak-ng-data" / "es_dict").write_bytes(b"RULES ONLY")
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(root))
        monkeypatch.setattr(cs, "_stock_espeak_dict", lambda lang: None)
        monkeypatch.setattr(cs, "ESPEAK_RULES_STRICT", False)
        assert cs.assert_espeak_rules_built_for("es", "es") == "es"
        assert "did not run" in capsys.readouterr().err

    def test_unresolvable_stock_path_raises_under_strict(
            self, monkeypatch, tmp_path):
        root = self._manifest(tmp_path, "# lang\tn\nes\t424\n")
        (root / "espeak-ng-data" / "es_dict").write_bytes(b"RULES ONLY")
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(root))
        monkeypatch.setattr(cs, "_stock_espeak_dict", lambda lang: None)
        monkeypatch.setattr(cs, "ESPEAK_RULES_STRICT", True)
        with pytest.raises(RuntimeError, match="did not run"):
            cs.assert_espeak_rules_built_for("es", "es")

    def test_missing_built_dict_is_also_inconclusive(
            self, monkeypatch, tmp_path, capsys):
        root = self._manifest(tmp_path, "# lang\tn\nes\t424\n")
        stock = tmp_path / "stock_es_dict"
        stock.write_bytes(b"STOCK")
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(root))
        monkeypatch.setattr(cs, "_stock_espeak_dict", lambda lang: str(stock))
        monkeypatch.setattr(cs, "ESPEAK_RULES_STRICT", False)
        assert cs.assert_espeak_rules_built_for("es", "es") == "es"
        assert "does not exist" in capsys.readouterr().err

    def test_dialect_voice_resolves_to_its_dictsource_language(
            self, monkeypatch, tmp_path):
        root = self._manifest(tmp_path, "# lang\tn\nca\t18873\n")
        (root / "espeak-ng-data" / "ca_dict").write_bytes(b"RULES ONLY")
        stock = tmp_path / "stock_ca_dict"
        stock.write_bytes(b"STOCK")
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(root))
        monkeypatch.setattr(cs, "_stock_espeak_dict", lambda lang: str(stock))
        assert cs.assert_espeak_rules_built_for("ca-x-balear", "ca-ba") == "ca"


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
        # A rules-only dir is only trusted when its build manifest names the
        # language (assert_espeak_rules_built_for), so the fixture writes one.
        rules_dir = tmp_path / "rules"
        (rules_dir / "espeak-ng-data").mkdir(parents=True)
        (rules_dir / cs.ESPEAK_RULES_MANIFEST).write_text(
            "# lang\tstripped_exception_lines\n yy\t0\n".replace(" ", ""),
            encoding="utf-8")
        monkeypatch.setattr(cs, "ESPEAK_RULES_DATA_PATH", str(rules_dir))
        monkeypatch.setattr(
            cs, "build_espeak_lexicon_tsv",
            lambda lang: str(tmp_path / "lex.tsv") if lang == "yy" else None)

        def fake_batch(words, voice, data_path=None):
            if data_path == str(rules_dir):
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

        install_fake_o2i(monkeypatch, FakeEngine())
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

        install_fake_o2i(monkeypatch, fake_o2i)

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

        install_fake_o2i(monkeypatch, fake_o2i)

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

        install_fake_o2i(monkeypatch, fake_o2i)
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

        install_fake_o2i(monkeypatch, fake_o2i)
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

        install_fake_o2i(monkeypatch, fake_o2i)
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

        install_fake_o2i(monkeypatch, fake_o2i)
        monkeypatch.setattr(cs, "espeak_available", lambda: True)
        # A local $ESPEAK_RULES_DATA_PATH build (as used by the board-regen
        # skill) would otherwise be probed for this mock language "rr" and
        # raise, since no real rules-only manifest lists it.
        monkeypatch.setattr(cs, "espeak_rules_available", lambda: False)
        monkeypatch.setattr(
            cs, "espeak_batch_transcribe",
            lambda words, voice, data_path=None: {w: "ola" for w in words})

        try:
            row = cs.compare_lang("rr", limit=10)[0]
        finally:
            cs.LANGS.pop("rr", None)

        assert row["espeak_same_source"] is False
        assert row["espeak_per"] == 0.0

    def test_gruut_excluded_on_cmudict_and_ipadict(self, monkeypatch):
        # B1: gruut's bundled en-US lexicon is CMUdict-derived (124,392
        # words, 98.2% coverage of both cmudict and ipadict) — scoring
        # gruut's dictionary LOOKUP against CMUdict-sourced gold is
        # circular, not G2P accuracy, exactly like espeak-vs-its-own-
        # exception-list or ahotts-vs-hitz_basque_ipa above.
        for dataset_name in ("cmudict", "ipadict"):
            pairs = [("ola", "ola")]
            monkeypatch.setattr(
                cs.benchmark, "DATASETS",
                {dataset_name: (lambda lang, limit: pairs, ["en-US"])})
            monkeypatch.setitem(
                cs.LANGS, "en-US",
                {"dataset": (dataset_name, "en-US"), "espeak": None,
                 "epitran": None, "gruut": "en-us"})

            fake_o2i = FakeEngine({"ola": "ola"})

            install_fake_o2i(monkeypatch, fake_o2i)
            monkeypatch.setattr(cs, "gruut_transcribe",
                                 lambda word, lang: "ola")
            monkeypatch.setattr(cs, "gruut_rules_only_available",
                                 lambda lang: True)
            monkeypatch.setattr(cs, "gruut_rules_only_transcribe",
                                 lambda word, lang: "ruleola")

            try:
                row = cs.compare_lang("en-US", limit=10)[0]
            finally:
                cs.LANGS.pop("en-US", None)

            assert row["gruut_per"] is None, dataset_name
            assert row["gruut_n"] == 0, dataset_name
            assert row["gruut_same_source"] is True, dataset_name
            assert cs._cell(row, "gruut") == "same-source", dataset_name
            # gruut_rules bypasses the lexicon entirely, so it is NOT
            # same-source even on cmudict/ipadict — it still measures
            # something real (the g2p fallback model's own accuracy).
            assert row["gruut_rules_per"] is not None, dataset_name

    def test_gruut_not_excluded_on_wikipron(self, monkeypatch):
        # The independent en/en-GB wikipron rows are NOT CMUdict-sourced
        # and must stay a real (non-same-source) comparison.
        pairs = [("ola", "olo")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"wikipron": (lambda lang, limit: pairs, ["en"])})
        monkeypatch.setitem(
            cs.LANGS, "en",
            {"dataset": ("wikipron", "en"), "espeak": None,
             "epitran": None, "gruut": "en-us"})

        fake_o2i = FakeEngine({"ola": "ola"})

        install_fake_o2i(monkeypatch, fake_o2i)
        monkeypatch.setattr(cs, "gruut_transcribe", lambda word, lang: "olo")
        monkeypatch.setattr(cs, "gruut_rules_only_available",
                             lambda lang: True)
        monkeypatch.setattr(cs, "gruut_rules_only_transcribe",
                             lambda word, lang: "olo")

        try:
            row = cs.compare_lang("en", limit=10)[0]
        finally:
            cs.LANGS.pop("en", None)

        assert row["gruut_same_source"] is False
        assert row["gruut_per"] == 0.0


class TestGruutRulesOnly:
    """gruut_rules_only_transcribe disables gruut's lexicon lookup at the
    settings level so every word falls through to its own g2p fallback
    model — mirrors espeak_rules's dictionary-emptied idea."""

    def test_rules_only_produces_different_output_than_lexicon(self):
        # A real, not mocked, check that the mechanism actually works:
        # gruut's en-US lexicon has an irregular entry for "colonel"
        # (/kɜːrnl/-ish); with the lexicon disabled, the g2p fallback
        # must read it off the spelling instead, producing something
        # DIFFERENT from the dictionary pronunciation.
        try:
            import gruut  # noqa: F401
        except ImportError:
            import pytest
            pytest.skip("gruut not installed")
        with_lexicon = cs.gruut_transcribe("colonel", "en_US")
        rules_only = cs.gruut_rules_only_transcribe("colonel", "en_US")
        assert with_lexicon is not None
        assert rules_only is not None
        assert with_lexicon != rules_only

    def test_unavailable_without_gruut(self, monkeypatch):
        monkeypatch.setitem(sys.modules, "gruut", None)
        monkeypatch.delitem(sys.modules, "gruut.text_processor",
                             raising=False)
        assert cs.gruut_rules_only_transcribe("hello", "en_US") is None


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
        assert "### aa" in text
        assert "| d | 2 | 0.1000 | same-source |" in text


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

        install_fake_o2i(monkeypatch, fake_o2i)

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

        install_fake_o2i(monkeypatch, fake_o2i)

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


class TestScoreboardStalenessNoteSampledVsGenuine:
    """B3: pt-PT's PER gap against benchmarks/results.json is NOT
    staleness — scripts/compare_systems.py scores a fixed-seed `sample_n`
    SUBSET while scripts/benchmark.py scores the FULL gold (same seed,
    different word count), so the two will never converge by
    regenerating either side. The note must say so distinctly from a
    genuine drift row, which DOES mean "go regenerate the stale side"."""

    def test_sampled_row_gets_the_different_reason_not_stale(
            self, tmp_path, monkeypatch):
        rows = [
            {"lang": "pt-PT", "dataset": "wikipron", "n": 2272,
             "o2i_per": 0.1346, "sampled": True},
        ]
        sb_path = tmp_path / "results.json"
        sb_path.write_text(json.dumps([
            {"lang": "pt-PT", "dataset": "wikipron", "per": 0.0903,
             "n": 56891},
        ]), encoding="utf-8")
        monkeypatch.setattr(cs.benchmark, "SCOREBOARD_JSON", str(sb_path))

        note = cs._scoreboard_staleness_note(rows)

        assert "not staleness" in note or "DIFFERENT reason" in note
        assert "pt-PT" in note
        assert "56891" in note
        assert "regenerating either side will not reconcile" in note

    def test_genuine_drift_row_still_calls_it_stale(self, tmp_path, monkeypatch):
        rows = [
            {"lang": "xx", "dataset": "d", "n": 100,
             "o2i_per": 0.50, "sampled": False},
        ]
        sb_path = tmp_path / "results.json"
        sb_path.write_text(json.dumps([
            {"lang": "xx", "dataset": "d", "per": 0.10, "n": 100},
        ]), encoding="utf-8")
        monkeypatch.setattr(cs.benchmark, "SCOREBOARD_JSON", str(sb_path))

        note = cs._scoreboard_staleness_note(rows)

        assert "stale" in note
        assert "xx" in note
        assert "not staleness" not in note


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


class TestWinnerColumn:
    """``_winner`` ranks over the LEXICON-FREE world only (owner
    directive: "anything with a lexicon doesn't count as a winner") —
    a lexicon-backed ``espeak``/``gruut`` STOCK value never counts, only
    its rules-only variant (or nothing, if no rules-only number exists
    for that row). Also: calls a near-tie ``tie`` rather than a spurious
    four-decimal win, and never lets a same-source cell win (it is not a
    real comparison)."""

    def test_clear_winner_named(self):
        row = {"o2i_per": 0.10, "espeak_per": 0.30}
        assert cs._winner(row) == "o2i"

    def test_stock_espeak_never_wins_even_when_lowest(self):
        # Mutation-resistant: espeak's LEXICON-BACKED stock value (0.10)
        # is lower than o2i's (0.30), but with no espeak_rules_per given
        # espeak has no lexicon-free representation at all — it must be
        # DROPPED from ranking, not silently fall back to stock. o2i,
        # the only remaining lexicon-free system, wins uncontested.
        # (If the lexicon exclusion in _rules_only_values is deleted or
        # bypassed, this assertion flips to "espeak" and fails.)
        row = {"o2i_per": 0.30, "espeak_per": 0.10}
        assert cs._winner(row) == "o2i"

    def test_espeak_rules_only_wins_over_o2i(self):
        # espeak's RULES-ONLY variant (lexicon-free) genuinely beats o2i
        # — this is the one way "espeak" can appear as a winner: always
        # under its rules-only label, never the bare lexicon-backed one.
        row = {"o2i_per": 0.30, "espeak_per": 0.05, "espeak_rules_per": 0.10}
        assert cs._winner(row) == "espeak rules-only"

    def test_tie_within_tolerance(self):
        # Tie cells must NAME who tied, never a bare "tie" — readability
        # blocker: a reader should not have to open the row to see who.
        row = {"o2i_per": 0.1000, "espeak_rules_per": 0.1005}
        assert cs._winner(row) == "tie (espeak rules-only, o2i)"

    def test_no_system_usable_above_threshold(self):
        # Even the best PER on the row is worse than the "is anyone
        # usable here" threshold — naming a precise "winner" among
        # systems that are all effectively failing the gold is
        # misleading, so the cell says so instead.
        row = {"o2i_per": 1.2, "espeak_rules_per": 1.1}
        assert cs._winner(row) == "no system is usable on this gold"

    def test_just_outside_tolerance_is_not_a_tie(self):
        row = {"o2i_per": 0.1000, "espeak_rules_per": 0.1020}
        assert cs._winner(row) == "o2i"

    def test_same_source_cell_never_wins(self):
        # espeak-ng's own-generated gold scores near-zero by
        # construction; it must not be crowned "winner" over a real o2i
        # number, even under its rules-only label.
        row = {"o2i_per": 0.20, "espeak_rules_per": 0.0,
               "espeak_rules_same_source": True}
        assert cs._winner(row) == "o2i"

    def test_no_comparable_systems_is_na(self):
        row = {"o2i_per": None, "espeak_per": None}
        assert cs._winner(row) == "n/a"

    def test_espeak_rules_label_used(self):
        row = {"o2i_per": 0.5, "espeak_rules_per": 0.1}
        assert cs._winner(row) == "espeak rules-only"

    def test_lexicon_free_engines_rank_at_stock_value(self):
        # epitran/pycotovia/ahotts/africa_g2p are audited lexicon-free —
        # they rank at their normal stock value, no substitution needed.
        row = {"o2i_per": 0.30, "epitran_per": 0.05}
        assert cs._winner(row) == "epitran"

    def test_gruut_stock_never_wins_even_when_lowest(self):
        # Same mutation-resistance guard as espeak, for gruut.
        row = {"o2i_per": 0.30, "gruut_per": 0.05}
        assert cs._winner(row) == "o2i"

    def test_gruut_rules_only_wins_under_its_own_label(self):
        row = {"o2i_per": 0.30, "gruut_per": 0.02, "gruut_rules_per": 0.10}
        assert cs._winner(row) == "gruut rules-only"


class TestLexiconBackedInformationalNoteCoversFamily:
    """C6: _lexicon_backed_informational_note previously only knew about
    espeak/gruut (via _RULES_ONLY_SUBSTITUTES) — tugaphone's and
    arbtok_stock's lexicon-backed wins were silently uncited even though
    both are excluded from ranking exactly like stock espeak/gruut."""

    def test_tugaphone_lexicon_win_is_disclosed(self):
        row = {"tugaphone_per": 0.1887}
        note = cs._lexicon_backed_informational_note(row, ranked_best=0.1951)
        assert "tugaphone with its lexicon scores 0.1887" in note

    def test_arbtok_stock_lexicon_win_is_disclosed(self):
        row = {"arbtok_stock_per": 0.01, "arbtok_stock_same_source": False}
        note = cs._lexicon_backed_informational_note(row, ranked_best=0.05)
        assert "arbtok with its lexicon scores 0.0100" in note

    def test_same_source_lexicon_column_is_not_cited(self):
        # A same-source arbtok_stock cell is not a real number — must
        # never be cited as "would have won".
        row = {"arbtok_stock_per": 0.0, "arbtok_stock_same_source": True}
        note = cs._lexicon_backed_informational_note(row, ranked_best=0.05)
        assert note == ""


class TestLeaderboardLexiconFreeRanking:
    """B2/board-semantics regression guard: the Winner column and the
    leaderboard rank over the LEXICON-FREE world (re-ranking ALL systems
    with rules-only variants substituted in, not just checking o2i
    against espeak_rules in isolation), honour _WINNER_TIE_TOLERANCE,
    and surface a lexicon-backed value that WOULD have won as a named,
    non-ranking informational aside — never silently. Pinned against the
    exact rows a reviewer caught the predecessor of this logic getting
    wrong on: es and ro wrongly claimed an "on rules-only" note
    (epitran actually still wins both under rules-only substitution);
    ca-x-valencia is a tie, not an outright o2i win; ca is a genuine o2i
    #1 flip once espeak's lexicon is excluded from ranking."""

    def test_epitran_still_wins_under_rules_substitution(self, monkeypatch):
        # es/wikipron: o2i=0.0797, espeak_rules=0.1066, epitran=0.0277.
        # epitran (no rules-only variant, keeps its stock value) is still
        # the best PER even after espeak is replaced by espeak_rules.
        row = {"lang": "es", "dataset": "wikipron", "n": 10,
               "o2i_per": 0.0797, "espeak_per": 0.1071,
               "espeak_rules_per": 0.1066, "epitran_per": 0.0277}
        monkeypatch.setitem(cs.LANGS, "es", {"dataset": ("wikipron", "es")})
        lines = cs._leaderboard_summary([row])
        bullet = next(l for l in lines if l.startswith("- **es"))
        assert bullet == "- **es (Spanish)** — epitran #1, o2i #2"

    def test_epitran_still_wins_ro(self, monkeypatch):
        row = {"lang": "ro", "dataset": "wikipron", "n": 10,
               "o2i_per": 0.0342, "espeak_per": 0.0825,
               "espeak_rules_per": 0.0761, "epitran_per": 0.0302}
        monkeypatch.setitem(cs.LANGS, "ro", {"dataset": ("wikipron", "ro")})
        lines = cs._leaderboard_summary([row])
        bullet = next(l for l in lines if l.startswith("- **ro"))
        assert bullet == "- **ro (Romanian)** — epitran #1, o2i #2"

    def test_tie_under_rules_substitution(self, monkeypatch):
        # ca-x-valencia/4catac: o2i=0.0759, espeak_rules=0.0762 (within
        # _WINNER_TIE_TOLERANCE of o2i) — a TIE in the lexicon-free
        # ranking. Regression guard for the reviewed bug: a bare
        # sorted(...)[0] in _leaderboard_line called this row an
        # outright "o2i #1", while _winner() correctly rendered
        # "tie (espeak rules-only, o2i)" for the SAME row — the two
        # must never contradict. This exact-equality assertion FAILS
        # against that pre-fix renderer (which produces
        # "o2i #1 (beats espeak rules-only)"), unlike the previous
        # tautological `"tie" in bullet or "o2i #1" in bullet` check.
        row = {"lang": "ca-x-valencia", "dataset": "4catac", "n": 10,
               "o2i_per": 0.0759, "espeak_per": 0.0439,
               "espeak_rules_per": 0.0762, "epitran_per": 0.3775}
        monkeypatch.setitem(
            cs.LANGS, "ca-x-valencia", {"dataset": ("4catac", "ca-x-valencia")})
        text = "\n".join(cs._leaderboard_summary([row]))
        bullet = next(l for l in text.splitlines()
                       if l.startswith("- **ca-x-valencia"))
        assert bullet == (
            "- **ca-x-valencia (Valencian)** — "
            "tie (espeak rules-only, o2i) #1 "
            "(espeak with its lexicon scores 0.0439 — informational)"
        )
        # The Winner column (_winner) and this leaderboard line must
        # agree on tie-ness for the identical row.
        assert cs._winner(row) == "tie (espeak rules-only, o2i)"

    def test_ca_o2i_flips_to_number_one_once_espeak_lexicon_excluded(
            self, monkeypatch):
        # ca/4catac: o2i clearly beats espeak_rules AND every other
        # system once espeak's lexicon-backed stock value (0.0403, the
        # actual board-committed number) is EXCLUDED from ranking — this
        # is the flip the owner directive names explicitly. Mutation-
        # resistant: if the exclusion of stock espeak is ever removed,
        # espeak (0.0403) beats o2i (0.0643) and this assertion fails.
        row = {"lang": "ca", "dataset": "4catac", "n": 10,
               "o2i_per": 0.0643, "espeak_per": 0.0403,
               "espeak_rules_per": 0.1206, "epitran_per": 0.4641}
        monkeypatch.setitem(cs.LANGS, "ca", {"dataset": ("4catac", "ca")})
        text = "\n".join(cs._leaderboard_summary([row]))
        bullet = next(l for l in text.splitlines()
                       if l.startswith("- **ca "))
        assert "o2i #1" in bullet
        assert "espeak #1" not in bullet

    def test_lexicon_backed_winner_surfaced_as_informational_aside(
            self, monkeypatch):
        # When the lexicon-backed stock value would have scored lowest
        # of all systems, it must still be NAMED (never hidden) as an
        # informational aside — just not counted as the ranked winner.
        row = {"lang": "ca", "dataset": "4catac", "n": 10,
               "o2i_per": 0.0643, "espeak_per": 0.0403,
               "espeak_rules_per": 0.1206, "epitran_per": 0.4641}
        monkeypatch.setitem(cs.LANGS, "ca", {"dataset": ("4catac", "ca")})
        text = "\n".join(cs._leaderboard_summary([row]))
        bullet = next(l for l in text.splitlines()
                       if l.startswith("- **ca "))
        assert "informational" in bullet
        assert "0.0403" in bullet

    def test_no_aside_when_no_lexicon_backed_value_would_have_won(
            self, monkeypatch):
        # o2i already beats even espeak's stock lexicon-backed value —
        # nothing informational to add.
        row = {"lang": "de", "dataset": "wikipron", "n": 10,
               "o2i_per": 0.02, "espeak_per": 0.05,
               "espeak_rules_per": 0.09}
        monkeypatch.setitem(cs.LANGS, "de", {"dataset": ("wikipron", "de")})
        text = "\n".join(cs._leaderboard_summary([row]))
        bullet = next(l for l in text.splitlines()
                       if l.startswith("- **de "))
        assert "informational" not in bullet


class TestLeaderboardSummary:
    """``_leaderboard_summary`` is the compact per-language standings
    block at the top of the doc — built from each language's PRIMARY
    gold row only, one line per language, ranked over the lexicon-free
    world (see ``TestLeaderboardLexiconFreeRanking``)."""

    def test_o2i_number_one_names_runner_up(self, monkeypatch):
        # epitran is audited lexicon-free, so it stays a real rival even
        # with no espeak_rules_per given (espeak itself is excluded).
        rows = [
            {"lang": "it", "dataset": "wikipron", "n": 10,
             "o2i_per": 0.04, "espeak_per": 0.07, "epitran_per": 0.09},
        ]
        monkeypatch.setitem(cs.LANGS, "it", {"dataset": ("wikipron", "it")})
        text = "\n".join(cs._leaderboard_summary(rows))
        assert "**it (Italian)** — o2i #1 (beats epitran)" in text

    def test_o2i_number_one_alone_when_no_lexicon_free_rival(
            self, monkeypatch):
        # espeak has only a lexicon-backed stock value on this row (no
        # espeak_rules_per) — it is EXCLUDED from ranking entirely, not
        # silently kept as a rival, so o2i stands alone as #1.
        rows = [
            {"lang": "it", "dataset": "wikipron", "n": 10,
             "o2i_per": 0.04, "espeak_per": 0.07},
        ]
        monkeypatch.setitem(cs.LANGS, "it", {"dataset": ("wikipron", "it")})
        text = "\n".join(cs._leaderboard_summary(rows))
        assert "**it (Italian)** — o2i #1" in text
        assert "beats" not in text.split("it (Italian)", 1)[1].split("\n", 1)[0]

    def test_o2i_not_first_names_the_winner_and_o2i_rank(self, monkeypatch):
        rows = [
            {"lang": "en-US", "dataset": "cmudict", "n": 10,
             "o2i_per": 0.50, "espeak_per": 0.30,
             "espeak_rules_per": 0.35},
        ]
        monkeypatch.setitem(
            cs.LANGS, "en-US", {"dataset": ("cmudict", "en-US")})
        text = "\n".join(cs._leaderboard_summary(rows))
        assert ("**en-US (American English (General American))** — "
                "espeak rules-only #1, o2i #2") in text
        # espeak's stock (lexicon-backed) 0.30 beats both o2i (0.50) AND
        # espeak_rules (0.35) — it must surface as a named informational
        # aside, never silently.
        bullet = text.split("en-US", 1)[1].split("\n", 1)[0]
        assert "informational" in bullet
        assert "0.3000" in bullet

    def test_only_primary_row_counted_per_language(self, monkeypatch):
        # A language with several registered golds must produce exactly
        # ONE leaderboard line, for its configured primary dataset.
        rows = [
            {"lang": "ca", "dataset": "4catac", "n": 10,
             "o2i_per": 0.06, "espeak_per": 0.04},
            {"lang": "ca", "dataset": "wikipron", "n": 5,
             "o2i_per": 0.25, "espeak_per": 0.22},
        ]
        monkeypatch.setitem(cs.LANGS, "ca", {"dataset": ("4catac", "ca")})
        lines = cs._leaderboard_summary(rows)
        ca_lines = [l for l in lines if l.startswith("- **ca ")]
        assert len(ca_lines) == 1


class TestDetailsBlockPresence:
    """The stale/coverage notes must survive the reorganization as a
    clearly separated, collapsible section at the bottom of the doc —
    honesty content is reorganized, never deleted."""

    def test_details_block_wraps_the_staleness_and_coverage_notes(
            self, tmp_path, monkeypatch):
        rows = [
            {"lang": "aa", "dataset": "d", "n": 2,
             "o2i_per": 0.1, "o2i_n": 2,
             "espeak_per": 0.3, "espeak_n": 2,
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
        assert "<details>" in text
        assert "</details>" in text
        details = text.split("<details>", 1)[1].split("</details>", 1)[0]
        assert "espeak-rules-only coverage" in details or \
            "espeak-rules-only" in details
        assert "Regenerate" in details
        # The details block comes AFTER the main results table, not
        # before it — data first, methodology after.
        assert text.index("### aa") < text.index("<details>")

    def test_stale_note_still_names_the_row(self, tmp_path, monkeypatch):
        # Regression guard: the honest per-row staleness naming
        # (results.json vs a fresh live run) must still be reachable in
        # the regenerated doc, just relocated into the details block.
        rows = [
            {"lang": "aa", "dataset": "d", "n": 2, "o2i_per": 0.5},
        ]
        monkeypatch.setattr(
            cs.benchmark, "SCOREBOARD_JSON", "/nonexistent/path.json")
        note = cs._scoreboard_staleness_note(rows)
        assert "could not be read" in note

        monkeypatch.setitem(cs.LANGS, "aa", {"dataset": ("d", "aa")})
        md_path = tmp_path / "comparison.md"
        json_path = tmp_path / "comparison.json"
        monkeypatch.setattr(cs, "COMPARISON_MD", str(md_path))
        monkeypatch.setattr(cs, "COMPARISON_JSON", str(json_path))
        cs.write_comparison(rows)
        text = md_path.read_text(encoding="utf-8")
        assert note in text


class TestFairComparison2x2SameSourceRendering:
    """B4 regression guard: the 2x2 table's `o2i` column used
    `_fmt(row['o2i_per'])` instead of `_cell(row, 'o2i')`, leaking a
    same-source row's raw (near-zero-by-construction) PER as if it were
    a real number — e.g. pt-PT/portuguese_tts showed `0.0000` instead of
    `same-source`."""

    def test_same_source_o2i_row_renders_same_source_not_zero(self):
        rows = [
            {"lang": "pt-PT", "dataset": "portuguese_tts", "n": 20,
             "o2i_per": 0.0, "o2i_same_source": True,
             "o2i_lex_per": None,
             "espeak_per": 0.3336, "espeak_same_source": False,
             "espeak_rules_per": 0.3331, "espeak_rules_same_source": False},
        ]
        lines = cs._fair_comparison_2x2_lines(rows)
        text = "\n".join(lines)
        row_line = next(l for l in lines if l.startswith("| pt-PT |"))
        assert "same-source" in row_line
        assert "0.0000" not in row_line


class TestEspeakRulesCoverageNote:
    """``_espeak_rules_coverage_note`` names rows that have a stock
    ``espeak`` number but no ``espeak-rules-only`` one yet — the
    staleness-style machinery for the new permanent column, extended
    exactly the way ``_scoreboard_staleness_note`` reports o2i drift."""

    def test_all_covered_reports_clean(self):
        rows = [
            {"lang": "fr", "dataset": "wikipron", "n": 10,
             "espeak_per": 0.07, "espeak_same_source": False,
             "espeak_rules_per": 0.08, "espeak_rules_same_source": False},
        ]
        note = cs._espeak_rules_coverage_note(rows)
        assert note == (
            "Every row with a stock `espeak` number also carries an "
            "`espeak-rules-only` one in this run."
        )

    def test_missing_row_is_named_with_its_n(self):
        rows = [
            {"lang": "fr", "dataset": "wikipron", "n": 10,
             "espeak_per": 0.07, "espeak_same_source": False,
             "espeak_rules_per": 0.08, "espeak_rules_same_source": False},
            {"lang": "ca", "dataset": "vox_communis", "n": 218451,
             "espeak_per": 0.8195, "espeak_same_source": False,
             "espeak_rules_per": None, "espeak_rules_same_source": False},
        ]
        note = cs._espeak_rules_coverage_note(rows)
        assert "1 row(s)" in note
        assert "`ca`/`vox_communis` (n=218451)" in note

    def test_no_espeak_number_at_all_is_not_flagged_missing(self):
        """A row with NO stock espeak number either (no voice mapping, or
        espeak-ng unavailable) has nothing to compare against — it must
        not be reported as a missing espeak-rules-only row, since that
        would fabricate an expectation the row can never meet."""
        rows = [
            {"lang": "arb", "dataset": "arabic_tts", "n": 5,
             "espeak_per": None, "espeak_same_source": False,
             "espeak_rules_per": None, "espeak_rules_same_source": False},
        ]
        note = cs._espeak_rules_coverage_note(rows)
        assert "also carries an" in note

    def test_same_source_espeak_row_is_not_flagged_missing(self):
        rows = [
            {"lang": "en-US", "dataset": "ipa_babylm", "n": 100,
             "espeak_per": 0.0, "espeak_same_source": True,
             "espeak_rules_per": None, "espeak_rules_same_source": True},
        ]
        note = cs._espeak_rules_coverage_note(rows)
        assert "also carries an" in note


class TestWriteComparisonEspeakRulesColumn:
    """The main comparison table renders an ``espeak-rules-only`` column
    for every row, alongside the existing ``espeak`` and ``epitran``
    columns — the schema/rendering change this PR adds on top of the
    already-wired ``espeak_rules_per`` scoring."""

    def test_header_and_populated_cell_rendered(self, tmp_path, monkeypatch):
        rows = [
            {"lang": "fr", "dataset": "wikipron", "n": 2,
             "o2i_per": 0.05, "o2i_n": 2,
             "espeak_per": 0.07, "espeak_n": 2, "espeak_same_source": False,
             "espeak_rules_per": 0.08, "espeak_rules_n": 2,
             "espeak_rules_same_source": False,
             "epitran_per": 0.2, "epitran_n": 2,
             "gruut_per": None, "gruut_n": 0,
             "provenance_tier": "crowd-scraped",
             "harness_version": "1.0", "limit": 10},
        ]
        monkeypatch.setitem(cs.LANGS, "fr", {"dataset": ("wikipron", "fr")})
        md_path = tmp_path / "comparison.md"
        json_path = tmp_path / "comparison.json"
        monkeypatch.setattr(cs, "COMPARISON_MD", str(md_path))
        monkeypatch.setattr(cs, "COMPARISON_JSON", str(json_path))

        cs.write_comparison(rows)

        text = md_path.read_text(encoding="utf-8")
        assert "espeak rules-only" in text
        assert "### fr" in text
        assert "| wikipron | 2 | 0.0500 | 0.0700 | 0.0800 | 0.2000" in text

    def test_missing_cell_renders_n_a_not_blank(self, tmp_path, monkeypatch):
        # Two rows for the same language: "wikipron" has no epitran number
        # while "cmudict" does, so the epitran column is NOT all-n/a for
        # the "fr" group and stays in the table — letting us pin that the
        # wikipron row's own missing epitran cell renders "n/a", not a
        # blank or an omitted cell. espeak_rules_per is None on BOTH rows,
        # so that column IS all-n/a for the group and is dropped per the
        # per-group column-omission rule.
        rows = [
            {"lang": "fr", "dataset": "wikipron", "n": 2,
             "o2i_per": 0.05, "o2i_n": 2,
             "espeak_per": 0.07, "espeak_n": 2, "espeak_same_source": False,
             "espeak_rules_per": None, "espeak_rules_n": 0,
             "espeak_rules_same_source": False,
             "epitran_per": None, "epitran_n": 0,
             "gruut_per": None, "gruut_n": 0,
             "provenance_tier": "crowd-scraped",
             "harness_version": "1.0", "limit": 10},
            {"lang": "fr", "dataset": "cmudict", "n": 3,
             "o2i_per": 0.06, "o2i_n": 3,
             "espeak_per": 0.08, "espeak_n": 3, "espeak_same_source": False,
             "espeak_rules_per": None, "espeak_rules_n": 0,
             "espeak_rules_same_source": False,
             "epitran_per": 0.3, "epitran_n": 3,
             "gruut_per": None, "gruut_n": 0,
             "provenance_tier": "crowd-scraped",
             "harness_version": "1.0", "limit": 10},
        ]
        monkeypatch.setitem(cs.LANGS, "fr", {"dataset": ("wikipron", "fr")})
        md_path = tmp_path / "comparison.md"
        json_path = tmp_path / "comparison.json"
        monkeypatch.setattr(cs, "COMPARISON_MD", str(md_path))
        monkeypatch.setattr(cs, "COMPARISON_JSON", str(json_path))

        cs.write_comparison(rows)

        text = md_path.read_text(encoding="utf-8")
        assert "### fr" in text
        assert "| wikipron | 2 | 0.0500 | 0.0700 | n/a |" in text
        assert "| cmudict | 3 | 0.0600 | 0.0800 | 0.3000 |" in text
        # espeak_rules had no data at all for this group -> column dropped,
        # not shown as a wall of n/a.
        fr_section = text.split("### fr", 1)[1].split("###", 1)[0]
        assert "espeak rules-only" not in fr_section
        assert ("2 row(s) have a stock `espeak` number but no "
                "`espeak-rules-only`") in text


# ─── lexicon-backed tier ────────────────────────────────────────────────────
#
# The tier's whole validity rests on ONE thing: each engine's key set must
# be its REAL lookup keys, matched with that engine's OWN lookup-time
# normalization. These tests therefore hit the extractors against small
# fixtures shaped like each engine's real data, then the union filter, the
# residual-gold guard, and the renderer's separation from the primary
# leaderboard.


def _fake_module(name, **attrs):
    """A throwaway module object for sys.modules-based import doubles."""
    import types
    mod = types.ModuleType(name)
    for key, value in attrs.items():
        setattr(mod, key, value)
    return mod


class TestEspeakLexiconKeys:
    def test_extracts_lowercased_headwords_from_dictsource(
            self, monkeypatch, tmp_path):
        (tmp_path / "en_list").write_text(
            "the      D@\n"
            "Paris    p'ariIs   // a proper noun\n"
            "_lig     ligature\n"
            "$nounf   directive\n"
            "a        01\n"
            "// comment only\n",
            encoding="utf-8")
        (tmp_path / "en_extra").write_text("Extra  Ekstr@\n", encoding="utf-8")
        monkeypatch.setattr(cs, "ESPEAK_DICTSOURCE_PATH", str(tmp_path))
        monkeypatch.setattr(cs, "espeak_available", lambda: False)

        keys = cs.espeak_lexicon_keys("en", {})

        # Headwords only, lowercased; directives, comments and the
        # single-letter "spell this letter" entries are not vocabulary.
        assert keys.keys == frozenset({"the", "paris", "extra"})
        assert keys.provenance["engine"] == "espeak-ng"
        assert keys.provenance["count"] == 3
        # Machine-independent: an absolute scratch-clone path in the
        # provenance would land in the committed doc and make it
        # unreproducible on another machine.
        assert str(tmp_path) not in keys.provenance["source"]

    def test_no_dictsource_path_means_no_key_set(self, monkeypatch):
        monkeypatch.setattr(cs, "ESPEAK_DICTSOURCE_PATH", None)
        assert cs.espeak_lexicon_keys("en", {}) is None

    def test_unmapped_language_means_no_key_set(self, monkeypatch, tmp_path):
        monkeypatch.setattr(cs, "ESPEAK_DICTSOURCE_PATH", str(tmp_path))
        assert cs.espeak_lexicon_keys("xx-unmapped", {}) is None


class TestGruutLexiconKeys:
    def _make_db(self, tmp_path, words):
        import sqlite3
        path = tmp_path / "lexicon.db"
        con = sqlite3.connect(path)
        con.execute("CREATE TABLE word_phonemes "
                    "(id INTEGER, word TEXT, pron_order INTEGER, "
                    "phonemes TEXT, role TEXT)")
        for i, word in enumerate(words):
            con.execute("INSERT INTO word_phonemes VALUES (?,?,?,?,?)",
                        (i, word, 0, "x", ""))
        con.commit()
        con.close()
        return path

    def test_extracts_word_column_from_lexicon_db(self, monkeypatch, tmp_path):
        self._make_db(tmp_path, ["the", "the", "Paris"])
        monkeypatch.setitem(
            sys.modules, "gruut_lang_en",
            _fake_module("gruut_lang_en",
                          __file__=str(tmp_path / "__init__.py")))

        keys = cs.gruut_lexicon_keys("en-us", {})

        assert keys.keys == frozenset({"the", "paris"})
        assert keys.provenance["engine"] == "gruut"

    def test_missing_language_package_means_no_key_set(self, monkeypatch):
        monkeypatch.setitem(sys.modules, "gruut_lang_zz", None)
        assert cs.gruut_lexicon_keys("zz", {}) is None


class TestTugaphoneLexiconKeys:
    def test_extracts_tugalex_headwords_for_the_lects_region(
            self, monkeypatch):
        class FakeLexicon:
            def get_ipa_map(self, region):
                assert region == "lbx"
                return {"Casa": "ˈka·zɐ", "pão": "ˈpɐ̃w"}

        monkeypatch.setitem(sys.modules, "tugalex",
                            _fake_module("tugalex", TugaLexicon=FakeLexicon))
        monkeypatch.setitem(
            sys.modules, "tugaphone.registry",
            _fake_module("tugaphone.registry",
                          resolve_lect=lambda lang: "pt-PT",
                          lexicon_region=lambda lect: "lbx"))

        keys = cs.tugaphone_lexicon_keys("pt-PT", {"tugaphone": "pt-PT"})

        # Matched on o2i's OWN lexicon key (NFC + language-aware lower) —
        # tugalex entries are consumed through register_lexicon, so a
        # case-sensitive match would readmit every capitalised headword.
        assert "casa" in keys.keys
        assert "pão" in keys.keys
        assert keys.provenance["count"] == 2

    def test_lect_without_a_region_has_no_key_set(self, monkeypatch):
        monkeypatch.setitem(sys.modules, "tugalex",
                            _fake_module("tugalex", TugaLexicon=object))
        monkeypatch.setitem(
            sys.modules, "tugaphone.registry",
            _fake_module("tugaphone.registry",
                          resolve_lect=lambda lang: "pt-XX",
                          lexicon_region=lambda lect: None))
        assert cs.tugaphone_lexicon_keys("pt-XX", {"tugaphone": "pt-XX"}) is None


class TestArbtokStockLexiconKeys:
    def _install(self, monkeypatch, stems, dialect, source_path="/tmp/x.tsv"):
        class FakeStem:
            entries = stems

        class FakeDialect:
            def __init__(self, lang):
                self.lang = lang

            @property
            def entries(self):
                return dialect

        monkeypatch.setitem(
            sys.modules, "arbtok.lexicon",
            _fake_module("arbtok.lexicon",
                          DEFAULT_LEXICON="hf://Org/repo/ar-stems.tsv",
                          StemLexicon=FakeStem,
                          resolve_source=lambda src: source_path))
        monkeypatch.setitem(
            sys.modules, "arbtok.dialect_lexicon",
            _fake_module("arbtok.dialect_lexicon", DialectLexicon=FakeDialect))

    def test_unions_stem_and_dialect_lexicons_and_records_revision(
            self, monkeypatch):
        self._install(
            monkeypatch,
            stems={"كتاب": "كِتَاب"},
            dialect={"كي": "كِي"},
            source_path="/cache/hub/datasets--Org--repo/snapshots/deadbeef/"
                        "ar-stems.tsv")

        keys = cs.arbtok_stock_lexicon_keys("ar", {"arbtok": "ar-MA"})

        assert keys.keys == frozenset({"كتاب", "كي"})
        assert keys.provenance["revision"] == "deadbeef"
        assert "ar-MA" in keys.provenance["source"]

    def test_unmapped_language_has_no_key_set(self, monkeypatch):
        assert cs.arbtok_stock_lexicon_keys("fr", {"arbtok": None}) is None


class TestO2iLexLexiconKeys:
    def test_reads_the_registered_overlays_own_words(
            self, monkeypatch, tmp_path):
        tsv = tmp_path / "en.tsv"
        tsv.write_text("The\tðə\nParis\tˈpæɹɪs\n", encoding="utf-8")
        monkeypatch.setattr(cs, "build_espeak_lexicon_tsv",
                             lambda lang: str(tsv))

        keys = cs.o2i_lex_lexicon_keys("en", {})

        # o2i participates symmetrically: its own overlay is filtered out
        # of the residual gold like everyone else's lexicon.
        assert keys.keys == frozenset({"the", "paris"})

    def test_absent_overlay_has_no_key_set(self, monkeypatch):
        monkeypatch.setattr(cs, "build_espeak_lexicon_tsv", lambda lang: None)
        assert cs.o2i_lex_lexicon_keys("en", {}) is None


class TestNoLexiconEngines:
    def test_lattice_only_engines_declare_an_empty_key_set(self):
        keys = cs._no_lexicon_keys("pt-PT", {})
        assert keys.keys == frozenset()
        assert keys.provenance["count"] == 0

    def test_hf_revision_of_non_hf_path_is_none(self):
        assert cs._hf_revision_of("/data/local/ar-stems.tsv") is None


class TestLexiconKeysCaching:
    def test_second_call_reads_the_cache_instead_of_re_extracting(
            self, monkeypatch, tmp_path):
        monkeypatch.setattr(cs, "LEXICON_KEY_CACHE_DIR", str(tmp_path))
        calls = []

        def extractor(lang, cfg):
            calls.append(lang)
            return cs.LexiconKeys(frozenset({"casa"}), {
                "engine": "fake", "source": "fixture", "version": "1.2.3",
                "count": 1, "normalization": "NFC + lowercase"})

        monkeypatch.setattr(cs, "_fixture_keys", extractor, raising=False)
        spec = cs.LexiconTierEngine("espeak", "fake (stock)",
                                     "_fixture_keys", "_nfc_lower_keyed")

        first = cs.lexicon_keys_for(spec, "pt-PT", {})
        second = cs.lexicon_keys_for(spec, "pt-PT", {})

        assert calls == ["pt-PT"]
        assert first.keys == second.keys == frozenset({"casa"})
        # Provenance survives the round trip — a published tier number must
        # be able to name the exact lexicon version it was filtered against.
        assert second.provenance["version"] == "1.2.3"

    def test_absent_source_is_not_cached_as_an_empty_lexicon(
            self, monkeypatch, tmp_path):
        monkeypatch.setattr(cs, "LEXICON_KEY_CACHE_DIR", str(tmp_path))
        monkeypatch.setattr(cs, "_fixture_keys", lambda lang, cfg: None,
                             raising=False)
        spec = cs.LexiconTierEngine("espeak", "fake (stock)",
                                     "_fixture_keys", "_nfc_lower_keyed")

        assert cs.lexicon_keys_for(spec, "pt-PT", {}) is None
        assert not list(tmp_path.iterdir())


def _tier_fixture(monkeypatch, tmp_path, keys_by_engine, words,
                  results=None, min_gold=None):
    """Wire a two-engine tier over *words* with fixed lexicon key sets."""
    monkeypatch.setattr(cs, "LEXICON_KEY_CACHE_DIR", str(tmp_path))
    specs = []
    for i, (engine, keyset) in enumerate(keys_by_engine.items()):
        name = f"_fixture_keys_{i}"
        monkeypatch.setattr(
            cs, name,
            lambda lang, cfg, keyset=keyset: cs.LexiconKeys(
                frozenset(keyset),
                {"engine": engine, "source": f"fixture:{engine}",
                 "version": "0", "count": len(keyset),
                 "normalization": "NFC + lowercase"}),
            raising=False)
        specs.append(cs.LexiconTierEngine(engine, f"{engine} (stock)", name,
                                           "_nfc_lower_keyed"))
    monkeypatch.setattr(cs, "LEXICON_TIER_ENGINES", specs)
    if min_gold is not None:
        monkeypatch.setattr(cs, "LEXICON_TIER_MIN_GOLD", min_gold)
    if results is None:
        results = {s.key: [(w, [w]) for w in words] for s in specs}
    return cs._lexicon_tier_for_row("xx", {}, words, results)


class TestLexiconTierUnionFilter:
    def test_gold_is_filtered_against_the_union_of_every_lexicon(
            self, monkeypatch, tmp_path):
        words = ["alpha", "beta", "gamma", "delta"]
        tier = _tier_fixture(
            monkeypatch, tmp_path,
            {"espeak": {"alpha"}, "gruut": {"beta"}}, words, min_gold=1)

        # UNION, not intersection: a word in ANY compared lexicon is a
        # lookup for that engine and must not be scored for anyone.
        assert tier["filtered_n"] == 2
        assert tier["lexicon_hits"] == {"espeak": 1, "gruut": 1}
        assert tier["n"] == 4

    def test_per_is_computed_on_the_residual_gold_only(
            self, monkeypatch, tmp_path):
        words = ["alpha", "beta"]
        # espeak is perfect on the word its own lexicon covers and wrong on
        # the residual one: a tier that failed to filter would report 0.0.
        results = {
            "espeak": [("alpha", ["alpha"]), ("xxxx", ["beta"])],
            "gruut": [("zzzzz", ["alpha"]), ("beta", ["beta"])],
        }
        tier = _tier_fixture(monkeypatch, tmp_path,
                             {"espeak": {"alpha"}, "gruut": set()},
                             words, results=results, min_gold=1)

        assert tier["filtered_n"] == 1
        assert tier["per"]["espeak"] > 0.0
        assert tier["per"]["gruut"] == 0.0
        assert cs._lexicon_tier_winner(tier) == "gruut (stock)"


class TestLexiconTierResidualGuard:
    def test_row_below_the_minimum_is_marked_insufficient_not_ranked(
            self, monkeypatch, tmp_path):
        words = [f"w{i}" for i in range(60)]
        tier = _tier_fixture(monkeypatch, tmp_path,
                             {"espeak": set(words[:20]), "gruut": set()},
                             words)

        assert tier["filtered_n"] == 40
        assert tier["insufficient_residual_gold"] is True
        assert tier["per"] == {}
        assert cs._lexicon_tier_winner(tier) == "insufficient residual gold (< 50)"

    def test_row_at_the_minimum_is_ranked(self, monkeypatch, tmp_path):
        words = [f"w{i}" for i in range(60)]
        tier = _tier_fixture(monkeypatch, tmp_path,
                             {"espeak": set(words[:10]), "gruut": set()},
                             words)

        assert tier["filtered_n"] == 50
        assert tier["insufficient_residual_gold"] is False
        assert tier["per"]["espeak"] == 0.0


class TestLexiconTierEngineGate:
    def test_one_engine_is_not_a_comparison(self, monkeypatch, tmp_path):
        assert _tier_fixture(monkeypatch, tmp_path, {"espeak": set()},
                             ["alpha"], min_gold=1) is None

    def test_engine_whose_lexicon_cannot_be_enumerated_is_dropped(
            self, monkeypatch, tmp_path):
        # The bug this guards: keeping such an engine in the tier with an
        # empty filter would publish its raw dictionary-lookup number as if
        # it had generalized.
        monkeypatch.setattr(cs, "LEXICON_KEY_CACHE_DIR", str(tmp_path))
        monkeypatch.setattr(cs, "_fixture_none", lambda lang, cfg: None,
                             raising=False)
        monkeypatch.setattr(
            cs, "_fixture_some",
            lambda lang, cfg: cs.LexiconKeys(frozenset(), {
                "engine": "g", "source": "s", "version": "0", "count": 0,
                "normalization": "NFC + lowercase"}),
            raising=False)
        monkeypatch.setattr(cs, "LEXICON_TIER_ENGINES", [
            cs.LexiconTierEngine("espeak", "espeak (stock)", "_fixture_none",
                                  "_nfc_lower_keyed"),
            cs.LexiconTierEngine("gruut", "gruut (stock)", "_fixture_some",
                                  "_nfc_lower_keyed"),
        ])
        words = ["alpha"]
        results = {"espeak": [("alpha", ["alpha"])],
                   "gruut": [("alpha", ["alpha"])]}

        # Only gruut survives -> fewer than two engines -> no tier at all.
        assert cs._lexicon_tier_for_row("xx", {}, words, results) is None


class TestLexiconTierRendering:
    def _rows(self):
        return [
            {"lang": "pt-PT", "dataset": "ep_dialects", "n": 100,
             "o2i_per": 0.10, "o2i_n": 100, "o2i_same_source": False,
             "espeak_per": 0.20, "espeak_n": 100,
             "espeak_same_source": False,
             "espeak_rules_per": 0.30, "espeak_rules_n": 100,
             "espeak_rules_same_source": False,
             "tugaphone_per": 0.05, "tugaphone_n": 100,
             "tugaphone_same_source": False,
             "provenance_tier": "expert-human", "harness_version": "1.0",
             "limit": "full",
             "lexicon_tier": {
                 "engines": ["espeak", "tugaphone"],
                 "n": 100, "filtered_n": 70,
                 "insufficient_residual_gold": False, "min_gold": 50,
                 "lexicon_hits": {"espeak": 10, "tugaphone": 25},
                 "lexicon_sizes": {"espeak": 500, "tugaphone": 90000},
                 "provenance": {
                     "espeak": {"engine": "espeak-ng", "source": "dictsource",
                                 "version": "1.52.0", "count": 500,
                                 "normalization": "NFC + lowercase"},
                     "tugaphone": {"engine": "tugaphone (tugalex)",
                                    "source": "tugalex", "version": "0.9",
                                    "count": 90000,
                                    "normalization": "o2i lexicon key"},
                 },
                 "per": {"espeak": 0.2500, "tugaphone": 0.1500},
                 "per_n": {"espeak": 70, "tugaphone": 70},
             }},
        ]

    def test_tier_has_its_own_labelled_section_and_winner(self):
        lines = cs._lexicon_backed_tier_lines(self._rows())
        text = "\n".join(lines)

        assert ("## Lexicon-backed tier — gold filtered against all "
                "compared lexicons") in text
        assert "| 100 | 70 |" in text
        assert "tugaphone (stock)" in text
        assert "10 (of 500 entries)" in text
        assert "25 (of 90000 entries)" in text
        assert "version `1.52.0`" in text

    def test_tier_never_leaks_into_the_primary_leaderboard(
            self, monkeypatch, tmp_path):
        rows = self._rows()
        monkeypatch.setitem(cs.LANGS, "pt-PT",
                            {"dataset": ("ep_dialects", "pt-PT")})
        md_path = tmp_path / "comparison.md"
        monkeypatch.setattr(cs, "COMPARISON_MD", str(md_path))
        monkeypatch.setattr(cs, "COMPARISON_JSON",
                             str(tmp_path / "comparison.json"))

        cs.write_comparison(rows, catalan_voices=None)
        text = md_path.read_text(encoding="utf-8")

        leaderboard = text.split("## Leaderboard", 1)[1].split("##", 1)[0]
        # The primary ranking is lexicon-FREE: espeak ranks as its
        # rules-only twin and no "(stock)" tier label may appear.
        assert "(stock)" not in leaderboard
        assert "o2i #1 (beats espeak rules-only)" in leaderboard
        # And the tier section sits below, on its own.
        assert text.index("## Leaderboard") < text.index(
            "## Lexicon-backed tier")

    def test_winner_column_ignores_the_tier_block_entirely(self):
        row = self._rows()[0]
        # tugaphone wins the tier (0.15) but is lexicon-backed, so the
        # primary Winner column must still rank the lexicon-free world.
        assert cs._lexicon_tier_winner(row["lexicon_tier"]) == \
            "tugaphone (stock)"
        assert cs._winner(row) == "o2i"

    def test_no_tier_rows_render_no_section(self):
        assert cs._lexicon_backed_tier_lines(
            [{"lang": "fr", "dataset": "wikipron", "lexicon_tier": None}]) == []


class TestEspeakLexiconKeysVoiceFallback:
    def test_row_without_a_dictsource_table_entry_uses_its_espeak_voice(
            self, monkeypatch, tmp_path):
        (tmp_path / "pt_list").write_text("casa  kaz@\n", encoding="utf-8")
        monkeypatch.setattr(cs, "ESPEAK_DICTSOURCE_PATH", str(tmp_path))
        monkeypatch.setattr(cs, "espeak_available", lambda: False)

        # pt-PT is not in DICTSOURCE_LANG; dropping it from the tier over
        # that would leave tugaphone unopposed on the only language where
        # two lexicon-carrying engines actually meet.
        keys = cs.espeak_lexicon_keys("pt-PT", {"espeak": "pt"})

        assert keys.keys == frozenset({"casa"})


class TestLexiconTierExtractionIsGated:
    def test_a_row_that_cannot_have_a_tier_extracts_nothing(
            self, monkeypatch, tmp_path):
        # arbtok's extraction fetches a 145k-entry lexicon over the
        # network; a single-engine row must never pay that cost.
        monkeypatch.setattr(cs, "LEXICON_KEY_CACHE_DIR", str(tmp_path))
        calls = []
        monkeypatch.setattr(cs, "_fixture_counted",
                             lambda lang, cfg: calls.append(lang),
                             raising=False)
        monkeypatch.setattr(cs, "LEXICON_TIER_ENGINES", [
            cs.LexiconTierEngine("arbtok_stock", "arbtok (stock)",
                                  "_fixture_counted", "_arbtok_lexicon_key"),
            cs.LexiconTierEngine("espeak", "espeak (stock)",
                                  "_fixture_counted", "_nfc_lower_keyed"),
        ])

        assert cs._lexicon_tier_for_row(
            "ar", {}, ["كتاب"], {"arbtok_stock": [("k", ["k"])]}) is None
        assert calls == []


class TestLexiconTierSentenceGold:
    def test_a_sentence_containing_a_looked_up_word_is_filtered_out(
            self, monkeypatch, tmp_path):
        words = ["bom dia como está", "o gato dorme", "chove muito hoje"]
        tier = _tier_fixture(monkeypatch, tmp_path,
                             {"espeak": {"dia"}, "tugaphone": {"gato"}},
                             words, min_gold=1)

        # A lexicon is consulted per WORD inside a sentence: matching only
        # whole entries would score both sentences as lexicon-free.
        assert tier["filtered_n"] == 1
        assert tier["lexicon_hits"] == {"espeak": 1, "tugaphone": 1}


class TestO2iLexOverlayIsActuallyConsulted:
    """C1 regression: the ``o2i_lex`` overlay was registered under the
    CONFIGURED code while ``G2P._override_for`` looks it up under the
    RESOLVED lect (``G2P("en").lang == "en-GB"``), so the overlay was
    never consulted and every published ``o2i_lex`` number was silently
    plain o2i."""

    def test_o2i_lex_differs_from_o2i_when_the_overlay_covers_gold(
            self, monkeypatch, tmp_path):
        pairs = [("colonel", "ˈkɜːnəl")]
        monkeypatch.setattr(
            cs.benchmark, "DATASETS",
            {"fake_en": (lambda lang, limit: pairs, ["en"])})
        monkeypatch.setitem(
            cs.LANGS, "en",
            {"dataset": ("fake_en", "en"), "espeak": None, "epitran": None,
             "gruut": None})

        registered = {}

        class AliasEngine:
            """A G2P whose configured code ("en") resolves to "en-GB" —
            the exact alias shape the bug hid in."""

            lang = "en-GB"

            def transcribe_word(self, word):
                entry = registered.get(self.lang, {}).get(word)
                return entry if entry is not None else "WRONG"

        def on_register(code, source):
            registered[code] = {"colonel": "ˈkɜːnəl"}

        install_fake_o2i(monkeypatch, AliasEngine(), on_register=on_register,
                          on_clear=lambda: registered.clear())
        tsv = tmp_path / "en.tsv"
        tsv.write_text("colonel\tˈkɜːnəl\n", encoding="utf-8")
        monkeypatch.setattr(cs, "build_espeak_lexicon_tsv",
                             lambda lang: str(tsv))

        row = cs.compare_lang("en", limit=10)[0]

        # Registered under the RESOLVED lect, so the overlay is reachable.
        assert row["o2i_lex_per"] == 0.0
        assert row["o2i_per"] > 0.0
        assert row["o2i_lex_per"] != row["o2i_per"]

    def test_lexicon_code_is_the_engines_resolved_lect(self):
        class Engine:
            lang = "en-GB"

        assert cs._o2i_lexicon_code(Engine(), "en") == "en-GB"
        assert cs._o2i_lexicon_code(object(), "en") == "en"


class TestEspeakWordlistLeadingConditionals:
    """C2 regression: espeak-ng writes a conditional BEFORE the headword
    (``?3 accursed ...``), and skipping those lines dropped 288 English /
    210 Portuguese headwords straight back into the tier's residual gold
    as words espeak-ng really does look up."""

    def test_a_conditional_entry_keeps_its_headword(
            self, monkeypatch, tmp_path):
        (tmp_path / "en_list").write_text(
            "?3 accursed   @k3:sId\n"
            "?!2 pretence  prI'tEns\n"
            "$nounf        directive\n"
            "_lig          ligature\n"
            "plain         pleIn\n",
            encoding="utf-8")

        words = cs._parse_espeak_wordlist_words(str(tmp_path), "en")

        assert words == ["accursed", "plain", "pretence"]


class TestLexiconKeysFingerprintCoversEveryVersion:
    """C3 regression: a version left out of the fingerprint reads a stale
    key set back AND publishes the stale version string beside it."""

    def _fingerprint(self):
        spec = cs.LexiconTierEngine("gruut", "gruut (stock)",
                                     "gruut_lexicon_keys", "_nfc_lower_keyed")
        return cs._lexicon_keys_fingerprint(spec, "en")

    def test_bumping_the_gruut_package_version_changes_the_fingerprint(
            self, monkeypatch):
        before = self._fingerprint()
        real = cs._installed_version
        monkeypatch.setattr(
            cs, "_installed_version",
            lambda dist: "99.0.0" if dist == "gruut_lang_en" else real(dist))
        assert self._fingerprint() != before

    def test_bumping_the_espeak_version_changes_the_fingerprint(
            self, monkeypatch):
        before = self._fingerprint()
        monkeypatch.setattr(cs, "_espeak_version", lambda: "99.99.99")
        assert self._fingerprint() != before


class TestLexiconCoversPunctuatedSentences:
    """C4 regression: splitting a sentence on whitespace alone left
    ``Olá,`` attached to its comma, which matches no lexicon key."""

    def test_a_punctuated_sentence_word_still_counts_as_covered(
            self, monkeypatch, tmp_path):
        words = ["Olá, amigos", "chove muito"]
        tier = _tier_fixture(monkeypatch, tmp_path,
                             {"espeak": {"olá"}, "tugaphone": set()},
                             words, min_gold=1)

        assert tier["filtered_n"] == 1
        assert tier["lexicon_hits"]["espeak"] == 1


class TestO2iLexProvenanceNamesTheRunningTree:
    """C5 regression: the provenance recorded the INSTALLED wheel's
    version, not the tree the run actually imported."""

    def test_provenance_version_is_the_imported_modules_version(
            self, monkeypatch, tmp_path):
        tsv = tmp_path / "en.tsv"
        tsv.write_text("the\tðə\n", encoding="utf-8")
        monkeypatch.setattr(cs, "build_espeak_lexicon_tsv",
                             lambda lang: str(tsv))
        monkeypatch.setattr(cs, "_running_o2i_version", lambda: "9.9.9-tree")
        monkeypatch.setattr(cs, "_installed_version",
                             lambda dist: "0.0.1-wheel")

        keys = cs.o2i_lex_lexicon_keys("en", {})

        assert keys.provenance["version"] == "9.9.9-tree"
