# Kwakiutl (`kwk`)

<!-- atlas:summary begin -->
Kwakiutl is a Wakashan language, written in the Latin script. Glottolog places it in the North America macroarea. The `kwk` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kwk` |
| ISO 639-3 | [kwk](https://iso639-3.sil.org/code/kwk), Kwak'wala |
| Wikipedia | [Kwakʼwala](https://en.wikipedia.org/wiki/Kwak%CA%BCwala) |
| Family | [Wakashan](by-family.md#wakashan) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Wakashan](https://tigregotico.github.io/orthography2ipa/#x-clade-waka1280) `x-clade-waka1280` |
| Explorer | [`kwk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kwk) |
| Spec file | [`kwk.json`](../../orthography2ipa/data/kwk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1947 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 79 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kwk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kwk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kwk_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Kwak'wala (kwak1269)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/kwak1269)
2. <a id="src-boas1947"></a>Boas, Franz (1947). *Kwakiutl Grammar, with a Glossary of the Suffixes*. Transactions of the American Philosophical Society, New Series, 37(3), American Philosophical Society, Philadelphia. Cited: 203-377.
3. <a id="src-kwk_orthography"></a>Wikipedia contributors (2024). *Kwakʼwala, Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kwak%CA%BCwala)
4. <a id="src-kwk_umista_irp"></a>School District 85 (Vancouver Island North) (2010). *Kwak̓wala 5 to 12, Integrated Resource Package 2010*. School District 85, British Columbia. Cited: E-4-E-6. [web.archive.org](https://web.archive.org/web/20160129070533/http://sd85-websrv2012.sd85.bc.ca/wp-content/uploads/2015/05/Kwakwala-IRP-approved.pdf)
5. <a id="src-unicode17_latin_extd"></a>Unicode Consortium (2025). *The Unicode Standard, Version 17.0: Latin Extended-D (U+A720-U+A7FF)*. Unicode, Inc. Cited: 1119. [unicode.org](https://www.unicode.org/charts/PDF/UA720.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kwk` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 116 | 0.0070 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 50 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ | d t tʼ |  |  | k kʷ kʷʼ kʼ ɡ ɡʷ | q qʷ qʷʼ qʼ ɢ ɢʷ | ʔ |
| Affricate |  | d͡z d͡ɮ t͡s t͡sʼ t͡ɬ t͡ɬʼ | tʃ |  |  |  |  |
| Nasal | m | n |  |  |  |  |  |
| Fricative |  | s | ʃ |  | x xʷ | χ χʷ | h |
| Lateral fricative |  | ɬ |  |  |  |  |  |
| Approximant |  |  |  | j |  |  |  |
| Lateral approximant |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [jˀ] [lˀ] [mˀ] [nˀ] [w] [wˀ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨a̱⟩ | [ə] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [t͡s] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨c̓⟩ | [t͡sʼ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dz⟩ | [d͡z] |  |
| ⟨dł⟩ | [d͡ɮ] |  |
| ⟨dᶻ⟩ | [d͡z] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gw⟩ | [ɡʷ] |  |
| ⟨gʷ⟩ | [ɡʷ] |  |
| ⟨g̱⟩ | [ɢ] |  |
| ⟨g̱w⟩ | [ɢʷ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨kʷ⟩ | [kʷ] |  |
| ⟨k̓⟩ | [kʼ] |  |
| ⟨k̓w⟩ | [kʷʼ] |  |
| ⟨k̓ʷ⟩ | [kʷʼ] |  |
| ⟨l⟩ | [l] |  |
| ⟨l̓⟩ | [lˀ] |  |
| ⟨m⟩ | [m] |  |
| ⟨m̓⟩ | [mˀ] |  |
| ⟨n⟩ | [n] |  |
| ⟨n̓⟩ | [nˀ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨p̓⟩ | [pʼ] |  |
| ⟨q⟩ | [q] |  |
| ⟨qʷ⟩ | [qʷ] |  |
| ⟨q̓⟩ | [qʼ] |  |
| ⟨q̓ʷ⟩ | [qʷʼ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [t͡s] |  |
| ⟨tł⟩ | [t͡ɬ] |  |
| ⟨t̓⟩ | [tʼ] |  |
| ⟨t̓s⟩ | [t͡sʼ] |  |
| ⟨t̓ł⟩ | [t͡ɬʼ] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨w̓⟩ | [wˀ] |  |
| ⟨x⟩ | [x] |  |
| ⟨xw⟩ | [xʷ] |  |
| ⟨xʷ⟩ | [xʷ] |  |
| ⟨x̌⟩ | [χ] |  |
| ⟨x̌ʷ⟩ | [χʷ] |  |
| ⟨x̱⟩ | [χ] |  |
| ⟨x̱w⟩ | [χʷ] |  |
| ⟨y⟩ | [j] |  |
| ⟨y̓⟩ | [jˀ] |  |
| ⟨ł⟩ | [ɬ] |  |
| ⟨ƛ⟩ | [t͡ɬ] |  |
| ⟨ƛ̓⟩ | [t͡ɬʼ] |  |
| ⟨ǧ⟩ | [ɢ] |  |
| ⟨ǧʷ⟩ | [ɢʷ] |  |
| ⟨ə⟩ | [ə] |  |
| ⟨ʔ⟩ | [ʔ] |  |
| ⟨ʼ⟩ | [ʔ] |  |
| ⟨ʼl⟩ | [lˀ] |  |
| ⟨ʼm⟩ | [mˀ] |  |
| ⟨ʼn⟩ | [nˀ] |  |
| ⟨ʼw⟩ | [wˀ] |  |
| ⟨ʼy⟩ | [jˀ] |  |
| ⟨ḵ⟩ | [q] |  |
| ⟨ḵw⟩ | [qʷ] |  |
| ⟨ḵ̓⟩ | [qʼ] |  |
| ⟨ḵ̓w⟩ | [qʷʼ] |  |
| ⟨Ꟛ⟩ | [d͡ɮ] |  |
| ⟨ꟛ⟩ | [d͡ɮ] |  |
| ⟨Ƛ⟩ | [t͡ɬ] |  |
| ⟨Ƛ̓⟩ | [t͡ɬʼ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kwk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kuwaiti Arabic](afb-KW.md) · [Home](../index.md) · [Kyrgyz →](ky.md)
