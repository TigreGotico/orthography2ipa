# Transcription conventions: Azorean Portuguese (pt-PT-x-acores)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Primary stress follows ordinary Portuguese lexical stress. A written acute or circumflex accent marks the stressed syllable (número [ˈnymɨɾu], está [ɨʃˈta]). Unaccented words ending in -a, -e, -o (plus -s), -am, -em or -ens are stressed on the penult (fruta [ˈfɾytɐ], custa [ˈkyʃtɐ]). Other unaccented words, ending in -l, -r, -z, -i, -u, -im, -um, -ã, -ão or -ões, are stressed on the final syllable (azul [ɐˈzuɫ], falar [fɐˈlaɾ]). Write ˈ before the onset of the stressed syllable in every word of two or more syllables. Leave monosyllables unmarked whether or not they are stressed (tu [ty], pão [pɐ̃w]). Do not mark secondary stress. Portuguese has no phonemic long vowels, no geminates and no case endings, so none of these bear on stress. Stress controls the Azorean (São Miguel-class) fronting: a stressed oral /u/ is [y] (fruta [ˈfɾytɐ], uma [ˈymɐ], tu [ty]). It stays [u] before a coda liquid in the same syllable (azul [ɐˈzuɫ], surdo [ˈsuɾdu]). A coda sibilant does NOT block fronting, as in the gold custa [ˈkyʃtɐ]; this disagrees with the spec's note that sibilants block it. Unstressed /u/ and nasal /ũ/ are never fronted (fumar [fuˈmaɾ], mundo [ˈmũdu]).

Source: Stress placement: Mateus & d'Andrade 2000, ch. 6 (word stress). Stressed /u/ fronting: Rogers 1948 on São Miguel/eastern Azores [y], as modelled in the spec's ACO rules and gold.

## Stressed and unstressed words

These words are proclitic or enclitic and unstressed, written with reduced vowels and no stress mark: articles o [u], a [ɐ], os [uʃ], as [ɐʃ]; contractions no [nu], do [du], ao [aw], pelo [ˈpelu]→ write [pɨlu]; prepositions de [dɨ], em [ɐ̃j], por [puɾ], com [kõ], para [pɐɾɐ]; conjunctions e [i], que [kɨ], se [sɨ], mas [mɐʃ]; clitic pronouns me [mɨ], te [tɨ], se [sɨ], lhe [ʎɨ], o/a [u]/[ɐ], nos [nuʃ]. They never front /u/: the article o is [u], never [y]. The numeral and article um/uns are [ũ]/[ũʃ]. Stressed words, fronted where applicable, are: stressed pronouns (tu [ty], ele [ˈelɨ], nós [nɔʃ]), uma [ˈymɐ], auxiliaries and copulas (é [ɛ], está [ɨʃˈta], tem [tɐ̃j]), and the negator não [nɐ̃w].

Source: Clitic guard pinned in the spec's word_exceptions; reduced clitic forms per Mateus & d'Andrade 2000, ch. 2 and ch. 6 (vowel reduction, clitics).

## Pausal forms

Not applicable. Portuguese has no pausal forms, case endings or nunation. Every word is written in the same form at a sentence end, at a comma and sentence-medially. Final unstressed -e is always written [ɨ] and final -o is always [u], never deleted (noite [ˈnojtɨ], fruto [ˈfɾytu]). The only position-sensitive process is the final-sibilant rule under connected_speech, where a pause counts as a voiceless context: [ʃ].

Source: Mateus & d'Andrade 2000, ch. 2 (citation forms of unstressed vowels).

## Connected speech

Only the word-final sibilant changes across a boundary. Each word stays in its own slot, and vowel elision and crasis are NOT written (de uma [dɨ ˈymɐ], a água [ɐ ˈaɣwɐ]). A final -s/-z is [ʃ] before a voiceless consonant or a pause (as casas [ɐʃ ˈkazɐʃ]). It is [ʒ] before a voiced consonant (os dias [uʒ ˈdiɐʃ]). It is also [ʒ] before a vowel-initial word, which is the Azorean/São Miguel sandhi, not standard [z] (os olhos [uʒ ˈɔʎuʃ], és o número um [ɛʒ u ˈnymɨɾu ũ]). Final -r stays [ɾ] in every context. Final -l stays [ɫ] in every context (mal estar [maɫ ɨʃˈtaɾ]).

Source: [ʒ] prevocalic sandhi: Portuguese With Leo 2021, as grounded in the spec's PT_FINAL_S_PREVOCALIC_VOICE override; this departs from the standard EP [z] of Mateus & d'Andrade 2000, ch. 5. Voicing before voiced consonants: Mateus & d'Andrade 2000.

## Glides and diphthongs

Write diphthong offglides as non-syllabic [j] and [w], never i̯ u̯: pai [paj], mau [maw], mãe [mɐ̃j], pão [pɐ̃w], limões [liˈmõjʃ]. Write nasal diphthongs with a tilde on the nucleus only. The ou digraph keeps the Azorean diphthong [ow], unlike Lisbon [o] (touradas [towˈɾadɐʃ], outro [ˈowtɾu]). The ei digraph is written [ɐj] as in the pt-PT base (primeiro [pɾiˈmɐjɾu]). Unstressed i or u before a vowel is written as a syllabic vowel, not a glide (piano [piˈɐnu]). The gu/qu sequence before a vowel is written with [w] (quatro [ˈkwatɾu], água [ˈaɣwɐ]). Nasal diphthongs are NOT reduced to vowel plus nasal: [ɐ̃w], [õjʃ], not the Madeiran [õns].

Source: Mateus & d'Andrade 2000, ch. 3 (glides and diphthongs); /ow/ preservation per the spec's ou → [ow] override and Rogers 1948.

## Other choices

### Unstressed vowel reduction

Use the inherited EP reduction. Unstressed /a/ is [ɐ], unstressed /e/ is [ɨ] (word-initial e- before s is [ɨ]: estar [ɨʃˈtaɾ]), and unstressed /o/ is [u]. Stressed /a/ before a nasal consonant is [ɐ] (cama [ˈkɐmɐ]). Sporadic island /e/→/i/ raising is not written.

Source: Mateus & d'Andrade 2000, ch. 2.

### Rhotics and laterals

Write initial r-, rr, and r after n, l or s as [ʁ] (rato [ˈʁatu], carro [ˈkaʁu]). Write all other r as [ɾ]. Write coda /l/ as [ɫ] and onset /l/ as [l]. The São Miguel [ʎ] for /l/ after /i/ is not written in this general node.

Source: Mateus & d'Andrade 2000, ch. 1 and ch. 5; [ʎ] excluded per the spec's node split to pt-PT-x-sao-miguel.

### Voiced stop lenition

Write /b d g/ as [β ð ɣ] after a vowel, inside a word or after a vowel-final word (cada [ˈkaðɐ], lago [ˈlaɣu]). Write them as [b d g] word-initially after a pause, after a nasal, and after [ɫ] for /d/.

Source: Mateus & d'Andrade 2000, ch. 1.

### Lexical island shibboleths

Do not write lexical variants such as boi [bô], pastar [pɐʃˈtâ] or Terceira's non-fronted muda. Use the regular forms: boi [boj], pastar [pɐʃˈtaɾ], muda [ˈmydɐ].

Source: The spec's documented limits; fronting per Rogers 1948.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
