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
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import (  # noqa: E402
    COMPETITOR_DERIVED_TIERS,
    DATASETS,
    NON_QUALIFYING_TIERS,
    PROVENANCE,
    PROVENANCE_BY_LANG,
    GATING_CUTOFF_TIER,
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


def test_gating_power_is_monotonic_in_tier_order():
    """RELIABILITY_TIERS reads as a quality ladder, so it must BE one.

    Every reader of that tuple takes an earlier position to mean more
    trustworthy, and acts on it: reclassifying a row they have just shown to
    be untrustworthy moves it DOWN the tuple. If gating power did not follow
    the order, that move could hand a gating vote to the row instead of
    taking one away, and nothing in the diff would look wrong. So the
    invariant is that gating power never increases as the tuple advances.
    """
    powers = [(tier, can_gate_promotion(tier)) for tier in RELIABILITY_TIERS]
    for (earlier, earlier_gates), (later, later_gates) in zip(powers, powers[1:]):
        assert earlier_gates >= later_gates, (
            f"{earlier!r} is ordered before {later!r} in RELIABILITY_TIERS but "
            f"gates={earlier_gates} while {later!r} gates={later_gates}: "
            f"reclassifying a row from {earlier!r} to {later!r} reads as a "
            f"downgrade and would GRANT it a gating vote"
        )


def test_gating_cutoff_is_the_last_gating_tier():
    """The cutoff constant names the boundary, so it must sit on it."""
    assert can_gate_promotion(GATING_CUTOFF_TIER) is True
    after = RELIABILITY_TIERS[RELIABILITY_TIERS.index(GATING_CUTOFF_TIER) + 1:]
    assert after, "the cutoff cannot be the last tier: nothing would be excluded"
    assert not any(can_gate_promotion(tier) for tier in after)


def test_agreement_tiers_extend_the_non_gating_tiers():
    """The two tier lattices may differ, but only in the documented direction.

    scripts/compare_systems.py keeps its own, narrower set of tiers a "we beat
    espeak" claim can rest on. A tier that cannot gate a quality decision here
    can certainly not support a comparison claim there, so the non-gating set
    must stay a subset of that module's agreement set. The reverse containment
    is deliberately NOT asserted: `machine-generated` is an agreement tier
    there and still gates here, for the reason given at GATING_CUTOFF_TIER.
    """
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
    from compare_systems import _AGREEMENT_TIERS, _GOLD_TIERS

    assert NON_QUALIFYING_TIERS <= _AGREEMENT_TIERS
    assert _GOLD_TIERS | _AGREEMENT_TIERS == set(RELIABILITY_TIERS)
    assert not (_GOLD_TIERS & _AGREEMENT_TIERS)


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


class TestGatingFieldDerivedAndRendered:
    """`build_scoreboard` writes each row's qualify/block determination as a
    `gating` field, derived from the row's own `provenance` via
    `can_gate_promotion()` — the SAME function `docs/quality_tiers.md`'s
    `production` criteria already use. Nothing computes qualification a
    second way: a hand-authored `gating` value that fell out of sync with
    `provenance` is exactly the defect #1351 reports.
    """

    def test_gating_matches_can_gate_promotion_for_every_tier(self):
        """The field is not a second policy: it IS `can_gate_promotion`
        applied to the row's provenance, for every tier in the lattice."""
        from benchmark import RELIABILITY_TIERS

        for tier in RELIABILITY_TIERS:
            row = {"provenance": tier}
            row["gating"] = can_gate_promotion(row["provenance"])
            assert row["gating"] == can_gate_promotion(tier)
            if tier in NON_QUALIFYING_TIERS:
                assert row["gating"] is False
            else:
                assert row["gating"] is True

    def test_build_scoreboard_writes_gating_from_live_provenance(self, monkeypatch):
        """An end-to-end row from `build_scoreboard` carries `gating` in
        agreement with `provenance_for()` for that dataset/language — not a
        constant, not omitted."""
        import benchmark

        def fake_loader(lang, limit):
            return [("saluton", "saluton")]

        monkeypatch.setitem(
            benchmark.DATASETS, "_fake_gating_ds", (fake_loader, ["eo"]))
        monkeypatch.setitem(benchmark.PROVENANCE, "_fake_gating_ds", "espeak-derived")
        try:
            rows = benchmark.build_scoreboard(
                None, only_langs=["eo"], only_datasets=["_fake_gating_ds"])
        finally:
            benchmark.DATASETS.pop("_fake_gating_ds", None)
            benchmark.PROVENANCE.pop("_fake_gating_ds", None)
        assert len(rows) == 1
        row = rows[0]
        assert row["provenance"] == "espeak-derived"
        assert row["gating"] is False
        assert row["gating"] == can_gate_promotion(row["provenance"])

    def test_backfilled_results_json_gating_matches_provenance(self):
        """Every one of the 643 committed rows carries a `gating` value that
        agrees with `can_gate_promotion(row["provenance"])` — the backfill
        must be a pure derivation, never a hand patch that can drift."""
        path = os.path.join(
            os.path.dirname(__file__), "..", "benchmarks", "results.json")
        with open(path, encoding="utf-8") as fh:
            rows = json.load(fh)
        assert len(rows) == 643
        mismatched = [
            (r["lang"], r["dataset"]) for r in rows
            if r.get("gating") != can_gate_promotion(r["provenance"])
        ]
        assert not mismatched, (
            f"rows whose committed `gating` disagrees with a fresh "
            f"can_gate_promotion(provenance) recomputation: {mismatched}")

    def test_non_qualifying_row_renders_distinct_per_marker(self, tmp_path, monkeypatch):
        """A non-qualifying row's `PER` cell in scoreboard.md carries the
        NON_QUALIFYING_MARK; a qualifying row's does not."""
        import benchmark

        monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(tmp_path / "r.json"))
        monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(tmp_path / "s.md"))
        rows = [
            dict(lang="xx", dataset="ds1", n=100, per=0.4351,
                 per_ci_low=0.4, per_ci_high=0.47, exact_match=0.5,
                 quality_tier="research", provenance="espeak-derived",
                 harness_version="1.1", limit=None, gating=False),
            dict(lang="yy", dataset="ds2", n=100, per=0.1234,
                 per_ci_low=0.1, per_ci_high=0.15, exact_match=0.9,
                 quality_tier="research", provenance="crowd-scraped",
                 harness_version="1.1", limit=None, gating=True),
        ]
        benchmark.write_scoreboard(rows)
        text = (tmp_path / "s.md").read_text(encoding="utf-8")
        xx_line = next(ln for ln in text.splitlines() if ln.startswith("| xx |"))
        yy_line = next(ln for ln in text.splitlines() if ln.startswith("| yy |"))
        assert f"0.4351{benchmark.NON_QUALIFYING_MARK}" in xx_line, xx_line
        assert benchmark.NON_QUALIFYING_MARK not in yy_line, yy_line

    def test_gating_true_never_marks_and_field_absent_never_marks(self, tmp_path, monkeypatch):
        """Only an explicit `gating: False` marks the PER cell. A legacy row
        with no `gating` key (pre-#1351 board) must not be misread as
        non-qualifying."""
        import benchmark

        monkeypatch.setattr(benchmark, "SCOREBOARD_JSON", str(tmp_path / "r.json"))
        monkeypatch.setattr(benchmark, "SCOREBOARD_MD", str(tmp_path / "s.md"))
        rows = [
            dict(lang="zz", dataset="ds3", n=100, per=0.3000,
                 per_ci_low=0.25, per_ci_high=0.35, exact_match=0.5,
                 quality_tier="research", provenance="crowd-scraped",
                 harness_version="1.1", limit=None),
        ]
        benchmark.write_scoreboard(rows)
        text = (tmp_path / "s.md").read_text(encoding="utf-8")
        zz_line = next(ln for ln in text.splitlines() if ln.startswith("| zz |"))
        assert benchmark.NON_QUALIFYING_MARK not in zz_line, zz_line

    def test_gating_round_trips_through_regeneration(self, monkeypatch):
        """Regenerating a targeted subset (`build_scoreboard` +
        `merge_scoreboard_rows`, the real refresh path — see
        `o2i-board-regen`) must reproduce the SAME `gating` value the
        committed row already carries, for a row picked from the actual
        committed board. A hand-authored value that happened to agree with
        `provenance` once, but is not RECOMPUTED on refresh, is exactly
        the defect #1351 reports and would NOT be caught by a static
        equality check against a freshly-hand-built dict — it must be
        caught by re-running the real scoring/merge path."""
        import benchmark

        committed = benchmark.read_scoreboard_rows()
        target = next(r for r in committed
                      if r["lang"] == "eo" and r["dataset"] == "wikipron")
        assert "gating" in target

        def fake_loader(lang, limit):
            return [("saluton", "saluton")]

        monkeypatch.setitem(
            benchmark.DATASETS, "wikipron", (fake_loader, ["eo"]))
        fresh = benchmark.build_scoreboard(
            None, only_langs=["eo"], only_datasets=["wikipron"])
        merged = benchmark.merge_scoreboard_rows(committed, fresh)
        refreshed = next(r for r in merged
                          if r["lang"] == "eo" and r["dataset"] == "wikipron")

        assert refreshed["gating"] == target["gating"]
        assert refreshed["gating"] == can_gate_promotion(refreshed["provenance"])
