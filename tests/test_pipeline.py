"""A Pipeline belongs to one engine, and no other engine can see it.

The expected values come from three places: the lexicon entries the test writes,
the spec JSON read straight from the data directory, and the textbook
transcriptions of the probe words (pt-PT ⟨gato⟩ [ˈɡatu], es-ES ⟨cantaba⟩
[kanˈtaβa]).
"""
from __future__ import annotations

import json
import logging
import os
import re
import subprocess
import sys
import warnings
from dataclasses import FrozenInstanceError
from pathlib import Path
from typing import List, Optional

import pytest

import orthography2ipa
from orthography2ipa import (
    G2P,
    Pipeline,
    SyllabifierPlugin,
    detect_stress,
    emission_inventory,
    get,
    load_lexicon,
    packaged_lexicon,
    phoneme_inventory,
)
from orthography2ipa import lexicon as lexmod
from orthography2ipa.inventory import phoneme_atoms, tokenize
from orthography2ipa.markup import MarkupError

pytestmark = pytest.mark.filterwarnings("ignore::DeprecationWarning")

GROUP = "orthography2ipa.lexicons"
PACKAGE = Path(orthography2ipa.__file__).parent

GATO_RULES = "ˈɡatu"
GATO_ENTRY = "ˈɡaʃtɐ"
GATO_OTHER = "ˈɡɔtɔ"
CANTABA_RULES = "kanˈtaβa"
# The mark is anchored from the end of the word, so a division that gives one
# syllable puts it on the last transcribed syllable.
CANTABA_ONE_SYLLABLE = "kantaˈβa"
# A click: no Portuguese table emits it, so only a lexicon can declare it.
CLICK = "ʘ"


@pytest.fixture(autouse=True)
def _no_process_lexicon(monkeypatch):
    monkeypatch.delenv(lexmod.LEXICON_DIR_ENV, raising=False)
    lexmod.clear_lexicons()
    yield
    lexmod.clear_lexicons()


def tsv(tmp_path, name, *rows):
    path = tmp_path / name
    path.write_text("".join(f"{w}\t{ipa}\n" for w, ipa in rows), encoding="utf-8")
    return path


class _Dist:
    name = "fake-lexicons"


class _EntryPoint:
    group = GROUP
    dist = _Dist()

    def __init__(self, name, provider):
        self.name = name
        self.value = f"fake-lexicons:{name}"
        self.provider = provider

    def load(self):
        return self.provider


@pytest.fixture
def installed(monkeypatch):
    """The entry points the test appends, and nothing else, are installed."""
    points: List[_EntryPoint] = []
    monkeypatch.setattr(
        lexmod, "entry_points",
        lambda group=None: list(points) if group == GROUP else [])
    lexmod.clear_lexicons()
    return points


@pytest.fixture
def pt_package(installed, tmp_path):
    path = tsv(tmp_path, "pt-PT.tsv", ("gato", GATO_ENTRY))
    installed.append(_EntryPoint("pt-PT", lambda code: path))
    return path


# ─── the defect: one engine's lexicon reached every other engine ────────────

def test_plain_engine_keeps_output_after_another_engine_takes_a_lexicon(pt_package):
    assert G2P("pt-PT").transcribe_word("gato") == GATO_RULES

    other = G2P("pt-PT", pipeline=Pipeline(lexicon=packaged_lexicon("pt-PT")))

    assert other.transcribe_word("gato") == GATO_ENTRY
    assert G2P("pt-PT").transcribe_word("gato") == GATO_RULES
    assert lexmod.available_lexicon_codes() == []


def test_engines_with_different_lexicons_run_side_by_side():
    first = G2P("pt-PT", pipeline=Pipeline(lexicon={"gato": GATO_ENTRY}))
    second = G2P("pt-PT", pipeline=Pipeline(lexicon={"gato": GATO_OTHER}))
    plain = G2P("pt-PT")

    for _ in range(2):
        assert first.transcribe_word("gato") == GATO_ENTRY
        assert second.transcribe_word("gato") == GATO_OTHER
        assert plain.transcribe_word("gato") == GATO_RULES


