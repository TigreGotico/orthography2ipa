# Mirandese (`mwl`) and its sub-dialects

Mirandese (*mirandés*, *lhéngua mirandesa*) is an Asturleonese language of the municipality of Miranda do Douro, in north-eastern Portugal. Portugal has recognised it as a co-official regional language since 1999. It is not a dialect of Portuguese. Its parent in this library is `ast-PT-x-medieval` (Medieval Asturian-Leonese of Portugal), and its features are West Iberian and Leonese, not Portuguese allophony. Modern Mirandese does carry a heavy Portuguese adstrate from schooling and administration, which shows mostly in the reduction of unstressed vowels. The spec `ancestors` list `pt-PT-x-medieval` and `ast-x-sanabria` as adstrates.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`, for the code of its section. Forms in italics are quoted from a source or from the gold. For the scores of the specs, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

| Code | Name | Sub-dialect | Tier |
|:--|:--|:--|:--|
| `mwl` | Mirandese (Central) | Central, the normal speech | research |
| `mwl-x-sendim` | Sendinês | Southern (Vila de Sendim) | research |
| `mwl-x-ifanes` | Ifanês | Northern or Raiano (the border) | research |

The three sub-dialects are the classical division of Vasconcelos (1900). The Central norm is the base of the orthography. The Northern or Raiano speech belongs to the border of the plateau, and Sendinês to Vila de Sendim.

`mwl` follows Leite de Vasconcelos, *Estudos de Philologia Mirandesa* I (1900, EPM), the first phonetic description of the language. Where later sources disagree with him, the spec `notes` quote both sides with their pages. The later reading stays in the lattice as a lower-ranked candidate.

## The sibilant system

Mirandese keeps the medieval Ibero-Romance sibilants that standard Portuguese and Spanish merged. The spec models a contrast of four sibilants and more:

| Spelling | Phoneme | Description |
|:--|:--|:--|
| ⟨s⟩, ⟨ss⟩ | /s̺/ | voiceless apico-alveolar fricative |
| ⟨s⟩ between vowels or before a voiced consonant | /z̺/ | voiced apico-alveolar |
| ⟨c⟩ before ⟨e i⟩, ⟨ç⟩ | /s/ | voiceless dorso-dental fricative |
| ⟨z⟩, word-final ⟨ç⟩ before a voiced consonant | /z/ | voiced dorso-dental |
| ⟨x⟩ | /ʃ/ | voiceless postalveolar |
| ⟨j⟩, ⟨g⟩ before ⟨e i⟩ | /ʒ/ | voiced postalveolar |
| ⟨ch⟩ | /t͡ʃ/ | voiceless postalveolar affricate, which modern European Portuguese changed to /ʃ/ |

The key opposition is apical ⟨s⟩ against dorso-dental ⟨c ç z⟩. The spec writes only the apical series with the IPA retracted diacritic (`s̺`, `z̺`), and it leaves the dorso-dental series plain (`s`, `z`). This is standard IPA and keeps the contrast explicit. It also matches the expert gold `TigreGotico/mirandese_g2p`, which never uses the narrower laminal diacritic `◌̻`. The letter ⟨ç⟩ is a fricative, not the Asturian affricate /t͡s/. It also occurs at the end of a word (*rapaç*, *lhuç*), where Portuguese writes ⟨-z⟩.

The apical ⟨s⟩ voices to [z̺] before a voiced consonant, inside a word and across words: `asno` [ˈaz̺nu], `mesmo` [ˈmez̺mu], `ls nius` [ɫz̺ ˈnjus̺]. A word-final ⟨ç⟩ is [z] before a voiced consonant in the next word: `lhuç del cielo` [ˈʎuz ðɨɫ ˈsjɪlu]. Before a voiceless consonant, a vowel or a pause, both stay voiceless. Vasconcelos (EPM I §13, p. 190) gives the voiced apical *"final de palavra antes de consoante sonora"*. He writes that the voiced dorsal *"em fim de palavra só póde ouvir-se quando a palavra seguinte começa por consoante sonora"*.

The letter ⟨j⟩ is always /ʒ/, as in West Iberian, never the Asturian palatal. The letter ⟨y⟩ is the Spanish palatal [ʝ] (`you` [ˈʝɵw]). Vasconcelos (p. 191) writes *"Como o y castelhano normal em yo"* and gives it as *"Inicial ou medial"*. So a word-final ⟨y⟩ is the glide [j] (`rey` [ˈrej]). The Convenção (letter Y) gives the glide [j], and the spec keeps it as the second candidate.

## Leonese features

Initial ⟨l⟩ is [l]. A written initial ⟨l⟩ is plain /l/ (`lindo` [ˈlĩndu], `litro` [ˈlitɾu]). Vasconcelos (EPM I §13, p. 188) gives *lĩ-ndo* with [l] and describes l as *"Como em português na palavra lapa"*. The Latin initial L that became [ʎ] is written ⟨lh⟩ (§111, p. 259).

The letter ⟨v⟩ is ⟨b⟩. Vasconcelos writes *"Na pronúncia normal mirandesa não existe differença entre b e v"* (§14, p. 193): `vaca` [ˈbakɐ], `uva` [ˈuβɐ], `envidar` [ɨ̃mbiˈðaɾ]. The letter ⟨ê⟩ is [e] (Convenção, letter table E): `yê` [ˈʝe], `yêrba` [ˈʝeɾβɐ]. The digraphs ⟨lh⟩ and ⟨nh⟩ are /ʎ/ and /ɲ/ in all positions.

### Leonese diphthongs

Latin short Ĕ gives ⟨iê ie⟩ [jɪ], and Latin short Ŏ gives ⟨uô uo⟩ [ʊ]: `tierra` [ˈtjɪrɐ], `puorta` [ˈpʊɾtɐ].

Vasconcelos writes the nuclei ẹ̌ and ọ̌ (§2, pp. 173 and 177). He puts ẹ̌ between the *i* of Portuguese *viu* and the *ê* of *cêrca*, close to the *i* of English *fill*. He describes ọ̌ as *"muito semelhante ao u do inglês full, butcher"*. He writes that the diphthong [wo] *"não é normal na falla mirandesa"*, and that it *"só se ouve em emphase ou voz pausada"* (p. 182, Obs. 2).

The Convenção writes the diphthongs [je] and [wo] (footnote 13). The same footnote says that in Duas Igrejas and Constantim *"[wo] é esporádico"*, which agrees with Vasconcelos. In `mwl`, [je] and [wo] are the second candidates, so they stay in the beam for a downstream rescorer. The ọ̌ of Vasconcelos occurs only in a stressed syllable (p. 177). So a final unstressed ⟨-uo⟩ is two vowels: `mútuo` [ˈmutuu].

### Other vowels

The accented ⟨é ó⟩ are [e o]. The Portuguese open vowels *"não existem na pronúncia normal mirandesa"* (§22, p. 198): `pé` [ˈpe], `pós` [ˈpos̺], `chapéu` [tʃɐˈpew]. The Convenção reads the acute accent as a *"qualidade relativamente aberta"*, [ɛ ɔ], and that is the second candidate of ⟨é ó⟩. Plain ⟨e o⟩ have no open candidate.

The digraph ⟨ou⟩ is [ɵw]. The base vowel *ö* of the diphthong *öu* is the *o* of English *go*, *no* (§2, p. 174): `touro` [ˈtɵwɾu].

A final ⟨-on⟩ is [ɵ̃w̃], because Latin -ONE gives *-öũ* (§110, p. 257, *perdigöũ*): `coraçon` [kuɾɐˈsɵ̃w̃], `son` [ˈs̺ɵ̃w̃]. The nasal vowel [õ] of the Convenção is the second candidate. Vasconcelos gives *non* as *nó* (`non` [ˈno]).

A final ⟨-ie⟩ or ⟨-ue⟩ has two syllables: *"Não são ditongos propriamente ditos, mas verdadeiros dissyllabos"* (§11, p. 185). So `tie` is [ˈtɪə], `tue` is [ˈtʊə] and `rue` is [ˈrʊə]. The stress falls on the *i* or *u*, and the vowels before it reduce like any pretonic vowel (p. 200): `fazie` [fɐˈzɪə], `tenie` [tɨˈnɪə]. A written accent keeps its place (`série` [ˈs̺eɾɪə]).

The one-syllable *pie* keeps the diphthong of Latin Ĕ (*pi̊ẹ̌*, §50, p. 219): `pie` [ˈpjɪ]. The Convenção (footnote 19) lists four forms for the same syllable. They are the hiatus [ie] (Duas Igrejas), the diphthong [je] (Malhadas), and the monophthongs [e] (Ifanes) and [i] (Sendim). The spec does not split the ending ⟨-ien⟩ in `mwl`. The words *bien* and the verb ending of *fugien* have the same spelling, and no rule can tell them apart.

A velar nasal [ŋ] stands between a nasal vowel and a vowel, inside a word and across words (§13, p. 192: *ũŋa*, *bĩẹ̌̃ ŋ alto*): `ũa` [ˈũŋɐ], `bien alto` [ˈbjɪ̃ ˈŋaɫtu]. The modern sources limit [ŋ] to a stressed nasal *u* before a vowel: Ferreira et al. (2014, §2) and the Convenção (*"Representação da nasalidade"*). The Convenção also allows a hiatus with no [ŋ]. The spec follows Vasconcelos.

The spec keeps the intervocalic /l/ and /n/ that it inherits from its parent. This retention is the defining Leonese trait that separates the group from Portuguese.

### The ⟨Vnh⟩ trigraphs

The digraphs ⟨an en in on un⟩ are nasal vowels. A greedy tokenizer would therefore read `danho` as ⟨an⟩ plus ⟨ho⟩ and lose the /ɲ/. So the spec lists the trigraphs ⟨anh enh inh onh unh⟩ as an oral vowel plus /ɲ/: `danho` [ˈdaɲu], `canhona` [kɐˈɲonɐ].

## Vowels, nasality and stress

The Portuguese adstrate shows in the reduction of unstressed vowels. Unstressed /a/ gives [ɐ], a pretonic or final /e/ gives [ɨ], and unstressed /o/ gives [u] (`abandono` [ɐβɐ̃nˈdonu]). The nasal-vowel digraphs give /ɐ̃ ẽ ĩ õ ũ/ before a consonant or at a word boundary. Before a vowel they are an oral vowel plus /n/. Before a stop the nasal consonant stays (see [Allophony](#allophony)).

Stress follows the Convenção (§ *Acento*). It falls on the penult by default. The endings `-r -l -z -ç -in -un -on -is -us -ns -ão` attract it to the last syllable, and any written accent overrides both.

The spec writes /u/ as [u] and a final ⟨e⟩ as [ɨ], after the published description of the central variety. Vasconcelos worked from the speech of Duas Igrejas. His letter table (EPM I §24, p. 200) gives unstressed ⟨o⟩ the value of the Portuguese unstressed o. It gives unstressed ⟨u⟩ as *"quasi u port. em tu, rua"*, and unstressed ⟨e⟩ as the Portuguese *"e surdo"*, with *de* as the example. Those values are [u] and [ɨ].

His entry for /u/ (§2) makes it closer than Portuguese (*"parecido com o ou francês"*), not central, in stressed and unstressed syllables alike.

Part of the `mirandese_g2p` gold writes the central [ʉ] instead. It does so for stressed ⟨u ú⟩ (*brúzio* [ˈbɾʉziʉ], *bufanda* [bʉˈfãdɐ]) and for a reduced final ⟨-o⟩ (*bagaroso* [bɐɣɐˈɾoz̺ʉ]). A few rows write a final ⟨e⟩ as [e̞].

This is the narrower notation of one contributor, not a second dialect. Under the same `central` tag, the gold writes [u] more often than [ʉ]. No environment separates them: *búltio* [ˈbʉɫtiʉ] and *adulto* [ɐˈdultu] both have closed syllables. A final ⟨e⟩ is also mostly [ɨ]. The remaining disagreements are a notation artefact, not a spec error, and the spec does not follow them.

The coda /l/ is the velarised [ɫ]. EPM I §13 (p. 188) gives a lateral that *"só existe em fim de syllaba"*. It is the same sound as Portuguese *caldo*, *sol* *"quando por si só constitue uma syllaba, como no artigo l antes de consoante"*: `caldo` [ˈkaɫdu], `sol` [ˈs̺oɫ], `l pai` [ɫ ˈpaj]. Vasconcelos writes the symbol *"só em notação phonetica"* and a plain `l` *"no uso corrente"*. That is a choice of spelling, not a second sound.

The gold writes a coda [l] more often than [ɫ], and the spec follows Vasconcelos. An onset /l/ stays [l], and the article `l` before a vowel stays [l]. The spec does not model the velarisation of the vowel before the lateral (§3, p. 179).

## Allophony

The spec declares cited [allophone rules](../engine/allophony.md) and sandhi rules.

### Nasal before a stop

Vasconcelos keeps the nasal consonant before a stop. He writes that it *"não é mera resonancia nasal"*, and that the words could be written *ã-mbos*, *sã-nto*, *lĩ-ndo*, *põ-ŋgo* (§13, pp. 187-188). So `ambos` is [ˈɐ̃mbus̺], `santo` is [ˈs̺ɐ̃ntu], `pongo` is [ˈpõŋɡu] and `siempre` is [ˈs̺jɪ̃mpɾɨ].

The consonant takes the place of the stop: [m] before ⟨p b⟩, [ŋ] before ⟨k g⟩. A word-final nasal goes into the vowel (`pan` [ˈpɐ̃], `fin` [ˈfĩ]). So does a nasal before a fricative or a liquid, where no source gives a kept consonant.

The `mirandese_g2p` gold writes the nasal vowel without the consonant (*santo* [ˈsɐ̃tu]). No modern source says that the consonant is absent. The Convenção (letters M and N) says that the letter *m* or *n* *"indica a nasalidade da vogal"*, which is a statement about spelling. The gold alone is not a citation, so the consonant stays.

The mid vowels [e o] give the broad mid nasals [ẽ õ]. Vasconcelos (EPM I §6, p. 180) gives nasal e as *"Tão aberto como em berra"* and nasal o as *"Tão aberto como em obra"*. The nasal table (§24, p. 201) gives *"com e entre é e ê"* and *"com o entre ó e ô"*.

### Spirants

The voiced stops /b d ɡ/ are the spirants [β ð ɣ] in the contexts that Vasconcelos lists (§13). In these lists, his letter *ʒ* is the voiced dorsal sibilant written ⟨z⟩.

| Letter | Stop | Spirant | Examples |
|:--|:--|:--|:--|
| ⟨b⟩, and ⟨v⟩, which is ⟨b⟩ | *"no princípio de palavra (depois de pausa ou de nasal)"* and after a nasal | *"entre vogaes, e depois de consoante sonora"* (p. 187) | `haber` [ɐˈβeɾ], `silba` [ˈs̺iɫβɐ], `servir` [s̺ɨɾˈβiɾ], `bibal` [biˈβaɫ] |
| ⟨d⟩ | after a pause, a nasal or *l* | *"intervocalico, e depois de s, ç (ʒ) e r"* (p. 188) | `dedo` [ˈdeðu], `tarde` [ˈtaɾðɨ], `mundo` [ˈmũndu], `caldo` [ˈkaɫdu] |
| ⟨g⟩ | elsewhere | *"intervocalico, e depois de s, l, r"* (p. 192) | `mogadouro` [muɣɐˈðɵwɾu], `algo` [ˈaɫɣu], `lhargo` [ˈʎaɾɣu] |

The spirants also apply across words. An initial ⟨d⟩ is a spirant after a word-final s, ç, r or vowel. An initial ⟨b⟩ is a spirant after s, ç, l, r or a vowel. An initial ⟨g⟩ is a spirant after s, l or r: `ls dedos` [ɫz̺ ˈðeðus̺], `la bida` [lɐ ˈβiðɐ]. For ⟨g⟩ after a vowel the page does not decide, and the stop stays (`la gata` [lɐ ˈɡatɐ]).

The Convenção (letters B and D) agrees with Vasconcelos for ⟨b⟩ and ⟨d⟩. Between vowels, the `mirandese_g2p` gold writes a stop for ⟨d⟩ more often than a spirant. No modern source supports that, so the spirant stays. The spirants are pan-Mirandese: the sub-dialects inherit them through `graphemes_base = mwl`.

## Sub-dialects

The sub-dialect specs inherit the full Central system (`graphemes_base = mwl`) and declare only their deltas.

### Sendinês (mwl-x-sendim)

Sendinês has three documented changes.

1. Monophthongisation: ⟨iê ie⟩ give /i/, and ⟨uô uo⟩ give /u/: `puorta` [ˈpuɾtɐ], `tierra` [ˈtirɐ] (§50, p. 219 and §58, p. 226).
2. The Latin initial L stays [l]. An ⟨lh⟩ at the start of a word is [l] (`lhado` [ˈlaðu], §111, p. 259). A medial ⟨lh⟩ stays [ʎ] (`uolho` [ˈuʎu]). Vasconcelos gives *ulho* (p. 226). The Primeiro Aditamento (2000) lets Sendinese writers spell a word-initial ⟨l-⟩. Secondary sources report that Sendinês loses every ⟨lh⟩ (*alá* for *alhá*). Vasconcelos does not say so, and the spec keeps the medial [ʎ].
3. A final ⟨-ien⟩ has two syllables, with the stress on the *i*: `bien` [ˈbiɨ̃], `quien` [ˈkiɨ̃], `cien` [ˈsiɨ̃] (§50, Obs. 1, p. 220). The final vowel is a reduced nasal. The footnote on p. 220 gives it as ẹ̌̃ or ẽ̥, and §11, Obs. 4 (p. 185) gives ḙ̃ or ẽ̥. The spec uses ẽ̥, written [ɨ̃], the value that both pages give. A proclitic form reduces to ĩ (Obs. 2: *quĩ foi, cĩ pessoas, bĩ feito*): `bien feito` [bĩ ˈfejtu].

Also, a final ⟨-ue⟩ is [u] (`rue` [ˈru], §67, p. 232). A final ⟨-on⟩ is [ɐ̃w̃] (`coraçon` [kuɾɐˈsɐ̃w̃]): the footnote of §110 says *"parece que se diz -ão"*.

### Ifanês (mwl-x-ifanes)

Ifanês is the Northern or Raiano speech of the *raia-sêcca* villages: Paradela, Ifanes, Constantim, Cicouro and S. Martinho de Angueira. In the register of spelling to IPA that the spec models, it is phonologically the same as Central. This is a documented negative result.

Vasconcelos surveys the Raiano villages one by one (EPM II, § "II. Mirandês raiano").

He states that the speech of S. Martinho keeps the Leonese diphthongs (*tierra*, *cielo*) and the mid vowels (*nobe*, *bono*, *posto*, *osso*) exactly as Central does. Of a Padre Nosso specimen, he writes that it *"não offerece differenças phoneticas em relação á do centro"*. The differences from Central are *"morphologicas (em pequeno número) e lexicologicas"*, and Constantim likewise *"não differe, senão no vocabulário"*. In Vol. I (pp. 219-220) he adds that Raiano *tierra* *"concorda com o mirandês normal"*, and he keeps the monophthong /i/ for Sendinês.

So Central and Raiano both keep the diphthongs ⟨ie⟩ and ⟨uo⟩ and the /ʎ/. Only Sendinês differs. The Raiano gold agrees: *fuogo* [ˈfwo.ʊ] keeps the diphthong, against the Sendinês [u]. The Convenção (1999, footnote 13) disagrees: *"Numas localidades, como Ifanes, verifica-se a redução de [je] para [e]"*. The two sources are 98 years apart, and the spec follows Vasconcelos.

The attested Raiano traits are lexical and morphosyntactic, not segmental. They include local adverb and pronoun forms at Ifanes (*pa-lhina*, *aquina*, *quina* for Central *alhi*, *eiqui*, and *calhe* "street"). They also include the demonstratives *esto*, *aquesto* and the words *tolho*, *lureiro*, *frol* at S. Martinho, and the border connective *antonces*. None of them changes a mapping from grapheme to phoneme. So the spec inherits the full Central system and declares no deltas: `fuogo` is [ˈfʊɣu] in `mwl-x-ifanes`, as in `mwl`.

## Input contract

Input is Mirandese text in the official orthography (Convenção 1999). Give the spec ⟨lh⟩, ⟨nh⟩, ⟨iê uô⟩ and ⟨ç⟩ as spelled. The spec respects the stress accent (´) and the nasal tilde (˜).

## Measuring against the gold

The `TigreGotico/mirandese_g2p` gold is `expert-human` and small, and its rows for the sub-dialects are very small. Read the confidence interval on [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md) before you read the PER of a sub-dialect.

The gold writes the nasal vowel without the nasal consonant. It writes [wo] and [je], [ɛ ɔ] in unmarked words, and [d] between vowels. Where it disagrees with Vasconcelos, `mwl` follows Vasconcelos, so its PER is higher than it would be with the modern readings. Some residual error also comes from notation choices of the gold that the rules cannot and should not follow. These are the central final vowel [ʉ] for an unstressed final ⟨-o⟩, and the plain coda [l].

## Sources

- Ferreira, M. B. & Raposo, D. (coords.) (1999). *Convenção Ortográfica da Língua Mirandesa.* Câmara Municipal de Miranda do Douro / Centro de Linguística da Universidade de Lisboa. The official orthography (§ L, § Sibilantes, § Ditongos, § Nasalidade, § Acento).
- Ferreira, M. B. & Raposo, D. (coords.) (2000). *Primeiro Aditamento à Convenção Ortográfica da Língua Mirandesa.* The provisions for Sendinês.
- Vasconcelos, J. Leite de (1900). *Estudos de Philologia Mirandesa* (Vol. I). Imprensa Nacional, Lisboa. The foundational description of the sibilant system and the sub-dialect division (pp. 172-173), from the speech of Duas Igrejas. §2 (pp. 173-179) describes each vowel, and §13 (pp. 187 ff.) each consonant, with the velarised lateral of the coda. §24 (p. 200) tabulates the value of every letter by syllable type, the locator for unstressed ⟨o u⟩ [u] and unstressed ⟨e⟩ [ɨ]. §113 (p. 265) covers a word-final `-l` from Latin `-L`. Raiano *tierra* agrees with the central norm (pp. 219-220).
- Vasconcelos, J. Leite de (1901). *Estudos de Philologia Mirandesa* (Vol. II). Imprensa Nacional, Lisboa. § "II. Mirandês raiano" (pp. 28-31): the Raiano villages have no phonetic differences from Central, only morphological and lexical ones.
- Ferreira, J. P., Chesi, C., Cho, H., Baldewijns, D., Braga, D. & Dias, M. (2014). *On Mirandese Language Resources for Text-To-Speech.* SLTU-2014, pp. 87-92. The Mirandese TTS phone set of 43 phones (§3.4), with the diphthongs *je*, *jen*, *wo*, *won*.
- Mateus, M. H. M. & d'Andrade, E. (2000). *The Phonology of Portuguese.* Oxford University Press. The reference for the shared Ibero-Romance processes (nasal place assimilation, spirantisation) and the adstrate reduction.
- Ferreira, M. B. (1995). *Variação linguística: perspectiva dialectológica*. Listed in the spec sources.
- Cunha, C. & Cintra, L. F. L. (1984). *Nova Gramática do Português Contemporâneo*. Listed in the spec sources.

---
[← Barranquenho](ext-PT-x-barrancos.md) · [Home](../index.md) · [Russian →](ru.md)
