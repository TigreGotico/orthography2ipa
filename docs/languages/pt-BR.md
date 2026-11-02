# Brazilian Portuguese (pt-BR)

| Field | Value |
|:---|:---|
| Code | `pt-BR` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | production |
| Parent | `pt-PT-x-medieval` |
| Sources | Barbosa & Albano (2004, JIPA), Câmara Jr. (1970), Mateus & d'Andrade (2000), Callou & Leite (2001), Cunha & Cintra (1984), Vigário (2003) |

`pt-BR` models the general Brazilian standard. It takes its grapheme, allophone and positional maps from `pt-PT-x-medieval` through the three `*_base` keys. Its `ancestors` add Old Tupi (`tpw`) as a substrate and Kimbundu (`kmb`) as an adstrate, for the lexicon. The regional Brazilian specs inherit from `pt-BR` and change only what their region changes. [pt-BR-dialects.md](pt-BR-dialects.md) describes them. Uruguayan Portuguese ([pt-UY.md](pt-UY.md)) is also a child of `pt-BR`. For a comparison with the other Romance languages, see [comparative.md](comparative.md).

Every transcription on this page is real output of `orthography2ipa.transcribe(text, "pt-BR")`. For the scores of the spec, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

## The two maps

The library models pronunciation as two maps (see [../engine/allophony.md](../engine/allophony.md)). The pre-lexical map goes from spelling to phoneme, in `positional_graphemes`. The post-lexical map goes from phoneme to surface allophone, in `allophone_rules`. `pt-BR` runs the post-lexical rules in two passes (`allophone_passes: 2`).

### Pre-lexical map

| Process | Rule | Example |
|:---|:---|:---|
| /t d/ affrication | ⟨t d⟩ give [t͡ʃ d͡ʒ] before ⟨i⟩ | `tio` [ˈt͡ʃiu], `dia` [ˈd͡ʒiɐ] |
| Coda /l/ vocalisation | ⟨l⟩ gives [w] before a consonant and at the end of a word | `sal` [ˈsaw], `alto` [ˈawtu] |
| Coda /s/ | ⟨s⟩ stays alveolar [s] in the coda | `mesmo` [ˈmesmu], `paz` [ˈpas] |
| Coda nasal | ⟨m n⟩ before a consonant or at the end of a word give a combining tilde (U+0303) | `campo` [ˈkɐ̃pu], `sim` [ˈsĩ], `mundo` [ˈmũdu] |
| Final unstressed vowels | ⟨a⟩ gives [ɐ], ⟨e o⟩ give the near-close [ɪ ʊ] | `capa` [ˈkapɐ] |
| Strong rhotic | word-initial ⟨r⟩ and ⟨rr⟩ give [ʁ] | `rato` [ˈʁatu], `carro` [ˈkaʁu] |

The *chiado* (coda /s/ to [ʃ]) belongs to Rio de Janeiro and some other regions, not to the general standard. So the base keeps an alveolar coda [s z], and the regional specs add the *chiado* where their sources report it.

### Post-lexical rules

| Rule ids | Process | Example |
|:---|:---|:---|
| `PT_NASAL_A_RAISE`, `PT_NASAL_E_RAISE`, `PT_NASAL_O_RAISE` | [a ɛ ɔ] give [ɐ e o] before the nasal tilde | `campo` [ˈkɐ̃pu], `tempo` [ˈtẽpu], `bom` [ˈbõ] |
| `BR_RAISE_FINAL_E`, `BR_RAISE_FINAL_O` | final [ɪ ʊ] give [i u] | `leite` [ˈlejt͡ʃi], `gato` [ˈɡatu] |
| `BR_RAISE_FINAL_ES`, `BR_RAISE_FINAL_OS` | unstressed ⟨e o⟩ give [i u] before a final ⟨-s⟩ | `leites` [ˈlejt͡ʃis], `gatos` [ˈɡatus] |
| `BR_AFFRIC_T_RAISED`, `BR_AFFRIC_D_RAISED` | /t d/ give [t͡ʃ d͡ʒ] before a raised [i ɪ] | `dente` [ˈdẽt͡ʃi], `tarde` [ˈtaɾd͡ʒi] |
| `BR_FINAL_EM_GLIDE`, `BR_FINAL_ENS_GLIDE` | final ⟨-em -en -ens⟩ give the diphthong [ẽj̃] | `bem` [ˈbẽj̃], `hífen` [ˈifẽj̃], `homens` [ˈomẽj̃s] |
| `BR_FINAL_AM_GLIDE` | final ⟨-am⟩ gives [ɐ̃w̃] | `falam` [ˈfalɐ̃w̃] |
| `PT_LEX_CLOSE_O`, `PT_LEX_CLOSE_E`, `PT_LEX_OPEN_O`, `PT_LEX_OPEN_E` | stressed mid-vowel height for listed words | `como` [ˈkomu], `forte` [ˈfɔɾt͡ʃi], `terra` [ˈtɛʁɐ] |
| `PT_LEX_X_S` | ⟨x⟩ is [s] in the stem ⟨troux-⟩ | `trouxe` [ˈtɾowsi] |
| `PT_INITIAL_EX_VOICED` | word-initial ⟨ex-⟩ before a vowel gives [ez] | `exame` [eˈzami] |