# ─── precedence: spec.word_exceptions > pipeline lexicon > rules ────────────

def test_word_exceptions_beat_the_pipeline_lexicon():
    spec_json = json.loads((PACKAGE / "data" / "pt-PT.json").read_text(encoding="utf-8"))
    word, inline = next(iter(spec_json["word_exceptions"].items()))

    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={word: CLICK}))

    assert engine.transcribe_word(word) == inline


def test_pipeline_lexicon_beats_the_rules():
    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={"gato": GATO_ENTRY}))
    assert engine.transcribe_word("gato") == GATO_ENTRY


def test_a_word_outside_the_pipeline_lexicon_takes_the_rules():
    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={"cão": "ˈkɐ̃w̃"}))
    assert engine.transcribe_word("gato") == GATO_RULES


def test_pipeline_lexicon_replaces_the_process_lexicon(tmp_path):
    lexmod.register_lexicon("pt-PT", str(tsv(
        tmp_path, "global.tsv", ("gato", GATO_OTHER), ("rato", GATO_OTHER))))

    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={"gato": GATO_ENTRY}))

    assert engine.transcribe_word("gato") == GATO_ENTRY
    assert engine.transcribe_word("rato") == "ˈʁatu"


def test_empty_pipeline_lexicon_is_a_lexicon_with_no_entries(tmp_path):
    lexmod.register_lexicon("pt-PT", str(tsv(tmp_path, "global.tsv", ("gato", GATO_OTHER))))

    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={}))

    assert engine.transcribe_word("gato") == GATO_RULES


def test_pipeline_without_a_lexicon_reads_the_process_lexicon(tmp_path):
    lexmod.register_lexicon("pt-PT", str(tsv(tmp_path, "global.tsv", ("gato", GATO_OTHER))))

    assert G2P("pt-PT", pipeline=Pipeline()).transcribe_word("gato") == GATO_OTHER
    assert G2P("pt-PT").transcribe_word("gato") == GATO_OTHER


def test_the_lexicon_report_scores_rules_and_lexicon_on_separate_engines(tmp_path, monkeypatch):
    sys.path.insert(0, str(PACKAGE.parent / "scripts"))
    try:
        import benchmark
    finally:
        sys.path.pop(0)
    tsv(tmp_path, "pt-PT.tsv", ("gato", GATO_OTHER))
    monkeypatch.setitem(benchmark._WIKIPRON_FILES, "pt-PT", "unused")
    monkeypatch.setattr(benchmark, "load_wikipron",
                        lambda tag, limit: [("gato", GATO_OTHER), ("rato", "ˈʁatu")])

    (row,) = benchmark.build_lexicon_report(str(tmp_path), None)

    assert (row["lexicon"], row["lang"], row["lexicon_entries"]) == ("pt-PT", "pt-PT", 1)
    assert row["n_covered"] == 1
    assert row["per_with_lexicon_covered"] == 0.0
    # ɡ a t u against ɡ ɔ t ɔ: two of the four phones differ.
    assert row["per_rules_only_covered"] == 0.5
    assert lexmod.available_lexicon_codes() == []


# ─── a hit takes the same path as a word exception ──────────────────────────

def test_an_entry_with_no_mark_gets_the_stress_of_the_spec():
    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={"gato": "ɡaʃtɐ"}))
    assert engine.transcribe_word("gato") == GATO_ENTRY


def test_a_hit_is_found_through_case_and_edge_punctuation():
    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={"gato": GATO_ENTRY}))
    assert engine.transcribe("Gato,") == GATO_ENTRY


def test_a_hit_reports_full_confidence():
    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={"gato": GATO_ENTRY}))
    assert engine.transcribe_detailed("gato").words[0].confidence == 1.0


