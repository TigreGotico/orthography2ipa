# Lisbon / Estremenho European Portuguese (pt-PT-x-lisbon) — Phonology Reference

**Code**: `pt-PT-x-lisbon` | **Family**: Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` | **Quality tier**: research
**Sources**: Hristovsky (2008, *Textos Seleccionados* XXIII ENAPL, APL, pp. 239–255); Mateus & d'Andrade (2000, *The Phonology of Portuguese*, p. 19); Cruz-Ferreira (1995, *JIPA* 25:90–94); Cintra (1971, *Boletim de Filologia* 22:81–116); Segura (2013, *Gramática do Português*, Fundação Calouste Gulbenkian)

## A distinct urban variety, not the conservative norm

`pt-PT-x-lisbon` models the speech of Lisbon and the surrounding
Estremenho (Centro-Litoral) zone as a **distinct urban variety with its own
phonological innovations**, expressed as a delta on top of the `pt-PT` base.
The `pt-PT` base is the broad *descriptive* European Portuguese standard; Lisbon
inherits it and adds features that **deviate from the conservative / neutral
prescriptive norm**, which is traditionally anchored to educated central
(Coimbra-type) speech.

The status of Lisbon relative to "the standard" is genuinely contested in the
literature, and this spec represents that honestly rather than picking a side.
Cintra (1971) argues that the prestige standard of European Portuguese broadly
coincides with the Central-Southern (Estremenho / Lisbon) type. The conservative
pedagogical reference norm, however, is often anchored to central (Coimbra)
speech, which lacks several of the Lisbon innovations recorded below. Lisbon is
therefore **not** encoded as identical to that reference norm.

## Inherited from pt-PT (not restated here)

These broad European Portuguese processes are **inherited unchanged** through
the `pt-PT` base edge (`graphemes_base`, `allophones_base`,
`positional_graphemes_base`, and the id-keyed `allophone_rules` overlay); they
are the values Lisbon shares with the base standard and are deliberately **not**
duplicated in this spec:

- **Strong unstressed vowel reduction** — pretonic/final unstressed /e/ → [ɨ]
  (inherited positional map). The spec keeps explicit unstressed /a/ → [ɐ] and
  /o/ → [u] reduction rows so it reduces the unstressed vowels without inheriting
  the base's open [ɔ]/[a] stressed-nucleus defaults (lexically unpredictable for
  spelling-unmarked stressed `<o>`/`<a>`).
- **Dark (velarised) coda /l/ → [ɫ]** (`PT_CODA_L_DARK`).
- **Coda-sibilant *chiado*** — coda /s z/ → [ʃ ʒ] (`PT_CODA_S_HUSH`,
  `PT_CODA_Z_HUSH`), with the coda-/s/ voicing/resyllabification sandhi.

## Lisbon innovations modelled

| Feature | Value | Example | Source |
|:--|:--|:--|:--|
| **Stressed `<e>` → [ɐ] before a palatal** | /e ɛ/ → **[ɐ]** before [ʎ ɲ ʃ ʒ] | coelho → [ˈkoɐʎu], fecho → [ˈfɐʃu], venho → [ˈvɐɲu], espelho → [eʃˈpɐʎu], abelha → [ɐˈbɐʎɐ] | Hristovsky 2008:239; Mateus & d'Andrade 2000:19 |
| `<ei>` diphthong lowering-centralisation | `<ei>` → **[ɐj]** | leite → [ˈlɐjtɨ], primeiro → [pɾiˈmɐjɾu], reino → [ˈʁɐjnu], seis → [ˈsɐjʃ] | Cintra 1971; Segura 2013; Mateus & d'Andrade 2000 |
| `<ou>` monophthongisation | `<ou>` → **[o]** | ouro → [ˈoɾu] | Segura 2013; Cintra 1971 |
| Rhotic realisation | /ʁ/ → **[ʁ]** (uvular fricative, Lisbon-urban norm) | carro → [ˈkaʁu] | Mateus & d'Andrade 2000 |

### The signature innovation: stressed `<e>` → [ɐ] before a palatal

The single most characteristic Lisbon feature modelled here is the
**centralisation of the stressed front mid vowel to [ɐ] before a palatal
consonant** — the palatals [ʎ ɲ ʃ ʒ] and the digraphs/letters that produce them
(`<lh>` → ʎ, `<nh>` → ɲ, `<ch>`/`<x>` → ʃ, `<j>`/`<g(e/i)>` → ʒ):

- coelho → **[ˈkoɐʎu]**, espelho → **[eʃˈpɐʎu]**, fecho → **[ˈfɐʃu]**,
  venho → **[ˈvɐɲu]**, abelha → **[ɐˈbɐʎɐ]**.

Hristovsky (2008:239) surveys the filological, dialectological and phonological
literature (Gonçalves Viana 1883, Cintra 1971, Barbosa 1965, Andrade 1981;
Barros 1994 for the sociolinguistic distribution *in Lisbon speech*) and reports
that all these authors agree the vowel /e/ (and /ɛ/) is realised as [ɐ] before a
palatal segment, as a dissimilatory process. Mateus & d'Andrade (2000:19) list
stressed [ɐ] as occurring in exactly three contexts — before a palatal consonant
(*telha* [ˈtɐʎɐ]), before the palatal glide (*lei* [ˈlɐj]) and before a nasal —
and treat it as a *derived*, not underlying, vowel. Cruz-Ferreira (1995:92)
notes that all vowels are raised and advanced before palato-alveolar and palatal
consonants. **The conservative / central (Coimbra-type = `pt-PT` base) norm keeps
[e]/[ɛ] in this context** — which is exactly why this is encoded as a Lisbon
delta rather than in the base.

This is implemented by the `LX_STRESSED_E_PREPALATAL` allophone rule
(`followed_by: "palatal"`), which runs as a post-lexical rescorer **after**
positional reduction. Because unstressed /e/ has already reduced to [ɨ] by that
stage, the rule fires only where the vowel still surfaces as [e]/[ɛ] — i.e. the
**stressed** (or word-initial) realisation. This makes the rule stress-gated
without needing a dedicated "stressed-before-palatal" position.

**Scope note (honestly stated).** Hristovsky (2008:239) reports the change for
/e/ in tonic *and/or* atonic position. The atonic case, however, is variable and
sociolinguistically graded (Barros 1994): in a broad transcription, unstressed
pre-palatal /e/ overwhelmingly reduces to [ɨ] — melhor → [mɨˈʎoɾ], fechar →
[fɨˈʃaɾ], mexer → [mɨˈʃɛɾ] — which is the value the base and the gold data use.
Only the categorical **stressed** case is modelled; the reduced unstressed value
is deliberately left untouched.

### The `<ei>` → [ɐj] diphthong

The `<ei>` → [ɐj] realisation is the diagnostic grapheme-level Estremenho
feature: conservative and Northern EP keep [ej] (see `pt-PT-x-porto`, which
declares `<ei>` → [ej] and `<ou>` → [ow] as its diphthong-preservation deltas),
while the Centro-Litoral / Estremenho zone lowers and centralises the nucleus to
[ɐj]. Cintra (1971) and Segura (2013) treat [ɐj] as characteristic of that zone.
The isophone of `<ei>` monophthongisation/centralisation is one of Cintra's
boundary lines running near the Tejo.

## Not modelled here

- **Intervocalic voiced-stop spirantisation** (/b d ɡ/ → [β ð ɣ]) is a general
  EP process, not Lisbon-specific, and is deliberately not encoded — every
  available pt gold is broad/phonemic and transcribes the stops (see the `pt-PT`
  base notes); it belongs to a future narrow-transcription task.
- **Apico-alveolar vs predorsodental sibilant place** (Cintra's primary
  North/South isogloss) is an articulatory distinction invisible to a
  phoneme-level, orthography-blind engine; the predorsodental value the base
  produces is what Lisbon uses.

## Benchmark

`pt-PT-x-lisbon` is scored against two expert-human gold sets — `ep_dialects`
(n = 45) and `clup_dialect` (n = 5). Note that these small, unvalidated gold
sets are internally inconsistent in exactly the pre-palatal context modelled
here (e.g. they transcribe *venho* with a plain front vowel), so the pre-palatal
delta does not by itself move the aggregate PER. The delta is justified on the
documented phonology, not on a PER gain.

## Sources

- **Hristovsky, Gueorgui (2008)**. *Estudo fonológico de alguns padrões na
  variação da vogal /e/ seguida de /i/ ([j]) ou de consoante palatal no Português
  Europeu*. In *Textos Seleccionados, XXIII Encontro Nacional da Associação
  Portuguesa de Linguística*, Lisboa: APL, pp. 239–255.
  [PDF](https://apl.pt/wp-content/uploads/2017/09/18-Hristovsky.pdf). (p. 239 for
  the /e/, /ɛ/ → [ɐ] before-palatal generalisation.)
- **Mateus, M. H. M. & d'Andrade, E. (2000)**. *The Phonology of Portuguese*.
  Oxford University Press. (p. 19: stressed [ɐ] before a palatal consonant, the
  palatal glide, or a nasal.)
- **Cruz-Ferreira, Madalena (1995)**. *European Portuguese*. Journal of the
  International Phonetic Association 25(2):90–94. (p. 92: vowels raised/advanced
  before palato-alveolar and palatal consonants.)
- **Cintra, L. F. Lindley (1971)**. *Nova proposta de classificação dos dialectos
  galego-portugueses*. Boletim de Filologia (Lisboa), vol. 22, pp. 81–116.
  [PDF](https://cvc.instituto-camoes.pt/hlp/biblioteca/novaproposta.pdf).
  Republished in *Estudos de Dialectologia Portuguesa*, Sá da Costa, 1983.
- **Segura, Luísa (2013)**. *Variedades dialetais do português europeu*. In
  Raposo et al. (eds.), *Gramática do Português*, vol. I, Fundação Calouste
  Gulbenkian, pp. 85–142.
- **Cunha, C. & Cintra, L. F. L. (1984)**. *Nova Gramática do Português
  Contemporâneo*. Sá da Costa.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-PT-x-alentejo](pt-PT-x-alentejo.md), [pt-PT-x-porto](pt-PT-x-porto.md)*
