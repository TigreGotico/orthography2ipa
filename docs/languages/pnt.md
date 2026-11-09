# Pontic Greek (`pnt`)

<!-- atlas:summary begin -->
Pontic Greek is a Hellenic language, written in the Greek script. Glottolog places it in Bulgaria, Greece, North Macedonia and Türkiye. The `pnt` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pnt` |
| ISO 639-3 | [pnt](https://iso639-3.sil.org/code/pnt), Pontic |
| Glottolog | [pont1253](https://glottolog.org/resource/languoid/id/pont1253), Pontic |
| Wikidata | [Q36748](https://www.wikidata.org/wiki/Q36748) |
| Wikipedia | [Pontic Greek](https://en.wikipedia.org/wiki/Pontic_Greek) |
| Family | [Indo-European](by-family.md#indo-european) > [Hellenic](by-family.md#indo-european--hellenic) |
| Region | [Eurasia](by-region.md#eurasia) > [Bulgaria](by-region.md#bulgaria), [Greece](by-region.md#greece), [North Macedonia](by-region.md#north-macedonia), [Türkiye](by-region.md#türkiye) |
| Script | [Greek](by-script.md#greek) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 700, living |
| Parent | [Modern Greek](el.md) `el` |
| Explorer | [`pnt` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pnt) |
| Spec file | [`pnt.json`](../../orthography2ipa/data/pnt.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Pontic Greek (Ποντιακά), archaic Greek dialect originally spoken along the Black Sea (Pontic) coast of Anatolia. Now spoken mainly in Greece. Retains many features of Ancient and Medieval Greek lost in standard Modern Greek. Uses standard Greek orthography. /i/ represented by η, ι, υ, ει, οι.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 1908 to 2024. [Sources](#sources) lists them. The spec file writes all 98 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pnt.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pnt` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-wiki-pnt"></a>Wikipedia contributors (2024). *Pontic Greek*.
2. <a id="src-armostis_etal2020"></a>Armostis, Spyros, Voniati, Louiza, Drosos, Konstantinos, Tafiadis, Dionysios (2020). *Trapezountian Pontic Greek in Etoloakarnania. Illustrations of the IPA*. Journal of the International Phonetic Association 52(2), 328-340 (free access). Cited: 330-339. [doi.org](https://doi.org/10.1017/S0025100320000201)
3. <a id="src-petrounias1999"></a>Petrounias, Evangelos (1999). *Κριτική του «μονοτονικού» ορθογραφικού συστήματος [A critique of the monotonic orthographic system]*. Κέντρο Ελληνικής Γλώσσας, Πύλη για την ελληνική γλώσσα (Θέματα ιστορίας της ελληνικής γλώσσας). Cited: §3.1. [greek-language.gr](https://www.greek-language.gr/greekLang/el/studies/history/thema_16/01.html)
4. <a id="src-oeconomides1908"></a>Oeconomides, Demosthenes E. (1908). *Lautlehre des Pontischen*. Leipzig: A. Deichert'sche Verlagsbuchhandlung Nachf. Cited: 2-3, 9, 25, 34, 84, 125, 175. [archive.org](https://archive.org/details/lautlehredespont00oikouoft)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 48 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  | c ɟ | k ɡ |
| Affricate |  |  |  | dz ts | dʒ tʃ |  |  |
| Nasal | m |  |  | n |  |  |  |
| Trill |  |  |  | r |  |  |  |
| Fricative |  | f v | ð θ | s z | ʃ | ç ʝ | x ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e ø | o |
| Near-open | æ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [af] [av] [ef] [ev] [ks] [mb] [nd] [ndz] [ps] [pʃ] [æv] [ŋɡ] [ɲɟ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ΐ⟩ | [i] |  |
| ⟨ά⟩ | [a] |  |
| ⟨έ⟩ | [e] |  |
| ⟨ή⟩ | [i] |  |
| ⟨ί⟩ | [i] |  |
| ⟨ΰ⟩ | [i] |  |
| ⟨α⟩ | [a] |  |
| ⟨α̈⟩ | [æ] |  |
| ⟨α̈υ⟩ | [æv] |  |
| ⟨αί⟩ | [e] |  |
| ⟨αι⟩ | [e] |  |
| ⟨αυ⟩ | [av] [af] |  |
| ⟨αύ⟩ | [av] [af] |  |
| ⟨αὶ⟩ | [e] |  |
| ⟨αὺ⟩ | [av] [af] |  |
| ⟨αῖ⟩ | [e] |  |
| ⟨αῦ⟩ | [av] [af] |  |
| ⟨β⟩ | [v] |  |
| ⟨β̇⟩ | [b] |  |
| ⟨γ⟩ | [ɣ] [j] |  |
| ⟨γγ⟩ | [ŋɡ] |  |
| ⟨γκ⟩ | [ŋɡ] | default [ŋɡ] · word initial [ɡ] |
| ⟨δ⟩ | [ð] |  |
| ⟨δ̇⟩ | [d] |  |
| ⟨ε⟩ | [e] |  |
| ⟨εί⟩ | [i] |  |
| ⟨ει⟩ | [i] |  |
| ⟨ευ⟩ | [ev] [ef] |  |
| ⟨εύ⟩ | [ev] [ef] |  |
| ⟨εὶ⟩ | [i] |  |
| ⟨εὺ⟩ | [ev] [ef] |  |
| ⟨εῖ⟩ | [i] |  |
| ⟨εῦ⟩ | [ev] [ef] |  |
| ⟨ζ⟩ | [z] |  |
| ⟨η⟩ | [i] |  |
| ⟨θ⟩ | [θ] |  |
| ⟨ι⟩ | [i] |  |
| ⟨κ⟩ | [k] |  |
| ⟨κ̇⟩ | [ɡ] |  |
| ⟨λ⟩ | [l] |  |
| ⟨μ⟩ | [m] |  |
| ⟨μπ⟩ | [mb] [b] | default [mb] · word initial [b] |
| ⟨ν⟩ | [n] |  |
| ⟨νγκ⟩ | [ŋɡ] |  |
| ⟨ντ⟩ | [nd] [d] | default [nd] · word initial [d] |
| ⟨ντζ⟩ | [ndz] |  |
| ⟨ξ⟩ | [ks] |  |
| ⟨ο⟩ | [o] |  |
| ⟨ο̈⟩ | [ø] |  |
| ⟨οί⟩ | [i] |  |
| ⟨οι⟩ | [i] |  |
| ⟨ου⟩ | [u] |  |
| ⟨ού⟩ | [u] |  |
| ⟨οὶ⟩ | [i] |  |
| ⟨οὺ⟩ | [u] |  |
| ⟨οῖ⟩ | [i] |  |
| ⟨οῦ⟩ | [u] |  |
| ⟨π⟩ | [p] |  |
| ⟨π̇⟩ | [b] |  |
| ⟨ρ⟩ | [r] |  |
| ⟨ς⟩ | [s] |  |
| ⟨σ⟩ | [s] |  |
| ⟨σ̇⟩ | [ʃ] |  |
| ⟨τ⟩ | [t] |  |
| ⟨τ̇⟩ | [d] |  |
| ⟨τ̇σ̇⟩ | [dʒ] |  |
| ⟨τζ⟩ | [dz] |  |
| ⟨τσ⟩ | [ts] |  |
| ⟨τσ̇⟩ | [tʃ] |  |
| ⟨υ⟩ | [i] |  |
| ⟨υί⟩ | [i] |  |
| ⟨υι⟩ | [i] |  |
| ⟨υὶ⟩ | [i] |  |
| ⟨υῖ⟩ | [i] |  |
| ⟨φ⟩ | [f] |  |
| ⟨χ⟩ | [x] [ç] |  |
| ⟨χ̇⟩ | [ʃ] |  |
| ⟨ψ⟩ | [ps] |  |
| ⟨ψ̇⟩ | [pʃ] |  |
| ⟨ω⟩ | [o] |  |
| ⟨ω̈⟩ | [ø] |  |
| ⟨ϊ⟩ | [i] |  |
| ⟨ϋ⟩ | [i] |  |
| ⟨ό⟩ | [o] |  |
| ⟨ύ⟩ | [i] |  |
| ⟨ώ⟩ | [o] |  |
| ⟨ὰ⟩ | [a] |  |
| ⟨ὲ⟩ | [e] |  |
| ⟨ὴ⟩ | [i] |  |
| ⟨ὶ⟩ | [i] |  |
| ⟨ὸ⟩ | [o] |  |
| ⟨ὺ⟩ | [i] |  |
| ⟨ὼ⟩ | [o] |  |
| ⟨ᾶ⟩ | [a] |  |
| ⟨ῆ⟩ | [i] |  |
| ⟨ῖ⟩ | [i] |  |
| ⟨ῦ⟩ | [i] |  |
| ⟨ῶ⟩ | [o] |  |

Stress falls on the penult by default. A written ⟨ά⟩ ⟨έ⟩ ⟨ή⟩ ⟨ί⟩ ⟨ό⟩ ⟨ύ⟩ ⟨ώ⟩ ⟨ΐ⟩ ⟨ΰ⟩ ⟨ᾶ⟩ ⟨ῆ⟩ ⟨ῖ⟩ ⟨ῦ⟩ ⟨ῶ⟩ ⟨ὰ⟩ ⟨ὲ⟩ ⟨ὴ⟩ ⟨ὶ⟩ ⟨ὸ⟩ ⟨ὺ⟩ ⟨ὼ⟩ marks the stressed vowel.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 11 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `EL_S_VOICING` | /s/ → [z], before [m] [n] [l] [ɾ] [r] [v] [ð] [ɣ] and 5 more | ⟨Άρκανσας⟩ [aɾkanzas] | Arvaniti 2007 |
| `EL_GAMMA_FRONTING` | /ɣ/ → [ʝ], before a front vowel, spelled ⟨γ⟩ | - | - |
| `PNT_K_PALATAL` | /k/ → [c], before [e] [i], spelled ⟨κ⟩ ⟨γ⟩ ⟨χ⟩ ⟨γκ⟩ ⟨γγ⟩ ⟨νγκ⟩ | ⟨vs.⟩ [ˈlice] | [Armostis 2020](#src-armostis_etal2020), [Oeconomides 1908](#src-oeconomides1908) |
| `PNT_G_PALATAL` | /ɡ/ → [ɟ], before [e] [i], spelled ⟨κ⟩ ⟨γ⟩ ⟨χ⟩ ⟨γκ⟩ ⟨γγ⟩ ⟨νγκ⟩ | - | [Armostis 2020](#src-armostis_etal2020) |
| `PNT_NG_PALATAL` | /ŋɡ/ → [ɲɟ], before [e] [i], spelled ⟨κ⟩ ⟨γ⟩ ⟨χ⟩ ⟨γκ⟩ ⟨γγ⟩ ⟨νγκ⟩ | ⟨but⟩ [ˈeɲɟen] | [Armostis 2020](#src-armostis_etal2020) |
| `PNT_X_PALATAL` | /x/ → [ç], before [e] [i], spelled ⟨κ⟩ ⟨γ⟩ ⟨χ⟩ ⟨γκ⟩ ⟨γγ⟩ ⟨νγκ⟩ | ⟨e.g.⟩ [ˈçile] | [Armostis 2020](#src-armostis_etal2020) |
| `PNT_GAMMA_PALATAL` | /ɣ/ → [ʝ], before [e] [i], spelled ⟨κ⟩ ⟨γ⟩ ⟨χ⟩ ⟨γκ⟩ ⟨γγ⟩ ⟨νγκ⟩ | - | [Armostis 2020](#src-armostis_etal2020) |
| `PNT_AU_VOICELESS` | /av/ → [af], before a consonant, with more context in the spec | - | [Oeconomides 1908](#src-oeconomides1908) |
| `PNT_AU_FINAL` | /av/ → [af], word-finally | - | [Oeconomides 1908](#src-oeconomides1908) |
| `PNT_EU_VOICELESS` | /ev/ → [ef], before a consonant, with more context in the spec | - | [Oeconomides 1908](#src-oeconomides1908) |
| `PNT_EU_FINAL` | /ev/ → [ef], word-finally | - | [Oeconomides 1908](#src-oeconomides1908) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pnt")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Polish](pl.md) · [Home](../index.md) · [Proto-Gulf Arabic →](afb.md)
