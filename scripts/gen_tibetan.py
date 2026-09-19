# -*- coding: utf-8 -*-
"""Regenerate the Tibetan (``bo``) syllable model in ``data/bo.json``.

Tibetan spelling is historical: a syllable is written prefix + superscript +
ROOT + subscript + vowel + suffix + post-suffix, and the whole written onset
collapses to ONE modern onset plus a tone register. The onset table and the
rhyme table are therefore closed inventories transcribed from published
sources rather than hand-typed, and this script is where a correction goes.
It rewrites graphemes, positional_graphemes, allophone_rules, allophones,
vowel_graphemes and phonemes in place and leaves the rest of the file alone.

Usage:
  python scripts/gen_tibetan.py
"""
import collections
import json
import os

SPEC_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "orthography2ipa", "data", "bo.json",
)

# ── Wylie → Tibetan Unicode ───────────────────────────────────────────────
LETTERS = {
    "k": "ཀ", "kh": "ཁ", "g": "ག", "ng": "ང",
    "c": "ཅ", "ch": "ཆ", "j": "ཇ", "ny": "ཉ",
    "t": "ཏ", "th": "ཐ", "d": "ད", "n": "ན",
    "p": "པ", "ph": "ཕ", "b": "བ", "m": "མ",
    "ts": "ཙ", "tsh": "ཚ", "dz": "ཛ", "w": "ཝ",
    "zh": "ཞ", "z": "ཟ", "'": "འ", "y": "ཡ",
    "r": "ར", "l": "ལ", "sh": "ཤ", "s": "ས",
    "h": "ཧ", "a": "ཨ",
}
#: Subjoined (U+0F90..) forms of the letters that occur under a root.
SUBJOINED = {"y": "ྱ", "r": "ྲ", "l": "ླ", "w": "ྭ", "h": "ྷ"}
#: Superscribed letters are written as the plain letter with the ROOT
#: subjoined under them, so the stack is spelled super + subjoined(root).
SUB_OF = {
    "k": "ྐ", "kh": "ྑ", "g": "ྒ", "ng": "ྔ", "c": "ྕ", "ch": "ྖ",
    "j": "ྗ", "ny": "ྙ", "t": "ྟ", "th": "ྠ", "d": "ྡ", "n": "ྣ",
    "p": "ྤ", "ph": "ྥ", "b": "ྦ", "m": "ྨ", "ts": "ྩ", "tsh": "ྪ",
    "dz": "ྫ", "zh": "ྮ", "z": "ྯ", "y": "ྱ", "r": "ྲ", "l": "ླ",
    "sh": "ྴ", "s": "ྶ", "h": "ྷ", "w": "ྭ",
}
PREFIXES = set("gdbm") | {"'"}
SUPERSCRIPTS = {"r", "l", "s"}
SUBSCRIPTS = {"y", "r", "l", "w", "h"}
#: Multi-letter Wylie graphs, longest first, so ``tsh`` is one letter.
_GRAPHS = sorted(LETTERS, key=len, reverse=True)

#: Wylie spellings the letter parser cannot reach, because they are fixed
#: digraphs written with two FULL letters rather than a stack.
IRREGULAR = {"db": "དབ", "dby": "དབྱ", "g.y": "གཡ"}


def wylie_letters(w):
    """Split a Wylie onset into its letters."""
    out, i = [], 0
    while i < len(w):
        for g in _GRAPHS:
            if w.startswith(g, i):
                out.append(g)
                i += len(g)
                break
        else:
            raise ValueError(w)
    return out


def wylie_stack(w):
    """Tibetan spelling of Wylie onset *w*, with any PREFIX letter dropped.

    The prefix is not part of the stack — it is a separate written letter
    that this spec silences positionally and whose only surviving effect is
    handled in the rule layer — so ``bsgr`` and ``sgr`` give the same stack.
    Returns ``None`` for spellings the caller handles itself.
    """
    if w in IRREGULAR:
        return IRREGULAR[w]
    ls = wylie_letters(w)
    # At most two subscripts stack under a root, and the wa-zur is always
    # the lower of the two: ⟨གྲྭ⟩ grw, ⟨རྩྭ⟩ rtsw.
    subs = []
    if len(ls) > 1 and ls[-1] == "w":
        subs.insert(0, ls.pop())
    if len(ls) > 1 and ls[-1] in SUBSCRIPTS:
        subs.insert(0, ls.pop())
    root = ls.pop()
    if ls and ls[-1] in SUPERSCRIPTS:
        super_ = ls.pop()
        stack = LETTERS[super_] + SUB_OF[root]
    else:
        stack = LETTERS[root]
    if ls and ls[-1] not in PREFIXES:
        raise ValueError("unparsed " + w)
    return stack + "".join(SUBJOINED[s] for s in subs)


