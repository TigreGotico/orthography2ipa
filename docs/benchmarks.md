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
on principle. One dataset-specific exception is documented below
(`hitz_basque_ipa`) for an academic/university NLP research center
publication — see that section for the rationale; it is not a general
relaxation of this rule.

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
| `ru` | `rus_cyrl_narrow.tsv` | ~large | Russian (Cyrillic). **Narrow, not broad** — see note below. |

Russian has no `_broad.tsv` in `data/scrape/tsv/`; upstream's own README
states some languages were only scraped in one transcription width
("some languages only have broad or narrow transcriptions, e.g. Russian
only has the latter"), and for Russian that is narrow. The harness's
default (non-`--narrow`) normalization already strips narrow-transcription
diacritics (`_NARROW_MARKS`) before scoring, so `rus_cyrl_narrow.tsv` is
directly comparable to the broad-tier gold used for the other languages
in this table; it was not previously wired for lack of a broad file, not
for any documented quality concern.

### European Portuguese IPA Lexicon (Infopédia)

[TigreGotico/infopedia-pt-ipa](https://huggingface.co/datasets/TigreGotico/infopedia-pt-ipa)
on Hugging Face: 102,685 word/IPA rows extracted from
[Infopédia](https://www.infopedia.pt/) (Porto Editora) via a graph crawl
of the dictionary that ran to convergence. License: `other` /
`infopedia-derived` — see the
[dataset card](https://huggingface.co/datasets/TigreGotico/infopedia-pt-ipa)
for terms. Covers European Portuguese (unmarked `pt` in the dataset
tags, `pt-PT` here for consistency with `portuguese_lexicon` and
`wikipron`). 62 entries carry more than one distinct pronunciation
(`pronunciations` field); the harness scores against all variants and
keeps the best match, per the standard multi-reference handling. No
rows are excluded.

### CMU Pronouncing Dictionary

[cmudict](https://github.com/cmusphinx/cmudict): ~134k American English
entries hand-curated by the CMU Speech Group. ARPABET, converted to IPA
via [scriptconv](https://github.com/TigreGotico/scriptconv). English
orthography is deeply irregular, so this row is a floor for a
rule-driven engine, reported for honesty rather than flattery.

### European Portuguese regional dialect gold set (`ep_dialects`)

250 sentence-level rows across seven EP regional varieties, manually
annotated with dialectal IPA.  Source: **TigreGotico internal dialect
research** — DIALECT\_PATTERNS.md feature matrix cross-checked against
whitepaper5 (*Phoneme-Level Dialect Transforms for European Portuguese*,
Miro 2026).  Provenance: sentence-level gold produced by the same team
that maintains the dialect specs; pending external peer validation.

The CSV lives at `tests/data/ep_dialect_sentences.csv`.  The benchmark
harness maps the seven CSV dialect codes to orthography2ipa language tags:

| CSV dialect\_code | orthography2ipa tag | Notes |
|---|---|---|
| `pt-PT-x-lisboa` | `pt-PT-x-lisbon` | Lisbon prestige |
| `pt-PT-x-north` | `pt-PT-x-porto` | Porto / Baixo-Minho representative |
| `pt-PT-x-central` | `pt-PT` | Coimbra-type conservative standard |
| `pt-PT-x-alentejo` | `pt-PT-x-alentejo` | |
| `pt-PT-x-algarve` | `pt-PT-x-algarve` | |
| `pt-PT-x-madeira` | `pt-PT-x-madeira` | |
| `pt-PT-x-azores` | `pt-PT-x-acores` | |

Because the gold contains sentence-level phonetics (connected-speech
reductions, liaison, stress-conditioned elisions), PER is naturally
higher than the lexicon benchmarks; it measures how well the engine
captures dialect-specific grapheme-to-phoneme rules, not connected-speech
phonology.

### CLUP dialect archive gold set (`clup_dialect`)

[TigreGotico/ArquivoDialetalCLUP_ipa](https://huggingface.co/datasets/TigreGotico/ArquivoDialetalCLUP_ipa)
on Hugging Face: 68 sentence-level rows (66 mapped, see below), IPA
transcriptions of interview excerpts from the
[Arquivo Dialetal](https://cl.up.pt/arquivo/) of the Centro de
Linguística da Universidade do Porto (CLUP). Each row carries a
`"<locality>, <district>"` region label; rows are grouped to an
orthography2ipa dialect tag by locality (exact match) then by district:

| District (or locality) | orthography2ipa tag | Rows |
|---|---|---:|
| Porto | `pt-PT-x-porto` | 17 |
| Braga | `pt-PT-x-minho` | 9 |
| Viseu, Coimbra | `pt-PT-x-beira` | 8 |
| Aveiro | `pt-PT-x-aveiro` | 6 |
| Bragança, Vila Real | `pt-PT-x-trasosmontes` | 6 |
| Lisboa | `pt-PT-x-lisbon` | 5 |
| Funchal, Ribeira Brava, Porto Santo | `pt-PT-x-madeira` | 4 |
| Viana do Castelo | `pt-PT-x-viana` | 4 |
| Faro | `pt-PT-x-algarve` | 3 |
| Terceira, São Miguel | `pt-PT-x-acores` | 2 |
| Portalegre | `pt-PT-x-alentejo` | 1 |
| Alfena, Porto (locality) | `pt-PT-x-alfena` | 1 |

Two rows (Marinha Grande and Amor, both Leiria district) are excluded:
Leiria straddles the Estremadura/Beira Litoral dialect boundary and has
no corresponding spec in this repo, so they are dropped rather than
forced into a neighbouring dialect.

Because the gold contains sentence-level, connected-speech phonetics
(the same caveat as `ep_dialects`), PER is naturally higher than the
lexicon benchmarks.

### Mirandese gold set

[TigreGotico/mirandese_g2p](https://huggingface.co/datasets/TigreGotico/mirandese_g2p)
on Hugging Face: ~220 word/IPA rows with a dialect column (central,
raiano, sendinese), collected by a native Mirandese speaker
([MdMV](https://commons.wikimedia.org/wiki/User:MdMV_or_Emdy_idk)).
Native-speaker provenance makes it the reference gold for Mirandese;
its size keeps results indicative rather than statistical.

### 4catac Catalan accents gold set

[projecte-aina/4catac](https://huggingface.co/datasets/projecte-aina/4catac)
on Hugging Face: 160 sentence-level rows per accent, expert-transcribed
in IPA following Institut d'Estudis Catalans guidelines, with
consensus review across multiple annotators. The same 160 sentences
(with small morphological adaptations where needed) are transcribed
separately for four Catalan accents, one TSV per accent:

| 4catac file | orthography2ipa tag | Notes |
|---|---|---|
| `Projecte BSC frases - Central.tsv` | `ca` | Central/standard Catalan |
| `Projecte BSC frases - Balear.tsv` | `ca-x-balear` | Balearic |
| `Projecte BSC frases - Nord-Occ.tsv` | `ca-x-occidental` | Northwestern/Lleidatà — **not** `ca-x-nord` (Northern Catalan/Rossellonès, a distinct dialect spoken in France that 4catac does not cover) |
| `Projecte BSC frases - Val.tsv` | `ca-x-valencia` | Valencian |

Sentences were "intentionally written to showcase various phonetic
phenomena" across the four accents, so this is a targeted, curated
gold set rather than a random sample. Because the gold is
sentence-level, PER reflects connected-speech phonology on top of
grapheme-to-phoneme rules, so it is naturally higher than the
lexicon-style benchmarks. No rows are excluded.

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

### HiTZ Basque Wikipedia IPA corpus (`hitz_basque_ipa`)

[HiTZ/wikipedia_basque_ipa](https://huggingface.co/datasets/HiTZ/wikipedia_basque_ipa)
on Hugging Face: ~1,672,981 paragraph-level `text`/`phonemes` rows
extracted from the Basque Wikipedia dump, published by
**HiTZ Zentroa / AhoLab**, the University of the Basque Country
(UPV/EHU)'s NLP research group. IPA is produced by **ahoNT**, HiTZ's
Basque text-processing and phonemization tool — i.e. this is
tool-generated IPA, not human-annotated.

Per the provenance-discipline rule above, tool-generated IPA is normally
excluded from this benchmark. This dataset is an **explicit,
dataset-specific exception**: the user directed that datasets published
by universities/academic NLP research centers count as legitimate gold
sources for this benchmark even when the IPA came from an automatic
tool, specifically because the publishing body (HiTZ) is an established
academic research group, not because the "human vs. tool" line has been
generally relaxed. This exception applies only to this dataset; it does
not license adding other automatically-phonemized sources without a
similar explicit call.

Wired as `eu` under the `hitz_basque_ipa` dataset key, **additive** to
the existing `wikipron` `eu` entry (Wiktionary-sourced, community
provenance) — it does not replace or reduce that coverage.

Because the source data is paragraph-level rather than word-level, the
loader (`load_hitz_basque` in `scripts/benchmark.py`) pages the dataset
through the Hugging Face datasets-server `rows` REST API (never
downloading the full parquet), whitespace-tokenizes each paragraph's
`text` and `phonemes` in lockstep (ahoNT emits one phoneme token per
source word, punctuation attached to the token, per the dataset card),
pairs tokens positionally, strips surrounding punctuation from both
sides, and keeps the first `limit` (default 300) deduplicated
single-word pairs. Single word-tokens are used as the scored unit —
following `load_ep_dialects`'s precedent of scoring non-lexicon-shaped
gold through the harness's standard `transcribe_word`/PER pipeline —
rather than whole sentences, since paragraph-level ahoNT stress
placement is not verified to depend on sentence context, making the
single-token span the more conservative unit to score in isolation.

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
| ep_dialects | pt-PT | 30 | 0.260 | 1.00 |
| ep_dialects | pt-PT-x-porto | 40 | 0.342 | 1.00 |
| ep_dialects | pt-PT-x-madeira | 30 | 0.362 | 1.00 |
| ep_dialects | pt-PT-x-algarve | 30 | 0.394 | 1.00 |
| ep_dialects | pt-PT-x-lisbon | 45 | 0.398 | 1.00 |
| ep_dialects | pt-PT-x-alentejo | 30 | 0.423 | 1.00 |
| ep_dialects | pt-PT-x-acores | 29 | 0.474 | 1.00 |
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

Reading the table: languages whose specs carry positional grapheme
rules and stress blocks (gl, es, pt-PT, mwl) score far better than
those without — the engine consults
`positional_graphemes`/`stress` whenever a spec provides them, so the
per-language path to a better number is richer spec data, not engine
changes. The pt-BR/pt-AO/pt-TL rows lack positional vowel-reduction
blocks; the en-US row reflects English orthography itself.

Among the newer rows: rule-complete languages with positional
grapheme blocks score best (eo, fi, ro, gl, eu, ast, sq, it); the
nb/da/sv/de rows reflect irregular stress and vowel-reduction patterns
not yet encoded in those specs, and the hi/ta/ml rows expose the
Indic-script calibration gap — engine-spec gaps, not dataset problems.


## Agreement with espeak-ng

[`scripts/espeak_agreement.py`](../scripts/espeak_agreement.py) compares
this engine's output against espeak-ng on the same word lists. This is
**not an accuracy benchmark** — espeak is not a gold standard. It
answers a deployment question: a TTS model trained on espeak
phonemization maps phoneme symbols to embedding IDs, so replacing its
front-end requires symbol-level compatibility, not correctness.

Signals: **exact** (identical transcription), **exact-nostress**
(identical after stress-mark removal — espeak places stress inside the
syllable, this engine before it), **segmental** (mean character
similarity, stress-stripped), and **oov-rate** — the fraction of words
whose transcription contains a symbol espeak never emits for that
voice. Out-of-inventory symbols become unknown embedding IDs, so
oov-rate is the hard-failure signal; the offending symbols are listed
per run.

Coverage is the overlap between this repo's registered gold-dataset
languages and espeak-ng's own voice list — every language with both a
wordlist loader and an espeak-ng voice gets a row; languages with no
espeak-ng voice (e.g. Galician, Mirandese) are skipped rather than
scored as zero.

Full committed scoreboard: [`docs/espeak_agreement.md`]
(espeak_agreement.md) (machine-readable:
[`benchmarks/espeak_agreement.json`](../benchmarks/espeak_agreement.json)).
Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/espeak_agreement.py --scoreboard
```

This is a snapshot, not a CI-gated check — there is no ground truth to
regress against, so `scripts/check_benchmark_regression.py` never reads
these numbers. A handful of languages (`pt-PT`, `pt-BR`, `pt-AO`,
`pt-MZ`, `pt-TL`, `en-US`) need the optional `tugalex`/`scriptconv`
loaders, and a handful of sentence-level sources (`ca` and its regional
variants) trip espeak-ng's own sentence-splitting on punctuation, which
misaligns the word-for-word comparison; both cases are skipped with a
visible warning rather than reported as fabricated numbers — rerun with
those dependencies installed and the missing rows fill in.

Reading the table: stress-mark placement alone rules out byte-exact
replacement almost everywhere; segmental similarity shows how close the
phone sequences are; the oov-rate column decides deployability. A
near-zero oov-rate (Spanish, French, Italian) means a symbol-mapping
shim suffices; a high one (English — espeak-ng writes the TRAP vowel as
⟨a⟩ where this engine emits ⟨æ⟩) means a per-symbol translation table
must be built and validated before any swap. A low oov-rate is a
signal of espeak-compatible **output shape**, not of linguistic
correctness — espeak-ng is an imperfect system being agreed with, not a
gold standard, so this table never substitutes for the gold-benchmark
scoreboard above.

