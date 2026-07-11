# Alfena / Douro-Litoral European Portuguese (`pt-PT-x-alfena`) — Phonology Reference

**Code**: `pt-PT-x-alfena` | **Family**: Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` (standard, Lisbon-type EP) | **Quality tier**: research
**Sources**: Cintra (1971, *Boletim de Filologia* 22:81–116), Álvarez Pérez
(2014, *Journal of Portuguese Linguistics* 13-1), Mateus & d'Andrade (2000)

**Alfena, Valongo — Greater Porto / Douro-Litoral** (Cintra's *Duriense* zone). Besides the shared northern features it is locally known for a vowel-breaking (*Brechung*) of stressed mid vowels ([ɛ]>[ɛ͜ɐ] etc.), enumerated as secondary allophonic variants from regional-dialect literature (not Cintra/Pérez) and not asserted as default output.

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


### 3. What is **not** modelled

* Porto's tonic-close-vowel diphthongisation ([e]>[je], [o]>[wo]) is a
  Porto/Baixo-Minho-Douro **subdivision marker** (Cintra 1971, p.93) kept in
  `pt-PT-x-porto`; it is **not** applied here.
* Retroflex sibilants [ʂ ʐ] and retroflex lateral/flap [ɭ ɽ] are **not** in
  Cintra (1971) or Álvarez Pérez (2014) — the northern reverso/apico-alveolar
  sibilant belongs to /s z/ (modelled above as [s̺ z̺]), not to /ʃ ʒ/.

## Sources

* **Cintra, L. F. Lindley (1971)**, *Nova proposta de classificação dos
  dialectos galego-portugueses*, Boletim de Filologia 22:81–116 (pp. 88, 92–93).
* **Álvarez Pérez, Xosé Afonso (2014)**, *European Portuguese dialectal
  features: a comparison with Cintra's proposal*, Journal of Portuguese
  Linguistics 13(1):29–62, DOI 10.5334/jpl.62 (pp. 35–39).
* Mateus, M. H. M. & d'Andrade, E. (2000), *The Phonology of Portuguese*, OUP.
