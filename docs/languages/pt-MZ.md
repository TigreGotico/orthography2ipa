# Mozambican Portuguese (pt-MZ)

| Field | Value |
|:---|:---|
| Code | `pt-MZ` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | research |
| Parent | `pt-PT` |
| Sources | Nhatuve (2019, *Revista de Letras* 21(32):130-144), Gonçalves (2010, *A Génese do Português de Moçambique*) through Barbosa (2011, review, *ELUP* 6(1):201-204), Gonçalves (1996), Stroud & Gonçalves (1997), Lopes (2004) |

Mozambican Portuguese (Português de Moçambique, PM) is an emerging non-native variety. Perpétua Gonçalves describes how it arises (Barbosa 2011:202, reviewing Gonçalves 2010:7). Children whose mother tongue is a Bantu language learn Portuguese as a second language. It is not a creole. About 6.5 % of Mozambicans have Portuguese as a first language, and most learn a Bantu language first (Barbosa 2011:202). The spec models the educated prestige variety of Maputo. Its `ancestors` list Swahili, Nyanja and Tsonga as substrates.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`. For the scores of the spec, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

## What the spec models

| Feature | pt-PT | pt-MZ | Source |
|:---|:---|:---|:---|
| Strong rhotic ⟨r rr⟩ | uvular [ʁ]: `rato` [ˈʁatu] | alveolar trill [r]: `rato` [ˈratu], `carro` [ˈkaru] | Nhatuve 2019:136-137 |
| Coda ⟨s⟩ | [ʃ ʒ]: `costas` [ˈkɔʃtɐʃ] | [s]: `costas` [ˈkɔstɐs] | override of `PT_CODA_S_HUSH` |
| Unstressed ⟨e⟩ | [ɨ]: `disse` [ˈdisɨ] | [e]: `disse` [ˈdise] | Gonçalves 2010, by analogy |
| Pretonic ⟨o⟩ | [u]: `morar` [muˈɾaɾ] | [o]: `morar` [moˈɾaɾ] | Gonçalves 2010, by analogy |

Nhatuve (2019:136) reports that in the oral Portuguese of Maputo, the onset ⟨r⟩ is an alveolar multiple vibrant [R], whatever vowel surrounds it. The contrast between /R/ and /ɾ/ tends to disappear (*"desaparece o fonema /r/"*). This copies the system of Changana and Ronga, Bantu languages that have only [R]. The spec keeps the tap between vowels and at the end of a word (`caro` [ˈkaɾu], `mar` [ˈmaɾ]). Nhatuve (2019:136) also reports that a word-final ⟨r⟩ often takes an extra vowel by paragoge ([falaɾ] to [falarɨ]). The spec does not model the paragoge.

Gonçalves (2010, ch. 2 "propriedades fónicas") and Barbosa (2011:203) describe the educated sound system of PM as an emerging norm. It reduces unstressed vowels less than European Portuguese does. The spec keeps an unstressed ⟨e⟩ as [e] and a pretonic ⟨o⟩ as [o]. An unstressed ⟨a⟩ still reduces to [ɐ] (`casa` [ˈkazɐ]), and a final ⟨o⟩ is [u] (`cabo` [ˈkabu]).

The vowel values are modelled by analogy. The direct instrumental vowel study read for the spec is Undolo (2014), on Angolan Portuguese. The PM values follow the shared Lusophone African pattern of weaker reduction, which Gonçalves describes for PM in general terms. No instrumental study of PM vowels was read, so treat these values as provisional.

The spec switches off the `pt-PT` rules `PT_FINAL_EM_NUCLEUS`, `PT_FINAL_EM_GLIDE`, `PT_FINAL_ENS_NUCLEUS` and `PT_FINAL_ENS_GLIDE`. So ⟨-em⟩ is the plain nasal vowel [ẽ] (`bem` [ˈbẽ], `homens` [ˈɔmẽs]). The `pt-PT` suffix and word-list rules for stressed vowel height are switched off too, because no source for these endings in Mozambique was read.

## Known gaps

- Nhatuve (2019:137) reports a voiced aspiration of ⟨lh⟩ /ʎ/ in Maputo speech, also a Bantu calque. It is a narrow allophonic detail below the grapheme layer, and the spec does not model it.
- The primaries read for the spec do not confirm a vocalisation of coda /l/ to [w] or Bantu pitch effects. The spec models neither, and the coda keeps the `pt-PT` [ɫ] (`sol` [ˈsɔɫ]).
- No source on this page gives the value of ⟨-em⟩. The plain [ẽ] rests on the notes of the switched-off rules only.
- The spec lists the open [ɛ ɔ] first for a stressed ⟨e o⟩ (`beleza` [beˈlɛzɐ]). No source on this page reports that for Mozambique.

## Input contract

Input is standard Portuguese orthography (Acordo Ortográfico 1990). Written accents carry stress, and the input needs no special preparation.

---
[← Cape Verdean Portuguese](pt-CV.md) · [Home](../index.md) · [Macau Portuguese →](pt-MO.md)
