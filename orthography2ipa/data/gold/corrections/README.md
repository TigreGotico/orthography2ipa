# Gold corrections overlays

Each file in this folder repairs a defect in an upstream gold set. The upstream file stays byte-identical. Each row of an overlay is one corrected gold entry, as one line of JSON.

A correction may come only from the spelling of the word or from a citation that was fetched and read. It may never come from the output of orthography2ipa, because a gold repaired with the engine's own answers measures nothing. The rules for citations are in [Citations](../../../../docs/contributing/citations.md). [Corrections overlays](../../../../docs/benchmarks.md#corrections-overlays) explains how the board scores an overlay.

## How the benchmark uses an overlay

`scripts/benchmark.py` registers each overlaid gold as a dataset of its own, named after the base set with `_corrected` added: `vox_communis_corrected`, `ipadict_corrected` and `portuguese_unified_corrected`. The uncorrected row stays on the board beside it, so the effect of the correction is the difference between the two rows. The corrected row keeps the provenance tier of its base gold. It never gates a quality promotion, because an automated process applied the corrections.

A correction applies only where the spelling and the original reading both match the upstream row exactly. If an upstream revision changes a reading, the correction stops applying and does not apply to the wrong row. The loader prints a warning that gives the number of overlay rows that matched nothing.

## Row fields

The `vox_communis` and `ipadict` overlays use these fields.

| Field | Meaning |
|---|---|
| `dataset` | The upstream gold set that the correction applies to. |
| `lang` | The language tag of the upstream row. |
| `spelling` | The orthographic word, matched exactly against upstream. |
| `original_reading` | The reading that upstream ships, matched exactly. |
| `corrected_reading` | The reading that the overlay substitutes. |
| `reason` | What is wrong with the original reading. |
| `authority` | The orthographic fact or the citation that the correction rests on. |
| `upstream_file` | The upstream file that the row comes from. Only in `ipadict_pt_BR.jsonl`. |
| `kind` | The defect that the row repairs. Only in `ipadict_pt_BR.jsonl`. |

`original_reading` is the reading as the benchmark loader reads it from the upstream file. For ipa-dict, that is the variant between the slashes.

The file name is `{dataset}_{lang}.jsonl`, with the hyphens of the language tag written as underscores. The `portuguese_unified_pt.jsonl` overlay is keyed on the dataset row, not on a language tag, and it has its own fields. Its section below lists them.

## Regenerate the overlays

`scripts/build_gold_corrections.py` writes every file in this folder again. It reads the upstream gold through the base loaders of `scripts/benchmark.py`, and each builder sees only the spelling and the reading. The build is deterministic: on an unchanged upstream cache it writes the committed bytes again. For each overlay it prints the upstream pairs it read and the rows it wrote. It also prints the counts of corrected and skipped rows.

```
PYTHONPATH=. python scripts/build_gold_corrections.py
```

## `vox_communis_vi.jsonl`

The VoxCommunis Vietnamese phone tier writes the same Chao tone letter ˨˨ for *ngang* and for *huyền*. This merges two contrastive tones. Vietnamese spelling writes huyền with a combining grave accent (U+0300) and writes ngang with no tone mark. The spelling alone tells the merged rows apart.

