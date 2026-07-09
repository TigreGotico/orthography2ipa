# espeak-ng agreement

Committed symbol-level agreement between orthography2ipa and espeak-ng, for every language where this repo has both a gold-dataset wordlist and espeak-ng has a voice. This is NOT an accuracy benchmark — see `docs/benchmarks.md` for what it means and does not mean. Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/espeak_agreement.py --scoreboard
```

Machine-readable form: [`benchmarks/espeak_agreement.json`](../benchmarks/espeak_agreement.json).

| Lang | espeak voice | N | Exact | Exact (no stress) | Segmental | OOV rate |
|---|---|---:|---:|---:|---:|---:|
| cy | cy | 300 | 0.0000 | 0.2700 | 0.7721 | 0.0333 |
| da | da | 300 | 0.0000 | 0.0367 | 0.5062 | 0.2033 |
| de | de | 300 | 0.0000 | 0.0067 | 0.6076 | 0.5133 |
| el | el | 300 | 0.1067 | 0.5700 | 0.8992 | 0.0000 |
| en | en-gb | 300 | 0.0000 | 0.0367 | 0.5132 | 0.8333 |
| en-GB | en-gb | 300 | 0.0000 | 0.0300 | 0.4969 | 0.8600 |
| eo | eo | 300 | 0.0300 | 0.7700 | 0.9690 | 0.0567 |
| es | es | 300 | 0.0500 | 0.5533 | 0.9147 | 0.0000 |
| eu | eu | 300 | 0.0000 | 0.3833 | 0.8814 | 0.0933 |
| fi | fi | 300 | 0.0000 | 0.0000 | 0.6218 | 1.0000 |
| fr | fr-fr | 300 | 0.0000 | 0.4800 | 0.8646 | 0.0000 |
| ga | ga | 300 | 0.0000 | 0.0000 | 0.4147 | 0.9833 |
| gd | gd | 300 | 0.0067 | 0.0067 | 0.2857 | 0.6600 |
| hi | hi | 300 | 0.0000 | 0.0000 | 0.4990 | 0.8500 |
| hr | hr | 300 | 0.0000 | 0.0533 | 0.6816 | 0.3667 |
| hy | hy | 300 | 0.0000 | 0.0000 | 0.5538 | 1.0000 |
| is | is | 300 | 0.0000 | 0.0033 | 0.6130 | 0.6000 |
| it | it | 300 | 0.0433 | 0.3633 | 0.8626 | 0.0000 |
| ml | ml | 300 | 0.0000 | 0.0000 | 0.3519 | 0.6167 |
| nb | nb | 300 | 0.0000 | 0.0100 | 0.5212 | 0.5600 |
| nl | nl | 300 | 0.0000 | 0.1433 | 0.6995 | 0.1467 |
| pl | pl | 300 | 0.1100 | 0.4500 | 0.9028 | 0.1333 |
| pt | pt | 300 | 0.0000 | 0.1067 | 0.7119 | 0.0300 |
| pt-PT-x-acores | pt | 30 | 0.0000 | 0.0000 | 0.6157 | 0.3333 |
| pt-PT-x-alentejo | pt | 30 | 0.0000 | 0.0000 | 0.5985 | 0.0333 |
| pt-PT-x-algarve | pt | 30 | 0.0000 | 0.0000 | 0.6726 | 0.1000 |
| pt-PT-x-lisbon | pt | 45 | 0.0000 | 0.0000 | 0.6026 | 0.4444 |
| pt-PT-x-madeira | pt | 30 | 0.0000 | 0.0000 | 0.6799 | 0.0000 |
| pt-PT-x-porto | pt | 40 | 0.0000 | 0.0000 | 0.5446 | 0.2750 |
| ro | ro | 300 | 0.0000 | 0.5167 | 0.8805 | 0.0600 |
| ru | ru | 300 | 0.0000 | 0.1033 | 0.6954 | 0.5133 |
| sk | sk | 300 | 0.1333 | 0.2733 | 0.8299 | 0.6633 |
| sq | sq | 300 | 0.0000 | 0.1167 | 0.6769 | 0.6067 |
| sv | sv | 300 | 0.0000 | 0.0667 | 0.6242 | 0.1333 |
| ta | ta | 300 | 0.0000 | 0.0033 | 0.4692 | 0.5233 |
| tr | tr | 300 | 0.0067 | 0.2033 | 0.8003 | 0.0000 |
