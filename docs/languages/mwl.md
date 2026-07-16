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

## The sibilant system — the hallmark

Mirandese preserves the medieval Ibero-Romance sibilant richness that
standard Portuguese and Spanish collapsed. The library models a **four-way+
contrast**:

| Orthography | Phoneme | Description |
|:--|:--|:--|
| ⟨s⟩, ⟨ss⟩ | /s̺/ | voiceless **apico-alveolar** fricative |
| intervocalic ⟨-s-⟩ | /z̺/ | voiced apico-alveolar |
| ⟨c⟩ (before e/i), ⟨ç⟩ | /s/ | voiceless **dorso-dental** fricative |
| ⟨z⟩ | /z/ | voiced dorso-dental |
| ⟨x⟩ | /ʃ/ | voiceless postalveolar |
| ⟨j⟩, ⟨g⟩ (before e/i) | /ʒ/ | voiced postalveolar |
| ⟨ch⟩ | /t͡ʃ/ | voiceless postalveolar **affricate** (still an affricate, unlike modern European Portuguese, which deaffricated it to /ʃ/) |

**Notation convention.** The crucial phonemic opposition is *apical*
(⟨s⟩) versus *dorso-dental* (⟨c, ç, z⟩). The library writes only the apical
series with the IPA retracted diacritic (`s̺`, `z̺`) and leaves the
dorso-dental series **plain** (`s`, `z`). This is IPA-standard, keeps the
contrast fully explicit, and matches the convention of the expert
`TigreGotico/mirandese_g2p` gold (which never uses the over-narrow laminal
`◌̻` diacritic). ⟨ç⟩ is a fricative, not the Asturian affricate /t͡s/, and it
occurs word-finally (`rapaç`, `lhuç`) where Portuguese would spell `-z`.

⟨j⟩ is always /ʒ/ (West Iberian) — never the Asturian palatal /ʝ/. The letter
⟨y⟩, by contrast, is the glide /j/ (`ye` → [je]).

## Leonese features

- **Initial-l palatalisation.** Word-initial ⟨l⟩ before a vowel is /ʎ/
  (`luç` → [ˈʎus]), per Convenção § L. Bare /l/ survives word-initially only
  in loanwords, proper nouns and the article — a documented residual limit,
  not modelled positionally.
