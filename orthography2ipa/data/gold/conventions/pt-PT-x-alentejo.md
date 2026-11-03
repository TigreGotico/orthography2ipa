# Transcription conventions: Alto Alentejo Portuguese (pt-PT-x-alentejo)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable in every lexical word, including monosyllables ([ˈmaɾ], [ˈpɐ̃w]). Leave clitics unmarked (see function_words). Do not mark secondary stress.

Placing the stress:
- A written acute, circumflex or grave accent marks the stressed vowel (café [kɐˈfɛ], você [vɔˈse]).
- Otherwise a tilde marks it (irmã [iɾˈmɐ̃], órgão keeps its acute).
- Otherwise, words ending in -a, -e, -o, -as, -es, -os, -am, -em, -ens take stress on the penult (casa [ˈkazɐ], falam [ˈfalɐ̃w]).
- All other words take final stress, including -i, -u, -im, -um, -r, -l, -z (azul [ɐˈzyɫ], falar [fɐˈlaɾ]).
- Hyphen-split pieces are stressed separately.

Syllable placement of ˈ: put the mark before the whole onset cluster ([pɾiˈmeɾ]). A preceding coda stays before the mark ([ɨʃˈta]).

Final-vowel deletion (see other) never moves the stress: cesto [ˈseʃt], leite [ˈlet].

Portuguese has no phonemic long vowels, geminates or case endings. Write no ː. Double rr and ss are single segments ([ˈkaru], [ˈpasu] before deletion).

Source: Mateus & d'Andrade (2000), ch. 6 (word stress); Cunha & Cintra (1984), chapter on orthographic accentuation. This is the standard EP stress system, which Alentejano shares.

## Stressed and unstressed words

Unstressed clitics carry no ˈ. They never undergo stressed-/u/ fronting or final-vowel deletion.

Unstressed list:
- Articles: o [u], a [ɐ], os [uʃ], as [ɐʃ], um [ũ], uns [ũʃ].
- Prepositions and contractions: de [dɨ], do [du], da [dɐ], dos [duʃ], em [ẽj], no [nu], na [nɐ], nos [nuʃ], a [ɐ], à [a], ao [aw], aos [awʃ], por [puɾ], pelo [pɨlu], pela [pɨlɐ], para [pɐɾɐ], com [kõ], sem [sẽj].
- Conjunctions: e [i], ou [o], que [kɨ], se [sɨ], mas [mɐʃ], nem [nẽj], porque [puɾkɨ].
- Object and reflexive clitics, including hyphen-split ones: me [mɨ], te [tɨ], se [sɨ], lhe [ʎɨ], lhes [ʎɨʃ], nos [nuʃ], vos [vuʃ], o/a/os/as, lo/la [lu]/[lɐ].
- Relative que [kɨ].

Stressed list (ˈ, full rules apply):
- Subject and strong pronouns: eu [ˈew], tu [ˈty], ele [ˈel], ela [ˈɛlɐ], nós [ˈnɔʃ], eles [ˈelɨʃ], mim [ˈmĩ].
- Possessives: meu [ˈme], sua [ˈsyɐ].
- uma/umas: [ˈymɐ], [ˈymɐʃ].
- Demonstratives: isto [ˈiʃt].
- Adverbs and interrogatives: como [ˈkom], não [ˈnɐ̃w].
- All verb forms, including auxiliaries: é [ˈɛ], está [ɨʃˈta], tem [ˈtẽj], foi [ˈfoj], há [ˈa].

Source: Mateus & d'Andrade (2000), ch. 6 on clitics and prosodic words. The um/uns/o/os/no/do/pelo guard follows the specification's proclitic guard; Brissos (2014) states that /u/-palatalisation is stressed-only.

## Pausal forms

Does not apply: Portuguese has no pausal forms, case endings or nunation.

Write every word the same way at a pause, at a comma and sentence-internally. Final-vowel deletion is a word-level rule applied in all positions (cesto [ˈseʃt] everywhere).

The only position-dependent item is coda /s/, governed by connected_speech: [ʃ] at a pause or comma (casas [ˈkazɐʃ]).

Source: Mateus & d'Andrade (2000), ch. 2–3. Brissos (2014) treats final-vowel deletion as a general word-final feature, not a pausal one.

## Connected speech

Only coda /s/ sandhi is written across word boundaries. It is written on the end of the first word, and every word keeps its own place.

Word-final s/z/x, chosen by the start of the next word:
- [z] before a vowel-initial word: os amigos [uz ɐˈmiguʃ].
- [ʒ] before a voiced consonant: os dias [uʒ ˈdiɐʃ].
- [ʃ] before a voiceless consonant, at a comma or at the sentence end: os pés [uʃ ˈpɛʃ].

No other cross-word process is written:
- No vowel elision or merger between words: que é [kɨ ˈɛ], a água [ɐ ˈagwɐ].
- No glide formation and no nasal liaison: em casa [ẽj ˈkazɐ].
- No resyllabification marks: final /l/ stays [ɫ] and final /ɾ/ stays [ɾ] before a vowel (mal ou [ˈmaɫ o], mar alto [ˈmaɾ ˈaɫt]).
- Words left consonant-final by deletion are written as is before vowels: sete anos [ˈsɛt ˈɐnuʃ].

