"""Tests for T-10: bundled IPA lexicon support.

Validates that load_lexicon() correctly reads the ast-PT-x-rionor CSV
(917 entries) and that the lexicon_csv field in the JSON is honoured.
"""
import pytest

import orthography2ipa
from orthography2ipa.json_loader import load_lexicon


class TestLoadLexicon:
    def test_returns_dict(self):
        lex = load_lexicon("ast-PT-x-rionor")
        assert isinstance(lex, dict)

    def test_entry_count(self):
        """CSV has 917 data rows (918 lines including header)."""
        lex = load_lexicon("ast-PT-x-rionor")
        assert len(lex) == 917

    def test_known_attested_entry(self):
        """'abajo' is attested (Macias 2003, p.33)."""
        lex = load_lexicon("ast-PT-x-rionor")
        assert "abajo" in lex
        assert lex["abajo"] == "aˈbaʒo"

    def test_keys_are_lowercase(self):
        lex = load_lexicon("ast-PT-x-rionor")
        for word in lex:
            assert word == word.lower(), f"Key not lowercase: {word!r}"

    def test_values_are_strings(self):
        lex = load_lexicon("ast-PT-x-rionor")
        for word, ipa in lex.items():
            assert isinstance(ipa, str) and len(ipa) > 0, \
                f"Empty IPA for {word!r}"

    def test_returns_none_for_missing_lexicon(self):
        """Languages without lexicon_csv return None."""
        lex = load_lexicon("pt-PT")
        assert lex is None

    def test_returns_none_for_unknown_code(self):
        lex = load_lexicon("xx-UNKNOWN")
        assert lex is None

    def test_accessible_via_top_level_import(self):
        """load_lexicon is part of the public API."""
        assert hasattr(orthography2ipa, "load_lexicon")
        lex = orthography2ipa.load_lexicon("ast-PT-x-rionor")
        assert lex is not None

    def test_betacism_entries_use_b_not_v(self):
        """All Rionorese IPA entries should use /b/ not /v/ (betacism)."""
        lex = load_lexicon("ast-PT-x-rionor")
        violations = {
            word: ipa for word, ipa in lex.items() if "v" in ipa
        }
        assert not violations, \
            f"Betacism violation — entries with /v/ in IPA: {list(violations.items())[:5]}"

    def test_lexicon_csv_field_in_json(self):
        """ast-PT-x-rionor.json has a lexicon_csv field pointing to the CSV."""
        import json
        from pathlib import Path
        data_dir = Path(orthography2ipa.__file__).parent / "data"
        with (data_dir / "ast-PT-x-rionor.json").open() as f:
            raw = json.load(f)
        assert "lexicon_csv" in raw
        csv_path = data_dir / raw["lexicon_csv"]
        assert csv_path.exists(), f"CSV declared in JSON not found: {csv_path}"
