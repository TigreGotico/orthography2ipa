# Benchmarks

How the G2P engine is evaluated: which gold pronunciation datasets are
used, where they come from, and the reference numbers the bundled
harness produces. Run any row yourself with
[`scripts/benchmark.py`](../scripts/benchmark.py):

```bash
python scripts/benchmark.py --dataset portuguese_unified --lang pt-PT
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

- **A gold set's value is its error model.** Human/lexicon gold is
  trustworthy. Rule-system gold (espeak, epitran) measures *agreement with a
  competitor* — informative, because a deterministic rule system's
  disagreements can be traced to a rule and adjudicated, but it can never
  certify us. LLM gold has *no error model at all*: no lexicon, no rules,
  nothing to attribute an error to, so a disagreement is not even diagnostic.
- **A low PER against a tool-generated gold means "agrees with that
  tool", NOT "correct".** `vox_communis`, `ipa_childes`, `ipa_babylm`
  and `hitz_basque_ipa` are all the output of an automatic phonemizer. Scoring
  well there says o2i reproduces that tool's decisions, right or wrong.
- **Scoring a system against a gold its own generator produced is
  near-tautological.** `hitz_basque_ipa` *is* the output of HiTZ's
  ahoNT/AhoTTS phonemizer, so a low PER for AhoTTS/ahotts-g2p on it just
  confirms the tool reproduces itself — it is not evidence of
  correctness. The same trap applies to any comparison where the
  evaluated system shares the gold's generator: use an **independent**
  gold (here, `wikipron` `eu`) for the fair comparison.
- **Comparing o2i to espeak on an espeak-derived gold is partly
  circular** for the same reason. `vox_communis`, `ipa_babylm` and the
  `phonemizer`-phonemized `ipa_childes` languages are all
  phonemizer/espeak-lineage; an espeak-vs-o2i table on that gold measures
  how similarly two systems diverge from the truth, not who is closer to
  it. **The same trap applies to epitran**, which
  [comparison](comparison.md) also benchmarks o2i against (`epitran_per`):
  the six `epitran`-phonemized `ipa_childes` languages are epitran's own
  output, so treating them as truth would double-count epitran as both rival
  and referee.
- **Absolute PER is noisy — treat it as directional, not precise.** The
  published scoreboard scores the **full** gold set of every language (see
  "Full-dataset scoreboard" below), so its `N` is the number of gold words
  actually covered — not a sample — and its
  PER is the whole-set number — but PER is still bound by the gold's own
  notation conventions and provenance, so read numbers as relative/ranking
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

The machine-readable tier per row lives in the `provenance` column of
[`docs/scoreboard.md`](scoreboard.md) and the `provenance` field of
[`benchmarks/results.json`](../benchmarks/results.json), resolved by
`provenance_for(dataset, lang)` in `scripts/benchmark.py` (a test forces
every registered dataset to carry a tier, so a new dataset cannot be added
without classifying it).

Most datasets are one source, so one `PROVENANCE` tier describes them.
Some are **collections of independently sourced files**, and for those a
single tier would be a lie — ipa-dict ships a human Icelandic dictionary,
a Wiktionary-built German list and *espeak-generated* British English side
by side. Those datasets carry a **per-language** tier in
`PROVENANCE_BY_LANG`, which `provenance_for` prefers over the dataset-wide
value, so the row's tier is always the tier of the *file it was scored
against*. The dataset-wide value then serves only as a fallback, and is
deliberately set to that dataset's most pessimistic tier: an unclassified
file degrades to "distrust it" rather than inheriting a tier it did not
earn. A test forces every wired ipa-dict language to carry its own
classification.

| Tier | What it means | Grain of salt |
|---|---|---|
| **expert-human** | IPA curated by phoneticians, trained annotators, or native speakers. | Still bound by the team's notation conventions; here often small-`N` and/or not peer-validated. |
| **lexicon-derived** | Human lexicographers, via a published dictionary's notation — sometimes through a mechanical notation transform (ARPABET→IPA, slashed-phonemic→IPA). | Dictionary conventions ≠ surface phonetics; the transform step can add its own artifacts. |
| **crowd-scraped** | Wiktionary community edits (WikiPron). | Uneven per language; some entries are themselves editor-applied rule output, not attested transcriptions. |
| **machine-generated** | A phonemizer's *own output* reused as the reference. | **Biggest grain of salt.** Low PER = agreement with that tool, not correctness. |
| **espeak-derived** | A **competitor's** output reused as the reference: espeak-ng, directly or through a wrapper (`ipa_babylm` via G2P+; the `phonemizer`-phonemized `ipa_childes` languages). | **Never gate a quality decision on this.** The row measures *agreement with espeak* — and espeak is a system we benchmark ourselves *against* ([comparison](comparison.md)). Diverging from it can mean we are right and it is wrong, which shows up here as a *worse* score. Quality also varies by language. Judge any divergence against a cited source, never against this number. Kept for its breadth as a directional signal. |
| **epitran-derived** | A **competitor's** output reused as the reference: [epitran](https://github.com/dmort27/epitran) (the six `epitran`-phonemized `ipa_childes` languages — `de-DE`, `es-ES`, `hr`, `hu`, `id`, `sr`). | **Never gate a quality decision on this** — same reason as `espeak-derived`, and epitran is likewise a system [comparison](comparison.md) scores us against (`epitran_per`). Scoring o2i against epitran's own output and calling it gold would count the same system as both rival and truth. Still diagnostic (epitran is a deterministic rule system, so a disagreement can be traced to a rule and adjudicated against a cited source), but never certifying. |
| **llm-generated** | The gold was produced by a large language model (`barranquenho_dict`, `mirandese_dict` — Claude, research-conditioned; `arabic_tts`, `portuguese_tts` — LLM-drafted, engine-pinned, literature-audited). | **Worst of all, and never a gate.** An LLM has no lexicon, no G2P model and no rules, therefore **no error model**: it emits plausible-*looking* IPA that can be confidently wrong with no systematic structure, and a disagreement cannot be attributed to anything. Certifies nothing and diagnoses nothing; read as a curiosity, not as evidence. This is why the GPT-4o-Mini-generated `dsvv-cair` dataset is [rejected outright](#rejected-candidates) rather than wired. |

### Per-dataset classification

Every dataset registered in `scripts/benchmark.py`'s `DATASETS`,
classified by reading its loader (source URL, docstring, transform) and
its section below. Where the evidence is incomplete, the uncertainty is
stated rather than papered over.

| Dataset | Tier | IPA produced by | Notes / grain of salt |
|---|---|---|---|
| `primary_sources` | expert-human | The phonologists and dialectologists the specs cite | Example transcriptions copied out of the cited grammars/monographs/theses, one printed page per row (`N=270` across 13 varieties). The most authoritative gold here — and the smallest. Arabic ḥarakāt on the input side are editor-supplied (the sources print transcription, not script); see the dataset README. |
| `arabic_tts` | llm-generated | **LLM-authored, literature-audited** | Sentence-level TTS gold, one TSV per lect across 33 Arabic varieties (`N=20`/lect). Every IPA line was drafted by a large language model, then **engine-pinned** (aligned to the current o2i output) and audited row-by-row against the phonological literature cited in each row's `notes` column ([docs/arabic-tts-gold.md](arabic-tts-gold.md)). Citation-auditing raises confidence but does **not** create an error model — no lexicon, no rules behind the gold — so the honest tier stays `llm-generated`: directional only, gates nothing. Because the gold is engine-pinned it doubles as a regression fixture (PER≈0 on the pinned engine), so a nonzero PER here flags a spec change, not necessarily an error. |
| `portuguese_tts` | llm-generated | **LLM-authored, literature-audited** | Sentence-level TTS gold, one TSV per lect across European Portuguese standard + 15 regional varieties (`N=20`/lect). Same protocol and caveats as `arabic_tts`: LLM-drafted, engine-pinned, audited against the citations in each row's `notes` ([docs/portuguese-tts-gold.md](portuguese-tts-gold.md)). `llm-generated` tier — directional/regression signal only. |
| `ep_dialects` | expert-human | TigreGotico team, manual annotation | Internal dialect research, **pending external peer validation**; sentence-level, `N≈29–45`. |
| `mirandese_g2p` | expert-human | Native Mirandese speaker | The reference gold and **most trustworthy signal for Mirandese** (row id `mirandese_g2p`, from `TigreGotico/mirandese_g2p`), split by the `dialect` column: central → `mwl` (`N≈205`), sendinese → `mwl-x-sendim` (`N≈11`), raiano → `mwl-x-ifanes` (`N≈2` — an anecdote, read the CI not the point PER). Small-`N`; a separate, more reliable source than any synthetic Mirandese IPA dictionary. |
| `4catac` | expert-human | Expert annotators (Projecte AINA/BSC) | IEC guidelines, multi-annotator consensus review; sentence-level, `N=160`, `0.00` exact-match reflects notation/connected-speech mismatch, not total failure. |
| `clup_dialect` | expert-human | U.Porto CLUP dialect archive | Interview corpus is expert university dialectology, **but who/what produced the IPA column (`ArquivoDialetalCLUP_ipa`) is not documented in the loader or dataset card — treat the tier as "best case".** Many rows `N=1–17`: read the CI, not the point PER. |
| `portuguese_unified` | lexicon-derived | Infopédia + Portal da Língua Portuguesa + pt.wiktionary.org (convention-normalized merge) | Single Portuguese gold (`TigreGotico/portuguese-unified-pronunciation-lexicon`, ~598k rows / 122k words, CC BY-SA 4.0), replacing the three separate golds it merges. One region per registered tag (see `_PT_UNIFIED_REGIONS`); `ipa_narrow` is scored; untagged plain-`pt` rows are excluded. The Infopédia/Portal majority is dictionary/semi-automated lexicography and the Wiktionary minority is crowd-scraped — directional, not peer-validated ground truth. |
| `cmudict` | lexicon-derived | CMU Speech Group (hand-curated ARPABET) | Human labels, but **mechanically mapped ARPABET→IPA** via `scriptconv`; the transform adds artifacts. |
| `ipadict` | **per-language** (see below) | Depends on the file: human dictionaries, Wiktionary scrapes, rule scripts, **espeak** | The only mixed-provenance dataset here: ipa-dict is a *collection* of independently sourced files, so each row carries the tier of the file it was scored against, not a dataset-wide tier. Full per-language table in [ipa-dict pronunciation dictionaries](#ipa-dict-pronunciation-dictionaries-ipadict). |
| `wikipron` | crowd-scraped | Wiktionary editors | Quality tracks community size; some entries are editor-rule output, not attested; multiple valid variants per word. |
| `wikipron_ar_diacritized` | crowd-scraped | Wiktionary editors + `text2tashkeel` input restoration | Same Arabic gold IPA as `wikipron`; only the INPUT word is machine-diacritized (~2% DER noise floor). Diagnostic for the vowelized-Arabic rules; certifies nothing beyond the raw row. See [Arabic with tashkeel restored](#arabic-with-tashkeel-restored-wikipron_ar_diacritized). |
| `ipa_childes` | **per-language** (see below) | Depends on the language: `phonemizer` (espeak-ng), `epitran`, or `pinyin_to_ipa` | Mixed-provenance like `ipadict`: the IPA-CHILDES card names a **different phonemizing tool per language**, so each row carries the tier its own tool earns — `espeak-derived`, `epitran-derived`, or `machine-generated` for Mandarin's `pinyin_to_ipa` table. Full per-language tool table in [IPA-CHILDES split](#ipa-childes-split-ipa_childes). |
| `ipa_babylm` | espeak-derived | G2P+ with the `phonemizer` backend (= espeak-ng), `en-us` | BabyLM 2024 corpora phonemized by [G2P+](https://github.com/codebyzeb/g2p-plus), which is a wrapper over `phonemizer`/`epitran`; the conversion notebook ([codebyzeb/babylm-ipa](https://github.com/codebyzeb/babylm-ipa)) calls the `phonemizer` backend, which requires espeak-ng. So this is espeak output: it can neither qualify nor block English. |
| `hitz_basque_ipa` | machine-generated | HiTZ **ahoNT / AhoTTS** phonemizer | University-published (HiTZ/UPV-EHU), but the gold **is ahoNT/AhoTTS output** — it was generated by that phonemizer, not human-annotated. So a low PER **for the AhoTTS/ahotts-g2p engine on this row is near-tautological** (a tool scored against its own output); the independent, Wiktionary-sourced `wikipron` `eu` row is the fair comparison for Basque. |
| `barranquenho_dict` | llm-generated | **LLM (Claude), research-conditioned** | IPA generated by a large language model prompted with the *Convenção Ortográfica do Barranquenho* and descriptive research on the variety — **not** a phonemizer, not orthography2ipa, not any downstream o2i consumer, so scoring o2i against it is **not circular**. But LLM IPA can be plausibly wrong and is **not human-verified**: directional only. |
| `mirandese_dict` | llm-generated | **LLM (Claude), research-conditioned** | IPA generated by a large language model prompted with the *Convenção Ortográfica da Língua Mirandesa* and sub-dialect descriptions — **not** a phonemizer, not orthography2ipa, not any downstream o2i consumer, so scoring o2i against it is **not circular**. Complementary to the native-speaker `mirandese` gold. LLM IPA is plausibly wrong and **not human-verified**: directional only. |

## Provenance discipline

Because reliable gold is scarce, the harness applies a deliberate
discipline: prefer human/community provenance, and where tool-generated
IPA is admitted, admit it **explicitly, per dataset, with the reason
recorded** — never silently. Six tool-generated sources are wired in: four
are automatic-phonemizer output (`hitz_basque_ipa`, `ipa_childes`,
`ipa_babylm`, `vox_communis`) and two are LLM-generated IPA
dictionaries (`barranquenho_dict`, `mirandese_dict`), each under a
documented, dataset-specific exception (academic-corpus provenance, an
explicit task override, or the LLM-gold rationale below) rather than a
blanket relaxation. Each row carries the tier its own generator earns —
`machine-generated`, `espeak-derived`, `epitran-derived` or `llm-generated`
— so the caveat above travels with every number it produces, and
`can_gate_promotion()` in `scripts/benchmark.py` refuses the last three as
promotion evidence. Adding another tool-generated source requires the same
explicit call; it is not the default. A gold whose provenance cannot be
established does **not** default to a flattering tier: it is classified at
the most pessimistic tier its evidence permits, or rejected.

The two LLM-generated dictionaries (`barranquenho_dict`, `mirandese_dict`)
sit at the `machine-generated` tier for a specific reason: their IPA was
written by a large language model conditioned on published orthographic
norms and research, so it is unverified by human phoneticians and can be
plausibly wrong. Crucially, though, it was **not** produced by a
phonemizer, by orthography2ipa, or by any downstream o2i consumer — so
unlike the phonemizer golds above, scoring o2i against these carries **no
circularity**. The scoreboard must never be used to "correct" a spec
toward these golds (that would launder LLM output into the spec); they are
directional benchmarks that surface disagreements to investigate against
real sources, not ground truth.

## Datasets

### Primary-source gold (`primary_sources`)

`orthography2ipa/data/gold/primary_sources/` — every row is a worked example
printed by a linguist in a source one of our own specs cites: Almbark & Hellmuth
(2015) for Damascene, Jasim (2020) for Baghdadi gilit and Muslawi qəltu, Fadda
(2016) for Ammani, Cotter (2016) for Gaza City, Brissos (2014) for the European
Portuguese central-interior and southwestern dialects, and the JIPA *Illustrations of
the IPA* word lists for Ukrainian (Pompino-Marschall, Steriopolo & Żygis 2017),
Russian (Yanushevskaya & Bunčić 2015), European Portuguese (Cruz-Ferreira 1995) and
Brazilian Portuguese (Barbosa & Albano 2004) — the last two cited by the `pt-PT` and
`pt-BR` specs themselves. the Castilian (Martínez-Celdrán, Fernández-Planas & Carrera-Sabaté 2003) and Argentine
(Coloma 2018) Spanish Illustrations. 270 rows, 13 varieties.

Each row carries the source id, the **printed** page (not the PDF page index —
they diverge, and `sources.json` records the offset per source), the source's own
notation verbatim, whether the source wrote it broad `/…/` or narrow `[…]`, and a
confidence. Nothing is silently coerced: transliterated rows can never be
`confidence: high`, and the Arabic input words carry editor-supplied ḥarakāt,
flagged per row.

It is deliberately small and deliberately adversarial: several rows exist
*because* the source contradicts the spec (gilit kaf affrication is not
front-vowel-conditioned; Ammani emphasis spreads onto a final /t/; the Beira and
Alentejo chain shifts are modelled only in their /u/ → [y] leg). The dataset
README lists all of them. Diagnose rules with it; do not gate a language on
`N=12`. Where a source's PDF mangles its own IPA (scans, legacy fonts), the rows are
transcribed from a render of the printed page — never decoded from the mangled bytes.

### Portuguese unified pronunciation lexicon (`portuguese_unified`)

[TigreGotico/portuguese-unified-pronunciation-lexicon](https://huggingface.co/datasets/TigreGotico/portuguese-unified-pronunciation-lexicon)
(~598k rows / 121,938 words, CC BY-SA 4.0) merges the three previous
Portuguese golds into one convention-normalized dataset and REPLACES their
separate loaders here:

- **Infopédia** (Porto Editora) — 102,685 dictionary extractions (European
  Portuguese, broad phonemic);
- **Portal da Língua Portuguesa** (INESC-ID) — the 10-region semi-automated
  phonetic lexicon (53,349 words);
- **pt.wiktionary.org** — 15,720 community-transcribed words with explicit
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

Core wired tags: `gl`, `es`, `pt`, `pt-BR`, `en`, `en-GB`.

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

Diacritization is input **normalization** and lives in the harness —
orthography2ipa itself does no normalization by design; a downstream
Arabic consumer is expected to feed vocalized (or diacritizer-restored)
text. Both rows are published: raw (deployment floor on bare text) and
diacritized (what the rules actually earn on vowelized input).
`text2tashkeel` is an optional dependency; without it the row is
skipped, never faked. The diacritized words are cached in
`.benchmark_cache/wikipron_ar_diacritized.tsv` for reproducibility —
delete the file to re-diacritize.

Additional wired languages — all from `data/scrape/tsv/` on the
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

Broad-mode normalization (`normalize(..., broad=True)`, the harness
default) folds narrow place-of-articulation diacritics — dental (U+032A
̪), apical (U+033A ̺), and laminal (U+033C ̼) — along with the other
marks in `_NARROW_MARKS`, so e.g. an apico-alveolar `[s̺]`/`[z̺]` scores
identically to plain `[s]`/`[z]` against a gold set that only writes the
latter. This keeps dialects that transcribe articulatory place detail
(e.g. Mirandese, and the pt-PT-x-trasosmontes/viana/minho/beira/aveiro/
alfena dialects) from being penalized per-sibilant for detail that broad
transcription conventions never encode in the first place. Narrow mode
(`--narrow`) does not fold these marks.

Russian has no `_broad.tsv` in `data/scrape/tsv/`; upstream's own README
states some languages were only scraped in one transcription width
("some languages only have broad or narrow transcriptions, e.g. Russian
only has the latter"), and for Russian that is narrow. The harness's
default (non-`--narrow`) normalization already strips narrow-transcription
diacritics (`_NARROW_MARKS`) before scoring, so `rus_cyrl_narrow.tsv` is
directly comparable to the broad-tier gold used for the other languages
in this table; it is wired despite shipping only as a narrow file, with no
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
on Hugging Face: ~220 word/IPA rows with a `dialect` column, collected by
a native Mirandese speaker
([MdMV](https://commons.wikimedia.org/wiki/User:MdMV_or_Emdy_idk)).
Registered as the row id `mirandese_g2p` and split by that column:
`central` → `mwl` (the Central norm the Mirandese orthography is built on),
`sendinese` → `mwl-x-sendim` (the Sendim sub-dialect), and `raiano` →
`mwl-x-ifanes` (the Raiano/Northern sub-dialect, whose Ifanês variety this
repo tags `mwl-x-ifanes`). Native-speaker provenance makes this the
reference gold and the most trustworthy signal for Mirandese — distinct
from, and more reliable than, any machine-generated Mirandese IPA
dictionary. Its size (especially `mwl-x-ifanes`, `N≈2`) keeps results
indicative rather than statistical: read the confidence interval.

### Barranquenho synthetic IPA dictionary (`barranquenho_dict`)

[TigreGotico/barranquenho-ipa-dict-synthetic](https://huggingface.co/datasets/TigreGotico/barranquenho-ipa-dict-synthetic)
on Hugging Face: 319 word/IPA entries for Barranquenho — the
Portuguese–Spanish contact variety of Barrancos — mapped to the
`ext-PT-x-barrancos` spec. Each row also carries part-of-speech, the
Portuguese and Spanish equivalents, and a phonological note; only the
orthography and IPA columns are scored (Barranquenho is Latin-script, so
no special input contract applies).

**Provenance — read this before trusting the number.** The IPA was
**generated by a large language model (Claude)** conditioned on the
published *Convenção Ortográfica do Barranquenho* and descriptive research
on the variety. It was **not** produced by a phonemizer, by
orthography2ipa, or by any downstream o2i consumer, so scoring o2i against
it is **not circular** — but it is unverified by human phoneticians and
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
| `central`, `all` | `mwl` | Central norm the orthography is built on; `all` = forms shared by every variety |
| `sendinês` | `mwl-x-sendim` | Southern Sendinês |
| `raiano` | `mwl-x-ifanes` | Ifanês **is** the Northern/Raiano subdialect in this repo's spec set (only 4 rows — read the CI, not the point PER) |

**Provenance — read this before trusting the number.** As with
`barranquenho_dict`, the IPA was **generated by a large language model
(Claude)** conditioned on the *Convenção Ortográfica da Língua Mirandesa*
and descriptive sub-dialect research — **not** by a phonemizer, by
orthography2ipa, or by any downstream o2i consumer (so **not circular**),
but unverified by human phoneticians and possibly wrong. Lowest
(`machine-generated`) tier, **directional only**; disagreements point to
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
| `Projecte BSC frases - Nord-Occ.tsv` | `ca-x-occidental` | Northwestern/Lleidatà — **not** `ca-x-nord` (Northern Catalan/Rossellonès, a distinct dialect spoken in France that 4catac does not cover) |
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
/ɛ/`; the loader emits each variant as its own gold pair, and the scorer
keeps the best-matching one). The project is MIT-licensed; each
third-party dataset keeps its own licence.

