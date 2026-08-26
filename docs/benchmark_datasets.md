# Benchmark gold datasets

Every gold pronunciation dataset the harness can score against, with where it
came from and what its numbers can and cannot support. Read
[benchmarks.md](benchmarks.md) first for the provenance tiers these sections
refer to.

Jump to a dataset:

- [Primary-source gold (`primary_sources`)](#primary-source-gold-primary_sources)
- [Portuguese unified pronunciation lexicon (`portuguese_unified`)](#portuguese-unified-pronunciation-lexicon-portuguese_unified)
- [WikiPron](#wikipron)
- [Arabic with tashkeel restored (`wikipron_ar_diacritized`)](#arabic-with-tashkeel-restored-wikipron_ar_diacritized)
- [Norwegian under the macrolanguage code (`wikipron_nor`)](#norwegian-under-the-macrolanguage-code-wikipron_nor)
- [CMU Pronouncing Dictionary](#cmu-pronouncing-dictionary)
- [European Portuguese regional dialect gold set (`ep_dialects`)](#european-portuguese-regional-dialect-gold-set-ep_dialects)
- [CLUP dialect archive gold set (`clup_dialect`)](#clup-dialect-archive-gold-set-clup_dialect)
- [Mirandese gold set](#mirandese-gold-set)
- [Barranquenho synthetic IPA dictionary (`barranquenho_dict`)](#barranquenho-synthetic-ipa-dictionary-barranquenho_dict)
- [Mirandese synthetic IPA dictionary (`mirandese_dict`)](#mirandese-synthetic-ipa-dictionary-mirandese_dict)
- [4catac Catalan accents gold set](#4catac-catalan-accents-gold-set)
- [ipa-dict pronunciation dictionaries (`ipadict`)](#ipa-dict-pronunciation-dictionaries-ipadict)
- [HiTZ Basque Wikipedia IPA corpus (`hitz_basque_ipa`)](#hitz-basque-wikipedia-ipa-corpus-hitz_basque_ipa)
- [VoxCommunis parallel G2P (`vox_communis`)](#voxcommunis-parallel-g2p-vox_communis)
- [VoxCommunis with the Vietnamese tone merge repaired (`vox_communis_corrected`)](#voxcommunis-with-the-vietnamese-tone-merge-repaired-vox_communis_corrected)
- [IPA-CHILDES split (`ipa_childes`)](#ipa-childes-split-ipa_childes)
- [IPA-BabyLM (`ipa_babylm`)](#ipa-babylm-ipa_babylm)
- [Lexibank/CLDF wordlist gold (`northeuralex`, `wold`)](#lexibankcldf-wordlist-gold-northeuralex-wold)
- [kaikki.org Wiktextract gold (`kaikki`)](#kaikkiorg-wiktextract-gold-kaikki)

### Primary-source gold (`primary_sources`)

`orthography2ipa/data/gold/primary_sources/`: every row is a worked example
printed by a linguist in a source one of our own specs cites: Almbark & Hellmuth
(2015) for Damascene, Jasim (2020) for Baghdadi gilit and Muslawi qəltu, Fadda
(2016) for Ammani, Cotter (2016) for Gaza City, Brissos (2014) for the European
Portuguese central-interior and southwestern dialects, and the JIPA *Illustrations of
the IPA* word lists for Ukrainian (Pompino-Marschall, Steriopolo & Żygis 2017),
Russian (Yanushevskaya & Bunčić 2015), European Portuguese (Cruz-Ferreira 1995) and
Brazilian Portuguese (Barbosa & Albano 2004): the last two cited by the `pt-PT` and
`pt-BR` specs themselves. the Castilian (Martínez-Celdrán, Fernández-Planas & Carrera-Sabaté 2003) and Argentine
(Coloma 2018) Spanish Illustrations, and the phonology chapter of
Williams-van Klinken, Hajek & Nordlinger (2002) for Tetun Dili. 664 rows, 36
varieties.

The Tetun Dili rows are the whole gold that language has, and they are read
strictly as a faithfulness check: the grammar they come from is also the source
the `tet` spec is written from, so they measure whether the engine reproduces
what that grammar says, never whether the grammar is right. Fourteen of the rows print no
spelling of their own — the thirteen-item stress inventory, which the grammar gives
in transcription only, and one /ʎ/ example — so their orthography is written out
with the grammar's own conventions and flagged `editor-supplied`. Every row was
transcribed from a render of the printed page, not from the PDF's text layer,
which mangles the IPA and flattens the trill/tap distinction the grammar does
make in transcription.

Each row carries the source id, the **printed** page (not the PDF page index: they diverge, and `sources.json` records the offset per source), the source's own
notation verbatim, whether the source wrote it broad `/…/` or narrow `[…]`, and a
confidence. Nothing is silently coerced: transliterated rows can never be
`confidence: high`, and the Arabic input words carry editor-supplied ḥarakāt,
flagged per row.

It is deliberately small and deliberately adversarial: several rows exist
*because* the source contradicts the spec (gilit kaf affrication is not
front-vowel-conditioned, Ammani emphasis spreads onto a final /t/, the Beira and
Alentejo chain shifts are modelled only in their /u/ → [y] leg). The dataset
README lists all of them. Diagnose rules with it. Do not gate a language on
`N=12`. Where a source's PDF mangles its own IPA (scans, legacy fonts), the rows are
transcribed from a render of the printed page: never decoded from the mangled bytes.

### Portuguese unified pronunciation lexicon (`portuguese_unified`)

[TigreGotico/portuguese-unified-pronunciation-lexicon](https://huggingface.co/datasets/TigreGotico/portuguese-unified-pronunciation-lexicon)
(~598k rows / 121,938 words, CC BY-SA 4.0) merges the three previous
Portuguese golds into one convention-normalized dataset and REPLACES their
separate loaders here:

- **Infopédia** (Porto Editora): 102,685 dictionary extractions (European
  Portuguese, broad phonemic).
- **Portal da Língua Portuguesa** (INESC-ID): the 10-region semi-automated
  phonetic lexicon (53,349 words).
- **pt.wiktionary.org**: 15,720 community-transcribed words with explicit
  region tags.

Each row is a word × region × source × POS tuple carrying both a broad
phonemic (`ipa_broad`) and a narrow phonetic (`ipa_narrow`) transcription
normalized across the three source conventions (`ə/ɨ`, `r/ɾ/ʀ`, `a/ɐ`,
optional-segment and syllable-marker stripping). **`ipa_narrow` is
scored**: it matches the transcription depth of the pt specs and of the
previous gold (explicit [ɐ ɨ ɾ ʀ ɫ]).

One region is scored per registered language tag (`_PT_UNIFIED_REGIONS`):
`pt-PT`, `pt-PT-x-lisbon`←`pt-PT-x-lisboa`, `pt-BR` (Wiktionary),
`pt-BR-x-sp`←`saopaulo`, `pt-BR-x-rj`←`riodejaneiro`, `pt-BR-x-carioca`,
`pt-BR-x-caipira`, `pt-AO`, `pt-MZ`←`maputo`, `pt-TL`←`dili`. Untagged
plain-`pt` rows (pan-Portuguese, 944) are excluded from every regional row.
The whole file is read and a fixed-seed random sample of up to `limit`
words is drawn per region (alphabetical heads would be biased).

**`pt-TL` carries a per-language override, `machine-generated`** (see
`PROVENANCE_BY_LANG["portuguese_unified"]`), not the dataset-wide
`lexicon-derived`. Diffed word-for-word against `pt-PT-x-lisboa` over the
53,147 words the two regions share, `pt-TL-x-dili` is a near-total 1:1
character correspondence with the Lisbon entries (ɐ→ə in 28,713 words, u→ʊ
in 11,653, ʀ→r in 3,994, ɫ→w in 1,681, d→ð in 212, g→ɣ in 146), and it still keeps Lisbon-style unstressed-vowel reduction (60%
of rows keep a reduced [ə], 31% a reduced final [ʊ]) and the Lisbon "chiado"
coda /s/→[ʃ]. The `pt-TL` spec's primary source (Albuquerque 2010:275 fn.7,
277) documents the opposite for East Timorese Portuguese — no
unstressed-vowel reduction, alveolar (non-hush) coda /s/ — so this row
measures agreement with a re-symbolized European Portuguese, not the
acrolectal variety the spec models. It can never gate a quality decision
on `pt-TL` (see `docs/languages/pt-TL.md`).

### WikiPron

Word/IPA pairs mined from Wiktionary by
[CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)
(Lee et al. 2020, *WikiPron: Mining Wiktionary for Massively
Multilingual Pronunciation Data*, LREC). Community-curated by Wiktionary
editors: reliable where the editor community is large. The broad-
transcription TSVs are used. Note the gold carries **multiple valid
transcriptions per word** (dialect variants such as Galician
seseo/gheada). The harness scores against all of them and keeps the
best match.

Core wired tags: `gl`, `es`, `pt`, `pt-BR`, `en`, `en-GB`.

#### Module-generated WikiPron rows

On a large tag the IPA column is what Wiktionary editors typed. On a small
one it often is not. Several languages have a per-language Lua generator
(`Module:<code>-IPA`) that the entries invoke through a bare pronunciation
template, so the "gold" for that tag is that module's output, scraped.

This is the `hitz_basque_ipa` problem in a `crowd-scraped` row: a low PER
there measures **agreement with the generator, not accuracy**, and the
scoreboard's provenance column does not say so, because the tier is set
per dataset and `wikipron` as a whole is genuinely crowd-scraped.

The same thing happens on a `kaikki` row, which extracts the same Wiktionary source through a different pipeline, so the table below is not WikiPron-only.

Six rows are known to be affected, three of them wired by the small-wikipron sweep:

| tag | what the gold actually is | how to read the row |
|---|---|---|
| `tew` (Tewa, `N=106`) | **entirely** `Module:tew-IPA` output — every headword carries a bare `{{tew-IPA}}` and no hand-typed IPA | **`PER 0.0000` certifies reproduction of `Module:tew-IPA` on 106 words, not accuracy.** The spec was built from the same Martinez (1982) orthography and Sutton (2014) values the module cites, and cross-checked against the module, so engine and gold share a source. |
| `ha` (Hausa, `N=1857`) | **entirely** `Module:ha-IPA` output — a 31-headword random sample carried a bare `{{ha-IPA\|<respelling>}}` template and no hand-typed IPA in all 31 cases | The module computes the IPA column from an editor-typed tone-and-length-marked respelling, not from spoken attestation per entry. Every `ha` row certifies reproduction of that module's output, not independent pronunciation accuracy; see [languages/ha.md](languages/ha.md). |
| `nmy` (Namuyi, `N=354`) | a **mix** of hand-typed IPA and `Module:nmy-IPA` output | Weaker form of the same caveat: part of the row is a reproduction test. The residual error is dominated by unwritten vowel nasalisation, which is a real gap either way. |
| `mn` (Khalkha Mongolian, `N=3528`) | a **mix** of hand-typed IPA and `Module:mn-IPA` output — a 40-headword sample of the raw en.wiktionary source drew roughly three module-generated entries for every hand-typed one | Same weaker caveat as `nmy`: part of the row is a reproduction test rather than an accuracy test. See [languages/mn.md](languages/mn.md). |
| `egy` (Ancient Egyptian, `N=2185`) | mostly `Module:egy-pron` output, invoked through `{{egy-pr}}`, plus hand-typed reconstructions on the same headwords | **`PER 0.0183` certifies reproduction of the codified Egyptological reading convention on 2185 words, not accuracy** — the convention is a way of saying the words aloud, not a reconstruction of how Egyptian sounded, and the spec encodes it from the same published guidelines the module implements. Not comparison-eligible. See [languages/egy.md](languages/egy.md). |
| `lo` (Lao, `kaikki`, `N=2308`) | `Module:lo-pron` output: 2674 of the 2682 entries carrying IPA give exactly two transcriptions noted Vientiane and Luang Prabang, the mechanical signature of the module generating both registers from the spelling, and the loader keeps the first (Vientiane) | The row measures agreement with `Module:lo-pron`, not accuracy. It is also floored: tone contour letters are 32.4% of the normalized gold characters and appear in every one of the 2308 words, while the engine writes no tone, so roughly a third of the PER is unreachable by any segmental rule. Read the segmental slice — PER over the gold with the tone letters removed — for what the spec actually changed. |
| `th` (Standard Thai, `N≈17k`) | **entirely** `Module:th-pron` output, invoked through a bare `{{th-pron}}` or `{{th-pron\|<respelling>}}` — an 11-word raw-wikitext sample (`เก็บ`, `ก่อน`, `ยิ้ม`, `สัตว์`, `จันทร์`, `รัก`, `บ้าน`, `น้ำ`, `หมา`, `โรงเรียน`, `ประเทศ`) found the template on every headword and no hand-typed IPA anywhere | The module computes tone and vowel length from the spelling (plus the optional respelling argument) the same way the spec's own tone-class/syllable-type analysis would, so a low PER on the tone-bearing part of the row would certify reproduction of that module, not accuracy. The spec now computes tone the same way, so the tone-bearing part of this row measures agreement with `Module:th-pron`'s computation rather than accuracy, and the rule's warrant has to come from its sources instead (see below). |

No such row may be used to certify a language's accuracy, and none
belongs in a cross-system comparison. What they do certify is that the
spec implements the published orthography consistently — which is the
claim the spec makes, and is worth measuring, under its own name.

#### Languages scored against a published spelling convention (`uby`, `twf`)

A related but distinct case: the gold is hand-typed, so it is not a
generator's output, but the *input* column is not a community spelling
either. Ubykh has been extinct since 1992 and was never written by its
speakers. Every Ubykh headword on Wiktionary is spelled in an
Abkhaz-based Cyrillic system published as the [Wiktionary Ubykh entry
guidelines](https://en.wiktionary.org/wiki/Wiktionary:Ubykh_entry_guidelines),
whose alphabet table gives the letter-to-IPA correspondence directly.

The `uby` row therefore certifies **reproduction of that published
convention, not accuracy about Ubykh as spoken**, and the spec's grapheme
map is that table. This is the same reading as the `egy` row above, with
one difference in its favour: the IPA is editor-typed, so the row still
measures whether the engine converts the spelling the way a human applying
the convention does — including the hand-written inconsistencies, which
put a floor under the residual error.

Taos (`twf`) belongs to the same class and is the stronger row of the two.
Its headwords are spelled in the practical orthography of Trager (1948) and
its IPA is editor-typed — the Wiktionary entries carry a literal
`{{IPA|twf|/…/}}`, with no pronunciation module in the loop — so the row
measures the same thing the `uby` row does: whether the engine applies the
published convention the way a human applying it does. The `PER 0.0240`
therefore certifies **reproduction of Trager's 1948 convention on 135
words**, not accuracy about Taos as spoken, and the residual error is
almost entirely hand-typed inconsistency in the gold rather than rule
error.

What separates Taos from Ubykh is that Taos is a living community language
and its orthography was taught to its speakers, so the convention is one
people actually write in rather than an editorial scheme imposed on an
extinct language. That makes the row more than a self-consistency check.
It does not make it accuracy: Trager's letters are Americanist, several
of his analytic choices have documented alternatives (the 1946 unit-phoneme
reading of the aspirates and ejectives, for one), and the row cannot
adjudicate between them. Not comparison-eligible.

A per-language provenance override (`PROVENANCE_BY_LANG["wikipron"]`) would
let the scoreboard carry this in the provenance column instead of only in
prose. That is a `scripts/benchmark.py` change and is proposed, not made,
here.

#### Variety mismatch (`fa`)

A third kind: the gold is neither a generator's output nor missing a
community orthography, but it targets a different variety of the language
than the spec does. The wikipron `fa` set (`fas_arab_broad`, `N=9279`) is
predominantly a Classical / Early New Persian reading, scraped from
Wiktionary; the `fa` spec here targets the modern Tehran standard. Over the
gold's 62914 segments, the classical markers (⟨aː eː oː r w xʷ⟩) dominate the
modern ones (⟨ɒː ɾ v t̪ʰ kʲ⟩) by roughly an order of magnitude, and of the cache's
10312 rows, 208 carry a modern marker against 7506 carrying a classical one,
20 with both. The `fa | wikipron` row on the scoreboard therefore certifies
how well the spec reproduces that Classical/Early New Persian reading
convention, not modern Iranian Persian pronunciation accuracy — see the
`fa.json` grapheme notes for the full count breakdown.

The `fa | ipadict` row (`fa.txt`, `N=7695`) carries its own caveat already
documented in the [ipa-dict source table](#ipa-dict-pronunciation-dictionaries-ipadict)
below: the source repository describes `fa.txt` as machine-generated from
Wiktionary plus PersPred "and a great deal of guesswork", and its own README
calls it "extremely experimental". A PER improvement against that row is a
comparison against an experimental machine-generated file, not a
gold-standard one.

#### A tone-marked gold measures the tone computation too (`th`)

WikiPron transcribes Standard Thai with Chao tone letters, and they are
not a garnish: **32% of every character in the `tha_thai_broad` gold** is
a tone letter (79,041 of 246,222 characters across all 18,416 gold rows,
counted after the benchmark normalizer runs; deduplicated to the 17,221
scored headwords it is 73,093 of 228,584, the same 32%), a count PER
charges in full because the letters are ordinary characters to an edit
distance. Read the `th` rows as two numbers: the segmental part, and the
tone the spec's `tone_rules` block computes from consonant class,
syllable shape, vowel length and tone mark. Scoring the same rows with
the tone letters removed from both sides gives the segmental part alone —
0.1651 against `wikipron` and 0.2218 against `vox_communis`.

The two Thai golds do not write the tone letter in the same slot. WikiPron
writes it after the rime, where IPA writes it (`k ɔː n ˨˩`); the
Epitran-derived `vox_communis` rows write it on the nucleus
(`k ɔː˨˩ n`). The spec follows WikiPron and IPA, so the `vox_communis`
row pays for the mismatch, and the reverse choice would cost more on the
row that is not machine-generated.

Placement, not tone identity, is what that mismatch costs. Scoring both
rows with every tone letter moved to the end of the string on both sides
— which neutralises where the letter is printed while keeping which tone
it is and in what order — gives 0.1713 against `wikipron` and 0.2295
against `vox_communis`. Against the unfolded 0.1881 and 0.4318, placement
alone accounts for 1.7 PER points on the `wikipron` row and 20.2 on the
`vox_communis` row, and the tone the spec computes differs from the tone
either gold carries by under a point on both.

That the gold's tone letters follow the same consonant-class × syllable-type
rule the spec states is not independent confirmation of the rule:
the gold IS that computation (`Module:th-pron`, see [Module-generated
WikiPron rows](#module-generated-wikipron-rows)), so agreement between the
two states the rule twice rather than checking it against a second source.
The rule's citation is Iwasaki & Ingkaphirom (2005) and Haas (1964), not
the gold.

Read `th`'s wikipron row accordingly, and quote the tone-blind figure
alongside it when the question is about segments. This is a spec-side
gap, not a gold defect: the gold is right to write the tone, and the
harness is right to score it. Stripping tone from tonal golds harness-wide
would hide a real deficiency behind a kinder number.

### Arabic with tashkeel restored (`wikipron_ar_diacritized`)

Written Arabic omits the short vowels (harakat): 0 of the ~14k raw
WikiPron Arabic words carry them, so the raw `ar` row scores the engine
on unvocalized input it cannot vowelize and its PER is dominated by
missing vowels rather than rule errors. This row keeps the **same gold
IPA** and restores tashkeel on the **input side only**, with
[text2tashkeel](https://github.com/TigreGotico/text2tashkeel) (ONNX
Arabic diacritizer, rawi default model, ~2% DER). Word-final harakat
are then stripped: the restored case endings (iʿrāb) are real Arabic,
but WikiPron gold records pausal pronunciations, which drop them.

Diacritization is input **normalization** and lives in the harness: orthography2ipa itself does no normalization by design. A downstream
Arabic consumer is expected to feed vocalized (or diacritizer-restored)
text. Both rows are published: raw (deployment floor on bare text) and
diacritized (what the rules actually earn on vowelized input).
`text2tashkeel` is an optional dependency. Without it the row is
skipped, never faked. The diacritized words are cached in
`.benchmark_cache/wikipron_ar_diacritized.tsv` for reproducibility: delete the file to re-diacritize.

### Norwegian under the macrolanguage code (`wikipron_nor`)

WikiPron sorts a pronunciation by the language code written inside the
Wiktionary `{{IPA|…}}` template, not by the language section the template
sits under. Norwegian editors frequently tag a Nynorsk entry with the
macrolanguage code `no` instead of `nn`, so those pronunciations are
scraped into `nor_latn_broad.tsv` rather than `nno_latn_broad.tsv`.

In a 200-word random sample of that file's headwords, 166 carry their
`{{IPA|no|…}}` line under a `==Norwegian Nynorsk==` section, 24 under
`==Norwegian Bokmål==`, 2 under both, and 2 under the legacy
`==Norwegian==` heading; 4 no longer carry a `no`-tagged template at all.
The file is Nynorsk with a Bokmål minority of roughly one word in eight,
and it is scored against the `nn` spec.

It stays a row of its own rather than being folded into `wikipron`/`nn`,
because it is a separate file with its own annotator pool and its own
Bokmål contamination. Merging the two would let each hide the other: the
contamination would vanish into a larger denominator, and a movement on
either file would become unattributable.

Additional wired languages: all from `data/scrape/tsv/` on the
[CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron) GitHub
repository, same CC-BY-SA provenance:

| o2ipa tag | WikiPron file | ~rows | Notes |
|---|---|---:|---|
| `it` | `ita_latn_broad.tsv` | 89 608 | Italian. Large it.wiktionary community |
| `fr` | `fra_latn_broad.tsv` | 97 652 | French. Large fr.wiktionary community |
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
| `ru` | `rus_cyrl_narrow.tsv` | ~large | Russian (Cyrillic). **Narrow, not broad**: see note below. |
| `ar` | `ara_arab_broad.tsv` | 17 563 | Modern Standard Arabic (Arabic script, WikiPron's `ara` macro-language code). Entries come from Wiktionary's fully-vocalized (tashkeel-marked) headwords, matching the `ar` spec's documented tashkeel-dependent input contract (see the spec's `notes` field). |

Broad-mode normalization (`normalize(..., broad=True)`, the harness
default) folds narrow place-of-articulation diacritics: dental (U+032A
̪), apical (U+033A ̺), and laminal (U+033C ̼): along with the other
marks in `_NARROW_MARKS`, so e.g. an apico-alveolar `[s̺]`/`[z̺]` scores
identically to plain `[s]`/`[z]` against a gold set that only writes the
latter. This keeps dialects that transcribe articulatory place detail
(e.g. Mirandese, and the pt-PT-x-trasosmontes/viana/minho/beira/aveiro/
alfena dialects) from being penalized per-sibilant for detail that broad
transcription conventions never encode in the first place. Narrow mode
(`--narrow`) does not fold these marks.

Russian has no `_broad.tsv` in `data/scrape/tsv/`. Upstream's own README
states some languages were only scraped in one transcription width
("some languages only have broad or narrow transcriptions, e.g. Russian
only has the latter"), and for Russian that is narrow. The harness's
default (non-`--narrow`) normalization already strips narrow-transcription
diacritics (`_NARROW_MARKS`) before scoring, so `rus_cyrl_narrow.tsv` is
directly comparable to the broad-tier gold used for the other languages
in this table. It is wired despite shipping only as a narrow file, with no
documented quality concern excluding it.

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
dialectos galego-portugueses", Boletim de Filologia 22:81-116.
Provenance: sentence-level gold produced by the same team that maintains
the dialect specs. Pending external peer validation.

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
higher than the lexicon benchmarks. It measures how well the engine
captures dialect-specific grapheme-to-phoneme rules, not connected-speech
phonology.

### CLUP dialect archive gold set (`clup_dialect`)

[TigreGotico/ArquivoDialetalCLUP_ipa](https://huggingface.co/datasets/TigreGotico/ArquivoDialetalCLUP_ipa)
on Hugging Face: 68 sentence-level rows (66 mapped, see below), IPA
transcriptions of interview excerpts from the
[Arquivo Dialetal](https://cl.up.pt/arquivo/) of the Centro de
Linguística da Universidade do Porto (CLUP). Each row carries a
`"<locality>, <district>"` region label. Rows are grouped to an
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
on Hugging Face: ~220 word/IPA rows with a `dialect` column, collected by
a native Mirandese speaker
([MdMV](https://commons.wikimedia.org/wiki/User:MdMV_or_Emdy_idk)).
Registered as the row id `mirandese_g2p` and split by that column:
`central` → `mwl` (the Central norm the Mirandese orthography is built on),
`sendinese` → `mwl-x-sendim` (the Sendim sub-dialect), and `raiano` →
`mwl-x-ifanes` (the Raiano/Northern sub-dialect, whose Ifanês variety this
repo tags `mwl-x-ifanes`). Native-speaker provenance makes this the
reference gold and the most trustworthy signal for Mirandese: distinct
from, and more reliable than, any machine-generated Mirandese IPA
dictionary. Its size (especially `mwl-x-ifanes`, `N≈2`) keeps results
indicative rather than statistical: read the confidence interval.

### Barranquenho synthetic IPA dictionary (`barranquenho_dict`)

[TigreGotico/barranquenho-ipa-dict-synthetic](https://huggingface.co/datasets/TigreGotico/barranquenho-ipa-dict-synthetic)
on Hugging Face: 319 word/IPA entries for Barranquenho: the
Portuguese-Spanish contact variety of Barrancos: mapped to the
`ext-PT-x-barrancos` spec. Each row also carries part-of-speech, the
Portuguese and Spanish equivalents, and a phonological note. Only the
orthography and IPA columns are scored (Barranquenho is Latin-script, so
no special input contract applies).

**Provenance: read this before trusting the number.** The IPA was
**generated by a large language model (Claude)** conditioned on the
published *Convenção Ortográfica do Barranquenho* and descriptive research
on the variety. It was **not** produced by a phonemizer, by
orthography2ipa, or by any downstream o2i consumer, so scoring o2i against
it is **not circular**: but it is unverified by human phoneticians and
can be plausibly wrong. It sits at the lowest (`machine-generated`)
reliability tier and is **directional only**. Disagreements are a prompt
to check real sources, never a licence to tune the spec toward the gold.

### Mirandese synthetic IPA dictionary (`mirandese_dict`)

[TigreGotico/mirandese-ipa-dict-synthetic](https://huggingface.co/datasets/TigreGotico/mirandese-ipa-dict-synthetic)
on Hugging Face: 671 word/IPA entries for Mirandese, each tagged with a
`dialect` column. This is a **separate, complementary** source from the
native-speaker `mirandese` gold above. Rows are split by dialect to the
matching spec (each row scored under exactly one tag):

| `dialect` value | orthography2ipa tag | Notes |
|---|---|---|
| `central`, `all` | `mwl` | Central norm the orthography is built on. `all` = forms shared by every variety |
| `sendinês` | `mwl-x-sendim` | Southern Sendinês |
| `raiano` | `mwl-x-ifanes` | Ifanês **is** the Northern/Raiano subdialect in this repo's spec set (only 4 rows: read the CI, not the point PER) |

**Provenance: read this before trusting the number.** As with
`barranquenho_dict`, the IPA was **generated by a large language model
(Claude)** conditioned on the *Convenção Ortográfica da Língua Mirandesa*
and descriptive sub-dialect research: **not** by a phonemizer, by
orthography2ipa, or by any downstream o2i consumer (so **not circular**),
but unverified by human phoneticians and possibly wrong. Lowest
(`machine-generated`) tier, **directional only**. Disagreements point to
real-source investigation, never spec tuning toward the gold.

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
| `Projecte BSC frases - Nord-Occ.tsv` | `ca-x-occidental` | Northwestern/Lleidatà: **not** `ca-x-nord` (Northern Catalan/Rossellonès, a distinct dialect spoken in France that 4catac does not cover) |
| `Projecte BSC frases - Val.tsv` | `ca-x-valencia` | Valencian |

Sentences were "intentionally written to showcase various phonetic
phenomena" across the four accents, so this is a targeted, curated
gold set rather than a random sample. Because the gold is
sentence-level, PER reflects connected-speech phonology on top of
grapheme-to-phoneme rules, so it is naturally higher than the
lexicon-style benchmarks. No rows are excluded.

### ipa-dict pronunciation dictionaries (`ipadict`)

[open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict):
31 open pronunciation dictionaries in `word TAB /IPA/` format (a word with
several attested pronunciations lists them comma-separated, `est  /ɛst/,
/ɛ/`, the loader emits each variant as its own gold pair, and the scorer
keeps the best-matching one). The project is MIT-licensed. Each
third-party dataset keeps its own licence.

**Read the tier before the number.** ipa-dict is not one source. Its
README Credits section: the only authority on where each file's IPA came
from: shows it mixing published human dictionaries, Wiktionary scrapes,
rule scripts and phonemizer output in a single repository, so this dataset
is classified **per language** (`_IPADICT_PROVENANCE` in
`scripts/benchmark.py`, surfaced per row by `provenance_for`). The
notorious case is **`en_UK`, which is espeak output**: it is credited to
[ipacards](https://github.com/leoboiko/ipacards), whose own `CREDITS` and
`bin/add-ipa-to-freq.py` shell out to `espeak`. That row measures agreement
with a competitor, so per [quality tiers](quality_tiers.md) it can **neither
qualify nor block** English: read the CMUdict and WikiPron English rows
instead. Where the Credits section names no source at all, the file is
classified `machine-generated` with the provenance recorded as UNVERIFIED.
a tier is never upgraded on a guess.

| Lang | ipa-dict file | Tier | Source (per the ipa-dict README Credits) |
|---|---|---|---|
| `is` | `is.txt` | lexicon-derived | [Pronunciation Dictionary for Icelandic](http://malfong.is/?pg=framburdur&lang=en) (Hjal project, malfong.is), CC BY 3.0: human-curated by Icelandic linguists. Higher coverage (~60k) than WikiPron `isl` (~11k): the primary Icelandic gold, with WikiPron as cross-check. |
| `en-US` | `en_US.txt` | lexicon-derived | [cmudict-ipa](https://github.com/lingz/cmudict-ipa) (CMU hand-curated ARPABET) + [syllabify](https://github.com/kylebgorman/syllabify) stress, MIT. Same lineage as the `cmudict` row, different notation transform. |
| `ja` | `ja.txt` | lexicon-derived | [EDICT](https://www.edrdg.org/jmdict/edict.html) readings (EDRDG), CC BY-SA 3.0. Only the kana entries score: kanji headwords transcribe to `''` and drop out of `N`. |
| `jam` | `jam.txt` | lexicon-derived | [A Learner's Grammar of Jamaican](https://github.com/opengrammar/jam-learners-grammar) (Open Grammar Project), CC BY 4.0. |
| `km` | `km.txt` | lexicon-derived | [Khmer-English Dictionary](https://www.aakanee.com/AC-Khmer/X/dict.html) (aakanee.com), CC BY-NC-SA 4.0. |
| `ro-RO` | `ro.txt` | lexicon-derived | [MaRePhoR](https://speech.utcluj.ro/marephor/) phonetic dictionary (UTCluj), CC BY-NC. |
| `sv` | `sv.txt` | lexicon-derived | [Folkets lexikon](https://folkets-lexikon.csc.kth.se/folkets/) (KTH), CC BY-SA 2.5. |
| `de-DE` | `de.txt` | crowd-scraped | [german-ipa-dict](https://github.com/devio-at/german-ipa-dict), built from Wiktionary, CC BY-SA. |
| `ar` | `ar.txt` | machine-generated | Tim Buckwalter's Arabic Morphological Analyzer output. |
| `es-ES` | `es_ES.txt` | machine-generated | [spanish-pronunciation-rules](https://github.com/easypronunciation/spanish-pronunciation-rules-php) PHP script. README calls it "experimental". |
| `es-MX` | `es_MX.txt` | machine-generated | Same script. The file is near-identical to `es_ES` (the two differ by ~11 lines), so the two rows are not independent evidence. |
| `fa` | `fa.txt` | machine-generated | Wiktionary + [PersPred](http://perspred.cnrs.fr/perspred-project) + "a great deal of guesswork". README: "extremely experimental". |
| `fi` | `fi.txt` | machine-generated | [prosodic1b](https://github.com/jsfalk/prosodic1b) (rule-based) over the Kotus wordlist, GPL 2.0. |
| `nl` | `nl.txt` | machine-generated | Instituut voor de Nederlandse Taal, CC BY: README: "an automated conversion from different data sources … no manual correction or revision has been done". |
| `or` | `or.txt` | machine-generated | [OdiaWikimedia Converter](https://github.com/OdiaWikimedia/Converter/tree/master/IPA-Romanization) over Wikimedia dumps. |
| `vi` | `vi_N.txt` | machine-generated | [vPhon](https://github.com/kirbyj/vPhon) converter over Ho Ngoc Duc's wordlist. Northern/Hanoi = the standard the `vi` spec targets. |
| `nb` | `nb.txt` | machine-generated | Base generation method **undocumented**. The README credits Dr. Espen Stranger-Johannessen for *correcting and updating* it, which is not evidence of expert authorship: so the tier is not upgraded. |
| `eo` | `eo.txt` | machine-generated | **PROVENANCE UNVERIFIED**: the Credits section names no source for Esperanto. |
| `fr-FR` | `fr_FR.txt` | machine-generated | **PROVENANCE UNVERIFIED**: no source credited for French. |
| `ms` | `ma.txt` | machine-generated | **PROVENANCE UNVERIFIED**: no source credited. ipa-dict's `ma` is "Malay (Malaysian and Indonesian)", i.e. the `ms` spec, *not* Moroccan Arabic. |
| `pt-BR` | `pt_BR.txt` | machine-generated | **PROVENANCE UNVERIFIED**: no source credited for Brazilian Portuguese. |
| `sw` | `sw.txt` | machine-generated | **PROVENANCE UNVERIFIED**: no source credited for Swahili (the entries even preserve capitalisation in the IPA, e.g. `Abadoni /Aɓaɗoni/`). |
| `en-GB` | `en_UK.txt` | **espeak-derived** | [ipacards](https://github.com/leoboiko/ipacards) (GPL 3.0), whose CREDITS list "Espeak" and whose `bin/add-ipa-to-freq.py` calls `espeak` directly. **Cannot qualify or block English.** |

Files deliberately **not** wired (recorded in `_IPADICT_UNWIRED`):

| File | Why not |
|---|---|
| `zh_hans`, `zh_hant` | Han-script gold, and no spec can read it: `zh` is a **pinyin/romanization** spec (`OrthographyKind.ROMANIZATION`), and the Han-script `zh-Hani` spec emits nothing for Han characters (`G2P("zh-Hani").transcribe_word("一") == ""`). Forcing either would produce a `PER=1.0`, `N=0` non-result. The two files carry identical pronunciations anyway (they differ only in written standard). |
| `yue` | Same: Han-script gold, and `G2P("yue")` emits nothing for it. The gold itself (KFCD Pingyam + 開放粵語詞典, CC BY 3.0) is good: the gap is on our side. |
| `ko` | Same: Hangul gold (Korean Wiktionary via [korean-word-ipa-dictionary](https://github.com/laviande22/korean-word-ipa-dictionary), CC BY-SA), and `G2P("ko")` emits nothing for Hangul syllable blocks. |
| `fr_QC` | No Québécois spec is registered. The file is also qc-ipa script output over `fr_FR` ("highly experimental"). |
| `tts` | Isan / Northeastern Thai ([Isaan-English Dictionary](https://www.aakanee.com/AC-Isaan/X/dict.html), CC BY-NC-SA 4.0). No `tts` spec. The `th` spec is a different language and must not stand in for it. |
| `vi_C`, `vi_S` | No Central/Southern Vietnamese specs (only `vi`). |

The Han/Hangul rows above are an **engine/spec gap, not a gold problem**:
those three golds are among the better-sourced files in the project and are
ready to wire the moment the logographic/Hangul orthographies are readable.
Odia (`or`) is scorable but is an **abugida**, so its number should be read
against the state of the abugida handling, not as a verdict on the `or`
spec.

### HiTZ Basque Wikipedia IPA corpus (`hitz_basque_ipa`)

[HiTZ/wikipedia_basque_ipa](https://huggingface.co/datasets/HiTZ/wikipedia_basque_ipa)
on Hugging Face: ~1,672,981 paragraph-level `text`/`phonemes` rows
extracted from the Basque Wikipedia dump, published by
**HiTZ Zentroa / AhoLab**, the University of the Basque Country
(UPV/EHU)'s NLP research group. IPA is produced by **ahoNT**, HiTZ's
Basque text-processing and phonemization tool: i.e. this is
tool-generated IPA, not human-annotated.

Per the provenance-discipline rule above, tool-generated IPA is normally
excluded from this benchmark. This dataset is an **explicit,
dataset-specific exception**: the user directed that datasets published
by universities/academic NLP research centers count as legitimate gold
sources for this benchmark even when the IPA came from an automatic
tool, specifically because the publishing body (HiTZ) is an established
academic research group, not because the "human vs. tool" line has been
generally relaxed. This exception applies only to this dataset. It does
not license adding other automatically-phonemized sources without a
similar explicit call.

Wired as `eu` under the `hitz_basque_ipa` dataset key, **additive** to
the existing `wikipron` `eu` entry (Wiktionary-sourced, community
provenance): it does not replace or reduce that coverage.

Because the source data is paragraph-level rather than word-level, the
loader (`load_hitz_basque` in `scripts/benchmark.py`) pages the dataset
through the Hugging Face datasets-server `rows` REST API (never
downloading the full parquet), whitespace-tokenizes each paragraph's
`text` and `phonemes` in lockstep (ahoNT emits one phoneme token per
source word, punctuation attached to the token, per the dataset card),
pairs tokens positionally, strips surrounding punctuation from both
sides, and collects deduplicated single-word pairs. This loader carries an
intrinsic, language-agnostic bound that `--limit` cannot lift: it stops
after `_HITZ_BASQUE_MAX_PARAGRAPHS` (500) paginated paragraphs rather than
pulling the full 1.67M-row set, so even the full `--scoreboard` run scores
the word pairs harvested from those first 500 paragraphs, not the entire
corpus. This is the one dataset that remains bounded under the full
scoreboard, and it is bounded by paging infrastructure (uniformly, not
per language), not by a sampling `--limit`. Single word-tokens are used as
the scored unit: following `load_ep_dialects`'s precedent of scoring non-lexicon-shaped
gold through the harness's standard `transcribe_word`/PER pipeline: rather than whole sentences, since paragraph-level ahoNT stress
placement is not verified to depend on sentence context, making the
single-token span the more conservative unit to score in isolation.

### VoxCommunis parallel G2P (`vox_communis`)

[fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)
(CC0): Common Voice utterances force-aligned by the VoxCommunis Corpus,
with per-utterance phone strings whose lexicons were built with **Epitran,
the XPF Corpus, Charsiu and custom dictionaries** (partially hand-corrected
by VoxCommunis, but not attributably per row). One small TSV per language.
69 language tags are wired (every per-language file with a matching spec,
plus a few regionalised aliases: `sv-se`→`sv`, `hy-am`→`hy`,
`fy-nl`→`fy`, `pa-in`→`pa`, and the region-untagged `pt` file under `pt-BR`,
the same policy as the WikiPron generic-pt row). `zh-cn` and `yue` are
deliberately **not** wired — see [Rejected candidates](#rejected-candidates).

The `phonemized_sentence` column is space-separated phones with `|` between
words, aligned with the whitespace-tokenized `aligned_sentence`. Rows are
split into word-level pairs like `ipa_childes`, skipping token-count
mismatches and stripping alignment artifacts.

**`spn` tokens are dropped, not scored.** `spn` is the Montreal Forced
Aligner's "spoken noise" symbol, which the VoxCommunis pipeline reuses for
any word its lexicon could not cover: the phone tier records the literal
string `spn` in place of that word's phones. It is a coverage-hole marker,
not a transcription, and the error from scoring it is **unbounded**, not
simply noisy. PER normalises by the *gold* length, so one real 10-segment
word scored against a 3-character `spn` contributes a per-word PER above 3. Whole
languages were pushed past PER 1.0 by this alone. Share of `spn` tokens in
the affected files: `kk` 59.4%, `ab` 46.5%, `cv` 31.3%,
`ba` 15.1%, `it` 12.5%, `sr` 9.6%, `es` 2.9%, `ca` 2.1%.

`spn` is the **only** token filtered. The obvious siblings (`sil`, `sp`,
`nsn`, `noise`) do occur, but overwhelmingly as *genuine transcriptions of
real words* — Welsh `sul` → /sil/ (336 rows), Amharic `ሲል`, Bulgarian
`сп`, Tamil `ஸ்ப்`, Korean `실`, Punjabi `ਸੀਲ` — so filtering on the phone
string would delete real gold. A further 61 rows across seven files carry
the marker on both tiers (word `sil` → phones `sil`), which does look like
an aligner placeholder leaking into the orthography; those are left in as
well, because the identity test is not safe either — Turkish `sil`
("wipe") is a real word genuinely pronounced [sil]. 61 rows out of ~2.6M
is far below the noise floor of an `epitran-derived` row.

**The remaining high rows are notation, not phonology.** With `spn` gone,
`vi`, `pa` and `as` still sit above PER 0.5 (board values 0.5596, 0.6607
and 0.6445 — see [languages/vi.md](languages/vi.md)), and in all three the
distance is a transcription convention rather than a phonological
disagreement: `vi` differs by tone-letter placement, vowel-length marking
and a handful of symbol variants; `pa` by length marking and a small set
of vowel/rhotic symbol choices, plus final-schwa deletion; `as` by length
marking, a similar symbol-choice set, and final-ɔ deletion. For `vi` the
folding is reproduced by `scripts/fold_vi_notation.py`, which removes one
convention at a time from both sides and re-scores with the harness's own
`normalize()`: 0.5596 as scored, 0.3277 without tone letters, 0.0398 once
vowel length, the unreleased-stop mark, ⟨ɨ⟩~⟨ɯ⟩ and the ⟨ă ɤ̆⟩ short-vowel
notation are folded too, and 0.0246 once the palatal/pre-velar reading of
the ⟨nh ch⟩ finals is folded as well. The `pa` and `as` foldings have no
committed script and are not stated as numbers. None of these foldings
belong in `normalize()` — it is the single scorer for every row, and
tone-letter placement in particular is language-specific — so the rows
stay as scored and are read with this offset in mind.

The `vi` gold is also wrong in one respect rather than merely different:
its tone tier writes one letter, ˨˨, for both ngang and huyền —
contrastive tones, tabulated separately by Kirby (2011: 386) on the
minimal pair *ma* 'ghost' / *mà* 'but' — on 967 of the row's 2 475 words
(39.1%). The dataset-wide `epitran-derived` tier already keeps that out of
every gating decision, so the finding is recorded in prose (here and in
[languages/vi.md](languages/vi.md)) rather than as a per-language
override. Reclassifying the row would in fact be counterproductive:
`NON_QUALIFYING_TIERS` contains `epitran-derived` but not
`machine-generated`, so moving the row to the tier that sits *higher* in
the ordered `RELIABILITY_TIERS` tuple would hand it a gating vote. Gating
is set membership, not tuple position.

**Known upstream contamination, `sr`.** 35.8% of Serbian tokens carry a
spurious word-initial `z` in the Charsiu-derived phone tier (`не` →
`znɛ`, `и` → `zi`, `а` → `za`). It is never doubled on words that
genuinely start with `з`, so it is an upstream lexicon artifact, not a
transcription convention. It is *not* filtered — there is no way to
distinguish it from a real word-initial /z/ without guessing — and it
inflates the `sr` row by roughly 0.04 PER (0.3298 → 0.2949 with the artifact
removed by hand). Read the `sr` vox_communis row with that offset in mind.

**Known coverage hole, `ba`.** The Bashkir gold cannot see the two letters
that define Bashkir. `ba.tsv` holds 209,210 sentence rows, and 188,980 of
its word tokens are spelled with ⟨ҙ⟩ or ⟨ҫ⟩ — the interdentals /ð/ and /θ/
that separate Bashkir from Tatar. Every one of those 188,980 tokens is
emitted as `spn` by the upstream phonemizer, which has no mapping for
either letter, so every one of them is dropped by the `spn` filter above.
What survives is 70,528 unique words with zero ⟨ҙ⟩ and zero ⟨ҫ⟩ in them.
The row is therefore not a sample of Bashkir but a sample of the Bashkir
that Epitran happens to cover, and no score on it can reward or punish the
spec's /ð/ and /θ/ rules. The row is kept because it still measures the
rest of the alphabet across a large vocabulary; it is read as breadth
only, and the interdentals are defended by `wikipron` and by unit tests.

**Known coverage hole, `ab` (Abkhaz): the gold has no symbol for
labialization, and Abkhaz is built on it.** Abkhaz contrasts roughly 58
consonants against two vowels, largely by palatalizing and labializing
almost every place of articulation (Beguš 2021,
[doi:10.1093/oxfordhb/9780190690694.013.18](https://doi.org/10.1093/oxfordhb/9780190690694.013.18),
§2.2.1). The orthography writes labialization with the modifier letter
⟨ә⟩ U+04D9. In `ab.tsv`, 44,279 of 76,464 word types (57.9%) are `spn`
rather than a transcription, and eight letters are at **100%** `spn` — ⟨ә⟩
(30,743 types), ⟨ԥ⟩ (7,984), ⟨қ⟩ (7,058), ⟨ӡ⟩ (5,024), ⟨ҩ⟩ (4,035), ⟨ҿ⟩
(2,678), ⟨ӷ⟩ (1,741), ⟨џ⟩ (811). So every labialized spelling is a coverage
hole, and the 32,185 scoreable types between them use only 35 distinct
phone symbols, not one of which carries /ʷ/. What survives is a sample of
the labialization-free residue of Abkhaz.

Most of the remaining distance is transcription convention, not mapping.
Folding the gold's undotted ⟨ш ж ҽ ҿ⟩ series onto the spec's retroflex
symbols removes 1.7 PER points, dropping the aspiration the gold never
writes removes 3.0, and reading ⟨е о и у⟩ as the gold's underlying
/aj aw j w/ instead of surface /e o i u/ removes a further 8.3 — leaving
about 6.5 points of real disagreement out of a raw 45.2. The spec keeps
aspiration and the retroflex series: the JIPA Illustration of Abkhaz
transcribes the language's own name /apʰsaʃʷa/
([doi:10.1017/S0025100320000390](https://doi.org/10.1017/S0025100320000390)),
and the independent `wikipron` `ab` row marks aspiration too.

This row is **not** given a `PROVENANCE_BY_LANG` override, deliberately.
The tier lattice has no rung below a competitor's output:
`machine-generated` reads as the weakest tier in the table above but is a
*qualifying* one, while `epitran-derived` is not, so overriding `ab` down
to `machine-generated` would hand a gating vote to the least trustworthy
row on the board. The dataset-wide tier stays, and the row stays
non-qualifying. (The `epitran` half of the label is also not literally true
here — Epitran ships no Abkhaz map — so the ab phone tier came from XPF,
Charsiu or a custom lexicon, unattributed.)

**Tier: `epitran-derived`**: Epitran is a scored competitor in
[comparison.md](comparison.md), so a disagreement here measures divergence
from a competitor's output. Directional breadth signal only. Can never gate
a regression or qualify a spec for the production tier.

**Known coverage hole, `gn` (Guaraní): the gold cannot write two of the
phonemes it is scored on.** Of the 4,264 `vox_communis` `gn` words, 1,353
contain the letter ⟨m⟩, and not one of them has a plain [m] in the gold:
Guaraní prenasalizes ⟨m⟩ and ⟨n⟩ before an oral vowel (`retãme` →
`ɾetãᵐbe`, `mba'épiko` → `ᵐbaʔepiko`), and the upstream phonemizer only
ever emits the prenasalized cluster, never the plain nasal. Separately, of
503 words containing ⟨ñ⟩, the gold writes [ɲ] in zero of them — it writes
[dʒ] in all 503, the same value it assigns to plain ⟨j⟩ (also [dʒ] in all
740 of the words that contain that letter), so the gold cannot
distinguish ⟨ñ⟩ from ⟨j⟩ at all. `wikipron`'s much smaller `gn` row does
not share either gap (69 of 85 ⟨m⟩-words keep [m], 32 of 34 ⟨ñ⟩-words
keep [ɲ]), so this is a property of this specific gold's phonemizer, not
of Guaraní. A spec that writes plain [m] and [ɲ] where the orthography
calls for them will never match this gold on those words, no matter how
the rest of the spec is written.

The German and Guaraní cases are the same failure mode at different
scales: before treating a `machine-generated`, `espeak-derived` or
`epitran-derived` row as something to close the gap on, count how often
the gold ever writes the phoneme a spec is emitting. A segment the gold
writes in a nontrivial share of the words where it belongs is a real
target. A segment the gold never writes at all, no matter how often the
orthography calls for it, is a ceiling contributed by the tool that
produced the gold, and no amount of tuning the spec will close it.

### VoxCommunis with the Vietnamese tone merge repaired (`vox_communis_corrected`)

The Vietnamese phone tier merges two contrastive tones. It writes the identical
Chao tone letter ˨˨ for both *ngang* (A1, the unmarked tone) and *huyền* (A2),
which Kirby's Illustration of the IPA tabulates as separate categories on the
classic minimal pair ⟨ma⟩ 'ghost' (ngang, "level") against ⟨mà⟩ 'but, yet'
(huyền, "mid falling"):

> Kirby, James P. (2011). Vietnamese (Hanoi Vietnamese). *Journal of the
> International Phonetic Association* 41(3): 381–392, tone table p. 386.
> <https://doi.org/10.1017/S0025100311000181>

Measured over the full 2475-pair row: 566 of 590 ngang tokens and 401 of 406
huyền tokens carry a tone-letter sequence of exactly ˨˨ — 39% of the row spelled
with one symbol for two phonemes.

The repair is derivable from spelling alone, which is what makes it admissible.
Vietnamese orthography writes huyền with a combining grave accent (⟨à è ì ò ù
ỳ⟩ and their circumflex, breve and horn variants) and writes ngang with no tone
mark at all, so which of the two merged tones a syllable carries is recoverable
from the Unicode combining marks with no phonological model in the loop. The
overlay rewrites the 401 grave-accented readings to ˧˩: Kirby prints tone
letters rather than Chao digits and labels huyền "mid falling" against hỏi's
"low falling", so huyền must begin above hỏi, which this gold writes ˨˩˨.

Left uncorrected and counted: 5 huyền tokens whose reading is not a single ˨˨
(multi-syllable readings, where no single tone letter is the merged one), and 2
tokens carrying two tone marks, whose tone cannot be read from the spelling at
all. The 566 merged ngang tokens are *not* corrected either — ˨˨ is what this
gold writes for ngang, and no citation makes it wrong within this gold's own
scale.

Correcting the merge does **not** move PER, and that is worth knowing: both
rows score 0.5596 over 2475 pairs, and 0.5716 over the 401 corrected pairs
alone. The engine writes huyền ˧˨, which is one substitution away from the
merged ˨˨ and one substitution away from the corrected ˧˩, so the repair is
edit-distance-equivalent. PER is simply blind to this defect. Writing the
engine's own ˧˨ into the gold instead would drop those 401 rows to PER 0.4048
and the whole row to 0.5325 — a 3-point gain bought by copying the answer, and
the exact reason the derivation rule exists.

### IPA-CHILDES split (`ipa_childes`)

[fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)
on Hugging Face: a postprocessed version of IPA-CHILDES, the phonemized
CHILDES child-language corpus (CC BY 4.0), split into per-language
`train`/`test` CSVs (28 languages, `test` split ranging from ~460k to
~74MB per language, 256,462 test rows for `en-US`). Each row is a
sentence-level utterance with several IPA columns. This harness uses
`ipa_g2p_plus` (the "G2P+" phonemizer column), which the dataset
publishes pipe-(" | ")-delimited with one segment per orthographic word,
aligned positionally with the whitespace-tokenized orthographic sentence.
Per the CHILDES/academic-corpus exception, tool-generated transcriptions
from this dataset are accepted as gold here: but **which** tool matters,
and it is not the same tool for every language.

#### Provenance: one tool per language, and every one of them is a competitor

The [IPA-CHILDES dataset card](https://huggingface.co/datasets/phonemetransformers/IPA-CHILDES)
states the phonemizing tool per language in its own table. Most languages
were run through `phonemizer` (whose backend is **espeak-ng**), six through
**epitran**, Mandarin through `pinyin_to_ipa` and Cantonese through
`pingyam`. espeak and epitran are *both* systems this project benchmarks
itself against ([comparison](comparison.md) has `espeak_per` and
`epitran_per` columns), so an IPA-CHILDES row measures **agreement with a
competitor**, not correctness. Every row is therefore tiered by its own
tool (`_IPA_CHILDES_TOOL` → `_IPA_CHILDES_PROVENANCE` in
`scripts/benchmark.py`, mechanically, with a test enforcing the mapping),
and none of the espeak/epitran rows can qualify or block a language for
`production` ([quality tiers](quality_tiers.md)).

| Language tag | Dataset folder | Tool (dataset card) | Tier | `N` | PER |
|---|---|---|---|---|---|
| `ca` | `ca-ES` | `phonemizer` (espeak-ng), `ca` | espeak-derived | 3814 | 0.3223 |
| `cy` | `cy-GB` | `phonemizer` (espeak-ng), `cy` | espeak-derived | 4666 | 0.3009 |
| `da` | `da-DK` | `phonemizer` (espeak-ng), `da` | espeak-derived | 2233 | 0.5170 |
| `de-DE` | `de-DE` | `epitran`, `deu-Latn` | epitran-derived | 24857 | 0.3948 |
| `en-GB` | `en-GB` | `phonemizer` (espeak-ng), `en-gb` | espeak-derived | 11447 | 0.3864 |
| `en-US` | `en-US` | `phonemizer` (espeak-ng), `en-us` | espeak-derived | 18055 | 0.4296 |
| `es-ES` | `es-ES` | `epitran`, `spa-Latn` | epitran-derived | 13155 | 0.0945 |
| `et` | `et-EE` | `phonemizer` (espeak-ng), `et` | espeak-derived | 11041 | 0.2953 |
| `eu` | `eu-ES` | `phonemizer` (espeak-ng), `eu` | espeak-derived | 3969 | 0.1297 |
| `fr-FR` | `fr-FR` | `phonemizer` (espeak-ng), `fr-fr` | espeak-derived | 9465 | 0.1966 |
| `ga` | `ga-IE` | `phonemizer` (espeak-ng), `ga` | espeak-derived | 1612 | 0.4406 |
| `hr` | `hr-HR` | `epitran`, `hrv-Latn` | epitran-derived | 4770 | 0.2066 |
| `hu` | `hu-HU` | `epitran`, `hun-Latn` | epitran-derived | 4781 | 0.1331 |
| `id` | `id-ID` | `epitran`, `ind-Latn` | epitran-derived | 9647 | 0.1223 |
| `is` | `is-IS` | `phonemizer` (espeak-ng), `is` | espeak-derived | 4106 | 0.3935 |
| `it-IT` | `it-IT` | `phonemizer` (espeak-ng), `it` | espeak-derived | 4584 | 0.2599 |
| `nb` | `nb-NO` | `phonemizer` (espeak-ng), `nb` | espeak-derived | 3176 | 0.4633 |
| `nl` | `nl-NL` | `phonemizer` (espeak-ng), `nl` | espeak-derived | 8108 | 0.3459 |
| `pl` | `pl-PL` | `phonemizer` (espeak-ng), `pl` | espeak-derived | 15524 | 0.3063 |
| `pt-BR` | `pt-BR` | `phonemizer` (espeak-ng), `pt-br` | espeak-derived | 2117 | 0.2536 |
| `pt-PT` | `pt-PT` | `phonemizer` (espeak-ng), `pt` | espeak-derived | 3846 | 0.2449 |
| `qu` | `qu-PE` | `phonemizer` (espeak-ng), `qu` | espeak-derived | 1855 | 0.4421 |
| `ro-RO` | `ro-RO` | `phonemizer` (espeak-ng), `ro` | espeak-derived | 2312 | 0.2647 |
| `sr` | `sr-RS` | `epitran`, `srp-Latn` | epitran-derived | 9838 | 0.4244 |
| `sv` | `sv-SE` | `phonemizer` (espeak-ng), `sv` | espeak-derived | 5202 | 0.4482 |
| `tr` | `tr-TR` | `phonemizer` (espeak-ng), `tr` | espeak-derived | 2748 | 0.1374 |
| `zh` | `zh-CN` | `pinyin_to_ipa`, `mandarin` | machine-generated | 4718 | 0.5167 |

Mandarin's `pinyin_to_ipa` is a deterministic Pinyin→IPA table rather than a
G2P system we compete with, so it is `machine-generated`, not
competitor-derived: but it is still a tool's output and still cannot be
read as truth. The Mandarin row is also read through the tokenizer that
[#305](https://github.com/TigreGotico/orthography2ipa/pull/305) reworks for
Han/punctuation input, so its number on this branch may move.

Only the `test` split is read (held out from G2P+ training). The loader (`load_ipa_childes` in
`scripts/benchmark.py`) splits each row's orthographic sentence and its
`ipa_g2p_plus` column on whitespace/`" | "` respectively, pairs tokens
positionally, skips rows whose token counts don't line up, and collects
deduplicated single-word pairs (the full `--scoreboard` run reads the whole
test split, `--limit N` keeps only the first N): the same
positional-alignment technique `load_hitz_basque` uses for paragraph-level
gold, applied here to dataset-native sentence-level alignment instead of
manual tokenization.

`zh` is read from the dataset's `stem` column rather than its `sentence`
column: `sentence` is Hanzi, but this repo's `zh` spec models **Pinyin**
syllables (its grapheme table is Pinyin initials/finals, not Hanzi), and
`stem` is CHILDES's own Pinyin-with-tone-number romanization of the same
utterance: the column that actually exercises the spec's grapheme table.

`ko-KR` is present in the dataset but **excluded** here, for the same
class of script/input-contract mismatch as the `zh` exclusion below:
this repo's `ko` spec's grapheme table is keyed on individual
compatibility jamo (`ㄱ`, `ㄲ`, `ㄷ`, ...), while real Korean text: including this dataset's: is precomposed Hangul syllable blocks (e.g.
`아홉`), which neither match the compatibility-jamo graphemes directly
nor decompose into them under NFD (NFD splits a Hangul syllable into
*conjoining* jamo, a different Unicode block from the *compatibility*
jamo the spec's grapheme table uses). `G2P('ko').transcribe_word(...)`
returns an empty string for every real Hangul word tested, so scoring
this row would not measure phonological accuracy: it is a
script/input-contract mismatch between the dataset and this repo's
`ko` spec, not a gap in the engine's Korean coverage. Bridging
compatibility jamo and precomposed Hangul is a real engine-level
enhancement that this row does not wait on.

Present in the dataset but **not** wired in:

- **`fa-IR`** (Persian): this corpus's Persian transcripts are Fingilish
  (ad hoc Latin transliteration, e.g. `"piano kar kardam"`), never Persian
  script. The `fa` spec here is Arabic-script only, so there is no clean
  grapheme match.
- **`ja-JP`** (Japanese): this corpus's Japanese transcripts are romaji
  only: the dataset has no kana/kanji column for Japanese: while the
  `ja` spec here has a hiragana grapheme table, so there is no clean
  grapheme match either.
- **`yue-CN`** (Cantonese): the `yue` spec is a stub with an **empty
  grapheme inventory** (Cantonese is written in Chinese characters, and the
  stub claims no letter-to-sound mapping). The dataset's own romanized
  column is Jyutping-with-tone-numbers, which the stub does not model
  either, so `G2P('yue').transcribe_word(...)` returns `""` for every row.
  A spec gap, not a gold problem.

#### German (`de-DE`): the epitran row measures a ceiling, not a defect

`de-DE`'s three `ipa_childes`-adjacent word-level golds disagree with each
other far more than a "German is mediocre" reading would suggest. Taking
the words that appear in all three of `wikipron`, `ipadict` and
`ipa_childes` (6,594 words, same engine, same broad/stress-stripped
normalization), the spec scores 0.1650 against `wikipron` and 0.1926
against `ipadict` — the two human/lexicographic golds — and 0.3993
against `ipa_childes`'s epitran output. German is not scoring worse than
its peers on this intersection; it is scoring specifically worse against
epitran, by more than double.

The reason is systematic, not diffuse. Across the 24,857 `de-DE`
`ipa_childes` words the engine covers, the epitran gold contains 588
occurrences of ə and 25 of ɐ (counting every ə/ɐ segment in the
normalized transcription, not the count of distinct words containing
one — by distinct word, ə appears in 448 of the golds), against 13,822
and 1,376 occurrences in the engine's own output — epitran's German gold
almost never writes either of German's two most common reduced-vowel
segments. Looking at where those segments belong:
of 3,755 words ending in orthographic ⟨-e⟩, the gold ends in ə exactly
twice and in ɛː or ɛ about 3,572 times — it spells the word-final schwa
as a full, often long, mid vowel instead. Of 1,437 words ending in
⟨-er⟩, it ends in ɐ zero times. Of 1,483 words ending in ⟨b⟩, ⟨d⟩ or
⟨g⟩, 1,151 keep a voiced final stop in the gold, so Auslautverhärtung
(German's word-final devoicing of obstruents) is not represented. Of 721
words with an initial ⟨Sp⟩ or ⟨St⟩, 640 are transcribed with a plain
/s/ rather than the /ʃp/, /ʃt/ that Standard German spelling pronunciation
requires. And the gold carries a length mark (ː) 37,082 times over the
same word set against the engine's 9,947. Every one of these is a
correct, standard, textbook description of German; every one of them
reads as an error against this gold, because epitran's `deu-Latn` table
does not model final-schwa reduction, the vocalized /r/, final-obstruent
devoicing, initial /ʃ/ before /p, t/, or German's own vowel-length
contrasts. Substituting just the ɛː-for-final-schwa convention into the
engine's own output (nothing else changed) drops the full-set PER from
0.3948 to 0.3618 by itself; the other four conventions each account for a
further slice of the gap. Scoring meaningfully below that residual would
mean reproducing epitran's specific omissions rather than describing
German, which is exactly what the `epitran-derived` tier
([Reliability tiers](benchmarks.md#reliability-tiers)) already warns this row can never
certify.

### IPA-BabyLM (`ipa_babylm`)

[phonemetransformers/IPA-BabyLM](https://huggingface.co/datasets/phonemetransformers/IPA-BabyLM)
on Hugging Face: the BabyLM 2024 pre-training corpora (BNC spoken, CHILDES,
Gutenberg, OpenSubtitles, Simple Wikipedia, Switchboard) converted to
phonemes with [G2P+](https://github.com/codebyzeb/g2p-plus). English only.
The two configs (`strict`, `strict-small`) differ **only** in their train
split and share one `dev` split, so there is exactly one gold set here, not
two. The harness reads the held-out `dev` split alone, never the train
portions the LMs were pre-trained on.

**Provenance: espeak, at one remove.** G2P+ is a *wrapper*: its backends
are `phonemizer` and `epitran`, and its `phonemizer` backend requires
espeak-ng. The conversion notebook that produced this dataset
([codebyzeb/babylm-ipa](https://github.com/codebyzeb/babylm-ipa),
`prepare_babylm.ipynb`) calls
`transcribe_utterances(..., "phonemizer", language="en-us", ...)`. So this
gold is espeak-ng output: it is tiered **`espeak-derived`** and can neither
qualify nor block English, exactly like the other espeak-lineage golds.

The loader pairs the `text` column with the `phonemized_utterance` column
(space-separated IPA segments, `WORD_BOUNDARY`-delimited between words) by
positional alignment, skipping rows whose token counts disagree, and
collects deduplicated word-level pairs. Full dev split: `N=20344`,
**PER 0.5257**: a high number that says o2i's English diverges *from
espeak* on a corpus of conversational/literary text. It is agreement, not
accuracy, and the far more informative English rows are `cmudict`
(lexicon-derived) and `wikipron`.

**Licence:** the dataset card declares none. The underlying BabyLM corpora
keep their own licences. Eval-only use.

### Lexibank/CLDF wordlist gold (`northeuralex`, `wold`)

[Lexibank](https://github.com/lexibank) republishes published comparative
wordlists and dictionaries in [CLDF](https://cldf.clld.org/) (Cross-Linguistic
Data Format): one `cldf/forms.csv` per dataset, keyed by `Language_ID`
(resolved to a Glottocode/ISO 639-3 code via `cldf/languages.csv`), with a
`Value` column (the word as originally recorded — real orthography or
script), a `Segments` column (space-separated IPA-ish phonemic segments,
`+` marking a morpheme boundary), and a `Source` column citing the specific
published dictionary/grammar each row was compiled from. This is compiled,
cited lexicographic data — not a phonemizer's own output — so it is tiered
`lexicon-derived`, the same class as `cmudict` and `portuguese_unified`.

This is the intended entry point for the **stub-promotion path**: both
wired datasets are restricted to o2i language codes whose spec is
`stub`/`skeleton` quality (not already `research`/`production`), so a low PER
here is progress evidence toward [quality_tiers.md](quality_tiers.md), not a
duplicate of an existing production-tier row.

**NorthEuraLex** ([lexibank/northeuralex](https://github.com/lexibank/northeuralex),
Dellert et al. 2020, *NorthEuraLex: a wide-coverage lexical database of
Northern Eurasia*): a 100+-language comparative wordlist. Every wired
language was smoke-checked (the engine must produce non-empty output for a
large majority of the language's forms) and restricted to specs with a
non-empty grapheme table:

| o2i tag | NorthEuraLex language | Spec quality | `N` | PER |
|---|---|---|---:|---:|
| `liv` | Livonian | skeleton | 1042 | 0.1837 |
| `sms` | Skolt Sami | skeleton | 1063 | 0.4344 |
| `sjd` | Kildin Sami | skeleton | 1011 | 0.2748 |
| `yrk` | Tundra Nenets | skeleton | 1016 | 0.4423 |
| `bua` | Buryat | skeleton | 1174 | 0.3003 |
| `evn` | Evenki | skeleton | 1132 | 0.3407 |
| `niv` | Nivkh | skeleton | 833 | 0.3922 |
| `ale` | Aleut | skeleton | 896 | 0.3993 |
| `ain` | Hokkaido Ainu | stub | 858 | 0.1672 |

Excluded despite an ISO/registry match: `yux` (Southern Yukaghir) has a
non-empty grapheme table but scored 0/913 non-empty in the smoke check — a
script/transliteration mismatch between the spec's grapheme inventory and
NorthEuraLex's Cyrillic orthography for this variety, not something a gold
row alone can fix.

**WOLD** ([lexibank/wold](https://github.com/lexibank/wold), Haspelmath &
Tadmor 2009, *World Loanword Database*): a 41-language loanword-typology
wordlist. Same selection discipline:

| o2i tag | WOLD language | Spec quality | `N` | PER |
|---|---|---|---:|---:|
| `car` | Galibi Carib (Kalina) | skeleton | 1190 | 0.1578 |
| `arn` | Mapudungun | stub | 1266 | 0.3114 |
| `gwd` | Gawwada | skeleton | 976 | 0.0481 |
| `irk` | Iraqw | skeleton | 1117 | 0.2182 |
| `crs` | Seychelles Creole | research | 1874 | 0.2240 |
| `rif` | Tarifiyt Berber | research | 1506 | 0.4095 |

Excluded despite an ISO match: WOLD's own `KildinSaami` (`sjd`) romanizes
the language differently from NorthEuraLex's Cyrillic forms and scored only
25/1473 non-empty in the smoke check. NorthEuraLex's `sjd` row above is the
one that actually exercises the spec's grapheme table for this language, so
WOLD's duplicate entry is left unwired rather than registered at a token
score.

Two further Lexibank datasets were inspected and rejected, and a later pass
over 21 more candidates wired none of them — see [Rejected candidates](#rejected-candidates).

All 41 WOLD languages have been cross-referenced against the o2i spec
registry. Of the 39 not wired here: most already
have gold from other datasets (wikipron/ipadict/ipa_childes/etc — English,
Dutch, Japanese, Mandarin, Thai, Vietnamese, Indonesian, Hawaiian, White
Hmong, Hausa, Lower Sorbian, Kildin Saami, ...); several have no registered
o2i spec at all (Kanuri, Zinacantan Tzotzil, Malagasy, Old High German,
Selice Romani, Sakha); the rest resolve to `stub` specs with an EMPTY
grapheme table (Archi, Bezhta, Manange, Ket, Oroqen, Ceq Wong, Takia,
Gurindji, Yaqui, Qeqchi, Otomi, Saramaccan, Imbabura Quechua, Hup, Wichi) —
nothing for a gold row to exercise. Only Gawwada, Iraqw, Seychelles Creole
and Tarifiyt Berber had both a non-empty grapheme table and no existing gold
anywhere in the registry; all four smoke-checked at ~100% non-empty engine
coverage on a 150-row sample and are wired above.

The `car`/`arn` PER figures in the table above (0.1578 / 0.3114) do not match
`benchmarks/results.json` (0.0857 / 0.0112). The board is the authority for a
score, so read the JSON values and treat the table cells as stale until a
rescore refreshes them.

### kaikki.org Wiktextract gold (`kaikki`)

[kaikki.org](https://kaikki.org/dictionary/) republishes
[Wiktextract](https://github.com/tatuylonen/wiktextract) (Ylonen 2022)
machine-extractions of Wiktionary as one JSON-lines file per language: each
entry carries a `word` (the headword as written), a `pos`, and a `sounds`
list of `{"ipa": "..."}` objects (often several transcription variants).
It draws on the same underlying Wiktionary community edits as `wikipron` —
a different extraction pipeline over the same source, not an independent
transcriber — so it is tiered `crowd-scraped`, same as `wikipron`.

The rows below come from a sweep of o2i specs with a non-empty grapheme
table and ZERO gold anywhere in this registry. Candidates were
cross-referenced against kaikki.org's per-language index; each wired
language was downloaded, filtered to entries carrying a non-empty
`sounds[].ipa` (dropping `pos: "character"` rows — single-letter/digraph
entries that gloss an orthographic symbol, e.g. Xhosa `hl` → /ɬ/, not
words), hand-sampled, and smoke-checked for ≥70% non-empty engine coverage
before wiring:

| o2i tag | kaikki language | Spec quality | `N` | coverage | PER |
|---|---|---|---:|---:|---:|
| `jv` | Javanese | skeleton | 93 | 100% | 0.2203 |
| `su` | Sundanese | skeleton | 397 | 99.5% | 0.0964 |
| `lo` | Lao | skeleton | 2305 | 99.3% | 0.7225 |
| `xh` | Xhosa | skeleton | 887 | 100% | 0.5725 |

Sample-audit notes (30 rows hand-checked per language, broad-transcription
IPA, word/IPA pairing spot-checked against the spec's own grapheme
description in `notes`):

- **`jv` (Javanese):** the kaikki dump is majority **Aksara Jawa** (Javanese
  script) entries even though the o2i `jv` spec only encodes the Latin
  romanization — a raw smoke check scored just 77/150 (51%) non-empty,
  under the 70% gate. Restricting the loader to Latin-script words only
  (`_KAIKKI_WORD_FILTER["jv"]`) recovers 100% coverage on the 127 Latin
  entries the dump actually has (93 after word+IPA de-duplication). Sampled
  pairs (`kurang` → `/ku.raŋ/`, `bantu` → `/ban.t̪u/`) match the spec's
  documented vowel/consonant inventory.
- **`su` (Sundanese):** clean, near-total coverage; sampled pairs (`balad`
  → `/ba.lad/`, `duit` → `/duˈit/, [duˈwit̪]`) agree with the spec's
  7-vowel description. Best PER of the four (0.0964).
- **`lo` (Lao):** coverage is excellent (99.3%), but PER is very high
  (0.7225) — **not a gold-quality problem**. Sampling shows the `lo` spec
  collapses nearly every vowel to `/o/` regardless of the actual
  Lao vowel sign (e.g. `ລາວ` gold `/laːw˧˥/` vs. engine `/lowo/`; `ຕາ` gold
  `/taː˩(˧)/` vs. engine `/to/`), and the gold's tone diacritics (Lao is a
  six-tone language) are not produced at all. The `lo` spec's vowel-sign
  mapping is substantially incomplete, and this gold row is the regression
  fixture that repair needs.
- **`xh` (Xhosa):** coverage is total, but PER is high (0.5725) because
  kaikki's Xhosa transcriptions are narrow phonetic — vowel length, tone
  (acute/circumflex marks), prenasalization, and breathy voicing are
  marked on nearly every syllable (e.g. `impala` gold `/íᵐpaːlá/` vs.
  engine `/impala/`), none of which the current segmental `xh` spec
  encodes. The gold is usable, and the row stays high-PER until the spec
  gains tone, length and prenasalization rules.

Rejected: **Tigrinya** — only 28 of 933 entries in kaikki's Tigrinya dump
carry a `sounds[].ipa` value, too thin to be a usable gold set.

None of `jv`/`su`/`lo`/`xh` promote to `research` from this gold alone:
each already has a cited entry in `sources`, but none has a `stress` block
or a documented stress-exemption in `notes` (Javanese and Sundanese in
particular have predictable but unencoded penultimate stress), which
`quality_tiers.md` also requires for the `research` tier. That is a
spec-authoring task, not a gold one.

`open-dict-data/ipa-dict` is exhausted: every one of its 31 upstream files
is either wired (`_IPADICT_FILES`) or explicitly rejected with a reason
(`_IPADICT_UNWIRED`), except `zh_hant.txt` (Traditional Chinese), which is
documented nowhere. It has the same problem as the rejected `zh_hans` and
`yue` entries, a Han-script gold against a Pinyin-romanization `zh` spec, so
it belongs in `_IPADICT_UNWIRED`.

A later sweep for the same thing, specs with a non-empty grapheme table
and no row anywhere in `results.json`, counted 735 zero-gold specs out of
7383 registered codes. The set shrinks as gold lands, so it is recomputed
rather than reused. The highest-population zero-gold specs (Nepali, Bhojpuri,
Awadhi, Sindhi, Igbo, Somali, Fula, Chhattisgarhi, Magahi, Oromo,
Lingala, Shona, Kirundi, Wolof, Konkani, and a few more) were
cross-referenced against kaikki.org's per-language index (size-checked
with a `HEAD` request before any download, nothing vendored):

| o2i tag | kaikki language | Spec quality | `N` | coverage | PER | verdict |
|---|---|---|---:|---:|---:|---|
| `so` | Somali | research | 200 | 100% | 0.5937 | wired |
| `om` | Oromo | skeleton | 53 | 100% | 0.5228 | wired |
| `ne` | Nepali | research | 2051 | 100% | 0.6047 | wired |
| `kok` | Konkani | research | 830 | 99.6% | 0.4944 | wired |

Sample-audit notes (30 rows hand-checked per language, broad
transcription, word/IPA pairing spot-checked against the spec's own
`notes`):

- **`so` (Somali):** clean, single-script (Latin) dump after the
  `_KAIKKI_WORD_FILTER["so"]` restriction (a handful of loanword/foreign
  entries were dropped, same rationale as `jv` above, with no Javanese-style
  majority-foreign-script problem here, just a minority to filter out).
  Every sampled word matches its orthography (`dhagax` → `/ˈɖɑ́ɡɑ̀ħ/`,
  `libaax` → `/lìˈbæ̂ːħ/`). PER is high (0.5937) because kaikki's Somali
  transcriptions are narrow — tone (high/low pitch accent marks), vowel
  length, and pharyngeal/epiglottal detail (`caws` gold
  `/ˈʡ͜ʢǽ͜ʉ̀s/` vs. engine `/ʕaws/`) are marked on nearly every word, none of
  which the segmental `so` spec encodes. The gold is usable, and the row
  stays high-PER until the spec gains tone and length rules.
- **`om` (Oromo):** clean, single-script (Latin) dump after the
  `_KAIKKI_WORD_FILTER["om"]` restriction. Word/IPA pairing checks out
  (`tokko` → `/ˈtɔ́kkɔ/`, `Waaqa` → `/ˈwɑ́ːkʼɐ/`). The gold's segmental
  notation is the standard descriptive one for Oromo and the spec matches
  it: short `a e i o u` are lax `ɐ ɛ ɪ ɔ ʊ` against long `ɑː eː iː oː uː`,
  the glottalised stops `ph x c q` are `pʼ tʼ tʃʼ kʼ`, and `dh` is the
  retroflex implosive `ᶑ`. What remains of the PER is almost entirely the
  pitch accent: kaikki marks a high tone with an acute on the vowel of
  nearly every entry, and Qubee does not write tone, so an
  orthography-driven spec cannot predict it. Those accent marks account
  for about 95% of the residual edit distance; the segmental transcription
  is otherwise near-exact. Tone is a notation gap of the same family as
  `so`'s, and it is the ceiling on this row rather than a spec defect.
- **`ne` (Nepali):** the largest haul of the four (2051 scorable
  entries after de-duplication), Devanagari script matching the spec
  directly — no script filter needed. Sampled pairs check out
  (`खतरनाक` → `/kʰʌt̪ʌrnäk/`, `विद्यार्थी` → `/bid̪̚d̪järt̪ʰi/`). PER is
  high (0.6047) almost entirely from one systematic, single-cause
  divergence: the `ne` spec inserts a schwa after every final consonant
  cluster/consonant the gold treats as silent or reduced (`कदर` gold
  `/kʌd̪ʌr/` vs. engine `/kəd̪ərə/`, `दश` gold `/d̪ʌs/` vs. engine
  `/d̪əʃə/`), plus a schwa-vs-`ʌ` vowel-quality mismatch throughout.
  The `ne` spec's schwa-deletion and vowel-reduction rules are
  substantially incomplete, and this gold row is the regression fixture
  that repair needs.
- **`kok` (Konkani):** clean Devanagari-script haul (830 scorable
  entries), same script family as the already-wired-elsewhere Devanagari
  specs. Sampled pairs check out (`आजी` → `/ɑːd͡ʒiː/`, `भाचो` →
  `/bʰɑːt͡sɔ/`). PER is high (0.4944) from the same final-schwa-insertion
  pattern as `ne` (`उठप` gold `/uʈʰəp/` vs. engine `/uʈʰəpə/`) plus
  nasalization the gold marks with a tilde that the spec's segmental
  output doesn't carry (`अदांव` gold `/ədɑ̃ːʋ/` vs. engine `/əd̪aː̃ʋə/`).
  This is the same final-schwa gap as `ne`, and it points at one shared
  Indo-Aryan-spec fix rather than two independent bugs.

None of `so`, `om`, `ne` or `kok` promote tiers from this gold alone.
`so`, `ne` and `kok` are already at `research`, each with a cited `sources`
entry and a `stress` block or exemption, and these rows supply the gold
benchmark `quality_tiers.md` says `research` should carry. Several other
specs are marked `research` with zero gold anywhere in `results.json`,
because the `test_data_quality.py` guard checks this only for `production`,
so the tier is under-enforced generally rather than for these three. `om`
stays `skeleton`: it has neither a cited source nor a stress block or
exemption, and that is a spec-authoring task.

**Investigated and rejected:**

- **Sindhi (`sd`)** — kaikki.org has a Sindhi dump (874/1771 entries carry
  `sounds[].ipa`), but every one of those entries is Perso-Arabic or
  Devanagari script (`زبان`, `त`); the `sd` spec is Latin-script only
  (Standard Sindhi romanization). Filtering to Latin-script words leaves
  **zero** entries — the dump has no Latin-script content at all.
  Rejected: wrong script for this spec, not fixable with a filter (there
  is nothing to filter *to*).
- **Santali (`sat`)** — kaikki.org has a Santali dump (537/928 entries
  carry `sounds[].ipa`), but every entry is in Ol Chiki script
  (`ᱫᱟᱜ`); the `sat` spec is a Latin romanization. Same problem as `sd`:
  filtering to Latin-script words leaves zero entries.
- **Tigrinya (`ti`)** — 28 of 933 entries carry `sounds[].ipa`, too thin
  to be a usable gold set.

`om`, `ff` (Fula), `ln` (Lingala), `sn` (Shona), `wo` (Wolof), `tw`
(Twi, via kaikki's `Akan` macrolanguage dump) and `st` (Southern Sotho,
via kaikki's generic `Sotho` dump) were all checked; `om` was the only
one of that group with a large enough clean sample after script
filtering to be worth wiring (53 usable entries vs. single digits to
low tens for the rest, several of which turned out to be dictionary
metadata — single-letter "character" entries the existing
`_KAIKKI_EXCLUDED_POS` filter doesn't catch because their `pos` isn't
literally `"character"` — rather than real words). The rest are not wired:
they are thin or contaminated candidates that need a tighter word-shape
filter first.

No kaikki.org dump exists (`HEAD` → 404, checked under the language's
common name and obvious alternates) for several other high-population
zero-gold candidates: Bhojpuri, Awadhi, Igbo, Chhattisgarhi, Northern
Sotho, Kirundi/Rundi, Minangkabau, Kongo, Tsonga, Maithili, Venda and
Southern Quechua. They are listed so the lookup is not repeated.

#### What the Konkani (`kok`) residual is made of

The Konkani gold is hand-typed, not module output. Entries carry
dialect-tagged variants that no generator would produce — `मामा` has a
Goud-Saraswat reading `[mɑːmɑː]` beside a Roman-Catholic `[mɑːm]`, and
`आपव्चे` carries four readings across two varieties — so the row is an
accuracy test rather than a reproduction test, and none of the
[Module-generated](#module-generated-wikipron-rows) caveats apply.

Two of the gold's conventions are not encoded in the spec, deliberately,
because encoding them would fit the gold rather than describe Konkani.

The gold writes the low vowel as `ɑ`. Over the 830 scored words, `⟨ा⟩` is
transcribed with `ɑ` 411 times against `a` 14 times (counted by regex
over the normalized gold of every word containing `⟨ा⟩`), so the
choice is uniform, but it is a notation choice: the published Konkani
inventories write the phoneme `/a/`. The spec keeps `aː`. Rewriting every
`a` to `ɑ` in the engine's output would take the row from PER 0.2245 to
0.1591 — 0.065 of the residual is this symbol and nothing else.

The gold reads `⟨फ⟩` as `[f]` in 34 words and `[pʰ]` in 10. The split is
lexical — `[f]` sits in the Portuguese stratum (`फोटो`, `फिलिप`,
`फार्मास`) and `[pʰ]` in the inherited one (`फिरप`, `फुटप`) — and nothing
in the orthography distinguishes them, so both readings stay in the
lattice with `pʰ` first. Reordering to `f` would buy 0.013 PER on this
lexicon and assert nothing about the language.

The affricate series is the largest genuinely unrecoverable contrast.
Konkani has phonemic `/ts dz/` beside `/tʃ dʒ/`, and Devanagari writes
both with `⟨च⟩` and `⟨ज⟩`. Almeida's conditioning — the affricate
spirantizes except word-initially, in gemination and after a nasal — does
not hold in this gold: `[z]` occurs 5 times word-initially against 10
times elsewhere, and affricates outnumber it in both positions. It is
therefore encoded as a second candidate per grapheme, not as a rule.

Taking an oracle over the five contrasts the orthography does not
determine (`e`/`ɛ`, `o`/`ɔ`, `tʃ`/`ts`, `dʒ`/`dz`, `pʰ`/`f`) — for each
word, the substitution mask minimizing edit distance to the gold — puts
the floor for this row at PER 0.1543. The board's Oracle@5 of 0.1339
is the same quantity measured through the engine's own beam. Of the
residual edit operations at PER 0.2245, 6.1% involve a schwa (1093 edit
operations over 5224 gold segments, 67 of them touching `ə`, counted by
`difflib` opcode over combining-mark-grouped segments).

## Rejected candidates

Datasets investigated and excluded due to tool-generated or unclear
provenance:

| Dataset | Verdict | Evidence |
|---|---|---|
| **[lexibank/ids](https://github.com/lexibank/ids)** (Intercontinental Dictionary Series) | **EXCLUDED: no IPA column** | `cldf/forms.csv`'s `Segments` column is empty on every one of its ~437k rows (verified by scanning the whole file). The `Form`/`Value` columns are the source script/orthography, but there is no phonemic transcription to score against at all. |
| **[lexibank/abvd](https://github.com/lexibank/abvd)** (Austronesian Basic Vocabulary Database) | **EXCLUDED: no IPA column** | Same problem as `ids`: `Segments` is empty on all ~347k rows. |
| **[lexibank/uralex](https://github.com/lexibank/uralex)** (Uralic) | **EXCLUDED: no IPA column** | `Segments` is empty on all ~10k sampled rows (repo also carries reconstructed proto-forms, e.g. `*tuli̮`, which would need excluding separately even if segments existed). |
| **[lexibank/tuled](https://github.com/lexibank/tuled)** (Tupían) | **EXCLUDED: transcription, not orthography** | `Value` already contains IPA symbols (`ʔ`, tone/length marks) and, joined, reproduces `Segments` almost verbatim (e.g. `naʔot` / `n a ʔ o t`) — the "orthography" column is the phonemic transcription itself, not an independent writing system. |
| **[lexibank/dravlex](https://github.com/lexibank/dravlex)** (Dravidian) | **EXCLUDED: transcription, not orthography** | `Value` is a Latin phonemic romanization (e.g. Kannada `na:nu`, Kodava `na:nə`) using ASCII `:` for vowel length, not each language's native script (Kannada/Telugu/Tamil/Malayalam scripts) or an attested romanization standard. |
| **[lexibank/chaconarawakan](https://github.com/lexibank/chaconarawakan)** (Arawakan) | **EXCLUDED: transcription, not orthography** | `Value` carries tone marks and slash-alternants inside `Segments` (`nhóa` → `ɲ ó/o a`) consistent with a comparative fieldwork transcription, not a standardized orthography for these mostly-unwritten languages. |
| **[lexibank/felekesemitic](https://github.com/lexibank/felekesemitic)** (Semitic) | **EXCLUDED: transcription, not orthography** | Amharic `Value` (`dǝmmǝrǝ1`) is a Latin phonemic transcription with a sense-index suffix, not Ge'ez script; the ejective is rendered as a non-standard `ќ` glyph rather than any Amharic orthography. |
| **[lexibank/hantganbangime](https://github.com/lexibank/hantganbangime)** (Dogon/Bangime) | **EXCLUDED: transcription, not orthography** | `Value` is IPA with tone diacritics (`ɡwìì`, `pɛ́`), for languages with no standardized practical orthography in this source. |
| **[lexibank/lundgrenomagoa](https://github.com/lexibank/lundgrenomagoa)** (Tupí-Guaraní: Omagua/Kokama) | **EXCLUDED: transcription, not orthography** | `Value` uses raw IPA (`β`, `ɨ`, `ɲ`, `ã`) directly, e.g. Tupinambá `aβá`, not a practical spelling system. |
| **[lexibank/naganorgyalrongic](https://github.com/lexibank/naganorgyalrongic)** (Gyalrongic) | **EXCLUDED: transcription, not orthography** | `Value` carries IPA tone-letter diacritics (`ˊ`, `ˉ`) and retroflex/uvular IPA symbols directly (`ˊtə rno[ʢ]k`); no established practical orthography for these varieties. |
| **[lexibank/robinsonap](https://github.com/lexibank/robinsonap)** (Alor-Pantar) | **INSPECTED, NOT WIRED: no spec coverage** | `Value` genuinely looks like practical orthography (real digraphs, e.g. `gunnang` → `g u n n a ŋ` shows `ng`→`ŋ`), unlike every other candidate inspected. But all 13 languages (`twe abz beu woi kvw jka lev kvd adn swt nec kyo`, plus a Glottolog-only proto-language row) resolve to `stub`-quality o2i specs with an EMPTY grapheme table — the loader's stub-promotion path requires a non-empty table to exercise, so there is nothing for a gold row to score against yet. Revisit once any of these specs gets a grapheme table. |
| **[lexibank/sagartst](https://github.com/lexibank/sagartst)** (Sino-Tibetan) | **EXCLUDED: transcription, not orthography** | `Value` is raw IPA with tone-number/tone-letter suffixes (`zji¹`, `%tʰamtɕɤt`) across all 50 languages sampled, including reconstructed Old Tibetan/Tangut forms. |
| **[lexibank/savelyevturkic](https://github.com/lexibank/savelyevturkic)** (Turkic) | **EXCLUDED: transcription, not orthography** | `Value` uses a comparative-Turkological transliteration (`tïrɣaḳ`, `dïrnaġ`) distinct from each language's actual standard orthography (e.g. real Azeri spells this word `dırnaq`, not `dïrnaġ`). |
| **[lexibank/abrahammonpa](https://github.com/lexibank/abrahammonpa)** (Monpa) | **EXCLUDED: transcription, not orthography** | `Value` is raw IPA (`dʒaŋ`, `aɕigaŋpo`); Monpa varieties here have no standard practical orthography in this source. |
| **[lexibank/allenbai](https://github.com/lexibank/allenbai)** (Bai) | **EXCLUDED: transcription, not orthography** | `Value` embeds IPA tone-number superscripts directly (`xẽ⁵⁵`, `kʰao³¹`). |
| **[lexibank/bantubvd](https://github.com/lexibank/bantubvd)** (Bantu) | **EXCLUDED: transcription, not orthography** | `Value` is raw IPA with tone diacritics and slash-alternants (`hjɔ̀ɔ́gɔ̀ʤ̑à`); `Language_ID` in this dump is also a bare numeric code, not resolvable without extra work. |
| **[lexibank/chindialectsurvey](https://github.com/lexibank/chindialectsurvey)** (Kuki-Chin) | **EXCLUDED: transcription, not orthography** | `Value` is raw IPA (`tʃe`, `kɑi`) across all 31 dialect samples. |
| **[lexibank/birchallchapacuran](https://github.com/lexibank/birchallchapacuran)** (Chapacuran) | **EXCLUDED: transcription, not orthography** | `Value` is IPA with diacritics not found in any practical orthography for these languages (`waʒ̟a`). |
| **[lexibank/gravinachadic](https://github.com/lexibank/gravinachadic)** (Chadic) | **EXCLUDED: transcription, not orthography** | Mixed within the same dataset: some rows look orthographic (`malay`, `mbelew`) but others are raw IPA (`sˈa`, `ŋtɑguleŋ`) for the same comparative list — inconsistent enough across its 48 languages that it reads as one normalized fieldwork transcription, not each language's writing system. |
| **[lexibank/kraftchadic](https://github.com/lexibank/kraftchadic)** (Chadic, incl. Hausa) | **EXCLUDED: transcription, not orthography** | Even the one language with a genuine standard orthography in the sample, Hausa, is rendered with tone/length diacritics real Hausa orthography does not use (`yā wankḕ`) — this is a linguistic transcription overlaid on Hausa letters, not the Boko orthography itself. |
| **[lexibank/luangthongkumkaren](https://github.com/lexibank/luangthongkumkaren)** (Karenic) | **EXCLUDED: reconstructed forms + transcription** | `Value` entries are starred reconstructions (`*loɁᴰ`) with IPA tone-letter suffixes, not attested words in any orthography. |
| **[lexibank/marrisonnaga](https://github.com/lexibank/marrisonnaga)** (Naga/Kuki-Chin, incl. Jingpho, Lushai, Manipuri) | **EXCLUDED: transcription, not orthography** | Superficially promising (real digraphs `ch`, `sh`, `hm`, `hn`), but every row across all 40 languages carries a `◦` syllable-break marker that belongs to Marrison's own comparative-list transcription convention, not to any of the languages' actual writing systems; "Manipuri" here is also romanized rather than the language's real Meitei Mayek/Bengali-script orthography. Applies even to the 3 languages with non-empty o2i grapheme tables (`kac`/Jingpho, `lus`/Lushai, `mni`/Manipuri, all already `research` tier). |
| **[lexibank/mitterhoferbena](https://github.com/lexibank/mitterhoferbena)** (Bena) | **EXCLUDED: transcription, not orthography** | `Value` embeds the IPA length mark `ː` directly (`liːho`). |
| **[dsvv-cair/ipa-transcription-datase](https://huggingface.co/datasets/dsvv-cair/ipa-transcription-datase)** (English, 122,594 rows, CC BY-NC 4.0) | **REJECTED: LLM-generated (GPT-4o Mini)** | The dataset card states it plainly: *"we constructed a large-scale, phonemically rich dataset using the **GPT-4o Mini API**"*. This is LLM-hallucinated IPA, and it is strictly worse than espeak/epitran gold rather than merely different: espeak and epitran are deterministic rule systems with characterisable failure modes, so a disagreement can be traced to a rule and adjudicated. An LLM has no lexicon, no G2P model and no rules, so its errors are unbounded, uncorrelated, and **not attributable to anything**. Scoring against it would measure "agreement with an LLM's guess" and would carry no diagnostic information. Not wired in any tier: the licence (CC BY-NC, fine for eval-only gold) is not the reason. The absent error model is. |
| **ipa-dict (tool-generated files: `ar`, `es_*`, `fa`, `fi`, `nb`, `nl`, `or`, `vi_*`, and the espeak-derived `en_UK`)** | WIRED, TIERED: not rejected | Each is registered with the tier its own provenance earns (`machine-generated`, or `espeak-derived` for `en_UK`), never `lexicon-derived`. See [ipa-dict pronunciation dictionaries](#ipa-dict-pronunciation-dictionaries-ipadict). A tool-generated gold is admitted explicitly, with the caveat travelling on the row: it is not silently promoted, and the espeak row can neither qualify nor block a language. |
| **ipa-dict `fr_QC.txt`** | EXCLUDED: no spec | No Québécois French spec is registered. The file is also qc-ipa script output over `fr_FR` ("highly experimental"). |
| **ipa-dict `tts.txt`** | EXCLUDED: no spec | Isan / Northeastern Thai. No `tts` spec, and the `th` spec is a different language. |
| **ipa-dict `zh_*`, `yue`** | EXCLUDED: untranscribable | Well-sourced golds (Unihan/KFCD, KFCD Pingyam), but Han script is lexical: no G2P without a dictionary: and the `zh` spec is a pinyin/romanization spec. An engine gap, not a gold problem. The former third member of this row, `ko` (Korean Wiktionary), is WIRED now: Hangul syllable blocks canonically decompose to the `ko` spec's conjoining-jamo graphemes. |
| **vox_communis `zh-cn.tsv`** | **DE-REGISTERED: untranscribable** | Same disposition as the ipa-dict `zh_*`/`yue` row above, and as this dataset's own `yue.tsv`. The o2i `zh` spec is a **pinyin** spec; `zh-cn.tsv`'s `aligned_sentence` column is Han characters (`盘固 草 为 禾 本科 …`). Every row transcribed to the empty string, so the board carried a `vox_communis` `zh` row composed entirely of "hypothesis empty, whole gold is a deletion" — a PER above 2 once the `spn` markers in that gold were counted as well. That is not a Mandarin score — it is the absence of a hanzi→pinyin front-end, reported in the units of a phone error rate. An engine gap, not a gold problem; the registration returns when such a front-end exists. (`ja` is deliberately kept: kana rows transcribe, only the kanji minority go empty, so its row still carries signal.) |
| **kaikki.org Occitan / a second `oc` gold** | **NOT WIRED: same source as the existing row** | The `oc` row already scores against WikiPron `oci_latn_broad.tsv`, which is a scrape of Wiktionary. kaikki.org is Wiktextract over that same Wiktionary, so a kaikki `oc` row would measure the engine twice against one body of transcription and read as corroboration it is not. The kaikki wiring rule is also explicit that the set exists for specs with no gold anywhere else. VoxCommunis, the one registered source that would be independent (Common Voice audio, force-aligned), has no Occitan file: `oc.tsv` and `oc-fr.tsv` both 404 on the `fdemelo/vox-communis-parallel-g2p` repo. Until an Occitan pronouncing dictionary or an aligned corpus turns up, Occitan has one gold, and it is a mixed-dialect one — see the `oc` spec notes for what it does and does not transcribe. |
| **kaikki.org Tetum** | **REJECTED: too thin** | 3 of 686 entries in the Tetum dump carry a `sounds[].ipa` value, thinner still than the already-rejected Tigrinya set. WikiPron has no Tetum scrape either, so `tet` is scored on the primary-source rows mined from its own reference grammar. |
| **Lexique 3.82 (French)** | EXCLUDED: complex notation | Data is human-curated (Boris New / Christophe Pallier, CNRS) and CC BY-SA 4.0, but uses a custom phonemic notation (not X-SAMPA, not IPA): `§`=ɔ̃, `°`=schwa-variant, `5`=ɛ̃, `8`=œ̃ etc.: not covered by `scriptconv.notation.xsampa_to_ipa`. A dedicated Lexique converter would be a clean follow-up. WikiPron `fra` is used in the interim. |
| **NST Swedish/Norwegian lexicons (Språkbanken/NB)** | EXCLUDED: no programmatic download | Authoritative SAMPA lexicons for sv/nb/da from Nasjonalbiblioteket. Human-curated. However no stable raw-download URL suitable for `urllib.request`. The portal serves interactive/catalogue pages. WikiPron Scandinavian TSVs used instead. |
| **CELEX2 (de/nl/en)** | EXCLUDED: proprietary | LDC license (LDC96L14), not freely downloadable. |
| **GlobalPhone** | EXCLUDED: ELRA license | Per-language ELRA licenses. Not freely downloadable. |

## Known finding: the nukta digraphs and the inherent vowel

Not a dataset issue — an engine one, recorded here because it is measured
against these golds and is deliberately NOT fixed in the PR that found it.

The tokenizer decides whether a grapheme key is a bare combining mark, and
therefore whether it takes the abugida inherent vowel, from the key's LAST
character. That is right for a key that IS a mark (anusvara `ং`) and wrong
for a key that merely ENDS in one. Two key shapes end in a mark:

* a **conjunct stack** — a letter plus SUBJOINED LETTERS, which Unicode
  encodes as combining marks (Tibetan `ཀྲ` = `ཀ` + U+0FB2). A subjoined
  letter is a letter, so the key is a consonant letter and must take the
  inherent vowel. This case IS fixed; `dz` depends on it.
* a **nukta digraph** — a letter plus a modifier sign (`क़` = `क` +
  U+093C DEVANAGARI SIGN NUKTA), in `hi bn as gu awa bho mr ne or pa kok
  mai km`. These keys get no inherent vowel today, so `क़लम` is `qləm`
  where the schwa-deletion rules should have been given a schwa to decide
  about (`qələm`).

The nukta half looks like the same bug and is not the same fix: giving
those keys the inherent vowel moves the fleet in both directions, and on a
same-session, same-cache differential against the current engine the
row-weighted net is NEGATIVE — `hi`/`wikipron` gains while `bn`/`vox_communis`
(30 261 rows) and `as` lose more. Whether the added vowel is right depends
on each Brahmic spec's own schwa-deletion coverage, which is a per-spec data
question, not a tokenizer question. It needs its own PR, with per-spec
schwa rules landing alongside the engine change rather than after it.

Beware, when measuring it, that committed board rows can predate a
gold-cache refresh and move on an UNMODIFIED tree: `or`/`ipadict` and
`ne`/`kaikki` both do. Any differential must
re-run both sides in one session against one cache, or it will read that
drift as a result.

---
[← Benchmarks](benchmarks.md) · [Home](index.md) · [Benchmark methodology →](benchmark_methodology.md)
