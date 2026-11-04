# Basque (Euskara) and its dialects

**Code**: `eu` and seven dialect codes | **Family**: language isolate | **Script**: Latin (alphabet) | **Quality tier**: see the table below

Basque is a language isolate: it has no demonstrated genetic relationship to any other language family. The library has a spec for Standard Basque (Euskara Batua) and a spec for each of seven dialects. This page tells what each spec models. It also tells what each spec leaves out, because standard Basque orthography does not write it.

| Code | Variety | Quality tier |
|:---|:---|:---|
| `eu` | Euskara Batua (standard) | production |
| `eu-biscayan
` | Biscayan (Western) | research |
| `eu-x-gipuzkoa` | Gipuzkoan (Central) | research |
| `eu-x-nafarra-garaia` | Upper (High) Navarrese | research |
| `eu-x-nafarra-beherea` | Lower Navarrese | research |
| `eu-x-lapurdi` | Lapurdian | research |
| `eu-x-zuberera` | Souletin (Zuberoan) | research |
| `eu-x-roncal` | Roncalese (Eastern Navarrese, extinct) | research |

The claims on this page come from sources that were read directly, with page numbers. Two open-access *Illustrations of the IPA* are the most useful references. One describes Goizueta, a conservative High Navarrese variety. The other describes Markina, a Biscayan variety. Together they document the two ends of the west-to-east continuum of sound change.

## Sources read

