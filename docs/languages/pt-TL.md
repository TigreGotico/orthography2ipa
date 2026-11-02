# East Timorese Portuguese (pt-TL)

| Field | Value |
|:---|:---|
| Code | `pt-TL` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | research |
| Parent | `pt-PT` |
| Primary source | Albuquerque, D. B. (2010), *Peculiaridades prosódicas do português falado em Timor Leste*, ReVEL 8(15):270-285, read in full |

East Timorese Portuguese (*Português de Timor Leste*, PTL) is a co-official language of Timor-Leste, with Tetum. It is a second-language, official variety for nearly the whole population. Albuquerque (2010:272) cites the 2001 Human Development Report: about 5 % of the population is fluent, against more than 80 % who speak Tetum. The spec `ancestors` list Tetum (`tet`) and Indonesian (`id`) as adstrates.

Albuquerque (2010:273, fig. 1) draws a continuum. At one end is the *norma europeia* of highly schooled urban speakers in Dili and Baucau. They use it in formal domains such as law, the university and the church. At the other end is the *português acrioulado* of rural speakers, with heavy transfer from their first language. The spec models the acrolectal end, the one that follows the norm.

Every transcription in `code` form on this page is real output of `orthography2ipa.transcribe(text, code)`. Forms in italics are quoted from the source. For the scores of the spec, see [../scoreboard.md](../scoreboard.md).

## Not a creole

PTL is not a creole based on Portuguese. The creoles of the region are separate contact languages:

- Bidau Creole Portuguese of Dili, which is moribund. Baxter (1990), *Notes on the Creole Portuguese of Bidau, Timor*, JPCL 5(1):1-38.
- The creoles of Macau and Malacca (Kristang) nearby.

Albuquerque (2010:275) argues that these Asian Portuguese creoles influenced PTL in its history. PTL itself is an emerging variety of Portuguese. Albuquerque calls it *"uma variedade não-nativa do português da Europa, como o Português de Moçambique … o Português de Angola"* (2010:274).

## Modelled features

Every feature comes from Albuquerque (2010).

| Feature | What the spec does | Evidence (page) |
|:---|:---|:---|
| No unstressed vowel reduction | unstressed ⟨a e o⟩ give [a e o], not [ɐ ɨ u] | *"as vogais dessas línguas … não sofrem lenição … bate [ˈba.te], roda [ˈɾɔ.da], enredo [enˈe.dɔ]"* (p. 275, fn. 7) |
| Alveolar rhotic | ⟨r rr⟩ give [r]. The tap [ɾ] stays between vowels and word-finally. No [ʁ] | *perguntar* [peˈgun.ta] (p. 278) |
| Digraph simplification | ⟨lh nh⟩ give [l n] first. [ʎ ɲ] are second, for speakers near the European norm | *olho* [ˈo.liu], *espelho* [esˈpe.lu], *vinho* [ˈbi.niu], *rascunho* [rasˈku.niu] (p. 276) |
| Alveolar coda /s/ | coda /s z/ stay alveolar, as overrides of `PT_CODA_S_HUSH` and `PT_CODA_Z_HUSH` by id | *escola* [isˈkɔ.la] ~ [iʃˈkɔ.la], variable (p. 277) |
| Paroxytone stress | stress from the spelling. The notes record the Austronesian stress on the penult | *"o acento primário predominantemente na penúltima sílaba … quase completa ausência de proparoxítonas"* (pp. 279-280) |

The main feature is the absence of vowel reduction. The parent `pt-PT` gives `bate` [ˈbatɨ] and `roda` [ˈʁɔdɐ]. The spec `pt-TL` gives `bate` [ˈbate] and `roda` [ˈrɔda], with full vowels. The stressed open vowels stay open: `roda` [ˈrɔda], `mesa` [ˈmɛza]. Albuquerque describes this trait of the Tetum and Austronesian substrate as the most consistent property of PTL.

