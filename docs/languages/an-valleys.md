# Pyrenean-valley Aragonese subdialects: Phonology Reference

**Codes**: `an-x-ansotano`, `an-x-cheso`, `an-x-chistau`, `an-x-belsetan`, `an-x-tensino` | **Family**: Indo-European > Romance | **Script**: Latin (alphabet) | **Parent**: `an` (Aragonese)

These five specs model the classic High Aragonese (*altoaragonés*) varieties of the Pyrenean valleys. Each one is a thin delta spec over the base Aragonese spec [`an`](../../orthography2ipa/data/an.json). The two regional specs `an-x-occident` (Western) and `an-x-oriental` (Ribagorçan) cover different cuts of the dialect continuum, outside the valleys.

| Valley | Code | Quality tier |
|:---|:---|:---|
| Ansó | `an-x-ansotano` | skeleton |
| Hecho | `an-x-cheso` | research |
| Gistaín (Chistau) | `an-x-chistau` | research |
| Bielsa | `an-x-belsetan` | research |
| Tena | `an-x-tensino` | skeleton |

## The shared base

Each valley spec sets `graphemes_base`, `allophones_base` and `positional_graphemes_base` to `"an"`, so it inherits everything general to Aragonese. The base keeps Latin initial F- as [f], as in *feito* and *fillo*. It keeps the /θ/ distinción for ⟨z⟩ and for ⟨c⟩ before a front vowel. It maps ⟨ll⟩ to the palatal lateral /ʎ/, with no yeísmo. It reads ⟨ch⟩ as [tʃ] and ⟨x⟩ as /ʃ/. The diphthongs from Latin Ĕ and Ŏ are in the spelling, and the base reads ⟨ie ue⟩ as [je we].

## Why the specs are thin

Aragonese orthography (the Grafía de Uesca and the Academia norms) is mostly phonemic. Much of what separates one valley from another is lexical or morphological: articles, verb endings and individual etyma. That variation shows in the spelling, not in the map from grapheme to IPA.

The Belsetán word *feto* (from FACTU, against general *feito*) is an example. It is spelled with ⟨t⟩, so the base map reads it correctly, and there is nothing to add at the phoneme level. So these specs model only the few deltas that are phonological. Each spec records its lexical and morphological features in its own `notes` and does not encode them as grapheme rules.

## Modelled deltas

| Valley (code) | Delta at the phoneme level | Spec field | Source |
|:---|:---|:---|:---|
| Cheso `an-x-cheso` | ⟨ix⟩ is [ʃ] with no epenthesis. The base offers [ʃ iʃ jʃ] for ⟨ix⟩, and Cheso keeps only [ʃ] | `graphemes` | Kuhn 1935 (through es.wikipedia, secondary) |
| Ansotano `an-x-ansotano` | Word-final ⟨r⟩ is deleted in Ansó. Fago and Hecho keep it | `positional_graphemes`, `r.word_final` | Barcos 2007 (secondary) |
| Belsetán `an-x-belsetan` | Geminates stay: ⟨l·l⟩ is [lː] and ⟨n·n⟩ is [nː] | `graphemes` | Badía Margarit 1950 (secondary) |
| Chistabín `an-x-chistau` | Geminates stay, and word-final ⟨r⟩ is deleted | `graphemes`, `positional_graphemes` | Blas Gabarda & Romanos 2008, Mott 1989 |
| Tensino `an-x-tensino` | The article forms *ro, ra, ros, ras* have the tap [ɾ], not the trill [r] that the base gives at the start of a word | `word_exceptions` | Vázquez Obrador 2021 (read directly) |

The Cheso delta does not change the top candidate for *buixo*, which is `ˈbwiʃo` in both `an` and `an-x-cheso`. It removes the [iʃ] and [jʃ] alternatives from the candidate set.

The source describes the Tensino tap after a vowel. The spec states it as whole-word entries, so the four article forms take [ɾ] in every context, including after a consonant.

```python
from orthography2ipa import G2P
G2P("an-x-cheso").transcribe_word("buixo")      # ˈbwiʃo
G2P("an-x-ansotano").transcribe_word("fablar")  # faˈbla
G2P("an-x-belsetan").transcribe_word("bel·la")  # ˈbelːa
G2P("an-x-belsetan").transcribe_word("pen·na")  # ˈpenːa
G2P("an-x-chistau").transcribe_word("comer")  # koˈme
G2P("an-x-chistau").transcribe_word("bel·lota")  # beˈlːota
G2P("an-x-tensino").transcribe_word("ro")       # ˈɾo
```

