"""Source-file gate for the unified Iberian-creole TTS gold set
(docs/evaluation/silver_sets.md#iberian_creole_tts).

Runs the validate subcommand of scripts/iberian_creole_tts_gold.py over every
Iberian-lexified creole lect that has a gold TSV — the whole roster across the
three shelves (Asian Portuguese mcm/idb/vkp, Atlantic kea/pov/pre/aoa/cri,
Spanish-lexified Caribbean/Philippine pap/cbk-zam/pln); the rest report as
pending. Checks schema, row minimum, feature-tag verifiability, duplicate
detection and citation-id resolution.

The board scores the set against its llm-corrected file, which
tests/test_llm_corrected_sets.py checks. Nothing here pins engine output.
"""
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "iberian_creole_tts_gold.py"


def test_iberian_creole_tts_gold_validates():
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "validate"],
        capture_output=True, text=True, timeout=600,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "all green" in proc.stdout
