# -*- coding: utf-8 -*-
"""Regenerate the Khmer (``km``) spec in ``data/km.json``.

The grapheme table is a cross-product — every consonant against the bânták,
tôndôkhéad and rôbat diacritics, every dominant consonant against the
sonorant subscripts whose series differs from its own — and the register
rules are one rule per dependent vowel sign, so the spec is generated rather
than hand-written and this script is where a correction goes.

Usage:
  python scripts/gen_khmer.py

Sources encoded here:
  Huffman, Franklin E. (1970) *Cambodian System of Writing and Beginning
  Reader*. Yale University Press — the IPA column of the Khmer script
  consonant and dependent-vowel tables (Wikipedia, "Khmer script",
  reproduces Huffman's values and cites him for them).
  Jacob, Judith M. (1968) *Introduction to Cambodian*. Oxford University
  Press — cited for the length distinction between the o-series ⟨ា⟩ and
  ⟨ៀ⟩, which this broad transcription does not carry.
  The vowel-nucleus and independent-vowel values follow Huffman's tables as
  reproduced in the Wikipedia "Khmer language" article.
"""
import json, collections, pathlib

# ── Consonants: letter -> (consonant value, series) ───────────────────────
CONS = [
    ("ក", "k",  "a"), ("ខ", "kʰ", "a"), ("គ", "k",  "o"), ("ឃ", "kʰ", "o"),
    ("ង", "ŋ",  "o"),
    ("ច", "c",  "a"), ("ឆ", "cʰ", "a"), ("ជ", "c",  "o"), ("ឈ", "cʰ", "o"),
    ("ញ", "ɲ",  "o"),
    ("ដ", "ɗ",  "a"), ("ឋ", "tʰ", "a"), ("ឌ", "ɗ",  "o"), ("ឍ", "tʰ", "o"),
    ("ណ", "n",  "a"),
    ("ត", "t",  "a"), ("ថ", "tʰ", "a"), ("ទ", "t",  "o"), ("ធ", "tʰ", "o"),
    ("ន", "n",  "o"),
    ("ប", "ɓ",  "a"), ("ផ", "pʰ", "a"), ("ព", "p",  "o"), ("ភ", "pʰ", "o"),
    ("ម", "m",  "o"),
    ("យ", "j",  "o"), ("រ", "r",  "o"), ("ល", "l",  "o"), ("វ", "ʋ",  "o"),
    ("ស", "s",  "a"), ("ហ", "h",  "a"), ("ឡ", "l",  "a"), ("អ", "ʔ",  "a"),
]

# Supplementary consonants (Khmer script, "Supplementary consonants"):
# digraphs built on ⟨ហ⟩ plus a subscript, and ⟨ប៉⟩, used for foreign sounds.
SUPP = [
    ("ហ្គ",  "ɡ", "a"), ("ហ្គ៊", "ɡ", "o"),
    ("ហ្ន",  "n", "a"),
    ("ហ្ម",  "m", "a"), ("ហ្ល",  "l", "a"),
    ("ហ្វ",  "f", "a"), ("ហ្វ៊", "f", "o"),
    ("ហ្ស",  "ʒ", "a"), ("ហ្ស៊", "ʒ", "o"),
]

MUUSIKATOAN = "៉"   # ៉  o-series -> a-series
TRIISAP = "៊"       # ៊  a-series -> o-series
BANTOC = "់"        # ់
ROBAT = "៌"         # ៌
TOANDAKHIAT = "៍"   # ៍
KAKABAT = "៎"       # ៎
AHSDA = "៏"         # ៏
SAMYOK = "័"        # ័

# ⟨៉⟩ converts the o-series sonorants ង ញ ម យ រ វ (and ល) to a-series, and
# turns ⟨ប⟩ [ɓ] into [p]; ⟨៊⟩ converts the a-series ស ហ ប អ to o-series.
MUUS_BASE = {"ង": "ŋ", "ញ": "ɲ", "ម": "m", "យ": "j", "រ": "r",
             "វ": "ʋ", "ល": "l", "ប": "p", "ន": "n"}
