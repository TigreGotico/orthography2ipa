# Mirandese (`mwl`) and its sub-dialects

Mirandese (*mirandés*, *lhéngua mirandesa*) is an **Asturleonese** language
spoken in the Miranda do Douro municipality of north-eastern Portugal, and
recognised as a co-official regional language of Portugal since 1999. It is
**not** a dialect of Portuguese: its parent in this library is
`ast-PT-x-medieval` (Medieval Asturian-Leonese of Portugal), and its features
are West Iberian / Leonese, not imported Portuguese allophony. Modern
Mirandese does, however, carry a heavy Portuguese **adstrate** (schooling,
administration), visible chiefly in unstressed-vowel reduction.

Codes covered here:

| Code | Name | Sub-dialect | Tier |
|:--|:--|:--|:--|
| `mwl` | Mirandese (Central) | Central / normal | research |
| `mwl-x-sendim` | Sendinês | Southern (Vila de Sendim) | research |
| `mwl-x-ifanes` | Ifanês | Northern / Raiano (border) | research |

The three sub-dialects are the classical division (Vasconcelos 1900): the
**Central** norm on which the orthography is built, the **Northern/Raiano**
speech of the plateau border, and the **Southern Sendinês** of Vila de Sendim.

`mwl` follows Leite de Vasconcellos (*Estudos de Philologia Mirandesa* I, 1900),
the first phonetic description of the language. Where later sources disagree
with him, the `notes` of the spec quote both sides with their pages, and the
later reading stays in the lattice as a lower-ranked candidate.

## The sibilant system: the hallmark

Mirandese preserves the medieval Ibero-Romance sibilant richness that
standard Portuguese and Spanish collapsed. The library models a **four-way+
contrast**:

| Orthography | Phoneme | Description |
|:--|:--|:--|
| ⟨s⟩, ⟨ss⟩ | /s̺/ | voiceless **apico-alveolar** fricative |
| ⟨s⟩ between vowels or before a voiced consonant | /z̺/ | voiced apico-alveolar |
| ⟨c⟩ (before e/i), ⟨ç⟩ | /s/ | voiceless **dorso-dental** fricative |
| ⟨z⟩, word-final ⟨ç⟩ before a voiced consonant | /z/ | voiced dorso-dental |
| ⟨x⟩ | /ʃ/ | voiceless postalveolar |
| ⟨j⟩, ⟨g⟩ (before e/i) | /ʒ/ | voiced postalveolar |
| ⟨ch⟩ | /t͡ʃ/ | voiceless postalveolar **affricate** (still an affricate, unlike modern European Portuguese, which deaffricated it to /ʃ/) |

**Notation convention.** The key phonemic opposition is *apical*
(⟨s⟩) versus *dorso-dental* (⟨c, ç, z⟩). The library writes only the apical
series with the IPA retracted diacritic (`s̺`, `z̺`) and leaves the
dorso-dental series **plain** (`s`, `z`). This is IPA-standard, keeps the
contrast fully explicit, and matches the convention of the expert
`TigreGotico/mirandese_g2p` gold (which never uses the over-narrow laminal
`◌̻` diacritic). ⟨ç⟩ is a fricative, not the Asturian affricate /t͡s/, and it
occurs word-finally (`rapaç`, `lhuç`) where Portuguese would spell `-z`.

**Voicing.** The apical ⟨s⟩ is voiced to [z̺] before a voiced consonant, inside
a word and across words: `asno` → [ˈaz̺nu], `mesmo` → [ˈmez̺mu], `ls nius` →
[ɫz̺ ˈnjus̺]. Word-final ⟨ç⟩ is [z] before a voiced consonant in the next word:
`lhuç del cielo` → [ˈʎuz ðɨɫ ˈsjɪlu]. Before a voiceless consonant, a vowel or
a pause both stay voiceless. Vasconcelos (EPM v1 §13, p. 190) gives the voiced
apical "final de palavra antes de consoante sonora" and the voiced dorsal
"em fim de palavra só póde ouvir-se quando a palavra seguinte começa por
consoante sonora".

