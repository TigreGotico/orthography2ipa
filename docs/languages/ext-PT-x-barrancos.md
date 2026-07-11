# Barranquenho (ext-PT-x-barrancos) — Phonology Reference

**Code**: `ext-PT-x-barrancos` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` | **Quality tier**: research | **Glottolog**: `barr1235`
**Sources**: Navas Sánchez-Élez (2011), *El barranqueño: un modelo de lenguas en contacto*; Clements, Amaral & Luís (2008, *BLS* 34); Convenção Ortográfica do Barranquenho (2025); Gramática Básica de Barranquenho (Gonçalves, Navas & Correia, 2025)

Barranquenho is the contact vernacular of Barrancos (Baixo Alentejo, Portugal),
spoken by roughly 1,600–2,000 people and listed by UNESCO as *definitely
endangered*. It is not a plain Portuguese dialect: Barrancos is surrounded on
three sides by the Spanish province of Huelva (Andalusia) and borders
Extremadura, and the variety is a genuine **contact language** — an Alentejo
European Portuguese base with a pervasive **Extremaduran/Andalusian Spanish
adstrate** (Navas Sánchez-Élez 2011; Clements, Amaral & Luís 2008). Modelling it
therefore means *overriding* several inherited European Portuguese processes,
not merely adding to them.

---

## Inheritance and the contact overrides

The spec sets `parent = pt-PT` and inherits pt-PT through `graphemes_base`,
`allophones_base` and `positional_graphemes_base`. Because `allophone_rules`
inherit by **OVERLAY_BY_ID** (a child rule with the same `id` replaces the
inherited one in place), Barranquenho would otherwise silently acquire the three
European Portuguese post-lexical rules — the Lisbon *chiado* coda sibilants and
the dark coda /l/. Those are exactly the EP features Barranquenho does **not**
share, so the spec **redeclares their ids to disable them**:

| Inherited EP rule (`id`) | EP surface | Barranquenho override | Why |
|:---|:---|:---|:---|
| `PT_CODA_S_HUSH` | coda /s/ → [ʃ] | → **[h]** | Andalusian-type aspiration, not chiado |
| `PT_CODA_Z_HUSH` | coda /z/ → [ʒ] | → **[h]** | coda sibilants neutralise to the aspirate |
| `PT_CODA_L_DARK` | coda /l/ → [ɫ] | → **[l]** (no-op) | clear alveolar /l/, no velarisation |

## Spanish-substrate / contact features modelled

1. **Coda /s/ (and /z/) aspiration → [h]** — the single most salient contact
   trait, shared with all southern-peninsular (Extremaduran/Andalusian)
   varieties and absent from every Portuguese dialect: *mehmu* (mesmo),
   *Lihboa* (Lisboa), *bihtu* (visto). Modelled both pre-lexically
   (`positional_graphemes` `s`: coda → [h]) and by the overridden allophone rule
   (Navas 2011; Clements et al. 2008; Convenção pp. 28–29).
2. **Word-final /s/, /r/, /l/ deletion** — absolute-final /s/ is silent (and not
   written); tonic final /r/ deletes (*cantá*, *senhô*, *dotô*); tonic final /l/
   deletes (*Brasí*, *Natá*, *Isabé*). Handled pre-lexically by
   `positional_graphemes` `word_final` → ∅ (Convenção pp. 31–32; Gramática
   pp. 19–20; Clements et al. 2008).
3. **Betacism (/v/–/b/ merger)** — ⟨v⟩ → /b/, with intervocalic [β]; /v/ is not
   a phoneme. Shared with Spanish and Northern Portuguese (Navas 2011; Gramática
   p. 17).
4. **Aspirated ⟨h⟩ = /h/** (also [x] in Spanish loans), an alveolar trill /r/
   for word-initial ⟨r⟩ and ⟨rr⟩ (not the EP uvular /ʁ/), and the /tʃ/
   affricate ⟨tch⟩.
5. **Seseo (no /θ/ distinción)** — ⟨c⟩ (before e/i), ⟨ç⟩, ⟨s⟩, ⟨z⟩ all map to
   alveolar sibilants; no Castilian interdental is introduced.
6. **Coda-conditioned nasal vowels** — a vowel before a syllable-final (coda)
   ⟨m/n⟩ nasalises and the nasal consonant is absorbed:
   [ã]←⟨am/an⟩, [ẽ]←⟨em/en⟩, [ĩ]←⟨im/in⟩, [õ]←⟨om/on⟩, [ũ]←⟨um/un⟩
   (*campu* [kɐ̃pu], *lindo* [lĩdu], *bom*/*bon* [bõ], *mundo* [mũdu]) — while an
   **intervocalic (onset)** ⟨m/n⟩ is a syllable onset and leaves the vowel oral
   (*lhano* [ʎanu], *cama* [kamɐ], *pequenu* [pɨkenu]). ⟨em/en⟩ realise the
   plain nasal vowel [ẽ] (not the EP diphthong [ẽj]). Modelled on the nasal
   *consonant* — coda ⟨m/n⟩ → a U+0303 combining tilde on the preceding vowel
   (`positional_graphemes` `m`/`n`: `word_final`/`before_consonant`), which the
   ⟨nh⟩/⟨lh⟩ digraphs pre-empt so they never mis-nasalise (*banho* [baɲu]) — with
   the vowel-quality raising ⟨a⟩→[ɐ̃], ⟨o⟩→[õ] supplied by the `allophone_rules`
   `PT_NASAL_A_RAISE` / `PT_NASAL_O_RAISE` (fire only before the tilde). Coda
   nasal-vowel graphing: Convenção p. 26, §1.8.1 *Vocalismo nasal tónico*.
7. Tonic nasal diphthongs ⟨-âu⟩ [ɐ̃w], ⟨-âi⟩ [ɐ̃j], ⟨-ôi⟩ [õj].
8. **Monosyllabic final-liquid exceptions** — the general tonic-final ⟨-l⟩/⟨-r⟩
   elision is suspended for the monosyllables *mal*, *tal*, *cual* (their lateral
   is pronounced in most contexts — Convenção §2.6 *Nota*) and *pur* (port.
   *por*), listed as `word_exceptions`. Polysyllables still elide (*Brasí*,
   *cantá*, *senhô*).

## Vowel reduction (retained from the Alentejo base)

Barranquenho keeps the inherited EP unstressed-vowel reduction: the Convenção
orthography itself encodes final raising (final -o written ⟨u⟩ = [u], final -e
written ⟨i⟩), so the inherited pt-PT vowel `positional_graphemes` are kept rather
than overridden. Finer differences in *pretonic* vocalism between Barranquenho
and Lisbon are not quantified at phoneme-mapping resolution in the cited sources
and are left inherited rather than invented (research-grounding rule).

## Worked examples

| Orthography | IPA | Features shown |
|:---|:---|:---|
| `mesmo` | ˈmɛhmu | coda /s/ → [h]; final -o → [u] |
| `visto` | ˈbihtu | betacism + coda-/s/ aspiration |
| `vaca` | ˈbakɐ | betacism |
| `cantar` | ˈkɐ̃tɐ | coda-n nasalises a→ɐ̃; final -r deletion |
| `campu` | ˈkɐ̃pu | coda-m nasalises a→ɐ̃ |
| `lindo` | ˈlĩdu | coda-n nasalises i→ĩ |
| `bom` | ˈbõ | coda-m nasalises, ɔ→õ, m absorbed |
| `lhano` | ˈʎanu | intervocalic (onset) n stays oral |
| `mal` | ˈmal | monosyllable keeps final -l (Convenção §2.6 Nota) |
| `Brasil` | ˈbɾazi | final -l deletion |

## Limitations

- **No gold benchmark**: Barranquenho has no scoreboard row; correctness here is
  by citation, not PER.
- Apico-alveolar articulatory detail and fine pretonic vocalism are not modelled
  (documented, not invented).
- Free variation between coda-/s/ aspiration [h] and full deletion ∅ is reduced
  to the aspirate for internal codas and deletion word-finally.
- The monosyllabic final-liquid retention is modelled as a closed
  `word_exceptions` set (*mal*, *tal*, *cual*, *pur*) rather than by a general
  rule: the positional layer has no syllable-count position, so the
  monosyllable-vs-polysyllable conditioning cannot be expressed generically. The
  e-series ⟨en⟩ digraph still greedily precedes ⟨nh⟩ in *venho*/*senhô* (a
  pre-existing tokenisation limitation, unaffected here); the i/o/u-series and
  ⟨nh⟩ elsewhere resolve correctly.

## Relation to `g2p_barranquenho`

A dedicated downstream engine, `g2p_barranquenho`, consumes this spec as its data
layer. This spec supplies the pre-lexical grapheme/positional maps and the
post-lexical contact overrides; the engine builds on them (see Workstream B
downstream migration). This page and the spec keep the input contract stable:
input is Barranquenho orthography per the 2025 Convenção (final -o written ⟨u⟩,
final -e written ⟨i⟩, deleted final -r/-l/-s not written), and the engine relies
on that shape.

## Sources

- Navas Sánchez-Élez, María Victoria (2011). *El barranqueño: un modelo de
  lenguas en contacto*. Madrid: Editorial Complutense / Centro de Linguística da
  Universidade de Lisboa, 320 pp. ISBN 978-84-9938-099-5.
- Clements, J. Clancy; Amaral, Patrícia; Luís, Ana R. (2008). "Cultural identity
  and the structure of a mixed language: The case of Barranquenho".
  *Proceedings of the Annual Meeting of the Berkeley Linguistics Society* 34,
  13–22. <https://hdl.handle.net/2022/24680>
- Convenção Ortográfica do Barranquenho (2025). II Congresso Barranquenho, Câmara
  Municipal de Barrancos.
- Gonçalves, M. F.; Navas, M. V.; Correia, V. M. D. (2025). *Gramática Básica de
  Barranquenho*. Universidade de Évora. ISBN 978-972-778-464-6.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [mwl](mwl.md), [romance](romance.md)*
