# Yakut (`sah`)

<!-- atlas:summary begin -->
Yakut is a Turkic language, written in the Cyrillic script. Glottolog places it in Russia. The `sah` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sah` |
| ISO 639-3 | [sah](https://iso639-3.sil.org/code/sah), Yakut |
| Glottolog | [yaku1245](https://glottolog.org/resource/languoid/id/yaku1245), Sakha |
| Wikidata | [Q34299](https://www.wikidata.org/wiki/Q34299) |
| Wikipedia | [Yakut language](https://en.wikipedia.org/wiki/Yakut_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1939, living |
| Parent | [Turkic](https://tigregotico.github.io/orthography2ipa/#x-clade-turk1311) `x-clade-turk1311` |
| Explorer | [`sah` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sah) |
| Spec file | [`sah.json`](../../orthography2ipa/data/sah.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Yakut (Sakha, саха тыла), a Siberian Turkic language of the Sakha Republic, Russia, written since 1939 in an extended Cyrillic alphabet: the Russian letters plus Ҕҕ, Ҥҥ, Өө, Һһ, Үү and the digraphs ⟨дь⟩ /d͡ʒ/ and ⟨нь⟩ /ɲ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2026. 3 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 50 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sah.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sah` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-yakut_language_wiki"></a>Wikipedia contributors (2026). *Yakut language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Yakut_language)
2. <a id="src-yakut_scripts_wiki"></a>Wikipedia contributors (2026). *Yakut scripts*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Yakut_scripts)
3. <a id="src-yakut_alphabet_ipa_wiki"></a>Wikipedia contributors (2026). *Yakut language, Alphabet, Vowels and Consonants (letter-to-IPA table)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Yakut_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sah` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 238 | 0.2492 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `sah` | generated | epitran-derived | CC0 1.0 | 11989 | 0.0862 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 51 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Affricate |  |  | t͡s | d͡ʒ t͡ʃ |  |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕː | ɣ | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː | u uː ɯ ɯː |
| Close-mid | e eː ø øː |  |
| Open-mid |  | ɔ ɔː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [ie] [ja] [je] [jo] [ju] [uɔ] [yø] [ɯa].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨аа⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дь⟩ | [d͡ʒ] |  |
| ⟨е⟩ | [e] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨ии⟩ | [iː] |  |
| ⟨иэ⟩ | [ie] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨о⟩ | [ɔ] |  |
| ⟨оо⟩ | [ɔː] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [ɾ] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨уо⟩ | [uɔ] |  |
| ⟨уу⟩ | [uː] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨ц⟩ | [t͡s] |  |
| ⟨ч⟩ | [t͡ʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕː] |  |
| ⟨ы⟩ | [ɯ] |  |
| ⟨ыа⟩ | [ɯa] |  |
| ⟨ыы⟩ | [ɯː] |  |
| ⟨э⟩ | [e] |  |
| ⟨ээ⟩ | [eː] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ҕ⟩ | [ɣ] [ʁ] |  |
| ⟨ҥ⟩ | [ŋ] |  |
| ⟨ү⟩ | [y] |  |
| ⟨үү⟩ | [yː] |  |
| ⟨үө⟩ | [yø] |  |
| ⟨һ⟩ | [h] |  |
| ⟨ө⟩ | [ø] |  |
| ⟨өө⟩ | [øː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sah")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Xhosa](xh.md) · [Home](../index.md) · [Yao →](yao.md)
