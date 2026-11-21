# Paraibano Portuguese (pt-BR-x-paraiba)

<!-- agent-hint
covers: how the Paraibano Portuguese spec differs from `pt-BR`
source: `orthography2ipa/data/pt-BR-x-paraiba.json`
generated: no
verify: `PYTHONPATH=$PWD python -m pytest tests/test_docs_prose.py tests/test_br_paraiba.py`
see: `docs/languages/pt-BR.md`, `docs/languages/pt-BR-dialects.md`
-->

| Field | Value |
|:---|:---|
| Code | `pt-BR-x-paraiba` |
| Alias | `pt-BR-x-pb` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | research |
| ISO 639-3 | `por` |
| Parent | `pt-BR` |
| Sources | Hora, Henrique & Amorim (2018), Henrique, Amorim & Hora (2022), Battisti & Dornelles Filho (2015), Mota & Lopes (2018), Callou, Serra & Cunha (2015), Aragão (2020), Silva, Araújo & Viana (2018) |

This spec models the Portuguese of the state of Paraíba, in the Brazilian Northeast. The consonant studies describe João Pessoa, the capital, through the VALPB corpus (*Variação Linguística na Paraíba*). The vowel studies cover the whole state through the *Atlas Linguístico da Paraíba*.

The alias `pt-BR-x-pb` uses the state code. The spec key spells out the state, because "PB" also abbreviates *português brasileiro* in Brazilian linguistics.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, "pt-BR-x-paraiba")`. For the scores of the spec, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

## Parent and ancestry

The spec sets `parent` to `pt-BR` and inherits Brazilian Portuguese through `graphemes_base`, `allophones_base` and `positional_graphemes_base`. It shares four features with [`pt-BR-x-recife`](pt-BR-dialects.md#pernambucano-pt-br-x-recife): dental /t d/ before /i/, open pretonic vowels, the aspirate coda /R/, and the deletion of a word-final /R/. It differs from Recife in the coda /S/. The final vowels and the nasal diphthongs come from `pt-BR`.

## Modelled features

The stops /t d/ stay stops before /i/, except after a coda [ʃ ʒ]. In the VALPB corpus, palatalisation occurs *"em torno de 7% nas oclusivas antes de [i]"* (Hora, Henrique & Amorim 2018: 280). The two studies behind that rate found 7 % and 5,45 % (p. 288). The ALiB rates the palatalisation in João Pessoa as *"baixa"* (Battisti & Dornelles Filho 2015: 226). The positional map gives the plain stop before ⟨i⟩, and the spec limits `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED` to the context after [ʃ ʒ]: `tia` [ˈtiɐ], `dia` [ˈdiɐ], `noite` [ˈnojti], `tarde` [ˈtahdi]. After a coda palatal fricative the affricate is the more frequent form: *"dentre os contextos precedentes, a fricativa palatal foi a que mais condicionou a taxa de produção das oclusivas dentais (56.4%)"* (p. 292). After a glide the rate is 3.7 %, after a pause 1.8 %, and after a vowel, a liquid or a nasal 3.1 %. So `desde` is [ˈdeʒd͡ʒi], `festival` is [feʃt͡ʃiˈvaw] and `destino` is [deʃˈt͡ʃĩnu], while `mestre` keeps [ˈmeʃtɾi], because ⟨tr⟩ is not /t/ before [i].

A coda /S/ is alveolar, except before /t d/. In the Northeast, *"à exceção de Recife, a forma mais utilizada é a alveolar"* (Hora, Henrique & Amorim 2018: 282). In João Pessoa, *"é quase categórico o uso [ʃ, ʒ] antes das consoantes oclusivas dentais [t] e [d], enquanto antes das outras consoantes, a pronúncia alveolar é a predominante"* (p. 283). The palatal reaches 97 % before a coronal, in 6.265 tokens (Henrique, Amorim & Hora 2022: 5). The rule `PB_CODA_S_BEFORE_T` gives [ʃ] before [t], and `PB_CODA_Z_BEFORE_D` gives [ʒ] before [d]: `posto` [ˈpoʃtu], `desde` [ˈdeʒd͡ʒi]. Coda ⟨x⟩ shares the archiphoneme, so `texto` is [ˈteʃtu] and `extinto` is [eʃˈt͡ʃĩtu]. Before other consonants and at the end of a word, the coda keeps the `pt-BR` values: `casca` [ˈkaskɐ], `mesmo` [ˈmezmu], `dois` [ˈdojs]. Speakers in João Pessoa hear *"ca[ʃ]ca", "me[ʒ]mo" e "doi[ʃ]"* as stereotypes of Rio de Janeiro and Recife (Hora, Henrique & Amorim 2018: 284).

Pretonic /e o/ open to [ɛ ɔ] before an open, nasal or low stressed vowel. Mota & Lopes (2018: 215) find that the pretonics *"têm uma maior probabilidade de se tornarem médias abertas no contexto de tônica também de timbre aberto (médias-baixas), médias nasais e diante da vogal baixa [a]"*. The *Atlas Linguístico da Paraíba* finds *"uma predominância das vogais médias abertas"* over the whole state (Aragão 2020: 172). In the same atlas, pretonic /O/ lowers in 81 of 98 tokens (Silva, Araújo & Viana 2018: 277). The rules `NE_PRETONIC_OPEN_E` and `NE_PRETONIC_OPEN_O` give `pedaço` [pɛˈdasu], `bolacha` [bɔˈlaʃɐ], `fogão` [fɔˈɡɐ̃w̃].

A coda /R/ is the aspirate [h], the *"[- vibrante] e [- anterior]"* norm of the Northeastern capitals (Callou, Serra & Cunha 2015: 197). João Pessoa deletes a word-final /R/ in 97 % of verbs and 95 % of other words (p. 207). The positional map gives [h] in the coda, and `NE_FINAL_R_DELETION` drops the final /R/: `porta` [ˈpohtɐ], `verde` [ˈvehdi], `mar` [ˈma].

| Spelling | IPA | Feature |
|:---|:---|:---|
| `tia` | ˈtiɐ | /t/ stays a stop before /i/ |
| `noite` | ˈnojti | /t/ stays a stop before a raised final ⟨e⟩ |
| `posto` | ˈpoʃtu | coda /S/ gives [ʃ] before /t/ |
| `desde` | ˈdeʒd͡ʒi | coda /S/ gives [ʒ] before /d/, and /d/ is the affricate after it |
| `festival` | feʃt͡ʃiˈvaw | /t/ is the affricate before /i/ after a coda [ʃ] |
| `tarde` | ˈtahdi | /d/ stays a stop after a coda [h] |
| `casca` | ˈkaskɐ | coda /S/ stays [s] before other consonants |
| `dois` | ˈdojs | word-final /S/ stays [s] |
| `fogão` | fɔˈɡɐ̃w̃ | pretonic /o/ opens before a nasal stressed vowel |
| `verde` | ˈvehdi | coda /R/ gives [h] |
| `mar` | ˈma | word-final /R/ is deleted |
| `dentes` | ˈdẽtis | final ⟨-es⟩ raises, no affrication, alveolar /S/ |

## What the spec does not model

The /t d/ and coda /S/ studies cover João Pessoa only. No opened source gives a rate for these two features in the interior of the state. The open pretonic vowels are the one feature with data for the whole state.

Henrique, Amorim & Hora (2022: 16) recorded six VALPB speakers again. In that sample the palatal coda also occurs before /n/. The spec does not model it, because six speakers do not support a default reading.

Some forms are frequent but are not the majority form. A word-final /S/ before a pause drops in 24,4 % of tokens (Henrique, Amorim & Hora 2022: 5). The atlas also lists the loss of final /l R s/, the reduction of /nd/, and the vocalisation of ⟨lh nh⟩, which depends on the speaker's schooling (Aragão 2020: 172). The spec gives the majority forms only.

No opened source describes the final vowels or the nasal diphthongs of Paraíba. The spec keeps the `pt-BR` values: `dentes` [ˈdẽtis], `homem` [ˈõmẽj̃].

## Input contract

Input is standard Brazilian Portuguese orthography. The spec gives the reading of João Pessoa where the sources differ by place.

## Limitations

No board gold exists for this variety. So the correctness of the spec rests on its citations, not on a PER. Each feature varies in speech, and the spec gives the majority form.

## Sources

- Aragão, Maria do Socorro Silva de (2020). "Atlas Linguístico da Paraíba". *Acta Semiótica et Lingvistica* 25(1). <https://periodicos.ufpb.br/index.php/actas/article/view/53679>
- Battisti, Elisa & Dornelles Filho, Adalberto Ayjara (2015). "Análise em tempo real da palatalização de /t/ e /d/ no português falado em uma comunidade ítalo-brasileira". *Revista da ABRALIN* 14(1), 221-246. <https://revista.abralin.org/index.php/abralin/article/download/1239/1162/549>
- Callou, Dinah, Serra, Carolina & Cunha, Cláudia (2015). "Mudança em curso no português brasileiro: o apagamento do R no dialeto nordestino". *Revista da ABRALIN* 14(1), 195-219. <https://revista.abralin.org/index.php/abralin/article/download/1238/1161>
- Henrique, Pedro Felipe de Lima, Amorim, A.W.D. & Hora, Dermeval da (2022). "O papel do estilo no uso do /S/ pós-vocálico em uma amostra de recontato". *Cadernos de Linguística* 3(1), e621. Pages of the Redalyc PDF. <https://doi.org/10.25189/2675-4916.2022.v3.n1.id621>
- Hora, Dermeval da, Henrique, Pedro Felipe de Lima & Amorim, A.W.D. (2018). "Produção e percepção: o processo de palatalização em jogo". *Diadorim* 20(2), 280-296. <https://doi.org/10.35520/diadorim.2018.v20n2a18269>
- Mota, Jacyra Andrade & Lopes, Paulo Henrique de Souza (2018). "Os subfalares do Norte e o traçado das vogais médias pretônicas". *Estudos de Lingüística Galega*, volume especial I, 209-218. <https://doi.org/10.15304/elg.ve1.3480>
- Silva, P.J.R., Araújo, A.A. & Viana, R.B.M. (2018). "O alçamento e o abaixamento da pretônica /O/ nos Atlas Linguísticos do Ceará, Paraíba e Bahia". *Entretextos* 18(1), 261-284. <https://ojs.uel.br/revistas/uel/index.php/entretextos/article/view/33138>

---
[← Cuiabano Portuguese](pt-BR-x-cuiaba.md) · [Home](../index.md) · [Angolan Portuguese →](pt-AO.md)
