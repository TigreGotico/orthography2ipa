# Lisbon / Estremenho European Portuguese (pt-PT-x-lisbon) — Phonology Reference

**Code**: `pt-PT-x-lisbon` | **Family**: Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` | **Quality tier**: research
**Sources**: Cintra (1971, *Boletim de Filologia* 22:81–116); Segura (2013, *Gramática do Português*, Fundação Calouste Gulbenkian); Mateus & d'Andrade (2000, *The Phonology of Portuguese*); Cunha & Cintra (1984, *Nova Gramática do Português Contemporâneo*)

## Lisbon is the reference variety, not a divergent dialect

The single most important fact about this spec is that it barely differs from its
parent. Cintra's (1971) classification of the Galician-Portuguese dialect space
establishes that the **standard, prestige norm of European Portuguese IS
essentially the Central-Southern / Lisbon (Estremenho) variety**. The `pt-PT`
base in this repository is built around exactly that Lisbon-type standard, so the
base already models nearly everything that characterises Lisbon speech.

Consequently, unlike the Northern (`pt-PT-x-porto`) or Southern
(`pt-PT-x-alentejo`, `-algarve`) specs — which override inherited processes to
express genuine regional divergence — `pt-PT-x-lisbon` declares only a small set
of **honest, well-sourced deltas** over an already Lisbon-shaped base. The main
deliverable of this spec is an accurate, non-padded record of that fact.

## Inherited from pt-PT (the standard = Lisbon, not restated here)

These diagnostic European Portuguese processes are **inherited unchanged** via
`graphemes_base`, `allophones_base` and `positional_graphemes_base`, because the
standard values already ARE the Lisbon values. They are deliberately **not**
duplicated in this spec:

- **Strong unstressed vowel reduction** — pretonic/final unstressed /e/ → [ɨ]
  (inherited positional map); the spec keeps explicit unstressed /a/ → [ɐ] and
  /o/ → [u] reduction rows so it reduces the unstressed vowels without inheriting
  the base's open [ɔ]/[a] stressed-nucleus defaults (lexically unpredictable for
  spelling-unmarked stressed `<o>`/`<a>`).
- **Dark (velarised) coda /l/ → [ɫ]** (`PT_CODA_L_DARK`).
- **Coda-sibilant *chiado*** — coda /s z/ → [ʃ ʒ] (`PT_CODA_S_HUSH`,
  `PT_CODA_Z_HUSH`), with the coda-/s/ voicing/resyllabification sandhi.

## Lisbon-specific deltas modelled

| Feature | Value | Example | Source |
|:--|:--|:--|:--|
| `<ei>` diphthong lowering-centralisation | `<ei>` → **[ɐj]** | leite → [ˈlɐjtɨ], primeiro → [pɾiˈmɐjɾu], reino → [ˈʁɐjnu], seis → [ˈsɐjʃ] | Cintra 1971; Segura 2013; Mateus & d'Andrade 2000 |
| `<ou>` monophthongisation | `<ou>` → **[o]** | ouro → [ˈoɾu] | Segura 2013; Cintra 1971 |
| Rhotic realisation | /ʁ/ → **[ʁ]** (uvular fricative, Lisbon-urban norm) | carro → [ˈkaʁu] | Mateus & d'Andrade 2000 |
| Reduced schwa | /ə/ → **[ɨ]** | — | Mateus & d'Andrade 2000 |

The **`<ei>` → [ɐj]** realisation is the single diagnostic grapheme-level Lisbon
feature: conservative and Northern EP keep [ej] (see `pt-PT-x-porto`, which
declares `<ei>` → [ej] and `<ou>` → [ow] as its diphthong-preservation deltas),
while the Centro-Litoral / Estremenho zone lowers and centralises the nucleus to
[ɐj]. Cintra (1971) and Segura (2013) treat [ɐj] as characteristic of that zone,
and Mateus & d'Andrade (2000) transcribe the standard `<ei>` as [ɐj].

## Known limits (documented, not faked)

- **Stressed `<e>` → [ɐ] before a palatal** (coelho, espelho, abelha) is a
  further reported Lisbon feature, but its conditioning — *stressed vowel before
  a palatal consonant* — is a context the engine's positional vocabulary does not
  currently express (there is no `before_palatal` `GraphemePosition`). Rather than
  approximate it with a rule that would over-apply, it is left **unmodelled** and
  recorded here as an engine limit. Adding a palatal-context position is engine
  work, not a data change.
- **Intervocalic voiced-stop spirantisation** (/b d ɡ/ → [β ð ɣ]) is a general EP
  process, not Lisbon-specific, and is deliberately not encoded — every available
  pt gold is broad/phonemic and transcribes the stops (see the `pt-PT` base
  notes); it belongs to a future narrow-transcription task.
- **Apico-alveolar vs predorsodental sibilant place** (Cintra's primary
  North/South isogloss) is an articulatory distinction invisible to a
  phoneme-level, orthography-blind engine; the Lisbon-standard predorsodental
  value is what the base produces.

## Benchmark

Measured on the `ep_dialects` expert-human gold (`pt-PT-x-lisbon`, n = 45,
PER ≈ 0.25). The transcription-affecting fields are unchanged: this change scrubs
unpublished citations from `notes`/`sources` and adds the honest documentation
above. The scoreboard row is therefore byte-identical.

## Sources

- **Cintra, L. F. Lindley (1971)**. *Nova proposta de classificação dos dialectos
  galego-portugueses*. Boletim de Filologia (Lisboa), vol. 22, pp. 81–116.
  [PDF](https://cvc.instituto-camoes.pt/hlp/biblioteca/novaproposta.pdf).
  Republished in *Estudos de Dialectologia Portuguesa*, Sá da Costa, 1983.
- **Segura, Luísa (2013)**. *Variedades dialetais do português europeu*. In
  Raposo et al. (eds.), *Gramática do Português*, vol. I, Fundação Calouste
  Gulbenkian, pp. 85–142.
- **Mateus, M. H. M. & d'Andrade, E. (2000)**. *The Phonology of Portuguese*.
  Oxford University Press.
- **Cunha, C. & Cintra, L. F. L. (1984)**. *Nova Gramática do Português
  Contemporâneo*. Sá da Costa.
