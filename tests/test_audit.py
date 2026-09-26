"""Tests for the ``audit`` field (issue #1369).

A completed audit that concludes "nothing needs fixing" previously left no
machine-findable trace: the conclusion lived only in ``notes`` prose or a
``docs/languages/*.md`` page, in whatever wording that wave happened to use.
``audit`` is a machine-readable record of that conclusion, keyed by gold
dataset the same way ``valid_ceiling`` is (#1350) — a conclusion reached by
looking at one gold's rows does not transfer to a different gold of the same
language.

This file covers: schema validation of a well-shaped and malformed value,
that ``conclusion`` is rejected outside the closed enum, that the field is
NOT inherited through ``parent`` (OWN_ONLY, like ``valid_ceiling``), and that
the backfilled records for shipped languages round-trip through the loader.
"""
import json

import pytest

from orthography2ipa import json_loader
from orthography2ipa.schema import LanguageSpecModel
from orthography2ipa.types import (
    AuditConclusion,
    AuditRecord,
    FIELD_INHERITANCE,
    InheritanceMode,
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
    def test_well_shaped_audit_validates(self):
        spec = LanguageSpecModel.model_validate({
            **MINIMAL_SPEC,
            "audit": {
                "wikipron": {
                    "conclusion": "input_limited",
                    "measured": "Folded tone out of both sides; PER dropped "
                                "from 0.44 to 0.008.",
                    "reference": "spec notes",
                },
            },
        })
        assert spec.audit["wikipron"].conclusion == AuditConclusion.INPUT_LIMITED
        assert spec.audit["wikipron"].reference == "spec notes"

    def test_two_datasets_are_both_kept(self):
        spec = LanguageSpecModel.model_validate({
            **MINIMAL_SPEC,
            "audit": {
                "wikipron": {
                    "conclusion": "input_limited",
                    "measured": "measured against wikipron",
                    "reference": "spec notes",
                },
                "vox_communis": {
                    "conclusion": "sample_too_small",
                    "measured": "n=1",
                    "reference": "spec notes",
                },
            },
        })
        assert spec.audit["wikipron"].conclusion == AuditConclusion.INPUT_LIMITED
        assert spec.audit["vox_communis"].conclusion == AuditConclusion.SAMPLE_TOO_SMALL

    def test_all_seven_enum_values_are_accepted(self):
        for value in (
            "input_limited", "degraded_input", "mislabeled_gold",
            "sample_too_small", "at_ceiling_documented",
            "change_refused_uncited", "logographic",
        ):
            spec = LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "audit": {
                    "wikipron": {
                        "conclusion": value,
                        "measured": "test",
                        "reference": "test",
                    },
                },
            })
            assert spec.audit["wikipron"].conclusion == value

    def test_conclusion_outside_enum_is_rejected(self):
        """The whole point of the field is a CLOSED enum — an arbitrary
        string must be rejected rather than accepted as free-form prose,
        which would reproduce the exact problem #1369 reports."""
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "audit": {
                    "wikipron": {
                        "conclusion": "looks-fine-to-me",
                        "measured": "test",
                        "reference": "test",
                    },
                },
            })

    def test_missing_measured_is_rejected(self):
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "audit": {
                    "wikipron": {
                        "conclusion": "input_limited",
                        "reference": "test",
                    },
                },
            })

    def test_missing_reference_is_rejected(self):
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "audit": {
                    "wikipron": {
                        "conclusion": "input_limited",
                        "measured": "test",
                    },
                },
            })

    def test_extra_key_is_rejected(self):
        with pytest.raises(Exception):
            LanguageSpecModel.model_validate({
                **MINIMAL_SPEC,
                "audit": {
                    "wikipron": {
                        "conclusion": "input_limited",
                        "measured": "test",
                        "reference": "test",
                        "audited_by": "someone",
                    },
                },
            })

    def test_field_is_optional(self):
        spec = LanguageSpecModel.model_validate(MINIMAL_SPEC)
        assert spec.audit is None


