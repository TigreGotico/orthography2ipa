# Transcription conventions: Korlai Indo-Portuguese (Korlai Creole Portuguese) (vkp)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Write no stress marks in any word. Published descriptions agree that Korlai stress is lexical. It continues the stressed syllable of the Portuguese etymon, and posttonic vowels are deleted (Port. fáca > fak). After that deletion the stress usually falls on the last remaining syllable. This placement cannot be recovered from Clements' spelling, and the specification declares no stress block, so stress is left unmarked throughout. Examples: fak [fak], kata [kata], butïk [butək], bharig [bʱariɡ]. Korlai has no phonemic vowel length, so there is no ː to place. It has no phonemic geminates: a doubled letter, if met, is written as a single consonant. There are no case endings. There is no lexical tone or pitch accent, and none is written.

Source: Clements 2013 (APiCS survey ch. 40), restating Clements 1996: 59-66; Clements & Koontz-Garboden 2002 (stress preservation with posttonic deletion). The omission of marks follows the specification note, not a claim that stress is absent.

## Stressed and unstressed words

Because no stress is marked anywhere, function words get no stress marks either. Pronouns, the TMA markers, the copula, postpositions and object or possessive markers, conjunctions and negation are all written in their full citation form, with full vowel quality. There are no reduced or weak forms and no vowel reduction to [ə]. Examples: yo [jo] 'I', bo [bo] 'you', ja [dʒa] (past marker), te [te] (present marker).

Source: Clements 1996: 59-66, as restated in Clements 2013 (APiCS ch. 40). Neither describes a strong/weak alternation for Korlai function words.

## Pausal forms

Does not apply. Korlai has no case endings and no nunation, and there is no described pausal alternation. Every word is written in the same form at a sentence end, at a comma and sentence-internally. Final vowels are kept as written: kata [kata].

Source: Clements 1996: 59-66; Clements 2013 (APiCS ch. 40). No pausal phenomena are reported.

## Connected speech

No cross-word processes are written. There is no assimilation, elision, liaison, linking consonant or resyllabification across word boundaries. Each word keeps its citation form in its own place, separated by single spaces. Word-internal phonology, such as nasal vowels and aspiration, is written as part of each word. Example: ɔ̃m kharm [ɔ̃m kʰarm], not [ɔ̃ŋ kʰarm].

Source: Clements 2013 (APiCS ch. 40) and Clements 1996 describe no obligatory external sandhi. Writing citation forms follows the specification's broad, word-by-word design.

## Glides and diphthongs

Glides are written as the consonant symbols [j] and [w], never as i̯ or u̯. A diphthong is written as vowel + [j] or [w], and a nasal vowel keeps its tilde before the glide: lɔ̃j [lɔ̃j] 'far'. Clements' ⟨y⟩ is written [j]: yo [jo]. ⟨j⟩ is ambiguous and is resolved by position. After a vowel at the end of a syllable or word it is the glide [j], as in lɔ̃j [lɔ̃j]. Before a vowel it is the affricate [dʒ], continuing Portuguese /ʒ/, as in ja [dʒa]. Prevocalic ⟨w⟩ or ⟨u⟩ before another vowel in the same syllable is written [w].

Source: Clements 2013 (APiCS ch. 40), example lɔ̃j; specification note 5 on the ⟨j⟩ ambiguity. The prevocalic [dʒ] reading follows the Indo-Portuguese reflex of Port. j/g described in Clements 1996.

## Other choices

### Central vowel ⟨ï⟩ and /ã/

The status of the central vowel and of /ã/ is contested. Write ⟨ï⟩ as [ə]: butïk [butək]. Write ⟨ã⟩ as [ã] wherever the source spelling has it. Do not create either vowel where the spelling lacks it.

Source: Clements 2013 (APiCS ch. 40) and the APiCS structure dataset differ on /ə/ and /ã/. The convention follows the specification's choice to write both.

### Aspirated and breathy stops

Write the voiceless C+h digraphs as aspirated stops [pʰ tʰ ʈʰ kʰ]. Write the voiced digraphs as breathy-voiced stops [bʱ dʱ ɡʱ]. Examples: kharm [kʰarm], thɛr [tʰɛr], bharig [bʱariɡ].

Source: Clements 1996: 59-66, via Clements 2013 (APiCS ch. 40).

### Labiodental

Write ⟨v⟩ as the approximant [ʋ] everywhere, never as [v].

Source: Clements 2013 (APiCS ch. 40), South Asian areal feature; specification note 6.

### Affricates and retroflexes

Write affricates without tie bars: [ts dz tʃ dʒ], with ⟨ch⟩ as [tʃ]. Write retroflex stops as [ʈ ʈʰ ɖ] only where the source spelling marks retroflexion. Never write [ɳ] or [ɭ].

Source: Clements 1996: 59-66, via Clements 2013 (APiCS ch. 40).

### Nasal vowels and rhotic

Write nasal vowels with a tilde and do not add a nasal consonant after them: sĩk [sĩk], ɔ̃m [ɔ̃m]. Write the rhotic broadly as [r] in all positions: kharm [kʰarm]. Write voiced velar g as [ɡ]: ag [aɡ].

Source: Clements 2013 (APiCS ch. 40), examples sĩk, ɔ̃m, kharm, ag.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
