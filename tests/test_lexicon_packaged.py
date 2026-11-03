"""Packaged lexicons: discoverable when installed, used only when enabled.

A package such as ``o2i-lexicons`` declares one entry point per language code
in the ``orthography2ipa.lexicons`` group. Installing it changes no output; the
caller enables it with ``use_packaged_lexicons``. The tests replace
``importlib.metadata.entry_points`` with test doubles, so they need no such
package installed.
"""
from __future__ import annotations

import ast
import logging
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import g2p as g2p_module
from orthography2ipa import lexicon as lexmod
from orthography2ipa.registry import available_json_codes

GROUP = "orthography2ipa.lexicons"
REPO = Path(__file__).resolve().parent.parent


class _Dist:
    def __init__(self, name):
        self.name = name


class _EntryPoint:
    """An ``importlib.metadata.EntryPoint`` double that counts its loads."""

    def __init__(self, name, provider, dist="fake-lexicons"):
        self.name = name
        self.value = f"{dist}:{name}"
        self.group = GROUP
        self.dist = _Dist(dist)
        self.provider = provider
        self.loads = 0

    def load(self):
        self.loads += 1
        return self.provider


@pytest.fixture
def providers(monkeypatch):
    """Install the given entry points as the only ``orthography2ipa.lexicons``."""
    calls = []
    installed = []

    def fake_entry_points(group=None):
        calls.append(group)
        return list(installed) if group == GROUP else []

    # raising=False keeps the fixture usable on a lexicon module that never
    # reads entry points, so a missing feature fails on behaviour.
    monkeypatch.setattr(lexmod, "entry_points", fake_entry_points, raising=False)
    lexmod.clear_lexicons()
    yield installed, calls
    lexmod.clear_lexicons()


def tsv(tmp_path, name, body):
    path = tmp_path / name
    path.write_text(body, encoding="utf-8")
    return path


# English ⟨yacht⟩ is /jɒt/, which the en-GB rules do not give from the spelling;
# ⟨colonel⟩ is /ˈkɜːnəl/. Each fixture lexicon holds these, so a hit is visible.
YACHT = "jɒt"
COLONEL = "ˈkɜːnəl"
WORDS = ["yacht", "colonel", "nation", "the", "choir"]


@pytest.fixture
def installed_en(providers, tmp_path):
    """An installed, not enabled, en-GB provider."""
    installed, calls = providers
    path = tsv(tmp_path, "en-GB.tsv", f"colonel\t{COLONEL}\nyacht\t{YACHT}\n")
    ep = _EntryPoint("en-GB", lambda code: path)
    installed.append(ep)
    return ep, calls, path


def rules_only(monkeypatch, words, code="en-GB"):
    with monkeypatch.context() as m:
        m.setattr(g2p_module, "get_lexicon", lambda c: {})
        return [orthography2ipa.G2P(code).transcribe_word(w) for w in words]


# ─── installed, not enabled: nothing changes ────────────────────────────────

def test_installed_provider_changes_no_output(installed_en, monkeypatch):
    ep, calls, _ = installed_en
    got = [orthography2ipa.G2P("en-GB").transcribe_word(w) for w in WORDS]
    assert lexmod.available_lexicon_codes() == []
    assert {c: lexmod.get_lexicon(c) for c in available_json_codes()
            if lexmod.get_lexicon(c)} == {}
    assert calls == []            # transcription never reads the entry points
    assert ep.loads == 0
    assert got == rules_only(monkeypatch, WORDS)
    assert got[0] != "ˈ" + YACHT


def test_installed_provider_is_discoverable(installed_en):
    ep, calls, path = installed_en
    assert lexmod.packaged_lexicon_sources() == {"en-GB": path}
    assert calls == [GROUP]
    assert lexmod.available_lexicon_codes() == []   # listed, still not enabled
    assert lexmod.get_lexicon("en-GB") == {}


# ─── enabled ────────────────────────────────────────────────────────────────

def test_enabled_lexicon_is_used(installed_en):
    assert orthography2ipa.use_packaged_lexicons() == ["en-GB"]
    assert lexmod.get_lexicon("en-GB") == {"colonel": COLONEL, "yacht": YACHT}
    assert orthography2ipa.G2P("en-GB").transcribe_word("yacht") == "ˈ" + YACHT
    assert orthography2ipa.G2P("en").transcribe_word("yacht") == "ˈ" + YACHT
    assert lexmod.available_lexicon_codes() == ["en-GB"]


def test_enable_by_code_and_by_alias(installed_en):
    assert orthography2ipa.use_packaged_lexicons(["en"]) == ["en-GB"]
    assert orthography2ipa.G2P("en-GB").transcribe_word("colonel") == COLONEL


def test_enabling_a_code_with_no_provider_raises(installed_en):
    with pytest.raises(LookupError, match=r"\['pt-PT'\]"):
        orthography2ipa.use_packaged_lexicons(["pt-PT"])
    assert lexmod.available_lexicon_codes() == []


def test_provider_loads_only_for_its_own_language(installed_en):
    ep, calls, _ = installed_en
    orthography2ipa.use_packaged_lexicons()
    lexmod.get_lexicon("pt-PT")
    assert ep.loads == 0
    lexmod.get_lexicon("en-GB")
    lexmod.get_lexicon("en-GB")
    assert ep.loads == 1
    assert calls == [GROUP]       # discovered once


