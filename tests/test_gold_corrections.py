"""Tests for the gold-corrections overlay mechanism.

An overlay repairs a mechanically-derivable defect in an upstream gold without
touching the upstream file, and is registered as its own dataset so the
uncorrected row stays on the board beside the corrected one.

Two properties are load-bearing and are asserted here rather than trusted:

* the corrections are derivable from the ORTHOGRAPHY — every row of the
  Vietnamese overlay is re-derived from the spelling's Unicode combining marks
  and must reproduce the committed file byte-for-byte;
* an overlay can never gate a promotion. A gold whose readings were rewritten
  by an automated process cannot certify the engine that is scored against it,
  and the tier the overlay is registered on has to say so.
"""
import ast
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import (  # noqa: E402
    DATASETS,
    GOLD_CORRECTIONS,
    PROVENANCE,
    apply_gold_corrections,
    can_gate_promotion,
    provenance_for,
    read_gold_corrections,
)
from build_gold_corrections import (  # noqa: E402
    TONE_LETTERS,
    VI_HUYEN_READING,
    VI_NGANG_READING,
    build_vi_tone_rows,
    vi_tone_from_spelling,
)

OVERLAY_FIELDS = {"dataset", "lang", "spelling", "original_reading",
                  "corrected_reading", "reason", "authority"}


def _overlays():
    return [(d, lang) for d, langs in GOLD_CORRECTIONS.items() for lang in langs]


@pytest.mark.parametrize("dataset,lang", _overlays())
def test_overlay_rows_are_complete_and_actually_change_something(dataset, lang):
    rows = read_gold_corrections(dataset, lang)
    assert rows
    for row in rows:
        assert set(row) == OVERLAY_FIELDS
        assert row["dataset"] == dataset and row["lang"] == lang
        assert row["original_reading"] != row["corrected_reading"]
        assert row["reason"].strip() and row["authority"].strip()


@pytest.mark.parametrize("dataset,lang", _overlays())
def test_overlay_is_registered_as_its_own_dataset(dataset, lang):
    """The corrected gold is a SEPARATE board row, never a rewrite of the
    original one: the difference between the two rows is the measurement of
    the upstream defect, and it is unreadable if only one number is published.
    """
    corrected = f"{dataset}_corrected"
    assert dataset in DATASETS
    assert corrected in DATASETS
    assert lang in DATASETS[corrected][1]


@pytest.mark.parametrize("dataset,lang", _overlays())
def test_no_overlay_can_gate_a_promotion(dataset, lang):
    """Whatever tier an overlay is registered on, it must be a non-gating one.

    A corrected gold is derived twice over — from a base gold and then from an
    automated correction pass — so it can diagnose, never certify.
    """
    # Through provenance_for, not PROVENANCE: scoring resolves a row's tier
    # that way, and a PROVENANCE_BY_LANG entry for the corrected dataset would
    # override the dataset-wide tier this test used to read.
    tier = provenance_for(f"{dataset}_corrected", lang)
    assert can_gate_promotion(tier) is False
    # and never more trustworthy than the base it was built from
    assert tier == provenance_for(dataset, lang)


def test_vi_tone_read_from_combining_marks_only():
    """The Vietnamese tone is read off the spelling. Vowel-quality diacritics
    (circumflex, breve, horn) are not tone marks and must not be mistaken for
    one, and a token carrying two tone marks is undeterminable, not a guess.
    """
    assert vi_tone_from_spelling("ma") == "ngang"
    assert vi_tone_from_spelling("mà") == "huyen"
    assert vi_tone_from_spelling("má") == "sac"
    assert vi_tone_from_spelling("mả") == "hoi"
    assert vi_tone_from_spelling("mã") == "nga"
    assert vi_tone_from_spelling("mạ") == "nang"
    # circumflex / breve / horn carry no tone
    assert vi_tone_from_spelling("tôi") == "ngang"
    assert vi_tone_from_spelling("ăn") == "ngang"
    assert vi_tone_from_spelling("từ") == "huyen"
    assert vi_tone_from_spelling("buồn") == "huyen"
    # two tone marks: two syllables in one token, no single tone to assign
    assert vi_tone_from_spelling("cà-phê") == "huyen"
    assert vi_tone_from_spelling("bàn là") is None


