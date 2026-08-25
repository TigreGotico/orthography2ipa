# Pyrenean-valley Aragonese subdialects: Phonology Reference

**Codes**: `an-x-ansotano`, `an-x-cheso`, `an-x-chistabin`, `an-x-belsetan`, `an-x-tensino` | **Family**: Indo-European > Romance | **Script**: Latin (alphabet) **Parent**: `an` (Aragonese) | **Quality tiers**: cheso / chistabín / belsetán = research. Ansotano / tensino = skeleton

These five specs model the classic High-Aragonese (*altoaragonés*) **Pyrenean valley** varieties as thin **delta** specs on the base Aragonese spec [`an`](../../orthography2ipa/data/an.json). They complement the two existing regional specs `an-x-occidental` (Western) and `an-x-oriental` (Ribagorçan), which cover different, non-valley cuts of the dialect continuum.

Everything general to Aragonese is **inherited** via `graphemes_base`/`allophones_base`/`positional_graphemes_base = "an"`.

This base layer preserves initial Latin **F-** ([f]-, *feito*, *fillo*) and keeps **/θ/ distinción**. It maps the palatal lateral **/ʎ/** to ⟨ll⟩ (no *yeísmo*). It reads ⟨ch⟩ as **[tʃ]** and ⟨x⟩ as **/ʃ/**. It applies the systematic Ĕ/Ŏ → *ie*/*ue* diphthongisation throughout.

Each valley declares **only** its own deltas on top of this shared base.

## Why the specs are thin (honesty note)

Aragonese orthography (Grafía de Uesca / Academia norms) is broadly **phonemic**. Much of what separates one valley from another is **lexical or morphological**: different articles, verb endings, individual etyma. That variation surfaces in *spelling*, not in the grapheme→IPA map.

A word like Belsetán *feto* (< FACTU, vs general *feito*) is already read correctly by the base map, because it is spelled with ⟨t⟩. There is nothing phoneme-level to add for it.

So these specs model only the handful of genuinely **phonological** deltas. Each spec documents the lexical and morphological distinctiveness in its own `notes`, rather than faking a grapheme rule for it.

## Modelled deltas, per valley

| Valley (code) | Modelled phoneme-level delta | Example | Source |
|:---|:---|:---|:---|
| **Cheso** `an-x-cheso` | ⟨x⟩/⟨ix⟩ = [ʃ] **without epenthesis** (base offers [ʃ, iʃ, jʃ] for ⟨ix⟩; cheso keeps only [ʃ]) | *buixo* → **ˈbwiʃo** (top-1 unchanged — the delta **narrows the candidate set**, dropping the [iʃ]/[jʃ] alternates the base would otherwise beam) | Kuhn 1935 (via es.wikipedia, secondary) |
| **Ansotano** `an-x-ansotano` | word-final ⟨r⟩ **deleted** (Ansó, vs retained in Fago / Cheso) | *fablar* → **ˈfabla** | Barcos 2007 (secondary) |
| **Belsetán** `an-x-belsetan` | **preserved geminates** ⟨l·l⟩=[lː], ⟨n·n⟩=[nː] | *bel·la* → **ˈbelːa**, *pen·na* → **ˈpenːa** | Badía Margarit 1950 (secondary) |
| **Chistabín** `an-x-chistabin` | preserved geminates **+** word-final ⟨r⟩ deletion | *bel·lota* → **beˈlːota**, *comer* → **koˈme** | Blas Gabarda & Romanos 2008; Mott 1989 |
| **Tensino** `an-x-tensino` | postvocalic article **ro/ra/ros/ras** realised with the weak **tap [ɾ]** (not the base word-initial trill [r]) | *ro* → **ɾo**, *ras* → **ɾas** | Vázquez Obrador 2021 (read) |

## Not modelled (documented in `notes`, deliberately)

