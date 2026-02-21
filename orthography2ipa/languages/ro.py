"""Romanian (ro) — grapheme→IPA and allophone mappings.

Sources:
- Chițoran, I. (2001). *The Phonology of Romanian*. Mouton de Gruyter.
- Sarlin, M. (2014). Romanian. *JIPA* 44(1).
- Rosetti, A. (1986). *Istoria limbii române*. 7th ed. Ed. Știintifică.
- Sala, M. (2005). *From Latin to Romanian*. U of Mississippi Press.
- Nandriș, O. (1963). *Phonétique historique du roumain*. Klincksieck.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

GRAPHEMES = {
    # --- Vowels ---
    "a": ["a"],
    "ă": ["ə"],  # central vowel (Balkan Romance innovation)
    "â": ["ɨ"],  # central vowel (Balkan Romance innovation)
    "e": ["e", "ɛ"],
    "i": ["i"],
    "î": ["ɨ"],  # same phoneme as ⟨â⟩
    "o": ["o"],
    "u": ["u"],

    # --- Consonants ---
    "b": ["b"],
    "c": ["k", "tʃ"],  # /tʃ/ before e,i
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "dʒ"],  # /dʒ/ before e,i
    "h": ["h"],
    "j": ["ʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["r"],
    "s": ["s"],
    "ș": ["ʃ"],
    "t": ["t"],
    "ț": ["ts"],
    "v": ["v"],
    "w": ["v", "w"],
    "x": ["ks", "ɡz"],
    "y": ["i", "j"],
    "z": ["z"],

    # --- Digraphs ---
    "ch": ["k"],  # before e,i: ⟨che⟩ = [ke]
    "gh": ["ɡ"],  # before e,i: ⟨ghe⟩ = [ɡe]
    "ce": ["tʃe"], "ci": ["tʃi"],
    "ge": ["dʒe"], "gi": ["dʒi"],

    # --- Diphthongs ---
    "ea": ["e̯a"], "oa": ["o̯a"],
    "ai": ["aj"], "ei": ["ej"], "oi": ["oj"], "ui": ["uj"],
    "au": ["aw"], "eu": ["ew"], "ou": ["ow"],
    "ia": ["ja"], "ie": ["je"], "io": ["jo"], "iu": ["ju"],
    "ua": ["wa"], "ue": ["we"],

    # --- Triphthongs ---
    "eau": ["e̯aw"],
    "eai": ["e̯aj"],
    "oai": ["o̯aj"],
    "iai": ["jaj"],
}

ALLOPHONES = {
    "b": ["b"], "d": ["d"], "ɡ": ["ɡ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f"], "v": ["v"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "ts": ["ts"], "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "h": ["h", "x"],
    "m": ["m"], "n": ["n", "ŋ"],
    "l": ["l"], "r": ["r", "ɾ"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "ə": ["ə"], "ɨ": ["ɨ"],
    "e": ["e"], "ɛ": ["ɛ"], "i": ["i"],
    "o": ["o"], "u": ["u"],
}

SPECS = {
    "ro-RO": LanguageSpec(
        code="ro-RO",
        name="Romanian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="la-x-balkans",
        ancestors=(
            Ancestor("la-x-balkans", P, 0.65,
                     "Balkan Romance Vulgar Latin: Eastern Romance "
                     "branch with no lenition, central vowels, "
                     "postposed article."),
            Ancestor("sla", SUP, 0.20,
                     "Slavic superstrate (7th c. onwards): massive "
                     "lexical influence (~40% of vocabulary), "
                     "some phonological impact (palatalisation "
                     "patterns, possible influence on central vowels). "
                     "Old Church Slavonic was the literary/liturgical "
                     "language until 16th–17th c."),
            Ancestor("xda", SUB, 0.05,
                     "Dacian/Thracian substrate: ~100+ words shared "
                     "with Albanian of unknown origin (copil, moș, "
                     "viezure). Possible influence on central vowels "
                     "/ə, ɨ/ and postposed article."),
            Ancestor("grc", AD, 0.03,
                     "Greek adstrate: Byzantine influence, shared "
                     "Balkan sprachbund features."),
            Ancestor("tr", AD, 0.04,
                     "Turkish adstrate (14th–19th c.): lexical "
                     "borrowings from Ottoman period."),
            Ancestor("hu", AD, 0.03,
                     "Hungarian adstrate: centuries of contact in "
                     "Transylvania. Lexical exchange."),
        ),
        notes=(
            "Standard Romanian. Eastern Romance, the ONLY Romance "
            "language east of the Adriatic. Key features: (1) Central "
            "vowels /ə/ (⟨ă⟩) and /ɨ/ (⟨â/î⟩) — unique in Romance. "
            "(2) NO intervocalic lenition (lup, foc — not *lub, *fogo). "
            "(3) Postposed definite article (lupul 'the wolf'). "
            "(4) Rich diphthong/triphthong system. (5) Rhotacism: "
            "intervocalic /l/ → /r/ in some words (soare < SOLEM). "
            "(6) Massive Slavic vocabulary layer (~40%). "
            "(7) Balkan sprachbund member (Chițoran 2001, Sala 2005)."
        ),
    ),
}
