# East Timorese Portuguese (pt-TL) — Phonology Reference

**Code**: `pt-TL` | **Family**: Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Parent**: `pt-PT`
**Primary source**: Albuquerque, D. B. (2010), *Peculiaridades prosódicas do
português falado em Timor Leste*, ReVEL 8(15):270–285 — **read in full**.

East Timorese Portuguese (*Português de Timor Leste*, PTL) is the co-official
language of Timor-Leste alongside Tetum. It is an **L2/official variety** for
nearly the whole population — the 2001 Human Development Report cited by
Albuquerque (2010:272) records only ~5% fluent, against >80% who speak Tetum.
This spec models the **acrolectal / norm-oriented** end of the continuum
Albuquerque (2010:273, fig.1) draws between *norma europeia* (urban
Dili/Baucau, highly-schooled speakers, formal domains: law, university,
church) and *português acrioulado* (rural, heavy L1 transfer).

## Not a creole

PTL is **not** a Portuguese-based creole. The region's creoles are separate
contact languages, modelled elsewhere:

- **Bidau Creole Portuguese** of Dili (moribund) — Baxter (1990), *Notes on
  the Creole Portuguese of Bidau, Timor*, JPCL 5(1):1–38.
- The neighbouring **Macau** and **Malacca (Kristang)** creoles.

Albuquerque (2010:275) argues these Asian Portuguese creoles influenced PTL
historically, but PTL itself is an emerging *variety* of Portuguese, "uma
variedade não-nativa do português da Europa, como o Português de Moçambique
… o Português de Angola" (2010:274).

## Modelled features (all Albuquerque 2010)

| Feature | What the spec does | Evidence (page) |
|:---|:---|:---|
| **No unstressed vowel reduction** | unstressed a→[a], e→[e], o→[o]; overrides inherited EP schwa/[ɨ] reduction | "as vogais dessas línguas … não sofrem lenição … bate [ˈba.te], roda [ˈɾɔ.da], enredo [enˈe.dɔ]" (p.275, fn.7) |
| **Alveolar rhotic** | ⟨r rr⟩ → [r]/[ɾ]; EP uvular [ʁ] absent | perguntar [peˈgun.ta] (p.278) |
| **Digraph simplification** | ⟨lh⟩→[l], ⟨nh⟩→[n] as first variant ([ʎ]/[ɲ] survive only near the European norm) | olho [ˈo.liu], espelho [esˈpe.lu]; vinho [ˈbi.niu], rascunho [rasˈku.niu] (p.276) |
| **Alveolar coda /s/** | coda /s z/ stay alveolar (no obligatory Lisbon *chiado*); overrides `PT_CODA_S_HUSH`/`PT_CODA_Z_HUSH` by id | escola [isˈkɔ.la] ~ [iʃˈkɔ.la] — variable (p.277) |
| **Paroxytone stress tendency** | inherited AO1990 stress; note documents Austronesian penult reinforcement | "o acento primário predominantemente na penúltima sílaba … quase completa ausência de proparoxítonas" (pp.279–280) |

The headline feature is the **absence of vowel reduction**: where the parent
`pt-PT` gives `bate` → [ˈbatɨ] and `roda` → [ˈʁɔdɐ], `pt-TL` gives
[ˈbate] and [ˈrɔda] — full vowels, with the EP **stressed** open/close
contrast preserved (roda [ɔ], mesa [ɛ]). This is the Tetum/Austronesian
substrate trait Albuquerque documents as the most consistent property of PTL.

## Documented but NOT modelled (honest limits)

These are attested in Albuquerque but confined to the *acrioulado* (basilectal)
end or exceed the base engine's capabilities, so they are recorded in the spec
`notes` rather than encoded:

- **Consonant substitutions** ʃ→s, ʒ→z, v→b, f→p and **vowel raising** e→i,
  o→u (p.276–277: chegar [seˈga], já [za]~[dʒa], livro [ˈli.bu], força
  [ˈpu.sa], chave [ˈsa.bi], soletrar [suˈle.ta]) — L1-transfer, too variable
  to encode as the acrolectal norm.
- **Denasalisation** of nasal diphthongs: educação [e.du.kaˈsa.u] (p.278).
- **Final-consonant apocope**, esp. in infinitives: abraçar [aˈba.sa], cair
  [kai], ajudar [aˈzu.da] (p.278–279) — a **deletion** the engine's allophone
  layer does not express; documented engine limit.
- **Metathesis / epenthesis**: perguntar [peˈgun.ta], advogado
  [a.di.boˈga.do] (p.278).
- **H–L% phrasal intonation** from the Timoric sprachbund (p.281; Himmelmann
  2008 on Waima'a) — prosodic, out of base scope.

## Tier rationale

`research`, not `production`: grounded in one fully-read primary
phonological/prosodic source (Albuquerque 2010) plus the EP inventory baseline
(Mateus & d'Andrade 2000, quoted via Albuquerque 2010:276). **No gold
benchmark** exists for this small L2 variety, so PER cannot be measured — the
production bar (gold n≥500) is unreachable at present.

## Sources

- Albuquerque, D. B. (2010). *Peculiaridades prosódicas do português falado
  em Timor Leste*. ReVEL 8(15):270–285. (primary, read in full)
- Baxter, A. N. (1990). *Notes on the Creole Portuguese of Bidau, Timor*.
  JPCL 5(1):1–38. (the separate Bidau creole)
- Hull, G. (2001). *A Morphological Overview of the Timoric Sprachbund*.
  Studies in Language and Culture of East Timor 4:98–205.
- Mateus, M. H. & d'Andrade, E. (2000). *The Phonology of Portuguese*. OUP.
  (EP baseline; via Albuquerque 2010:276)
- Thomaz, L. F. F. R. (2002). *Babel Loro Sa'e*. Instituto Camões.
