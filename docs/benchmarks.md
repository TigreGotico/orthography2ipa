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

## Provenance and reliability (read this before trusting any number)

Reliable G2P "gold" barely exists. There is no large, human-verified,
IPA-transcribed word list for most of the languages here — so the
datasets below are, in honest descending order of trust,
phonetician-curated, native-speaker-collected, dictionary-extracted,
Wiktionary-scraped, or **a phonemizer's own output reused as a
reference**. This is not a defect to hide; it is the state of the field,
and it changes how every number on the [scoreboard](scoreboard.md) must
be read:

- **A low PER against a `machine-generated` gold means "agrees with that
  tool", NOT "correct".** `styletts2_phonemes`, `ipa_childes` and
  `hitz_basque_ipa` are all the output of an automatic phonemizer. Scoring
  well there says o2i reproduces that tool's decisions, right or wrong.
- **Scoring a system against a gold its own generator produced is
  near-tautological.** `hitz_basque_ipa` *is* the output of HiTZ's
  ahoNT/AhoTTS phonemizer, so a low PER for AhoTTS/ahotts-g2p on it just
  confirms the tool reproduces itself — it is not evidence of
  correctness. The same trap applies to any comparison where the
  evaluated system shares the gold's generator: use an **independent**
  gold (here, `wikipron` `eu`) for the fair comparison.
- **Comparing o2i to espeak on an espeak-derived gold is partly
  circular** for the same reason. `styletts2_phonemes` is
  phonemizer/espeak-lineage; an espeak-vs-o2i table on that gold measures
  how similarly two systems diverge from the truth, not who is closer to
  it.
- **Absolute PER is noisy — treat it as directional, not precise.** Runs
  are capped at 300 alphabetically-ordered words; the same spec can move
  ±several points between slices. Read numbers as relative/ranking
  signals, not measurements to three decimals.
- **Small-`N` rows are anecdotes.** Many `clup_dialect` rows are `N=1–17`
  and several `ep_dialects`/`mirandese` rows are `N<30`. Always
  cross-reference the row's bootstrap `95% CI` on the scoreboard: a wide
  or degenerate interval (e.g. `N=1` gives `[x, x]`) means the row cannot
  support a conclusion, only a hint.

Even the `expert-human` tier is not "truth": it is bound by the
annotating team's transcription conventions (broad vs narrow choices,
stress and tie-bar notation, dialect target) and, in this repo, is often
small-n or not yet externally peer-validated. The tiers rank *how the IPA
was produced*, not a guarantee of correctness.

### Reliability tiers

The machine-readable tier per dataset lives in the `provenance` column of
[`docs/scoreboard.md`](scoreboard.md) and the `provenance` field of
[`benchmarks/results.json`](../benchmarks/results.json), sourced from the
single `PROVENANCE` map in `scripts/benchmark.py` (a test forces every
registered dataset to carry a tier, so a new dataset cannot be added
without classifying it).

| Tier | What it means | Grain of salt |
|---|---|---|
| **expert-human** | IPA curated by phoneticians, trained annotators, or native speakers. | Still bound by the team's notation conventions; here often small-`N` and/or not peer-validated. |
| **lexicon-derived** | Human lexicographers, via a published dictionary's notation — sometimes through a mechanical notation transform (ARPABET→IPA, slashed-phonemic→IPA). | Dictionary conventions ≠ surface phonetics; the transform step can add its own artifacts. |
| **crowd-scraped** | Wiktionary community edits (WikiPron). | Uneven per language; some entries are themselves editor-applied rule output, not attested transcriptions. |
| **machine-generated** | A phonemizer's *own output* reused as the reference. | **Biggest grain of salt.** Low PER = agreement with that tool, not correctness; espeak-lineage golds make an espeak comparison partly circular. |

### Per-dataset classification

Every dataset registered in `scripts/benchmark.py`'s `DATASETS`,
classified by reading its loader (source URL, docstring, transform) and
its section below. Where the evidence is incomplete, the uncertainty is
stated rather than papered over.

