# -*- coding: utf-8 -*-
"""Regenerate the Burmese (``my``) grapheme table in ``data/my.json``.

The table is a cross-product — every consonant letter against the medial
signs, every rhyme against the three tones — so it is generated rather than
hand-written, and this script is where a correction goes. It edits the
graphemes, allophones, dependent_vowels, tone_inventory, notes and sources
of the existing spec in place and leaves the rest of the file alone.

Usage:
  python scripts/gen_burmese.py
"""
import collections
import json
import os
import unicodedata

SPEC_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "orthography2ipa", "data", "my.json",
)

ASAT = "်"
CREAKY = "့"   # ့
HIGH = "း"     # း
ANUS = "ံ"     # ံ

# ── base consonant letters ────────────────────────────────────────────────
BASE = {
    "က": "k", "ခ": "kʰ", "ဂ": "ɡ", "ဃ": "ɡ", "င": "ŋ",
    "စ": "s", "ဆ": "sʰ", "ဇ": "z", "ဈ": "z", "ည": "ɲ", "ဉ": "ɲ",
    "ဋ": "t", "ဌ": "tʰ", "ဍ": "d", "ဎ": "d", "ဏ": "n",
    "တ": "t", "ထ": "tʰ", "ဒ": "d", "ဓ": "d", "န": "n",
    "ပ": "p", "ဖ": "pʰ", "ဗ": "b", "ဘ": "b", "မ": "m",
    "ယ": "j", "ရ": "j", "လ": "l", "ဝ": "w", "သ": "θ",
    "ဟ": "h", "ဠ": "l", "အ": "ʔ", "ဿ": "θ",
}

# palatal medial ⟨ျ⟩/⟨ြ⟩: velars affricate, everything else keeps the glide
PALATAL = {
    "k": "tɕ", "kʰ": "tɕʰ", "ɡ": "dʑ", "ŋ": "ɲ",
    "p": "pj", "pʰ": "pʰj", "b": "bj", "m": "mj",
    "l": "lj", "h": "hj", "θ": "θj",
}
# ⟨ှ⟩ ha-hto: the sonorant it attaches to is voiceless
HA_HTO = {
    "m": "m̥", "n": "n̥", "ŋ": "ŋ̊", "ɲ": "ɲ̊", "l": "l̥",
    "j": "ʃ", "w": "ʍ", "h": "h",
}
PALATAL_HA_HTO = {"m": "m̥j", "l": "ʃ", "p": "pʰj", "b": "pʰj"}

graphemes = collections.OrderedDict()
for letter, ipa in BASE.items():
    graphemes[letter] = [ipa]
for letter, ipa in BASE.items():
    for medial in ("ျ", "ြ"):          # ျ ြ
        if ipa in PALATAL:
            graphemes[letter + medial] = [PALATAL[ipa]]
    if ipa in HA_HTO:
        graphemes[letter + "ှ"] = [HA_HTO[ipa]]
    if ipa in PALATAL_HA_HTO:
        graphemes[letter + "ျှ"] = [PALATAL_HA_HTO[ipa]]

# independent vowel letters
graphemes.update({
    "ဣ": ["ʔḭ"], "ဤ": ["ʔì"], "ဥ": ["ʔṵ"], "ဦ": ["ʔù"],
    "ဧ": ["ʔè"], "ဩ": ["ʔɔ́"], "ဪ": ["ʔɔ̀"],
})