- Hualde, Lujanbio & Zubiri (2010), "Goizueta Basque", *JIPA* 40(1): 113-127. [doi:10.1017/S0025100309990260](https://doi.org/10.1017/S0025100309990260)
- Bedialauneta Txurruka & Hualde (2023), "Markina Basque", *JIPA* 53(3): 1095-1122. [doi:10.1017/S0025100322000032](https://doi.org/10.1017/S0025100322000032)
- Hualde (2018), "Aspiration in Basque", *Papers in Historical Phonology* 3: 1-27. [doi:10.2218/pihph.3.2018.2602](https://doi.org/10.2218/pihph.3.2018.2602)
- Egurtzegi (2013), "Phonetics and Phonology", chapter 4 in Martínez-Areta (ed.), *Basque and Proto-Basque* (Peter Lang): 119-183.
- Michelena (1977), *Fonética Histórica Vasca* (FHV). It is cited by page through Egurtzegi (2013) and Hualde (2018), and the original was not consulted.

## The base inventory (`eu`, Euskara Batua)

Conservative Basque has a three-way contrast of sibilant place. This is the typologically notable feature of the language (Hualde et al. 2010: 119). The `eu` spec keeps all six sibilants apart:

| Orthography | Fricative | Affricate |
|:---|:---|:---|
| z / tz | lamino-alveolar `s̻` | `ts̻` |
| s / ts | apico-alveolar `s̺` | `ts̺` |
| x / tx | postalveolar `ʃ` | `tʃ` |

The palatal stops `c` (⟨tt⟩) and `ɟ` (⟨dd⟩), the palatal nasal `ɲ` (⟨ñ⟩) and the palatal lateral `ʎ` (⟨ll⟩) come historically from palatalisation of `t d n l` after /i/. The spec maps the four spellings directly. Palatalisation of a plain ⟨n⟩ or ⟨l⟩ after /i/ is lexically conditioned in Batua, so the spec states no rule for it. Basque has five vowels /i e a o u/ (2010: 122).

The `eu` spec applies these allophone rules:

| Rule | Effect | Source |
|:---|:---|:---|
| `EU_SPIRANT_B`, `EU_SPIRANT_D`, `EU_SPIRANT_Ɡ` | /b d ɡ/ become [β ð ɣ] after a vowel | Hualde et al. 2010: 116 |
| `NASAL_LABIAL_ASSIM` | /n/ becomes [m] before /b p m/ | Hualde et al. 2010: 120 |
| `EU_OFFGLIDE_I`, `EU_OFFGLIDE_U` and their word-final pair | a high vowel after a vowel, with no vowel after it, becomes [j] or [w] | Hualde & Ortiz de Urbina 2003 |
| `EU_TRILL_CODA`, `EU_TRILL_FINAL` | the tap /ɾ/ becomes the trill [r] in the coda | Hualde & Ortiz de Urbina 2003 |

Aspiration, as /h/ and as aspirated stops, survives only in the eastern (continental) dialects. The west lost it (Hualde 2018: 2). The `eu` spec reads ⟨h⟩ as silent.

## Dialects: the west-to-east continuum

The specs follow the modern classification of Koldo Zuazo. Western is Biscayan, and Central is Gipuzkoan. High Navarrese stands alone. Navarro-Lapurdian groups Lapurdian and Lower Navarrese. Souletin (Zuberoan) is the easternmost dialect. The extinct Eastern Navarrese dialect includes Roncalese.

Every dialect spec takes its graphemes, allophones and positional graphemes from `eu` (`graphemes_base`, `allophones_base` and `positional_graphemes_base`). It then states only its own differences.

### Biscayan: `eu-biscayan
` (Western)

The Biscayan spec follows Markina Basque (Bedialauneta & Hualde 2023). Western Basque has merged sibilant contrasts that the base keeps. The apico-alveolar `s̺` and the lamino-alveolar `s̻` merge to one apico-alveolar `s̺`. The affricates `ts̺` and `ts̻` merge to one denti-alveolar `ts̻` (2023: 1098). So the spec reads both ⟨s⟩ and ⟨z⟩ as /s̺/, and both ⟨ts⟩ and ⟨tz⟩ as /ts̻/. The palatal stop `c` (⟨tt⟩) merges with `tʃ` (2023: 1098), and the spec reads ⟨tt⟩ as [tʃ].

After /i/, the dialect palatalises /s/ to [ʃ], /t/ to [tʃ], /n/ to [ɲ] and /l/ to [ʎ] (2023: 1102-1104). The spec lists [ʃ], [ɲ] and [ʎ] as second candidates for ⟨s z⟩, /n/ and /l/. It states no rule for the /i/ context, so the first candidate stays unpalatalised. Biscayan has no aspiration (Hualde 2018: 2), and the spec keeps ⟨h⟩ silent.

The spec does not model the Biscayan raising of the article /-a/ to [-e] after a high vowel (*baso+a* > *basue*, 2023: 1107-1108). This is a morphophonological process on the article, and a context-free grapheme rule cannot state it.

### Gipuzkoan: `eu-x-gipuzkoa` (Central)

Gipuzkoan is the living dialect that is closest to Batua, and its spec adds nothing to the base. Eastern Gipuzkoan keeps the three-way sibilant contrast. In western areas the contrast varies and neutralises, because the Western merger intrudes (Bedialauneta & Hualde 2023: 1098). Gipuzkoan has no /h/ (Hualde 2018: 2). In the westernmost towns, the palatal stop `c` is merging with `tʃ` (Hualde et al. 2010: 118).

Contrastive pitch accent belongs to specific northern-Biscayan and Navarrese varieties, for example Goizueta (Hualde et al. 2010: 113, 123). It is not a feature of general Gipuzkoan, and the spec makes no pitch-accent claim for it.

### Upper (High) Navarrese: `eu-x-nafarra-garaia`

The Upper Navarrese spec follows Goizueta (Hualde et al. 2010), a conservative High Navarrese variety. The three-way sibilant contrast is fully stable here, and the neutralisations run further west (2010: 119). Goizueta has no /h/ (2010: 113 fn. 1). Yeísmo is in progress: /ʎ/ becomes [ʝ] or [j] (2010: 120). The spec lists [ʝ] as a second candidate for /ʎ/.

The spec contradicts its own source on /h/. Its `notes` say that /h/ is absent, but its `graphemes` table maps ⟨h⟩ to [h], so `haizea` gives `hai̯s̻ea`. This is an open defect in the spec data.

### Lower Navarrese: `eu-x-nafarra-beherea`

Lower Navarrese is an eastern variety with aspiration. With Lapurdian it forms the Navarro-Lapurdian dialect of Zuazo. /h/ is a productive phoneme (Hualde 2018: 1-3), and the spec reads ⟨h⟩ as [h]. Voiceless stops have aspirated variants [pʰ tʰ kʰ] in the onset of a stressed syllable near the start of the word (Hualde 2018: 5-6, reporting Michelena FHV). They are less systematically phonemic than in Souletin. The spec lists [pʰ tʰ kʰ] as second candidates for /p t k/, because a grapheme rule cannot state the stress window.

### Lapurdian: `eu-x-lapurdi`

Lapurdian is the classical literary dialect, as in Axular's *Gero* (1643). Classical Lapurdian had both /h/ and aspirated stops (Hualde 2018: 5, list (1)). Coastal French Basque lost aspiration by the 19th century (Hualde 2018: 2). So modern coastal Lapurdian keeps /h/ only residually. The spec reads ⟨h⟩ as [h] and lists silence as the second candidate.

Lapurdian keeps the full three-way sibilant contrast. Under French contact, uvular [ʁ] appears next to the inherited [r] and [ɾ]. The spec lists [ʁ] as a second candidate for both rhotics.

### Souletin (Zuberoan): `eu-x-zuberera` (easternmost)

Souletin is the most divergent variety, and it is in contact with Gascon Occitan. It has these features:

- The front rounded vowel /y/, written ⟨ü⟩. Souletin is the only Basque dialect with a sixth vowel, which came from older /u/ by fronting (Egurtzegi 2013: 127-128). The orthography writes it, and the spec maps ⟨ü⟩ to [y].
- A three-way plosive contrast: voiced, voiceless unaspirated and voiceless aspirated /pʰ tʰ kʰ/ are full phonemes (Hualde 2018: 2, citing Lafon 1958/1999). The spec maps ⟨kh⟩ to [kʰ] and lists [pʰ tʰ kʰ] as second candidates for /p t k/.
- Two aspirate phonemes, oral /h/ and nasalised /h̃/ (Hualde 2018: 2). The spec reads ⟨h⟩ as [h].
- Contrastive nasalised vowels. Souletin alone among the living dialects keeps the old series of nasalised vowels. They occur around nasal consonants and in stressed final position after loss of an old /-n/ (*ardu* [arðũ] < *ardano*, Egurtzegi 2013: 127).

Standard orthography does not write vowel nasality or the aspiration contrast on ⟨p t k⟩. So the spec documents both and emits neither as a first candidate.

### Roncalese (Eastern Navarrese): `eu-x-roncal` (extinct)

Roncalese is the Basque of the Roncal valley in easternmost Navarre. With Salazarese it forms the Eastern Navarrese dialect of Zuazo. It is extinct, and its last fluent speakers were gone by about 1991 (Egurtzegi 2013: 127). Bonaparte and Michelena's FHV document it. It has these features:

- Contrastive nasalised vowels, kept "exactly as … in the modern Souletin dialect" (Egurtzegi 2013: 127). Secondary sources report that nasalisation could reach any syllable in Roncalese, but only the final syllable in Souletin. This comes from an abstract that was not read in full.
- Eastern aspiration, /h/ and [pʰ tʰ kʰ], which was already receding (Hualde 2018: 2-3, 19). The spec reads ⟨h⟩ as [h] with silence as the second candidate, and lists [pʰ tʰ kʰ] as second candidates for /p t k/.
- High-vowel metaphony, /i/ to /u/ before /u/ (*tipula* > *tupla*, Egurtzegi 2013: 131, citing FHV: 79).
- Intense syncope, with sibilant and tap clusters that no other dialect has (*zira* > *zra* 'you are', Egurtzegi 2013: 135-136, FHV: 160).

The nasalisation, the metaphony and the syncope are historical or morphophonological, and the orthography does not show them. The spec emits only the eastern aspiration.

## Ancestry and distance

Every dialect spec declares `parent: eu` with an ancestor weight of 0.9. So `ancestry_similarity(get("eu"), get("eu-x-zuberera"))` returns 0.9, and two sibling dialects score 0.81.

## Orthographic depth and production threshold

Euskara Batua has a shallow (phonemic) orthography, so the 0.15 PER production threshold applies (see [quality tiers](../specs/quality_tiers.md#the-per-threshold)). Its spelling is regular. The palatal spellings ⟨tt dd ñ ll⟩ and the affricate digraphs ⟨tz ts tx⟩ are closed rules that a spec can encode.

Basque accent varies by dialect, and the orthography never writes it.

Batua has no official accent norm, and its spelling marks no accent. The `stress` block puts the accent on the second syllable of the word. This is the General Central [+2] pattern. Hualde (1994: 1559) proposes it for Batua, and Elordieta, Gaminde & Hualde (1998: 402) record it in Batua speech (*gizóna*, *emákumea*, *txistúlaria*).

A monosyllabic root (*lúrra*) takes the accent on the first syllable. So does a closed set of marked words (*lékuan*, *áurrera*). The spelling shows neither, so the spec does not model them.

The Eastern dialect specs (Souletin, Roncalese, Lapurdian, Lower Navarrese) declare their own penultimate [-2] block (Hualde 2022: 92, 97). Gipuzkoan inherits [+2], the General Central system (Hualde 2022: 84).

Biscayan and Upper Navarrese state `"stress": false` and print no stress marks. Each area mixes accent systems. Bizkaia has the Western systems, where most words are unaccented and the accent falls on the phrase, next to Central systems (Hualde 2022: 83, Table 1). Upper Navarre has the tonal [+2H] system of Goizueta (Hualde 2022: 84, Table 2) and the penultimate [-2] of the Baztan Valley (Hualde 2022: 80). No single block can be written for either spec.

The engine writes the stress mark inside the affricates *ts̻ ts̺* (*beltˈs̻aɾi*). The IPA segmenter does not read an affricate with a diacritic below as one segment.

## Benchmark

The `wikipron` row is crowd-scraped and is the row that can qualify `eu` for production. The `vox_communis` row is epitran-derived and the `ipa_childes` row is espeak-derived, so neither can gate a promotion. The `hitz_basque_ipa` row is machine-generated, with tool-generated transcriptions in the StyleTTS2 convention. The `spain_romance_tts` rows for `eu` and the dialects are LLM-generated, and an LLM-generated row never gates. See the [scoreboard](../evaluation/generated/scoreboard.md) for the scores.

---
[← Mongolian](mn.md) · [Home](../index.md) · [Finnish →](fi.md)
