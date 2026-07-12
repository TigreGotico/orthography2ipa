# Hindi (hi) — Phonology Reference

**Code**: `hi` | **Family**: Indo-European > Indo-Aryan | **Script**: Devanagari (abugida)
**Quality tier**: research | **Sources**: Masica (1991), Ohala (1983), Pandey (2014)

---

## Devanagari Script Overview

Devanagari is an **abugida** — consonant letters carry an inherent vowel /ə/ (schwa), which is overridden by explicit vowel marks (mātrā). The inherent vowel is deleted in certain phonological environments (see Schwa Deletion below).

| Component | Description | Example |
|:---|:---|:---|
| Consonant letter | Carries inherent /ə/ | क = /kə/ |
| Vowel mark (mātrā) | Replaces inherent vowel | का = /kaː/ |
| Halant (्) | Suppresses inherent vowel | क् = /k/ (pure consonant) |
| Independent vowel | Used word-initially | अ = /ə/, आ = /aː/ |

---

## Four-Way Laryngeal Contrast

Hindi has the most complex stop system of major world languages: **four laryngeal categories** for each place of articulation:

| Category | Bilabial | Alveolar (dental) | Retroflex | Velar |
|:---|:---:|:---:|:---:|:---:|
| Voiceless unaspirated | प [p] | त [t̪] | ट [ʈ] | क [k] |
| Voiceless aspirated | फ [pʰ] | थ [t̪ʰ] | ठ [ʈʰ] | ख [kʰ] |
| Voiced | ब [b] | द [d̪] | ड [ɖ] | ग [ɡ] |
| Voiced aspirated (breathy) | भ [bʱ] | ध [d̪ʱ] | ढ [ɖʱ] | घ [ɡʱ] |

**Dental vs. Retroflex**: Hindi distinguishes dentals (tongue tip to upper teeth) and retroflexes (tongue tip curled back):
- `ताल` [t̪aːl] "rhythm" vs. `टाल` [ʈaːl] "to put off"

**Nasals** also follow this pattern: ङ [ŋ], ञ [ɲ], ण [ɳ], न [n], म [m]

---

## Retroflex Flapping

In intervocalic position, retroflex stops **ड [ɖ]** and **ढ [ɖʱ]** are realized as **flaps**:

| Grapheme | Default | Intervocalic | Examples |
|:---:|:---:|:---:|:---|
| ड | [ɖ] | [ɽ] | `पड़ना` [pɐɽnaː] "to fall" |
| ढ | [ɖʱ] | [ɽʱ] | — |

This is encoded in `positional_graphemes`:
```json
"ड": {"intervocalic": ["ɽ"], "default": ["ɖ"]}
```

---

## Schwa Deletion

The inherent vowel /ə/ undergoes **systematic deletion** in Hindi:

### Rule 1: Word-final deletion
The final /ə/ of a word is always deleted (unless the word is monosyllabic):
- `कमल` /kəmələ/ → [kəmɐl] "lotus"

### Rule 2: Medial deletion (Pandey's rule)
In CVCV sequences, the first /ə/ is deleted if the second syllable has /ə/ and the following syllable is stressed:
- `करना` /kərənaː/ → [kərnaː] "to do"

This makes Hindi phonology significantly more complex than a simple grapheme-to-IPA mapping suggests.

### Schwa in positional_graphemes:
```json
"अ": {"word_final": [""], "nucleus_unstressed": ["ə"], "default": ["ə"]}
```

---

## Vowel System

| Grapheme (independent) | Mātrā | IPA | Example |
|:---:|:---:|:---:|:---|
| अ | (inherent) | [ə] | `कमल` "lotus" |
| आ | ा | [aː] | `काम` [kaːm] "work" |
| इ | ि | [ɪ] | `किताब` [kɪtaːb] "book" |
| ई | ी | [iː] | `दीवार` [diːwaːr] "wall" |
| उ | ु | [ʊ] | `उन` [ʊn] "them" |
| ऊ | ू | [uː] | `ऊन` [uːn] "wool" |
| ए | े | [eː] | `एक` [eːk] "one" |
| ऐ | ै | [ɛː] | `ऐसा` [ɛːsaː] "such" |
| ओ | ो | [oː] | `ओस` [oːs] "dew" |
| औ | ौ | [ɔː] | `औरत` [ɔːɾɐt] "woman" |

---

## Nasalization

| Symbol | Name | Function | IPA |
|:---:|:---:|:---|:---:|
| ं | Anusvara | Nasalizes preceding vowel; before consonants assimilates to place | [̃] / [m/n/ŋ] |
| ँ | Chandrabindu | Pure nasalization of vowel | [̃] |

Examples:
- `हाँ` [hɑ̃ː] "yes"
- `अंग` [ɐŋɡ] "body part" (anusvara before velar → [ŋ])
- `अंत` [ɐnt] (anusvara before dental → [n])

---

## Perso-Arabic Loans (Nukta Letters)

Hindi has borrowed consonants via Perso-Arabic loanwords, marked with a dot (nukta):

| Grapheme | IPA | Origin | Example |
|:---:|:---:|:---|:---|
| क़ | [q] | Arabic قاف | `क़िस्मत` "fate" |
| ख़ | [x] | Arabic/Persian خ | `ख़त` "letter" |
| ग़ | [ɣ] | Arabic/Persian غ | `ग़ैर` "other" |
| ज़ | [z] | Arabic/Persian ز | `ज़मीन` "earth" |
| फ़ | [f] | Arabic/Persian ف | `फ़र्क` "difference" |

Many speakers, especially in colloquial speech, replace these with native equivalents (q→k, x→kh, z→j, f→ph).

---

## References

- Masica, C.P. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
- Ohala, M. (1983). *Aspects of Hindi Phonology*. Motilal Banarsidass.
- Pandey, P. (2014). Hindi. In: *Phonologies of Asia and Africa*. Eisenbrauns.
- Wikipedia: [Hindi phonology](https://en.wikipedia.org/wiki/Hindi_phonology)

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)