# ── rhymes ────────────────────────────────────────────────────────────────
# Each entry: spelling(s) without tone mark -> (creaky, low, high) nucleus.
# Tone is written: unmarked = low, ⟨့⟩ = creaky, ⟨း⟩ = high, except the open
# ⟨a i u⟩ and ⟨ɛ ɔ⟩ series where the vowel-sign choice itself carries it.
TONED = [
    # (spelling, creaky, low, high) — tone from ့ / bare / း
    (["င်", "ဉ်"], "ɪ̰ɴ", "ɪ̀ɴ", "ɪ́ɴ"),                 # င် ဉ်
    (["န်", "မ်", "ဏ်", ANUS],
     "a̰ɴ", "àɴ", "áɴ"),                                                    # န် မ် ဏ် ံ
    (["ိန်", "ိမ်", "ိ" + ANUS],
     "ḛɪɴ", "èɪɴ", "éɪɴ"),                                                  # ိန် ိမ် ိံ
    (["ုန်", "ုမ်", "ု" + ANUS],
     "o̰ʊɴ", "òʊɴ", "óʊɴ"),                                                 # ုန် ုမ် ုံ
    (["ောင်", "ေါင်"], "a̰ʊɴ", "àʊɴ", "áʊɴ"),  # ောင် ေါင်
    (["ိုင်"], "a̰ɪɴ", "àɪɴ", "áɪɴ"),                   # ိုင်
    (["ွန်", "ွမ်"], "ʊ̰ɴ", "ʊ̀ɴ", "ʊ́ɴ"),    # ွန် ွမ်
    (["ွင်"], "wɪ̰ɴ", "wɪ̀ɴ", "wɪ́ɴ"),                   # ွင်
    (["ေ"], "ḛ", "è", "é"),                                            # ေ
    (["ွေ"], "wḛ", "wè", "wé"),                                   # ွေ
    (["ော်"], "ɔ̰", "ɔ̀", "ɔ̀"),                             # ော်
    (["ေါ်"], "ɔ̰", "ɔ̀", "ɔ̀"),                             # ေါ်
    (["ို", "ိုယ်", "ိုလ်"], "o̰", "ò", "ó"),  # ို ိုယ် ိုလ်
    (["ွို"], "wo̰", "wò", "wó"),                            # ွို
]


def _key(*parts):
    """Canonical spelling of a rhyme.

    The creaky mark ⟨့⟩ (U+1037, ccc 7) sorts BEFORE the asat ⟨်⟩ (U+103A,
    ccc 9), so ⟨ကန့်⟩ is spelled na + dot-below + asat. Composing the pieces
    naively gives the wrong order; NFC reorders them the way the corpus
    spells them.
    """
    return unicodedata.normalize("NFC", "".join(parts))


rhymes = collections.OrderedDict()
for spellings, creaky, low, high in TONED:
    for sp in spellings:
        rhymes[_key(sp, CREAKY)] = [creaky]
        rhymes[_key(sp)] = [low]
        rhymes[_key(sp, HIGH)] = [high]

# ⟨ည်⟩ is the one rhyme with no settled Yangon value: /ì/ ~ /è/ ~ /ɛ̀/.
rhymes[_key("ည်")] = ["ì", "è", "ɛ̀"]
rhymes[_key("ည်", CREAKY)] = ["ḭ", "ḛ"]
rhymes[_key("ည်", HIGH)] = ["í", "ɛ́", "é"]

# open rhymes whose tone is carried by the vowel-sign choice
rhymes.update({
    "ာ": ["à"], "ာ" + HIGH: ["á"], "ာ" + CREAKY: ["a̰"],
    "ါ": ["à"], "ါ" + HIGH: ["á"], "ါ" + CREAKY: ["a̰"],
    "ိ": ["ḭ"], "ီ": ["ì"], "ီ" + HIGH: ["í"],
    "ု": ["ṵ"], "ူ": ["ù"], "ူ" + HIGH: ["ú"],
    "ဲ": ["ɛ́"], "ဲ" + CREAKY: ["ɛ̰"],
    "ယ်": ["ɛ̀"],
    "ော": ["ɔ́"], "ော" + CREAKY: ["ɔ̰"],
    "ေါ": ["ɔ́"], "ေါ" + CREAKY: ["ɔ̰"],
    # ⟨ွ⟩ medial + open rhymes
    "ွ": ["wa̰"],
    "ွာ": ["wà"], "ွာ" + HIGH: ["wá"],
    "ွါ": ["wà"], "ွါ" + HIGH: ["wá"],
    "ွဲ": ["wɛ́"], "ွယ်": ["wɛ̀"],
    "ွိ": ["wḭ"], "ွီ": ["wì"],
    # ⟨လ်⟩ is not one of the eight native finals: outside ⟨ိုလ်⟩ it occurs
    # only in loan spellings, where it is read as a plain /l/.
    "လ်": ["l"],
})

