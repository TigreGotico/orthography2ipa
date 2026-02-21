"""Franco-Provençal and Rhaeto-Romance languages.

Contains:
- frp: Franco-Provençal / Arpitan (Gallo-Romance)
- rm:  Romansh (Rhaeto-Romance)
- lld: Ladin (Rhaeto-Romance)
- fur: Friulian (Rhaeto-Romance)

Sources:
Franco-Provençal:
- Tuaillon, G. (1988). 'Le franco-provençal: progrès d'une
  définition.' *Travaux de linguistique et de littérature* 26(1).
- Stich, D. (2003). *Dictionnaire francoprovençal/français,
  français/francoprovençal*. Éd. Le Carré.
- Martin, J.-B. (2005). *Le francoprovençal de poche*. Assimil.
- Kristol, A.M. (2016). 'Francoprovençal.' In Ledgeway & Maiden
  (eds.), *The Oxford Guide to the Romance Languages*. OUP.

Rhaeto-Romance:
- Haiman, J. & Benincà, P. (1992). *The Rhaeto-Romance Languages*.
  Routledge.
- Liver, R. (1999). *Rätoromanisch: eine Einführung in das
  Bündnerromanische*. Narr.
- Iliescu, M. (2016). 'Friulian.' In Ledgeway & Maiden (eds.),
  *The Oxford Guide to the Romance Languages*. OUP.
- Craffonara, L. (1977). 'Zur Stellung des Dolomitenladinischen.'
  *Ladinia* 1.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# FRANCO-PROVENÇAL / ARPITAN (frp)
# ═══════════════════════════════════════════════════════════════════════════
#
# A distinct Gallo-Romance language between French (Oïl) and Occitan (Oc).
# Spoken historically in: Savoie, Lyonnais, Suisse Romande, Aosta Valley.
#
# KEY FEATURES distinguishing from French AND Occitan:
# 1. Latin CA- → [tʃ] (like French) but less extreme than French [ʃ]
# 2. Preservation of final -a (unlike French which deletes it)
# 3. /u/ → /y/ fronting (shared with French, absent in Occitan)
# 4. Less nasal vowels than French
# 5. Conservative consonant clusters

GRAPHEMES_FRP = {
    # --- Vowels ---
    "a": ["a"],
    "â": ["ɑ"],
    "e": ["e", "ɛ"],
    "é": ["e"],
    "è": ["ɛ"],
    "ê": ["ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "ô": ["o"],
    "u": ["y"],  # fronted (Gallo-Romance innovation)
    "ou": ["u"],  # back /u/ preserved here

    # --- Nasal vowels (fewer than French) ---
    "an": ["ã"],
    "en": ["ẽ"],
    "on": ["õ"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "s"],  # /s/ before e,i (like French)
    "ch": ["tʃ"],  # < CA- (intermediate: not [k] like Oc, not [ʃ] like Fr.)
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],
    "j": ["dʒ", "ʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "qu": ["k"],
    "r": ["ʁ", "r"],  # varies by region: uvular in urban, trill in rural
    "s": ["s", "z"],
    "t": ["t"],
    "v": ["v"],
    "z": ["z", "dz"],

    # --- Digraphs ---
    "gn": ["ɲ"],
    "ll": ["ʎ", "j"],  # depalatalised to [j] in many areas
    "ts": ["ts"],
    "dz": ["dz"],
    "sh": ["ʃ"],

    # --- Diphthongs ---
    "ai": ["aj", "ɛ"],
    "ei": ["ej"],
    "oi": ["we", "wɛ"],
    "au": ["aw", "o"],
}

ALLOPHONES_FRP = {
    "p": ["p"], "b": ["b", "β"],
    "t": ["t"], "d": ["d", "ð"],
    "k": ["k"], "ɡ": ["ɡ", "ɣ"],
    "tʃ": ["tʃ", "ts"], "dʒ": ["dʒ", "dz"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "ts": ["ts"], "dz": ["dz"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ", "j"],
    "ʁ": ["ʁ", "ʀ"], "r": ["r", "ɾ"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "ɑ": ["ɑ"], "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"], "o": ["o"], "ɔ": ["ɔ"],
    "y": ["y"], "u": ["u"],
    "ã": ["ã"], "ẽ": ["ẽ"], "õ": ["õ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# ROMANSH (rm)
# ═══════════════════════════════════════════════════════════════════════════
#
# Rhaeto-Romance language of Graubünden, Switzerland.
# ~60,000 speakers. National language of Switzerland since 1938.
# Written standard: Rumantsch Grischun (RG, since 1982).
#
# KEY FEATURES:
# 1. Palatalisation of CA- → [tɕ] (diagnostic Rhaeto-Romance feature)
# 2. Front rounded vowels /y, ø/ (Gallo-Romance heritage)
# 3. Preservation of some Latin consonant clusters (pl-, cl-, fl-)
# 4. German superstrate influence (bilingual for centuries)

GRAPHEMES_RM = {
    # --- Vowels ---
    "a": ["a"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],
    "ü": ["y"],  # front rounded (Gallo-Romance)

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "ts"],  # [ts] before e,i
    "ch": ["k", "tɕ"],  # [tɕ] < CA- in some idioms
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],
    "gl": ["ʎ"],
    "gn": ["ɲ"],
    "h": ["h"],  # in German loans
    "j": ["j"],
    "k": ["k"],  # in loans
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "qu": ["kw"],
    "r": ["r"],
    "s": ["s", "z"],
    "sch": ["ʃ"],
    "t": ["t"],
    "tg": ["dʒ"],  # < Latin CA- (Sursilvan)
    "tsch": ["tʃ"],
    "v": ["v"],
    "z": ["ts"],
}

ALLOPHONES_RM = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "ts": ["ts"], "dʒ": ["dʒ"],
    "tʃ": ["tʃ"], "tɕ": ["tɕ"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"],
    "h": ["h"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "r": ["r", "ɾ"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"],
    "i": ["i"], "o": ["o"], "ɔ": ["ɔ"],
    "u": ["u"], "y": ["y"],
}

# ═══════════════════════════════════════════════════════════════════════════
# LADIN (lld)
# ═══════════════════════════════════════════════════════════════════════════
#
# Rhaeto-Romance of the Dolomites (South Tyrol, Trentino, Belluno).
# ~30,000 speakers. Key Rhaeto-Romance features + Italo-Romance contact.
#
# KEY FEATURES:
# 1. Palatalisation of CA- → [tʃ] (Rhaeto-Romance diagnostic)
# 2. Preservation of Latin consonant clusters (PL-, CL-, FL-)
# 3. Front rounded vowels /y, ø/
# 4. Gemination (Italo-Romance influence)

GRAPHEMES_LLD = {
    # --- Vowels ---
    "a": ["a"],
    "e": ["e", "ɛ"],
    "ë": ["ə"],  # central vowel (some varieties)
    "i": ["i"],
    "o": ["o", "ɔ"],
    "ö": ["ø"],  # front rounded
    "u": ["u"],
    "ü": ["y"],  # front rounded

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "tʃ"],  # [tʃ] before e,i
    "ch": ["k"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],
    "gh": ["ɡ"],
    "gn": ["ɲ"],
    "gl": ["ʎ"],  # < Latin -LI-
    "h": ["∅"],
    "j": ["dʒ"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "qu": ["kw"],
    "r": ["r"],
    "s": ["s", "z"],
    "sc": ["ʃ"],  # before e,i
    "t": ["t"],
    "v": ["v"],
    "z": ["ts", "dz"],
}

ALLOPHONES_LLD = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "ts": ["ts"], "dz": ["dz"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "r": ["r", "ɾ"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "e": ["e"], "ɛ": ["ɛ"], "ə": ["ə"],
    "i": ["i"], "o": ["o"], "ɔ": ["ɔ"],
    "u": ["u"], "y": ["y"], "ø": ["ø"],
}

# ═══════════════════════════════════════════════════════════════════════════
# FRIULIAN (fur)
# ═══════════════════════════════════════════════════════════════════════════
#
# Rhaeto-Romance of Friuli-Venezia Giulia, NE Italy.
# ~600,000 speakers. The largest Rhaeto-Romance language.
#
# Classification is debated: some put it with Rhaeto-Romance (→ Gallo),
# others with NE Italo-Romance. We classify under la-x-italia with
# strong Gallo-Romance adstrate influence, following Benincà (1997).
#
# KEY FEATURES:
# 1. Long vowels (phonemic length, unique in modern Italo-Romance)
# 2. Palatalisation of CA-, GA- (Rhaeto-Romance feature)
# 3. Final consonant clusters retained
# 4. /θ/ in some varieties (archaic or substrate?)

GRAPHEMES_FUR = {
    # --- Vowels (with phonemic length) ---
    "a": ["a"],
    "â": ["aː"],  # long vowels (phonemic!)
    "e": ["e", "ɛ"],
    "ê": ["eː"],
    "i": ["i"],
    "î": ["iː"],
    "o": ["o", "ɔ"],
    "ô": ["oː"],
    "u": ["u"],
    "û": ["uː"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "tʃ"],  # [tʃ] before e,i
    "ch": ["k"],
    "cj": ["tʃ"],  # palatalised (< CA-)
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],
    "gj": ["dʒ"],  # palatalised (< GA-)
    "gl": ["ʎ"],
    "gn": ["ɲ"],
    "h": ["∅"],
    "j": ["j"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "qu": ["kw"],
    "r": ["r"],
    "s": ["s", "z"],
    "sc": ["ʃ"],
    "t": ["t"],
    "v": ["v"],
    "z": ["ts", "dz"],
}

ALLOPHONES_FUR = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "ts": ["ts"], "dz": ["dz"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"],
    "m": ["m"], "n": ["n", "ŋ"], "ɲ": ["ɲ"],
    "l": ["l"], "ʎ": ["ʎ"],
    "r": ["r", "ɾ"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "aː": ["aː"],
    "e": ["e"], "eː": ["eː"], "ɛ": ["ɛ"],
    "i": ["i"], "iː": ["iː"],
    "o": ["o"], "oː": ["oː"], "ɔ": ["ɔ"],
    "u": ["u"], "uː": ["uː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "frp": LanguageSpec(
        code="frp",
        name="Franco-Provençal (Arpitan)",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_FRP,
        allophones=ALLOPHONES_FRP,
        parent="la-x-gallia",
        ancestors=(
            Ancestor("la-x-gallia", P, 0.78,
                     "Gallo-Romance parent: shares /u/→/y/ fronting, "
                     "CA- palatalisation with French and Occitan."),
            Ancestor("xcg", SUB, 0.08,
                     "Gaulish substrate: shared with French. "
                     "Vigesimal traces, some lexicon."),
            Ancestor("gem", SUP, 0.07,
                     "Burgundian/Frankish superstrate: less intense "
                     "than in French, more than in Occitan."),
        ),
        notes=(
            "Franco-Provençal / Arpitan. A distinct Gallo-Romance "
            "language intermediate between French (Oïl) and Occitan "
            "(Oc). Spoken historically in Savoie, Lyonnais, Suisse "
            "Romande, and Aosta Valley. Key features: (1) CA- → [tʃ] "
            "(like French, vs Occitan [ka]). (2) Final -a preserved "
            "(unlike French). (3) /u/→/y/ fronting (shared with French). "
            "(4) Less nasal vowels than French. ~150,000 speakers, "
            "severely endangered (Kristol 2016)."
        ),
    ),
    "rm": LanguageSpec(
        code="rm",
        name="Romansh",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_RM,
        allophones=ALLOPHONES_RM,
        parent="la-x-gallia",
        ancestors=(
            Ancestor("la-x-gallia", P, 0.70,
                     "Gallo-Romance parent: Rhaeto-Romance branch."),
            Ancestor("cel", SUB, 0.08,
                     "Celtic (Raetian/Lepontic) substrate: Alpine "
                     "Celtic may have influenced consonant clusters."),
            Ancestor("de-DE", AD, 0.15,
                     "German adstrate: centuries of bilingualism. "
                     "Massive lexical influence, some phonological "
                     "(aspiration of stops, /h/ restoration)."),
        ),
        notes=(
            "Romansh (Rumantsch). Rhaeto-Romance language of "
            "Graubünden, Switzerland. ~60,000 speakers. National "
            "language since 1938. Written standard: Rumantsch Grischun "
            "(1982). Five spoken idioms: Sursilvan, Sutsilvan, "
            "Surmiran, Puter, Vallader. Key features: (1) CA- "
            "palatalisation. (2) Front rounded vowels /y/. "
            "(3) Heavy German contact influence (Liver 1999)."
        ),
    ),
    "lld": LanguageSpec(
        code="lld",
        name="Ladin",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_LLD,
        allophones=ALLOPHONES_LLD,
        parent="la-x-gallia",
        ancestors=(
            Ancestor("la-x-gallia", P, 0.72,
                     "Gallo-Romance parent: Rhaeto-Romance branch."),
            Ancestor("cel", SUB, 0.06,
                     "Celtic (Raetian) substrate."),
            Ancestor("de-DE", AD, 0.10,
                     "German adstrate: South Tyrol bilingualism."),
            Ancestor("it-IT", AD, 0.08,
                     "Italian adstrate: Trentino-Belluno contact."),
        ),
        notes=(
            "Ladin. Rhaeto-Romance language of the Dolomites (South "
            "Tyrol, Trentino, Belluno). ~30,000 speakers. Key features: "
            "(1) CA- → [tʃ] palatalisation. (2) Front rounded vowels "
            "/y, ø/. (3) Preservation of Latin PL-, CL-, FL- clusters. "
            "(4) Central vowel /ə/ in some varieties. German and "
            "Italian adstrate influence (Craffonara 1977)."
        ),
    ),
    "fur": LanguageSpec(
        code="fur",
        name="Friulian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_FUR,
        allophones=ALLOPHONES_FUR,
        parent="la-x-italia",
        ancestors=(
            Ancestor("la-x-italia", P, 0.70,
                     "Italo-Romance parent: following Benincà (1997), "
                     "Friulian is NE Italo-Romance with Rhaeto features."),
            Ancestor("la-x-gallia", AD, 0.12,
                     "Gallo-Romance adstrate: shares CA- palatalisation, "
                     "some vowel features with Rhaeto-Romance."),
            Ancestor("cel", SUB, 0.05,
                     "Celtic (Carnic) substrate."),
            Ancestor("de-DE", AD, 0.05,
                     "German adstrate: Friuli-Carinthia contact."),
        ),
        notes=(
            "Friulian (Furlan). Largest Rhaeto-Romance language, "
            "~600,000 speakers in Friuli-Venezia Giulia. Classification "
            "debated: Rhaeto-Romance or NE Italo-Romance with Rhaeto "
            "features. Key features: (1) Phonemic vowel LENGTH (unique "
            "in modern Italo-Romance). (2) CA-/GA- palatalisation to "
            "[tʃ]/[dʒ]. (3) Final consonant clusters retained. "
            "(4) Official regional language since 1999 (Iliescu 2016)."
        ),
    ),
}
