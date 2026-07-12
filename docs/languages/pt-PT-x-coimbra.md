# Conimbricense European Portuguese (pt-PT-x-coimbra) — Phonology Reference

**Code**: `pt-PT-x-coimbra` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` (standard, Lisbon-type EP) | **Quality tier**: research
**Sources**: Portuguese With Leo, "Coimbra tem sotaque?" (native-speaker, **not** academic); Cintra (1971); Mateus & d'Andrade (2000)

`pt-PT-x-coimbra` models the European Portuguese of **Coimbra**, the central
variety widely called *"o sotaque mais neutro de Portugal"*. It is a **delta**
spec over the broad `pt-PT` base. Its defining property is **conservatism**: it
keeps the base values that Lisbon/Estremenho innovates away from, and adds only
one marked local delta — the `[ʒ]` prevocalic external /s/-sandhi.

## The one modelled delta: `[ʒ]` prevocalic /s/-sandhi

A word-final coda /s/ before a vowel-initial following word is realised as the
post-alveolar **`[ʒ]`** (re-declaring `PT_FINAL_S_PREVOCALIC_VOICE` with
transform `ʒ`), where the `pt-PT` base has `[z]`:

| Phrase | pt-PT | pt-PT-x-coimbra |
|:---|:---|:---|
| os olhos | ˈoz ˈoʎuʃ | **ˈoʒ ˈoʎuʃ** |
| estás a ver | eˈʃtaz ˈɐ ˈvɛɾ | eˈʃta**ʒ** ˈɐ ˈvɛɾ |

**Variable, `[ʒ]`-pole.** The centre is genuinely variable `[z]`~`[ʒ]`. The
Coimbra speaker Lúcio (*conimbricense de gema*) answers, asked how he links "os
olhos": *"Nós faríamos a junção com o som de J"* — while the Lisbon host uses
`[z]`; Lúcio also says *"esta é uma coisa que varia muito"*. The spec models the
marked local `[ʒ]` pole. The standard/Lisbon literature gives `[z]` (Mateus &
d'Andrade 2000: ch.2); no page-pinned academic source for the Coimbra
prevocalic `[ʒ]` was located.

## Deliberately inherited (Coimbra diverges by *not* innovating)

Coimbra keeps the base values; it is distinguished from Lisbon precisely by the
**absence** of the Lisbon innovations:

| Feature | Coimbra (= base) | Lisbon |
|:---|:---|:---|
| stressed ⟨e⟩ before a palatal | coelho → **ˈkɔɛʎu** ("coêlho", mid vowel) | ˈko**ɐ**ʎu ("coâlho", `[ɐ]`) |
| ⟨ei⟩ | fevereiro → …ˈɾ**ej**ɾu (`[ej]`) | …ˈɾ**ɐj**ɾu (`[ɐj]`) |
| ⟨ou⟩ | pouco → ˈp**o**ku (monophthong) | ˈp**o**ku |
| unstressed /i/ | Filipa → f**i**ˈlipɐ (retained) | "Flipa" (deleted) |

The Coimbra guest calls the pre-palatal `[e]` words (coelho, espelho,
vermelho, Fonte da Telha) *"das coisas que mais distinguem o sotaque de Coimbra
do sotaque de Lisboa"*, saying Coimbra *"fala da forma que teoricamente é o
correto"*. The `[ej]` value is described as intermediate between Lisbon `[ɐj]`
(*"menos A"*) and the very strong Porto `[ej]` (*"não tanto E"*). The
conservative pre-palatal `[e]` is corroborated for the neighbouring North by the
[Trás-os-Montes](pt-PT-x-trasosmontes.md) speaker (*"vermelho eu digo vermelho,
Lisboa vermalho"*).

## Not modelled

The **OI~OU lexical doublet** preference (Coimbra *toiro / loiça / loiro* where
Lisbon prefers *touro / louça*) is an orthographic-lexical choice, not a regular
grapheme rule, and is left to the lexicon.

## Try it

```python
from orthography2ipa.g2p import G2P
eng = G2P("pt-PT-x-coimbra")
eng.transcribe("os olhos")    # ˈoʒ ˈoʎuʃ   — [ʒ] prevocalic sandhi
eng.transcribe("coelho")      # ˈkɔɛʎu       — mid vowel kept (not Lisbon [ɐ])
eng.transcribe("fevereiro")   # fɨvɨˈɾejɾu   — [ej] kept
eng.transcribe("Filipa")      # fiˈlipɐ      — unstressed /i/ retained
```

## Sources

- **Portuguese With Leo (with Lúcio).** *Coimbra tem sotaque?* YouTube
  (native-speaker / popular-linguistics, **not** academic).
  <https://www.youtube.com/watch?v=R4yUi68VHFg>
- **Cintra, Luís F. Lindley (1971).** *Nova proposta de classificação dos
  dialectos galego-portugueses.* Boletim de Filologia 22, 81–116.
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-PT-x-lisbon](pt-PT-x-lisbon.md), [pt-PT-x-porto](pt-PT-x-porto.md), [pt-PT-x-trasosmontes](pt-PT-x-trasosmontes.md)*
