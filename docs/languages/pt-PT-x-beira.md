# Beirão / Beira European Portuguese (`pt-PT-x-beira`) — Phonology Reference

**Code**: `pt-PT-x-beira` | **Family**: Indo-European > Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` (standard, Lisbon-type EP) | **Quality tier**: research
**Sources**: Cintra (1971, *Boletim de Filologia* 22:81–116), Álvarez Pérez
(2014, *Journal of Portuguese Linguistics* 13-1), Brissos (2014, *JPL* 13-1),
Mateus & d'Andrade (2000)

**Beira Litoral (Coimbra, Aveiro), Beira Alta (Viseu, Guarda), Beira Baixa (Castelo Branco)**. The apico-alveolar sibilant of this zone is the *s beirão* itself — Cintra (1971, p.88) notes the most palatalised apical variant is *"vulgarmente conhecida pelo nome de s beirão"*. Pérez (2014) places the clearest apical core in the districts of Viseu, Guarda and Castelo Branco, and documents the /b/–/v/ merger extending through the eastern Guarda/Castelo-Branco districts that Cintra's original map omitted. A conservative alveolar rhotic (trill [r]) is enumerated as a variant of /ʁ/.

## Diagnostic features modelled

These four specs sit in Cintra's (1971) **Baixo-Minhoto-Duriense-Beirão**
dialect group. They inherit the whole standard pt-PT system (unstressed vowel
reduction, dark coda /l/, coda-sibilant *chiado*, sandhi) via `graphemes_base`
/ `positional_graphemes_base` / `allophones_base`, and declare only their
northern deltas.

### 1. Apico-alveolar-**only** sibilant system

Archaic Portuguese distinguished **four sibilants**: apico-alveolar [s̺ z̺]
(from ⟨s⟩, ⟨ss⟩) opposed to laminal/predorsodental [s z] (from ⟨c⟩ before
e/i, ⟨ç⟩, ⟨z⟩). Cintra (1971, p.93):

> *"a existência de um sistema de quatro sibilantes — [s̺] e [z̺]
> ápicoalveolares (correspondentes aos grafemas s e ss)… opondo-se a e
> convivendo com o [s] e o [z] predorsodentais (correspondentes aos grafemas
> ce,i, ç e z)."*

The far-northern **Transmontano/Alto-Minhoto** dialects keep this four-way
opposition intact. This group does **not**: it neutralises the opposition
**in favour of the apical branch** — both ⟨s/ss⟩ **and** ⟨c/ç/z⟩ collapse to
a single apico-alveolar [s̺] (voiceless) / [z̺] (voiced). Álvarez Pérez
(2014, pp.37-38):

> *"the other groups of northern dialects, denoted by Cintra as
> Baixo-Minhotos, Durienses and Beirões, kept only the apico-alveolar
> branch; on the other hand, the rest of Portugal (as well as standard
> Portuguese) neutralised the opposition in favour of laminal sibilants."*

Modelled as a grapheme + positional delta: ⟨s⟩ onset → [s̺], intervocalic
⟨-s-⟩ → [z̺], ⟨ss⟩ → [s̺], ⟨c⟩ before e/i → [s̺], ⟨ç⟩ → [s̺], ⟨z⟩ → [z̺].
Syllable-coda ⟨s/z⟩ keep the inherited pan-EP *chiado* neutralisation to
[ʃ]/[ʒ]. This is the **two-sibilant apical-only** system, distinct from the
four-sibilant Transmontano and from the laminal-only Centre-South/standard.

The apico-alveolar segment is a real, distinct IPA symbol ([s̺] = s + U+033A
COMBINING INVERTED BRIDGE BELOW) and is modelled **actively**, not deleted or
declared unmodellable.

### 2. Northern betacism — /v/ ~ /b/ merger

Cintra's (1971, p.88) first diagnostic northern feature:

> *"o desaparecimento da oposição fonológica entre os fonemas /v/ e /b/ e a
> sua fusão num fonema único /b/, realizado ora como oclusiva, ora como
> fricativa (ou espirante) b ou β."*

Modelled as the grapheme delta ⟨v⟩ → [b] (~[β]). Álvarez Pérez (2014,
pp.35-37) reassessed the extent with the ALEPG corpus and found the bilabial
merger covers roughly twice Cintra's mapped area — categorical in the far
north and extending **along the coast beyond the district of Coimbra** and
through the **eastern districts of Guarda and Castelo Branco** — which is why
betacism is applied to all four zones below.

### Worked examples

| Word | pt-PT (standard) | this dialect |
|:---|:---|:---|
| sol (⟨s-⟩) | ˈsɔɫ | **ˈs̺ɔɫ** |
| casa (⟨-s-⟩) | ˈkazɐ | **ˈkaz̺ɐ** |
| cedo (⟨c⟩+e) | ˈsɛdu | **ˈs̺ɛdu** |
| cinco (⟨c⟩+i) | ˈsinku | **ˈs̺inku** |
| praça (⟨ç⟩) | ˈpɾasɐ | **ˈpɾas̺ɐ** |
| zebra (⟨z⟩) | ˈzɛbɾɐ | **ˈz̺ɛbɾɐ** |
| dez (⟨-z⟩ coda) | ˈdɛʃ | ˈdɛʃ (chiado inherited) |
| vaca (⟨v⟩) | ˈvakɐ | **ˈbakɐ** |
| uva (⟨-v-⟩) | ˈuvɐ | **ˈuβɐ** (intervocalic spirant) |


### 3. Beira-Baixa stressed /u/ → [y] palatalisation (`pt-PT-x-beira` only)

Cintra (1971, p.14 of the CVC reflow) delimits the **Beira-Baixa / Alto-Alentejo**
zone — *"uma região que tem como principais núcleos urbanos Castelo-Branco e
Portalegre"* — by the isogloss of stressed-/u/ palatalisation:

> *"Como isófona que possa marcar o limite da zona, parece-me preferível
> escolher, a da palatalização, em maior ou menor grau, da vogal tónica u"*,
> within *"uma profunda alteração de timbre de todo o sistema vocálico,
> principalmente do tónico"*.

He adds that at the zone's edges the trait that stays most perceptible is exactly
this u-timbre change (*"o traço que permanece mais perceptível é a alteração do
timbre do u"*). The explicit front-rounded **[y]** value is written in the
adjacent Barlavento-Algarvio passage of the same *"reacção em cadeia"* — *"a
palatalização da lábio-velar [u] em [y]"* — the two zones sharing the
/u/-palatalisation isogloss; Brissos (2014) documents it acoustically for the
central-southern zone ([tˈyd] *tudo*, [lˈymɨ] *lume*).

Modelled as the allophone rule **`BEI_U_FRONTING`** (stressed nucleus only),
mirroring the sister mainland zone `pt-PT-x-alentejo` (and `pt-PT-x-algarve`).
Being a whole-tonic-system **mainland chain shift**, it fronts even before a
tautosyllabic coda liquid (*sul* → [ˈs̺yɫ]) — deliberately **without** the
insular `pt-PT-x-acores` `ACO_U_KEEP_BEFORE_CODA` block, which is a Rogers-1948
São-Miguel open-nucleus conditioning with no mainland source. A **proclitic
guard** (`word_exceptions`, same design as the sister mainland specs) pins the
monosyllabic clitics *o/os/no/nos/do/dos/ao/aos/pelo/pelos/um/uns* to their
inherited Beira nuclei so the word-level stress detector cannot mis-front *do* →
[ˈdy].

**Scope / intra-node limit** (documented, not faked): /u/-fronting is the
**Beira-Baixa** (Castelo-Branco) sub-zone realisation; Beira Litoral (Coimbra,
Aveiro) and Beira Alta (Viseu, Guarda) sit in the Baixo-Minhoto-Duriense-Beirão
group and do **not** palatalise tonic /u/. This general Beira node models the
strongest (Beira-Baixa) realisation — the same modelling stance as
`pt-PT-x-acores` (Terceira gold vs the São Miguel /u/-fronting). The sibling
specs `pt-PT-x-minho`, `pt-PT-x-alfena` and `pt-PT-x-aveiro` do **not** carry
the rule.

| Word | pt-PT (standard) | `pt-PT-x-beira` |
|:---|:---|:---|
| tudo | ˈtudu | **ˈtydu** |
| lume | ˈlumɨ | **ˈlymɨ** |
| número | ˈnumɨɾu | **ˈnymɨɾu** |
| sul (before coda /l/) | ˈsuɫ | **ˈs̺yɫ** (fronts — mainland chain shift) |
| turistas (pretonic /u/) | tuˈɾiʃtɐʃ | tuˈɾiʃtɐʃ (unstressed — no fronting) |
| do (proclitic) | ˈdu | ˈdu (guard — never [ˈdy]) |

### 4. What is **not** modelled

* Porto's tonic-close-vowel diphthongisation ([e]>[je], [o]>[wo]) is a
  Porto/Baixo-Minho-Douro **subdivision marker** (Cintra 1971, p.93) kept in
  `pt-PT-x-porto`; it is **not** applied here.
* Retroflex sibilants [ʂ ʐ] and retroflex lateral/flap [ɭ ɽ] are **not** in
  Cintra (1971) or Álvarez Pérez (2014) — the northern reverso/apico-alveolar
  sibilant belongs to /s z/ (modelled above as [s̺ z̺]), not to /ʃ ʒ/.

## Sources

* **Cintra, L. F. Lindley (1971)**, *Nova proposta de classificação dos
  dialectos galego-portugueses*, Boletim de Filologia 22:81–116 (pp. 14 of the
  CVC reflow — Beira-Baixa/Alto-Alentejo stressed-/u/ isogloss — 88, 92–93).
* **Álvarez Pérez, Xosé Afonso (2014)**, *European Portuguese dialectal
  features: a comparison with Cintra's proposal*, Journal of Portuguese
  Linguistics 13(1):29–62, DOI 10.5334/jpl.62 (pp. 35–39).
* **Brissos, Fernando (2014)**, *New insights into Portuguese central-southern
  dialects…*, Journal of Portuguese Linguistics 13(1):63–115 (acoustic
  documentation of central-southern stressed /u/ → [y]).
* Mateus, M. H. M. & d'Andrade, E. (2000), *The Phonology of Portuguese*, OUP.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-PT-x-aveiro](pt-PT-x-aveiro.md), [pt-PT-x-porto](pt-PT-x-porto.md)*
