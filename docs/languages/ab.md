# Abkhaz (`ab`)

<!-- atlas:summary begin -->
Abkhaz is an Abkhaz-Adyge language, written in the Cyrillic script. Glottolog places it in Georgia, Russia and Türkiye. The `ab` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ab` |
| ISO 639-3 | [abk](https://iso639-3.sil.org/code/abk), Abkhazian |
| Glottolog | [abkh1244](https://glottolog.org/resource/languoid/id/abkh1244), Abkhaz |
| Wikidata | [Q5111](https://www.wikidata.org/wiki/Q5111) |
| Wikipedia | [Abkhaz language](https://en.wikipedia.org/wiki/Abkhaz_language) |
| Family | [Abkhaz-Adyge](by-family.md#abkhaz-adyge) |
| Region | [Eurasia](by-region.md#eurasia) > [Georgia](by-region.md#georgia), [Russia](by-region.md#russia), [Türkiye](by-region.md#türkiye) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1862, living |
| Parent | [Abkhaz-Adyge](https://tigregotico.github.io/orthography2ipa/#x-clade-abkh1242) `x-clade-abkh1242` |
| Explorer | [`ab` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ab) |
| Spec file | [`ab.json`](../../orthography2ipa/data/ab.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Abkhaz (аԥсшәа), Northwest Caucasian, written since 1954 in an extended Cyrillic alphabet. INPUT CONTRACT: Cyrillic text in the modern (1954) Abkhaz orthography, Unicode NFC, lowercase folding applied by the engine.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1979 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 67 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ab.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ab` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-begus2021"></a>Beguš, Gašper (2021). *Segmental Phonetics and Phonology in Caucasian languages*. Oxford University Press, in Polinsky (ed.), The Oxford Handbook of Languages of the Caucasus. [doi.org](https://doi.org/10.1093/oxfordhb/9780190690694.013.18)
2. <a id="src-andersson2023"></a>Andersson, Samuel, Vaux, Bert, Pysipa (Şener), Zihni (2023). *Cwyzhy Abkhaz (Illustration of the IPA)*. Journal of the International Phonetic Association 53(1): 266, 286. Cited: 266-286. [doi.org](https://doi.org/10.1017/S0025100320000390)
3. <a id="src-hewitt1979"></a>Hewitt, B. George (1979). *Abkhaz (Lingua Descriptive Studies)*. North-Holland.
4. <a id="src-abkhaz_alphabet_wiki"></a>Wikipedia contributors (2025). *Abkhaz alphabet*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Abkhaz_alphabet)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ab` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 165 | 0.2311 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ab` | generated | epitran-derived | CC0 1.0 | 32180 | 0.1964 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 67 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Pharyngeal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b pʰ pʼ |  | d dʷ tʰ tʷʰ tʷʼ tʼ |  |  |  | kʰ kʲʰ kʲʼ kʷʰ kʷʼ kʼ ɡ ɡʲ ɡʷ | qʲʼ qʷʼ qʼ |  |
| Affricate |  |  | d͡z t͡sʰ t͡sʼ | d͡ʒ t͡ʃʰ t͡ʃʼ | ɖ͡ʐ ʈ͡ʂʰ ʈ͡ʂʼ | d͡ʑʷ t͡ɕʷʰ t͡ɕʷʼ |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʃʷ ʒ ʒʷ | ʂ ʐ | ɕ |  | ʁ ʁʲ ʁʷ χ χʲ χʷ | ħ ħʷ |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ji] [w] [ɥ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨гь⟩ | [ɡʲ] |  |
| ⟨гә⟩ | [ɡʷ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дә⟩ | [dʷ] |  |
| ⟨е⟩ | [e] |  |
| ⟨ж⟩ | [ʐ] |  |
| ⟨жь⟩ | [ʒ] |  |
| ⟨жә⟩ | [ʒʷ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] [ji] [iː] |  |
| ⟨к⟩ | [kʼ] |  |
| ⟨кь⟩ | [kʲʼ] |  |
| ⟨кә⟩ | [kʷʼ] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [pʼ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [tʼ] |  |
| ⟨тә⟩ | [tʷʼ] |  |
| ⟨у⟩ | [w] [u] [uː] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨хь⟩ | [χʲ] |  |
| ⟨хә⟩ | [χʷ] |  |
| ⟨ц⟩ | [t͡sʰ] |  |
| ⟨цә⟩ | [t͡ɕʷʰ] |  |
| ⟨ч⟩ | [t͡ʃʰ] |  |
| ⟨ш⟩ | [ʂ] |  |
| ⟨шь⟩ | [ʃ] |  |
| ⟨шә⟩ | [ʃʷ] |  |
| ⟨ы⟩ | [ə] |  |
| ⟨џ⟩ | [ɖ͡ʐ] |  |
| ⟨џь⟩ | [d͡ʒ] |  |
| ⟨ҕ⟩ | [ʁ] |  |
| ⟨ҕь⟩ | [ʁʲ] |  |
| ⟨қ⟩ | [kʰ] |  |
| ⟨қь⟩ | [kʲʰ] |  |
| ⟨қә⟩ | [kʷʰ] |  |
| ⟨ҟ⟩ | [qʼ] |  |
| ⟨ҟь⟩ | [qʲʼ] |  |
| ⟨ҟә⟩ | [qʷʼ] |  |
| ⟨ҧ⟩ | [pʰ] |  |
| ⟨ҩ⟩ | [ɥ] |  |
| ⟨ҫ⟩ | [ɕ] |  |
| ⟨ҭ⟩ | [tʰ] |  |
| ⟨ҭә⟩ | [tʷʰ] |  |
| ⟨ҳ⟩ | [ħ] |  |
| ⟨ҳә⟩ | [ħʷ] |  |
| ⟨ҵ⟩ | [t͡sʼ] |  |
| ⟨ҵә⟩ | [t͡ɕʷʼ] |  |
| ⟨ҷ⟩ | [t͡ʃʼ] |  |
| ⟨ҽ⟩ | [ʈ͡ʂʰ] |  |
| ⟨ҿ⟩ | [ʈ͡ʂʼ] |  |
| ⟨ӄ⟩ | [kʰ] |  |
| ⟨ӡ⟩ | [d͡z] |  |
| ⟨ӡә⟩ | [d͡ʑʷ] |  |
| ⟨ӷ⟩ | [ʁ] |  |
| ⟨ӷь⟩ | [ʁʲ] |  |
| ⟨ӷә⟩ | [ʁʷ] |  |
| ⟨ԥ⟩ | [pʰ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ab")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← A Fala](fax.md) · [Home](../index.md) · [Abruzzese →](it-IT-x-abruzzo.md)