For comparison, the base spec `an` gives `faˈblaɾ` for *fablar* and `ˈbella` for *bel·la*.

## Not modelled

These features are in each spec's `notes` and stay out of the grapheme rules on purpose:

| Valley | Features left to `notes` |
|:---|:---|
| Cheso | Loss of [tʃ] in a closed set of etyma (*itar* from IECTARE, *hermano* from GERMANU), which the spelling already shows. Infinitive final /r/ kept even before enclitics, the contrast with Ansotano. The article *o/a/os/as*. The auxiliary *ser*. Agreement of the participle with the object |
| Ansotano | Intervocalic -d- kept (*odir*). Conservative morphology |
| Belsetán | -CT- to -t- (*feto*), -ULT- to -ut- (*muto*), NOCTE to *nuet*. -LL- to -r- in the pronouns *er, ers* (Gascon influence). The article *el/la/es/las*. Archaic *nusaltros/vusaltros*. Unstressed strong perfects (*tenié, trayé, benié*) |
| Chistabín | Voicing of intervocalic Latin voiceless stops (*caixigo, cadiera, radigón*). The article *el/la/es/las*. The 1PL verb ending -m (a Ribagorçan parallel). Participles in -au/-iu. Agreement of the participle with the object |
| Tensino | Cacuminal ⟨-ch-⟩ [tʃ] where general Aragonese has -ll- (*estach, gricha*). Intervocalic -p-, -t-, -k- kept. The preterite in -ós (*puyós, cantós*). The conditional in -arba/-erba/-irba |

## Geography of the diphthongs

Várvaro (1991) traces the medieval *ué* and *uá* isoglosses across these valleys. The study is *De la escritura al habla: la diptongación de O breve tónica en el Alto Aragón*, in *AFA* XLVI-XLVII, pp. 245-268. Hecho shows only *ué* (printed page 250). *uá* occurs in the Valle de Tena and in the modern *uá* area at Bielsa (page 250). The Ansó documents have no *uá* (page 250). Gistaín shows *ué* (page 251).

Várvaro (1991) is the one primary study read in full for these specs. The synchronic phonetics of each valley come from the Spanish Wikipedia dialect articles, which are secondary. For Chistabín and Tensino they come from an online summary read directly and from Vázquez Obrador (2021). The `sources` field of each spec gives the provenance of each claim.

## Sources

- Kuhn, A. (1935). *Der hocharagonesische Dialekt.* Revue de Linguistique Romane XI: 1-312. The classic monograph on High Aragonese and the basis for Ansó and Hecho. Consulted through secondary summaries, because the original was not available.
- Badía Margarit, A. M. (1950). *El habla del valle de Bielsa (Pirineo aragonés).* CSIC. Belsetán geminates and the -CT- and -ULT- reductions.
- Nagore Laín, F. (1986). *El aragonés de Panticosa. Gramática.* Instituto de Estudios Altoaragoneses. The reference grammar for Tensino.
- Blas Gabarda, F. & Romanos Hernando, F. (2008). *Diccionario aragonés chistabín (Bal de Chistau).* Gara d'Edizions.
- Mott, B. (1989). *El habla de Gistaín.* Instituto de Estudios Altoaragoneses.
- Barcos, M. A. (2007). *El aragonés ansotano: estudio lingüístico de Ansó y Fago.* Gara d'Edizions. The contrast in final -r between Ansó and Fago.
- Vázquez Obrador, J. (2021). *En torno al origen de los alomorfos (e)ro, (e)ra, (e)ros, (e)ras del artículo determinado aragonés.* Revista de Filología Románica 38: 121-132. Read directly.
- Várvaro, A. (1991). *De la escritura al habla: la diptongación de O breve tónica en el Alto Aragón.* Archivo de Filología Aragonesa XLVI-XLVII: 245-268, with the valley content on printed pp. 250-251. Read directly.

---
[← Ligurian / Genoese](lij.md) · [Home](../index.md) · [European Portuguese →](pt-PT.md)
