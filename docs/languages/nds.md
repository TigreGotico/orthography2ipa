# Low German (Plattdeutsch) (`nds`)

<!-- atlas:summary begin -->
Low German (Plattdeutsch) is a West Germanic language, written in the Latin script. Glottolog places it in Germany. The `nds` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nds` |
| ISO 639-3 | [nds](https://iso639-3.sil.org/code/nds), Low German |
| Glottolog | [nort2627](https://glottolog.org/resource/languoid/id/nort2627), Eastern Low German |
| Wikidata | [Q25433](https://www.wikidata.org/wiki/Q25433) |
| Wikipedia | [Low German](https://en.wikipedia.org/wiki/Low_German) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Germany](by-region.md#germany) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1600, living |
| Ancestor | [Old Saxon](https://tigregotico.github.io/orthography2ipa/#osx) `osx` |
| Explorer | [`nds` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nds) |
| Spec file | [`nds.json`](../../orthography2ipa/data/nds.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Low German (Plattdeutsch / Nedderdütsch), encoded for the SASS orthography of Northern Low Saxon (Nordniedersächsisch), the most widely used Low German spelling. Descended from Old Saxon, NOT from Old High German, and it did not undergo the High German consonant shift: maken vs. German machen, water vs. German Wasser.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1990 to 2018. [Sources](#sources) lists them. The spec file writes all 72 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nds.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nds` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sass2018"></a>Thies, Heinrich (Hrsg.) (2018). *SASS Plattdeutsche Schreibregeln*. Wachholtz / Fehrs-Gilde. Cited: §§1, 3, 6, 9, 12, 16, 18, 20, 21, 23, 27. [sass-platt.de](https://sass-platt.de/plattdeutsche-rechtschreibung/)
2. <a id="src-sassgrammatik"></a>Thies, Heinrich (2011). *SASS Plattdeutsche Grammatik*. Wachholtz. Cited: 1.1.4.1, 1.1.4.5, 1.1.4.6. [sass-platt.de](https://sass-platt.de/plattdeutsche-grammatik/)
3. <a id="src-prehn2012"></a>Prehn, Maike (2012). *Vowel quantity and the fortis-lenis distinction in North Low Saxon*. LOT (LOT Dissertation Series 291), Utrecht. Cited: ch. 3, ch. 5.1, ch. 6. [lotpublications.nl](https://www.lotpublications.nl/Documents/291_fulltext.pdf)
4. <a id="src-lindow1998"></a>Lindow, W. & Möhn, D. & Niebaum, H. & Stellmacher, D. & Taubken, H. & Wirrer, J. (1998). *Niederdeutsche Grammatik*. Verlag Schuster, Leer. Cited: 30.
5. <a id="src-stellmacher1990"></a>Stellmacher, D. (1990). *Niederdeutsche Sprache: Eine Einführung*. Peter Lang.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nds` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 308 | 0.2231 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 56 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Affricate |  |  | ts | tʃ |  |  |  |  |
| Nasal | m |  | n n̩ |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  | ʀ |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ | ç | x ɣ | ʁ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː yː |  | uː |
| Near-close | ɪ ʏ |  | ʊ |
| Close-mid | eː øː |  | oː |
| Mid |  | ə |  |
| Open-mid | œ ɛ ɛː |  | ɔ ɔː |
| Near-open |  | ɐ ɐ̯ |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [aɪ] [aʊ] [ks] [kv] [sp] [st] [ŋk] [ɔʏ] [ʃp] [ʃt].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [ɔː] [aː] |  |
| ⟨aa⟩ | [ɔː] [oː] [aː] |  |
| ⟨ah⟩ | [ɔː] [oː] |  |
| ⟨ai⟩ | [aɪ] |  |
| ⟨au⟩ | [aʊ] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [k] [ts] |  |
| ⟨ch⟩ | [x] |  |
| ⟨ck⟩ | [k] |  |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨e⟩ | [ɛ] [eː] [ə] | default [ɛ] [eː] [ə] · nucleus stressed [ɛ] [eː] · nucleus unstressed [ə] |
| ⟨ee⟩ | [eː] |  |
| ⟨eh⟩ | [eː] |  |
| ⟨ei⟩ | [aɪ] |  |
| ⟨eu⟩ | [ɔʏ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [ɣ] [x] | default [ɡ] · intervocalic [ɡ] [ɣ] · word final [x] [ç] · word initial [ɡ] [ç] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] [iː] |  |
| ⟨ie⟩ | [iː] |  |
| ⟨ih⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨o⟩ | [ɔ] [oː] |  |
| ⟨oh⟩ | [oː] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kv] |  |
| ⟨r⟩ | [r] [ɾ] [ʁ] | before consonant [r] [ɐ̯] · default [r] [ɾ] · word final [r] [ɐ̯] |
| ⟨s⟩ | [z] [s] | default [s] · intervocalic [z] · word final [s] · word initial [z] |
| ⟨sch⟩ | [ʃ] |  |
| ⟨sp⟩ | [sp] [ʃp] |  |
| ⟨ss⟩ | [s] |  |
| ⟨st⟩ | [st] [ʃt] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t] |  |
| ⟨tsch⟩ | [tʃ] |  |
| ⟨tz⟩ | [ts] |  |
| ⟨u⟩ | [ʊ] [uː] |  |
| ⟨uh⟩ | [uː] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] [f] | default [v] · word final [f] |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [ʏ] [yː] |  |
| ⟨yy⟩ | [yː] |  |
| ⟨z⟩ | [ts] |  |
| ⟨ß⟩ | [s] |  |
| ⟨à⟩ | [a] [ɔː] [aː] |  |
| ⟨â⟩ | [a] [ɔː] [aː] |  |
| ⟨ä⟩ | [ɛ] [ɛː] |  |
| ⟨äh⟩ | [ɛː] |  |
| ⟨äu⟩ | [ɔʏ] |  |
| ⟨ää⟩ | [ɛː] |  |
| ⟨å⟩ | [a] [ɔː] [aː] |  |
| ⟨æ⟩ | [ɛ] [ɛː] |  |
| ⟨ë⟩ | [ɛ] [eː] [ə] |  |
| ⟨ö⟩ | [œ] [øː] |  |
| ⟨öh⟩ | [øː] |  |
| ⟨öö⟩ | [øː] |  |
| ⟨ü⟩ | [ʏ] [yː] |  |
| ⟨üh⟩ | [yː] |  |
| ⟨üü⟩ | [yː] |  |
| ⟨ę⟩ | [ɛ] [eː] [ə] |  |
| ⟨œ⟩ | [œ] [øː] |  |

Stress falls on the first syllable by default.

Grammatical endings: ⟨-en⟩ ∅ [n̩], ⟨-er⟩ ∅ [ɐ].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 14 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NDS_OPEN_SYLLABLE_A` | /a/ → [ɔː], stressed, in the nucleus, before a consonant, spelled ⟨a⟩, with more context in the spec | - | - |
| `NDS_OPEN_SYLLABLE_E` | /ɛ/ → [eː], stressed, in the nucleus, before a consonant, spelled ⟨e⟩, with more context in the spec | - | - |
| `NDS_OPEN_SYLLABLE_I` | /ɪ/ → [iː], stressed, in the nucleus, before a consonant, spelled ⟨i⟩, with more context in the spec | - | - |
| `NDS_OPEN_SYLLABLE_O` | /ɔ/ → [oː], stressed, in the nucleus, before a consonant, spelled ⟨o⟩, with more context in the spec | - | - |
| `NDS_OPEN_SYLLABLE_U` | /ʊ/ → [uː], stressed, in the nucleus, before a consonant, spelled ⟨u⟩, with more context in the spec | - | - |
| `NDS_OPEN_SYLLABLE_OE` | /œ/ → [øː], stressed, in the nucleus, before a consonant, spelled ⟨ö⟩, with more context in the spec | - | - |
| `NDS_OPEN_SYLLABLE_UE` | /ʏ/ → [yː], stressed, in the nucleus, before a consonant, spelled ⟨ü⟩, with more context in the spec | - | - |
| `NDS_OPEN_FINAL_A` | /a/ → [ɔː], word-finally, stressed, in the nucleus, spelled ⟨a⟩ | - | - |
| `NDS_OPEN_FINAL_E` | /ɛ/ → [eː], word-finally, stressed, in the nucleus, spelled ⟨e⟩ | - | - |
| `NDS_OPEN_FINAL_I` | /ɪ/ → [iː], word-finally, stressed, in the nucleus, spelled ⟨i⟩ | - | - |
| `NDS_OPEN_FINAL_O` | /ɔ/ → [oː], word-finally, stressed, in the nucleus, spelled ⟨o⟩ | - | - |
| `NDS_OPEN_FINAL_U` | /ʊ/ → [uː], word-finally, stressed, in the nucleus, spelled ⟨u⟩ | - | - |
| `NDS_OPEN_FINAL_OE` | /œ/ → [øː], word-finally, stressed, in the nucleus, spelled ⟨ö⟩ | - | - |
| `NDS_OPEN_FINAL_UE` | /ʏ/ → [yː], word-finally, stressed, in the nucleus, spelled ⟨ü⟩ | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nds")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Louisiana Creole](lou.md) · [Home](../index.md) · [Lower Navarrese Basque →](eu-x-nafarra-beherea.md)
