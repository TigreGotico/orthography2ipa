"""Tests for competitor-derived and LLM-generated gold.

A gold set's value is its ERROR MODEL:

- human / lexicon gold is trustworthy;
- rule-system gold (espeak, epitran) measures agreement with a system this
  project benchmarks itself AGAINST (docs/comparison.md scores both
  ``espeak_per`` and ``epitran_per``), so it is diagnostic — a deterministic
  rule system's disagreements can be traced to a rule and adjudicated — but it
  can never CERTIFY us;
- LLM gold has no lexicon, no rules and therefore no error model at all: a
  disagreement is not even attributable, so it certifies nothing and diagnoses
  nothing.

These tests are the forcing function for that distinction: the tiers exist, the
IPA-CHILDES rows carry the tier of the TOOL its dataset card names for that
language (not one flattering dataset-wide tier), and no such row can qualify a
language for the ``production`` quality tier (docs/quality_tiers.md).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import (  # noqa: E402
    COMPETITOR_DERIVED_TIERS,
    DATASETS,
    NON_QUALIFYING_TIERS,
    PROVENANCE,
    PROVENANCE_BY_LANG,
    RELIABILITY_TIERS,
    _IPA_CHILDES_FOLDERS,
    _IPA_CHILDES_PROVENANCE,
    _IPA_CHILDES_TOOL,
    can_gate_promotion,
    provenance_for,
)

# The promotion bar of docs/quality_tiers.md, in code, so the rule can be tested.
PRODUCTION_MIN_N = 500


def _promotable(rows) -> bool:
    """Is there a scoreboard row that may qualify a language for `production`?
    Mirrors docs/quality_tiers.md: at least 500 evaluated entries on a gold
    whose tier can gate."""
    return any(
        row["n"] >= PRODUCTION_MIN_N and can_gate_promotion(row["provenance"])
        for row in rows
    )


def test_competitor_tiers_exist_and_are_ordered_last():
    """espeak/epitran/LLM gold are the least trustworthy tiers, in that order."""
    assert COMPETITOR_DERIVED_TIERS == {"espeak-derived", "epitran-derived"}
    assert RELIABILITY_TIERS[-3:] == (
        "espeak-derived",
        "epitran-derived",
        "llm-generated",
    )
    assert NON_QUALIFYING_TIERS == COMPETITOR_DERIVED_TIERS | {"llm-generated"}


def test_can_gate_promotion_refuses_competitor_and_llm_gold():
    for tier in ("expert-human", "lexicon-derived", "crowd-scraped",
                 "machine-generated"):
        assert can_gate_promotion(tier) is True
    for tier in ("espeak-derived", "epitran-derived", "llm-generated"):
        assert can_gate_promotion(tier) is False


def test_can_gate_promotion_rejects_unknown_tier():
    """A typo'd tier must blow up, never silently pass the gate."""
    try:
        can_gate_promotion("hand-wavy")
    except ValueError:
        return
    raise AssertionError("unknown tier silently accepted")


def test_language_with_only_competitor_gold_is_not_promotable():
    """A language whose only >=500-entry gold is a competitor's own output has
    NO usable gold: it stays at `research` (docs/quality_tiers.md)."""
    rows = [
        {"lang": "xx", "dataset": "ipa_childes", "n": 18055,
         "provenance": "espeak-derived"},
        {"lang": "xx", "dataset": "ipa_childes", "n": 9647,
         "provenance": "epitran-derived"},
        {"lang": "xx", "dataset": "wikipron", "n": 12,
         "provenance": "crowd-scraped"},  # trustworthy but far under the bar
    ]
    assert not _promotable(rows)

    rows.append({"lang": "xx", "dataset": "cmudict", "n": 600,
                 "provenance": "lexicon-derived"})
    assert _promotable(rows)


def test_language_with_only_llm_gold_is_not_promotable():
    """LLM gold has no error model; it can never qualify a promotion, at any N."""
    rows = [
        {"lang": "xx", "dataset": "mirandese_dict", "n": 50000,
         "provenance": "llm-generated"},
    ]
    assert not _promotable(rows)


def test_llm_generated_datasets_are_tiered_as_such():
    """The two LLM-written IPA dictionaries must not hide under
    `machine-generated` alongside real phonemizer output."""
    assert PROVENANCE["barranquenho_dict"] == "llm-generated"
    assert PROVENANCE["mirandese_dict"] == "llm-generated"


def test_ipa_childes_is_classified_per_language_by_its_tool():
    """IPA-CHILDES names a DIFFERENT phonemizing tool per language on its
    dataset card; the tier must follow the tool, mechanically."""
    assert PROVENANCE_BY_LANG["ipa_childes"] is _IPA_CHILDES_PROVENANCE
    assert sorted(_IPA_CHILDES_TOOL) == sorted(_IPA_CHILDES_FOLDERS)
    for lang, tool in _IPA_CHILDES_TOOL.items():
        tier = provenance_for("ipa_childes", lang)
        if tool.startswith("phonemizer"):
            assert tier == "espeak-derived", lang
        elif tool.startswith("epitran"):
            assert tier == "epitran-derived", lang
        else:
            assert tier == "machine-generated", lang


def test_ipa_childes_known_tool_assignments():
    """Spot-check the dataset card's own table: `phonemizer` (espeak-ng) for
    EnglishNA/Estonian, `epitran` for Indonesian/Hungarian/Serbian/German/
    Spanish/Croatian, `pinyin_to_ipa` for Mandarin. These six were previously
    all tagged `machine-generated`, which was wrong for every one of them
    except Mandarin."""
    assert provenance_for("ipa_childes", "en-US") == "espeak-derived"
    assert provenance_for("ipa_childes", "et") == "espeak-derived"
    assert provenance_for("ipa_childes", "id") == "epitran-derived"
    assert provenance_for("ipa_childes", "hu") == "epitran-derived"
    assert provenance_for("ipa_childes", "sr") == "epitran-derived"
    assert provenance_for("ipa_childes", "zh") == "machine-generated"


def test_ipa_childes_dataset_wide_fallback_cannot_gate():
    """An ipa_childes language with no explicit tool classification must
    degrade to a tier that can never qualify a promotion, never to a
    flattering one."""
    assert not can_gate_promotion(PROVENANCE["ipa_childes"])
    assert not can_gate_promotion(provenance_for("ipa_childes", "unclassified"))


def test_ipa_babylm_is_espeak_derived():
    """IPA-BabyLM's IPA comes from G2P+, which wraps phonemizer/espeak-ng; the
    conversion notebook (codebyzeb/babylm-ipa) calls the phonemizer backend
    with language en-us. It is espeak output and cannot gate English."""
    assert PROVENANCE["ipa_babylm"] == "espeak-derived"
    assert not can_gate_promotion(provenance_for("ipa_babylm", "en-US"))
    assert DATASETS["ipa_babylm"][1] == ["en-US"]


def test_ipa_childes_languages_are_real_spec_codes():
    from orthography2ipa import available_codes

    unknown = sorted(set(_IPA_CHILDES_FOLDERS) - set(available_codes()))
    assert not unknown, f"ipa_childes languages with no spec: {unknown}"
