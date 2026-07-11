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

## The defining feature: final unstressed high-vowel deletion

Cintra (1971) lists the deletion of final unstressed high vowels as one of the
most typical features of the region:

> "a queda das vogais finais -u, -i (ou -e), outro dos fenómenos mais típicos
> desta região" — Cintra (1971)

Brissos (2014) confirms it acoustically ("Final unstressed [u] disappears or is
reduced to [ɨ]", e.g. [sˈœʃt] *cesto*). In pt-PT the final unstressed vowels
surface as [u] (from graphic ⟨o/u⟩) and [ɨ] (from ⟨e⟩); this rule drops them
word-finally. Final /ɐ/ (from ⟨a⟩) is **spared**, matching the source, which
lists only final -u, -i, -e.

### Post-lexical allophony (allophone_rules)

| id | Process | Rule | Example |
|:---|:---|:---|:---|
| `ALE_FINAL_HIGH_VOWEL_DELETION` | Final high-vowel deletion | /u i ɨ/ → ∅ / unstressed _# | `gosto` [ˈɡɔʃt], `noite` [ˈnojt] |

Conditioned on **word-final + unstressed**, so it never touches a stressed
final vowel (`café` keeps its [ɛ]) nor a word-medial vowel; and the low final
/ɐ/ is excluded (`calma` [ˈkaɫmɐ]).

```python
from orthography2ipa import G2P
G2P("pt-PT-x-alentejo").transcribe_word("gosto")  # ˈɡɔʃt
G2P("pt-PT-x-alentejo").transcribe_word("noite")  # ˈnojt
G2P("pt-PT-x-alentejo").transcribe_word("calma")  # ˈkaɫmɐ  (final ɐ kept)
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
that transcribes final vowels **in full** and does not encode Cintra's
deletion, so `ALE_FINAL_HIGH_VOWEL_DELETION` *lowers* agreement with that
small-n, unvalidated set (PER 0.2941 → 0.3155) while being the cited,
linguistically-correct realisation. Per the honesty gate this is kept and
documented, not tuned away — the divergence is a limit of the gold, not of the
rule. The same holds for the inherited dark-l and intervocalic-/d/ behaviours
where the gold uses a clear [l] / retained [d].

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