# ── onsets ────────────────────────────────────────────────────────────────
#: The onset inventory of Standard Tibetan: every written onset spelling
#: against the onset it opens and the tone register it assigns. Transcribed
#: from the THL Simplified Phonetic Transcription table (Germano &
#: Tournadre 2003), which lists the Tournadre phonetic value of each Wylie
#: onset with its register (´ = high, ` = low).
#:
#: Prenasalisation is NOT carried over. The source writes ⟨འག⟩ ŋkà, ⟨མཇ⟩
#: ɲtɕà and their kin with a homorganic nasal, but the Lhasa consonant
#: inventory has no prenasalised series (Zhang 2024); what the spelling
#: predicts and this spec keeps is the DE-ASPIRATION those prefixes cause,
#: expressed once in the rule layer instead of per stack.
ONSETS = [
    ("p", "high", ["p", "sp", "dp", "lp"]),
    ("p", "low", ["rb", "sb", "lb", "'b"]),
    ("pʰ", "high", ["ph", "'ph"]),
    ("pʰ", "low", ["b"]),
    ("b", "low", ["bh"]),
    ("m", "high", ["rm", "sm", "dm", "smr"]),
    ("m", "low", ["m", "mr"]),
    ("w", "low", ["db", "w"]),
    ("t", "high", ["t", "rt", "lt", "st", "tw", "gt", "bt", "brt", "blt",
                   "bst", "lth"]),
    ("t", "low", ["rd", "sd", "gd", "bd", "brd", "bsd", "zl", "bzl", "ld",
                  "md", "'d", "bld"]),
    ("tʰ", "high", ["th", "mth", "'th"]),
    ("tʰ", "low", ["d", "dw"]),
    ("n", "high", ["rn", "sn", "gn", "brn", "bsn", "mn"]),
    ("n", "low", ["n"]),
    ("l", "high", ["kl", "gl", "bl", "rl", "sl", "brl", "bsl"]),
    ("l", "low", ["l", "lw"]),
    ("l̥", "high", ["lh"]),
    ("ts", "high", ["ts", "rts", "sts", "rtsw", "stsw", "gts", "bts",
                    "brts", "bsts"]),
    ("ts", "low", ["rdz", "gdz", "brdz", "mdz", "'dz"]),
    ("tsʰ", "high", ["tsh", "tshw", "mtsh", "'tsh"]),
    ("tsʰ", "low", ["dz"]),
    ("s", "high", ["s", "sr", "sw", "gs", "bs", "bsr"]),
    ("s", "low", ["z", "zw", "gz", "bz"]),
    ("ʈʂ", "high", ["kr", "rkr", "lkr", "skr", "tr", "pr", "lpr", "spr",
                    "dkr", "dpr", "bkr", "bskr"]),
    ("ʈʂ", "low", ["rgr", "lgr", "sgr", "dgr", "dbr", "bsgr", "rbr", "lbr",
                   "sbr", "mgr", "'gr", "'dr", "'br"]),
    ("ʈʂʰ", "high", ["khr", "thr", "phr", "mkhr", "'khr", "'phr"]),
    ("ʈʂʰ", "low", ["gr", "dr", "br", "grw"]),
    ("ʂ", "high", ["hr"]),
    ("ʐ", "low", ["r", "rw"]),
    ("r̥", "high", ["rh"]),
    ("c", "high", ["ky", "rky", "lky", "sky", "dky", "bky", "brky", "bsky"]),
    ("c", "low", ["rgy", "lgy", "sgy", "dgy", "bgy", "brgy", "bsgy", "mgy",
                  "'gy"]),
    ("cʰ", "high", ["khy", "mkhy", "'khy"]),
    ("cʰ", "low", ["gy"]),
    ("ç", "high", ["hy"]),
    ("tɕ", "high", ["c", "cw", "gc", "bc", "lc", "py", "lpy", "spy", "dpy"]),
    ("tɕ", "low", ["rby", "lby", "sby", "rj", "gj", "brj", "lj", "mj", "'j",
                   "'by"]),
    ("tɕʰ", "high", ["ch", "mch", "'ch", "phy", "'phy"]),
    ("tɕʰ", "low", ["j", "by"]),
    ("ɕ", "high", ["sh", "shw", "gsh", "bsh"]),
    ("ɕ", "low", ["zh", "zhw", "gzh", "bzh"]),
    ("ɲ", "high", ["rny", "sny", "gny", "brny", "bsny", "mny", "nyw", "rmy",
                   "smy"]),
    ("ɲ", "low", ["ny", "my"]),
    ("j", "high", ["g.y"]),
    ("j", "low", ["y", "dby"]),
    ("k", "high", ["k", "rk", "lk", "sk", "kw", "dk", "bk", "brk", "bsk"]),
    ("k", "low", ["rg", "lg", "sg", "dg", "bg", "brg", "bsg", "mg", "'g"]),
    ("kʰ", "high", ["kh", "khw", "mkh", "'kh"]),
    ("kʰ", "low", ["g", "gw"]),
    ("ŋ", "high", ["rng", "lng", "sng", "dng", "brng", "bsng", "mng"]),
    ("ŋ", "low", ["ng"]),
    ("ʔ", "high", ["a"]),
    ("h", "high", ["h", "hw"]),
]

