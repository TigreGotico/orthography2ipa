"""The loom parity table of docs/guide/loom_export.md states benchmarks/loom_parity.json."""
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def test_the_parity_table_matches_the_result_file():
    result = json.loads((REPO / "benchmarks" / "loom_parity.json").read_text(encoding="utf-8"))
    page = (REPO / "docs" / "guide" / "loom_export.md").read_text(encoding="utf-8")
    vectors = result["vectors"]
    gold = result["gold"]
    assert (f"| Conformance vectors | {vectors['files']} files | {vectors['cases']} | {vectors['identical']} |"
            in page)
    assert f"| Gold sentences | {gold['lects']} lects | {gold['sentences']} | {gold['identical']} |" in page
    assert re.search(rf"loom\.cpp commit `{result['loom_commit']}` and orthography2ipa {re.escape(result['orthography2ipa'])}\.",
                     page)
