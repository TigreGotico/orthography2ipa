# Leader languages

<!-- agent-hint
covers: the board row of each leader language tag
source: `benchmarks/results.json`, `orthography2ipa/data/*.json`
generated: yes, by `scripts/gen_leaders_doc.py`
verify: `python3 scripts/gen_leaders_doc.py --check`
see: `docs/benchmarks.md`, `docs/languages/a-z.md`
-->

The table gives one board row for each leader language tag. The resolved spec is the code that `orthography2ipa.get(tag)` returns. A tag with no spec file of its own resolves to a broader spec, and the table names that spec. The scoreboard has no rule that marks one row as the primary row of a language, so the best gold row is the gating row with the largest N.

| Tag | Resolved spec | Spec tier | Best gold dataset | N | PER | 95% CI | Provenance tier | Page |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- |
| `pt-PT` | `pt-PT` | research | `portuguese_unified` | 105553 | 0.1866 | 0.1857–0.1875 | lexicon-derived | [pt-PT.md](pt-PT.md) |
| `pt-BR` | `pt-BR` | production | `ipadict` | 95933 | 0.2313 | 0.2303–0.2323 | machine-generated | [pt-BR.md](pt-BR.md) |
| `es-CO` | `es-CO` | skeleton | no gating row |  |  |  |  | [`es-CO` in the data explorer](https://tigregotico.github.io/orthography2ipa/#es-CO) |
| `fr-FR` | `fr-FR` | research | `ipadict` | 245718 | 0.0753 | 0.0748–0.0758 | machine-generated | [fr-FR.md](fr-FR.md) |
| `it-IT` | `it-IT` | research | no gating row |  |  |  |  | [it-IT.md](it-IT.md) |
| `de-DE` | `de-DE` | research | `ipadict` | 777785 | 0.2303 | 0.2300–0.2307 | crowd-scraped | [de-DE.md](de-DE.md) |
| `nl-NL` | `nl-NL` | research | `ipadict` | 117869 | 0.2627 | 0.2618–0.2635 | machine-generated | [nl-NL.md](nl-NL.md) |
| `da-DK` | `da` (no `da-DK` spec) | research | `wikipron` | 4331 | 0.3455 | 0.3386–0.3523 | crowd-scraped | [da.md](da.md) |
| `kab` | `kab` | research | no gating row |  |  |  |  | [kab.md](kab.md) |
| `hi-IN` | `hi` (no `hi-IN` spec) | research | `wikipron` | 30376 | 0.1252 | 0.1240–0.1263 | crowd-scraped | [hi.md](hi.md) |
| `bn-IN` | `bn` (no `bn-IN` spec) | research | `wikipron` | 6527 | 0.2398 | 0.2349–0.2448 | crowd-scraped | [bn.md](bn.md) |
| `mwr` | `dhd` (no `mwr` spec) | stub | no gating row |  |  |  |  | [`dhd` in the data explorer](https://tigregotico.github.io/orthography2ipa/#dhd) |

---
[← Zulu](zu.md) · [Home](../index.md) · [Comparative phonology →](comparative.md)
