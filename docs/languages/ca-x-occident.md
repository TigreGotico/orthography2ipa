# North-Western Catalan (`ca-x-occident`)

<!-- atlas:summary begin -->
North-Western Catalan is a Romance variety, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `ca-x-occident` spec is at the research tier. It cites 11 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ca-x-occident` |
| Aliases | `ca-x-occidental` |
| ISO 639-3 | [cat](https://iso639-3.sil.org/code/cat), Catalan |
| Glottolog | [cata1291](https://glottolog.org/resource/languoid/id/cata1291), Català Nord-Occidental |
| Wikidata | [Q2941598](https://www.wikidata.org/wiki/Q2941598) |
| Wikipedia | [Western Catalan](https://en.wikipedia.org/wiki/Western_Catalan) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance](by-family.md#indo-european--italic--romance) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Ancestor | [Old Catalan](https://tigregotico.github.io/orthography2ipa/#ca-x-medieval) `ca-x-medieval` |
| Explorer | [`ca-x-occident` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ca-x-occident) |
| Spec file | [`ca-x-occident.json`](../../orthography2ipa/data/ca-x-occident.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> NORTH-WESTERN CATALAN (català nord-occidental: lleidatà, pallarès, ribagorçà, tortosí), the northern half of the WESTERN block. It descends from Old Catalan (ca-x-medieval), not from Central Catalan.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 11 works, from 1962 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes 1 of the 50 spellings of its letter table and takes the other 49 from [Old Catalan](https://tigregotico.github.io/orthography2ipa/#ca-x-medieval) `ca-x-medieval`.

The [spec file](../../orthography2ipa/data/ca-x-occident.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ca-x-occident` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 11 works. 6 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wheeler2005"></a>Wheeler, M. W. (2005). *The Phonology of Catalan*. Oxford University Press. [global.oup.com](https://global.oup.com/academic/product/the-phonology-of-catalan-9780199258147)
2. <a id="src-badia_i_margarit1994"></a>Badia i Margarit, A. M. (1994). *Gramàtica de la llengua catalana: descriptiva, normativa, diatòpica, diacrònica*. Enciclopèdia Catalana.
3. <a id="src-recasens1996"></a>Recasens, D. (1996). *Fonètica descriptiva del català: assaig de caracterització de la pronúncia del vocalisme i consonantisme del català al segle XX*. Institut d'Estudis Catalans.
4. <a id="src-veny1982"></a>Veny, J. (1982). *Els parlars catalans: síntesi de dialectologia*. Editorial Moll.
5. <a id="src-iec2016"></a>Institut d'Estudis Catalans (2016). *Gramàtica de la llengua catalana*. Institut d'Estudis Catalans. [giec.iec.cat](https://giec.iec.cat/)
6. <a id="src-dcvb"></a>Alcover, A. M. & Moll, F. de B. (1962). *Diccionari català-valencià-balear*. Editorial Moll. [dcvb.iec.cat](https://dcvb.iec.cat/)
7. <a id="src-wiktionary_ca"></a>Wiktionary contributors (2026). *Wiktionary, the free dictionary, Catalan entries*. Wikimedia Foundation. [en.wiktionary.org](https://en.wiktionary.org/wiki/Category:Catalan_lemmas)
8. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
9. <a id="src-wikipedia_catalan_phonology"></a>Wikipedia contributors (2026). *Catalan phonology (Wikipedia)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Catalan_phonology)
10. <a id="src-wikipedia_catalan_dialects"></a>Wikipedia contributors (2026). *Catalan dialects (Wikipedia)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Catalan_dialects)
11. <a id="src-bonet_lloret1998"></a>Bonet, E. & Lloret, M.-R. (1998). *Fonologia catalana*. Ariel.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `4catac` ([projecte-aina/4catac](https://huggingface.co/datasets/projecte-aina/4catac)) | `ca-x-occident` | gold | expert-human | CC BY 4.0 | 160 | 0.0822 | yes |
| `spain_romance_tts` | `ca-x-occident` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0724 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 51 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |
| Affricate |  |  |  | dz ts | dʒ tʃ |  |  |
| Nasal | m | ɱ |  | n |  | ɲ | ŋ |
| Trill |  |  |  | r |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |
| Fricative | β | f v | ð | s z | ʃ ʒ |  | ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l lː ɫ ɫː |  | ʎ |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [jʃ] [ks] [ku] [kw] [rs] [w] [ɡu] [ɡw] [ɡz] [ɣu] [ɣw].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ |  |
| ⟨a⟩ | [a] [ə] | default [a] · word final [ɛ] |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [s] | before front vowel [s] · default [k] |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ɛ] [ə] | default [e] [ɛ] · nucleus unstressed [e] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] | before front vowel [dʒ] · default [ɡ] |
| ⟨gu⟩ | [ɡ] [ɡw] | before front vowel [ɡ] · before vowel [ɡw] · default [ɡu] |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] [j] | after vowel [j] · default [i] |
| ⟨ix⟩ | [jʃ] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] | before consonant [l] [ɫ] · onset [l] · word final [l] [ɫ] |
| ⟨ll⟩ | [ʎ] |  |
| ⟨l·l⟩ | [lː] [ɫː] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] [ɔ] [u] | default [o] [ɔ] · nucleus unstressed [o] |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] [kw] | before front vowel [k] · before vowel [kw] · default [ku] |
| ⟨r⟩ | [ɾ] [r] | before vowel [ɾ] · default [r] · intervocalic [ɾ] · word final ∅ · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨rs⟩ | [rs] [s] | default [rs] · word final [s] |
| ⟨s⟩ | [s] [z] | default [s] · intervocalic [z] |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tg⟩ | [dʒ] |  |
| ⟨tj⟩ | [dʒ] |  |
| ⟨tx⟩ | [tʃ] |  |
| ⟨tz⟩ | [dz] |  |
| ⟨u⟩ | [u] [w] | after vowel [w] · default [u] |
| ⟨v⟩ | [b] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] [ks] | after consonant [tʃ] · before consonant [ks] · default [ʃ] · intervocalic [ks] · word initial [tʃ] |
| ⟨z⟩ | [z] |  |
| ⟨à⟩ | [a] |  |
| ⟨ç⟩ | [s] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ï⟩ | [i] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ü⟩ | [u] [w] | after consonant [w] · default [u] |
| ⟨’⟩ | ∅ |  |

