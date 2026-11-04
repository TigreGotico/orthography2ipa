# TTS silver sets

The TTS silver sets are full sentences with a broad IPA transcription, one TSV file per lect. A large language model wrote them, and each IPA cell is the output of this engine. They are therefore [silver labels, never gold](../contributing/citations.md#silver-labels-are-never-gold). They have two uses. First, they check a TTS voice for a lect. Synthesize each sentence, listen to it or run ASR on it, and compare the result with the stored IPA. Second, they pin the sentence-level behaviour of the engine, so a spec change that alters a transcription fails CI.

Five sets share one design. This page describes the design once, then lists what each set adds.

## The five sets

| Set | Lects covered | Builder | Test | Benchmark tier |
|---|---|---|---|---|
| [`arabic_tts`](#arabic_tts) | Classical Arabic, Modern Standard Arabic, the spoken dialects from Mauritania to Oman, Andalusi Arabic, and the five Arabic grouping nodes | `scripts/arabic_tts_gold.py`, with `scripts/_gold_build.py` | `tests/test_arabic_tts_gold.py` | `llm-generated` |
| [`kabyle_tts`](#kabyle_tts) | Kabyle | `scripts/kabyle_tts_gold.py` | `tests/test_kabyle_tts_gold.py` | not a benchmark dataset |
| [`portuguese_tts`](#portuguese_tts) | European, Brazilian, African and Asian Portuguese, medieval Portuguese and Galician-Portuguese, Mirandese, the Asturleonese speech of Trás-os-Montes, and Barranquenho | `scripts/portuguese_tts_gold.py` | `tests/test_portuguese_tts_gold.py` | `llm-generated` |
| [`iberian_creole_tts`](#iberian_creole_tts) | The Portuguese creoles of Asia and the Gulf of Guinea, the Upper Guinea creoles, and the Spanish creoles of the Caribbean and the Philippines | `scripts/iberian_creole_tts_gold.py` | `tests/test_iberian_creole_tts_gold.py` | not a benchmark dataset |
| [`spain_romance_tts`](#spain_romance_tts) | Castilian and its accents, Galician, Asturleonese, Aragonese, Catalan and Valencian, Aranese, Fala, Extremaduran, Ladino, Latin American and Equatoguinean Spanish, and Basque | `scripts/spain_romance_tts_gold.py` | `tests/test_spain_romance_tts_gold.py` | `llm-generated` |

The files live in `orthography2ipa/data/gold/<set>/<code>.tsv`. List that directory for the lects that have a file. The `LECTS` list at the top of each builder is the full roster that `validate` checks.

The benchmark tier comes from `PROVENANCE` in `scripts/benchmark.py`. `kabyle_tts` and `iberian_creole_tts` are not in the dataset registry, so the scoreboard does not score them. See [What a score on these sets means](#what-a-score-on-these-sets-means).

## Schema

Each file is tab-separated UTF-8 with a header row. The columns are the `FIELDS` list of each builder.

| Column | Content |
|---|---|
| `id` | `<lect>-NNN`, numbered from `001` |
| `sentence` | The sentence in the input orthography of the lect. This is the text a TTS voice receives, and the text the engine transcribes. |
| `raw` | Arabic only. The sentence with the ḥarakāt removed, which is what a TTS normally receives. |
| `ipa` | The engine draft from `transcribe(sentence, lect)`, audited against the cited sources of the lect |
| `gloss_en` | An English translation |
| `features` | Coverage tags, separated by semicolons (see [Feature tags](#feature-tags)) |
| `notes` | Corrections to the engine output, and the source ids from the spec's `sources` that justify the row |

All columns except `notes` must be non-empty. The `notes` column must carry at least one source id, so in practice it is required too.

Only the Arabic set has a `raw` column. Arabic orthography leaves short vowels unwritten, and the engine takes fully vocalized text as its Arabic input. In the other four sets the spelling already writes every segment a speaker needs, so the sentence is the TTS input as it stands.

## The engine draft and the corrected label

`draft` writes the `ipa` column from the engine output for `sentence` under the lect. The author then audits each row against the lect's `sources` and records every correction in `notes`, with the source id that grounds it. `validate` does not compare the `ipa` column with the engine.

The board does not score the `ipa` column. It scores the label that [`scripts/correct_silver_ipa.py`](../contributing/silver_correction.md) wrote for each row, in `orthography2ipa/data/gold/<set>.llm-corrected.jsonl`. `tests/test_llm_corrected_sets.py` checks that each such file holds exactly the rows of its source set. A row that you add to, or change in, a source file therefore needs a correction run before the suite passes again.

Never edit the `ipa` column, or a corrected label, to hide a spec bug. When the engine is wrong, fix the spec, with a citation from the lect's `sources`.

## What `validate` checks

`validate` reads every lect in `LECTS`, or only the lects you name. It prints `all green` and exits 0 when every row passes.

| Check | A row or file fails when |
|---|---|
| Schema | a column of the schema is missing |
| Required fields | `id`, `sentence`, `ipa`, `gloss_en` or `features` is empty (`raw` too, in the Arabic set) |
| Row minimum | a lect file has fewer than `MIN_ROWS` rows. `MIN_ROWS` is 20 in the Kabyle builder and 5 in the other four. |
| Duplicates | two rows of one lect have the same sentence |
| Feature tags | a tag is unknown, or its predicate is false on the row |
| Citations | `notes` names an id that is not in the lect's `sources`, holds an author-year citation in free text, or holds no resolvable id |
| Arabic vocalization | `raw` differs from `sentence` with the ḥarakāt removed, or a consonant has no diacritic outside the allowed cases |

A source id is lowercase letters and a four-digit year, with an optional suffix, such as `naitzerrad2001` or `kossmann_stroomer1997`. `validate` rejects a free-text citation such as "Watson 2002", because a name in prose cannot be resolved against the spec.

The Arabic vocalization check allows a bare consonant in word-final position, where the pausal form drops the vowel. It also allows the bare lām of the definite article.

A lect in `LECTS` with no file is pending in four builders. They print it in the pending count, and it does not fail. A lect can therefore join the roster before its file exists. The Arabic builder has no pending state, so a missing Arabic file fails `validate`.

## Feature tags

A phonetic tag is a predicate over the sentence and its IPA. The predicates are in the `FEATURES` table of each builder. `validate` runs the predicate of every tag on its row, so a tag can appear only on a row where it is true. The predicate kind says what the tag reads:

| Kind | Reads | Used for |
|---|---|---|
| `ipa` | the transcription | a reflex that the IPA shows directly, such as a pharyngeal or a long vowel |
| `orth` (`raw` in the Arabic builder) | the spelling | an axis whose reflex varies between lects, where the stable grapheme is the witness |
| `both` | the spelling and the transcription | an axis tied to a position: the tag needs the trigger in the spelling and the predicted reflex in the IPA |

A `both` tag proves that the row exercises the axis, not that the row merely lacks a contrary symbol. Two `sandhi` tags are an exception. The Portuguese and Spain-Romance builders label `sandhi` as `both`, but its predicate reads only the spelling.

Shape tags describe the sentence type. `validate` accepts them without a check. The shape tags of each set are listed in its section below.

## Authoring sentences

The builders share three subcommands. Run them from the root of a checkout. Each builder puts the checkout on its own import path, so no `PYTHONPATH` is needed.

1. Print the coverage checklist of a lect:

   ```bash
   python scripts/kabyle_tts_gold.py checklist kab
   ```

   The output starts with the lect name and the source ids of the spec. Then it lists every tag with its kind, and an `x` marks each tag that the set already covers:

   ```text
   feature checklist (tag  verified-by  covered?):
     [x] spirantization   (ipa)
     [x] geminate         (ipa)
     [x] emphatic         (ipa)
     [x] pharyngeal       (ipa)
     [x] affricate        (ipa)
     [x] uvular           (ipa)
     [x] velar_fricative  (ipa)
     [x] schwa            (ipa)
     [x] glide            (ipa)
     [x] postnasal_stop   (both)
     [x] velar_nasal      (ipa)
     [x] greeting         (shape, not machine-verified)
     [x] imperative       (shape, not machine-verified)
     [x] negation         (shape, not machine-verified)
     [x] question         (shape, not machine-verified)
     [x] statement        (shape, not machine-verified)

   full phonetic coverage.
   ```

   A lect with gaps ends with a `MISSING phonetic coverage:` line instead.

2. Write sentences in the orthography of the lect that cover the missing tags. Take the vocabulary from the literature that the lect's spec cites.
3. Put one sentence per line in a text file and draft rows from it:

   ```bash
   python scripts/kabyle_tts_gold.py draft kab lines.txt
   ```

   The draft writes TSV to standard output, with the IPA and the tags that the predicates find. It leaves `gloss_en` empty and marks `notes` for review:

   ```text
   id	sentence	ipa	gloss_en	features	notes
   kab-001	Azul fell-awen.	æzul fəlː æwən		geminate;schwa;glide	NEEDS-REVIEW: author gloss + citation id from spec sources
   ```

4. Write the gloss, the shape tags and the `notes` yourself, with a source id in the notes.
5. Check the IPA against the phoneme mappings and the sources of the spec. If the engine is wrong, fix the spec as described in [The engine draft and the corrected label](#the-engine-draft-and-the-corrected-label).
6. Run `python scripts/kabyle_tts_gold.py validate` and confirm that it prints `all green`. The test file of the set runs the same command in CI.

The `checklist` docstrings mention an optional TSV argument, but the parser accepts only the lect code.

### The register rule

Every sentence uses vocabulary and morphology that the cited literature attests for that lect. Never invent a regional form to show off a feature. If the lect's `sources` do not document a regional form, use the neutral standard form instead.

### Sentence frames

The Portuguese and Spain-Romance sets build each lect's rows on one list of shared meanings. The rows are then comparable across lects, and each lect still uses its own words:

1. weather, with a negation
2. a price, with a number
3. an appointment
4. family or residence
5. directions, as an imperative
6. an opinion about food
7. a where-question
8. a how-many question
9. a conditional
10. past shopping
11. future travel
12. a phone call
13. a greeting pair
14. a proverb

Coverage rows follow the frames. They fill the phonetic tags that frames 1 to 14 left empty for the lect.

Both sets are also written to be rich in sandhi. Word junctions are where these languages change sounds: vowel elision and liaison, and /s/ voicing before a voiced onset. Those are what a TTS voice most often gets wrong. Write most rows with at least one `sandhi` junction, so the set tests connected speech and not only isolated words.

## What a score on these sets means

A language model wrote the sentences of all five sets. For `arabic_tts` and `portuguese_tts` it also drafted each transcription. Each draft was then pinned to the engine and audited row by row against the literature cited in `notes`. The `spain_romance_tts` transcriptions are drafted by `transcribe` itself. Each row of every set names in `notes` the spec sources that ground it, and `validate` checks that each id resolves.

The scoreboard scores `arabic_tts`, `portuguese_tts` and `spain_romance_tts` against their corrected labels, at the `llm-corrected` tier. That tier is silver and can never gate a quality decision. Two blind model passes wrote each label, and a third pass decided where they differed, with the engine output in view. The label is still a language model's. A PER on these rows measures distance from that label. It is not an accuracy, and a row is never evidence for a phonetic value. The `kabyle_tts` and `iberian_creole_tts` sets have corrected labels too, but the board does not register them.

The citation audit in `notes` raises confidence in the sentences and their grounding. It does not raise the tier of the IPA, and it does not make a silver set gold. [Gold defects](gold_defects.md#circular) records these sets as circular, and [benchmarks.md](benchmarks.md#provenance-and-reliability-read-this-before-trusting-any-number) explains the tiers.

## `arabic_tts`

The Arabic set covers Classical Arabic (`arb`), Modern Standard Arabic (`ar`), the spoken dialects, Andalusi Arabic (`xaa`) and five grouping nodes. The `sentence` column is fully vocalized dialectal orthography, which is the Arabic input contract of the engine. The `raw` column holds the same text without ḥarakāt.

### Grouping nodes

The grouping nodes are `afb`, `apc`, `ar-x-maghrebi`, `ar-x-mashriqi` and `ar-x-peninsular`. Their register is pan-group. A sentence uses only words that the leaves of the group share. Examples are Gulf `šlon` and `wāyid`, Levantine `qaddēsh` and `baddi`, and pan-Maghrebi `bzzāf` and `shri` in the sense of Heath and Marçais.

Where the leaves of a group differ, the node does not choose a reflex. The set shows the rank-1 candidate of the node instead. `ar-x-maghrebi` keeps /q/ and puts ʒ first for ǧīm. `ar-x-peninsular` puts the fricative interdentals first and keeps the diphthongs. `afb` and `apc` change ay and aw to ē and ō. That is the documented behaviour of the node, and each row notes it.

### Tags

| Tag | Kind | True when |
|---|---|---|
| `qaf` | `raw` | the spelling has ق. The reflex varies by dialect, so the letter is the witness. |
| `jim` | `raw` | the spelling has ج |
| `interdental` | `raw` | the spelling has ث, ذ or ظ |
| `kaf` | `raw` | the spelling has ك |
| `hamza` | `raw` | the spelling has ء, أ, إ, ئ or ؤ |
| `ta_marbuta` | `raw` | the spelling has ة |
| `sun_assim` | `raw` | the article ال stands before a sun letter |
| `emphatic` | `ipa` | the IPA has ˤ or ɫ |
| `pharyngeal` | `ipa` | the IPA has ħ or ʕ |
| `geminate` | `ipa` | the IPA, with stress marks removed, has a doubled consonant, or the spelling has a shadda |
| `long_vowel` | `ipa` | a vowel carries ː |
| `diphthong` | `ipa` | the IPA has a or ɑ or æ before w or j, or has eː or oː |

The `geminate` predicate removes the stress marks first. A geminate spans a syllable boundary, so the stress mark falls between its two halves, as in `rˈradʒulu`.

The shape tags are `statement`, `question`, `negation`, `imperative` and `number`. The rows of each lect cover the phonetic tags present in that lect, plus at least one question, one negation, one number and one imperative.

### Authoring differences

The Arabic `draft` vocalizes each line with text2tashkeel (`rawi-ensemble`) before it transcribes. text2tashkeel models Modern Standard Arabic only. For a dialect its output is out of domain, so `draft` marks each row for correction against the lect's sources. Classical and Modern Standard Arabic drafts still need a review of case endings and waṣl. The Arabic `draft` stops with an import error when the `text2tashkeel` package is not installed. When the package is installed but vocalization fails on a line, the draft keeps the line as written and records the error in `notes`.

`scripts/_gold_build.py` is a second way to write an Arabic file. It takes a lect code and a Python file that defines `ROWS` as a list of `(sentence, gloss_en, shape_tags, notes)` tuples. It computes `raw`, the IPA and the machine tags, warns about bare consonants, and overwrites `<lect>.tsv`:

```bash
python scripts/_gold_build.py arz-EG rows_ar_eg.py
```

If a fix to the spec changes a letter mapping, run `scripts/gen_arabic_orthography_keys.py` again.

### Vocalized connected speech

The set follows the conventions for vocalized text that `scripts/gen_arabic_orthography_keys.py` encodes. A sun letter carries the shadda of the assimilated article. Proclitics contract with the article, tā marbūṭa links to the next word, tanwīn sits on its alif seat, and waṣl elides. The docstring of that script gives the rules and their grounding in Ryding and Watson. Dialect sentences spell the article as their literature does: Cairene and Baghdadi `اِلْ‍` /il/, and the Levantine contraction `عَ ال‍`.

### Grounding by lect

| Lect | What the rows show | Sources |
|---|---|---|
| `arb` | Sībawayhi's lateral emphatic ض [ɮˤ] | spec notes |
| `ar` | the merged stop [dˤ] for ض | Versteegh 2001 |
| `arz-EG` | ج /ɡ/, ق /ʔ/, stop interdentals, the article `اِلْ‍` | Badawi and Hinds 1986, Mitchell 1956 |
| `apc-SY`, `apc-LB`, `apc-JO`, `apc-PS` | ق /ʔ/ (/g/ in the Jordanian koine), ج /ʒ/ (/dʒ/ in Jordan), ay and aw to ē and ō, final imāla -e written `ِة`. Beirut fronting of ā to ē is frequent, from an `apc-LB` spec rule. | Cowell 1964, Almbark and Hellmuth 2015, Al-Wer 2020, Cotter 2016 |
| `acm-IQ` | gilit Iraqi: ق /ɡ/ written گ, ك to چ /tʃ/, interdentals kept, ay and aw to ē and ō | Erwin 1963 |
| `ar-IQ-x-qeltu` | /q/ and plain /k/ kept. The qeltu and gilit split is the diagnostic of the pair. | Blanc 1964 |
| `apd-SD` | ج /ɟ/, a palatal stop, ق /ɡ/, and the words zōl and dāyir | Dickins 2007 |
| `shu-TD`, `shu-NG` | g-dialect qāf, and frames with an n- first person singular imperfect | Owens 1993 |
| `afb-AE`, `afb-BH`, `afb-KW`, `afb-QA` | ق /ɡ/, affricated kāf چ /tʃ/, interdentals kept, ē and ō from `afb` | Holes 2004, Alshammari 2026 |
| `acx-OM` | the sedentary control: /q/, plain /k/, diphthongs kept | Al-Balushi 2016 |
| `ars-SA` | the epenthesis of the gahawa syndrome (gahawa, aḥamar) | Ingham 1994 |
| `acw-SA` | urban stop interdentals, and a register close to Cairene | Omar 1975, Abdoh 2010 |
| `ayn-YE` | the verb aští, diphthongs and interdentals kept | Watson 2002 |
| `ars-SA-x-qassim` | the Najdi velar affricates [ts] and [dz], and /aj aw/ to [eː oː] (loːnak, joːm, bureːda), which central Najdi does not have | Alhoody 2019:42, Al-Rojaie 2013 |
| `ar-SA-x-rijal-alma` | the old lateral emphatics, ض as voiced [ɮˤ] and ظ as voiceless [ɬˤ], kept apart, and [q] for qāf | Watson and Al-Azraqi 2011, Asiri 2009, Al-Azraqi 2010 |
| `afb-SA-x-sharqiya` | Baḥārna ج to [j], affricated kāf [tʃ], qāf [ɡ] | Johnstone 1967, Holes 2004, Al-Taisan 2022 |
| `ary-MA` | heavy initial clusters, ma-...-š negation, n- first person singular, and the words ma-ṭīša, zwīn and bzzāf | Harrell 1962, Heath 2020 |
| `aeb-TN` | barša and bāhi, with the interdentals kept | Gibson 2009 |
| `arq-DZ` | mlīḥ and wāš rāk, attested in PADIC | Boucherit 2002 |
| `ar-LY` | halba and nibbi, with ق /ɡ/ | Pereira 2008 |
| `mey-MR` | Ḥassāniyya keeps the interdentals | Taine-Cheikh 2007 |

The lexical attestation also draws on the PADIC, QADI, EDC and SDC corpora. The sentences are written for the set, never copied from a corpus.

### Limits

The specs of `shu-TD`, `shu-NG`, `aeb-TN`, `arq-DZ`, `ar-LY` and `mey-MR` have thinner grounding. Their sentences keep to well-attested features shared across the region. No dialect vocalization is text2tashkeel output as it stands: each draft is corrected against the sources of the lect. The IPA is broad, and the pre-pausal tanwīn is kept, as in full style.

## `kabyle_tts`

The Kabyle set is written in the standard Berber Latin alphabet. That is the Tamaziɣt orthography of INALCO, which the Kabyle Wikipedia and the grammars of Naït-Zerrad use. It is the input contract of the `kab` spec. Tifinagh is a secondary script for Kabyle and the set does not cover it. Transliterate a Tifinagh text to the Latin orthography first.

### Tags

| Tag | Kind | True when |
|---|---|---|
| `spirantization` | `ipa` | a spirantized lax stop [β ð θ ç ʝ] surfaces. The class also catches [ðˤ]. This is the signature feature of Kabyle. |
| `geminate` | `ipa` | a length mark ː surfaces: a tense consonant, kept as a stop |
| `emphatic` | `ipa` | ˤ surfaces (⟨ṛ ṣ ḍ ṭ ẓ⟩ to [rˤ sˤ dˤ tˤ zˤ]) |
| `pharyngeal` | `ipa` | [ħ] or [ʕ] surfaces, from the Arabic series ⟨ḥ ɛ⟩ |
| `affricate` | `ipa` | [t͡ʃ] or [d͡ʒ] surfaces (⟨č ǧ⟩) |
| `uvular` | `ipa` | [q] or [χ] surfaces (⟨q x⟩) |
| `velar_fricative` | `ipa` | ⟨ɣ⟩ surfaces as [ɣ] or [ʁ]. The spec writes the uvular [ʁ] in every position and keeps [ɣ] as a documented variant. |
| `schwa` | `ipa` | the epenthetic [ə], written ⟨e⟩, surfaces |
| `glide` | `ipa` | [j] or [w] surfaces |
| `postnasal_stop` | `both` | the spelling has ⟨nt nd nb⟩ and the IPA has [nt], [nd] or [mb]: the stop survives after the nasal |
| `velar_nasal` | `ipa` | [ŋ] surfaces, from nasal place assimilation before a dorsal |

`postnasal_stop` needs both the written cluster and the surviving stop. The tag then proves that the row tests the block on spirantization, not only that the row has no spirant.

The shape tags are `statement`, `question`, `negation`, `imperative` and `greeting`.

### Register

The vocabulary and morphology come from Dallet 1982, the Kabyle-French dictionary, and Naït-Zerrad 2001, the reference grammar. The morphosyntax exercises what a Kabyle voice most often gets wrong. One case is the annexed state of a noun after a preposition (`ɣer wexxam`, `ɣer ugadir`). The others are the two-part negation `ur … ara`, the clitics `d-` and `ad`, and the aspect stems of the verb.

### Grounding

These transcriptions come from the `kab` spec:

| Input | Output | What it shows |
|---|---|---|
| `adrar` | `æðrær` | lax ⟨d⟩ spirantizes to [ð] |
| `taqbaylit` | `θɑqβæjliθ` | lax ⟨t⟩ and ⟨b⟩ spirantize to [θ] and [β] |
| `yeṭṭef` | `jətˤːəf` | the tense counterpart stays a stop |
| `meqqer` | `məqːər` | the tense counterpart stays a stop |
| `nteddu` | `ntədːu` | the stop survives after a homorganic nasal |

Kossmann and Stroomer 1997 (pages 466 to 469) describe spirantization and the stops that resist it. The rules `KAB_BLOCK_SPIRANT_T_AFTER_N`, `KAB_BLOCK_SPIRANT_D_AFTER_N` and `KAB_BLOCK_SPIRANT_B_AFTER_M` model the block after a nasal.

A lax stop can also stay a stop after other consonants. In `argaz` the spec gives `ærɡæz`, because /ʝ/ becomes a stop after r, l and n (Bedar, Quellec and Tifrit 2022). The emphatic and pharyngeal series, the affricates, the uvulars, [ɣ], nasal assimilation to [ŋ] and the epenthetic [ə] each occur in at least one row.

## `portuguese_tts`

The Portuguese set uses ordinary Portuguese orthography. Mirandese and its subdialects use their own orthography, the Convenção Ortográfica. The roster also holds the Asturleonese speech of Rionor and Guadramil in Portugal, because those lects share the sandhi of Portuguese contact. Sanabrese (`ast-x-sanabria`) is a lect of Spain, so it is in the Spain-Romance set.

### Tags

| Tag | Kind | True when |
|---|---|---|
| `vowel_reduction` | `ipa` | [ɨ] or [ɐ] surfaces (heavy in European lects, light in Brazilian lects) |
| `coda_sibilant` | `both` | the spelling has ⟨s z x⟩ in a coda, and the IPA has [ʃ] or [ʒ] in a coda, before a consonant or a word boundary. An onset [ʃ ʒ] from ⟨ch⟩, ⟨j⟩ or soft ⟨g⟩ does not count. |
| `open_mid` | `ipa` | [ɛ] or [ɔ] surfaces |
| `close_mid` | `ipa` | [e] or [o] surfaces, bare or nasal |
| `nasal_vowel` | `ipa` | a nasal vowel surfaces. The predicate decomposes the IPA first, so a combining tilde and a precomposed letter such as ã count the same. |
| `nasal_diphthong` | `ipa` | a nasal glide [w̃] or [j̃] surfaces (ão, ãe, õe) |
| `palatal` | `ipa` | [ʎ] or [ɲ] surfaces |
| `rhotic` | `ipa` | a strong R [ʀ ʁ r h χ] surfaces. The tap [ɾ] does not count. |
| `diphthong_ei_ou` | `orth` | the spelling has ⟨ei⟩ or ⟨ou⟩. Whether the diphthong stays or becomes one vowel is the choice of the lect. |
| `l_dark_or_velar` | `orth` | the spelling has ⟨l⟩ in a coda. The reflex varies: [ɫ], velar or [w]. The digraph ⟨lh⟩ does not count. |
| `u_fronting` | `ipa` | [y] surfaces: the island fronting of /u/ in the Azores and Madeira |
| `sandhi` | `both` | the spelling has a vowel-final word before a vowel-initial word, or an ⟨s z x⟩-final word before a voiced onset. The predicate reads only the spelling. |

The shape tags are `statement`, `question`, `negation`, `imperative` and `number`.

### Register

Each lect uses its own words where its sources attest them. Porto keeps the northern ei to [e]. Brazilian lects choose `você` or `tu` by region. Caipira has the retroflex r only in its attested coda contexts. Alentejo uses its gerund progressive. The Azores and Madeira use their attested island words and the fronting of /u/.

Reuse words that the primary-source gold of the spec attests (`orthography2ipa/data/gold/primary_sources/rows.jsonl`). A row then also witnesses a primary source.

### Grounding

| Lect | What the rows show | Sources |
|---|---|---|
| `pt-PT` | heavy reduction of unstressed vowels to [ɨ ɐ u], coda sibilant [ʃ ʒ], dark coda [ɫ], the open-close mid contrast, nasal vowels and nasal diphthongs [ɐ̃w̃ ɐ̃j̃ õj̃], palatals [ʎ ɲ], uvular strong R [ʁ] | Cruz-Ferreira 1995, Mateus and d'Andrade 2000, Cunha and Cintra 1984 |
| `pt-PT-x-lisbon` | the `pt-PT` profile with the article `o` raised to [u] and the fullest reduction. Coverage rows reuse the words of the Cruz-Ferreira IPA illustration (`gato`, `rato`, `mundo`, `chato`, `pilha`), so they witness the primary-source gold directly. | Cintra 1971, Segura 2013, Cruz-Ferreira 1995 |

## `iberian_creole_tts`

The creole set holds the Portuguese- and Spanish-lexified creoles that go back to the Iberian expansion. The sentences carry real creole morphosyntax: TMA particles before the verb, creole pronoun sets, reduced verb paradigms and substrate vocabulary. They are never Portuguese or Spanish sentences with creole words put in. Attested example forms from the sources (the APiCS surveys 40 to 42, Baxter, Cardoso, Clements) are used as given wherever possible.

Each lect uses its own written convention. Where a community orthography is stable, the set uses it, as for Kristang. Where no stable written form exists, the set uses the scholarly Latin transcription of the documentation.

### Which variety each code models

The ISO 639-3 code does not always name the variety that the spec models. The spec's `notes` decide.

| Code | Spec models | Orthography |
|---|---|---|
| `mcm` | Kristang (Papiá Kristang, Malacca Creole Portuguese) | Baxter's practical spelling, based on Malay (Baxter 1988, Baxter and de Silva 2004) |
| `idb` | Sri Lanka Portuguese Creole (Batticaloa and Trincomalee Burgher), not Diu or Daman | Cardoso's scholarly Latin convention: doubled vowels for length, ⟨nh ng ch j⟩, IPA ⟨ɛ ɔ⟩ |
| `vkp` | Korlai Indo-Portuguese ("Kristi", Maharashtra) | Clements' scholarly transcription: Roman letters and IPA ⟨ɛ ɔ ʈ ɖ⟩, tilde nasals, ⟨ï⟩, aspirates ⟨bh kh th⟩ |
| `kea` | Kabuverdianu (Cape Verdean Creole) | ALUPEC |
| `pov` | Guinea-Bissau Kriol | the Kihm and Scantamburlo convention |
| `pre` | Principense (Lung'Ie) | the community spelling of the Gulf of Guinea |
| `aoa` | Angolar (Ngola) | the community spelling of the Gulf of Guinea, with circumflex nasality and no written tone |
| `cri` | Sãotomense (Forro, Santome) | ALUSTP, a seven-vowel system where bare ⟨e o⟩ are [ɛ ɔ] |
| `pap` | Papiamento (Curaçao) | the phonemic spelling of Curaçao: ⟨k⟩ for ⟨c⟩, grave ⟨ò⟩ |
| `cbk-zam` | Chavacano (Zamboangueño) | the practical spelling of Zamboanga |
| `pln` | Palenquero (San Basilio de Palenque) | a practical spelling based on Spanish, with prenasal ⟨nd ng⟩ and postposed `nu` |

### Tags

| Tag | Kind | True when |
|---|---|---|
| `retroflex` | `ipa` | a retroflex [ʈ ɖ ɳ ɭ ɽ] surfaces: Korlai stops from Marathi contact, Sri Lanka [ɳ ɭ] after back vowels |
| `aspirated` | `ipa` | an aspirated or breathy stop ʰ or ʱ surfaces (Korlai ⟨bh kh th dh gh⟩) |
| `nasal_coda` | `ipa` | a nasal stands word-final or before a consonant: the coda left when a nasal vowel lost its nasality, and cluster codas |
| `prenasal_cluster` | `ipa` | a nasal stands directly before a stop or affricate anywhere (mb nd ŋɡ ndʒ ɳɖ) |
| `syllabic_nasal` | `ipa` | a nasal carries the syllabic mark, or a word starts with a nasal before a stop or affricate (Kristang `ngua`, `nsentu`, `ngka`) |
| `vowel_length` | `ipa` | a long vowel ː surfaces (Sri Lanka phonemic length) |
| `approximant_v` | `ipa` | [ʋ] surfaces: etymological /v/ as a South Asian labial approximant |
| `glide` | `ipa` | [j] or [w] surfaces |
| `prenasal_stop` | `both` | a word starts with ⟨mb nd ng mp⟩ and the IPA has [mb], [nd], [ŋɡ] or [mp]: the prenasal onset of the Gulf of Guinea and the substrate |
| `labial_velar` | `both` | the spelling has ⟨gb⟩ or ⟨kp⟩ and the IPA has [ɡ͡b] or [k͡p]: the Niger-Congo labial-velar stop (`pre`, `aoa`, `cri`) |
| `postalveolar` | `ipa` | [ʃ] or [ʒ] surfaces: ⟨x⟩ [ʃ], ⟨j⟩ [ʒ], Caribbean coda /s/ to [ʃ] |
| `coda_sibilant` | `ipa` | a word ends in [ʃ] or [ʒ] (coda /s/ in `kea` and `pap`, ⟨x⟩ in `cri`) |
| `velarized_l` | `ipa` | [ɫ] surfaces (the velarized coda /l/ of `kea`) |
| `tap` | `ipa` | [ɾ] surfaces |
| `stress` | `ipa` | a stress mark ˈ surfaces. `kea` assigns stress, and the Gulf of Guinea specs do not. |
| `nasal_vowel` | `ipa` | a nasal vowel surfaces: Korlai /ĩ ũ ɛ̃ ɔ̃/, the Atlantic ⟨ã ẽ ĩ õ ũ⟩. Kristang and Sri Lanka Portuguese lost them. |
| `affricate` | `ipa` | [tʃ dʒ ts dz] surfaces (old ⟨ch⟩ and ⟨j⟩, creole ⟨tx dj⟩, Korlai [ts dz]) |
| `palatal_nasal` | `ipa` | [ɲ] surfaces (Kristang ⟨ny⟩, ⟨nh⟩ in Sri Lanka and `kea`, Caribbean ⟨ñ⟩) |
| `velar_nasal` | `ipa` | [ŋ] surfaces |
| `open_mid` | `ipa` | [ɛ] or [ɔ] surfaces (Sri Lanka, the seven vowels of `cri`, ⟨ò⟩ in `pap`) |
| `schwa` | `ipa` | [ə] surfaces (the Korlai central vowel ⟨ï⟩) |
| `strong_rhotic` | `ipa` | [ʀ] or [r] surfaces, not the tap: the Asian trill, word-initial and ⟨rr⟩ in `kea`, alveolar /r/ in `pov` |

`prenasal_cluster` and `prenasal_stop` are separate axes, and both can be true on one row. `prenasal_cluster` reads any position off the IPA. `prenasal_stop` needs a word-initial onset in the spelling.

The shape tags are `statement`, `question`, `negation`, `imperative` and `number`. Five more shape tags mark creole morphosyntax: `tma` (a tense, mood or aspect particle), `no_agreement` (an invariant noun or adjective), `pronoun`, `plural` and `copula`.

### Axes that do not apply

The Spanish- and Portuguese-lexified creoles do not share the axes of Iberian Romance. Those axes are distinción, seseo and ceceo, yeísmo, Romance ⟨ie ue⟩ diphthongs, gheada, and coda /s/ aspiration as a variable that separates lects. They do not apply to these languages and the set does not model them. The `pap`, `cbk-zam` and `pln` rows carry only the creole tags that their IPA shows. Coda /s/ to [ʃ] in `pap` is `postalveolar` and `coda_sibilant`, and the prenasal ⟨nd ng⟩ of Palenquero is `prenasal_stop`.

## `spain_romance_tts`

The Spain-Romance set covers the Romance lects of Spain and the peripheral Romance of the Iberian west. It also covers Latin American and Equatoguinean Spanish, and Basque. Basque is not Romance, but it is an Iberian language, and its rows use their own `eu_` tags.

Each lect uses its own orthography. Galician uses the RAG standard or the reintegrationist spelling, Asturian uses ALLA, and Aragonese uses its Academia. Catalan and Valencian use IEC or AVL, and Aranese uses its attested convention. The medieval stages use period spelling, and Ladino uses its Latin convention. The Spanish-lexified creoles `pap`, `cbk-zam` and `pln` are not Iberian Romance. They are in the [`iberian_creole_tts`](#iberian_creole_tts) set.

### Tags

| Tag | Kind | True when |
|---|---|---|
| `distincion` | `both` | the spelling has ⟨c⟩ before a front vowel, ⟨z⟩ or ⟨ç⟩, and the IPA has [θ]: /θ/ kept apart from /s/, or the ceceo reflex |
| `seseo` | `both` | the same spelling, and the IPA has [s] and no [θ] |
| `lateral_palatal` | `both` | the spelling has ⟨ll⟩ or ⟨lh⟩, and [ʎ] surfaces |
| `yeismo` | `both` | the spelling has ⟨ll⟩ or ⟨y⟩ before a vowel, and the IPA has [ʝ] and no [ʎ] |
| `palatal_nasal` | `ipa` | [ɲ] surfaces (⟨ñ nh ny⟩) |
| `palatal_initial` | `both` | a word starts with ⟨ll lh ñ nh⟩, and [ʎ] or [ɲ] surfaces: Asturleonese initial palatalization of L- and N- |
| `gheada` | `both` | the spelling has the phoneme /g/ (⟨ga go gu⟩, ⟨gue gui⟩, ⟨g⟩ before a liquid or nasal), and [ħ] or [h] surfaces in an onset |
| `coda_s_aspiration` | `both` | the spelling has ⟨s⟩ in a coda, and [h] surfaces in a coda: southern aspiration of /s/ |
| `diphthong_ie_ue` | `both` | the spelling has ⟨ie⟩, or ⟨ue uo⟩ not after ⟨q g⟩, and the IPA has [je we wo]: Romance diphthongization |
| `final_u` | `both` | a word ends in ⟨u⟩ after a consonant, and an IPA word ends in [u]: Asturleonese raising of final -o to -u |
| `open_mid` | `ipa` | [ɛ] or [ɔ] surfaces: the seven-vowel contrast of Galician, Catalan and Asturleonese |
| `vocalismo_abierto` | `both` | the spelling has ⟨s⟩ in a coda, and [æ], [ɛ] or [ɔ] surfaces: the Eastern Andalusian open vowel left by a lost plural -s |
| `schwa` | `ipa` | [ə] surfaces: Catalan unstressed reduction |
| `velar_nasal` | `ipa` | [ŋ] surfaces: Galician coda -n and ⟨nh⟩, Catalan ⟨ng⟩ |
| `sibilant_voicing` | `ipa` | [z] or [ʒ] surfaces: voiced sibilants, present in Catalan and absent in Galician |
| `rhotic` | `ipa` | the trill [r] surfaces |
| `rhotic_tap` | `ipa` | the tap [ɾ] surfaces: the neutralized coda rhotic of Balearic and Valencian |
| `postalveolar_affricate` | `ipa` | [tʃ] or [dʒ] surfaces: the Western Catalan reflex of ⟨j⟩ and ⟨g⟩ before a front vowel, where Eastern Catalan has [ʒ] |
| `sandhi` | `both` | the spelling has a vowel-final word before a vowel-initial word, or an ⟨s⟩-final word before a voiced onset. The predicate reads only the spelling. |
| `eu_sibilant_apical` | `both` | ⟨s⟩ outside ⟨ts⟩, and the apico-alveolar [s̺] outside an affricate |
| `eu_sibilant_laminal` | `both` | ⟨z⟩ outside ⟨tz⟩, and the lamino-alveolar [s̻] outside an affricate |
| `eu_sibilant_postalveolar` | `both` | ⟨x⟩, and [ʃ] outside [tʃ] |
| `eu_sibilant_neutral` | `both` | ⟨z⟩ outside ⟨tz⟩, with [s̺] and no [s̻]: the Biscayan merger of apical and laminal |
| `eu_affricate_apical` | `both` | ⟨ts⟩, and [ts̺] |
| `eu_affricate_laminal` | `both` | ⟨tz⟩, and [ts̻] |
| `eu_affricate_postalveolar` | `both` | ⟨tx⟩, and [tʃ] |
| `eu_palatal_stop` | `both` | ⟨tt⟩ or ⟨dd⟩, and [c] or [ɟ] |
| `eu_front_rounded` | `both` | ⟨ü⟩, and [y]: Souletin and Roncalese |
| `eu_aspiration` | `both` | ⟨h⟩, and [h]: the aspiration of the northern dialects |
| `eu_negation_sandhi` | `both` | a separate word ⟨ez⟩ stands before a d, z, n, l, b or g onset, and the IPA shows the contraction at that juncture (ezt-, etz-, en-, el-, ezp-, ezk-) |

`rhotic` and `rhotic_tap` are separate on purpose. A row tagged `rhotic` must show the trill, and a row tagged `rhotic_tap` must show the tap, so neither tag can stand in for the other.

The shape tags are `statement`, `question`, `negation`, `imperative` and `number`.

### Tags tied to a position

`gheada` and `coda_s_aspiration` share the symbol [h], so the predicates separate them by position. Gheada is /g/ as [ħ] or [h] in an onset, before a vowel. Aspirated coda /s/ is [h] before a consonant or a word boundary. A fricative elsewhere in the sentence therefore never sets the wrong tag. `diphthong_ie_ue` ignores the silent ⟨u⟩ of ⟨que qui gue gui⟩, so `aquel` and `pequeño` do not count. `final_u` needs a consonant before the ⟨u⟩, so the glide of a falling diphthong ⟨…ou⟩ does not count.

### Axes a lect does not have

Leave an axis off the rows of a lect that does not have it, and say so in the row's `notes` where it matters. Standard Galician has no gheada, because /g/ stays [ɡ]. It has no yeísmo, because ⟨ll⟩ keeps [ʎ]. It has no Romance diphthongs (`fronte`, `torce`, not `fuente`, `tuerce`) and no voiced sibilants. A Galician sub-lect with gheada uses the `gheada` tag where its spec gives the reflex.

### Register

Each lect uses its own attested words, never Castilian spoken with an accent. Galician uses `mercar`, `paxaro` and `rúa`. Sanabrese uses `cuostan`, `buonas`, `you` and `ye`. Aragonese uses the forms of its Academia, and Catalan and Valencian use the IEC and AVL register.

### Grounding

| Lect | What the rows show | Sources |
|---|---|---|
| `es-ES` | distinción ⟨c z⟩ [θ], yeísmo ⟨ll y⟩ [ʝ], Romance diphthongs from Ĕ and Ŏ, palatal nasal [ɲ], the trill and tap contrast, sandhi | Hualde 2005, Penny 2002, Harris 1969 |
| `gl-ES` | distinción without seseo, [ʎ] without yeísmo, the open mids [ɛ ɔ], velar nasal [ŋ] in coda -n and ⟨nh⟩ (`unha`), [ʃ] from the old sibilants, and no gheada in the standard | Regueira 1996, Freixeiro Mato 1998, Carballo Calero 1979 |
| `ast-x-sanabria` | stressed Ŏ to /wo/ (`cuostan`, `buonas`), initial L- to [ʎ] and N- to [ɲ], distinción [θ], final -o to -u, and four sibilants | Frías Conde, García Arias 2003 |

---
[← The pinned WikiPron mirror](wikipron_mirror.md) · [Home](../index.md) · [Gold defects →](gold_defects.md)
