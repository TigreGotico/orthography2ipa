"""Mirandese (mwl) — grapheme→IPA and allophone mappings.

Mirandese (Mirandês) is the only Asturleonese language with official legal
recognition in Portugal (Law nº 7/99, 1999). Spoken in the Terra de Miranda,
Bragança district, extreme NE Portugal. ~1,500 regular speakers (2020).

Includes the Sendinês (meridional) subdialect which differs systematically
in diphthong reduction and L-palatalization.

Sources:
- Belina, M. (2016). "Lengua mirandesa: su historia y sistema fonético."
  Universidad de Wrocław.
- Frías Conde, X. & Quarteu, R. (2002). "L mirandés: ũa lhéngua
  minoritaira an Pertual." Ianua 2: 89–105.
- Cumbençon Ourtográfica da Lhéngua Mirandesa (1999, rev. 2000).
- Ferreira, M.B. (1999). "Lição de mirandês."
- Merlan, A. (2009). El mirandés: situación sociolingüística.

Conventions:
- ISO 639-3: mwl (Mirandese).
- Orthography follows the Cumbençon Ourtográfica (1999).
- 22 consonant phonemes, 7 oral + 5 nasal vowels, 18 diphthongs.
- Key features: L-palatalization (lh- initial), betacism, 4-way sibilant
  system (/s z ɕ ʑ/), Leonese diphthongs (-iê- [je], -uô- [wo]),
  initial ei- diphthongization, -ōnis → -on [õ].
"""
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# Central Mirandese (standard / normative)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_MWL = {
    # --- Single vowels ---
    "a": ["a", "ɐ"],
    "e": ["e", "ɛ"],
    "i": ["i"],
    "o": ["o", "ɔ"],
    "u": ["u"],

    # --- Accented vowels ---
    "á": ["a"],
    "â": ["ɐ"],
    "é": ["ɛ"],
    "ê": ["e"],
    "í": ["i"],
    "ó": ["ɔ"],
    "ô": ["o"],
    "ú": ["u"],

    # --- Nasal vowels (written with n/m in coda) ---
    # The unique nasal centralised anterior vowel /ɨ̃/ in unstressed
    # syllables closed by n/m: bendima [bɨ̃ˈðimɐ], sembrado [sɨ̃ˈβɾaðu]
    "ã": ["ɐ̃"],
    "õ": ["õ"],

    # --- Single consonants ---
    "b": ["b"],  # covers all historical /b/ AND /v/ (betacism)
    "c": ["k", "s"],  # /k/ before a,o,u; /s/ before e,i
    "ç": ["s"],  # voiceless dental sibilant
    "d": ["d"],
    "f": ["f"],
    "g": ["ɡ", "ʒ"],
    "h": [""],  # silent
    "j": ["ʒ"],
    "k": ["k"],
    "l": ["l", "ɫ"],  # clear/dark
    "m": ["m"],
    "n": ["n"],
    "p": ["p"],
    "q": ["k"],
    "r": ["r", "ɾ"],  # trill initial/geminate; tap intervocalic
    "s": ["ɕ", "ʑ", "s", "z"],  # 4-way sibilant: ⟨s⟩ = /ɕ/ or /ʑ/ (apico-dental pair)
    "t": ["t"],
    "v": ["b"],  # betacism: no /v/ phoneme
    "x": ["ʃ"],
    "z": ["z", "ʑ"],  # dental voiced / alveolar-palatal voiced

    # --- Consonant digraphs ---
    "ch": ["tʃ"],  # affricate (from PL-, CL-, FL- clusters)
    "lh": ["ʎ"],  # palatal lateral — from L- initial AND -LL-
    "nh": ["ɲ"],  # palatal nasal — from -NN-
    "rr": ["r"],  # alveolar trill
    "ss": ["s"],  # voiceless dental
    "qu": ["k", "kw"],
    "gu": ["ɡ", "ɡw"],

    # --- Leonese diphthongs (hallmark feature) ---
    # From Latin short Ĕ → iê [je]
    "iê": ["je"],  # piêdra, siête, biêlho, fiêrro
    # From Latin short Ŏ → uô [wo]
    "uô": ["wo"],  # puôrta, ruôda, fuôro, cuôrpo

    # --- Initial ei- diphthongization (unique to Mirandese) ---
    "ei": ["ej"],  # eibangelho, eisemplo, eimigrar

    # --- Other oral diphthongs ---
    "ai": ["aj"],
    "au": ["aw"],
    "eu": ["ew"],
    "iu": ["iw"],
    "oi": ["oj"],
    "ou": ["ow"],
    "ui": ["uj"],

    # --- Nasal endings ---
    # -ōnis → -on [õ] (unique peninsular feature per Belina 2016)
    "on": ["õ"],  # lhion, peixon, naçon
    "ão": ["ɐ̃w̃"],  # (in Portuguese-contact words)
}