TRII_BASE = {"ស": "s", "ហ": "h", "ប": "ɓ", "អ": "ʔ"}

# ── Dependent vowels: sign -> (a-series, o-series, extra a-series cands) ──
VOWELS = [
    ("ា", "aː", "iə"),         # ា
    ("ិ", "ə",  "ɨ"),          # ិ
    ("ី", "əj", "iː"),         # ី
    ("ឹ", "ə",  "ɨ"),          # ឹ
    ("ឺ", "əː", "ɨː"),         # ឺ
    ("ុ", "o",  "u"),          # ុ
    ("ូ", "oː", "uː"),         # ូ
    ("ួ", "uə", "uə"),         # ួ
    ("ើ", "aə", "əː"),         # ើ
    ("ឿ", "ɨə", "ɨə"),         # ឿ
    ("ៀ", "iə", "iə"),         # ៀ
    ("េ", "eː", "eː"),         # េ
    ("ែ", "ae", "ɛː"),         # ែ
    ("ៃ", "aj", "əj"),         # ៃ
    ("ោ", "ao", "oː"),         # ោ
    ("ៅ", "aɨ", "əɨ"),         # ៅ
]

NIKAHIT = "ំ"  # ំ
REAHMUK = "ះ"  # ះ
YUKOLEA = "ៈ"  # ៈ

# Vowel-plus-diacritic rhymes ("Modification by diacritics").
RHYMES = [
    ("ុ" + NIKAHIT, "om",  "um"),    # ុំ
    (NIKAHIT,            "ɑm",  "um"),    # ំ
    ("ា" + NIKAHIT, "am",  "ŏəm"),   # ាំ
    (REAHMUK,            "ah",  "ĕəh"),   # ះ
    ("ិ" + REAHMUK, "eh",  "ih"),    # ិះ
    ("ុ" + REAHMUK, "oh",  "uh"),    # ុះ
    ("េ" + REAHMUK, "eh",  "ih"),    # េះ
    ("ោ" + REAHMUK, "ɑh",  "ŭəh"),   # ោះ
    ("ើ" + REAHMUK, "əh",  "əh"),    # ើះ
    ("ឹ" + REAHMUK, "əh",  "əh"),    # ឹះ
    ("ែ" + REAHMUK, "eh",  "eh"),    # ែះ
    (YUKOLEA,            "aʔ",  "ĕəʔ"),   # ៈ
    (SAMYOK,             "a",   "ŏə"),    # ័
    # ⟨៏⟩ âsda marks that a consonant with no dependent vowel is read with its
    # inherent vowel instead of as a final consonant, so it spells the
    # inherent vowel itself.
    (AHSDA,              "ɑː",  "ɔː"),    # ៏
]

# ── Independent vowels (their own nucleus; no inherent vowel) ────────────
INDEP = {
    "ឥ": ["ʔe", "ʔə", "ʔəj"],
    "ឦ": ["ʔej"],
    "ឧ": ["ʔu", "ʔo"],
    "ឩ": ["ʔuː"],
    "ឪ": ["ʔɨw", "ʔəw"],
    "ឫ": ["rɨ"],
    "ឬ": ["rɨː"],
    "ឭ": ["lɨ"],
    "ឮ": ["lɨː"],
    "ឯ": ["ʔae", "ʔɛː", "ʔeː"],
    "ឰ": ["ʔaj"],
    "ឱ": ["ʔao"],
    "ឲ": ["ʔao"],
    "ឳ": ["ʔaw"],
}

DIGITS = {c: [""] for c in "០១២៣៤៥៦៧៨៩"}
PUNCT = {c: [""] for c in "។៕៖៙៚៘​៓"}

# ═════════════════════════════════════════════════════════════════════════
graphemes: "collections.OrderedDict[str, list]" = collections.OrderedDict()
a_series: list = []
o_series: list = []

for letter, value, series in CONS:
    graphemes[letter] = [value]
    (a_series if series == "a" else o_series).append(letter)

