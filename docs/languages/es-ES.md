# Castilian Spanish (`es-ES`)

<!-- atlas:summary begin -->
Castilian Spanish is an Ibero-Romance language, written in the Latin script. Its code names Spain. The `es-ES` spec is at the production tier. It cites 12 sources and has 6 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `es-ES` |
| Aliases | `spa` |
| ISO 639-3 | [spa](https://iso639-3.sil.org/code/spa), Spanish |
| Glottolog | [cast1244](https://glottolog.org/resource/languoid/id/cast1244), Castilian |
| Wikidata | [Q1321](https://www.wikidata.org/wiki/Q1321) |
| Wikipedia | [Spanish language](https://en.wikipedia.org/wiki/Spanish_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance](by-family.md#indo-european--italic--romance--ibero-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Spain](by-region.md#spain) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [production](../specs/quality_tiers.md#production) |
| Attested | from 1500, living |
| Ancestor | [Castilian](https://tigregotico.github.io/orthography2ipa/#es-ES-x-medieval) `es-ES-x-medieval` |
| Child lects | 34, see [Related lects](#related-lects) |
| Explorer | [`es-ES` in the data explorer](https://tigregotico.github.io/orthography2ipa/#es-ES) |
| Spec file | [`es-ES.json`](../../orthography2ipa/data/es-ES.json) |
<!-- atlas:header end -->

## Overview

The `es-ES` spec transcribes standard Peninsular Spanish, the Castilian norm that the Real Academia Española describes. The bare tag `es` resolves to it, because Spain is the default region of `es`. The Latin American varieties are separate specs under `es-419` and the country tags, and they take their letter table from this one.

Spanish spelling is shallow, so the production bar for this spec is a PER of 0.15, not the 0.25 of a deep orthography ([quality tiers](../specs/quality_tiers.md#the-per-threshold)). A small closed set of contextual rules covers most of the letters: ⟨c⟩ and ⟨g⟩ before a front vowel, the digraphs ⟨gu⟩ and ⟨qu⟩, the silent ⟨h⟩, and ⟨y⟩ as a consonant or a vowel.

Castilian keeps *distinción*. The letter ⟨z⟩ and the letter ⟨c⟩ before ⟨e i⟩ are /θ/, and ⟨s⟩ is /s/, so `zona` is [ˈθona] and `sola` is [ˈsola]. This contrast separates Castilian from the *seseo* of Andalusia, the Canary Islands and Latin America, where both letters are /s/. The spec also merges ⟨ll⟩ with ⟨y⟩ as /ʝ/ (`calle` [ˈkaʝe]), which is the *yeísmo* of most speakers of the modern standard. The letters ⟨b⟩ and ⟨v⟩ are one phoneme, and ⟨j⟩ and ⟨g⟩ before a front vowel are the velar fricative /x/.

## Spirants and nasals

The voiced stops /b d ɡ/ are stops only after a pause and after a nasal, and /d/ is also a stop after /l/. Everywhere else they are the spirants [β ð ɣ], and the rule applies across a word boundary too. Navarro Tomás (1918) states the three cases in § 82 (p. 63), § 101 (p. 75) and § 129 (p. 109). So `cabra` is [ˈkaβɾa] and `la boca` is [la ˈβoka], but `hombre` keeps its stop, and `el domingo` keeps the stop of /d/ after /l/. The allophone rules handle the cases inside a word, and the cross-word rules handle the start of the next word.

A nasal at the end of a syllable takes the place of the consonant after it. Before a labial it is [m] and before a velar it is [ŋ], inside a word (`cinco` [ˈθiŋko]) and across words (`un buen baile` [um ˈbwem ˈbai̯le]). Navarro Tomás (1918) gives the velar case in § 133 (pp. 111-112) and the labial case across words in § 87 (p. 66).

## Diphthongs and stress

A rising diphthong starts with a consonantal glide, and a falling diphthong ends with a vowel that is not syllabic: `nación` is [naˈθjon] and `aire` is [ˈai̯ɾe]. The spec takes this asymmetry from Hualde (2005, ch. 4) and from the *Fonética y fonología* of the academies (2011, ch. 8). A written accent marks stress, not a hiatus.

Stress is predictable from the spelling. A word that ends in a vowel, ⟨n⟩ or ⟨s⟩ takes the penult, and a word that ends in another consonant takes the last syllable (Navarro Tomás 1918, § 156, p. 140). A written accent overrides both. A final vowel plus ⟨y⟩ counts as a consonant ending, so ⟨estoy⟩, ⟨virrey⟩ and ⟨Uruguay⟩ take final stress with no accent (DPD, s.v. *tilde*, § 1.2.1).

## Weak points

The final ⟨y⟩ of ⟨ay ey oy uy⟩ comes out as a full [i]: `estoy` is [esˈtoi], while `aire` has the glide [i̯]. Navarro Tomás (1918, § 47, p. 39) gives the written ⟨y⟩ of these diphthongs as the semivowel [i̯], so the output does not match the spec's own source.

The spec notes describe the apical /s/ of Castilian, [s̺], but the letter table writes plain [s]. The spec also has no rule for /s/ before a voiced consonant, so `mismo` comes out [ˈmismo]. A rule for that context needs a cited page first.

The letter ⟨x⟩ is [ks] by default. The Mexican place names that keep the old value /x/, such as ⟨México⟩ and ⟨Oaxaca⟩, are not exceptions in this spec, so `México` comes out [ˈmeksiko].

The letter table gives ⟨e⟩ a second reading [ɛ] and ⟨o⟩ a second reading [ɔ]. The lattice offers these readings as candidates, so [ɛ] and [ɔ] appear in the inventory chart. No rule selects them, and the transcription keeps [e] and [o]: `perro` is [ˈpero] and `torre` is [ˈtore]. The spec cites no source for the two readings.

Seseo, the degree of yeísmo and the weakening of a coda /s/ belong to the regional specs, not to `es-ES`. A gold entry that an editor from one of those regions transcribed counts as an error against this spec. So the PER on the crowd-sourced sets is slightly higher than the spec deserves.

<!-- atlas:lects begin -->
## Related lects

These specs name `es-ES` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Rioplatense Spanish](https://tigregotico.github.io/orthography2ipa/#es-AR) `es-AR`: Argentina, research tier
- [Bolivian Spanish](https://tigregotico.github.io/orthography2ipa/#es-BO) `es-BO`: Bolivia, skeleton tier
- [Chilean Spanish](https://tigregotico.github.io/orthography2ipa/#es-CL) `es-CL`: Chile, research tier
- [Colombian Spanish (Bogotá)](https://tigregotico.github.io/orthography2ipa/#es-CO) `es-CO`: Colombia, skeleton tier
- [Colombian Spanish (Coastal)](https://tigregotico.github.io/orthography2ipa/#es-CO-x-costa) `es-CO-x-costa`: Colombia, research tier
- [Colombian Spanish (Paisa/Medellín)](https://tigregotico.github.io/orthography2ipa/#es-CO-x-paisa) `es-CO-x-paisa`: Colombia, skeleton tier
- [Palenquero (Lengua ri Palenge)](https://tigregotico.github.io/orthography2ipa/#pln) `pln`: Colombia, research tier
- [Costa Rican Spanish](https://tigregotico.github.io/orthography2ipa/#es-CR) `es-CR`: Costa Rica, skeleton tier
- [Cuban Spanish](https://tigregotico.github.io/orthography2ipa/#es-CU) `es-CU`: Cuba, research tier
- [Dominican Spanish](https://tigregotico.github.io/orthography2ipa/#es-DO) `es-DO`: Dominican Republic, research tier
- [Ecuadorian Spanish](https://tigregotico.github.io/orthography2ipa/#es-EC) `es-EC`: Ecuador, skeleton tier
- [Salvadoran Spanish](https://tigregotico.github.io/orthography2ipa/#es-SV) `es-SV`: El Salvador, stub tier
- [Equatoguinean Spanish](https://tigregotico.github.io/orthography2ipa/#es-GQ) `es-GQ`: Equatorial Guinea, skeleton tier
- [Guatemalan Spanish](https://tigregotico.github.io/orthography2ipa/#es-GT) `es-GT`: Guatemala, skeleton tier
- [Honduran Spanish](https://tigregotico.github.io/orthography2ipa/#es-HN) `es-HN`: Honduras, stub tier
- [Mexican Spanish (Highland)](https://tigregotico.github.io/orthography2ipa/#es-MX) `es-MX`: Mexico, research tier
- [Mexican Spanish (Coastal)](https://tigregotico.github.io/orthography2ipa/#es-MX-x-costa) `es-MX-x-costa`: Mexico, research tier
- [Nicaraguan Spanish](https://tigregotico.github.io/orthography2ipa/#es-NI) `es-NI`: Nicaragua, research tier
- [Panamanian Spanish](https://tigregotico.github.io/orthography2ipa/#es-PA) `es-PA`: Panama, research tier
- [Paraguayan Spanish](https://tigregotico.github.io/orthography2ipa/#es-PY) `es-PY`: Paraguay, skeleton tier
- [Peruvian Spanish (Andean)](https://tigregotico.github.io/orthography2ipa/#es-PE) `es-PE`: Peru, skeleton tier
- [Peruvian Spanish (Lima)](https://tigregotico.github.io/orthography2ipa/#es-PE-x-lima) `es-PE-x-lima`: Peru, skeleton tier
- [Chavacano (Zamboangueño)](https://tigregotico.github.io/orthography2ipa/#cbk-PH) `cbk-PH`: Philippines, research tier
- [Extremaduran](https://tigregotico.github.io/orthography2ipa/#ext) `ext`: Portugal, Spain, research tier
- [Puerto Rican Spanish](https://tigregotico.github.io/orthography2ipa/#es-PR) `es-PR`: Puerto Rico, research tier
- [Eastern Andalusian Spanish](https://tigregotico.github.io/orthography2ipa/#es-ES-x-andalusi-e) `es-ES-x-andalusi-e`: Spain, research tier
- [Western Andalusian Spanish](https://tigregotico.github.io/orthography2ipa/#es-ES-x-andalusi-w) `es-ES-x-andalusi-w`: Spain, research tier
- [Canarian Spanish](https://tigregotico.github.io/orthography2ipa/#es-ES-x-canarias) `es-ES-x-canarias`: Spain, research tier
- [Cantabrian Spanish (Montañés)](https://tigregotico.github.io/orthography2ipa/#es-ES-x-cantabri) `es-ES-x-cantabri`: Spain, research tier
- [Extremaduran Spanish (Extremeño)](https://tigregotico.github.io/orthography2ipa/#es-ES-x-extremad) `es-ES-x-extremad`: Spain, research tier
- [Murcian Spanish (Panocho)](https://tigregotico.github.io/orthography2ipa/#es-ES-x-murcia) `es-ES-x-murcia`: Spain, research tier
- [Uruguayan Spanish](https://tigregotico.github.io/orthography2ipa/#es-UY) `es-UY`: Uruguay, skeleton tier
- [Venezuelan Spanish](https://tigregotico.github.io/orthography2ipa/#es-VE) `es-VE`: Venezuela, research tier
- [Latin American Spanish](https://tigregotico.github.io/orthography2ipa/#es-419) `es-419`: skeleton tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 12 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-navarro1918"></a>Navarro Tomás, T. (1918). *Manual de pronunciación española*. Centro de Estudios Históricos, Madrid. Cited: § 47 p. 39, § 50 p. 41, § 82 pp. 63-64, § 87 p. 66, § 101-102 pp. 75-77, § 111 p. 86, § 122 pp. 100-102, § 128-129 pp. 108-109, § 133 pp. 111-112, § 149 p. 134, § 156 p. 140. [archive.org](https://archive.org/details/manualdepronunci00navauoft)
2. <a id="src-rae_dpd_tilde"></a>Real Academia Española & Asociación de Academias de la Lengua Española (2026). *Diccionario panhispánico de dudas, 2nd ed. (online), s.v. tilde*. RAE-ASALE. Cited: § 1.2.1-1.2.2. [rae.es](https://www.rae.es/dpd/tilde)
3. <a id="src-hualde2005"></a>Hualde, J.I. (2005). *The Sounds of Spanish*. Cambridge University Press.
4. <a id="src-penny2002"></a>Penny, R. (2002). *A History of the Spanish Language*. Cambridge University Press.
5. <a id="src-harris1969"></a>Harris, J.W. (1969). *Spanish Phonology*. MIT Press.
6. <a id="src-navarro1977"></a>Navarro Tomás, T. (1977). *Manual de pronunciación española*. CSIC.
7. <a id="src-rae2011"></a>Real Academia Española & Asociación de Academias de la Lengua Española (2011). *Nueva gramática de la lengua española: Fonética y fonología*. Espasa.
8. <a id="src-quilis1993"></a>Quilis, A. (1993). *Tratado de fonología y fonética españolas*. Gredos.
9. <a id="src-rae2010ortografia"></a>Real Academia Española & Asociación de Academias de la Lengua Española (2010). *Ortografía de la lengua española*. Espasa. Cited: 225, 235, 237.
10. <a id="src-hualde2003basque"></a>Hualde, J.I. & Ortiz de Urbina, J. (eds.) (2003). *A Grammar of Basque*. Mouton de Gruyter.
11. <a id="src-lipski1986"></a>Lipski, John M. (1986). *Reduction of Spanish Word-Final /s/ and /n/*. Canadian Journal of Linguistics / Revue canadienne de linguistique 31(2). Cited: p. 140, pp. 146-147.
12. <a id="src-lipski_overview"></a>Lipski, John M. (2011). *Geographical and Social Varieties of Spanish: An Overview*. In J.I. Hualde, A. Olarrea & E. O'Rourke (eds.), The Handbook of Hispanic Linguistics, Wiley-Blackwell. Cited: pp. 1-26. [johnlipski.github.io](https://johnlipski.github.io/geo.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `primary_sources` | `es-ES` | gold | expert-human | - | 41 | 0.0232 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `es` | gold | crowd-scraped | CC BY-SA | 132189 | 0.0774 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `es-ES` | generated | machine-generated | MIT, each file its own | 595896 | 0.0127 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `es-ES` | generated | epitran-derived | CC BY 4.0 | 13155 | 0.0863 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `es` | generated | epitran-derived | CC0 | 48067 | 0.0594 | no |
| `spain_romance_tts` | `es-ES` | silver | llm-corrected | - | 20 | 0.0029 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 65 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  |  | tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f | ð θ | s s̺ |  | ʝ | x ɣ | χ |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [ai̯] [aj] [au̯] [aw] [ei̯] [ej] [eu̯] [ew] [ia] [ie] [io] [ja] [je] [jo] [ju] [ks] [oi̯] [oj] [ua] [ue] [uo] [w] [wa] [we] [wi] [wo] [ɟʝ] [ɡw] [ɡwe] [ɡwi] [ʝa] [ʝe] [ʝo].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ai̯] | before vowel [aj] · default [ai̯] |
| ⟨au⟩ | [au̯] | before vowel [aw] · default [au̯] |
| ⟨b⟩ | [b] | intervocalic [β] |
| ⟨c⟩ | [k] [θ] | before e [θ] · before i [θ] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | intervocalic [ð] · word final [ð] |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ei̯] | before vowel [ej] · default [ei̯] |
| ⟨eu⟩ | [eu̯] | before vowel [ew] · default [eu̯] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [x] | before e [x] · before i [x] · intervocalic [ɣ] |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨güe⟩ | [ɡwe] |  |
| ⟨güi⟩ | [ɡwi] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ie⟩ | [je] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iu⟩ | [ju] |  |
| ⟨iá⟩ | [ja] | default [ja] · word initial [ia] |
| ⟨ié⟩ | [je] | default [je] · word initial [ie] |
| ⟨ió⟩ | [jo] | default [jo] · word initial [io] |
| ⟨j⟩ | [x] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ʝ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] | before consonant [n] [ŋ] · word final [n] [ŋ] |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oi⟩ | [oi̯] | before vowel [oj] · default [oi̯] |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ɾ] | before consonant [ɾ] · intervocalic [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tx⟩ | [tʃ] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] |  |
| ⟨ui⟩ | [wi] |  |
| ⟨uo⟩ | [wo] |  |
| ⟨uá⟩ | [wa] | default [wa] · word initial [ua] |
| ⟨ué⟩ | [we] | default [we] · word initial [ue] |
| ⟨uó⟩ | [wo] | default [wo] · word initial [uo] |
| ⟨v⟩ | [b] | intervocalic [β] |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ks] [s] | before consonant [s] |
| ⟨y⟩ | [ʝ] [i] | before vowel [ʝ] · default [i] |
| ⟨z⟩ | [θ] |  |
| ⟨á⟩ | [a] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ü⟩ | [w] |  |
| ⟨ý⟩ | [i] |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-r⟩ ⟨-l⟩ ⟨-d⟩ ⟨-z⟩ ⟨-j⟩ ⟨-x⟩ ⟨-k⟩ ⟨-f⟩ ⟨-t⟩ ⟨-c⟩ ⟨-b⟩ ⟨-p⟩ ⟨-g⟩ ⟨-m⟩ ⟨-ión⟩ ⟨-ad⟩ ⟨-or⟩ ⟨-al⟩ ⟨-ay⟩ ⟨-ey⟩ ⟨-oy⟩ ⟨-uy⟩. These endings take the penult: ⟨-n⟩ ⟨-s⟩ ⟨-ns⟩.

Whole-word exceptions (6): ⟨guión⟩ [ɡiˈon], ⟨muón⟩ [muˈon], ⟨pión⟩ [piˈon], ⟨prión⟩ [pɾiˈon], ⟨ruán⟩ [ruˈan], ⟨sión⟩ [siˈon].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 6 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `ES_TRILL_AFTER_CORONAL` | /ɾ/ → [r], after [n] [l] [s] | ⟨alrededor⟩ [alreðeˈðoɾ] | [Hualde 2005](#src-hualde2005), [Navarro 1977](#src-navarro1977), [Quilis 1993](#src-quilis1993) |
| `ES_NASAL_LABIAL` | /n/ → [m], before [b] [β] [p] [m] | ⟨inmaculada⟩ [immakuˈlaða] | [Hualde 2005](#src-hualde2005), [Navarro 1977](#src-navarro1977), [Quilis 1993](#src-quilis1993) |
| `ES_NASAL_VELAR` | /n/ → [ŋ], in the coda, before [k] [ɡ] [ɣ] [x] [w] | ⟨cinco⟩ [θíŋko] | [Navarro 1918](#src-navarro1918) |
| `ES_SPIRANT_B` | /b/ → [β], after [a] [e] [i] [o] [u] [ɛ] [ɔ] [æ] and 28 more | - | [Navarro 1918](#src-navarro1918) |
| `ES_SPIRANT_D` | /d/ → [ð], after [a] [e] [i] [o] [u] [ɛ] [ɔ] [æ] and 26 more | - | [Navarro 1918](#src-navarro1918) |
| `ES_SPIRANT_G` | /ɡ/ → [ɣ], after [a] [e] [i] [o] [u] [ɛ] [ɔ] [æ] and 28 more | - | [Navarro 1918](#src-navarro1918) |

The spec applies 6 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `ES_EXT_SPIRANT_B` | `[^mnŋɲ̃]$` | `^([ˈˌ]?)b` | right [β] | - | [Navarro 1918](#src-navarro1918) |
| `ES_EXT_SPIRANT_D` | `[^mnŋɲ̃lʎ]$` | `^([ˈˌ]?)d` | right [ð] | - | [Navarro 1918](#src-navarro1918) |
| `ES_EXT_SPIRANT_G` | `[^mnŋɲ̃]$` | `^([ˈˌ]?)ɡ` | right [ɣ] | - | [Navarro 1918](#src-navarro1918) |
| `ES_EXT_FINAL_N_LABIAL` | `[nŋ]$` | `^[ˈˌ]?[pbβm]` | left [m] | ⟨un buen baile⟩ [um bwem baile] | [Navarro 1918](#src-navarro1918), [Lipski 1986](#src-lipski1986), [Lipski 2011](#src-lipski_overview) |
| `ES_EXT_FINAL_N_CORONAL` | `[nŋ]$` | `^[ˈˌ]?[tdðθszlɾrnɲʎʝʃʒf]` | left [n] | - | [Navarro 1918](#src-navarro1918), [Lipski 1986](#src-lipski1986), [Lipski 2011](#src-lipski_overview) |
| `ES_EXT_FINAL_N_VELAR` | `[nŋ]$` | `^[ˈˌ]?[kɡɣxw]` | left [ŋ] | ⟨en casa⟩ [eŋ kása] | [Navarro 1918](#src-navarro1918), [Lipski 1986](#src-lipski1986), [Lipski 2011](#src-lipski_overview) |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="zona|sola|calle|cabra|la boca|hombre|el domingo|cinco|un buen baile|nación|aire|estoy|mismo|México" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "es-ES")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| zona | [ˈθona] |
| sola | [ˈsola] |
| calle | [ˈkaʝe] |
| cabra | [ˈkaβɾa] |
| la boca | [la ˈβoka] |
| hombre | [ˈombɾe] |
| el domingo | [el doˈmiŋɡo] |
| cinco | [ˈθiŋko] |
| un buen baile | [um ˈbwem ˈbai̯le] |
| nación | [naˈθjon] |
| aire | [ˈai̯ɾe] |
| estoy | [esˈtoi] |
| mismo | [ˈmismo] |
| México | [ˈmeksiko] |

The next table sets the engine output against worked examples printed in a cited source, from the [primary-source gold](../evaluation/datasets.md#primary-source-gold-primary_sources). The rows are spread evenly over that set. The last column says whether the two transcriptions are the same string.

| Spelling | Printed in the source | Engine output | Source, page | Same |
|:--|:--|:--|:--|:--|
| pelo | ˈpelo | [ˈpelo] | Martínez-Celdrán 2003, p. 255 | yes |
| feo | ˈfeo | [ˈfeo] | Martínez-Celdrán 2003, p. 255 | yes |
| nuca | ˈnuka | [ˈnuka] | Martínez-Celdrán 2003, p. 255 | yes |
| sola | ˈsola | [ˈsola] | Martínez-Celdrán 2003, p. 255 | yes |
| gato | ˈɡato | [ˈɡato] | Martínez-Celdrán 2003, p. 255 | yes |
| jarrón | xaˈron | [xaˈron] | Martínez-Celdrán 2003, p. 255 | yes |
| peso | ˈpeso | [ˈpeso] | Martínez-Celdrán 2003, p. 256 | yes |
| puso | ˈpuso | [ˈpuso] | Martínez-Celdrán 2003, p. 256 | yes |
| posó | poˈso | [poˈso] | Martínez-Celdrán 2003, p. 256 | yes |
| hacia | ˈaθja | [ˈaθja] | Martínez-Celdrán 2003, p. 256 | yes |
| bueno | ˈbweno | [ˈbweno] | Martínez-Celdrán 2003, p. 256 | yes |
| peine | ˈpei̯ne | [ˈpei̯ne] | Martínez-Celdrán 2003, p. 256 | yes |

Source: Martínez-Celdrán, E., Fernández-Planas, A.M. & Carrera-Sabaté, J. (2003). *Castilian Spanish (Illustrations of the IPA)*. Journal of the International Phonetic Association 33(2):255-259. [cambridge.org](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/39B1C556856D62AF8FC53D3F22435750/S0025100303001373a.pdf/castilian-spanish.pdf)
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Languages from A to Z](a-z.md) · [Home](../index.md) · [Arabic →](ar.md)
