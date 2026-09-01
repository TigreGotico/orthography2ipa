"""Guard against grapheme rules keyed to the wrong apostrophe-family
codepoint.

``ket.json`` mapped ``’`` U+2019 RIGHT SINGLE QUOTATION MARK to a glottal
stop, but the northeuralex gold's orthography column writes the same mark
as ``ʼ`` U+02BC MODIFIER LETTER APOSTROPHE. The rule never fired: it is
visually indistinguishable from a working one, but silently drops the
phoneme it encodes on every word that uses the codepoint the gold actually
writes (#1468). Nine more specs (niv, sid, oji, nhx, akk, srs, bdq, mak,
uk) plus liv carried the same defect.

These marks are not canonically equivalent, so no amount of Unicode
normalisation makes one match another -- the fix is to map every variant a
gold actually uses, which is what ``br``, ``ha``, ``car``, ``ty``, ``yrk``
and others already do.

A grapheme rule that matches nothing must not be able to look healthy: it
ships, passes every other test, and is inert on a slice of the input. That
applies to this guard too, so the marks each gold uses are committed as a
fixture rather than recomputed from a download or from a cache that only
exists on one machine. ``test_specs_map_every_apostrophe_codepoint_their_gold_uses``
therefore runs everywhere and needs no network and no gold; the companion
test re-derives the fixture from real golds when a cache is present, so the
fixture cannot silently drift away from the data it describes.

Only a spec that maps SOME apostrophe-family codepoint is held to this
standard. A spec mapping none has made no claim about the mark -- in many
orthographies it is punctuation or an elision marker rather than a
grapheme -- and that is a separate question from a rule keyed to the wrong
variant of a mark it does encode.
"""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402

from orthography2ipa.json_loader import load_json_spec  # noqa: E402


APOSTROPHE_FAMILY = frozenset(
    chr(cp) for cp in (0x2019, 0x02BC, 0x0027, 0x02BB, 0x2018))

_FIXTURE = os.path.join(
    os.path.dirname(__file__), "data", "apostrophe_gold_marks.json")


def _fmt(marks):
    return ",".join("U+%04X" % ord(c) for c in sorted(marks, key=ord))


def _gold_marks_fixture():
    with open(_FIXTURE, encoding="utf-8") as fh:
        raw = json.load(fh)
    return {
        key: {chr(int(cp[2:], 16)) for cp in cps}
        for key, cps in raw.items()
    }


def _spec_mapped_marks(lang):
    spec = load_json_spec(lang)
    graphemes = getattr(spec, "graphemes", None) or {}
    return {c for key in graphemes for c in key if c in APOSTROPHE_FAMILY}


def _block_network(*args, **kwargs):
    raise RuntimeError("network access is not allowed in this test")


def test_specs_map_every_apostrophe_codepoint_their_gold_uses():
    fixture = _gold_marks_fixture()
    assert fixture, "the apostrophe gold-marks fixture is empty"

    checked = 0
    failures = []
    for key, gold_marks in sorted(fixture.items()):
        lang = key.split("/", 1)[0]
        try:
            mapped = _spec_mapped_marks(lang)
        except Exception:
            continue
        if not mapped:
            continue  # spec makes no claim about the mark; see module docstring
        checked += 1
        missing = gold_marks - mapped
        if missing:
            failures.append(
                "%s: maps %s but the gold also uses %s -- add the missing "
                "apostrophe-family codepoint(s) as additional grapheme keys "
                "onto the same candidate(s)."
                % (key, _fmt(mapped), _fmt(missing)))

    assert checked > 0, (
        "no spec with apostrophe-family grapheme keys was checked against the "
        "fixture -- the fixture keys no longer resolve to specs, so this "
        "guard is silently checking nothing")
    assert not failures, (
        "apostrophe codepoint mismatch(es):\n" + "\n".join(failures))


def test_the_gold_marks_fixture_still_matches_the_real_golds():
    """The fixture is data about the golds, not about the specs, so it can
    only rot when a gold is re-scraped. Re-derive it wherever the golds are
    actually available."""
    cache = benchmark.CACHE_DIR
    if not (os.path.isdir(cache)
            and any(n.endswith(".tsv") for n in os.listdir(cache))):
        pytest.skip(
            "no gold cache under %s -- populate .benchmark_cache to re-derive "
            "the apostrophe fixture" % cache)

    fixture = _gold_marks_fixture()
    orig = benchmark.urllib.request.urlretrieve
    benchmark.urllib.request.urlretrieve = _block_network
    derived = {}
    seen = set()
    try:
        for dataset_name, (loader, langs) in benchmark.DATASETS.items():
            for lang in langs:
                if lang in seen:
                    continue
                try:
                    pairs = loader(lang, 200000)
                except Exception:
                    continue
                if not pairs:
                    continue
                seen.add(lang)
                marks = {c for word, _ipa in pairs
                         for c in word if c in APOSTROPHE_FAMILY}
                if marks:
                    derived["%s/%s" % (lang, dataset_name)] = marks
    finally:
        benchmark.urllib.request.urlretrieve = orig

    if not derived:
        pytest.skip(
            "the cache under %s holds no gold this fixture covers" % cache)

    stale = []
    for key, marks in sorted(derived.items()):
        recorded = fixture.get(key)
        if recorded is None:
            stale.append("%s: gold uses %s but the fixture has no entry"
                         % (key, _fmt(marks)))
        elif recorded != marks:
            stale.append("%s: fixture records %s, gold now uses %s"
                         % (key, _fmt(recorded), _fmt(marks)))
    assert not stale, (
        "tests/data/apostrophe_gold_marks.json is stale:\n" + "\n".join(stale))