Stress falls on the penult by default. A written ⟨à⟩ ⟨è⟩ ⟨é⟩ ⟨í⟩ ⟨ò⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-r⟩ ⟨-l⟩ ⟨-t⟩ ⟨-d⟩ ⟨-p⟩ ⟨-b⟩ ⟨-c⟩ ⟨-k⟩ ⟨-g⟩ ⟨-m⟩ ⟨-f⟩ ⟨-x⟩ ⟨-j⟩ ⟨-ç⟩ ⟨-z⟩ ⟨-ig⟩ ⟨-ll⟩ ⟨-ns⟩ ⟨-rs⟩ ⟨-ls⟩ ⟨-ts⟩ ⟨-ps⟩ ⟨-cs⟩ ⟨-ms⟩ ⟨-ds⟩ ⟨-bs⟩ ⟨-gs⟩ ⟨-fs⟩ ⟨-nts⟩ ⟨-lts⟩ ⟨-rts⟩ ⟨-sts⟩ ⟨-ncs⟩ ⟨-igs⟩ ⟨-tzs⟩ ⟨-ig⟩ ⟨-rn⟩ ⟨-rm⟩ ⟨-ai⟩ ⟨-au⟩ ⟨-ei⟩ ⟨-eu⟩ ⟨-iu⟩ ⟨-oi⟩ ⟨-ou⟩ ⟨-ny⟩ ⟨-nys⟩. These endings take the penult: ⟨-as⟩ ⟨-es⟩ ⟨-is⟩ ⟨-os⟩ ⟨-us⟩ ⟨-en⟩ ⟨-in⟩.

