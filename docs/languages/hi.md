# Hindi (hi): Phonology Reference

**Code**: `hi` | **Family**: Indo-European > Indo-Iranian > Indo-Aryan | **Script**: Devanagari (abugida) | **Quality tier**: research

The `hi` spec describes Standard Hindi (Khaṛī Bolī) in Devanagari. Its parent is Sanskrit (`sa`). The spec states its own letter table and does not inherit one. Its main rules are the inherent vowel and its deletion, the four-way laryngeal contrast, and the nukta letters of Perso-Arabic loans.

## The Devanagari abugida

Devanagari is an abugida. A consonant letter carries an inherent vowel /ə/, and a vowel sign (mātrā) replaces it. The spec declares /ə/ as its `inherent_vowel`. Hindi deletes the inherent vowel in some positions (see [Schwa deletion](#schwa-deletion)).

| Component | What it does | Engine output |
|:---|:---|:---|
| Consonant letter | Carries the inherent /ə/ | क `kə` |
| Vowel sign (mātrā) | Replaces the inherent vowel | का `kaː` |
| Virama (्) | Removes the inherent vowel | क् `k` |
| Independent vowel | Writes a vowel with no consonant before it | आ `aː` |

## Four-way laryngeal contrast

Hindi stops have four laryngeal categories at each place of articulation (Ohala 1983, Masica 1991):

| Category | Bilabial | Dental | Retroflex | Velar |
|:---|:---:|:---:|:---:|:---:|
| Voiceless unaspirated | प [p] | त [t̪] | ट [ʈ] | क [k] |
| Voiceless aspirated | फ [pʰ] | थ [t̪ʰ] | ठ [ʈʰ] | ख [kʰ] |
| Voiced | ब [b] | द [d̪] | ड [ɖ] | ग [ɡ] |
| Voiced aspirated (breathy) | भ [bʱ] | ध [d̪ʱ] | ढ [ɖʱ] | घ [ɡʱ] |

Dentals and retroflexes contrast. The spec keeps them apart: ताल 'rhythm' gives `t̪aːl`, and टाल 'to put off' gives `ʈaːl`. The nasals are ङ [ŋ], ञ [ɲ], ण [ɳ], न [n] and म [m].

## Retroflex flaps

Between vowels, the retroflex stops ड [ɖ] and ढ [ɖʱ] are flaps [ɽ ɽʱ]. The orthography writes the flaps with a nukta, as ड़ and ढ़, and the spec maps those letters to `ɽ` and `ɽʱ`. The spec has no positional rule for the bare letters, so ड and ढ are always `ɖ` and `ɖʱ`.

| Word | Engine output |
|:---|:---|
| पड़ना 'to fall' | `pəɽnaː` |
| बढ़ना 'to grow' | `bəɽʱnaː` |
| बडा (bare ड) | `bəɖaː` |

## Schwa deletion

Hindi does not pronounce the inherent vowel in two positions. The spec states both as `allophone_rules`, one rule per consonant phoneme.

The `HI_SCHWA_FINAL_*` rules delete the inherent vowel of a word-final consonant letter. They apply after a cluster too, as in शब्द `ʃəbd̪`. They do not apply at the start of a word, so a monosyllabic one-letter word keeps its only vowel: न gives `nə`. The source is Ohala (1983, ch. 5) and Ohala (1999: 101). The `अ` grapheme also has a `word_final` entry that writes nothing.

The `HI_SCHWA_MEDIAL_*` rules delete a medial inherent vowel in the context VC_CV, applied from right to left (Narasimhan, Sproat & Kiraz 2004). The `HI_SCHWA_KEEP_*` rules guard that deletion after a consonant (Ohala 1983, ch. 5).

| Word | Engine output |
|:---|:---|
| कमल 'lotus' | `kəməl` |
| करना 'to do' | `kəɾnaː` |
| अपना 'own' | `əpnaː` |
| राम | `ɾaːm` |

Sanskrit (`sa`) keeps the inherent vowel and declares no such rule. That is why the deletion is in the Hindi data and not in the engine.

## Vowels

| Independent | Mātrā | IPA | Example (engine output) |
|:---:|:---:|:---:|:---|
| अ | (inherent) | [ə] | कमल `kəməl` |
| आ | ा | [aː] | काम `kaːm` 'work' |
| इ | ि | [ɪ] | किताब `kɪt̪aːb` 'book' |
| ई | ी | [iː] | दीवार `d̪iːʋaːɾ` 'wall' |
| उ | ु | [ʊ] | उन `ʊn` 'them' |
| ऊ | ू | [uː] | ऊन `uːn` 'wool' |
| ए | े | [eː] | एक `eːk` 'one' |
| ऐ | ै | [ɛː] | ऐसा `ɛːsaː` 'such' |
| ओ | ो | [oː] | ओस `oːs` 'dew' |
| औ | ौ | [ɔː] | औरत `ɔːɾət̪` 'woman' |

## Nasalisation

Two signs write nasality. Chandrabindu ँ nasalises the vowel. Anusvara ं nasalises the vowel too, and before a consonant it is a nasal at the place of that consonant: अंग is [ɐŋɡ] and अंत is [ɐnt]. The spec writes both signs as nasalisation of the vowel in every position. The `before_consonant` entry of ं is the nasal tilde, not a nasal consonant.

| Word | Engine output |
|:---|:---|
| हाँ 'yes' | `ɦãː` |
| अंग 'body part' | `ə̃ɡ` |
| अंत 'end' | `ə̃t̪` |

## Perso-Arabic loans (nukta letters)

Hindi writes consonants from Perso-Arabic loans with a dot below the letter (nukta). The spec maps each of them:

| Letter | IPA | Origin | Example |
|:---:|:---:|:---|:---|
| क़ | [q] | Arabic ق | क़िस्मत 'fate', `qɪsmət̪` |
| ख़ | [x] | Arabic and Persian خ | ख़त 'letter' |
| ग़ | [ɣ] | Arabic and Persian غ | ग़ैर 'other', `ɣɛːɾ` |
| ज़ | [z] | Arabic and Persian ز | ज़मीन 'earth' |
| फ़ | [f] | Arabic and Persian ف | फ़र्क 'difference' |

Many speakers, mostly in colloquial speech, use the native equivalents (q to k, x to kʰ, z to dʒ, f to pʰ). The spec writes the loan value.

## Known limitations

A word-initial nukta letter with no vowel sign loses its inherent vowel. ख़त gives `xt̪`, ज़मीन gives `zmiːn`, and फ़र्क gives `fɾk`, each with no /ə/ after the first consonant. The same letter keeps its vowel inside a word: मज़ा gives `məzaː`. The precomposed and the decomposed nukta spellings give the same output.

Anusvara before a consonant is nasalisation of the vowel in the output, not a homorganic nasal.

## Gold rows

The `wikipron` row is `crowd-scraped` and can gate. The `vox_communis` row is `epitran-derived`, so it can neither qualify nor block a promotion. For the figures, see the [scoreboard](../scoreboard.md).

## References

- Masica, C.P. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
- Ohala, M. (1983). *Aspects of Hindi Phonology*. Motilal Banarsidass.
- Pandey, P. (2014). Hindi. In: *Phonologies of Asia and Africa*. Eisenbrauns.
- Wikipedia: [Hindi phonology](https://en.wikipedia.org/wiki/Hindi_phonology)

The spec's `sources` also cite Shapiro (1989), Cardona & Jain (2003), Ohala (1999) and Narasimhan, Sproat & Kiraz (2004).

---
[← Hausa](ha.md) · [Home](../index.md) · [Assamese →](as.md)