- **Cheso**: loss of [tʃ] in a closed etymon set (*itar* < IECTARE, *hermano* < GERMANU: spelled without ⟨ch⟩, so already correct). Infinitive final /r/ **preserved** even before enclitics (the diagnostic contrast with Ansotano). article *o/a/os/as*. Auxiliary *ser*. Participle–object agreement.
- **Ansotano**: retention of intervocalic -d- (*odir*). Conservative morphology.
- **Belsetán**: -CT- → -t- (*feto*), -ULT- → -ut- (*muto*), NOCTE > *nuet*. -LL- → -r- in the pronouns *er, ers* (Gascon-influenced). Article *el/la/es/las*. Archaic *nusaltros/vusaltros*. Atonic strong perfects (*tenié, trayé, benié*).
- **Chistabín**: voicing of intervocalic Latin voiceless stops (*caixigo, cadiera, radigón*). Article *el/la/es/las*. 1PL verb ending **-m** (Ribagorçan parallel). Participles *-au/-iu*. Participle–object agreement.
- **Tensino**: cacuminal ⟨-ch-⟩ [tʃ] where general Aragonese has -ll- (*estach, gricha*). Conservation of intervocalic -p-/-t-/-k-. Preterite in **-ós** (*puyós, cantós*). The Aragonese conditional in **-arba/-erba/-irba**.

## Diphthongisation geography (Várvaro, read directly)

Várvaro (1991, *AFA* XLVI-XLVII, *De la escritura al habla: la diptongación de O breve tónica en el Alto Aragón*, pp. 245-268) traces the medieval *ué*/*uá* isoglosses across exactly these valleys. Hecho shows only *ué* (printed page 250). *uá* surfaces in the Valle de Tena and inside the modern *uá* area at Bielsa (page 250). Ansó documents lack *uá* (page 250). Gistaín shows *ué* (page 251).

This is the one primary study read in full for these specs. The per-valley synchronic phonetics were drawn from the Spanish-Wikipedia dialect articles (secondary). For Chistabín and Tensino, they come from a directly-read online summary and from Vázquez Obrador (2021). See each spec's `sources` for the honest provenance of every claim.

```python
from orthography2ipa import G2P
G2P("an-x-cheso").transcribe_word("buixo")      # ˈbwiʃo   — no epenthesis
G2P("an-x-ansotano").transcribe_word("fablar")  # ˈfabla   — final-r deletion
G2P("an-x-belsetan").transcribe_word("bel·la")  # ˈbelːa   — geminate lateral
G2P("an-x-chistabin").transcribe_word("comer")  # koˈme    — final-r deletion
G2P("an-x-tensino").transcribe_word("ro")       # ɾo       — weak-tap article
```

## Sources

- **Kuhn, A. (1935).** *Der hocharagonesische Dialekt.* Revue de Linguistique Romane XI: 1-312. (The classic High-Aragonese monograph, foundational for Ansó and Hecho. Consulted via secondary summaries, not directly obtainable.)
- **Badía Margarit, A. M. (1950).** *El habla del valle de Bielsa (Pirineo aragonés).* CSIC. (Belsetán geminates and -CT-/-ULT- reductions.)
- **Nagore Laín, F. (1986).** *El aragonés de Panticosa. Gramática.* Instituto de Estudios Altoaragoneses. (Tensino reference grammar.)
- **Blas Gabarda, F. & Romanos Hernando, F. (2008).** *Diccionario aragonés chistabín (Bal de Chistau).* Gara d'Edizions.
- **Mott, B. (1989).** *El habla de Gistaín.* Instituto de Estudios Altoaragoneses.
- **Barcos, M. A. (2007).** *El aragonés ansotano: estudio lingüístico de Ansó y Fago.* Gara d'Edizions. (Ansó vs Fago final-r contrast.)
- **Vázquez Obrador, J. (2021).** *En torno al origen de los alomorfos (e)ro, (e)ra, (e)ros, (e)ras del artículo determinado aragonés.* Revista de Filología Románica 38: 121-132. [Read directly.]
- **Várvaro, A. (1991).** *De la escritura al habla: la diptongación de O breve tónica en el Alto Aragón.* Archivo de Filología Aragonesa XLVI-XLVII: 245-268 (valley content on printed pp. 250-251). [Read directly.]

---
[← Ligurian / Genoese](lij.md) · [Home](../index.md) · [Lisbon / Estremenho European Portuguese →](pt-PT-x-lisbon.md)
