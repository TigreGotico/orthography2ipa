"""Shared fixtures and configuration for orthography2ipa test suite."""
import pytest

import orthography2ipa


# ═══════════════════════════════════════════════════════════════════════════
# Commonly used language specs
# ═══════════════════════════════════════════════════════════════════════════

@pytest.fixture(scope="session")
def all_codes():
    """All registered language codes (session-scoped for performance)."""
    return orthography2ipa.available_codes()


@pytest.fixture(scope="session")
def all_families():
    """All language families (session-scoped)."""
    return orthography2ipa.available_families()


# Core language fixtures (session-scoped to avoid repeated loading)

@pytest.fixture(scope="session")
def spec_en():
    return orthography2ipa.get("en-GB")


@pytest.fixture(scope="session")
def spec_es():
    return orthography2ipa.get("es-ES")


@pytest.fixture(scope="session")
def spec_pt():
    return orthography2ipa.get("pt-PT")


@pytest.fixture(scope="session")
def spec_pt_br():
    return orthography2ipa.get("pt-BR")


@pytest.fixture(scope="session")
def spec_fr():
    return orthography2ipa.get("fr-FR")


@pytest.fixture(scope="session")
def spec_de():
    return orthography2ipa.get("de-DE")


@pytest.fixture(scope="session")
def spec_la():
    return orthography2ipa.get("la")


@pytest.fixture(scope="session")
def spec_it():
    return orthography2ipa.get("it-IT")


# ═══════════════════════════════════════════════════════════════════════════
# Test markers
# ═══════════════════════════════════════════════════════════════════════════

def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "linguistic: marks linguistically-critical spot checks"
    )
    config.addinivalue_line(
        "markers", "iberian: marks Iberian Peninsula language accuracy tests"
    )
    config.addinivalue_line(
        "markers", "germanic: marks Germanic language accuracy tests"
    )
    config.addinivalue_line(
        "markers", "celtic: marks Celtic language accuracy tests"
    )
    config.addinivalue_line(
        "markers", "slavic: marks Slavic language accuracy tests"
    )


# ═══════════════════════════════════════════════════════════════════════════
# Per-language coverage report for Iberian test suite
# ═══════════════════════════════════════════════════════════════════════════

#: Maps test class name → language code.
#: Add new entries whenever a new language class is added to test_iberian.py.
_IBERIAN_CLASS_TO_CODE: dict[str, str] = {
    "TestSpanishES": "es-ES",
    "TestPortuguesePT": "pt-PT",
    "TestCatalan": "ca",
    "TestGalician": "gl",
    "TestBasqueEU": "eu",
    "TestAsturian": "ast",
    "TestMirandese": "mwl",
    "TestAragonese": "an",
    "TestSpanishAndalusianEast": "es-ES-x-andalusia-e",
    "TestSpanishRioplatense": "es-AR",
    "TestCatalanValencian": "ca-x-valencia",
    "TestCatalanBalearic": "ca-x-balear",
    "TestPortugueseBrazilian": "pt-BR",
    "TestGalicianWestern": "gl-x-occidental",
    "TestIberianIsoglosses": "(cross-language)",
    # Extended dialects (test_iberian_extended.py)
    "TestSpanishWesternAndalusian": "es-ES-x-andalusia-w",
    "TestSpanishCanarian": "es-ES-x-canarias",
    "TestSpanishMurcian": "es-ES-x-murcia",
    "TestSpanishMexican": "es-MX",
    "TestSpanishChilean": "es-CL",
    "TestSpanishVenezuelan": "es-VE",
    "TestSpanishLatinAmerican": "es-419",
    "TestExtremaduran": "ext",
    "TestPortugueseLisbon": "pt-PT-x-lisbon",
    "TestPortuguesePorto": "pt-PT-x-porto",
    "TestPortugueseAngolan": "pt-AO",
    "TestPortugueseRioDeJaneiro": "pt-BR-x-rj",
    "TestCatalanNord": "ca-x-nord",
    "TestCatalanOccidental": "ca-x-occidental",
    "TestGalicianStandard": "gl-ES",
    "TestGalicianOriental": "gl-x-oriental",
    "TestBasqueBizkaiera": "eu-x-bizkaiera",
    "TestBasqueGipuzkera": "eu-x-gipuzkera",
    "TestAsturianOccidental": "ast-x-occidental",
    "TestAsturianOriental": "ast-x-oriental",
    "TestAsturianCantabrian": "ast-x-cantabrian",
    "TestLeonese": "ast-x-leon",
    "TestAsturianPortugueseMedieval": "ast-PT-x-medieval",
    "TestMirandeseSendim": "mwl-x-sendim",
    "TestMiraneseIfanes": "mwl-x-ifanes",
    "TestAragonesOccidental": "an-x-occidental",
    "TestAragonesOriental": "an-x-oriental",
    "TestFrench": "fr-FR",
    "TestItalian": "it-IT",
}


