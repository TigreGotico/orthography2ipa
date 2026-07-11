# Uruguayan Portuguese (pt-UY) — Riverense / DPU Phonology Reference

**Code**: `pt-UY` | **Family**: Romance | **Script**: Latin (alphabet)
**Parent**: `pt-BR` | **Quality tier**: research | **ISO 639-3**: `por`
**Sources**: Carvalho (1998), *Variation and diffusion of Uruguayan Portuguese in a bilingual border town*; Rona (1965), *El dialecto fronterizo del Norte del Uruguay*; Hensey (1972), *The Sociolinguistics of the Brazilian-Uruguayan Border*; Elizaincín (1992), *Dialectos en Contacto*; Sturza (2021)

Uruguayan Portuguese is the Portuguese-based border-contact vernacular of
northern Uruguay — the Rivera region and the Brazilian frontier. The scholarly
literature names it **Dialectos Portugueses del Uruguay** (DPU, Elizaincín),
**fronterizo** (Rona), and **Riverense**; speakers themselves call it
**portuñol** or *brasilero*. It is **not** Uruguay's national language (that is
Spanish): it is a rural-origin Portuguese vernacular in intense contact with
border Spanish, historically the sole language of the border communities and now
diglossic (Carvalho 1998: 642; Elizaincín 1992).

---

## Parent and ancestry

The spec sets `parent = pt-BR` and inherits Brazilian Portuguese through
`graphemes_base`, `allophones_base` and `positional_graphemes_base`. This is the
choice the read source supports: Carvalho (1998: 646, Figure 1) models the
community as a **dialectal continuum** whose two poles are *Rural Uruguayan
Portuguese* (RUP) and *Urban Brazilian Portuguese* (UBP), and states that the
variety differs from standard Brazilian "mainly in three respects" — retained
rural features, Spanish interference, and hybrid forms. The reference/diffusion
norm toward which Rivera speech moves is urban BP. The **vowel system** is
inherited unchanged from pt-BR (seven oral vowels /a ɛ e i ɔ o u/ plus the nasal
set), matching the inventory reported for the variety.

| Ancestor | Role | Why |
|:---|:---|:---|
| `pt-BR` | parent | structural base + diffusion norm; vowels and most maps inherited (Carvalho 1998: 646) |
| `es-UY` | adstrate | border Spanish; source of dental-stop retention, alveolar trill, coda-/l/ retention (Carvalho 1998: 646; Elizaincín 1992) |
| `pt-PT` | substrate | historical rural European Portuguese of the original settlers (Carvalho 1998: 642) |

## Modelled features

1. **Vocalisation of the palatal lateral ⟨lh⟩ /ʎ/ → glide [j]** — the single most
   salient rural/focused marker. Rona (1965: 23, via Carvalho 1998: 646) found it
   categorical and proposed the glide as the only phoneme: *"the pronunciation of
   the lateral phoneme as a front glide, as in /mujɛ/ instead of the standard
   /muʎɛr/"* (Carvalho 1998: 646); local *coié* vs Brazilian *colher* (p. 647).
   The palatal [ʎ] is the diffusing urban-BP form, kept as the second candidate.
   → *mulher* [muˈjeɾ], *trabalho* [tɾaˈbaju].
2. **Retention of dental /t d/ before /i/ (no palatalisation)** — *"the maintenance
   of the dental stops /d/ and /t/ followed by /i/, a tendency kept probably due
   to Spanish interference"* (Carvalho 1998: 646). The dental realisation was
   *nearly categorical* in Rivera (Rona 1965: 40; Hensey 1972: 60, both via
   Carvalho 1998: 648). Standard-BP palatalisation ([dʒia]/[tʃia]) is an ongoing
   diffusion led by young, higher-status, female speakers (Carvalho 1998: 649,
   Tables 4–6) — documented here, not made the focused-variety default.
   → *dia* [ˈdiɐ], *tia* [ˈtiɐ], *partido* [paˈɾtidu].
