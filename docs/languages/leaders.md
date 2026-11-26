# Leader languages

<!-- agent-hint
covers: the board row of each leader language tag
source: `benchmarks/results.json`, `orthography2ipa/data/*.json`
generated: yes, by `scripts/gen_leaders_doc.py`
verify: `python3 scripts/gen_leaders_doc.py --check`
see: `docs/benchmarks.md`, `docs/languages/a-z.md`
-->

The table gives one board row for each leader language tag. The resolved spec is the code that `orthography2ipa.get(tag)` returns. A tag with no spec file of its own resolves to a broader spec, and the table names that spec. The scoreboard has no rule that marks one row as the primary row of a language. The best gold row is the gating row on the most trusted provenance tier, in the order expert-human, lexicon-derived, crowd-scraped, machine-generated, and then the row with the largest N. Only rows with N of at least 1000 count, unless no row reaches 1000. A tag with no gating row shows its best other row by the same rule, marked "does not gate". A tag with no row shows "not measured".

| Tag | Resolved spec | Spec tier | Best gold dataset | N | PER | 95% CI | Provenance tier | Page |
| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- |
| `pt-PT` | `pt-PT` | research | `portuguese_unified` | 105553 | 0.1866 | 0.1857–0.1875 | lexicon-derived | [pt-PT.md](pt-PT.md) |
| `pt-BR` | `pt-BR` | production | `portuguese_unified` | 23123 | 0.1421 | 0.1400–0.1440 | lexicon-derived | [pt-BR.md](pt-BR.md) |
| `es-CO` | `es-CO` | skeleton | `spain_romance_tts` | 20 | 0.0120 | 0.0043–0.0210 | llm-corrected (does not gate) | [`es-CO` in the data explorer](https://tigregotico.github.io/orthography2ipa/#es-CO) |
| `fr-FR` | `fr-FR` | research | `ipadict` | 245718 | 0.0753 | 0.0748–0.0758 | machine-generated | [fr-FR.md](fr-FR.md) |
| `it-IT` | `it-IT` | research | `ipa_childes` | 4583 | 0.2353 | 0.2299–0.2407 | espeak-derived (does not gate) | [it-IT.md](it-IT.md) |
| `de-DE` | `de-DE` | research | `ipadict` | 777785 | 0.2303 | 0.2300–0.2307 | crowd-scraped | [de-DE.md](de-DE.md) |
| `nl-NL` | `nl-NL` | research | `wikipron` | 45872 | 0.1803 | 0.1790–0.1817 | crowd-scraped | [nl-NL.md](nl-NL.md) |
| `da-DK` | `da` (no `da-DK` spec) | research | `wikipron` | 4331 | 0.3455 | 0.3386–0.3523 | crowd-scraped | [da.md](da.md) |
| `kab` | `kab` | research | `vox_communis` | 54545 | 0.2071 | 0.2057–0.2083 | epitran-derived (does not gate) | [kab.md](kab.md) |
| `hi-IN` | `hi` (no `hi-IN` spec) | research | `wikipron` | 30376 | 0.1252 | 0.1240–0.1263 | crowd-scraped | [hi.md](hi.md) |
| `bn-IN` | `bn` (no `bn-IN` spec) | research | `wikipron` | 6527 | 0.2398 | 0.2349–0.2448 | crowd-scraped | [bn.md](bn.md) |
| `mwr` | unsupported: resolves to the `dhd` stub (a member of the mwr macrolanguage), no phonology | stub | not measured |  |  |  |  | [`dhd` in the data explorer](https://tigregotico.github.io/orthography2ipa/#dhd) |

---
[← Zulu](zu.md) · [Home](../index.md) · [Comparative phonology →](comparative.md)
