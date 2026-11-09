# Southern Russian (`ru-x-southern`)

<!-- atlas:summary begin -->
Southern Russian is an East Slavic variety, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `ru-x-southern` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ru-x-southern` |
| ISO 639-3 | [rus](https://iso639-3.sil.org/code/rus), Russian |
| Wikipedia | [Southern Russian dialects](https://en.wikipedia.org/wiki/Southern_Russian_dialects) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > East Slavic](by-family.md#indo-european--balto-slavic--slavic--east-slavic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1600, living |
| Parent | [Russian](ru.md) `ru` |
| Child lects | 2, see [Related lects](#related-lects) |
| Explorer | [`ru-x-southern` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ru-x-southern) |
| Spec file | [`ru-x-southern.json`](../../orthography2ipa/data/ru-x-southern.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Southern Russian dialects (Ryazan, Kursk, Voronezh, Tula). Г = FRICATIVE [ɣ], 'фрикативное произношение фонемы /г/, то есть [ɣ]', the single isogloss that defines the Southern zone, and it devoices to [x] rather than [k] word-finally …

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1985 to 2004. [Sources](#sources) lists them. The spec file writes 1 of the 36 spellings of its letter table and takes the other 35 from [Russian](ru.md) `ru`.

The [spec file](../../orthography2ipa/data/ru-x-southern.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `ru-x-southern` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Don Cossack Russian](https://tigregotico.github.io/orthography2ipa/#ru-x-don) `ru-x-don`: stub tier
- [Kursk-Orel Russian](https://tigregotico.github.io/orthography2ipa/#ru-x-kursk-orel) `ru-x-kursk-orel`: stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
2. <a id="src-timberlake2004"></a>Timberlake, A. (2004). *A Reference Grammar of Russian*. Cambridge University Press.
3. <a id="src-zalizniak1985"></a>Zalizniak, A.A. (1985). *Ot praslavyanskoy aktsentovki k russkoy*. Nauka.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 83 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ p pʲ |  | d dʲ t tʲ |  |  | k kʲ ɡ ɡʲ |
| Affricate |  |  | ts |  | tɕ |  |
| Nasal | m mʲ |  | n nʲ |  |  | ŋ |
| Trill |  |  | r rʲ |  |  |  |
| Fricative |  | f fʲ v vʲ | s sʲ z zʲ | ʂ ʐ | ɕː | x xʲ ɣ |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | lʲ ɫ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Near-close | ɪ |  | ʊ |
| Close-mid | e | ɵ | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  |  |
| Near-open |  | ɐ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [bʲjɪɣə] [dʲjɪɣə] [ja] [je] [jo] [ju] [jə] [jɪ] [jɵ] [jʊ] [lʲjɪɣə] [mʲjɪɣə] [nʲjɪɣə] [nʲɪɣə] [pʲjɪɣə] [rʲjɪɣə] [sʲjɪɣə] [sʲɪɣə] [tsɨɣə] [tɕj] [tɕjɪɣə] [tɕɪɣə] [tʲjɪɣə] [vʲjɪɣə] [zʲjɪɣə] [ɕːɪɣə] [əɣə] [ʂj] [ʂɨɣə] [ʐj] [ʐjɪɣə] [ʐɨɣə] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨́⟩ | ∅ |  |
| ⟨а⟩ | [a] | first pretonic [a] · posttonic [ə] · pretonic [ə] |
| ⟨б⟩ | [b] | default [b] · word final [p] |
| ⟨в⟩ | [v] | default [v] · word final [f] |
| ⟨г⟩ | [ɣ] | default [ɣ] · word final [x] |
| ⟨д⟩ | [d] | default [d] · word final [t] |
| ⟨е⟩ | [je] [e] | first pretonic [ja] [a] [jɪ] [ɪ] · posttonic [jɪ] [ɪ] · pretonic [jɪ] [ɪ] |
| ⟨ж⟩ | [ʐ] | default [ʐ] · word final [ʂ] |
| ⟨з⟩ | [z] | default [z] · word final [s] |
| ⟨и⟩ | [i] | posttonic [ɪ] · pretonic [ɪ] |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [ɫ] |  |
| ⟨ль⟩ | [lʲ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] | first pretonic [a] · posttonic [ə] · pretonic [ə] |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] | posttonic [ʊ] · pretonic [ʊ] |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tɕ] |  |
| ⟨ш⟩ | [ʂ] |  |
| ⟨щ⟩ | [ɕː] |  |
| ⟨щь⟩ | [ɕː] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [ɛ] | posttonic [ɪ] · pretonic [ɪ] |
| ⟨ю⟩ | [ju] | posttonic [jʊ] · pretonic [jʊ] |
| ⟨я⟩ | [ja] | first pretonic [ja] [jɪ] · posttonic [jə] · pretonic [jɪ] |
| ⟨ё⟩ | [jo] | default [jo] |

Stress falls on the penult by default. A written ⟨ё⟩ ⟨́⟩ marks the stressed vowel.

Whole-word exceptions (25): ⟨всего⟩ [fsʲaˈɣo], ⟨дорого⟩ [ˈdorəɣə], ⟨его⟩ [jaˈɣo], ⟨кого⟩ [kaˈɣo], ⟨лого⟩ [ˈɫoɣə], ⟨много⟩ [ˈmnoɣə], ⟨моего⟩ [məjaˈɣo], ⟨намного⟩ [naˈmnoɣə], ⟨него⟩ [nʲaˈɣo], ⟨недорого⟩ [nʲaˈdorəɣə], ⟨немного⟩ [nʲaˈmnoɣə], ⟨никого⟩ [nʲɪkaˈɣo], ⟨ничего⟩ [nʲɪtɕaˈɣo], ⟨ничьего⟩ [nʲɪtɕjaˈɣo], ⟨ого⟩ [ˈoɣo], ⟨одного⟩ [ədnaˈɣo], ⟨своего⟩ [svəjaˈɣo], ⟨сего⟩ [sʲaˈɣo], ⟨строго⟩ [ˈstroɣə], ⟨твоего⟩ [tvəjaˈɣo], ⟨того⟩ [taˈɣo], ⟨убого⟩ [ʊˈboɣə], ⟨чего⟩ [tɕaˈɣo], ⟨чьего⟩ [tɕjaˈɣo], ⟨этого⟩ [ˈɛtəɣə].

Grammatical endings: ⟨-бьего⟩ [bʲjɪɣə], ⟨-вьего⟩ [vʲjɪɣə], ⟨-дьего⟩ [dʲjɪɣə], ⟨-жего⟩ [ʐɨɣə], ⟨-жьего⟩ [ʐjɪɣə], ⟨-зьего⟩ [zʲjɪɣə], ⟨-льего⟩ [lʲjɪɣə], ⟨-мьего⟩ [mʲjɪɣə], ⟨-него⟩ [nʲɪɣə], ⟨-ньего⟩ [nʲjɪɣə], ⟨-ого⟩ [əɣə], ⟨-пьего⟩ [pʲjɪɣə], ⟨-рьего⟩ [rʲjɪɣə], ⟨-сего⟩ [sʲɪɣə], ⟨-сьего⟩ [sʲjɪɣə], ⟨-тьего⟩ [tʲjɪɣə], ⟨-цего⟩ [tsɨɣə], ⟨-чего⟩ [tɕɪɣə], ⟨-чьего⟩ [tɕjɪɣə], ⟨-шего⟩ [ʂɨɣə], ⟨-щего⟩ [ɕːɪɣə].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 62 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `RU_HARD_BACK_jɪ` | /jɪ/ → [ɨ], after [ʐ] [ʂ] [ts] | - | - |
| `RU_HARD_BACK_je` | /je/ → [ɛ], after [ʐ] [ʂ] [ts] | ⟨жест⟩ [ʐɛst] | [Timberlake 2004](#src-timberlake2004), Avanesov 1956, Jones & Ward 1969 |
| `RU_HARD_BACK_ɪ` | /ɪ/ → [ɨ], after [ʐ] [ʂ] [ts] | - | - |
| `RU_HARD_BACK_i` | /i/ → [ɨ], after [ʐ] [ʂ] [ts] | - | - |
| `RU_HARD_BACK_e` | /e/ → [ɛ], after [ʐ] [ʂ] [ts] | ⟨жест⟩ [ʐɛst] | [Timberlake 2004](#src-timberlake2004), Avanesov 1956, Jones & Ward 1969 |
| `RU_DEVOICE_SOFT_FIN_b` | /b/ → [pʲ], before [ʲ], with more context in the spec | - | - |
| `RU_DEVOICE_SOFT_FIN_v` | /v/ → [fʲ], before [ʲ], with more context in the spec | - | - |
| `RU_DEVOICE_SOFT_FIN_d` | /d/ → [tʲ], before [ʲ], with more context in the spec | - | - |
| `RU_DEVOICE_SOFT_FIN_z` | /z/ → [sʲ], before [ʲ], with more context in the spec | - | - |
| `RU_DEVOICE_SOFT_FIN_ɡ` | /ɡ/ → [kʲ], before [ʲ], with more context in the spec | - | - |
| `RU_PALAT_b` | /b/ → [bʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_v` | /v/ → [vʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_ɡ` | /ɡ/ → [ɡʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_d` | /d/ → [dʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_z` | /z/ → [zʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_k` | /k/ → [kʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_ɫ` | /ɫ/ → [lʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_m` | /m/ → [mʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_n` | /n/ → [nʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_p` | /p/ → [pʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_r` | /r/ → [rʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_s` | /s/ → [sʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_t` | /t/ → [tʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_f` | /f/ → [fʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_x` | /x/ → [xʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_SOFT_SIGN_SILENT` | /ʲ/ → ∅, after [b] [d] [f] [j] [k] [m] [n] [p] and 13 more | - | - |
| `RU_DEIOTA_jɪ` | /jɪ/ → [ɪ], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_DEIOTA_jə` | /jə/ → [ə], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_DEIOTA_jʊ` | /jʊ/ → [ʊ], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_DEIOTA_je` | /je/ → [e], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_DEIOTA_ja` | /ja/ → [a], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_DEIOTA_ju` | /ju/ → [u], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_HARD_BACK_jo` | /jo/ → [o], after [ʐ] [ʂ] [ts] | ⟨шёл⟩ [ʂoɫ] | [Timberlake 2004](#src-timberlake2004), Jones & Ward 1969 |
| `RU_DEIOTA_jo` | /jo/ → [ɵ], after [b] [d] [f] [j] [k] [m] [n] [p] and 12 more | - | - |
| `RU_DEIOTA_jo_separative` | /jo/ → [jɵ], after [ʲ] [lʲ] | ⟨бельё⟩ [bʲɪlʲjɵ] | - |
| `RU_REGR_DEVOICE_b` | /b/ → [p], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨абсолют⟩ [ɐpsɐlʲut] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_bʲ` | /bʲ/ → [pʲ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_v` | /v/ → [f], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨всё⟩ [fsʲɵ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_vʲ` | /vʲ/ → [fʲ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_d` | /d/ → [t], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨водка⟩ [votkə] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_dʲ` | /dʲ/ → [tʲ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_ɡ` | /ɡ/ → [k], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨водка⟩ [votkə] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_ɡʲ` | /ɡʲ/ → [kʲ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_z` | /z/ → [s], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨всё⟩ [fsʲɵ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_zʲ` | /zʲ/ → [sʲ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨всё⟩ [fsʲɵ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_ʐ` | /ʐ/ → [ʂ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_p` | /p/ → [b], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_pʲ` | /pʲ/ → [bʲ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_t` | /t/ → [d], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨сделать⟩ [zʲdʲelətʲ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_tʲ` | /tʲ/ → [dʲ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨сделать⟩ [zʲdʲelətʲ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_k` | /k/ → [ɡ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨вокзал⟩ [vɐɡzaɫ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_kʲ` | /kʲ/ → [ɡʲ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_s` | /s/ → [z], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨сделать⟩ [zʲdʲelətʲ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_sʲ` | /sʲ/ → [zʲ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨сделать⟩ [zʲdʲelətʲ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_f` | /f/ → [v], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨вокзал⟩ [vɐɡzaɫ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_fʲ` | /fʲ/ → [vʲ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_ʂ` | /ʂ/ → [ʐ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_PALAT_s` | /s/ → [sʲ], before [t] [d] [n], with more context in the spec | ⟨гости⟩ [ɡosʲtʲɪ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_PALAT_z` | /z/ → [zʲ], before [t] [d] [n], with more context in the spec | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_PALAT_n` | /n/ → [nʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tɕ] [ɕː] | ⟨снег⟩ [sʲnʲek] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_PALAT_t` | /t/ → [tʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tɕ] [ɕː] | ⟨гости⟩ [ɡosʲtʲɪ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_PALAT_d` | /d/ → [dʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tɕ] [ɕː] | - | [Timberlake 2004](#src-timberlake2004) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ru-x-southern")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Southern Min](nan-Latn-pehoeji.md) · [Home](../index.md) · [Southern Sotho →](st.md)
