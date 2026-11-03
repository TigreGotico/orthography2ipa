# Gold defects

A [provenance tier](benchmarks.md#reliability-tiers) says where a gold transcription came from, not whether it is right about the language. This page is the registry of measured defects in individual gold rows. In each case the gold merges a contrast, marks something impossible, describes another lect, mixes conventions, or comes from the system it scores.

The figures were measured against the cached gold in `.benchmark_cache/`, with the loaders that the scoreboard uses, so each one can be reproduced. They count words and symbols in the gold files, which the harness pins.

These findings decide what a reader may conclude from a score. A high PER on a row whose gold merges two tones says nothing about the spec. A spec change toward such a gold is gold-fitting, and the harness rules forbid it.

## Defect classes

The class of a defect decides what can be done about it, so the registry is ordered by class, not by language.

| Class | What the gold does | What can be done |
|---|---|---|
| Merged contrast | writes one symbol for two things that the language keeps apart | The orthography still carries the contrast, so the owner of the gold can undo the merge. |
| Missing data | never encodes the contrast, so no symbol for it occurs in the file | Nothing recovers it. Exclude the row, or read it as a partial score over the subset it covers. |
| Structurally impossible marking | puts a mark where the language cannot have one | It is a bug in the tool that made the gold, and only that tool can fix it. |
| Wrong variety | is consistent, but describes another lect than its tag | Relabel it, or replace it with a gold for the named variety. |
| Mixed conventions | merges incompatible transcription traditions in one file | Whether the traditions separate cleanly has to be tested, not assumed. |
| Circular | comes from the system it scores, or from the authorship that wrote the specs | The score measures self-agreement. Only an independent gold helps. |
| False provenance label | carries a tier that names a tool that cannot have made it | The number may be usable, but the reason a reader was given to trust or distrust it is wrong. |

## A note on gating

`row_gates()` in `scripts/benchmark.py` decides whether a row may qualify or block a language for the `production` quality tier ([quality tiers](../specs/quality_tiers.md)). [Confidence intervals](benchmarks.md#confidence-intervals) gives its three conditions, and [reliability tiers](benchmarks.md#reliability-tiers) says which tiers gate.

The gating does not run the way a reader expects. `machine-generated` gold gates, and `epitran-derived` gold does not, because the objection to the competitor tiers is circularity, not quality. The entries with the most effect are therefore not the worst-transcribed ones. They are the `crowd-scraped` and `machine-generated` rows, which can block a promotion while they carry a defect that has nothing to do with the spec.

## The registry

| Dataset | Language | Class | Evidence | Effect |
|---|---|---|---|---|
| `vox_communis` | Vietnamese (`vi`) | Merged contrast | [ngang and huyền share ˨˨](#vietnamese-vox_communis), and the tone letter sits inside the rime | `epitran-derived`, cannot gate. `vox_communis_corrected` repairs the huyền side. |
| `vox_communis` | Abkhaz (`ab`) | Missing data | [no labialization symbol](#abkhaz-vox_communis), and eight letters always `spn` | `epitran-derived`, cannot gate. Only exclusion helps. |
| `ipa_childes` | Danish (`da`) | Structurally impossible marking | [stød on a short vowel before a voiceless stop](#danish-ipa_childes), and double stød in one stress group | `espeak-derived`, cannot gate. The fix is upstream. |
| `portuguese_unified` | East Timorese Portuguese (`pt-TL`) | Wrong variety | [the `pt-TL-x-dili` region is Lisbon Portuguese with other symbols](#east-timorese-portuguese-portuguese_unified) | `machine-generated`, gates. Needs a gold from Timorese speakers. |
| `wikipron` | Persian (`fa`) | Wrong variety | [Classical Persian markers dominate](#persian-wikipron) | `crowd-scraped`, gates. Relabel or replace. |
| `primary_sources` | Algerian Arabic (`ar-DZ`) | Wrong variety | [one Tlemcen word scored against an Algiers spec](#algerian-arabic-primary_sources) | Below `THIN_ROW_N`, so it does not gate. |
| `wikipron` | Middle English (`enm`) | Mixed conventions | [vowel length differs between readings of one headword](#middle-english-wikipron) | `crowd-scraped`, gates. The spec records the length fold as a ceiling. |
| `wikipron` | Coptic (`cop`) | Mixed conventions | [competing reconstructions mixed inside single readings](#coptic-wikipron) | `crowd-scraped`, gates. Only per-row tagging helps. |
| `wikipron` | Limburgish (`li`) | Mixed conventions | [Veldeke, Rheinische Dokumenta and Eupen spellings in one file](#limburgish-wikipron) | `crowd-scraped`, gates. `li-x-rheindok` models one convention. |
| `wikipron` | Scottish Gaelic (`gd`) | Mixed conventions | [two notations for ⟨b d g⟩ and mixed dialects](#scottish-gaelic-wikipron) | `crowd-scraped`, gates. Fix in the normalizer or upstream. |
| `wikipron` | Middle High German (`gmh`) | Mixed conventions | [Wiktionary page titles, not Lachmann spelling](#middle-high-german-wikipron) | `crowd-scraped`, gates. Score against `gmh-x-wikt`. |
| `wikipron` | Kapampangan (`pam`) | Mixed conventions | [⟨e⟩ where the spec writes ⟨ɛ⟩, and readings that conflict](#kapampangan-wikipron) | `crowd-scraped`, gates. Left as it is. |
| `arabic_tts`, `portuguese_tts`, `spain_romance_tts` | Arabic, Portuguese, the languages of Spain | Circular | [the model lineage that wrote the specs also wrote the label, and saw the engine output](#the-tts-silver-sets-arabic_tts-portuguese_tts-spain_romance_tts) | `llm-corrected`, cannot gate |
| `vox_communis` | Abkhaz (`ab`) | False provenance label | [epitran has no Abkhaz map](#abkhaz-vox_communis-1) | No effect on gating. The label is wrong. |

The sections below give the evidence that does not fit in a table cell.

## Merged contrast

### Vietnamese, `vox_communis`

The row loads 2,475 word types, and 2,468 of them carry at least one tone letter. The gold writes ⟨˨˨⟩ for two contrastive tones. Vietnamese writes tone without ambiguity, so the tone of each headword can be read off its diacritic. Ngang, with no diacritic, takes ⟨˨˨⟩ in 584 of its 590 types. Huyền, with a grave accent, takes it in all 406 of its 406 types. No other tone class uses the symbol, apart from one stray hỏi type.

That puts ⟨˨˨⟩ in 991 types, and in 967 of them it is the only tone. That is 39.1% of the row. Ngang is a level tone and huyền is a low falling tone, often breathy. They form a minimal contrast, and the gold gives them one Chao letter. About two fifths of the row therefore cannot tell a correct tone from a wrong one.

The row also places tone in the wrong spot. In 1,957 of the 2,468 toned types (79.3%) the tone letter sits inside the rime, with segments after it. An example is `t oː˨˨ j` for *tôi*. Tone belongs to the whole syllable and is written after it by convention. A spec that writes tone at the end of the syllable mismatches those 1,957 types on position alone, even when the tone is right.

The tier is `epitran-derived`, so the row cannot gate. The merge lives in the VoxCommunis lexicons. The shipped gold is never rewritten here. The `vox_communis_corrected` overlay repairs the huyền side from the grave accent alone, as [its section in the dataset catalogue](datasets.md#voxcommunis-with-the-vietnamese-tone-merge-repaired-vox_communis_corrected) describes.

## Missing data

### Abkhaz, `vox_communis`

Abkhaz has a very large consonant inventory and only two vowels, and it palatalizes and labializes almost every place of articulation (Beguš 2021, [doi:10.1093/oxfordhb/9780190690694.013.18](https://doi.org/10.1093/oxfordhb/9780190690694.013.18), §2.2.1). The orthography writes labialization with the modifier letter ⟨ә⟩ (U+04D9). The gold cannot write labialization at all. The file holds 76,459 raw word types. In 44,279 of them (57.9%) the phones are `spn`, the "spoken noise" marker of the forced aligner. The pipeline also writes `spn` for any word that its lexicon does not cover. The 32,180 types that remain use exactly 35 phone symbols, and none carries the labialization mark ⟨ʷ⟩.

The inventory is `a b d f j kʲʼ kʼ l m n pʼ qʲʼ qʼ r s t ts tsʼ tʃ tʃʲ tʃʲʼ tʼ v w z ħ ə ɡ ɡʲ ʃ ʃʲ ʒ ʒʲ χ χʲ`. Palatalization occurs throughout, and labialization never occurs.

The `spn` half is not random. Eight Abkhaz letters are `spn` in every type that contains them: ⟨ә⟩ (30,743 types), ⟨ԥ⟩ (7,984), ⟨қ⟩ (7,058), ⟨ӡ⟩ (5,024), ⟨ҩ⟩ (4,035), ⟨ҿ⟩ (2,678), ⟨ӷ⟩ (1,741) and ⟨џ⟩ (811). The lexicon of the gold does not cover them. The scoreable subset is therefore the part of the vocabulary that avoids those letters.

Nothing can be recovered. A missing symbol cannot be inferred from a file that never contains it. The row can only be excluded, or read as a score over a biased subset. The tier is `epitran-derived`, so it cannot gate in any case. The part of the distance that is convention, not mapping, is in the [dataset catalogue](datasets.md#coverage-hole-in-abkhaz-ab).

## Structurally impossible marking

### Danish, `ipa_childes`

Danish stød is a laryngealization tied to a stressed syllable. Two rules of the language apply to the gold. A stress group carries at most one stød. Stød also needs a stødbasis, which is a long vowel or a sonorant coda. A short vowel before a voiceless stop cannot carry it.

The scored column (`ipa_g2p_plus`) writes stød as ⟨ˤ⟩, not ⟨ʔ⟩. Of 2,233 word types, 1,302 carry the mark, and 328 carry it twice or more. 224 put it on a short vowel directly before a voiceless stop: *op* `ɔˤp`, *ikke* `eˤkə`, *nok* `nɔˤk`, *lidt* `leˤt`. The types with more than one stød are ordinary words of two morphemes, not compounds with two stress groups: *hedder* `heˤðɔˤ`, *holder* `hɔˤlɔˤ`, *flere* `fleˤɔˤ`.

The two IPA columns of the file show the mechanism. The raw `ipa_espeak` column marks 1,297 types with ⟨ʔ⟩, and 110 of those marks are word-initial. A word-initial ⟨ʔ⟩ is not stød. It is the glottal onset that espeak-ng puts before a word that starts with a vowel. 106 of the 110 come back in the scored column with ⟨ˤ⟩ on the vowel: *op* `ʔʌp` to `ɔˤp`, *også* `ʔʌsə` to `ɔˤsə`, *ikke* `ʔekə` to `eˤkə`, *en* `ʔen` to `eˤn`.

espeak-ng uses one symbol for two unrelated things, and the G2P+ conversion reads every one of them as stød. That one confusion produces the cases without stødbasis and inflates the count of double stød. The scored data holds no ⟨ʔ⟩ at all. The fault shows as ⟨ˤ⟩ in the scored column and as ⟨ʔ⟩ in the espeak column.

The fix belongs to espeak-ng and G2P+, not to this project. The tier is `espeak-derived`, so the row cannot gate. It is also no evidence about stød placement in either direction.

## Wrong variety

### East Timorese Portuguese, `portuguese_unified`

The `pt-TL` row reads the `pt-TL-x-dili` region of the unified lexicon. That region is not independent Timorese lexicography. A word-by-word diff against `pt-PT-x-lisboa` finds 53,147 shared words, and 3,076 of them are byte-identical in the two regions.

The diff then keeps the 35,800 shared entries whose transcriptions have the same length, where a positional diff means something. Six substitutions account for 90.6% of the 63,189 character differences:

| Substitution | Count |
|---|---:|
| ɐ to ə | 30,042 |
| u to ʊ | 12,075 |
| u to o | 7,345 |
| ʀ to r | 4,186 |
| ɐ to a | 1,858 |
| ɫ to w | 1,724 |

Further down come d to ð (223) and ɡ to ɣ (150). These counts are over the first-variant pairs of equal length.

Another symbol for the reduced unstressed vowel of European Portuguese does not remove the vowel. 60% of `pt-TL-x-dili` entries still have a reduced [ə], and 31% still end in a reduced [ʊ]. Coda /s/ still surfaces as the Lisbon hush: gold *instrumentista* is `ĩʃtɾumẽntˈiʃtə`, and Lisbon has `ĩʃtɾumẽtˈiʃtɐ`. Albuquerque (2010:275 fn. 7, 277), the source of the `pt-TL` spec, documents the opposite for this variety. It has no reduction of unstressed vowels and an alveolar coda /s/ with no hush. The row therefore measures agreement with European Portuguese in other symbols, not with the East Timorese acrolect that the spec models.

This entry matters most, because the row gates. `_PT_UNIFIED_PROVENANCE` already lowers `pt-TL` from the dataset tier `lexicon-derived` to `machine-generated`, so a low PER here cannot mean that the spec is right. The tier order still lets the row block a promotion, and such a block is not phonological. No transcription work fixes the defect. It needs a gold collected from Timorese speakers.

### Persian, `wikipron`

The WikiPron `fa` set is mostly Classical or Early New Persian, not the modern Iranian Persian that the `fa` tag names. Over the 62,914 gold segments of the file, the classical reading wins on every diagnostic:

| Classical | Count | Modern | Count |
|---|---:|---|---:|
| ⟨aː⟩ | 5,654 | ⟨ɒː⟩ | 142 |
| ⟨r⟩ | 4,078 | ⟨ɾ⟩ | 154 |
| ⟨w⟩ | 1,130 | ⟨v⟩ | 24 |
| ⟨q⟩ | 880 | ⟨ɣ⟩ | 332 |
| /i u/ | 2,796 and 2,075 | short /e o/ | 139 and 106 |

The majhūl vowels, which Iranian Persian merged into /iː uː/ centuries ago, are still frequent: ⟨eː⟩ 513 and ⟨oː⟩ 523. So is labialized ⟨xʷ⟩ for ⟨خو⟩, with 124. The modern markers ⟨t̪ʰ kʲ⟩ are rare too. Overall the classical markers outnumber the modern ones by about an order of magnitude, and few rows carry a modern marker.

A better description of Persian cannot improve this row. The only way to lower its PER is to transcribe Classical Persian under the tag `fa`, which would be false. The gold is fine and its tag is wrong. The fix is a correct label, or a gold from a modern Iranian source. The tier is `crowd-scraped`, so the row gates, and the wrong label has consequences.

### Algerian Arabic, `primary_sources`

The `ar-DZ` row on `primary_sources` has one gold pair: id `guerrero2019-010`, زَوْجَتُه "his wife". It is filed against Guerrero (2019), who quotes the 1908 description of Tlemcen Arabic by W. Marçais. *Le dialecte arabe parlé à Tlemcen* (1902) is the earlier monograph of the same author on the same city. The row is far below `THIN_ROW_N`, so `per_ci_low` and `per_ci_high` in `benchmarks/results.json` are null, and the scoreboard shows `n too small`. The `PROVENANCE` comment in `scripts/benchmark.py` warns that `primary_sources` rows "diagnose rules rather than certify a language on their own."

The `ar-DZ` spec models old urban Algiers, after Boucherit (2002). It cites the Tlemcen material of Marçais only for the isogloss of the interdental stops. Guerrero's example is Algerian, but it is western Tlemcen speech. It also carries a construct-state contraction that the spec was never built to produce. In Marçais the word surfaces as *zūžtăh* ['zuːʃtah]. The short /a/ of the possessive syncopates, /aw/ contracts to /uː/, and /ʒ/ devoices to [ʃ] before /t/. The spec reads the vocalized input as it is written, `ˈzawʒatuh`, with no syncope, contraction or devoicing.

None of the three changes is an oversight. `DZ_SHORT_REDUCE`, the one syncope rule of the spec, documents that short /a/ syncope is left out on purpose. A rule for /a/ needs an engine class that can exclude gutturals and pharyngeals, and a blanket /a/ to ə rule over-generates. The /aw/ contraction and the devoicing across a morpheme boundary have no other attestation in the spec's sources. A rule written to match one word would be gold-fitting on one row, not a sourced correction.

Read the row as too small to diagnose anything beyond the one documented gap. It is no evidence that the spec handles Algerian Arabic badly. The tier is `expert-human`, but the row has one word, below `THIN_ROW_N`, so `row_gates()` keeps it out of every gating decision.

## Mixed conventions

### Middle English, `wikipron`

The `enm` gold (`enm_latn_broad.tsv`) has 18,272 readings over 6,466 headwords. It is the crowd-scraped Wiktionary reconstruction of late Middle English as Chaucer spoke it. Its vowel-length notation changes inside one headword.

The count runs on the scored form of each reading: `benchmark.normalize(broad=True, strip_stress=True)`, then one copy per headword. 1,403 of the 6,466 headwords (21.7%) keep two or more readings that differ only by the length mark ⟨ː⟩ on a vowel. The editors disagree with each other about whether a vowel is long. The same count over the raw TSV strings gives 1,291 (20.0%). The two differ because the narrow-mark and NFC folds merge a few raw readings before the comparison. The figure 1,403 matches what enters the PER computation, because scoring always normalizes first.

The mismatches this causes show length on plain vowel letters in closed syllables: `Irish` gold /iːriʃ/, `Simon` gold /simɔːn/, `amen` gold /aːmɛn/. The spelling gives no signal there that the macron graphemes ⟨ā ē ī ō ū⟩ of the spec could use. The length follows the Wiktionary reconstruction of open-syllable lengthening, not the spelling.

The spec maps ⟨y⟩ by position: a glide /j/ before a vowel (`yong`, `yarn`, `York`), and /i/ elsewhere. Elsewhere ⟨y⟩ is a graphic variant of ⟨i⟩ next to minim strokes, so `ydel` matches `idle` (Mossé 1952, Jordan 1974). ⟨x⟩ maps to /ks/, which the gold confirms in all 191 occurrences (`Oxenford`). ⟨ð⟩ maps as a variant of thorn.

With the length mark folded out of both hypothesis and gold, the row falls below the 0.25 production threshold. The row is limited by the gold's own disagreement about vowel length, not by a spec defect. `valid_ceiling.wikipron` in `enm.json` records the measured fold. Folding the acute, grave and caron accents with the length mark changes nothing, because the gold does not carry them. That negative result is in the same citation.

Final ⟨-e⟩ is unstable too. Of the 2,350 headwords with a final ⟨e⟩, 12 realise it as [ə] in every reading and 416 drop it in every reading. The other 1,922 (81.8%) mix pronounced and silent readings for one headword. A naive fold, which strips a final [ə] from both sides when the headword ends in ⟨e⟩, makes PER worse. It turns correct [ə] outputs of the spec into mismatches against readings that keep theirs. No defensible fold was found, so no ceiling is recorded for final ⟨-e⟩.

Headword spelling is not standardized either. A near-duplicate scan over adjacent sorted headwords (Ratcliff/Obershelp similarity above 0.86, length difference at most 2) finds 669 pairs that are probably one lexeme. They are scribal and dialect variants, such as Northern and Midland forms. The harness scores several references per word, but it cannot merge distinct headwords. That is a property of an unstandardized medieval written language, not a defect and not a spec bug.

`enm` is the parent of `en-GB` in the ancestry, but `en-GB` has no `*_base` keys, so no data crosses from `enm` into any descendant. `en-US` inherits from `en-GB`, not `enm`, through four keys: `graphemes_base`, `allophones_base`, `grammatical_endings_base` and `word_exceptions_base`. An edit to `enm` therefore reaches no other spec. An edit to `en-GB` reaches `en-US`.

The tier is `crowd-scraped`, so the row gates.

### Coptic, `wikipron`

The Coptic gold mixes reconstruction traditions. The file holds 881 rows over 591 spellings, and 155 spellings carry two or more readings. Symbols of competing reconstructions occur side by side: ⟨ʔ⟩ in 181 readings, ⟨β⟩ in 68, ⟨x⟩ in 30, ⟨v⟩ in 19 and ⟨θ⟩ in 8.

The obvious repair does not work. It splits the file into two systems, one plain with short vowels and one ejective with long vowels. Of the 881 readings, 536 are plain with no length mark and 38 are ejective with length. The other 307 mix a marker from each tradition. The traditions do not separate, so the only fix is per-row tagging by someone who knows Coptic philology. This negative result rules out the cheap fix.

The tier is `crowd-scraped`, so the row gates.

### Limburgish, `wikipron`

The `li` spec implements *Spelling 2003 voor de Limburgse dialecten*, the Veldeke spelling. It states that ad-hoc spellings based on Dutch or German are out of scope. The gold mixes headwords from the Veldeke spelling with alternative forms from Wiktionary. These come from the German-based spelling, from Rheinische Dokumenta and from the Eupen dialect.

The file holds 1,128 gold lines over 989 headwords. 123 headwords are homographs with two or more readings. The spelling underdetermines the pronunciation, partly through dialect variation, and partly because Spelling 2003 does not write the contrast of sleeptoon and stoottoon. 90 gold lines, over 55 words, carry an IPA tone letter that the spelling cannot supply.

Tone is not the main source of error here, unlike the Hausa and Kikuyu tone folds. Folding the tone letters out of both sides barely moves the PER of the row. The `li` spec notes record the figures, and `tests/test_li_gold_composition.py` checks them. The main driver is the mix of spelling conventions. Mistranscribing an out-of-contract spelling is the documented behaviour of the spec, not a defect in it.

The gold's own spelling measures the mix. Of the 140 headwords whose IPA has a postalveolar fricative, 130 write it `sch` and 7 write it `sj`, the Spelling 2003 form. `ae` occurs in 10 headwords and `ao` in 14, against 114 with `ä` and 34 with `ü`. The Veldeke convention that the row is scored against is a small minority of the file.

Two other conventions separate cleanly. 89 headwords carry a sign that belongs only to Rheinische Dokumenta (`e̩`, `ǫ`, `ṣ`, `c͜h`). 222 carry the acute and diaeresis signs of the Eupen spelling. No headword carries both. Rheinische Dokumenta is a published standard, the transcription system of the Landschaftsverband Rheinland for the dialects of the Rhineland (Honnen 1987). It therefore has its own spec, `li-x-rheindok`, because a distinct written convention for one language gets its own entry. `li-x-rheindok` scores those 89 headwords far better than `li` does, and 58 of them come out exactly right.

`li` still targets Spelling 2003. The Eupen block stays unmodelled. No published orthography for it was found, and a sign table inferred from the gold that then scores it would be fitting, not description. The board still scores the whole file against `li`. Splitting the gold by convention is upstream work at Wiktionary, or a local exclusion, not a spec change. The tier is `crowd-scraped`, so the row gates. The `li` spec carries the verdict as a machine-readable `mislabeled_gold` audit record.

### Scottish Gaelic, `wikipron`

The `gd` gold has 3,720 headwords over 6,000 lines. It mixes two things that the spec cannot follow at once.

The first is a notation split for the plain stops ⟨b d g⟩. The modern instrumental analysis finds "very little or no closure voicing even in word-medial stops which are orthographically b d g". It writes the series as an aspiration contrast, /pʰ/ against /p/ (Nance and Stuart-Smith 2013, summarized in Nance and Ó Maolalaigh 2020). The spec follows that analysis. 185 of the 3,720 headwords use the older devoicing convention of Borgstrøm (1940) and Oftedal (1956), /b̥ d̥ ɡ̊/, for the same sounds.

The second is dialect mixing. 986 of the 3,720 headwords carry two or more pronunciations that cannot both be right. They differ in the quality of the stressed vowel, or in whether preaspiration occurs. That fits the crowd-scraped origin of WikiPron, with many contributors, not one variety.

Two phenomena that the spelling underdetermines were folded out of both sides and scored again. Preaspiration is encoded (`GD_PREASP_*`), and svarabhakti, an unwritten epenthetic vowel, is not (see the `gd` spec notes). Neither fold lowers PER. The preaspiration fold leaves it flat, and the svarabhakti fold makes it worse. Neither phenomenon is the main source of error, unlike the tone folds of Hausa, Kikuyu and Limburgish. The mixed devoicing notation and the mixed dialects are the larger drivers, and they are harder to fold.

The fix is to normalize the two devoicing conventions in the IPA normalizer of the benchmark, which is a fold and not a spec change. The other fix is a single-dialect subset upstream at Wiktionary or WikiPron. The tier is `crowd-scraped`, so the row gates.

### Middle High German, `wikipron`

The `gmh` spec targets the normalized orthography of Karl Lachmann. It writes long vowels with a circumflex (â ê î ô û) and the umlaut reflexes as ⟨æ œ⟩ (Paul, *Mittelhochdeutsche Grammatik*, revised by Klein, Solms and Wegera, 2007). The gold has 1,724 source words, and 1,516 are scored after the tokenizer filter. It does not use that convention. None of the 1,724 words carries a circumflex vowel or ⟨ë⟩, while 115 carry ⟨æ⟩ or ⟨œ⟩ and 130 carry ⟨ä ö ü⟩.

That is a second, real spelling convention, not a defect. The English Wiktionary style page (*Wiktionary:About Middle High German*) explains it. It says that "certain letters with diacritics (ë ā ē ī ō ū ȥ) are not used in article titles, but are used when displaying the word". It adds that "this does not apply to the umlauted vowels ä, ö, ü, æ, œ". WikiPron scrapes the page title, not the displayed headword, so the policy predicts the counts above exactly.

A distinct written convention for one language gets its own spec, as `cdo-Latn-buc` beside `cdo` and `zh-Hani` beside `zh`. This one is `gmh-x-wikt`. It takes the phonology of `gmh` whole through `graphemes_base` and nulls only the circumflex length graphemes, which this convention never writes. `gmh` keeps Lachmann's convention, which is correct for edited text in scholarly normalization. Score the `wikipron` gold against `gmh-x-wikt`, not `gmh`.

The bare ⟨z⟩ is a narrower case that cannot be recovered, and it affects both specs. Middle High German ⟨z⟩ continues two outcomes of the High German consonant shift. One is the affricate [t͡s] ("herze", "heizen", "gezogen"). The other is a fricative [s] ("az", "biz", "daz"). Only the doubled spellings settle it: ⟨tz⟩ is the geminate affricate and ⟨zz⟩ the geminate fricative, and the spec maps both. Some editions mark the fricative with a special z (ȝ or ȥ), but this gold does not. The bare ⟨z⟩ split is therefore limited by the input, and the spec keeps the affricate default rather than fit it to this gold.

The tier is `crowd-scraped`, so the row gates. Schwa reduction, apical ⟨s⟩ and the ⟨tz⟩ and ⟨zz⟩ geminates are recoverable from the spelling of the gold, and the spec encodes them.

### Kapampangan, `wikipron`

The `pam` spec writes its mid front vowel as open-mid /ɛ/. It follows the phonology summary of the Wikipedia article on the language, which cites Forman 1971, *Kapampangan Grammar Notes*, pages 28 and 29, for stress. The gold never writes that symbol. None of its 926 headwords carries ⟨ɛ⟩, and 119 carry plain ⟨e⟩.

Both write the same vowel letter, and only the IPA symbol differs. This is a mismatch of notation, not an unwritten contrast. It is left as it is. Changing the spec to /e/ to match one gold's convention would be gold-fitting against an analysis sourced from Forman. Folding ⟨ɛ⟩ to ⟨e⟩ on both sides lowers the PER of the row. The fold does not count toward `valid_ceiling` in `pam.json`. That ceiling is for what the spelling cannot write: the glottal stop, and the unmarked lexical stress behind the /a/~[ə], /i/~[ɪ] and /u/~[ʊ] alternation.

The file also carries plain crowd-scraped noise. 48 headwords recur with two or more readings that conflict for one spelling ("Guagua" `ɡwaɡwə` and `wawəʔ`, "anak" `ənak` and `anək`). That fits unpredictable stress placement by each annotator, not a systematic split of conventions. The tier is `crowd-scraped`, so the row gates.

## Circular

### The TTS silver sets (`arabic_tts`, `portuguese_tts`, `spain_romance_tts`)

The board scores these three silver sets against their [corrected labels](../contributing/silver_correction.md). Two passes wrote each label blind to the engine, and the label is not a copy of the engine output. It stays circular in two ways.

The authorship is circular. The Claude lineage that wrote the specs also wrote the sentences, the source IPA and the corrected label. The provenance comment on the sibling `gold20_arabic` dataset calls that relation "near-circular".

The adjudication saw the engine. Where the two blind passes and the engine disagree, a third pass decides the label with the engine output as one of its candidates.

All three are `llm-corrected`, so none can gate, and the tier is correct. A PER on these rows measures distance from a model's label. No citation audit converts it into an accuracy. Only an independently collected gold would.

## False provenance label

### Abkhaz, `vox_communis`

The `ab` row carries the tier `epitran-derived`, and epitran cannot have produced it. epitran 1.35.2 ships 161 grapheme-to-phoneme maps in `epitran/data/map/`, and none is Abkhaz. It has no `abk` map and no `ab` map in any script. Another tool of the VoxCommunis pipeline built the Abkhaz phone tier: XPF, Charsiu or a custom dictionary.

The dataset-wide tier `epitran-derived` is a reasonable default for VoxCommunis. Its lexicons come from a mix of tools, and the tier is pessimistic on purpose. For this row, though, the label names a competitor that was not used. The name of the competitor is exactly what the tier exists to tell a reader. The reader is told to read the row as divergence from epitran, and no epitran output exists to diverge from.

The effect on gating is nil, because `epitran-derived` and the tiers that could replace it all refuse to gate. The fix is a name: the row needs a tier that does not claim a tool that was not used. The [dataset catalogue](datasets.md#coverage-hole-in-abkhaz-ab) explains why the row gets no `PROVENANCE_BY_LANG` override.

## Alphabet-chart entries in a row

The [scoreboard](generated/scoreboard.md) gives one PER per gold row. That number says something about running text only if the gold is running text. WikiPron scrapes Wiktionary headwords. For a small language, a Wiktionary edition often lists the whole alphabet as ordinary headwords: single letters, names of digraphs, and letters with diacritics. They sit in the same TSV as real words. A grapheme table transcribes those entries by construction, because they are the table read back. A row can therefore look excellent while its gold says little about real sentences.

[`scripts/gold_composition.py`](../../scripts/gold_composition.py) measures this. It reads each row of `benchmarks/results.json`, loads its gold from `.benchmark_cache/`, and splits it into a trivial subset and a subset of real words. It scores each subset with `evaluate_words` from `scripts/benchmark.py`, with stress stripped and broad normalization. `trivial_per` and `real_per` are therefore in the units of the board's PER column. The script never changes a spec or a board file.

### What counts as trivial

The signal comes from the language's own alphabet. Every spec has a `graphemes` table, which lists its letters and its multi-character units such as the Kwak'wala digraphs `kw`, `ch` and `dz`. An entry is a short form when its base form has one or two characters. The base form folds case and drops combining marks. If the distinct short forms of a row cover at least `ALPHABET_COVERAGE_THRESHOLD` (0.3) of the spec's alphabet, the row is an alphabet chart. All its short entries are then trivial. Below that coverage they stay ordinary short words.

A few short real words never come close to 30% of a real alphabet. A real scrape of an alphabet chart usually covers far more of it. Multi-word entries, from the sentence-level gold sets, are never trivial, because an alphabet chart is a list of words.

The fold catches more than plain letters. A chart row with a diacritic folds to the same base form as its bare letter and counts once. An example is the Kwak'wala "A̱", a plain `a` with a combining macron below. A chart row that spells a digraph such as `kw` as its own headword counts too. The comparison is with the spec's alphabet, not with a fixed length.

A fixed length cutoff, where any entry of two characters or fewer is trivial, does not work. Many languages have short real words: function words of one letter, such as French "y" or English "a", and content words of one syllable. A length rule would treat those the same in every language. Chinese monosyllables would count like the alphabet rows of Kwak'wala, for unrelated reasons.

A second kind of trivial entry has its own count, `n_bound_affix`. A single-word entry that contains U+0640 ARABIC TATWEEL is a bound affix from an inflection table, not a free word. The `_TATWEEL` docstring in the script gives the `tru` examples. Such an entry is trivial whatever its length or alphabet coverage.

The method does not find an entry whose gold is the name of a letter rather than its sound, such as English "y" as /waɪ/. That would need a per-language table of letter names, which does not exist here. Guessing one from the gold would make exactly the kind of unsourced rule that this project rejects. It shows indirectly, though. A chart row whose trivial subset scores unexpectedly badly usually has entries glossed with letter names, which the engine correctly does not produce.

### Running the script

Run it from the root of a checkout:

```bash
PYTHONPATH=. python scripts/gold_composition.py --max-n 5000
```

| Option | Effect |
|---|---|
| `--start N`, `--end N` | score only the board rows `[start:end]`, so a full sweep can run in batches |
| `--max-n N` | skip a row whose board `n` is above `N`, without loading its gold |

The script prints one JSON object. `rows_scored` and `rows_skipped_no_cache` count the rows it scored and skipped, and the `skipped` list names the skipped rows. A row is skipped when its gold is not in the cache, when it is above `--max-n`, or when its loader fails. The script blocks network access, so it never downloads gold. Its output depends only on what is in the cache. `most_flattered` lists the ten rows with the largest positive `gap`, and `rows` lists every scored row.

The `--max-n` skip has a known bound. A spec's alphabet has a few dozen graphemes. Even if every grapheme appears as a headword, a gold of `N` words has a trivial share below about `alphabet_size / N`. That bound fails for a script that writes one character per morpheme. A spot check of `ja` on `ipadict` found a large trivial share far above the cutoff. A CJK row skipped by `--max-n` can therefore hold a real finding, so check such rows with a higher bound or with none.

### Reading the output

| Field | Meaning |
|---|---|
| `trivial_share` | the trivial entries as a fraction of all the loaded gold entries of the row |
| `alphabet_coverage`, `is_alphabet_chart` | the share of the spec's alphabet that the short forms cover, and whether it reaches the threshold |
| `trivial_per`, `real_per` | the PER of each subset |
| `real_n` | the number of covered real words behind `real_per` |
| `gap` | `real_per − trivial_per` |

A large positive `gap` is the finding that the script exists to surface. An easy trivial subset pulls the headline PER down, while the real words score much worse. A negative `gap` means the trivial subset scored worse than the real words. That happens on a very small chart row with few real words left, or when the chart entries carry letter names. Then the alphabet chart does not flatter the row, and the output reports that as it is.

A `gap` from a handful of real words is noisy, as any PER on a small row is. Read it with that limit in mind.

`kwk` on `wikipron` is the row the method was built on, and it is a counter-example. 108 of its 116 raw entries (93.1%) are trivial: mostly single Latin letters, and several chart rows with diacritics such as "A̱". Its trivial subset scores worse than its real words, so the `gap` is negative. Eight real words are too few to lean on, but the direction holds. The alphabet chart does not make this row look good.

`tru` on `wikipron` has 6 bound-affix entries among its 232 raw entries (2.6%). They also score worse than the real words, so the bound forms are harder for the spec, not easier.

### What the measurement is not

It is not a spec fix, and it never moves `docs/evaluation/generated/scoreboard.md` or `benchmarks/results.json`. Only `scripts/benchmark.py` writes those, from the actual behaviour of the spec. A large `gap` means that the row needs a larger and more representative gold before it can support a claim about running text. It is not evidence that the spec is wrong. A `trivial_per` or `real_per` on a `crowd-scraped` or lower tier carries every caveat of that tier, as [benchmarks.md](benchmarks.md#provenance-and-reliability-read-this-before-trusting-any-number) describes.

---
[← TTS silver sets](silver_sets.md) · [Home](../index.md) · [Scoreboard →](generated/scoreboard.md)
