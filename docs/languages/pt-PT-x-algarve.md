# Algarvio Portuguese (pt-PT-x-algarve) — Phonology Reference

**Code**: `pt-PT-x-algarve` | **Family**: Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Parent**: `pt-PT`
**Sources**: Cintra (1971, *Boletim de Filologia* 22: 81–116), Brissos (2014,
*Journal of Portuguese Linguistics* 13(1): 63–115), Segura da Cruz (1989),
Mateus & d'Andrade (2000), Cunha & Cintra (1984), Boléo (1974)

Algarvio is the southernmost continental European Portuguese dialect (Faro,
Portimão, Lagos, Sagres). It inherits the full pt-PT base — graphemes,
positional rules and the post-lexical `allophone_rules` (dark coda /l/,
coda-sibilant chiado) — and declares only its own deltas. See
[../allophony.md](../allophony.md) for the two-maps model.

## The defining feature: stressed /u/ → [y]

The most salient and diagnostic Algarvio feature is the fronting of the
**stressed** labio-velar /u/ to the front rounded vowel **[y]** (as in French
*tu*, German *über*) — the isogloss by which Cintra (1971) delimits the
*Barlavento* Algarvio:

> "a palatalização, em maior ou menor grau, da vogal tónica u" — Cintra (1971)

Brissos (2014) gives the acoustic forms [tˈyd] *tudo*, [lˈymɨ] *lume*; Segura da
Cruz (1989) devotes a whole study to it ("La palatalisation de [u] dans le
«Barlavento Algarvio»"). It is **stressed-only** — Lüdtke (1957) and Maia
(1975–78, via Cintra 1971 and Brissos 2014) note it does not reach an
unstressed /u/.

### Post-lexical allophony (allophone_rules)

| id | Process | Rule | Example |
|:---|:---|:---|:---|
| `ALG_U_FRONTING` | Stressed /u/ fronting | /u/ → [y] / stressed nucleus | `tudo` [ˈtydu], `lume` [ˈlymɨ] |

The rule is conditioned on the **stressed nucleus** only. This keeps it
faithful and prevents a cascade: the pt-PT base reduces an unstressed /o/ to
[u], and that reduced [u] is unstressed, so `ALG_U_FRONTING` never feeds on it.

```python
from orthography2ipa import G2P
G2P("pt-PT-x-algarve").transcribe_word("tudo")      # ˈtydu
G2P("pt-PT-x-algarve").transcribe_word("sul")       # ˈsyɫ
G2P("pt-PT-x-algarve").transcribe_word("turistas")  # tuˈɾiʃtɐʒ  (unstressed u kept)
```

### Proclitic guard (word_exceptions)

The word-level stress detector mis-marks the common monosyllabic clitics as
stressed, which would otherwise let `ALG_U_FRONTING` wrongly front the article
and contraction vowels (`o` → [ˈy], `no` → [ˈny]). Since in real Algarvio the
article/contraction vowel is [u], these function words carry explicit
`word_exceptions` with their correct [u]-vowel forms:

| word | form | word | form | word | form |
|:---|:---|:---|:---|:---|:---|
| o | u | no | nu | do | du |
| os | uʒ | nos | nuʒ | dos | duʒ |
| ao | aw | aos | awʒ | um | ũ |
| pelo | pɛlu | pelos | pɛluʒ | uns | ũʒ |

```python
G2P("pt-PT-x-algarve").transcribe_word("o")   # ˈu   (NOT ˈy)
G2P("pt-PT-x-algarve").transcribe("no mar")    # ˈnu ˈmaɾ
```

Genuine stressed lexical /u/ (`tu`, `sul`, `tudo`) is untouched by the guard
and still fronts.

## Other modelled features (inherited or delta)

| Process | Where | Example |
|:---|:---|:---|
| /ej/ → [e] monophthong | `graphemes` delta | `leite` [ˈletɨ] |
| /ow/ → [o] monophthong | `graphemes` delta | `outro` [ˈotɾu] |
| Word-final /s/ → [ʒ] (sibilant voicing) | `positional_graphemes` delta | `mas` [maʒ] |
| Dark coda /l/ → [ɫ] | inherited `allophone_rules` | `sol` [ˈsɔɫ] |
| Coda /s/ → [ʃ] (chiado) | inherited `allophone_rules` | `gosto` [ˈɡɔʃtu] |
| Open stressed vowels [ɛ, ɔ] | inherited | `forte` [ˈfɔɾtɨ] |

## What the spec deliberately does NOT model

Honest limits, each a documented decision:

- **The wider central-southern chain shift** — Brissos (2014) documents a
  stressed [a] → [ɛ] fronting in high-vowel/palatal contexts and an [ɔ] → [o̝]
  raising. These are context-conditioned and only variably categorical;
  modelling them alongside `ALG_U_FRONTING` risks a cascade collapse of the
  vowel space, so only the categorical /u/ → [y] is realised and the rest is
  documented here.
- **Apico-alveolar sibilant [s̺]** (older/rural speakers) — an *articulatory*
  distinction with no phonemic contrast in this variety; Cintra (1971) flags
  this class of feature as not phoneme-level simulable, so it is not encoded.
- **No betacism**: /v/ and /b/ stay distinct (unlike the northern dialects).

## Note on the ep_dialects gold

The bundled `ep_dialects` expert set is a light, near-standard read that never
uses [y]; it therefore does not reward the fronting rule. Its PER moves
0.3134 → 0.3152 (+0.0018, within the 0.005 CI epsilon) from a **single**
sentence ("O Algarve é turístico") where the harness feeds the whole sentence
to the word-level `transcribe_word` and the space-separated syllabifier
mis-assigns stress to the /u/ of *turístico*. Transcribed per word the feature
is correct (`turístico` → [tuˈɾiʃtiku], no fronting). Kept and documented per
the honesty gate — the divergence is a limit of the sentence-level gold path,
not of the cited rule.

## Sources

- **Cintra, L. F. Lindley (1971)**. *Nova proposta de classificação dos
  dialectos galego-portugueses*. Boletim de Filologia 22: 81–116.
  <https://cvc.instituto-camoes.pt/hlp/biblioteca/novaproposta.pdf>
- **Brissos, Fernando (2014)**. *New insights into Portuguese central-southern
  dialects: understanding their present and past forms through acoustic data
  from stressed vowels*. Journal of Portuguese Linguistics 13(1): 63–115.
  <https://www.clul.ulisboa.pt/files/849/Brissos_2014_comprimido.pdf>
- **Segura da Cruz, Maria Luísa (1989)**. *La palatalisation de [u] dans le
  «Barlavento Algarvio»*. In *Espaces romans* II: 434–456. Grenoble:
  Université Stendhal / ELLUG.
- Mateus, M. H. M. & d'Andrade, E. (2000). *The Phonology of Portuguese*. OUP.
- Cunha, C. & Cintra, L. F. L. (1984). *Nova Gramática do Português
  Contemporâneo*. Sá da Costa.
- Boléo, M. P. (1974). *Estudos de linguística portuguesa e românica*. U. Coimbra.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-PT-x-alentejo](pt-PT-x-alentejo.md), [pt-PT-x-lisbon](pt-PT-x-lisbon.md)*
