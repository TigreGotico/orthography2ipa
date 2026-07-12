# French (fr-FR) — Phonology Reference

**Code**: `fr-FR` | **Family**: Indo-European > Romance > Gallo-Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Orthographic depth**: deep (production threshold ≤ 0.25 PER)
**Sources**: Fouché (1959), Tranel (1987), Ladefoged & Maddieson (1996), Fougeron & Smith (1993), Tranel (1995)
**Benchmark**: wikipron `fra_latn_broad.tsv`, `fr` tag, n=279, PER=0.1559 (see `benchmarks/results.json`)

---

## Consonant System

### Key Consonant Rules

#### Softening: C and G Before Front Vowels

| Grapheme | Before e/i/y | Elsewhere | Examples |
|:---:|:---:|:---:|:---|
| c | [s] | [k] | `ceci` [səsi], `cœur` [kœʁ] |
| g | [ʒ] | [ɡ] | `général` [ʒeneʁal], `gâteau` [ɡɑto] |

The digraphs ⟨ç⟩ always → [s]; ⟨gu⟩ before e/i → [ɡ] (overrides softening); ⟨ge⟩/⟨gi⟩ digraphs → [ʒ].

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
| o (closed) | [o] | `pot` [po] |
| o (open) | [ɔ] | `sort` [sɔʁ] |
| ô | [o] | `côte` [kot] |
| u, û | [y] | `lune` [lyn] |
| ou | [u] | `tour` [tuʁ] |
| eu (closed) | [ø] | `feu` [fø] |
| eu (open) | [œ] | `peur` [pœʁ] |

Word-final unstressed ⟨e⟩ (e caduc) defaults to silent via a `positional_graphemes` `word_final` override, matching the modern colloquial elision of the mute e (`Abbeville` [abvil], not [abvilə]). This is correct for polysyllabic words but is a known engine-limit exception for monosyllabic function words (`le`, `que`, `de`), where the schwa is the only syllable nucleus and is grammatically obligatory.

### Nasal Vowels

| Grapheme | IPA | Example | Note |
|:---:|:---:|:---|:---|
| an, am, en, em | [ɑ̃] | `blanc` [blɑ̃] | Denasalizes before vowel in same word |
| in, im, ain, ein | [ɛ̃] | `vin` [vɛ̃] | |
| on, om | [ɔ̃] | `bon` [bɔ̃] | |
| un, um | [œ̃] | `lundi` [lœ̃di] | Merges with [ɛ̃] for many Parisian speakers |

**Denasalization**: Before a vowel within the same word, nasal vowels denasalize and the nasal consonant resurfaces, encoded via `positional_graphemes` `before_vowel` branches: `an`→[an] (`analyse` [analiz]), `am`→[am] (`amateur` [amatœʁ]), `en`→[ɛn], `em`→[ɛm], `in`→[in] (`inutile` [inytil]), `im`→[im] (`imaginer` [imaʒine]), `on`→[ɔn] (`bonasse` [bɔnas]), `om`→[ɔm], `un`→[yn] (`unanime` [ynanim]), `um`→[ym]. The doubled-consonant trigger for denasalization (`immense`, `ennemi`) is not modelled this way because the doubled letter is consumed by the `mm`/`nn` digraph before the positional check on the nasal grapheme runs — a known engine-limit gap, not a missing rule.

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

**Elision** (`le`/`la`/`je`/`de`/`que`/`ne`/`ce`/`se` + vowel-initial word → `l'`/`j'`/`d'`/`qu'`/`n'`/`c'`/`s'`) is already resolved in standard written French — the apostrophe form is the orthographic input — so it requires no additional G2P transform. Liaison is a genuine cross-word sandhi phenomenon and is encoded in `sandhi_rules` (`FR_LIAISON_Z`, `FR_LIAISON_T`, `FR_LIAISON_N`, `FR_LIAISON_R`, `FR_LIAISON_P`, `FR_ENCHAÎNEMENT`). Blocking liaison before h-aspiré words is not currently modelled: `h` maps to the empty string identically for both h-muet (`l'homme`, liaison/elision apply) and h-aspiré (`le héros`, liaison/elision blocked) words, so distinguishing them requires a lexical h-aspiré wordlist, which is out of scope for this pass.

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

- **h-aspiré blocking**: not modelled (see Liaison section above) — needs a lexical wordlist, not encodable purely from orthography.
- **Word-final schwa in monosyllables**: `positional_graphemes` silences word-final `e` by default (e caduc), which is correct for polysyllabic words but incorrectly silences the vowel of one-syllable function words (`le`, `que`, `de`).
- **Denasalization before doubled nasal letters**: `immense`, `ennemi`-type denasalization (nasal digraph followed by its own doubled consonant) is not triggered because `mm`/`nn` are tokenized as their own digraphs, not exposed as `before_consonant` context on the nasal vowel grapheme.
- **Loanword/proper-noun irregularity**: transliterated foreign names (`Amsterdam`, `Akram`) and acronyms spelled letter-by-letter dominate the residual wikipron mismatches; these are lexical exceptions rather than encodable grapheme rules.

---

## References

- Fouché, P. (1959). *Traité de prononciation française*. Klincksieck.
- Tranel, B. (1987). *The Sounds of French*. Cambridge University Press.
- Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
- Fougeron, C. & Smith, C.L. (1993). Illustrations of the IPA: French. *Journal of the International Phonetic Association*, 23(2), 73–76.
- Tranel, B. (1995). French liaison and elision revisited: A unified account within Optimality Theory. Rutgers Optimality Archive, ROA-15.
- Wikipedia: [French phonology](https://en.wikipedia.org/wiki/French_phonology)

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [romance](romance.md), [it-IT](it-IT.md), [pt-PT](pt-PT.md)*
