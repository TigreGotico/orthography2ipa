# Examples

Runnable scripts, ordered from first transcription to building on the engine.
Each is self-contained and prints what it demonstrates:

```bash
pip install orthography2ipa
python examples/01_basic_usage.py
```

| Script | Shows |
|---|---|
| [`01_basic_usage.py`](01_basic_usage.py) | Load a spec, read grapheme→IPA and allophone maps, list languages |
| [`02_distance_metrics.py`](02_distance_metrics.py) | Phonological / spelling / ancestry distance between languages |
| [`03_tokenizer.py`](03_tokenizer.py) | Grapheme tokenization and IPA beam search |
| [`04_dialect_transforms.py`](04_dialect_transforms.py) | Dialect-specific IPA transforms (Portuguese varieties) |
| [`05_script_distance.py`](05_script_distance.py) | Typological distance between writing systems |
| [`06_sandhi.py`](06_sandhi.py) | Cross-word-boundary rules (sandhi / liaison) |
| [`07_lattice_and_rescorer.py`](07_lattice_and_rescorer.py) | The ranked lattice, per-word confidence, and refining it with a `LatticeRescorer` |
| [`08_lexicon_overlay.py`](08_lexicon_overlay.py) | Overlaying an external `word→ipa` lexicon by path / URL / `hf://` id |

New to the library? Read [`docs/getting_started.md`](../docs/getting_started.md)
first, then work down this list. Building a specialised phonemizer on top of the
engine? Start at `07` and see [`docs/lattice.md`](../docs/lattice.md).
