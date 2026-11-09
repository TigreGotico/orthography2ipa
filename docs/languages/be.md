# Belarusian (`be`)

<!-- atlas:summary begin -->
Belarusian is an East Slavic language, written in the Cyrillic script. Glottolog places it in 6 countries. The `be` spec is at the research tier. It cites 2 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `be` |
| ISO 639-3 | [bel](https://iso639-3.sil.org/code/bel), Belarusian |
| Glottolog | [bela1254](https://glottolog.org/resource/languoid/id/bela1254), Belarusian |
| Wikidata | [Q9091](https://www.wikidata.org/wiki/Q9091) |
| Wikipedia | [Belarusian language](https://en.wikipedia.org/wiki/Belarusian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > East Slavic](by-family.md#indo-european--balto-slavic--slavic--east-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Belarus](by-region.md#belarus), [Latvia](by-region.md#latvia), [Lithuania](by-region.md#lithuania), [Poland](by-region.md#poland), [Russia](by-region.md#russia), [Ukraine](by-region.md#ukraine) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [East Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-east1426) `x-clade-east1426` |
| Explorer | [`be` in the data explorer](https://tigregotico.github.io/orthography2ipa/#be) |
| Spec file | [`be.json`](../../orthography2ipa/data/be.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Belarusian (Tarashkevitsa/Narkamaŭka). Distinctive features: ⟨г⟩ = [ɣ] (voiced velar fricative, not plosive), ⟨ў⟩ = [w] (unique letter for non-syllabic /w/), pervasive аканне (unstressed /ɔ/ → [a]), яканне (unstressed /ɛ/ → [i] after soft consonants), full affricate writing: ⟨дз⟩ = [dz], ⟨дж⟩ = [dʒ].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1993. [Sources](#sources) lists them. The spec file writes all 110 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/be.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `be` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
2. <a id="src-mayo1993"></a>Mayo, P. (1993). *Belorussian*. in B. Comrie & G. Corbett (eds.), The Slavonic Languages.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `be` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 7229 | 0.0064 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `be` | generated | epitran-derived | CC0 1.0 | 153529 | 0.1276 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 138 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ p pʲ |  | d t |  |  |  | k ɡ |
| Affricate |  |  | dz dzʲ dzʲː dzː ts tsʲ tsʲː tsː | dʒ tʃ |  |  |  |
| Nasal | m mʲ |  | n nʲ nʲː nː |  |  |  | ŋ |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f fʲ v vʲ | s sʲ sʲː sː z zʲ zʲː zː | ʃ ʒ | ʂ ʐ |  | x ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  | l lʲ lʲː lː ɫ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u u̯ |
| Near-close | ɪ |  | ʊ |
| Close-mid | e |  | o |
| Open-mid | ɛ |  | ɔ |
| Near-open |  | ɐ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [bʲa] [bʲe] [bʲi] [bʲo] [bʲu] [dʐ] [fʲa] [fʲe] [fʲi] [fʲo] [fʲu] [iji] [ja] [je] [ji] [jo] [ju] [kʲa] [kʲe] [kʲi] [kʲo] [kʲu] [lʲa] [lʲe] [lʲi] [lʲo] [lʲu] [mʲa] [mʲe] [mʲi] [mʲo] [mʲu] [nʲa] [nʲe] [nʲi] [nʲo] [nʲu] [pʲa] [pʲe] [pʲi], and 36 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ |  |
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] | word final [p] |
| ⟨бе⟩ | [bʲe] |  |
| ⟨бю⟩ | [bʲu] |  |
| ⟨бя⟩ | [bʲa] |  |
| ⟨бё⟩ | [bʲo] |  |
| ⟨бі⟩ | [bʲi] |  |
| ⟨в⟩ | [v] | word final [f] |
| ⟨ве⟩ | [vʲe] |  |
| ⟨вю⟩ | [vʲu] |  |
| ⟨вя⟩ | [vʲa] |  |
| ⟨вё⟩ | [vʲo] |  |
| ⟨ві⟩ | [vʲi] |  |
| ⟨г⟩ | [ɣ] | word final [x] |
| ⟨ге⟩ | [ɣʲe] |  |
| ⟨гю⟩ | [ɣʲu] |  |
| ⟨гя⟩ | [ɣʲa] |  |
| ⟨гё⟩ | [ɣʲo] |  |
| ⟨гі⟩ | [ɣʲi] |  |
| ⟨д⟩ | [d] | word final [t] |
| ⟨дж⟩ | [dʐ] |  |
| ⟨дз⟩ | [dz] |  |
| ⟨дздз⟩ | [dzː] |  |
| ⟨е⟩ | [je] [e] |  |
| ⟨ж⟩ | [ʐ] | word final [ʂ] |
| ⟨з⟩ | [z] | word final [s] |
| ⟨зе⟩ | [zʲe] |  |
| ⟨зз⟩ | [zː] |  |
| ⟨зю⟩ | [zʲu] |  |
| ⟨зя⟩ | [zʲa] |  |
| ⟨зё⟩ | [zʲo] |  |
| ⟨зі⟩ | [zʲi] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨ке⟩ | [kʲe] |  |
| ⟨кю⟩ | [kʲu] |  |
| ⟨кя⟩ | [kʲa] |  |
| ⟨кё⟩ | [kʲo] |  |
| ⟨кі⟩ | [kʲi] |  |
| ⟨л⟩ | [ɫ] |  |
| ⟨ле⟩ | [lʲe] |  |
| ⟨лл⟩ | [lː] |  |
| ⟨ль⟩ | [lʲ] |  |
| ⟨лю⟩ | [lʲu] |  |
| ⟨ля⟩ | [lʲa] |  |
| ⟨лё⟩ | [lʲo] |  |
| ⟨лі⟩ | [lʲi] |  |
| ⟨м⟩ | [m] |  |
| ⟨ме⟩ | [mʲe] |  |
| ⟨мю⟩ | [mʲu] |  |
| ⟨мя⟩ | [mʲa] |  |
| ⟨мё⟩ | [mʲo] |  |
| ⟨мі⟩ | [mʲi] |  |
| ⟨н⟩ | [n] |  |
| ⟨не⟩ | [nʲe] |  |
| ⟨нн⟩ | [nː] |  |
| ⟨ню⟩ | [nʲu] |  |
| ⟨ня⟩ | [nʲa] |  |
| ⟨нё⟩ | [nʲo] |  |
| ⟨ні⟩ | [nʲi] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨пе⟩ | [pʲe] |  |
| ⟨пю⟩ | [pʲu] |  |
| ⟨пя⟩ | [pʲa] |  |
| ⟨пё⟩ | [pʲo] |  |
| ⟨пі⟩ | [pʲi] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨се⟩ | [sʲe] |  |
| ⟨сс⟩ | [sː] |  |
| ⟨сю⟩ | [sʲu] |  |
| ⟨ся⟩ | [sʲa] |  |
| ⟨сё⟩ | [sʲo] |  |
| ⟨сі⟩ | [sʲi] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨фе⟩ | [fʲe] |  |
| ⟨фю⟩ | [fʲu] |  |
| ⟨фя⟩ | [fʲa] |  |
| ⟨фё⟩ | [fʲo] |  |
| ⟨фі⟩ | [fʲi] |  |
| ⟨х⟩ | [x] |  |
| ⟨хе⟩ | [xʲe] |  |
| ⟨хю⟩ | [xʲu] |  |
| ⟨хя⟩ | [xʲa] |  |
| ⟨хё⟩ | [xʲo] |  |
| ⟨хі⟩ | [xʲi] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨це⟩ | [tsʲe] |  |
| ⟨цц⟩ | [tsː] |  |
| ⟨цю⟩ | [tsʲu] |  |
| ⟨ця⟩ | [tsʲa] |  |
| ⟨цё⟩ | [tsʲo] |  |
| ⟨ці⟩ | [tsʲi] |  |
| ⟨ч⟩ | [tʂ] |  |
| ⟨ш⟩ | [ʂ] |  |
| ⟨шч⟩ | [ʂtʂ] |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [ɛ] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨і⟩ | [i] | default [i] · word initial [ji] |
| ⟨іі⟩ | [iji] |  |
| ⟨ў⟩ | [u̯] | default [u̯] · word initial [w] |
| ⟨ґ⟩ | [ɡ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 34 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `BE_REGR_PALAT_s` | /s/ → [sʲ], before [tsʲ] [dzʲ] [nʲ] [sʲ] [zʲ] [lʲ] [bʲ] [vʲ] and 4 more | ⟨адкласці⟩ [atkɫasʲtsʲi] | [Mayo 1993](#src-mayo1993) |
| `BE_REGR_PALAT_z` | /z/ → [zʲ], before [tsʲ] [nʲ] [sʲ] [zʲ] [lʲ] [bʲ] [vʲ] [mʲ] and 3 more | ⟨звер⟩ [zʲvʲer] | [Mayo 1993](#src-mayo1993) |
| `BE_REGR_PALAT_n` | /n/ → [nʲ], before [tsʲ] [dzʲ] [nʲ] [sʲ] [zʲ] [lʲ] | - | [Mayo 1993](#src-mayo1993) |
| `BE_REGR_DEVOICE_b` | /b/ → [p], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 7 more | - | [Mayo 1993](#src-mayo1993) |
| `BE_REGR_DEVOICE_d` | /d/ → [t], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 7 more | ⟨адкласці⟩ [atkɫasʲtsʲi] | [Mayo 1993](#src-mayo1993) |
| `BE_REGR_DEVOICE_ɡ` | /ɡ/ → [k], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 7 more | ⟨адкласці⟩ [atkɫasʲtsʲi] | [Mayo 1993](#src-mayo1993) |
| `BE_REGR_DEVOICE_z` | /z/ → [s], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 7 more | ⟨адкласці⟩ [atkɫasʲtsʲi] | [Mayo 1993](#src-mayo1993) |
| `BE_REGR_DEVOICE_ʐ` | /ʐ/ → [ʂ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 7 more | - | [Mayo 1993](#src-mayo1993) |
| `BE_REGR_DEVOICE_v` | /v/ → [f], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 7 more | - | [Mayo 1993](#src-mayo1993) |
| `BE_REGR_DEVOICE_dz` | /dz/ → [ts], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 7 more | ⟨адкласці⟩ [atkɫasʲtsʲi] | [Mayo 1993](#src-mayo1993) |
| `BE_REGR_DEVOICE_ɣ` | /ɣ/ → [x], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 7 more | - | [Mayo 1993](#src-mayo1993) |
| `BE_PALAT_dz` | /dz/ → [dzʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_ts` | /ts/ → [tsʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_d` | /d/ → [dzʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_t` | /t/ → [tsʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_n` | /n/ → [nʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_ɫ` | /ɫ/ → [lʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_s` | /s/ → [sʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_z` | /z/ → [zʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_b` | /b/ → [bʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_v` | /v/ → [vʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_m` | /m/ → [mʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_p` | /p/ → [pʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_f` | /f/ → [fʲ], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_nː` | /nː/ → [nʲː], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_lː` | /lː/ → [lʲː], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_sː` | /sː/ → [sʲː], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_zː` | /zː/ → [zʲː], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_tsː` | /tsː/ → [tsʲː], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_PALAT_dzː` | /dzː/ → [dzʲː], before [je] [jo] [ju] [ja] [i] | - | - |
| `BE_DEIOTA_je` | /je/ → [e], after [b] [d] [dz] [dzː] [f] [j] [k] [lː] and 20 more | - | - |
| `BE_DEIOTA_jo` | /jo/ → [o], after [b] [d] [dz] [dzː] [f] [j] [k] [lː] and 20 more | - | - |
| `BE_DEIOTA_ju` | /ju/ → [u], after [b] [d] [dz] [dzː] [f] [j] [k] [lː] and 20 more | - | - |
| `BE_DEIOTA_ja` | /ja/ → [a], after [b] [d] [dz] [dzː] [f] [j] [k] [lː] and 20 more | ⟨Дар'я⟩ [darja] | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "be")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Bats](bbl.md) · [Home](../index.md) · [Belsetán Aragonese →](an-x-belsetan.md)