def _has_prefix(w):
    if w in IRREGULAR:
        return False
    ls = wylie_letters(w)
    if len(ls) > 1 and ls[-1] == "w":
        ls.pop()
    if len(ls) > 1 and ls[-1] in SUBSCRIPTS:
        ls.pop()
    ls.pop()
    if ls and ls[-1] in SUPERSCRIPTS:
        ls.pop()
    return bool(ls)


onset_ipa = collections.OrderedDict()
register = {}
#: A prefixed spelling reduces to the same stack as its prefix-less twin —
#: ``mng`` to ⟨ང⟩, ``bsgr`` to ⟨སྒྲ⟩ — but only the prefix-less spelling
#: states that stack's OWN register, so every prefix-less spelling is read
#: first and a prefixed one only fills a stack no other spelling reached.
for prefixed in (False, True):
    for ipa, reg, spellings in ONSETS:
        for w in spellings:
            if _has_prefix(w) != prefixed:
                continue
            stack = wylie_stack(w)
            if stack in onset_ipa:
                continue
            onset_ipa[stack] = ipa
            register[stack] = reg

#: ⟨འ⟩ a-chung opens a syllable with no consonant and is the low-register
#: counterpart of ⟨ཨ⟩; it is also a prefix and a suffix, both silent, so it
#: is resolved positionally rather than here.
ACHUNG = "འ"
register[ACHUNG] = "low"

HIGH_ONSETS = [g for g in onset_ipa if register[g] == "high"]
LOW_ONSETS = [g for g in onset_ipa if register[g] == "low"] + [ACHUNG]

#: Onsets that a written prefix de-aspirates. A prefixed voiced letter is
#: the unaspirated member of its low-register pair — ⟨ག⟩ kʰà against ⟨དག⟩
#: kà, ⟨ད⟩ tʰà against ⟨བད⟩ tà (Germano & Tournadre 2003).
DEASPIRATE = {"kʰ": "k", "tʰ": "t", "pʰ": "p", "tsʰ": "ts", "tɕʰ": "tɕ",
              "cʰ": "c", "ʈʂʰ": "ʈʂ"}
PREFIX_LETTERS = ["ག", "ད", "བ", "མ", "འ"]

# ── rhymes ────────────────────────────────────────────────────────────────
VOWEL_SIGNS = {"a": "", "i": "ི", "u": "ུ", "e": "ེ", "o": "ོ"}

