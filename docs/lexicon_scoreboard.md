# Lexicon-overlay scoreboard

Rules-only vs with-lexicon PER for every language that ships an optional sidecar lexicon (`orthography2ipa/data/lexicons/{code}.tsv` — see [`docs/data_model.md`](data_model.md) and [`orthography2ipa/lexicon.py`]). This keeps rule quality honest: the overlay must *improve* PER without letting the underlying grapheme rules rot behind lexicon coverage. Same gold, scored twice — once with `get_lexicon` stubbed to `{}` (rules-only) and once with the sidecar active. Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --lexicon-report
```

`PER (covered)` columns restrict scoring to the gold words the lexicon actually contains — where the overlay can act — so the covered-subset delta is the lexicon's own accuracy vs the rules on the *same* words. The `full` columns dilute that by every gold word outside the (deliberately capped, top-frequency) pilot lexicon; a full production lexicon belongs downstream (see [`docs/adding_a_language.md`](adding_a_language.md)).

| Lexicon | Lang | Gold | Entries | N (full) | PER rules-only (full) | PER +lexicon (full) | N (covered) | PER rules-only (covered) | PER +lexicon (covered) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| en-GB | en | wikipron | 5000 | 2280 | 0.4416 | 0.4329 | 82 | 0.4165 | 0.1761 |
| en-GB | en-GB | wikipron | 5000 | 2378 | 0.4242 | 0.4156 | 80 | 0.3902 | 0.1344 |
