"""English (en) — grapheme→IPA and allophone mappings.

Sources:
- Wells, J.C. (2008). *Longman Pronunciation Dictionary*, 3rd ed.
- Roach, P. (2009). *English Phonetics and Phonology*, 4th ed.
- Cruttenden, A. (2014). *Gimson's Pronunciation of English*, 8th ed.

Conventions:
- Graphemes reflect standard English orthography (General American bias
  for vowel splits; RP noted via allophones).
- Digraphs/trigraphs are those recognised in standard phonics and
  spelling pedagogy (e.g. ⟨th⟩, ⟨sh⟩, ⟨tch⟩, ⟨igh⟩).
- Allophones list positional and free variants attested in GA and/or RP.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

# ── Graphemes ──────────────────────────────────────────────────────────────
GRAPHEMES = {
    # --- Single letters ---
    "a": ["æ", "ɑː", "eɪ", "ə", "ɔː"],
    "b": ["b"],
    "c": ["k", "s"],
    "d": ["d"],
    "e": ["ɛ", "iː", "ə"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],
    "h": ["h"],
    "i": ["ɪ", "iː", "aɪ"],
    "j": ["dʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "o": ["ɒ", "oʊ", "ɔː", "ʌ", "uː"],
    "p": ["p"],
    "q": ["k"],  # always in ⟨qu⟩
    "r": ["ɹ"],
    "s": ["s", "z"],
    "t": ["t"],
    "u": ["ʌ", "juː", "uː", "ʊ"],
    "v": ["v"],
    "w": ["w"],
    "x": ["ks", "ɡz"],
    "y": ["j", "iː", "aɪ", "ɪ"],
    "z": ["z"],

    # --- Consonant digraphs ---
    "ch": ["tʃ", "k", "ʃ"],  # church / chemistry / machine
    "ck": ["k"],
    "dg": ["dʒ"],  # edge, badge
    "gh": ["ɡ", "f", ""],  # ghost / laugh / though
    "gn": ["n"],  # gnome (initial), sign
    "kn": ["n"],  # know, knee
    "ng": ["ŋ", "ŋɡ"],  # sing / finger
    "ph": ["f"],  # phone
    "qu": ["kw"],  # queen
    "sc": ["s"],  # science (before e/i)
    "sh": ["ʃ"],  # ship
    "ss": ["s"],  # miss
    "th": ["θ", "ð"],  # thin / this
    "wh": ["w", "ʍ"],  # which, what
    "wr": ["ɹ"],  # write (⟨w⟩ silent)

    # --- Consonant trigraphs ---
    "tch": ["tʃ"],  # watch, match
    "dge": ["dʒ"],  # bridge, edge

    # --- Vowel digraphs ---
    "ai": ["eɪ"],  # rain, wait
    "ay": ["eɪ"],  # day, play
    "ea": ["iː", "ɛ"],  # beat / bread
    "ee": ["iː"],  # see, tree
    "ei": ["iː", "eɪ"],  # receive / vein
    "ey": ["iː", "eɪ"],  # key / they
    "ie": ["aɪ", "iː"],  # pie / field
    "oa": ["oʊ"],  # boat, goat
    "oe": ["oʊ", "uː"],  # toe / shoe
    "oo": ["uː", "ʊ"],  # food / book
    "ou": ["aʊ", "ʌ", "uː"],  # house / touch / soup
    "ow": ["aʊ", "oʊ"],  # cow / snow
    "ue": ["juː", "uː"],  # cue / blue
    "ui": ["uː", "ɪ"],  # fruit / build

    # --- Vowel trigraphs ---
    "eau": ["juː", "oʊ"],  # beauty / bureau
    "igh": ["aɪ"],  # high, night
    "ough": ["ɔː", "oʊ", "ʌf", "ɒf", "aʊ", "uː"],  # thought/though/tough/cough/plough/through

    # --- R-coloured vowel digraphs ---
    "ar": ["ɑːɹ"],  # car, star
    "er": ["ɜːɹ", "əɹ"],  # her, water
    "ir": ["ɜːɹ"],  # bird, stir
    "or": ["ɔːɹ"],  # for, born
    "ur": ["ɜːɹ"],  # burn, turn

    # --- R-coloured trigraphs ---
    "air": ["ɛəɹ"],  # fair, hair
    "are": ["ɛəɹ"],  # care, share
    "ear": ["ɪəɹ", "ɛəɹ"],  # near / bear
    "eer": ["ɪəɹ"],  # deer, beer
    "ire": ["aɪəɹ"],  # fire, hire
    "oar": ["ɔːɹ"],  # board, soar
    "ore": ["ɔːɹ"],  # more, store
    "our": ["aʊəɹ", "ɔːɹ"],  # hour / four
    "ure": ["jʊəɹ", "ʊəɹ"],  # cure, sure
}

# ── Allophones ─────────────────────────────────────────────────────────────
ALLOPHONES = {
    # Plosives
    "p": ["p", "pʰ", "p̚"],  # aspirated word-initially; unreleased in coda
    "b": ["b", "b̥"],  # partially devoiced utterance-finally
    "t": ["t", "tʰ", "ɾ", "ʔ", "t̚"],  # aspirated; GA flap; glottal stop; unreleased
    "d": ["d", "d̥", "ɾ"],  # devoiced finally; GA flap
    "k": ["k", "kʰ", "k̚"],  # aspirated; unreleased
    "ɡ": ["ɡ", "ɡ̊"],  # partially devoiced finally

    # Fricatives
    "f": ["f"],
    "v": ["v", "v̥"],
    "θ": ["θ"],
    "ð": ["ð", "d̪"],  # dental stop in casual speech
    "s": ["s"],
    "z": ["z", "z̥"],
    "ʃ": ["ʃ"],
    "ʒ": ["ʒ", "ʒ̊"],
    "h": ["h", "ɦ"],  # voiced between vowels

    # Affricates
    "tʃ": ["tʃ"],
    "dʒ": ["dʒ", "dʒ̊"],

    # Nasals
    "m": ["m", "ɱ"],  # labiodental before /f, v/
    "n": ["n", "n̪", "ɱ", "ŋ"],  # dental before /θ, ð/; velar before /k, ɡ/
    "ŋ": ["ŋ"],

    # Approximants
    "ɹ": ["ɹ", "ɻ", "ɹ̥"],  # retroflex variant; devoiced after voiceless stop
    "l": ["l", "ɫ"],  # clear onset; dark coda (GA)
    "w": ["w", "ʍ", "w̥"],  # voiceless in ⟨wh⟩ (some dialects)
    "j": ["j"],

    # Monophthongs
    "iː": ["iː"],
    "ɪ": ["ɪ"],
    "ɛ": ["ɛ"],
    "æ": ["æ", "eə"],  # raised in some GA dialects
    "ɑː": ["ɑː", "ɒ"],  # RP uses [ɒ] for LOT
    "ɒ": ["ɒ", "ɑ"],  # GA merges with [ɑ]
    "ɔː": ["ɔː"],
    "ʊ": ["ʊ"],
    "uː": ["uː", "ʉː"],  # fronted in many GA speakers
    "ʌ": ["ʌ", "ɐ"],
    "ɜːɹ": ["ɜːɹ", "ɝː"],  # r-coloured
    "ə": ["ə", "ɚ"],  # r-coloured schwa

    # Diphthongs
    "eɪ": ["eɪ"],
    "aɪ": ["aɪ", "ɑɪ"],
    "ɔɪ": ["ɔɪ"],
    "oʊ": ["oʊ", "əʊ"],  # GA / RP
    "aʊ": ["aʊ", "æʊ"],
}

# ── Spec ───────────────────────────────────────────────────────────────────
SPECS = {
    "en-GB": LanguageSpec(
        code="en-GB",
        name="English",
        family="Germanic",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="gem",
        ancestors=(
            Ancestor("enm", P, 0.85,
                     "Descent from Middle English (Chaucerian stage)"),
            Ancestor("xbr", SUB, 0.03,
                     "Brythonic Celtic substrate: place names (London, Thames, "
                     "Kent, Dover, Avon); cf. Jackson (1953)"),
            Ancestor("non", SUP, 0.05,
                     "Old Norse Danelaw superstrate (8th-11th c.): they/their/them, "
                     "sky, take, give, window, egg; cf. Townend (2002)"),
            Ancestor("fr-FR", SUP, 0.07,
                     "Norman French superstrate (post-1066): ~10,000 words; "
                     "/v/ phonemicised, /ʒ/ introduced; cf. Pope (1934)"),
        ),
        notes=(
            "Vowel inventory biased toward General American (GA). "
            "RP / Southern British variants noted in allophone map. "
            "Grapheme set covers standard English phonics; highly "
            "irregular orthography means many words require lexicon lookup."
        ),
    ),
}