#: Written suffix → (coda consonant, per-vowel nucleus, tone contour class).
#: Transcribed from the rhyme table of the SASM/GNC transcription of
#: Standard Tibetan, whose Lhasa IPA column follows Brush (1997).
#:
#: The contour class is the syllable's own: Lhasa has two registers, each
#: realised flat in an open or sonorant-closed syllable and falling in a
#: syllable closed by a historical stop or by ⟨ས⟩ — which is why ⟨ཁམ⟩
#: kham [kʰám] and ⟨ཁམས⟩ khams [kʰâm] differ only in contour, and why the
#: falling contour and a final [k]/[ʔ] never contrast (DeLancey 2003).
#: A post-suffix ⟨ས⟩ is never itself pronounced; it survives only as the
#: falling contour it forces on the rhyme in front of it, which is why the
#: sonorant-closed rhymes appear twice — once bare, once with the ⟨ས⟩ two
#: graphemes ahead.
RHYMES = [
    # suffixes,   coda, {vowel: nucleus},                   contour, post-s
    (["ག"], "ʔ", {"a": "a", "i": "i", "u": "u", "e": "e", "o": "o"},
     "fall", None),
    (["བ"], "p", {"a": "a", "i": "i", "u": "u", "e": "e", "o": "o"},
     "fall", None),
    (["ད", "ས"], "", {"a": "ɛː", "i": "iː", "u": "yː", "e": "eː", "o": "øː"},
     "fall", None),
    (["ང"], "ŋ", {"a": "a", "i": "i", "u": "u", "e": "e", "o": "o"},
     "fall", True),
    (["མ"], "m", {"a": "a", "i": "i", "u": "u", "e": "e", "o": "o"},
     "fall", True),
    (["ང"], "ŋ", {"a": "a", "i": "i", "u": "u", "e": "e", "o": "o"},
     "level", None),
    (["མ"], "m", {"a": "a", "i": "i", "u": "u", "e": "e", "o": "o"},
     "level", None),
    (["ན"], "", {"a": "ɛ̃", "i": "ĩ", "u": "ỹ", "e": "ẽ", "o": "ø̃"},
     "level", None),
    (["ལ", "འི"], "", {"a": "ɛː", "i": "iː", "u": "yː", "e": "eː",
                       "o": "øː"}, "level", None),
    (["ར", "འ"], "", {"a": "aː", "i": "iː", "u": "uː", "e": "eː",
                      "o": "oː"}, "level", None),
]

#: The four surface contours: register × syllable type.
CONTOUR = {("high", "level"): "˥˥", ("high", "fall"): "˥˨",
           ("low", "level"): "˩˨", ("low", "fall"): "˩˧˨"}

graphemes = collections.OrderedDict()
for stack, ipa in onset_ipa.items():
    graphemes[stack] = [ipa]
for v, sign in VOWEL_SIGNS.items():
    if sign:
        graphemes[sign] = [v]
#: ⟨ཱ⟩ the Sanskrit length mark, and the two Sanskrit diphthong signs.
graphemes["ཱ"] = ["ː"]
graphemes["ཻ"] = ["e"]
graphemes["ཽ"] = ["o"]
#: The tsheg delimits the syllable. Mapping it keeps every positional and
#: allophonic context syllable-local instead of letting a suffix rule reach
#: across a syllable boundary.
graphemes["་"] = [""]
graphemes["༌"] = [""]

# ── positional: prefixes are silent, suffixes are codas ───────────────────
positional = collections.OrderedDict()
for letter in PREFIX_LETTERS:
    positional.setdefault(letter, {})["before_consonant"] = [""]
for suffixes, coda, _nuclei, _contour, _post in RHYMES:
    for suf in suffixes:
        positional.setdefault(suf, {})["after_vowel"] = [""]
#: ⟨འི⟩ and ⟨འུ⟩ are the genitive and the diphthong written with a-chung.
#: Word-initially the same two characters open a syllable with no onset,
#: which is the reading the default position keeps.
#: Syllable-initially ⟨འ⟩ a-chung is the onset itself — a glottal stop in
#: the low register (Germano & Tournadre 2003) — where the prefix and the
#: suffix readings above leave it silent.
positional[ACHUNG]["default"] = ["ʔ"]
positional["འི"] = {"after_vowel": [""], "default": ["i"]}
positional["འུ"] = {"after_vowel": [""], "default": ["u"]}

# ── rules: the nucleus carries the suffix's umlaut and the syllable tone ──
CITE = ("Germano & Tournadre 2003 for the register of each written onset; "
        "the SASM/GNC rhyme table (Lhasa column after Brush 1997) for the "
        "nucleus; DeLancey 2003 for the complementary distribution of the "
        "falling contour and a final stop.")

rules = []


def _rule(rid, phoneme, surface, reg, **kw):
    r = {"id": rid, "phonemes": [phoneme], "surface": surface,
         "notes": CITE}
    r.update(kw)
    rules.append(r)


HIGH_IPA = sorted({onset_ipa[g] for g in HIGH_ONSETS})
LOW_IPA = sorted({onset_ipa[g] for g in LOW_ONSETS if g in onset_ipa})