# checked rhymes — a final stop is [ʔ] and the syllable has no tone contrast
CHECKED = {
    "က်": "ɛʔ",                                    # က်
    "ဂ်": "ɛʔ", "ခ်": "ɛʔ",              # ဂ် ခ်
    "စ်": "ɪʔ", "ဇ်": "ɪʔ",              # စ် ဇ်
    "ဆ်": "ɪʔ", "ဈ်": "ɪʔ",              # ဆ် ဈ်
    "တ်": "aʔ", "ပ်": "aʔ",              # တ် ပ်
    "ဋ်": "aʔ", "ဌ်": "aʔ",              # ဋ် ဌ်
    "ဍ်": "aʔ", "ဎ်": "aʔ",              # ဍ် ဎ်
    "ထ်": "aʔ", "ဒ်": "aʔ",              # ထ် ဒ်
    "ဓ်": "aʔ", "ဖ်": "aʔ",              # ဓ် ဖ်
    "ဗ်": "aʔ", "ဘ်": "aʔ",              # ဗ် ဘ်
    "သ်": "aʔ",                                    # သ်
    "ိတ်": "eɪʔ", "ိပ်": "eɪʔ",  # ိတ် ိပ်
    "ိ" + "က်": "eɪʔ",                          # ိက်
    "ုတ်": "oʊʔ", "ုပ်": "oʊʔ",  # ုတ် ုပ်
    "ွတ်": "ʊʔ", "ွပ်": "ʊʔ",    # ွတ် ွပ်
    "ွက်": "wɛʔ",                               # ွက်
    "ွစ်": "wɪʔ",                               # ွစ်
    "ောက်": "aʊʔ",                         # ောက်
    "ိုက်": "aɪʔ",                         # ိုက်
}
for sp, ipa in CHECKED.items():
    rhymes[sp] = [ipa]

rhymes = collections.OrderedDict(
    (_key(k), v) for k, v in rhymes.items()
)
graphemes.update(rhymes)

# the surface inventory (Watkins 2001), tone diacritics excluded
allophones = collections.OrderedDict()
for ipa in ["k", "kʰ", "ɡ", "ŋ", "ŋ̊", "s", "sʰ", "z", "ʃ", "tɕ", "tɕʰ", "dʑ",
            "ɲ", "ɲ̊", "t", "tʰ", "d", "n", "n̥", "p", "pʰ", "b", "m", "m̥",
            "j", "l", "l̥", "w", "ʍ", "θ", "h", "ʔ", "ɴ",
            "a", "i", "u", "e", "o", "ɛ", "ɔ", "ɪ", "ʊ", "ə"]:
    allophones[ipa] = [ipa]

