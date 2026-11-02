# Lexicon-overlay scoreboard

Rules-only against with-lexicon PER for each language with a caller-registered lexicon. The package bundles no lexicon: see [`docs/guide/lexicon.md`](../../guide/lexicon.md) and `orthography2ipa/lexicon.py`. Each gold set is scored twice, once with `get_lexicon` stubbed to `{}` (rules-only) and once with the lexicon active. A lexicon must lower PER, and the rules-only column shows whether the grapheme rules still hold up without it. Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --lexicon-report
```

The `covered` columns score only the gold words that the lexicon holds, where the overlay can act. Their delta is the accuracy of the lexicon against the rules on the same words. The `full` columns score every gold word, so the words outside the capped, top-frequency pilot lexicon dilute the delta. A full production lexicon belongs downstream (see [`docs/guide/lexicon.md`](../../guide/lexicon.md)).

| Lexicon | Lang | Gold | Entries | N (full) | PER rules-only (full) | PER +lexicon (full) | N (covered) | PER rules-only (covered) | PER +lexicon (covered) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| en-GB | en | wikipron | 5000 | 2280 | 0.4416 | 0.4329 | 82 | 0.4165 | 0.1761 |
| en-GB | en-GB | wikipron | 5000 | 2378 | 0.4242 | 0.4156 | 80 | 0.3902 | 0.1344 |

---
[← espeak-ng agreement](espeak_agreement.md) · [Home](../../index.md) · [Spec diagnostics →](spec_diagnostics.md)
