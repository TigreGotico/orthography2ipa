"""Validate every language-spec JSON file against the pydantic schema.

Parametrized over all ``data/*.json`` files so each spec is an individual test
case; a failure names the offending file and field path.
"""
import pytest

from orthography2ipa.schema import (
    LanguageSpecModel,
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