Write b d g as stops (no [β ð ɣ] in broad transcription).

Source: Mateus & d'Andrade (2000), ch. 2–3 (coda /s/ realisation and its voicing before vowels and voiced consonants). This is standard EP, shared by the southern dialects.

## Glides and diphthongs

Write off-glides and on-glides as [j] and [w], never i̯ or u̯: pai [ˈpaj], mau [ˈmaw], noite [ˈnojt], água [ˈagwɐ], história [iʃˈtɔɾjɐ], sério [ˈsɛɾju].

Nasal diphthongs: put the tilde on the first element only. Examples: não [ˈnɐ̃w], mãe [ˈmɐ̃j], põe [ˈpõj], muito [ˈmũjt], bem [ˈbẽj].

Monophthongisation (the dialect has no glide here, so write none):
- ei becomes [e]: leite [ˈlet], primeiro [pɾiˈmeɾ], falei [fɐˈle].
- ou becomes [o]: pouco [ˈpok], ou [o].
- eu in possessives meu/teu/seu (and plurals) and in 3sg preterite -eu becomes [e]: meu [ˈme], comeu [kuˈme].
- The pronoun eu keeps [ˈew].

Hiatus from /d/-loss is written as two full vowels, not a glide: nada [ˈnaɐ], cansado [kɐ̃ˈsau].

Source: Mateus & d'Andrade (2000), ch. 3 (glides [j w] and nasal diphthongs). The ei/ou/eu monophthongs follow Cintra (1971) on southern monophthongisation and the specification's notes (4)–(5).

## Other choices

### Stressed /u/ fronting

Write stressed oral /u/ as [y]: tu [ˈty], azul [ɐˈzyɫ], fumo [ˈfym], uva [ˈyvɐ], fruta [ˈfɾytɐ], tudo [ˈtyd].

Keep [u] when the consonant immediately before it is p, b or m: mudo [ˈmud], fumo has f so it is fronted, pura [ˈpuɾɐ], muro [ˈmuɾ].

Unstressed /u/ and nasal [ũ] are never fronted: nunca [ˈnũkɐ], um [ũ].

The symbol [y] covers the phonetic range [ʉ]~[y]. Brissos 2014b reports it as mostly central [ʉ] in the Centro-Interior; this convention keeps the specification's single symbol.

Source: Cintra (1971), zone-defining isogloss; Brissos (2014b), pp. 87–89 (bilabial condition); Brissos & Saramago (2014), pp. 55–59.

### Final unstressed vowel deletion

In stressed lexical words, delete absolute word-final unstressed -o [u], -e [ɨ] and -i when a consonant precedes: cesto [ˈseʃt], leite [ˈlet], sete [ˈsɛt], ele [ˈel], primeiro [pɾiˈmeɾ].

Keep the vowel in these cases:
- After a vowel or glide: rio [ˈriu], sério [ˈsɛɾju].
- Before plural -s: cestos [ˈseʃtuʃ], leites [ˈletɨʃ].
- Final -a [ɐ] is always kept.
- Clitics keep their vowels.

This departs from the specification's own examples leite [ˈletɨ] and primeiro [pɼiˈmeɼu]; the deletion rule is applied consistently instead. Write the tap as [ɾ], not ɼ.

Source: Brissos (2014), documenting the deletion of final [u]; Lüdtke (1956/57) as summarised in Cintra (1971), note 58.

### Intervocalic /d/ loss

Delete /d/ only in words of two or more syllables ending in stressed -ado(s), -ada(s), -ido(s), -ida(s): nada [ˈnaɐ], vida [ˈviɐ], cansado [kɐ̃ˈsau], partida [pɐɾˈtiɐ]. The final vowel is kept in hiatus. cada is an exception: [ˈkɐdɐ].

Keep /d/ elsewhere: tudo [ˈtyd], mudo [ˈmud], todo [ˈtod]. This departs from the specification's blanket rule and its mudo→[ˈmu], following Brissos's attested [tˈyd].

Source: Brissos (2014), example tudo [tˈyd]; specification note (3), restricted.

### Rhotics and laterals

Strong r (word-initial, rr, after n/l/s) is the alveolar trill [r]: rio [ˈriu], carro [ˈkar]. Write no Lisbon uvular [ʁ].

All other r is the tap [ɾ].

Coda and word-final /l/ is [ɫ]; the specification's ł means [ɫ]: mal [ˈmaɫ], alto [ˈaɫt]. Onset /l/ is [l].

Source: Mateus & d'Andrade (2000), ch. 2 (regional trill vs uvular; velarised /l/).

### Southern vocalism vs Lisbon

There is no Lisbon centralisation of /e/ before palatals: telha [ˈteʎɐ], espelho [ɨʃˈpeʎ].

Nasal -em/-ém is [ẽj], not [ɐ̃j]: bem [ˈbẽj], também [tɐ̃ˈbẽj].

Unstressed reduction follows standard EP: a becomes [ɐ], e becomes [ɨ], o becomes [u].

Stressed open e is written [ɛ] without breaking. The specification's lexically restricted [ɛ͜ɐ] has no word list, so it is not written.

Source: Mateus & d'Andrade (2000), ch. 2–3 (Lisbon-specific centralisation); Cintra (1971) and Brissos (2014) on southern vocalism.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
