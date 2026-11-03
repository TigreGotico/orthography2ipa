# Transcription conventions: Transmontano Portuguese (pt-PT-x-trasosmontes)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Primary stress is lexical and is read from the spelling. An acute or circumflex accent marks the stressed syllable, and a tilde marks it when no other accent is written. Without an accent, words ending in a, e, o (optionally followed by s), am, em or ens are stressed on the penult. All other words are stressed on the final syllable. Write ˈ before the onset of the stressed syllable in every stressed word, monosyllables included: chave [ˈtʃabɨ], passo [ˈpas̺u], cozer [kuˈzeɾ], café [kɐˈfɛ], chá [ˈtʃa], mês [ˈmes̺], não [ˈnɐ̃w̃]. Unstressed function words (see function_words) get no mark. Secondary stress is never marked. Stress decides vowel quality. Stressed vowels are [a ɐ ɛ e i ɔ o u] and nasal [ɐ̃ ẽ ĩ õ ũ]. Unstressed ⟨a e o⟩ reduce to [ɐ ɨ u]: pequeno [pɨˈkenu], cidade [s̺iˈdadɨ]. Word-initial unstressed ⟨e⟩ before a coda sibilant is [i]: estar [iʃˈtaɾ]. Vowel length, geminates and case endings do not apply: Portuguese has no phonemic length and no geminates (⟨ss⟩ = [s̺], ⟨rr⟩ = [r]), and no case endings.

Source: Standard EP stress and reduction as in Mateus & d'Andrade 2000, ch. 6 (stress) and ch. 2 (vowel reduction), inherited unchanged by the Transmontano delta.

## Stressed and unstressed words

The following are unstressed: no ˈ, reduced vowels, one citation form each. Definite articles: o [u], a [ɐ], os [us̺], as [ɐs̺]. Clitic pronouns: me [mɨ], te [tɨ], se [s̺ɨ], lhe [ʎɨ], lhes [ʎɨs̺], nos [nus̺], vos [bus̺], o/a/lo/la [u ɐ lu lɐ]. Prepositions: de [dɨ], em [ɐ̃j̃], com [kõ], por [puɾ], para [pɐɾɐ], sem [s̺ɐ̃j̃], a [ɐ]. Contractions: do [du], da [dɐ], no [nu], na [nɐ], ao [aw], à [a], pelo [pɨlu], pela [pɨlɐ], num [nũ]. Conjunctions: e [i], que [kɨ], se [s̺ɨ], mas [mɐs̺], ou [ow], nem [nɐ̃j̃], porque [puɾkɨ]. A clitic split off by a hyphen is its own unstressed word: dá-me [ˈda mɨ], fazê-lo [fɐˈze lu]. The following carry stress: indefinite articles um [ˈũ], uma [ˈumɐ]; strong pronouns eu [ˈew], tu [ˈtu], ele [ˈelɨ], mim [ˈmĩ]; possessives meu [ˈmew]; demonstratives; numerals; não [ˈnɐ̃w̃]; interrogatives quê [ˈke], quando [ˈkwɐ̃du]; other polysyllabic adverbs and conjunctions (como [ˈkomu]); and every verb form, auxiliaries included: é [ˈɛ], está [iʃˈta], tem [ˈtɐ̃j̃], há [ˈa], foi [ˈfoj]. Run the sandhi rules of connected_speech on these forms.

Source: Standard EP clitic and weak forms, Mateus & d'Andrade 2000, ch. 6 (prosodic word and clitics), with Transmontano segment deltas from Cintra 1971:87, 93.

## Pausal forms

Portuguese has no pausal morphology. Final unstressed vowels keep their reduced quality before a pause and are never dropped: chave [ˈtʃabɨ], passo [ˈpas̺u], casa [ˈkaz̺ɐ]. Case endings and nunation (tanwīn) do not apply. The only pause-conditioned choice is the word-final sibilant. Before a pause (sentence end or any punctuation, comma included), final ⟨s⟩ and ⟨z⟩ are written [s̺]: chaves [ˈtʃabɨs̺], vez [ˈbes̺], mês [ˈmes̺]. This departs from the Lisbon/inherited and CLUP-gold pausal [ʃ] (chaves [ˈtʃaβɨʃ]), following the spec's word-final [s̺]. Final ⟨r⟩ stays [ɾ]: falar [fɐˈlaɾ]. Final ⟨l⟩ stays [ɫ]: sol [ˈs̺ɔɫ].

Source: Cintra 1971, note 29 to p. 93 ('[s̺] ápico-alveolar (correspondente a s inicial e final ...)'); vowel retention per Mateus & d'Andrade 2000, ch. 2.

## Connected speech

The only cross-word process written is the word-final sibilant sandhi. It changes only the final segment of the first word, and both words stay separate. (1) Before a vowel-initial word, write voiced apical [z̺]: os amigos [uz̺ ɐˈmiɡus̺], mas eu [mɐz̺ ˈew], dez anos [ˈdɛz̺ ˈɐnus̺]. This follows Cintra's [z̺] for intervocalic s. It is not the [ʒ] attested for one Chaves speaker, and not the inherited laminal [z]. (2) Before a voiceless consonant, write [ʃ]: as casas [ɐʃ ˈkaz̺ɐs̺]. (3) Before a voiced consonant, write [ʒ]: os dias [uʒ ˈdiɐs̺], mais longe [ˈmajʒ ˈlõʒɨ]. These match word-internal preconsonantal chiado: festa [ˈfɛʃtɐ], mesmo [ˈmeʒmu]. (4) Before a pause, write [s̺] (see pausal_forms). The following are not written: vowel elision, crasis, glide formation and resyllabification across word boundaries; [β ð ɣ] spirantisation; and nasal or place assimilation. Every other word keeps its citation form: de amigo [dɨ ɐˈmiɡu], que eu [kɨ ˈew], mal aberto [ˈmaɫ ɐˈbɛɾtu], falar alto [fɐˈlaɾ ˈaɫtu].

