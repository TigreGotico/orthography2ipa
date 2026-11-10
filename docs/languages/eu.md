# Basque (Euskara) (`eu`)

<!-- atlas:summary begin -->
Basque (Euskara) is a Vasconic language, written in the Latin script. Glottolog places it in France and Spain. The `eu` spec is at the production tier. It cites 10 sources and has 5 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `eu` |
| Aliases | `eus` |
| ISO 639-3 | [eus](https://iso639-3.sil.org/code/eus), Basque |
| Glottolog | [basq1248](https://glottolog.org/resource/languoid/id/basq1248), Basque |
| Wikidata | [Q8752](https://www.wikidata.org/wiki/Q8752) |
| Wikipedia | [Basque language](https://en.wikipedia.org/wiki/Basque_language) |
| Family | [Vasconic](by-family.md#vasconic) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france), [Spain](by-region.md#spain) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [production](../specs/quality_tiers.md#production) |
| Attested | from 1500, living |
| Ancestor | [Aquitanian (Proto-Basque)](https://tigregotico.github.io/orthography2ipa/#xaq) `xaq` |
| Child lects | 7, see [Related lects](#related-lects) |
| Explorer | [`eu` in the data explorer](https://tigregotico.github.io/orthography2ipa/#eu) |
| Spec file | [`eu.json`](../../orthography2ipa/data/eu.json) |
<!-- atlas:header end -->

## Overview

The `eu` spec models Standard Basque, Euskara Batua. Seven child specs model the dialects, from Biscayan in the west to Souletin in the east.

Batua writes most sounds with one letter or with a fixed digraph. The affricates are ⟨tz ts tx⟩, and the palatals are ⟨tt dd ñ ll⟩. The spelling is regular, so the 0.15 PER threshold for a shallow orthography applies (see [quality tiers](../specs/quality_tiers.md#the-per-threshold)). The spelling does not write the accent. It also does not write the aspirated stops of the eastern dialects or the nasal vowels of Souletin. This page tells what each spec models and what it leaves out.

Two *Illustrations of the IPA* are the main sources for the segments. Hualde, Lujanbio & Zubiri (2010) describe Goizueta, a town in northwestern Navarre (p. 113). Bedialauneta Txurruka & Hualde (2023) describe Markina, a town in Bizkaia on the border with Gipuzkoa (p. 1095). The two varieties sit at the two ends of the west-to-east chain of sound change. Two papers in *Euskera*, the journal of the Basque Academy [Euskaltzaindia](https://www.euskaltzaindia.eus/), give the accent of Batua.

## Sibilants and affricates

Conservative Basque contrasts three places for its sibilants. Each fricative has an affricate partner (Hualde et al. 2010: 119). The `eu` spec keeps all six segments apart:

| Spelling | Fricative | Affricate |
|:---|:---|:---|
| z / tz | lamino-alveolar [s̻] | [ts̻] |
| s / ts | apico-alveolar [s̺] | [ts̺] |
| x / tx | postalveolar [ʃ] | [tʃ] |

The contrast is fully stable in Goizueta. Further west, in many Gipuzkoan varieties and in all Bizkaian ones, neutralisations reduce it (Hualde et al. 2010: 119). After a nasal or a liquid, the fricative and the affricate neutralise in favour of the affricate (2010: 120).

## Palatals

Basque has the palatal stops [c] ⟨tt⟩ and [ɟ] ⟨dd⟩, the palatal nasal [ɲ] ⟨ñ⟩ and the palatal lateral [ʎ] ⟨ll⟩. They come from the palatalisation of /t d n l/ after /i/. Affective forms are a second source of /c/ (Hualde et al. 2010: 117, 120). The spec maps the four spellings directly.

In Goizueta, /n/ and /l/ palatalise after /i/ (2010: 120). The spec notes treat this palatalisation as lexical in Batua, so the spec states no rule for a plain ⟨n⟩ or ⟨l⟩ after ⟨i⟩.

In the speech of younger Goizueta speakers, /ʎ/ loses its lateral contact and merges with the palatal approximant [j] (2010: 114, 120). In northern Bizkaian and western Gipuzkoan areas, /c/ has merged or is merging with /tʃ/ (2010: 119).

## Stops, spirants and nasals

The voiced stops /b d ɡ/ are approximants after a vowel and in most contexts after a consonant (Hualde et al. 2010: 116). Examples are *alaba* [aláβa] and *adarra* [aðára]. The rules `EU_SPIRANT_B`, `EU_SPIRANT_D` and `EU_SPIRANT_Ɡ` write [β ð ɣ] after a vowel only. Markina also has [ð] after a consonant, as in *talde* [talðe] (Bedialauneta Txurruka & Hualde 2023: 1104).

A nasal takes the place of articulation of the next consonant (Hualde et al. 2010: 120). Markina shows this in *kanpo* [kampo] and *ango* [aŋgo] (2023: 1103). The spec has only the labial rule `NASAL_LABIAL_ASSIM`, which changes /n/ to [m] before /b p m/.

After the negative particle *ez*, a voiced stop becomes voiceless. Examples are *ez dakit* [estakit] and *ez dator* [estator] (2023: 1101). The spec writes this sandhi, and *ez dakit* gives [ˈes̻ taˈkit].

## Rhotics, vowels and diphthongs

The tap and the trill contrast only between vowels. In all other positions the trill occurs (Hualde et al. 2010: 120). Markina has a trill in the coda, as in *parkatu* and *sartu* (2023: 1104). The rules `EU_TRILL_CODA` and `EU_TRILL_FINAL` write the trill [r] for the tap in the coda (Hualde & Ortiz de Urbina 2003).

Basque has five vowels, /i e a o u/ (Hualde et al. 2010: 121). The falling diphthongs are [ai̯ ei̯ oi̯ au̯ eu̯] (2010: 121), and Markina adds [ui̯] in *duin* (2023: 1107). A sequence of rising sonority is a hiatus, and so is a sequence of two high vowels (2010: 122, 2023: 1108). Four rules write a high vowel after a vowel as [j] or [w] when no vowel follows (Hualde & Ortiz de Urbina 2003). They are `EU_OFFGLIDE_I`, `EU_OFFGLIDE_U` and their word-final pair.

## Aspiration

Most living dialects have no aspiration, as /h/ or as an aspirated stop. The varieties north of the Pyrenees, in France, have /h/ from the first texts until the present (Hualde 2018: 1-2). The coastal area of the French Basque Country lost aspiration in the 19th century (2018: 2, fn. 1).

The aspirating varieties have three series of stops: /b d ɡ/, /p t k/ and /pʰ tʰ kʰ/ (2018: 2). The modern spelling writes the aspirated stops as ⟨ph th kh⟩ (2018: 3). A word has at most one aspirate, and it occurs in one of the first two syllables (2018: 2-3). Michelena relates this aspiration to the onset of the stressed syllable (2018: 5-6).

The `eu` spec reads ⟨h⟩ as silent, so *haizea* gives [ai̯ˈs̻ea]. The eastern dialect specs read ⟨h⟩ as [h].

## Accent

The spelling never writes the accent. Hualde (1994: 1559) proposes an accent for Batua: the second syllable of the word takes the accent, as in *mendía*, *txakúrra* and *emákumea*. This is the General Central [+2] system (Hualde 2022: 84, Table 2). Elordieta, Gaminde & Hualde (1998: 402) record it in the Batua of young speakers in Donostia, as in *gizóna*, *autóbusa*, *txistúlaria* and *basóa*. The `stress` block of `eu` puts the accent on the second syllable.

Some words take the accent on the first syllable. Hualde (1994: 1559) names words with a root of one syllable (*lurra*, *lurrera*) and a set of marked words (*lekuan*, *aurrera*, *atzetik*). The young Donostia speakers also stress the first syllable of a disyllable that ends in a vowel (*áte*, *méndi*). They do the same for a word with a root of one syllable (*lúrrari*, *béltzari*) (1998: 402). The spelling shows none of these conditions. The spec notes keep [+2] for the disyllables on purpose, after Elordieta et al. (1998: 403).

Rule III of Hualde (1994: 1559) puts a second accent on the last syllable of the phrase. The spec does not model the phrase accent.

The accent systems differ by area. The Western-Central area runs from Getxo to Arantza, and the Eastern area has its own systems (Hualde 2022: 80). East of the Bidasoa, the accent is on the second syllable from the end, [-2] (2022: 92). The Souletin, Roncalese, Lapurdian and Lower Navarrese specs declare this [-2] block (2022: 92, 97). Gipuzkoan inherits the [+2] block of `eu` (2022: 84).

The Biscayan and Upper Navarrese specs state `"stress": false` and print no stress marks, because each area mixes systems. Bizkaia has the Western systems, in which most words have no lexical accent and the accent falls on the phrase (2022: 83, Table 1). Upper Navarre has the tonal [+2H] system of Goizueta (2022: 84, Table 2) and the [-2] of the Baztan Valley (2022: 80, fn. 5). In Goizueta, both the place of the stress and its tone are lexically contrastive (Hualde et al. 2010: 123). One `stress` block cannot hold either area.

## The dialects

The notes of `eu-x-lapurdi`, `eu-x-nafarra-beherea` and `eu-x-roncal` name the classification of Koldo Zuazo. In the spec notes, Biscayan is the Western dialect and Gipuzkoan is the Central dialect. Lapurdian and Lower Navarrese form the Navarro-Lapurdian dialect. Roncalese is extinct and belongs to Eastern Navarrese.

| Spec | Variety | Main source of the spec |
|:---|:---|:---|
| [`eu-biscayan`](eu-biscayan.md) | Biscayan (Western) | Bedialauneta Txurruka & Hualde (2023), Markina |
| [`eu-x-gipuzkoa`](eu-x-gipuzkoa.md) | Gipuzkoan (Central) | Hualde et al. (2010), Bedialauneta Txurruka & Hualde (2023) |
| [`eu-x-nafarra-garaia`](eu-x-nafarra-garaia.md) | Upper Navarrese | Hualde et al. (2010), Goizueta |
| [`eu-x-nafarra-beherea`](eu-x-nafarra-beherea.md) | Lower Navarrese | Hualde (2018) |
| [`eu-x-lapurdi`](eu-x-lapurdi.md) | Lapurdian | Hualde (2018) |
| [`eu-x-zuberera`](eu-x-zuberera.md) | Souletin (Zuberoan) | Hualde (2018), Egurtzegi (2013) |
| [`eu-x-roncal`](https://tigregotico.github.io/orthography2ipa/#eu-x-roncal) | Roncalese (extinct) | Egurtzegi (2013), Hualde (2018) |

Every dialect spec takes its graphemes, allophones and positional graphemes from `eu`, through `graphemes_base`, `allophones_base` and `positional_graphemes_base`. It then states only its own differences.

### Biscayan

The Biscayan spec follows Markina. Markina, like all varieties of Bizkaia and Araba and many Gipuzkoan ones, merges ⟨s⟩ and ⟨z⟩ into one apico-alveolar /s/. The affricates merge into one lamino-dental affricate, and /c/ merges with /tʃ/ (Bedialauneta Txurruka & Hualde 2023: 1098). So the spec reads both ⟨s⟩ and ⟨z⟩ as [s̺], both ⟨ts⟩ and ⟨tz⟩ as [ts̻], and ⟨tt⟩ as [tʃ].

After /i/, Markina palatalises /s/ to [ʃ], /t/ to [tʃ], /n/ to [ɲ] and /l/ to [ʎ] (2023: 1102-1104). The spec lists [ʃ], [ɲ] and [ʎ] as second candidates. It states no rule for the /i/ context, so the first candidate stays plain. Biscayan has no aspiration (Hualde 2018: 2), and the spec keeps ⟨h⟩ silent.

After a high vowel, the article *-a* becomes *-e*, as in *basue* 'the forest' (2023: 1107-1108). This is a process on the article, and a grapheme rule without context cannot state it, so the spec does not model it.

### Gipuzkoan

The Gipuzkoan spec differs from the base in one value. It gives ⟨h⟩ no [h] candidate, where `eu` lists [h]. Both read ⟨h⟩ as silent first, so *haizea* gives [ai̯ˈs̻ea] in both. Its notes call Gipuzkoan the living dialect closest to Batua. Many Gipuzkoan varieties merge ⟨s⟩ and ⟨z⟩ as the Western dialect does (Bedialauneta Txurruka & Hualde 2023: 1098, Hualde et al. 2010: 119). Gipuzkoan has no /h/ (Hualde 2018: 2). In western Gipuzkoan areas, /c/ is merging with /tʃ/ (Hualde et al. 2010: 119). The spec notes cite Hualde et al. (2010: 113, 123-124) for the absence of a lexical pitch accent of the Goizueta type in general Gipuzkoan.

### Upper Navarrese

The Upper Navarrese spec follows Goizueta. The three-way sibilant contrast is fully stable there (Hualde et al. 2010: 119). The consonants that Goizueta lost in its history are not in its inventory (2010: 114, fn. 1). Example (4) writes the lost consonants in parentheses, and /h/ is one of them, as in *bi(h)ár* [biár] 'tomorrow' (2010: 122). In younger speech, /ʎ/ merges with [j] (2010: 120). The spec lists [ʝ] as a second candidate for /ʎ/.

### Lower Navarrese

Lower Navarrese is an eastern variety with aspiration. /h/ is a phoneme (Hualde 2018: 1-3), and the spec reads ⟨h⟩ as [h]. The voiceless stops have aspirated forms [pʰ tʰ kʰ] in the onset of a stressed syllable near the start of the word (2018: 5-6, after Michelena). A grapheme rule cannot state this stress window, so the spec lists [pʰ tʰ kʰ] as second candidates for /p t k/.

### Lapurdian

Classical Lapurdian is the language of Axular's *Gero* (1643), which represents the speech of Sara (Hualde 2018: 3). It had both /h/ and aspirated stops (2018: 4-5, list (1)). The coastal area lost aspiration in the 19th century (2018: 2, fn. 1). So the spec reads ⟨h⟩ as [h] and lists silence as the second candidate.

The spec notes say that Lapurdian keeps the full three-way sibilant contrast. The spec lists the uvular [ʁ] as a second candidate for both rhotics, as a French contact feature. No source of the spec gives a page for this feature.

### Souletin

Souletin is the easternmost dialect. It has these features:

- A sixth vowel, the front rounded /y/, written ⟨ü⟩. Egurtzegi (2013: 127-128) derives it from an older /u/. The spec maps ⟨ü⟩ to [y].
- Three series of stops: voiced, voiceless and aspirated (Hualde 2018: 2, after Lafon). The spec maps ⟨kh⟩ to [kʰ] and lists [pʰ tʰ kʰ] as second candidates for /p t k/.
- Two aspirates, oral /h/ and nasal /h̃/ (Hualde 2018: 2). The spec reads ⟨h⟩ as [h].
- Nasal vowels. Egurtzegi (2013: 126-127) finds them next to a nasal consonant and in a stressed final syllable that lost an old /-n/, as in *ardu* [arðũ] from *\*ardano*.
- The accent on the second syllable from the end, and on the last syllable after a contraction, as in *alhabá* (Hualde 2022: 97).

The spelling does not write the nasal vowels or the aspiration on ⟨p t k⟩. So the spec documents both and emits neither as a first candidate.

### Roncalese

Roncalese is the Basque of the Roncal valley in easternmost Navarre. Egurtzegi (2013: 126) states that it disappeared in the 20th century. Bonaparte and Michelena documented it. It has these features:

- Nasal vowels. Egurtzegi (2013: 126) states that Souletin keeps them "exactly as they were found in the defunct Roncalese variety".
- A /k-/ in demonstratives where other dialects have /h-/, as in *kaur* 'this' for *haur* and *kori* 'that' for *hori* (Hualde 2018: 13).
- Metaphony of /i/ to /u/ before /u/. Egurtzegi (2013: 131), after Michelena, gives *tipula* > *tupla* 'onion'.
- Strong syncope. Egurtzegi (2013: 135), after Michelena, gives a syncope between a sibilant and a tap that only Roncalese and Salazarese show, as in *zira* > *zra* 'you are'.

The nasal vowels, the metaphony and the syncope are historical or morphological processes, and the spelling does not show them. The spec emits only the eastern aspiration. It reads ⟨h⟩ as [h] with silence as the second candidate. It lists [pʰ tʰ kʰ] as second candidates for /p t k/.

## Ancestry and distance

Every dialect spec declares `parent: eu` with an ancestor weight of 0.9. So `ancestry_similarity(get("eu"), get("eu-x-zuberera"))` returns 0.9, and two sibling dialects score 0.81.

## Reference data and tools

Five provenance tiers never gate a promotion: the three that name a competing tool (`espeak-derived`, `epitran-derived` and `lupo-derived`) and the two language-model tiers ([which gold can gate](../specs/quality_tiers.md#which-gold-can-gate)). The `Gates` column of the Datasets block below gives the rows that gate.

The `wikipron` row is crowd-scraped Wiktionary data. The source of the `hitz_basque_ipa` row is [HiTZ/wikipedia_basque_ipa](https://huggingface.co/datasets/HiTZ/wikipedia_basque_ipa).

The [dataset catalogue](../evaluation/datasets.md) gives it as the output of the ahoNT phonemizer of HiTZ Zentroa and AhoLab. Its tier is `machine-generated`, which can gate.

The catalogue gives the `vox_communis` row the tier `epitran-derived` and the `ipa_childes` row the tier `espeak-derived`. The `spain_romance_tts` row is `llm-corrected` silver.

The README of [TigreGotico/ahotts-g2p](https://github.com/TigreGotico/ahotts-g2p) describes it as a pure-Python port of the [AhoTTS](https://github.com/aholab/AhoTTS) front end. It writes the single-character IPA string that StyleTTS2 and VITS models read. The [dataset catalogue](../evaluation/datasets.md) tells a reader to compare AhoTTS through this port on the `wikipron` row.

The README of [TigreGotico/euskaphone](https://github.com/TigreGotico/euskaphone) describes it as a dialect-aware Basque phonemizer and TTS front end on the lattice of this library, in which each dialect is a Basque lect spec.

## Weak points

The engine output below comes from `orthography2ipa.transcribe` on the worked examples of the sources.

| Word | Source form | `eu` output | Problem |
|:---|:---|:---|:---|
| *lurra* | *lúrra* (Hualde 1994: 1559) | [luˈra] | The accent is on the second syllable. The root has one syllable. |
| *lurrari* | *lúrrari* (Elordieta et al. 1998: 402) | [luˈraɾi] | Same cause. |
| *beltzari* | *béltzari* (1998: 402) | [beltˈs̻aɾi] | The accent is on the wrong syllable, and the mark splits the affricate. |
| *lekuan* | *lékuan* (Hualde 1994: 1559) | [leˈkuan] | The spec has no list of marked words. |
| *aurrera* | *áurrera* (1994: 1559) | [au̯ˈreɾa] | Same cause. |
| *ango* | [aŋgo] (Bedialauneta Txurruka & Hualde 2023: 1103) | [anˈɡo] | No velar assimilation. Only the labial rule exists. |
| *talde* | [talðe] (2023: 1104) | [talˈde] | No spirant after a consonant. |
| *ilargi* | spirant after a consonant (Hualde et al. 2010: 116) | [iˈlarɡi] | Same cause. |

The engine puts the stress mark inside the affricates [ts̻] and [ts̺]. Examples are *atzo* [atˈs̻o], *eutsi* [eu̯tˈs̺i] and *bertsolariarekin* [bertˈs̺olaɾiaɾekin]. The IPA segmenter does not read an affricate with a diacritic below its second symbol as one segment. [tʃ] has no such diacritic, and *etxe* gives [eˈtʃe].

The spec keeps [+2] in *ate* [aˈte] and *mendi* [menˈdi], where young Donostia speakers have [+1] (Elordieta et al. 1998: 402). This is a choice that the spec notes state. *mina* gives [miˈna], where Markina has /miɲe/ (2023: 1103). This is also a choice, because the spec notes treat the palatalisation as lexical in Batua.

The dialect specs have these defects in their data:

- `eu-x-nafarra-garaia`: the notes say that /h/ is absent, but the letter table maps ⟨h⟩ to [h]. So *haizea* gives [hai̯s̻ea].
- `eu-x-lapurdi`, `eu-x-nafarra-beherea` and `eu-x-roncal`: the letter table has no ⟨kh⟩, so *khe* gives [ˈkhe] with two segments. Only `eu-x-zuberera` maps ⟨kh⟩ to [kʰ], although the modern spelling of all aspirating varieties uses ⟨ph th kh⟩ (Hualde 2018: 3).
- `eu-x-roncal`: the notes cite Hualde (2018: 2-3) for a receding Roncalese aspiration. Those pages describe the eastern dialects and the receding aspiration in general, but they do not name Roncalese.

<!-- atlas:lects begin -->
## Related lects

These specs name `eu` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Biscayan Basque (Bizkaiera)](eu-biscayan.md) `eu-biscayan`: research tier
- [Gipuzkoan Basque (Gipuzkera)](eu-x-gipuzkoa.md) `eu-x-gipuzkoa`: research tier
- [Lapurdian Basque (Lapurtera)](eu-x-lapurdi.md) `eu-x-lapurdi`: research tier
- [Lower Navarrese Basque](eu-x-nafarra-beherea.md) `eu-x-nafarra-beherea`: research tier
- [Upper Navarrese Basque](eu-x-nafarra-garaia.md) `eu-x-nafarra-garaia`: research tier
- [Roncalese Basque (Erronkariera)](https://tigregotico.github.io/orthography2ipa/#eu-x-roncal) `eu-x-roncal`: research tier
- [Souletin Basque (Zuberera)](eu-x-zuberera.md) `eu-x-zuberera`: research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 10 works. 7 of them have a DOI or a URL. The spec file holds a note on what 8 of them support.

1. <a id="src-hualde_ortiz_de_urbina2003"></a>Hualde, J.I. & Ortiz de Urbina, J. (eds.) (2003). *A Grammar of Basque*. Mouton de Gruyter. Cited: 15-65 (Hualde, 'Segmental phonology').
2. <a id="src-hualde_lujanbio_zubiri2010"></a>Hualde, J.I., Lujanbio, O. & Zubiri, J.J. (2010). *Goizueta Basque (Illustrations of the IPA)*. Journal of the International Phonetic Association 40(1). Cited: 113-127. [doi.org](https://doi.org/10.1017/S0025100309990260)
3. <a id="src-bedialauneta_hualde2023"></a>Bedialauneta Txurruka, I. & Hualde, J.I. (2023). *Markina Basque (Illustration of the IPA)*. Journal of the International Phonetic Association 53(3). Cited: 1095-1122. [doi.org](https://doi.org/10.1017/S0025100322000032)
4. <a id="src-hualde2018_aspiration"></a>Hualde, J.I. (2018). *Aspiration in Basque*. Papers in Historical Phonology 3. Cited: 1-27. [doi.org](https://doi.org/10.2218/pihph.3.2018.2602)
5. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
6. <a id="src-hualde1991"></a>Hualde, J.I. (1991). *Basque Phonology*. Routledge (Theoretical Linguistics series). Cited: ch. 'The negative particle ez' / consonant assimilation sandhi.
7. <a id="src-hualde1994_batua"></a>Hualde, J.I. (1994). *Euskal azentuak eta euskara batua*. Euskera 39 (2. aldia), Euskaltzaindia. Cited: 1549-1568. [euskaltzaindia.eus](https://www.euskaltzaindia.eus/dok/euskera/50051.pdf)
8. <a id="src-elordieta_gaminde_hualde1998"></a>Elordieta, G., Gaminde, I. & Hualde, J.I. (1998). *Euskal azentua gaur eta bihar*. Euskera 43 (2. aldia), Euskaltzaindia. Cited: 399-423. [euskaltzaindia.eus](https://www.euskaltzaindia.eus/dok/euskera/49465.pdf)
9. <a id="src-hualde2022_ocb"></a>Hualde, J.I. (2022). *The reconstruction of Old Common Basque accentuation: Closing open issues*. Anuario del Seminario de Filología Vasca Julio de Urquijo (ASJU) 56(2). Cited: 77-106. [doi.org](https://doi.org/10.1387/asju.23983)
10. <a id="src-hualde1986_tone_stress"></a>Hualde, J.I. (1986). *Tone and Stress in Basque: a Preliminary Study*. Anuario del Seminario de Filología Vasca Julio de Urquijo (ASJU) 20(3). Cited: 867-896. [ojs.ehu.eus](https://ojs.ehu.eus/index.php/ASJU/article/download/7813/7007)
<!-- atlas:sources end -->

### Notes on the sources

The list below adds what each work supports, with the page.

- Hualde, Lujanbio & Zubiri (2010), "Goizueta Basque", *JIPA* 40(1): 113-127. The consonants and their allophones (pp. 114-120), the vowels and diphthongs (pp. 121-122), and the lexical stress and tone (p. 123).
- Bedialauneta Txurruka & Hualde (2023), "Markina Basque", *JIPA* 53(3): 1095-1121. The Western mergers (p. 1098), the sandhi after *ez* (p. 1101), the palatalisation and assimilation (pp. 1102-1104), and the article after a high vowel (pp. 1107-1108).
- Hualde (2018), "Aspiration in Basque", *Papers in Historical Phonology* 3: 1-27, open access at [journals.ed.ac.uk](https://journals.ed.ac.uk/pihph/article/view/2602). The distribution of /h/ and of the aspirated stops (pp. 1-6), and the Roncalese demonstratives (p. 13).
- Hualde (1994), *Euskal azentuak eta euskara batua*, *Euskera* 39. The [+2] proposal for Batua and its exceptions (p. 1559).
- Elordieta, Gaminde & Hualde (1998), *Euskal azentua gaur eta bihar*, *Euskera* 43. The accent of young Batua speakers in Donostia (pp. 402-403).
- Hualde (2022), ASJU 56(2), open access at [ojs.ehu.eus](https://ojs.ehu.eus/index.php/ASJU/article/view/23983). The accent areas (p. 80), the Western and Central systems (pp. 83-84, Tables 1 and 2), and the Eastern [-2] (pp. 92, 97).
- Egurtzegi (2013), "Phonetics and Phonology", chapter 4 in Martínez-Areta (ed.), *Basque and Proto-Basque* (Peter Lang): 119-183. An author copy with the page numbers of the book is open at [phonetik.uni-muenchen.de](https://www.phonetik.uni-muenchen.de/personen/assoziierte_wissenschaftler/egurtzegi_ander/2013_protobasque_phonology.pdf). The nasal vowels and the end of Roncalese (pp. 126-127), the Souletin /y/ (pp. 127-128), the metaphony (p. 131) and the syncope (p. 135).
- Hualde & Ortiz de Urbina (2003), *A Grammar of Basque*. The spec cites it for the off-glide and trill rules. This page did not re-open it.
- Michelena (1977), *Fonética Histórica Vasca* (FHV). It is cited by page through Egurtzegi (2013) and Hualde (2018). The original was not consulted.

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `eu` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 12008 | 0.0546 | yes |
| `hitz_basque_ipa` ([HiTZ/wikipedia_basque_ipa](https://huggingface.co/datasets/HiTZ/wikipedia_basque_ipa)) | `eu` | generated | machine-generated | CC BY-SA 4.0 | 3113 | 0.0984 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `eu` | generated | espeak-derived | CC BY 4.0 | 3969 | 0.0821 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `eu` | generated | epitran-derived | CC0 1.0 | 63415 | 0.0429 | no |
| `spain_romance_tts` | `eu` | silver | llm-corrected | Apache-2.0 (this repository) | 26 | 0.0436 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 41 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  | c ɟ | k ɡ |  |
| Affricate |  |  |  | ts̺ ts̻ | tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f | ð | s̺ s̻ | ʃ |  | x ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [ai̯] [au̯] [ei̯] [eu̯] [oi̯] [ui̯] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ai̯] |  |
| ⟨au⟩ | [au̯] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [ɟ] |  |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ei̯] |  |
| ⟨eu⟩ | [eu̯] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] [x] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oi̯] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] | before consonant [r] · intervocalic [ɾ] · word final [r] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s̺] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts̺] |  |
| ⟨tt⟩ | [c] |  |
| ⟨tx⟩ | [tʃ] |  |
| ⟨tz⟩ | [ts̻] |  |
| ⟨u⟩ | [u] |  |
| ⟨ui⟩ | [ui̯] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨z⟩ | [s̻] |  |
| ⟨ñ⟩ | [ɲ] |  |

Stress falls on the second syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 10 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NASAL_LABIAL_ASSIM` | /n/ → [m], before [b] [p] [m] | ⟨anbulantzia⟩ [ambulants̩ia] | [Hualde 2010](#src-hualde_lujanbio_zubiri2010), Lujanbio & Zubiri 2010 |
| `EU_SPIRANT_B` | /b/ → [β], after a vowel | ⟨abere⟩ [aβeɾe] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_SPIRANT_D` | /d/ → [ð], after a vowel | ⟨adar⟩ [aðar] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_SPIRANT_Ɡ` | /ɡ/ → [ɣ], after a vowel | ⟨egin⟩ [eɣin] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_OFFGLIDE_I` | /i/ → [j], after a vowel, before a consonant | ⟨ai⟩ [aj] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_OFFGLIDE_I_FINAL` | /i/ → [j], word-finally, after a vowel | ⟨ai⟩ [aj] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_OFFGLIDE_U` | /u/ → [w], after a vowel, before a consonant | ⟨au⟩ [aw] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_OFFGLIDE_U_FINAL` | /u/ → [w], word-finally, after a vowel | ⟨au⟩ [aw] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_TRILL_CODA` | /ɾ/ → [r], before a consonant | ⟨adar⟩ [aðar] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |
| `EU_TRILL_FINAL` | /ɾ/ → [r], word-finally | ⟨adar⟩ [aðar] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), Ortiz de Urbina 2003 |

The spec applies 6 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `EU_EZ_D_DEVOICE` | `^[ˈˌ]?es̻$` | `^([ˈˌ]?)d` | right [t] | ⟨eztut⟩ [es̻ tut] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), [Hualde 1991](#src-hualde1991), Ortiz de Urbina 2003 |
| `EU_EZ_Z_AFFRICATE` | `^([ˈˌ]?)es̻$` | `^([ˈˌ]?)s̻` | left [e], right [ts̻] | - | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), [Hualde 1991](#src-hualde1991), Ortiz de Urbina 2003 |
| `EU_EZ_N_ASSIM` | `^([ˈˌ]?)es̻$` | `^[ˈˌ]?n` | left [e] | ⟨enaiz⟩ [e nais̻] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), [Hualde 1991](#src-hualde1991), Ortiz de Urbina 2003 |
| `EU_EZ_L_ASSIM` | `^([ˈˌ]?)es̻$` | `^[ˈˌ]?l` | left [e] | ⟨eluke⟩ [e luke] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), [Hualde 1991](#src-hualde1991), Ortiz de Urbina 2003 |
| `EU_EZ_B_DEVOICE` | `^[ˈˌ]?es̻$` | `^([ˈˌ]?)b` | right [p] | ⟨ezpalitz⟩ [es̻ palits̻] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), [Hualde 1991](#src-hualde1991), Ortiz de Urbina 2003 |
| `EU_EZ_G_DEVOICE` | `^[ˈˌ]?es̻$` | `^([ˈˌ]?)ɡ` | right [k] | ⟨ezkara⟩ [es̻ kaɾa] | [Hualde 2003](#src-hualde_ortiz_de_urbina2003), [Hualde 1991](#src-hualde1991), Ortiz de Urbina 2003 |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="gizona|autobusa|txistularia|lurra|beltzari|lekuan|aurrera|atzo|ango|talde|kanpo|parkatu|ez dakit|haizea" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "eu")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| gizona | [ɡiˈs̻ona] |
| autobusa | [au̯ˈtoβus̺a] |
| txistularia | [tʃis̺ˈtulaɾia] |
| lurra | [luˈra] |
| beltzari | [beltˈs̻aɾi] |
| lekuan | [leˈkuan] |
| aurrera | [au̯ˈreɾa] |
| atzo | [atˈs̻o] |
| ango | [anˈɡo] |
| talde | [talˈde] |
| kanpo | [kamˈpo] |
| parkatu | [parˈkatu] |
| ez dakit | [ˈes̻ taˈkit] |
| haizea | [ai̯ˈs̻ea] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

| Repository | What it does with this spec |
|:--|:--|
| [euskaphone](https://github.com/TigreGotico/euskaphone) | A dialect-aware Basque phonemizer over the orthography2ipa lattice. |
<!-- atlas:related end -->

---
[← Bashkir](ba.md) · [Home](../index.md) · [Bats →](bbl.md)