The overlay writes ˧˩ for huyền. [Kirby (2011: 386)](https://doi.org/10.1017/S0025100311000181) labels huyền "mid falling" against the "low falling" of hỏi, so huyền starts above the register of hỏi. The upstream ngang is ˨˨ and its hỏi is ˨˩˨, so ˧˩ differs from each tone-letter sequence in the file. For example, the overlay changes *biền* from `ɓiə˨˨n` to `ɓiə˧˩n`.

The build corrects a row only when the spelling has one tone mark and that mark is the huyền grave. The tone letters of the reading must also be exactly ˨˨. It counts the rows it leaves alone. A spelling with more than one tone mark is a token of more than one syllable, and no single tone applies to it (`tone_undeterminable`). A grave-accented spelling whose reading is not ˨˨ does not show the merge, and the build does not correct it (`huyen_reading_not_ngang`).

## `ipadict_pt_BR.jsonl`

The ipa-dict Brazilian Portuguese file `pt_BR.txt` writes one primary stress on a hyphenated word and never writes a secondary stress. On many hyphenated rows, that one stress is on the wrong syllable. The `kind` field names which of two defects a row has.

In enclisis (`kind` `enclitic`), the gold stresses the penultimate syllable of the host and the clitic as one string: *acusa-o* `a.ku.ˈza.ʊ`, *matando-os* `ma.tã.ˈdo.ʊs`. An enclitic pronoun is unstressed, and the host keeps its own stress. The accent rules of the Acordo Ortográfico 1990 show this. The host of *adorá-lo* keeps the tonic vowel of *adorar* (Base VIII, 1.º b). Toneli (2011: 2) gives a host plus an enclitic, as in *fala-se*, as one prosodic word with one primary accent. The overlay writes `a.ˈku.za.ʊ` and `ma.ˈtã.do.ʊs`.

In a compound (`kind` `compound`), the gold stresses an element before the last: *pára-brisas* `ˈpa.ɾa.bɾi.zəs`, *pós-ditadura* `ˈpɔʒ.dʒi.ta.du.ɾə`. The last element of a Portuguese compound carries the main stress.

Bechara writes that in a compound by juxtaposition each radical keeps its stress, "sendo o último o mais forte" (*Moderna Gramática Portuguesa*, p. 340). [Ciberdúvidas, resposta 28042](https://ciberduvidas.iscte-iul.pt/consultorio/perguntas/x/28042) quotes this passage. Toneli (2011: 2) states that the main prominence of a compound prosodic word "será sempre o elemento mais à direita". The overlay writes `pa.ɾa.ˈbɾi.zəs` and `pɔʒ.dʒi.ta.ˈdu.ɾə`.

The spelling alone gives the stressed syllable of each element, by the accent rules of the Acordo Ortográfico 1990 (Bases VIII, IX and X). A written acute or circumflex marks the syllable. Without one, a word that ends in -a, -e, -o, -as, -es, -os, -am, -em or -ens is paroxytone. A word with another ending is oxytone. The build maps that syllable onto the dotted syllables of the gold.

Only the stress mark moves. Each segment stays as upstream wrote it. Some corrected compounds keep a second upstream defect that the overlay does not repair. The gold writes the vowel of the stressed syllable as if it were unstressed (*não-lógicos* `nãʊ̃.ˈlɪ.ʒi.kʊs`).

The build reads only hyphenated rows. It counts each row it leaves alone under one of these reasons:

| Count | Reason |
|---|---|
| `already_correct` | The gold already stresses the right syllable. |
| `empty_element` | An element is empty, as in a truncated upstream entry such as `obras-`. |
| `no_host` | Every element is a clitic. |
| `nucleus_count_mismatch` | The vowel nuclei of the spelling do not add up to the syllables of the gold. |
| `misspelling` | A misspelt -lo or -la enclisis, such as *ajuda-lo* for *ajudá-lo*. |
| `mesoclisis` | A mesoclisis, such as *encontrar-se-ão*. |
| `gold_stress_unreadable` | The gold reading has no readable primary stress. |
| `stress_undeterminable` | The spelling rules cannot place the stress of the element. |
| `gold_stress_other_shape` | The gold stress is wrong, but not in the shape that the defect names. |

Toneli, Priscila Marques (2011). *O comportamento prosódico de palavras compostas no Português Brasileiro*. I Congresso Nacional de Estudos Linguísticos, Vitória-ES.

## `portuguese_unified_pt.jsonl`

This overlay corrects rows of the Portuguese unified pronunciation lexicon (`TigreGotico/portuguese-unified-pronunciation-lexicon`). The file is keyed on the source row of that dataset, not on an o2i language tag. Any consumer of the dataset can apply the same rows. Its fields differ from the fields above.

| Field | Meaning |
|---|---|
| `dataset` | Always `portuguese_unified`. |
| `source` | `infopedia`, `wiktionary`, `infopedia+wiktionary` or `portal`, read from the fields of the row. |
| `region` | The region tag of the dataset, for example `pt-PT-x-lisboa`. This is not the o2i tag (`pt-PT-x-lisbon`). |
| `word`, `pos` | The headword and the part of speech of the row. |
| `field` | `ipa_narrow` or `ipa_broad`. |
| `original_reading` | The reading that the row ships, matched exactly. |
| `corrected_reading` | The reading to use. `null` drops the row. |
| `kind` | `accent_contradiction`, `unaccented_stress`, `missing_mark`, `wrong_headword` or `mojibake`. |
| `reason`, `authority` | What is wrong, and the orthographic fact or the fetched citation. |

The written accent, or the accent rules of the Acordo Ortográfico 1990, settles each stressed syllable. Each `kind` value names one defect of the source rows.

| Kind | Defect | Example |
|---|---|---|
| `accent_contradiction` | The primary mark is on a syllable other than the one that a written acute or circumflex marks. | Infopédia *busílis* `buziˈliʃ` |
| `unaccented_stress` | An unaccented word has its mark where the accent rules do not put it. An unaccented -ar infinitive is oxytone. | Infopédia *malucar* `mɐˈlukar` |
| `missing_mark` | The reading has no primary mark. The Portal Lisbon rows lose it on a stressed vowel after [j]. | *paciente* `pɐsjẽt` |
| `wrong_headword` | The reading transcribes another headword. | *tração* rows that read *seleto* |
| `mojibake` | The reading ends in mis-encoded text. | Maputo rows |

A correction moves, adds or removes a stress mark, or drops a variant or a row. It changes no segment, except where a stray symbol stands in for the mark (`koitádu`, `traveˡsejru`). A mark goes only on a vowel that the stressed letter can spell. A row that also needs a segment fix stays uncorrected. For example, a stressed [ɨ] cannot spell ⟨ê⟩, so the Lisbon *sêxtuplo* row `sɨʃtˈuplu` stays as it is.

The file corrects both the narrow and the broad field, and the broad corrections follow the narrow ones. The `portuguese_unified_corrected` dataset of the benchmark applies only the `ipa_narrow` rows. The `ipa_broad` rows are there for other consumers of the dataset.
