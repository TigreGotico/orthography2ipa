# Hunsrik (Riograndenser Hunsrückisch) (`hrx`)

<!-- atlas:summary begin -->
Hunsrik (Riograndenser Hunsrückisch) is a Northwest Germanic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `hrx` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `hrx` |
| ISO 639-3 | [hrx](https://iso639-3.sil.org/code/hrx), Hunsrik |
| Wikipedia | [Riograndenser Hunsrückisch](https://en.wikipedia.org/wiki/Riograndenser_Hunsr%C3%BCckisch) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic](by-family.md#indo-european--germanic--northwest-germanic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Ancestor | [Middle High German](https://tigregotico.github.io/orthography2ipa/#gmh) `gmh` |
| Explorer | [`hrx` in the data explorer](https://tigregotico.github.io/orthography2ipa/#hrx) |
| Spec file | [`hrx.json`](../../orthography2ipa/data/hrx.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Hunsrik, a West-Central German (Rhine-Franconian) language of southern Brazil, described here in the German-based ESCRITHU/ALMA-H written norm rather than in Wiesemann's Hunsrik Schreiwer orthography, which spells the same language with ⟨x⟩ for /ʃ/ and ⟨y⟩ for /j/. The consonants are where German spelling misleads.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1996 to 2007. [Sources](#sources) lists them. The spec file writes all 75 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/hrx.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `hrx` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-altenhofen2007"></a>Altenhofen, Cléo V., Frey, Jaqueline, Käfer, Maria Lidiani, Klassmann, Mário S., Neumann, Gerson R., Pupp Spinassé, Karen (2007). *Fundamentos para uma escrita do Hunsrückisch falado no Brasil*. Revista Contingentia 2. Cited: 73-87. [seer.ufrgs.br](https://seer.ufrgs.br/index.php/contingentia/article/view/3867)
2. <a id="src-altenhofen1996"></a>Altenhofen, Cléo Vilson (1996). *Hunsrückisch in Rio Grande do Sul: Ein Beitrag zur Beschreibung einer deutschbrasilianischen Dialektvarietät*. Franz Steiner Verlag.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `hrx` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2002 | 0.0821 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 46 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  | t tʰ |  |  | k kʰ |  |
| Affricate |  |  | t͡s | t͡ʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s | ʃ | ç | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e eː |  | o oː õ |
| Mid |  | ə |  |
| Open-mid | ɛ ɛː |  | ɔ ɔː |
| Near-open |  | ɐ ɐ̃ |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [aɪ̯] [aʊ̯] [ks] [kv] [kw] [ŋk] [ɔɪ̯].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [ɔː] |  |
| ⟨ah⟩ | [aː] |  |
| ⟨au⟩ | [aʊ̯] |  |
| ⟨b⟩ | [p] |  |
| ⟨bb⟩ | [p] |  |
| ⟨c⟩ | [k] | before front vowel [s] · default [k] |
| ⟨ch⟩ | [x] | after consonant [ç] · after front vowel [ç] · default [x] · word initial [ʃ] |
| ⟨ck⟩ | [k] |  |
| ⟨d⟩ | [t] |  |
| ⟨dd⟩ | [t] |  |
| ⟨e⟩ | [ə] | default [ə] [e] · nucleus stressed [e] [eː] [ɛ] · nucleus unstressed [ə] |
| ⟨ee⟩ | [eː] |  |
| ⟨eh⟩ | [eː] |  |
| ⟨ei⟩ | [aɪ̯] |  |
| ⟨eu⟩ | [ɔɪ̯] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [f] |  |
| ⟨g⟩ | [k] |  |
| ⟨gg⟩ | [k] |  |
| ⟨gh⟩ | [x] | after consonant [ç] · after front vowel [ç] · default [x] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ie⟩ | [iː] |  |
| ⟨ih⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] [ŋk] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nn⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oh⟩ | [oː] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kw] [kv] |  |
| ⟨r⟩ | [r] | before consonant ∅ [r] · default [r] · word final [ɐ] ∅ |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sch⟩ | [ʃ] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tsch⟩ | [t͡ʃ] |  |
| ⟨tt⟩ | [t] |  |
| ⟨tz⟩ | [t͡s] |  |
| ⟨u⟩ | [u] |  |
| ⟨uh⟩ | [uː] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] | default [v] · word final [f] |
| ⟨w⟩ | [v] |  |
| ⟨ww⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [t͡s] |  |
| ⟨á⟩ | [aː] |  |
| ⟨â⟩ | [a] |  |
| ⟨ã⟩ | [ɐ̃] |  |
| ⟨ä⟩ | [ɛ] |  |
| ⟨ää⟩ | [ɛː] |  |
| ⟨ç⟩ | [s] |  |
| ⟨é⟩ | [ɛ] |  |
| ⟨ê⟩ | [e] |  |
| ⟨ë⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ó⟩ | [ɔ] |  |
| ⟨õ⟩ | [õ] |  |
| ⟨ö⟩ | [e] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ü⟩ | [i] |  |

Stress falls on the first syllable by default. A written ⟨á⟩ marks the stressed vowel.

Grammatical endings: ⟨-er⟩ [a].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 8 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `HRX_ASPIRATE_P` | /p/ → [pʰ], word-initially, before a vowel, spelled ⟨p⟩ | - | [Altenhofen 2007](#src-altenhofen2007) |
| `HRX_ASPIRATE_T` | /t/ → [tʰ], word-initially, before a vowel, spelled ⟨t⟩ | - | [Altenhofen 2007](#src-altenhofen2007) |
| `HRX_ASPIRATE_K` | /k/ → [kʰ], word-initially, before a vowel, spelled ⟨k⟩ ⟨ck⟩ | - | [Altenhofen 2007](#src-altenhofen2007) |
| `HRX_S_RETRACTION` | /s/ → [ʃ], spelled ⟨s⟩, before ⟨p⟩ ⟨t⟩ | - | [Altenhofen 2007](#src-altenhofen2007) |
| `HRX_LONG_A_OPEN_FINAL` | /a/ → [aː], stressed, in the nucleus, before a consonant, spelled ⟨a⟩, with more context in the spec | - | [Altenhofen 2007](#src-altenhofen2007) |
| `HRX_LONG_I_OPEN_FINAL` | /i/ → [iː], stressed, in the nucleus, before a consonant, spelled ⟨i⟩, with more context in the spec | - | [Altenhofen 2007](#src-altenhofen2007) |
| `HRX_LONG_O_OPEN_FINAL` | /o/ → [oː], stressed, in the nucleus, before a consonant, spelled ⟨o⟩, with more context in the spec | - | [Altenhofen 2007](#src-altenhofen2007) |
| `HRX_LONG_U_OPEN_FINAL` | /u/ → [uː], stressed, in the nucleus, before a consonant, spelled ⟨u⟩, with more context in the spec | - | [Altenhofen 2007](#src-altenhofen2007) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "hrx")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hungarian](hu.md) · [Home](../index.md) · [Iban →](iba.md)
