"""Tests for language-code resolution — bare tags, defaults, nearest match.

Validates:
- Bare primary-language tags resolve to their curated reference variety
- Every registered code's bare primary subtag is loadable (the curated
  table cannot rot as specs are added)
- Nearest-language fallback for unregistered regional tags
- Unknown languages still raise KeyError
- resolve() exposes the resolution without loading a spec
"""
import pytest

import orthography2ipa
from orthography2ipa import available_codes, get, resolve
from orthography2ipa.types import LanguageSpec


class TestBareDefaults:
    """Bare primary tags resolve to the reference variety."""

    @pytest.mark.parametrize("bare,expected", [
        ("de", "de-DE"),
        ("en", "en-GB"),
        ("es", "es-ES"),
        ("fr", "fr-FR"),
        ("it", "it-IT"),
        ("pt", "pt-PT"),
        ("ro", "ro-RO"),
    ])
    def test_curated_defaults(self, bare, expected):
        assert resolve(bare) == expected
        spec = get(bare)
        assert isinstance(spec, LanguageSpec)
        assert spec is get(expected)

    def test_every_bare_primary_resolves(self):
        """Every registered code's primary subtag must itself load."""
        primaries = {code.split("-")[0] for code in available_codes()}
        failures = []
        for primary in sorted(primaries):
            try:
                get(primary)
            except Exception as exc:
                failures.append(f"{primary}: {exc.__class__.__name__}")
        assert not failures, (
            "bare primary subtags without a resolution "
            f"(extend _BARE_DEFAULTS or add a spec): {failures}"
        )


class TestNearestMatch:
    """Unregistered regional tags fall back to the nearest registered code."""

    @pytest.mark.parametrize("requested,language", [
        ("en-NZ", "en"),
        ("fr-CA", "fr"),
        ("de-LU", "de"),
        ("es-HN", "es"),
    ])
    def test_unregistered_region_resolves_within_language(
            self, requested, language):
        resolved = resolve(requested)
        assert resolved.split("-")[0] == language
        assert isinstance(get(requested), LanguageSpec)

    def test_existing_codes_resolve_to_themselves(self):
        for code in ("pt-PT", "ast-PT-x-rionor", "eu-x-bizkaiera", "ar"):
            assert resolve(code) == code

    def test_iso639_3_aliases_still_resolve(self):
        assert resolve("por") == "pt-PT"
        assert resolve("eng") == "en-GB"
        assert resolve("spa") == "es-ES"

    def test_underscore_and_case_normalisation(self):
        assert resolve("pt_BR") == "pt-BR"
        assert resolve("EN-gb") == "en-GB"


class TestUnknownLanguage:
    """No usable match leaves the code unchanged and get() raises."""

    def test_unknown_language_raises(self):
        with pytest.raises(KeyError):
            get("zz-ZZ")

    def test_unknown_language_resolve_unchanged(self):
        assert resolve("zz-ZZ") == "zz-ZZ"