- **⟨lh⟩ = /ʎ/, ⟨nh⟩ = /ɲ/** in all positions.
- **Leonese diphthongs.** Latin short Ĕ → ⟨iê/ie⟩ = [je],
  Latin short Ŏ → ⟨uô/uo⟩ = [wo] (`tierra` → [ˈtjerɐ], `puorta` →
  [ˈpwoɾtɐ]). Mirandese has a single intermediate mid /e o/ quality
  ("menos abertos que os nossos"; the ⟨ie⟩ nucleus lies between [i] and [e]
  — Vasconcelos, *Estudos de Philologia Mirandesa* v1 §§2,4,10, pp.178-183),
  so the diphthongs are **close**; open [jɛ]/[wɔ] are non-contrastive
  allophonic variants. This matches the human gold majority
  (`rabielho` → [rɐˈβjeʎu], `squierdo` → [ˈs̺kjeɾdu]).
- **Intervocalic /l/ and /n/ preserved** (inherited from the parent) — the
  defining Leonese retention that distinguishes the group from Portuguese.

### The ⟨Vnh⟩ trigraphs

Because ⟨an, en, in, on, un⟩ are nasal-vowel digraphs, a naive greedy
tokenizer would parse `danho` as `an` + `ho` and lose the /ɲ/. The spec
therefore lists the trigraphs ⟨anh, enh, inh, onh, unh⟩ explicitly (oral
vowel + /ɲ/), so `danho` → [ˈdaɲu] and `canhona` → [kaˈɲonɐ].

## Vowels, nasality and stress

The Portuguese adstrate shows up as **unstressed-vowel reduction**:
unstressed /a/ → [ɐ], pretonic/final /e/ → [ɨ], unstressed /o/ → [u]
(`abandono` → [ɐbɐ̃ˈdonu]). Nasal-vowel digraphs realise /ɐ̃ ẽ ĩ õ ũ/ before
a consonant or at a word boundary; before a vowel they are oral vowel + /n/.
Stress follows the Convenção § Acento: paroxytone by default, with the
oxytone-attracting endings `-r -l -z -ç -in -un -on -is -us -ns -ão` and any
written accent overriding.

The spec transcribes /u/ as **[u]**. The `mirandese_g2p` gold instead writes it
narrowly as the centralised **[ʉ]** — and does so for *both* stressed ⟨u/ú⟩
(`brúzio` → [ˈbɾʉziʉ], `bufanda` → [bʉˈfãdɐ]) and reduced final ⟨-o⟩
(`bagaroso` → [bɐɣɐˈɾoz̺ʉ]). Because [ʉ] there is the transcriber's realisation
symbol for /u/ generally, not a distinct vowel in complementary distribution,
the [ʉ]↔[u] disagreements are a **notation artifact**, not a spec error: the
spec is deliberately left with the broad [u] and the mismatch is not chased.

## Allophony (post-lexical)

The spec declares cited [allophone rules](../allophony.md). First, coda /n/
assimilates in place to a following **labial** ([m]) or **velar** ([ŋ]) stop
(Mateus & d'Andrade 2000:11).

Second, **intervocalic /b/ spirantisation** (⟨b⟩ → [β] between vowels):
`haber` → [ɐˈβeɾ], `rabudo` → [rɐˈβudu], `nuobo` → [ˈnwoβu]. This is the
general Ibero-Romance lenition of voiced stops — /b d ɡ/ surface as the
fricatives/approximants [β ð ɣ] everywhere **except** after a pause or a nasal
(Mateus & d'Andrade 2000:11; Ferreira & Raposo 1999; the [Mirandese Wikipedia
phonology](https://en.wikipedia.org/wiki/Mirandese_language#Consonants):
"voiced stops /b d ɡ/ may be lenited as fricatives [β ð ɣ]"), which is why the
rule requires a preceding vowel (word-initial ⟨b⟩ keeps the stop:
`bibal` → [biˈβal]).

**Pre-consonantal nasalisation.** A nasal digraph ⟨an en in on un⟩ (⟨am…⟩)
before *any* stop — voiceless or voiced ⟨mb nd ng nt…⟩ — nasalises the vowel
and the nasal is absorbed, the following stop retained: `brando` → [ˈbɾɐ̃du],
`quando` → [ˈkwɐ̃du], `bufanda` → [buˈfɐ̃dɐ], `lhéngua` → [ˈʎẽɡwɐ],
`ambos` → [ˈɐ̃bus̺], `sendo` → [ˈs̺ẽdu]. Stressed open [ɛ ɔ] raise to
close-mid nasal [ẽ õ]. This is the inherited Ibero-Romance nasal-vowel +
absorption behaviour and matches the human gold on every nasal+stop word;
the earlier oral ⟨mb nd ng⟩ digraph treatment was contradicted by the gold
and removed.

The rule is applied **per phoneme**, on the evidence of the expert-human
`mirandese_g2p` gold measured at true oral-intervocalic positions (post-nasal
excluded):

- **/b/ → [β]**: spirant-dominant (β:9 / b:5), so it is rewritten. It is a net
  win on the human gold (PER 0.1901 → 0.1851); the residual over-spirantised
  loans (`brabo`, `alternatibo`) are the lexical variability the downstream
  `mwl_phonemizer` can condition on.
- **/ɡ/ → [ɣ]**: already spirantised intervocalically at the
  `positional_graphemes` layer (`mogadouro` → [muɣɐˈdowɾu]), so it needs **no**
  allophone rule; adding one only misfires after a diphthong glide (`eigual` →
  gold stop [ɐjˈɡwal]).