| Dataset | Tier | IPA produced by | Notes / grain of salt |
|---|---|---|---|
| `ep_dialects` | expert-human | TigreGotico team, manual annotation | Internal dialect research, **pending external peer validation**; sentence-level, `N≈29–45`. |
| `mirandese` | expert-human | Native Mirandese speaker | Reference gold for Mirandese, but small (`mwl` `N≈205`; `mwl-x-sendim` `N≈11` — an anecdote). |
| `4catac` | expert-human | Expert annotators (Projecte AINA/BSC) | IEC guidelines, multi-annotator consensus review; sentence-level, `N=160`, `0.00` exact-match reflects notation/connected-speech mismatch, not total failure. |
| `clup_dialect` | expert-human | U.Porto CLUP dialect archive | Interview corpus is expert university dialectology, **but who/what produced the IPA column (`ArquivoDialetalCLUP_ipa`) is not documented in the loader or dataset card — treat the tier as "best case".** Many rows `N=1–17`: read the CI, not the point PER. |
| `portuguese_lexicon` | lexicon-derived | Portal da Língua Portuguesa lexicographers | Via `tugalex`; the strongest Portuguese gold, but dictionary citation-form IPA, not connected speech. |
| `infopedia_pt` | lexicon-derived | Infopédia (Porto Editora) dictionary | Graph-crawl extraction of a published dictionary; citation-form conventions. |
| `cmudict` | lexicon-derived | CMU Speech Group (hand-curated ARPABET) | Human labels, but **mechanically mapped ARPABET→IPA** via `scriptconv`; the transform adds artifacts. |
| `ipadict` | lexicon-derived | Hjal/malfong Icelandic linguists (`is` only) | Only the human-curated `is` file is wired; the ipa-dict *project* is mixed-provenance and many of its files are tool-generated (see "Rejected candidates") — do not generalize this tier to other ipa-dict languages. |
| `wikipron` | crowd-scraped | Wiktionary editors | Quality tracks community size; some entries are editor-rule output, not attested; multiple valid variants per word. |
| `styletts2_phonemes` | machine-generated | Automatic phonemizer (TTS `synthetic` tag) | **Grain of salt maximal.** Phonemizer/espeak-lineage; low PER = agrees with the phonemizer; espeak comparison on this gold is partly circular. |
| `ipa_childes` | machine-generated | CHILDES "G2P+" automatic phonemizer | Tool-phonemized child-language corpus; accepted under the academic-corpus exception, still tool output. |
| `hitz_basque_ipa` | machine-generated | HiTZ **ahoNT / AhoTTS** phonemizer | University-published (HiTZ/UPV-EHU), but the gold **is ahoNT/AhoTTS output** — it was generated by that phonemizer, not human-annotated. So a low PER **for the AhoTTS/ahotts-g2p engine on this row is near-tautological** (a tool scored against its own output); the independent, Wiktionary-sourced `wikipron` `eu` row is the fair comparison for Basque. |

## Provenance discipline

Because reliable gold is scarce, the harness applies a deliberate
discipline: prefer human/community provenance, and where tool-generated
IPA is admitted, admit it **explicitly, per dataset, with the reason
recorded** — never silently. Three tool-generated sources are wired in
(`hitz_basque_ipa`, `ipa_childes`, `styletts2_phonemes`), each under a
documented, dataset-specific exception (academic-corpus provenance or an
explicit task override) rather than a blanket relaxation. Their rows
carry the `machine-generated` tier so the caveat above travels with every
number they produce. Adding another tool-generated source requires the
same explicit call; it is not the default.

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
| `ar` | `ara_arab_broad.tsv` | 17 563 | Modern Standard Arabic (Arabic script, WikiPron's `ara` macro-language code). Entries come from Wiktionary's fully-vocalized (tashkeel-marked) headwords, matching the `ar` spec's documented tashkeel-dependent input contract (see the spec's `notes` field). |

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
annotated with dialectal IPA.  Source: DIALECT\_PATTERNS.md feature matrix,
derived from Cintra, L.F.L. (1971), "Nova proposta de classificação dos
dialectos galego-portugueses", Boletim de Filologia 22:81–116.
Provenance: sentence-level gold produced by the same team that maintains
the dialect specs; pending external peer validation.

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

### StyleTTS2 community multilingual phonemes (`styletts2_phonemes`)