def test_vi_overlay_rederives_from_spelling_alone():
    """Re-derive every committed row from its own spelling and its own
    original reading, with no upstream file and no engine in the loop. The
    committed overlay must be exactly what the derivation produces.
    """
    committed = read_gold_corrections("vox_communis", "vi")
    rebuilt, stats = build_vi_tone_rows(
        [(r["spelling"], r["original_reading"]) for r in committed])
    assert stats["corrected"] == len(committed)
    assert rebuilt == sorted(
        committed, key=lambda r: (r["spelling"], r["original_reading"]))


def test_vi_overlay_only_touches_the_merged_tone_letter():
    for row in read_gold_corrections("vox_communis", "vi"):
        assert vi_tone_from_spelling(row["spelling"]) == "huyen"
        original, corrected = row["original_reading"], row["corrected_reading"]
        assert "".join(TONE_LETTERS.findall(original)) == VI_NGANG_READING
        assert "".join(TONE_LETTERS.findall(corrected)) == VI_HUYEN_READING
        # the segmental string is untouched
        assert (original.replace(VI_NGANG_READING, "")
                == corrected.replace(VI_HUYEN_READING, ""))


def test_uncorrectable_rows_are_left_alone():
    """Negative results are left in the gold, not guessed at: a grave-accented
    spelling whose reading is NOT the merged ˨˨, and a token whose tone cannot
    be read from the spelling, both stay uncorrected.
    """
    rows, stats = build_vi_tone_rows([
        ("mà", "maː˨˨"),           # correctable
        ("mà", "maː˨˩"),           # grave, but no merge to repair
        ("bàn là", "ɓaːn˨˨laː˨˨"),  # two tone marks, undeterminable
        ("ma", "maː˨˨"),           # ngang, not ours to touch
    ])
    assert [r["spelling"] for r in rows] == ["mà"]
    assert rows[0]["original_reading"] == "maː˨˨"
    assert stats == {"corrected": 1, "huyen_reading_not_ngang": 1,
                     "tone_undeterminable": 1, "not_huyen": 1}


def test_corrections_apply_only_on_an_exact_upstream_match():
    """A correction is keyed on the spelling AND the reading it was derived
    against. If upstream revises that reading, the correction must lapse
    rather than overwrite a row it was never inspected against.
    """
    row = read_gold_corrections("vox_communis", "vi")[0]
    pairs = [
        (row["spelling"], row["original_reading"]),
        (row["spelling"], row["original_reading"] + "ʔ"),  # upstream moved
        ("khong-in-the-overlay", "xoŋm˨˨"),
    ]
    out, applied, unmatched = apply_gold_corrections(pairs, "vox_communis", "vi")
    assert applied == 1
    assert out[0] == (row["spelling"], row["corrected_reading"])
    assert out[1:] == pairs[1:]
    assert unmatched == len(read_gold_corrections("vox_communis", "vi")) - 1


def _engine_module_references(tree):
    """Module names the source NAMES, by any of the routes that can reach one.

    Plain imports are only the obvious route. ``main()`` does ``import
    benchmark``, and scripts/benchmark.py imports the engine, so
    ``orthography2ipa`` is already live in ``sys.modules`` while the overlay
    builds: ``sys.modules[...]``, ``importlib.import_module(...)`` and
    ``__import__(...)`` all reach it without an import statement. Those three
    are read here as well.
    """
    named = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            named.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            named.add(node.module or "")
        elif isinstance(node, ast.Subscript):
            target = ast.unparse(node.value)
            if target.endswith("modules") and isinstance(node.slice, ast.Constant):
                named.add(str(node.slice.value))
        elif isinstance(node, ast.Call):
            callee = ast.unparse(node.func)
            if callee.endswith("import_module") or callee == "__import__":
                for arg in node.args[:1]:
                    if isinstance(arg, ast.Constant):
                        named.add(str(arg.value))
    return named