**Read the tier before the number.** ipa-dict is not one source. Its
README Credits section — the only authority on where each file's IPA came
from — shows it mixing published human dictionaries, Wiktionary scrapes,
rule scripts and phonemizer output in a single repository, so this dataset
is classified **per language** (`_IPADICT_PROVENANCE` in
`scripts/benchmark.py`, surfaced per row by `provenance_for`). The
notorious case is **`en_UK`, which is espeak output**: it is credited to
[ipacards](https://github.com/leoboiko/ipacards), whose own `CREDITS` and
`bin/add-ipa-to-freq.py` shell out to `espeak`. That row measures agreement
with a competitor, so per [quality tiers](quality_tiers.md) it can **neither
qualify nor block** English — read the CMUdict and WikiPron English rows
instead. Where the Credits section names no source at all, the file is
classified `machine-generated` with the provenance recorded as UNVERIFIED;
a tier is never upgraded on a guess.

| Lang | ipa-dict file | Tier | Source (per the ipa-dict README Credits) |
|---|---|---|---|
| `is` | `is.txt` | lexicon-derived | [Pronunciation Dictionary for Icelandic](http://malfong.is/?pg=framburdur&lang=en) (Hjal project, malfong.is), CC BY 3.0 — human-curated by Icelandic linguists. Higher coverage (~60k) than WikiPron `isl` (~11k): the primary Icelandic gold, with WikiPron as cross-check. |
| `en-US` | `en_US.txt` | lexicon-derived | [cmudict-ipa](https://github.com/lingz/cmudict-ipa) (CMU hand-curated ARPABET) + [syllabify](https://github.com/kylebgorman/syllabify) stress, MIT. Same lineage as the `cmudict` row, different notation transform. |
| `ja` | `ja.txt` | lexicon-derived | [EDICT](https://www.edrdg.org/jmdict/edict.html) readings (EDRDG), CC BY-SA 3.0. Only the kana entries score: kanji headwords transcribe to `''` and drop out of `N`. |
| `jam` | `jam.txt` | lexicon-derived | [A Learner's Grammar of Jamaican](https://github.com/opengrammar/jam-learners-grammar) (Open Grammar Project), CC BY 4.0. |
| `km` | `km.txt` | lexicon-derived | [Khmer-English Dictionary](https://www.aakanee.com/AC-Khmer/X/dict.html) (aakanee.com), CC BY-NC-SA 4.0. |
| `ro-RO` | `ro.txt` | lexicon-derived | [MaRePhoR](https://speech.utcluj.ro/marephor/) phonetic dictionary (UTCluj), CC BY-NC. |
| `sv` | `sv.txt` | lexicon-derived | [Folkets lexikon](https://folkets-lexikon.csc.kth.se/folkets/) (KTH), CC BY-SA 2.5. |
| `de-DE` | `de.txt` | crowd-scraped | [german-ipa-dict](https://github.com/devio-at/german-ipa-dict), built from Wiktionary, CC BY-SA. |
| `ar` | `ar.txt` | machine-generated | Tim Buckwalter's Arabic Morphological Analyzer output. |
| `es-ES` | `es_ES.txt` | machine-generated | [spanish-pronunciation-rules](https://github.com/easypronunciation/spanish-pronunciation-rules-php) PHP script; README calls it "experimental". |
| `es-MX` | `es_MX.txt` | machine-generated | Same script; the file is near-identical to `es_ES` (the two differ by ~11 lines), so the two rows are not independent evidence. |
| `fa` | `fa.txt` | machine-generated | Wiktionary + [PersPred](http://perspred.cnrs.fr/perspred-project) + "a great deal of guesswork"; README: "extremely experimental". |
| `fi` | `fi.txt` | machine-generated | [prosodic1b](https://github.com/jsfalk/prosodic1b) (rule-based) over the Kotus wordlist, GPL 2.0. |
| `nl` | `nl.txt` | machine-generated | Instituut voor de Nederlandse Taal, CC BY — README: "an automated conversion from different data sources … no manual correction or revision has been done". |
| `or` | `or.txt` | machine-generated | [OdiaWikimedia Converter](https://github.com/OdiaWikimedia/Converter/tree/master/IPA-Romanization) over Wikimedia dumps. |
| `vi` | `vi_N.txt` | machine-generated | [vPhon](https://github.com/kirbyj/vPhon) converter over Ho Ngoc Duc's wordlist. Northern/Hanoi = the standard the `vi` spec targets. |
| `nb` | `nb.txt` | machine-generated | Base generation method **undocumented**; the README credits Dr. Espen Stranger-Johannessen for *correcting and updating* it, which is not evidence of expert authorship — so the tier is not upgraded. |
| `eo` | `eo.txt` | machine-generated | **PROVENANCE UNVERIFIED** — the Credits section names no source for Esperanto. |
| `fr-FR` | `fr_FR.txt` | machine-generated | **PROVENANCE UNVERIFIED** — no source credited for French. |
| `ms` | `ma.txt` | machine-generated | **PROVENANCE UNVERIFIED** — no source credited. ipa-dict's `ma` is "Malay (Malaysian and Indonesian)", i.e. the `ms` spec, *not* Moroccan Arabic. |
| `pt-BR` | `pt_BR.txt` | machine-generated | **PROVENANCE UNVERIFIED** — no source credited for Brazilian Portuguese. |
| `sw` | `sw.txt` | machine-generated | **PROVENANCE UNVERIFIED** — no source credited for Swahili (the entries even preserve capitalisation in the IPA, e.g. `Abadoni /Aɓaɗoni/`). |
| `en-GB` | `en_UK.txt` | **espeak-derived** | [ipacards](https://github.com/leoboiko/ipacards) (GPL 3.0), whose CREDITS list "Espeak" and whose `bin/add-ipa-to-freq.py` calls `espeak` directly. **Cannot qualify or block English.** |

Files deliberately **not** wired (recorded in `_IPADICT_UNWIRED`):

| File | Why not |
|---|---|
| `zh_hans`, `zh_hant` | Han-script gold, and no spec can read it: `zh` is a **pinyin/romanization** spec (`OrthographyKind.ROMANIZATION`), and the Han-script `zh-Hani` spec emits nothing for Han characters (`G2P("zh-Hani").transcribe_word("一") == ""`). Forcing either would produce a `PER=1.0`, `N=0` non-result. The two files carry identical pronunciations anyway (they differ only in written standard). |
| `yue` | Same: Han-script gold, and `G2P("yue")` emits nothing for it. The gold itself (KFCD Pingyam + 開放粵語詞典, CC BY 3.0) is good — the gap is on our side. |
| `ko` | Same: Hangul gold (Korean Wiktionary via [korean-word-ipa-dictionary](https://github.com/laviande22/korean-word-ipa-dictionary), CC BY-SA), and `G2P("ko")` emits nothing for Hangul syllable blocks. |
| `fr_QC` | No Québécois spec is registered. The file is also qc-ipa script output over `fr_FR` ("highly experimental"). |
| `tts` | Isan / Northeastern Thai ([Isaan-English Dictionary](https://www.aakanee.com/AC-Isaan/X/dict.html), CC BY-NC-SA 4.0). No `tts` spec; the `th` spec is a different language and must not stand in for it. |
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
sides, and collects deduplicated single-word pairs. This loader carries an
intrinsic, language-agnostic bound that `--limit` cannot lift: it stops
after `_HITZ_BASQUE_MAX_PARAGRAPHS` (500) paginated paragraphs rather than
pulling the full 1.67M-row set, so even the full `--scoreboard` run scores
the word pairs harvested from those first 500 paragraphs, not the entire
corpus. This is the one dataset that remains bounded under the full
scoreboard, and it is bounded by paging infrastructure (uniformly, not
per language), not by a sampling `--limit`. Single word-tokens are used as
the scored unit —
following `load_ep_dialects`'s precedent of scoring non-lexicon-shaped
gold through the harness's standard `transcribe_word`/PER pipeline —
rather than whole sentences, since paragraph-level ahoNT stress
placement is not verified to depend on sentence context, making the
single-token span the more conservative unit to score in isolation.

### VoxCommunis parallel G2P (`vox_communis`)

[fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)
(CC0): Common Voice utterances force-aligned by the VoxCommunis Corpus,
with per-utterance phone strings whose lexicons were built with **Epitran,
the XPF Corpus, Charsiu and custom dictionaries** (partially hand-corrected
by VoxCommunis, but not attributably per row). One small TSV per language;
71 language tags are wired (every per-language file with a matching spec,
plus a few regionalised aliases — `sv-se`→`sv`, `zh-cn`→`zh`, `hy-am`→`hy`,
`fy-nl`→`fy`, `pa-in`→`pa`, and the region-untagged `pt` file under `pt-BR`,
the same policy as the WikiPron generic-pt row).

The `phonemized_sentence` column is space-separated phones with `|` between
words, aligned with the whitespace-tokenized `aligned_sentence`; rows are
split into word-level pairs like `ipa_childes`, skipping token-count
mismatches and stripping alignment artifacts.

**Tier: `epitran-derived`** — Epitran is a scored competitor in
[comparison.md](comparison.md), so a disagreement here measures divergence
from a competitor's output. Directional breadth signal only; can never gate
a regression or qualify a spec for the production tier.

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
from this dataset are accepted as gold here — but **which** tool matters,
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
| `de-DE` | `de-DE` | `epitran`, `deu-Latn` | epitran-derived | 24859 | 0.3881 |
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
competitor-derived — but it is still a tool's output and still cannot be
read as truth. The Mandarin row is also read through the tokenizer that
[#305](https://github.com/TigreGotico/orthography2ipa/pull/305) reworks for
Han/punctuation input, so its number on this branch may move.

Only the `test` split is read (held out from G2P+ training). The loader (`load_ipa_childes` in
`scripts/benchmark.py`) splits each row's orthographic sentence and its
`ipa_g2p_plus` column on whitespace/`" | "` respectively, pairs tokens
positionally, skips rows whose token counts don't line up, and collects
deduplicated single-word pairs (the full `--scoreboard` run reads the whole
test split; `--limit N` keeps only the first N) — the same
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
- **`yue-CN`** (Cantonese): the `yue` spec is a stub with an **empty
  grapheme inventory** (Cantonese is written in Chinese characters, and the
  stub claims no letter-to-sound mapping); the dataset's own romanized
  column is Jyutping-with-tone-numbers, which the stub does not model
  either, so `G2P('yue').transcribe_word(...)` returns `""` for every row.
  A spec gap, not a gold problem.

### IPA-BabyLM (`ipa_babylm`)

[phonemetransformers/IPA-BabyLM](https://huggingface.co/datasets/phonemetransformers/IPA-BabyLM)
on Hugging Face: the BabyLM 2024 pre-training corpora (BNC spoken, CHILDES,
Gutenberg, OpenSubtitles, Simple Wikipedia, Switchboard) converted to
phonemes with [G2P+](https://github.com/codebyzeb/g2p-plus). English only.
The two configs (`strict`, `strict-small`) differ **only** in their train
split and share one `dev` split, so there is exactly one gold set here, not
two; the harness reads the held-out `dev` split alone, never the train
portions the LMs were pre-trained on.

**Provenance — espeak, at one remove.** G2P+ is a *wrapper*: its backends
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
**PER 0.5257** — a high number that says o2i's English diverges *from
espeak* on a corpus of conversational/literary text; it is agreement, not
accuracy, and the far more informative English rows are `cmudict`
(lexicon-derived) and `wikipron`.

**Licence:** the dataset card declares none; the underlying BabyLM corpora
keep their own licences. Eval-only use.

## Rejected candidates

Datasets investigated and excluded due to tool-generated or unclear
provenance:

| Dataset | Verdict | Evidence |
|---|---|---|
| **[dsvv-cair/ipa-transcription-datase](https://huggingface.co/datasets/dsvv-cair/ipa-transcription-datase)** (English, 122,594 rows, CC BY-NC 4.0) | **REJECTED — LLM-generated (GPT-4o Mini)** | The dataset card states it plainly: *"we constructed a large-scale, phonemically rich dataset using the **GPT-4o Mini API**"*. This is LLM-hallucinated IPA, and it is strictly worse than espeak/epitran gold rather than merely different: espeak and epitran are deterministic rule systems with characterisable failure modes, so a disagreement can be traced to a rule and adjudicated; an LLM has no lexicon, no G2P model and no rules, so its errors are unbounded, uncorrelated, and **not attributable to anything**. Scoring against it would measure "agreement with an LLM's guess" and would carry no diagnostic information. Not wired in any tier — the licence (CC BY-NC, fine for eval-only gold) is not the reason; the absent error model is. |
| **ipa-dict (tool-generated files: `ar`, `es_*`, `fa`, `fi`, `nb`, `nl`, `or`, `vi_*`, and the espeak-derived `en_UK`)** | WIRED, TIERED — not rejected | Each is registered with the tier its own provenance earns (`machine-generated`, or `espeak-derived` for `en_UK`), never `lexicon-derived`; see [ipa-dict pronunciation dictionaries](#ipa-dict-pronunciation-dictionaries-ipadict). A tool-generated gold is admitted explicitly, with the caveat travelling on the row — it is not silently promoted, and the espeak row can neither qualify nor block a language. |
| **ipa-dict `fr_QC.txt`** | EXCLUDED — no spec | No Québécois French spec is registered; the file is also qc-ipa script output over `fr_FR` ("highly experimental"). |
| **ipa-dict `tts.txt`** | EXCLUDED — no spec | Isan / Northeastern Thai; no `tts` spec, and the `th` spec is a different language. |
| **ipa-dict `zh_*`, `yue`** | EXCLUDED — untranscribable | Well-sourced golds (Unihan/KFCD, KFCD Pingyam), but Han script is lexical — no G2P without a dictionary — and the `zh` spec is a pinyin/romanization spec. An engine gap, not a gold problem. The former third member of this row, `ko` (Korean Wiktionary), is WIRED now: Hangul syllable blocks canonically decompose to the `ko` spec's conjoining-jamo graphemes. |
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
PYTHONPATH=$PWD python scripts/error_analysis.py pt-PT --dataset portuguese_unified --limit 300
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
- The committed `--scoreboard` scores the **full** gold set of every
  language (no cap), so each row's `N` is the number of gold words covered,
  not a sample (see
  "Full-dataset scoreboard" below). Ad-hoc `--limit N` runs (and the CI
  regression sample) apply a uniform cap for speed; those are reference
  points, not the published number.

### Full-dataset scoreboard

The committed scoreboard (`docs/scoreboard.md` / `benchmarks/results.json`)
is **full-dataset**: `scripts/benchmark.py --scoreboard` scores the entire
gold set of every registered dataset/language with **no cap**, applied
uniformly (there is no per-language limit). The `N` column is therefore the
real number of covered gold words, not a sample size. Regenerating it is
slow (the 598k-row `portuguese_unified` gold
dominates the runtime), which is why the CI regression gate does *not* re-run
it in full — see below.

`--limit N` still exists for ad-hoc fast runs and applies the **same** cap
`N` to every language (never a per-language mix). The one dataset that stays
bounded even under the full run is `hitz_basque_ipa`: its loader pages the
Hugging Face rows API and stops at `_HITZ_BASQUE_MAX_PARAGRAPHS` (500)
paragraphs rather than pulling the full 1.67M-row corpus — a fixed,
language-agnostic paging bound, not a sampling `--limit`, disclosed in its
dataset section above.

**CI regression strategy (full-vs-sample would be dishonest, so it isn't
done).** Re-running the full scoreboard inside a PR CI job is too slow to be
practical, but comparing a *sampled* current run against the *full* baseline
would compare two different slices and manufacture spurious "regressions".
So the gate never mixes slices: `scripts/check_benchmark_regression.py`
re-scores at a fixed **uniform** sample (`benchmark.CI_SAMPLE_LIMIT`, the
same cap for every language) and compares against a **separate** baseline
committed at that identical cap, `benchmarks/results_ci_sample.json`
(generated by `scripts/benchmark.py --ci-sample`, clearly labeled the "CI
regression sample"). Both sides are sliced identically, so a flagged
regression is a real PER change, not slice noise. The published docs
scoreboard stays full regardless. A minimum-scored-row floor still fails the
gate closed if a wholesale dataset-loading outage would otherwise produce a
false green. Refresh `results_ci_sample.json` whenever the full scoreboard is
regenerated.

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

### Rules-only vs with-lexicon PER (lexicon overlay)

Languages that ship an optional lexicon overlay
(a caller-registered TSV, never bundled — see
[`data_model.md`](data_model.md#lexicon-overlay-sidecar-word_exceptions-at-scale))
are scored **twice** on the same gold — once with the lexicon disabled
(`get_lexicon` stubbed to `{}`, the "rules-only PER") and once with it active
(the "with-lexicon PER"). This keeps rule quality honest: the overlay has to
*improve* PER without letting the underlying grapheme rules rot behind lexicon
coverage. The results live in a dedicated report, separate from the main
scoreboard (which is untouched — languages with no lexicon are byte-identical
with or without this feature):

```bash
python scripts/benchmark.py --lexicon-report
```

writes [`lexicon_scoreboard.md`](lexicon_scoreboard.md) and
`benchmarks/lexicon_results.json`. Each row reports both the **full-slice**
delta and the **covered-subset** delta (scoring restricted to gold words the
lexicon actually contains — where the overlay can act). The covered-subset
delta is the honest measure of the lexicon's own accuracy vs the rules on the
*same* words; the full-slice number is diluted by every gold word outside the
deliberately capped, top-frequency pilot lexicon. The shipped `en-GB` pilot
(CMUdict-derived, General American) cuts PER on covered words roughly in half
against the independent WikiPron gold — the pilot proves the mechanism; full
production lexica belong downstream.

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
these numbers. One language (`en-US`) needs the optional `scriptconv`
loader, and a handful of sentence-level sources (`ca` and its regional
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


---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Scoreboard](scoreboard.md) · [Quality tiers](quality_tiers.md) · [Comparison](comparison.md)*
