"""Regression gate for the Arabic TTS gold set (docs/arabic-tts-gold.md).

Runs the validate subcommand of scripts/arabic_tts_gold.py over all 25 lects:
schema, row minimum, diacritization completeness, o2i transcription
regression, feature-tag verifiability and duplicate detection. If a spec
change alters a gold transcription this fails, forcing a deliberate
reconciliation of the spec and the gold (cited accuracy wins).
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
