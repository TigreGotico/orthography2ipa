# Cree (`cr`)

<!-- atlas:summary begin -->
Cree is an Algic language, written in the Canadian Aboriginal Syllabics script. Glottolog places it in the North America macroarea. The `cr` spec is at the research tier. It cites 6 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `cr` |
| ISO 639-3 | [cre](https://iso639-3.sil.org/code/cre), Cree |
| Glottolog | [cree1271](https://glottolog.org/resource/languoid/id/cree1271), Cree-Montagnais-Naskapi |
| Wikidata | [Q33390](https://www.wikidata.org/wiki/Q33390) |
| Wikipedia | [Cree language](https://en.wikipedia.org/wiki/Cree_language) |
| Family | [Algic](by-family.md#algic) |
| Region | [North America](by-region.md#north-america) |
| Script | [Canadian Aboriginal Syllabics](by-script.md#canadian-aboriginal-syllabics) (syllabary) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1840, living |
| Parent | [Algic](https://tigregotico.github.io/orthography2ipa/#x-clade-algi1248) `x-clade-algi1248` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`cr` in the data explorer](https://tigregotico.github.io/orthography2ipa/#cr) |
| Spec file | [`cr.json`](../../orthography2ipa/data/cr.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cree (ᓀᐦᐃᔭᐍᐏᐣ). INPUT CONTRACT: WESTERN CREE SYLLABICS (Unified Canadian Aboriginal Syllabics, U+1400..U+167F, NFC). The Standard Roman Orthography (SRO) is a separate, Latin input and is NOT covered by this map.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 6 works, from 1996 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 222 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/cr.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `cr` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Plains Cree](crk.md) `crk`: research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 5 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-cree_wiki"></a>Wikipedia contributors (2024). *Cree language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Cree_language)
2. <a id="src-wolfart1996"></a>Wolfart, H. Christoph (1996). *Sketch of Cree, an Algonquian Language*. Handbook of North American Indians, Vol. 17 (Smithsonian Institution).
3. <a id="src-western_cree_syllabics_wiki"></a>Wikipedia contributors (2026). *Western Cree syllabics*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Western_Cree_syllabics)
4. <a id="src-starks_ballard2005"></a>Starks, Donna & Ballard, Elaine (2005). *Woods Cree /ð/: An Unusual Type of Sonorant*. International Journal of American Linguistics 71(1). Cited: 102-115. [doi.org](https://doi.org/10.1086/430580)
5. <a id="src-algonquian_atlas_plains_cree"></a>Algonquian Linguistic Atlas (2020). *Plains Cree: Sounds, Consonants and Vowels*. Algonquian Linguistic Atlas. [plainscree.atlas-ling.ca](https://plainscree.atlas-ling.ca/grammar/sounds/vowels/)
6. <a id="src-unicode_cas_chart"></a>The Unicode Consortium (2024). *Unified Canadian Aboriginal Syllabics (Unicode code chart U+1400..U+167F)*. Unicode Consortium. [unicode.org](https://www.unicode.org/charts/PDF/U1400.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 153 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Dental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t |  | k | ʔ |
| Affricate |  |  | ts |  |  |  |
| Nasal | m |  | n |  |  |  |
| Fricative |  | ð | s |  |  | h |
| Approximant |  |  | ɹ | j |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | iː |  |
| Near-close | ɪ |  |
| Close-mid | eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [hk] [ja] [jaː] [jeː] [jiː] [jo] [joː] [jwa] [jwaː] [jweː] [jwiː] [jwo] [jwoː] [jwɪ] [jɪ] [ka] [kaː] [keː] [kiː] [ko] [koː] [kw] [kwa] [kwaː] [kweː] [kwiː] [kwo] [kwoː] [kwɪ] [kɪ] [ma] [maː] [meː] [miː] [mo] [moː] [mwa] [mwaː] [mweː] [mwiː], and 93 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ᐁ⟩ | [eː] |  |
| ⟨ᐃ⟩ | [ɪ] |  |
| ⟨ᐄ⟩ | [iː] |  |
| ⟨ᐅ⟩ | [o] |  |
| ⟨ᐆ⟩ | [oː] |  |
| ⟨ᐊ⟩ | [a] |  |
| ⟨ᐋ⟩ | [aː] |  |
| ⟨ᐌ⟩ | [weː] |  |
| ⟨ᐍ⟩ | [weː] |  |
| ⟨ᐎ⟩ | [wɪ] |  |
| ⟨ᐏ⟩ | [wɪ] |  |
| ⟨ᐐ⟩ | [wiː] |  |
| ⟨ᐑ⟩ | [wiː] |  |
| ⟨ᐒ⟩ | [wo] |  |
| ⟨ᐓ⟩ | [wo] |  |
| ⟨ᐔ⟩ | [woː] |  |
| ⟨ᐕ⟩ | [woː] |  |
| ⟨ᐗ⟩ | [wa] |  |
| ⟨ᐘ⟩ | [wa] |  |
| ⟨ᐙ⟩ | [waː] |  |
| ⟨ᐚ⟩ | [waː] |  |
| ⟨ᐝ⟩ | [j] |  |
| ⟨ᐞ⟩ | [ʔ] |  |
| ⟨ᐟ⟩ | [t] |  |
| ⟨ᐠ⟩ | [k] |  |
| ⟨ᐢ⟩ | [s] |  |
| ⟨ᐣ⟩ | [n] |  |
| ⟨ᐤ⟩ | [w] |  |
| ⟨ᐦ⟩ | [h] |  |
| ⟨ᐧ⟩ | [w] |  |
| ⟨ᐨ⟩ | [ts] |  |
| ⟨ᐯ⟩ | [peː] |  |
| ⟨ᐱ⟩ | [pɪ] |  |
| ⟨ᐲ⟩ | [piː] |  |
| ⟨ᐳ⟩ | [po] |  |
| ⟨ᐴ⟩ | [poː] |  |
| ⟨ᐸ⟩ | [pa] |  |
| ⟨ᐹ⟩ | [paː] |  |
| ⟨ᐺ⟩ | [pweː] |  |
| ⟨ᐻ⟩ | [pweː] |  |
| ⟨ᐼ⟩ | [pwɪ] |  |
| ⟨ᐽ⟩ | [pwɪ] |  |
| ⟨ᐾ⟩ | [pwiː] |  |
| ⟨ᐿ⟩ | [pwiː] |  |
| ⟨ᑀ⟩ | [pwo] |  |
| ⟨ᑁ⟩ | [pwo] |  |
| ⟨ᑂ⟩ | [pwoː] |  |
| ⟨ᑃ⟩ | [pwoː] |  |
| ⟨ᑄ⟩ | [pwa] |  |
| ⟨ᑅ⟩ | [pwa] |  |
| ⟨ᑆ⟩ | [pwaː] |  |
| ⟨ᑇ⟩ | [pwaː] |  |
| ⟨ᑉ⟩ | [p] |  |
| ⟨ᑊ⟩ | [p] |  |
| ⟨ᑌ⟩ | [teː] |  |
| ⟨ᑎ⟩ | [tɪ] |  |
| ⟨ᑏ⟩ | [tiː] |  |
| ⟨ᑐ⟩ | [to] |  |
| ⟨ᑑ⟩ | [toː] |  |
| ⟨ᑕ⟩ | [ta] |  |
| ⟨ᑖ⟩ | [taː] |  |
| ⟨ᑗ⟩ | [tweː] |  |
| ⟨ᑘ⟩ | [tweː] |  |
| ⟨ᑙ⟩ | [twɪ] |  |
| ⟨ᑚ⟩ | [twɪ] |  |
| ⟨ᑛ⟩ | [twiː] |  |
| ⟨ᑜ⟩ | [twiː] |  |
| ⟨ᑝ⟩ | [two] |  |
| ⟨ᑞ⟩ | [two] |  |
| ⟨ᑟ⟩ | [twoː] |  |
| ⟨ᑠ⟩ | [twoː] |  |
| ⟨ᑡ⟩ | [twa] |  |
| ⟨ᑢ⟩ | [twa] |  |
| ⟨ᑣ⟩ | [twaː] |  |
| ⟨ᑤ⟩ | [twaː] |  |
| ⟨ᑦ⟩ | [t] |  |
| ⟨ᑫ⟩ | [keː] |  |
| ⟨ᑭ⟩ | [kɪ] |  |
| ⟨ᑮ⟩ | [kiː] |  |
| ⟨ᑯ⟩ | [ko] |  |
| ⟨ᑰ⟩ | [koː] |  |
| ⟨ᑲ⟩ | [ka] |  |
| ⟨ᑳ⟩ | [kaː] |  |
| ⟨ᑴ⟩ | [kweː] |  |
| ⟨ᑵ⟩ | [kweː] |  |
| ⟨ᑶ⟩ | [kwɪ] |  |
| ⟨ᑷ⟩ | [kwɪ] |  |
| ⟨ᑸ⟩ | [kwiː] |  |
| ⟨ᑹ⟩ | [kwiː] |  |
| ⟨ᑺ⟩ | [kwo] |  |
| ⟨ᑻ⟩ | [kwo] |  |
| ⟨ᑼ⟩ | [kwoː] |  |
| ⟨ᑽ⟩ | [kwoː] |  |
| ⟨ᑾ⟩ | [kwa] |  |
| ⟨ᑿ⟩ | [kwa] |  |
| ⟨ᒀ⟩ | [kwaː] |  |
| ⟨ᒁ⟩ | [kwaː] |  |
| ⟨ᒃ⟩ | [k] |  |
| ⟨ᒄ⟩ | [kw] |  |
| ⟨ᒉ⟩ | [tseː] |  |
| ⟨ᒋ⟩ | [tsɪ] |  |
| ⟨ᒌ⟩ | [tsiː] |  |
| ⟨ᒍ⟩ | [tso] |  |
| ⟨ᒎ⟩ | [tsoː] |  |
| ⟨ᒐ⟩ | [tsa] |  |
| ⟨ᒑ⟩ | [tsaː] |  |
| ⟨ᒒ⟩ | [tsweː] |  |
| ⟨ᒓ⟩ | [tsweː] |  |
| ⟨ᒔ⟩ | [tswɪ] |  |
| ⟨ᒕ⟩ | [tswɪ] |  |
| ⟨ᒖ⟩ | [tswiː] |  |
| ⟨ᒗ⟩ | [tswiː] |  |
| ⟨ᒘ⟩ | [tswo] |  |
| ⟨ᒙ⟩ | [tswo] |  |
| ⟨ᒚ⟩ | [tswoː] |  |
| ⟨ᒛ⟩ | [tswoː] |  |
| ⟨ᒜ⟩ | [tswa] |  |
| ⟨ᒝ⟩ | [tswa] |  |
| ⟨ᒞ⟩ | [tswaː] |  |
| ⟨ᒟ⟩ | [tswaː] |  |
| ⟨ᒡ⟩ | [ts] |  |
| ⟨ᒣ⟩ | [meː] |  |
| ⟨ᒥ⟩ | [mɪ] |  |
| ⟨ᒦ⟩ | [miː] |  |
| ⟨ᒧ⟩ | [mo] |  |
| ⟨ᒨ⟩ | [moː] |  |
| ⟨ᒪ⟩ | [ma] |  |
| ⟨ᒫ⟩ | [maː] |  |
| ⟨ᒬ⟩ | [mweː] |  |
| ⟨ᒭ⟩ | [mweː] |  |
| ⟨ᒮ⟩ | [mwɪ] |  |
| ⟨ᒯ⟩ | [mwɪ] |  |
| ⟨ᒰ⟩ | [mwiː] |  |
| ⟨ᒱ⟩ | [mwiː] |  |
| ⟨ᒲ⟩ | [mwo] |  |
| ⟨ᒳ⟩ | [mwo] |  |
| ⟨ᒴ⟩ | [mwoː] |  |
| ⟨ᒵ⟩ | [mwoː] |  |
| ⟨ᒶ⟩ | [mwa] |  |
| ⟨ᒷ⟩ | [mwa] |  |
| ⟨ᒸ⟩ | [mwaː] |  |
| ⟨ᒹ⟩ | [mwaː] |  |
| ⟨ᒻ⟩ | [m] |  |
| ⟨ᒼ⟩ | [m] |  |
| ⟨ᓀ⟩ | [neː] |  |
| ⟨ᓂ⟩ | [nɪ] |  |
| ⟨ᓃ⟩ | [niː] |  |
| ⟨ᓄ⟩ | [no] |  |
| ⟨ᓅ⟩ | [noː] |  |
| ⟨ᓇ⟩ | [na] |  |
| ⟨ᓈ⟩ | [naː] |  |
| ⟨ᓉ⟩ | [nweː] |  |
| ⟨ᓊ⟩ | [nweː] |  |
| ⟨ᓋ⟩ | [nwa] |  |
| ⟨ᓌ⟩ | [nwa] |  |
| ⟨ᓍ⟩ | [nwaː] |  |
| ⟨ᓎ⟩ | [nwaː] |  |
| ⟨ᓐ⟩ | [n] |  |
| ⟨ᓬ⟩ | [l] |  |
| ⟨ᓭ⟩ | [seː] |  |
| ⟨ᓯ⟩ | [sɪ] |  |
| ⟨ᓰ⟩ | [siː] |  |
| ⟨ᓱ⟩ | [so] |  |
| ⟨ᓲ⟩ | [soː] |  |
| ⟨ᓴ⟩ | [sa] |  |
| ⟨ᓵ⟩ | [saː] |  |
| ⟨ᓶ⟩ | [sweː] |  |
| ⟨ᓷ⟩ | [sweː] |  |
| ⟨ᓸ⟩ | [swɪ] |  |
| ⟨ᓹ⟩ | [swɪ] |  |
| ⟨ᓺ⟩ | [swiː] |  |
| ⟨ᓻ⟩ | [swiː] |  |
| ⟨ᓼ⟩ | [swo] |  |
| ⟨ᓽ⟩ | [swo] |  |
| ⟨ᓾ⟩ | [swoː] |  |
| ⟨ᓿ⟩ | [swoː] |  |
| ⟨ᔀ⟩ | [swa] |  |
| ⟨ᔁ⟩ | [swa] |  |
| ⟨ᔂ⟩ | [swaː] |  |
| ⟨ᔃ⟩ | [swaː] |  |
| ⟨ᔅ⟩ | [s] |  |
| ⟨ᔦ⟩ | [jeː] |  |
| ⟨ᔨ⟩ | [jɪ] |  |
| ⟨ᔩ⟩ | [jiː] |  |
| ⟨ᔪ⟩ | [jo] |  |
| ⟨ᔫ⟩ | [joː] |  |
| ⟨ᔭ⟩ | [ja] |  |
| ⟨ᔮ⟩ | [jaː] |  |
| ⟨ᔯ⟩ | [jweː] |  |
| ⟨ᔰ⟩ | [jweː] |  |
| ⟨ᔱ⟩ | [jwɪ] |  |
| ⟨ᔲ⟩ | [jwɪ] |  |
| ⟨ᔳ⟩ | [jwiː] |  |
| ⟨ᔴ⟩ | [jwiː] |  |
| ⟨ᔵ⟩ | [jwo] |  |
| ⟨ᔶ⟩ | [jwo] |  |
| ⟨ᔷ⟩ | [jwoː] |  |
| ⟨ᔸ⟩ | [jwoː] |  |
| ⟨ᔹ⟩ | [jwa] |  |
| ⟨ᔺ⟩ | [jwa] |  |
| ⟨ᔻ⟩ | [jwaː] |  |
| ⟨ᔼ⟩ | [jwaː] |  |
| ⟨ᔾ⟩ | [j] |  |
| ⟨ᕀ⟩ | [j] |  |
| ⟨ᕒ⟩ | [ɹ] |  |
| ⟨ᕽ⟩ | [hk] |  |
| ⟨ᖊ⟩ | [ɹeː] |  |
| ⟨ᖋ⟩ | [ɹɪ] |  |
| ⟨ᖌ⟩ | [ɹo] |  |
| ⟨ᖍ⟩ | [ɹa] |  |
| ⟨ᖧ⟩ | [ðeː] |  |
| ⟨ᖨ⟩ | [ðɪ] |  |
| ⟨ᖩ⟩ | [ðiː] |  |
| ⟨ᖪ⟩ | [ðo] |  |
| ⟨ᖫ⟩ | [ðoː] |  |
| ⟨ᖬ⟩ | [ða] |  |
| ⟨ᖭ⟩ | [ðaː] |  |
| ⟨ᙾ⟩ | [ð] |  |
| ⟨ᣆ⟩ | [nwɪ] |  |
| ⟨ᣈ⟩ | [nwiː] |  |
| ⟨ᣊ⟩ | [nwo] |  |
| ⟨ᣌ⟩ | [nwoː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "cr")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Corsican](co.md) · [Home](../index.md) · [Crimean Tatar →](crh.md)
