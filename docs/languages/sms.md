# Skolt Sami (`sms`)

<!-- atlas:summary begin -->
Skolt Sami is a Saami language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `sms` spec is at the research tier. It cites 5 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sms` |
| ISO 639-3 | [sms](https://iso639-3.sil.org/code/sms), Skolt Sami |
| Wikipedia | [Skolt Sami language](https://en.wikipedia.org/wiki/Skolt_Sami_language) |
| Family | [Uralic](by-family.md#uralic) > [Saami](by-family.md#uralic--saami) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Saami](https://tigregotico.github.io/orthography2ipa/#x-clade-saam1281) `x-clade-saam1281` |
| Explorer | [`sms` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sms) |
| Spec file | [`sms.json`](../../orthography2ipa/data/sms.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skolt Sami is an Eastern Saami language of the Uralic family, written since 1973 in a Latin orthography rich in special letters.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 2010 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 60 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sms.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sms` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sms_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Skolt Saami (skol1241)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/skol1241)
2. <a id="src-sms_orthography"></a>Wikipedia contributors (2024). *Skolt Sami language, writing system and phonology*. [en.wikipedia.org](https://en.wikipedia.org/wiki/Skolt_Sami_language)
3. <a id="src-feist2010"></a>Feist, Timothy (2010). *A grammar of Skolt Saami*. University of Manchester (PhD thesis).
4. <a id="src-giellalt_lang_sms"></a>Divvun and Giellatekno (giellalt) (2024). *lang-sms: Skolt Sami language model, orthography data (docs/data/1-2-syll_pal-CC.txt, docs/data/1-2-syll_no-pal-CC.txt)*. UiT The Arctic University of Norway. [github.com](https://github.com/giellalt/lang-sms)
5. <a id="src-uralic_languages_2ed"></a>Bakró-Nagy, M., Laakso, J. & Skribnik, E. (eds.) (2022). *The Uralic Languages, 2nd edition*. Routledge. [api.pageplace.de](https://api.pageplace.de/preview/DT0400.9781317230977_A42846364/preview-9781317230977_A42846364.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `sms` | gold | lexicon-derived | CC BY 4.0 | 1063 | 0.2200 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sms` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 111 | 0.0045 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 58 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |
| Affricate |  |  |  | dz ts | dʒ tʃ |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |
| Trill |  |  |  | r |  |  |  |
| Fricative |  | f v | ð | s z | ʃ ʒ | ʝ | x ɣ |
| Lateral approximant |  |  |  | l |  | ʎ |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e eː | ɘ ɘː | o oː |
| Open-mid | ɛ ɛː |  | ɔ ɔː |
| Near-open |  | ɐ ɐː |  |
| Open | a aː |  | ɑ ɑː |

Sequences that the spec writes as one unit: [ccç] [cç] [ddz] [ddʒ] [tts] [ttʃ] [ɟɟʝ] [ɟʝ] [ɲɲ] [ʎʎ] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ |  |
| ⟨a⟩ | [ɑ] |  |
| ⟨aa⟩ | [ɑː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨cc⟩ | [tts] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ee⟩ | [eː] [ɛː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [ʝ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lj⟩ | [ʎ] |  |
| ⟨llj⟩ | [ʎʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nj⟩ | [ɲ] |  |
| ⟨nnj⟩ | [ɲɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [z] |  |
| ⟨´⟩ | [ʲ] |  |
| ⟨â⟩ | [ɐ] |  |
| ⟨ââ⟩ | [ɐː] |  |
| ⟨ä⟩ | [a] |  |
| ⟨ää⟩ | [aː] |  |
| ⟨å⟩ | [ɔ] |  |
| ⟨åå⟩ | [ɔː] |  |
| ⟨õ⟩ | [ɘ] |  |
| ⟨õõ⟩ | [ɘː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨čč⟩ | [ttʃ] |  |
| ⟨đ⟩ | [ð] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ž⟩ | [ʒ] |  |
| ⟨ǥ⟩ | [ɣ] |  |
| ⟨ǧ⟩ | [ɟʝ] |  |
| ⟨ǧǧ⟩ | [ɟɟʝ] |  |
| ⟨ǩ⟩ | [cç] |  |
| ⟨ǩǩ⟩ | [ccç] |  |
| ⟨ǯ⟩ | [dʒ] |  |
| ⟨ǯǯ⟩ | [ddʒ] |  |
| ⟨ʒ⟩ | [dz] |  |
| ⟨ʒʒ⟩ | [ddz] |  |
| ⟨ʹ⟩ | [ʲ] |  |
| ⟨ˊ⟩ | [ʲ] |  |
| ⟨’⟩ | ∅ |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 2 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `SMS_PALATALISATION_MARK` | /ʲ/ → ∅, before a consonant, with more context in the spec | - | - |
| `SMS_PALATALISATION_MARK_NO_TARGET` | /ʲ/ → ∅, before a vowel | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sms")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sinhala](si.md) · [Home](../index.md) · [Slovak →](sk.md)
