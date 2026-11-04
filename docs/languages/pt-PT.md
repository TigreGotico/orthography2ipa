# European Portuguese (pt-PT)

| Field | Value |
|:---|:---|
| Code | `pt-PT` |
| Family | Indo-European > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | research |
| Base spec | `pt-PT-x-medieval` (Old Portuguese), which takes its own base from `roa-x-galaico-pt` |
| Sources | Mateus & d'Andrade (2000), Cruz-Ferreira (1995, *JIPA* 25(2)), Cruz-Ferreira (1999), Cunha & Cintra (1984), Mateus et al. (2003), Vigário (2003) |

The `pt-PT` spec models the broad standard of European Portuguese (EP). Its two defining traits are strong reduction of unstressed vowels and a large set of coda consonant realisations. This page gives what the spec models and the place in the pipeline where each process runs.

The `pt-PT` spec is also the base of the regional European Portuguese specs. The [European Portuguese dialects](pt-PT-dialects.md) page describes those specs and what each one changes. Input is standard spelling under the Acordo Ortográfico (1990).

## Two maps: where each process is modelled

The library realises pronunciation as two maps (see [../engine/allophony.md](../engine/allophony.md)). The pre-lexical map goes from spelling to phoneme, in `graphemes` and `positional_graphemes`. The post-lexical map goes from phoneme to surface allophone, in `allophone_rules`. Cross-word changes are in `sandhi_rules`.

| Process | Map | Field |
|:---|:---|:---|
| Unstressed vowel reduction | pre-lexical | `positional_graphemes` |
| Coda vowel nasalisation (⟨m n⟩) | pre-lexical and post-lexical | `positional_graphemes` (tilde) and `allophone_rules` (vowel quality) |
| Dark (velarised) coda /l/ | post-lexical | `allophone_rules` |
| Coda sibilants (*chiado*) | post-lexical | `allophone_rules` |
| Coda /s/ voicing across words | sandhi | `sandhi_rules` |

## Unstressed vowel reduction

Reduction is the most diagnostic EP feature. Unstressed vowels raise or move to the centre:

| Vowel | Stressed | Unstressed | Example |
|:---:|:---:|:---:|:---|
| a | [a] | [ɐ] | `cada` [ˈkadɐ] |
| e | [ɛ] or [e] | [ɨ] | `pele` [ˈpɛlɨ] |
| o | [ɔ] or [o] | [u] | `bola` [ˈbɔlɐ], `pomar` [puˈmaɾ] |

The positional rows of ⟨a⟩, ⟨e⟩ and ⟨o⟩ carry the reduction. They are `nucleus_stressed`, `nucleus_unstressed`, `pretonic` and `word_final`, plus `posttonic` for ⟨a⟩. Each row sets the vowel by stress and position. The `allophone_rules` layer does not repeat the reduction, because a second rule for the same change would never fire.

Speakers often delete a word-final [ɨ]. The spec writes the vowel. The optional sandhi rule `PT_ELISION` deletes a final [ɨ] before a vowel (`de amanhã` → [d‿ɐmɐɲã]), but the default transcription keeps it: `de amor` gives [dɨ ɐˈmoɾ]. A word exception maps the conjunction `e` to [i].

## Coda vowel nasalisation

