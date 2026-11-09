# Persian (Farsi) (`fa`)

<!-- atlas:summary begin -->
Persian (Farsi) is an Iranian language, written in the Arabic script. Glottolog places it in 6 countries. The `fa` spec is at the research tier. It cites 5 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `fa` |
| Aliases | `fas` |
| ISO 639-3 | [fas](https://iso639-3.sil.org/code/fas), Persian |
| Glottolog | [west2369](https://glottolog.org/resource/languoid/id/west2369), Western Farsi |
| Wikidata | [Q9168](https://www.wikidata.org/wiki/Q9168) |
| Wikipedia | [Persian language](https://en.wikipedia.org/wiki/Persian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Iranian](by-family.md#indo-european--indo-iranian--iranian) |
| Region | [Eurasia](by-region.md#eurasia) > [Afghanistan](by-region.md#afghanistan), [Azerbaijan](by-region.md#azerbaijan), [Iran](by-region.md#iran), [Iraq](by-region.md#iraq), [Turkmenistan](by-region.md#turkmenistan), [Türkiye](by-region.md#türkiye) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Ancestor | [Proto-Iranian](https://tigregotico.github.io/orthography2ipa/#ira) `ira` |
| Child lects | 4, see [Related lects](#related-lects) |
| Explorer | [`fa` in the data explorer](https://tigregotico.github.io/orthography2ipa/#fa) |
| Spec file | [`fa.json`](../../orthography2ipa/data/fa.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Tehran standard. Many Arabic emphatic/pharyngeal consonants have merged with plain counterparts. 6-vowel system: /ɒː, æ, e, o, iː, uː/ (Windfuhr 1979/2009, Majidi & Ternes 1991 JIPA illustration, Toosarvandani 2004). ORTHOGRAPHY. Perso-Arabic is an abjad with three matres lectionis.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1979 to 2009. [Sources](#sources) lists them. The spec file writes all 47 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/fa.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `fa` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Dari (Afghan Persian)](https://tigregotico.github.io/orthography2ipa/#fa-AF) `fa-AF`: Afghanistan, skeleton tier
- [Tajik](tg.md) `tg`: Afghanistan, China, Kyrgyzstan, Tajikistan, Uzbekistan, research tier
- [Early New Persian (Perso-Arabic reading)](https://tigregotico.github.io/orthography2ipa/#fa-x-enp) `fa-x-enp`: research tier
- [Tehran Persian (Standard Iranian)](https://tigregotico.github.io/orthography2ipa/#fa-x-tehran) `fa-x-tehran`: skeleton tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 0 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-mahootian1997"></a>Mahootian, S. (1997). *Persian*. Routledge.
2. <a id="src-windfuhr1979"></a>Windfuhr, G. (1979). *Persian Grammar: History and State of Its Study*. Mouton.
3. <a id="src-lazard1992"></a>Lazard, G. (1992). *A Grammar of Contemporary Persian*. Mazda Publishers.
4. <a id="src-majidi1991"></a>Majidi, M.-R. & Ternes, E. (1991). *Persian (Farsi)*. Journal of the International Phonetic Association 21(2), Illustrations of the IPA. Cited: 96-97.
5. <a id="src-windfuhr2009"></a>Windfuhr, G. & Perry, J. R. (2009). *Persian and Tajik (in G. Windfuhr, ed., The Iranian Languages)*. Routledge.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `fa` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 9279 | 0.3943 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `fa` | generated | machine-generated | MIT, each file its own | 7695 | 0.2540 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 43 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ | ɢ | ʔ |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ | ʁ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | iː | uː |
| Close-mid | e | o |
| Near-open | æ |  |
| Open |  | ɒː |

Sequences that the spec writes as one unit: [hɒː] [ow] [xɒː] [xɒːh] [ɒːh] [ʔɒː] [ʔɒːh].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ء⟩ | [ʔ] |  |
| ⟨آ⟩ | [ʔɒː] |  |
| ⟨آه⟩ | [ʔɒːh] |  |
| ⟨أ⟩ | [ʔ] |  |
| ⟨ؤ⟩ | [ʔ] |  |
| ⟨ئ⟩ | [ʔ] |  |
| ⟨ا⟩ | [ʔ] [ɒː] | default [ɒː] · word initial [ʔ] |
| ⟨اه⟩ | [ɒːh] |  |
| ⟨ب⟩ | [b] |  |
| ⟨ت⟩ | [t] |  |
| ⟨ث⟩ | [s] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨ح⟩ | [h] |  |
| ⟨خ⟩ | [x] |  |
| ⟨خوا⟩ | [xɒː] |  |
| ⟨خواه⟩ | [xɒːh] |  |
| ⟨د⟩ | [d] |  |
| ⟨ذ⟩ | [z] |  |
| ⟨ر⟩ | [ɾ] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [s] |  |
| ⟨ض⟩ | [z] |  |
| ⟨ط⟩ | [t] |  |
| ⟨ظ⟩ | [z] |  |
| ⟨ع⟩ | [ʔ] |  |
| ⟨غ⟩ | [ɣ] [ɢ] |  |
| ⟨ف⟩ | [f] |  |
| ⟨ق⟩ | [ɣ] [ɢ] |  |
| ⟨ك⟩ | [k] |  |
| ⟨ل⟩ | [l] |  |
| ⟨م⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨ه⟩ | [h] [e] | default [h] · word final [e] [h] |
| ⟨ها⟩ | [hɒː] |  |
| ⟨و⟩ | [v] [uː] [ow] | default [uː] [ow] [v] · word initial [v] |
| ⟨ي⟩ | [j] [iː] | default [iː] [j] · word initial [j] |
| ⟨َ⟩ | [æ] |  |
| ⟨ُ⟩ | [o] |  |
| ⟨ِ⟩ | [e] |  |
| ⟨پ⟩ | [p] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨ژ⟩ | [ʒ] |  |
| ⟨ک⟩ | [k] |  |
| ⟨گ⟩ | [ɡ] |  |
| ⟨ی⟩ | [j] [iː] | default [iː] [j] · word initial [j] |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "fa")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Pennsylvania German](pdc.md) · [Home](../index.md) · [Phalura →](phl.md)
