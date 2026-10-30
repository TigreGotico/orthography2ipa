"""Tests for the gold-corrections overlay mechanism.

An overlay repairs a mechanically-derivable defect in an upstream gold without
touching the upstream file, and is registered as its own dataset so the
uncorrected row stays on the board beside the corrected one.

Two properties are load-bearing and are asserted here rather than trusted:

* the corrections are derivable from the ORTHOGRAPHY — every row of each
  overlay is re-derived from its own spelling and original reading and must
  reproduce the committed file;
* an overlay can never gate a promotion. A gold whose readings were rewritten
  by an automated process cannot certify the engine that is scored against it,
  so its dataset never gates, whatever tier its base gold carries.
"""
import ast
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import (  # noqa: E402
    CORRECTED_DATASETS,
    DATASETS,
    GOLD_CORRECTIONS,
    THIN_ROW_N,
    apply_gold_corrections,
    provenance_for,
    read_gold_corrections,
    row_gates,
)
from build_gold_corrections import (  # noqa: E402
    TONE_LETTERS,
    VI_HUYEN_READING,
    VI_NGANG_READING,
    build_pt_stress_rows,
    build_vi_tone_rows,
    pt_nuclei,
    pt_stress_from_end,
    vi_tone_from_spelling,
)

OVERLAY_FIELDS = {"dataset", "lang", "spelling", "original_reading",
                  "corrected_reading", "reason", "authority"}
#: The fields that make a row portable into a corrections dataset assembled
#: from several sources: the upstream file it was keyed on and the kind of
#: defect it repairs.
PORTABLE_FIELDS = OVERLAY_FIELDS | {"upstream_file", "kind"}


def _overlays():
    return [(d, lang) for d, langs in GOLD_CORRECTIONS.items() for lang in langs]


@pytest.mark.parametrize("dataset,lang", _overlays())
def test_overlay_rows_are_complete_and_actually_change_something(dataset, lang):
    rows = read_gold_corrections(dataset, lang)
    assert rows
    for row in rows:
        assert OVERLAY_FIELDS <= set(row) <= PORTABLE_FIELDS
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
    """An overlay row never gates, and it keeps its base gold's tier.

    A corrected gold is derived twice over — from a base gold and then from an
    automated correction pass — so it can diagnose, never certify. The tier
    stays the base's because that is where most of its readings came from;
    the dataset, not the tier, is what keeps the row from gating.
    """
    corrected = f"{dataset}_corrected"
    assert corrected in CORRECTED_DATASETS
    # Through provenance_for, not PROVENANCE: scoring resolves a row's tier
    # that way, including any PROVENANCE_BY_LANG entry.
    tier = provenance_for(corrected, lang)
    assert tier == provenance_for(dataset, lang)
    assert row_gates(tier, 10 * THIN_ROW_N, corrected) is False
    # the most trusted tier cannot make an overlay row gate either
    assert row_gates("expert-human", 10 * THIN_ROW_N, corrected) is False


def test_the_gating_check_can_fail():
    """The test above is only worth something if the same tier and sample
    DO gate on a dataset that is not an overlay."""
    assert row_gates(provenance_for("ipadict", "pt-BR"), 10 * THIN_ROW_N,
                     "ipadict") is True


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
            assert f"{dataset}_{lang.replace('-', '_')}.jsonl" in names


@pytest.mark.parametrize("dataset,lang", _overlays())
def test_overlay_file_is_deterministic_jsonl(dataset, lang):
    path = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa",
                        "data", "gold", "corrections",
                        f"{dataset}_{lang.replace('-', '_')}.jsonl")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    keys = [(json.loads(ln)["spelling"], json.loads(ln)["original_reading"])
            for ln in lines]
    assert keys == sorted(keys)
    for line in lines:
        assert line == json.dumps(json.loads(line), ensure_ascii=False,
                                  sort_keys=True)


# --- ipa-dict pt-BR: stress of hyphenated words ---------------------------

def test_pt_nuclei_read_diphthongs_and_hiatuses_from_spelling():
    """A falling diphthong is one nucleus, every other vowel pair a hiatus,
    and the u of qu/gu before a vowel is never a nucleus. Unaccented i/u
    before nh, or before an l m n r z closing the syllable, is a hiatus
    (Base X: rainha, ainda, juiz)."""
    assert pt_nuclei("muito") == ["ui", "o"]
    assert pt_nuclei("queijo") == ["ei", "o"]
    assert pt_nuclei("guerra") == ["e", "a"]
    assert pt_nuclei("saída") == ["a", "í", "a"]
    assert pt_nuclei("ainda") == ["a", "i", "a"]
    assert pt_nuclei("rainha") == ["a", "i", "a"]
    assert pt_nuclei("juiz") == ["u", "i"]
    assert pt_nuclei("coelho") == ["o", "e", "o"]
    assert pt_nuclei("irmão") == ["i", "ão"]


