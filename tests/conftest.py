"""Shared fixtures and configuration for orthography2ipa test suite."""
import pytest

import orthography2ipa
from orthography2ipa.types import LanguageSpec


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
