"""Tests for the ``valid_ceiling`` field (issues #1343, #1350).

A ``valid_ceiling`` is a MEASURED PER floor once an orthographically-unwritten
contrast (tone, vowel length, or both) is folded out of both prediction and
gold. A fold is defined relative to ONE gold's notation conventions, so the
measurement is scoped to a (language, dataset) pair, never to the language
alone (#1350): ``valid_ceiling`` is an object keyed by dataset name, one
entry per gold the language has actually been measured against.

This file covers: schema validation of a well-shaped and a malformed value,
that the old language-scoped shape is rejected rather than silently
reinterpreted, that the field is NOT inherited through ``parent`` (OWN_ONLY,
like ``orthography_standard`` and ``timespan``), and that the scoreboard
renders a ceiling only on the row whose dataset it names.
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
                "wikipron": {
                    "per": 0.0223,
                    "folded": "tone+length",
                    "citation": "Measured across PRs #1063, #1109, #1203, "
                                "#1295; see docs/languages/ha.md.",
                },
            },
        })
        assert spec.valid_ceiling["wikipron"].per == 0.0223
        assert spec.valid_ceiling["wikipron"].folded == "tone+length"

    def test_two_datasets_are_both_kept(self):
        """A language may legitimately have several ceilings, one per gold
        it has been measured against — they must not clobber each other."""
        spec = LanguageSpecModel.model_validate({
            **MINIMAL_SPEC,
            "valid_ceiling": {
                "wikipron": {
                    "per": 0.02, "folded": "tone",
                    "citation": "measured against wikipron",
                },
                "vox_communis": {
                    "per": 0.09, "folded": "tone+length",
                    "citation": "measured against vox_communis",
                },
            },
        })
        assert spec.valid_ceiling["wikipron"].per == 0.02
        assert spec.valid_ceiling["vox_communis"].per == 0.09

    def test_old_language_scoped_shape_is_rejected(self):
        """The pre-#1350 shape — a bare {per, folded, citation} object with
        no dataset key — must be rejected, not silently accepted: a ceiling
        with no named dataset cannot be resolved to the row it was measured
        against, which is exactly the bug #1350 reports."""
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "valid_ceiling": {
                    "per": 0.0223,
                    "folded": "tone+length",
                    "citation": "see docs/languages/ha.md",
                },
            })

    def test_missing_folded_is_rejected(self):
        """`folded` is required: a bare PER number with no statement of what
        contrast was folded is exactly the conflation the field exists to
        prevent (tone alone vs. tone+length give very different numbers)."""
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "valid_ceiling": {
                    "wikipron": {
                        "per": 0.0223,
                        "citation": "see docs/languages/ha.md",
                    },
                },
            })

    def test_missing_citation_is_rejected(self):
        """An assertion with no citation for why the contrast is unwritten
        is exactly the "unmeasured ceiling" this field must never carry."""
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "valid_ceiling": {
                    "wikipron": {
                        "per": 0.0223,
                        "folded": "tone+length",
                    },
                },
            })

    def test_per_out_of_range_is_rejected(self):
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "valid_ceiling": {
                    "wikipron": {
                        "per": 1.5,
                        "folded": "tone",
                        "citation": "bogus",
                    },
                },
            })

    def test_extra_key_is_rejected(self):
        """Strict model: an unrecognised sub-key (e.g. a typo) must fail
        loudly rather than silently vanish."""
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "valid_ceiling": {
                    "wikipron": {
                        "per": 0.0223,
                        "folded": "tone",
                        "citation": "bogus",
                        "measured_by": "someone",
                    },
                },
            })

    def test_field_is_optional(self):
        """No valid_ceiling at all must still validate — most rows have no
        measurement yet, and absence must never be an error."""
        spec = LanguageSpecModel.model_validate(MINIMAL_SPEC)
        assert spec.valid_ceiling is None