for suffixes, coda, nuclei, contour, post_s in RHYMES:
    tag = "_".join(str(ord(s[0])) for s in suffixes) + ("_S" if post_s else "")
    extra = {"followed_by_phoneme_2": ["s"]} if post_s else {}
    for reg in ("high", "low"):
        onsets = HIGH_ONSETS if reg == "high" else LOW_ONSETS
        ipas = HIGH_IPA if reg == "high" else LOW_IPA
        tone = CONTOUR[(reg, contour)]
        for v, nucleus in nuclei.items():
            surface = nucleus + coda + tone
            _rule(f"BO_RHYME_{tag}_{v}_{reg.upper()}", v, surface, reg,
                  preceded_by_grapheme=onsets, followed_by_grapheme=suffixes,
                  **extra)
            if v == "a":
                # The inherent vowel is a segment INSIDE the onset
                # grapheme's own slot, so the rule must match that grapheme
                # and name the onset phoneme it follows — a slot-internal
                # segment is only reachable to a rule that states its
                # phoneme neighbourhood.
                _rule(f"BO_RHYME_{tag}_INH_{reg.upper()}", v, surface, reg,
                      grapheme=onsets, preceded_by_phoneme=ipas,
                      followed_by_grapheme=suffixes, **extra)

# open syllables: register only, flat contour
for reg in ("high", "low"):
    onsets = HIGH_ONSETS if reg == "high" else LOW_ONSETS
    ipas = HIGH_IPA if reg == "high" else LOW_IPA
    tone = CONTOUR[(reg, "level")]
    for v in ("a", "i", "u", "e", "o"):
        _rule(f"BO_TONE_{v}_{reg.upper()}", v, v + tone, reg,
              preceded_by_grapheme=onsets)
        if v == "a":
            _rule(f"BO_TONE_INH_{reg.upper()}", v, v + tone, reg,
                  grapheme=onsets, preceded_by_phoneme=ipas)

#: The post-suffix ⟨ས⟩ stands after a suffix ⟨ག ང བ མ⟩ and is not
#: pronounced; the falling contour it forces on the rhyme in front of it is
#: all that survives of it.
for cls in ("vowel", "consonant"):
    rules.append({
        "id": "BO_POST_SUFFIX_S_" + cls.upper(),
        "phonemes": ["s"], "surface": "",
        "grapheme": ["ས"], "preceded_by_grapheme": ["ག", "ང", "བ", "མ"],
        "preceded_by_2": cls,
        "notes": ("The post-suffix ⟨ས⟩ follows a suffix ⟨ག ང བ མ⟩ and is "
                  "not pronounced; the falling contour it forces on the "
                  "rhyme is all that survives of it (DeLancey 2003). The "
                  "letter two back tells a post-suffix from a ROOT ⟨ས⟩ "
                  "standing after its own prefix, where the syllable has "
                  "not started yet and there is no such letter."),
    })

#: ⟨བ⟩ opening a syllable that is not the word's first is a semivowel:
#: ⟨་བ⟩ is wa and ⟨་བོ⟩ is wo (SASM/GNC transcription, onset variation).
rules.append({
    "id": "BO_MEDIAL_BA_LENITION",
    "phonemes": ["pʰ"], "surface": "w",
    "grapheme": ["བ"], "preceded_by_grapheme": ["་"],
    "followed_by_phoneme": ["a", "i", "u", "e", "o"],
    "notes": ("⟨བ⟩ opening a non-initial syllable is [w]: ⟨་བ⟩ wa, ⟨་བོ⟩ "
              "wo (SASM/GNC transcription of Standard Tibetan)."),
})

# a written prefix de-aspirates the low-register onset it stands before
for aspirated, plain in DEASPIRATE.items():
    targets = [g for g in onset_ipa
               if onset_ipa[g] == aspirated and register[g] == "low"]
    if not targets:
        continue
    rules.append({
        "id": f"BO_PREFIX_DEASPIRATION_{aspirated}",
        "phonemes": [aspirated], "surface": plain,
        "followed_by_phoneme": ["a", "i", "u", "e", "o"],
        "grapheme": targets,
        "preceded_by_grapheme": PREFIX_LETTERS,
        "notes": ("A written prefix leaves the low-register onset "
                  "unaspirated: ⟨ག⟩ kʰà against ⟨དག⟩ kà. The high-register "
                  "aspirates keep their aspiration under the same prefixes "
                  "— ⟨འཁ⟩ is kʰá — so only the voiced-letter series is "
                  "targeted (Germano & Tournadre 2003)."),
    })