def test_overlay_never_names_the_engine():
    """The derivation path must not consult orthography2ipa. A gold repaired
    with this project's own answers would score beautifully and measure
    nothing.

    This is a SPELLING check over the source, not a proof of unreachability:
    the engine is live in ``sys.modules`` during the build (see
    :func:`_engine_module_references`), so nothing can stop a determined
    caller from getting at it. What the check does guarantee is that no route
    to the engine is written down in the file, across all four ways of naming
    a module.
    """
    path = os.path.join(os.path.dirname(__file__), "..", "scripts",
                        "build_gold_corrections.py")
    with open(path, encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    named = _engine_module_references(tree)
    assert not [m for m in named if m.split(".")[0] == "orthography2ipa"]


def test_upstream_gold_file_is_not_shipped_alongside_the_overlay():
    """The overlay repairs the upstream gold; it never replaces or vendors it.
    Nothing that looks like a copy of the cached upstream file may appear in
    the corrections directory.
    """
    directory = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa",
                             "data", "gold", "corrections")
    names = sorted(os.listdir(directory))
    assert names
    for name in names:
        assert name.endswith((".jsonl", ".md")), name
    for dataset, langs in GOLD_CORRECTIONS.items():
        for lang in langs:
            assert f"{dataset}_{lang}.jsonl" in names


def test_overlay_file_is_deterministic_jsonl():
    path = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa",
                        "data", "gold", "corrections", "vox_communis_vi.jsonl")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    keys = [(json.loads(ln)["spelling"], json.loads(ln)["original_reading"])
            for ln in lines]
    assert keys == sorted(keys)
    for line in lines:
        assert line == json.dumps(json.loads(line), ensure_ascii=False,
                                  sort_keys=True)


# ─── portuguese_unified ─────────────────────────────────────────────────────
#
# This overlay is keyed on the SOURCE row of the dataset, not on an o2i
# language tag, so its rows carry their own schema and are read through
# read_pt_unified_corrections rather than GOLD_CORRECTIONS.

from benchmark import (  # noqa: E402
    CORRECTED_DATASETS,
    PT_UNIFIED_CORRECTED_LANGS,
    _PT_UNIFIED_REGIONS,
    pt_unified_source,
    read_pt_unified_corrections,
    row_gates,
)
from build_gold_corrections import (  # noqa: E402
    PT_UNIFIED_BROAD_DECISIONS,
    PT_UNIFIED_DECISIONS,
    build_pt_unified_rows,
    pt_broad_from_narrow,
    pt_ie_mark,
    pt_ie_stressed,
)

PT_FIELDS = {"dataset", "source", "region", "word", "pos", "field",
             "original_reading", "corrected_reading", "kind", "reason",
             "authority"}
PT_KINDS = {"accent_contradiction", "unaccented_stress", "missing_mark",
            "wrong_headword", "mojibake"}
PT_SOURCES = {"infopedia", "infopedia+wiktionary", "wiktionary", "portal"}


def _marks_removed(reading):
    return reading.replace("ˈ", "").replace("'", "")


def test_pt_unified_rows_are_complete_and_keyed_on_the_source_row():
    rows = read_pt_unified_corrections()
    assert rows
    keys = set()
    for row in rows:
        assert set(row) == PT_FIELDS
        assert row["dataset"] == "portuguese_unified"
        assert row["source"] in PT_SOURCES
        assert row["field"] in ("ipa_narrow", "ipa_broad")
        assert row["kind"] in PT_KINDS
        assert row["original_reading"] != row["corrected_reading"]
        assert row["reason"].strip() and row["authority"].strip()
        key = (row["word"], row["region"], row["source"], row["pos"],
               row["field"], row["original_reading"])
        assert key not in keys
        keys.add(key)


def test_pt_unified_corrections_move_marks_and_keep_segments():
    """A stress correction moves, adds or removes a mark and nothing else.
    The only segment changes are a dropped variant and the two rows where a
    stray symbol stands in for the mark."""
    stand_ins = {"koitádu", "traveˡsejru"}
    for row in read_pt_unified_corrections():
        original, corrected = row["original_reading"], row["corrected_reading"]
        if corrected is None:
            assert row["kind"] in ("wrong_headword", "mojibake")
            continue
        if row["kind"] == "wrong_headword":
            assert set(corrected.split(",")) < set(original.split(","))
        elif original in stand_ins:
            assert row["kind"] == "missing_mark"
        else:
            assert _marks_removed(corrected) == _marks_removed(original)
            assert corrected.count("ˈ") + corrected.count("'") >= 1


def test_pt_unified_drops_are_only_headword_and_mojibake_rows():
    rows = read_pt_unified_corrections()
    dropped = [r for r in rows if r["corrected_reading"] is None]
    assert {r["kind"] for r in dropped} == {"wrong_headword", "mojibake"}
    for row in dropped:
        assert row["field"] == "ipa_narrow"
        if row["kind"] == "mojibake":
            assert "Ã" in row["original_reading"]


