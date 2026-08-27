"""Tests for the ``valid_ceiling`` field (issue #1343).

A ``valid_ceiling`` is a MEASURED PER floor once an orthographically-unwritten
contrast (tone, vowel length, or both) is folded out of both prediction and
gold. This file covers: schema validation of a well-shaped and a malformed
value, that the field is NOT inherited through ``parent`` (OWN_ONLY, like
``orthography_standard`` and ``timespan``), and that the scoreboard renders
the new column without disturbing raw PER.
"""
import json

import pytest

from orthography2ipa import json_loader
from orthography2ipa.schema import LanguageSpecModel
from orthography2ipa.types import (
    FIELD_INHERITANCE,
    InheritanceMode,
    ValidCeiling,
)


MINIMAL_SPEC = {
    "code": "zz",
    "name": "Test",
    "family": "Test",
    "script": "Latin",
    "graphemes": {"a": ["a"]},
    "allophones": {"a": ["a"]},
}


class TestSchemaValidation:
    def test_well_shaped_valid_ceiling_validates(self):
        spec = LanguageSpecModel.model_validate({
            **MINIMAL_SPEC,
            "valid_ceiling": {
                "per": 0.0223,
                "folded": "tone+length",
                "citation": "Measured across PRs #1063, #1109, #1203, #1295; "
                            "see docs/languages/ha.md.",
            },
        })
        assert spec.valid_ceiling.per == 0.0223
        assert spec.valid_ceiling.folded == "tone+length"

    def test_missing_folded_is_rejected(self):
        """`folded` is required: a bare PER number with no statement of what
        contrast was folded is exactly the conflation the field exists to
        prevent (tone alone vs. tone+length give very different numbers)."""
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "valid_ceiling": {
                    "per": 0.0223,
                    "citation": "see docs/languages/ha.md",
                },
            })

    def test_missing_citation_is_rejected(self):
        """An assertion with no citation for why the contrast is unwritten
        is exactly the "unmeasured ceiling" this field must never carry."""
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "valid_ceiling": {
                    "per": 0.0223,
                    "folded": "tone+length",
                },
            })

    def test_per_out_of_range_is_rejected(self):
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "valid_ceiling": {
                    "per": 1.5,
                    "folded": "tone",
                    "citation": "bogus",
                },
            })

    def test_extra_key_is_rejected(self):
        """Strict model: an unrecognised sub-key (e.g. a typo) must fail
        loudly rather than silently vanish."""
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "valid_ceiling": {
                    "per": 0.0223,
                    "folded": "tone",
                    "citation": "bogus",
                    "measured_by": "someone",
                },
            })

    def test_field_is_optional(self):
        """No valid_ceiling at all must still validate — most rows have no
        measurement yet, and absence must never be an error."""
        spec = LanguageSpecModel.model_validate(MINIMAL_SPEC)
        assert spec.valid_ceiling is None


class TestInheritance:
    def test_registered_as_own_only(self):
        assert FIELD_INHERITANCE["valid_ceiling"] is InheritanceMode.OWN_ONLY

    def test_not_inherited_through_parent(self, tmp_path, monkeypatch):
        """A dialect that inherits graphemes from a parent with a measured
        ceiling must NOT silently inherit that ceiling: the ceiling is a
        measurement executed against the PARENT's own gold rows, and
        asserting it for a child that was never rescored would be exactly
        the "unmeasured ceiling" this field forbids."""
        parent = {
            **MINIMAL_SPEC,
            "code": "zzparent",
            "valid_ceiling": {
                "per": 0.01,
                "folded": "tone",
                "citation": "test fixture",
            },
        }
        child = {
            "code": "zzchild",
            "name": "Test Child",
            "family": "Test",
            "script": "Latin",
            "parent": "zzparent",
            "graphemes_base": "zzparent",
        }
        parent_file = tmp_path / "zzparent.json"
        child_file = tmp_path / "zzchild.json"
        parent_file.write_text(json.dumps(parent))
        child_file.write_text(json.dumps(child))

        monkeypatch.setitem(json_loader._index, "zzparent", parent_file)
        monkeypatch.setitem(json_loader._index, "zzchild", child_file)
        monkeypatch.delitem(json_loader._specs, "zzparent", raising=False)
        monkeypatch.delitem(json_loader._specs, "zzchild", raising=False)

        parent_spec = json_loader.load_json_spec("zzparent")
        child_spec = json_loader.load_json_spec("zzchild")

        assert isinstance(parent_spec.valid_ceiling, ValidCeiling)
        assert parent_spec.valid_ceiling.per == 0.01
        assert child_spec.valid_ceiling is None, (
            "child inherited the parent's valid_ceiling — it must stay "
            "own-file-only (OWN_ONLY)"
        )

        monkeypatch.delitem(json_loader._specs, "zzparent", raising=False)
        monkeypatch.delitem(json_loader._specs, "zzchild", raising=False)


class TestLoaderParsesShippedData:
    def test_ha_valid_ceiling_loads(self):
        spec = json_loader.load_json_spec("ha")
        assert spec.valid_ceiling is not None
        assert spec.valid_ceiling.per == pytest.approx(0.0223)
        assert spec.valid_ceiling.folded == "tone+length"

    def test_ee_valid_ceiling_loads(self):
        spec = json_loader.load_json_spec("ee")
        assert spec.valid_ceiling is not None
        assert spec.valid_ceiling.per == pytest.approx(0.008)
        assert spec.valid_ceiling.folded == "tone"


class TestScoreboardColumn:
    def test_ceiling_column_present_and_marks_below_threshold(
        self, tmp_path, monkeypatch
    ):
        import sys
        import os

        sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
        import benchmark  # noqa: E402

        # Never write through the real committed board paths from a test —
        # redirect both artifacts this function touches to a scratch dir.
        monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(tmp_path / "scoreboard.md"))
        monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(tmp_path / "results.json"))

        rows = [
            {
                "lang": "ha", "dataset": "wikipron", "n": 1857, "per": 0.5340,
                "per_ci_low": 0.51, "per_ci_high": 0.55, "exact_match": 0.0022,
                "quality_tier": "production", "provenance": "crowd-scraped",
                "valid_ceiling": {"per": 0.0223, "folded": "tone+length",
                                  "citation": "see docs/languages/ha.md"},
            },
            {
                "lang": "xx", "dataset": "wikipron", "n": 100, "per": 0.9,
                "per_ci_low": 0.8, "per_ci_high": 0.95, "exact_match": 0.0,
                "quality_tier": None, "provenance": None,
            },
        ]
        benchmark.write_scoreboard(rows)
        with open(benchmark.SCOREBOARD_MD, encoding="utf-8") as fh:
            doc = fh.read()

        assert "Ceiling" in doc
        # ha's raw PER (0.5340) must be unchanged in the rendered row.
        assert "0.5340" in doc
        # The recorded ceiling is below CEILING_GATING_THRESHOLD and must be
        # visibly marked, distinguishing a proved-input-limited row from a
        # genuinely failing one (xx, which has no ceiling at all → "-").
        ha_line = [l for l in doc.splitlines() if l.startswith("| ha ")][0]
        xx_line = [l for l in doc.splitlines() if l.startswith("| xx ")][0]
        assert "0.0223" in ha_line and "†" in ha_line
        assert "| - |" in xx_line or " - " in xx_line
