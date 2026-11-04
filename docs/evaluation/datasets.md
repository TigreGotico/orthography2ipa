# Benchmark gold datasets

This page lists every gold pronunciation dataset that the harness can score against. For each one it says where the data came from and what its numbers can and cannot support. Read [benchmarks.md](benchmarks.md) first for the provenance tiers that this page uses.

The registry is `DATASETS` in [`scripts/benchmark.py`](../../scripts/benchmark.py). `python scripts/benchmark.py --list` prints every registry key with the language tags it covers. Row sizes and scores are on the [scoreboard](generated/scoreboard.md) and in [`benchmarks/results.json`](../../benchmarks/results.json), never on this page.

## Summary

The tier column is the value of `provenance_for()`. "Per language" means that `PROVENANCE_BY_LANG` gives each language its own tier. A dash in the licence column means that this page does not state one.

| Registry key | Languages | Tier | Source | Licence | What it supports |
|---|---|---|---|---|---|
| `primary_sources` | Arabic dialects, Portuguese varieties, Spanish, Hebrew, Russian, Ukrainian, Tetun Dili and others | expert-human | Worked examples printed in the sources the specs cite | - | Rule diagnosis. Too small to gate a language alone. |
| `arabic_tts` | Arabic dialects | llm-corrected | Sentences drafted by a language model and audited against cited literature, with the [corrected label](../contributing/silver_correction.md) | - | Silver. Direction only. |
| `gold20_arabic` | Arabic dialects | llm-corrected | [Salesteq/arabic-dialects-gold20](https://huggingface.co/datasets/Salesteq/arabic-dialects-gold20), with the [corrected label](../contributing/silver_correction.md) | - | Silver. Direction only. Often the only gold for a dialect. |
| `portuguese_tts` | Portuguese varieties and the other languages of Portugal | llm-corrected | Sentences drafted by a language model and audited against cited literature, with the [corrected label](../contributing/silver_correction.md) | - | Silver. Direction only. |
| `spain_romance_tts` | Romance languages and Basque of Spain, with Latin American Spanish | llm-corrected | Sentences transcribed by the engine itself, with the [corrected label](../contributing/silver_correction.md) | - | Silver. Direction only. |
| `ep_dialects` | European Portuguese regional varieties | expert-human | TigreGotico team annotation | - | Sentence-level dialect rules. Not peer-validated. |
| `wikipron` | Most languages with Wiktionary pronunciations | crowd-scraped | [CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron) | CC BY-SA | Breadth. Some tags are reproduction tests. |
| `wikipron_ar_diacritized` | Arabic | crowd-scraped | The `wikipron` gold with machine-restored short vowels in the input | CC BY-SA | The rules for vowelized Arabic. |
| `wikipron_nor` | Norwegian Nynorsk | crowd-scraped | The WikiPron file under the code `nor` | CC BY-SA | Nynorsk, with a Bokmål minority. |
| `wikipron_restored` | Ewe, Middle High German, Yoruba, Hebrew | crowd-scraped | [The pinned WikiPron mirror](wikipron_mirror.md) | CC BY-SA 4.0 | Rules on the displayed spelling. A subset of `wikipron`. |
| `mirandese_g2p` | Mirandese, with its Sendinese and Raiano varieties | expert-human | [TigreGotico/mirandese_g2p](https://huggingface.co/datasets/TigreGotico/mirandese_g2p) | - | The best Mirandese signal. Small. |
| `barranquenho_dict` | Barranquenho | llm-corrected | [TigreGotico/barranquenho-ipa-dict-synthetic](https://huggingface.co/datasets/TigreGotico/barranquenho-ipa-dict-synthetic), with the [corrected label](../contributing/silver_correction.md) | - | Silver. Direction only. |
| `mirandese_dict` | Mirandese varieties | llm-corrected | [TigreGotico/mirandese-ipa-dict-synthetic](https://huggingface.co/datasets/TigreGotico/mirandese-ipa-dict-synthetic), with the [corrected label](../contributing/silver_correction.md) | - | Silver. Direction only. |
| `portuguese_unified` | Portuguese of Portugal, Brazil, Angola, Mozambique and Timor-Leste | lexicon-derived, `pt-TL` machine-generated | [TigreGotico/portuguese-unified-pronunciation-lexicon](https://huggingface.co/datasets/TigreGotico/portuguese-unified-pronunciation-lexicon) | CC BY-SA 4.0 | The main Portuguese gold. |
| `portuguese_unified_corrected` | The same, without the carioca and caipira regions | as the base | `portuguese_unified` with an overlay that fixes stress marks and drops mis-keyed rows | CC BY-SA 4.0 | Reading the base defect. Never gates. |
| `4catac` | Central, Balearic, North-Western and Valencian Catalan | expert-human | [projecte-aina/4catac](https://huggingface.co/datasets/projecte-aina/4catac) | - | Accent rules, at sentence level. |
| `hitz_basque_ipa` | Basque | machine-generated | [HiTZ/wikipedia_basque_ipa](https://huggingface.co/datasets/HiTZ/wikipedia_basque_ipa) | - | Agreement with the ahoNT phonemizer. |
| `clup_dialect` | European Portuguese dialects | expert-human | [TigreGotico/ArquivoDialetalCLUP_ipa](https://huggingface.co/datasets/TigreGotico/ArquivoDialetalCLUP_ipa) | - | Hints. Most rows are tiny. |
| `cmudict` | American English | lexicon-derived | [cmusphinx/cmudict](https://github.com/cmusphinx/cmudict) | - | A floor for English spelling. |
| `ipadict` | Icelandic, Japanese, Khmer, Korean, Persian, Vietnamese and many European languages | per language | [open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict) | MIT, each file its own | Depends on the file. |
| `ipadict_corrected` | Brazilian Portuguese | machine-generated | `ipadict` with a stress overlay | as the base | Stress accuracy. Never gates. |
| `ipa_childes` | Child-directed speech in European languages, Indonesian, Quechua and Mandarin | per language | [fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split) | CC BY 4.0 | Agreement with a competitor. |
| `vox_communis` | The Common Voice languages | epitran-derived | [fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p) | CC0 | Breadth only. Never gates. |
| `vox_communis_corrected` | Vietnamese | epitran-derived | `vox_communis` with a tone overlay | CC0 | Reading the base defect. Never gates. |
| `ipa_babylm` | English | espeak-derived | [phonemetransformers/IPA-BabyLM](https://huggingface.co/datasets/phonemetransformers/IPA-BabyLM) | none declared | Agreement with espeak-ng. |
| `northeuralex` | Uralic, Caucasian, Tungusic, Paleo-Siberian and other languages of northern Eurasia | lexicon-derived | [lexibank/northeuralex](https://github.com/lexibank/northeuralex) | - | Progress for specs with no other gold. |
| `wold` | Galibi Carib, Mapudungun, Gawwada, Iraqw, Seychelles Creole, Tarifiyt Berber | lexicon-derived | [lexibank/wold](https://github.com/lexibank/wold) | - | Progress for specs with no other gold. |
| `kaikki` | Javanese, Sundanese, Lao, Xhosa, Somali, Oromo, Nepali, Konkani | crowd-scraped | [kaikki.org](https://kaikki.org/dictionary/) | - | Gold for specs with no other gold. |
| `alphacep_ru_book` | Russian | machine-generated | [alphacep/biggest-ru-book-cleanup](https://huggingface.co/datasets/alphacep/biggest-ru-book-cleanup) | - | Agreement with a morphophonemic annotation. |
| `coruss_ru` | Russian | expert-human | CoRuSS, SPbU phonetics lab | - | Distance to spontaneous speech. |

[TTS silver sets](silver_sets.md) describes the three TTS sentence sets in this table: `arabic_tts`, `portuguese_tts` and `spain_romance_tts`. It also describes two more that the harness does not score, and the protocol they share. A language model wrote all five, so they are silver labels, not gold. [gold_defects.md](gold_defects.md) records individual rows of these datasets that carry a measured defect.

## Primary-source gold (`primary_sources`)

The rows live in `orthography2ipa/data/gold/primary_sources/`. Every row is a worked example printed by a linguist in a source that one of the specs cites. The sources include the Arabic dialect studies behind the Arabic specs and the Portuguese dialect monographs. They also include the JIPA *Illustrations of the IPA* for Ukrainian, Russian, European and Brazilian Portuguese, and Castilian and Argentine Spanish. The [dataset README](../../orthography2ipa/data/gold/primary_sources/README.md) lists every source by language.

Each row carries the source id and the printed page, which is not the PDF page index. The two differ, and `sources.json` records the offset per source.

The row also carries the notation of the source verbatim, whether the source wrote it broad `/…/` or narrow `[…]`, and a confidence. Nothing is silently coerced. A transliterated row can never have `confidence: high`, and the Arabic input words carry ḥarakāt that an editor supplied, flagged per row. Where the PDF of a source mangles its own IPA, through a scan or a legacy font, the row is transcribed from a render of the printed page. It is never decoded from the mangled bytes.

The dataset is small and adversarial on purpose. Several rows exist because the source contradicts the spec, and the README lists them. Use it to diagnose rules. Do not gate a language on it.

The Tetun Dili rows are the only gold for that language. They are a faithfulness check only, because the grammar they come from (Williams-van Klinken, Hajek & Nordlinger 2002) is also the source of the `tet` spec. They measure whether the engine reproduces what that grammar says, never whether the grammar is right. Some rows print no spelling, such as the stress inventory, which the grammar gives in transcription only. Their orthography is written out with the conventions of the grammar and flagged `editor-supplied`. Every row was transcribed from a render of the printed page, because the text layer of the PDF mangles the IPA and flattens the trill and tap distinction.

## Arabic sets from a language model (`gold20_arabic`)

[`Salesteq/arabic-dialects-gold20`](https://huggingface.co/datasets/Salesteq/arabic-dialects-gold20) is a sibling of `arabic_tts` with the same shape: one TSV per lect, a vocalized `sentence` as input and a broad `ipa` gold. The harness fetches it at run time and caches it. It is never vendored.

The set is semi-synthetic. The same Claude lineage that wrote the Arabic dialect specs drafted every transcription, so the relation to the specs is close to circular. A native Arabic speaker then spot-checked the set and judged it good.

That check is context, not a tier upgrade. It is not a per-row audit against cited literature, and no lexicon or rule system stands behind the gold. The set is registered because most of these dialects have no other gold at all. The tier stays `llm-generated`, so the row gates nothing and certifies nothing.

## Portuguese unified pronunciation lexicon (`portuguese_unified`)

[TigreGotico/portuguese-unified-pronunciation-lexicon](https://huggingface.co/datasets/TigreGotico/portuguese-unified-pronunciation-lexicon) merges three Portuguese golds into one dataset with one notation, and it replaces their separate loaders. The three sources are these:

| Source | Content |
|---|---|
| Infopédia (Porto Editora) | Dictionary extractions of European Portuguese, broad phonemic. |
| Portal da Língua Portuguesa (INESC-ID) | A semi-automated phonetic lexicon in ten regions. |
| pt.wiktionary.org | Community transcriptions with explicit region tags. |

Each row is a tuple of word, region, source and part of speech. It carries a broad phonemic `ipa_broad` and a narrow phonetic `ipa_narrow`, normalized across the three source conventions (`ə/ɨ`, `r/ɾ/ʀ`, `a/ɐ`, optional segments and syllable markers). The harness scores `ipa_narrow`, because its depth matches the Portuguese specs, with explicit [ɐ ɨ ɾ ʀ ɫ]. The Infopédia and Portal majority is dictionary or semi-automated lexicography, and the Wiktionary minority is crowd-scraped. Read the row as a direction, not as peer-validated truth.

One region is scored per registered tag (`_PT_UNIFIED_REGIONS`):

| Tag | Region in the dataset |
|---|---|
| `pt-PT` | `pt-PT` |
| `pt-PT-x-lisbon` | `pt-PT-x-lisboa` |
| `pt-BR` | `pt-BR` |
| `pt-BR-x-sp` | `pt-BR-x-saopaulo` |
| `pt-BR-x-rj` | `pt-BR-x-riodejaneiro` |
| `pt-BR-x-carioca` | `pt-BR-x-carioca` |
| `pt-BR-x-caipira` | `pt-BR-x-caipira` |
| `pt-AO` | `pt-AO` |
| `pt-MZ` | `pt-MZ-x-maputo` |
| `pt-TL` | `pt-TL-x-dili` |

Rows tagged only `pt`, with no region, are excluded from every regional row. The loader reads the whole file and draws a random sample of words per region with a fixed seed (`SAMPLE_SEED`), because the first words in alphabetical order would bias the sample.

`pt-TL` carries its own tier, `machine-generated`, in `PROVENANCE_BY_LANG["portuguese_unified"]`. Its `pt-TL-x-dili` region is the Lisbon entries written with other symbols, not Timorese lexicography. [Gold defects](gold_defects.md#east-timorese-portuguese-portuguese_unified) gives the measured substitutions and the source that contradicts them. The `machine-generated` tier still gates. The downgrade records the problem and does not exempt the row from the gates. See [languages/pt-TL.md](../languages/pt-TL.md).

### Stress overlay (`portuguese_unified_corrected`)

`portuguese_unified_corrected` sits beside `portuguese_unified` on the board. Its overlay, `portuguese_unified_pt.jsonl`, is keyed on the source row of the dataset: source, region, word, part of speech, field and the reading the row ships. The overlay moves or adds a primary stress mark where the spelling settles the stressed syllable. A written accent settles it, and so do the accent rules of the Acordo Ortográfico 1990. It also drops rows that transcribe another headword or that end in mis-encoded text.

The corrected row scores the same sampled words as the base row, so the two numbers compare. It covers only the regions where the overlay corrects at least one reading, which leaves out `pt-BR-x-carioca` and `pt-BR-x-caipira`. [Corrections overlays](benchmarks.md#corrections-overlays) gives the rules that every overlay follows.

## WikiPron

[CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron) (Lee et al. 2020, *WikiPron: Mining Wiktionary for Massively Multilingual Pronunciation Data*, LREC) mines word and IPA pairs from English Wiktionary. Wiktionary editors curate the data, so it is reliable where the editor community is large and uneven where it is small. The gold often carries several valid transcriptions per word, such as the Galician seseo and gheada variants, and [the scorer](benchmarks.md#how-a-score-is-computed) keeps the best match.

`_WIKIPRON_FILES` maps each tag to one file under `data/scrape/tsv/` of the upstream repository. The loader reads the upstream branch and caches each file. The harness uses the broad file of a language where upstream publishes one. For a language that upstream scraped only narrow, such as Russian (`rus_cyrl_narrow.tsv`), it uses the narrow file. Some mappings need a note:

| Tag | WikiPron file | Note |
|---|---|---|
| `es` | `spa_latn_ca_broad.tsv` | Castilian. `es-419` reads the Latin American file. |
| `pt-PT`, `pt-BR` | `por_latn_po_broad.tsv`, `por_latn_bz_broad.tsv` | The two national files. |
| `en`, `en-GB` | `eng_latn_us_broad.tsv`, `eng_latn_uk_broad.tsv` | American and British English. |
| `cy` | `cym_latn_nw_broad.tsv` | Welsh, the north-western dialect. |
| `hr` | `hbs_latn_broad.tsv` | The Latin-script file of the `hbs` macrolanguage. |
| `hy` | `hye_armn_e_broad.tsv` | Eastern Armenian. |
| `ar` | `ara_arab_broad.tsv` | Modern Standard Arabic, scraped from vocalized headwords. This matches the input contract in the notes of the `ar` spec. |
| `ru` | `rus_cyrl_narrow.tsv` | Upstream scraped Russian only narrow. |

### Module-generated WikiPron rows

On a large tag, the IPA column is what Wiktionary editors typed. On a small tag it often is not. Several languages have a Lua generator per language (`Module:<code>-IPA`), and the entries call it through a bare pronunciation template. The gold for such a tag is the output of that module, scraped. A low PER there measures agreement with the generator, not accuracy.

The provenance column does not say so, because the tier is set per dataset and `wikipron` as a whole is crowd-scraped. A `kaikki` row extracts the same Wiktionary source through another pipeline, so the same thing can happen there.

| Tag | What the gold is | How to read the row |
|---|---|---|
| `tew` (Tewa) | Entirely `Module:tew-IPA` output. Every headword carries a bare `{{tew-IPA}}`. | A reproduction test of the module. The spec uses the same Martinez (1982) orthography and Sutton (2014) values that the module cites. |
| `ha` (Hausa) | Entirely `Module:ha-IPA` output, computed from an editor-typed respelling with tone and length. | A reproduction test of the module, not of spoken pronunciation. See [languages/ha.md](../languages/ha.md). |
| `nmy` (Namuyi) | A mix of hand-typed IPA and `Module:nmy-IPA` output. | Partly a reproduction test. Unwritten vowel nasalization dominates the residual, which is a real gap either way. |
| `mn` (Khalkha Mongolian) | A mix, with about three entries from `Module:mn-IPA` for each hand-typed one in a sample. | Partly a reproduction test. See [languages/mn.md](../languages/mn.md). |
| `egy` (Ancient Egyptian) | Mostly `Module:egy-pron` output through `{{egy-pr}}`, with hand-typed reconstructions. | Reproduction of the Egyptological reading convention, not of how Egyptian sounded. Not eligible for comparison. See [languages/egy.md](../languages/egy.md). |
| `lo` (Lao, `kaikki`) | `Module:lo-pron` output. Almost every entry gives a Vientiane and a Luang Prabang reading, and the loader keeps the first. | Agreement with the module. Tone letters are about a third of the gold characters, and the engine writes no tone. Read the PER without tone letters. |
| `crk` (Plains Cree) | Almost entirely `Module:crk-IPA` output, with very few hand-typed rows. | The spec follows the symbol key of Bloomfield (1934), not the mechanical vowel rewrites of the module. The residual is the artefacts of the module. |
| `th` (Standard Thai) | Entirely `Module:th-pron` output, through a bare `{{th-pron}}`. | The tone part measures agreement with the tone computation of the module. See [the Thai section](#a-tone-marked-gold-measures-the-tone-computation-too-th). |

For `crk`, the module writes `i` as `ɪ`, `o` as `ʊ` and `a` as `ʌ`. It then repairs `ʌː` to `ɑː`, and `ɪ` before ⟨w y⟩ back to `i`. Copying that list would drive the PER toward zero while it certifies only the module. The spec takes the two rewrites that the Bloomfield key supports, `ɪ` and `ʊ`. The residual is the backing of `a` and `â`, which the sources call an occasional excursion, and the module's `i` before ⟨w y⟩.

No such row may certify the accuracy of a language, and none belongs in a cross-system comparison. What these rows do certify is that the spec implements the published orthography consistently. That is the claim the spec makes, and it is worth measuring under its own name.

### Languages scored against a published spelling convention (`uby`, `twf`)

In this related case the gold is hand-typed, so it is not the output of a generator. The input column is not a community spelling either. Ubykh has been extinct since 1992, and its speakers never wrote it. Every Ubykh headword on Wiktionary uses a Cyrillic system based on Abkhaz. The system is published as the [Wiktionary Ubykh entry guidelines](https://en.wiktionary.org/wiki/Wiktionary:Ubykh_entry_guidelines). Its alphabet table gives the letter-to-IPA correspondence directly, and the grapheme map of the spec is that table.

The `uby` row therefore certifies reproduction of that published convention, not accuracy about Ubykh as spoken. This is the same reading as the `egy` row, with one difference in its favour. The IPA is typed by editors, so the row still measures whether the engine converts the spelling the way a human who applies the convention does. The hand-typed inconsistencies put a floor under the residual error.

Taos (`twf`) belongs to the same class and is the stronger of the two rows. Its headwords use the practical orthography of Trager (1948), and its IPA is typed by editors: the entries carry a literal `{{IPA|twf|/…/}}`, with no module. The row certifies reproduction of the convention of Trager, and its residual error is almost all inconsistency in the hand-typed gold.

Taos is a living community language, and its orthography was taught to its speakers. The convention is one that people write, not an editorial scheme for an extinct language. The row is still not accuracy. The letters of Trager are Americanist, several of his analytic choices have documented alternatives, and the row cannot choose between them. It is not eligible for comparison.

A per-language override in `PROVENANCE_BY_LANG["wikipron"]` would put this caveat in the provenance column instead of only in prose. That needs a change to `scripts/benchmark.py`.

### Variety mismatch (`fa`)

In a third case the gold targets another variety of the language than the spec does. The `fa` gold (`fas_arab_broad.tsv`) is mostly a Classical or Early New Persian reading, and the `fa` spec targets the modern Tehran standard. The `fa` `wikipron` row therefore measures how well the spec reproduces that classical reading convention, not modern Iranian Persian. [Gold defects](gold_defects.md#persian-wikipron) gives the marker counts, and the grapheme notes of `fa.json` record them. The `fa` `ipadict` row has its own caveat, in the [ipa-dict table](#ipa-dict-pronunciation-dictionaries-ipadict).

### A tone-marked gold measures the tone computation too (`th`)

WikiPron transcribes Standard Thai with Chao tone letters, and they are about a third of all characters in the `tha_thai_broad` gold after normalization. An edit distance treats them as ordinary characters, so PER charges them in full. Read the `th` rows as two numbers: the segmental part, and the tone that the `tone_rules` block of the spec computes from consonant class, syllable shape, vowel length and tone mark. Scoring the rows with the tone letters removed from both sides gives the segmental part alone.

The two Thai golds put the tone letter in different slots. WikiPron writes it after the rime, as IPA does (`k ɔː n ˨˩`). The `vox_communis` rows, which come from Epitran, write it on the nucleus (`k ɔː˨˩ n`). The spec follows WikiPron and IPA, so the `vox_communis` row pays for the mismatch. The reverse choice would cost more on the row that a machine did not generate.

That mismatch costs placement, not tone identity. Move every tone letter to the end of the string on both sides, which keeps which tone it is and in what order. Placement then accounts for a small part of the `wikipron` PER and most of the gap on the `vox_communis` row. The tone that the spec computes differs from the tone of either gold by under a point of PER.

The tone letters of the gold follow the same rule of consonant class and syllable type that the spec states. That is not an independent confirmation. The gold is that computation (`Module:th-pron`, see [Module-generated WikiPron rows](#module-generated-wikipron-rows)), so the agreement states the rule twice. The citation for the rule is Iwasaki & Ingkaphirom (2005) and Haas (1964), not the gold.

Quote the tone-blind figure next to the `th` `wikipron` row when the question is about segments. This is a gap on the spec side, not a gold defect. The gold is right to write the tone, and the harness is right to score it. Stripping tone from tonal golds across the harness would hide a real deficiency behind a kinder number.

## Arabic with tashkeel restored (`wikipron_ar_diacritized`)

Written Arabic omits the short vowels (harakat), and none of the raw WikiPron Arabic words carry them. The raw `ar` row therefore scores the engine on input that it cannot vowelize, and missing vowels dominate its PER. This row keeps the same gold IPA and restores tashkeel on the input side only. It uses [text2tashkeel](https://github.com/TigreGotico/text2tashkeel), an ONNX diacritizer for Arabic with a diacritic error rate of about 2% on its default rawi model. The harness then strips word-final harakat. The restored case endings are real Arabic, but WikiPron records pausal pronunciations, which drop them.

Diacritization is input normalization, and it lives in the harness. orthography2ipa does no normalization by design, and a downstream Arabic consumer is expected to supply vocalized text. Both rows are published. The raw row is the floor for bare text, and the diacritized row shows what the rules earn on vowelized input.

`text2tashkeel` is an optional dependency. Without it the row is skipped, never faked, and no CI job installs it, so the row carries `"ci_reproducible": false`. The diacritized words are cached in `.benchmark_cache/wikipron_ar_diacritized.tsv`. Delete that file to diacritize again.

## WikiPron with the display headword restored (`wikipron_restored`)

WikiPron scrapes the Wiktionary page title, and for some languages the title is not the word that Wiktionary displays. The Middle High German entry guidelines keep some letters with diacritics out of article titles and use them in the displayed word. [Gold defects](gold_defects.md#middle-high-german-wikipron) quotes the policy. Ewe, Yoruba and Hebrew titles drop tone marks and niqqud the same way.

The gold IPA still transcribes those contrasts. The affected rows give the engine an input that cannot encode what it is scored on, so their PER measures the loss in the input, not the rules. In the Ewe file, most rows mark tone in the IPA that the spelling cannot express, and about half of all gold segments carry tone.

This row keeps the same gold IPA and replaces only the input word with the headword that Wiktionary renders for that language. The script `scripts/restore_wikipron_orthography.py` recovers it from the MediaWiki API, and [the pinned mirror](wikipron_mirror.md) republishes it. The row reads that mirror, never the upstream WikiPron branch. [What restoration will not do](wikipron_mirror.md#what-restoration-will-not-do) lists the rules that keep the script from guessing. A page holds one section per language: the page `Adam` alone carries an English `Adam`, a Hausa `Adàm` and an Ewe `Ádàm`.

Coverage is partial, and nothing is guessed. A page with no headword override, no section for the language, two conflicting headwords or a skeleton mismatch gives no restored word. The loader skips an empty restored cell and never falls back to the title. The row is therefore a subset of the matching `wikipron` row. Compare its PER only with that row restricted to the same words.

Most Ewe rows restore, and a minority of Middle High German rows do. For Yoruba and Hebrew, conflicting headwords are the largest uncovered category, and that is the method working. One untoned or unpointed title is often the title of several words, and the page renders a headword for each: `aba` renders `abà`, `abá`, `àba` and `àbá`. The title cannot say which one a gold row meant, so the row is refused.

The skeleton mismatches are almost all Hebrew. There the pointed spelling often drops a mater lectionis that the unpointed title writes, as `אלוהים` against `אֱלֹהִים`. That changes the consonants and is more than a restoration of diacritics.

Ewe scores very low on the restored input, low enough to deserve suspicion. Its tone is written with the same combining marks that the IPA uses, so a gold compared with itself would look the same. It is not that.

The restoration code never reads the IPA column, and no restored word in any of the four languages equals its gold. The same rows with their original spellings, through the same code, still score high, and restored words paired with shuffled golds score far worse. Hebrew settles it: its orthography is Hebrew script and its gold is IPA, so no copy is possible, and it still improves sharply. The spec does real grapheme work on the restored inputs, such as ⟨Ábràhàm⟩ to [áblàhàm] and ⟨Àbarị̀ṣà⟩ to [àbāɾʃà].

The Ewe figure says that the tone-marked orthography of Ewe is very nearly a transliteration of its phonemic transcription. For the same reason, the row cannot test the spec hard. Yoruba, with a real residual from downstep and the extended ⟨ị ụ⟩, and Hebrew are the more informative rows.

The Hebrew gold mixes transcription traditions. A minority of rows are Tiberian in flavour, with vowel length, ɔ, ə, ŋ, θ, ð, sˤ, tˤ and hataf ă, which the five-vowel inventory of Modern Israeli Hebrew cannot produce. That effect barely moves the restoration figure, because most affected words also carry a Modern transcription and the harness scores the best gold.

The few words with only non-Modern references score much worse than the rest. Restoration helps them too, but the spec describes Modern Israeli Hebrew and cannot reproduce a Tiberian transcription from any input.

Middle High German moves the other way and gets worse on restored input. The `gmh` spec maps ⟨â î ô û ä ö ü æ œ⟩ and has no entry for the ⟨ë ā ē ī ō ū ȥ⟩ that appear only in the display form. The lossy gold had hidden a real gap in the spec, and the restored input showed it. The restored row is scored against `gmh`, not `gmh-x-wikt`. The `gmh-x-wikt` spec models the title spelling that the plain `wikipron` row gives it, and the restored row is a third orthography.

The provenance stays `crowd-scraped`. The IPA is byte-identical to WikiPron, and the input word comes from the headword line of the same page, so no new annotator and no machine transcription enter. The row has every quality problem that WikiPron has, and one more. The input and the gold come from the same page, and for a near-phonemic orthography the two are not independent. A very low PER on such a language says that the spec agrees with the transliteration of the editors, not that it was tested hard.

[The pinned WikiPron mirror](wikipron_mirror.md) gives the schema of the mirror, the reason for the pin, the screen of every upstream language and the refresh.

## Norwegian under the macrolanguage code (`wikipron_nor`)

WikiPron sorts a pronunciation by the language code inside the Wiktionary `{{IPA|…}}` template, not by the language section that holds the template. Norwegian editors often tag a Nynorsk entry with the macrolanguage code `no` instead of `nn`. Those pronunciations are then scraped into `nor_latn_broad.tsv`, not `nno_latn_broad.tsv`.

A random sample of the headwords of that file found most of their `{{IPA|no|…}}` lines under a `==Norwegian Nynorsk==` section, about one in eight under `==Norwegian Bokmål==`, and a few under both or under the old `==Norwegian==` heading. The file is Nynorsk with a Bokmål minority, and it is scored against the `nn` spec.

The file stays a row of its own and is not folded into `wikipron` `nn`. It is a separate file with its own annotators and its own Bokmål contamination. A merge would let each file hide the other. The contamination would vanish into a larger denominator, and a movement on either file would lose its cause.

## CMU Pronouncing Dictionary

[cmudict](https://github.com/cmusphinx/cmudict) holds American English entries that the CMU Speech Group curated by hand in ARPABET. [scriptconv](https://github.com/TigreGotico/scriptconv) converts them to IPA, and that mechanical transform can add its own errors. English spelling is deeply irregular, so this row is a floor for a rule-driven engine.

## European Portuguese regional dialect gold set (`ep_dialects`)

The TigreGotico team that maintains the dialect specs annotated these sentences in dialectal IPA. The annotation follows the classification of Cintra, L.F.L. (1971), "Nova proposta de classificação dos dialectos galego-portugueses", *Boletim de Filologia* 22:81-116. The set is pending external peer validation. The CSV is `tests/data/ep_dialect_sentences.csv`, and the harness maps its dialect codes to these tags:

| CSV `dialect_code` | Tag | Note |
|---|---|---|
| `pt-PT-x-lisboa` | `pt-PT-x-lisbon` | Lisbon prestige variety |
| `pt-PT-x-north` | `pt-PT-x-porto` | Porto and Baixo-Minho |
| `pt-PT-x-central` | `pt-PT` | The conservative standard of the Coimbra type |
| `pt-PT-x-alentejo` | `pt-PT-x-alentejo` | |
| `pt-PT-x-algarve` | `pt-PT-x-algarve` | |
| `pt-PT-x-madeira` | `pt-PT-x-madeira` | |
| `pt-PT-x-azores` | `pt-PT-x-acores` | |

The gold is sentence-level phonetics, with connected-speech reductions, liaison and elisions conditioned by stress. PER is therefore higher than on the lexicon benchmarks. The row measures how well the engine captures the grapheme-to-phoneme rules of a dialect, not its connected-speech phonology. Each tag has only a few dozen sentences, so read the confidence interval.

## CLUP dialect archive gold set (`clup_dialect`)

[TigreGotico/ArquivoDialetalCLUP_ipa](https://huggingface.co/datasets/TigreGotico/ArquivoDialetalCLUP_ipa) holds sentence-level IPA transcriptions of interview excerpts from the [Arquivo Dialetal](https://cl.up.pt/arquivo/) of the Centro de Linguística da Universidade do Porto (CLUP). The interviews are expert university dialectology. Neither the loader nor the dataset card says who or what produced the IPA column, so read the `expert-human` tier as the best case. Each row carries a `"<locality>, <district>"` label. The loader maps a row to a tag by locality first, on an exact match, and then by district:

| District or locality | Tag |
|---|---|
| Porto | `pt-PT-x-porto` |
| Braga | `pt-PT-x-minho` |
| Viseu, Coimbra | `pt-PT-x-beira` |
| Aveiro | `pt-PT-x-aveiro` |
| Bragança, Vila Real | `pt-PT-x-tras-os-montes` |
| Lisboa | `pt-PT-x-lisbon` |
| Funchal, Ribeira Brava, Porto Santo | `pt-PT-x-madeira` |
| Viana do Castelo | `pt-PT-x-viana` |
| Faro | `pt-PT-x-algarve` |
| Terceira, São Miguel | `pt-PT-x-acores` |
| Portalegre | `pt-PT-x-alentejo` |
| Alfena (locality in Porto) | `pt-PT-x-alfena` |

Two rows, from Marinha Grande and Amor in the Leiria district, are excluded. Leiria straddles the boundary between the Estremadura and Beira Litoral dialects, and no spec here covers it, so the rows are dropped and not forced into a neighbour. The gold is connected speech, as in `ep_dialects`, so PER is higher than on the lexicon benchmarks. Most tags have only a handful of rows, so read the interval, not the point PER.

## Mirandese gold set

[TigreGotico/mirandese_g2p](https://huggingface.co/datasets/TigreGotico/mirandese_g2p) holds word and IPA rows with a `dialect` column, collected by a native speaker of Mirandese ([MdMV](https://commons.wikimedia.org/wiki/User:MdMV_or_Emdy_idk)). Its registry key is `mirandese_g2p`, and it is split by that column:

| `dialect` | Tag | Variety |
|---|---|---|
| `central` | `mwl` | The Central norm that the Mirandese orthography is built on |
| `sendinese` | `mwl-x-sendim` | The Sendim sub-dialect |
| `raiano` | `mwl-x-ifanes` | The Raiano or Northern sub-dialect, whose Ifanês variety this repository tags `mwl-x-ifanes` |

Its native-speaker provenance makes it the reference gold and the most trustworthy signal for Mirandese. It is separate from, and more reliable than, any synthetic Mirandese dictionary. It is small, and `mwl-x-ifanes` has only a few rows, so read the confidence interval.

## Barranquenho synthetic IPA dictionary (`barranquenho_dict`)

[TigreGotico/barranquenho-ipa-dict-synthetic](https://huggingface.co/datasets/TigreGotico/barranquenho-ipa-dict-synthetic) holds word and IPA entries for Barranquenho, the Portuguese-Spanish contact variety of Barrancos, scored against the `ext-PT-x-barranco` spec. Each row also carries a part of speech, the Portuguese and Spanish equivalents, and a phonological note. Only the orthography and IPA columns are scored.

A large language model (Claude) wrote the IPA, conditioned on the published *Convenção Ortográfica do Barranquenho* and descriptive research on the variety. No phonemizer, no part of this engine and no consumer of it produced the IPA, so scoring against it is not circular. No phonetician verified it, and it can be wrong. The tier is `llm-generated`, so the row gates nothing and is a [direction only](benchmarks.md#provenance-discipline).

## Mirandese synthetic IPA dictionary (`mirandese_dict`)

[TigreGotico/mirandese-ipa-dict-synthetic](https://huggingface.co/datasets/TigreGotico/mirandese-ipa-dict-synthetic) holds word and IPA entries for Mirandese, each with a `dialect` column. It is a separate source from the native-speaker gold above, and it complements it. Each row is scored under exactly one tag:

| `dialect` | Tag | Note |
|---|---|---|
| `central`, `all` | `mwl` | The Central norm. `all` marks forms that every variety shares. |
| `sendinês` | `mwl-x-sendim` | Southern Sendinês |
| `raiano` | `mwl-x-ifanes` | Ifanês is the Northern or Raiano sub-dialect in this spec set. Only a few rows, so read the interval. |

The provenance is the same as for `barranquenho_dict`. A large language model (Claude) wrote the IPA, conditioned on the *Convenção Ortográfica da Língua Mirandesa* and descriptive research on the sub-dialects. The row is not circular, not verified by a phonetician, and possibly wrong. The tier is `llm-generated`, and the row is a direction only.

## 4catac Catalan accents gold set

[projecte-aina/4catac](https://huggingface.co/datasets/projecte-aina/4catac) holds sentence-level rows in IPA, transcribed by experts to the guidelines of the Institut d'Estudis Catalans and reviewed by several annotators for consensus. The same sentences, with small morphological adaptations, are transcribed separately for four accents, one TSV per accent:

| File | Tag | Accent |
|---|---|---|
| `Projecte BSC frases - Central.tsv` | `ca` | Central, the standard |
| `Projecte BSC frases - Balear.tsv` | `ca-x-balear` | Balearic |
| `Projecte BSC frases - Nord-Occ.tsv` | `ca-x-occident` | North-Western (Lleidatà), not `ca-x-nord`. Northern Catalan (Rossellonès) is a separate dialect of France that 4catac does not cover. |
| `Projecte BSC frases - Val.tsv` | `ca-x-valencia` | Valencian |

The authors "intentionally wrote" the sentences "to showcase various phonetic phenomena", so the set is targeted, not a random sample. The gold is sentence-level, so PER includes connected-speech phonology on top of the grapheme rules and is higher than on the lexicon benchmarks. A low exact match there reflects notation and connected speech, not total failure. No rows are excluded.

## ipa-dict pronunciation dictionaries (`ipadict`)

[open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict) collects open pronunciation dictionaries in `word TAB /IPA/` format. A word with several pronunciations lists them comma-separated (`est  /ɛst/, /ɛ/`). The loader writes each variant as its own gold pair. The project is MIT-licensed, and each third-party file keeps its own licence.

Read the tier before the number, because ipa-dict is not one source. The README Credits section is the only authority on where the IPA of each file came from. It shows human dictionaries, Wiktionary scrapes, rule scripts and phonemizer output side by side. The dataset therefore has a tier per language (`_IPADICT_PROVENANCE` in `scripts/benchmark.py`, read by `provenance_for`).

The main trap is `en_UK`, which is espeak output. It is credited to [ipacards](https://github.com/leoboiko/ipacards), whose `CREDITS` and `bin/add-ipa-to-freq.py` call `espeak`. That row can neither qualify nor block English (see [quality_tiers.md](../specs/quality_tiers.md)), so read the CMUdict and WikiPron English rows instead.

A file for which the Credits name no source is `machine-generated`, marked as unverified. A tier is never upgraded on a guess.

| Tag | File | Tier | Source, per the Credits |
|---|---|---|---|
| `is` | `is.txt` | lexicon-derived | [Pronunciation Dictionary for Icelandic](http://malfong.is/?pg=framburdur&lang=en) (Hjal project), CC BY 3.0, curated by Icelandic linguists. Larger than the WikiPron Icelandic file, so it is the main Icelandic gold. |
| `en-US` | `en_US.txt` | lexicon-derived | [cmudict-ipa](https://github.com/lingz/cmudict-ipa) with stress from [syllabify](https://github.com/kylebgorman/syllabify), MIT. The same lineage as `cmudict`, with another notation transform. |
| `ja` | `ja.txt` | lexicon-derived | [EDICT](https://www.edrdg.org/jmdict/edict.html) readings (EDRDG), CC BY-SA 3.0. A word written only in kanji transcribes to `''` (see the Japanese note below the tables). |
| `jam` | `jam.txt` | lexicon-derived | [A Learner's Grammar of Jamaican](https://github.com/opengrammar/jam-learners-grammar) (Open Grammar Project), CC BY 4.0. |
| `km` | `km.txt` | lexicon-derived | [Khmer-English Dictionary](https://www.aakanee.com/AC-Khmer/X/dict.html) (aakanee.com), CC BY-NC-SA 4.0. |
| `ro-RO` | `ro.txt` | lexicon-derived | [MaRePhoR](https://speech.utcluj.ro/marephor/) phonetic dictionary (UTCluj), CC BY-NC. |
| `sv` | `sv.txt` | lexicon-derived | [Folkets lexikon](https://folkets-lexikon.csc.kth.se/folkets/) (KTH), CC BY-SA 2.5. |
| `de-DE` | `de.txt` | crowd-scraped | [german-ipa-dict](https://github.com/devio-at/german-ipa-dict), built from Wiktionary, CC BY-SA. |
| `ko` | `ko.txt` | crowd-scraped | Korean Wiktionary through [korean-word-ipa-dictionary](https://github.com/laviande22/korean-word-ipa-dictionary), CC BY-SA. The `ko` spec reads Hangul syllable blocks. |
| `ar` | `ar.txt` | machine-generated | The output of the Arabic Morphological Analyzer of Tim Buckwalter. |
| `es-ES` | `es_ES.txt` | machine-generated | The [spanish-pronunciation-rules](https://github.com/easypronunciation/spanish-pronunciation-rules-php) PHP script, which its README calls "experimental". |
| `es-MX` | `es_MX.txt` | machine-generated | The same script. The file is near-identical to `es_ES`, so the two rows are not independent evidence. |
| `fa` | `fa.txt` | machine-generated | Wiktionary, [PersPred](http://perspred.cnrs.fr/perspred-project) and "a great deal of guesswork". The README calls it "extremely experimental", so an improvement against this row is no evidence about Persian. |
| `fi` | `fi.txt` | machine-generated | [prosodic1b](https://github.com/jsfalk/prosodic1b), a rule-based tool, over the Kotus word list, GPL 2.0. |
| `nl` | `nl.txt` | machine-generated | Instituut voor de Nederlandse Taal, CC BY. The README says that "no manual correction or revision has been done". |
| `or` | `or.txt` | machine-generated | [OdiaWikimedia Converter](https://github.com/OdiaWikimedia/Converter/tree/master/IPA-Romanization) over Wikimedia dumps. |
| `vi` | `vi_N.txt` | machine-generated | The [vPhon](https://github.com/kirbyj/vPhon) converter over the word list of Ho Ngoc Duc. Northern (Hanoi) is the standard that the `vi` spec targets. |
| `nb` | `nb.txt` | machine-generated | The generation method is not documented. A credit for correcting and updating the file is not evidence of expert authorship. |
| `eo` | `eo.txt` | machine-generated | Unverified. The Credits name no source. |
| `fr-FR` | `fr_FR.txt` | machine-generated | Unverified. The Credits name no source. |
| `ms` | `ma.txt` | machine-generated | Unverified. ipa-dict `ma` is Malay (Malaysian and Indonesian), the `ms` spec, not Moroccan Arabic. |
| `pt-BR` | `pt_BR.txt` | machine-generated | Unverified. The Credits name no source. |
| `sw` | `sw.txt` | machine-generated | Unverified. The entries even keep capital letters in the IPA, as in `Abadoni /Aɓaɗoni/`. |
| `en-GB` | `en_UK.txt` | espeak-derived | [ipacards](https://github.com/leoboiko/ipacards) (GPL 3.0), whose credits list espeak and whose script calls it. Cannot qualify or block English. |

The files not wired are recorded with their reasons in `_IPADICT_UNWIRED`:

| File | Reason |
|---|---|
| `zh_hans`, `zh_hant` | Han-script gold. The `zh` spec is a pinyin romanization spec (`OrthographyKind.ROMANIZATION`), and the Han-script `zh-Hani` spec writes nothing for a Han character (`G2P("zh-Hani").transcribe_word("一") == ""`). The two files differ only in written standard. |
| `yue` | Han-script gold, and `G2P("yue")` writes nothing for it. The gold itself (KFCD Pingyam and 開放粵語詞典, CC BY 3.0) is good. The gap is on this side. |
| `fr_QC` | No Québécois spec is registered. The file is also the output of the qc-ipa script over `fr_FR` ("highly experimental"). |
| `tts` | Isan, or Northeastern Thai ([Isaan-English Dictionary](https://www.aakanee.com/AC-Isaan/X/dict.html), CC BY-NC-SA 4.0). No `tts` spec is registered, and the `th` spec is another language. |
| `vi_C`, `vi_S` | No Central or Southern Vietnamese spec is registered. |

The Han-script files are a gap in the engine, not in the gold. They are among the better-sourced files of the project, and they can be wired once a spec reads a logographic orthography. Odia (`or`) scores, but it is an abugida. Read its number against the state of abugida handling, not as a verdict on the `or` spec.

The Japanese row scores fewer words than its loader yields, because a word written only in kanji gets no hypothesis from the kana spec and drops out. A word that contains at least one kana is scored, and most Japanese words are a kanji stem with a kana ending. The engine then reads the ending and must still produce the reading of the whole word.

Those words carry several times the error rate of the words written only in kana, and they outnumber them. The Japanese PER therefore mostly measures the missing kanji front-end. The quality of the kana-to-IPA rules shows only in the all-kana subset, and no board column reports that subset.

## HiTZ Basque Wikipedia IPA corpus (`hitz_basque_ipa`)

[HiTZ/wikipedia_basque_ipa](https://huggingface.co/datasets/HiTZ/wikipedia_basque_ipa) holds paragraph-level `text` and `phonemes` rows extracted from the Basque Wikipedia dump. HiTZ Zentroa and AhoLab publish it. AhoLab is the language technology group of the University of the Basque Country (UPV/EHU).

ahoNT, the Basque text processing and phonemization tool of HiTZ, produced the IPA, so this is tool output, not human annotation.

This dataset is an explicit exception to the [provenance discipline](benchmarks.md#provenance-discipline), because an academic research group publishes it. The row is additive to the `wikipron` `eu` row, which is the independent gold for Basque. A low PER for AhoTTS on this row only shows that the tool reproduces itself, so compare AhoTTS on the `wikipron` `eu` row instead.

The source data is paragraph-level, so `load_hitz_basque` pages the dataset through the `rows` REST API of the Hugging Face datasets server and never downloads the full parquet. It splits the `text` and `phonemes` of each paragraph on whitespace in step. The dataset card says ahoNT writes one phoneme token per source word, with punctuation attached. The loader pairs the tokens by position, strips punctuation from both sides, and collects unique single-word pairs.

It stops after `_HITZ_BASQUE_MAX_PARAGRAPHS` (500) paragraphs, a bound that `--limit` cannot lift, so even the full scoreboard scores only the words from those paragraphs. The loader scores single words, as `load_ep_dialects` does for gold that is not shaped like a lexicon. Nothing shows that ahoNT places stress by sentence context, so a single token is the conservative unit.

## VoxCommunis parallel G2P (`vox_communis`)

[fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p) (CC0) holds Common Voice utterances force-aligned by the VoxCommunis Corpus. Each utterance has a phone string from lexicons built with Epitran, the XPF Corpus, Charsiu and custom dictionaries. VoxCommunis corrected part of them by hand, but no row says which. There is one small TSV per language.

69 language tags are wired: every file with a matching spec, and a few regional aliases. The aliases are `sv-se` to `sv`, `hy-am` to `hy`, `fy-nl` to `fy`, `pa-in` to `pa`, and the `pt` file with no region to `pt-BR`. The `zh-cn` and `yue` files are deliberately not wired (see [Rejected candidates](#rejected-candidates)). The tier is `epitran-derived`, because Epitran is a scored competitor in [comparison.md](generated/comparison.md). A disagreement measures divergence from the output of a competitor. The row is a breadth signal only, and it can never gate a regression or qualify a spec.

The `phonemized_sentence` column holds phones separated by spaces, with `|` between words, aligned with the whitespace tokens of `aligned_sentence`. The loader splits rows into word pairs like `ipa_childes`. It skips rows whose token counts differ and strips alignment artefacts.

The loader drops `spn` tokens and does not score them. `spn` is the "spoken noise" symbol of the Montreal Forced Aligner, and VoxCommunis reuses it for any word that its lexicon could not cover. It marks a hole in coverage, not a transcription. PER divides by the gold length, so one real long word scored against a three-character `spn` gives a per-word PER above 3, and the error has no bound. Some files lose a large share of their tokens to `spn`, worst of all Kazakh, Abkhaz and Chuvash.

`spn` is the only token filtered. Its siblings `sil`, `sp`, `nsn` and `noise` do occur, but mostly as real transcriptions of real words: Welsh `sul` is /sil/, and Amharic `ሲል`, Bulgarian `сп`, Tamil `ஸ்ப்`, Korean `실` and Punjabi `ਸੀਲ` are similar. Filtering on the phone string would delete real gold.

A few rows carry the marker on both tiers (word `sil`, phones `sil`), which looks like a placeholder from the aligner. Those rows stay too, because the identity test is not safe either. Turkish `sil` ("wipe") is a real word pronounced [sil]. The few such rows are far below the noise floor of an `epitran-derived` row.

### Notation, not phonology (`vi`, `pa`, `as`)

With `spn` gone, the `vi`, `pa` and `as` rows still score high. In all three the distance is a transcription convention, not a phonological disagreement. Vietnamese differs by tone-letter placement, vowel-length marking and a few symbol variants. Punjabi differs by length marking, a few vowel and rhotic symbols, and final schwa deletion. Assamese differs by length marking, similar symbol choices, and final ɔ deletion.

The scripts `scripts/fold_vi_notation.py` and `scripts/fold_pa_notation.py` remove one convention at a time from both sides and score again with the `normalize()` of the harness. Most of the Vietnamese distance goes once the conventions are folded. The `as` folding has no committed script, so no figure is stated for it. None of these folds belongs in `normalize()`, which is the one scorer for every row, and tone-letter placement is specific to each language. The rows stay as scored, and readers take the offset into account.

The `vi` gold is also wrong in one respect, not only different: it merges the tones ngang and huyền ([gold defects](gold_defects.md#vietnamese-vox_communis) has the evidence). The `epitran-derived` tier already keeps the row out of every gating decision. The finding therefore stays in prose, here and in [languages/vi.md](../languages/vi.md), and not in a per-language override. An override to `machine-generated` would give the row a gating vote ([reliability tiers](benchmarks.md#reliability-tiers)). `vox_communis_corrected` repairs the merge (see below).

### European Portuguese under a Brazilian label (`pt-BR`)

The VoxCommunis `pt` file is the Common Voice locale with no region. It is mapped to `pt-BR`, because most Portuguese traffic on Common Voice is Brazilian. Its phone tier is not. `scripts/fold_pt_br_notation.py` measures the whole cached file, and none of the features that separate Brazilian from European Portuguese appear in it. Final ⟨-l⟩ never vocalizes to [w], ⟨t⟩ never affricates before /i/, ⟨d⟩ almost never does, and final unstressed ⟨-e⟩ and ⟨-o⟩ never raise to [i] and [u]. The European coda sibilant [ʃ] appears on every word that ends in ⟨-s⟩.

The file is also wrong about Portuguese of any variety in two ways. Its symbol inventory has neither ⟨ʎ⟩ nor ⟨ɲ⟩, so the ⟨lh⟩ and ⟨nh⟩ digraphs just lose their ⟨h⟩ (`gatilho` gives `ɡɐtilo`, `tinha` gives `tinɐ`). It also applies the European coda rule inside the ⟨ss⟩ digraph and writes [ʃs] on almost every ⟨ss⟩ word (`isso` gives `iʃso`). Folding ten conventions of the gold out of both sides, one at a time, removes most of the distance. As for `vi`, the folds stay out of `normalize()` and the row stays as scored. See [languages/pt-BR.md](../languages/pt-BR.md).

### Serbian contamination (`sr`)

About a third of the Serbian tokens carry a spurious word-initial `z` in the phone tier that comes from Charsiu (`не` gives `znɛ`, `и` gives `zi`, `а` gives `za`). It is never doubled on words that really start with `з`, so it is an artefact of the upstream lexicon, not a convention. It is not filtered, because no test separates it from a real word-initial /z/ without a guess. It inflates the `sr` row by a few PER points. Read the row with that offset in mind.

### Coverage hole in Bashkir (`ba`)

The Bashkir gold cannot see the two letters that define Bashkir. A large share of the word tokens in `ba.tsv` are spelled with ⟨ҙ⟩ or ⟨ҫ⟩, the interdentals /ð/ and /θ/ that separate Bashkir from Tatar. The upstream phonemizer maps neither letter, so it writes every such token as `spn`, and the `spn` filter drops them all. The words that remain contain no ⟨ҙ⟩ and no ⟨ҫ⟩.

The row is therefore a sample of the Bashkir that Epitran covers, and no score on it can reward or punish the /ð/ and /θ/ rules of the spec. The row stays because it measures the rest of the alphabet across a large vocabulary. Read it as breadth only. The `wikipron` row and the unit tests defend the interdentals.

### Coverage hole in Abkhaz (`ab`)

The Abkhaz gold has no symbol for labialization, and more than half of its word types are `spn`. [Gold defects](gold_defects.md#abkhaz-vox_communis) gives the counts and the eight letters that are always `spn`. What survives is the part of Abkhaz without labialization, and most of its remaining distance is convention, not mapping.

Three folds remove most of it. The first maps the undotted ⟨ш ж ҽ ҿ⟩ series of the gold onto the retroflex symbols of the spec. The second removes the aspiration that the gold never writes. The third reads ⟨е о и у⟩ as the underlying /aj aw j w/ of the gold. A small part of real disagreement remains. The spec keeps aspiration and the retroflex series, because the JIPA Illustration of Abkhaz transcribes the name of the language as /apʰsaʃʷa/ ([doi:10.1017/S0025100320000390](https://doi.org/10.1017/S0025100320000390)). The independent `wikipron` `ab` row marks aspiration too.

The row gets no `PROVENANCE_BY_LANG` override, on purpose. The tier ladder has no rung below the output of a competitor. An override to `machine-generated` would give the row a gating vote ([reliability tiers](benchmarks.md#reliability-tiers)). The dataset tier stays, and the row stays non-qualifying, although [the `epitran` part of the label is wrong](gold_defects.md#abkhaz-vox_communis-1) for this row.

### Coverage hole in Guaraní (`gn`)

The `gn` gold cannot write two of the phonemes that it is scored on. Guaraní prenasalizes ⟨m⟩ and ⟨n⟩ before an oral vowel (`retãme` gives `ɾetãᵐbe`, `mba'épiko` gives `ᵐbaʔepiko`). The upstream phonemizer writes only the prenasalized cluster, so no word with ⟨m⟩ has a plain [m] in the gold. The gold also never writes [ɲ] for ⟨ñ⟩. It writes [dʒ], the same value it gives to plain ⟨j⟩, so it cannot tell ⟨ñ⟩ from ⟨j⟩ at all.

The smaller `wikipron` `gn` row has neither gap, so the problem is the phonemizer of this gold, not Guaraní. A spec that writes plain [m] and [ɲ] where the orthography asks for them never matches this gold on those words. That is a ceiling set by the tool, as the [provenance discipline](benchmarks.md#provenance-discipline) describes.

## VoxCommunis with the Vietnamese tone merge repaired (`vox_communis_corrected`)

The Vietnamese phone tier writes the same Chao tone letter ˨˨ for *ngang* (A1, the unmarked tone) and *huyền* (A2) ([gold defects](gold_defects.md#vietnamese-vox_communis) counts the merge). The Illustration of the IPA by Kirby tabulates them as separate categories, on the minimal pair ⟨ma⟩ 'ghost' (ngang, "level") and ⟨mà⟩ 'but, yet' (huyền, "mid falling"):

> Kirby, James P. (2011). Vietnamese (Hanoi Vietnamese). *Journal of the International Phonetic Association* 41(3): 381-392, tone table p. 386. <https://doi.org/10.1017/S0025100311000181>

The repair comes from the spelling alone, and that is what makes it admissible. Vietnamese writes huyền with a combining grave accent (⟨à è ì ò ù ỳ⟩ and their circumflex, breve and horn variants) and ngang with no tone mark. The combining marks therefore show which of the two merged tones a syllable carries, with no phonological model involved. The overlay rewrites the grave-accented readings to ˧˩. Kirby prints tone letters, not Chao digits, and labels huyền "mid falling" against the "low falling" of hỏi. Huyền must therefore start above hỏi, which this gold writes ˨˩˨.

Some tokens stay uncorrected and are counted. A huyền token whose reading is not a single ˨˨ stays, because in a reading of several syllables no single tone letter is the merged one. A token with two tone marks stays, because its tone cannot be read from the spelling. The merged ngang tokens are not corrected either. ˨˨ is what this gold writes for ngang, and no citation makes it wrong within the scale of this gold.

The repair does not move PER, and that is worth knowing. The engine writes huyền as ˧˨, which is one substitution away from the merged ˨˨ and one from the corrected ˧˩. The repair is equivalent in edit distance, and PER cannot see this defect. Writing the engine's own ˧˨ into the gold would lower the PER of the row by several points. That gain would come from copying the answer, which is exactly why the derivation rule exists.

## ipa-dict with the pt-BR hyphenated-word stress repaired (`ipadict_corrected`)

The ipa-dict Brazilian Portuguese file `pt_BR.txt` writes one primary stress on each hyphenated word, and on many of them it puts the stress on the wrong syllable. In enclitic forms it stresses the penultimate syllable of host and clitic written as one string (*acusa-o* `a.ku.ˈza.ʊ`). The clitic is unstressed, and the host keeps its own stress. In compounds it stresses an element before the last (*pós-ditadura* `ˈpɔʒ.dʒi.ta.du.ɾə`). The last element carries the main stress of a Portuguese compound:

> Toneli, Priscila Marques (2011). O comportamento prosódico de palavras compostas no Português Brasileiro. I Congresso Nacional de Estudos Linguísticos, p. 2.

> Bechara, *Moderna Gramática Portuguesa*, p. 340, quoted in Ciberdúvidas da Língua Portuguesa, resposta 28042. <https://ciberduvidas.iscte-iul.pt/consultorio/perguntas/x/28042>

The repair reads the stressed syllable of the host, or of the last element, from the spelling by the accent rules of the Acordo Ortográfico 1990. It moves only the stress mark onto the gold's own syllable, and no segment changes. A row stays as it is when the vowel nuclei of the spelling do not add up to the syllable count of the gold, or when an element is empty. It also stays for a misspelt *-lo* enclisis such as *ajuda-lo*, and for mesoclisis. The overlay file and its README in `orthography2ipa/data/gold/corrections/` give the full rule, and the build report counts each case.

The row keeps the `machine-generated` tier of the base file and, like every [overlay](benchmarks.md#corrections-overlays), never gates. PER is the same on both rows, because PER strips stress marks. Stress accuracy rises on `ipadict_corrected` over the same eligible words.

## IPA-CHILDES split (`ipa_childes`)

[fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split) is a processed version of IPA-CHILDES, the phonemized CHILDES corpus of child language (CC BY 4.0), split into `train` and `test` CSVs per language. Each row is an utterance with several IPA columns. The harness uses `ipa_g2p_plus`, the column from the G2P+ phonemizer. The dataset writes it with one segment per orthographic word, separated by `" | "`, aligned by position with the whitespace tokens of the sentence. The CHILDES academic-corpus exception admits these tool transcriptions as gold, but which tool made them matters, and it differs per language.

### Provenance: one tool per language, and every one of them is a competitor

The [IPA-CHILDES dataset card](https://huggingface.co/datasets/phonemetransformers/IPA-CHILDES) names the phonemizing tool per language. Most languages went through `phonemizer`, whose backend is espeak-ng. Six went through epitran, and Mandarin went through `pinyin_to_ipa`. espeak-ng and epitran are both systems that this project scores itself against ([comparison](generated/comparison.md) has `espeak_per` and `epitran_per` columns). An IPA-CHILDES row therefore measures agreement with a competitor, not correctness. Each row takes the tier of its own tool, from `_IPA_CHILDES_TOOL` through `_IPA_CHILDES_PROVENANCE` in `scripts/benchmark.py`, and a test enforces the mapping. None of the espeak or epitran rows can qualify or block a language for `production` ([quality tiers](../specs/quality_tiers.md)).

| Tag | Dataset folder | Tool, per the card | Tier |
|---|---|---|---|
| `ca` | `ca-ES` | `phonemizer` (espeak-ng), `ca` | espeak-derived |
| `cy` | `cy-GB` | `phonemizer` (espeak-ng), `cy` | espeak-derived |
| `da` | `da-DK` | `phonemizer` (espeak-ng), `da` | espeak-derived |
| `de-DE` | `de-DE` | `epitran`, `deu-Latn` | epitran-derived |
| `en-GB` | `en-GB` | `phonemizer` (espeak-ng), `en-gb` | espeak-derived |
| `en-US` | `en-US` | `phonemizer` (espeak-ng), `en-us` | espeak-derived |
| `es-ES` | `es-ES` | `epitran`, `spa-Latn` | epitran-derived |
| `et` | `et-EE` | `phonemizer` (espeak-ng), `et` | espeak-derived |
| `eu` | `eu-ES` | `phonemizer` (espeak-ng), `eu` | espeak-derived |
| `fr-FR` | `fr-FR` | `phonemizer` (espeak-ng), `fr-fr` | espeak-derived |
| `ga` | `ga-IE` | `phonemizer` (espeak-ng), `ga` | espeak-derived |
| `hr` | `hr-HR` | `epitran`, `hrv-Latn` | epitran-derived |
| `hu` | `hu-HU` | `epitran`, `hun-Latn` | epitran-derived |
| `id` | `id-ID` | `epitran`, `ind-Latn` | epitran-derived |
| `is` | `is-IS` | `phonemizer` (espeak-ng), `is` | espeak-derived |
| `it-IT` | `it-IT` | `phonemizer` (espeak-ng), `it` | espeak-derived |
| `nb` | `nb-NO` | `phonemizer` (espeak-ng), `nb` | espeak-derived |
| `nl` | `nl-NL` | `phonemizer` (espeak-ng), `nl` | espeak-derived |
| `pl` | `pl-PL` | `phonemizer` (espeak-ng), `pl` | espeak-derived |
| `pt-BR` | `pt-BR` | `phonemizer` (espeak-ng), `pt-br` | espeak-derived |
| `pt-PT` | `pt-PT` | `phonemizer` (espeak-ng), `pt` | espeak-derived |
| `quz` | `qu-PE` | `phonemizer` (espeak-ng), `qu` | espeak-derived |
| `ro-RO` | `ro-RO` | `phonemizer` (espeak-ng), `ro` | espeak-derived |
| `sr` | `sr-RS` | `epitran`, `srp-Latn` | epitran-derived |
| `sv` | `sv-SE` | `phonemizer` (espeak-ng), `sv` | espeak-derived |
| `tr` | `tr-TR` | `phonemizer` (espeak-ng), `tr` | espeak-derived |
| `zh` | `zh-CN` | `pinyin_to_ipa`, `mandarin` | machine-generated |

The `pinyin_to_ipa` tool of Mandarin is a deterministic table from Pinyin to IPA, not a G2P system that this project competes with. It is therefore `machine-generated`, not a competitor tier, but it is still the output of a tool and still not the truth.

The harness reads only the `test` split, which G2P+ training held out. The loader `load_ipa_childes` splits the orthographic sentence on whitespace and the `ipa_g2p_plus` column on `" | "`, and pairs the tokens by position. It skips rows whose token counts differ and collects unique single-word pairs. The full scoreboard reads the whole test split, and `--limit N` keeps the first N. This is the positional alignment that `load_hitz_basque` uses, applied to an alignment that the dataset already provides.

For `zh`, the loader reads the `stem` column, not `sentence`. The `sentence` column is Hanzi, and the `zh` spec models Pinyin syllables, with a grapheme table of Pinyin initials and finals. The `stem` column is the Pinyin of CHILDES, with tone numbers, for the same utterance, so it is the column that exercises the spec.

These folders are in the dataset and are not wired:

| Folder | Reason |
|---|---|
| `fa-IR` | The Persian transcripts are Fingilish, an ad hoc Latin transliteration (`"piano kar kardam"`), never Persian script. The `fa` spec reads Arabic script only. |
| `ja-JP` | The Japanese transcripts are romaji only, with no kana or kanji column, and the `ja` spec has a hiragana grapheme table. |
| `ko-KR` | The `ko` spec reads Hangul syllable blocks, so the folder can be wired. Its Korean column needs its own check first: which phonemizer made it, and whether it is romanization or Hangul. |
| `yue-CN` | The `yue` spec is a stub with an empty grapheme inventory, and the romanized column of the dataset is Jyutping with tone numbers, which the stub does not model. `G2P('yue').transcribe_word(...)` returns `""` for every row. A spec gap, not a gold problem. |

### German (`de-DE`): the epitran row measures a ceiling, not a defect

The three word-level German golds disagree with each other far more than a reading of "German is mediocre" would suggest. On the words that `wikipron`, `ipadict` and `ipa_childes` all contain, with the same engine and normalization, the spec scores far worse against the epitran output of `ipa_childes` than against the two human golds. German does not score worse than its peers. It scores worse against epitran specifically.

The reason is systematic. The epitran gold almost never writes ə or ɐ, the two most common reduced vowels of German, while the engine writes them often. Words that end in ⟨-e⟩ almost always end in a full mid vowel in the gold, often long, and hardly ever in ə. Words that end in ⟨-er⟩ never end in ɐ. Most words that end in ⟨b d g⟩ keep a voiced final stop, so final devoicing (Auslautverhärtung) is missing.

Most words that start with ⟨Sp⟩ or ⟨St⟩ have a plain /s/, not the /ʃp/ and /ʃt/ that standard German requires. The gold also writes far more length marks than the engine.

Each of these is a correct, standard description of German, and each reads as an error against this gold. The `deu-Latn` table of epitran does not model final schwa, vocalized /r/, final devoicing, initial /ʃ/ before /p t/, or the vowel-length contrasts of German. Putting the full-vowel convention for final schwa into the engine output, with nothing else changed, lowers the PER of the row clearly by itself. The other conventions account for further slices of the gap. A score well below that residual would mean reproducing the omissions of epitran, not describing German. The `epitran-derived` tier ([Reliability tiers](benchmarks.md#reliability-tiers)) already says that this row can never certify the spec.

## IPA-BabyLM (`ipa_babylm`)

[phonemetransformers/IPA-BabyLM](https://huggingface.co/datasets/phonemetransformers/IPA-BabyLM) holds the BabyLM 2024 pre-training corpora (BNC spoken, CHILDES, Gutenberg, OpenSubtitles, Simple Wikipedia and Switchboard), converted to phonemes with [G2P+](https://github.com/codebyzeb/g2p-plus). It covers English only. The two configs, `strict` and `strict-small`, differ only in their train split and share one `dev` split, so there is one gold set here, not two. The harness reads only the held-out `dev` split, never the train data that the models were trained on.

The provenance is espeak at one remove. G2P+ is a wrapper whose backends are `phonemizer` and `epitran`, and its `phonemizer` backend needs espeak-ng. The notebook that produced this dataset ([codebyzeb/babylm-ipa](https://github.com/codebyzeb/babylm-ipa), `prepare_babylm.ipynb`) calls `transcribe_utterances(..., "phonemizer", language="en-us", ...)`. The gold is therefore espeak-ng output. Its tier is `espeak-derived`, and it can neither qualify nor block English.

The loader pairs the `text` column with the `phonemized_utterance` column by position. That column holds IPA segments separated by spaces, with `WORD_BOUNDARY` between words. The loader skips rows whose token counts differ and collects unique word pairs. A high PER here says that the English of this engine diverges from espeak on conversational and literary text. It is agreement, not accuracy. The `cmudict` and `wikipron` rows are far more informative for English.

The dataset card declares no licence. The underlying BabyLM corpora keep their own licences, so use the set for evaluation only.

## Lexibank/CLDF wordlist gold (`northeuralex`, `wold`)

[Lexibank](https://github.com/lexibank) republishes comparative word lists and dictionaries in [CLDF](https://cldf.clld.org/) (Cross-Linguistic Data Format). Each dataset has one `cldf/forms.csv`, keyed by `Language_ID`, which `cldf/languages.csv` resolves to a Glottocode or ISO 639-3 code. The `Value` column holds the word as recorded, in its real orthography or script. The `Segments` column holds phonemic segments separated by spaces, with `+` at a morpheme boundary. The `Source` column cites the dictionary or grammar each row comes from. This is compiled, cited lexicographic data, not phonemizer output, so the tier is `lexicon-derived`, the class of `cmudict` and `portuguese_unified`.

These datasets serve specs that have a grapheme table and no other gold. A wired language must have a non-empty grapheme table, and a smoke check must show that the engine gives non-empty output for a large majority of its forms. A low PER here is evidence toward a higher tier in [quality_tiers.md](../specs/quality_tiers.md), not a copy of an existing row. Sample sizes, spec tiers and PER are on the [scoreboard](generated/scoreboard.md) under each dataset.

[NorthEuraLex](https://github.com/lexibank/northeuralex) (Dellert et al. 2020, *NorthEuraLex: a wide-coverage lexical database of Northern Eurasia*) is a comparative word list of more than a hundred languages. The wired tags and their NorthEuraLex IDs are `_NORTHEURALEX_LANGS` in `scripts/benchmark.py`, and `--list` prints them.

They cover Uralic languages, such as Livonian, the Sami languages, Mari, Mansi and the Samoyedic languages. They cover Caucasian languages (Adyghe, Avar, Lak, Dargwa, Lezgian, Tsez) and Tungusic languages. They cover Paleo-Siberian languages and isolates (Nivkh, Chukchi, Itelmen, Ket, the Yukaghir languages). Others include Latvian, Buryat, Aleut and Hokkaido Ainu.

Two tags need a code translation. NorthEuraLex identifies Avar as `ava`, not `av`, and Latvian as `lav`, not `lv`. Its `dar` row is North-Central Dargwa, the Akusha-based standard that the `dar` spec targets.

Some languages are excluded despite a code match. `yux` (Southern Yukaghir) has a grapheme table but gave no non-empty output in the smoke check. Its grapheme inventory and the Cyrillic orthography of NorthEuraLex for that variety do not match, and a gold row cannot fix that. The `bsk` (Burushaski) is excluded because its NorthEuraLex `Value` column is the scholarly transcription of Berger (1998), not a community orthography.

[WOLD](https://github.com/lexibank/wold) (Haspelmath & Tadmor 2009, *World Loanword Database*) is a word list for loanword typology. Its wired tags are `car` (Galibi Carib, WOLD `Kalina`), `arn` (Mapudungun), `gwd` (Gawwada), `irk` (Iraqw), `crs` (Seychelles Creole) and `rif` (Tarifiyt Berber), in `_WOLD_LANGS`. The WOLD `KildinSaami` list is excluded. It romanizes Kildin Sami differently from the Cyrillic forms of NorthEuraLex and gave almost no non-empty output, while the NorthEuraLex `sjd` row exercises the grapheme table of the spec.

Every WOLD language was checked against the registry. Most of the unwired ones already have gold elsewhere, such as English, Dutch, Japanese, Mandarin, Thai, Vietnamese, Indonesian, Hawaiian, White Hmong, Hausa, Lower Sorbian and Kildin Sami. Some have no spec: Kanuri, Zinacantan Tzotzil, Malagasy, Old High German, Selice Romani and Sakha. The rest resolve to stub specs with an empty grapheme table, which gives a gold row nothing to exercise. Those are Archi, Bezhta, Manange, Ket, Oroqen, Ceq Wong, Takia, Gurindji, Yaqui, Qeqchi, Otomi, Saramaccan, Imbabura Quechua, Hup and Wichi.

Other Lexibank datasets were inspected and rejected (see [Rejected candidates](#rejected-candidates)).

## kaikki.org Wiktextract gold (`kaikki`)

[kaikki.org](https://kaikki.org/dictionary/) republishes the [Wiktextract](https://github.com/tatuylonen/wiktextract) (Ylonen 2022) extraction of Wiktionary as one JSON-lines file per language. Each entry carries a `word` (the headword as written), a `pos`, and a `sounds` list of `{"ipa": "..."}` objects, often with several variants. It draws on the same community edits as `wikipron` through another pipeline, so it is not an independent transcriber, and its tier is `crowd-scraped`.

The set exists for specs that have a grapheme table and no other gold. Each candidate was looked up in the language index of kaikki.org, with its size checked by a `HEAD` request before any download, and nothing is vendored. The loader keeps entries with a non-empty `sounds[].ipa` and drops `pos: "character"` entries (`_KAIKKI_EXCLUDED_POS`), which gloss a letter or digraph and are not words (Xhosa `hl` gives /ɬ/). Each wired language was sampled by hand and smoke-checked for non-empty output on at least 70% of entries. For `jv`, `so` and `om`, `_KAIKKI_WORD_FILTER` keeps only Latin-script words.

| Tag | Language | Notes from the hand sample |
|---|---|---|
| `jv` | Javanese | Most of the dump is in Javanese script, and the spec encodes only the Latin romanization. The Latin filter restores full coverage on the Latin entries. |
| `su` | Sundanese | Clean, near-total coverage. The sampled pairs agree with the seven-vowel description of the spec. |
| `lo` | Lao | The IPA is `Module:lo-pron` output (see [Module-generated WikiPron rows](#module-generated-wikipron-rows)). The engine writes no tone. |
| `xh` | Xhosa | The transcriptions are narrow, with vowel length, tone, prenasalization and breathy voice on almost every syllable (`impala` gives `/íᵐpaːlá/`). The segmental spec encodes none of these. |
| `so` | Somali | A few foreign entries are filtered out. The transcriptions are narrow, with tone, vowel length and pharyngeal detail on almost every word (`caws` gives `/ˈʡ͜ʢǽ͜ʉ̀s/`), which the segmental spec does not encode. |
| `om` | Oromo | The segmental notation is the standard descriptive one, and the spec matches it. Short `a e i o u` are lax `ɐ ɛ ɪ ɔ ʊ` against long `ɑː eː iː oː uː`. The glottalised stops `ph x c q` are `pʼ tʼ tʃʼ kʼ`, and `dh` is the retroflex implosive `ᶑ`. Most of the residual is the high-tone acute that kaikki writes on almost every entry and Qubee does not write. |
| `ne` | Nepali | Devanagari, matching the spec with no filter. The residual is the schwa that the spec adds after a final consonant the gold treats as silent (`कदर` gives `/kʌd̪ʌr/`), and schwa against `ʌ`. |
| `kok` | Konkani | Devanagari, with the same final-schwa gap as `ne` (`उठप` gives `/uʈʰəp/`). The gold also marks nasalization with a tilde that the spec does not write (`अदांव` gives `/ədɑ̃ːʋ/`). See [the Konkani residual](#what-the-konkani-kok-residual-is-made-of). |

Several of these rows score high, and the hand samples show that the gold is not the cause. When the spec misses a vowel sign, the gold row is the regression fixture that the repair needs. Where the gold is narrow or tonal and the spec is segmental, the row stays high until the spec gains tone, length and prenasalization rules. The final-schwa gap of `ne` and `kok` points at one shared fix for the Indo-Aryan specs, not two separate bugs.

A kaikki row alone does not promote a spec. For the `research` tier, [quality_tiers.md](../specs/quality_tiers.md) also asks for a cited source and a `stress` block or a documented stress exemption, and that is spec-authoring work. Javanese and Sundanese, for example, have predictable penultimate stress that their specs do not encode. The test `tests/test_data_quality.py` checks for a qualifying benchmark only on `production` specs, so the gold requirement of `research` is not enforced by a test.

Some candidates were investigated and rejected:

| Language | Reason |
|---|---|
| Sindhi (`sd`) | Every entry with IPA is in Perso-Arabic or Devanagari script, and the `sd` spec is Latin only. A Latin filter leaves nothing. |
| Santali (`sat`) | Every entry is in Ol Chiki script, and the `sat` spec is a Latin romanization. A Latin filter leaves nothing. |
| Tigrinya (`ti`) | Very few entries carry `sounds[].ipa`, too few for a gold set. |
| Fula, Lingala, Shona, Wolof, Twi, Southern Sotho | After the script filter each left only a handful of entries. Several were dictionary metadata, single-letter entries whose `pos` is not literally `"character"`. They need a tighter word-shape filter first. Twi was checked through the `Akan` dump and Southern Sotho through the `Sotho` dump. |

kaikki.org has no dump (`HEAD` gives 404, under the common name and obvious alternatives) for Bhojpuri, Awadhi, Igbo, Chhattisgarhi, Northern Sotho, Kirundi, Minangkabau, Kongo, Tsonga, Maithili, Venda and Southern Quechua. They are listed so that nobody repeats the lookup. The set of specs with no gold shrinks as gold lands, so recompute it from `results.json` before a new sweep.

### What the Konkani (`kok`) residual is made of

The Konkani gold is hand-typed, not module output. Entries carry variants tagged by dialect that no generator would produce. `मामा` has a Goud Saraswat reading `[mɑːmɑː]` beside a Roman Catholic `[mɑːm]`. The row is therefore an accuracy test, not a reproduction test, and the [module caveats](#module-generated-wikipron-rows) do not apply.

The spec does not encode two conventions of the gold, on purpose, because encoding them would fit the gold and not describe Konkani. The gold writes the low vowel of `⟨ा⟩` as `ɑ` almost every time. The choice is uniform, but it is notation, because the published Konkani inventories write the phoneme `/a/`. The spec keeps `aː`, and a sizeable part of the residual is this one symbol.

The gold reads `⟨फ⟩` as `[f]` in some words and `[pʰ]` in others. The split is lexical. `[f]` sits in the Portuguese layer (`फोटो`, `फिलिप`) and `[pʰ]` in the inherited one (`फिरप`, `फुटप`), and the orthography does not distinguish them. Both readings stay in the lattice with `pʰ` first. Putting `f` first would gain a little PER on this lexicon and assert nothing about the language.

The affricates are the largest contrast that the spelling cannot recover. Konkani has phonemic `/ts dz/` beside `/tʃ dʒ/`, and Devanagari writes both with `⟨च⟩` and `⟨ज⟩`. Almeida conditions the contrast: the affricate spirantizes except word-initially, in gemination and after a nasal. That conditioning does not hold in this gold. The fricative `[z]` occurs word-initially as well as elsewhere, and affricates outnumber it in both positions. The spec therefore encodes the contrast as a second candidate per grapheme, not as a rule.

An oracle over the five contrasts that the orthography does not decide (`e`/`ɛ`, `o`/`ɔ`, `tʃ`/`ts`, `dʒ`/`dz`, `pʰ`/`f`) picks, per word, the choice closest to the gold. That floor is close to the `Oracle@5` of the board, which measures the same quantity through the beam of the engine. Only a small share of the residual edit operations involve a schwa.

## Russian gold (`alphacep_ru_book`, `coruss_ru`)

`alphacep_ru_book` reads the `dev` split of [alphacep/biggest-ru-book-cleanup](https://huggingface.co/datasets/alphacep/biggest-ru-book-cleanup), a cleaned phone-level annotation of the Russian audiobook data `its5Q/biggest-ru-book`. Each row is `wav|sentence|phones`, with one segment group per word, and the loader splits rows into word pairs as `load_vox_communis` does. An automatic accentuator and G2P made the phone tier, so the tier is `machine-generated`, which gates. The annotation is morphophonemic. It keeps the full quality of unstressed vowels (`молчал` is written with an unreduced [o]), and it writes the genitive ⟨г⟩ as [g], not the spoken [v].

This engine writes surface phonetics, so the row disagrees on exactly those two features. That is a mismatch between two legitimate conventions, and it must not be fixed by adding exceptions to the spec.

`coruss_ru` reads the CoRuSS phonetic dictionaries (Kachkovskaia et al. 2016, LREC) of the phonetics lab of Saint Petersburg State University. They are `word [transcription] count` rows over read speech, monologue and dialogue, transcribed by experts from audio with no engine involved. The lab's ASCII notation ([russpeech.spbu.ru/transkrip.htm](https://russpeech.spbu.ru/transkrip.htm)) is mapped to IPA by the loader.

The transcription is surface-phonetic and colloquial. It records what a speaker said in unscripted speech, syllable deletions included (⟨Александровна⟩ [lʲiksanə], ⟨Волгоград⟩ [vodɡrat]). A G2P cannot reach a low PER here and is not meant to. Read the number as the distance to spontaneous surface forms, and compare it only with other runs on this dataset. The loader keeps every attested realization of a word form, so the row has several references per word.

## Rejected candidates

These datasets were investigated and excluded, because a tool generated the IPA, the provenance is unclear, or the data cannot be scored:

| Dataset | Verdict | Evidence |
|---|---|---|
| [lexibank/ids](https://github.com/lexibank/ids) (Intercontinental Dictionary Series) | Excluded: no IPA column | `Segments` is empty on every row of `cldf/forms.csv`. A scan of the whole file confirmed it. |
| [lexibank/abvd](https://github.com/lexibank/abvd) (Austronesian Basic Vocabulary Database) | Excluded: no IPA column | `Segments` is empty on every row, as in `ids`. |
| [lexibank/uralex](https://github.com/lexibank/uralex) (Uralic) | Excluded: no IPA column | `Segments` is empty on every sampled row. The repository also carries reconstructed forms such as `*tuli̮`. |
| [lexibank/tuled](https://github.com/lexibank/tuled) (Tupían) | Excluded: transcription, not orthography | `Value` already holds IPA symbols, and joined it reproduces `Segments` (`naʔot` and `n a ʔ o t`). |
| [lexibank/dravlex](https://github.com/lexibank/dravlex) (Dravidian) | Excluded: transcription, not orthography | `Value` is a Latin phonemic romanization with ASCII `:` for length (Kannada `na:nu`). It is not the native script or an attested romanization. |
| [lexibank/chaconarawakan](https://github.com/lexibank/chaconarawakan) (Arawakan) | Excluded: transcription, not orthography | `Value` carries tone marks and slash alternants (`nhóa` gives `ɲ ó/o a`). That is fieldwork transcription for mostly unwritten languages. |
| [lexibank/felekesemitic](https://github.com/lexibank/felekesemitic) (Semitic) | Excluded: transcription, not orthography | Amharic `Value` (`dǝmmǝrǝ1`) is a Latin transcription with a sense index, not Ge'ez script. |
| [lexibank/hantganbangime](https://github.com/lexibank/hantganbangime) (Dogon, Bangime) | Excluded: transcription, not orthography | `Value` is IPA with tone diacritics (`ɡwìì`, `pɛ́`), for languages with no standard orthography in this source. |
| [lexibank/lundgrenomagoa](https://github.com/lexibank/lundgrenomagoa) (Omagua, Kokama) | Excluded: transcription, not orthography | `Value` uses raw IPA (`β`, `ɨ`, `ɲ`, `ã`), as in Tupinambá `aβá`. |
| [lexibank/naganorgyalrongic](https://github.com/lexibank/naganorgyalrongic) (Gyalrongic) | Excluded: transcription, not orthography | `Value` carries IPA tone letters and uvular symbols (`ˊtə rno[ʢ]k`). These varieties have no established orthography. |
| [lexibank/robinsonap](https://github.com/lexibank/robinsonap) (Alor-Pantar) | Inspected, not wired: no spec coverage | `Value` looks like a practical orthography (`gunnang` gives `g u n n a ŋ`). Its languages (`twe abz beu woi kvw jka lev kvd adn swt nec kyo`) all resolve to stub specs with an empty grapheme table. Revisit when one of these specs gets a grapheme table. |
| [lexibank/sagartst](https://github.com/lexibank/sagartst) (Sino-Tibetan) | Excluded: transcription, not orthography | `Value` is raw IPA with tone numbers or tone letters (`zji¹`) in every sampled language, including reconstructed forms. |
| [lexibank/savelyevturkic](https://github.com/lexibank/savelyevturkic) (Turkic) | Excluded: transcription, not orthography | `Value` uses a Turkological transliteration (`dïrnaġ`), not the standard orthography (Azeri `dırnaq`). |
| [lexibank/abrahammonpa](https://github.com/lexibank/abrahammonpa) (Monpa) | Excluded: transcription, not orthography | `Value` is raw IPA (`dʒaŋ`). These varieties have no standard orthography in this source. |
| [lexibank/allenbai](https://github.com/lexibank/allenbai) (Bai) | Excluded: transcription, not orthography | `Value` embeds tone numbers in superscript (`xẽ⁵⁵`, `kʰao³¹`). |
| [lexibank/bantubvd](https://github.com/lexibank/bantubvd) (Bantu) | Excluded: transcription, not orthography | `Value` is raw IPA with tone diacritics and slash alternants. `Language_ID` is also a bare number. |
| [lexibank/chindialectsurvey](https://github.com/lexibank/chindialectsurvey) (Kuki-Chin) | Excluded: transcription, not orthography | `Value` is raw IPA (`tʃe`, `kɑi`) in every dialect sampled. |
| [lexibank/birchallchapacuran](https://github.com/lexibank/birchallchapacuran) (Chapacuran) | Excluded: transcription, not orthography | `Value` is IPA with diacritics that no practical orthography of these languages uses (`waʒ̟a`). |
| [lexibank/gravinachadic](https://github.com/lexibank/gravinachadic) (Chadic) | Excluded: transcription, not orthography | Some rows look orthographic (`malay`), others are raw IPA (`sˈa`). It reads as one normalized fieldwork transcription. |
| [lexibank/kraftchadic](https://github.com/lexibank/kraftchadic) (Chadic, with Hausa) | Excluded: transcription, not orthography | Even Hausa has tone and length marks that Boko does not use (`yā wankḕ`). It is a transcription on Hausa letters. |
| [lexibank/luangthongkumkaren](https://github.com/lexibank/luangthongkumkaren) (Karenic) | Excluded: reconstructed forms | `Value` entries are starred reconstructions with tone letters (`*loɁᴰ`), not attested words. |
| [lexibank/marrisonnaga](https://github.com/lexibank/marrisonnaga) (Naga, Kuki-Chin, with Jingpho, Lushai, Manipuri) | Excluded: transcription, not orthography | Every row carries the `◦` syllable mark of the comparative list of Marrison, and Manipuri is romanized, not in its own script. This holds for `kac`, `lus` and `mni` too. |
| [lexibank/mitterhoferbena](https://github.com/lexibank/mitterhoferbena) (Bena) | Excluded: transcription, not orthography | `Value` embeds the IPA length mark (`liːho`). |
| [dsvv-cair/ipa-transcription-datase](https://huggingface.co/datasets/dsvv-cair/ipa-transcription-datase) (English, CC BY-NC 4.0) | Rejected: written by a language model | The card says the authors built the set "using the GPT-4o Mini API". A language model has no error model, so a disagreement says nothing. The licence is not the reason. |
| ipa-dict tool-generated files | Wired with their tiers | Each has the tier of its own provenance, never `lexicon-derived`. See [ipa-dict](#ipa-dict-pronunciation-dictionaries-ipadict). |
| ipa-dict `fr_QC.txt` | Excluded: no spec | No Québécois spec is registered, and the file is qc-ipa output over `fr_FR`. |
| ipa-dict `tts.txt` | Excluded: no spec | Isan has no `tts` spec, and the `th` spec is another language. |
| ipa-dict `zh_hans`, `zh_hant`, `yue` | Excluded: cannot be transcribed | Well-sourced Han-script golds. Han script needs a dictionary, and the `zh` spec reads pinyin. A gap in the engine, not in the gold. |
| `vox_communis` `zh-cn.tsv` | Deregistered: cannot be transcribed | The `aligned_sentence` column is Han characters, and the `zh` spec reads pinyin. Every row was empty, so the row measured a missing front-end from hanzi to pinyin. It returns when such a front-end exists. |
| `vox_communis` `yue.tsv` | Not wired: cannot be transcribed | Han script, and the `yue` spec is a stub. |
| kaikki.org Occitan | Not wired: same source as the existing row | The `oc` row already reads WikiPron, and kaikki reads the same Wiktionary. A second row would measure one body of transcription twice. VoxCommunis has no Occitan file. |
| kaikki.org Tetum | Rejected: too thin | Almost no entries carry IPA, and WikiPron has no Tetum. `tet` is scored on the primary-source rows of its own grammar. |
| Lexique 3.82 (French) | Excluded: notation | Human-curated by Boris New and Christophe Pallier (CNRS), and CC BY-SA 4.0. Its custom notation (`§` for ɔ̃, `5` for ɛ̃, `8` for œ̃, `°` for a schwa variant) is neither X-SAMPA nor IPA, and `scriptconv.notation.xsampa_to_ipa` does not convert it. A dedicated converter would be a clean follow-up. WikiPron `fra` is the French gold meanwhile. |
| NST lexicons for Swedish, Norwegian and Danish (Språkbanken) | Excluded: no programmatic download | Authoritative human SAMPA lexicons for Swedish, Norwegian Bokmål and Danish from Nasjonalbiblioteket. The portal serves catalogue pages and no stable raw URL. The WikiPron Scandinavian files are used instead. |
| CELEX2 (German, Dutch, English) | Excluded: proprietary | LDC licence (LDC96L14). |
| GlobalPhone | Excluded: ELRA licence | Licensed per language, not freely downloadable. |

The `ja` `vox_communis` file stays registered. Its kana rows transcribe, and only the kanji minority give empty output, so the row still carries signal.

## Known finding: the nukta digraphs and the inherent vowel

This is an engine issue, not a dataset issue. It is recorded here because these golds measure it, and it needs its own change.

The tokenizer decides from the last character of a grapheme key whether the key is a bare combining mark. That decides whether the key takes the inherent vowel of an abugida. That is right for a key that is a mark, such as anusvara `ং`, and wrong for a key that only ends in one. Two key shapes end in a mark. A conjunct stack is a letter plus subjoined letters, which Unicode encodes as combining marks (Tibetan `ཀྲ` is `ཀ` plus U+0FB2). A subjoined letter is a letter, so the key takes the inherent vowel, and the engine handles this case. `dz` depends on it.

A nukta digraph is a letter plus a modifier sign (`क़` is `क` plus U+093C DEVANAGARI SIGN NUKTA), in `hi bn as gu awa bho mr ne or pa kok mai km`. These keys get no inherent vowel, so `क़लम` gives `qləm`, where the schwa-deletion rules should have received a schwa to decide about (`qələm`).

The nukta case looks like the same bug but needs another fix. Giving those keys the inherent vowel moves rows in both directions. On a differential in one session against one cache, the net over the rows is negative: `hi` `wikipron` gains, while `bn` `vox_communis` and `as` lose more. Whether the added vowel is right depends on the schwa-deletion coverage of each Brahmic spec, which is a data question per spec, not a tokenizer question. The change needs per-spec schwa rules in the same change as the engine fix. Run any such differential as [board regeneration](../contributing/board.md#before-you-regenerate) describes, with both sides in one session against one cache.

---
[← Benchmarks](benchmarks.md) · [Home](../index.md) · [The pinned WikiPron mirror →](wikipron_mirror.md)
