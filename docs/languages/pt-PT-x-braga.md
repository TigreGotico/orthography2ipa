# Bracarense European Portuguese (pt-PT-x-braga) — Phonology Reference

**Code**: `pt-PT-x-braga` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` (standard, Lisbon-type EP) | **Quality tier**: research
**Sources**: Portuguese With Leo, "Sotaque e expressões de Braga" + "The 8 accents" (native-speaker, **not** academic); Cintra (1971); Segura (2013)

`pt-PT-x-braga` models the European Portuguese of **Braga** (Minho), a Northern
variety of Cintra's **Baixo-Minho / Douro-Litoral** diphthongisation zone,
described natively as **heavier / more strongly Northern than Porto**. It is a
**delta** spec over the broad `pt-PT` base.

## Diagnostic features modelled

### 1. Northern betacism — /v/ → [b] (~[β])

The /v/~/b/ opposition is lost; both merge in /b/, surfacing as the stop `[b]`
or the softer spirant `[β]`. Modelled as the post-lexical allophone rule
**`BRA_BETACISM`**:

| Word | pt-PT | pt-PT-x-braga |
|:---|:---|:---|
| vaca | ˈvakɐ | **ˈbakɐ** |
| vou | ˈvow | **ˈbow** |
| vacina | vɐˈsinɐ | **bɐˈsinɐ** |

The Braga speaker Miguel: *"pões o B em vez do V … às vezes é um B mais
pronunciado, outras vezes é um B mais suave tipo Bou"*; *"no norte diz-se
bácina"* (vacina). Cintra (1971:87) grounds the merger, *"realizado ora como
oclusiva, ora como fricativa (ou espirante) b ou β"*.

### 2. Tonic-close-vowel diphthongisation — [e] → [je], [o] → [wo]

The Cintra Baixo-Minho marker: a **stressed close** mid vowel becomes a rising
diphthong (`BRA_DIPHTHONGISE_E` / `BRA_DIPHTHONGISE_O`):

| Word | pt-PT | pt-PT-x-braga |
|:---|:---|:---|
| mês | ˈmeʃ | **ˈmjeʃ** |
| ele | ˈelɨ | ˈ**je**lɨ |
| avô | ɐˈvo | ɐˈb**wo** |

Natively attested via *"o quê → o quiê"* (quê `[ke]` → `[kje]`) and *"mieu"*
(meu) in the 8-accents overview. **Limit** (shared with
[pt-PT-x-porto](pt-PT-x-porto.md)): gated to the close `[e]`/`[o]`; because
open/close for spelling-unmarked stressed ⟨e⟩/⟨o⟩ is lexical and the base map
defaults to the *open* allophone, underlying-close words the engine transcribes
open (cedo, medo) escape the rule — widening to `[ɛ]`/`[ɔ]` would wrongly
diphthongise genuinely open vowels (café, avó) and is rejected.

### 3. Diphthong preservation — ⟨ou⟩ → [ow], ⟨ei⟩ → [ej]

Kept where Lisbon monophthongises/lowers (`[o]`, `[ɐj]`): pouco → ˈp**ow**ku,
fevereiro → …ˈɾ**ej**ɾu. Miguel: *"tu dizes OU, dizes vOU ou bOU"*.

## Not modelled

The northern **open vowels** and **prosodic lengthening** for emphasis (*"abres
mais o A em cantÁdo"*, *"mais musical, mais cantado"*), the variable word-final
**paragogic -r** in -ar verbs (*"Faláre", "gostarE"* — *"já não foi tanto"*),
the *"beim"* (bem) nasal detail, and the morphosyntactic *"vós ides / vinde /
ide"* are documented but not encoded (gradient / lexical / non-phonological).

## Try it

```python
from orthography2ipa.g2p import G2P
eng = G2P("pt-PT-x-braga")
eng.transcribe("vaca")        # ˈbakɐ   — betacism
eng.transcribe("mês")         # ˈmjeʃ   — close [e] → [je]
eng.transcribe("avô")         # ɐˈbwo   — close [o] → [wo] (+ betacism)
eng.transcribe("pouco")       # ˈpowku  — ⟨ou⟩ → [ow] preserved
```

## Sources

- **Portuguese With Leo (with Miguel).** *Sotaque e expressões de Braga.*
  YouTube (native-speaker, **not** academic).
  <https://www.youtube.com/watch?v=xaen3F8256M>
- **Portuguese With Leo.** *The 8 Portuguese accents of Portugal.*
  <https://www.youtube.com/watch?v=pitj0XxYO7I>
- **Cintra, Luís F. Lindley (1971).** *Nova proposta de classificação dos
  dialectos galego-portugueses.* Boletim de Filologia 22, 81–116.
- **Segura, Luísa (2013).** *Variedades dialetais do português europeu.* In
  *Gramática do Português*, vol. I, 85–142.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-PT-x-porto](pt-PT-x-porto.md), [pt-PT-x-trasosmontes](pt-PT-x-trasosmontes.md), [pt-PT-x-minho](pt-PT-x-minho.md)*
