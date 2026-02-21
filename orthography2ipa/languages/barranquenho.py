"""Barranquenho (ext-PT-x-barrancos) — grapheme→IPA and allophone mappings.

A contact language spoken in Barrancos, Alentejo, Portugal, arising from
prolonged contact between southern Portuguese (Alentejano), Extremaduran,
and Andalusian Spanish. Recognised by Portuguese law (Lei nº 97/2021).

Sources:
- Gramática Básica de Barranquenho (2025). U. Évora / UNESCO Chair.
- Convenção Ortográfica do Barranquenho (2025). U. Évora / UNESCO Chair.
- Dicionário de Barranquenho (2025). U. Évora / UNESCO Chair.
- Gonçalves, M.F. / Navas, M.V. (2021). *O barranquenho como língua de
  contacto no contexto românico*. Lisboa: Colibri.
- Leite de Vasconcelos, J. (1901, 1955). Studies on Barranquenho.

Conventions:
- Code ext-PT-x-barrancos: ext = Extremaduran (closest macro-classification
  for this Iberian border contact variety), PT = Portugal, x-barrancos =
  private-use subtag for Barrancos locality.
- Orthography follows the 2025 Convenção Ortográfica do Barranquenho.
- Key distinctive features: betacism (/v/→/b/), sibilant aspiration
  (/s/→[h] in coda), loss of final /-l/ and /-ɾ/, diphthong
  monophthongization (/ej/→[e], /ow/→[o]), unstressed final [ɐ̃w̃]→[õ].
"""
from orthography2ipa.types import LanguageSpec, GraphemePosition as GP

GRAPHEMES_BRQ = {
    # --- Single vowels ---
    "a": ["a", "ɐ"],
    "e": ["e", "ɛ", "ɨ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],

    # --- Accented vowels (distinctive Barranquenho usage) ---
    "á": ["a"],  # stressed open (often marks deleted final -l/-r)
    "à": ["a"],  # contraction or pre-deleted liquid
    "â": ["ɐ"],
    "ã": ["ɐ̃"],
    "é": ["ɛ"],  # open-mid (often marks deleted final -l: amabè)
    "ê": ["e"],  # close-mid (from monophthongized /ej/ or /ow/)
    "í": ["i"],
    "ó": ["ɔ"],  # open-mid (marks deleted -l: ehpanhó)
    "ô": ["o"],  # close-mid (from monophthongized /ow/: dotô)
    "õ": ["õ"],
    "ú": ["u"],
    "è": ["ɛ"],  # pre-deleted liquid marker

    # --- Single consonants ---
    "b": ["b"],  # covers all historical /b/ AND /v/ (betacism)
    "c": ["k", "s"],  # /k/ before a,o,u; /s/ before e,i
    "ç": ["s"],
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "ʒ"],  # /ɡ/ before a,o,u; /ʒ/ before e,i
    "h": ["h", "x", ""],  # [h] aspiration of coda /s/; [x] in Sp. loans; silent etymological
    "j": ["ʒ"],
    "k": ["k"],
    "l": ["l"],  # NB: deleted in word-final stressed syllables
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["ʁ", "ɾ", "r"],  # uvular/trill initial; tap intervocalic
    "s": ["s", "z", "h"],  # [h] in coda before C (aspiration); [z] intervocalic
    "t": ["t"],
    "v": ["b"],  # betacism: ⟨v⟩ only in imported toponyms
    "w": ["w"],
    "x": ["ʃ", "ks", "z", "s"],
    "y": ["j"],
    "z": ["z"],

    # --- Consonant digraphs ---
    "ch": ["ʃ"],
    "lh": ["ʎ"],
    "nh": ["ɲ"],
    "rr": ["ʁ", "r"],  # uvular or alveolar trill
    "ss": ["s"],
    "tch": ["tʃ"],  # affricate (Spanish loans: catchondeu)
    "qu": ["k", "kw"],
    "gu": ["ɡ", "ɡw"],
    "gü": ["ɡw"],  # explicit labiovelar (güe, güi)

    # --- Oral diphthongs (reduced set due to monophthongization) ---
    # /ej/ → [e] and /ow/ → [o] are systematic — represented by ⟨ê⟩ and ⟨ô⟩
    "ai": ["aj"],
    "au": ["aw"],
    "eu": ["ew"],
    "iu": ["iw"],
    "oi": ["oj"],
    "ui": ["uj"],
    # NB: ⟨ei⟩ and ⟨ou⟩ do NOT appear in native Barranquenho — they
    # monophthongize to ⟨ê⟩ and ⟨ô⟩ respectively.

    # --- Nasal diphthongs ---
    "ãu": ["ɐ̃w̃"],  # stressed final: fejãu, sãu
    "ãi": ["ɐ̃j̃"],  # mãi, pãi
    "õi": ["õj̃"],  # patrõi, liçõi
    "eãu": ["jɐ̃w̃"],  # leãu (triphthong)

    # --- Unstressed final nasal reduction ---
    # Written ⟨-on⟩: canton, eron, ehtabon — phonemically [õ]
    "on": ["õ"],  # in word-final unstressed position
}

