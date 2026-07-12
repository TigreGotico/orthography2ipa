# Changelog

## [3.2.0a1](https://github.com/TigreGotico/orthography2ipa/tree/3.2.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/3.1.0a2...3.2.0a1)

**Merged pull requests:**

- feat\(data\): promote the first six languages to production tier [\#328](https://github.com/TigreGotico/orthography2ipa/pull/328) ([JarbasAl](https://github.com/JarbasAl))

## [3.1.0a2](https://github.com/TigreGotico/orthography2ipa/tree/3.1.0a2) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/3.1.0a1...3.1.0a2)

**Merged pull requests:**

- chore\(benchmarks\): regenerate full-dataset scoreboard + CI sample [\#326](https://github.com/TigreGotico/orthography2ipa/pull/326) ([JarbasAl](https://github.com/JarbasAl))

## [3.1.0a1](https://github.com/TigreGotico/orthography2ipa/tree/3.1.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/3.0.1a1...3.1.0a1)

**Merged pull requests:**

- feat\(benchmark\): Arabic gold with tashkeel restored [\#324](https://github.com/TigreGotico/orthography2ipa/pull/324) ([JarbasAl](https://github.com/JarbasAl))

## [3.0.1a1](https://github.com/TigreGotico/orthography2ipa/tree/3.0.1a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/3.0.0a2...3.0.1a1)

**Merged pull requests:**

- fix\(stress\): epenthetic schwa no longer shifts the stress mark a syllable late [\#322](https://github.com/TigreGotico/orthography2ipa/pull/322) ([JarbasAl](https://github.com/JarbasAl))

## [3.0.0a2](https://github.com/TigreGotico/orthography2ipa/tree/3.0.0a2) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/3.0.0a1...3.0.0a2)

**Merged pull requests:**

- refactor\(benchmark\): drop the tugalex wrapper, load the HF lexicon directly [\#319](https://github.com/TigreGotico/orthography2ipa/pull/319) ([JarbasAl](https://github.com/JarbasAl))

## [3.0.0a1](https://github.com/TigreGotico/orthography2ipa/tree/3.0.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/2.0.0a1...3.0.0a1)

**Breaking changes:**

- feat!: script-agnostic vowel classification \(spec-derived, not a Latin letter list\) [\#316](https://github.com/TigreGotico/orthography2ipa/pull/316) ([JarbasAl](https://github.com/JarbasAl))

## [2.0.0a1](https://github.com/TigreGotico/orthography2ipa/tree/2.0.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.88.0a2...2.0.0a1)

**Breaking changes:**

- feat\(ca\)!: re-root the Catalan family on Old Catalan and restore the open-mid default [\#315](https://github.com/TigreGotico/orthography2ipa/pull/315) ([JarbasAl](https://github.com/JarbasAl))

## [1.88.0a2](https://github.com/TigreGotico/orthography2ipa/tree/1.88.0a2) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.88.0a1...1.88.0a2)

**Merged pull requests:**

- refactor\(data\): drop Tamil/Malayalam allophone rules that can never fire [\#313](https://github.com/TigreGotico/orthography2ipa/pull/313) ([JarbasAl](https://github.com/JarbasAl))

## [1.88.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.88.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.87.0a1...1.88.0a1)

**Merged pull requests:**

- feat\(benchmarks\): tier competitor- and LLM-derived gold; wire IPA-CHILDES + IPA-BabyLM [\#308](https://github.com/TigreGotico/orthography2ipa/pull/308) ([JarbasAl](https://github.com/JarbasAl))

## [1.87.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.87.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.86.2a1...1.87.0a1)

**Merged pull requests:**

- feat\(benchmark\): wire the full ipa-dict corpus with per-language provenance [\#304](https://github.com/TigreGotico/orthography2ipa/pull/304) ([JarbasAl](https://github.com/JarbasAl))

## [1.86.2a1](https://github.com/TigreGotico/orthography2ipa/tree/1.86.2a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.86.1a1...1.86.2a1)

**Merged pull requests:**

- fix: cancel the inherent vowel in abugidas instead of always appending it [\#303](https://github.com/TigreGotico/orthography2ipa/pull/303) ([JarbasAl](https://github.com/JarbasAl))

## [1.86.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.86.1a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.86.0a1...1.86.1a1)

**Merged pull requests:**

- fix: let maximal munch win over punctuation \(fixes flaky TestTokenizerRoundTrip\) [\#305](https://github.com/TigreGotico/orthography2ipa/pull/305) ([JarbasAl](https://github.com/JarbasAl))
- feat: encode the Goidelic broad/slender system \(ga, gd\) [\#301](https://github.com/TigreGotico/orthography2ipa/pull/301) ([JarbasAl](https://github.com/JarbasAl))

## [1.86.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.86.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.85.0a1...1.86.0a1)

**Breaking changes:**

- feat!: phonological\_distance stops reading the writing system [\#299](https://github.com/TigreGotico/orthography2ipa/pull/299) ([JarbasAl](https://github.com/JarbasAl))

**Merged pull requests:**

- fix\(benchmark\): score sentence gold with the sentence API, not the word API [\#302](https://github.com/TigreGotico/orthography2ipa/pull/302) ([JarbasAl](https://github.com/JarbasAl))
- feat\(scandinavian\): quantity, reduction and lenition for da/nb/sv [\#298](https://github.com/TigreGotico/orthography2ipa/pull/298) ([JarbasAl](https://github.com/JarbasAl))

## [1.85.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.85.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.84.0a1...1.85.0a1)

**Merged pull requests:**

- feat\(data\): grapheme maps for syllabary and alphabet scripts [\#279](https://github.com/TigreGotico/orthography2ipa/pull/279) ([JarbasAl](https://github.com/JarbasAl))

## [1.84.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.84.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.83.0a2...1.84.0a1)

**Merged pull requests:**

- feat\(data\): add the missing languages \(Tier A specs + honest stubs\) [\#275](https://github.com/TigreGotico/orthography2ipa/pull/275) ([JarbasAl](https://github.com/JarbasAl))

## [1.83.0a2](https://github.com/TigreGotico/orthography2ipa/tree/1.83.0a2) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.83.0a1...1.83.0a2)

**Merged pull requests:**

- docs: refresh the README and docs to match the library [\#292](https://github.com/TigreGotico/orthography2ipa/pull/292) ([JarbasAl](https://github.com/JarbasAl))

## [1.83.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.83.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.82.0a1...1.83.0a1)

**Merged pull requests:**

- feat: distinguish native scripts, romanizations and transliterations — and stop zh lying [\#291](https://github.com/TigreGotico/orthography2ipa/pull/291) ([JarbasAl](https://github.com/JarbasAl))

## [1.82.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.82.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.81.0a1...1.82.0a1)

**Merged pull requests:**

- feat: state the phoneme inventory directly, independent of the orthography [\#287](https://github.com/TigreGotico/orthography2ipa/pull/287) ([JarbasAl](https://github.com/JarbasAl))

## [1.81.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.81.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.80.0a1...1.81.0a1)

**Merged pull requests:**

- feat\(data\): locations for regional dialects [\#288](https://github.com/TigreGotico/orthography2ipa/pull/288) ([JarbasAl](https://github.com/JarbasAl))

## [1.80.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.80.0a1) (2026-07-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.79.1a1...1.80.0a1)

**Merged pull requests:**

- feat: geographic axis — location from Glottolog and great-circle distance [\#282](https://github.com/TigreGotico/orthography2ipa/pull/282) ([JarbasAl](https://github.com/JarbasAl))

## [1.79.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.79.1a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.79.0a1...1.79.1a1)

**Merged pull requests:**

- fix: wire the new stubs into the clade chain instead of authoring a family [\#285](https://github.com/TigreGotico/orthography2ipa/pull/285) ([JarbasAl](https://github.com/JarbasAl))

## [1.79.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.79.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.78.0a1...1.79.0a1)

## [1.78.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.78.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.77.0a1...1.78.0a1)

**Merged pull requests:**

- feat: spelling divergence — how differently two orthographies write the same sounds [\#281](https://github.com/TigreGotico/orthography2ipa/pull/281) ([JarbasAl](https://github.com/JarbasAl))
- feat: model language families as clade nodes and derive the family field [\#280](https://github.com/TigreGotico/orthography2ipa/pull/280) ([JarbasAl](https://github.com/JarbasAl))
- feat\(data\): multi-edition Wikipedia URLs + missing-language stubs [\#272](https://github.com/TigreGotico/orthography2ipa/pull/272) ([JarbasAl](https://github.com/JarbasAl))

## [1.77.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.77.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.76.0a1...1.77.0a1)

**Merged pull requests:**

- fix\(benchmarks\): classify styletts2 as espeak-derived, and never gate on it [\#276](https://github.com/TigreGotico/orthography2ipa/pull/276) ([JarbasAl](https://github.com/JarbasAl))
- feat\(data\): populate wikidata/phoible/wals cross-reference ids [\#274](https://github.com/TigreGotico/orthography2ipa/pull/274) ([JarbasAl](https://github.com/JarbasAl))

## [1.76.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.76.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.75.0a1...1.76.0a1)

**Merged pull requests:**

- feat\(data\): align language metadata + glottolog\_code to Glottolog; audit hierarchy [\#271](https://github.com/TigreGotico/orthography2ipa/pull/271) ([JarbasAl](https://github.com/JarbasAl))

## [1.75.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.75.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.74.0a1...1.75.0a1)

**Merged pull requests:**

- feat: surface dropped spec fields, add catalog ids and the official orthography [\#269](https://github.com/TigreGotico/orthography2ipa/pull/269) ([JarbasAl](https://github.com/JarbasAl))
- feat: score the published benchmark scoreboard on full datasets [\#268](https://github.com/TigreGotico/orthography2ipa/pull/268) ([JarbasAl](https://github.com/JarbasAl))

## [1.74.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.74.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.73.0a1...1.74.0a1)

**Merged pull requests:**

- feat\(explorer\): add family-tree and contact-graph views [\#267](https://github.com/TigreGotico/orthography2ipa/pull/267) ([JarbasAl](https://github.com/JarbasAl))

## [1.73.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.73.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.72.1a1...1.73.0a1)

**Merged pull requests:**

- feat: lexicon overlay \(sidecar TSV\) — word\_exceptions at scale \(E3\) [\#263](https://github.com/TigreGotico/orthography2ipa/pull/263) ([JarbasAl](https://github.com/JarbasAl))

## [1.72.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.72.1a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.72.0a1...1.72.1a1)

**Merged pull requests:**

- fix\(data\): model Portuguese coda vowel nasalization in base pt-PT/pt-BR \(major gap\) [\#264](https://github.com/TigreGotico/orthography2ipa/pull/264) ([JarbasAl](https://github.com/JarbasAl))

## [1.72.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.72.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.71.1a1...1.72.0a1)

**Merged pull requests:**

- feat: feature-export API — o2i as linguistic features for ML/CRF downstream \(F1\) [\#260](https://github.com/TigreGotico/orthography2ipa/pull/260) ([JarbasAl](https://github.com/JarbasAl))

## [1.71.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.71.1a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.71.0a1...1.71.1a1)

**Merged pull requests:**

- feat\(data\): Alentejo/Beira /u/→\[y\] fronting \(harvested + Cintra-cited\) [\#258](https://github.com/TigreGotico/orthography2ipa/pull/258) ([JarbasAl](https://github.com/JarbasAl))
- fix\(data\): EP external /s/-sandhi was inert — right\_context missed leading stress + reduced vowels [\#257](https://github.com/TigreGotico/orthography2ipa/pull/257) ([JarbasAl](https://github.com/JarbasAl))

## [1.71.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.71.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.70.2a1...1.71.0a1)

**Merged pull requests:**

- feat\(data\): Maghrebi + Yemeni + Sudanese Arabic dialects [\#254](https://github.com/TigreGotico/orthography2ipa/pull/254) ([JarbasAl](https://github.com/JarbasAl))

## [1.70.2a1](https://github.com/TigreGotico/orthography2ipa/tree/1.70.2a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.70.1a1...1.70.2a1)

**Merged pull requests:**

- fix\(data\): model Mirandese intervocalic /b/ spirantisation \(b→β\) [\#252](https://github.com/TigreGotico/orthography2ipa/pull/252) ([JarbasAl](https://github.com/JarbasAl))

## [1.70.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.70.1a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.70.0a1...1.70.1a1)

**Merged pull requests:**

- fix\(data\): Arabic alif-maksūra merge + word-final glide-coda after sukūn [\#251](https://github.com/TigreGotico/orthography2ipa/pull/251) ([JarbasAl](https://github.com/JarbasAl))

## [1.70.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.70.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.69.0a1...1.70.0a1)

**Merged pull requests:**

- feat: sentence-context seam — cross-word lattice + boundary rescorer + phrase position \(C4\) [\#248](https://github.com/TigreGotico/orthography2ipa/pull/248) ([JarbasAl](https://github.com/JarbasAl))

## [1.69.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.69.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.68.0a1...1.69.0a1)

**Merged pull requests:**

- feat\(data\): European Portuguese accent enrichment \(Coimbra/Braga/São-Miguel + validations\) [\#247](https://github.com/TigreGotico/orthography2ipa/pull/247) ([JarbasAl](https://github.com/JarbasAl))

## [1.68.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.68.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.67.0a1...1.68.0a1)

**Merged pull requests:**

- feat\(data\): enrich ancestry metadata — non-Indo-European \(round 2\) [\#245](https://github.com/TigreGotico/orthography2ipa/pull/245) ([JarbasAl](https://github.com/JarbasAl))

## [1.67.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.67.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.66.0a1...1.67.0a1)

**Merged pull requests:**

- feat\(data\): enrich ancestry metadata — Indo-European \(round 2\) [\#243](https://github.com/TigreGotico/orthography2ipa/pull/243) ([JarbasAl](https://github.com/JarbasAl))

## [1.66.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.66.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.65.0a1...1.66.0a1)

**Merged pull requests:**

- feat\(data\): enrich ancestry/substrate/superstrate/adstrate metadata \(round 1\) [\#240](https://github.com/TigreGotico/orthography2ipa/pull/240) ([JarbasAl](https://github.com/JarbasAl))

## [1.65.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.65.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.64.0a1...1.65.0a1)

**Merged pull requests:**

- feat\(data\): Portuguese external /s/-sandhi before vowels \(Algarve/Azores \[ʒ\], standard \[z\]\) [\#238](https://github.com/TigreGotico/orthography2ipa/pull/238) ([JarbasAl](https://github.com/JarbasAl))

## [1.64.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.64.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.63.0a1...1.64.0a1)

**Merged pull requests:**

- feat\(benchmarks\): human-gold Mirandese + Infopédia + Portal-scraped Portuguese gold rows [\#235](https://github.com/TigreGotico/orthography2ipa/pull/235) ([JarbasAl](https://github.com/JarbasAl))

## [1.63.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.63.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.62.0a1...1.63.0a1)

**Merged pull requests:**

- feat: Arabic engine improvements — ligature normalization, gemination, ar spec fixes [\#233](https://github.com/TigreGotico/orthography2ipa/pull/233) ([JarbasAl](https://github.com/JarbasAl))

## [1.62.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.62.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.61.0a1...1.62.0a1)

**Merged pull requests:**

- feat: ẽĩũ orthographic vowels + Barranquenho coda-nasalization [\#231](https://github.com/TigreGotico/orthography2ipa/pull/231) ([JarbasAl](https://github.com/JarbasAl))

## [1.61.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.61.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.60.1a2...1.61.0a1)

**Merged pull requests:**

- feat\(benchmarks\): barranquenho + mirandese synthetic IPA-dict gold rows [\#230](https://github.com/TigreGotico/orthography2ipa/pull/230) ([JarbasAl](https://github.com/JarbasAl))

## [1.60.1a2](https://github.com/TigreGotico/orthography2ipa/tree/1.60.1a2) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.60.1a1...1.60.1a2)

**Merged pull requests:**

- docs: when to refine the lattice vs fork the tokenizer [\#229](https://github.com/TigreGotico/orthography2ipa/pull/229) ([JarbasAl](https://github.com/JarbasAl))

## [1.60.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.60.1a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.60.0a1...1.60.1a1)

**Merged pull requests:**

- fix\(ci\): pin setup-uv to resolvable v7 in Pages workflow [\#227](https://github.com/TigreGotico/orthography2ipa/pull/227) ([JarbasAl](https://github.com/JarbasAl))

## [1.60.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.60.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.59.0a2...1.60.0a1)

**Merged pull requests:**

- feat: static language-data explorer for gh-pages [\#223](https://github.com/TigreGotico/orthography2ipa/pull/223) ([JarbasAl](https://github.com/JarbasAl))

## [1.59.0a2](https://github.com/TigreGotico/orthography2ipa/tree/1.59.0a2) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.59.0a1...1.59.0a2)

**Merged pull requests:**

- docs: front-page treatment for the pronunciation lattice \(B7\) [\#224](https://github.com/TigreGotico/orthography2ipa/pull/224) ([JarbasAl](https://github.com/JarbasAl))

## [1.59.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.59.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.58.1a1...1.59.0a1)

**Merged pull requests:**

- feat: per-word lattice confidence and OOV signal \(B5\) [\#221](https://github.com/TigreGotico/orthography2ipa/pull/221) ([JarbasAl](https://github.com/JarbasAl))

## [1.58.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.58.1a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.58.0a1...1.58.1a1)

**Merged pull requests:**

- fix\(data\): validate and correct Galician and Asturleonese phonology [\#217](https://github.com/TigreGotico/orthography2ipa/pull/217) ([JarbasAl](https://github.com/JarbasAl))

## [1.58.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.58.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.57.0a1...1.58.0a1)

**Merged pull requests:**

- feat\(data\): model Lisbon pre-palatal vowel centralization, reframe as deviating variety [\#218](https://github.com/TigreGotico/orthography2ipa/pull/218) ([JarbasAl](https://github.com/JarbasAl))

## [1.57.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.57.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.56.0a4...1.57.0a1)

**Merged pull requests:**

- feat\(data\): South/Central-West/North Brazilian Portuguese dialects [\#215](https://github.com/TigreGotico/orthography2ipa/pull/215) ([JarbasAl](https://github.com/JarbasAl))

## [1.56.0a4](https://github.com/TigreGotico/orthography2ipa/tree/1.56.0a4) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.56.0a3...1.56.0a4)

**Merged pull requests:**

- docs: add navigation footers to Basque language pages [\#212](https://github.com/TigreGotico/orthography2ipa/pull/212) ([JarbasAl](https://github.com/JarbasAl))

## [1.56.0a3](https://github.com/TigreGotico/orthography2ipa/tree/1.56.0a3) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.56.0a2...1.56.0a3)

**Merged pull requests:**

- docs: timeless standalone concept pages with navigation footers [\#208](https://github.com/TigreGotico/orthography2ipa/pull/208) ([JarbasAl](https://github.com/JarbasAl))

## [1.56.0a2](https://github.com/TigreGotico/orthography2ipa/tree/1.56.0a2) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.56.0a1...1.56.0a2)

**Merged pull requests:**

- docs: timeless standalone language pages with navigation footers [\#207](https://github.com/TigreGotico/orthography2ipa/pull/207) ([JarbasAl](https://github.com/JarbasAl))

## [1.56.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.56.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.55.0a1...1.56.0a1)

**Merged pull requests:**

- feat\(data\): validate Basque dialects and add Roncalese \(Erronkariera\) [\#206](https://github.com/TigreGotico/orthography2ipa/pull/206) ([JarbasAl](https://github.com/JarbasAl))

## [1.55.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.55.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.54.0a1...1.55.0a1)

**Merged pull requests:**

- feat\(data\): Aragonese Pyrenean valley subdialects \(Ansotano, Cheso, Chistabín, Belsetán, Tensino\) [\#204](https://github.com/TigreGotico/orthography2ipa/pull/204) ([JarbasAl](https://github.com/JarbasAl))

## [1.54.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.54.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.53.0a1...1.54.0a1)

**Merged pull requests:**

- feat\(data\): scaffold Latin American Spanish regional stubs, adstrates, and ancestry chains [\#201](https://github.com/TigreGotico/orthography2ipa/pull/201) ([JarbasAl](https://github.com/JarbasAl))

## [1.53.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.53.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.52.0a1...1.53.0a1)

## [1.52.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.52.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.51.0a1...1.52.0a1)

**Merged pull requests:**

- feat\(data\): model Carioca, Fluminense and Mineiro Brazilian Portuguese [\#199](https://github.com/TigreGotico/orthography2ipa/pull/199) ([JarbasAl](https://github.com/JarbasAl))
- feat\(data\): research-grounded Iraqi Arabic \(gilit Baghdadi and qeltu Northern\) [\#198](https://github.com/TigreGotico/orthography2ipa/pull/198) ([JarbasAl](https://github.com/JarbasAl))

## [1.51.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.51.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.50.0a1...1.51.0a1)

**Merged pull requests:**

- feat\(data\): model Paulistano, Caipira and Paranaense Brazilian Portuguese [\#196](https://github.com/TigreGotico/orthography2ipa/pull/196) ([JarbasAl](https://github.com/JarbasAl))

## [1.50.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.50.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.49.0a1...1.50.0a1)

**Merged pull requests:**

- feat\(data\): research-grounded Angolan, Cape Verdean and Mozambican Portuguese [\#191](https://github.com/TigreGotico/orthography2ipa/pull/191) ([JarbasAl](https://github.com/JarbasAl))

## [1.49.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.49.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.48.0a1...1.49.0a1)

**Merged pull requests:**

- feat\(data\): model Minho, Alfena, Beira and Aveiro European Portuguese dialects [\#182](https://github.com/TigreGotico/orthography2ipa/pull/182) ([JarbasAl](https://github.com/JarbasAl))

## [1.48.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.48.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.47.0a1...1.48.0a1)

**Merged pull requests:**

- feat\(data\): research-grounded Macau and East-Timorese Portuguese [\#189](https://github.com/TigreGotico/orthography2ipa/pull/189) ([JarbasAl](https://github.com/JarbasAl))

## [1.47.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.47.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.46.1a1...1.47.0a1)

**Merged pull requests:**

- feat\(data\): add Uruguayan Portuguese \(Riverense / DPU\) [\#188](https://github.com/TigreGotico/orthography2ipa/pull/188) ([JarbasAl](https://github.com/JarbasAl))

## [1.46.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.46.1a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.46.0a1...1.46.1a1)

**Merged pull requests:**

- fix\(benchmark\): fold apical/laminal place diacritics in broad-mode scoring [\#187](https://github.com/TigreGotico/orthography2ipa/pull/187) ([JarbasAl](https://github.com/JarbasAl))

## [1.46.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.46.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.45.0a1...1.46.0a1)

**Merged pull requests:**

- feat\(data\): research-grounded Gulf Arabic dialects \(Emirati, Bahraini, Kuwaiti, Qatari, Omani\) [\#183](https://github.com/TigreGotico/orthography2ipa/pull/183) ([JarbasAl](https://github.com/JarbasAl))

## [1.45.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.45.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.44.0a2...1.45.0a1)

**Merged pull requests:**

- feat\(data\): add Kabyle Berber ancestry chain and stub ancestor specs [\#184](https://github.com/TigreGotico/orthography2ipa/pull/184) ([JarbasAl](https://github.com/JarbasAl))

## [1.44.0a2](https://github.com/TigreGotico/orthography2ipa/tree/1.44.0a2) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.44.0a1...1.44.0a2)

**Merged pull requests:**

- chore: remove private DIALECT\_PATTERNS reference from EP-dialect gold docstring [\#181](https://github.com/TigreGotico/orthography2ipa/pull/181) ([JarbasAl](https://github.com/JarbasAl))

## [1.44.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.44.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.43.0a2...1.44.0a1)

**Merged pull requests:**

- feat\(data\): model Transmontano and Alto-Minhoto European Portuguese dialects [\#165](https://github.com/TigreGotico/orthography2ipa/pull/165) ([JarbasAl](https://github.com/JarbasAl))

## [1.43.0a2](https://github.com/TigreGotico/orthography2ipa/tree/1.43.0a2) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.43.0a1...1.43.0a2)

## [1.43.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.43.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.42.1a1...1.43.0a1)

**Merged pull requests:**

- chore: regenerate scoreboard.md to match results.json [\#177](https://github.com/TigreGotico/orthography2ipa/pull/177) ([JarbasAl](https://github.com/JarbasAl))
- feat\(data\): add Kabyle \(Taqbaylit\) Berber language spec [\#173](https://github.com/TigreGotico/orthography2ipa/pull/173) ([JarbasAl](https://github.com/JarbasAl))
- feat\(data\): research-grounded Levantine Arabic dialects \(Damascene, Beiruti, Ammani, Palestinian\) [\#171](https://github.com/TigreGotico/orthography2ipa/pull/171) ([JarbasAl](https://github.com/JarbasAl))

## [1.42.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.42.1a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.42.0a1...1.42.1a1)

**Merged pull requests:**

- fix\(data\): correct fabricated Cintra citation in Alentejano spec [\#172](https://github.com/TigreGotico/orthography2ipa/pull/172) ([JarbasAl](https://github.com/JarbasAl))

## [1.42.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.42.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.41.0a1...1.42.0a1)

**Merged pull requests:**

- feat\(data\): model Açoriano and Madeirense European Portuguese dialects [\#168](https://github.com/TigreGotico/orthography2ipa/pull/168) ([JarbasAl](https://github.com/JarbasAl))

## [1.41.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.41.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.40.0a1...1.41.0a1)

**Merged pull requests:**

- feat\(types\): add palatal-consonant grapheme positions and allophone class [\#169](https://github.com/TigreGotico/orthography2ipa/pull/169) ([JarbasAl](https://github.com/JarbasAl))

## [1.40.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.40.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.39.0a1...1.40.0a1)

**Merged pull requests:**

- feat\(data\): model Lisbon \(Estremenho\) European Portuguese dialect [\#166](https://github.com/TigreGotico/orthography2ipa/pull/166) ([JarbasAl](https://github.com/JarbasAl))

## [1.39.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.39.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.38.0a2...1.39.0a1)

**Merged pull requests:**

- feat\(data\): model Alentejano and Algarvio European Portuguese dialects [\#159](https://github.com/TigreGotico/orthography2ipa/pull/159) ([JarbasAl](https://github.com/JarbasAl))

## [1.38.0a2](https://github.com/TigreGotico/orthography2ipa/tree/1.38.0a2) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.38.0a1...1.38.0a2)

**Merged pull requests:**

- chore: cite Cintra 1971 in place of private dialect-transform whitepaper [\#163](https://github.com/TigreGotico/orthography2ipa/pull/163) ([JarbasAl](https://github.com/JarbasAl))

## [1.38.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.38.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.37.0a1...1.38.0a1)

## [1.37.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.37.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.36.1a1...1.37.0a1)

**Merged pull requests:**

- feat\(data\): research-grounded Barranquenho \(Portuguese-Spanish contact variety\) [\#158](https://github.com/TigreGotico/orthography2ipa/pull/158) ([JarbasAl](https://github.com/JarbasAl))
- feat\(data\): model Porto European Portuguese dialect [\#157](https://github.com/TigreGotico/orthography2ipa/pull/157) ([JarbasAl](https://github.com/JarbasAl))
- feat\(data\): research-grounded Mirandese phonology \(mwl + Sendinese + Ifanes\) [\#156](https://github.com/TigreGotico/orthography2ipa/pull/156) ([JarbasAl](https://github.com/JarbasAl))

## [1.36.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.36.1a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.36.0a1...1.36.1a1)

**Merged pull requests:**

- fix\(data\): correct Catalan vowel reduction \(stress-conditioned\) and add spirantization [\#152](https://github.com/TigreGotico/orthography2ipa/pull/152) ([JarbasAl](https://github.com/JarbasAl))

## [1.36.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.36.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.35.0a1...1.36.0a1)

**Merged pull requests:**

- feat\(data\): model European Portuguese allophony \(pt-PT\) [\#148](https://github.com/TigreGotico/orthography2ipa/pull/148) ([JarbasAl](https://github.com/JarbasAl))

## [1.35.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.35.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.34.0a2...1.35.0a1)

**Merged pull requests:**

- feat\(data\): research-grounded Ligurian \(Genoese\) spec from grafia ofiçiâ [\#151](https://github.com/TigreGotico/orthography2ipa/pull/151) ([JarbasAl](https://github.com/JarbasAl))

## [1.34.0a2](https://github.com/TigreGotico/orthography2ipa/tree/1.34.0a2) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.34.0a1...1.34.0a2)

**Merged pull requests:**

- docs\(benchmarks\): document gold-data provenance and reliability caveats [\#149](https://github.com/TigreGotico/orthography2ipa/pull/149) ([JarbasAl](https://github.com/JarbasAl))

## [1.34.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.34.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.33.0a1...1.34.0a1)

**Merged pull requests:**

- feat\(data\): model Brazilian Portuguese allophony \(pt-BR\) [\#147](https://github.com/TigreGotico/orthography2ipa/pull/147) ([JarbasAl](https://github.com/JarbasAl))
- feat\(data\): research-grounded MSA, Egyptian, and Saudi Arabic phonology [\#146](https://github.com/TigreGotico/orthography2ipa/pull/146) ([JarbasAl](https://github.com/JarbasAl))
- feat\(scripts\): compare Catalan dialects vs BSC espeak + pycotovia/pyahotts [\#145](https://github.com/TigreGotico/orthography2ipa/pull/145) ([JarbasAl](https://github.com/JarbasAl))

## [1.33.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.33.0a1) (2026-07-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.32.0a1...1.33.0a1)

**Merged pull requests:**

- feat\(engine\): apply context-conditioned allophone rules as post-lexical rescorer \(B8\) [\#143](https://github.com/TigreGotico/orthography2ipa/pull/143) ([JarbasAl](https://github.com/JarbasAl))

## [1.32.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.32.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.31.0a1...1.32.0a1)

## [1.31.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.31.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.30.0a1...1.31.0a1)

## [1.30.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.30.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.29.0a1...1.30.0a1)

## [1.29.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.29.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.28.0a1...1.29.0a1)

## [1.28.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.28.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.27.0a1...1.28.0a1)

## [1.27.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.27.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.26.0a1...1.27.0a1)

## [1.26.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.26.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.25.0a1...1.26.0a1)

## [1.25.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.25.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.24.0a1...1.25.0a1)

## [1.24.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.24.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.23.0a1...1.24.0a1)

## [1.23.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.23.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.22.2a2...1.23.0a1)

## [1.22.2a2](https://github.com/TigreGotico/orthography2ipa/tree/1.22.2a2) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.22.2a1...1.22.2a2)

## [1.22.2a1](https://github.com/TigreGotico/orthography2ipa/tree/1.22.2a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.22.1a1...1.22.2a1)

## [1.22.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.22.1a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.22.0a1...1.22.1a1)

## [1.22.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.22.0a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.21.2a1...1.22.0a1)

## [1.21.2a1](https://github.com/TigreGotico/orthography2ipa/tree/1.21.2a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.21.1a1...1.21.2a1)

## [1.21.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.21.1a1) (2026-07-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.21.0a1...1.21.1a1)

## [1.21.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.21.0a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.20.0a1...1.21.0a1)

## [1.20.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.20.0a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.19.1a1...1.20.0a1)

## [1.19.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.19.1a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.19.0a1...1.19.1a1)

## [1.19.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.19.0a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.18.0a1...1.19.0a1)

## [1.18.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.18.0a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.17.0a1...1.18.0a1)

## [1.17.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.17.0a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.16.0a1...1.17.0a1)

## [1.16.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.16.0a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.15.2a1...1.16.0a1)

## [1.15.2a1](https://github.com/TigreGotico/orthography2ipa/tree/1.15.2a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.15.1a1...1.15.2a1)

## [1.15.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.15.1a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.15.0a1...1.15.1a1)

## [1.15.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.15.0a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.14.0a1...1.15.0a1)

## [1.14.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.14.0a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.13.1a2...1.14.0a1)

## [1.13.1a2](https://github.com/TigreGotico/orthography2ipa/tree/1.13.1a2) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.13.1a1...1.13.1a2)

## [1.13.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.13.1a1) (2026-07-09)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.13.0a1...1.13.1a1)

## [1.13.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.13.0a1) (2026-06-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.12.0a1...1.13.0a1)

## [1.12.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.12.0a1) (2026-06-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.11.0a1...1.12.0a1)

## [1.11.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.11.0a1) (2026-06-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.10.0a1...1.11.0a1)

## [1.10.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.10.0a1) (2026-06-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.9.0a1...1.10.0a1)

## [1.9.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.9.0a1) (2026-06-12)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.8.1a1...1.9.0a1)

## [1.8.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.8.1a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.8.0a1...1.8.1a1)

## [1.8.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.8.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.7.0a1...1.8.0a1)

## [1.7.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.7.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.6.0a2...1.7.0a1)

## [1.6.0a2](https://github.com/TigreGotico/orthography2ipa/tree/1.6.0a2) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.6.0a1...1.6.0a2)

## [1.6.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.6.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.5.0a1...1.6.0a1)

## [1.5.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.5.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.4.0a1...1.5.0a1)

## [1.4.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.4.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.3.1a2...1.4.0a1)

## [1.3.1a2](https://github.com/TigreGotico/orthography2ipa/tree/1.3.1a2) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.3.1a1...1.3.1a2)

## [1.3.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.3.1a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.3.0a1...1.3.1a1)

## [1.3.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.3.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.2.0a1...1.3.0a1)

## [1.2.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.2.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.1.3a1...1.2.0a1)

## [1.1.3a1](https://github.com/TigreGotico/orthography2ipa/tree/1.1.3a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.1.2a1...1.1.3a1)

## [1.1.2a1](https://github.com/TigreGotico/orthography2ipa/tree/1.1.2a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.1.1a1...1.1.2a1)

## [1.1.1a1](https://github.com/TigreGotico/orthography2ipa/tree/1.1.1a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.1.0a1...1.1.1a1)

## [1.1.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.1.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/1.0.0a1...1.1.0a1)

## [1.0.0a1](https://github.com/TigreGotico/orthography2ipa/tree/1.0.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/0.7.0a1...1.0.0a1)

## [0.7.0a1](https://github.com/TigreGotico/orthography2ipa/tree/0.7.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/0.6.0a1...0.7.0a1)

## [0.6.0a1](https://github.com/TigreGotico/orthography2ipa/tree/0.6.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/0.5.0a1...0.6.0a1)

## [0.5.0a1](https://github.com/TigreGotico/orthography2ipa/tree/0.5.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/0.4.0a1...0.5.0a1)

## [0.4.0a1](https://github.com/TigreGotico/orthography2ipa/tree/0.4.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/0.3.0a1...0.4.0a1)

## [0.3.0a1](https://github.com/TigreGotico/orthography2ipa/tree/0.3.0a1) (2026-06-11)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/0.2.1a1...0.3.0a1)

## [0.2.1a1](https://github.com/TigreGotico/orthography2ipa/tree/0.2.1a1) (2026-06-10)

[Full Changelog](https://github.com/TigreGotico/orthography2ipa/compare/73cf93d2bc10be1e32a61e00a380c4ed632a0148...0.2.1a1)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
