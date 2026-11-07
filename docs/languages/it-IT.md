# Italian (it-IT): Phonology Reference

**Code**: `it-IT` | **Family**: Indo-European > Romance > Italo-Romance | **Script**: Latin (alphabet) | **Quality tier**: research

The `it-IT` spec describes Standard Italian, which rests on Florentine and Tuscan usage. Where the regional varieties disagree, it writes the Standard Northern value. The sources are Lepschy & Lepschy (1988), Maiden (1995), Rogers & d'Arcangeli (2004), Bertinetto & Loporcaro (2005), Krämer (2009) and Canepari (2009).

## C and G softening

The letters ⟨c⟩ and ⟨g⟩ are [tʃ] and [dʒ] before ⟨e⟩ and ⟨i⟩, and [k] and [ɡ] elsewhere. The digraphs ⟨ch⟩ and ⟨gh⟩ always keep the stop. The spec states the softening as `before_e` and `before_i` entries in `positional_graphemes`.

| Grapheme | Before ⟨e i⟩ | Elsewhere | Spec output |
|:---:|:---:|:---:|:---|
| c | tʃ | k | ⟨cena⟩ `ˈtʃena`, ⟨cosa⟩ `ˈkoza` |
| g | dʒ | ɡ | ⟨gente⟩ `ˈdʒente`, ⟨gatto⟩ `ˈɡatːo` |
| ch | k | k | ⟨chiaro⟩ `ˈkjaro` |
| sc | ʃ | sk | ⟨scena⟩ `ˈʃena`, ⟨scala⟩ `ˈskala` |

The ⟨i⟩ of ⟨ci⟩, ⟨gi⟩ and ⟨sci⟩ before another vowel is a spelling marker and has no sound of its own. The spec declares these sequences as graphemes with a `before_vowel` entry, so ⟨cielo⟩ gives `ˈtʃelo` and not a form with [i]. The doubled ⟨cc⟩ and ⟨gg⟩ take the value that the next vowel selects, as in ⟨leggo⟩ `ˈleɡːo` and ⟨legge⟩ `ˈledːʒe`. Only the stop part of the geminate affricate is long (Krämer 2009, §2.2 and §7.1). The sequences ⟨cci⟩ and ⟨ggi⟩ mute the ⟨i⟩ in the same way: ⟨faccia⟩ gives `ˈfatːʃa` and ⟨maggio⟩ gives `ˈmadːʒo`.

The digraph ⟨gu⟩ before a vowel is /ɡw/, the voiced partner of ⟨qu⟩. So ⟨guerra⟩ gives `ˈɡwerːa`. Before a consonant the ⟨u⟩ is an ordinary vowel, as in ⟨gustare⟩.

## GL and the palatal lateral

The digraph ⟨gl⟩ is [ʎ] before ⟨i⟩ and [ɡl] elsewhere. The spec gives ⟨figlio⟩ as `ˈfiʎʎo` and ⟨glottale⟩ as `ɡloˈtːale`. The palatal lateral is long between vowels, and the rule `IT_INHERENT_GEMINATE_GLI` writes it twice. The rules `IT_INHERENT_GEMINATE_GN`, `IT_INHERENT_GEMINATE_SC`, `IT_INHERENT_GEMINATE_TS` and `IT_INHERENT_GEMINATE_DZ` do the same for ⟨gn⟩, ⟨sc⟩ and ⟨z⟩.

## S and Z

A single ⟨s⟩ is [s] at the start of a word and [z] between vowels, as in ⟨casa⟩ `ˈkaza`. Intervocalic voicing is the northern and central norm, and southern varieties keep [s]. Before a consonant, Italian has no voicing contrast. The rule `IT_S_VOICING_BEFORE_VOICED_C` gives [z] before every voiced consonant, so ⟨svelto⟩ gives `ˈzvelto`. Before a voiceless consonant ⟨s⟩ stays [s], as in ⟨pasta⟩ (Bertinetto & Loporcaro 2005, Krämer 2009 §5.3).