def test_provider_is_called_with_its_entry_point_name(providers, tmp_path):
    installed, _ = providers
    asked = []
    path = tsv(tmp_path, "en-GB.tsv", f"yacht\t{YACHT}\n")
    installed.append(_EntryPoint("en-GB", lambda code: asked.append(code) or path))
    orthography2ipa.use_packaged_lexicons()
    lexmod.get_lexicon("en-GB")
    assert asked == ["en-GB"]


def test_clear_disables_the_packaged_lexicon(installed_en, monkeypatch):
    orthography2ipa.use_packaged_lexicons()
    assert orthography2ipa.G2P("en-GB").transcribe_word("yacht") == "ˈ" + YACHT
    lexmod.clear_lexicons()
    assert lexmod.available_lexicon_codes() == []
    assert [orthography2ipa.G2P("en-GB").transcribe_word(w) for w in WORDS] == \
        rules_only(monkeypatch, WORDS)


# ─── precedence: word_exceptions > register / dir > packaged > rules ────────

def test_registered_lexicon_beats_packaged(installed_en, tmp_path):
    orthography2ipa.use_packaged_lexicons()
    assert orthography2ipa.G2P("en-GB").transcribe_word("colonel") == COLONEL
    lexmod.register_lexicon("en-GB", str(tsv(tmp_path, "mine.tsv", "colonel\tkɝnəl\n")))
    assert orthography2ipa.G2P("en-GB").transcribe_word("colonel") == "ˈkɝnəl"


def test_lexicon_dir_beats_packaged(installed_en, tmp_path):
    orthography2ipa.use_packaged_lexicons()
    assert orthography2ipa.G2P("en-GB").transcribe_word("colonel") == COLONEL
    d = tmp_path / "dir"
    d.mkdir()
    tsv(d, "en-GB.tsv", "colonel\tkɝnəl\n")
    lexmod.set_lexicon_dir(d)
    assert orthography2ipa.G2P("en-GB").transcribe_word("colonel") == "ˈkɝnəl"


def test_spec_word_exceptions_beat_packaged(providers, tmp_path):
    installed, _ = providers
    assert orthography2ipa.get("en-GB").word_exceptions["the"] == "ðə"
    packaged = tsv(tmp_path, "packaged.tsv", f"colonel\t{COLONEL}\nthe\tθiː\n")
    installed.append(_EntryPoint("en-GB", lambda code: packaged))
    orthography2ipa.use_packaged_lexicons()
    engine = orthography2ipa.G2P("en-GB")
    assert engine.transcribe_word("colonel") == COLONEL
    assert engine.transcribe_word("the") == "ðə"


# ─── providers that cannot be used ──────────────────────────────────────────

def test_provider_for_an_unregistered_code_is_skipped(providers, tmp_path, caplog):
    installed, _ = providers
    path = tsv(tmp_path, "x.tsv", f"yacht\t{YACHT}\n")
    installed.append(_EntryPoint("en-GB-x-nowhere", lambda code: path))
    with caplog.at_level(logging.WARNING, logger=lexmod.__name__):
        assert orthography2ipa.use_packaged_lexicons() == []
    assert "names no registered spec" in caplog.text
    assert lexmod.get_lexicon("en-GB") == {}


def test_failing_provider_falls_back_to_rules(providers, caplog):
    installed, _ = providers

    def broken(code):
        raise RuntimeError("data missing")

    installed.append(_EntryPoint("en-GB", broken))
    orthography2ipa.use_packaged_lexicons()
    with caplog.at_level(logging.WARNING, logger=lexmod.__name__):
        assert lexmod.get_lexicon("en-GB") == {}
    assert "data missing" in caplog.text
    assert lexmod.packaged_lexicon_sources() == {}


def test_provider_returning_a_missing_file_is_ignored(providers, tmp_path, caplog):
    installed, _ = providers
    installed.append(_EntryPoint("en-GB", lambda code: tmp_path / "gone.tsv"))
    orthography2ipa.use_packaged_lexicons()
    with caplog.at_level(logging.WARNING, logger=lexmod.__name__):
        assert lexmod.get_lexicon("en-GB") == {}
    assert "not a file" in caplog.text


def test_exact_code_provider_wins_over_an_alias(providers, tmp_path, caplog):
    installed, _ = providers
    alias = tsv(tmp_path, "en.tsv", "colonel\tkɝnəl\n")
    exact = tsv(tmp_path, "en-GB.tsv", f"colonel\t{COLONEL}\n")
    installed.append(_EntryPoint("en", lambda code: alias, dist="a-lexicons"))
    installed.append(_EntryPoint("en-GB", lambda code: exact, dist="z-lexicons"))
    with caplog.at_level(logging.WARNING, logger=lexmod.__name__):
        orthography2ipa.use_packaged_lexicons()
        assert lexmod.get_lexicon("en-GB") == {"colonel": COLONEL}
    assert "both serve 'en-GB'" in caplog.text


# ─── the board stays rules-only ─────────────────────────────────────────────

def test_the_benchmark_never_enables_packaged_lexicons():
    """The board is scored without packaged lexicons, whatever is installed,
    because the harness never makes the one call that enables them."""
    tree = ast.parse((REPO / "scripts" / "benchmark.py").read_text(encoding="utf-8"))
    names = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    names |= {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
    names |= {a.name for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)
              for a in n.names}
    assert "use_packaged_lexicons" not in names