def pytest_terminal_summary(
    terminalreporter,  # type: ignore[override]
    exitstatus: int,
    config,
) -> None:
    """Print a per-language pass/fail coverage table for Iberian tests."""
    from collections import defaultdict

    # outcome → list[report]
    stats = getattr(terminalreporter, "stats", {})

    counts: dict[str, dict[str, int]] = defaultdict(
        lambda: {"passed": 0, "failed": 0, "error": 0}
    )

    for outcome in ("passed", "failed", "error"):
        for report in stats.get(outcome, []):
            # nodeid: tests/test_iberian.py::TestSpanishES::test_grapheme_c_default_velar
            parts = report.nodeid.split("::")
            if len(parts) < 3:
                continue
            file_part = parts[0]
            if "test_iberian" not in file_part:
                continue
            cls_name = parts[1]
            lang = _IBERIAN_CLASS_TO_CODE.get(cls_name)
            if lang:
                counts[lang][outcome] += 1

    if not counts:
        return

    terminalreporter.write_sep("=", "Iberian Language Test Coverage")

    col_lang = 30
    col_p = 8
    col_f = 8
    col_e = 8
    col_tot = 8
    col_pct = 8

    header = (
        f"{'Language':<{col_lang}}"
        f"{'Passed':>{col_p}}"
        f"{'Failed':>{col_f}}"
        f"{'Error':>{col_e}}"
        f"{'Total':>{col_tot}}"
        f"{'Pass%':>{col_pct}}"
    )
    terminalreporter.write_line(header)
    terminalreporter.write_line("-" * (col_lang + col_p + col_f + col_e + col_tot + col_pct))

    overall_passed = overall_total = 0
    for lang in sorted(counts):
        p = counts[lang]["passed"]
        f = counts[lang]["failed"]
        e = counts[lang]["error"]
        tot = p + f + e
        pct = 100.0 * p / tot if tot else 0.0
        overall_passed += p
        overall_total += tot
        flag = "" if f + e == 0 else " ✗"
        terminalreporter.write_line(
            f"{lang:<{col_lang}}"
            f"{p:>{col_p}}"
            f"{f:>{col_f}}"
            f"{e:>{col_e}}"
            f"{tot:>{col_tot}}"
            f"{pct:>{col_pct}.1f}%"
            f"{flag}"
        )

    terminalreporter.write_line("-" * (col_lang + col_p + col_f + col_e + col_tot + col_pct))
    overall_pct = 100.0 * overall_passed / overall_total if overall_total else 0.0
    terminalreporter.write_line(
        f"{'TOTAL (iberian)':<{col_lang}}"
        f"{overall_passed:>{col_p}}"
        f"{overall_total - overall_passed:>{col_f}}"
        f"{'':>{col_e}}"
        f"{overall_total:>{col_tot}}"
        f"{overall_pct:>{col_pct}.1f}%"
    )
    terminalreporter.write_sep("=")