# ─── load_lexicon and packaged_lexicon return a mapping and set no state ────

def test_load_lexicon_returns_the_file_entries(tmp_path):
    path = tsv(tmp_path, "x.tsv", ("gato", GATO_ENTRY), ("gato", GATO_OTHER), ("rato", "ˈʁatu"))

    assert load_lexicon(str(path)) == {"gato": GATO_ENTRY, "rato": "ˈʁatu"}
    assert load_lexicon(path) == {"gato": GATO_ENTRY, "rato": "ˈʁatu"}


def test_load_lexicon_sets_no_state(tmp_path):
    load_lexicon(tsv(tmp_path, "pt-PT.tsv", ("gato", GATO_ENTRY)))

    assert lexmod.available_lexicon_codes() == []
    assert G2P("pt-PT").transcribe_word("gato") == GATO_RULES


def test_load_lexicon_raises_for_a_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError, match="absent.tsv"):
        load_lexicon(tmp_path / "absent.tsv")


def test_packaged_lexicon_returns_the_provider_entries(pt_package):
    assert packaged_lexicon("pt-PT") == {"gato": GATO_ENTRY}


def test_packaged_lexicon_resolves_an_alias_and_names_the_provider_code(installed, tmp_path):
    path = tsv(tmp_path, "pt-PT.tsv", ("gato", GATO_ENTRY))
    seen = []
    installed.append(_EntryPoint("pt-PT", lambda code: seen.append(code) or path))

    assert packaged_lexicon("pt") == {"gato": GATO_ENTRY}
    assert seen == ["pt-PT"]


def test_packaged_lexicon_raises_with_no_provider(pt_package):
    with pytest.raises(LookupError, match="en-GB.*pt-PT"):
        packaged_lexicon("en-GB")


def test_packaged_lexicon_raises_when_the_provider_fails(installed, caplog):
    def broken(code):
        raise RuntimeError("no data")

    installed.append(_EntryPoint("pt-PT", broken))

    with caplog.at_level(logging.WARNING, logger="orthography2ipa.lexicon"):
        with pytest.raises(LookupError, match="pt-PT"):
            packaged_lexicon("pt-PT")
    assert "no data" in caplog.text


# ─── the inventory counts the engine's lexicon ──────────────────────────────

def test_engine_inventory_counts_its_own_lexicon():
    forced = f'<phoneme ph="{CLICK}a">x</phoneme>'
    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={"x": f"{CLICK}a", "y": CLICK}))

    assert engine.transcribe(forced) == f"{CLICK}a"
    with pytest.raises(MarkupError, match=CLICK):
        G2P("pt-PT").transcribe(forced)


def test_engine_inventory_ignores_the_process_lexicon(tmp_path):
    lexmod.register_lexicon("pt-PT", str(tsv(tmp_path, "global.tsv", ("gato", CLICK))))
    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={}))

    with pytest.raises(MarkupError, match=CLICK):
        engine.transcribe(f'<phoneme ph="{CLICK}">x</phoneme>')


def test_inventory_functions_read_the_mapping_they_are_given(tmp_path):
    spec = get("pt-PT")
    lexicon = {"x": f"{CLICK}a"}

    assert f"{CLICK}a" in emission_inventory(spec, lexicon)
    assert f"{CLICK}a" not in emission_inventory(spec)
    assert CLICK not in phoneme_inventory(spec)
    assert f"{CLICK}a" in phoneme_atoms(spec, lexicon)
    assert tokenize(f"{CLICK}a", spec, lexicon) == [f"{CLICK}a"]
    assert tokenize(f"{CLICK}a", spec) == [CLICK, "a"]

    lexmod.register_lexicon("pt-PT", str(tsv(tmp_path, "global.tsv", ("gato", "ǃ"))))
    assert "ǃ" in emission_inventory(spec)
    assert "ǃ" not in emission_inventory(spec, lexicon)
    assert "ǃ" not in emission_inventory(spec, {})


