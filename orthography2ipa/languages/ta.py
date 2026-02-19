"""Tamil (ta) — grapheme→IPA and allophone mappings.

Sources:
- Asher, R.E. (1985). *Tamil*. Croom Helm.
- Keane, E. (2004). Tamil. *JIPA* 34(1).
- Krishnamurti, Bh. (2003). *The Dravidian Languages*. CUP.
- Lehmann, T. (1989). *A Grammar of Modern Tamil*. PILC.
- Subrahmanyam, P.S. (1983). *Dravidian Comparative Phonology*. Annamalai University.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
AD = AncestorRole.ADSTRATE
SUB = AncestorRole.SUBSTRATE

# ══════════════════════════════════════════════════════════════════════════════
# Standard Tamil — Tamil Nadu / Sri Lanka
# ══════════════════════════════════════════════════════════════════════════════
# Tamil phonology is radically different from Indo-Aryan:
# - No aspirated stops phonemically (aspirates are allophones)
# - No voiced/voiceless distinction in stops (voice is positional allophone)
# - Strong agglutinative morphology
# - Retroflex lateral /ɭ/, retroflex approximant /ɻ/ (unique rhotic)
# - Diglossia: formal (centami) vs. colloquial speech differ greatly

GRAPHEMES = {
    # --- Independent vowels (uyir: 'life' letters) ---
    "அ": ["a"],  # short a
    "ஆ": ["aː"],  # long ā
    "இ": ["i"],  # short i
    "ஈ": ["iː"],  # long ī
    "உ": ["u"],  # short u (often → [ɯ] in closed syllable)
    "ஊ": ["uː"],  # long ū
    "எ": ["e"],  # short e
    "ஏ": ["eː"],  # long ē
    "ஐ": ["ai"],  # ai diphthong
    "ஒ": ["o"],  # short o
    "ஓ": ["oː"],  # long ō
    "ஔ": ["au"],  # au diphthong

    # --- Vowel diacritics (combined with consonants) ---
    "ா": ["aː"],
    "ி": ["i"], "ீ": ["iː"],
    "ு": ["u"], "ூ": ["uː"],
    "ெ": ["e"], "ே": ["eː"],
    "ை": ["ai"],
    "ொ": ["o"], "ோ": ["oː"],
    "ௌ": ["au"],
    "்": [""],  # puḷḷi (virāma): marks bare consonant

    # --- Stops and nasals (mei: 'body' letters) ---
    # Velars
    "க": ["k", "ɡ", "x"],  # [k] initially; [ɡ] medially; [x] in some contexts
    "ங": ["ŋ"],

    # Palatals
    "ச": ["tɕ", "s", "dʑ"],  # [tɕ] initially; [s] medially (allophone)
    "ஞ": ["ɲ"],

    # Retroflexes
    "ட": ["ʈ", "ɖ"],  # [ʈ] initially; [ɖ] medially
    "ண": ["ɳ"],

    # Dentals
    "த": ["t̪", "d̪", "ð"],  # [t̪] initially; [d̪] medially; [ð] intervocalically
    "ந": ["n"],
    "ன": ["n"],  # alveolar nasal (distinguished in formal Tamil)

    # Labials
    "ப": ["p", "b"],  # [p] initially; [b] medially
    "ம": ["m"],

    # --- Approximants / liquids (vallinam / mellinam) ---
    "ய": ["j"],
    "ர": ["r"],  # alveolar trill / tap
    "ல": ["l"],  # alveolar lateral
    "வ": ["ʋ", "v"],  # labiodental approximant
    "ழ": ["ɻ"],  # retroflex approximant (unique Tamil phoneme!)
    "ள": ["ɭ"],  # retroflex lateral
    "ற": ["r", "tɾ"],  # alveolar trill (stronger); [tɾ] initially

    # --- Grantha letters (for Sanskrit/loan words) ---
    "ஜ": ["dʒ"],  # ja
    "ஶ": ["ʃ"],  # śa
    "ஷ": ["ʂ"],  # ṣa
    "ஸ": ["s"],  # sa
    "ஹ": ["h"],  # ha
    "க்ஷ": ["kʂ"],  # kṣa
    "ஸ்ரீ": ["ʃriː"],  # śrī

    # --- Numerals / special signs ---
    "ஃ": ["k", ""],  # āytam: special phoneme (varies by analysis)
}

ALLOPHONES = {
    # Tamil stops: no phonemic aspiration; voice is positional
    "k": ["k", "ɡ", "x", "h"],
    # [k] word-initial and after homorganic nasal
    # [ɡ] between vowels (medially)
    # [x] intervocalically in some dialects
    # [h] or zero in fast speech

    "tɕ": ["tɕ", "s", "dʑ", "ɕ"],
    # [tɕ] initially/after nasal; [s] medially in formal; [ʑ] colloquially

    "ʈ": ["ʈ", "ɖ", "ɽ"],
    # [ʈ] initially; [ɖ] medially; [ɽ] flap in some dialects

    "t̪": ["t̪", "d̪", "ð"],
    # [t̪] initially; [d̪] medially; [ð] intervocalically

    "p": ["p", "b", "β"],
    # [p] initially; [b] medially; [β] intervocalically

    # Nasals
    "m": ["m"],
    "n": ["n", "n̪"],
    "ɲ": ["ɲ", "j"],  # [j] in colloquial before front vowel
    "ɳ": ["ɳ"],
    "ŋ": ["ŋ"],

    # Approximants / liquids
    "j": ["j"],
    "ʋ": ["ʋ", "v", "w"],
    "r": ["r", "ɾ"],
    "l": ["l"],
    "ɻ": ["ɻ"],  # retroflex approximant
    "ɭ": ["ɭ"],  # retroflex lateral

    # Grantha consonants (Sanskrit loans)
    "dʒ": ["dʒ"],
    "ʃ": ["ʃ"],
    "ʂ": ["ʂ"],
    "s": ["s"],
    "h": ["h"],

    # Vowels
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u", "ɯ"],  # [ɯ] in some closed-syllable positions
    "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ai": ["ai"], "au": ["au"],
}

SPECS = {
    "ta": LanguageSpec(
        code="ta",
        name="Tamil",
        family="Dravidian",
        script="Tamil",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent=None,
        ancestors=(
            Ancestor("ta-x-proto-dravidian", P, 0.90,
                     "Direct descendant of Proto-Dravidian via Proto-South-Dravidian"),
            Ancestor("sa", AD, 0.08,
                     "Sanskrit adstrate: Grantha letters, Sanskrit loanwords in formal register"),
        ),
        notes=(
            "Standard Tamil (Tamil Nadu, India + Sri Lanka). "
            "Dravidian language, not related to Indo-Aryan. "
            "Key features: no aspirated stop phonemes (aspiration is allophonic); "
            "voiced/voiceless distinction positional (not phonemic for native words); "
            "unique retroflex approximant ⟨ழ⟩ = [ɻ]; "
            "retroflex lateral ⟨ள⟩ = [ɭ]; alveolar ⟨ன⟩ vs dental ⟨ந⟩. "
            "Strong diglossia: literary (centamiḻ) vs spoken (kōccai tamiḻ). "
            "Oldest attested Dravidian language (inscriptions from 3rd c. BCE)."
        ),
    ),
}
