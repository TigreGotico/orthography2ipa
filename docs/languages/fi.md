# Finnish (`fi`)

**Code**: `fi` | **Family**: Uralic > Finnic | **Script**: Latin (alphabet) | **Quality tier**: production

The `fi` spec describes Standard Finnish (yleiskieli). The orthography is almost phonemic: each grapheme maps to one phoneme. Both consonant length and vowel length are phonemic, and the spelling writes them as double letters.

## Orthographic depth and production threshold

Finnish has a shallow (phonemic) orthography, so the shallow threshold of 0.15 PER applies (see [quality tiers](../quality_tiers.md#the-per-threshold)). The irregularities are few and can be listed: ⟨ng⟩ is /ŋː/, ⟨nk⟩ is /ŋk/, and the loanword letters ⟨b d g f⟩ occur.

## Phonology

The eight vowels /i y e ø æ ɑ o u/ each have a short and a long value, written single and double. The spec has a grapheme for each of the 18 phonemic diphthongs, such as ⟨ai⟩, ⟨äy⟩ and ⟨uo⟩, so that each one counts as one syllable nucleus. Each geminate consonant is a grapheme too: ⟨kk⟩ is [kː] and ⟨ss⟩ is [sː].

Vowel harmony between front and back vowels limits which suffixes occur. It does not change the map from grapheme to phoneme, so the spec does not model it.

Stress is fixed on the first syllable, and the `stress` block states this with `default_position: 1`. The spec gives `ˈkeŋkæ` for `kenkä`, `ˈkeŋːæt` for `kengät` and `ˈhelsiŋki` for `Helsinki`.

## Benchmark

Three gold rows score the spec. For the figures, see the [scoreboard](../scoreboard.md). The `wikipron` row is crowd-scraped and can qualify a promotion. It is one of the largest single gold sets on the board. The `ipadict` row is the output of a rule script, and the `vox_communis` row is epitran-derived. Neither of them can gate a promotion.

## Known limitations

Boundary gemination (rajageminaatio) is a sandhi effect across words, as in *tule tänne* [tulet tænːe]. The spelling does not write it, so the spec cannot get it from the text. The spec gives `ˈtule ˈtænːe`. Gold sets of single words do not contain it.

The spec has no mapping for ⟨š⟩ and ⟨ž⟩, which occur in loans. The engine drops each of them with an `UnmappedGraphemeWarning`, so `šakki` comes out as `ˈɑkːi`.

## Sources

- Abondolo, D. (ed.) (1998). *The Uralic Languages*. Routledge.
- Hakulinen, L. (1979). *The Structure and Development of the Finnish Language*.
- Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*.

---
[← Basque (Euskara) and its dialects](eu.md) · [Home](../index.md) · [Vietnamese →](vi.md)