for key, value, series in SUPP:
    graphemes[key] = [value]
    (a_series if series == "a" else o_series).append(key)

for base, value in MUUS_BASE.items():
    key = base + MUUSIKATOAN
    graphemes[key] = [value]
    a_series.append(key)
for base, value in TRII_BASE.items():
    key = base + TRIISAP
    graphemes[key] = [value]
    o_series.append(key)

# Bantoc sits on the syllable's FINAL consonant, so ⟨C់⟩ is one grapheme:
# that keeps the shortening it triggers visible to the nucleus one slot back
# as a `followed_by_grapheme` context.
bantoc_keys: list = []
for letter, value, _series in CONS:
    key = letter + BANTOC
    graphemes[key] = [value]
    bantoc_keys.append(key)
for base, value in MUUS_BASE.items():
    key = base + MUUSIKATOAN + BANTOC
    graphemes[key] = [value]
    bantoc_keys.append(key)
for base, value in TRII_BASE.items():
    key = base + TRIISAP + BANTOC
    graphemes[key] = [value]
    bantoc_keys.append(key)

# Consonant clusters whose SERIES is not the subscript's. In a cluster the
# dominant member decides how a following dependent vowel is read — stops and
# fricatives dominate sonorants, and between two dominant members the
# subscript wins (Huffman 1970). The engine reads the letter immediately
# before the vowel sign, which is the subscript, so that is already right
# except when a dominant main consonant carries a sonorant subscript of the
# OTHER series: ⟨ខ្វ⟩ in ខ្មែរ is a-series although ⟨វ⟩ alone is o-series.
# Those clusters are spelled out as single graphemes so the vowel sign sees
# the cluster and its series instead of the subscript's.
DOMINANT = {"k", "kʰ", "c", "cʰ", "ɗ", "t", "tʰ", "ɓ", "p", "pʰ",
            "s", "h", "ʔ", "ɡ", "f", "ʒ"}
COENG = "\u17d2"
_series_of = {l: s_ for l, _v, s_ in CONS}
_value_of = {l: v for l, v, _s in CONS}
cluster_keys = []
for c1, v1, s1 in CONS:
    if v1 not in DOMINANT:
        continue
    for c2, v2, s2 in CONS:
        if v2 in DOMINANT or s2 == s1:
            continue
        # ⟨ប⟩ bâ spells [ɓ] only before a vowel; in a cluster it is [p].
        head = "p" if c1 == "ប" else v1
        key = c1 + COENG + c2
        graphemes[key] = [head + v2]
        cluster_keys.append((key, s1))
# ⟨ប⟩ bâ spells [ɓ] only before a vowel, so it is [p] in front of ANY
# subscript — including the dominant ones the loop above skips, which keep
# their own series because between two dominant members the subscript wins.
for c2, v2, s2 in CONS:
    if v2 not in DOMINANT:
        continue
    key = "ប" + COENG + c2
    graphemes[key] = ["p" + v2]
    cluster_keys.append((key, s2))

for key, s_ in cluster_keys:
    (a_series if s_ == "a" else o_series).append(key)

# ⟨៍⟩ toandakhiat and ⟨៌⟩ robat both silence the letter they sit on.
for letter, _value, _series in CONS:
    graphemes[letter + TOANDAKHIAT] = [""]
    graphemes[letter + ROBAT] = [""]

dependent_vowels: list = []
ALT = {"ូ": ["ou"], "ី": ["ej"], "ៃ": ["ej"]}
for sign, a_val, _o_val in VOWELS:
    graphemes[sign] = [a_val] + ALT.get(sign, [])
    dependent_vowels.append(sign)
for sign, a_val, _o_val in RHYMES:
    graphemes[sign] = [a_val]
    dependent_vowels.append(sign)

for key, cands in INDEP.items():
    graphemes[key] = list(cands)
graphemes.update(DIGITS)
graphemes.update(PUNCT)
graphemes[KAKABAT] = [""]
graphemes["ៗ"] = [""]

