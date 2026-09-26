# French (fr-FR): Phonology Reference

**Code**: `fr-FR` | **Family**: Indo-European > Romance > Gallo-Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Orthographic depth**: deep (production threshold ≤ 0.25 PER)
**Sources**: Fouché (1959), Tranel (1987), Ladefoged & Maddieson (1996), Fougeron & Smith (1993), Tranel (1995), Walker (2001)
**Benchmark**: wikipron `fra_latn_broad.tsv`, `fr` tag, n=85495, PER=0.0882 (see `benchmarks/results.json`)

---

## Consonant System

### Key Consonant Rules

#### Softening: C and G Before Front Vowels

| Grapheme | Before e/i/y | Elsewhere | Examples |
|:---:|:---:|:---:|:---|
| c | [s] | [k] | `ceci` [səsi], `cœur` [kœʁ] |
| g | [ʒ] | [ɡ] | `général` [ʒeneʁal], `gâteau` [ɡɑto] |

The digraphs ⟨ç⟩ always → [s]. ⟨gu⟩ before e/i → [ɡ] (overrides softening). ⟨ge⟩/⟨gi⟩ digraphs → [ʒ].

#### Silent Word-Final Consonants

In modern French, **most written word-final consonants are not pronounced** in isolation. They may surface in liaison before a vowel-initial word.

| Grapheme | Word-final | Liaison (before vowel) | Examples |
|:---:|:---:|:---:|:---|
| s | [∅] | [z] | `les amis` [le‿z‿ami] |
| t | [∅] | [t] | `petit enfant` [pəti‿t‿ɑ̃fɑ̃] |
| d | [∅] | [t] | `grand homme` [ɡʁɑ̃‿t‿ɔm] |
| p | [∅] | rare | `trop aimable` |
| x | [∅] | [z] | `deux enfants` [dø‿z‿ɑ̃fɑ̃] |
| r | [∅] | [ʁ] | infinitives: `parler` [paʁle] (r silent) |
| n | [∅] | [n] | `bon ami` [bɔ‿n‿ami] |

**Exceptions**: `cher` [ʃɛʁ], `mer` [mɛʁ], monosyllables, borrowed words.

Liaison is encoded as `intervocalic_cross_word` in `positional_graphemes`:
```json
"s": {"intervocalic_cross_word": ["z"], "word_final": [""], "default": ["s"]}
```

#### Intervocalic S

Within a word, ⟨s⟩ between two vowels is voiced [z]:

| Environment | Realization | Examples |
|:---|:---:|:---|
| Intervocalic | [z] | `maison` [mɛzɔ̃], `rose` [ʁoz] |
| Elsewhere | [s] | `sac` [sak], `masse` [mas] |

Note: ⟨ss⟩ → [s] (voiceless): `passer` [pase].

#### Doubled Consonants

Doubled consonant letters (`bb`, `dd`, `ff`, `gg`, `ll`, `mm`, `nn`, `pp`, `rr`, `tt`) degeminate to a single consonant, the modern-French default (Fouché 1959; Tranel 1987): `Abbeville` [abvil], `Allier` [alje], `Abdallah` [abdala]. The `ill` digraph (after a vowel) keeps its special [ij]/[il] treatment ahead of the generic `ll` digraph via maximal-munch tokenization.

**Irregular ⟨ill⟩ = [il] class**: a small closed set of words keeps ⟨ill⟩ as [il] rather than the [ij] default — `ville`, `mille`, `tranquille` (and `tranquillement`), and the place name `Lille` — handled as `word_exceptions` (Tranel 1987 §4.3).

#### Mute grammatical endings ⟨-er⟩ / ⟨-ez⟩

Word-final ⟨-er⟩ of infinitives and agent nouns is [e], and the 2pl ⟨-ez⟩ is
[e]: `parler` [paʁle], `manger` [mɑ̃ʒe], `boulanger` [bulɑ̃ʒe], `mangez`
[mɑ̃ʒe], `nez` [ne], `chez` [ʃe], `assez` [ase] — final-consonant elision in the
*grammatical ending* (Fouché 1959; Tranel 1987 §3). This is `grammatical_endings`,
not a grapheme: the same letters inside a word (`personne` [pɛʁsɔn], `version`
[vɛʁsjɔ̃], `terre` [təʁ]) are ordinary graphemes and stay untouched, and the
ending still matches behind the transparent plural ⟨-s⟩ (`boulangers` [bulɑ̃ʒe]).

