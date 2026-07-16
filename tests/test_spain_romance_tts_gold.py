"""Regression gate for the Spain-Romance TTS gold set (docs/spain-romance-tts-gold.md).

Runs the validate subcommand of scripts/spain_romance_tts_gold.py over every
Spain-Romance lect that has a gold TSV (the rest report as pending): schema,
row minimum, o2i transcription regression, feature-tag verifiability, duplicate
detection and citation-id resolution. If a spec change alters a gold
transcription this fails, forcing a deliberate reconciliation of the spec and
the gold (cited accuracy wins).
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