SOURCES = [
    {
        "id": "thl_phonetics",
        "author": "Germano, David & Tournadre, Nicolas",
        "year": 2003,
        "title": "THL Simplified Phonetic Transcription of Standard Tibetan",
        "publisher": "Tibetan and Himalayan Library, University of Virginia",
        "url": "http://www.thlib.org/reference/transliteration/",
        "pages": None,
        "notes": ("The onset table this spec transcribes: every written "
                  "onset spelling against its Lhasa onset and tone "
                  "register. Consulted as reproduced in the Wikipedia "
                  "articles 'THL Simplified Phonetic Transcription' and "
                  "'Tibetan pinyin'."),
    },
    {
        "id": "tournadre_dorje2003",
        "author": "Tournadre, Nicolas & Sangda Dorje",
        "year": 2003,
        "title": "Manual of Standard Tibetan: Language and Civilization",
        "publisher": "Snow Lion",
        "url": None,
        "pages": None,
        "notes": ("The standard reference grammar of Standard Tibetan and "
                  "the source of the eight-vowel analysis and the "
                  "nasalised series; edition not consulted directly."),
    },
    {
        "id": "delancey2003",
        "author": "DeLancey, Scott",
        "year": 2003,
        "title": "Lhasa Tibetan",
        "publisher": ("In: Thurgood, G. & LaPolla, R. (eds.), "
                      "The Sino-Tibetan Languages, Routledge"),
        "url": None,
        "pages": None,
        "notes": ("The two-tone analysis, and the complementary "
                  "distribution of the falling contour with a final stop "
                  "that this spec's contour rule states."),
    },
    {
        "id": "sasm_gnc",
        "author": "SASM/GNC/SRC",
        "year": 1976,
        "title": "Transcription of Tibetan (Tibetan pinyin)",
        "publisher": "State Administration of Surveying and Mapping, China",
        "url": "https://www.eki.ee/wgrs/rom1_bo.pdf",
        "pages": None,
        "notes": ("Official transcription of Standard Tibetan; its rhyme "
                  "table, whose Lhasa IPA column follows Brush (1997), is "
                  "the source of the suffix-conditioned nuclei, and its "
                  "onset-variation section of the medial ⟨བ⟩ lenition."),
    },
    {
        "id": "brush1997",
        "author": "Brush, Beaumont",
        "year": 1997,
        "title": ("The Status of Coronal in the Historical Development of "
                  "Lhasa Tibetan Rhymes"),
        "publisher": "SIL Electronic Working Papers",
        "url": "https://www.sil.org/silewp/1997/001/silewp1997-001.pdf",
        "pages": None,
        "notes": "The Lhasa rhyme inventory behind the rhyme table.",
    },
    {
        "id": "zhang2024",
        "author": "Zhang, Yubin",
        "year": 2024,
        "title": "Central Tibetan (Lhasa)",
        "publisher": ("Journal of the International Phonetic Association "
                      "54(2)"),
        "url": "https://doi.org/10.1017/S0025100324000033",
        "pages": "788-810",
        "notes": ("Illustration of the IPA for Lhasa Tibetan: the "
                  "consonant inventory, which carries no prenasalised "
                  "series, and the four realisations of /ɹ/."),
    },
    {
        "id": "tibetan_wiki",
        "author": "Wikipedia contributors",
        "year": 2024,
        "title": "Lhasa Tibetan",
        "publisher": "Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Lhasa_Tibetan",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Lhasa_Tibetan",
        "pages": None,
        "notes": None,
    },
    {
        "id": "wikipron",
        "author": "Lee, Jackson L. et al.",
        "year": 2020,
        "title": ("WikiPron: A Tool for Extracting Pronunciation Data from "
                  "Wiktionary"),
        "publisher": "LREC",
        "url": "https://github.com/CUNY-CL/wikipron",
        "pages": None,
        "notes": ("Source of the bod_tibt_broad.tsv gold registered in "
                  "scripts/benchmark.py. Three quarters of its words carry "
                  "both a Lhasa reading and a Classical one; this spec "
                  "describes the Lhasa language."),
    },
]

