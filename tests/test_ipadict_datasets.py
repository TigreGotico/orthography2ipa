"""Tests for the ipa-dict gold corpus (open-dict-data/ipa-dict).

ipa-dict is a COLLECTION of independently-sourced dictionaries, not one
source: a human Icelandic dictionary (Hjal/malfong), a Wiktionary-built
German list, rule-script Spanish, and espeak-generated British English all
live in the same project. A single dataset-wide reliability tier would
therefore be a lie, so the harness classifies this dataset PER LANGUAGE
(``PROVENANCE_BY_LANG`` / :func:`provenance_for`). These tests are the
forcing function for that: no ipa-dict language can be registered without
its own evidence-based tier, and the espeak-derived row must stay marked as
such (an espeak gold can neither qualify nor block a language —
docs/quality_tiers.md).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402
from benchmark import (  # noqa: E402
    DATASETS,
    PROVENANCE,
    PROVENANCE_BY_LANG,
    RELIABILITY_TIERS,
    _IPADICT_FILES,
    _IPADICT_PROVENANCE,
    _IPADICT_UNWIRED,
    build_scoreboard,
    load_ipadict,
    provenance_for,
)


def test_registered_languages_are_real_spec_codes():
    """Every wired language must resolve to a registered spec — no invented
    tags, and no gold registered against a language the engine cannot load."""
    from orthography2ipa import available_codes

    codes = set(available_codes())
    unknown = sorted(set(_IPADICT_FILES) - codes)
    assert not unknown, f"ipadict langs with no spec: {unknown}"


def test_dataset_registry_lists_every_wired_language():
    loader, langs = DATASETS["ipadict"]
    assert loader is load_ipadict
    assert langs == sorted(_IPADICT_FILES)


def test_every_wired_language_has_its_own_provenance_tier():
    """Forcing function: wiring an ipa-dict language without classifying its
    provenance fails CI. The dataset-wide tier must never silently cover a
    newly wired file."""
    missing = sorted(set(_IPADICT_FILES) - set(_IPADICT_PROVENANCE))
    assert not missing, f"ipadict langs with no per-language tier: {missing}"

    orphan = sorted(set(_IPADICT_PROVENANCE) - set(_IPADICT_FILES))
    assert not orphan, f"per-language tiers for unregistered langs: {orphan}"


def test_per_language_tiers_are_known_values():
    for lang, tier in _IPADICT_PROVENANCE.items():
        assert tier in RELIABILITY_TIERS, f"{lang}: unknown tier {tier!r}"


def test_english_uk_is_marked_espeak_derived():
    """ipa-dict's en_UK comes from ipacards, whose own CREDITS and
    bin/add-ipa-to-freq.py shell out to `espeak`. Scoring against it measures
    agreement with a competitor, so the tier must stay `espeak-derived` — it
    can neither qualify nor block English."""
    assert _IPADICT_PROVENANCE["en-GB"] == "espeak-derived"
    assert provenance_for("ipadict", "en-GB") == "espeak-derived"


def test_unwired_languages_are_documented_and_not_registered():
    """Files left out carry a recorded reason and must not also be wired."""
    overlap = set(_IPADICT_UNWIRED) & set(_IPADICT_FILES.values())
    assert not overlap, f"unwired files that are also registered: {overlap}"
    for code, reason in _IPADICT_UNWIRED.items():
        assert reason.strip(), f"{code} left out with no reason"


def test_provenance_for_prefers_the_per_language_tier():
    """A mixed-provenance dataset's row carries the tier of the FILE it was
    scored against, not the dataset-wide fallback."""
    assert provenance_for("ipadict", "is") == "lexicon-derived"
    assert provenance_for("ipadict", "es-ES") == "machine-generated"
    assert provenance_for("ipadict", "de-DE") == "crowd-scraped"
    # single-source datasets are unaffected
    assert provenance_for("wikipron", "gl") == PROVENANCE["wikipron"]


def test_provenance_for_falls_back_to_the_pessimistic_dataset_tier():
    """An unclassified language degrades to distrust, never to a better tier
    it did not earn."""
    assert "xx" not in _IPADICT_PROVENANCE
    assert provenance_for("ipadict", "xx") == PROVENANCE["ipadict"]
    assert PROVENANCE["ipadict"] == "machine-generated"
    assert PROVENANCE_BY_LANG["ipadict"] is _IPADICT_PROVENANCE


def test_loader_parses_word_tab_slashed_ipa(tmp_path, monkeypatch):
    lines = "hus\t/hʉːs/\nkatt\t/katː/\n"
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: lines)
    pairs = load_ipadict("is", 10)
    assert pairs == [("hus", "hʉːs"), ("katt", "katː")]


def test_loader_emits_one_pair_per_comma_separated_variant(monkeypatch):
    """ipa-dict lists every attested pronunciation for a word, comma
    separated (`est  /ɛst/, /ɛ/`). Each becomes its own gold pair, which is
    how evaluate_words consumes multiple valid golds per word."""
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: "est\t/ɛst/, /ɛ/\n")
    assert load_ipadict("fr-FR", 10) == [("est", "ɛst"), ("est", "ɛ")]


def test_loader_limit_counts_emitted_pairs(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: "est\t/ɛst/, /ɛ/\nun\t/œ̃/\n")
    assert load_ipadict("fr-FR", 2) == [("est", "ɛst"), ("est", "ɛ")]


def test_loader_skips_malformed_lines(monkeypatch):
    text = "good\t/ɡʊd/\nnotabbed /x/\nempty\t\n"
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: text)
    assert load_ipadict("en-US", 10) == [("good", "ɡʊd")]


def test_scoreboard_rows_carry_the_per_language_tier(monkeypatch):
    """The tier must travel with the ROW, so a scoreboard reader can never
    mistake the espeak-derived English row for the human Icelandic one."""
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: "a\t/a/\n")
    monkeypatch.setattr(
        benchmark, "DATASETS", {"ipadict": (load_ipadict, ["is", "en-GB"])})
    rows = {r["lang"]: r["provenance"] for r in build_scoreboard(limit=5)}
    assert rows["is"] == "lexicon-derived"
    assert rows["en-GB"] == "espeak-derived"
