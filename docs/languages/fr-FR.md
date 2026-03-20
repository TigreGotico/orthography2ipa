# French (fr-FR) — Phonology Reference

**Code**: `fr-FR` | **Family**: Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Sources**: Léon (1992), Tranel (1987), Côté (2000)

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

---

## Vowel System

### Oral Vowels

| Grapheme | IPA | Example |
|:---:|:---:|:---|
| a | [a] | `chat` [ʃa] |
| â | [ɑ] | `pâte` [pɑt] |
| é | [e] | `été` [ete] |
| è, ê, ë | [ɛ] | `mère` [mɛʁ] |
| e (unstressed) | [ə] | `le` [lə] |
| i, î, ï | [i] | `île` [il] |
| o (closed) | [o] | `pot` [po] |
| o (open) | [ɔ] | `sort` [sɔʁ] |
| ô | [o] | `côte` [kot] |
| u, û | [y] | `lune` [lyn] |
| ou | [u] | `tour` [tuʁ] |
| eu (closed) | [ø] | `feu` [fø] |
| eu (open) | [œ] | `peur` [pœʁ] |

### Nasal Vowels

| Grapheme | IPA | Example | Note |
|:---:|:---:|:---|:---|
| an, am, en, em | [ɑ̃] | `blanc` [blɑ̃] | Denasalizes before vowel in same word |
| in, im, ain, ein | [ɛ̃] | `vin` [vɛ̃] | |
| on, om | [ɔ̃] | `bon` [bɔ̃] | |
| un, um | [œ̃] | `lundi` [lœ̃di] | Merges with [ɛ̃] for many speakers |

**Denasalization**: Before a vowel within the same word, nasal vowels denasalize and the nasal consonant resurfaces: `bonne` [bɔn] vs. `bon` [bɔ̃].

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

---

## References

- Léon, P. (1992). *Phonétisme et prononciations du français*. Nathan.
- Tranel, B. (1987). *The Sounds of French*. Cambridge University Press.
- Côté, M.-H. (2000). *Consonant cluster simplification*. MIT dissertation.
- Wikipedia: [French phonology](https://en.wikipedia.org/wiki/French_phonology)
