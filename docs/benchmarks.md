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
IPA-transcribed word list for most of the languages here: so the
datasets below are, in honest descending order of trust,
phonetician-curated, native-speaker-collected, dictionary-extracted,
Wiktionary-scraped, or **a phonemizer's own output reused as a
reference**. This is not a defect to hide. It is the state of the field,
and it changes how every number on the [scoreboard](scoreboard.md) must
be read:

- **A gold set's value is its error model.** Human/lexicon gold is
  trustworthy. Rule-system gold (espeak, epitran) measures *agreement with a
  competitor*: informative, because a deterministic rule system's
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
  confirms the tool reproduces itself: it is not evidence of
  correctness. The same trap applies to any comparison where the
  evaluated system shares the gold's generator: use an **independent**
  gold (here, `wikipron` `eu`) for the fair comparison.
- **Comparing o2i to espeak on an espeak-derived gold is partly
  circular** for the same reason. `vox_communis`, `ipa_babylm` and the
  `phonemizer`-phonemized `ipa_childes` languages are all
  phonemizer/espeak-lineage. An espeak-vs-o2i table on that gold measures
  how similarly two systems diverge from the truth, not who is closer to
  it. **The same trap applies to epitran**, which
  [comparison](comparison.md) also benchmarks o2i against (`epitran_per`):
  the six `epitran`-phonemized `ipa_childes` languages are epitran's own
  output, so treating them as truth would double-count epitran as both rival
  and referee.
- **Absolute PER is noisy: treat it as directional, not precise.** The
  published scoreboard scores the **full** gold set of every language (see
  "Full-dataset scoreboard" below), so its `N` is the number of gold words
  actually covered: not a sample: and its
  PER is the whole-set number: but PER is still bound by the gold's own
  notation conventions and provenance, so read numbers as relative/ranking
  signals, not measurements to three decimals.
