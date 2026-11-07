# Transcription conventions: Papiamentu (Papiamento) (pap)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable of every word of two or more syllables. Do not mark monosyllables, whether content or function words. Placement follows the FPI spelling rule. (1) If the word has an acute vowel (á é í ó ú), that syllable is stressed: kachó [kaˈtʃo], muhé [muˈhe], akí [aˈki], kantá [kanˈta], lápis [ˈlapis]. (2) Otherwise, a word ending in a vowel or a falling diphthong takes penultimate stress: mesa [ˈmesa], kanta [ˈkanta], tabata [taˈbata], Kòrsou [ˈkɔɾsou̯], Papiamentu [papiaˈmentu]. (3) Otherwise, a word ending in a consonant takes final stress: kanal [kaˈnal], señor [seˈɲoɾ]. (4) The plural suffix -nan is never stressed, and the stem keeps its own stress: bukinan [ˈbukinan], kachónan [kaˈtʃonan], kasnan [ˈkasnan]. (5) Unadapted Dutch or English loans whose stress breaks rules 2–3 without an acute take their usual pronunciation: dòkter [ˈdɔkteɾ]. To count syllables, a falling diphthong (ai ei oi ui au eu ou) is one nucleus. Any other two adjacent vowel letters are two syllables, except u after k or g before a vowel (see glides). Papiamentu has no phonemic vowel length, no geminates and no case endings, so none are written. Römer's lexical tone (e.g. noun/verb pitch contrasts) is not transcribed; only stress is marked.

Source: Fundashon pa Planifikashon di Idioma (2009), Ortografia di papiamentu, rules on the acute accent; Römer (1991), Studies in Papiamentu tonology, on the stressed syllables marked by the acute; Kouwenberg & Murray (1994), phonology chapter. The spec note 'penultimate by default' is refined here to the FPI vowel-final vs consonant-final rule.

## Stressed and unstressed words

Function words carry no stress mark in connected speech. Most are monosyllabic, so they fall under the no-mark-on-monosyllables rule. They include: articles e [e] and un [un]; TMA markers ta [ta], a [a], lo [lo]; negation no [no]; subject and object pronouns mi [mi], bo [bo], e [e], nos [nos], nan [nan]; prepositions di [di], na [na], pa [pa], ku [ku], den [den]; and conjunctions i [i], ku [ku], ma [ma], of [of]. Polysyllabic function words keep their lexical stress mark, so every polysyllable is treated alike: tabata [taˈbata], boso [ˈboso], riba [ˈriba], pero [ˈpeɾo], ainda [aˈinda]. Emphatic pronouns are stressed content forms: ami [aˈmi], abo [aˈbo], aboso [aˈboso]. Do not reduce the vowels of function words; Papiamentu has no schwa reduction.

Source: Kouwenberg & Murray (1994), sections on pronouns and the preverbal TMA markers ta, a, lo; FPI (2009) for the spelling of the forms.

## Pausal forms

Does not apply: Papiamentu has no pausal forms, case endings or nunation. Words are written identically at a comma, at the end of a sentence and inside the sentence.

Source: Kouwenberg & Murray (1994), phonology and morphology chapters (no pausal morphology described).

## Connected speech

Write every word in its citation form, in its own place. Do not write elision, vowel coalescence, liaison, linking, cross-word nasal or voicing assimilation, or resyllabification across word boundaries. Examples: mi a bai [mi a bai̯], e kas [e kas], nan ta kome [nan ta ˈkome]. If the text itself contracts with an apostrophe (e.g. m'a), the engine splits it into two words. Transcribe each piece as written: m [m], a [a].

Source: Kouwenberg & Murray (1994), phonology chapter (citation forms); FPI (2009) spelling as the basis for word forms.

## Glides and diphthongs

Orthographic consonantal ⟨y⟩ and ⟨w⟩ are [j] and [w]: yu [ju], awa [ˈawa], ayera [aˈjeɾa]. ⟨ll⟩ in a loan is [j]. The second element of a falling diphthong is non-syllabic [i̯ u̯]: bai [bai̯], kai [kai̯], rei [rei̯], boi [boi̯], Kòrsou [ˈkɔɾsou̯], dau [dau̯]. ⟨u⟩ after k or g before a vowel is [w]: kuater [ˈkwateɾ], guiá [ɡwiˈa]. Any other ⟨i u⟩ next to a vowel is a full syllable nucleus [i u]: dia [ˈdia], papia [paˈpia], Papiamentu [papiaˈmentu].

Source: FPI (2009), treatment of ⟨y w⟩ and the vowel digraphs; Kouwenberg & Murray (1994), phonology chapter, phonemic diphthongs ai ei oi au.

## Other choices

### mid and front rounded vowels

Plain ⟨e o⟩ are [e o] in every position, including closed syllables: mesa [ˈmesa], kome [ˈkome], kanta [ˈkanta]. Only grave ⟨è ò⟩ are written [ɛ ɔ]: Kòrsou [ˈkɔɾsou̯], bèrdè [ˈbɛɾdɛ]. ⟨ü⟩ is [y] (hür [hyɾ]) and ⟨ù⟩ is [ʏ] (bùs [bʏs]). Acute vowels are the base vowels plus stress. Do not apply free [e]~[ɛ], [o]~[ɔ] variation beyond what the spelling shows.

Source: FPI (2009), diacritics è ò ù ü; Kouwenberg & Murray (1994) describe the [e]~[ɛ], [o]~[ɔ] variation, which is fixed here by the spelling.

### coda /s/

Write ⟨s⟩ as [s] in every position, including codas and word-final: kas [kas], mas [mas], nos [nos], lápis [ˈlapis]. Write [ʃ] only for ⟨sh⟩: mashá [maˈʃa], kos [kos] but kosh- forms [koʃ]. This departs from the spec note's coda-/s/ palatalisation rule. Palatalisation of coda /s/ is not part of the standard Curaçao/Bonaire pronunciation, which keeps [s].

Source: Standard pronunciation as reflected in FPI (2009) phonemic spelling (⟨s⟩ vs ⟨sh⟩ contrast); departs from the note attributed to Kouwenberg & Murray (1994).

### consonant symbols

⟨r⟩ = [ɾ] (bira [ˈbiɾa], kòr [kɔɾ]); ⟨g⟩ = [ɡ] in all positions, with no spirantisation of b d g; ⟨h⟩ = [h] (muhé [muˈhe]); ⟨ch⟩ = [tʃ]; ⟨dj⟩ = [dʒ]; ⟨sh⟩ = [ʃ]; ⟨zh⟩ = [ʒ]; ⟨ñ⟩ = [ɲ]. Within a word, write n before k or g as [ŋ] (lenga [ˈleŋɡa]). Write coda n elsewhere as [n], with no nasal vowels: tin [tin], un [un].

Source: Kouwenberg & Murray (1994), consonant inventory; FPI (2009) grapheme values.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