Each rule cites its sources in its `notes` field in `orthography2ipa/data/pt-BR.json`. The spec also has one word exception: the conjunction `e` is [i].

### Coda nasalisation

A vowel before a coda ⟨m n⟩ nasalises, and the nasal consonant goes (Mateus & d'Andrade 2000: ch. 2, Barbosa & Albano 2004). The positional map writes the coda ⟨m n⟩ as a combining tilde on the vowel before it. The three `PT_NASAL_*_RAISE` rules then set the vowel quality. They change the oral vowel under the tilde, so the tilde never doubles.

An onset ⟨m n⟩ between vowels leaves the vowel oral (`cama` [ˈkamɐ], `ano` [ˈanu]). The tokenizer reads ⟨nh⟩ first, so `banho` [ˈbaɲu] keeps its oral vowel.

The nasal diphthongs ⟨ão ãe õe⟩ are whole graphemes, and these rules do not touch them. The high vowels ⟨i u⟩ need no quality rule, because [ĩ ũ] share the oral bases [i u]. Brazilian Portuguese does not reduce an unstressed ⟨o⟩ to [u], so its ⟨o⟩ before a coda nasal is already [o] (`contar` [kõˈtaɾ], `bondade` [bõˈdad͡ʒi]). The European rule `PT_NASAL_O_UNRED` is therefore not part of this spec.

A guard in `PhonetokTokenizer._expand_beam` (`orthography2ipa/phonetok.py`) keeps a tilde only when it falls on an oral vowel or a glide. On any other segment, the tokenizer drops that branch and keeps the nasal consonant. This stops a doubled tilde on ⟨nn⟩ in loans: `inn` [ˈĩn], `Finn` [ˈfĩn].

### Final vowels and affrication

Word-final unstressed /e o/ raise to the close vowels [i u] (Barbosa & Albano 2004: 229, Câmara Jr. 1970). The positional map selects the near-close [ɪ ʊ] at the end of the word, and `BR_RAISE_FINAL_E` and `BR_RAISE_FINAL_O` raise them. The rules target the reduced [ɪ ʊ] only, never the underlying /e o/. So a regional spec that keeps a final [e] or [o] inherits the rules, and they do not fire there.

The positional map affricates /t d/ only before a written ⟨i⟩. A final ⟨e⟩ becomes [i] only after the post-lexical raising, so the positional map cannot see it. The rules `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED` affricate /t d/ before the raised vowel (Barbosa & Albano 2004: 228). The regional specs with dental /t d/ switch these two rules off by id.

Word-final ⟨-em⟩, ⟨-en⟩ and the plural ⟨-ens⟩ are the nasal diphthong [ẽj̃], with the close-mid nucleus kept. The Northeastern and Minas Gerais specs reduce a post-stressed ⟨e⟩ to [ɪ], and they keep that reduction in ⟨-en⟩ and ⟨-ens⟩ too: `homens` is [ˈomɪ̃s] in `pt-BR-x-mg`.

```python
from orthography2ipa import G2P
G2P("pt-BR").transcribe_word("gato")   # ˈɡatu
G2P("pt-BR").transcribe_word("leite")  # ˈlejt͡ʃi
G2P("pt-BR", apply_allophony=False).transcribe_word("gato")  # ˈɡatʊ (broad)
```

## What the base does not model

Brazilian pretonic reduction is much weaker than the European one. The base keeps distinct pretonic /e o/ (`menino` [meˈninu]), so only the final position raises. The Minas Gerais and Northeastern specs change the pretonic vowels for their regions.

A coda /r/ as [h] or [x] is very variable across Brazil. The base keeps the tap [ɾ] (`porta` [ˈpoɾtɐ], `mar` [ˈmaɾ]). The wikipron pt-BR gold writes a final ⟨r⟩ most often as [ʁ] and almost never as [h]. The regional specs add a posterior coda rhotic where their sources report it.

## Sibilants, digraphs and ⟨w⟩

Brazilian Portuguese has one sibilant pair, the plain alveolar /s z/ (Barbosa & Albano 2004: 228, consonant chart, alveolar column: `saca` [ˈsakɐ] against `zaca` [ˈzakɐ]). The apico-alveolar [s̺ z̺] belongs to a different system. Galician-Portuguese has it, and `roa-x-galaicopt` and `pt-PT-x-medieval` model it with four sibilants. Some northern European dialects keep it, and each of their specs declares it for itself (see [pt-PT-dialects.md](pt-PT-dialects.md#northern-sibilant-systems)).

The base `pt-PT-x-medieval` maps ⟨ce ci⟩ to [s̺], and `roa-x-galaicopt` maps ⟨ss⟩ to [s̺]. So `pt-BR` declares the ⟨ss⟩ digraph and a positional ⟨c⟩ before ⟨e i⟩ with the plain [s]: `isso` [ˈisu], `cidade` [siˈdad͡ʒi].

⟨ss⟩ and ⟨rr⟩ are digraphs, not geminates. Portuguese has no contrastive consonant length. The digraph ⟨ss⟩ spells /s/ between vowels, where a single ⟨s⟩ is /z/. The digraph ⟨rr⟩ spells the strong rhotic, which contrasts with the tap (`carro` [ˈkaʁu] against `caro` [ˈkaɾu], Barbosa & Albano 2004: 228). Neither gives a doubled segment, so `collapse_geminates` stays unset.

The only doubled segments come from loans and names that keep their spelling (`watts` [ˈwatts], `reddit` [ˈʁedd͡ʒit]), and the gold sets double them too.

The letter ⟨w⟩ is rare but not silent. It is [w] in English loans and [v] in Germanic names, as in `pt-PT`: `web` [ˈweb], `show` [ˈsow].

## Reading the vox_communis row

The `vox_communis` row of `pt-BR` measures the gold, not this spec. Its phone tier is Epitran output over the Common Voice `pt` locale, which has no region tag. That output is European Portuguese. `scripts/fold_pt_br_notation.py` counts the features that define Brazilian Portuguese over the whole file, and none of them appears:

| Feature | Attested in the gold |
|:---|---:|
| final ⟨-l⟩ vocalised to [w] | 0 / 948 |
| ⟨t⟩ affricated before /i/ | 0 / 2378 |
| ⟨d⟩ affricated before /i/ | 5 / 1637 |
| final unstressed ⟨-e⟩ raised to [i] | 0 / 2956 |
| final unstressed ⟨-o⟩ raised to [u] | 0 / 7429 |
| final ⟨-s⟩ alveolar, not the European [ʃ] | 0 / 7429 |

The gold is also wrong about Portuguese of any variety. Its symbol inventory has neither ⟨ʎ⟩ nor ⟨ɲ⟩, so every ⟨lh⟩ and ⟨nh⟩ word loses its digraph (`gatilho` gives [ɡɐtilo], `tinha` gives [tinɐ]). It also applies the European coda-sibilant rule inside the ⟨ss⟩ digraph and writes [ʃs] on almost every ⟨ss⟩ word (`isso` gives [iʃso]).

The script folds ten conventions of the gold out of both sides, one at a time, and scores again after each fold. The `audit.vox_communis` entry in the spec records each step. The row is classified `epitran-derived` and cannot gate anything. Read it as a measurement of Epitran's European map, not as evidence about the Brazilian spec.

## Tier

`pt-BR` is at the production tier. Portuguese spelling is deep: vowel quality depends on stress, nasality and the word. So the deep-orthography threshold of [quality tiers](../specs/quality_tiers.md) applies, PER at most 0.25 on a gate-eligible gold of at least 500 entries. The qualifying row is `wikipron` (crowd-scraped). The other rows use other transcription conventions, and [../evaluation/datasets.md](../evaluation/datasets.md) describes them. For the figures, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

---
[← European Portuguese dialects](pt-PT-dialects.md) · [Home](../index.md) · [Brazilian Portuguese dialects →](pt-BR-dialects.md)
