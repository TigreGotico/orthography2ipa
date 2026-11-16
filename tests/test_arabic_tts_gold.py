"""Source-file gate for the Arabic TTS gold set (docs/evaluation/silver_sets.md#arabic_tts).

Runs the validate subcommand of scripts/arabic_tts_gold.py over all 25 lects:
schema, row minimum, diacritization completeness, feature-tag verifiability
and duplicate detection.

The board scores the set against its llm-corrected file, which
tests/test_llm_corrected_sets.py checks. Nothing here pins engine output.
"""
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "arabic_tts_gold.py"


def test_arabic_tts_gold_validates():
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "validate"],
        capture_output=True, text=True, timeout=600,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "all green" in proc.stdout