def test_pt_unified_corrected_langs_match_the_overlay():
    regions = {r["region"] for r in read_pt_unified_corrections()
               if r["field"] == "ipa_narrow"}
    expected = sorted(lang for lang, region in _PT_UNIFIED_REGIONS.items()
                      if region in regions)
    assert PT_UNIFIED_CORRECTED_LANGS == expected


def test_pt_unified_overlay_is_registered_and_never_gates():
    assert "portuguese_unified_corrected" in DATASETS
    assert "portuguese_unified_corrected" in CORRECTED_DATASETS
    for lang in PT_UNIFIED_CORRECTED_LANGS:
        tier = provenance_for("portuguese_unified_corrected", lang)
        assert tier == provenance_for("portuguese_unified", lang)
        assert row_gates(tier, 10 ** 6, "portuguese_unified_corrected") is False
    # the base row still gates on the same tier
    assert row_gates(provenance_for("portuguese_unified", "pt-PT"), 10 ** 6,
                     "portuguese_unified") is True


def test_pt_unified_overlay_file_is_deterministic_jsonl():
    path = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa",
                        "data", "gold", "corrections", "portuguese_unified_pt.jsonl")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    rows = [json.loads(line) for line in lines]
    keys = [(r["word"], r["region"], r["source"], r["pos"], r["field"],
             r["original_reading"]) for r in rows]
    assert keys == sorted(keys)
    for line in lines:
        assert line == json.dumps(json.loads(line), ensure_ascii=False,
                                  sort_keys=True)


def _upstream_row(word, region, ipa_narrow, ipa_broad="", source="portal", pos=""):
    return {"word": word, "region": region, "ipa_narrow": ipa_narrow,
            "ipa_broad": ipa_broad, "pos": pos,
            "phones": "x" if source == "portal" else "",
            "infopedia_url": "u" if "infopedia" in source else "",
            "wiktionary_url": "u" if "wiktionary" in source else ""}


def test_pt_unified_source_is_read_from_the_row():
    assert pt_unified_source(_upstream_row("a", "r", "a")) == "portal"
    assert pt_unified_source(_upstream_row("a", "r", "a", source="infopedia")) == "infopedia"
    assert pt_unified_source(_upstream_row("a", "r", "a", source="wiktionary")) == "wiktionary"
    assert pt_unified_source(
        _upstream_row("a", "r", "a", source="infopedia+wiktionary")) == "infopedia+wiktionary"


def test_pt_ie_rule_reads_the_stress_from_the_spelling():
    # paroxytone in -e/-a/-o with <ie>/<ee> as the next-to-last vowel group
    for word in ("paciente", "frieza", "ambiente", "guineense", "geena", "lamuriento"):
        assert pt_ie_stressed(word), word
    # <iê>: the circumflex settles it
    assert pt_ie_stressed("ciência") and pt_ie_stressed("biênio")
    # not the next-to-last group, another accent, or an oxytone ending
    for word in ("dieta-a", "variedade", "ciências-x", "paciência-mente",
                 "piedoso", "série", "quietar", "dieese"):
        assert not pt_ie_stressed(word), word
    assert pt_ie_mark("pɐsjẽtɨ") == "pɐsjˈẽtɨ"
    # decomposed nasal vowel: the mark goes before the base vowel
    assert pt_ie_mark("pɐsjẽtɨ") == "pɐsjˈẽtɨ"
    assert pt_ie_mark("pɐsjˈẽtɨ") is None           # already marked
    assert pt_ie_mark("sjẽsjẽ") is None             # two candidates
    assert pt_ie_mark("sjẽ") is None                # one nucleus


def test_pt_broad_follows_the_narrow_nucleus_and_the_source_convention():
    # Infopédia writes the mark before the onset, the Portal before the vowel
    assert pt_broad_from_narrow("buziˈliʃ", "buˈziliʃ", "infopedia") == "buˈziliʃ"
    assert pt_broad_from_narrow("klimˈaks", "klˈimaks", "portal") == "klˈimaks"
    assert pt_broad_from_narrow("aniˈdridu", "aˈnidridu", "infopedia") == "aˈnidridu"
    # a hiatus keeps its place: li-a-na
    assert pt_broad_from_narrow("liãna", "liˈɐ̃nɐ", "wiktionary") == "liˈãna"
    # already right, or nuclei that do not line up: no broad correction
    assert pt_broad_from_narrow("buˈziliʃ", "buˈziliʃ", "infopedia") is None
    assert pt_broad_from_narrow("buzliʃ", "buˈziliʃ", "infopedia") is None


