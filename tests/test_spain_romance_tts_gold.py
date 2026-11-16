"""Source-file gate for the Spain-Romance TTS gold set (docs/evaluation/silver_sets.md#spain_romance_tts).

Runs the validate subcommand of scripts/spain_romance_tts_gold.py over every
Spain-Romance lect that has a gold TSV (the rest report as pending): schema,
row minimum, feature-tag verifiability, duplicate detection and citation-id
resolution.

The board scores the set against its llm-corrected file, which
tests/test_llm_corrected_sets.py checks. Nothing here pins engine output.
"""
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "spain_romance_tts_gold.py"


def test_spain_romance_tts_gold_validates():
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "validate"],
        capture_output=True, text=True, timeout=600,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "all green" in proc.stdout
