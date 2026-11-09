# Yiddish (`yi`)

<!-- atlas:summary begin -->
Yiddish is a West Germanic language, written in the Hebrew script. Glottolog places it in 22 countries. The `yi` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `yi` |
| ISO 639-3 | [yid](https://iso639-3.sil.org/code/yid), Yiddish |
| Glottolog | [east2295](https://glottolog.org/resource/languoid/id/east2295), Eastern Yiddish |
| Wikidata | [Q8641](https://www.wikidata.org/wiki/Q8641) |
| Wikipedia | [Yiddish language](https://en.wikipedia.org/wiki/Yiddish_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Argentina](by-region.md#argentina), [Australia](by-region.md#australia), [Belarus](by-region.md#belarus), [Belgium](by-region.md#belgium), [Canada](by-region.md#canada), [Costa Rica](by-region.md#costa-rica), [Estonia](by-region.md#estonia), [Hungary](by-region.md#hungary) and 14 more |
| Script | [Hebrew](by-script.md#hebrew) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Parent | [West Germanic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2793) `x-clade-west2793` |
| Explorer | [`yi` in the data explorer](https://tigregotico.github.io/orthography2ipa/#yi) |
| Spec file | [`yi.json`](../../orthography2ipa/data/yi.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Eastern Yiddish in YIVO orthography, pointed, with the historical unpointed spelling of the Hebrew-Aramaic component retained (⟨ח⟩ ⟨ת⟩ ⟨שׂ⟩ ⟨כּ⟩ ⟨תּ⟩) and the five final forms ⟨ך ם ן ף ץ⟩ in use, neither holds in Soviet orthography, which respells the Hebrew-Aramaic component phonetically.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2024. [Sources](#sources) lists them. The spec file writes all 50 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/yi.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `yi` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wiki-yi"></a>Wikipedia contributors (2024). *Yiddish language*.
2. <a id="src-wiki-yi-phon"></a>Wikipedia contributors (2024). *Yiddish phonology*.
3. <a id="src-wiki-yi-orth"></a>Wikipedia contributors (2024). *Yiddish orthography*.
4. <a id="src-jlp-yi"></a>Jewish Language Project (2024). *Yiddish (Eastern)*. [jewishlanguages.org](https://www.jewishlanguages.org/eastern-yiddish)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `yi` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4051 | 0.2042 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |  |
| Nasal | m m̩ |  | n n̩ |  |  | ŋ ŋ̩ |  |  |
| Trill |  |  | r |  |  |  | ʀ |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l l̩ |  | ʎ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  |  |
| Near-close | ɪ |  | ʊ |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [aɪ] [ji] [ɔɪ] [ɛɪ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨א⟩ | ∅ [a] |  |
| ⟨אַ⟩ | [a] |  |
| ⟨אָ⟩ | [ɔ] |  |
| ⟨ב⟩ | [b] |  |
| ⟨בֿ⟩ | [v] |  |
| ⟨ג⟩ | [ɡ] |  |
| ⟨ד⟩ | [d] |  |
| ⟨דזש⟩ | [dʒ] |  |
| ⟨ה⟩ | [h] |  |
| ⟨ו⟩ | [ʊ] |  |
| ⟨וּ⟩ | [ʊ] |  |
| ⟨וו⟩ | [v] |  |
| ⟨וי⟩ | [ɔɪ] |  |
| ⟨ז⟩ | [z] |  |
| ⟨זש⟩ | [ʒ] |  |
| ⟨ח⟩ | [χ] [x] |  |
| ⟨ט⟩ | [t] |  |
| ⟨טש⟩ | [tʃ] |  |
| ⟨י⟩ | [ɪ] [j] | word initial [j] [ɪ] |
| ⟨יִ⟩ | [i] |  |
| ⟨יי⟩ | [ɛɪ] |  |
| ⟨ייִ⟩ | [ji] |  |
| ⟨ייַ⟩ | [aɪ] |  |
| ⟨ך⟩ | [χ] [x] |  |
| ⟨כ⟩ | [χ] [x] |  |
| ⟨כּ⟩ | [k] |  |
| ⟨ל⟩ | [l] [ʎ] |  |
| ⟨ם⟩ | [m] |  |
| ⟨מ⟩ | [m] |  |
| ⟨ן⟩ | [n] |  |
| ⟨נ⟩ | [n] |  |
| ⟨ס⟩ | [s] |  |
| ⟨ע⟩ | [ɛ] [ə] | nucleus unstressed [ə] [ɛ] |
| ⟨ף⟩ | [f] |  |
| ⟨פ⟩ | [f] |  |
| ⟨פּ⟩ | [p] |  |
| ⟨פֿ⟩ | [f] |  |
| ⟨ץ⟩ | [ts] |  |
| ⟨צ⟩ | [ts] |  |
| ⟨ק⟩ | [k] |  |
| ⟨ר⟩ | [r] [ʀ] [ɾ] |  |
| ⟨ש⟩ | [ʃ] |  |
| ⟨שׁ⟩ | [ʃ] |  |
| ⟨שׂ⟩ | [s] |  |
| ⟨ת⟩ | [s] |  |
| ⟨תּ⟩ | [t] |  |
| ⟨װ⟩ | [v] |  |
| ⟨ױ⟩ | [ɔɪ] |  |
| ⟨ײ⟩ | [ɛɪ] |  |
| ⟨ײַ⟩ | [aɪ] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 5 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `YI_N_VELAR` | /n/ → [ŋ], before [k] [ɡ] | ⟨נג⟩ [ŋɡ] | - |
| `YI_N_SYLL_BILABIAL` | /n/ → [m̩], word-finally, after [m] [b] [p] | ⟨לעבן⟩ [ˈlɛbm̩] | - |
| `YI_N_SYLL_DORSAL` | /n/ → [ŋ̩], word-finally, after [k] [ɡ] [ŋ] [χ] [x] | ⟨יאָגן⟩ [ˈjɔɡŋ̩] | - |
| `YI_N_SYLLABIC` | /n/ → [n̩], word-finally, after a consonant | ⟨אָװנט⟩ [ˈɔvn̩t] | - |
| `YI_L_SYLLABIC` | /l/ → [l̩], word-finally, after a consonant | ⟨אײזל⟩ [ˈɛɪzl̩] | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "yi")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Yemeni Arabic](ayn-YE.md) · [Home](../index.md) · [Yoruba →](yo.md)