ALLOPHONES_BRQ = {
    # Plosives
    "p": ["p"],
    "b": ["b", "β"],  # [β] intervocalic in rapid speech (Spanish-like)
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "ɡ": ["ɡ"],

    # Fricatives
    "f": ["f"],
    "s": ["s", "h"],  # [h] in coda before C (sibilant aspiration)
    "z": ["z"],
    "ʃ": ["ʃ"],
    "ʒ": ["ʒ"],
    "h": ["h"],  # aspiration product of coda /s/
    "x": ["x"],  # marginal: Spanish loan phoneme

    # Affricate
    "tʃ": ["tʃ"],  # Spanish loans only

    # Rhotics
    "ʁ": ["ʁ", "r"],  # uvular (most speakers) or alveolar trill (rural)
    "ɾ": ["ɾ"],  # NB: deleted in word-final stressed position

    # Nasals
    "m": ["m"],
    "n": ["n"],
    "ɲ": ["ɲ"],

    # Laterals
    "l": ["l"],  # NB: deleted in word-final stressed position
    "ʎ": ["ʎ"],

    # Glides
    "w": ["w"],
    "j": ["j"],

    # Monophthongs
    "a": ["a"],
    "ɐ": ["ɐ"],
    "e": ["e"],
    "ɛ": ["ɛ"],
    "ɨ": ["ɨ"],
    "i": ["i"],
    "o": ["o"],
    "ɔ": ["ɔ"],
    "u": ["u"],

    # Nasal vowels
    "ɐ̃": ["ɐ̃"],
    "ẽ": ["ẽ"],
    "ĩ": ["ĩ"],
    "õ": ["õ"],
    "ũ": ["ũ"],
}

POSITIONAL_BARRANQUENHO = {
    "s": {
        GP.WORD_INITIAL: ["s"],
        GP.INTERVOCALIC: ["z"],  # Portuguese-like voicing
        GP.CODA: ["h", "ʃ"],  # Spanish aspiration + Portuguese palatalisation
        GP.WORD_FINAL: ["h", "ʃ"],
    },
    "b": {
        GP.DEFAULT: ["b"],
        GP.INTERVOCALIC: ["β"],
    },
    "d": {
        GP.DEFAULT: ["d"],
        GP.INTERVOCALIC: ["ð"],
        GP.WORD_FINAL: ["ð", "∅"],
    },
    "g": {
        GP.DEFAULT: ["ɡ"],
        GP.INTERVOCALIC: ["ɣ"],
    },
    "r": {
        GP.WORD_INITIAL: ["r"],
        GP.INTERVOCALIC: ["ɾ"],
        GP.CODA: ["ɾ"],
    },
    "l": {
        GP.ONSET: ["l"],
        GP.CODA: ["l", "ɫ"],
    },
}

SPECS = {
    "ext-PT-x-barrancos": LanguageSpec(
        code="ext-PT-x-barrancos",
        name="Barranquenho",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_BRQ,
        allophones=ALLOPHONES_BRQ,
        positional_graphemes=POSITIONAL_BARRANQUENHO,
        parent="ext",
        notes=(
            "Contact language of Barrancos, Portugal (Lei nº 97/2021). "
            "Portuguese-based phonology with Extremaduran/Andalusian features: "
            "betacism (/v/→[b]), sibilant aspiration (/s/→[h] in coda), "
            "loss of final /-l/ and /-ɾ/ in stressed syllables, "
            "monophthongization of /ej/→[e] and /ow/→[o], "
            "unstressed final [ɐ̃w̃]→[õ] (-on ending), "
            "marginal /tʃ/ and /x/ from Spanish loans. "
            "Orthography per Convenção Ortográfica do Barranquenho (2025)."
        ),
    ),
}
