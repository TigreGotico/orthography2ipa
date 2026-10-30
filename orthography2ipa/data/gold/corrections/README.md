# Gold corrections overlays

Each file here repairs a defect in an upstream gold set without touching the
upstream file, which stays byte-identical. One JSONL row per corrected gold
entry:

| field | meaning |
|---|---|
| `dataset` | the upstream gold set the correction applies to |
| `lang` | the language tag of the upstream row |
| `spelling` | the orthographic word, matched exactly against upstream |
| `original_reading` | the reading upstream shipped, matched exactly |
| `corrected_reading` | the reading the overlay substitutes |
| `reason` | what is wrong with the original reading |
| `authority` | the orthographic fact or the citation the correction rests on |
| `upstream_file` | the upstream file the row was read from (`ipadict_pt_BR.jsonl` only) |
| `kind` | the defect the row repairs (`ipadict_pt_BR.jsonl` only) |

`original_reading` is the reading as the benchmark loader reads it from the
upstream file. For ipa-dict that is the variant between the slashes.

A correction may be derived only from the orthography of the word or from a
fetched citation, never from what orthography2ipa outputs. The overlaid gold is
registered as its own benchmark dataset so the uncorrected row stays on the
board beside it, and it can never gate a quality promotion. See
"Corrections overlays" in `docs/benchmarks.md` for the full rules.

The file name is `{dataset}_{lang}.jsonl`, with the hyphens of the language
tag written as underscores.

Regenerate with:

    PYTHONPATH=. python scripts/build_gold_corrections.py

## `vox_communis_vi.jsonl`

The VoxCommunis Vietnamese phone tier writes the same Chao tone letter ˨˨ for
*ngang* and *huyền*, merging two contrastive tones. Vietnamese orthography
writes huyền with a combining grave accent, so the merged rows are separable
from the spelling alone; the substituted ˧˩ follows Kirby (2011: 386), who
labels huyền "mid falling" against hỏi's "low falling". 401 rows corrected,
7 left uncorrected and reported by the build.

## `ipadict_pt_BR.jsonl`

The ipa-dict Brazilian Portuguese file `pt_BR.txt` writes one primary stress on
a hyphenated word. It never writes a secondary stress. On 656 of its 2361
hyphenated rows that one stress is on the wrong syllable, in two ways.

In enclisis (`kind` `enclitic`, 149 rows) the gold stresses the penultimate
syllable of host and clitic written as one string: *acusa-o* `a.ku.ˈza.ʊ`,
*matando-os* `ma.tã.ˈdo.ʊs`. An enclitic pronoun is unstressed and the host
keeps its own stress. The Acordo Ortográfico 1990 shows this in its accent
rules: the host of *adorá-lo* keeps the tonic vowel of *adorar* (Base VIII,
1.º b). Toneli (2011: 2) gives host plus enclitic, as in *fala-se*, as one
prosodic word with one primary accent. The overlay writes `a.ˈku.za.ʊ` and
`ma.ˈtã.do.ʊs`.

In a compound (`kind` `compound`, 507 rows) the gold stresses an element before
the last: *pára-brisas* `ˈpa.ɾa.bɾi.zəs`, *pós-ditadura* `ˈpɔʒ.dʒi.ta.du.ɾə`.
The last element of a Portuguese compound carries the main stress. Bechara
writes that in a compound by juxtaposition each radical keeps its stress,
"sendo o último o mais forte" (*Moderna Gramática Portuguesa*, p. 340, quoted
in Ciberdúvidas resposta 28042). Toneli (2011: 2) states that the main
prominence of a compound prosodic word "será sempre o elemento mais à
direita". The overlay writes `pa.ɾa.ˈbɾi.zəs` and `pɔʒ.dʒi.ta.ˈdu.ɾə`.

The stressed syllable of each element comes from the spelling alone, by the
Acordo Ortográfico 1990 accent rules (Bases VIII, IX and X). A written acute or
circumflex marks it. Otherwise a word that ends in -a, -e, -o, -as, -es, -os,
-am, -em or -ens is paroxytone, and a word with another ending is oxytone. The
build maps that syllable onto the gold's own dotted syllables. Only the stress
mark moves, and every segment stays as upstream wrote it. 32 corrected
compounds keep a second upstream defect that the overlay does not repair: the
gold writes the vowel of the newly stressed syllable as if it were unstressed
(*não-lógicos* `nãʊ̃.ˈlɪ.ʒi.kʊs`).

The build leaves these hyphenated rows alone and counts them:

| reason | rows |
|---|---|
| gold already stresses the right syllable | 1630 |
| empty element, a truncated upstream entry such as `obras-` | 34 |
| the spelling's nuclei do not add up to the gold's syllables | 32 |
| misspelt -lo/-la enclisis, such as *ajuda-lo* for *ajudá-lo* | 7 |
| mesoclisis, such as *encontrar-se-ão* | 2 |

    Toneli, Priscila Marques (2011). O comportamento prosódico de palavras
    compostas no Português Brasileiro. I Congresso Nacional de Estudos
    Linguísticos, Vitória-ES.

    Ciberdúvidas da Língua Portuguesa, resposta 28042, "Composição por
    aglutinação e composição por justaposição, novamente".
    https://ciberduvidas.iscte-iul.pt/consultorio/perguntas/x/28042

## `portuguese_unified_pt.jsonl`

This overlay corrects rows of the Portuguese unified pronunciation lexicon
(`TigreGotico/portuguese-unified-pronunciation-lexicon`). The file is keyed on
the source row of the dataset, not on an o2i language tag, so any consumer of
the dataset can apply the same rows. Its fields differ from the table above:

| field | meaning |
|---|---|
| `dataset` | always `portuguese_unified` |
| `source` | `infopedia`, `wiktionary`, `infopedia+wiktionary` or `portal`, read from the row's fields |
| `region` | the dataset's region tag, for example `pt-PT-x-lisboa` |
| `word`, `pos` | the headword and the part of speech of the row |
| `field` | `ipa_narrow` or `ipa_broad` |
| `original_reading` | the reading the row ships, matched exactly |
| `corrected_reading` | the reading to use; `null` drops the row |
| `kind` | `accent_contradiction`, `unaccented_stress`, `missing_mark`, `wrong_headword` or `mojibake` |
| `reason`, `authority` | what is wrong, and the orthographic fact or the fetched citation |

A correction moves or adds the primary stress mark, drops a variant, or drops
a row. It changes no segment. The written accent, or the accent rules of the
Acordo Ortográfico 1990, settles each stressed syllable. A row is dropped when
its reading transcribes another headword (*tração* rows that read *seleto*),
or when it ends in mis-encoded text. A mark goes only on a vowel that the
stressed letter can spell. A row that also needs a segment fix stays
uncorrected.

The narrow field has 539 corrections: 79 accent contradictions, 24 unaccented
words stressed against the accent rules, 337 missing marks, 48 rows or
variants of another headword, and 51 rows with mis-encoded text. The broad
field has 441 corrections that follow the narrow ones.