# ── allophone rules ──────────────────────────────────────────────────────
CONS_PHONEMES = sorted({v for _l, v, _s in CONS} | {v for _k, v, _s in SUPP}
                       | set(MUUS_BASE.values()) | set(TRII_BASE.values()))

SERIES_NOTE = (
    "Khmer consonant letters fall into two registers, the a-series (inherent "
    "vowel â [ɑː]) and the o-series (inherent vowel ô [ɔː]). The series is a "
    "property of the LETTER, not of the sound it spells: ⟨ក⟩ and ⟨គ⟩ both "
    "spell [k] but ⟨កា⟩ is [kaː] and ⟨គា⟩ is [kiə]. Every dependent vowel "
    "sign therefore has two readings, chosen by the series of the consonant "
    "it is attached to, and the spec gives the a-series reading in the "
    "grapheme table and shifts it here. The registers descend from a Middle "
    "Khmer voicing contrast that was lost after it had already reshaped the "
    "following vowel. The o-series ⟨ា⟩ is the high centring diphthong [iə], "
    "the same nucleus ⟨ៀ⟩ spells; Jacob 1968 separates the two by length "
    "([iːə] against [iə]), a distinction this broad transcription does not "
    "carry. Source: Huffman 1970, Cambodian System of Writing and Beginning "
    "Reader."
)

rules: list = []

# 1. The inherent vowel of an o-series letter is [ɔː], not [ɑː]. The inherent
#    vowel is glued to the consonant in one slot, so the rule fires on the
#    vowel SEGMENT inside it and is anchored by `preceded_by_phoneme`.
rules.append({
    "id": "KM_INHERENT_O_SERIES",
    "phonemes": ["ɑː"],
    "surface": "ɔː",
    "preceded_by_phoneme": CONS_PHONEMES,
    "grapheme": o_series,
    "notes": SERIES_NOTE,
})

# 2. Dependent vowel signs: the o-series reading after an o-series letter.
for sign, a_val, o_val in VOWELS + RHYMES:
    if a_val == o_val:
        continue
    rules.append({
        "id": "KM_VOWEL_O_%04X" % ord(sign[-1]) if len(sign) == 1 else
              "KM_VOWEL_O_" + "_".join("%04X" % ord(c) for c in sign),
        "phonemes": [a_val],
        "surface": o_val,
        "grapheme": [sign],
        "preceded_by_grapheme": o_series,
        "notes": SERIES_NOTE,
    })

BANTOC_NOTE = (
    "Bânták ⟨់⟩, written over the last consonant of a syllable, shortens the "
    "nucleus and changes its quality: inherent â [ɑː] becomes [ɑ], inherent "
    "ô [ɔː] becomes [u] before a final labial and [ŏə] elsewhere, and the ⟨ា⟩ "
    "sign becomes [a] in the a-series and, in the o-series, [ĕə] before a "
    "final ⟨ក គ ង ហ⟩ and [ŏə] elsewhere. Source: Huffman 1970."
)
LABIAL_BANTOC = [c + BANTOC for c in "បពភផម"]
rules.append({
    "id": "KM_BANTOC_O_LABIAL",
    "phonemes": ["ɔː"],
    "surface": "u",
    "preceded_by_phoneme": CONS_PHONEMES,
    "followed_by_grapheme": LABIAL_BANTOC,
    "notes": BANTOC_NOTE,
})
for src, dst in (("ɑː", "ɑ"), ("ɔː", "ŏə")):
    rules.append({
        "id": "KM_BANTOC_" + ("A" if src == "ɑː" else "O"),
        "phonemes": [src],
        "surface": dst,
        "preceded_by_phoneme": CONS_PHONEMES,
        "followed_by_grapheme": bantoc_keys,
        "notes": BANTOC_NOTE,
    })
