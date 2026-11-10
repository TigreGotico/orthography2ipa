# Mongolian (`mn`)

<!-- atlas:summary begin -->
Mongolian is a Mongolic language, written in the Cyrillic script. Glottolog places it in Mongolia and Russia. The `mn` spec is at the research tier. It cites 2 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mn` |
| ISO 639-3 | [mon](https://iso639-3.sil.org/code/mon), Mongolian |
| Glottolog | [halh1238](https://glottolog.org/resource/languoid/id/halh1238), Halh Mongolian |
| Wikidata | [Q9246](https://www.wikidata.org/wiki/Q9246) |
| Wikipedia | [Mongolian language](https://en.wikipedia.org/wiki/Mongolian_language) |
| Family | [Mongolic](by-family.md#mongolic) |
| Region | [Eurasia](by-region.md#eurasia) > [Mongolia](by-region.md#mongolia), [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1941, living |
| Parent | [Proto-Mongolic (family node)](https://tigregotico.github.io/orthography2ipa/#xgn) `xgn` |
| Explorer | [`mn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mn) |
| Spec file | [`mn.json`](../../orthography2ipa/data/mn.json) |
<!-- atlas:header end -->

## Overview

The `mn` spec describes Khalkha Mongolian in the Cyrillic orthography of Mongolia. The spec does not cover the Traditional Mongolian script under this tag. The description follows Svantesson (2003), "Khalkha", in Janhunen (ed.) *The Mongolic Languages*, which is the spec's `sources` entry.

## Consonants

Khalkha has no voiced obstruents. The laryngeal contrast is strong (aspirated) against weak (plain voiceless unaspirated). So ⟨п т ц ч к⟩ are [pʰ tʰ tsʰ tɕʰ kʰ] and ⟨б д з ж⟩ are [p t ts tɕ].

The weak velar ⟨г⟩ is the one exception. It is functionally voiced [ɡ], voiceless [k] word-finally and before a voiceless consonant, and often the fricative [ɣ] between vowels. ⟨л⟩ is a lateral fricative [ɮ], and ⟨ш⟩ is an alveopalatal [ɕ].

Word-final ⟨н⟩ is /ŋ/. The orthography writes a following vowel letter exactly when the nasal is alveolar. So ⟨хан⟩ 'king' is [xaŋ], against ⟨хана⟩ 'wall' [xan].

| Word | Engine output |
|---|---|
| ⟨гар⟩ | `ɡar` |
| ⟨ногоон⟩ | `nɔɣɔːŋ` |
| ⟨агт⟩ | `aktʰ` |
| ⟨пал⟩ | `pʰaɮ` |
| ⟨хан⟩ | `xaŋ` |
| ⟨хана⟩ | `xana` |