The other features in the spec output: `olho` [ˈɔlo], `vinho` [ˈvino], `escola` [esˈkɔla], `perguntar` [perɡũˈtaɾ], `carro` [ˈkaro].

The spec also switches off the `pt-PT` suffix and word-list rules for stressed vowel height and the ⟨-em⟩ nucleus rules. Their notes say that no source for these endings in Timor-Leste was read, or that the variety keeps the close-mid nasal nucleus. So `bem` is [ˈbẽj̃].

## Documented but not modelled

Albuquerque attests the features below, but they belong to the basilectal *acrioulado* end or go beyond the base engine. The spec records them in its `notes` and does not encode them.

- Consonant substitutions ʃ→s, ʒ→z, v→b, f→p, and vowel raising e→i, o→u (pp. 276-277): *chegar* [seˈga], *já* [za]~[dʒa], *livro* [ˈli.bu], *força* [ˈpu.sa], *chave* [ˈsa.bi], *soletrar* [suˈle.ta]. They come from transfer from the first language and vary too much to encode as the acrolectal norm.
- Denasalisation of nasal diphthongs: *educação* [e.du.kaˈsa.u] (p. 278).
- Loss of a final consonant, mostly in infinitives: *abraçar* [aˈba.sa], *cair* [kai], *ajudar* [aˈzu.da] (pp. 278-279). This is a deletion that the allophone layer of the engine does not express.
- Metathesis and epenthesis: *perguntar* [peˈgun.ta], *advogado* [a.di.boˈga.do] (p. 278).
- The H-L% phrasal intonation of the Timoric sprachbund (p. 281, Himmelmann 2008 on Waima'a). It is prosodic and outside the base scope.

## Tier and gold

The spec is at the research tier, not the production tier. It rests on one fully read primary source on phonology and prosody (Albuquerque 2010). The European inventory is its baseline (Mateus & d'Andrade 2000, quoted through Albuquerque 2010:276).

The `pt-TL-x-dili` region of the `portuguese_unified` gold is scored against this spec. The board classifies it `machine-generated`, not `lexicon-derived`. Diffed word for word against `pt-PT-x-lisboa`, it is a near-total one-to-one character substitution of the Lisbon entries (ɐ→ə, u→ʊ, ʀ→r, ɫ→w, d→ð, g→ɣ). It is not independent Timorese lexicography.

A new symbol for the reduced vowel does not remove the reduction. Many rows of `pt-TL-x-dili` still have a reduced [ə] or a reduced final [ʊ]. The coda /s/ is still the Lisbon *chiado* [ʃ]: the gold gives *instrumentista* as [ĩʃtɾumẽntˈiʃtə]. The primary source of this spec documents the opposite (Albuquerque 2010:275 fn. 7, 277). East Timorese Portuguese has no reduction of unstressed vowels and an alveolar coda /s/. The `audit.portuguese_unified` entry of the spec records this as a mislabelled gold.

So the row measures agreement with a re-symbolised European Portuguese, not with the acrolectal variety that the spec models. Its PER says nothing about the spec. The row meets the production size bar of n ≥ 500 in row count only, not in reliability. It still gates, as [../benchmark_datasets.md](../benchmark_datasets.md) explains.

## Sources

- Albuquerque, D. B. (2010). *Peculiaridades prosódicas do português falado em Timor Leste*. ReVEL 8(15):270-285. The primary source, read in full.
- Baxter, A. N. (1990). *Notes on the Creole Portuguese of Bidau, Timor*. JPCL 5(1):1-38. The separate Bidau creole.
- Hull, G. (2001). *A Morphological Overview of the Timoric Sprachbund*. Studies in Language and Culture of East Timor 4:98-205.
- Mateus, M. H. & d'Andrade, E. (2000). *The Phonology of Portuguese*. OUP. The European baseline, through Albuquerque (2010:276).
- Thomaz, L. F. F. R. (2002). *Babel Loro Sa'e*. Instituto Camões.

---
[← Macau Portuguese](pt-MO.md) · [Home](../index.md) · [Uruguayan Portuguese →](pt-UY.md)
