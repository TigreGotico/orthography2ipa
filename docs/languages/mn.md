# Mongolian (Khalkha, Cyrillic script): `mn`

**Code**: `mn` | **Family**: Mongolic | **Script**: Cyrillic (alphabet) | **Quality tier**: research

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

---
[← Assamese](as.md) · [Home](../index.md) · [Basque (Euskara) and its dialects →](eu.md)