def test_pt_stress_read_from_spelling():
    """Counted from the end, 1 = last syllable. A written acute or
    circumflex marks the syllable; otherwise -a/-e/-o(s), -am, -em/-ens are
    paroxytone and the other endings oxytone."""
    assert pt_stress_from_end("acusa") == 2
    assert pt_stress_from_end("matando") == 2
    assert pt_stress_from_end("falam") == 2
    assert pt_stress_from_end("homens") == 2
    assert pt_stress_from_end("abandonou") == 1
    assert pt_stress_from_end("abandoná") == 1
    assert pt_stress_from_end("juiz") == 1
    assert pt_stress_from_end("irmão") == 1
    assert pt_stress_from_end("soviéticos") == 3
    assert pt_stress_from_end("pós") == 1
    # an ending the accent rules do not cover is not guessed
    assert pt_stress_from_end("iceberg") is None


#: Upstream ipa-dict pt_BR.txt rows. Each expected reading was worked out by
#: hand from the spelling, not from any engine output.
_PT_HAND_ROWS = [
    # acusa = a-cu-sa, paroxytone: stress on cu; the clitic o is one syllable
    ("acusa-o", "a.ku.ˈza.ʊ", "a.ˈku.za.ʊ", "enclitic"),
    # matando = ma-tan-do, paroxytone: stress on tan
    ("matando-os", "ma.tã.ˈdo.ʊs", "ma.ˈtã.do.ʊs", "enclitic"),
    # apresenta = a-pre-sen-ta, paroxytone: stress on sen
    ("apresenta-nos", "a.pɾe.zẽ.ˈtã.nʊs", "a.pɾe.ˈzẽ.tã.nʊs", "enclitic"),
    # last element brisas = bri-sas, paroxytone: stress on bri
    ("pára-brisas", "ˈpa.ɾa.bɾi.zəs", "pa.ɾa.ˈbɾi.zəs", "compound"),
    # last element ditadura = di-ta-du-ra, paroxytone: stress on du
    ("pós-ditadura", "ˈpɔʒ.dʒi.ta.du.ɾə", "pɔʒ.dʒi.ta.ˈdu.ɾə", "compound"),
    # soviéticos: the acute marks vi-É, third syllable from the end
    ("pró-soviéticos", "ˈpɾɔ.zo.vi.ɛ.tʃi.kʊs", "pɾɔ.zo.vi.ˈɛ.tʃi.kʊs",
     "compound"),
]


def test_pt_hand_rows_are_corrected_to_the_hand_computed_reading():
    rows, stats = build_pt_stress_rows(
        [(w, g) for w, g, _, _ in _PT_HAND_ROWS], "pt_BR.txt")
    got = {r["spelling"]: (r["corrected_reading"], r["kind"]) for r in rows}
    assert got == {w: (c, k) for w, _, c, k in _PT_HAND_ROWS}
    assert stats["corrected_enclitic"] == 3
    assert stats["corrected_compound"] == 3
    for row in rows:
        assert set(row) == PORTABLE_FIELDS
        assert row["dataset"] == "ipadict" and row["lang"] == "pt-BR"
        assert row["upstream_file"] == "pt_BR.txt"


def test_pt_rows_the_rule_cannot_reach_are_left_alone():
    """A misspelling, a correct gold, a row whose syllables do not match the
    spelling's nuclei, an empty element and a mesoclisis are all counted and
    none of them is corrected."""
    rows, stats = build_pt_stress_rows([
        ("ajuda-lo", "a.ʒu.ˈda.lʊ"),         # misspelt ajudá-lo
        ("abandoná-los", "a.bã.do.ˈna.lʊs"),  # gold already right
        ("estado-juiz", "es.ta.do.ˈʒuyz"),    # ju-iz is 2 nuclei, gold 1
        ("obras-", "o.ˈbɾas."),               # truncated upstream entry
        ("encontrar-se-ão", "ẽ.kõ.tɾax.si.ˈãʊ̃"),
        ("acusa", "a.ˈku.zə"),                # not hyphenated
    ], "pt_BR.txt")
    assert rows == []
    assert stats["misspelling"] == 1
    assert stats["already_correct"] == 1
    assert stats["nucleus_count_mismatch"] == 1
    assert stats["empty_element"] == 1
    assert stats["mesoclisis"] == 1
    assert sum(stats.values()) == 5


def test_pt_overlay_rederives_from_spelling_alone():
    committed = read_gold_corrections("ipadict", "pt-BR")
    rebuilt, stats = build_pt_stress_rows(
        [(r["spelling"], r["original_reading"]) for r in committed],
        "pt_BR.txt")
    assert stats["corrected_enclitic"] + stats["corrected_compound"] == len(
        committed)
    assert rebuilt == sorted(
        committed, key=lambda r: (r["spelling"], r["original_reading"]))


def test_pt_overlay_only_moves_the_stress_mark():
    for row in read_gold_corrections("ipadict", "pt-BR"):
        original, corrected = row["original_reading"], row["corrected_reading"]
        assert corrected.count("ˈ") == 1
        assert original.replace("ˈ", "") == corrected.replace("ˈ", "")
        assert "ˌ" not in corrected
        assert row["kind"] in ("enclitic", "compound")
