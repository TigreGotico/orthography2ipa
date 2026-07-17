# espeak-ng agreement

Committed symbol-level agreement between orthography2ipa and espeak-ng, for every language where this repo has both a gold-dataset wordlist and espeak-ng has a voice. This is NOT an accuracy benchmark — see `docs/benchmarks.md` for what it means and does not mean. Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/espeak_agreement.py --scoreboard
```

Machine-readable form: [`benchmarks/espeak_agreement.json`](../benchmarks/espeak_agreement.json).

| Lang | espeak voice | N | Exact | Exact (no stress) | Segmental | OOV rate |
|---|---|---:|---:|---:|---:|---:|
| cy | cy | 300 | 0.0000 | 0.2700 | 0.7731 | 0.0267 |
| da | da | 300 | 0.0333 | 0.0533 | 0.5241 | 0.1667 |
| de | de | 300 | 0.0000 | 0.0067 | 0.6076 | 0.5133 |
| el | el | 300 | 0.0900 | 0.3567 | 0.8760 | 0.4667 |
| en | en-gb | 300 | 0.0000 | 0.0467 | 0.5394 | 0.8333 |
| en-GB | en-gb | 300 | 0.0000 | 0.0400 | 0.5319 | 0.8600 |
| en-US | en-us | 300 | 0.0000 | 0.0500 | 0.5738 | 0.2733 |
| eo | eo | 300 | 0.0300 | 0.7700 | 0.9690 | 0.0567 |
| es | es | 300 | 0.0600 | 0.6133 | 0.9313 | 0.0000 |
| eu | eu | 300 | 0.0000 | 0.3800 | 0.8465 | 0.2233 |
| fi | fi | 300 | 0.0000 | 0.0000 | 0.6218 | 1.0000 |
| fr | fr-fr | 300 | 0.0000 | 0.5100 | 0.8732 | 0.0000 |
| ga | ga | 300 | 0.0033 | 0.0067 | 0.4787 | 0.8867 |
| gd | gd | 300 | 0.0033 | 0.0033 | 0.5043 | 0.4067 |
| hi | hi | 300 | 0.0000 | 0.0000 | 0.5844 | 0.8633 |
| hr | hr | 300 | 0.0000 | 0.0533 | 0.6816 | 0.3667 |
| hy | hy | 300 | 0.0000 | 0.0000 | 0.5538 | 1.0000 |
| is | is | 300 | 0.0000 | 0.0033 | 0.6130 | 0.6000 |
| it | it | 300 | 0.0500 | 0.3633 | 0.8617 | 0.0000 |
| ml | ml | 300 | 0.0000 | 0.0000 | 0.5267 | 0.6267 |
| nb | nb | 300 | 0.0167 | 0.0233 | 0.5321 | 0.4933 |
| nl | nl | 300 | 0.0000 | 0.1433 | 0.6995 | 0.1467 |
| pl | pl | 300 | 0.1267 | 0.6833 | 0.9545 | 0.1333 |
| pt-AO | pt | 300 | 0.0000 | 0.0200 | 0.6053 | 0.3833 |
| pt-BR | pt-br | 300 | 0.0000 | 0.0233 | 0.6968 | 0.4100 |
| pt-MZ | pt | 535 | 0.0019 | 0.0206 | 0.6382 | 0.6280 |
| pt-PT | pt | 350 | 0.0029 | 0.1171 | 0.7557 | 0.2800 |
| pt-PT-x-acores | pt | 30 | 0.0000 | 0.0000 | 0.6774 | 0.3667 |
| pt-PT-x-alentejo | pt | 30 | 0.0000 | 0.0000 | 0.5837 | 0.3000 |
| pt-PT-x-algarve | pt | 30 | 0.0000 | 0.0000 | 0.6511 | 0.4667 |
| pt-PT-x-lisbon | pt | 45 | 0.0000 | 0.0000 | 0.6085 | 0.6222 |
| pt-PT-x-madeira | pt | 30 | 0.0000 | 0.0000 | 0.6714 | 0.4333 |
| pt-PT-x-porto | pt | 40 | 0.0000 | 0.0000 | 0.5310 | 0.5250 |
| pt-TL | pt | 300 | 0.0000 | 0.0000 | 0.5539 | 0.6200 |
| ro | ro | 300 | 0.0000 | 0.5000 | 0.8783 | 0.0667 |
| ru | ru | 300 | 0.0000 | 0.0067 | 0.5493 | 0.9167 |
| sk | sk | 300 | 0.1333 | 0.2733 | 0.8299 | 0.6633 |
| sq | sq | 300 | 0.0000 | 0.1167 | 0.6769 | 0.6067 |
| sv | sv | 300 | 0.0433 | 0.2100 | 0.7250 | 0.1367 |
| ta | ta | 300 | 0.0000 | 0.0433 | 0.6579 | 0.4733 |
| tr | tr | 300 | 0.0000 | 0.2033 | 0.8003 | 0.0000 |