class TestLoaderRejectsOldShape:
    def test_old_language_scoped_shape_raises(self, tmp_path, monkeypatch):
        spec_dict = {
            **MINIMAL_SPEC,
            "code": "zzold",
            "valid_ceiling": {
                "per": 0.0223,
                "folded": "tone+length",
                "citation": "old shape",
            },
        }
        spec_file = tmp_path / "zzold.json"
        spec_file.write_text(json.dumps(spec_dict))
        monkeypatch.setitem(json_loader._index, "zzold", spec_file)
        monkeypatch.delitem(json_loader._specs, "zzold", raising=False)
        try:
            with pytest.raises(ValueError):
                json_loader.load_json_spec("zzold")
        finally:
            monkeypatch.delitem(json_loader._specs, "zzold", raising=False)


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
                "wikipron": {
                    "per": 0.01,
                    "folded": "tone",
                    "citation": "test fixture",
                },
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

        assert isinstance(parent_spec.valid_ceiling["wikipron"], ValidCeiling)
        assert parent_spec.valid_ceiling["wikipron"].per == 0.01
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
        assert spec.valid_ceiling["wikipron"].per == pytest.approx(0.0223)
        assert spec.valid_ceiling["wikipron"].folded == "tone+length"

    def test_ee_valid_ceiling_loads(self):
        spec = json_loader.load_json_spec("ee")
        assert spec.valid_ceiling is not None
        assert spec.valid_ceiling["wikipron"].per == pytest.approx(0.008)
        assert spec.valid_ceiling["wikipron"].folded == "tone"


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


class TestCeilingResolvesByDatasetNotLanguage:
    """The bug #1350 reports: resolving `_valid_ceiling` by language alone
    spreads a ceiling measured on one gold across every other gold of that
    language. These assert the fix — resolution is keyed by
    (language, dataset), and a ceiling renders ONLY on its own dataset's
    row, never on a sibling row of the same language scored on a different
    gold."""

    def _spec_with_ceilings(self, **ceilings):
        class _Spec:
            pass
        spec = _Spec()
        spec.valid_ceiling = {
            name: ValidCeiling(per=c["per"], folded=c["folded"],
                               citation=c["citation"])
            for name, c in ceilings.items()
        }
        return spec

    def test_resolves_only_own_dataset(self, monkeypatch):
        import sys
        import os
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
        import benchmark  # noqa: E402

        spec = self._spec_with_ceilings(
            wikipron={"per": 0.0223, "folded": "tone+length",
                      "citation": "measured on wikipron"},
        )
        monkeypatch.setattr(
            "orthography2ipa.get", lambda lang: spec, raising=False
        )
        import orthography2ipa
        monkeypatch.setattr(orthography2ipa, "get", lambda lang: spec)

        # Own dataset resolves.
        result = benchmark._valid_ceiling("ha", "wikipron")
        assert result is not None
        assert result["per"] == 0.0223

        # A sibling dataset of the SAME language, never folded, must NOT
        # inherit wikipron's measurement.
        result_sibling = benchmark._valid_ceiling("ha", "vox_communis")
        assert result_sibling is None

    def test_multiple_datasets_each_render_on_own_row_only(
        self, tmp_path, monkeypatch
    ):
        import sys
        import os
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
        import benchmark  # noqa: E402

        monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(tmp_path / "scoreboard.md"))
        monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(tmp_path / "results.json"))

        rows = [
            {
                "lang": "vi", "dataset": "ipadict", "n": 500, "per": 0.0777,
                "per_ci_low": 0.06, "per_ci_high": 0.09, "exact_match": 0.9,
                "quality_tier": "production", "provenance": "dictionary",
                "valid_ceiling": {"per": 0.0246, "folded": "tone",
                                  "citation": "measured against ipadict"},
            },
            {
                "lang": "vi", "dataset": "vox_communis", "n": 400,
                "per": 0.5596, "per_ci_low": 0.5, "per_ci_high": 0.6,
                "exact_match": 0.1, "quality_tier": "production",
                "provenance": "crowd-scraped",
                # No ceiling: vox_communis has NOT been folded for vi.
            },
        ]
        benchmark.write_scoreboard(rows)
        with open(benchmark.SCOREBOARD_MD, encoding="utf-8") as fh:
            doc = fh.read()

        ipadict_line = [
            l for l in doc.splitlines()
            if l.startswith("| vi | ipadict")
        ][0]
        vox_line = [
            l for l in doc.splitlines()
            if l.startswith("| vi | vox_communis")
        ][0]
        assert "0.0246" in ipadict_line
        # The vox_communis row must NOT show ipadict's ceiling.
        assert "0.0246" not in vox_line
        assert " - " in vox_line or "| - |" in vox_line
