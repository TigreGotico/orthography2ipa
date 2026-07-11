# Alto-Minhoto European Portuguese (pt-PT-x-viana) — Phonology Reference

**Code**: `pt-PT-x-viana` | **Family**: Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` (standard, Lisbon-type EP) | **Quality tier**: research
**Sources**: Cintra (1971, *Boletim de Filologia* 22:81–116), Álvarez Pérez
(2014, *Journal of Portuguese Linguistics* 13-1:29–62), Mateus & d'Andrade (2000)

`pt-PT-x-viana` models the European Portuguese of the **Alto Minho** (Viana do
Castelo, Ponte de Lima). Cintra (1971:93) groups it **together with
[Trás-os-Montes](pt-PT-x-trasosmontes.md)** as a single
*grupo transmontano-alto-minhoto* — the conservative Northern varieties that
alone retain the medieval **four-sibilant system**. The two specs share the same
sibilant deltas. It is a **delta** spec: it inherits the whole standard pt-PT
system (unstressed vowel reduction, dark coda /l/, sandhi) via `graphemes_base` /
`allophones_base` and declares only the archaic-Northern deltas.

## Diagnostic features modelled

### 1. Four-sibilant system (Cintra trait 2 — his primary North/South isogloss)

The Alto Minho keeps the medieval **four-way apico-alveolar vs laminal
(predorsodental) sibilant contrast** that the rest of Portugal has collapsed.
Modelled as a positional-grapheme delta on ⟨s⟩ (+ a ⟨ss⟩ grapheme), leaving the
laminal ⟨c, ç, z⟩ series inherited and unmarked (the Mirandese/`mwl` notation
convention):

| Grapheme (position) | Sibilant | IPA | Example |
|:---|:---|:---|:---|
| ⟨s⟩ initial, ⟨ss⟩ | voiceless **apico-alveolar** | **[s̺]** | sal → **ˈs̺aɫ**, passo → **ˈpas̺u** |
| ⟨s⟩ word-final | voiceless **apico-alveolar** | **[s̺]** | anos → **ˈɐnus̺** |
| ⟨-s-⟩ intervocalic | voiced **apico-alveolar** | **[z̺]** | casa → **ˈkaz̺ɐ** |
| ⟨c⟩(e/i), ⟨ç⟩ | voiceless **laminal** | [s] | paço → **ˈpasu**, cinco → **ˈsinku** |
| ⟨z⟩ | voiced **laminal** | [z] | cozer → kuˈzeɾ |

The diagnostic **minimal pairs stay distinct**: `passo` [ˈpas̺u] ≠ `paço` [ˈpasu];
`coser` [kuˈz̺eɾ] ≠ `cozer` [kuˈzeɾ].

Cintra (1971:93): *"a existência de um sistema de quatro sibilantes — [s̺] e [z̺]
ápicoalveolares (correspondentes aos grafemas s e ss) … opondo-se … ao [s] e o
[z] predorsodentais (correspondentes aos grafemas ce,i, ç e z)"*; note 29 (footnote to the p.93 discussion)
fixes the positions: *"[s̺] ápico-alveolar (correspondente a s inicial e final e
ss interior) … [z̺] ápicoalveolar (correspondente ao s intervocálico)"*. Álvarez
Pérez (2014:37, §4) confirms from ALEPG data that the conservative four-sibilant
system is precisely *"the group of dialects that Cintra called Transmontanos and
Alto-Minhotos"*, and gives the same grapheme/etymology mapping used here.

**Notation.** Cintra's own term is *apico-alveolar* / *"reverso"*; his [s̺]/[z̺]
are commonly rendered **[ʂ]/[ʐ]** in modern IPA (the *"s beirão"/"reverso"* is
acoustically retroflex-like), recorded as the surface variant in `allophones` —
but the Cintra symbols [s̺]/[z̺] are used as the default.

**Limit.** Preconsonantal coda ⟨s⟩ (`festa`, `gosto`) keeps the inherited pan-EP
*chiado* [ʃ]: Cintra's note 29 lists the [s̺] positions as *"s inicial e final e
ss interior"* only, so the preconsonantal palatalisation is left inherited.

### 2. Northern betacism — /v/ ~ /b/ merger (Cintra trait 1)

The /v/ ~ /b/ opposition is lost; both merge into /b/. Cintra (1971:87):
*"o desaparecimento da oposição fonológica entre os fonemas /v/ e /b/ e a sua
fusão num fonema único /b/, realizado ora como oclusiva, ora como fricativa (ou
espirante) b ou β"*. Modelled as allophone rule `PT_NORTH_BETACISM` (`/v/ → [b]`,
the [β] spirant variant recorded in `allophones`).

| Word | pt-PT | pt-PT-x-viana |
|:---|:---|:---|
| vinho | ˈviɲu | **ˈbiɲu** |
| vaca | ˈvakɐ | **ˈbakɐ** |
| estava | eˈʃtavɐ | **eˈʃtabɐ** |

Attested in the CLUP Alto-Minho gold (`vou → bow`, `ver → beɾ`).

### 3. Archaic ⟨ch⟩ affricate (Cintra trait 3)

The syllable-onset /tʃ/–/ʃ/ contrast is **preserved**: ⟨ch⟩ = [tʃ] vs ⟨x⟩ = [ʃ].
Cintra (1971:87): *"a permanência da distinção fonológica em posição inicial de
sílaba entre o fonema /tʃ/, representado pelo grafema ch e o fonema /ʃ/
representado pelo grafema x"*. Modelled as a grapheme delta (⟨ch⟩ → [tʃ]):
`chave → ˈtʃabɨ`.

## Not modelled (deliberately)

Porto's tonic-close-vowel diphthongisation ([e]→[je], [o]→[wo]) is a
*Baixo-Minho / Douro-Litoral* feature; Cintra (1971:93) places it in the *other*
northern group, so it is **not applied** to the transmontano-alto-minhoto
varieties.

```python
from orthography2ipa import G2P
eng = G2P("pt-PT-x-viana")
eng.transcribe_word("passo")   # ˈpas̺u   — apico [s̺]
eng.transcribe_word("paço")    # ˈpasu    — laminal [s]  (minimal pair)
eng.transcribe_word("casa")    # ˈkaz̺ɐ   — intervocalic [z̺]
eng.transcribe_word("vinho")   # ˈbiɲu    — betacism
eng.transcribe_word("chave")   # ˈtʃabɨ   — archaic ⟨ch⟩ affricate + betacism
```

## Benchmark

`clup_dialect` (`pt-PT-x-viana`) is a **tiny (n=4), sentence-level** gold from the
U.Porto CLUP archive with undocumented IPA-column provenance, so correctness
rests on the cited sources, not the noisy PER. The character-level PER rises
(0.4666 → 0.4984) because the gold renders the apico-alveolar series
inconsistently ([ʃ], [ʂ], plain [s]) while the spec emits Cintra's [s̺]/[z̺]; the
four-sibilant contrast is the correct, source-grounded model and is kept per the
honesty gate.

## Sources

- **Cintra, L. F. Lindley (1971).** *Nova proposta de classificação dos
  dialectos galego-portugueses.* Boletim de Filologia (Centro de Estudos
  Filológicos, Lisboa) 22: 81–116. (Republished in *Estudos de Dialectologia
  Portuguesa*, Sá da Costa, 1983, pp. 117–163.)
- **Álvarez Pérez, Xosé Afonso (2014).** *European Portuguese dialectal
  features: a comparison with Cintra's proposal.*
  Journal of Portuguese Linguistics 13(1): 29–62.
  [doi:10.5334/jpl.62](https://doi.org/10.5334/jpl.62)
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.
