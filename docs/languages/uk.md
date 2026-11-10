# Ukrainian (`uk`)

<!-- atlas:summary begin -->
Ukrainian is an East Slavic language, written in the Cyrillic script. Glottolog places it in 8 countries. The `uk` spec is at the research tier. It cites 4 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `uk` |
| Aliases | `ukr` |
| ISO 639-3 | [ukr](https://iso639-3.sil.org/code/ukr), Ukrainian |
| Glottolog | [ukra1253](https://glottolog.org/resource/languoid/id/ukra1253), Ukrainian |
| Wikidata | [Q8798](https://www.wikidata.org/wiki/Q8798) |
| Wikipedia | [Ukrainian language](https://en.wikipedia.org/wiki/Ukrainian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > East Slavic](by-family.md#indo-european--balto-slavic--slavic--east-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Belarus](by-region.md#belarus), [Hungary](by-region.md#hungary), [Moldova](by-region.md#moldova), [Poland](by-region.md#poland), [Romania](by-region.md#romania), [Russia](by-region.md#russia), [Slovakia](by-region.md#slovakia), [Ukraine](by-region.md#ukraine) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [East Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-east1426) `x-clade-east1426` |
| Explorer | [`uk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#uk) |
| Spec file | [`uk.json`](../../orthography2ipa/data/uk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Ukrainian. Key differences from Russian: ⟨г⟩ = [ɦ] (not [ɡ]), ⟨ґ⟩ = [ɡ] as separate letter, ⟨в⟩ = [ʋ] approximant, no vowel reduction (no аканье).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1993 to 2017. [Sources](#sources) lists them. The spec file writes all 45 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/uk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `uk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
2. <a id="src-shevelov1993"></a>Shevelov, G.Y. (1993). *Ukrainian*. in B. Comrie & G. Corbett (eds.), The Slavonic Languages.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
4. <a id="src-pompino2017"></a>Pompino-Marschall, B., Pashchenko, E. & Mołczanow, J. (2017). *Ukrainian (Illustrations of the IPA)*. Journal of the International Phonetic Association 47(3), 349-357. Cited: 349-357. [doi.org](https://doi.org/10.1017/S0025100316000372)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `primary_sources` | `uk` | gold | expert-human | Apache-2.0 (this repository). Each row quotes and cites a published example. | 45 | 0.0759 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `uk` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 51646 | 0.0992 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `uk` | generated | epitran-derived | CC0 1.0 | 51621 | 0.2672 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 75 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ p pʲ |  | d dʲ dʲː dː t tʲ tʲː tː |  |  | k kʲ ɡ ɡʲ |  |
| Affricate |  |  | ts tsʲ tsʲː tsː | tʃ |  |  |  |
| Nasal | m mʲ |  | n nʲ nʲː nː |  |  | ŋ |  |
| Trill |  |  | r rʲ rʲː rː |  |  |  |  |
| Fricative |  | f fʲ | s sʲ sʲː sː z zʲ zʲː zː | ʃ ʒ |  | x xʲ | ɦ ɦʲ |
| Approximant |  | ʋ ʋʲ |  |  | j |  |  |
| Lateral approximant |  |  | l lʲ lʲː ɫ ɫː |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i i̯ |  | u u̯ |
| Near-close | ɪ |  | ʊ |
| Close-mid | e |  |  |
| Open-mid | ɛ |  | ɔ |
| Near-open |  | ɐ |  |
| Open | a |  | ɑ |

Sequences that the spec writes as one unit: [ja] [ji] [ju] [jɛ] [w] [ʃtʃ] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ |  |
| ⟨ʼ⟩ | ∅ |  |
| ⟨а⟩ | [a] | posttonic [ɐ] · pretonic [ɐ] |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [ʋ] | before consonant [u̯] · before o [w] · before u [w] · default [ʋ] · word final [u̯] |
| ⟨г⟩ | [ɦ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дд⟩ | [dː] |  |
| ⟨е⟩ | [ɛ] | posttonic [e] · pretonic [e] |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨зз⟩ | [zː] |  |
| ⟨и⟩ | [ɪ] | posttonic [e] · pretonic [e] |
| ⟨й⟩ | [j] | after vowel [i̯] · default [j] |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [ɫ] |  |
| ⟨лл⟩ | [ɫː] |  |
| ⟨ль⟩ | [lʲ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нн⟩ | [nː] |  |
| ⟨о⟩ | [ɔ] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨рр⟩ | [rː] |  |
| ⟨с⟩ | [s] |  |
| ⟨сс⟩ | [sː] |  |
| ⟨т⟩ | [t] |  |
| ⟨тт⟩ | [tː] |  |
| ⟨у⟩ | [u] | posttonic [ʊ] · pretonic [ʊ] |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨цц⟩ | [tsː] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃtʃ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨є⟩ | [jɛ] |  |
| ⟨і⟩ | [i] |  |
| ⟨ї⟩ | [ji] |  |
| ⟨ґ⟩ | [ɡ] |  |
| ⟨’⟩ | ∅ |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 43 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `UK_ASSIM_PALAT_d` | /d/ → [dʲ], before [b] [d] [dz] [f] [k] [m] [n] [p] and 10 more, with more context in the spec | ⟨Індія⟩ [inʲˈdʲijɐ] | - |
| `UK_ASSIM_PALAT_t` | /t/ → [tʲ], before [b] [d] [dz] [f] [k] [m] [n] [p] and 10 more, with more context in the spec | - | - |
| `UK_ASSIM_PALAT_z` | /z/ → [zʲ], before [b] [d] [dz] [f] [k] [m] [n] [p] and 10 more, with more context in the spec | - | - |
| `UK_ASSIM_PALAT_s` | /s/ → [sʲ], before [b] [d] [dz] [f] [k] [m] [n] [p] and 10 more, with more context in the spec | - | - |
| `UK_ASSIM_PALAT_ts` | /ts/ → [tsʲ], before [b] [d] [dz] [f] [k] [m] [n] [p] and 10 more, with more context in the spec | - | - |
| `UK_ASSIM_PALAT_ɫ` | /ɫ/ → [lʲ], before [b] [d] [dz] [f] [k] [m] [n] [p] and 10 more, with more context in the spec | - | - |
| `UK_ASSIM_PALAT_n` | /n/ → [nʲ], before [b] [d] [dz] [f] [k] [m] [n] [p] and 10 more, with more context in the spec | ⟨Індія⟩ [inʲˈdʲijɐ] | - |
| `UK_PALAT_nː` | /nː/ → [nʲː], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | ⟨знання⟩ [znɐˈnʲːɑ] | - |
| `UK_PALAT_ɫː` | /ɫː/ → [lʲː], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_dː` | /dː/ → [dʲː], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_tː` | /tː/ → [tʲː], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | ⟨життя⟩ [ʒɪˈtʲːɑ] | - |
| `UK_PALAT_zː` | /zː/ → [zʲː], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_sː` | /sː/ → [sʲː], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_tsː` | /tsː/ → [tsʲː], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_rː` | /rː/ → [rʲː], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_b` | /b/ → [bʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_ʋ` | /ʋ/ → [ʋʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_ɦ` | /ɦ/ → [ɦʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_ɡ` | /ɡ/ → [ɡʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_d` | /d/ → [dʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_z` | /z/ → [zʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_k` | /k/ → [kʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_ɫ` | /ɫ/ → [lʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_l` | /l/ → [lʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_m` | /m/ → [mʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_n` | /n/ → [nʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_p` | /p/ → [pʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_r` | /r/ → [rʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_s` | /s/ → [sʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_t` | /t/ → [tʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_f` | /f/ → [fʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_x` | /x/ → [xʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_PALAT_ts` | /ts/ → [tsʲ], before [ji] [jɛ] [ja] [ju] [jo] [j] [i] [ʲ] | - | - |
| `UK_DEIOTA_jɛ` | /jɛ/ → [ɛ], after [b] [d] [dː] [f] [j] [k] [m] [n] and 19 more | - | - |
| `UK_DEIOTA_ja` | /ja/ → [a], after [b] [d] [dː] [f] [j] [k] [m] [n] and 19 more | ⟨дядько⟩ [ˈdʲadʲko] | - |
| `UK_DEIOTA_ji` | /ji/ → [i], after [b] [d] [dː] [f] [j] [k] [m] [n] and 19 more | - | - |
| `UK_SOFT_SIGN_SILENT` | /ʲ/ → ∅, after [b] [d] [f] [j] [k] [m] [n] [p] and 11 more | - | - |
| `UK_DEIOTA_ju` | /ju/ → [u], after [b] [d] [dː] [f] [j] [k] [m] [n] and 19 more | - | - |
| `UK_REGR_PALAT_s` | /s/ → [sʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tsʲ] [bʲ] and 5 more | ⟨кістка⟩ [kʲisʲtʲkɐ] | [Pompino-Marschall 2017](#src-pompino2017), Pashchenko & Mołczanow 2017 |
| `UK_REGR_PALAT_z` | /z/ → [zʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tsʲ] [bʲ] and 5 more | ⟨звер⟩ [zʲvʲer] | [Pompino-Marschall 2017](#src-pompino2017), Pashchenko & Mołczanow 2017 |
| `UK_REGR_PALAT_n` | /n/ → [nʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tsʲ] | - | [Pompino-Marschall 2017](#src-pompino2017), Pashchenko & Mołczanow 2017 |
| `UK_REGR_PALAT_t` | /t/ → [tʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tsʲ] | ⟨кістка⟩ [kʲisʲtʲkɐ] | [Pompino-Marschall 2017](#src-pompino2017), Pashchenko & Mołczanow 2017 |
| `UK_REGR_PALAT_d` | /d/ → [dʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tsʲ] | - | [Pompino-Marschall 2017](#src-pompino2017), Pashchenko & Mołczanow 2017 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "uk")`. They are engine output, not reference transcriptions.

The next table sets the engine output against worked examples printed in a cited source, from the [primary-source gold](../evaluation/datasets.md#primary-source-gold-primary_sources). The rows are spread evenly over that set. The last column says whether the two transcriptions are the same string.

| Spelling | Printed in the source | Engine output | Source, page | Same |
|:--|:--|:--|:--|:--|
| паз | paz | [ˈpaz] | Pompino-Marschall 2017, p. 351 | no |
| білий | ˈbʲiɫɪi̯ | [ˈbʲiɫei̯] | Pompino-Marschall 2017, p. 351 | no |
| ладь | ɫadʲ | [ˈɫadʲ] | Pompino-Marschall 2017, p. 351 | no |
| ґільотина | ɡʲilʲɔˈtɪna | [ɡʲilʲɔˈtɪnɐ] | Pompino-Marschall 2017, p. 351 | no |
| стань | stanʲ | [ˈstanʲ] | Pompino-Marschall 2017, p. 351 | no |
| рис | rɪs | [ˈrɪs] | Pompino-Marschall 2017, p. 351 | no |
| шар | ʃar | [ˈʃar] | Pompino-Marschall 2017, p. 351 | no |
| хай | xai̯ | [ˈxai̯] | Pompino-Marschall 2017, p. 351 | no |
| цеп | t͡sɛp | [ˈtsɛp] | Pompino-Marschall 2017, p. 351 | no |
| дзюрчати | d͡zʲurˈt͡ʃatɪ | [dʲzʲurˈtʃate] | Pompino-Marschall 2017, p. 351 | no |
| бджілка | ˈbd͡ʒʲiɫka | [ˈbdʒiɫkɐ] | Pompino-Marschall 2017, p. 351 | no |
| свят | sʲʋʲat | [ˈsʲʋʲat] | Pompino-Marschall 2017, p. 351 | no |

Source: Pompino-Marschall, B., Steriopolo, E. & Żygis, M. (2017). *Ukrainian (Illustrations of the IPA)*. Journal of the International Phonetic Association 47(3):349-357. [cambridge.org](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D20ECF62B57E4162670BD938A4B8EA33/S0025100316000372a.pdf/ukrainian.pdf)
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Udmurt](udm.md) · [Home](../index.md) · [Ulwa →](ulw.md)
