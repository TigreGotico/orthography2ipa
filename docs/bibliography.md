# Bibliography

This page lists reference works for spec authors, grouped by language family. The authoritative record of what a spec cites is that spec's own `sources` array. A bold key in a table is the `id` that the specs use for the work. A work with no key is a recommended reference that no spec cites in `sources`. The rules for citing are in [citation honesty](contributing/citations.md).

## How a spec cites a work

Each entry of a spec's `sources` array names one work. The loader turns it into a `LinguisticSource`, and `LanguageSpec.sources` holds a tuple of them:

```python
import orthography2ipa

[s.id for s in orthography2ipa.get("de-DE").sources][:3]   # ['wiese1996', 'hall2003', 'mangold2005']
```

| Field | Required | What it holds |
|---|---|---|
| `id` | yes | A short cite key, such as `wells1982_vol2`, unique inside the spec |
| `author` | yes | The authors, such as `Wells, J.C.` |
| `year` | yes | The year of publication |
| `title` | yes | The full title of the work |
| `publisher` | no | The publisher, or the journal with volume and pages |
| `url` | no | A URL for an online work, or `null` for a print-only work |
| `doi` | no | The DOI, which is the preferred stable identifier |
| `wikipedia_url` | no | A Wikipedia article for a human reader. It does not make the entry a citation |
| `pages` | no | The page range that you read, such as `pp. 45-72` |
| `notes` | no | What the source supports |