# ─── the syllabifier ────────────────────────────────────────────────────────

class _Fixed(SyllabifierPlugin):
    """Answers with the division it was given, and records its calls."""

    def __init__(self, division: Optional[List[str]]) -> None:
        self.division = division
        self.calls: List[tuple] = []

    def syllabify(self, word: str, lang: Optional[str] = None) -> List[str]:
        self.calls.append((word, lang))
        if self.division is None:
            raise ValueError("cannot split")
        return self.division

    @property
    def language_codes(self) -> List[str]:
        return ["es-ES"]


ONE_SYLLABLE = ["cantaba"]
RULES_DIVISION = ["can", "ta", "ba"]


def test_an_installed_syllabifier_changes_no_transcription(tmp_path):
    """A distribution on the path declares the entry point, and a fresh process
    is where discovery would find it."""
    (tmp_path / "one_syllable.py").write_text(
        "from orthography2ipa import SyllabifierPlugin\n"
        "class OneSyllable(SyllabifierPlugin):\n"
        "    language_codes = ['es-ES']\n"
        "    def syllabify(self, word, lang=None):\n"
        "        return [word]\n", encoding="utf-8")
    info = tmp_path / "one_syllable-1.0.dist-info"
    info.mkdir()
    (info / "METADATA").write_text(
        "Metadata-Version: 2.1\nName: one-syllable\nVersion: 1.0\n", encoding="utf-8")
    (info / "entry_points.txt").write_text(
        "[orthography2ipa.syllabify]\none = one_syllable:OneSyllable\n", encoding="utf-8")
    code = "from orthography2ipa import G2P; print(G2P('es-ES').transcribe_word('cantaba'))"

    done = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True, check=True,
        env={**os.environ, "PYTHONPATH": os.pathsep.join([str(tmp_path), str(PACKAGE.parent)])})

    assert done.stdout.strip() == CANTABA_RULES


def test_pipeline_syllabifier_answers_for_its_engine():
    mine = _Fixed(ONE_SYLLABLE)
    engine = G2P("es-ES", pipeline=Pipeline(syllabifier=mine))

    assert engine.transcribe_word("cantaba") == CANTABA_ONE_SYLLABLE
    assert mine.calls == [("cantaba", "es-ES")]


def test_engine_with_no_syllabifier_uses_the_bundled_splitter():
    mine = _Fixed(ONE_SYLLABLE)
    G2P("es-ES", pipeline=Pipeline(syllabifier=mine)).transcribe_word("cantaba")

    assert G2P("es-ES").transcribe_word("cantaba") == CANTABA_RULES
    assert mine.calls == [("cantaba", "es-ES")]


def test_engines_with_different_syllabifiers_run_side_by_side():
    first = G2P("es-ES", pipeline=Pipeline(syllabifier=_Fixed(ONE_SYLLABLE)))
    second = G2P("es-ES", pipeline=Pipeline(syllabifier=_Fixed(RULES_DIVISION)))

    for _ in range(2):
        assert first.transcribe_word("cantaba") == CANTABA_ONE_SYLLABLE
        assert second.transcribe_word("cantaba") == CANTABA_RULES


@pytest.mark.parametrize("division", [["x"], [], None])
def test_a_word_the_syllabifier_cannot_split_goes_to_the_bundled_splitter(division):
    mine = _Fixed(division)
    engine = G2P("es-ES", pipeline=Pipeline(syllabifier=mine))

    assert engine.transcribe_word("cantaba") == CANTABA_RULES
    assert mine.calls == [("cantaba", "es-ES")]


def test_detect_stress_takes_the_syllabifier():
    rules = get("es-ES").stress
    mine = _Fixed(ONE_SYLLABLE)

    assert detect_stress("cantaba", rules, lang="es-ES") == 1
    assert detect_stress("cantaba", rules, lang="es-ES", syllabifier=mine) == 0
    assert detect_stress("cantaba", rules, syllabifier=mine) == 0
    assert mine.calls == [("cantaba", "es-ES"), ("cantaba", None)]


