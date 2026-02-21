# Examples

This folder contains runnable demonstration scripts for the `orthography2ipa` package.

---

## Scripts

### `01_basic_usage.py`
**Basic usage** — loading language specs, exploring grapheme→IPA mappings, allophone inventories, inventory sizes, and available language families.

```bash
python examples/01_basic_usage.py
```

### `02_tokenizer.py`
**Tokenizer** — using `PhonetokTokenizer` to segment text by grapheme, generate IPA transcription paths via beam search, handle mixed content (digits, punctuation, unknowns), and expand allophones.

```bash
python examples/02_tokenizer.py
```

### `03_distance_metrics.py`
**Distance metrics** — segment-level feature vectors and distances, inventory distance, grapheme divergence, allophone overlap, combined phonological distance, pairwise distance matrices, and ancestry similarity.

```bash
python examples/03_distance_metrics.py
```

### `04_dialect_comparison.py`
**Dialect comparison** — comparing phonological properties across dialect families (Spanish varieties, Portuguese varieties, Catalan dialects, Basque dialects), with distance tables and per-grapheme comparisons.

```bash
python examples/04_dialect_comparison.py
```

### `05_ancestry_and_history.py`
**Ancestry and history** — tracing language lineages through the ancestry system, exploring pre-Roman Iberian substrate languages, Barranquenho as a contact language, and historical time depth via phonological distance from Latin.

```bash
python examples/05_ancestry_and_history.py
```

### `06_advanced_nlp.py`
**Advanced NLP integration** — building phonemic transcription pipelines, tracking cognates across Romance languages, finding closest languages, analyzing phoneme inventories, building pronunciation dictionaries, and cross-lingual phoneme correspondence.

```bash
python examples/06_advanced_nlp.py
```

---

## Running All Examples

```bash
for f in examples/0*.py; do
    echo "==============================="
    echo "Running: $f"
    echo "==============================="
    python "$f"
    echo
done
```

---

## Expected Output Notes

- Some outputs involve distance calculations that run the full feature-vector comparison; allow a few seconds for large pairwise matrices.
- A few codes may be absent from distance tables if their modules are not yet installed — those rows are silently skipped.
- IPA characters are printed as-is and require a UTF-8 capable terminal.