The closed set of nouns and adverbs that keep /ɛʁ/ — `mer`, `fer`, `cher`,
`ver`, `hier`, `hiver`, `enfer`, `cancer`, `amer`, `super`, and the ⟨-er⟩
loanwords (`leader`, `container`, `poker`) — stays in `word_exceptions`, which
outranks the endings; their ⟨-s⟩ plurals are listed there too.

#### Ambiguous ending ⟨-ent⟩: both readings, no decision

The 3rd-person-plural inflection ⟨-ent⟩ is mute (`parlent` [paʁl], `munissent`
[mynis]); the nominal and adjectival ⟨-ent⟩ is [ɑ̃] (`vent`, `dent`, `cent`,
`argent`, `moment`, `comment`). Nothing in the spelling separates them — it is a
part-of-speech fact (Fouché 1959; Tranel 1987 §3; Divay & Vitale 1997), and this
library takes no part-of-speech input.

So French declares the ending as a **deferring candidate list**, `"ent": [null,
""]`. `null` at element 0 keeps rank 1 exactly where the grapheme tables put it
— nasal ⟨en⟩ plus a silent ⟨t⟩ — so every 1-best is unchanged (`vent` [vɑ̃],
`moment` [mɔmɑ̃], `parlent` [paʁlɑ̃]). The mute reading is added below it, where
`word_candidates`, oracle@k and a downstream POS-aware rescorer can reach it;
before this it was in no beam at any width. ⟨-ment⟩ is deliberately not declared
separately: it is the same ambiguity (`dorment` is mute, `moment` is not).

#### Glide Formation

Word-internal ⟨i⟩ before another vowel letter glides to [j] (`positional_graphemes` `before_vowel` branch, Tranel 1987 §5-6): `pied` [pje], `fiacre` [fjakʁ]. This is distinct from the ⟨y⟩/⟨ien⟩/⟨oui⟩ digraphs, which already carry [j] unconditionally.

Known trade-off: hiatus is preserved in a small learned/prefixed class (`anti-`, `bi-`, `archi-` compounds, and nouns such as `lion`, `ion`, `chiite`, `biathlon`) where careful speech and the wikipron reference keep [iV] rather than [jV] (Tranel 1987 §5 notes this variation). The rule glides these too — 23 words in the wikipron corpus move away from the reference while 8,097 move toward it. A finer split would need syllable-count or morpheme-boundary knowledge the orthography does not encode.

The glide is blocked when the following vowel is itself the word's last audible slot (the engine-level `before_final_vowel` position) — word-final unmarked ⟨ie⟩ stays [i] rather than gliding into a vowel-less [vj]: `vie` [vi], `envie` [ɑ̃vi], `folie` [fɔli], `Algérie` [alʒeʁi], and the plural `vies` [vi] (⟨s⟩ is a transparent, independently-silenced suffix grapheme — Tranel 1987 §3 — so it doesn't count as "more word left"). This does not affect `pied`/`fiacre`, where the vowel after ⟨i⟩ is followed by a real root-final consonant and still must carry the syllable's nucleus.

---

## Vowel System

### Oral Vowels

| Grapheme | IPA | Example |
|:---:|:---:|:---|
| a | [a] | `chat` [ʃa] |
| â | [ɑ] | `pâte` [pɑt] |
| é | [e] | `été` [ete] |
| è, ê, ë | [ɛ] | `mère` [mɛʁ] |
| e (unstressed, non-final) | [ə] | `le` [lə] |
| e (word-final) | silent | `Adèle` [adɛl] (not [adɛlə]) |
| i, î, ï | [i] | `île` [il] |
| o (open syllable) | [o] | `pot` [po] |
| o (closed syllable) | [ɔ] | `sort` [sɔʁ] |
| ô | [o] | `côte` [kot] |
| u, û | [y] | `lune` [lyn] |
| ou | [u] | `tour` [tuʁ] |
| eu (open syllable) | [ø] | `feu` [fø] |
| eu (closed syllable) | [œ] | `peur` [pœʁ] |

