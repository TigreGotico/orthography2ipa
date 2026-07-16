"""Regression gate for the Atlantic Iberian-creole TTS gold set
(docs/creoles-atlantic-tts-gold.md).

Runs the validate subcommand of scripts/creoles_atlantic_tts_gold.py over every
creole lect with a gold TSV (kea, pov, pre, aoa, cri; the rest report as
pending): schema, row minimum, o2i transcription regression, feature-tag
verifiability, in-lect duplicate detection and citation-id resolution. If a spec
change alters a gold transcription this fails, forcing a deliberate
reconciliation of the spec and the gold (cited accuracy wins).
"""
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "creoles_atlantic_tts_gold.py"


def test_creoles_atlantic_tts_gold_validates():
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "validate"],
        capture_output=True, text=True, timeout=600,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "all green" in proc.stdout
