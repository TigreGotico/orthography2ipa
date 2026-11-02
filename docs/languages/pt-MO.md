# Macau Portuguese (pt-MO)

| Field | Value |
|:---|:---|
| Code | `pt-MO` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | skeleton |
| Parent | `pt-PT` |
| Sources | Batalha (1959), Pinharanda-Nunes (2011), English Wikipedia *Macanese Portuguese* (flagged secondary) |

Macau Portuguese (*Português de Macau*) is a co-official language of the Macau SAR of the People's Republic of China, with Chinese. A small first-language and heritage community speaks it. It is also the second-language official register of legislation, the courts and public administration. Its use has declined since the handover of 1999. It is the most European of the Asian Portuguese varieties, and it *"closely follows the standard European dialect in pronunciation and vocabulary"*. The spec `ancestors` list Chinese (`zh`) and Patuá (`mzs`) as adstrates.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`. For the scores of the spec, see [../scoreboard.md](../scoreboard.md).

## Patuá is a separate language

The Macanese creole, Patuá, is also called *maquista* or, historically, the *"dialecto macaense"*. It is a distinct contact language based on Portuguese, with Cantonese, Malay, Kristang (Malacca), Konkani and Sinhala elements, and it is nearly extinct. Do not confuse it with the modern Portuguese of Macau that this spec models.

- Batalha, G. N. (1959). *Estado actual do dialecto macaense*. Revista de Filologia Portuguesa 9:177-213. It describes the creole. Albuquerque (2010:283) cites Batalha (1959:181) for creole prosody, which confirms the reference.
- Pinharanda-Nunes, M. (2011). *Estudo da Expressão Morfo-Sintáctica das Categorias de Tempo, Modo e Aspecto em Maquista*. PhD, University of Macau. It is the first doctoral thesis on the grammar of Patuá, the creole and not the Portuguese variety.

## Why the spec stays at the skeleton tier

The literature on the phonology of Macau Portuguese is thin. No peer-reviewed phonological description of Macau Portuguese, as opposed to the Patuá creole, was available to read for the spec. The specialists who publish on the languages of Macau (Pinharanda-Nunes, Batalha) describe the creole.

The only phonological description read is the English Wikipedia article *Macanese Portuguese*. Its phonology section cites no source, so the spec uses it only as a flagged secondary source. It reports these traits:

1. The variety *"nowadays closely follows the standard European dialect in pronunciation and vocabulary"*. So the spec keeps the inherited `pt-PT` maps as the modelled norm: the uvular [ʁ], the European vowel reduction and the coda *chiado*.
2. [ʒ] is devoiced to [ʃ], *"a trait almost unique to Macau"*.
3. Second-language speakers drop the final /ɾ/ of the infinitive (*comer*, *dormir*) and keep /ɾ/ elsewhere (*mar*). This parallels African and most Brazilian Portuguese.
4. Some second-language speakers have patterns influenced by Cantonese, partly non-rhotic. Speakers with higher education in Portuguese do not have them.

Only the uncited secondary source documents traits 2 to 4. They are variable second-language traits, and trait 3 is a deletion that the allophone layer of the engine does not express. So the spec records them in its `notes` and does not encode them. The spec reaches the research tier only when a citable phonological description of Macau Portuguese is available and read.

## What the spec models

`pt-MO` inherits the `pt-PT` maps: graphemes, positional vowel reduction, coda allophony and the uvular rhotic. Most output is the same as `pt-PT`: `bate` [ˈbatɨ], `mesmo` [ˈmɛʃmu], `costas` [ˈkɔʃtɐʃ].

The spec declares its own rhotic. Its ⟨r⟩ grapheme lists [ʁ] first, and its positional map keeps the tap [ɾ] between vowels only. So the output has [ʁ] in a coda and in a cluster, where `pt-PT` has the tap:

| Word | pt-PT | pt-MO |
|:---|:---|:---|
| mar | ˈmaɾ | ˈmaʁ |
| livro | ˈlivɾu | ˈlivʁu |
| caro | ˈkaɾu | ˈkaɾu |

The spec also switches off the `pt-PT` suffix and word-list rules for stressed vowel height and the ⟨-em⟩ nucleus rules. Their notes say that no source for these endings in Macau was read. So some stressed vowels and ⟨-em⟩ differ from `pt-PT`: `beleza` is [bɨˈlɛzɐ] against [bɨˈlezɐ], and `bem` is [ˈbẽj̃] against [ˈbɐ̃j̃].

## Known gaps

- No source on this page supports the uvular [ʁ] in a coda or a cluster. The reported trait 3 points the other way, toward a kept tap in *mar*.

## Sources

- Batalha, G. N. (1959). *Estado actual do dialecto macaense*. Revista de Filologia Portuguesa 9:177-213. On the creole.
- Pinharanda-Nunes, M. (2011). PhD thesis on the tense, mood and aspect of Maquista. University of Macau. On the creole.
- English Wikipedia, *Macanese Portuguese*. A flagged secondary source: its phonology section cites nothing. It is the only phonological description of the Portuguese variety that was available.

---
[← Mozambican Portuguese](pt-MZ.md) · [Home](../index.md) · [East Timorese Portuguese →](pt-TL.md)
