"""Guadramilês (ast-PT-x-guadramil) — grapheme→IPA and allophone mappings.

Guadramilês is a nearly extinct Leonese dialect spoken in Guadramil, Bragança
district, northeastern Portugal. ~0–5 active speakers. Deeper inside
Portuguese territory than Rionorês, giving it stronger Portuguese influence.

Sources:
- Single oral testimony of traditional wedding customs, transcribed using
  Portuguese orthographic conventions (no standardised writing system exists).
- Comparative analysis with Rionorês (Macias 2003) and Mirandese (Belina
  2016, Frías Conde & Quarteu 2002).

Conventions:
- Code ast-PT-x-guadramil: ast = Asturleonese, PT = Portugal,
  x-guadramil = private-use subtag for Guadramil locality.
- Orthography follows Portuguese conventions as no standard exists.
- IPA reconstructed from comparative Leonese phonology.
- Key features: betacism, L-palatalization (lhuna), Leonese diphthongs
  (fiesta, almuorço), imperfect -aba, 3pl -n, negator nun, pronoun you.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES_GUAD = {
    # --- Single vowels ---
    "a": ["a", "ɐ"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],

    # --- Accented vowels ---
    "á": ["a"],
    "é": ["ɛ"],
    "ê": ["e"],
    "í": ["i"],
    "ó": ["ɔ"],
    "ô": ["o"],
    "ú": ["u"],

    # --- Single consonants ---
    "b": ["b"],  # betacism: all /b/ and /v/
    "c": ["k", "s"],
    "ç": ["s", "θ"],  # diç [diθ] or [dis] — unclear
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "ʒ"],
    "h": [""],  # silent
    "j": ["ʒ"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["r", "ɾ"],
    "s": ["s", "z"],
    "t": ["t"],
    "v": ["b"],  # betacism
    "x": ["ʃ"],
    "z": ["z", "θ"],  # word-final -ç/-z may be [θ] (Leonese trace)

    # --- Consonant digraphs ---
    "ch": ["ʃ"],  # NB: Guadramilês lost the affricate [tʃ] (unlike Rionorês)
    "lh": ["ʎ"],  # L-palatalization: lhuna (lua)
    "nh": ["ɲ"],
    "rr": ["r"],
    "ss": ["s"],
    "qu": ["k", "kw"],
    "gu": ["ɡ", "ɡw"],

    # --- Leonese diphthongs ---
    # Ĕ → ie [je]
    "ie": ["je"],  # fiesta, iéran, mientras
    "iê": ["je"],
    # Ŏ → uo [wo]
    "uo": ["wo"],  # almuorço, uolho
    "uô": ["wo"],

    # --- Falling diphthongs ---
    "ai": ["aj"],  # baile
    "au": ["aw"],
    "ei": ["ej"],  # eili
    "iu": ["ju"],
    "oi": ["oj"],  # noibo, noiba
    "ou": ["ow"],  # you [jow], outra
    "ui": ["uj"],

    # --- Nasal patterns ---
    # Oral V + nasal C (pan, bin, una) rather than Portuguese nasal diphthongs
    "ão": ["aw"],  # heavily Portuguese-influenced forms only
    "ãe": ["aj"],
}

ALLOPHONES_GUAD = {
    # Plosives
    "p": ["p"],
    "b": ["b", "β"],
    "t": ["t"],
    "d": ["d", "ð"],
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],

    # Fricatives
    "f": ["f"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],
    "ʒ": ["ʒ"],
    "θ": ["θ"],  # tentative: word-final -ç (diç)

    # Rhotics
    "r": ["r"],
    "ɾ": ["ɾ"],

    # Nasals
    "m": ["m"],
    "n": ["n"],
    "ɲ": ["ɲ"],

    # Laterals
    "l": ["l"],
    "ʎ": ["ʎ"],  # from L-initial palatalization

    # Glides
    "w": ["w"],
    "j": ["j"],

    # Oral vowels
    "a": ["a"],
    "ɐ": ["ɐ"],
    "e": ["e"],
    "ɛ": ["ɛ"],
    "i": ["i"],
    "o": ["o"],
    "ɔ": ["ɔ"],
    "u": ["u"],

    # Nasal vowels (less systematic, tendency toward oral V + nasal C)
    "ɐ̃": ["ɐ̃"],
    "ẽ": ["ẽ"],
    "ĩ": ["ĩ"],
    "õ": ["õ"],
    "ũ": ["ũ"],
}

SPECS = {
    "ast-PT-x-guadramil": LanguageSpec(
        code="ast-PT-x-guadramil",
        name="Guadramilês",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_GUAD,
        allophones=ALLOPHONES_GUAD,
        parent="ast",
        notes=(
            "Nearly extinct Leonese dialect of Guadramil, Bragança. ~0–5 "
            "active speakers. Deeper inside Portuguese territory than "
            "Rionorês, with stronger Portuguese lexical influence. "
            "Key features: betacism (/v/→[b]), L-palatalization (lhuna), "
            "Leonese diphthongs (Ĕ → [je] fiesta, Ŏ → [wo] almuorço), "
            "imperfect -aba/-ában (not -ava/-avam), 3pl marker -n (stában, "
            "fazíen, dezíen, iéran), negator nun/num, pronoun you [jow] "
            "(1sg), Leonese article la (fem.), preposition cun (com), "
            "haber as existential (habia), tener for possession (tenia). "
            "Lost the affricate [tʃ] (chamar [ʃ], unlike Rionorês tchamar "
            "[tʃ]). Uses Portuguese masc. article o (not Leonese al/l). "
            "Possible [θ] for word-final -ç (diç 'diz'). "
            "Based on single oral testimony; no standard orthography. "
            "IPA is reconstructed from comparative Leonese phonology."
        ),
    ),
}
