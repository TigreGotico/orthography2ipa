"""Pashto (ps) — grapheme→IPA and allophone mappings.

Pashto is an Eastern Iranian language spoken primarily in Afghanistan
and Pakistan. It is referenced as an adstrate of Dari (Afghan Persian,
fa-AF).

Pashto is one of Afghanistan's two official languages alongside Dari.
It belongs to the Eastern Iranian branch, unlike Persian (Western Iranian).

This spec represents Standard Afghan Pashto (Kandahari base, the
prestige/literary variety).

Sources:
- Penzl, H. (1955). *A Grammar of Pashto*. ACLS.
- David, A.B. (2014). *Descriptive Grammar of Pashto*. Mouton.
- Tegey, H. & Robson, B. (1996). *A Reference Grammar of Pashto*.
  Center for Applied Linguistics.
- Morgenstierne, G. (1927). "An Etymological Vocabulary of Pashto."
  *Det Norske Videnskaps-Akademi*.
- Henderson, M.M.T. (1983). "Four Varieties of Pashto." *JIPA* 13(1).
- Skjærvø, P.O. (2006). "Pashto." In: *Compendium Linguarum
  Iranicarum*, ed. Schmitt. Reichert.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT

# ═══════════════════════════════════════════════════════════════════════════
# PASHTO (ps) — Standard Afghan Pashto
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Indo-European > Indo-Iranian > Iranian > Eastern Iranian
# Script: Pashto alphabet (modified Arabic, with extra letters)
# Speakers: ~50–60 million (Afghanistan + Pakistan)
#
# KEY PHONOLOGICAL FEATURES (Penzl 1955, David 2014):
#
# 1. RETROFLEX CONSONANTS: ʈ, ɖ, ɻ, ɳ — a hallmark of Pashto within
#    Iranian; attributed to Indo-Aryan contact or internal development.
#
# 2. POSTALVEOLAR AFFRICATES: ts, dz (from earlier *č, *ǰ) — "Pashto
#    shift" that distinguishes it from Persian. Also tʃ, dʒ in loanwords.
#
# 3. RETROFLEX FRICATIVES: ʂ, ʐ (Southern/Kandahari dialect);
#    in Northern (Peshawar) these → x, ɡ or ʃ, ʒ.
#
# 4. LATERAL FRICATIVE: ɬ (voiceless lateral fricative) — very unusual
#    in Iranian languages; only in Southern Pashto.
#
# 5. PHARYNGEALS: absent (unlike Arabic/Persian ħ ʕ are not native)
#
# 6. STRESS: generally penultimate; can be phonemic in some minimal pairs
#
# 7. VOWELS: 7-vowel system /a i u e o ə ɑː/ (with length in /ɑː/)

GRAPHEMES = {
    # --- Arabic-script letters with Pashto values ---
    # Vowels (mostly unwritten as in Arabic; some marked)
    "ا": ["ɑː", "a"],   # alef: long /ɑː/ or initial /a/
    "آ": ["ɑː"],         # alef-madda
    "و": ["w", "u", "o"],  # waw: consonant or vowel
    "ی": ["j", "i", "e"],  # ya: consonant or vowel
    "ې": ["e"],           # ye with hamza below — /e/ vowel
    "ۍ": ["əi"],          # feminine marker (final -əi)
    "ئ": ["ai", "əi"],    # hamza-ye

    # --- Stops ---
    "ب": ["b"],
    "پ": ["p"],
    "ت": ["t"],
    "ټ": ["ʈ"],           # retroflex t — KEY Pashto letter
    "د": ["d"],
    "ډ": ["ɖ"],           # retroflex d — KEY Pashto letter
    "ک": ["k"],
    "ګ": ["ɡ"],           # Pashto form of gaf
    "ق": ["q"],           # in Arabic loanwords

    # --- Affricates ---
    "څ": ["ts"],          # KEY PASHTO: < Proto-Iranian *č
    "ځ": ["dz"],          # KEY PASHTO: < Proto-Iranian *ǰ
    "چ": ["tʃ"],          # in loanwords / some dialects
    "ج": ["dʒ"],          # in loanwords / some dialects

    # --- Fricatives ---
    "ف": ["f"],           # mostly in loanwords
    "ث": ["s"],           # merged with /s/ (like Persian)
    "س": ["s"],
    "ز": ["z"],
    "ص": ["s"],           # merged with /s/
    "ض": ["z"],           # merged with /z/
    "ش": ["ʃ"],
    "ښ": ["ʂ"],           # KEY PASHTO: retroflex fricative (Southern)
    "ژ": ["ʒ"],
    "ږ": ["ʐ"],           # KEY PASHTO: voiced retroflex fricative (Southern)
    "خ": ["x"],
    "غ": ["ɣ"],
    "ح": ["h"],           # merged with /h/ (no pharyngeal)
    "ه": ["h", "a"],      # /h/ or silent (marking final vowel)
    "ع": ["ʔ"],           # glottal stop (pharyngeal lost)
    "ذ": ["z"],           # merged with /z/
    "ظ": ["z"],           # merged with /z/
    "ط": ["t"],           # merged with /t/

    # --- Nasals ---
    "م": ["m"],
    "ن": ["n"],
    "ڼ": ["ɳ"],           # retroflex n — KEY Pashto letter

    # --- Liquids ---
    "ل": ["l"],
    "ر": ["ɾ"],
    "ړ": ["ɻ"],           # retroflex flap — KEY Pashto letter

    # --- Short vowel diacritics (usually unwritten) ---
    "\u064E": ["a"],      # fatha
    "\u0650": ["i"],      # kasra
    "\u064F": ["u"],      # damma
}

ALLOPHONES = {
    # Stops
    "p": ["p", "pʰ"],  # aspiration in onset
    "b": ["b"],
    "t": ["t", "tʰ"],
    "d": ["d"],
    "ʈ": ["ʈ", "ʈʰ"],
    "ɖ": ["ɖ"],
    "k": ["k", "kʰ"],
    "ɡ": ["ɡ"],
    "q": ["q"],         # in Arabic loanwords only

    # Affricates
    "ts": ["ts"],
    "dz": ["dz"],
    "tʃ": ["tʃ"],
    "dʒ": ["dʒ"],

    # Fricatives
    "f": ["f"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "ʂ": ["ʂ", "ʃ"],   # Southern ʂ; Northern → ʃ or x
    "ʐ": ["ʐ", "ʒ"],   # Southern ʐ; Northern → ʒ or ɡ
    "x": ["x"], "ɣ": ["ɣ"],
    "h": ["h"],
    "ʔ": ["ʔ"],

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],   # assimilation before velars
    "ɳ": ["ɳ"],

    # Liquids
    "l": ["l"],
    "ɾ": ["ɾ", "r"],   # trill in emphatic/geminate
    "ɻ": ["ɻ"],        # retroflex flap

    # Glides
    "j": ["j"], "w": ["w"],

    # Vowels (7-vowel system)
    "a": ["a", "ɐ"],
    "ɑː": ["ɑː"],
    "i": ["i"],
    "u": ["u"],
    "e": ["e"],
    "o": ["o"],
    "ə": ["ə"],
}


SPECS = {
    "ps": LanguageSpec(
        code="ps",
        name="Pashto (Standard Afghan)",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="ine",
        ancestors=(
            Ancestor("ine", P, 0.95,
                     "Indo-European > Indo-Iranian > Iranian > Eastern Iranian"),
        ),
        notes=(
            "Pashto (پښتو) — Standard Afghan Pashto (Kandahari base). "
            "Eastern Iranian language; ~50–60 million speakers. "
            "One of two official languages of Afghanistan (with Dari). "
            "DEFINING FEATURES vs. Persian: "
            "(1) Retroflex consonants ʈ, ɖ, ɳ, ɻ, ʂ, ʐ; "
            "(2) Pashto shift: Proto-Iranian *č → ts, *ǰ → dz; "
            "(3) No pharyngeals (ħ ʕ absent, unlike Arabic); "
            "(4) 7-vowel system /a i u e o ə ɑː/; "
            "(5) Retroflex fricatives ʂ, ʐ in Southern dialect. "
            "Modified Arabic script with extra letters for retroflexes "
            "and affricates (ټ ډ ڼ ړ څ ځ ښ ږ). "
            "ADSTRATE EFFECT ON DARI: some retroflex-influenced articulation "
            "in Afghan Persian speakers with Pashto contact. "
            "Refs: Penzl (1955), David (2014), Tegey & Robson (1996)."
        ),
    ),
}