Whole-word exceptions (43): ⟨a⟩ [a], ⟨al⟩ [al], ⟨als⟩ [als], ⟨amb⟩ [am], ⟨d⟩ [d], ⟨de⟩ [de], ⟨del⟩ [del], ⟨dels⟩ [dels], ⟨el⟩ [el], ⟨els⟩ [els], ⟨em⟩ [em], ⟨en⟩ [en], ⟨ens⟩ [ens], ⟨es⟩ [es], ⟨et⟩ [et], ⟨hi⟩ [i], ⟨ho⟩ [o], ⟨i⟩ [i], ⟨l⟩ [l], ⟨la⟩ [la], ⟨les⟩ [les], ⟨li⟩ [li], ⟨lo⟩ [lo], ⟨m⟩ [m], ⟨me⟩ [me], ⟨molt⟩ [mol], ⟨molts⟩ [mols], ⟨n⟩ [n], ⟨ne⟩ [ne], ⟨ni⟩ [ni], and 13 more in the spec file.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 37 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `CA_TRILL_AFTER_NLS` | /ɾ/ → [r], after [l] [ɫ] [n] [s] [z] | ⟨honra⟩ [ˈonra] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_IG_AFFRICATE` | /ɡ/ → [tʃ], word-finally, after [i] [j] | ⟨vaig⟩ [ˈbatʃ] | [Wheeler 2005](#src-wheeler2005) |
| `CA_FINAL_IG_GLIDE_ABSORB` | /j/ → ∅, before [ɡ], spelled ⟨i⟩ | ⟨vaig⟩ [ˈbatʃ] | [Wheeler 2005](#src-wheeler2005) |
| `CA_CLUSTER_T_FINAL` | /t d/ → ∅, word-finally, after [n] [l] [ɫ] | ⟨camp⟩ [ˈkam] | [Wheeler 2005](#src-wheeler2005), [Veny 1982](#src-veny1982), Recasens 1993 |
| `CA_CLUSTER_P_FINAL` | /p b/ → ∅, word-finally, after [m] | ⟨camp⟩ [ˈkam] | [Wheeler 2005](#src-wheeler2005), [Veny 1982](#src-veny1982), Recasens 1993 |
| `CA_CLUSTER_K_FINAL` | /k ɡ/ → ∅, word-finally, after [n] [ŋ] | ⟨camp⟩ [ˈkam] | [Wheeler 2005](#src-wheeler2005), [Veny 1982](#src-veny1982), Recasens 1993 |
| `CA_CLUSTER_T_PLURAL` | /t d/ → ∅, after [n] [l] [ɫ], before [s] | ⟨importants⟩ [impuɾˈtans] | [Wheeler 2005](#src-wheeler2005), [Veny 1982](#src-veny1982), Recasens 1993 |
| `CA_CLUSTER_P_PLURAL` | /p b/ → ∅, after [m], before [s] | ⟨importants⟩ [impuɾˈtans] | [Wheeler 2005](#src-wheeler2005), [Veny 1982](#src-veny1982), Recasens 1993 |
| `CA_CLUSTER_K_PLURAL` | /k ɡ/ → ∅, after [n] [ŋ], before [s] | ⟨importants⟩ [impuɾˈtans] | [Wheeler 2005](#src-wheeler2005), [Veny 1982](#src-veny1982), Recasens 1993 |
| `CA_DEVOICE_B` | /b/ → [p], word-finally | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_DEVOICE_D` | /d/ → [t], word-finally | ⟨fred⟩ [ˈfɾet] | [Wheeler 2005](#src-wheeler2005) |
| `CA_DEVOICE_G` | /ɡ/ → [k], word-finally | - | [Wheeler 2005](#src-wheeler2005) |
| `CA_DEVOICE_Z` | /z/ → [s], word-finally | - | [Wheeler 2005](#src-wheeler2005) |
| `CA_DEVOICE_ZH` | /ʒ/ → [ʃ], word-finally | - | [Wheeler 2005](#src-wheeler2005) |
| `CA_DEVOICE_V` | /v/ → [f], word-finally | - | [Wheeler 2005](#src-wheeler2005) |
| `CA_DEVOICE_DZH` | /dʒ/ → [tʃ], word-finally | ⟨mig⟩ [ˈmitʃ] | [Wheeler 2005](#src-wheeler2005) |
| `CA_DEVOICE_DZ` | /dz/ → [ts], word-finally | - | [Wheeler 2005](#src-wheeler2005) |
| `CA_NASAL_LABIAL` | /n/ → [m], before [p] [b] [m] | ⟨pare⟩ [umˈpaɾe] | [Wheeler 2005](#src-wheeler2005), [Bonet 1998](#src-bonet_lloret1998), Recasens 1993 |
| `CA_NASAL_LABIODENTAL` | /n m/ → [ɱ], before [f] [v] | ⟨enfadar⟩ [əɱfəˈða] | [Wheeler 2005](#src-wheeler2005), [Bonet 1998](#src-bonet_lloret1998), Recasens 1993 |
| `CA_NASAL_VELAR` | /n/ → [ŋ], before [k] [ɡ] | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_NASAL_PALATAL` | /n/ → [ɲ], before [ʃ] [ʒ] [ʎ] | ⟨any llunyà⟩ [ˈaɲ ʎuˈɲa] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_GEMINATE_BL` | /b/ → [b], before [l] [ɫ] | ⟨poble⟩ [ˈpɔbːlə] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_GEMINATE_GL` | /ɡ/ → [ɡ], before [l] [ɫ] | ⟨regla⟩ [ˈreɡːlə] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_SPIRANT_B` | /b/ → [β], after a vowel | ⟨roba⟩ [ˈrɔβə] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_SPIRANT_D` | /d/ → [ð], after a vowel | ⟨cada⟩ [ˈkaðə] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_SPIRANT_G` | /ɡ/ → [ɣ], after a vowel | ⟨pagar⟩ [pəˈɣa] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_SPIRANT_GW` | /ɡw/ → [ɣw], after a vowel | ⟨aigua⟩ [ˈajɣwə] | - |
| `CA_SPIRANT_GU` | /ɡu/ → [ɣu], after a vowel | ⟨recorregut⟩ [rəkurəˈɣut] | - |
| `CA_SPIRANT_B_CONT` | /b/ → [β], after [ɾ] [r] [l] [ɫ] [s] [z] [ʃ] [ʒ] and 15 more | ⟨arbres⟩ [ˈaɾβɾəs] | [Wheeler 2005](#src-wheeler2005) |
| `CA_SPIRANT_G_CONT` | /ɡ/ → [ɣ], after [ɾ] [r] [l] [ɫ] [s] [z] [ʃ] [ʒ] and 15 more | - | [Wheeler 2005](#src-wheeler2005) |
| `CA_SPIRANT_GW_CONT` | /ɡw/ → [ɣw], after [ɾ] [r] [l] [ɫ] [s] [z] [ʃ] [ʒ] and 15 more | - | [Wheeler 2005](#src-wheeler2005) |
| `CA_SPIRANT_GU_CONT` | /ɡu/ → [ɣu], after [ɾ] [r] [l] [ɫ] [s] [z] [ʃ] [ʒ] and 15 more | - | [Wheeler 2005](#src-wheeler2005) |
| `CA_SPIRANT_D_CONT` | /d/ → [ð], after [ɾ] [r] [s] [z] [ʃ] [ʒ] [f] [v] and 5 more | - | [Wheeler 2005](#src-wheeler2005) |
| `CA_X_GZ` | /ks/ → [ɡz], after a front vowel, before a vowel, spelled ⟨x⟩ | ⟨exercici⟩ [əɡzərˈsisi] | [Wheeler 2005](#src-wheeler2005) |
| `NW_FINAL_A_STRESSED_KEEP` | /ɛ/ → [a], word-finally, stressed, spelled ⟨a⟩ | ⟨pa⟩ [ˈpa] | [Wheeler 2005](#src-wheeler2005), [Recasens 1996](#src-recasens1996), [Veny 1982](#src-veny1982) |
| `NW_OPEN_O` | /o/ → [ɔ], stressed, in 6 listed words | ⟨corre⟩ [ˈkɔɾe] | [Recasens 1996](#src-recasens1996), [Veny 1982](#src-veny1982) |
| `WESTERN_INITIAL_E_TO_A` | /e/ → [a], word-initially, unstressed, before [m] [ɱ] [n] [ŋ] [s] [z], with more context in the spec | ⟨estar⟩ [asˈta] | [Recasens 1996](#src-recasens1996), [Veny 1982](#src-veny1982) |

The spec applies 27 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `CA_CLUSTER_PRECONS_T` | `([nlɫ])t$` | `^[ˈˌ]?[pbtdkɡfvszʃʒmnɲŋlʎɫɾrβðɣ]` | left ∅ | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_CLUSTER_PRECONS_P` | `(m)p$` | `^[ˈˌ]?[pbtdkɡfvszʃʒmnɲŋlʎɫɾrβðɣ]` | left ∅ | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_CLUSTER_PRECONS_K` | `([nŋ])k$` | `^[ˈˌ]?[pbtdkɡfvszʃʒmnɲŋlʎɫɾrβðɣ]` | left ∅ | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_PS_VOICING` | `ps$` | `^[ˈˌ]?[aeiouəɛɔɐbdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | left [bz] | ⟨cops havíem⟩ [ˈkɔbz əˈβiəm] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_TS_VOICING` | `ts$` | `^[ˈˌ]?[aeiouəɛɔɐbdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | left [dz] | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_KS_VOICING` | `ks$` | `^[ˈˌ]?[aeiouəɛɔɐbdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | left [ɡz] | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_S_VOICING` | `s$` | `^[ˈˌ]?[aeiouəɛɔɐbdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | left [z] | ⟨els amics⟩ [əlz əˈmiks] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_TSH_VOICING` | `tʃ$` | `^[ˈˌ]?[aeiouəɛɔɐbdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | left [dʒ] | ⟨vaig obrir⟩ [ˈbadʒ uˈβɾi] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_SH_VOICING` | `ʃ$` | `^[ˈˌ]?[aeiouəɛɔɐbdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | left [ʒ] | ⟨vaig obrir⟩ [ˈbadʒ uˈβɾi] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_T_VOICING` | `t$` | `^[ˈˌ]?[bdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | left [d] | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_P_VOICING` | `p$` | `^[ˈˌ]?[bdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | left [b] | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_K_VOICING` | `k$` | `^[ˈˌ]?[bdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | left [ɡ] | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_FINAL_F_VOICING` | `f$` | `^[ˈˌ]?[bdɡβðɣvzʒmnɲŋlʎɫɾrjw]` | left [v] | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_EXT_SPIRANT_B` | `[aeiouəɛɔiuwjszʃʒfvβðɣɾrlɫ]$` | `^([ˈˌ]?)b` | right [β] | ⟨es va⟩ [əz ˈβa] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_EXT_SPIRANT_G` | `[aeiouəɛɔiuwjszʃʒfvβðɣɾrlɫ]$` | `^([ˈˌ]?)ɡ` | right [ɣ] | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_EXT_SPIRANT_D` | `[aeiouəɛɔiuwjszʃʒfvβðɣɾr]$` | `^([ˈˌ]?)d(?!ʒ)` | right [ð] | ⟨de decidir⟩ [ðə ðəsiˈði] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_EXT_NASAL_LABIAL` | `n$` | `^[ˈˌ]?[pbmf]` | left [m] | ⟨un peu⟩ [um ˈpɛw] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_EXT_NASAL_VELAR` | `n$` | `^[ˈˌ]?[kɡ]` | left [ŋ] | ⟨un gat⟩ [uŋ ˈɡat] | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_EXT_NASAL_PALATAL` | `n$` | `^[ˈˌ]?(?:ʃ\|ʒ\|ʎ)` | left [ɲ] | ⟨against Eastern⟩ [uɲ ˈʒudʒə] | - |
| `CA_ELIDE_ELS` | `[aeiouɛɔəɐ]$` | `^els$` | right [ls] | - | - |
| `CA_ELIDE_EL` | `[aeiouɛɔəɐ]$` | `^el$` | right [l] | ⟨que el tap⟩ [ke l ˈtab] | [Wheeler 2005](#src-wheeler2005), [Bonet 1998](#src-bonet_lloret1998), IEC 2016 |
| `CA_DEGEM_S` | `[ˈˌ]?s$` | `^[ˈˌ]?s` | left ∅ | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_DEGEM_SH` | `[ˈˌ]?ʃ$` | `^[ˈˌ]?ʃ` | left ∅ | - | [Wheeler 2005](#src-wheeler2005), Recasens 1993 |
| `CA_ELIDE_INITIAL_VOWEL` | `[aeiouɛɔɐ]$` | `^[aeoəɛɔɐ](?=.*[aeiouəɛɔɐ])` | right ∅ | ⟨va anar⟩ [ˈba ˈna] | [Wheeler 2005](#src-wheeler2005), [Bonet 1998](#src-bonet_lloret1998) |
| `CA_HIATUS_GLIDE_I` | `[aeiouəɛɔɐ]$` | `^i` | right [j] | ⟨pollastre i⟩ [puˈʎastɾə j] | [Wheeler 2005](#src-wheeler2005), [Bonet 1998](#src-bonet_lloret1998) |
| `CA_HIATUS_GLIDE_U` | `[aeiouəɛɔɐ]$` | `^u(?=.)` | right [w] | ⟨beure un⟩ [ˈbɛwɾə wn] | [Wheeler 2005](#src-wheeler2005), [Bonet 1998](#src-bonet_lloret1998) |
| `CA_CLITIC_GLIDE_I_BEFORE_VOWEL` | `^i$` | `^(?!(?:[ˈˌ]?els?)$)[ˈˌ]?[aeiouəɛɔɐ]` | left [j] | ⟨hi havia⟩ [j əˈβiə] | [Wheeler 2005](#src-wheeler2005), [Bonet 1998](#src-bonet_lloret1998), IEC 2016 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ca-x-occident")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← North Frisian](frr.md) · [Home](../index.md) · [Northern Catalan →](ca-x-nord.md)
