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


class TestRegionAndDialectDefaults:
    """Region and dialect Arabic tags resolve to the intended spec.

    ``ar-SA`` — the natural code for Saudi Arabic — has no exact spec (the
    Saudi varieties are keyed by private-use subtag), so nearest-match would
    otherwise pick whichever sibling sorts first. A curated region default and
    private-use dialect aliases steer it to the intended variety instead. The
    Saudi default (Najdi) is an editorial convention, not a claim in the data.
    """

    @pytest.mark.parametrize("requested,expected", [
        ("ar-SA", "ar-SA-x-najd"),        # region default: most widely spoken
        ("ar-x-najdi", "ar-SA-x-najd"),   # dialect named in a private-use subtag
        ("ar-x-hejazi", "ar-SA-x-hejaz"),
        ("ar-x-hijazi", "ar-SA-x-hejaz"),
    ])
    def test_region_and_dialect_defaults(self, requested, expected):
        assert resolve(requested) == expected
        assert isinstance(get(requested), LanguageSpec)
        assert get(requested) is get(expected)

    @pytest.mark.parametrize("requested,expected", [
        ("ar", "ar"),                     # MSA leaf, unchanged
        ("ar-EG", "ar-EG"),               # region with a single spec
        ("ar-SA-x-najd", "ar-SA-x-najd"), # exact dialect spec, unchanged
    ])
    def test_existing_arabic_mappings_are_unregressed(self, requested, expected):
        assert resolve(requested) == expected

    def test_unknown_arabic_region_falls_back_to_msa(self):
        assert resolve("ar-ZZ") == "ar"


class TestUnknownLanguage:
    """No usable match leaves the code unchanged and get() raises."""

    def test_unknown_language_raises(self):
        with pytest.raises(KeyError):
            get("zz-ZZ")

    def test_unknown_language_resolve_unchanged(self):
        assert resolve("zz-ZZ") == "zz-ZZ"
