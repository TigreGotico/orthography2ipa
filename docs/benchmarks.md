# Benchmarks

What a benchmark number from this project means, and how far it can be
trusted. A provenance tier says where a transcription came from, not whether
it is right about the language, and this page is where that distinction is
defined.

Three pages cover the benchmark set. This one covers the provenance tiers and
the corrections overlays. [benchmark_datasets.md](benchmark_datasets.md)
catalogues every gold dataset, where it came from, and the caveats that
qualify its rows, together with the candidates this project examined and
refused. [benchmark_methodology.md](benchmark_methodology.md) covers how a
score is computed, how to reproduce one, and how to find out why a language
scores badly. The measured numbers live on the [scoreboard](scoreboard.md),
with the cross-system view in [comparison.md](comparison.md).

[gold_defects.md](gold_defects.md) is the registry of individual rows whose
gold was measured to merge a contrast, mark something the language forbids,
describe the wrong variety, mix transcription traditions, or derive from the
system it scores.

Run any row yourself with [`scripts/benchmark.py`](../scripts/benchmark.py):

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
  support a conclusion, only a hint. The scoreboard marks these rows
  with a `†` after `N` (see "Confidence intervals" below) so they cannot
  be mistaken for a measurement of the same weight as a row scored on
  thousands of words.

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
| **llm-generated** | The gold was produced by a large language model (`barranquenho_dict`, `mirandese_dict`: Claude, research-conditioned, `arabic_tts`, `portuguese_tts`: LLM-drafted, engine-pinned, literature-audited, `gold20_arabic`: LLM-drafted, native-speaker spot-checked). | **Worst of all, and never a gate.** An LLM has no lexicon, no G2P model and no rules, therefore **no error model**: it emits plausible-*looking* IPA that can be confidently wrong with no systematic structure, and a disagreement cannot be attributed to anything. Certifies nothing and diagnoses nothing. Read as a curiosity, not as evidence. This is why the GPT-4o-Mini-generated `dsvv-cair` dataset is [rejected outright](benchmark_datasets.md#rejected-candidates) rather than wired. |

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
| `portuguese_unified` | lexicon-derived, **`pt-TL` overridden to `machine-generated`** (see below) | Infopédia + Portal da Língua Portuguesa + pt.wiktionary.org (convention-normalized merge) | Single Portuguese gold (`TigreGotico/portuguese-unified-pronunciation-lexicon`, ~598k rows / 122k words, CC BY-SA 4.0), replacing the three separate golds it merges. One region per registered tag (see `_PT_UNIFIED_REGIONS`). `ipa_narrow` is scored. Untagged plain-`pt` rows are excluded. The Infopédia/Portal majority is dictionary/semi-automated lexicography and the Wiktionary minority is crowd-scraped: directional, not peer-validated ground truth. |
| `cmudict` | lexicon-derived | CMU Speech Group (hand-curated ARPABET) | Human labels, but **mechanically mapped ARPABET→IPA** via `scriptconv`. The transform adds artifacts. |
| `ipadict` | **per-language** (see below) | Depends on the file: human dictionaries, Wiktionary scrapes, rule scripts, **espeak** | The only mixed-provenance dataset here: ipa-dict is a *collection* of independently sourced files, so each row carries the tier of the file it was scored against, not a dataset-wide tier. Full per-language table in [ipa-dict pronunciation dictionaries](benchmark_datasets.md#ipa-dict-pronunciation-dictionaries-ipadict). |
| `wikipron` | crowd-scraped | Wiktionary editors | Quality tracks community size. Some entries are editor-rule output, not attested. Multiple valid variants per word. **On a few small-community tags the IPA column is not editor-typed at all but the output of a Wiktionary Lua module, which makes those rows a reproduction test rather than an accuracy test: see [Module-generated WikiPron rows](benchmark_datasets.md#module-generated-wikipron-rows).** |
| `wikipron_ar_diacritized` | crowd-scraped | Wiktionary editors + `text2tashkeel` input restoration | Same Arabic gold IPA as `wikipron`. Only the INPUT word is machine-diacritized (~2% DER noise floor). Diagnostic for the vowelized-Arabic rules. Certifies nothing beyond the raw row. See [Arabic with tashkeel restored](benchmark_datasets.md#arabic-with-tashkeel-restored-wikipron_ar_diacritized). |
| `wikipron_nor` | crowd-scraped | Wiktionary editors | The WikiPron scrape filed under the Norwegian **macrolanguage** code `nor`, because WikiPron sorts an entry by the code inside its `{{IPA|…}}` template rather than by the section heading above it. The words are predominantly Nynorsk, so the row is scored against `nn`. See [Norwegian under the macrolanguage code](benchmark_datasets.md#norwegian-under-the-macrolanguage-code-wikipron_nor). |
| `ipa_childes` | **per-language** (see below) | Depends on the language: `phonemizer` (espeak-ng), `epitran`, or `pinyin_to_ipa` | Mixed-provenance like `ipadict`: the IPA-CHILDES card names a **different phonemizing tool per language**, so each row carries the tier its own tool earns: `espeak-derived`, `epitran-derived`, or `machine-generated` for Mandarin's `pinyin_to_ipa` table. Full per-language tool table in [IPA-CHILDES split](benchmark_datasets.md#ipa-childes-split-ipa_childes). |
| `ipa_babylm` | espeak-derived | G2P+ with the `phonemizer` backend (= espeak-ng), `en-us` | BabyLM 2024 corpora phonemized by [G2P+](https://github.com/codebyzeb/g2p-plus), which is a wrapper over `phonemizer`/`epitran`. The conversion notebook ([codebyzeb/babylm-ipa](https://github.com/codebyzeb/babylm-ipa)) calls the `phonemizer` backend, which requires espeak-ng. So this is espeak output: it can neither qualify nor block English. |
| `hitz_basque_ipa` | machine-generated | HiTZ **ahoNT / AhoTTS** phonemizer | University-published (HiTZ/UPV-EHU), but the gold **is ahoNT/AhoTTS output**: it was generated by that phonemizer, not human-annotated. So a low PER **for the AhoTTS/ahotts-g2p engine on this row is near-tautological** (a tool scored against its own output). The independent, Wiktionary-sourced `wikipron` `eu` row is the fair comparison for Basque. |
| `barranquenho_dict` | llm-generated | **LLM (Claude), research-conditioned** | IPA generated by a large language model prompted with the *Convenção Ortográfica do Barranquenho* and descriptive research on the variety: **not** a phonemizer, not orthography2ipa, not any downstream o2i consumer, so scoring o2i against it is **not circular**. But LLM IPA can be plausibly wrong and is **not human-verified**: directional only. |
| `mirandese_dict` | llm-generated | **LLM (Claude), research-conditioned** | IPA generated by a large language model prompted with the *Convenção Ortográfica da Língua Mirandesa* and sub-dialect descriptions: **not** a phonemizer, not orthography2ipa, not any downstream o2i consumer, so scoring o2i against it is **not circular**. Complementary to the native-speaker `mirandese` gold. LLM IPA is plausibly wrong and **not human-verified**: directional only. |
| `northeuralex` | lexicon-derived | Cited published dictionaries, compiled by Dellert et al. | [NorthEuraLex](https://github.com/lexibank/northeuralex) (Dellert et al. 2020), 100+-language wordlist. Each CLDF row cites its source dictionary in `Source`. 18 languages wired (`_NORTHEURALEX_LANGS`): the original 9 plus 9 more (`udm`, `ady`, `av`, `lbe`, `dar`, `lez`, `lv`, `smn`, `vep`) that had zero gold anywhere before registration. See [Lexibank/CLDF wordlist gold](benchmark_datasets.md#lexibankcldf-wordlist-gold-northeuralex-wold). |
| `wold` | lexicon-derived | Cited published dictionaries, compiled by Haspelmath & Tadmor | [World Loanword Database](https://github.com/lexibank/wold) (Haspelmath & Tadmor 2009), 41-language loanword-typology wordlist. 6 languages wired (`_WOLD_LANGS`): 4 `stub`/`skeleton`, 2 already `research`. See [Lexibank/CLDF wordlist gold](benchmark_datasets.md#lexibankcldf-wordlist-gold-northeuralex-wold). |
| `kaikki` | crowd-scraped | Wiktionary editors, machine-extracted | [kaikki.org](https://kaikki.org/dictionary/) Wiktextract per-language JSON-lines dumps — a different extraction pipeline over the same Wiktionary source as `wikipron`, not an independent transcriber. 4 languages wired (`_KAIKKI_LANGS`), all zero-gold `skeleton` specs before this registration: `jv` (Javanese, `N=93`, Latin-script entries only — see below), `su` (Sundanese, `N=397`), `lo` (Lao, `N=2308`, whose IPA column is `Module:lo-pron` output — see [Module-generated WikiPron rows](benchmark_datasets.md#module-generated-wikipron-rows)), `xh` (Xhosa, `N=887`). See [kaikki.org Wiktextract gold](benchmark_datasets.md#kaikkiorg-wiktextract-gold-kaikki). |

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

## Corrections overlays

Some upstream gold sets carry a defect that is visible from the outside and
repairable without guessing. An **overlay** is how that repair is shipped: a
small committed file, one row per corrected gold entry, recording the spelling,
the reading the upstream shipped, the reading the overlay substitutes, the
reason, and the authority the correction rests on. The upstream file is never
edited. `scripts/build_gold_corrections.py` regenerates the overlays,
`scripts/benchmark.py` applies them, and the overlays live in
`orthography2ipa/data/gold/corrections/`.

**A correction may be derived only from the orthography of the word or from a
fetched citation.** It may never be derived from what orthography2ipa outputs.
This is the whole rule. A gold repaired with this project's own answers is a
circular gold: the board row it produces looks excellent and measures nothing,
because the engine is being scored against a copy of itself. The derivation
script imports no orthography2ipa, and a test enforces that by parsing its
imports.

**Overlays are separate datasets, never rewrites.** A corrected gold is
registered under its own name — `vox_communis_corrected` beside
`vox_communis` — so both rows stay on the board. The difference between the
two rows *is* the measurement of the upstream defect, and it cannot be read
if only one number is published. A correction is keyed on the spelling and the
original reading together, so an upstream revision makes the correction lapse
rather than overwrite a row nobody inspected.

**Overlays can never gate a promotion.** A corrected gold inherits the tier of
the base it was built from and can never rise above it: repairing one derivable
defect leaves the untouched majority of the rows exactly what they were, and
the repair itself was applied by an automated process rather than by a
phonetician reading each row. `can_gate_promotion()` must be false for whatever
tier an overlay lands on, and a test asserts it. An overlay makes a gold more
readable, not more authoritative.

**What must not be corrected.** Anything the rule above cannot reach stays in
the gold untouched and gets counted in the build report: a spelling whose
reading does not show the defect the overlay repairs, and a spelling whose
correct value cannot be determined at all. A skipped row is a reportable
negative result, not a gap to fill with a plausible guess.

---
[← Link audit](link-audit.md) · [Home](index.md) · [Benchmark gold datasets →](benchmark_datasets.md)
