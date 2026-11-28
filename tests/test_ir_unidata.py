"""The IR compiler reads the pinned Unicode table, not the host unicodedata."""
import unicodedata

import pytest

from orthography2ipa.ir import cache, compiler, layout, unidata

# Unassigned in every Unicode version so far.
_NEW_LETTER = chr(0xE0080)


class _HostUnicode:
    """The host unicodedata of an older or a newer Python. The newer one assigns
    one more Latin letter and, as Python 3.14 and 3.13.14 do, lists the
    decompositions of the Hangul syllables."""

    def __init__(self, newer: bool):
        self.newer = newer

    def __getattr__(self, name):
        return getattr(unicodedata, name)

    def category(self, c):
        return "Ll" if self.newer and c == _NEW_LETTER else unicodedata.category(c)

    def name(self, c, *default):
        if self.newer and c == _NEW_LETTER:
            return "LATIN SMALL LETTER NEW"
        return unicodedata.name(c, *default)

    def decomposition(self, c):
        if "가" <= c <= "힣":
            return " ".join(f"{ord(x):04X}" for x in unicodedata.normalize("NFD", c)) if self.newer else ""
        return unicodedata.decomposition(c)


def _clear_caches():
    for cached in (compiler._base_ir, compiler._script_chars, compiler._compositions):
        cached.cache_clear()


def _ir_bytes(monkeypatch, code, host):
    monkeypatch.setattr(compiler, "unicodedata", host)
    _clear_caches()
    return layout.canonical_bytes(compiler.compile_spec(code, **cache.DEFAULT_OPTIONS))


@pytest.fixture(autouse=True)
def fresh_caches():
    yield
    _clear_caches()


@pytest.mark.parametrize("code", ["eo", "ko"])
def test_ir_bytes_do_not_follow_the_host_unicode_version(code, monkeypatch):
    older = _ir_bytes(monkeypatch, code, _HostUnicode(newer=False))
    assert _ir_bytes(monkeypatch, code, _HostUnicode(newer=True)) == older


def test_source_names_the_pinned_version():
    doc = layout.decode(compiler.compile_spec("eo", **cache.DEFAULT_OPTIONS))
    assert doc["source"]["unidata"] == unidata.VERSION == "14.0.0"


def test_every_pinned_codepoint_is_assigned_on_the_host():
    # Unicode never unassigns a codepoint, so the host knows every one the table admits.
    lost = [cp for cp in range(0x110000)
            if unidata.assigned(chr(cp)) and unicodedata.category(chr(cp)) == "Cn"]
    assert lost == []