class TestLoaderRejectsBadShape:
    def test_non_object_audit_raises(self, tmp_path, monkeypatch):
        spec_dict = {
            **MINIMAL_SPEC,
            "code": "zzbadaudit",
            "audit": "input_limited",
        }
        spec_file = tmp_path / "zzbadaudit.json"
        spec_file.write_text(json.dumps(spec_dict))
        monkeypatch.setitem(json_loader._index, "zzbadaudit", spec_file)
        monkeypatch.delitem(json_loader._specs, "zzbadaudit", raising=False)
        try:
            with pytest.raises(ValueError):
                json_loader.load_json_spec("zzbadaudit")
        finally:
            monkeypatch.delitem(json_loader._specs, "zzbadaudit", raising=False)

    def test_bad_enum_value_raises(self, tmp_path, monkeypatch):
        spec_dict = {
            **MINIMAL_SPEC,
            "code": "zzbadenum",
            "audit": {
                "wikipron": {
                    "conclusion": "not-a-real-value",
                    "measured": "test",
                    "reference": "test",
                },
            },
        }
        spec_file = tmp_path / "zzbadenum.json"
        spec_file.write_text(json.dumps(spec_dict))
        monkeypatch.setitem(json_loader._index, "zzbadenum", spec_file)
        monkeypatch.delitem(json_loader._specs, "zzbadenum", raising=False)
        try:
            with pytest.raises(ValueError):
                json_loader.load_json_spec("zzbadenum")
        finally:
            monkeypatch.delitem(json_loader._specs, "zzbadenum", raising=False)


class TestInheritance:
    def test_registered_as_own_only(self):
        assert FIELD_INHERITANCE["audit"] is InheritanceMode.OWN_ONLY

    def test_not_inherited_through_parent(self, tmp_path, monkeypatch):
        """A dialect that inherits graphemes from an audited parent must NOT
        silently inherit the parent's audit verdict: the audit was reached
        by looking at the PARENT's own gold rows, and the child's rows have
        not themselves been examined."""
        parent = {
            **MINIMAL_SPEC,
            "code": "zzauditparent",
            "audit": {
                "wikipron": {
                    "conclusion": "input_limited",
                    "measured": "test fixture",
                    "reference": "test fixture",
                },
            },
        }
        child = {
            "code": "zzauditchild",
            "name": "Test Child",
            "family": "Test",
            "script": "Latin",
            "parent": "zzauditparent",
            "graphemes_base": "zzauditparent",
        }
        parent_file = tmp_path / "zzauditparent.json"
        child_file = tmp_path / "zzauditchild.json"
        parent_file.write_text(json.dumps(parent))
        child_file.write_text(json.dumps(child))

        monkeypatch.setitem(json_loader._index, "zzauditparent", parent_file)
        monkeypatch.setitem(json_loader._index, "zzauditchild", child_file)
        monkeypatch.delitem(json_loader._specs, "zzauditparent", raising=False)
        monkeypatch.delitem(json_loader._specs, "zzauditchild", raising=False)

        parent_spec = json_loader.load_json_spec("zzauditparent")
        child_spec = json_loader.load_json_spec("zzauditchild")

        assert isinstance(parent_spec.audit["wikipron"], AuditRecord)
        assert child_spec.audit is None, (
            "child inherited the parent's audit record — it must stay "
            "own-file-only (OWN_ONLY)"
        )

        monkeypatch.delitem(json_loader._specs, "zzauditparent", raising=False)
        monkeypatch.delitem(json_loader._specs, "zzauditchild", raising=False)


class TestBackfilledRecordsRoundTrip:
    """The records backfilled onto shipped specs for #1369 must load and
    carry the conclusion documented in each spec's own prose."""

    @pytest.mark.parametrize("code,dataset,conclusion", [
        ("yol", "wikipron", AuditConclusion.MISLABELED_GOLD),
        ("pt-TL", "portuguese_unified", AuditConclusion.MISLABELED_GOLD),
        ("ar-DZ", "primary_sources", AuditConclusion.SAMPLE_TOO_SMALL),
        ("se", "wikipron", AuditConclusion.CHANGE_REFUSED_UNCITED),
        ("ja", "ipadict", AuditConclusion.LOGOGRAPHIC),
        ("da", "wikipron", AuditConclusion.AT_CEILING_DOCUMENTED),
        ("so", "kaikki", AuditConclusion.CHANGE_REFUSED_UNCITED),
        ("km", "ipadict", AuditConclusion.CHANGE_REFUSED_UNCITED),
    ])
    def test_backfilled_conclusion_loads(self, code, dataset, conclusion):
        spec = json_loader.load_json_spec(code)
        assert spec.audit is not None, f"{code}: no audit record backfilled"
        assert dataset in spec.audit, (
            f"{code}: no audit entry for dataset {dataset!r}, has "
            f"{list(spec.audit)}"
        )
        assert spec.audit[dataset].conclusion == conclusion


