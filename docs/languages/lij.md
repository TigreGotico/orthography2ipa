# Ligurian / Genoese (lij) — Phonology Reference

**Code**: `lij` | **Family**: Romance (Gallo-Italic) | **Script**: Latin (alphabet)
**Quality tier**: research | **Reference variety**: Genoese (*Zeneise*)
**Sources**: Académia Ligùstica do Brénno, *Grafia ofiçiâ* (2008); Toso, *Grammatica del genovese* (1997); Forner, *Generative Phonologie des Dialekts von Genua* (1975); Maiden & Parry, *The Dialects of Italy* (1997); Omniglot (tertiary cross-check)

---

## Input contract

This spec follows the **standardised *grafia ofiçiâ*** of the
[Académia Ligùstica do Brénno](https://en.wikipedia.org/wiki/Academia_Ligustica_do_Brenno)
— the official Genoese orthography adopted by the Ligurian Wikipedia and by
Toso's dictionaries. Feed it text in that orthography (accents and length
marks included); ad-hoc or Italianising spellings are out of scope.

Ligurian is a Gallo-Italic language of Liguria (~500,000 speakers), the
historical lingua franca of Mediterranean maritime trade.

---

## Hallmark grapheme → IPA correspondences

These are the features a correct Genoese spec must get right — several are
diagnostic of the language and set it apart from Italian.

| Grapheme | IPA | Note |
|:---:|:---:|:---|
| `x` | /ʒ/ | **The diagnostic Genoese letter** — the French ⟨j⟩ sound (`gexa` [ˈdʒeʒa] "church") |
| `o` | /u/ | Genoese ⟨o⟩ is Italian ⟨u⟩; `ó` = /u/, `ô` = /uː/ |
| `ò` | /ɔ/ | Open back — contrasts with `o` = /u/; `ö` = /ɔː/ |
| `u` | /y/ | Front rounded; `û`, `ü` = /yː/ |
| `eu` | /ø/ | Front rounded mid; `êu` = /øː/ |
| `æ` | /ɛː/ | Long open-mid front (`çittæ` [siˈtɛː] "city") |
| `ç` | /s/ | Cedilla voiceless sibilant |
| `z` | /z/ | **Always /z/** — never an affricate (unlike Italian) |
| `sc` | /ʃ/ before a front vowel, else /sk/ | positional |
| `scc` | /ʃtʃ/ | trigraph (`scciappâ` [ʃtʃiaˈpaː]) |
| `n-`, `nn-` | /ŋ/ | the intervocalic **velar nasal** (`lann-a` [ˈlãŋa] "wool") |

### C and G softening (positional)

| Grapheme | Before a front vowel | Elsewhere |
|:---:|:---:|:---:|
| `c` | [tʃ] | [k] (`ch` = [k] always) |
| `g` | [dʒ] | [ɡ] (`gh` = [ɡ] always) |

### Vowel length and stress (accent marks)

The grafia encodes length and stress orthographically:

- **Grave** `à è ì ò ù` — the stressed vowel (quality: /a ɛ i ɔ y/).
- **Acute** `é ó` — stressed close-mid /e/ and /u/.
- **Circumflex** `â ê î ô û` — long stressed vowels word-finally (/aː eː iː uː yː/).
- **Diaeresis** `ä ë ï ö ü` — long vowels word-medially.

Default stress is **paroxytone** (penultimate); any written accent marks the
stressed syllable and always wins, so stress is recoverable from the spelling.

---

## Post-lexical allophony (`allophone_rules`)

The velar nasal and vowel nasalisation are modelled as post-lexical rules
(the second of the library's "two maps"):

| Rule | Effect | Source |
|:---|:---|:---|
| `LIJ_N_VELAR_FINAL` | word-final /n/ → [ŋ] (`can` → [kaŋ] "dog") | Toso 1997 |
| `LIJ_N_VELAR_ASSIM` | /n/ → [ŋ] before /k ɡ/ | Toso 1997 |
| `LIJ_N_LABIAL_ASSIM` | /n/ → [m] before /p b m f/ | Toso 1997 |
| `LIJ_NASAL_*` | vowel → nasalised before [ŋ] (`lann-a` → [ˈlãŋa]) | Forner 1975; Toso 1997 |

Modern Genoese has **total degemination**, so double consonants map to a
single phoneme (`xatta` → [ˈʒata] "cat").

---

## Vowel inventory

Close: /i y u/ · Mid: /e ø ɛ ɔ/ · Open: /a/ — each with a long counterpart
(/iː yː uː eː øː ɛː ɔː aː/), and nasalised allophones before the velar nasal.
The front rounded pair **/y ø/** and the length contrast are the salient
vocalic features (Forner 1975).

---

## Modelled limitations

- The silent ⟨i⟩ marker after palatal `c`/`g` before a back vowel is handled
  via `cia/cio/ciu/gia/gio/giu…` digraphs, so `ciù` → [ˈtʃy] and
  `giornâ` → [dʒurˈnaː] (the ⟨i⟩ does not surface). Before a consonant the
  ⟨i⟩ is a real vowel and is kept (`cina` → [ˈtʃina]).
- `gl` is treated as [ɡl] (Genoese lacks the Italian ⟨gli⟩ = [ʎ]).
- No registered gold benchmark exists for Ligurian; correctness rests on the
  cited grafia ofiçiâ and descriptive grammars, not on PER.

---

## Sources

- Académia Ligùstica do Brénno. *Grafia ofiçiâ: grafia moderna do zeneize.* 2008. <http://www.zeneize.net/>
- Toso, Fiorenzo. *Grammatica del genovese: varietà urbana e di koinè.* Le Mani, 1997.
- Forner, Werner. *Generative Phonologie des Dialekts von Genua.* Buske, 1975.
- Maiden, M. & Parry, M. (eds.) *The Dialects of Italy.* Routledge, 1997.
- Omniglot. *Genoese (Zeneize) language and pronunciation.* <https://www.omniglot.com/writing/genoese.htm> (tertiary cross-check).

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [romance](romance.md), [it-IT](it-IT.md)*
