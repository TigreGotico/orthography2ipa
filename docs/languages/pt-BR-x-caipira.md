# Caipira Portuguese (pt-BR-x-caipira) — Phonology Reference

**Code**: `pt-BR-x-caipira` | **Family**: Romance | **Script**: Latin (alphabet)
**Parent**: `pt-BR` (Brazilian standard) | **Quality tier**: research
**Sources**: Amaral (1920, *O Dialeto Caipira*), Castilho (2010), Mateus &
d'Andrade (2000), Callou & Leite (2001), Silva (2002)

`pt-BR-x-caipira` models the **Caipira** speech of the São Paulo interior,
western Minas Gerais, Goiás, Mato Grosso, Mato Grosso do Sul and the Paraná
hinterland. It is a **delta** spec: it inherits the whole pt-BR base
(`graphemes_base` / `allophones_base` / `positional_graphemes_base` = `pt-BR`)
and overrides only the diagnostic Caipira features.

The foundational description is Amadeu Amaral's *O Dialeto Caipira* (1920) —
the first systematic dialectological monograph on a Brazilian variety. The
features below are page-cited (by Amaral's numbered sections) to the full
text, read directly.

## Diagnostic features modelled

### 1. The retroflex "r caipira" — coda /r/ → [ɻ] (Amaral §6b)

The hallmark of the dialect. Amaral (1920) §6b:

> *"r inter e post-vocálico (arara, carta) possui um valor peculiar: é
> linguo-palatal e guturalizado. Na sua prolação … a língua … vira a
> extremidade para cima, sem tocá-la na abóbada palatal. Não há quase nenhuma
> vibração tremulante. Para o ouvido, este r caipira assemelha-se bastante ao
> r inglês post-vocálico."*

That is a **non-trilled retroflex approximant** — a tongue-tip curled up
without contact, acoustically like English post-vocalic /r/ — modelled as
[ɻ]. It is declared in `positional_graphemes.r` at `before_consonant`, `coda`
and `word_final`.

| Word | pt-BR | pt-BR-x-caipira |
|:---|:---|:---|
| porta | ˈpoɾtɐ | **ˈpoɻtɐ** |
| carta | ˈkaɾtɐ | **ˈkaɻtɐ** |
| mar | ˈmaɾ | **ˈmaɻ** |

Intervocalic weak /r/ stays a **tap** ([ˈkaɾu] *caro*); the strong onset
rhotic stays dorsal/glottal ([ˈhatu] *rato*). Word-final /r/ optionally
elides — Amaral §23a: *"Cai, quando final de palavra: andá, muié, esquecê,
subi, vapô"* — declared as `word_final: [ɻ, ""]`.

> **Note on vowel quality.** Amaral cites *porta* with an open [ɔ]. Open-mid
> tonic vowels of unmarked ⟨o⟩/⟨e⟩ are **lexical and not predictable from
> spelling**, so the engine derives the close [o] (→ [ˈpoɻtɐ]). The retroflex
> — the Caipira feature — is derived correctly; the vowel is a documented
> engine limit, not a Caipira claim.

### 2. Coda /l/ rhotacism (Amaral §22a) — traditional [ɻ] variant

Amaral §22a: *"l - Em final de sílaba, muda-se em r: quarquér, papér, mér,
arma."* Traditional rural Caipira turns coda /l/ into the same rhotic and
hence the retroflex. Modern urban Caipira, however, has adopted the general
pt-BR vocalisation to [w] (*sol* → [ˈsow]). The spec therefore keeps **[w] as
the primary coda-/l/ realisation** and declares **[ɻ] as the traditional
Amaral variant** in `positional_graphemes.l`, so no false modern claim is made
while the documented historical form is retained.

### 3. Laminodental coda /s/ — no *chiado* (Amaral §6a)

Amaral §6a: *"s propriamente sibilante, assobiado, e bem assim chiante, são
aqui desconhecidos."* Coda /s/ is a plain alveolar [s] (*mesmo* → [ˈmesmu],
*costas* → [ˈkostas]) — never the Carioca palatal [ʃ]/[ʒ].

### 4. /ʎ/ vocalisation (Amaral §25, §6e)

Amaral §25: *"lh - Vocaliza-se em i: espaiado, maio, muié"*; §6e: the palatal
lateral *"não existe no dialeto"*. Modelled as the allophone ʎ → [j].

## Inherited from pt-BR (unchanged)

/t d/ palatalisation before /i/ (*tia* → [ˈt͡ʃiɐ], *dia* → [ˈd͡ʒiɐ]), final
unstressed vowel reduction, and coda /l/ vocalisation to [w] are inherited and
not restated.

## Known limits (documented, not faked)

**Historical vowel retention.** Amaral §8 records that early-20c rural Caipira
did **not** raise final unstressed /e/→[i] or /o/→[u]: *"Não se operou aqui a
permuta de e final por i … como não se operou a de o por u."* Modern Caipira
has since aligned with general pt-BR raising, which the spec inherits; the
1920 divergence is documented here rather than modelled.

**Lexical open-mid vowels** (the [ɔ] of *porta*) are not derivable — see the
note above.

```python
from orthography2ipa import G2P
eng = G2P("pt-BR-x-caipira")
eng.transcribe_word("porta")   # ˈpoɻtɐ  — retroflex before consonant
eng.transcribe_word("mar")     # ˈmaɻ    — retroflex word-final
eng.transcribe_word("caro")    # ˈkaɾu   — intervocalic tap, not retroflex
eng.transcribe_word("mesmo")   # ˈmesmu  — coda /s/ alveolar, no chiado
```

## Sources

- **Amaral, Amadeu (1920).** *O Dialeto Caipira.* Casa Editora "O Livro", São
  Paulo. (§6a–b retroflex /r/ and laminodental /s/; §8 vowel retention; §22a
  coda /l/ rhotacism; §23a final-/r/ elision; §25 /ʎ/ vocalisation.)
- **Castilho, Ataliba T. (2010).** *Nova Gramática do Português Brasileiro.*
  Contexto.
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.
- **Callou, D. & Leite, Y. (2001).** *Iniciação à fonética e à fonologia*
  (8th ed.). Zahar.
- **Silva, T. C. (2002).** *Fonética e fonologia do português.* Contexto.
