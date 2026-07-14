"""The lexicon overlay is supplied by the caller, never bundled.

A word lexicon is a corpus, not a description of a language, so the library
ships none. The caller registers one from a local file, a URL, or a Hugging
Face id, and an unregistered language behaves exactly as if this module did not
exist.
"""
from __future__ import annotations

import pytest

import orthography2ipa
from orthography2ipa.lexicon import (
    available_lexicon_codes,
    clear_lexicons,
    get_lexicon,
    lexicon_path,
    register_lexicon,
    resolve_lexicon_source,
    set_lexicon_dir,
)


@pytest.fixture(autouse=True)
def _no_lexicons():
    """Every test starts and ends with nothing registered."""
    clear_lexicons()
    yield
    clear_lexicons()


@pytest.fixture
def tsv(tmp_path):
    p = tmp_path / "en-GB.tsv"
    p.write_text("nation\tˈneɪʃən\ncat\tkæt\n", encoding="utf-8")
    return p


class TestNothingIsBundled:
    def test_no_lexicon_ships(self):
        assert available_lexicon_codes() == []
        assert get_lexicon("en-GB") == {}
        assert lexicon_path("en-GB") is None

    def test_unregistered_language_uses_rules_only(self):
        """No lexicon → the engine behaves as if the overlay did not exist."""
        assert orthography2ipa.transcribe("nation", "en-GB") == "nætɪɒn"

    def test_no_lexicon_files_in_the_package(self):
        from pathlib import Path
        data = Path(orthography2ipa.__file__).parent / "data"
        assert not (data / "lexicons").exists()


class TestLocalFile:
    def test_register_path(self, tsv):
        register_lexicon("en-GB", str(tsv))
        assert get_lexicon("en-GB")["cat"] == "kæt"
        assert available_lexicon_codes() == ["en-GB"]

    def test_lexicon_overrides_the_rules(self, tsv):
        register_lexicon("en-GB", str(tsv))
        assert orthography2ipa.transcribe("nation", "en-GB") == "ˈneɪʃən"

    def test_clear_restores_rules_only(self, tsv):
        register_lexicon("en-GB", str(tsv))
        clear_lexicons()
        assert orthography2ipa.transcribe("nation", "en-GB") == "nætɪɒn"

    def test_missing_file_is_an_error(self):
        register_lexicon("en-GB", "/no/such/lexicon.tsv")
        with pytest.raises(FileNotFoundError):
            get_lexicon("en-GB")


class TestLexiconDir:
    def test_dir_is_discovered_by_code(self, tsv):
        set_lexicon_dir(tsv.parent)
        assert available_lexicon_codes() == ["en-GB"]
        assert orthography2ipa.transcribe("nation", "en-GB") == "ˈneɪʃən"

    def test_registered_source_wins_over_the_dir(self, tsv, tmp_path):
        other = tmp_path / "other.tsv"
        other.write_text("nation\tnaʃon\n", encoding="utf-8")
        set_lexicon_dir(tsv.parent)
        register_lexicon("en-GB", str(other))
        assert get_lexicon("en-GB")["nation"] == "naʃon"

    def test_env_var(self, tsv, monkeypatch):
        monkeypatch.setenv("ORTHOGRAPHY2IPA_LEXICON_DIR", str(tsv.parent))
        get_lexicon.cache_clear()
        assert get_lexicon("en-GB")["cat"] == "kæt"


class TestRemoteSources:
    def test_hf_id_must_name_a_file(self):
        with pytest.raises(ValueError, match="hf://"):
            resolve_lexicon_source("hf://Owner/repo")

    def test_registration_does_not_fetch(self):
        """Lazy: no network until the language is actually transcribed."""
        register_lexicon("en-GB", "https://example.invalid/en.tsv")
        assert available_lexicon_codes() == ["en-GB"]