rules.append({
    "id": "KM_BANTOC_AA",
    "phonemes": ["aː"],
    "surface": "a",
    "grapheme": ["ា"],
    "followed_by_grapheme": bantoc_keys,
    "notes": BANTOC_NOTE,
})
VELAR_BANTOC = [c + BANTOC for c in "កគងហ"]
rules.append({
    "id": "KM_BANTOC_AA_O_VELAR",
    "phonemes": ["iə"],
    "surface": "eə",
    "grapheme": ["ា"],
    "followed_by_grapheme": VELAR_BANTOC,
    "notes": BANTOC_NOTE,
})
rules.append({
    "id": "KM_BANTOC_AA_O",
    "phonemes": ["iə"],
    "surface": "ŏə",
    "grapheme": ["ា"],
    "followed_by_grapheme": bantoc_keys,
    "notes": BANTOC_NOTE,
})

# (iii) o-series inherent ô under bânták is [u] before a final labial


# 2b. Minor (unstressed) presyllables. A consonant that opens a weak initial
#     syllable and carries no written vowel is read with its inherent vowel
#     shortened, as if bânták were written over it.
PRESYLLABLE_NOTE = (
    "An initial consonant with no dependent vowel in a weak (unstressed) "
    "presyllable is pronounced with its inherent vowel shortened, as if the "
    "bânták diacritic were written: a-series â [ɑː] becomes [ɑ] and o-series "
    "ô [ɔː] becomes [ŏə]; in casual speech both reduce further to [ə]. Only "
    "the final syllable of a Khmer word is strong, so the condition here is "
    "that another nucleus follows in the same word. Source: Huffman 1970."
)
for src, dst in (("ɑː", "ɑ"), ("ɔː", "ŏə")):
    rules.append({
        "id": "KM_PRESYLLABLE_" + ("A" if src == "ɑː" else "O"),
        "phonemes": [src],
        "surface": dst,
        "preceded_by_phoneme": CONS_PHONEMES,
        "followed_by_nucleus": True,
        "notes": PRESYLLABLE_NOTE,
    })

# 2c. ⟨ិ⟩ and ⟨ុ⟩ in an open syllable.
OPEN_NOTE = (
    "⟨ិ⟩ and ⟨ុ⟩ are [ə]/[ɨ] and [o]/[u] in a closed syllable but [e]/[i] and "
    "[o]/[u] closed by a glottal stop in a stressed syllable with no written "
    "final consonant. Source: Huffman 1970."
)
for sign, val, surface in (("ិ", "ə", "eʔ"), ("ិ", "ɨ", "iʔ"),
                           ("ុ", "o", "oʔ"), ("ុ", "u", "uʔ")):
    rules.append({
        "id": "KM_OPEN_%04X_%s" % (ord(sign[-1]), val),
        "phonemes": [val],
        "surface": surface,
        "grapheme": [sign],
        "word_final": True,
        "notes": OPEN_NOTE,
    })

# 3. Final-consonant realisations. Khmer allows one final consonant and
#    releases none of them.
rules.append({
    "id": "KM_FINAL_R_SILENT",
    "phonemes": ["r"],
    "surface": "",
    "syllable_position": "coda",
    "word_final": True,
    "notes": (
        "Word-final ⟨រ⟩ rô is silent in the standard (central plains) "
        "dialect; Northern Khmer keeps it. Source: Huffman 1970."
    ),
})
rules.append({
    "id": "KM_FINAL_S_H",
    "phonemes": ["s"],
    "surface": "h",
    "syllable_position": "coda",
    "word_final": True,
    "notes": (
        "Word-final ⟨ស⟩ sâ is [h] (phonetically close to [ç]); Khmer has no "
        "final sibilant. Source: Huffman 1970."
    ),
})
rules.append({
    "id": "KM_FINAL_IMPLOSIVE_T",
    "phonemes": ["ɗ"],
    "surface": "t",
    "syllable_position": "coda",
    "word_final": True,
    "notes": (
        "The implosives are onset-only: ⟨ដ⟩ dâ and ⟨ឌ⟩ dô are [t] in final "
        "position. Source: Huffman 1970."
    ),
})
rules.append({
    "id": "KM_FINAL_B_P",
    "phonemes": ["ɓ"],
    "surface": "p",
    "syllable_position": "coda",
    "word_final": True,
    "notes": (
        "⟨ប⟩ bâ spells [ɓ] only before a vowel; anywhere else — in a coda "
        "or as the head of a cluster — it is [p]. Source: Huffman 1970."
    ),
})
GLOTTAL_NOTE = (
    "A final ⟨ក⟩/⟨ខ⟩ is a glottal stop rather than [k] after the vowels "
    "[ɑː aː iə ɨə uə ɑ a ĕə ŭə] — the short and long low and centring "
    "nuclei. After the other vowels it stays [k]. Source: Huffman 1970."
)
GLOTTAL_AFTER = ["ɑː", "aː", "iə", "ɨə", "uə", "ɑ", "a", "ĕə", "ŭə"]
for src in ("k", "kʰ"):
    rules.append({
        "id": "KM_FINAL_K_GLOTTAL" + ("_ASP" if src == "kʰ" else ""),
        "phonemes": [src],
        "surface": "ʔ",
        "syllable_position": "coda",
        "word_final": True,
        "preceded_by_phoneme": GLOTTAL_AFTER,
        "notes": GLOTTAL_NOTE,
    })