The schema of each field is in [`SCHEMA.md`](../orthography2ipa/data/SCHEMA.md#sources-schema).

## Germanic

| Language | Work | What it is good for |
|---|---|---|
| English | **wells1982_vol1**: Wells, J.C. (1982). *Accents of English, Vol. 1: An Introduction*. Cambridge University Press. | The framework of lexical sets and the overview of English accents |
| English | **wells1982_vol2**: Wells, J.C. (1982). *Accents of English, Vol. 2: The British Isles*. Cambridge University Press. | The accents of Britain and Ireland |
| English | **wells1982_vol3**: Wells, J.C. (1982). *Accents of English, Vol. 3: Beyond the British Isles*. Cambridge University Press. | North American, Australian and South African English |
| English | **roach2009**: Roach, P. (2009). *English Phonetics and Phonology: A Practical Course* (4th ed.). Cambridge University Press. | A practical description of RP |
| English | **gimson2014**: Cruttenden, A. (ed.) (2014). *Gimson's Pronunciation of English* (8th ed.). Routledge. | The standard reference for British English pronunciation |
| English | **ladefoged1999_ame**: Ladefoged, P. (1999). American English. In: *Handbook of the International Phonetic Association*. Cambridge University Press. | A short IPA description of American English |
| English | **cox_palethorpe2007**: Cox, F. & Palethorpe, S. (2007). Australian English. *Journal of the International Phonetic Association*, 37(3), 341-350. | A JIPA illustration of Australian English |
| English | **stuartsmith2003**: Stuart-Smith, J. (2003). Glasgow. In: Upton, C. (ed.), *Urban Voices*. Arnold. | The accent of Glasgow |
| English | **carney1994**: Carney, E. (1994). *A Survey of English Spelling*. Routledge. | The spelling-to-sound reference for English. Its account of weak-vowel reduction and of digraph and suffix correspondences (⟨-tion⟩, ⟨-sion⟩, ⟨-cian⟩) supports the `nucleus_unstressed` and multigraph rules of `en-GB` |
| German | **wiese1996**: Wiese, R. (1996). *The Phonology of German*. Oxford University Press. | The phonology of Standard German, final devoicing included |
| German | **hall2003**: Hall, T.A. (2003). *Phonologie des Deutschen: eine Einführung*. de Gruyter. | An introduction to German phonology |
| German | **mangold2005**: Mangold, M. (2005). *Duden Aussprachewörterbuch* (6th ed.). Dudenverlag. | The pronunciation dictionary of Standard German |
| German | **muhr_schrodt1997**: Muhr, R. & Schrodt, R. (1997). *Österreichisches Deutsch und andere nationale Varietäten plurizentrischer Sprachen in Europa*. Daedalus. | Austrian German |
| German | **christen1998**: Christen, H. (1998). *Convergenz und Divergenz in der schweizerdeutschen Gegenwartsdialekte*. Francke. | Swiss German dialects |
| Dutch | **gussenhoven1999**: Gussenhoven, C. (1999). Dutch. In: *Handbook of the International Phonetic Association*. Cambridge University Press. | A short IPA description of Dutch. The `li` spec uses the same key for Gussenhoven, C. & Aarts, F. (1999), *The dialect of Maastricht* |
| Dutch | **vdHulst_ritter1999**: van der Hulst, H. & Ritter, N.A. (eds.) (1999). *The Syllable: Views and Facts*. Mouton de Gruyter. | Syllable structure |
| Swedish | **riad2014**: Riad, T. (2014). *The Phonology of Swedish*. Oxford University Press. | The phonology of Swedish |
| Swedish | **engstrand1999**: Engstrand, O. (1999). Swedish. In: *Handbook of the International Phonetic Association*. Cambridge University Press. | A short IPA description of Swedish |
| Norwegian | **haugen1976**: Haugen, E. (1976). *The Scandinavian Languages: An Introduction to their History*. Faber and Faber. | The history of the Scandinavian languages |
| Norwegian | **kristoffersen2000**: Kristoffersen, G. (2000). *The Phonology of Norwegian*. Oxford University Press. | The phonology of Norwegian |
| Danish | **basboll2005**: Basbøll, H. (2005). *The Phonology of Danish*. Oxford University Press. | The phonology of Danish |
| Danish | **gronnum2005**: Grønnum, N. (2005). *Fonetik og fonologi: Almen og dansk*. Akademisk Forlag. | Danish phonetics |
| Icelandic | **einarsson1945**: Einarsson, S. (1945). *Icelandic: Grammar, Texts, Glossary*. Johns Hopkins Press. | A grammar of Icelandic |
| Icelandic, Faroese | **arnason2011**: Árnason, K. (2011). *The Phonology of Icelandic and Faroese*. Oxford University Press. | The phonology of Icelandic and Faroese |
| Afrikaans | **donaldson1993**: Donaldson, B.C. (1993). *A Grammar of Afrikaans*. Mouton de Gruyter. | A grammar of Afrikaans |
| Low German | **stellmacher1990**: Stellmacher, D. (1990). *Niederdeutsche Sprache: Eine Einführung*. Peter Lang. | An introduction to Low German |
| Middle English | **mosse1952**: Mossé, F. (1952). *A Handbook of Middle English*. Johns Hopkins Press. | Middle English |
| Middle English | **jordan1974**: Jordan, R. (1974). *Handbook of Middle English Grammar: Phonology*. Mouton. | Middle English phonology |
| Old English | **hogg1992**: Hogg, R.M. (1992). *A Grammar of Old English, Vol. 1: Phonology*. Blackwell. | Old English phonology |
| Old English | **campbell1959**: Campbell, A. (1959). *Old English Grammar*. Oxford University Press. | Old English grammar |
| Old Norse | **noreen1923**: Noreen, A. (1923). *Altisländische und altnorwegische Grammatik* (4th ed.). Max Niemeyer. | Old Icelandic and Old Norwegian grammar |
| Old Norse | **gordon1957**: Gordon, E.V. (1957). *An Introduction to Old Norse* (2nd ed., rev. Taylor, A.R.). Oxford University Press. | An introduction to Old Norse |
| Old Saxon | **gallee1910**: Gallée, J.H. (1910). *Altsächsische Grammatik* (2nd ed.). Max Niemeyer. | Old Saxon grammar |
| Old High German | **braune2004**: Braune, W. (rev. Heidermanns, F.) (2004). *Althochdeutsche Grammatik I: Laut- und Formenlehre* (15th ed.). Max Niemeyer. | Old High German phonology and morphology |
| Old High German | **schatz1927**: Schatz, J. (1927). *Althochdeutsche Grammatik*. Vandenhoeck & Ruprecht. | Old High German grammar |
| Proto-Germanic | **ringe2006**: Ringe, D. (2006). *From Proto-Indo-European to Proto-Germanic*. Oxford University Press. | The sound changes from PIE to Proto-Germanic |

## Romance

| Language | Work | What it is good for |
|---|---|---|
| Spanish | **hualde2005**: Hualde, J.I. (2005). *The Sounds of Spanish*. Cambridge University Press. | Spanish phonetics and phonology, lenition and the dialect contrasts included |
| Spanish | **rae2011**: Real Academia Española & Asociación de Academias de la Lengua Española (2011). *Nueva gramática de la lengua española: Fonética y fonología*. Espasa. | The academic description of Spanish phonetics |
| Portuguese | Teyssier, P. (1980). *Histoire de la langue portugaise*. PUF. | The history of Portuguese |
| Portuguese | **brissos2014**: Brissos, F. (2014). *New insights into Portuguese central-southern dialects: understanding their present and past forms through acoustic data from stressed vowels*. Journal of Portuguese Linguistics 13(1). [PDF](https://www.clul.ulisboa.pt/files/849/Brissos_2014_comprimido.pdf), read in full. | The stressed vowels of the central and southern European Portuguese dialects. Mined for the `primary_sources` gold |
| Catalan | **wheeler2005**: Wheeler, M.W. (2005). *The Phonology of Catalan*. Oxford University Press. | The phonology of Catalan |

## Slavic

| Language | Work | What it is good for |
|---|---|---|
| Slavic | **comrie_corbett1993**: Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge. | One chapter per Slavic language |
| Russian | Comrie, B. et al. (1996). *The Russian Language in the Twentieth Century*. Oxford University Press. | Standard Russian and its variation |

## Semitic

| Language | Work | What it is good for |
|---|---|---|
| Levantine Arabic | **almbark2015**: Almbark, R. & Hellmuth, S. (2015). *Acoustic analysis of the Syrian Arabic vowel system*. Proceedings of ICPhS 2015 (paper 0612), Glasgow. [PDF](https://www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2015/Papers/ICPHS0612.pdf), read in full. | The Syrian vowel system. Mined for the `primary_sources` gold |
| Levantine Arabic | **cotter2016**: Cotter, W.M. (2016). *One Piece of the Puzzle: Notes on the Historic Interdental Fricatives /θ, ð, ðˤ/ in the Arabic Dialect of Gaza City*. Journal of Arabic and Islamic Studies 16:149-162. [PDF](https://www.lancaster.ac.uk/jais/volume/docs/vol16/v16_05_cotter_149-162.pdf), read in full. | The interdentals of Gaza City. Mined for the `primary_sources` gold |
| Levantine Arabic | **alwer2020**: Al-Wer, E. (2020). *New-dialect formation: The Amman dialect*. In C. Lucas & S. Manfredi (eds.), *Arabic and contact-induced change*, 551-566. Berlin: Language Science Press. [Open access](https://langsci-press.org/catalog/book/235), read in full. | The formation of the Amman dialect |
| Levantine Arabic | **fadda2016**: Fadda, H. (2016). *Language Variation in Western Amman*. MA thesis, Canada Institute of Linguistics. [PDF](https://www.canil.ca/wordpress/wp-content/uploads/2019/11/Fadda-Language-Variation-in-Western-Amman.pdf), phonology chapter read. | Variation in Western Amman. Mined for the `primary_sources` gold |
| Levantine Arabic | **cowell1964**: Cowell, M.W. (1964). *A Reference Grammar of Syrian Arabic (Based on the Dialect of Damascus)*. Georgetown University Press. | Not obtained (Internet Archive lends it only). Cited only as Almbark & Hellmuth (2015) report and re-test it |
| Arabic | **watson2002**: Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press. | Emphasis spreading |
| Mesopotamian Arabic | **jasim2020**: Jasim, M. (2020). *Tafxiːm in the vowels of Muslawi Qəltu and Baghdadi Gilit dialects of Arabic*. PhD thesis, Newcastle University. [PDF](https://theses.ncl.ac.uk/jspui/bitstream/10443/4899/1/Jasim%20M%202020.pdf), chapters 2 and 4 read. | Emphasis in the vowels of Mosul and Baghdad. Mined for the `primary_sources` gold |

## Indo-European and historical

| Language | Work | What it is good for |
|---|---|---|
| Proto-Indo-European | **fortson2010**: Fortson IV, B.W. (2010). *Indo-European Language and Culture: An Introduction* (2nd ed.). Wiley-Blackwell. | The reconstructed protolanguage and the sound laws of its branches |
| Latin, Greek | Sihler, A. (1995). *New Comparative Grammar of Greek and Latin*. Oxford University Press. | The historical phonology of Latin and Greek |
| Aquitanian | Gorrochategui, J. (1984). *Onomástica indígena de Aquitania*. Universidad del País Vasco. | The native personal and divine names of Aquitania |

## Sources mined for gold

The [`primary_sources`](../orthography2ipa/data/gold/primary_sources/README.md) benchmark set is built from the worked transcriptions that the cited sources print. Examples are the Arabic works above and `brissos2014`. Others are the JIPA *Illustrations of the IPA* for Ukrainian (`pompino2017`), Russian (`yanushevskaya2015`), European Portuguese (`cruzferreira1995`) and Brazilian Portuguese (`barbosa2004`). Each gold row names its source and its printed page. The file `sources.json` in that directory lists every source of the set. For each source, it records how the printed folio maps to the page index of the PDF.

## Lexicon sources

The sources of a caller-registered lexicon, such as CMUdict for English, are on the [lexicon](lexicon.md) page.

---
[← IPA Reference](ipa_reference.md) · [Home](index.md) · [Spec authoring rules →](contributing/spec_authoring.md)