⟨j⟩ is always /ʒ/ (West Iberian), never the Asturian palatal. The letter ⟨y⟩ is
the Spanish palatal [ʝ] (`you` → [ˈʝɵw]): Vasconcellos (p. 191) writes "Como o
*y* castelhano normal em *yo*" and gives it as "Inicial ou medial", so a
word-final ⟨y⟩ is the glide [j] (`rey` → [ˈrej]). The Convenção (letter Y)
gives the glide [j], which is the second candidate here.

## Leonese features

- **Initial ⟨l⟩ is [l].** A written initial ⟨l⟩ is plain /l/ (`lindo` → [ˈlĩndu],
  `litro` → [ˈlitɾu]): Vasconcelos (EPM v1 §13, p. 188) gives `lĩ-ndo` with [l]
  and describes l as "Como em português na palavra *lapa*". The Latin initial
  L that became [ʎ] is written ⟨lh⟩ (§111, p. 259).
- **⟨v⟩ is ⟨b⟩.** "Na pronúncia normal mirandesa não existe differença entre b
  e v" (§14, p. 193): `vaca` → [ˈbakɐ], `uva` → [ˈuβɐ], `envidar` → [ɨ̃mbiˈðaɾ].
- **⟨ê⟩ is [e]** (Convenção, letter table E): `yê` → [ˈʝe], `yêrba` → [ˈʝeɾβɐ].
- **⟨lh⟩ = /ʎ/, ⟨nh⟩ = /ɲ/** in all positions.
- **Leonese diphthongs.** Latin short Ĕ → ⟨iê/ie⟩ = [jɪ], Latin short Ŏ →
  ⟨uô/uo⟩ = [ʊ] (`tierra` → [ˈtjɪrɐ], `puorta` → [ˈpʊɾtɐ]). Vasconcellos
  writes the nuclei ẹ̌ and ọ̌ (§2, pp. 173 and 177): ẹ̌ lies between the *i* of
  Portuguese *viu* and the *ê* of *cêrca*, close to the *i* of English *fill*,
  and ọ̌ is "muito semelhante ao *u* do inglês *full*, *butcher*". The
  diphthong [wo] "não é normal na falla mirandesa; só se ouve em emphase ou voz
  pausada" (p. 182, Obs. 2). The Convenção writes the diphthongs [je] and
  [wo] (footnote 13), and the same footnote says that in Duas Igrejas and
  Constantim "[wo] é esporádico", which agrees with Vasconcellos. In `mwl`
  [je] and [wo] are the second candidates, which keeps them in the beam for a
  downstream rescorer. Vasconcellos's ọ̌ occurs only in a stressed syllable
  (p. 177), so a final unstressed ⟨-uo⟩ is two vowels: `mútuo` → [ˈmutuu].
- **⟨é⟩ and ⟨ó⟩ are [e] and [o].** The Portuguese open vowels "não existem na
  pronúncia normal mirandesa" (§22, p. 198): `pé` → [ˈpe], `pós` → [ˈpos̺],
  `chapéu` → [tʃɐˈpew]. The Convenção reads the acute accent as a "qualidade
  relativamente aberta" ([ɛ], [ɔ]); that is the second candidate of ⟨é⟩ and
  ⟨ó⟩. Plain ⟨e⟩ and ⟨o⟩ have no open
  candidate.
- **⟨ou⟩ is [ɵw].** The base vowel *ö* of the diphthong *öu* is the *o* of
  English *go*, *no* (§2, p. 174): `touro` → [ˈtɵwɾu].
- **Final ⟨-on⟩ is [ɵ̃w̃].** Latin -ONE gives *-öũ* (§110, p. 257: *perdigöũ*):
  `coraçon` → [kuɾɐˈsɵ̃w̃], `son` → [ˈs̺ɵ̃w̃]. The nasal vowel [õ] of the Convenção
  is the second candidate. Vasconcellos gives `non` as *nó* (`non` → [ˈno]).
- **Final ⟨-ie⟩ and ⟨-ue⟩ have two syllables.** "Não são ditongos propriamente
  ditos, mas verdadeiros dissyllabos" (§11, p. 185): `tie` → [ˈtɪə], `tue` →
  [ˈtʊə], `rue` → [ˈrʊə]. The stress is on the *i* or *u*, and the vowels before
  it reduce like any pretonic vowel (p. 200): `fazie` → [fɐˈzɪə], `tenie` →
  [tɨˈnɪə]. A written accent keeps its place (`série` → [ˈs̺eɾɪə]). The
  one-syllable `pie` keeps the diphthong of Latin Ĕ (*pi̊ẹ̌*, §50, p. 219):
  `pie` → [ˈpjɪ]. The Convenção (footnote 19) lists the hiatus [ie] (Duas
  Igrejas) beside the diphthong [je] (Malhadas) and the monophthongs [e]
  (Ifanes) and [i] (Sendim) for the same syllable. The ending ⟨-ien⟩ is not split in `mwl`:
  *bien* and the verb ending *fugien* have the same spelling, and no rule can
  tell them apart.
- **A velar nasal [ŋ] stands between a nasal vowel and a vowel**, inside a word
  and across words (§13, p. 192: *ũŋa*, *bĩẹ̌̃ ŋ alto*): `ũa` → [ˈũŋɐ],
  `bien alto` → [ˈbjɪ̃ ˈŋaɫtu]. The modern sources limit [ŋ] to a stressed nasal
  *u* before a vowel: Ferreira et al. (2014, §2) and the Convenção
  ("Representação da nasalidade"), which also allows a hiatus with no [ŋ]. The
  spec follows Vasconcellos.
- **Intervocalic /l/ and /n/ preserved** (inherited from the parent), the
  defining Leonese retention that distinguishes the group from Portuguese.

### The ⟨Vnh⟩ trigraphs

Because ⟨an, en, in, on, un⟩ are nasal-vowel digraphs, a naive greedy
tokenizer would parse `danho` as `an` + `ho` and lose the /ɲ/. The spec
therefore lists the trigraphs ⟨anh, enh, inh, onh, unh⟩ explicitly (oral
vowel + /ɲ/), so `danho` → [ˈdaɲu] and `canhona` → [kaˈɲonɐ].

## Vowels, nasality and stress

The Portuguese adstrate shows up as **unstressed-vowel reduction**:
unstressed /a/ → [ɐ], pretonic/final /e/ → [ɨ], unstressed /o/ → [u]
(`abandono` → [ɐβɐ̃nˈdonu]). Nasal-vowel digraphs realise /ɐ̃ ẽ ĩ õ ũ/ before
a consonant or at a word boundary. Before a vowel they are oral vowel + /n/.
Before a stop the nasal consonant stays (see Allophony).
Stress follows the Convenção § Acento: paroxytone by default, with the
oxytone-attracting endings `-r -l -z -ç -in -un -on -is -us -ns -ão` and any
written accent overriding.

The spec transcribes /u/ as **[u]** and final ⟨e⟩ as **[ɨ]**, on the published
description of the central variety. Vasconcelos worked from the speech of
Duas-Igrejas, and his letter table (EPM v1 §24, p. 200) gives unstressed ⟨o⟩ the
value of the Portuguese unstressed o, unstressed ⟨u⟩ as "quasi u port. em *tu*,
*rua*", and unstressed ⟨e⟩ as the Portuguese "e surdo" with *de* as the example —
that is, [u] and [ɨ]. His entry for /u/ (§2) puts it *closer* than Portuguese
("parecido com o *ou* francês"), not centralised, and stressed and unstressed
alike.

Part of the `mirandese_g2p` gold instead writes the centralised **[ʉ]**, for
*both* stressed ⟨u/ú⟩ (`brúzio` → [ˈbɾʉziʉ], `bufanda` → [bʉˈfãdɐ]) and reduced
final ⟨-o⟩ (`bagaroso` → [bɐɣɐˈɾoz̺ʉ]), and a few rows write final ⟨e⟩ as [e̞].
That is one contributor's narrower notation, not a second dialect: under the
same `central` tag the gold carries 65 [u] against 36 [ʉ] with no environment
separating them (`búltio` [ˈbʉɫtiʉ] and `adulto` [ɐˈdultu] are both closed
syllables), and final ⟨e⟩ splits 20 [ɨ] against 3 [e̞]. The residual
disagreements are a **notation artifact**, not a spec error, and are not chased.

**Coda /l/** is velarised [ɫ]. EPM v1 §13 (p. 188) gives a lateral that "só
existe em fim de syllaba" and, "quando por si só constitue uma syllaba, como no
artigo l antes de consoante", the same sound as Portuguese *caldo*, *sol*: `caldo`
→ [ˈkaɫdu], `sol` → [ˈs̺oɫ], `l pai` → [ɫ ˈpaj]. LdV writes the symbol "só em
notação phonetica" and plain `l` "no uso corrente", which is a choice of spelling
and not a second sound. The gold writes coda [l] 14 times against [ɫ] 6; the spec
follows LdV. Onset /l/ stays [l]. The article `l` before a vowel stays [l]. The
velarisation of the preceding vowel (§3, p. 179) is not modelled.

## Allophony (post-lexical)

The spec declares cited [allophone rules](../allophony.md) and sandhi rules.

**Nasal + stop.** Vasconcellos keeps the nasal consonant before a stop: "não é
mera resonancia nasal" and the words could be written *ã-mbos*, *sã-nto*,
*lĩ-ndo*, *põ-ŋgo* (§13, pp. 187-188). So `ambos` → [ˈɐ̃mbus̺], `santo` →
[ˈs̺ɐ̃ntu], `pongo` → [ˈpõŋɡu], `siempre` → [ˈs̺jɪ̃mpɾɨ]. The consonant takes the
place of the stop: [m] before ⟨p b⟩, [ŋ] before ⟨k g⟩. A word-final nasal is
absorbed into the vowel (`pan` → [ˈpɐ̃], `fin` → [ˈfĩ]), and so is a nasal
before a fricative or a liquid, where no source gives a kept consonant. The
`mirandese_g2p` gold writes the nasal vowel without the consonant (`santo` →
[ˈsɐ̃tu]). No modern source says that the consonant is absent. The Convenção
(letters M and N) says that the letter *m* or *n* "indica a nasalidade da
vogal", which is a statement about spelling. The gold alone is not a
citation, so the consonant stays.

The mid vowels [e o] give the broad mid nasals [ẽ õ]: Vasconcellos (EPM v1 §6,
p. 180) gives nasal e as "Tão aberto como em *berra*" and nasal o as "Tão aberto
como em *obra*", and the nasal table (§24, p. 201) gives "com e entre é e ê" and
"com o entre ó e ô".

**Spirants.** The voiced stops /b d ɡ/ are spirants [β ð ɣ] in the contexts that
Vasconcellos lists (§13). ⟨b⟩ (and ⟨v⟩, which is ⟨b⟩) is a stop "no princípio de
palavra (depois de pausa ou de nasal)" and after a nasal, and a spirant "entre
vogaes, e depois de consoante sonora" (p. 187): `haber` → [ɐˈβeɾ], `silba` →
[ˈs̺iɫβɐ], `servir` → [s̺ɨɾˈβiɾ], `bibal` → [biˈβaɫ]. ⟨d⟩ is a spirant "intervocalico,
e depois de s, ç (ʒ) e r" and a stop after a pause, a nasal or *l* (p. 188):
`dedo` → [ˈdeðu], `tarde` → [ˈtaɾðɨ], `mundo` → [ˈmũndu], `caldo` → [ˈkaɫdu].
⟨g⟩ is a spirant "intervocalico, e depois de s, l, r" (p. 192): `mogadouro` →
[muɣɐˈðɵwɾu], `algo` → [ˈaɫɣu], `lhargo` → [ˈʎaɾɣu]. (Vasconcellos's *ʒ* is
his letter for the voiced dorsal sibilant written ⟨z⟩.) Across words, an
initial ⟨d⟩ after a word-final s, ç, r or vowel, an initial ⟨b⟩ after s, ç, l,
r or vowel and an initial ⟨g⟩ after s, l or r are spirants too (`ls dedos` →
[ɫz̺ ˈðeðus̺], `la bida` → [lɐ ˈβiðɐ]). For ⟨g⟩ after a vowel the page does not
decide, and the stop stays (`la gata` → [lɐ ˈɡatɐ]). The
Convenção (letters B and D) agrees with Vasconcellos for ⟨b⟩ and ⟨d⟩. The
`mirandese_g2p` gold writes a stop between vowels more often than a spirant for
⟨d⟩ (25 stops against 7 spirants in a plain count of its 205 words). No modern
source supports that, so the spirant stays.

The spirants are **pan-Mirandese**: the sub-dialects inherit them through
`graphemes_base = mwl`.

## Sub-dialects

Sub-dialect specs inherit the full Central system (`graphemes_base = mwl`) and
declare only their **deltas**:

- **Sendinês (`mwl-x-sendim`)**: three documented changes:
  1. **Monophthongisation**: ⟨iê/ie⟩ → /i/, ⟨uô/uo⟩ → /u/ (`puorta` →
     [ˈpuɾtɐ]; §50, p. 219 and §58, p. 226).
  2. **The Latin initial L stays [l]**: ⟨lh⟩ at the start of a word is [l]
     (`lhado` → [ˈlaðu]; §111, p. 259). A medial ⟨lh⟩ stays [ʎ]
     (`uolho` → [ˈuʎu]; Vasconcellos gives *ulho*, p. 226). The Primeiro
     Aditamento (2000) permits Sendinese writers to spell word-initial ⟨l-⟩.
     Secondary sources report that Sendinês loses every ⟨lh⟩ (`alá` for `alhá`);
     Vasconcellos does not say so, and the spec keeps the medial [ʎ].
  3. **Final ⟨-ien⟩ has two syllables** with the stress on the *i*: `bien` →
     [ˈbiɨ̃], `quien` → [ˈkiɨ̃], `cien` → [ˈsiɨ̃] (§50, Obs. 1, p. 220). The
     final vowel is a reduced nasal: the footnote on p. 220 gives it as
     ẹ̌̃ or ẽ̥, and §11, Obs. 4 (p. 185) as ḙ̃ or ẽ̥; the spec uses ẽ̥ [ɨ̃], the
     value both pages give. A proclitic form reduces to ĩ (Obs. 2: *quĩ foi,
     cĩ pessoas, bĩ feito*): `bien feito` → [bĩ ˈfejtu]. Final ⟨-ue⟩ is [u]
     (`rue` → [ˈru], §67, p. 232), and
     final ⟨-on⟩ is [ɐ̃w̃] (`coraçon` → [kuɾɐˈsɐ̃w̃]; the footnote of §110 says
     "parece que se diz -ão").
- **Ifanês (`mwl-x-ifanes`)**: the Northern/Raiano speech of the raia-sêcca
  villages (Paradela, Ifanes, Constantim, Cicouro, S. Martinho de Angueira).
  It is **phonologically identical to Central** in the modeled grapheme→IPA
  register, a documented **negative result**, not an untested assumption.
  Vasconcelos surveys the Raiano villages one by one (EPM Vol. II, § "II.
  Mirandês raiano") and states plainly that the speech of S. Martinho keeps the
  Leonese diphthongs (`tierra`, `cielo`) and mid outcomes (`nobe`, `bono`,
  `posto`, `osso`) exactly as Central, and, transcribing a Padre Nosso
  specimen, that it *"não offerece differenças phoneticas em relação á do
  centro"*. The differences from Central are *"morphologicas (em pequeno
  número) e lexicologicas"* (Constantim likewise *"não differe, senão no
  vocabulário"*). In Vol. I (pp.219-220) he adds that raiano `tierra` *"concorda
  com o mirandês normal"*, reserving the monophthong /i/ for Sendinês. Both
  Central and Raiano keep the diphthongs ⟨ie⟩ and ⟨uo⟩ and /ʎ/. Only Sendinês
  diverges. The Raiano gold corroborates it (`fuogo` → [ˈfwo.ʊ], diphthong
  retained. Contrast the Sendinês [u]). The Convenção (1999, footnote 13)
  disagrees: "Numas localidades, como Ifanes, verifica-se a redução de [je] para
  [e]". The two sources are 98 years apart. The spec follows Vasconcellos. The attested Raiano distinctives are
  lexical and morphosyntactic, not segmental: local adverb/pronoun forms at
  Ifanes (`pa-lhina`, `aquina`, `quina` for Central `alhi`/`eiqui`; `calhe`
  "street"), the demonstratives `esto`/`aquesto` and lexemes `tolho`,
  `lureiro`, `frol` at S. Martinho, and the raia connective `antonces`, none of
  which change a grapheme→phoneme mapping. The spec therefore inherits the full
  Central system unchanged and declares no deltas.

## Input contract

Input is Mirandese text in the **official orthography** (Convenção 1999).
Feed written ⟨lh⟩, ⟨nh⟩, ⟨iê/uô⟩, ⟨ç⟩ as spelled. The accents that mark stress
(´) and the nasal tilde (˜) are respected.

## Benchmarks

Measured against `TigreGotico/mirandese_g2p` (expert-human, small-`n`):

| Code | n | PER |
|:--|--:|--:|
| `mwl` | 205 | 0.2303 |
| `mwl-x-sendim` | 11 | 0.4470 (wide CI, do not over-read) |
| `mwl-x-ifanes` | 2 | 0.6250 (n = 2, do not read) |

The gold writes the nasal vowel without the nasal consonant, [wo] and [je], [ɛ ɔ]
in unmarked words, and [d] between vowels. Where it disagrees with
Vasconcellos, `mwl` follows Vasconcellos, so its PER is higher than it
would be with the modern readings. Residual error is also due to gold-notation
choices the rules cannot and should not chase: the transcriber's centralised
final vowel [ʉ] for unstressed final ⟨-o⟩ (see above), and the plain coda [l].

## Sources

- **Ferreira, M. B. & Raposo, D. (coords.) (1999).** *Convenção Ortográfica
  da Língua Mirandesa.* Câmara Municipal de Miranda do Douro / Centro de
  Linguística da Universidade de Lisboa., the official orthography (§ L,
  § Sibilantes, § Ditongos, § Nasalidade, § Acento).
- **Ferreira, M. B. & Raposo, D. (coords.) (2000).** *Primeiro Aditamento à
  Convenção Ortográfica da Língua Mirandesa.*, Sendinês provisions.
- **Vasconcelos, J. Leite de (1900).** *Estudos de Philologia Mirandesa
  (Vol. I).* Imprensa Nacional, Lisboa., foundational description of the
  sibilant system and the sub-dialect division (pp.172-173), based on the
  speech of Duas-Igrejas. §2 (pp.173-179) describes each vowel, §13
  (pp.187 ff.) each consonant including the coda-only velarised lateral, and
  §24 (p.200) tabulates the phonetic value of every letter by syllable type —
  the locator for unstressed ⟨o u⟩ = [u] and unstressed ⟨e⟩ = [ɨ]. §113
  (p.265) covers word-final `-l` from Latin `-L`. Raiano `tierra` agrees with
  the central norm (pp.219-220).
- **Vasconcelos, J. Leite de (1901).** *Estudos de Philologia Mirandesa
  (Vol. II).* Imprensa Nacional, Lisboa., § "II. Mirandês raiano" (pp.28-31):
  the Raiano villages offer no phonetic differences from Central. Their
  divergences are morphological and lexical.
- **Ferreira, J. P., Chesi, C., Cho, H., Baldewijns, D., Braga, D. & Dias,
  M. (2014).** *On Mirandese Language Resources for Text-To-Speech.* SLTU-2014,
  pp. 87-92., the 43-phone Mirandese TTS phone set (§3.4) with the diphthongs
  *je*, *jen*, *wo*, *won*.
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press., reference for the shared Ibero-Romance processes
  (nasal place assimilation, spirantisation) and the adstrate reduction.

---
[← Madeiran European Portuguese](pt-PT-x-madeira.md) · [Home](../index.md) · [Slavic Languages →](slavic.md)