NOTES = """Standard (Lhasa) Tibetan. The spec resolves the Tibetan SYLLABLE, not the letter: spelling is historical, and a syllable is prefix + superscript + ROOT + subscript + vowel + suffix + post-suffix, of which only the root, the vowel and the register survive intact in the modern language.

How each part is expressed:
* The written ONSET is one grapheme key. A superscribed or subjoined letter is a combining mark, so ⟨སྤྲ⟩, ⟨ཁྱ⟩, ⟨ཀྲ⟩ and ⟨ལྷ⟩ are single orthographic stacks that open a single consonant — ⟨ཁྱ⟩ is /cʰ/, ⟨ཁྲ⟩ is /ʈʂʰ/. ⟨གཡ⟩ and ⟨དབ⟩ are the two fixed digraphs of the same kind written with full letters. The inventory is closed and is the onset table of the language, not a product of its parts.
* PREFIXED letters ⟨ག ད བ མ འ⟩ are silent, and being silent carry no inherent vowel either. What they leave behind is aspiration: a prefixed low-register root is the unaspirated member of its pair, so ⟨ག⟩ is kʰà but ⟨དག⟩ is kà. The high-register aspirates keep their aspiration under the same prefixes.
* The TSHEG ⟨་⟩ delimits the syllable. Mapping it keeps every positional and allophonic context syllable-local instead of letting a suffix rule reach across a syllable boundary.
* The RHYME is one unit. A written suffix is not pronounced as itself: it fixes the nucleus, the coda and the tone contour together, so ⟨ད⟩ and ⟨ས⟩ umlaut and lengthen the vowel and leave no consonant (⟨ཁྱོད⟩ [cʰøː]), ⟨ན⟩ nasalises it, ⟨ར⟩ and ⟨ལ⟩ lengthen it, and only ⟨ག ང བ མ⟩ leave a coda. The post-suffix ⟨ས⟩ is never pronounced.
* TONE is a two-way register contrast and it is derivable from the spelling: the written onset decides it. Each register has two contours, flat in an open or sonorant-closed syllable and falling in a syllable closed by a historical stop or by ⟨ས⟩ — which is why ⟨ཁམ⟩ kham and ⟨ཁམས⟩ khams differ only in contour. The contour is written at the end of the rhyme, where the WikiPron gold marks it.

Segments are phonemic, not narrow: the backed and laxed vowels of a closed syllable ([ʌ] for /a/, [ɔ] for /o/) are allophones and are not written, and the prenasalised onsets of the Tournadre transcription are not in the Lhasa phoneme inventory and are not emitted.

KNOWN CEILING. A Tibetan syllable whose first letter is one of the five prefixes is structurally ambiguous: ⟨གང⟩ gang is root + suffix while ⟨དགོན⟩ dgon is prefix + root. Telling them apart needs a syllable parser that reads the whole syllable before choosing, which a left-to-right positional resolution cannot do, so the prefix reading is taken uniformly and the root + suffix spellings are read wrong. The residual error is that, gold rows transcribed narrowly, and — in the WikiPron gold specifically — the rows that give a Classical rather than a Lhasa reading."""

# ── write the spec ────────────────────────────────────────────────────────
spec = json.load(open(SPEC_PATH, encoding="utf-8"))
spec["graphemes"] = graphemes
spec["positional_graphemes"] = positional
spec["allophone_rules"] = rules
spec["vowel_graphemes"] = [s for s in VOWEL_SIGNS.values() if s] + \
    ["ཱ", "ཻ", "ཽ"]
spec["coda_no_inherent_vowel"] = True
spec["quality"] = "research"
spec["notes"] = NOTES
spec["sources"] = SOURCES

inventory = sorted({ipa for ipa in onset_ipa.values() if ipa} |
                   {"ʔ", "p", "m", "ŋ"})
vowels = sorted({n for _s, _c, nuc, _t, _p in RHYMES for n in nuc.values()} |
                set("aiueo"))
spec["phonemes"] = inventory + vowels
spec["allophones"] = {
    **{p: [p] for p in inventory + vowels},
    # In the low register the unaspirated stops and affricates are voiced
    # and the aspirates lose much of their aspiration (Zhang 2024).
    "ʐ": ["ʐ", "ɹ", "r"],
}

with open(SPEC_PATH, "w", encoding="utf-8") as fh:
    json.dump(spec, fh, ensure_ascii=False, indent=2)
    fh.write("\n")

print(f"onsets={len(onset_ipa)} graphemes={len(graphemes)} "
      f"positional={len(positional)} rules={len(rules)}")
