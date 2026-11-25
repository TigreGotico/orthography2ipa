"""The spec field guard fails on a field the compiler ignores."""
import dataclasses
import importlib.util
from pathlib import Path

import pytest

from orthography2ipa.types import LanguageSpec

_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_spec_fields.py"
_spec = importlib.util.spec_from_file_location("check_spec_fields", _PATH)
guard = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(guard)


@dataclasses.dataclass(frozen=True)
class _SpecWithDummy(LanguageSpec):
    dummy_flag: bool = False


@pytest.fixture(autouse=True)
def _restore_root():
    yield
    guard._ROOT[:] = [LanguageSpec]


def test_unread_new_field_fails_the_guard():
    failures = guard.check(root=_SpecWithDummy, bases=("th",))
    assert any(f.startswith("_SpecWithDummy.dummy_flag: the compiler ignores it") for f in failures)


def test_declaring_the_new_field_clears_it(monkeypatch):
    monkeypatch.setitem(guard.INERT, "_SpecWithDummy.dummy_flag", "test field")
    failures = guard.check(root=_SpecWithDummy, bases=("th",))
    assert not any(f.startswith("_SpecWithDummy.dummy_flag") for f in failures)


def test_a_lowered_field_is_seen_as_lowered():
    from orthography2ipa import registry
    th = registry.get(registry.resolve("th"))
    assert guard.probe(LanguageSpec, "collapse_geminates", {"th": th}) == "lowered"


def test_a_stale_declaration_fails(monkeypatch):
    monkeypatch.setitem(guard.INERT, "LanguageSpec.no_such_field", "gone")
    monkeypatch.setitem(guard.INERT, "LanguageSpec.collapse_geminates", "wrongly declared")
    failures = guard.check(bases=("th",))
    assert "LanguageSpec.no_such_field: in INERT, but no such field" in failures
    assert "LanguageSpec.collapse_geminates: declared inert, but the IR changes with it" in failures


def test_a_field_that_only_grows_the_alphabet_is_not_lowered(monkeypatch):
    from orthography2ipa import registry
    from orthography2ipa.ir import compiler
    from orthography2ipa.types import StressRules
    monkeypatch.setattr(compiler, "cliticless_keys", lambda spec: ())
    th = registry.get(registry.resolve("th"))
    assert guard.probe(StressRules, "cliticless_words", {"th": th}) != "lowered"