3. **Lateral retention of coda /l/ → [l]** (no L-vocalisation to [w] as in urban
   BP) — *secondary* source (Wikipedia, *Uruguayan Portuguese*), consistent with
   the Spanish adstrate. Overrides the inherited pt-BR coda /l/ → [w].
   → *Brasil* [bɾaˈzil], *alto* [ˈaltu].
4. **Word-initial ⟨r⟩ and ⟨rr⟩ = alveolar trill [r]** (not the guttural/uvular
   [ʁ] of urban BP) — *secondary* source (Wikipedia), consistent with border
   Spanish. Intervocalic and coda ⟨r⟩ stay the tap [ɾ].
   → *Rivera* [riˈveɾɐ], *carro* [ˈkaru].

## Worked examples

| Orthography | IPA | Features shown |
|:---|:---|:---|
| `mulher` | muˈjeɾ | ⟨lh⟩ → glide [j] |
| `trabalho` | tɾaˈbaju | ⟨lh⟩ → glide [j] |
| `dia` | ˈdiɐ | dental /d/ before /i/ (no [dʒ]) |
| `tia` | ˈtiɐ | dental /t/ before /i/ (no [tʃ]) |
| `Brasil` | bɾaˈzil | coda /l/ retained as [l] |
| `carro` | ˈkaru | ⟨rr⟩ → alveolar trill [r] |

## What is deliberately not modelled (research-grounding)

- **Coda /s/** is left inherited from pt-BR (alveolar [s]). Carvalho's
  quantitative /s/-aspiration work concerns border **Spanish**, not clearly the
  Portuguese variety, so no [h] aspiration is imposed without a primary source
  documenting it for the Portuguese.
- **No betacism**: unlike Barranquenho, DPU keeps /v/ (*vida* [ˈvidɐ]).
- Fine pretonic vocalism and any DPU-specific nasal-vowel detail beyond the
  inherited pt-BR set are not quantified in the read sources and are left
  inherited rather than invented.

## Input contract

Input is standard Portuguese orthography (as used for the variety in the
literature and in written *portuñol*). The spec transcribes the **focused, rural
local norm** described by Rona, Hensey and Carvalho; the palatalising /
guttural-r urban-BP variants are the diffusion pole of the continuum, documented
in the notes rather than produced by default.

## Limitations

- **No gold benchmark**: pt-UY has no scoreboard row; correctness here is by
  citation, not PER (precedent: `ext-PT-x-barrancos`).
- Features 3–4 rest on a secondary source (Wikipedia); the two headline features
  (1–2) are primary (Carvalho 1998, page-cited).
- Sociolinguistic variation along the RUP↔UBP continuum is real and gradient;
  the spec fixes the focused-local pole and notes the diffusion.

## Sources

- Carvalho, Ana Maria (1998). "Variation and diffusion of Uruguayan Portuguese in
  a bilingual border town". *Actas do I Simposio Internacional sobre o
  Bilingüismo*, Universidade de Vigo, pp. 642–651.
  <https://ssl.webs.uvigo.es/actas1997/05/Carvalho.pdf>
- Rona, José Pedro (1965). *El dialecto fronterizo del Norte del Uruguay*.
  Montevideo: Universidad de la República (cited via Carvalho 1998).
- Hensey, Fritz (1972). *The Sociolinguistics of the Brazilian-Uruguayan Border*.
  The Hague: Mouton (cited via Carvalho 1998).
- Elizaincín, Adolfo (1992). *Dialectos en Contacto. Español y Portugués en
  España y América*. Montevideo: Arca (framework via Carvalho 1998).
- Sturza, Eliana Rosa (2021). "Português do Uruguai e Português de Missões:
  língua, território e fronteira". *Línguas e Instrumentos Linguísticos* 24(48),
  177–198. <https://doi.org/10.20396/lil.v24i48.8667912>