- **Small-`N` rows are anecdotes.** Many `clup_dialect` rows are `N=1-17`
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
single tier would be a lie: ipa-dict ships a human Icelandic dictionary,
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
| **expert-human** | IPA curated by phoneticians, trained annotators, or native speakers. | Still bound by the team's notation conventions. Here often small-`N` and/or not peer-validated. |
| **lexicon-derived** | Human lexicographers, via a published dictionary's notation: sometimes through a mechanical notation transform (ARPABET→IPA, slashed-phonemic→IPA). | Dictionary conventions ≠ surface phonetics. The transform step can add its own artifacts. |
| **crowd-scraped** | Wiktionary community edits (WikiPron). | Uneven per language. Some entries are themselves editor-applied rule output, not attested transcriptions. |
| **machine-generated** | A phonemizer's *own output* reused as the reference. | **Biggest grain of salt.** Low PER = agreement with that tool, not correctness. |
| **espeak-derived** | A **competitor's** output reused as the reference: espeak-ng, directly or through a wrapper (`ipa_babylm` via G2P+, the `phonemizer`-phonemized `ipa_childes` languages). | **Never gate a quality decision on this.** The row measures *agreement with espeak*: and espeak is a system we benchmark ourselves *against* ([comparison](comparison.md)). Diverging from it can mean we are right and it is wrong, which shows up here as a *worse* score. Quality also varies by language. Judge any divergence against a cited source, never against this number. Kept for its breadth as a directional signal. |
| **epitran-derived** | A **competitor's** output reused as the reference: [epitran](https://github.com/dmort27/epitran) (the six `epitran`-phonemized `ipa_childes` languages: `de-DE`, `es-ES`, `hr`, `hu`, `id`, `sr`). | **Never gate a quality decision on this**: same reason as `espeak-derived`, and epitran is likewise a system [comparison](comparison.md) scores us against (`epitran_per`). Scoring o2i against epitran's own output and calling it gold would count the same system as both rival and truth. Still diagnostic (epitran is a deterministic rule system, so a disagreement can be traced to a rule and adjudicated against a cited source), but never certifying. |
| **llm-generated** | The gold was produced by a large language model (`barranquenho_dict`, `mirandese_dict`: Claude, research-conditioned, `arabic_tts`, `portuguese_tts`: LLM-drafted, engine-pinned, literature-audited, `gold20_arabic`: LLM-drafted, native-speaker spot-checked). | **Worst of all, and never a gate.** An LLM has no lexicon, no G2P model and no rules, therefore **no error model**: it emits plausible-*looking* IPA that can be confidently wrong with no systematic structure, and a disagreement cannot be attributed to anything. Certifies nothing and diagnoses nothing. Read as a curiosity, not as evidence. This is why the GPT-4o-Mini-generated `dsvv-cair` dataset is [rejected outright](#rejected-candidates) rather than wired. |

### Per-dataset classification

Every dataset registered in `scripts/benchmark.py`'s `DATASETS`,
classified by reading its loader (source URL, docstring, transform) and
its section below. Where the evidence is incomplete, the uncertainty is
stated rather than papered over.

| Dataset | Tier | IPA produced by | Notes / grain of salt |
|---|---|---|---|
| `primary_sources` | expert-human | The phonologists and dialectologists the specs cite | Example transcriptions copied out of the cited grammars/monographs/theses, one printed page per row (`N=664` across 36 varieties). The most authoritative gold here: and the smallest. Arabic ḥarakāt on the input side are editor-supplied (the sources print transcription, not script). See the dataset README. |
| `arabic_tts` | llm-generated | **LLM-authored, literature-audited** | Sentence-level TTS gold, one TSV per lect across 33 Arabic varieties (`N=20`/lect). Every IPA line was drafted by a large language model, then **engine-pinned** (aligned to the current o2i output) and audited row-by-row against the phonological literature cited in each row's `notes` column ([docs/arabic-tts-gold.md](arabic-tts-gold.md)). Citation-auditing raises confidence but does **not** create an error model: no lexicon, no rules behind the gold: so the honest tier stays `llm-generated`: directional only, gates nothing. Because the gold is engine-pinned it doubles as a regression fixture (PER≈0 on the pinned engine), so a nonzero PER here flags a spec change, not necessarily an error. |
| `gold20_arabic` | llm-generated | **LLM (Claude), native-speaker spot-checked** | [`Salesteq/arabic-dialects-gold20`](https://huggingface.co/datasets/Salesteq/arabic-dialects-gold20) on Hugging Face — a SIBLING gold set to `arabic_tts`, same shape (one TSV per lect, `N=20`/lect, 33 Arabic varieties, vocalized `sentence` in, broad `ipa` gold), fetched at runtime and cached (never vendored). Semi-synthetic: every transcription was drafted by the same Claude lineage that authored the o2i Arabic dialect specs it is scored against — a **near-circular** relationship — then **spot-checked by a native Arabic speaker who judged the set good**. That spot-check is documented context, not a tier upgrade: it is not a systematic per-row audit against cited literature (unlike `arabic_tts`'s `fable_corrections` column), so there is still no lexicon and no rule system behind the gold. Registered anyway because for most of these Arabic dialects **no other gold exists at all** — a directional signal is better than none, not evidence the number can be trusted numerically. Tier stays `llm-generated`, the lowest: gates no quality decision, certifies nothing. |
| `portuguese_tts` | llm-generated | **LLM-authored, literature-audited** | Sentence-level TTS gold, one TSV per lect across European Portuguese standard + 15 regional varieties (`N=20`/lect). Same protocol and caveats as `arabic_tts`: LLM-drafted, engine-pinned, audited against the citations in each row's `notes` ([docs/portuguese-tts-gold.md](portuguese-tts-gold.md)). `llm-generated` tier: directional/regression signal only. |
| `ep_dialects` | expert-human | TigreGotico team, manual annotation | Internal dialect research, **pending external peer validation**. Sentence-level, `N≈29-45`. |
| `mirandese_g2p` | expert-human | Native Mirandese speaker | The reference gold and **most trustworthy signal for Mirandese** (row id `mirandese_g2p`, from `TigreGotico/mirandese_g2p`), split by the `dialect` column: central → `mwl` (`N≈205`), sendinese → `mwl-x-sendim` (`N≈11`), raiano → `mwl-x-ifanes` (`N≈2`: an anecdote, read the CI not the point PER). Small-`N`. A separate, more reliable source than any synthetic Mirandese IPA dictionary. |
| `4catac` | expert-human | Expert annotators (Projecte AINA/BSC) | IEC guidelines, multi-annotator consensus review. Sentence-level, `N=160`, `0.00` exact-match reflects notation/connected-speech mismatch, not total failure. |
| `clup_dialect` | expert-human | U.Porto CLUP dialect archive | Interview corpus is expert university dialectology, **but who/what produced the IPA column (`ArquivoDialetalCLUP_ipa`) is not documented in the loader or dataset card: treat the tier as "best case".** Many rows `N=1-17`: read the CI, not the point PER. |
| `coruss_ru` | expert-human | SPbU phonetics lab, transcribed from audio | The CoRuSS phonetic dictionaries (Kachkovskaia et al. 2016, LREC), published by the Saint Petersburg State University phonetics lab as a RAR archive of `word [transcription] count` rows over read speech, monologues and dialogue. Expert human transcription with no engine in the loop, in the lab's own ASCII notation (documented at [russpeech.spbu.ru/transkrip.htm](https://russpeech.spbu.ru/transkrip.htm)) mapped to IPA by the loader. **Surface-phonetic and colloquial**: it records what a speaker actually said in unscripted conversation, syllable deletions and all (⟨Александровна⟩ [lʲiksanə], ⟨Волгоград⟩ [vodɡrat]), so a G2P cannot reach a low PER here and is not meant to. Read the number as the distance to spontaneous-speech surface forms and compare it only against other runs on this dataset, never against a lexicon gold's PER. Every attested realization of a wordform is kept, so the row is multi-reference. |
| `portuguese_unified` | lexicon-derived | Infopédia + Portal da Língua Portuguesa + pt.wiktionary.org (convention-normalized merge) | Single Portuguese gold (`TigreGotico/portuguese-unified-pronunciation-lexicon`, ~598k rows / 122k words, CC BY-SA 4.0), replacing the three separate golds it merges. One region per registered tag (see `_PT_UNIFIED_REGIONS`). `ipa_narrow` is scored. Untagged plain-`pt` rows are excluded. The Infopédia/Portal majority is dictionary/semi-automated lexicography and the Wiktionary minority is crowd-scraped: directional, not peer-validated ground truth. |
| `cmudict` | lexicon-derived | CMU Speech Group (hand-curated ARPABET) | Human labels, but **mechanically mapped ARPABET→IPA** via `scriptconv`. The transform adds artifacts. |
| `ipadict` | **per-language** (see below) | Depends on the file: human dictionaries, Wiktionary scrapes, rule scripts, **espeak** | The only mixed-provenance dataset here: ipa-dict is a *collection* of independently sourced files, so each row carries the tier of the file it was scored against, not a dataset-wide tier. Full per-language table in [ipa-dict pronunciation dictionaries](#ipa-dict-pronunciation-dictionaries-ipadict). |
| `wikipron` | crowd-scraped | Wiktionary editors | Quality tracks community size. Some entries are editor-rule output, not attested. Multiple valid variants per word. **On a few small-community tags the IPA column is not editor-typed at all but the output of a Wiktionary Lua module, which makes those rows a reproduction test rather than an accuracy test: see [Module-generated WikiPron rows](#module-generated-wikipron-rows).** |
| `wikipron_ar_diacritized` | crowd-scraped | Wiktionary editors + `text2tashkeel` input restoration | Same Arabic gold IPA as `wikipron`. Only the INPUT word is machine-diacritized (~2% DER noise floor). Diagnostic for the vowelized-Arabic rules. Certifies nothing beyond the raw row. See [Arabic with tashkeel restored](#arabic-with-tashkeel-restored-wikipron_ar_diacritized). |
| `ipa_childes` | **per-language** (see below) | Depends on the language: `phonemizer` (espeak-ng), `epitran`, or `pinyin_to_ipa` | Mixed-provenance like `ipadict`: the IPA-CHILDES card names a **different phonemizing tool per language**, so each row carries the tier its own tool earns: `espeak-derived`, `epitran-derived`, or `machine-generated` for Mandarin's `pinyin_to_ipa` table. Full per-language tool table in [IPA-CHILDES split](#ipa-childes-split-ipa_childes). |
| `ipa_babylm` | espeak-derived | G2P+ with the `phonemizer` backend (= espeak-ng), `en-us` | BabyLM 2024 corpora phonemized by [G2P+](https://github.com/codebyzeb/g2p-plus), which is a wrapper over `phonemizer`/`epitran`. The conversion notebook ([codebyzeb/babylm-ipa](https://github.com/codebyzeb/babylm-ipa)) calls the `phonemizer` backend, which requires espeak-ng. So this is espeak output: it can neither qualify nor block English. |
| `hitz_basque_ipa` | machine-generated | HiTZ **ahoNT / AhoTTS** phonemizer | University-published (HiTZ/UPV-EHU), but the gold **is ahoNT/AhoTTS output**: it was generated by that phonemizer, not human-annotated. So a low PER **for the AhoTTS/ahotts-g2p engine on this row is near-tautological** (a tool scored against its own output). The independent, Wiktionary-sourced `wikipron` `eu` row is the fair comparison for Basque. |
| `barranquenho_dict` | llm-generated | **LLM (Claude), research-conditioned** | IPA generated by a large language model prompted with the *Convenção Ortográfica do Barranquenho* and descriptive research on the variety: **not** a phonemizer, not orthography2ipa, not any downstream o2i consumer, so scoring o2i against it is **not circular**. But LLM IPA can be plausibly wrong and is **not human-verified**: directional only. |
| `mirandese_dict` | llm-generated | **LLM (Claude), research-conditioned** | IPA generated by a large language model prompted with the *Convenção Ortográfica da Língua Mirandesa* and sub-dialect descriptions: **not** a phonemizer, not orthography2ipa, not any downstream o2i consumer, so scoring o2i against it is **not circular**. Complementary to the native-speaker `mirandese` gold. LLM IPA is plausibly wrong and **not human-verified**: directional only. |
| `northeuralex` | lexicon-derived | Cited published dictionaries, compiled by Dellert et al. | [NorthEuraLex](https://github.com/lexibank/northeuralex) (Dellert et al. 2020), 100+-language wordlist. Each CLDF row cites its source dictionary in `Source`. 18 languages wired (`_NORTHEURALEX_LANGS`): the original 9 plus a wave of 9 more (`udm`, `ady`, `av`, `lbe`, `dar`, `lez`, `lv`, `smn`, `vep`) that had zero gold anywhere before registration. See [Lexibank/CLDF wordlist gold](#lexibankcldf-wordlist-gold-northeuralex-wold). |
| `wold` | lexicon-derived | Cited published dictionaries, compiled by Haspelmath & Tadmor | [World Loanword Database](https://github.com/lexibank/wold) (Haspelmath & Tadmor 2009), 41-language loanword-typology wordlist. 6 languages wired (`_WOLD_LANGS`): 4 `stub`/`skeleton`, 2 already `research`. See [Lexibank/CLDF wordlist gold](#lexibankcldf-wordlist-gold-northeuralex-wold). |
| `kaikki` | crowd-scraped | Wiktionary editors, machine-extracted | [kaikki.org](https://kaikki.org/dictionary/) Wiktextract per-language JSON-lines dumps — a different extraction pipeline over the same Wiktionary source as `wikipron`, not an independent transcriber. 4 languages wired (`_KAIKKI_LANGS`), all zero-gold `skeleton` specs before this registration: `jv` (Javanese, `N=93`, Latin-script entries only — see below), `su` (Sundanese, `N=397`), `lo` (Lao, `N=2305`), `xh` (Xhosa, `N=887`). See [kaikki.org Wiktextract gold](#kaikkiorg-wiktextract-gold-kaikki). |

## Provenance discipline

Because reliable gold is scarce, the harness applies a deliberate
discipline: prefer human/community provenance, and where tool-generated
IPA is admitted, admit it **explicitly, per dataset, with the reason
recorded**: never silently. Six tool-generated sources are wired in: four
are automatic-phonemizer output (`hitz_basque_ipa`, `ipa_childes`,
`ipa_babylm`, `vox_communis`) and two are LLM-generated IPA
dictionaries (`barranquenho_dict`, `mirandese_dict`), each under a
documented, dataset-specific exception (academic-corpus provenance, an
explicit task override, or the LLM-gold rationale below) rather than a
blanket relaxation. Each row carries the tier its own generator earns: `machine-generated`, `espeak-derived`, `epitran-derived` or `llm-generated`: so the caveat above travels with every number it produces, and
`can_gate_promotion()` in `scripts/benchmark.py` refuses the last three as
promotion evidence. Adding another tool-generated source requires the same
explicit call. It is not the default. A gold whose provenance cannot be
established does **not** default to a flattering tier: it is classified at
the most pessimistic tier its evidence permits, or rejected.

The two LLM-generated dictionaries (`barranquenho_dict`, `mirandese_dict`)
sit at the `machine-generated` tier for a specific reason: their IPA was
written by a large language model conditioned on published orthographic
norms and research, so it is unverified by human phoneticians and can be
plausibly wrong. Crucially, though, it was **not** produced by a
phonemizer, by orthography2ipa, or by any downstream o2i consumer: so
unlike the phonemizer golds above, scoring o2i against these carries **no
circularity**. The scoreboard must never be used to "correct" a spec
toward these golds (that would launder LLM output into the spec). They are
directional benchmarks that surface disagreements to investigate against
real sources, not ground truth.

## Datasets

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

Four rows are known to be affected, three of them wired by the small-wikipron sweep:

| tag | what the gold actually is | how to read the row |
|---|---|---|
| `tew` (Tewa, `N=106`) | **entirely** `Module:tew-IPA` output — every headword carries a bare `{{tew-IPA}}` and no hand-typed IPA | **`PER 0.0000` certifies reproduction of `Module:tew-IPA` on 106 words, not accuracy.** The spec was built from the same Martinez (1982) orthography and Sutton (2014) values the module cites, and cross-checked against the module, so engine and gold share a source. |
| `ha` (Hausa, `N=1857`) | **entirely** `Module:ha-IPA` output — a 31-headword random sample carried a bare `{{ha-IPA\|<respelling>}}` template and no hand-typed IPA in all 31 cases | The module computes the IPA column from an editor-typed tone-and-length-marked respelling, not from spoken attestation per entry. Every `ha` row certifies reproduction of that module's output, not independent pronunciation accuracy; see [languages/ha.md](languages/ha.md). |
| `nmy` (Namuyi, `N=354`) | a **mix** of hand-typed IPA and `Module:nmy-IPA` output | Weaker form of the same caveat: part of the row is a reproduction test. The residual error is dominated by unwritten vowel nasalisation, which is a real gap either way. |
| `mn` (Khalkha Mongolian, `N=3528`) | a **mix** of hand-typed IPA and `Module:mn-IPA` output — a 40-headword sample of the raw en.wiktionary source drew roughly three module-generated entries for every hand-typed one | Same weaker caveat as `nmy`: part of the row is a reproduction test rather than an accuracy test. See [languages/mn.md](languages/mn.md). |
| `egy` (Ancient Egyptian, `N=2185`) | mostly `Module:egy-pron` output, invoked through `{{egy-pr}}`, plus hand-typed reconstructions on the same headwords | **`PER 0.0183` certifies reproduction of the codified Egyptological reading convention on 2185 words, not accuracy** — the convention is a way of saying the words aloud, not a reconstruction of how Egyptian sounded, and the spec encodes it from the same published guidelines the module implements. Not comparison-eligible. See [languages/egy.md](languages/egy.md). |
| `th` (Standard Thai, `N≈17k`) | **entirely** `Module:th-pron` output, invoked through a bare `{{th-pron}}` or `{{th-pron\|<respelling>}}` — an 11-word raw-wikitext sample (`เก็บ`, `ก่อน`, `ยิ้ม`, `สัตว์`, `จันทร์`, `รัก`, `บ้าน`, `น้ำ`, `หมา`, `โรงเรียน`, `ประเทศ`) found the template on every headword and no hand-typed IPA anywhere | The module computes tone and vowel length from the spelling (plus the optional respelling argument) the same way the spec's own tone-class/syllable-type analysis would, so a low PER on the tone-bearing part of the row would certify reproduction of that module, not accuracy. The spec does not compute tone (see below), so this does not currently inflate the published number, but it bounds what a future tone mechanism could claim credit for: agreement with `Module:th-pron`'s tone computation is not independent confirmation of it. |

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

#### Tone-marked golds put a floor under a spec that emits no tone (`th`)

WikiPron transcribes Standard Thai with Chao tone letters, and they are
not a garnish: **32% of every character in the `tha_thai_broad` gold** is
a tone letter (79,041 of 246,222 characters across all 18,416 gold rows,
counted after the benchmark normalizer runs; deduplicated to the 17,221
scored headwords it is 73,093 of 228,584, the same 32%), a
count PER charges in full because the letters are ordinary characters to
an edit distance. A spec that emits no tone therefore cannot score below
about 0.32 on this row whatever its segments do, and the published number
splits into a segmental part it can move and a tonal part it cannot.

Thai tone is not unwritten prosody — it is recoverable from the spelling,
from the initial consonant's class crossed with the syllable's type, its
vowel length and any tone mark. What is missing is the mechanism: a spec
can declare a `tone_inventory` (descriptive) and ask for tone symbols to
be docked syllable-finally (`tone_marks_syllable_final`, which only moves
symbols a grapheme table already produced), and neither computes a tone.
Doing so needs a syllable analysis of the WRITTEN word, and the same gap
covers Lao and every other Tai spec scored against a tone-marked gold.

That the gold's tone letters follow the same consonant-class × syllable-type
rule this section describes is not independent confirmation of the rule:
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
not a transcription, and scoring it is not merely noisy but **unbounded** —
PER normalises by the *gold* length, so one real 10-segment word scored
against a 3-character `spn` contributes a per-word PER above 3. Whole
languages were pushed past PER 1.0 by this alone. Share of `spn` tokens in
the affected files (measured 2026-08): `kk` 59.4%, `ab` 46.5%, `cv` 31.3%,
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
`vi`, `pa` and `as` still sit above PER 0.5 (board values 0.5597, 0.6607
and 0.6445 — see [languages/vi.md](languages/vi.md)), and in all three the
distance is a transcription convention rather than a phonological
disagreement: `vi` differs by tone-letter placement, vowel-length marking
and a handful of symbol variants; `pa` by length marking and a small set
of vowel/rhotic symbol choices, plus final-schwa deletion; `as` by length
marking, a similar symbol-choice set, and final-ɔ deletion. Folding those
conventions out by hand brings each row down substantially, but the exact
intermediate figures are not reproduced by any committed script, so they
are not stated here as precise numbers. None of these foldings belong in
`normalize()` — it is the single scorer for every row, and tone-letter
placement in particular is language-specific — so the rows stay as scored
and are read with this offset in mind.

**Known upstream contamination, `sr`.** 35.8% of Serbian tokens carry a
spurious word-initial `z` in the Charsiu-derived phone tier (`не` →
`znɛ`, `и` → `zi`, `а` → `za`). It is never doubled on words that
genuinely start with `з`, so it is an upstream lexicon artifact, not a
transcription convention. It is *not* filtered — there is no way to
distinguish it from a real word-initial /z/ without guessing — and it
inflates the `sr` row by roughly 0.04 PER (0.3298 → 0.2949 with the artifact
removed by hand). Read the `sr` vox_communis row with that offset in mind.

**Tier: `epitran-derived`**: Epitran is a scored competitor in
[comparison.md](comparison.md), so a disagreement here measures divergence
from a competitor's output. Directional breadth signal only. Can never gate
a regression or qualify a spec for the production tier.

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
enhancement, left for a future change. It is out of scope here.

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

Two further Lexibank datasets were inspected and rejected early on, and a
further audit wave (2026-08) inspected 21 more candidates without wiring any
of them — see [Rejected candidates](#rejected-candidates).

**2026-08 gold-hunting wave 1** — all 41 WOLD languages cross-referenced
against the o2i spec registry. Of the 39 not already wired: most already
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
coverage on a 150-row sample and are now wired above.

**FINDING for a future wave:** the `car`/`arn` PER figures in the table above
(0.1578 / 0.3114) do not match `benchmarks/results.json` (0.0857 / 0.0112) —
the doc table appears to predate a later re-run of the harness or a spec
change and was never refreshed. Not fixed here (out of scope: gold
acquisition only, not spec/doc repair), but flagged for the next
housekeeping pass.

### kaikki.org Wiktextract gold (`kaikki`)

[kaikki.org](https://kaikki.org/dictionary/) republishes
[Wiktextract](https://github.com/tatuylonen/wiktextract) (Ylonen 2022)
machine-extractions of Wiktionary as one JSON-lines file per language: each
entry carries a `word` (the headword as written), a `pos`, and a `sounds`
list of `{"ipa": "..."}` objects (often several transcription variants).
It draws on the same underlying Wiktionary community edits as `wikipron` —
a different extraction pipeline over the same source, not an independent
transcriber — so it is tiered `crowd-scraped`, same as `wikipron`.

**2026-08 gold-hunting wave 2** targeted o2i specs with a non-empty
grapheme table and ZERO gold anywhere in this registry. Candidates were
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
  7-vowel description. Best PER of the wave (0.0964).
- **`lo` (Lao):** coverage is excellent (99.3%), but PER is very high
  (0.7225) — **not a gold-quality problem**. Sampling shows the `lo` spec
  currently collapses nearly every vowel to `/o/` regardless of the actual
  Lao vowel sign (e.g. `ລາວ` gold `/laːw˧˥/` vs. engine `/lowo/`; `ຕາ` gold
  `/taː˩(˧)/` vs. engine `/to/`), and the gold's tone diacritics (Lao is a
  six-tone language) are not produced at all. **FINDING for a future
  wave:** the `lo` spec's vowel-sign mapping looks substantially
  incomplete/wrong; this gold row is a real regression fixture for that
  future repair, not evidence against wiring it now (gold acquisition
  only, no spec fixing in this wave).
- **`xh` (Xhosa):** coverage is total, but PER is high (0.5725) because
  kaikki's Xhosa transcriptions are narrow phonetic — vowel length, tone
  (acute/circumflex marks), prenasalization, and breathy voicing are
  marked on nearly every syllable (e.g. `impala` gold `/íᵐpaːlá/` vs.
  engine `/impala/`), none of which the current segmental `xh` spec
  encodes. **FINDING for a future wave:** Xhosa gold is usable but will
  stay high-PER until the spec gains tone/length/prenasalization rules;
  flagged, not fixed here.

Rejected: **Tigrinya** — only 28 of 933 entries in kaikki's Tigrinya dump
carry a `sounds[].ipa` value, too thin to be a usable gold set.

None of `jv`/`su`/`lo`/`xh` promote to `research` from this gold alone:
each already has a cited entry in `sources`, but none has a `stress` block
or a documented stress-exemption in `notes` (Javanese and Sundanese in
particular have predictable — but currently unencoded — penultimate
stress), which `quality_tiers.md` also requires for the `research` tier.
That is a spec-authoring task, out of scope for a gold-only wave.

**FINDING for a future wave:** `open-dict-data/ipa-dict` is fully exhausted
— every one of its 31 upstream files is either wired (`_IPADICT_FILES`) or
explicitly rejected with a reason (`_IPADICT_UNWIRED`), **except**
`zh_hant.txt` (Traditional Chinese), which is documented nowhere. It has the
same problem as the already-rejected `zh_hans`/`yue` entries (Han-script
gold against a Pinyin-romanization `zh` spec), so it should be added to
`_IPADICT_UNWIRED` for completeness, but that is a spec/doc-hygiene fix, not
a gold acquisition, so it is only noted here.

**2026-08 gold-hunting wave 3.** The zero-gold sweep (specs with a
non-empty grapheme table and no row anywhere in `results.json`) was
re-run from scratch rather than reused, since it shrinks with every
wave: 735 zero-gold specs out of 7383 registered codes at the start of
this wave. The highest-population zero-gold specs (Nepali, Bhojpuri,
Awadhi, Sindhi, Igbo, Somali, Fula, Chhattisgarhi, Magahi, Oromo,
Lingala, Shona, Kirundi, Wolof, Konkani, and a few more) were
cross-referenced against kaikki.org's per-language index (size-checked
with a `HEAD` request before any download, same as wave 2, nothing
vendored):

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
  entries were dropped, same rationale as `jv` in wave 2 — no Javanese-style
  majority-foreign-script problem here, just a minority to filter out).
  Every sampled word matches its orthography (`dhagax` → `/ˈɖɑ́ɡɑ̀ħ/`,
  `libaax` → `/lìˈbæ̂ːħ/`). PER is high (0.5937) because kaikki's Somali
  transcriptions are narrow — tone (high/low pitch accent marks), vowel
  length, and pharyngeal/epiglottal detail (`caws` gold
  `/ˈʡ͜ʢǽ͜ʉ̀s/` vs. engine `/ʕaws/`) are marked on nearly every word, none of
  which the current segmental `so` spec encodes. **FINDING for a future
  wave:** Somali gold is usable but will stay high-PER until the spec
  gains tone/length rules; flagged, not fixed here.
- **`om` (Oromo):** clean, single-script (Latin) dump after the
  `_KAIKKI_WORD_FILTER["om"]` restriction. Word/IPA pairing checks out
  (`tokko` → `/ˈtɔ́kkɔ/`, `Waaqa` → `/ˈwɑ́ːkʼɐ/`). Only 53 usable entries
  (thin, like `jv`'s 93 in wave 2) but every one is scorable. PER is high
  (0.5228) mostly from tone/stress marks and a few vowel-quality choices
  (gold's ATR-influenced `ɐ`/`ɔ`/`ɛ` vs. the spec's plain five-vowel
  output) the current spec doesn't encode. **FINDING for a future wave:**
  same tone/vowel-quality gap as `so`.
- **`ne` (Nepali):** by far the largest haul of the wave (2051 scorable
  entries after de-duplication), Devanagari script matching the spec
  directly — no script filter needed. Sampled pairs check out
  (`खतरनाक` → `/kʰʌt̪ʌrnäk/`, `विद्यार्थी` → `/bid̪̚d̪järt̪ʰi/`). PER is
  high (0.6047) almost entirely from one systematic, single-cause
  divergence: the `ne` spec inserts a schwa after every final consonant
  cluster/consonant the gold treats as silent or reduced (`कदर` gold
  `/kʌd̪ʌr/` vs. engine `/kəd̪ərə/`, `दश` gold `/d̪ʌs/` vs. engine
  `/d̪əʃə/`), plus a schwa-vs-`ʌ` vowel-quality mismatch throughout.
  **FINDING for a future wave:** the `ne` spec's schwa-deletion /
  vowel-reduction rules look substantially incomplete; this gold row is a
  real regression fixture for that repair, not evidence against wiring it
  now.
- **`kok` (Konkani):** clean Devanagari-script haul (830 scorable
  entries), same script family as the already-wired-elsewhere Devanagari
  specs. Sampled pairs check out (`आजी` → `/ɑːd͡ʒiː/`, `भाचो` →
  `/bʰɑːt͡sɔ/`). PER is high (0.4944) from the same final-schwa-insertion
  pattern as `ne` (`उठप` gold `/uʈʰəp/` vs. engine `/uʈʰəpə/`) plus
  nasalization the gold marks with a tilde that the spec's segmental
  output doesn't carry (`अदांव` gold `/ədɑ̃ːʋ/` vs. engine `/əd̪aː̃ʋə/`).
  **FINDING for a future wave:** same final-schwa gap as `ne` — likely a
  shared Indo-Aryan-spec fix, not two independent bugs.

None of `so`/`om`/`ne`/`kok` promote tiers from this gold alone. `so`,
`ne` and `kok` were already at `research` (each already has a cited
`sources` entry and a `stress` block/exemption) — this wave only adds
the gold-benchmark row `quality_tiers.md` says `research` should have had
all along; **note for a future hygiene pass:** several other specs in
this registry are marked `research` with zero gold anywhere in
`results.json` (the `test_data_quality.py` guard does not check this for
`research`, only for `production`), so `so`/`ne`/`kok` were not uniquely
missing this — the whole tier is under-enforced. `om` stays `skeleton`:
it has neither a cited source nor a stress block/exemption, which is a
spec-authoring task out of scope for a gold-only wave.

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
- **Tigrinya (`ti`), re-checked** — unchanged since wave 2: still 28 of
  933 entries carry `sounds[].ipa`. Stays rejected for the same
  too-thin reason.

`om`, `ff` (Fula), `ln` (Lingala), `sn` (Shona), `wo` (Wolof), `tw`
(Twi, via kaikki's `Akan` macrolanguage dump) and `st` (Southern Sotho,
via kaikki's generic `Sotho` dump) were all checked; `om` was the only
one of that group with a large enough clean sample after script
filtering to be worth wiring (53 usable entries vs. single digits to
low tens for the rest, several of which turned out to be dictionary
metadata — single-letter "character" entries the existing
`_KAIKKI_EXCLUDED_POS` filter doesn't catch because their `pos` isn't
literally `"character"` — rather than real words). Not wired this wave;
flagged as thin/contaminated candidates a future wave could revisit with
a tighter word-shape filter.

No kaikki.org dump exists (`HEAD` → 404, checked under the language's
common name and obvious alternates) for several other high-population
zero-gold candidates: Bhojpuri, Awadhi, Igbo, Chhattisgarhi, Northern
Sotho, Kirundi/Rundi, Minangkabau, Kongo, Tsonga, Maithili, Venda and
Southern Quechua. Noted here so a future wave doesn't re-spend time on
the same lookup.

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
| **[lexibank/robinsonap](https://github.com/lexibank/robinsonap)** (Alor-Pantar) | **INSPECTED, NOT WIRED: no spec coverage** | `Value` genuinely looks like practical orthography (real digraphs, e.g. `gunnang` → `g u n n a ŋ` shows `ng`→`ŋ`), unlike every other 2026-08 candidate. But all 13 languages (`twe abz beu woi kvw jka lev kvd adn swt nec kyo`, plus a Glottolog-only proto-language row) resolve to `stub`-quality o2i specs with an EMPTY grapheme table — the loader's stub-promotion path requires a non-empty table to exercise, so there is nothing for a gold row to score against yet. Revisit once any of these specs gets a grapheme table. |
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

## Diagnosing a language

The scoreboard tells you *that* a language scores badly. It does not tell
you *why*. `scripts/error_analysis.py` is the microscope: it runs a gold
dataset through the engine and reports where the errors concentrate, so
spec work starts from evidence instead of guesswork. It is strictly
read-only: it never touches a spec or any other file.

```bash
PYTHONPATH=$PWD python scripts/error_analysis.py pt-PT --dataset portuguese_unified --limit 300
```

`<lang>` is required. `--dataset` is optional (when omitted, the first
registered dataset that covers the language is used), `--limit` caps the
gold slice (default 300, same as the benchmark harness), and `--json`
emits all three sections as one JSON object instead of the text report.
Alignment reuses the same routine (`scripts.benchmark.align`) and the
same default normalization (stress marks and narrow diacritics stripped)
that the scoreboard uses, so what you see here matches how PER is scored.

The report has three sections. Read them in this order:

1. **Top-20 phoneme confusion pairs** (`gold -> hyp`). Each row is an
   aligned mismatch, ranked by how often it occurs. `∅` on the gold side
   is an *insertion* (the engine emitted a phoneme the gold does not
   have). `∅` on the hyp side is a *deletion* (the engine dropped a gold
   phoneme). A single high-count pair: e.g. `'r' -> 'ɾ'`: is usually
   one wrong or missing grapheme/allophone rule and the fastest fix.

2. **Top-20 worst words**: the words with the highest per-word PER, gold
   and hyp side by side. Use these to see the confusion pairs *in
   context*: whether a substitution is systematic (every word) or
   conditioned (only before front vowels, only word-finally, etc.), which
   tells you whether the fix is a flat grapheme change or a positional
   rule.

3. **Per-grapheme blame**: for each orthographic character/digraph in
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

- **PER**: character-level Levenshtein distance over IPA, divided by
  reference length. Mean over evaluated words. **WER**: fraction of
  words with any error.
- **Multi-reference**: rows are grouped by word and a hypothesis is
  scored against every gold variant, keeping the minimum PER.
- **Segmentation-free**: whitespace is removed before comparison (some
  gold sets space-separate phonemes).
- **Default normalization**: stress marks and narrow-transcription
  apparatus (raising/dentality diacritics, syllable separators, tie
  bars) are stripped from both sides: gold sets differ in
  transcription depth, and the engine should not be scored on notation
  conventions. `--keep-stress` / `--narrow` disable this.
- The committed `--scoreboard` scores the **full** gold set of every
  language (no cap), so each row's `N` is the number of gold words covered,
  not a sample (see
  "Full-dataset scoreboard" below). Ad-hoc `--limit N` runs (and the CI
  regression sample) apply a uniform cap for speed. Those are reference
  points, not the published number.

### Full-dataset scoreboard

The committed scoreboard (`docs/scoreboard.md` / `benchmarks/results.json`)
is **full-dataset**: `scripts/benchmark.py --scoreboard` scores the entire
gold set of every registered dataset/language with **no cap**, applied
uniformly (there is no per-language limit). The `N` column is therefore the
real number of covered gold words, not a sample size. Regenerating it is
slow (the 598k-row `portuguese_unified` gold
dominates the runtime), which is why the CI regression gate does *not* re-run
it in full: see below.

`--limit N` still exists for ad-hoc fast runs and applies the **same** cap
`N` to every language (never a per-language mix). The one dataset that stays
bounded even under the full run is `hitz_basque_ipa`: its loader pages the
Hugging Face rows API and stops at `_HITZ_BASQUE_MAX_PARAGRAPHS` (500)
paragraphs rather than pulling the full 1.67M-row corpus: a fixed,
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

**Board staleness is a separate failure the regression gate cannot see.**
That gate is one-sided: it fires when a row gets WORSE, so a row left
behind by a change to its own gold loader publishes a stale number
indefinitely and CI stays green. `scripts/check_board_row_counts.py` is
the tripwire for that. It reloads each committed row's gold and fails when
the row's `n` exceeds the pair count the loader now yields, which is an
impossibility — scoring consumes the loader's output, so `n` sits at or
below it. The check is deliberately one-directional, because an `n` BELOW
the pair count is normal: `ja` scores 42.5k of 48.6k pairs, since the kana
spec produces no hypothesis for a kanji-only word. A row whose loader
refuses the language outright is reported too, which catches a board row
fossilised by a de-registration. Run it after every board regeneration:

```bash
PYTHONPATH=$PWD python scripts/check_board_row_counts.py
```

### Confidence intervals

Every scoreboard row (`docs/scoreboard.md` / `benchmarks/results.json`)
carries a 95% bootstrap confidence interval on the mean PER, alongside
the point estimate, so a single-slice PER number can be read with its
uncertainty rather than as a false-precision leaderboard entry:

- The per-word PER list underlying a row's mean PER is resampled with
  replacement 1000 times. The mean of each resample is computed, and
  the interval is the 2.5th/97.5th percentile of that distribution.
- Resampling uses `random.Random(BOOTSTRAP_SEED)` (`scripts/benchmark.py`),
  never the global RNG, with a fixed seed constant: the same input PER
  list always yields the same `[low, high]` bounds, on any machine, on
  any run. This is what makes the CI reproducible rather than a
  moving target that would itself trigger false benchmark-regression
  noise.
- The regression gate (`scripts/check_benchmark_regression.py`) keeps
  comparing the point-estimate PER against the committed baseline with
  its existing epsilon: the CI is a reporting/diagnostic addition, not
  part of the pass/fail regression check.
- A wide interval is itself informative: it flags a row whose PER is
  noisy given its sample size (small `N`, or high per-word variance),
  and is a signal to grow the gold set before trusting a narrow slice
  of PER movement as a real regression or improvement.

### Top-k oracle PER (lattice quality vs ranking error)

A single PER number answers "was the first guess right". It cannot say
*why* a wrong guess was wrong. Two very different failures hide behind
one score:

- **Ranking error** — a BETTER reading than the one the engine ranked
  first is somewhere in the top-k. Nothing is missing from the language
  data; the weights ordered the beam badly. This is recoverable
  downstream: consumers of the lattice rescore it.
- **Model error** — no better reading exists in the lattice at any
  depth. No reranking can find one. Only new rules or new data fix this.

**Oracle PER@k** separates the two. It is the per-word *minimum* PER
over the engine's top-k readings, averaged exactly like the 1-best PER
(same normalization, same edit distance, same multi-gold rule). So:

    PER − Oracle@k   = ranking error  (the rescoring headroom)
    Oracle@k         = model error    (what rules/data must fix)

The columns `Oracle@3` and `Oracle@5` are in `docs/scoreboard.md` and
`benchmarks/results.json` (`oracle_per_top3`, `oracle_per_top5`).

**The headroom is an upper bound, not a forecast.** An oracle picks the
best candidate per word *after seeing the gold*. No real rescorer has
that information, so `PER − Oracle@k` is the ceiling on what any
reranking could ever buy, and a deployed rescorer will realize some
fraction of it. Quote it as a ceiling.

**A better reading is not the right reading.** `Oracle@k` dropping means
a CLOSER candidate is in the beam — closer in edit distance, and usually
still wrong. The strict version is the **`OracleX@k`** columns
(`oracle_exact_top3`, `oracle_exact_top5`): the fraction of words where
some top-k candidate *equals* a gold exactly. That is the `Exact match`
column generalized from k=1 to k. Measured on the current board, only a
minority of the PER-oracle gain is exact hits — fr 41.4%, de 25.8% —
so the PER oracle overstates "the engine already knows the answer" by
roughly 2x. Use `OracleX@k` for any claim of that shape. Both shares are
computed on the board's numbers and therefore **without injected
alternatives** (see the next section): the ratio is taken over the
committed row's `PER → Oracle@5` and `Exact match → OracleX@5`, never
over the injected-alternative figures, which would inflate it.

### Injected alternatives do not count as ranking error

Some oracle movement is not a discovery about the engine. It is a reading the
data **deliberately injected** into the beam — a list-valued
`grammatical_endings` entry, which adds a licit reading the spec cannot choose
between so that a downstream rescorer can (see
[SCHEMA.md](../orthography2ipa/data/SCHEMA.md#ambiguous-endings)). French
⟨-ent⟩ is the first of these.

**HARD rule: oracle@k movement caused by an injected alternative is reported
separately, under its own heading, and never counts toward ranking-error
analysis or any beat-espeak claim.**

**This is enforced by construction, not by discipline.** The scoreboard run
builds its engine with `G2P(lang, expose_ambiguous_endings=False)`, so a
list-valued ending contributes nothing to the beam it scores: every oracle cell
in `docs/scoreboard.md` and `benchmarks/results.json`, for every language and
every dataset, is measured on the beam the engine RANKS. A row whose language
declares injected alternatives records which ones it excluded in
`oracle_injected_alternatives` (`["fr-FR ent"]` on the fr/wikipron row), so the
exclusion travels with the numbers. That field is derived from the flag the row
was **scored with**, not from the spec: a row measured with exposure on claims
no exclusion and leaves the field off, because a provenance field that asserts
an exclusion the run did not perform is worse than no field at all. 1-best is
identical either way — an
alternative can never reach rank 1 — so the `PER` and `Exact match` columns do
not depend on this choice at all.

To measure the injected movement itself, pass the flag explicitly:

```python
evaluate_words_oracle(pairs, "fr", strip_stress=True, broad=True,
                      expose_ambiguous_endings=True)
```

Reproduced on the full fr/wikipron row (n=85495): `PER 0.0888` and
`Exact match 0.6185` in BOTH modes; `Oracle@5 0.0665 → 0.0627` and
`OracleX@5 0.6712 → 0.6888` when the ⟨-ent⟩ alternative is exposed, with
`Oracle@3` unmoved at `0.0723` because the mute reading lands at rank 4-5. The
first pair is the accuracy claim, and its invariance is the proof that an
injected reading never reaches rank 1; the second pair is reachability and
belongs only under this heading.

The reason is that the two would otherwise be the same number measured
differently. `PER − Oracle@k` is meant to read as "the engine already produced a
better answer and mis-ranked it" — a property of the weights that a rescorer
could realise. An injected alternative moves that gap by *construction*: adding
candidates to the beam can only lower an oracle, so any spec could raise its own
oracle arbitrarily by declaring more alternatives, while the 1-best does not
move and nothing about the ranking got better. Folding it into the headroom
would be marking our own diagnostic to our own edit.

So, when reporting:

- Give the 1-best columns first, and say they are unchanged. That is the claim
  an injected alternative is allowed to make.
- Give the oracle delta under an explicit **injected-alternative oracle
  movement** heading, naming the ending and the spec that declares it.
- Do not add it to a `PER − Oracle@k` headroom figure, a ranking-error budget,
  or a per-phenomenon ranking-failure count.
- Never carry it into `comparison.md` or any "beats espeak / epitran / X"
  sentence. Those compare one pronunciation to one pronunciation, and this is
  the k-inflating case the oracle ban below already exists for.

The value of an injected alternative is *reachability* — the reading exists for
a rescorer that has the fact we do not. Report it as reachability (for example,
"gold in top-10 went 0 → 192 of 300 gold-mute types"), not as accuracy.

### The Oracle@1 self-check

The readings come from `G2P.word_candidates`, which runs every beam path
through the same word-final pipeline as `transcribe_word` — geminate
collapse, grammatical-ending rewrite, stress marking, lexicon override.
Element 0 is therefore normally `transcribe_word`'s own answer, which is
what makes Oracle@1 equal the PER column.

That identity is **not guaranteed by construction**: `transcribe_word`
defaults to greedy width-1 search, while `word_candidates` runs a
width-`max(k, 8)` beam, and a wider beam may reach a cheaper path that
greedy pruning discarded. The two agree on every gold set measured, but
the harness verifies rather than assumes: it computes Oracle@1 on every
run, and if it differs from PER — or if any word's candidate 0 differs
from its 1-best — the run prints `ENGINE BUG` and **exits non-zero
without writing the scoreboard**. A corrupt committed artifact reported
as success is worse than a failed run.

**Oracle@k is a diagnostic for this engine only. It must never appear
in a cross-system comparison or a "beats X" claim.** espeak-ng, epitran
and every other system in [`comparison.md`](comparison.md) emit ONE
pronunciation. Setting their single answer against the best of k of ours
compares k guesses to one, and any conclusion drawn from it is an
artifact of the k. `scripts/compare_systems.py` does not read these
fields, and the CI regression gate
(`benchmarks/results_ci_sample.json`) stays 1-best.

Two more limits worth stating plainly:

- **Word-level only.** The beam is per word. Sentence-level gold sets
  (`4catac` and the TTS gold sets — note `vox_communis` is *word*-level
  and does get an oracle) get none: the columns read `-` and
  `oracle_scored_words` is `0`. Composing a sentence-level beam out of
  word beams would invent a ranking the engine never produces, so the
  harness refuses to.
- **`·` is not `-`.** A cell reads `·` when the row has not been
  rescored since the oracle columns were added, and `-` when the row is
  sentence-level and can never have one. A full scoreboard is ~10M
  scored words, so most rows are still `·` and get refreshed in batches.
  The two states are never merged into one blank: an unrescored row must
  not read as "no ranking error".
- **Phenomena-neutral.** The gap says a better reading was mis-ranked.
  It does not say *which* phonological phenomenon is involved. Use
  [`error_analysis.py`](../scripts/error_analysis.py) for that.

Cost, measured on `fr` WikiPron (85k words, beam width 8): **1.63x** the
1-best run in a cold process (2.04s vs 1.25s over a 3000-word probe,
reproduced across runs). That is cheap enough that `--scoreboard` opts
in; `--no-topk` turns it off for a fast ad-hoc rerun.

`build_scoreboard(..., oracle=...)` defaults to **off**, and each caller
opts in explicitly. The CI regression gate
(`check_benchmark_regression.py`) and the `--ci-sample` baseline compare
1-best PER only, and would otherwise pay 1.6x across every row for
columns they never read.

Because a full scoreboard is ~10M scored words, rows can be refreshed a
few at a time and merged into the committed board:

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --scoreboard \
    --dataset wikipron --lang fr
```

A subset run scores each row exactly as the full run does; the rows it
did not touch are carried through unchanged.

### Rules-only vs with-lexicon PER (lexicon overlay)

Languages that ship an optional lexicon overlay
(a caller-registered TSV, never bundled: see
[`data_model.md`](data_model.md#lexicon-overlay-sidecar-word_exceptions-at-scale))
are scored **twice** on the same gold: once with the lexicon disabled
(`get_lexicon` stubbed to `{}`, the "rules-only PER") and once with it active
(the "with-lexicon PER"). This keeps rule quality honest: the overlay has to
*improve* PER without letting the underlying grapheme rules rot behind lexicon
coverage. The results live in a dedicated report, separate from the main
scoreboard (which is untouched: languages with no lexicon are byte-identical
with or without this feature):

```bash
python scripts/benchmark.py --lexicon-report
```

writes [`lexicon_scoreboard.md`](lexicon_scoreboard.md) and
`benchmarks/lexicon_results.json`. Each row reports both the **full-slice**
delta and the **covered-subset** delta (scoring restricted to gold words the
lexicon actually contains: where the overlay can act). The covered-subset
delta is the honest measure of the lexicon's own accuracy vs the rules on the
*same* words. The full-slice number is diluted by every gold word outside the
deliberately capped, top-frequency pilot lexicon. The shipped `en-GB` pilot
(CMUdict-derived, General American) cuts PER on covered words roughly in half
against the independent WikiPron gold: the pilot proves the mechanism. Full
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
those without: the engine consults
`positional_graphemes`/`stress` whenever a spec provides them, so the
per-language path to a better number is richer spec data, not engine
changes. The pt-BR/pt-AO/pt-TL rows lack positional vowel-reduction
blocks. The en-US row reflects English orthography itself.

Among the newer rows: rule-complete languages with positional
grapheme blocks score best (eo, fi, ro, gl, eu, ast, sq, it). The
nb/da/sv/de rows reflect irregular stress and vowel-reduction patterns
not yet encoded in those specs, and the hi/ta/ml rows expose the
Indic-script calibration gap: engine-spec gaps, not dataset problems.


## Agreement with espeak-ng

[`scripts/espeak_agreement.py`](../scripts/espeak_agreement.py) compares
this engine's output against espeak-ng on the same word lists. This is
**not an accuracy benchmark**: espeak is not a gold standard. It
answers a deployment question: a TTS model trained on espeak
phonemization maps phoneme symbols to embedding IDs, so replacing its
front-end requires symbol-level compatibility, not correctness.

Signals: **exact** (identical transcription), **exact-nostress**
(identical after stress-mark removal: espeak places stress inside the
syllable, this engine before it), **segmental** (mean character
similarity, stress-stripped), and **oov-rate**: the fraction of words
whose transcription contains a symbol espeak never emits for that
voice. Out-of-inventory symbols become unknown embedding IDs, so
oov-rate is the hard-failure signal. The offending symbols are listed
per run.

Coverage is the overlap between this repo's registered gold-dataset
languages and espeak-ng's own voice list: every language with both a
wordlist loader and an espeak-ng voice gets a row. Languages with no
espeak-ng voice (e.g. Galician, Mirandese) are skipped rather than
scored as zero.

Full committed scoreboard: [`docs/espeak_agreement.md`]
(espeak_agreement.md) (machine-readable:
[`benchmarks/espeak_agreement.json`](../benchmarks/espeak_agreement.json)).
Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/espeak_agreement.py --scoreboard
```

This is a snapshot, not a CI-gated check: there is no ground truth to
regress against, so `scripts/check_benchmark_regression.py` never reads
these numbers. One language (`en-US`) needs the optional `scriptconv`
loader, and a handful of sentence-level sources (`ca` and its regional
variants) trip espeak-ng's own sentence-splitting on punctuation, which
misaligns the word-for-word comparison. Both cases are skipped with a
visible warning rather than reported as fabricated numbers: rerun with
those dependencies installed and the missing rows fill in.

Reading the table: stress-mark placement alone rules out byte-exact
replacement almost everywhere. Segmental similarity shows how close the
phone sequences are. The oov-rate column decides deployability. A
near-zero oov-rate (Spanish, French, Italian) means a symbol-mapping
shim suffices. A high one (English: espeak-ng writes the TRAP vowel as
⟨a⟩ where this engine emits ⟨æ⟩) means a per-symbol translation table
must be built and validated before any swap. A low oov-rate is a
signal of espeak-compatible **output shape**, not of linguistic
correctness: espeak-ng is an imperfect system being agreed with, not a
gold standard, so this table never substitutes for the gold-benchmark
scoreboard above.


---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Scoreboard](scoreboard.md) · [Quality tiers](quality_tiers.md) · [Comparison](comparison.md)*
