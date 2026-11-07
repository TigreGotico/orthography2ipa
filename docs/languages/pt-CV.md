# Cape Verdean Portuguese (pt-CV)

| Field | Value |
|:---|:---|
| Code | `pt-CV` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | skeleton |
| Parent | `pt-PT` |
| Sources | Freitas (2017, *RILP* 31:153-172, on the Creole), Undolo (2014, on Angolan Portuguese), Lang (2009), Baptista (2002), Veiga (2004) |

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`. For the scores of the spec, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

## Cape Verdean Portuguese is not the Creole

This spec models Cape Verdean Portuguese (Português de Cabo Verde), the formal and second-language variety of Portuguese, co-official in Cape Verde. It is a different language from Cape Verdean Creole (Kabuverdianu or Kriolu, ISO `kea`), the first language of almost the whole population. The Creole formed from the Portuguese of the 16th and 17th centuries and from West African languages. Freitas (2017:154) writes that it already *"se diferenciava sobretudo com relação às vogais átonas"* from its Portuguese lexifier. The two languages share a territory and speakers switch between them, but they are different systems. The Creole has its own entry, `kea`, and the spec lists it in `ancestors` as an adstrate.

## What the spec models

The other Lusophone African norms are reported to keep their vowels close to the spelling. Cape Verdean Portuguese is reported to share that, with a few conservative consonants. The table gives each reported feature and what the spec does with it.

| Feature | pt-PT | Reported for pt-CV | What the spec does |
|:---|:---|:---|:---|
| Unstressed vowel reduction | strong | reduced or absent | ⟨e⟩ keeps [e]: `disse` [ˈdise], `presidente` [preziˈdẽte]. ⟨a o⟩ still reduce: `casa` [ˈkazɐ], `morar` [muˈrar] |
| Coda ⟨s⟩ | [ʃ ʒ] | [s] | [s], an override of `PT_CODA_S_HUSH`: `costas` [ˈkɔstɐs], `feliz` [feˈlis] |
| Rhotic | uvular [ʁ] | alveolar [r] | [r] for every ⟨r⟩ and ⟨rr⟩: `rato` [ˈratu], `mar` [ˈmar] |
| Stressed mid ⟨e o⟩ | [e o] or [ɛ ɔ] by word | more open [ɛ ɔ] | close [e o] first, open second: `dezena` [deˈzenɐ] |
| ⟨b d g⟩ between vowels | stops in the spec | stops [b d ɡ] | stops, as in `pt-PT`: `cabo` [ˈkabu], `nada` [ˈnadɐ] |
| ⟨l⟩ | velarised [ɫ] in the coda | dental [l̪] | not modelled: `sol` [ˈsɔɫ] |

The spec also switches off `PT_FINAL_EM_NUCLEUS` and `PT_FINAL_ENS_NUCLEUS`, so ⟨-em⟩ keeps the close-mid nucleus with a palatal glide: `bem` [ˈbẽj̃]. The `pt-PT` suffix and word-list rules for stressed vowel height are switched off too, because no source for these endings in Cape Verde was read.

## Why the spec stays at the skeleton tier

No instrumental phonology of Cape Verdean Portuguese, as opposed to the Creole, was available to read for the spec. So the features above rest on three things:

1. The general Lusophone African pattern of weaker reduction. Its read primary is Undolo (2014:183-184), on Angolan Portuguese.
2. The read Creole primary, Freitas (2017). The spec uses it only to fix the line between the Creole and the Portuguese.
3. The Wikipedia description of Cape Verdean Portuguese, which cites no source for these features. The spec flags it as secondary.

The features are therefore provisional. The specs `pt-AO` and `pt-MZ` reach the research tier, because each has a read primary for its own variety (Undolo 2014, Nhatuve 2019). The spec `pt-CV` stays at the skeleton tier until a read source on Cape Verdean Portuguese exists. The test file `tests/test_lusophone_african.py` holds this tier.

## Known gaps

- The spec gives the trill [r] to every ⟨r⟩, so the tap and the trill no longer contrast: `caro` and `carro` are both [ˈkaru].
- The reported opening of the stressed mid vowels is not in the output. The spec lists the close vowel first.

## Input contract

Input is standard Portuguese orthography (Acordo Ortográfico 1990). Do not give the spec Kabuverdianu text in the Creole orthography (ALUPEC). That is a different language, and it belongs to the `kea` entry.

---
[← Angolan Portuguese](pt-AO.md) · [Home](../index.md) · [Mozambican Portuguese →](pt-MZ.md)