The output for ⟨хана⟩ keeps the final vowel letter (see [Known limits](#known-limits)).

## Vowels

The seven vowels carry pharyngeal (ATR) harmony. The historically back rounded ⟨о у⟩ are pharyngealised [ɔ ʊ]. The historically front rounded ⟨ө ү⟩ are centralised [ɵ u], and ⟨и⟩ is neutral.

A doubled letter writes a long vowel. ⟨й⟩ writes the four diphthongs in -i, and ⟨ий⟩ writes long /iː/. The historical diphthong ⟨эй⟩ has merged with /eː/.

The iotated letters ⟨е ё ю я⟩ write a glide at the start of a word and after a vowel. After a consonant they write palatalisation of that consonant. ⟨е⟩ stands for iotated ö, so it spells /jɵ/. An iotated letter followed by its matching plain vowel letter (⟨яа ёо юу юү еэ⟩) writes one long nucleus, as a doubled plain vowel does. The second letter states the length and the side of the harmony that the nucleus is on: ⟨юу⟩ gives `jʊː` and ⟨юү⟩ gives `juː`.

## The soft and hard signs

Both signs ⟨ь ъ⟩ write palatalisation of the consonant before them: ⟨хорь⟩ gives `xɔrʲ` and ⟨арьс⟩ gives `arʲs`.

Before one of ⟨е ё ю я⟩, the signs are the separating signs of the Russian-derived spelling. They mark a syllable break that the glide of the iotated letter fills, and they add no segment: ⟨объект⟩ gives `ɔpjɵkʰtʰ`, ⟨томьёо⟩ gives `tʰɔmjɔː`, and ⟨харьяалах⟩ gives `xarjaːɮax`.

Svantesson (2003) does not describe the separating spellings, which occur in Russian loans. The reading comes from the WikiPron `mon_cyrl_broad` gold. Most gold words that spell ⟨ь⟩ or ⟨ъ⟩ before an iotated letter show a bare glide with no palatalisation mark, and the result holds for ⟨ь⟩ alone. Two exceptions remain. ⟨харьяа⟩ [xarʲjaː] is palatalised, and its own derivative ⟨харьяалах⟩ [xarjaːɮax] contradicts it. The voluntative forms ⟨идье⟩ [itiː] and ⟨оръё⟩ [ɔriː] spell only a long vowel with no glide. The spec gives `itjɵ` and `ɔrjɔ` for these two, which is a known divergence.

⟨ь⟩ and ⟨ъ⟩ alternate freely in this position. The gold spells some words both ways with the same transcription: ⟨объект⟩ and ⟨обьект⟩ are both [ɔpjɵkʰtʰ], and ⟨авъяас⟩ and ⟨авьяас⟩ are both [aw̜jaːs]. This is evidence that the sign is an allograph here, not the Russian hard and soft contrast.

## Known limits

The short vowel letters of non-initial syllables do not write phonemes. They write reduced schwas, which syllable structure inserts and which are absent from the underlying form. To find out whether a vowel letter is in a non-initial syllable, and whether the consonants around it form a well-formed coda, the engine needs a syllabifier. The engine does not run one for this spec, so the spec does not implement the reduction.

Every short vowel letter therefore keeps its full quality, medial or word-final: ⟨хамар⟩ gives `xamar` and ⟨хана⟩ gives `xana`. This also keeps the only vowel of a CV monosyllable: ⟨би⟩ 'I' gives `pi` and ⟨та⟩ 'you' gives `tʰa`. A plain word-final deletion rule would delete that vowel wrongly, because it is in the initial syllable of the word.

Word prominence is not contrastive, and the literature does not agree on its place. So the spec declares no `stress` block.

## Gold rows

Mongolian Cyrillic is a deep orthography for the purpose of the tiers. The letters record a historical shape of the word from before the reduction, not its surface form. So the 0.25 deep-orthography threshold applies (see [quality tiers](../specs/quality_tiers.md#the-per-threshold)). For the figures, see the [scoreboard](../evaluation/generated/scoreboard.md).

The WikiPron `mon_cyrl_broad` gold (`crowd-scraped`) is a mix of hand-typed Wiktionary IPA and `Module:mn-IPA` output. In a sample of the raw en.wiktionary source, most entries were module output. Part of this row is therefore a reproduction test, not an accuracy test (see [Module-generated WikiPron rows](../evaluation/datasets.md#module-generated-wikipron-rows)). The `vox_communis` row is `epitran-derived`, so it can neither qualify nor block a promotion.

The WikiPron gold is a narrow phonetic transcription. It differs from this spec in the depth of the transcription, not in the phonology:

| Gold convention | Spec |
|---|---|
| The weak velar is [k] in every position, word-initially too | `ɡ`, with `k` word-finally and before a voiceless consonant |
| Final sonorants are devoiced ([r̥], [ɮ̥]) | Not marked |
| ⟨в⟩ is a lowered [w̜] | `w` |
| Half-length is marked | Not marked |
| The epenthetic schwa is written | Not inserted |

The spec never emits these symbols, so they set a floor on the PER that no rule change can recover. The spec keeps [ɡ] at the start of a word, because the source states it, although the gold's [k] would lower the measured PER.

<!-- atlas:lects begin -->
## Related lects

No spec names `mn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-svantesson2003_khalkha"></a>Svantesson, Jan-Olof (2003). *Khalkha*. In Juha Janhunen (ed.), The Mongolic Languages. London: Routledge.
2. <a id="src-mongolian_wiki"></a>Wikipedia contributors (2024). *Mongolian language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Mongolian_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 3528 | 0.1557 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `mn` | generated | epitran-derived | CC0 1.0 | 15592 | 0.2077 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 64 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  | t tʰ |  | k kʰ ɡ |
| Affricate |  |  | ts tsʰ | tɕ tɕʰ |  |
| Nasal | m |  | n |  | ŋ |
| Trill |  |  | r |  |  |
| Fricative |  | f | s | ɕ | x ɣ |
| Lateral fricative |  |  | ɮ |  |  |
| Approximant |  |  |  | j |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː ʲu ʲuː |
| Near-close |  |  | ʊ ʊː ʲʊ ʲʊː |
| Close-mid | e eː ʲe ʲeː | ɵ ɵː ʲɵ |  |
| Open-mid |  |  | ɔ ɔː ʲɔ ʲɔː |
| Open | a aː ʲa ʲaː |  |  |

Sequences that the spec writes as one unit: [ai] [ja] [jaː] [je] [jeː] [ju] [juː] [jɔ] [jɔː] [jɵ] [jʊ] [jʊː] [ui] [w] [ɔi] [ʊi] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] | default [a] · word initial [a] |
| ⟨аа⟩ | [aː] |  |
| ⟨ай⟩ | [ai] |  |
| ⟨б⟩ | [p] |  |
| ⟨в⟩ | [w] |  |
| ⟨г⟩ | [ɡ] [ɣ] | default [ɡ] · intervocalic [ɣ] · word final [k] |
| ⟨д⟩ | [t] |  |
| ⟨е⟩ | [jɵ] [je] | after consonant [ʲɵ] [ʲe] · default [jɵ] [je] |
| ⟨еэ⟩ | [jeː] | after consonant [ʲeː] · default [jeː] |
| ⟨ж⟩ | [tɕ] |  |
| ⟨з⟩ | [ts] |  |
| ⟨и⟩ | [i] | default [i] · word initial [i] |
| ⟨ий⟩ | [iː] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [kʰ] |  |
| ⟨л⟩ | [ɮ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] | default [n] · word final [ŋ] |
| ⟨о⟩ | [ɔ] | default [ɔ] · word initial [ɔ] |
| ⟨ой⟩ | [ɔi] |  |
| ⟨оо⟩ | [ɔː] |  |
| ⟨п⟩ | [pʰ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [tʰ] |  |
| ⟨у⟩ | [ʊ] | default [ʊ] · word initial [ʊ] |
| ⟨уй⟩ | [ʊi] |  |
| ⟨уу⟩ | [ʊː] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [tsʰ] |  |
| ⟨ч⟩ | [tɕʰ] |  |
| ⟨ш⟩ | [ɕ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | [ʲ] |  |
| ⟨ъе⟩ | [jɵ] [je] |  |
| ⟨ъеэ⟩ | [jeː] |  |
| ⟨ъю⟩ | [jʊ] |  |
| ⟨ъюу⟩ | [jʊː] |  |
| ⟨ъюү⟩ | [juː] |  |
| ⟨ъя⟩ | [ja] |  |
| ⟨ъяа⟩ | [jaː] |  |
| ⟨ъё⟩ | [jɔ] |  |
| ⟨ъёо⟩ | [jɔː] |  |
| ⟨ы⟩ | [i] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨ье⟩ | [jɵ] [je] |  |
| ⟨ьеэ⟩ | [jeː] |  |
| ⟨ью⟩ | [jʊ] |  |
| ⟨ьюу⟩ | [jʊː] |  |
| ⟨ьюү⟩ | [juː] |  |
| ⟨ья⟩ | [ja] |  |
| ⟨ьяа⟩ | [jaː] |  |
| ⟨ьё⟩ | [jɔ] |  |
| ⟨ьёо⟩ | [jɔː] |  |
| ⟨э⟩ | [e] | default [e] · word initial [e] |
| ⟨эй⟩ | [eː] |  |
| ⟨ээ⟩ | [eː] |  |
| ⟨ю⟩ | [jʊ] [ju] | after consonant [ʲʊ] [ʲu] · default [jʊ] [ju] |
| ⟨юу⟩ | [jʊː] | after consonant [ʲʊː] · default [jʊː] |
| ⟨юү⟩ | [juː] | after consonant [ʲuː] · default [juː] |
| ⟨я⟩ | [ja] | after consonant [ʲa] · default [ja] |
| ⟨яа⟩ | [jaː] | after consonant [ʲaː] · default [jaː] |
| ⟨ё⟩ | [jɔ] | after consonant [ʲɔ] · default [jɔ] |
| ⟨ёо⟩ | [jɔː] | after consonant [ʲɔː] · default [jɔː] |
| ⟨ү⟩ | [u] | default [u] · word initial [u] |
| ⟨үй⟩ | [ui] |  |
| ⟨үү⟩ | [uː] |  |
| ⟨ө⟩ | [ɵ] | default [ɵ] · word initial [ɵ] |
| ⟨өө⟩ | [ɵː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 3 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `MN_N_VELAR_ASSIM` | /n/ → [ŋ], before [ɡ] [k] [x] [ɣ] [kʰ] | ⟨möngg⟩ [mɵŋɡ] | [Svantesson 2003](#src-svantesson2003_khalkha) |
| `MN_N_LABIAL_ASSIM` | /n/ → [m], before [p] [pʰ] [m] [w] | ⟨möngg⟩ [mɵŋɡ] | [Svantesson 2003](#src-svantesson2003_khalkha) |
| `MN_WEAK_VELAR_DEVOICE` | /ɡ/ → [k], before [pʰ] [tʰ] [tsʰ] [tɕʰ] [kʰ] [p] [t] [ts] and 4 more | ⟨п т ц ч к⟩ [pʰ tʰ tsʰ tɕʰ kʰ] | [Svantesson 2003](#src-svantesson2003_khalkha) |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="харьяа|харьяалах|идье|оръё|хана|гар|арьс|ногоон|томьёо|объект|хамар|юу" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mn")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| харьяа | [xarjaː] |
| харьяалах | [xarjaːɮax] |
| идье | [itjɵ] |
| оръё | [ɔrjɔ] |
| хана | [xana] |
| гар | [ɡar] |
| арьс | [arʲs] |
| ногоон | [nɔɣɔːŋ] |
| томьёо | [tʰɔmjɔː] |
| объект | [ɔpjɵkʰtʰ] |
| хамар | [xamar] |
| юу | [jʊː] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Moksha](mdf.md) · [Home](../index.md) · [Mooré →](mos.md)