The letter ⟨z⟩ is [dz] at the start of a word, so ⟨zero⟩ gives `ˈdzero`. After a consonant the spec ranks [ts] first and [dz] second, so ⟨marzo⟩ gives `ˈmartso`. Between vowels the default [ts] becomes long through `IT_INHERENT_GEMINATE_TS`: ⟨nazione⟩ gives `natˈtsjone`. The doubled ⟨zz⟩ is [tːs] first and [dːz] second, so ⟨pizza⟩ gives `ˈpitːsa`.

## Geminate consonants

Italian contrasts short and long consonants. The spec maps every doubled letter to a long consonant with the length mark ⟨ː⟩.

| Short | Long | Gloss |
|:---|:---|:---|
| ⟨fato⟩ `ˈfato` | ⟨fatto⟩ `ˈfatːo` | fate, done |
| ⟨caro⟩ `ˈkaro` | ⟨carro⟩ `ˈkarːo` | dear, cart |
| ⟨pala⟩ `ˈpala` | ⟨palla⟩ `ˈpalːa` | shovel, ball |

Raddoppiamento fonosintattico lengthens a consonant across a word boundary. It belongs to the sandhi layer, and the spec does not model it.

## Vowels

Italian has seven stressed vowels, /a e ɛ i o ɔ u/. In unstressed syllables the open-mid /ɛ ɔ/ do not occur, which leaves five vowels. In the reference grammars, a stressed vowel is long in an open syllable and short in a closed one, as in [ˈpaːdre] and [ˈfɔrte].

The spec writes only ⟨e⟩ /e/ and ⟨o⟩ /o/ for the mid vowels, and it does not write vowel length. The choice between the close-mid and the open-mid vowel depends on the word and its history, and the spelling does not mark it. So ⟨bello⟩ gives `ˈbelːo` and ⟨forte⟩ gives `ˈforte`.

The sequences ⟨ia ie io iu⟩ and ⟨ua ue uo⟩ are glide plus vowel. The spec gives ⟨pianta⟩ as `ˈpjanta`, ⟨buono⟩ as `ˈbwono` and ⟨quando⟩ as `ˈkwando`.

## Stress

The `stress` block puts stress on the penultimate syllable by default. A written accent (⟨à è é ì ò ó ù⟩) always marks the stressed vowel and overrides the default. Antepenultimate stress, as in ⟨tavola⟩, is lexical. Standard spelling does not require an accent on it, so the spec cannot predict it.

## Known limitations

The spec cannot recover these contrasts from the spelling, and a downstream lexicon must supply them:

| Contrast | Example |
|:---|:---|
| Close-mid against open-mid vowels | ⟨bello⟩ has [ɛ], the spec writes `e` |
| [ts] against [dz] for ⟨z⟩ and ⟨zz⟩ | ⟨azzurro⟩ [addzurro] against ⟨pizza⟩ [pittsa] |
| Glide against hiatus for ⟨i u⟩ before a vowel | ⟨Adriana⟩ [adriana] against ⟨piano⟩ [pjano] |
| Antepenultimate stress | ⟨tavola⟩ |
| Tuscan [s] against Northern [z] between vowels | ⟨casa⟩ |

The spec `notes` give the share of the remaining error that each contrast causes on the WikiPron gold. The scores are on the [scoreboard](../evaluation/generated/scoreboard.md).

## References

- Lepschy, A.L. & Lepschy, G. (1988). *The Italian Language Today* (2nd ed.). Routledge.
- Maiden, M. (1995). *A Linguistic History of Italian*. Longman.
- Rogers, D. & d'Arcangeli, L. (2004). *Italian*. Journal of the IPA, 34(1), 117-121.
- Bertinetto, P.M. & Loporcaro, M. (2005). The sound pattern of Standard Italian, as compared with the varieties spoken in Florence, Milan and Rome. *Journal of the International Phonetic Association*.
- Krämer, M. (2009). *The Phonology of Italian*. Oxford University Press.
- Canepari, L. (2009). *Dizionario di pronuncia italiana* (DiPI). Zanichelli.
- Wikipedia: [Italian phonology](https://en.wikipedia.org/wiki/Italian_phonology)

---
[← French](fr-FR.md) · [Home](../index.md) · [Ligurian / Genoese →](lij.md)
