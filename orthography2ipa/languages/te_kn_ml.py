"""Telugu (te), Kannada (kn), and Malayalam (ml) — grapheme→IPA and allophone mappings.

Sources:
- Krishnamurti, Bh. (2003). *The Dravidian Languages*. CUP.
- Subrahmanyam, P.S. (1983). *Dravidian Comparative Phonology*. Annamalai University.
- Lisker, L. (1963). 'The Telugu stops'. *Phonetica* 9.
- Keane, E. (2004). Tamil. *JIPA* (used for Dravidian comparison).
- Namboodiripad, S. (1998). *Malayalam Phonology*. Thiruvananthapuram.
- Kelkar, A. (1958). 'Kannada phonology'. *Indian Linguistics* 19.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
AD = AncestorRole.ADSTRATE
SUB = AncestorRole.SUBSTRATE

# ══════════════════════════════════════════════════════════════════════════════
# Telugu — Andhra Pradesh / Telangana; Telugu script
# ══════════════════════════════════════════════════════════════════════════════
# Unlike Tamil: Telugu HAS aspirated stops (borrowed from Sanskrit contact);
# Voiced/voiceless distinction phonemic in stops.
# Has /ɭ/ retroflex lateral phonemic.

GRAPHEMES_TE = {
    # --- Independent vowels ---
    "అ": ["a"], "ఆ": ["aː"],
    "ఇ": ["i"], "ఈ": ["iː"],
    "ఉ": ["u"], "ఊ": ["uː"],
    "ఋ": ["r̩"],
    "ఎ": ["e"], "ఏ": ["eː"],
    "ఐ": ["ai"],
    "ఒ": ["o"], "ఓ": ["oː"],
    "ఔ": ["au"],

    # --- Vowel diacritics ---
    "ా": ["aː"],
    "ి": ["i"], "ీ": ["iː"],
    "ు": ["u"], "ూ": ["uː"],
    "ృ": ["r̩"],
    "ె": ["e"], "ే": ["eː"], "ై": ["ai"],
    "ొ": ["o"], "ో": ["oː"], "ౌ": ["au"],
    "ం": ["̃m", "ŋ"],  # anusvāra
    "ః": ["h"],  # visarga
    "్": [""],  # virāma

    # --- Stops: Telugu has aspirated series from Sanskrit ---
    # Velars
    "క": ["k"], "ఖ": ["kʰ"], "గ": ["ɡ"], "ఘ": ["ɡʱ"], "ఙ": ["ŋ"],
    # Palatals
    "చ": ["tɕ"], "ఛ": ["tɕʰ"], "జ": ["dʑ"], "ఝ": ["dʑʱ"], "ఞ": ["ɲ"],
    # Retroflexes
    "ట": ["ʈ"], "ఠ": ["ʈʰ"], "డ": ["ɖ"], "ఢ": ["ɖʱ"], "ణ": ["ɳ"],
    # Dentals
    "త": ["t̪"], "థ": ["t̪ʰ"], "ద": ["d̪"], "ధ": ["d̪ʱ"], "న": ["n"],
    # Labials
    "ప": ["p"], "ఫ": ["pʰ"], "బ": ["b"], "భ": ["bʱ"], "మ": ["m"],

    # --- Approximants / liquids ---
    "య": ["j"],
    "ర": ["r"],  # alveolar trill
    "ల": ["l"],  # alveolar lateral
    "వ": ["ʋ"],
    "ళ": ["ɭ"],  # retroflex lateral (distinct from ల)
    "ఱ": ["r̝"],  # archaic: strong trill (historically distinct from ర)

    # --- Sibilants / aspirate ---
    "శ": ["ɕ"],  # palatal sibilant
    "ష": ["ʂ"],  # retroflex sibilant
    "స": ["s"],  # dental sibilant
    "హ": ["h"],
}

ALLOPHONES_TE = {
    # Telugu stops are phonemically voiced/voiceless AND aspirated
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tɕ": ["tɕ"], "tɕʰ": ["tɕʰ"],
    "dʑ": ["dʑ"], "dʑʱ": ["dʑʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"],
    "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"],
    "m": ["m"], "n": ["n", "ɳ", "ŋ"],
    "ɲ": ["ɲ"], "ɳ": ["ɳ"],
    "ɕ": ["ɕ"], "ʂ": ["ʂ"], "s": ["s"],
    "h": ["h"],
    "r": ["r"], "l": ["l"], "ɭ": ["ɭ"],
    "ʋ": ["ʋ", "w"], "j": ["j"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ai": ["ai"], "au": ["au"],
}

# ══════════════════════════════════════════════════════════════════════════════
# Kannada — Karnataka; Kannada script (close to Telugu script)
# ══════════════════════════════════════════════════════════════════════════════

GRAPHEMES_KN = {
    # --- Independent vowels ---
    "ಅ": ["a"], "ಆ": ["aː"],
    "ಇ": ["i"], "ಈ": ["iː"],
    "ಉ": ["u"], "ಊ": ["uː"],
    "ಋ": ["r̩"],
    "ಎ": ["e"], "ಏ": ["eː"],
    "ಐ": ["ai"],
    "ಒ": ["o"], "ಓ": ["oː"],
    "ಔ": ["au"],

    # --- Vowel diacritics ---
    "ಾ": ["aː"],
    "ಿ": ["i"], "ೀ": ["iː"],
    "ು": ["u"], "ೂ": ["uː"],
    "ೃ": ["r̩"],
    "ೆ": ["e"], "ೇ": ["eː"], "ೈ": ["ai"],
    "ೊ": ["o"], "ೋ": ["oː"], "ೌ": ["au"],
    "ಂ": ["̃ŋ"], "ಃ": ["h"], "್": [""],

    # --- Stops: Kannada has full aspirated series ---
    "ಕ": ["k"], "ಖ": ["kʰ"], "ಗ": ["ɡ"], "ಘ": ["ɡʱ"], "ಙ": ["ŋ"],
    "ಚ": ["tɕ"], "ಛ": ["tɕʰ"], "ಜ": ["dʑ"], "ಝ": ["dʑʱ"], "ಞ": ["ɲ"],
    "ಟ": ["ʈ"], "ಠ": ["ʈʰ"], "ಡ": ["ɖ"], "ಢ": ["ɖʱ"], "ಣ": ["ɳ"],
    "ತ": ["t̪"], "ಥ": ["t̪ʰ"], "ದ": ["d̪"], "ಧ": ["d̪ʱ"], "ನ": ["n"],
    "ಪ": ["p"], "ಫ": ["pʰ"], "ಬ": ["b"], "ಭ": ["bʱ"], "ಮ": ["m"],

    # --- Approximants / liquids ---
    "ಯ": ["j"],
    "ರ": ["r"],  # alveolar trill
    "ಲ": ["l"],
    "ವ": ["ʋ"],
    "ಳ": ["ɭ"],  # retroflex lateral
    "ಱ": ["ɻ"],  # retroflex approximant (archaic; still in dialects)

    # --- Sibilants / aspirate ---
    "ಶ": ["ʃ"],
    "ಷ": ["ʂ"],
    "ಸ": ["s"],
    "ಹ": ["h"],
}

ALLOPHONES_KN = dict(ALLOPHONES_TE)  # Very similar phonological system

# ══════════════════════════════════════════════════════════════════════════════
# Malayalam — Kerala; Malayalam script (most complex Brahmic script)
# ══════════════════════════════════════════════════════════════════════════════
# Key features: /z/ phoneme (from *ḻ); gemination phonemic;
# very large consonant cluster inventory; aspirates from Sanskrit.

GRAPHEMES_ML = {
    # --- Independent vowels ---
    "അ": ["a"], "ആ": ["aː"],
    "ഇ": ["i"], "ഈ": ["iː"],
    "ഉ": ["u"], "ഊ": ["uː"],
    "ഋ": ["r̩"], "ൠ": ["r̩ː"],
    "ഌ": ["l̩"],
    "എ": ["e"], "ഏ": ["eː"],
    "ഐ": ["ai"],
    "ഒ": ["o"], "ഓ": ["oː"],
    "ഔ": ["au"],

    # --- Vowel diacritics ---
    "ാ": ["aː"],
    "ി": ["i"], "ീ": ["iː"],
    "ു": ["u"], "ൂ": ["uː"],
    "ൃ": ["r̩"],
    "െ": ["e"], "േ": ["eː"], "ൈ": ["ai"],
    "ൊ": ["o"], "ോ": ["oː"], "ൌ": ["au"],
    "ം": ["̃m", "ŋ"], "ഃ": ["h"], "്": [""],

    # --- Stops ---
    "ക": ["k"], "ഖ": ["kʰ"], "ഗ": ["ɡ"], "ഘ": ["ɡʱ"], "ങ": ["ŋ"],
    "ച": ["tɕ"], "ഛ": ["tɕʰ"], "ജ": ["dʑ"], "ഝ": ["dʑʱ"], "ഞ": ["ɲ"],
    "ട": ["ʈ"], "ഠ": ["ʈʰ"], "ഡ": ["ɖ"], "ഢ": ["ɖʱ"], "ണ": ["ɳ"],
    "ത": ["t̪"], "ഥ": ["t̪ʰ"], "ദ": ["d̪"], "ധ": ["d̪ʱ"], "ന": ["n"],
    "പ": ["p"], "ഫ": ["pʰ"], "ബ": ["b"], "ഭ": ["bʱ"], "മ": ["m"],

    # --- Approximants / liquids ---
    "യ": ["j"],
    "ര": ["r"],  # alveolar trill / flap
    "ല": ["l"],  # alveolar lateral
    "വ": ["ʋ"],
    "ഴ": ["z"],  # unique phoneme: derived from Proto-Dravidian *ḻ
    "ള": ["ɭ"],  # retroflex lateral
    "റ": ["r"],  # alveolar (historically strong trill; now = /r/ in standard)

    # --- Sibilants / aspirate ---
    "ശ": ["ʃ"],
    "ഷ": ["ʂ"],
    "സ": ["s"],
    "ഹ": ["h"],
}

ALLOPHONES_ML = {
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "tɕ": ["tɕ"], "tɕʰ": ["tɕʰ"],
    "dʑ": ["dʑ"], "dʑʱ": ["dʑʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"],
    "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"],
    "m": ["m"], "n": ["n", "ɳ", "ŋ"],
    "ɲ": ["ɲ"], "ɳ": ["ɳ"],
    "ʃ": ["ʃ"], "ʂ": ["ʂ"], "s": ["s"],
    "h": ["h"],
    "r": ["r", "ɾ"],
    "l": ["l"], "ɭ": ["ɭ"],
    "z": ["z", "ɻ"],  # /z/ (unique to Malayalam among major Dravidian)
    "ʋ": ["ʋ", "w"], "j": ["j"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ai": ["ai"], "au": ["au"],
    "r̩": ["r̩"],
}

SPECS = {
    "te": LanguageSpec(
        code="te",
        name="Telugu",
        family="Dravidian",
        script="Telugu",
        graphemes=GRAPHEMES_TE,
        allophones=ALLOPHONES_TE,
        parent=None,
        ancestors=(
            Ancestor("ta-x-proto-dravidian", P, 0.85,
                     "Descent from Proto-South-Central Dravidian"),
            Ancestor("sa", AD, 0.12,
                     "Sanskrit adstrate: heavy borrowing into classical literature (Prabandha)"),
        ),
        notes=(
            "Standard Telugu (Andhra Pradesh and Telangana). "
            "Most widely spoken Dravidian language. "
            "Unlike Tamil, Telugu has aspirated stops from Sanskrit contact "
            "fully integrated into the phonological system. "
            "⟨ళ⟩ = [ɭ] retroflex lateral phonemic. "
            "All vowels have short/long distinction."
        ),
    ),
    "kn": LanguageSpec(
        code="kn",
        name="Kannada",
        family="Dravidian",
        script="Kannada",
        graphemes=GRAPHEMES_KN,
        allophones=ALLOPHONES_KN,
        parent=None,
        ancestors=(
            Ancestor("ta-x-proto-dravidian", P, 0.85,
                     "Descent from Proto-South-Dravidian"),
            Ancestor("sa", AD, 0.10,
                     "Sanskrit adstrate through Kadamba, Chalukya, Hoysala courts"),
            Ancestor("te", AD, 0.03,
                     "Telugu adstrate along eastern borders"),
        ),
        notes=(
            "Standard Kannada (Karnataka). "
            "Phonological system closely parallel to Telugu. "
            "⟨ಳ⟩ = [ɭ] retroflex lateral phonemic. "
            "Archaic ⟨ಱ⟩ = [ɻ] (retroflex approximant, cf. Tamil/Malayalam ⟨ழ⟩) "
            "survives in some dialects. "
            "Aspiration in native words only post-Sanskrit contact."
        ),
    ),
    "ml": LanguageSpec(
        code="ml",
        name="Malayalam",
        family="Dravidian",
        script="Malayalam",
        graphemes=GRAPHEMES_ML,
        allophones=ALLOPHONES_ML,
        parent=None,
        ancestors=(
            Ancestor("ta", P, 0.75,
                     "Descended from Old Tamil; split c. 9th century CE"),
            Ancestor("sa", AD, 0.20,
                     "Very heavy Sanskrit adstrate: ~50% of formal vocabulary"),
        ),
        notes=(
            "Standard Malayalam (Kerala). "
            "Descended from Old Tamil, diverged c. 9th–13th century CE. "
            "Unique phoneme: ⟨ഴ⟩ = /z/ (derived from Proto-Dravidian *ḻ, "
            "retained as /z/ only in Malayalam). "
            "Uses the most complex Brahmic script (~60 base characters). "
            "Phonemic gemination. Heavy Sanskrit vocabulary in formal register."
        ),
    ),
}