class TestSoAtrFoldRefused:
    """so/kaikki (#so-tone-ceiling): a tone-only ``valid_ceiling`` is
    recorded, but the much larger [+/-ATR] vowel-quality fold (ɑ ɛ ɪ ɔ ɞ
    onto a e i o) is deliberately refused for lack of a citation that
    settles whether the contrast is real or a notation artifact (Gabbard
    2010). This pins both halves of that decision so neither can silently
    regress: the ceiling must stay tone-only, and the audit conclusion must
    stay a refusal, not a claim the vowel question is resolved."""

    def test_valid_ceiling_folds_tone_only_not_vowel_quality(self):
        spec = json_loader.load_json_spec("so")
        ceiling = spec.valid_ceiling["kaikki"]
        assert ceiling.folded == "tone"
        assert ceiling.per == pytest.approx(0.4092)
        for lax_vowel in "ɑɛɪɔɞ":
            assert lax_vowel not in ceiling.folded

    def test_atr_fold_is_recorded_as_refused_not_resolved(self):
        spec = json_loader.load_json_spec("so")
        entry = spec.audit["kaikki"]
        assert entry.conclusion == AuditConclusion.CHANGE_REFUSED_UNCITED
        assert "ATR" in entry.measured


class TestDegradedInputIsNotInputLimited:
    """``degraded_input`` separates a limit of the GOLD from a limit of the
    WRITING SYSTEM (T-2622, ruling in
    ``knowledge/wiki/audits/o2i/valid-ceiling-tone-ruling.md``).

    ``input_limited`` says the ordinary written norm does not write a contrast
    the gold transcribes, and that is what licenses a ``valid_ceiling``. Two
    shipped rows were real audits with the opposite finding — the orthography
    writes the contrast and the scraped input column dropped it — and had to
    borrow ``input_limited`` because no value said so. These tests pin which
    row is which, and the invariant that separates them.
    """

    def test_yo_wikipron_is_degraded_input_not_input_limited(self):
        """Yoruba writes tone with acute / nothing / grave (Adesola 2005);
        32 of 4937 scraped headwords carry a mark. The limit is the scrape."""
        entry = json_loader.load_json_spec("yo").audit["wikipron"]
        assert entry.conclusion == AuditConclusion.DEGRADED_INPUT
        assert entry.conclusion != AuditConclusion.INPUT_LIMITED

    def test_tru_wikipron_is_degraded_input_not_input_limited(self):
        """The Surayt Orthography writes /a/ and shewa with vowel points; 0 of
        232 scraped spellings carry one."""
        entry = json_loader.load_json_spec("tru").audit["wikipron"]
        assert entry.conclusion == AuditConclusion.DEGRADED_INPUT

    def test_a_degraded_input_row_never_carries_a_valid_ceiling(self):
        """The invariant the value exists to express. A ceiling is the best PER
        once a contrast the ORTHOGRAPHY cannot write is folded out, so a row
        whose orthography does write it must not have one — the fold belongs in
        the audit record's own ``measured`` field instead."""
        offenders, seen = [], []
        for code in json_loader.available_json_codes():
            spec = json_loader.load_json_spec(code)
            for dataset, entry in (spec.audit or {}).items():
                if entry.conclusion != AuditConclusion.DEGRADED_INPUT:
                    continue
                seen.append(f"{code}/{dataset}")
                if dataset in (spec.valid_ceiling or {}):
                    offenders.append(f"{code}/{dataset}")
        # Without this the check passes on any tree that has no such row at
        # all, including the tree before this value existed.
        assert sorted(seen) == ["tru/wikipron", "yo/wikipron"], (
            f"expected exactly the two ruled rows to use the value, got {seen}"
        )
        assert not offenders, (
            "degraded_input rows carrying a valid_ceiling, which the "
            f"conclusion forbids: {offenders}"
        )

    def test_the_script_has_the_marks_rows_stay_input_limited(self):
        """A script that HAS the marks and omits them in running text is
        input_limited, not degraded_input. Arabic harakat and Hebrew niqqud are
        the reason the boundary needs stating: ordinary text omits both, so
        those rows are limited by the written norm, not by the scrape."""
        for code in ("ar", "ar-EG", "ar-MA", "he"):
            entry = json_loader.load_json_spec(code).audit["wikipron"]
            assert entry.conclusion == AuditConclusion.INPUT_LIMITED, (
                f"{code}/wikipron moved off input_limited; the ordinary "
                "written norm omits these marks, so it belongs there"
            )

    def test_ee_wikipron_stays_input_limited_despite_a_restorable_headword(self):
        """The near-miss. ``ee``/``wikipron`` restores tone from the Wiktionary
        DISPLAY headword and reaches PER 0.0007, which looks like degraded
        input — but standard Ewe marks tone only where disambiguation requires
        it (Ansre 1961; Capo 1991). A dictionary headword marking what running
        text does not is a lexicographic convention, not the written norm, so
        the row stays input_limited and keeps its ceiling."""
        spec = json_loader.load_json_spec("ee")
        assert spec.audit["wikipron"].conclusion == AuditConclusion.INPUT_LIMITED
        assert "wikipron" in spec.valid_ceiling
