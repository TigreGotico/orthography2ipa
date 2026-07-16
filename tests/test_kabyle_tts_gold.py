"""Regression gate for the Kabyle TTS gold set (docs/kabyle-tts-gold.md).

Runs the validate subcommand of scripts/kabyle_tts_gold.py over every Kabyle
lect that has a gold TSV (the rest report as pending): schema, row minimum, o2i
transcription regression, feature-tag verifiability, duplicate detection and
citation-id resolution against the lect's spec sources. If a spec change alters
a gold transcription this fails, forcing a deliberate reconciliation of the
spec and the gold (cited accuracy wins — the IPA column is never hand-edited).
"""
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "kabyle_tts_gold.py"


def test_kabyle_tts_gold_validates():
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "validate"],
        capture_output=True, text=True, timeout=600,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "all green" in proc.stdout
