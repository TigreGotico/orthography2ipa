# Angolan Portuguese (pt-AO)

| Field | Value |
|:---|:---|
| Code | `pt-AO` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | research |
| Parent | `pt-PT` |
| Sources | Undolo (2014, *Revista de Filología Románica* 31(2):181-187), Chavagne (2005, PhD, Lyon 2), Inverno (2011, PhD, Coimbra), Mateus & d'Andrade (2000), Cunha & Cintra (1984) |

Angolan Portuguese (Português de Angola, PA) is the emerging second norm of educated Angolan speakers. It is not a creole. Portuguese has been the sole official language of Angola since 1975. It is the mother tongue of a growing urban minority and the second language of most Angolans. It is in contact with many Bantu languages, such as Umbundu, Kimbundu and Kikongo. The spec inherits the `pt-PT` maps and removes several European reduction processes from them.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`. For the scores of the spec, see [../scoreboard.md](../scoreboard.md).

## What the spec models

The main feature is a vocalism close to the spelling. Angolan Portuguese lacks the strong European reduction of unstressed vowels, so its written vowels keep their full quality. Undolo (2014) describes the vowel system of educated speakers against the European one. The spec encodes the difference as an own positional map for ⟨a e o⟩ over the inherited `pt-PT` map.

| Feature | pt-PT | pt-AO | Source |
|:---|:---|:---|:---|
| Final unstressed ⟨a⟩ | [ɐ]: `casa` [ˈkazɐ] | [a]: `casa` [ˈkaza] | Undolo 2014:183 |
| Pretonic ⟨e⟩ | [ɨ]: `menino` [mɨˈninu] | [e]: `menino` [meˈninʊ] | Undolo 2014:183 |
| Pretonic ⟨o⟩ | [u]: `morar` [muˈɾaɾ] | [o]: `morar` [moˈɾaɾ] | Undolo 2014:184 |
| Final unstressed ⟨e⟩ | [ɨ]: `disse` [ˈdisɨ] | [ɨ], kept: `disse` [ˈdisɨ] | Undolo 2014:183 |
| Coda ⟨s⟩ | [ʃ]: `costas` [ˈkɔʃtɐʃ] | [s]: `costas` [ˈkɔstas] | spec override of `PT_CODA_S_HUSH` |

Undolo (2014:184) sums up the system as one that *"não sofre elevação e centralização em posição átona"*. In it, [ɨ] *"restringe-se à posição átona final"*. Chavagne (2005:64) reports the same independently: in Angolan Portuguese *"les voyelles atones gardent le timbre des voyelles toniques"*. Unstressed syllables keep the quality of the stressed vowels, and the intensity contrast between them is much smaller than in European Portuguese. Undolo (2014:186) attributes the full vocalism to the simple syllable structure, with open nuclei, of the Angolan Bantu substrate.

Undolo (2014:183-184) also reports a tendency to open the stressed mid vowels, with [ɛ ɔ] favoured over [e o] (for example [beˈlɛza]). The tendency is variable and lexical. The spec lists [ɛ] before [e] and [ɔ] before [o] for a stressed vowel. So the top output is open, and the close vowel is the second candidate: `beleza` [beˈlɛza], `mesa` [ˈmɛza].

The spec switches off the coda rules `PT_CODA_S_HUSH` and `PT_CODA_Z_HUSH` by redeclaring their ids with an alveolar surface. It also switches off `PT_FINAL_EM_NUCLEUS` and `PT_FINAL_ENS_NUCLEUS`, because Angolan Portuguese does not centralise unstressed vowels (Undolo 2014:183-184). So ⟨-em⟩ keeps the close-mid nucleus: `bem` [ˈbẽj̃]. The `pt-PT` suffix and word-list rules for stressed vowel height (`PT_SUFFIX_*`, `PT_LEX_*_SUFFIX`, `PT_ER_CLOSE`, `PT_LEX_OPEN_ER`, `PT_FINAL_EN_*`) are switched off too. Their notes say that no source for these endings in Angola was read.

## Known gaps

- Undolo (2014:184) reports a central open nasal [ã] where European Portuguese has [ɐ̃]. The spec does not model it.
- The spec has no source for the rhotic. Its ⟨r⟩ map gives the tap [ɾ] at the start of a word, between vowels and at the end of a word. Elsewhere the inherited grapheme value [ʁ] comes first: `rato` [ˈɾatʊ], `pedra` [ˈpɛdʁa], `porta` [ˈpɔʁta], `carro` [ˈkaʁʊ].
- A final unstressed ⟨o⟩ is the near-close [ʊ] (`cabo` [ˈkabʊ]), where `pt-PT` gives [u]. No source on this page states the value.
- Inverno (2011) is a thesis on the morphosyntax of the restructured vernacular of Dundo. The spec cites it for the contact setting only, not for the vowel model.

## Input contract

Input is standard Portuguese orthography (Acordo Ortográfico 1990). The spec uses the written accents for stress, and the input needs no special preparation.

---
[← Brazilian Portuguese dialects](pt-BR-dialects.md) · [Home](../index.md) · [Cape Verdean Portuguese →](pt-CV.md)