#### Mid-Vowel Aperture: the *loi de position*

The three mid-vowel pairs /e ɛ/, /ø œ/ and /o ɔ/ are not free: the close-mid
member belongs to an **open** syllable (*syllabe libre*, no coda) and the
open-mid member to a **closed** one (*syllabe entravée*). Fougeron & Smith
(1993) state the law in exactly those terms, and Tranel (1987) ch. 3-4 and
Walker (2001) ch. 3 give it with its limits. This spec models **standard
Parisian/northern** French, which is what the wikipron gold transcribes.

| Pair | Open syllable | Closed syllable |
|:---|:---|:---|
| /ø œ/ | `heu·reux` [øʁø], `jeu·di` [ʒødi] | `jeune` [ʒœn], `heure` [œʁ], `seule` [sœl] |
| /o ɔ/ | `mot` [mo], `nu·mé·ro` [nymeʁo] | `bord` [bɔʁ], `botte` [bɔt] |
| /e ɛ/ | `é·té` [ete], `nu·mé·ro` [nymeʁo] | `sel` [sɛl], `Abel` [abɛl] |

Three points, and one of them is about the engine rather than about French:

- **Aperture is decided ORTHOGRAPHICALLY, and the coda test is a proxy.** The
  law is about a pronounced coda, but the engine has only letters, so it asks
  a spelling question instead: strip the graphemes THIS spec declares silent
  word-finally, then look at what the syllable now ends in. Two consequences
  worth knowing before trusting an aperture answer:
  - A final syllable whose only vowel letter is a mute ⟨e⟩ has no nucleus, so
    it is folded into its predecessor (`positional.merge_nucleusless_final_syllable`,
    generic and spec-driven): `jeu·ne` becomes one syllable `jeune`, which
    strips to `jeun` and is CLOSED — [ʒœn], not [ʒø] plus a silent tail. Same
    for `heure` [œʁ], `veuve` [vœv], `seule` [sœl].
  - The strip then runs a SECOND time on that merged string, on letters that
    are no longer word-final in the pronunciation. That is why `meute` [møt]
    and `heureuse` [øʁøz] come out right for the wrong reason: both strip back
    to an open `meu`/`reu` because the spec calls word-final ⟨t⟩ and ⟨s⟩ mute,
    yet the /t/ and the /z/ are both pronounced. The vowel is close-mid in
    those two words for a real reason (the /z/ exception below; the ⟨t⟩+⟨e⟩
    shape), not because the syllable is open.

  Where the proxy is simply wrong: a pronounced coda that does not close for
  the law — an obstruent + liquid cluster, `neutre` [nøtʁ] and `feutre` [føtʁ]
  come out with [œ] — and a /z/ that is spelled ⟨z⟩ and so cannot be stripped,
  which is what the rule below exists to catch. Both are known and measured,
  not hypothetical: 20 types regress corpus-wide, against 232 fixed.
- **/z/ keeps the vowel close** even in a closed syllable — the standard
  closing-environment exception, stated for the whole mid series: `rose`
  [ʁoz], `chose` [ʃoz] (`FR_O_BEFORE_Z`), and `Deleuze` [dəløz], `yeuz` [jøz]
  (`FR_EU_BEFORE_Z`) — Fouché 1959; Tranel 1987 §3; Walker 2001 ch. 3. The
  ⟨eu⟩ half is needed only where the /z/ is spelled ⟨z⟩: the far commoner
  ⟨euse⟩ words (`heureuse`, `creuse`, `chanteuse`) already reach [ø] through
  the strip described above.
- **/ʁ/ opens ⟨au⟩**: `Laure` [lɔʁ], `aurore` [ɔʁɔʁ], `restaurant`
  [ʁɛstɔʁɑ̃], `dinosaure` [dinozɔʁ] — the one systematic exception to the
  otherwise exceptionless ⟨au⟩ = [o] (`FR_AU_BEFORE_R`; Fouché 1959; Tranel
  1987 ch. 3; Walker 2001 ch. 3). Learned and foreign spellings resist it
  (`Saurat`, `nauruan`, `vaurien` keep [o] in the gold): 139 wikipron types
  move toward the reference, 8 away.