[styletts2-community/multilingual-phonemes-10k-alpha](https://huggingface.co/datasets/styletts2-community/multilingual-phonemes-10k-alpha)
on Hugging Face: sentence-level `text`/`phonemes` pairs, one JSON
config file per language, released under **CC BY-SA 3.0**. The
transcriptions are machine-generated (phonemized for TTS
training/evaluation, per the `synthetic` dataset tag) rather than
hand-annotated; per an explicit, task-specific override this benchmark
treats them as usable gold regardless of human-vs-tool provenance,
same as the `hitz_basque_ipa` exception above but without the
academic-publisher condition attached — this override is scoped to
this dataset only.

The dataset ships 15 single-language configs plus an `en-xl` config
(a 100K-row scale-up of the same English data already covered by the
`en` config here and by `wikipron`/`cmudict`, so it is left out as
redundant). 14 of the 15 single-language configs are wired, each
against the `orthography2ipa` language tag matching its config name:

| Lang | Rows (full file) |
|---|---:|
| `en` | 10,212 |
| `ca` | 13,451 |
| `de` | 11,355 |
| `es` | 10,449 |
| `el` | 10,260 |
| `fa` | 13,031 |
| `fi` | 10,347 |
| `fr` | 10,395 |
| `it` | 10,235 |
| `pl` | 11,446 |
| `pt` | 11,585 |
| `ru` | 10,604 |
| `sv` | 2,706 |
| `uk` | 11,064 |

`fa` and `uk` had no prior gold coverage in this harness before this
dataset; the rest are additive, complementary sentence-level
cross-checks to their existing word-level `wikipron`/lexicon entries.

`zh` was evaluated but is excluded from this dataset: this repo's
`zh` spec (`orthography2ipa/data/zh.json`) declares graphemes that are
romanized pinyin letters and expects romanized pinyin input, while the
`styletts2_phonemes` dataset's `zh` config's `text` field is raw hanzi
(e.g. `"分布于美洲的北温带..."`). The engine cannot transcribe hanzi at
all (`G2P('zh').transcribe_word('你好')` returns an empty string), so
scoring this row would not measure phonological accuracy — it is a
script/input-contract mismatch between the dataset and this repo's
`zh` spec, not a gap in the engine's Mandarin coverage.

The loader (`load_styletts2_phonemes` in `scripts/benchmark.py`)
downloads each language's JSON file directly and pairs `text` with
`phonemes` positionally, scored as sentence-level spans through the
harness's standard pipeline (as with `4catac`/`ep_dialects`).

### IPA-CHILDES split (`ipa_childes`)

[fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)
on Hugging Face: a postprocessed version of IPA-CHILDES, the phonemized
CHILDES child-language corpus (CC BY 4.0), split into per-language
`train`/`test` CSVs (28 languages, `test` split ranging from ~460k to
~74MB per language, 256,462 test rows for `en-US`). Each row is a
sentence-level utterance with several IPA columns; this harness uses
`ipa_g2p_plus` (the "G2P+" phonemizer column), which the dataset
publishes pipe-(" | ")-delimited with one segment per orthographic word,
aligned positionally with the whitespace-tokenized orthographic sentence.
Per the CHILDES/academic-corpus exception, tool-generated transcriptions
from this dataset are accepted as gold here.

Wired under the `ipa_childes` dataset key for `en-US`, `et`, `hu`, `id`,
`sr`, `zh` — 6 of the dataset languages with no prior gold coverage in
this harness at all *and* a language tag registered in this repo's specs
(`orthography2ipa/data/*.json`). Only the `test` split is read (held out
from G2P+ training). The loader (`load_ipa_childes` in
`scripts/benchmark.py`) splits each row's orthographic sentence and its
`ipa_g2p_plus` column on whitespace/`" | "` respectively, pairs tokens
positionally, skips rows whose token counts don't line up, and keeps the
first `limit` (default 300) deduplicated single-word pairs — the same
positional-alignment technique `load_hitz_basque` uses for paragraph-level
gold, applied here to dataset-native sentence-level alignment instead of
manual tokenization.

`zh` is read from the dataset's `stem` column rather than its `sentence`
column: `sentence` is Hanzi, but this repo's `zh` spec models **Pinyin**
syllables (its grapheme table is Pinyin initials/finals, not Hanzi), and
`stem` is CHILDES's own Pinyin-with-tone-number romanization of the same
utterance — the column that actually exercises the spec's grapheme table.

`ko-KR` is present in the dataset but **excluded** here, for the same
class of script/input-contract mismatch as the `zh` exclusion below:
this repo's `ko` spec's grapheme table is keyed on individual
compatibility jamo (`ㄱ`, `ㄲ`, `ㄷ`, ...), while real Korean text —
including this dataset's — is precomposed Hangul syllable blocks (e.g.
`아홉`), which neither match the compatibility-jamo graphemes directly
nor decompose into them under NFD (NFD splits a Hangul syllable into
*conjoining* jamo, a different Unicode block from the *compatibility*
jamo the spec's grapheme table uses). `G2P('ko').transcribe_word(...)`
returns an empty string for every real Hangul word tested, so scoring
this row would not measure phonological accuracy — it is a
script/input-contract mismatch between the dataset and this repo's
`ko` spec, not a gap in the engine's Korean coverage. Bridging
compatibility jamo and precomposed Hangul is a real engine-level
enhancement, left for a future change; it is out of scope here.

Present in the dataset but **not** wired in:

- **`fa-IR`** (Persian): this corpus's Persian transcripts are Fingilish
  (ad hoc Latin transliteration, e.g. `"piano kar kardam"`), never Persian
  script; the `fa` spec here is Arabic-script only, so there is no clean
  grapheme match.
- **`ja-JP`** (Japanese): this corpus's Japanese transcripts are romaji
  only — the dataset has no kana/kanji column for Japanese — while the
  `ja` spec here has a hiragana grapheme table, so there is no clean
  grapheme match either.
- **`ca-ES`, `cy-GB`, `da-DK`, `de-DE`, `en-GB`, `es-ES`, `eu-ES`, `fr-FR`,
  `ga-IE`, `hr-HR`, `is-IS`, `it-IT`, `nb-NO`, `nl-NL`, `pl-PL`, `pt-BR`,
  `pt-PT`, `ro-RO`, `sv-SE`, `tr-TR`**: language codes with an existing
  spec in this repo, but every one of them already has gold coverage from
  another dataset above; not worth the extra CSV download for
  already-measured languages.
- **`qu-PE`** (Quechua), **`yue-CN`** (Cantonese): no corresponding spec
  exists in this repo at all.

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

## Diagnosing a language

The scoreboard tells you *that* a language scores badly; it does not tell
you *why*. `scripts/error_analysis.py` is the microscope: it runs a gold
dataset through the engine and reports where the errors concentrate, so
spec work starts from evidence instead of guesswork. It is strictly
read-only — it never touches a spec or any other file.

```bash
PYTHONPATH=$PWD python scripts/error_analysis.py pt-PT --dataset infopedia_pt --limit 300
```

`<lang>` is required; `--dataset` is optional (when omitted, the first
registered dataset that covers the language is used), `--limit` caps the
gold slice (default 300, same as the benchmark harness), and `--json`
emits all three sections as one JSON object instead of the text report.
Alignment reuses the same routine (`scripts.benchmark.align`) and the
same default normalization (stress marks and narrow diacritics stripped)
that the scoreboard uses, so what you see here matches how PER is scored.

The report has three sections; read them in this order:

1. **Top-20 phoneme confusion pairs** (`gold -> hyp`). Each row is an
   aligned mismatch, ranked by how often it occurs. `∅` on the gold side
   is an *insertion* (the engine emitted a phoneme the gold does not
   have); `∅` on the hyp side is a *deletion* (the engine dropped a gold
   phoneme). A single high-count pair — e.g. `'r' -> 'ɾ'` — is usually
   one wrong or missing grapheme/allophone rule and the fastest fix.

2. **Top-20 worst words** — the words with the highest per-word PER, gold
   and hyp side by side. Use these to see the confusion pairs *in
   context*: whether a substitution is systematic (every word) or
   conditioned (only before front vowels, only word-finally, etc.), which
   tells you whether the fix is a flat grapheme change or a positional
   rule.

3. **Per-grapheme blame** — for each orthographic character/digraph in
   the spec's grapheme map, the mean PER of gold words containing it
   (minimum 3 occurrences), worst-first. This points at which *spelling*
   is costing you accuracy. It is a triage signal (substring containment,
   not tokenization), so treat a high-blame grapheme as "look here first",
   then confirm against the confusion pairs and worst words.

Feed the top confusion pairs into the per-language procedure: classify
each systematic error (missing/wrong grapheme mapping, missing positional
rule, missing sandhi, stress placement, or genuinely lexical), cite a
published source for every spec change, and re-run the tool to confirm
the pair's count dropped.

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

### Confidence intervals

Every scoreboard row (`docs/scoreboard.md` / `benchmarks/results.json`)
carries a 95% bootstrap confidence interval on the mean PER, alongside
the point estimate, so a single-slice PER number can be read with its
uncertainty rather than as a false-precision leaderboard entry:

- The per-word PER list underlying a row's mean PER is resampled with
  replacement 1000 times; the mean of each resample is computed, and
  the interval is the 2.5th/97.5th percentile of that distribution.
- Resampling uses `random.Random(BOOTSTRAP_SEED)` (`scripts/benchmark.py`),
  never the global RNG, with a fixed seed constant — the same input PER
  list always yields the same `[low, high]` bounds, on any machine, on
  any run. This is what makes the CI reproducible rather than a
  moving target that would itself trigger false benchmark-regression
  noise.
- The regression gate (`scripts/check_benchmark_regression.py`) keeps
  comparing the point-estimate PER against the committed baseline with
  its existing epsilon — the CI is a reporting/diagnostic addition, not
  part of the pass/fail regression check.
- A wide interval is itself informative: it flags a row whose PER is
  noisy given its sample size (small `N`, or high per-word variance),
  and is a signal to grow the gold set before trusting a narrow slice
  of PER movement as a real regression or improvement.

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

