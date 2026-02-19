"""Urdu (ur) — grapheme→IPA and allophone mappings.

Sources:
- Schmidt, R.L. (1999). *Urdu: An Essential Grammar*. Routledge.
- Hussain, S. (2004). *Urdu Phonetics and Phonology*. Center for Research in Urdu Language Processing.
- Ohala, M. (1983). *Aspects of Hindi Phonology*. (shared base with Urdu)
- Khan, S. (1999). Urdu. *Handbook of the IPA*.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE

# Urdu is written in Nastaliq (Perso-Arabic script, right-to-left).
# Phonologically nearly identical to Hindi (Hindustani base) but:
# - Has /q/, /x/, /ɣ/, /f/, /z/ as phonemic (not just loan phonemes) for educated speakers
# - Has retroflex flap /ɽ/ and breathy stops phonemically

GRAPHEMES = {
    # --- Independent vowels (written forms / harakat) ---
    "ا": ["ə", "aː"],  # alef: short a or long ā depending on context
    "آ": ["aː"],  # alef madda: long ā
    "و": ["uː", "oː", "ʋ"],  # waw: ū, o, or consonant v/w
    "ی": ["iː", "eː", "j"],  # ye: ī, ē, or consonant y
    "ے": ["eː"],  # baṛī ye: long ē (final position)
    "ہ": ["ɦ", "ə"],  # he: h or silent schwa in final position
    "ع": ["ʔ", ""],  # ain: glottal stop (often silent in educated speech)

    # --- Short vowels (diacritics, often omitted in Nastaliq) ---
    "َ": ["ə"],  # zabar (fatha): short a
    "ِ": ["ɪ"],  # zer (kasra): short i
    "ُ": ["ʊ"],  # pesh (damma): short u
    "ً": ["ən"],  # tanwin fatha: -an (loanwords)

    # --- Consonants ---
    "ب": ["b"],
    "پ": ["p"],
    "ت": ["t̪"],
    "ٹ": ["ʈ"],  # retroflex t (Urdu-specific)
    "ث": ["s"],  # historically /θ/, modern = /s/
    "ج": ["dʒ"],
    "چ": ["tʃ"],
    "ح": ["h"],  # aspirate h (Arabic loan)
    "خ": ["x"],  # velar fricative
    "د": ["d̪"],
    "ڈ": ["ɖ"],  # retroflex d
    "ذ": ["z"],  # historically /ð/
    "ر": ["r"],
    "ڑ": ["ɽ"],  # retroflex flap
    "ز": ["z"],
    "ژ": ["ʒ"],  # in loanwords (French-origin)
    "س": ["s"],
    "ش": ["ʃ"],
    "ص": ["s"],  # Arabic emphatic; = /s/ in Urdu
    "ض": ["z"],  # Arabic emphatic; = /z/ in Urdu
    "ط": ["t̪"],  # Arabic emphatic; = /t/ in Urdu
    "ظ": ["z"],  # Arabic emphatic; = /z/ in Urdu
    "غ": ["ɣ"],  # voiced velar fricative
    "ف": ["f"],
    "ق": ["q"],  # uvular stop
    "ک": ["k"],
    "گ": ["ɡ"],
    "ل": ["l"],
    "م": ["m"],
    "ن": ["n"],
    "ں": ["̃"],  # nun ghunna: nasalisation only
    "ہ": ["ɦ"],
    "ھ": ["ʰ"],  # do chashmi he: aspiration diacritic
    "و": ["ʋ"],
    "ی": ["j"],
    "ے": ["j"],

    # --- Aspirated consonants (do chashmi he digraphs) ---
    "بھ": ["bʱ"], "پھ": ["pʰ"], "تھ": ["t̪ʰ"], "ٹھ": ["ʈʰ"],
    "جھ": ["dʒʱ"], "چھ": ["tʃʰ"], "دھ": ["d̪ʱ"], "ڈھ": ["ɖʱ"],
    "گھ": ["ɡʱ"], "کھ": ["kʰ"], "لھ": ["lʱ"], "مھ": ["mʱ"],
    "نھ": ["nʱ"], "رھ": ["rʱ"], "ڑھ": ["ɽʱ"],

    # --- Nukta (dot below) letters ---
    "ق": ["q"],
}

ALLOPHONES = {
    "p": ["p"], "pʰ": ["pʰ"],
    "b": ["b"], "bʱ": ["bʱ"],
    "t̪": ["t̪"], "t̪ʰ": ["t̪ʰ"],
    "d̪": ["d̪"], "d̪ʱ": ["d̪ʱ"],
    "ʈ": ["ʈ"], "ʈʰ": ["ʈʰ"],
    "ɖ": ["ɖ"], "ɖʱ": ["ɖʱ"],
    "k": ["k"], "kʰ": ["kʰ"],
    "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "q": ["q", "k"],  # /q/ → [k] for less educated speakers
    "tʃ": ["tʃ"], "tʃʰ": ["tʃʰ"],
    "dʒ": ["dʒ"], "dʒʱ": ["dʒʱ"],
    "f": ["f", "pʰ"],  # /f/ → [pʰ] for speakers without labiodentals
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ", "ʃ"],
    "x": ["x"], "ɣ": ["ɣ", "ɡ"],
    "ɦ": ["ɦ", "h"],
    "h": ["h"],
    "m": ["m"], "n": ["n"],
    "ɽ": ["ɽ"], "r": ["r"],
    "l": ["l"],
    "ʋ": ["ʋ", "w", "v"],
    "j": ["j"],
    # Vowels
    "ə": ["ə"], "aː": ["aː"],
    "ɪ": ["ɪ"], "iː": ["iː"],
    "ʊ": ["ʊ"], "uː": ["uː"],
    "eː": ["eː"], "oː": ["oː"],
}

SPECS = {
    "ur": LanguageSpec(
        code="ur",
        name="Urdu",
        family="Indo-Aryan",
        script="Arabic",  # Nastaliq
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        parent="hi",
        ancestors=(
            Ancestor("hi", P, 0.75,
                     "Hindustani base shared with Hindi (Khaṛī Bolī)"),
            Ancestor("fa", AD, 0.15,
                     "Persian adstrate: massive vocabulary, some phonological influence (/x ɣ q/)"),
            Ancestor("ar", AD, 0.10,
                     "Arabic adstrate: religious/scholarly vocabulary, pharyngeal consonants"),
        ),
        notes=(
            "Standard Urdu (Pakistan national language, Indian Muslim register). "
            "Phonologically near-identical to Hindi but with additional phonemes "
            "from Persian/Arabic loans: /q x ɣ f z/. "
            "Written right-to-left in Nastaliq (a form of Perso-Arabic script). "
            "Four-way laryngeal contrast: plain/aspirated × voiced/voiceless. "
            "Retroflex series: /ʈ ɖ ɽ/ graphically distinct from dentals."
        ),
    ),
}
