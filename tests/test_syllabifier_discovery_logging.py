"""Discovery logging for syllabifier plugins — expected absence vs real failure.

A plugin's own optional third-party dependency being missing (e.g.
``silabificador`` for ``pip install orthography2ipa[portuguese]``) is the
documented normal case for an ordinary install, not a defect. It must not be
reported at the same level as a plugin that IS installed but fails to load.
Either way, a broken plugin must never take the working ones down with it.
"""
import logging

from orthography2ipa import registry


class _FakeEntryPoint:
    """Stands in for an ``importlib.metadata.EntryPoint``."""

    def __init__(self, name, cls):
        self.name = name
        self._cls = cls

    def load(self):
        return self._cls


class _MissingOptionalDependencyPlugin:
    """Stands in for a plugin whose bundled optional package is not
    installed — the expected case, e.g. ``SilabificadorSyllabifier`` without
    ``silabificador`` present."""

    def __init__(self):
        raise ModuleNotFoundError("No module named 'not_a_real_package'")

    def syllabify(self, word, lang=None):
        return [word]

    @property
    def language_codes(self):
        return ["xx"]

    @property
    def priority(self):
        return 50


class _RaisingPlugin:
    """Stands in for a plugin that IS installed but fails to load."""

    def __init__(self):
        raise RuntimeError("boom")

    def syllabify(self, word, lang=None):
        return [word]

    @property
    def language_codes(self):
        return ["yy"]

    @property
    def priority(self):
        return 50


class _WorkingPlugin:
    """A plugin that loads fine — must survive a neighbour's failure."""

    def syllabify(self, word, lang=None):
        return [word]

    @property
    def language_codes(self):
        return ["zz"]

    @property
    def priority(self):
        return 50


def test_missing_optional_dependency_is_debug_not_warning(monkeypatch, caplog):
    """An ordinary install without the optional extra logs nothing a user
    would see by default — it is DEBUG, not WARNING."""
    eps = [
        _FakeEntryPoint("missing_optional", _MissingOptionalDependencyPlugin),
        _FakeEntryPoint("working", _WorkingPlugin),
    ]
    monkeypatch.setattr(registry, "entry_points", lambda group=None: eps)

    with caplog.at_level(logging.DEBUG, logger="orthography2ipa.registry"):
        plugins = registry._discover_syllabifiers()

    warnings = [r for r in caplog.records if r.levelno >= logging.WARNING]
    debugs = [r for r in caplog.records if r.levelno == logging.DEBUG]
    assert warnings == []
    assert any("missing_optional" in r.getMessage() for r in debugs)

    # the other, working plugin is still discovered
    assert "zz" in plugins
    assert isinstance(plugins["zz"], _WorkingPlugin)


def test_a_real_failure_still_warns(monkeypatch, caplog):
    """A plugin that IS installed but raises on load keeps its WARNING."""
    eps = [
        _FakeEntryPoint("raising", _RaisingPlugin),
        _FakeEntryPoint("working", _WorkingPlugin),
    ]
    monkeypatch.setattr(registry, "entry_points", lambda group=None: eps)

    with caplog.at_level(logging.DEBUG, logger="orthography2ipa.registry"):
        plugins = registry._discover_syllabifiers()

    warnings = [r for r in caplog.records if r.levelno >= logging.WARNING]
    assert len(warnings) == 1
    assert "raising" in warnings[0].getMessage()
    assert "boom" in warnings[0].getMessage()

    # the broken plugin does not take the working one down
    assert "zz" in plugins
    assert isinstance(plugins["zz"], _WorkingPlugin)