Source: Sandhi pattern of standard EP, Mateus & d'Andrade 2000, ch. 2/5. The apical values follow Cintra 1971:93 and note 29. The prevocalic [ʒ] is reported only by Portuguese With Leo 2022 and is not adopted.

## Glides and diphthongs

Write non-syllabic vocoids as [j] and [w], never as i̯ or u̯. Oral falling diphthongs: pai [ˈpaj], mau [ˈmaw], foi [ˈfoj], céu [ˈsɛw], eu [ˈew], dói [ˈdɔj]. Nasal diphthongs carry a tilde on both elements: não [ˈnɐ̃w̃], mãe [ˈmɐ̃j̃], põe [ˈpõj̃], muito [ˈmũj̃tu]. Northern conservative values replace the Lisbon ones. ⟨ei⟩ is [ej], not Lisbon [ɐj]: primeiro [pɾiˈmejɾu], leite [ˈlejtɨ]. ⟨ou⟩ is the diphthong [ow], not monophthongal [o]: pouco [ˈpowku], ou [ow]. ⟨ão⟩ is [ɐ̃w̃], never [õ] or [ɐ̃n]: cão [ˈkɐ̃w̃]. Final ⟨em⟩ and ⟨ens⟩ keep the inherited [ɐ̃j̃]: bem [ˈbɐ̃j̃], também [tɐ̃ˈbɐ̃j̃]. Unstressed ⟨i⟩ or ⟨u⟩ before a vowel in the same word is a rising glide: história [iʃˈtɔɾjɐ], água [ˈaɡwɐ], quando [ˈkwɐ̃du]. Write two syllabic vowels only where the spelling shows hiatus with an accent: saúde [s̺ɐˈudɨ], país [pɐˈis̺].

Source: Cintra 1971 (conservation of ou and ei as a northern trait in the classification); Mateus & d'Andrade 2000, ch. 2 (glide notation and nasal diphthongs); ão retention confirmed by Portuguese With Leo 2022.

## Other choices

### Four-sibilant system

Use the apical series [s̺ z̺] for spelled ⟨s⟩ and the laminal series [s z] for ⟨c ç z⟩. Word-initial ⟨s⟩, ⟨s⟩ after a consonant, and ⟨ss⟩ are [s̺]: sapo [ˈs̺apu], pensar [pẽˈs̺aɾ], passo [ˈpas̺u]. Intervocalic ⟨s⟩ is [z̺]: casa [ˈkaz̺ɐ], coser [kuˈz̺eɾ]. ⟨c⟩ before e/i and ⟨ç⟩ are [s]: paço [ˈpasu], cedo [ˈsedu]. Onset ⟨z⟩ is [z]: cozer [kuˈzeɾ]. Preconsonantal coda ⟨s⟩ is [ʃ] or [ʒ]. Always use Cintra's [s̺ z̺], never [ʂ ʐ].

Source: Cintra 1971:93 and note 29; Álvarez Pérez 2014, §4, pp. 36–38.

### Affricate ⟨ch⟩

⟨ch⟩ is [tʃ] and ⟨x⟩ is [ʃ] (or a lexical [ks], [s] or [z]): chave [ˈtʃabɨ], chá [ˈtʃa], xaile [ˈʃajlɨ], táxi [ˈtaksi].

Source: Cintra 1971:87 (trait 3).

### Betacism

⟨v⟩ and ⟨b⟩ are both [b] in all positions. Spirant [β] is not written in broad transcription: vento [ˈbẽtu], Chaves [ˈtʃabɨs̺], novo [ˈnobu].

Source: Cintra 1971:87 (trait 1); confirmed by Portuguese With Leo 2022.

### Strong rhotic

Strong r is the apical trill [r]. This covers word-initial ⟨r⟩, ⟨rr⟩, and ⟨r⟩ after n, l or s: rio [ˈriu], carro [ˈkaru], honra [ˈõrɐ]. Single ⟨r⟩ elsewhere is the tap [ɾ]: caro [ˈkaɾu], mar [ˈmaɾ]. This departs from the inherited Lisbon uvular [ʁ], following the traditional northern and interior realisation.

Source: Mateus & d'Andrade 2000, ch. 1 (the alveolar trill as a regional and conservative variant of /R/ beside urban [ʁ]).

### Mid vowels before palatals

Stressed ⟨e⟩ before [ʎ ɲ ʒ ʃ] stays [e] and is not centralised to Lisbon [ɐ]: vermelho [bɨɾˈmeʎu], coelho [kuˈeʎu], telha [ˈteʎɐ]. No Porto-type diphthongisation of stressed [e] or [o].

Source: Portuguese With Leo 2022 (vermelho, not 'vermalho'); Cintra 1971:93 (no baixo-minhoto diphthongisation in this group).

### Laterals and palatals

Onset ⟨l⟩ is [l]. Coda ⟨l⟩ is dark [ɫ], including word-final before a vowel: alto [ˈaɫtu], sol [ˈs̺ɔɫ]. ⟨lh⟩ is [ʎ]. ⟨nh⟩ is [ɲ]. ⟨j⟩ and ⟨g⟩ before e/i are [ʒ]: gente [ˈʒẽtɨ].

Source: Mateus & d'Andrade 2000, ch. 2 (inherited standard EP).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