for src, dst in (("kʰ", "k"), ("cʰ", "c"), ("tʰ", "t"), ("pʰ", "p")):
    rules.append({
        "id": "KM_FINAL_DEASPIRATE_" + dst.upper(),
        "phonemes": [src],
        "surface": dst,
        "syllable_position": "coda",
        "word_final": True,
        "notes": (
            "The aspirate letters are aspirated only before a vowel; in final "
            "position aspiration is not realised and the stop is unreleased. "
            "Source: Huffman 1970."
        ),
    })

spec = collections.OrderedDict()
spec["code"] = "km"
spec["name"] = "Khmer"
spec["glottolog_code"] = "cent1989"
spec["script"] = "Khmer"
spec["script_type"] = "abugida"
spec["inherent_vowel"] = "ɑː"
spec["coda_no_inherent_vowel"] = True
spec["iso639_3"] = "khm"
spec["quality"] = "research"
spec["graphemes"] = graphemes
spec["dependent_vowels"] = dependent_vowels
spec["allophone_rules"] = rules
spec["allophone_passes"] = 2
spec["notes"] = (
    "Khmer (Cambodian), written in the Khmer abugida. The spec is organised "
    "around the two-series register system: every consonant letter carries "
    "an inherent vowel, â [ɑː] for the a-series and ô [ɔː] for the o-series, "
    "and that same series decides which of its two readings each dependent "
    "vowel sign takes. The grapheme table gives the a-series reading and the "
    "allophone rules shift it after an o-series letter. Khmer is not tonal. "
    "A word takes at most one final consonant, and finals are unreleased: "
    "final ⟨រ⟩ is silent, final ⟨ស⟩ is [h], final ⟨ដ ឌ⟩ are [t], final ⟨ប⟩ "
    "is [p], the aspirates lose their aspiration, and final ⟨ក ខ⟩ are a "
    "glottal stop after a low or centring nucleus. Three known gaps. A "
    "dominant consonant also governs a NON-DOMINANT one later in the same "
    "word, across an intervening vowel, and the rules here read only the "
    "letter immediately before the vowel sign: ⟨សេរីភាព⟩ is [seːrəjpʰiəp], "
    "with the a-series ⟨ី⟩ that the leading ⟨ស⟩ imposes on ⟨រ⟩, and comes "
    "out with the o-series [iː] instead. The [ăʔ]/[ĕəʔ] open syllable of "
    "Pali and Sanskrit loans is lexically conditioned and not modelled, so "
    "⟨កថា⟩ is [kaʔtʰaː] and comes out [kɑtʰaː]. And the a-series ⟨ូ⟩ is "
    "written [oː] here, after Huffman's monophthong table, although both "
    "shipped golds transcribe it [ou] — 471 such tokens in the wikipron "
    "gold and 183 in ipadict; [ou] is carried as a second candidate rather "
    "than promoted, because the spec follows the source and not the gold."
)
spec["sources"] = [
    {
        "id": "huffman1970",
        "author": "Huffman, Franklin E.",
        "year": 1970,
        "title": "Cambodian System of Writing and Beginning Reader",
        "publisher": "Yale University Press",
        "url": None,
        "wikipedia_url": None,
        "pages": None,
        "notes": ("The reference description of the Khmer writing system: "
                  "the consonant series, the two-reading dependent vowel "
                  "table and the final-consonant realisations. Consulted "
                  "through the IPA columns of the Wikipedia 'Khmer script' "
                  "tables, which cite Huffman for them; the book itself was "
                  "not opened, so no page locators are given."),
    },
    {
        "id": "jacob1968",
        "author": "Jacob, Judith M.",
        "year": 1968,
        "title": "Introduction to Cambodian",
        "publisher": "Oxford University Press",
        "url": None,
        "wikipedia_url": None,
        "pages": None,
        "notes": ("Cited for the length distinction between the o-series "
                  "⟨ា⟩ [iːə] and ⟨ៀ⟩ [iə], which this spec does not carry. "
                  "Reached through the Wikipedia 'Khmer script' article's "
                  "citation of it; the book itself was not opened, so no "
                  "page locators are given."),
    },
    {
        "id": "khmer_script_wiki",
        "author": "Wikipedia contributors",
        "year": 2026,
        "title": "Khmer script",
        "publisher": "Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Khmer_script",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Khmer_script",
        "pages": None,
        "notes": ("Consonant series table, dependent-vowel table with both "
                  "series readings, the diacritic inventory and the "
                  "final-consonant notes."),
    },
    {
        "id": "khmer_wiki",
        "author": "Wikipedia contributors",
        "year": 2026,
        "title": "Khmer language",
        "publisher": "Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Khmer_language",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Khmer_language",
        "pages": None,
        "notes": "Phoneme inventory, coda restrictions and stress.",
    },
]
spec["parent"] = "kha-x-proto-mon-khmer"
spec["ancestors"] = [
    {"code": "kha-x-proto-mon-khmer", "role": "parent", "weight": 0.8,
     "notes": "Khmeric branch of Austroasiatic (Mon-Khmer)."},
    {"code": "sa", "role": "adstrate", "weight": 0.14,
     "notes": "Sanskrit adstrate: the Hindu-Buddhist learned/royal register."},
    {"code": "pi", "role": "adstrate", "weight": 0.1,
     "notes": "Pali adstrate: Theravada Buddhist religious vocabulary."},
]
spec["wikipedia"] = [
    "https://en.wikipedia.org/wiki/Khmer_language",
    "https://km.wikipedia.org/wiki/%E1%9E%97%E1%9E%B6%E1%9E%9F%E1%9E%B6%E1%9E%81%E1%9F%92%E1%9E%98%E1%9F%82%E1%9E%9A",
]
spec["timespan"] = {"start_year": 611, "end_year": None}
spec["wikidata_qid"] = "Q9205"
spec["phoible_id"] = "cent1989"
spec["wals_code"] = "khm"
spec["location"] = {
    "latitude": 12.0515, "longitude": 105.015, "source": "glottolog",
    "notes": "Glottolog's representative point for Central Khmer.",
}
spec["stress"] = {
    "default_position": -1,
    "final_stress_endings": [],
    "penult_stress_endings": [],
    "marked_vowels": [],
    "stress_mark": "ˈ",
    "notes": ("Khmer word stress is predictable and falls on the final "
              "syllable of a word or compound; the minor (unstressed) "
              "presyllables that precede it are not separately modelled. "
              "Stress is not contrastive. Source: Huffman 1970."),
}

target = (pathlib.Path(__file__).resolve().parent.parent
          / "orthography2ipa" / "data" / "km.json")
target.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n")
print("graphemes:", len(graphemes), "rules:", len(rules),
      "a-series:", len(a_series), "o-series:", len(o_series))
