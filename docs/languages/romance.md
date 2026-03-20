# Romance Languages — Comparative Phonology Reference

**Codes**: `es-ES`, `fr-FR`, `it-IT`, `pt-PT`, `pt-BR`, `ca`, `ro-RO`, `gl-ES`, `oc-x-aranes`, and variants
**Family**: Romance (from Latin) | **Script**: Latin (alphabet)

---

## C/G Softening — Shared Romance Feature

All Romance languages inherited Latin's **palatal softening** of ⟨c⟩ and ⟨g⟩ before front vowels:

| Language | c before e/i | g before e/i | Notes |
|:---|:---:|:---:|:---|
| French | [s] | [ʒ] | Also before y |
| Italian | [tʃ] | [dʒ] | Digraphs ch/gh override |
| Spanish | [s] (Lat. Am.) / [θ] (Castilian) | [x] | g before e/i → [x] |
| Portuguese | [s] | [ʒ] | |
| Catalan | [s] | [dʒ] / [ʒ] | |
| Romanian | [tʃ] | [dʒ] | |

---

## Spanish (es-ES) Phonology

### Seseo vs. Distinción

| Variety | ⟨c⟩/⟨z⟩ before e/i | Example |
|:---|:---:|:---|
| Castilian (Spain) | [θ] (dental fricative) | `cero` [ˈθeɾo] |
| Latin American + Andalusian | [s] | `cero` [ˈseɾo] |

### Spanish Lenition (Spirantization)

In connected speech, Spanish voiced stops become fricatives/approximants **between vowels**:

| Phoneme | Allophone | Environment | Example |
|:---:|:---:|:---|:---|
| /b/ | [β] | Intervocalic | `lobo` [ˈloβo] "wolf" |
| /d/ | [ð] | Intervocalic | `lado` [ˈlaðo] "side" |
| /g/ | [ɣ] | Intervocalic | `lago` [ˈlaɣo] "lake" |

(Encoded in `allophones`, not `positional_graphemes`, as it's post-phonemic)

### Spanish Rhotic Contrast

| Grapheme | IPA | Environment | Example |
|:---:|:---:|:---|:---|
| r (single) | [ɾ] (tap) | Intervocalic | `pero` [ˈpeɾo] "but" |
| rr (double) | [r] (trill) | Intervocalic | `perro` [ˈpero] "dog" |
| r | [r] (trill) | Word-initial | `rosa` [ˈrosa] |
| r | [r] (trill) | After n/l/s | `Israel` |

---

## Portuguese Phonology

Portuguese has the most complex phonology of the major Romance languages.

### European (pt-PT) vs. Brazilian (pt-BR)

| Feature | pt-PT (Lisbon) | pt-BR (standard) |
|:---|:---:|:---:|
| Unstressed e | [ɨ] (near-close central) | [e] or [i] |
| Unstressed o | [u] | [o] or [u] |
| -al, -el word-final | [ɐl]/[ɛl] | [aw]/[ɛw] (l-vocalization) |
| r (initial/rr) | [ʁ] (uvular) | [h] or [x] |
| s/z word-final | [ʃ]/[ʒ] (Lisbon) | [s]/[z] |

### S Allophony (pt-PT Lisbon)

Portuguese ⟨s⟩ has the most complex distribution in Romance:

| Position | Realization | Example |
|:---|:---:|:---|
| Word-initial | [s] | `sol` [sol] |
| Intervocalic | [z] | `casa` [ˈkazɐ] |
| Before voiced consonant | [ʒ] | `mesmo` [ˈmeʒmu] |
| Before voiceless consonant | [ʃ] | `estar` [ɨʃˈtar] |
| Word-final | [ʃ] (Lisbon) | `gatos` [ˈɡatuʃ] |
| Cross-word before vowel | [z] | `os amigos` [uz‿ɐˈmiɡuʃ] |

This is fully encoded in `pt-PT.json`'s `positional_graphemes`.

---

## French Nasal Vowels vs. Italian/Spanish

French preserved Latin nasal vowels; Italian and Spanish lost them:

| Latin | French | Italian | Spanish |
|:---|:---:|:---:|:---:|
| *finem | `fin` [fɛ̃] | `fine` [ˈfiːne] | `fin` [fin] |
| *bonum | `bon` [bɔ̃] | `buono` [ˈbwɔno] | `bueno` [ˈbweno] |
| `grande` | `grand` [ɡʁɑ̃] | `grande` [ˈɡrande] | `grande` [ˈɡɾande] |

---

## Romanian — Most Conservative Romance Language

Romanian preserved features lost in Western Romance:
- Case system (nominative/accusative vs. genitive/dative)
- Neuter gender
- Definite article suffixed to noun: `om` "man" → `omul` "the man"
- Schwa phoneme: `ă` [ə]
- Central high unrounded: `â`/`î` [ɨ]

### Romanian Key Graphemes

| Grapheme | IPA | Example |
|:---:|:---:|:---|
| ă | [ə] | `mamă` [ˈmamə] |
| â, î | [ɨ] | `înainte` [ɨnˈainte] |
| e | [je] word-initial | `este` [ˈjeste] |
| c before e/i | [tʃ] | `cer` [tʃer] |
| g before e/i | [dʒ] | `ger` [dʒer] |
| ch | [k] | `cheie` [ˈkeje] |
| gh | [ɡ] | `gheaţă` [ˈɡjatsə] |

---

## Catalan — Between French and Iberian

Catalan occupies a phonological position between French and Iberian Romance:
- Unstressed vowel reduction (like Portuguese/French): `a`→[ə], `e`→[ə] unstressed (Central Catalan)
- [l·l] (geminate lateral): `col·legi` [kulˈledʒi]
- ⟨·⟩ (punt volat) distinguishes `l·l` from `ll` [ʎ]
- Dialectal variation: Valencian, Balearic, Northern Catalan

---

## References

- Penny, R. (2002). *A History of the Spanish Language* (2nd ed.). CUP.
- Tranel, B. (1987). *The Sounds of French*. CUP.
- Lepschy & Lepschy (1988). *The Italian Language Today*. Routledge.
- Mateus, M.H. & d'Andrade, E. (2000). *The Phonology of Portuguese*. OUP.
- Maiden, M. & Parry, M. (1997). *The Dialects of Italy*. Routledge.
