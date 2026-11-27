"""The count tables of ``docs/evaluation/gold_defects.md`` match
``benchmarks/gold_defects.json``, which ``scripts/measure_gold_defects.py``
measures from the gold cache."""

import json
import os
import re

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load():
    with open(os.path.join(_ROOT, "benchmarks", "gold_defects.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    with open(os.path.join(_ROOT, "docs", "evaluation", "gold_defects.md"), encoding="utf-8") as fh:
        page = fh.read()
    return data, page


def _int(cell):
    return int(cell.strip().replace(",", ""))


def test_pt_tl_substitution_table():
    data, page = _load()
    rows = re.findall(r"^\| (\S+) to (\S+) \| ([\d,]+) \|$", page, re.M)
    want = [(s["lisboa"], s["dili"], s["count"]) for s in data["pt_tl"]["substitutions"]]
    assert [(a, b, _int(n)) for a, b, n in rows] == want


def test_pt_tl_prose_counts():
    data, page = _load()
    pt = data["pt_tl"]
    share = sum(s["count"] for s in pt["substitutions"]) / pt["character_differences"]
    assert (f"finds {pt['shared_words']:,} shared words, and {pt['identical_words']:,} "
            "of them are byte-identical") in page
    assert f"keeps the {pt['equal_length_words']:,} shared entries" in page
    assert (f"Six substitutions account for {100 * share:.1f}% of the "
            f"{pt['character_differences']:,} character differences") in page


def test_fa_diagnostic_table():
    data, page = _load()
    rows = re.findall(r"^\| ⟨(\S+)⟩ \| ([\d,]+) \| ⟨(\S+)⟩ \| ([\d,]+) \|$", page, re.M)
    assert len(rows) == 4
    for classical, n_classical, modern, n_modern in rows:
        assert data["fa"][classical] == _int(n_classical)
        assert data["fa"][modern] == _int(n_modern)