ALLOPHONES_MWL = {
    # Plosives
    "p": ["p"],
    "b": ["b", "β"],  # spirantised intervocalic (Leonese pattern)
    "t": ["t"],
    "d": ["d", "ð"],  # spirantised intervocalic
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],  # spirantised intervocalic

    # Fricatives — the distinctive 4-way sibilant system
    "f": ["f"],
    "s": ["s"],  # voiceless dental (⟨c⟩ before e/i, ⟨ç⟩)
    "z": ["z"],  # voiced dental (⟨z⟩)
    "ɕ": ["ɕ"],  # voiceless alveolar-palatal (⟨s⟩ initial, after C, coda)
    "ʑ": ["ʑ"],  # voiced alveolar-palatal (⟨s⟩ intervocalic, before voiced C)
    "ʃ": ["ʃ"],  # voiceless postalveolar
    "ʒ": ["ʒ"],  # voiced postalveolar

    # Affricate
    "tʃ": ["tʃ"],  # from PL-, CL-, FL- (chamar [tʃɐˈmaɾ])

    # Rhotics
    "r": ["r"],  # alveolar trill (initial, rr)
    "ɾ": ["ɾ"],  # alveolar tap (intervocalic, clusters)

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],  # [ŋ] before velars
    "ɲ": ["ɲ"],  # from Latin -NN-

    # Laterals
    "l": ["l"],
    "ɫ": ["ɫ"],  # velarised in coda
    "ʎ": ["ʎ"],  # from Latin L- initial AND -LL-

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
    "ɨ": ["ɨ"],  # centralised, unstressed

    # Nasal vowels
    "ɐ̃": ["ɐ̃"],
    "ɨ̃": ["ɨ̃"],  # unique Mirandese: unstressed before n/m
    "ẽ": ["ẽ"],
    "ĩ": ["ĩ"],
    "õ": ["õ"],
    "ũ": ["ũ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Sendinês (meridional subdialect)
# Key differences: monophthongization of -iê-/-uô-, NO L-palatalization
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_MWL_SENDIM = {
    **GRAPHEMES_MWL,
    # Diphthongs reduce to simple vowels in Sendinês
    "ie": ["i"],  # tirra (= tiêrra), not [je]
    "uo": ["u"],  # curpo (= cuôrpo), not [wo]
    # Override the standard diphthong entries
    "iê": ["i"],  # monophthongised
    "uô": ["u"],  # monophthongised
}

ALLOPHONES_MWL_SENDIM = {
    **ALLOPHONES_MWL,
    # No L-palatalization: lh- initial → [l] not [ʎ]
    # (luna not lhuna, lobo not lhobu)
    # This is captured in notes; grapheme ⟨l⟩ rather than ⟨lh⟩ used in Sendinês
}

# ═══════════════════════════════════════════════════════════════════════════
# Specs
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "mwl": LanguageSpec(
        code="mwl",
        name="Mirandese",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_MWL,
        allophones=ALLOPHONES_MWL,
        parent="la",
        notes=(
            "Central Mirandese (standard normative variety). Asturleonese "
            "language, official in Portugal since 1999 (Law 7/99). ~1,500 "
            "regular speakers. Key features: L-palatalization (Latin L- → [ʎ], "
            "written ⟨lh-⟩), betacism (/v/→[b]), unique 4-way sibilant system "
            "(/s z ɕ ʑ/ — only on Iberian Peninsula), Leonese diphthongs "
            "(Lat. Ĕ → [je] ⟨-iê-⟩, Lat. Ŏ → [wo] ⟨-uô-⟩), initial ei- "
            "diphthongization (eibangelho, eisemplo — unique to Mirandese), "
            "-ōnis → -on [õ] (nasal ending distinct from both Pt. -ão and "
            "Sp. -ón). Conjugated infinitive borrowed from Portuguese contact. "
            "Orthography: Cumbençon Ourtográfica da Lhéngua Mirandesa (1999)."
        ),
    ),
    "mwl-x-sendim": LanguageSpec(
        code="mwl-x-sendim",
        name="Sendinês (Mirandese meridional)",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_MWL_SENDIM,
        allophones=ALLOPHONES_MWL_SENDIM,
        parent="mwl",
        notes=(
            "Sendinês subdialect of Mirandese, spoken in Vila de Sendim "
            "(southern extreme of Terra de Miranda). Differs from central "
            "Mirandese in: (1) monophthongization of -iê- → -i- and "
            "-uô- → -u- (tirra not tiêrra, curpo not cuôrpo); "
            "(2) NO palatalization of initial L- (luna not lhuna, lobo not "
            "lhobu). Orthographic addendum (2000) reflects these differences. "
            "Written ⟨-ie-⟩ and ⟨-uo-⟩ instead of ⟨-iê-⟩ and ⟨-uô-⟩."
        ),
    ),
}
