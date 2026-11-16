"""Packaged patches: a second entry-point group, read only when the caller asks.

A provider supplies the exceptions of a code through ``orthography2ipa.lexicons``
and its patches through ``orthography2ipa.lexicon_patches``. ``packaged_lexicon``
returns the exceptions; ``packaged_lexicon(code, patches=True)`` merges the
patches under them. The expected mappings are the rows each test writes, and the
rules reading of ⟨gato⟩ is the textbook pt-PT [ˈɡatu].
"""
from __future__ import annotations

import logging
from typing import Dict, List

import pytest

from orthography2ipa import G2P, Pipeline, packaged_lexicon
from orthography2ipa import lexicon as lexmod

pytestmark = pytest.mark.filterwarnings("ignore::DeprecationWarning")

GROUP = "orthography2ipa.lexicons"
PATCH_GROUP = "orthography2ipa.lexicon_patches"

GATO_RULES = "ˈɡatu"
GATO_EXCEPTION = "ˈɡaʃtɐ"
GATO_PATCH = "ˈɡɔtɔ"
RATO_PATCH = "ˈʁɔtu"


class _Dist:
    name = "fake-lexicons"


class _EntryPoint:
    dist = _Dist()

    def __init__(self, group, name, provider):
        self.group = group
        self.name = name
        self.value = f"fake-lexicons:{name}"
        self.provider = provider

    def load(self):
        return self.provider


@pytest.fixture
def installed(monkeypatch):
    """The entry points the test adds, by group, and nothing else, are installed."""
    points: Dict[str, List[_EntryPoint]] = {GROUP: [], PATCH_GROUP: []}
    calls: List[str] = []

    def fake_entry_points(group=None):
        calls.append(group)
        return list(points.get(group, []))

    monkeypatch.setattr(lexmod, "entry_points", fake_entry_points)
    monkeypatch.delenv(lexmod.LEXICON_DIR_ENV, raising=False)
    lexmod.clear_lexicons()
    yield points, calls
    lexmod.clear_lexicons()


def tsv(tmp_path, name, *rows):
    path = tmp_path / name
    path.write_text("".join(f"{w}\t{ipa}\n" for w, ipa in rows), encoding="utf-8")
    return path


def provide(points, group, code, path, seen=None):
    def provider(name):
        if seen is not None:
            seen.append(name)
        return path
    points[group].append(_EntryPoint(group, code, provider))


@pytest.fixture
def pt_both(installed, tmp_path):
    """A pt-PT provider of one exception (gato) and one patch (rato)."""
    points, calls = installed
    exceptions = tsv(tmp_path, "exceptions.tsv", ("gato", GATO_EXCEPTION))
    patches = tsv(tmp_path, "patches.tsv", ("rato", RATO_PATCH))
    provide(points, GROUP, "pt-PT", exceptions)
    provide(points, PATCH_GROUP, "pt-PT", patches)
    return exceptions, patches, calls


def test_patches_join_the_lexicon_only_when_asked(pt_both):
    assert packaged_lexicon("pt-PT") == {"gato": GATO_EXCEPTION}
    assert packaged_lexicon("pt-PT", patches=True) == {
        "gato": GATO_EXCEPTION, "rato": RATO_PATCH}
    assert G2P("pt-PT").transcribe_word("gato") == GATO_RULES


def test_an_exception_wins_over_a_patch_for_the_same_word(installed, tmp_path):
    points, _ = installed
    provide(points, GROUP, "pt-PT", tsv(tmp_path, "e.tsv", ("gato", GATO_EXCEPTION)))
    provide(points, PATCH_GROUP, "pt-PT",
            tsv(tmp_path, "p.tsv", ("gato", GATO_PATCH), ("rato", RATO_PATCH)))

    lexicon = packaged_lexicon("pt-PT", patches=True)

    assert lexicon == {"gato": GATO_EXCEPTION, "rato": RATO_PATCH}
    engine = G2P("pt-PT", pipeline=Pipeline(lexicon=lexicon))
    assert engine.transcribe_word("gato") == GATO_EXCEPTION
    assert engine.transcribe_word("rato") == RATO_PATCH


def test_asking_for_absent_patches_raises(installed, tmp_path):
    points, _ = installed
    provide(points, GROUP, "pt-PT", tsv(tmp_path, "e.tsv", ("gato", GATO_EXCEPTION)))

    with pytest.raises(LookupError, match="patch file for 'pt-PT'"):
        packaged_lexicon("pt-PT", patches=True)
    assert packaged_lexicon("pt-PT") == {"gato": GATO_EXCEPTION}


def test_patches_without_exceptions_raise(installed, tmp_path):
    points, _ = installed
    provide(points, PATCH_GROUP, "pt-PT", tsv(tmp_path, "p.tsv", ("rato", RATO_PATCH)))

    with pytest.raises(LookupError, match="lexicon file for 'pt-PT'"):
        packaged_lexicon("pt-PT", patches=True)
    assert lexmod.packaged_lexicon_sources(patches=True) == {"pt-PT": tmp_path / "p.tsv"}


def test_a_failing_patch_provider_raises_and_logs(installed, tmp_path, caplog):
    points, _ = installed
    provide(points, GROUP, "pt-PT", tsv(tmp_path, "e.tsv", ("gato", GATO_EXCEPTION)))

    def broken(code):
        raise RuntimeError("patch data missing")

    points[PATCH_GROUP].append(_EntryPoint(PATCH_GROUP, "pt-PT", broken))

    with caplog.at_level(logging.WARNING, logger="orthography2ipa.lexicon"):
        with pytest.raises(LookupError, match="patch file"):
            packaged_lexicon("pt-PT", patches=True)
    assert "patch data missing" in caplog.text


def test_patch_provider_resolves_an_alias_and_gets_its_own_name(installed, tmp_path):
    points, _ = installed
    seen: List[str] = []
    provide(points, GROUP, "pt-PT", tsv(tmp_path, "e.tsv", ("gato", GATO_EXCEPTION)))
    provide(points, PATCH_GROUP, "pt-PT", tsv(tmp_path, "p.tsv", ("rato", RATO_PATCH)), seen)

    assert packaged_lexicon("pt", patches=True)["rato"] == RATO_PATCH
    assert seen == ["pt-PT"]


def test_sources_list_each_kind_apart(pt_both):
    exceptions, patches, _ = pt_both

    assert lexmod.packaged_lexicon_sources() == {"pt-PT": exceptions}
    assert lexmod.packaged_lexicon_sources(patches=True) == {"pt-PT": patches}


def test_the_patch_group_is_read_only_when_patches_are_asked_for(pt_both):
    _, _, calls = pt_both

    packaged_lexicon("pt-PT")
    lexmod.packaged_lexicon_sources()
    assert calls == [GROUP]

    packaged_lexicon("pt-PT", patches=True)
    packaged_lexicon("pt-PT", patches=True)
    assert calls == [GROUP, PATCH_GROUP]


def test_the_deprecated_switch_never_enables_patches(pt_both):
    # The patch provider is live, so its absence below is not vacuous.
    assert packaged_lexicon("pt-PT", patches=True)["rato"] == RATO_PATCH

    lexmod.use_packaged_lexicons(["pt-PT"])

    assert lexmod.get_lexicon("pt-PT") == {"gato": GATO_EXCEPTION}
    assert G2P("pt-PT").transcribe_word("gato") == GATO_EXCEPTION
