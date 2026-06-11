# Benchmarks

How the G2P engine is evaluated: which gold pronunciation datasets are
used, where they come from, and the reference numbers the bundled
harness produces. Run any row yourself with
[`scripts/benchmark.py`](../scripts/benchmark.py):

```bash
python scripts/benchmark.py --dataset portuguese_lexicon --lang pt-PT
python scripts/benchmark.py --dataset wikipron --lang fi
python scripts/benchmark.py --list
```

## Provenance discipline

A gold set is only usable for evaluation when its transcriptions come
from humans. Many public "G2P datasets" are generated with espeak-ng or
phonemizer wrappers — scoring against those measures agreement with
another rule engine, not correctness. Every dataset below is selected
for human or community provenance; anything tool-generated is excluded
on principle.

## Datasets

### Portal da Língua Portuguesa lexicon

Per-region IPA for ~617k Portuguese entries, scraped from the
INESC-ID [Portal da Língua Portuguesa](https://www.portaldalinguaportuguesa.org/)
and published as
[TigreGotico/portuguese_phonetic_lexicon](https://huggingface.co/datasets/TigreGotico/portuguese_phonetic_lexicon)
on Hugging Face. The harness loads it through
[tugalex](https://github.com/TigreGotico/tugalex), the lexicon library
that wraps this dataset; one region maps to each language tag (Lisbon →
`pt-PT`, Rio de Janeiro → `pt-BR`, Luanda → `pt-AO`, Maputo → `pt-MZ`,
Díli → `pt-TL`). Lexicographer-curated; the strongest gold available
for Portuguese and the only one with regional coverage.

### WikiPron

Word/IPA pairs mined from Wiktionary by
[CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)
(Lee et al. 2020, *WikiPron: Mining Wiktionary for Massively
Multilingual Pronunciation Data*, LREC). Community-curated by Wiktionary
editors — reliable where the editor community is large; the broad-
transcription TSVs are used. Note the gold carries **multiple valid
transcriptions per word** (dialect variants such as Galician
seseo/gheada); the harness scores against all of them and keeps the
best match.

Previously wired: `gl`, `es`, `pt`, `pt-BR`, `en`, `en-GB`.

New languages added in this survey — all from `data/scrape/tsv/` on the
[CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron) GitHub
repository, same CC-BY-SA provenance:

| o2ipa tag | WikiPron file | ~rows | Notes |
|---|---|---:|---|
| `it` | `ita_latn_broad.tsv` | 89 608 | Italian; large it.wiktionary community |
| `fr` | `fra_latn_broad.tsv` | 97 652 | French; large fr.wiktionary community |
| `de` | `deu_latn_broad.tsv` | 60 277 | German |
| `nl` | `nld_latn_broad.tsv` | 58 539 | Dutch |
| `pl` | `pol_latn_broad.tsv` | 157 042 | Polish |
| `fi` | `fin_latn_broad.tsv` | 173 449 | Finnish |
| `ro` | `ron_latn_broad.tsv` | 9 286 | Romanian |
| `ast` | `ast_latn_broad.tsv` | 4 192 | Asturian |
| `oc` | `oci_latn_broad.tsv` | 748 | Occitan |
| `sv` | `swe_latn_broad.tsv` | 5 856 | Swedish |
| `da` | `dan_latn_broad.tsv` | 4 773 | Danish |
| `nb` | `nob_latn_broad.tsv` | 3 432 | Norwegian Bokmål |
| `is` | `isl_latn_broad.tsv` | 10 719 | Icelandic (Wiktionary-grade) |
| `cy` | `cym_latn_nw_broad.tsv` | 17 213 | Welsh (NW dialect) |
| `ga` | `gle_latn_broad.tsv` | 21 164 | Irish |
| `gd` | `gla_latn_broad.tsv` | 6 000 | Scottish Gaelic |
| `el` | `ell_grek_broad.tsv` | 19 601 | Modern Greek |
| `hy` | `hye_armn_e_broad.tsv` | 18 011 | Eastern Armenian |
| `sk` | `slk_latn_broad.tsv` | 15 950 | Slovak |
| `hr` | `hbs_latn_broad.tsv` | 26 163 | Croatian (hbs macro-language, Latin script) |
| `sq` | `sqi_latn_broad.tsv` | 5 376 | Albanian |
| `tr` | `tur_latn_broad.tsv` | 12 321 | Turkish |
| `eu` | `eus_latn_broad.tsv` | 20 115 | Basque |
| `tl` | `tgl_latn_broad.tsv` | 28 295 | Tagalog |
| `eo` | `epo_latn_broad.tsv` | 41 287 | Esperanto |
| `hi` | `hin_deva_broad.tsv` | 33 057 | Hindi (Devanagari) |
| `ta` | `tam_taml_broad.tsv` | 10 492 | Tamil (Tamil script) |
| `ml` | `mal_mlym_broad.tsv` | 10 406 | Malayalam (Malayalam script) |

### CMU Pronouncing Dictionary

[cmudict](https://github.com/cmusphinx/cmudict): ~134k American English
entries hand-curated by the CMU Speech Group. ARPABET, converted to IPA
via [scriptconv](https://github.com/TigreGotico/scriptconv). English
orthography is deeply irregular, so this row is a floor for a
rule-driven engine, reported for honesty rather than flattery.

### Mirandese gold set

[TigreGotico/mirandese_g2p](https://huggingface.co/datasets/TigreGotico/mirandese_g2p)
on Hugging Face: ~220 word/IPA rows with a dialect column (central,
raiano, sendinese), collected by a native Mirandese speaker
([MdMV](https://commons.wikimedia.org/wiki/User:MdMV_or_Emdy_idk)).
Native-speaker provenance makes it the reference gold for Mirandese;
its size keeps results indicative rather than statistical.

### Icelandic Pronunciation Dictionary (ipa-dict)

[open-dict-data/ipa-dict `is.txt`](https://github.com/open-dict-data/ipa-dict/blob/master/data/is.txt):
~60k Icelandic entries sourced from the
[Hjal project / Pronunciation Dictionary for Icelandic](http://malfong.is/?pg=framburdur&lang=en)
(malfong.is), released under **CC BY 3.0**. The ipa-dict README states:
"Icelandic IPA is from the Pronunciation Dictionary for Icelandic by
the Hjal project, released under CC BY 3.0, with some changes." The
Hjal project is an Icelandic NLP initiative; the source dictionary is
human-curated by Icelandic linguists. This provides higher coverage
than the WikiPron `isl_latn_broad.tsv` (~11k rows) and uses the
`word TAB /IPA/` format with slashes stripped by the loader. Use as
the primary Icelandic gold (`ipadict is`); the WikiPron Icelandic row
is wired as a secondary cross-check.

## Rejected candidates

Datasets investigated and excluded due to tool-generated or unclear
provenance:

| Dataset | Verdict | Evidence |
|---|---|---|
| **ipa-dict `fi.txt`** | CIRCULAR | README: "prosodic1b by @jsfalk for Finnish IPA data" — prosodic1b is a rule-based syllabification and stress tool, not human IPA annotation. |
| **ipa-dict `es_ES.txt` / `es_MX.txt`** | CIRCULAR | README: "generated using Timur Baytukalov's spanish-pronunciation-rules PHP script. Experimental." |
| **ipa-dict `ar.txt`** | CIRCULAR | README: "generated by Tim Buckwalter's Arabic Morphological Analyzer with adjustments." |
| **ipa-dict `fa.txt`** | CIRCULAR | README: "pieced together from Wiktionary, PersPred, and a great deal of **guesswork**. Should be considered extremely experimental." |
| **ipa-dict `fr_QC.txt`** | CIRCULAR | README: "generated using the qc-ipa converter and is _highly experimental_." |
| **ipa-dict `vi_*.txt`** | CIRCULAR | README: "generated by @TasseDeCafe using vPhon." |
| **ipa-dict `nb.txt`** | USE-WITH-CARE | README credits Dr. Espen Stranger-Johannessen for "correcting and updating" but the generation method for the base data is not documented. WikiPron `nob` used instead. |
| **ipa-dict `nl.txt`** | USE-WITH-CARE | README: "automated conversion from different data sources and no manual correction or revision has been done on the entire set" (INT/CC BY). WikiPron `nld` preferred (Wiktionary community). |
| **Lexique 3.82 (French)** | EXCLUDED — complex notation | Data is human-curated (Boris New / Christophe Pallier, CNRS) and CC BY-SA 4.0, but uses a custom phonemic notation (not X-SAMPA, not IPA) — `§`=ɔ̃, `°`=schwa-variant, `5`=ɛ̃, `8`=œ̃ etc. — not covered by `scriptconv.notation.xsampa_to_ipa`. A dedicated Lexique converter would be a clean follow-up; WikiPron `fra` is used in the interim. |
| **NST Swedish/Norwegian lexicons (Språkbanken/NB)** | EXCLUDED — no programmatic download | Authoritative SAMPA lexicons for sv/nb/da from Nasjonalbiblioteket. Human-curated. However no stable raw-download URL suitable for `urllib.request`; the portal serves interactive/catalogue pages. WikiPron Scandinavian TSVs used instead. |
| **CELEX2 (de/nl/en)** | EXCLUDED — proprietary | LDC license (LDC96L14), not freely downloadable. |
| **GlobalPhone** | EXCLUDED — ELRA license | Per-language ELRA licenses; not freely downloadable. |

## Methodology

- **PER** — character-level Levenshtein distance over IPA, divided by
  reference length; mean over evaluated words. **WER** — fraction of
  words with any error.
- **Multi-reference**: rows are grouped by word and a hypothesis is
  scored against every gold variant, keeping the minimum PER.
- **Segmentation-free**: whitespace is removed before comparison (some
  gold sets space-separate phonemes).
- **Default normalization**: stress marks and narrow-transcription
  apparatus (raising/dentality diacritics, syllable separators, tie
  bars) are stripped from both sides — gold sets differ in
  transcription depth, and the engine should not be scored on notation
  conventions. `--keep-stress` / `--narrow` disable this.
- Runs are capped at 300 words by default — gold sets are alphabetical,
  so treat single-slice numbers as reference points, not leaderboard
  entries.

## Reference numbers

`python scripts/benchmark.py --dataset <d> --lang <l> --limit 300`:

| Dataset | Lang | N | PER | WER |
|---|---|---:|---:|---:|
| wikipron | eo | 300 | 0.030 | 0.13 |
| wikipron | fi | 294 | 0.039 | 0.25 |
| wikipron | ro | 281 | 0.060 | 0.36 |
| wikipron | gl | 264 | 0.073 | 0.37 |
| wikipron | eu | 240 | 0.077 | 0.41 |
| wikipron | ast | 300 | 0.088 | 0.41 |
| wikipron | sq | 249 | 0.092 | 0.31 |
| wikipron | es | 298 | 0.100 | 0.52 |
| wikipron | it | 276 | 0.101 | 0.51 |
| wikipron | pl | 287 | 0.120 | 0.64 |
| wikipron | sk | 300 | 0.121 | 0.53 |
| wikipron | tr | 296 | 0.138 | 0.60 |
| wikipron | el | 298 | 0.152 | 0.69 |
| wikipron | oc | 266 | 0.160 | 0.63 |
| wikipron | pt | 243 | 0.190 | 0.71 |
| wikipron | cy | 271 | 0.217 | 0.70 |
| ipadict | is | 300 | 0.230 | 0.91 |
| mirandese | mwl | 205 | 0.230 | 0.76 |
| wikipron | is | 258 | 0.223 | 0.86 |
| wikipron | hr | 292 | 0.276 | 0.98 |
| wikipron | tl | 269 | 0.231 | 0.96 |
| portuguese_lexicon | pt-PT | 300 | 0.167 | 0.73 |
| portuguese_lexicon | pt-MZ | 300 | 0.288 | 0.86 |
| portuguese_lexicon | pt-BR | 300 | 0.420 | 1.00 |
| portuguese_lexicon | pt-AO | 300 | 0.398 | 1.00 |
| portuguese_lexicon | pt-TL | 300 | 0.487 | 1.00 |
| wikipron | nl | 260 | 0.314 | 0.83 |
| wikipron | fr | 279 | 0.318 | 0.81 |
| wikipron | sv | 279 | 0.351 | 0.94 |
| wikipron | de | 269 | 0.366 | 0.97 |
| wikipron | hy | 297 | 0.070 | 0.38 |
| wikipron | ga | 134 | 0.433 | 0.96 |
| wikipron | da | 273 | 0.442 | 0.95 |
| wikipron | hi | 262 | 0.457 | 0.99 |
| mirandese | mwl-x-sendim | 11 | 0.553 | 0.82 |
| wikipron | nb | 226 | 0.513 | 0.98 |
| cmudict | en-US | 300 | 0.612 | 0.98 |
| wikipron | gd | 210 | 0.687 | 0.97 |
| wikipron | ml | 281 | 0.672 | 1.00 |
| wikipron | ta | 293 | 0.895 | 1.00 |
| wikipron | pt-BR | 125 | 0.328 | 0.99 |

Reading the table: rule-complete languages with positional grapheme
blocks score best (eo, fi, ro, gl, eu, ast, sq, it). High PER for nb,
da, sv, de reflects irregular stress/vowel-reduction patterns not yet
encoded in those specs. The hi/ta/ml rows expose the current gap for
Indic scripts — G2P rules for those languages are present but not
fully calibrated to the Wiktionary transcription style. The da/nb/sv
rows are an engine-spec gap, not a dataset problem.
