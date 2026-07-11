# Micaelense European Portuguese (pt-PT-x-sao-miguel) — Phonology Reference

**Code**: `pt-PT-x-sao-miguel` | **Family**: Indo-European > Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` (standard, Lisbon-type EP) | **Quality tier**: research
**Sources**: Portuguese With Leo, "Sotaque e expressões dos Açores – São Miguel" + "The 8 accents" (native-speaker, **not** academic); Rogers (1948); Segura (2013)

`pt-PT-x-sao-miguel` models the European Portuguese of **São Miguel** (Azores),
the eastern-Azorean *micaelense* micro-variety — the most idiosyncratic and
stereotyped Azorean accent. It is split out from the general
[pt-PT-x-acores](pt-PT-x-acores.md) node (which stays the general / other-islands
node, **Terceira** as its gold reference) so the micro-variety can be modelled
precisely without moving the Azorean gold. It is a **delta** over the broad
`pt-PT` base.

## Diagnostic features modelled

### 1. Stressed open-syllable /u/ → [y] fronting

The single most stereotyped micaelense trait — the one that makes the accent
*"sound French"* (`SM_U_KEEP_BEFORE_CODA` then `SM_U_FRONTING`):

| Word | pt-PT | pt-PT-x-sao-miguel |
|:---|:---|:---|
| número | ˈnumɨɾu | ˈn**y**mɨɾu |
| tu | ˈtu | ˈt**y** |
| azul (blocked before coda) | ɐˈzuɫ | ɐˈz**u**ɫ |

Catarina: *"o u faz com que pareça realmente um sotaque assim muito francês … é
a nossa característica, é o û"*. Categorical here (vs the Terceira gold's
`[ˈmudɐ]`, São Miguel `[ˈmydɐ]`). The article/contraction clitics are pinned in
`word_exceptions` so a proclitic *o/do/no/ao* is `[u]`, never `[y]`.

### 2. Intervocalic /l/ → [ʎ] after /i/

Same environment as [pt-PT-x-madeira](pt-PT-x-madeira.md) (`SM_L_PALATALISATION`):

| Word | pt-PT | pt-PT-x-sao-miguel |
|:---|:---|:---|
| quilo | ˈkilu | ˈki**ʎ**u |
| Filipa | fiˈlipɐ | fiˈ**ʎ**ipɐ |
| mochila | muˈʃilɐ | muˈʃi**ʎ**ɐ |

**Honesty note.** This feature is sourced from the 8-accents overview (São
Miguel grouped with Madeira, *Filipa → "Flhipa"*) and **not** demonstrated in the
São Miguel deep-dive itself; it is corroborated by the Madeira deep-dive (where
the `-il → -ilh` process is strongly attested: *quilómetro → "quilhómetro"*) and
by Segura (2013) for the Atlantic islands. The gate is exact — /l/ after any
other front vowel is untouched (teleférico → tɨlɨˈfɛɾiku).

### 3. `[ʒ]` prevocalic external /s/-sandhi

Shared with the Algarve (re-declaring `PT_FINAL_S_PREVOCALIC_VOICE` → `ʒ`):
estás a ver → eˈʃta**ʒ** ˈɐ ˈvɛɾ. Overview: the shared Algarvean-Azorean J,
*"quijentrar", "Todojos", "Éjunúmerúm"* (és o número um).

## Deliberately inherited: "coêlho" (not "coâlho")

São Miguel keeps the **non-centralised** mid vowel before a palatal —
coelho → **ˈkɔɛʎu** ("coêlho") — where Lisbon centralises to `[ɐ]` (ˈkoɐʎu,
"coâlho") and Madeira likewise has "coâlho". The São Miguel *coêlho* vs the
Madeiran *coâlho* is the classic island-distinguishing minimal contrast
(8-accents overview).

## Not modelled

The very closed o/u vowels (gradient); the **variable** singular ⟨ão⟩ →
monophthong nasal `[ɐ̃]` (cão → *"cã"*, ladrão → *"ladrã"* — *"às vezes"*; a
blanket rule would wrongly hit são → `[sɐ̃w]`); the word-final **-R deletion** in
verbs (comer → *"comê"*, passear → *"passeá"* — cannot be gated to infinitives
from orthography without also dropping /r/ in mar/cor); *"non"* for não; the
heavy gerund preference and the Anglo-Azorean *calafão* loan vocabulary
(lexical / morphosyntactic).

## Try it

```python
from orthography2ipa.g2p import G2P
eng = G2P("pt-PT-x-sao-miguel")
eng.transcribe("número")      # ˈnymɨɾu  — /u/ → [y]
eng.transcribe("quilo")       # ˈkiʎu    — /l/ → [ʎ] after /i/
eng.transcribe("coelho")      # ˈkɔɛʎu   — "coêlho", mid vowel kept
eng.transcribe("azul")        # ɐˈzuɫ    — fronting blocked before coda
```

## Sources

- **Portuguese With Leo (with Catarina).** *Sotaque e expressões dos Açores –
  São Miguel.* YouTube (native-speaker, **not** academic).
  <https://www.youtube.com/watch?v=6IqeBcjK_fk>
- **Portuguese With Leo.** *The 8 Portuguese accents of Portugal.*
  <https://www.youtube.com/watch?v=pitj0XxYO7I>
- **Rogers, Francis M. (1948).** *Insular Portuguese Pronunciation: Porto Santo
  and Eastern Azores.* Hispanic Review 16(1), 1–32.
- **Segura, Luísa (2013).** *Variedades dialetais do português europeu.* In
  *Gramática do Português*, vol. I, 85–142.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-PT-x-acores](pt-PT-x-acores.md), [pt-PT-x-madeira](pt-PT-x-madeira.md), [pt-PT-x-algarve](pt-PT-x-algarve.md)*