spec = json.load(open(SPEC_PATH, encoding="utf-8"))
spec["graphemes"] = graphemes
spec["allophones"] = allophones
spec["inherent_vowel"] = "a̰"
spec["dependent_vowels"] = sorted(rhymes, key=len, reverse=True)
spec["tone_inventory"] = {
    "creaky": "high, slightly falling, creaky/tense phonation — written ⟨့⟩, or by the vowel sign ⟨ိ ု⟩",
    "low": "low, slightly rising, modal phonation — written by the bare rhyme, or ⟨ာ ီ ူ ေ⟩",
    "high": "high falling, breathy phonation — written ⟨း⟩, or by the vowel sign ⟨ဲ ော⟩",
    "checked": "short, closed by [ʔ]; no tone contrast — written with a final stop letter + asat ⟨်⟩",
}
spec["notes"] = (
    "Burmese in the Myanmar script, standard (Yangon) pronunciation. The "
    "spec models the syllable as ONSET + RHYME. An onset is a consonant "
    "letter, optionally with a medial sign: the palatal medial ⟨ျ⟩/⟨ြ⟩ turns "
    "the velars into palato-alveolar affricates (⟨ကျ⟩ [tɕ], ⟨ချ⟩ [tɕʰ], "
    "⟨ဂျ⟩ [dʑ]) and leaves a /j/ glide on the labials (⟨မျ⟩ [mj]), while "
    "ha-hto ⟨ှ⟩ makes the sonorant it attaches to voiceless (⟨မှ⟩ [m̥], "
    "⟨လှ⟩ [l̥], ⟨ရှ⟩ [ʃ]) (Watkins 2001; Wheatley 1990). ⟨ရ⟩ has merged with "
    "⟨ယ⟩ to /j/ in the standard language. A rhyme is written as a unit — an "
    "optional vowel sign, an optional final consonant letter carrying the "
    "asat ⟨်⟩, and an optional tone mark — and is listed here as one "
    "grapheme, because the vowel it spells is not predictable from its parts: "
    "the only codas Burmese permits are [ʔ] and nasalisation, so every final "
    "stop letter neutralises to [ʔ] and every final nasal letter to a "
    "nasalised rhyme, with the preceding vowel shifted (⟨ကန်⟩ [kàɴ] but "
    "⟨ကင်⟩ [kɪ̀ɴ], ⟨ကတ်⟩ [kaʔ] but ⟨ကက်⟩ [kɛʔ] and ⟨ကစ်⟩ [kɪʔ]). Tone is "
    "orthographic: unmarked is low, ⟨့⟩ is creaky, ⟨း⟩ is high, and in the "
    "open ⟨a i u⟩ series the choice of vowel sign carries it instead "
    "(⟨ကိ⟩ [kḭ], ⟨ကီ⟩ [kì], ⟨ကီး⟩ [kí]); checked syllables have no tone "
    "contrast. Nasalisation is written ⟨ɴ⟩ here, the notation of the Burmese "
    "descriptive tradition; ⟨ɰ̃⟩ is the same segment in other sources. "
    "⟨ည်⟩ is the one rhyme with no settled standard value and is given three "
    "candidates /ì/ ~ /è/ ~ /ɛ̀/. Two things the orthography does not "
    "determine are left unmodelled: the minor-syllable reduction that makes a "
    "bare consonant letter [Cə] instead of [Ca̰] in some polysyllables, and "
    "the word-internal voicing sandhi that voices a syllable-initial "
    "voiceless obstruent after an unchecked syllable — both are lexically "
    "conditioned and a bare consonant letter is spelled identically either "
    "way. Stress exemption: word prominence is carried by the tone system "
    "rather than a separate lexical stress accent; no stress block is "
    "declared."
)
spec["sources"] = [
    {"id": "watkins2001", "author": "Watkins, J. W.", "year": 2001,
     "title": "Burmese (Illustrations of the IPA)",
     "publisher": "Journal of the International Phonetic Association 31(2), 291-295",
     "url": "https://doi.org/10.1017/S0025100301002122",
     "pages": "291-295",
     "notes": "Standard description of the Burmese inventory, rhymes and "
              "four tones; edition not consulted for this spec."},
    {"id": "okell1969", "author": "Okell, J.", "year": 1969,
     "title": "A Reference Grammar of Colloquial Burmese",
     "publisher": "Oxford University Press", "url": None,
     "pages": None, "notes": "Edition not consulted for this spec."},
    {"id": "wheatley1990", "author": "Wheatley, J. K.", "year": 1990,
     "title": "Burmese, in B. Comrie (ed.), The World's Major Languages",
     "publisher": "Oxford University Press", "url": None,
     "pages": None, "notes": "Edition not consulted for this spec."},
    {"id": "burmese_wiki", "author": "Wikipedia contributors", "year": 2024,
     "title": "Burmese alphabet; Burmese phonology", "publisher": "Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Burmese_alphabet",
     "wikipedia_url": "https://en.wikipedia.org/wiki/Burmese_alphabet",
     "pages": None, "notes": "Rhyme-by-rhyme orthography-to-IPA tables; the source actually "
              "read when building this grapheme table."},
]
spec["quality"] = "research"

with open(SPEC_PATH, "w", encoding="utf-8") as fh:
    json.dump(spec, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print("graphemes:", len(graphemes), "dependent_vowels:", len(spec["dependent_vowels"]))
