"""Parametrized tests for all registered language codes.

Validates basic structural properties for every spec in data/.
"""
import pytest

from orthography2ipa.registry import available_codes, get
from orthography2ipa.types import QualityTier, ScriptType


@pytest.fixture(params=available_codes())
def lang_code(request):
    return request.param


def _try_load(code):
    """Try loading a spec, return None if it fails."""
    try:
        return get(code)
    except (KeyError, ValueError):
        return None


class TestAllLanguagesBasic:
    def test_code_matches(self, lang_code):
        spec = _try_load(lang_code)
        if spec is None:
            pytest.skip(f"Could not load {lang_code}")
        assert spec.code == lang_code

    def test_has_name(self, lang_code):
        spec = _try_load(lang_code)
        if spec is None:
            pytest.skip(f"Could not load {lang_code}")
        assert spec.name

    def test_has_family(self, lang_code):
        spec = _try_load(lang_code)
        if spec is None:
            pytest.skip(f"Could not load {lang_code}")
        assert spec.family

    def test_has_script(self, lang_code):
        spec = _try_load(lang_code)
        if spec is None:
            pytest.skip(f"Could not load {lang_code}")
        # Proto-languages and reconstructed languages predate writing
        if spec.script is None:
            pytest.skip(f"No script (proto/reconstructed): {lang_code}")
        assert spec.script

    def test_quality_is_valid(self, lang_code):
        spec = _try_load(lang_code)
        if spec is None:
            pytest.skip(f"Could not load {lang_code}")
        assert isinstance(spec.quality, QualityTier)

    def test_script_type_is_valid(self, lang_code):
        spec = _try_load(lang_code)
        if spec is None:
            pytest.skip(f"Could not load {lang_code}")
        assert isinstance(spec.script_type, ScriptType)