A vowel before a nasal ⟨m⟩ or ⟨n⟩ in the same syllable becomes nasal. This happens word-finally or before another consonant. The nasal consonant joins the vowel and is not a separate segment (Mateus & d'Andrade 2000, ch. 2, *Nasality*). Portuguese has five nasal vowels, /ɐ̃ ẽ ĩ õ ũ/:

| Spelling | Oral base | Nasal vowel | Example |
|:---|:---:|:---:|:---|
| ⟨am an⟩ | [a] to [ɐ] | [ɐ̃] | `campo` [ˈkɐ̃pu], `cantar` [kɐ̃ˈtaɾ], `ambos` [ˈɐ̃buʃ] |
| ⟨em en⟩ | [ɛ] to [e] | [ẽ] | `tempo` [ˈtẽpu], `entre` [ˈẽtɾɨ] |
| ⟨im in⟩ | [i] | [ĩ] | `sim` [ˈsĩ], `fim` [ˈfĩ], `lindo` [ˈlĩdu] |
| ⟨om on⟩ | [ɔ] to [o] | [õ] | `bom` [ˈbõ], `onde` [ˈõdɨ] |
| ⟨um un⟩ | [u] | [ũ] | `mundo` [ˈmũdu], `um` [ˈũ] |

The process uses both maps, as in the [Barranquenho](ext-PT-x-barranco.md) spec.

The pre-lexical map makes the vowel nasal. The `positional_graphemes` entries for ⟨m⟩ and ⟨n⟩ map the coda positions (`before_consonant`, `word_final`) to one combining tilde, U+0303. The tilde replaces the nasal consonant and attaches to the vowel before it. An ⟨m⟩ or ⟨n⟩ between vowels matches no coda key, so it stays a consonant and the vowel stays oral: `cama` [ˈkamɐ], `ano` [ˈɐnu], `nome` [ˈnɔmɨ].

The post-lexical map sets the vowel quality. Five rules move the vowel to the oral base of its nasal vowel when the next segment is the tilde. The rule `PT_NASAL_A_RAISE` changes a to ɐ, `PT_NASAL_E_RAISE` changes ɛ to e and `PT_NASAL_O_RAISE` changes ɔ to o.

The rules `PT_NASAL_O_UNRED` and `PT_NASAL_E_UNRED` undo the reduction of an unstressed ⟨o⟩ and ⟨e⟩ (see below). An oral vowel before an onset nasal does not change. The tilde comes only from the ⟨m n⟩ slot, so a vowel never gets two tildes. A lexical ⟨i⟩ or ⟨u⟩ needs no rule, because [ĩ ũ] have the same oral base as [i u].

### Reduced ⟨o⟩ and ⟨e⟩ before a nasal

Unstressed vowel reduction changes ⟨o⟩ to [u], which would give `contar` as [kũˈtaɾ]. Before a coda nasal the reduction does not apply. An unstressed ⟨o⟩ there is the nasal mid vowel [õ], never [ũ] (Mateus & d'Andrade 2000, ch. 2, *Nasality*). The pre-lexical map has already reduced the vowel to [u] when the allophone layer runs. So `PT_NASAL_O_UNRED` changes that [u] back to [o] before the tilde: `contar` [kõˈtaɾ], `comprar` [kõˈpɾaɾ], `bondade` [bõˈdadɨ], `pombal` [põˈbaɫ], `montanha` [mõˈtaɲɐ], `bombom` [bõˈbõ].

The rule has a grapheme condition (`AllophoneRule.grapheme`). It fires only on a reduced ⟨o⟩. A lexical ⟨u⟩ before a nasal keeps its high [ũ]: `um` [ˈũ], `mundo` [ˈmũdu], `algum` [ɐɫˈɡũ], `segundo` [sɨˈɡũdu]. Both vowels are the phoneme [u] at that point, and only the spelling tells them apart. The pt-BR spec and the non-reducing varieties (pt-AO, pt-MZ, pt-TL) do not reduce ⟨o⟩ to [u]. Their ⟨o⟩ before a nasal is already [o], so the rule has no effect there.

The rule `PT_NASAL_E_UNRED` does the same for ⟨e⟩. An unstressed ⟨e⟩ before a coda nasal is [ẽ], not a reduced vowel: `entender` [ẽtẽˈdeɾ], `pensar` [pẽˈsaɾ]. Cruz-Ferreira (1999) lists no nasal counterpart of the unstressed [ɨ]. The rule note gives the quote.

### Word-final ⟨-em⟩, ⟨-en⟩ and ⟨-er⟩

A word-final ⟨-em⟩ is the nasal diphthong [ɐ̃j̃] (Mateus & d'Andrade 2000, ch. 4, and Cruz-Ferreira 1995). `PT_FINAL_EM_NUCLEUS` sets the nucleus [ɐ] and `PT_FINAL_EM_GLIDE` adds the glide: `bem` [ˈbɐ̃j̃], `homem` [ˈɔmɐ̃j̃]. The `PT_FINAL_ENS_*` rules do the same for the plural ⟨-ens⟩ (`homens` [ˈɔmɐ̃j̃ʃ]), and `PT_FINAL_AM_GLIDE` gives ⟨-am⟩ as [ɐ̃w̃] (`falam` [ˈfalɐ̃w̃]).

A learned noun in ⟨-en⟩ keeps a final consonant. Infopédia gives `hífen` [ˈifɛn], `pólen` [ˈpɔlɛn] and `abdómen` [ɐˈbdɔmɛn]. The ⟨-em⟩ diphthong rules match ⟨m⟩ only, so these words never get [ɐ̃j̃]. `PT_FINAL_EN_NUCLEUS` sets the open vowel [ɛ] and `PT_FINAL_EN_CODA` sets the consonant [n]. The spec gives `hífen` [ˈifɛn], `pólen` [ˈpɔlɛn] and `abdómen` [ɐbˈdɔmɛn]. The plural `hífenes` has no word-final ⟨n⟩ and gives [ˈifɨnɨʃ].

The stressed ⟨e⟩ of an infinitive in ⟨-er⟩ is close-mid [e]: `comer` [kuˈmeɾ], `ter` [ˈteɾ], `entender` [ẽtẽˈdeɾ]. Spelling does not show open or close quality. So the pre-lexical map writes [ɛ] for every stressed ⟨e⟩, and `PT_ER_CLOSE` closes it before a word-final ⟨r⟩. A word list, `PT_LEX_OPEN_ER`, keeps the open vowel of the nouns and loan words that Infopédia writes with [ɛ]: `mulher` [muˈʎɛɾ], `talher` [tɐˈʎɛɾ], `qualquer` [kwɐɫˈkɛɾ], `quer` [ˈkɛɾ], `mister` [miʃˈtɛɾ].

The Baixo-Minho specs `pt-PT-x-porto` and `pt-PT-x-braga` diphthongise both: `comer` [kuˈmjeɾ] and `mulher` [muˈʎjɛɾ]. The African and Asian varieties and Barranquenho switch off `PT_ER_CLOSE`, `PT_LEX_OPEN_ER`, `PT_FINAL_EN_NUCLEUS` and `PT_FINAL_EN_CODA`, and keep their own output. The rule notes carry the sources.

### Engine guard: the nasal tilde attaches only to a vowel

The coda ⟨m n⟩ slot carries an oral consonant fallback, [m] or [n], below the tilde in the beam. An engine guard in `PhonetokTokenizer._expand_beam` drops the tilde branch when the phoneme before it is not an oral vowel or a nasal-diphthong glide. The fallback consonant then wins. The guard keeps the output valid IPA in two cases:

1. The ⟨gu⟩ to [ɡ] vowel drop (`algum`, `segundo`) leaves a consonant before the coda slot. The tilde does not attach to the [ɡ].
2. In ⟨nn⟩ loans (`inn` [ˈĩn], `Finn` [ˈfĩn]), a second nasal slot does not put a second tilde on a vowel that is already nasal.

A tilde that lands on a vowel is never touched, so the nasal diphthongs ⟨ão ãe õe⟩, with their glides [w̃ j̃], do not change.

The design avoids two other collisions:

- The digraphs ⟨nh⟩ and ⟨lh⟩ stay whole. Longest-match tokenisation reads ⟨nh⟩ as one grapheme, [ɲ], before the rule for a single ⟨n⟩ can see it. So the ⟨n⟩ of ⟨nh⟩ never makes the vowel before it nasal: `banho` [ˈbaɲu].
- The nasal diphthongs ⟨ão ãe õe⟩ are whole graphemes, [ɐ̃w̃], [ɐ̃j̃] and [õj̃], with no separate ⟨m n⟩. The coda-nasal rules do not touch them: `pão` [ˈpɐ̃w̃], `mãe` [ˈmɐ̃j̃], `põe` [ˈpõj̃].

## Stressed ⟨e⟩ and ⟨o⟩ in suffix endings

Spelling does not show whether an unmarked stressed ⟨e⟩ or ⟨o⟩ is open or close. The pre-lexical map writes the open vowel, [ɛ] and [ɔ]. In Infopédia, outside the suffix classes below, the open vowel is the more frequent one, so the default stays open.

A suffix class is different, because its stressed vowel has one value. Seven post-lexical rules close the vowel of these word-final endings:

| Rule | Ending | Example |
|:---|:---|:---|
| `PT_SUFFIX_EZ_CLOSE` | ⟨-ez⟩ | `rapidez` [ʁɐpiˈdeʃ] |
| `PT_SUFFIX_EZA_ESA_CLOSE` | ⟨-eza -esa⟩ | `beleza` [bɨˈlezɐ], `mesa` [ˈmezɐ] |
| `PT_SUFFIX_EMA_CLOSE` | ⟨-ema⟩ | `sistema` [siʃˈtemɐ] |
| `PT_SUFFIX_ESCO_CLOSE` | ⟨-esco -esca⟩ | `dantesco` [dɐ̃ˈteʃku] |
| `PT_SUFFIX_OR_CLOSE` | ⟨-or⟩ | `trabalhador` [tɾɐbɐʎɐˈdoɾ], `amor` [ɐˈmoɾ] |
| `PT_SUFFIX_OSO_CLOSE` | ⟨-oso⟩ | `famoso` [fɐˈmozu] |
| `PT_SUFFIX_ONHO_CLOSE` | ⟨-onho -onha⟩ | `risonho` [ʁiˈzoɲu] |

Cunha and Cintra name each ending as a suffix. The rule notes quote the grammar and give the Infopédia counts behind each rule. The words that Infopédia writes with the open vowel are in two lists that come before the rules, `PT_LEX_OPEN_E_SUFFIX` and `PT_LEX_OPEN_O_SUFFIX`. They hold the comparatives `melhor` [mɨˈʎɔɾ], `pior` [piˈɔɾ], `maior` [maˈjɔɾ] and `menor` [mɨˈnɔɾ], and also `suor`, `reza` and `pesca`. The ⟨e⟩ list also holds the verb forms `pesa`, `preza`, `despreza`, `pesco`, `rema` and `crema`, because the verb form of a homograph has the open vowel.

The endings ⟨-eno -ena⟩ and ⟨-ona⟩ have no rule. Infopédia gives their nouns and adjectives a close vowel (`chileno` [ʃiˈlenu], `zona` [ˈzonɐ]). It gives the forms of the verbs in ⟨-enar⟩ and ⟨-onar⟩ an open vowel (`ordena` [ɔɾˈdɛnɐ], `funciona` [fũˈsjɔnɐ]). The spelling cannot tell the two groups apart. The Wiktionary readings in WikiPron include verb forms, and a close rule is wrong for many of them. So the spec keeps the open default for all of these words: `chileno` gives [ʃiˈlɛnu] and `zona` gives [ˈzɔnɐ].

The feminine and the plural of ⟨-oso⟩ keep the open vowel, because only the masculine singular closes it. The gate of `PT_SUFFIX_OSO_CLOSE` is the word-final ⟨o⟩, so these forms do not match: `famosa` [fɐˈmɔzɐ], `famosos` [fɐˈmɔzuʃ].

Other word lists set the height of frequent words outside the suffix classes. The lists `PT_LEX_CLOSE_O` and `PT_LEX_CLOSE_E` pin a close vowel (`sopa`, `como`, `fresco`). The lists `PT_LEX_OPEN_O` and `PT_LEX_OPEN_E` pin an open vowel (`sol`, `forte`, `terra`, `dez`). The rule `PT_LEX_X_S` gives the ⟨x⟩ of the stem ⟨troux-⟩ of *trazer* as [s].

Porto, Braga and Terceira have their own process for the stressed mid vowels, so they switch these rules off. The African and Asian varieties, Barranquenho and the creoles also switch them off, because no source for them was read.

## Coda consonants

EP has three coda consonant processes that the pre-lexical map cannot reach cleanly at word edges. They are `allophone_rules` keyed on `syllable_position: "coda"`:

| Rule id | Process | Example |
|:---|:---|:---|
| `PT_CODA_L_DARK` | velarised coda /l/ to [ɫ] | `sol` [ˈsɔɫ], `alto` [ˈɐɫtu] |
| `PT_CODA_S_HUSH` | coda /s/ to [ʃ] (*chiado*) | `pasta` [ˈpaʃtɐ] |
| `PT_CODA_Z_HUSH` | coda /z/ to [ʒ] | the voiced counterpart |

An onset /l/ or /s/ does not change: `bola` [ˈbɔlɐ], `casa` [ˈkazɐ].

The coda sibilant values are the standard (Lisbon) realisation. Some northern and island dialects keep an apico-alveolar [s̺] in the coda. The `pt-PT-x-*` specs carry those differences. They inherit these three rules by id and override only what differs (see [how the dialect specs inherit](pt-PT-dialects.md#how-the-dialect-specs-inherit-from-pt-pt)).

## External /s/-sandhi

A word-final coda /s/ is [ʃ] alone and before a voiceless consonant. Across a word boundary it changes with the next word. Two `sandhi_rules` set the value:

| Rule id | Context | Value | Example |
|:---|:---|:---|:---|
| `PT_FINAL_S_PREVOCALIC_VOICE` | `…s#` + `#V…` | [z] | `estás a ver` [eʃˈtaz ɐ ˈveɾ], `os amigos` [oz ɐˈmiɡuʃ] |
| `PT_CODA_S_VOICING` | `…s#` + `#[voiced C]…` | [ʒ] | `estás bem` [eʃˈtaʒ ˈbɐ̃j̃], `as bocas` [ɐʒ ˈbɔkɐʃ], `os dois` [oʒ ˈdojʃ] |

Before a vowel, the final sibilant joins the next syllable and is voiced to the alveolar [z]. Before a voiced consonant, it takes the voicing of that consonant and is the post-alveolar [ʒ] (Mateus & d'Andrade 2000, ch. 2). Before a voiceless consonant it stays [ʃ]: `estás feliz` [eʃˈtaʃ fɨˈliʃ]. A single word does not change: `estás` [eʃˈtaʃ].

The `right_context` of `PT_CODA_S_VOICING` is `^[ˈˌ]?[bdgvzʒmnɲɾʁlʎ]`. The optional stress mark lets it fire on a next word that starts with a stressed syllable, such as `bocas` [ˈbɔkɐʃ].

The standard [z] before a vowel is well documented (Mateus & d'Andrade 2000, ch. 2). Wikipedia, *Portuguese phonology*, section Consonant sandhi, gives `bons amigos` [bõz ɐˈmiɣuʃ]. Every `pt-PT-x-*` spec inherits both rules by id. Some dialects use [ʒ] before a vowel as well. The [dialect page](pt-PT-dialects.md#s-sandhi-before-a-vowel) gives the value of each spec and its sources.

## Not modelled

Spirantisation of the voiced stops between vowels (/b d ɡ/ to [β ð ɣ], Mateus & d'Andrade 2000) is a real EP process, but the spec does not encode it. Every available `pt` gold (`infopedia_pt`, `ep_dialects`, WikiPron) is broad and writes the plain stops. So no gold rewards the rule. It is left for a narrow-transcription task. The rule for shipping a rule is that it is correct and that it is neutral or better on an adequate gold.

## Gold sets that disagree with the spec

Two gold sets write some processes differently from the spec. See [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md) for the scores.

WikiPron writes the EP coda /l/ as a plain [l]. So `PT_CODA_L_DARK` disagrees with the WikiPron `pt` row, while the narrow human gold sets agree with it. The rule stays, because it is correct and the higher-quality gold sets support it.

`styletts2_phonemes` is a machine gold from an espeak-style phonemiser. It writes a coda nasal as a nasal vowel plus a nasal consonant or [ŋ] (`campo` as `kˈɐ̃mpʊ`, `conde` as `kˈoŋdɨ`). The standard broad transcription, and every higher-quality gold here, puts the consonant into the nasal vowel (`campo` [ˈkɐ̃pu]). The spec follows the standard.

## Other notes

Portuguese keeps the /v/ and /b/ distinction, which Castilian lost: `vinho` [ˈviɲu], `bebe` [ˈbɛbɨ]. The nasal vowels and nasal diphthongs (⟨ão ãe õe⟩) are diagnostic, and they drive the placement of final stress.

---
[← Pyrenean-valley Aragonese subdialects](an-valleys.md) · [Home](../index.md) · [European Portuguese dialects →](pt-PT-dialects.md)