# ─── the object ─────────────────────────────────────────────────────────────

def test_pipeline_is_frozen():
    pipeline = Pipeline(lexicon={"gato": GATO_ENTRY})
    with pytest.raises(FrozenInstanceError):
        pipeline.lexicon = {}


# ─── the process-wide API is deprecated and still works ─────────────────────

def _removal_version() -> str:
    text = (PACKAGE / "version.py").read_text(encoding="utf-8")
    major = int(re.search(r"VERSION_MAJOR = (\d+)", text).group(1))
    return f"{major + 1}.0.0"


def _warns(name: str):
    return pytest.warns(
        DeprecationWarning,
        match=rf"{re.escape(name)} is deprecated and will be removed in "
              rf"{re.escape(_removal_version())}")


def test_register_lexicon_warns_and_works(tmp_path):
    path = tsv(tmp_path, "pt-PT.tsv", ("gato", GATO_ENTRY))
    with _warns("register_lexicon"):
        lexmod.register_lexicon("pt-PT", str(path))
    assert G2P("pt-PT").transcribe_word("gato") == GATO_ENTRY


def test_set_lexicon_dir_warns_and_works(tmp_path):
    tsv(tmp_path, "pt-PT.tsv", ("gato", GATO_ENTRY))
    with _warns("set_lexicon_dir"):
        lexmod.set_lexicon_dir(tmp_path)
    assert G2P("pt-PT").transcribe_word("gato") == GATO_ENTRY


def test_lexicon_dir_variable_warns_and_works(tmp_path, monkeypatch):
    tsv(tmp_path, "pt-PT.tsv", ("gato", GATO_ENTRY))
    monkeypatch.setenv(lexmod.LEXICON_DIR_ENV, str(tmp_path))
    with _warns(f"${lexmod.LEXICON_DIR_ENV}"):
        assert G2P("pt-PT").transcribe_word("gato") == GATO_ENTRY


def test_use_packaged_lexicons_warns_and_works(pt_package):
    with _warns("use_packaged_lexicons"):
        assert lexmod.use_packaged_lexicons(["pt-PT"]) == ["pt-PT"]
    assert G2P("pt-PT").transcribe_word("gato") == GATO_ENTRY


def test_clear_lexicons_warns_and_works(tmp_path):
    lexmod.register_lexicon("pt-PT", str(tsv(tmp_path, "pt-PT.tsv", ("gato", GATO_ENTRY))))
    with _warns("clear_lexicons"):
        lexmod.clear_lexicons()
    assert G2P("pt-PT").transcribe_word("gato") == GATO_RULES


def test_get_syllabifier_warns_and_finds_nothing():
    with _warns("get_syllabifier"):
        assert orthography2ipa.get_syllabifier("pt-PT") is None


def test_get_lexicon_warns_and_works(tmp_path):
    lexmod.register_lexicon("pt-PT", str(tsv(tmp_path, "pt-PT.tsv", ("gato", GATO_ENTRY))))
    with _warns("get_lexicon"):
        assert orthography2ipa.get_lexicon("pt-PT") == {"gato": GATO_ENTRY}


def test_the_new_path_warns_about_nothing(pt_package):
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        lexicon = packaged_lexicon("pt-PT")
        assert load_lexicon(pt_package) == lexicon
        assert lexmod.packaged_lexicon_sources() == {"pt-PT": pt_package}
        engine = G2P("pt-PT", pipeline=Pipeline(lexicon=lexicon))
        assert engine.transcribe("gato") == GATO_ENTRY
        assert engine.transcribe("rato") == "ˈʁatu"
        assert G2P("pt-PT").transcribe("gato") == GATO_RULES
        assert phoneme_inventory(get("pt-PT"))