def test_pt_build_corrects_drops_and_leaves_alone():
    rows = [
        # a decision in the table
        _upstream_row("busílis", "pt-PT", "buziˈliʃ", "buziˈliʃ",
                      source="infopedia+wiktionary", pos="NOUN"),
        # the <ie> rule
        _upstream_row("paciente", "pt-PT-x-lisboa", "pɐsjẽtɨ", "pasjẽte", pos="NOUN"),
        # mojibake
        _upstream_row("alagem", "pt-MZ-x-maputo", "ɐlˈaʒẽçollins-nÃ£o-tem",
                      "alˈaʒẽçollins-nÃ£o-tem", pos="NOUN"),
        # left alone: the <ie> rule needs a Portal row, and this row is marked
        _upstream_row("paciente", "pt-PT", "pɐˈsjẽtɨ", "paˈsjẽte", source="infopedia"),
    ]
    decisions_used = [d for d in PT_UNIFIED_DECISIONS if d[0] == "busílis"]
    assert decisions_used
    import build_gold_corrections as builder
    saved = builder.PT_UNIFIED_DECISIONS, builder.PT_UNIFIED_BROAD_DECISIONS
    builder.PT_UNIFIED_DECISIONS, builder.PT_UNIFIED_BROAD_DECISIONS = tuple(decisions_used), ()
    try:
        out, stats = build_pt_unified_rows(rows)
    finally:
        builder.PT_UNIFIED_DECISIONS, builder.PT_UNIFIED_BROAD_DECISIONS = saved
    got = {(r["word"], r["region"], r["field"]): r["corrected_reading"] for r in out}
    assert got == {
        ("busílis", "pt-PT", "ipa_narrow"): "buˈziliʃ",
        ("busílis", "pt-PT", "ipa_broad"): "buˈziliʃ",
        ("paciente", "pt-PT-x-lisboa", "ipa_narrow"): "pɐsjˈẽtɨ",
        ("paciente", "pt-PT-x-lisboa", "ipa_broad"): "pasjˈẽte",
        ("alagem", "pt-MZ-x-maputo", "ipa_narrow"): None,
    }
    assert stats["rows_in"] == 4 and stats["overlay_rows"] == 5


def test_pt_build_refuses_a_decision_that_matches_nothing():
    with pytest.raises(ValueError, match="matches no upstream row"):
        build_pt_unified_rows([_upstream_row("outra", "pt-PT", "ˈotɾɐ")])


def test_pt_decisions_place_the_mark_on_a_vowel_the_letter_can_spell():
    """Every hand decision driven by a written accent stresses a vowel that
    letter spells, read from the corrected reading itself."""
    import unicodedata
    spells = {"á": "aɐ", "â": "ɐaə", "é": "ɛe", "ê": "eɛɐə", "í": "iɪ",
              "ó": "ɔo", "ô": "oɔ", "ú": "uʊ"}
    rows = list(PT_UNIFIED_DECISIONS) + list(PT_UNIFIED_BROAD_DECISIONS)
    for word, region, source, original, corrected, kind, basis in rows:
        if basis not in spells or corrected is None:
            continue
        for variant in corrected.split(","):
            nfd = unicodedata.normalize("NFD", variant)
            mark = max(nfd.find("ˈ"), nfd.find("'"))
            after = [c for c in nfd[mark + 1:] if c in "aɐeɛəɨioɔuʊɪ"]
            assert after and after[0] in spells[basis], (word, region, variant)


def test_pt_engine_never_enters_the_derivation():
    """The decision table, the <ie> rule and the broad derivation take
    spellings and readings only. The table is a literal: no entry is a call."""
    path = os.path.join(os.path.dirname(__file__), "..", "scripts",
                        "build_gold_corrections.py")
    with open(path, encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.AnnAssign) and getattr(node.target, "id", "") in (
                "PT_UNIFIED_DECISIONS", "PT_UNIFIED_BROAD_DECISIONS"):
            assert not [n for n in ast.walk(node.value) if isinstance(n, ast.Call)]
