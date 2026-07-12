"""Validate every language-spec JSON file against the pydantic schema.

Parametrized over all ``data/*.json`` files so each spec is an individual test
case; a failure names the offending file and field path.
"""
import pytest

from orthography2ipa.schema import (
    LanguageSpecModel,
    SandhiRuleModel,
    format_failure,
    iter_spec_files,
    validate_spec_file,
)

_SPEC_FILES = iter_spec_files()


def test_data_dir_not_empty():
    assert _SPEC_FILES, "no spec JSON files discovered under data/"


@pytest.mark.parametrize(
    "spec_path", _SPEC_FILES, ids=[p.stem for p in _SPEC_FILES]
)
def test_spec_validates(spec_path):
    try:
        spec = validate_spec_file(spec_path)
    except Exception as exc:  # noqa: BLE001 — surface the field path in the message
        pytest.fail(format_failure(spec_path.stem, exc))
    # filename stem must match the declared code
    assert spec.code == spec_path.stem, (
        f"{spec_path.name}: code {spec.code!r} != filename stem {spec_path.stem!r}"
    )


def test_all_specs_pass_in_bulk():
    from orthography2ipa.schema import validate_all

    ok, failures = validate_all()
    assert not failures, "\n".join(
        format_failure(code, exc) for code, exc in failures
    )
    assert len(ok) == len(_SPEC_FILES)


def test_extra_keys_are_forbidden():
    """The model must reject unknown keys (regression guard for extra='forbid')."""
    with pytest.raises(Exception):
        LanguageSpecModel.model_validate(
            {
                "code": "xx",
                "name": "Test",
                "family": "Test",
                "script": "Latin",
                "graphemes": {"a": ["a"]},
                "allophones": {"a": ["a"]},
                "bogus_unknown_key": 1,
            }
        )


# ─── SandhiRuleModel ───────────────────────────────────────────────────────

_SANDHI_BASE = {
    "id": "X_RULE",
    "name": "x-rule",
    "left_context": "s$",
    "right_context": "^[aeiou]",
}


def test_sandhi_rule_accepts_a_left_transform():
    rule = SandhiRuleModel.model_validate({**_SANDHI_BASE, "transform": "z"})
    assert rule.transform == "z"
    assert rule.right_transform is None


def test_sandhi_rule_accepts_a_right_transform():
    rule = SandhiRuleModel.model_validate(
        {**_SANDHI_BASE, "right_transform": "ð"}
    )
    assert rule.right_transform == "ð"
    assert rule.transform is None


def test_sandhi_rule_accepts_both_transforms():
    rule = SandhiRuleModel.model_validate(
        {**_SANDHI_BASE, "transform": "z", "right_transform": "ð"}
    )
    assert rule.transform == "z" and rule.right_transform == "ð"


def test_sandhi_rule_without_any_transform_is_rejected():
    """A rule with neither ``transform`` nor ``right_transform`` matches a
    boundary and then changes nothing — a silently inert rule, indistinguishable
    at runtime from a typo in its contexts. The schema must reject it."""
    with pytest.raises(Exception, match="right_transform"):
        SandhiRuleModel.model_validate(dict(_SANDHI_BASE))
