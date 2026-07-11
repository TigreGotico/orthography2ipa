# Alentejano Portuguese (pt-PT-x-alentejo) — Phonology Reference

**Code**: `pt-PT-x-alentejo` | **Family**: Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Parent**: `pt-PT`
**Sources**: Cintra (1971, *Boletim de Filologia* 22: 81–116), Brissos (2014,
*Journal of Portuguese Linguistics* 13(1): 63–115), Mateus & d'Andrade (2000),
Cunha & Cintra (1984), Boléo (1974)

Alentejano is the central-southern European Portuguese dialect of the Alto
Alentejo (Portalegre, Évora, Beja). It inherits the full pt-PT base —
including the standard's strong unstressed vowel reduction and the post-lexical
`allophone_rules` (dark coda /l/, coda-sibilant chiado) — and declares only its
own deltas. See [../allophony.md](../allophony.md) for the two-maps model.

## The defining feature: stressed /u/ → [y] palatalisation

Cintra (1971) delimits the Beira-Baixa / Alto-Alentejo zone by a single
isogloss — the palatalisation of the stressed /u/, part of a whole-system
timbre shift ("uma profunda alteração de timbre de todo o sistema vocálico,
principalmente do tónico"):

> "a palatalização, em maior ou menor grau, da vogal tónica u" — Cintra (1971,
> p. 14 of the CVC reflow)

Cintra writes the explicit IPA value [y] for the neighbouring Barlavento
Algarvio of the *same* "reacção em cadeia" ("a palatalização da lábio-velar
[u] em [y]"), and records the Alto-Alentejo tonic *u* as palatalised "ü" in his
note 56; [y] is its phonetic value. The rule is restricted to the **stressed
nucleus**, so unstressed /u/ (e.g. `turistas`) is untouched.

A **proclitic guard** (`word_exceptions`) keeps the common monosyllabic clitics
— `o/os/no/nos/do/dos/ao/aos/pelo/pelos/um/uns` — on their [u] vowel, because
the word-level stress detector otherwise mis-marks them as stressed and would
front the article/contraction vowel to [y].

## Final unstressed high-vowel deletion

The region also deletes final unstressed high vowels -u/-i/-e. The primary
source is Brissos (2014), an acoustic study of central-southern EP ("Final
unstressed [u] disappears or is reduced to [ɨ]", e.g. [sˈœʃt] *cesto*).

> Cintra (1971) mentions this only in **note 58** (p. 27), where he is
> summarising **Lüdtke (1956/57)** — "a queda das vogais finais -u, -i (ou -e),
> outro dos fenómenos mais típicos desta região, mas cujos limites não
> coincidem perfeitamente com os dos primeiros" — expressly noting its
> isoglosses do not coincide with the zone's defining feature. It is therefore
> **not** one of Cintra's own diagnostics and is not cited as such.

In pt-PT the final unstressed vowels surface as [u] (from graphic ⟨o/u⟩) and
[ɨ] (from ⟨e⟩); this rule drops them word-finally. Final /ɐ/ (from ⟨a⟩) is
**spared**, matching the sources, which list only final -u, -i, -e.

### Post-lexical allophony (allophone_rules)

| id | Process | Rule | Example |
|:---|:---|:---|:---|
| `ALE_U_FRONTING` | Stressed /u/ fronting | /u/ → [y] / stressed nucleus | `sul` [ˈsyɫ], `lume` [ˈlym] |
| `ALE_FINAL_HIGH_VOWEL_DELETION` | Final high-vowel deletion | /u i ɨ/ → ∅ / unstressed _# | `gosto` [ˈɡɔʃt], `noite` [ˈnojt] |

`ALE_U_FRONTING` fires only on the **stressed nucleus**, so unstressed /u/ is
left as [u] (`turistas` [tuˈɾiʃtɐʃ]) and the guarded clitics keep [u] (`o`
[ˈu], `no` [ˈnu]). `ALE_FINAL_HIGH_VOWEL_DELETION` is conditioned on
**word-final + unstressed**, so it never touches a stressed final vowel
(`café` [kɐˈfɛ]) nor a word-medial vowel; the low final /ɐ/ is excluded
(`calma` [ˈkaɫmɐ]).

```python
from orthography2ipa import G2P
G2P("pt-PT-x-alentejo").transcribe("sul")    # ˈsyɫ   (stressed /u/ -> [y])
G2P("pt-PT-x-alentejo").transcribe("o")      # ˈu     (proclitic guard)
G2P("pt-PT-x-alentejo").transcribe("gosto")  # ˈɡɔʃt  (final vowel deleted)
G2P("pt-PT-x-alentejo").transcribe("calma")  # ˈkaɫmɐ (final ɐ kept)
```

## Other modelled features (inherited or delta)

| Process | Where | Example |
|:---|:---|:---|
| Intervocalic /d/ deletion | `positional_graphemes` delta | `nada` [ˈnaɐ], `vida` [ˈviɐ] |
| /ej/ → [e] monophthong | `graphemes` delta | `leite` [ˈletɨ] |
| /ow/ → [o] monophthong | `graphemes` delta | `outro` [ˈotɾu] |
| meu-class /ew/ → [e] | `graphemes` delta | `meu` [me] |
| Dark coda /l/ → [ɫ] | inherited `allophone_rules` | `sol` [ˈsɔɫ] |
| Coda /s/ → [ʃ] (chiado) | inherited `allophone_rules` | `gosto` [ˈɡɔʃt] |

## Divergence from the ep_dialects gold (honest note)

The bundled `ep_dialects` expert gold (n=30) is a light, near-standard read
that transcribes final vowels **in full** and does not encode the /u/-fronting
or the final-vowel deletion, so `ALE_U_FRONTING` and
`ALE_FINAL_HIGH_VOWEL_DELETION` slightly *lower* agreement with that small-n,
unvalidated set (PER 0.3155 → 0.3174, within the bootstrap CI) while being the
cited, linguistically-correct realisations. Per the honesty gate these are kept
and documented, not tuned away — the divergence is a limit of the gold, not of
the rules. The same holds for the inherited dark-l and intervocalic-/d/
behaviours where the gold uses a clear [l] / retained [d].

## Sources

- **Cintra, L. F. Lindley (1971)**. *Nova proposta de classificação dos
  dialectos galego-portugueses*. Boletim de Filologia 22: 81–116.
  <https://cvc.instituto-camoes.pt/hlp/biblioteca/novaproposta.pdf>
- **Brissos, Fernando (2014)**. *New insights into Portuguese central-southern
  dialects: understanding their present and past forms through acoustic data
  from stressed vowels*. Journal of Portuguese Linguistics 13(1): 63–115.
  <https://www.clul.ulisboa.pt/files/849/Brissos_2014_comprimido.pdf>
- Mateus, M. H. M. & d'Andrade, E. (2000). *The Phonology of Portuguese*. OUP.
- Cunha, C. & Cintra, L. F. L. (1984). *Nova Gramática do Português
  Contemporâneo*. Sá da Costa.
- Boléo, M. P. (1974). *Estudos de linguística portuguesa e românica*. U. Coimbra.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-PT-x-algarve](pt-PT-x-algarve.md), [pt-PT-x-lisbon](pt-PT-x-lisbon.md)*