What is deliberately **not** modelled:

- **⟨o⟩ read off syllable aperture.** Generalising open→[o] is the *southern*
  French pattern (Walker 2001 ch. 3). Standard French keeps [ɔ] in non-final
  open syllables — `ho·mo·phone` [ɔmɔfɔn], `o·bole` [ɔbɔl], `homme` [ɔm] —
  so ⟨o⟩ stays on the word-final-open and pre-/z/ rules above. Tried: PER
  0.0887 → 0.1177, 16,836 wikipron types worse against 447 better.
- **⟨e⟩ read off syllable aperture.** French ⟨e⟩ is [ɛ] in a *graphically*
  closed syllable whether or not the coda is pronounced (`met` [mɛ], `mets`
  [mɛ], `effets` [efɛ]), so it keeps the orthographic `FR_E_CLOSED_CLUSTER` /
  `FR_E_CLOSED_FINAL` rules. Tried: PER 0.0887 → 0.0903.
- **⟨eu⟩ opened before /ʁ/**, as the ⟨au⟩ rule does. In an open syllable the
  quality is lexical rather than positional — `heureux` [øʁø] and `euro`
  [øʁo] against `fleurette` [flœʁɛt] — which is what Walker (2001) ch. 3 says
  of non-final syllables. Tried: 103 types better, 112 worse, PER unmoved.

Word-final unstressed ⟨e⟩ (e caduc) defaults to silent via a `positional_graphemes` `word_final` override, matching the modern colloquial elision of the mute e (`Abbeville` [abvil], not [abvilə]). This is correct for polysyllabic words but is a known engine-limit exception for monosyllabic function words (`le`, `que`, `de`), where the schwa is the only syllable nucleus and is grammatically obligatory.

### Nasal Vowels

| Grapheme | IPA | Example | Note |
|:---:|:---:|:---|:---|
| an, am, en, em | [ɑ̃] | `blanc` [blɑ̃] | Denasalizes before vowel in same word |
| in, im, ain, ein | [ɛ̃] | `vin` [vɛ̃] | |
| on, om | [ɔ̃] | `bon` [bɔ̃] | |
| un, um | [œ̃] | `lundi` [lœ̃di] | Merges with [ɛ̃] for many Parisian speakers |

**Denasalization**: Before a vowel within the same word, nasal vowels denasalize and the nasal consonant resurfaces, encoded via `positional_graphemes` `before_vowel` branches: `an`→[an] (`analyse` [analiz]), `am`→[am] (`amateur` [amatœʁ]), `en`→[ɛn], `em`→[ɛm], `in`→[in] (`inutile` [inytil]), `im`→[im] (`imaginer` [imaʒine]), `on`→[ɔn] (`bonasse` [bɔnas]), `om`→[ɔm], `un`→[yn] (`unanime` [ynanim]), `um`→[ym]. The doubled-consonant trigger for denasalization (`immense`, `ennemi`) is not modelled this way because the doubled letter is consumed by the `mm`/`nn` digraph before the positional check on the nasal grapheme runs, a known engine-limit gap, not a missing rule.

**ɛ̃/œ̃ merger**: Fougeron & Smith (1993) document that many speakers, especially in and around Paris, merge /œ̃/ into /ɛ̃/ (`brun`/`brin`, `un`/`hein` become homophonous), while conservative Standard French retains the distinction. Both realizations are kept as allophones of `œ̃` in `allophones` rather than collapsing the phoneme inventory, since Fougeron & Smith still treat /œ̃/ as phonemically distinct for their reference (young Parisian female) speaker.

---

## Liaison

Liaison is a cross-word sandhi process where a normally silent final consonant is pronounced before a vowel-initial word.

**Obligatory** (grammatically conditioned):
- Determiner + noun: `les amis` [le‿z‿ami]
- Adjective + noun: `petit ami` [pəti‿t‿ami]
- Subject pronoun + verb: `nous avons` [nu‿z‿avɔ̃]

**Forbidden** (liaison blocked):
- After conjunction `et`
- Before aspirate-h words: `les haricots` [le.aʁiko] (no liaison)
- Singular noun + adjective: `un étudiant américain` (no liaison after étudiant)

Tranel (1995) formalises liaison and elision within Optimality Theory as both driven by ONSET satisfaction (syllables prefer an onset consonant): linking consonants and eliding vowels are underlyingly "floating" segments that surface only when doing so yields a better-formed syllable for the following vowel-initial word. Aspirate-h words (`hibou` [ibu]) are lexically vowel-initial but block both liaison (`les hiboux` *[lezibu]) and elision (`le hibou` *[libu]) because they require left-edge alignment between the word boundary and the syllable boundary (ALIGN-LEFT ≫ ONSET), unlike regular vowel-initial words where ONSET dominates alignment.

**Elision** (`le`/`la`/`je`/`de`/`que`/`ne`/`ce`/`se` + vowel-initial word → `l'`/`j'`/`d'`/`qu'`/`n'`/`c'`/`s'`) is already resolved in standard written French, the apostrophe form is the orthographic input, so it requires no additional G2P transform. Liaison is a genuine cross-word sandhi phenomenon and is encoded in `sandhi_rules` (`FR_LIAISON_Z`, `FR_LIAISON_T`, `FR_LIAISON_N`, `FR_LIAISON_R`, `FR_LIAISON_P`, `FR_ENCHAÎNEMENT`). Blocking liaison before h-aspiré words is not currently modelled: `h` maps to the empty string identically for both h-muet (`l'homme`, liaison/elision apply) and h-aspiré (`le héros`, liaison/elision blocked) words, so distinguishing them requires a lexical h-aspiré wordlist, which is out of scope for this pass.

---

## Digraphs

| Grapheme | IPA | Examples |
|:---:|:---:|:---|
| ch | [ʃ] | `chat` [ʃa] |
| gn | [ɲ] | `vigne` [viɲ] |
| ph | [f] | `photo` [foto] |
| ill (after vowel) | [ij] | `fille` [fij] |
| oi | [wa] | `moi` [mwa] |
| ou | [u] | `ou` [u] |
| ui | [ɥi] | `nuit` [nɥi] |
| eu | [ø/œ] | `feu` [fø] / `peur` [pœʁ] |
| bb, dd, ff, gg, ll, mm, nn, pp, rr, tt | single consonant | `Abbeville` [abvil], `Allier` [alje] |

---

## Known Engine-Limit Exceptions

- **h-aspiré blocking**: not modelled (see Liaison section above), needs a lexical wordlist, not encodable purely from orthography.
- **Word-final schwa in monosyllables**: `positional_graphemes` silences word-final `e` by default (e caduc), which is correct for polysyllabic words but incorrectly silences the vowel of one-syllable function words (`le`, `que`, `de`).
- **Denasalization before doubled nasal letters**: `immense`, `ennemi`-type denasalization (nasal digraph followed by its own doubled consonant) is not triggered because `mm`/`nn` are tokenized as their own digraphs, not exposed as `before_consonant` context on the nasal vowel grapheme.
- **Loanword/proper-noun irregularity**: transliterated foreign names (`Amsterdam`, `Akram`) and acronyms spelled letter-by-letter dominate the residual wikipron mismatches. These are lexical exceptions rather than encodable grapheme rules.

---

## References

- Fouché, P. (1959). *Traité de prononciation française*. Klincksieck.
- Tranel, B. (1987). *The Sounds of French*. Cambridge University Press.
- Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
- Fougeron, C. & Smith, C.L. (1993). Illustrations of the IPA: French. *Journal of the International Phonetic Association*, 23(2), 73–76.
- Tranel, B. (1995). French liaison and elision revisited: A unified account within Optimality Theory. Rutgers Optimality Archive, ROA-15.
- Wikipedia: [French phonology](https://en.wikipedia.org/wiki/French_phonology)

---
[← Romanian](ro-RO.md) · [Home](../index.md) · [Italian →](it-IT.md)