- **/d/**: intervocalic /d/ is **stop-dominant** in the gold (d:13 / ð:7) — the
  documented Asturleonese conservatism/occlusion of /d/, and why the Wikipedia
  wording is hedged ("may be"). It keeps its positional default [d] (`nada` →
  [ˈnadɐ]); [ð] stays only an `allophones` inventory / lattice candidate,
  realisable by the downstream `mwl_phonemizer` where lexical conditioning is
  available.

Spirantisation is **pan-Mirandese**: the sub-dialects inherit the /b/ rule via
`graphemes_base = mwl` (`haber` → [ɐˈβeɾ] in Sendinês and Ifanês too).

## Sub-dialects

Sub-dialect specs inherit the full Central system (`graphemes_base = mwl`) and
declare only their **deltas**:

- **Sendinês (`mwl-x-sendim`)** — two documented changes:
  1. **Monophthongisation**: ⟨iê/ie⟩ → /i/, ⟨uô/uo⟩ → /u/ (`puorta` →
     [ˈpuɾtɐ]).
  2. **Depalatalisation**: /ʎ/ → /l/ — words other dialects say with ⟨lh⟩ are
     said with /l/ (`lhado` → [ˈladu], `alhá` → [ɐˈla]); word-initial ⟨l⟩ is
     likewise plain /l/. The Primeiro Aditamento (2000) permits Sendinese
     writers to spell word-initial ⟨l-⟩.
- **Ifanês (`mwl-x-ifanes`)** — the Northern/Raiano speech of Ifanes. The
  published descriptions record **no** segmental orthography→phoneme
  divergence from Central: both keep the diphthongs [je]/[wo] and /ʎ/ (only
  Sendinês diverges), corroborated by the Raiano gold (`fuogo` → [ˈfwo.ʊ],
  diphthong retained). Its distinctives are morphosyntactic/lexical (article
  forms, some nasalisation) and out of scope for a grapheme→IPA spec, so it
  inherits Central unchanged; the ⟨iê⟩ diphthong is preserved rather than
  monophthongised to [e], for which no source records a divergence.

## Input contract

Input is Mirandese text in the **official orthography** (Convenção 1999).
Feed written ⟨lh⟩, ⟨nh⟩, ⟨iê/uô⟩, ⟨ç⟩ as spelled; the accents that mark stress
(´) and the nasal tilde (˜) are respected.

## Benchmarks

Measured against `TigreGotico/mirandese_g2p` (expert-human, small-`n`):

| Code | n | PER |
|:--|--:|--:|
| `mwl` | 205 | 0.1851 (was 0.1901 before /b/ spirantisation) |
| `mwl-x-sendim` | 11 | 0.3914 (wide CI — do not over-read) |

The /b/-spirantisation rule *lowers* the central-Mirandese PER (the largest,
most trustworthy row). The Sendinês row nudges up because its one
intervocalic-/b/ token, `lhobo`, is transcribed with a stop [ˈlobʊ] in the
`n = 11` gold — small-`n` lexical variability, not a Sendinês-specific block on
a pan-Ibero-Romance process. Residual error is otherwise dominated by
gold-notation choices the rules cannot and should not chase: the transcriber's
centralised final vowel [ʉ] for unstressed final ⟨-o⟩ (see below), and the
lexically variable /d/ occlusion (see Allophony above).

## Sources

- **Ferreira, M. B. & Raposo, D. (coords.) (1999).** *Convenção Ortográfica
  da Língua Mirandesa.* Câmara Municipal de Miranda do Douro / Centro de
  Linguística da Universidade de Lisboa. — the official orthography (§ L,
  § Sibilantes, § Ditongos, § Nasalidade, § Acento).
- **Ferreira, M. B. & Raposo, D. (coords.) (2000).** *Primeiro Aditamento à
  Convenção Ortográfica da Língua Mirandesa.* — Sendinês provisions.
- **Vasconcelos, J. Leite de (1900).** *Estudos de Philologia Mirandesa
  (Vol. I).* Imprensa Nacional, Lisboa. — foundational description of the
  sibilant system and the sub-dialect division.
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press. — reference for the shared Ibero-Romance processes
  (nasal place assimilation, spirantisation) and the adstrate reduction.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [romance](romance.md), [pt-PT](pt-PT.md), [ext-PT-x-barrancos](ext-PT-x-barrancos.md)*
