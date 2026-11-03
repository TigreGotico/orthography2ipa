"""Default lexicons that an installed package supplies through entry points.

A package such as ``o2i-lexicons`` declares one entry point per language code
in the ``orthography2ipa.lexicons`` group. The tests replace
``importlib.metadata.entry_points`` with test doubles, so they need no such
package installed.
"""
from __future__ import annotations

import logging

import pytest

import orthography2ipa
from orthography2ipa import lexicon as lexmod
from orthography2ipa.registry import available_json_codes

GROUP = "orthography2ipa.lexicons"


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
    # reads entry points, so a missing discovery fails on behaviour.
    monkeypatch.setattr(lexmod, "entry_points", fake_entry_points, raising=False)
    lexmod.clear_lexicons()
    yield installed, calls
    lexmod.clear_lexicons()


def tsv(tmp_path, name, body):
    path = tmp_path / name
    path.write_text(body, encoding="utf-8")
    return path


# The rules give 'ˈkɒlənəl' for ⟨colonel⟩ and 'ˈkɒnʃəns' for ⟨conscience⟩;
# each fixture lexicon below says something else, so a hit is visible.
COLONEL = "ˈkɜːnəl"


def test_no_provider_gives_every_spec_an_empty_lexicon(providers):
    assert lexmod.available_lexicon_codes() == []
    assert {code: lexmod.get_lexicon(code) for code in available_json_codes()
            if lexmod.get_lexicon(code)} == {}


def test_no_provider_output_equals_rules_only(providers, monkeypatch):
    words = ["colonel", "nation", "the", "choir", "yacht"]
    with_discovery = [orthography2ipa.G2P("en-GB").transcribe_word(w) for w in words]
    from orthography2ipa import g2p as g2p_module
    monkeypatch.setattr(g2p_module, "get_lexicon", lambda code: {})
    rules_only = [orthography2ipa.G2P("en-GB").transcribe_word(w) for w in words]
    assert with_discovery == rules_only


def test_packaged_lexicon_is_used(providers, tmp_path):
    installed, _ = providers
    path = tsv(tmp_path, "en-GB.tsv", f"colonel\t{COLONEL}\n")
    installed.append(_EntryPoint("en-GB", lambda code: path))
    assert lexmod.get_lexicon("en-GB") == {"colonel": COLONEL}
    assert orthography2ipa.G2P("en-GB").transcribe_word("colonel") == COLONEL
    assert lexmod.available_lexicon_codes() == ["en-GB"]


def test_provider_is_called_with_its_entry_point_name(providers, tmp_path):
    installed, _ = providers
    asked = []
    path = tsv(tmp_path, "en-GB.tsv", f"colonel\t{COLONEL}\n")
    installed.append(_EntryPoint("en-GB", lambda code: asked.append(code) or path))
    lexmod.get_lexicon("en-GB")
    assert asked == ["en-GB"]


def test_discovery_waits_for_the_first_lookup(providers, tmp_path):
    installed, calls = providers
    path = tsv(tmp_path, "en-GB.tsv", f"colonel\t{COLONEL}\n")
    ep = _EntryPoint("en-GB", lambda code: path)
    installed.append(ep)
    orthography2ipa.G2P("en-GB")
    orthography2ipa.get("en-GB")
    assert calls == []
    lexmod.get_lexicon("pt-PT")
    assert calls == [GROUP]
    assert ep.loads == 0          # another language does not load this provider
    lexmod.get_lexicon("en-GB")
    lexmod.get_lexicon("en-GB")
    assert calls == [GROUP]       # discovered once per process
    assert ep.loads == 1


def test_bare_code_provider_serves_the_resolved_spec(providers, tmp_path):
    installed, _ = providers
    path = tsv(tmp_path, "en.tsv", f"colonel\t{COLONEL}\n")
    installed.append(_EntryPoint("en", lambda code: path))
    assert orthography2ipa.G2P("en").transcribe_word("colonel") == COLONEL
    assert orthography2ipa.G2P("en-GB").transcribe_word("colonel") == COLONEL


# ─── precedence: word_exceptions > register / dir > packaged > rules ────────

def test_registered_lexicon_beats_packaged(providers, tmp_path):
    installed, _ = providers
    packaged = tsv(tmp_path, "packaged.tsv", f"colonel\t{COLONEL}\n")
    installed.append(_EntryPoint("en-GB", lambda code: packaged))
    assert orthography2ipa.G2P("en-GB").transcribe_word("colonel") == COLONEL
    lexmod.register_lexicon("en-GB", str(tsv(tmp_path, "mine.tsv", "colonel\tkɝnəl\n")))
    assert orthography2ipa.G2P("en-GB").transcribe_word("colonel") == "ˈkɝnəl"


def test_lexicon_dir_beats_packaged(providers, tmp_path):
    installed, _ = providers
    packaged = tsv(tmp_path, "packaged.tsv", f"colonel\t{COLONEL}\n")
    installed.append(_EntryPoint("en-GB", lambda code: packaged))
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
    engine = orthography2ipa.G2P("en-GB")
    assert engine.transcribe_word("colonel") == COLONEL
    assert engine.transcribe_word("the") == "ðə"


def test_packaged_beats_rules(providers, tmp_path):
    installed, _ = providers
    rules = orthography2ipa.G2P("en-GB").transcribe_word("colonel")
    assert rules != COLONEL
    path = tsv(tmp_path, "en-GB.tsv", f"colonel\t{COLONEL}\n")
    installed.append(_EntryPoint("en-GB", lambda code: path))
    lexmod.clear_lexicons()
    assert orthography2ipa.G2P("en-GB").transcribe_word("colonel") == COLONEL


# ─── providers that cannot be used ──────────────────────────────────────────

def test_provider_for_an_unregistered_code_is_skipped(providers, tmp_path, caplog):
    installed, _ = providers
    path = tsv(tmp_path, "x.tsv", f"colonel\t{COLONEL}\n")
    installed.append(_EntryPoint("en-GB-x-nowhere", lambda code: path))
    with caplog.at_level(logging.WARNING, logger=lexmod.__name__):
        assert lexmod.get_lexicon("en-GB") == {}
    assert "names no registered spec" in caplog.text
    assert lexmod.available_lexicon_codes() == []


def test_failing_provider_falls_back_to_rules(providers, caplog):
    installed, _ = providers

    def broken(code):
        raise RuntimeError("data missing")

    installed.append(_EntryPoint("en-GB", broken))
    rules = orthography2ipa.G2P("pt-PT").transcribe_word("casa")
    with caplog.at_level(logging.WARNING, logger=lexmod.__name__):
        assert lexmod.get_lexicon("en-GB") == {}
    assert "data missing" in caplog.text
    assert orthography2ipa.G2P("pt-PT").transcribe_word("casa") == rules


def test_provider_returning_a_missing_file_is_ignored(providers, tmp_path, caplog):
    installed, _ = providers
    installed.append(_EntryPoint("en-GB", lambda code: tmp_path / "gone.tsv"))
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
        assert lexmod.get_lexicon("en-GB") == {"colonel": COLONEL}
    assert "both serve 'en-GB'" in caplog.text
