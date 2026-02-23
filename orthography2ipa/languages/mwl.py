"""Mirandese (mwl) — grapheme→IPA and allophone mappings.

Mirandese (Mirandês) is the only Asturleonese language with official legal
recognition in Portugal (Law nº 7/99, 1999). Spoken in the Terra de Miranda,
Bragança district, extreme NE Portugal. ~1,500 regular speakers (2020).

Genealogy: Latin → Hispanic Vulgar Latin → Asturleonese → (Leonese branch) →
           Mirandese.

Includes the Sendinês (meridional) subdialect which differs systematically
in diphthong reduction and L-palatalization.

Sources:
- Cumbençon Ourtográfica da Lhéngua Mirandesa (1999, rev. 2000).
  Câmara Municipal de Miranda do Douro / Centro de Linguística da
  Universidade de Lisboa. — PRIMARY ORTHOGRAPHIC AUTHORITY.
- Ferreira, M.B. & Raposo, D. (1999). "Convenção Ortográfica da
  Língua Mirandesa." Centro de Linguística da Universidade de Lisboa.
- Belina, M. (2016). "Lengua mirandesa: su historia y sistema fonético."
  Universidad de Wrocław.
- Frías Conde, X. & Quarteu, R. (2002). "L mirandés: ũa lhéngua
  minoritaira an Pertual." Ianua 2: 89–105.
- Merlan, A. (2009). El mirandés: situación sociolingüística.
- Vasconcellos, J.L. de (1900). Estudos de Philologia Mirandesa, vols. I–II.

Sibilant system (4-way contrast, unique to NE Iberian Peninsula):
  The Convenção (p.16) and Atlas Linguistique Roman describe four sibilants:
  - Apical voiceless [s̺] — ⟨s⟩ (initial, after C, coda before voiceless C),
    ⟨ss⟩ (intervocalic). Tongue tip raised toward alveolar ridge.
  - Apical voiced [z̺] — ⟨s⟩ (intervocalic, before voiced C).
    Same articulation, voiced.
  - Predorsal voiceless [s̻] — ⟨ç⟩, ⟨c⟩ before e/i.
    Tongue blade against upper teeth (dental/laminal).
  - Predorsal voiced [z̻] — ⟨z⟩.
    Same articulation, voiced.
  This apical/predorsal contrast is shared with NE Portuguese dialects,
  Trás-os-Montes, parts of Minho, and Beira Alta.

Conventions:
- ISO 639-3: mwl (Mirandese).
- Orthography follows the Cumbençon Ourtográfica (1999).
- 22 consonant phonemes, 7 oral + 5 nasal vowels, 18+ diphthongs.
- Key features: L-palatalization (lh- initial), betacism, 4-way sibilant
  system (/s̺ z̺ s̻ z̻/), Leonese diphthongs (-iê- [je], -uô- [wo]),
  initial ei- diphthongization, -ōnis → -on [õ].
"""
from orthography2ipa.types import (
    Ancestor, AncestorRole, LanguageSpec, GraphemePosition as GP,
)

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# Central Mirandese (standard / normative)
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_MWL = {
    # ── Single vowels ─────────────────────────────────────────────────────
    # Convenção p.9, p.13: ⟨a⟩ = [a] open in stressed oral syllable,
    # [ɐ] closed in unstressed positions.
    "a": ["a", "ɐ"],
    # Convenção p.9, p.14: ⟨e⟩ = [ɛ] open (accented), [e] closed,
    # [ɨ] reduced in unstressed (intermediate timbre, noted in footnote 1).
    "e": ["ɛ", "e", "ɨ"],
    "i": ["i"],
    # Convenção p.10, p.15: ⟨o⟩ = [ɔ] open, [o] closed,
    # [u] reduced in unstressed pretonic/final positions.
    "o": ["ɔ", "o", "u"],
    "u": ["u"],

    # ── Accented vowels (accent marks disambiguate quality) ───────────────
    # Convenção p.20: acute = open quality, circumflex = non-open.
    "á": ["a"],       # stressed open a
    "â": ["ɐ"],       # (used in ã-based forms only)
    "é": ["ɛ"],       # stressed open e (sé, précio, mês)
    "ê": ["e"],       # stressed closed e (abiês, pra)
    "í": ["i"],       # stressed i
    "ó": ["ɔ"],       # stressed open o (abó, bóbida)
    "ô": ["o"],       # stressed closed o (in diphthongs uô)
    "ú": ["u"],       # stressed u

    # ── Tilde vowels (nasal) ──────────────────────────────────────────────
    # Convenção p.19: tilde marks nasal u in hiatus (ũa = indefinite article)
    "ã": ["ɐ̃"],
    "õ": ["õ"],
    "ũ": ["ũ"],       # ũa (indefinite article feminine), alg̃ua

    # ── Single consonants ─────────────────────────────────────────────────
    # Convenção p.9–11, p.13–17.
    "b": ["b"],       # Convenção p.13: occlusive initial/post-nasal,
                      #   fricative [β] intervocalic and post-sonorant
    "c": ["k", "s̻"],  # Convenção p.13: [k] before a,o,u; predorsal [s̻]
                      #   before e,i (cebada, ciêgo)
    "ç": ["s̻"],      # Convenção p.13: predorsal voiceless sibilant.
                      #   Before voiced C in phrase: voices to [z̻].
    "d": ["d"],       # Convenção p.14: occlusive initial/post-nasal/post-l,
                      #   fricative [ð] intervocalic
    "f": ["f"],       # Convenção p.14: no difference from other Romance
    "g": ["ɡ", "ʒ"],  # Convenção p.14: [ɡ] before a,o,u (occlusive initial,
                      #   fricative [ɣ] intervocalic); [ʒ] before e,i
    "h": [""],        # Convenção p.14: silent; etymological h kept in most
                      #   cases (haber, home, hoije). Part of digraphs ch,lh,nh.
    "j": ["ʒ"],      # Convenção p.14: palatal voiced [ʒ] before a,o,u
                      #   (Janeiro). Also before e,i by etymology (arranjo).
    "k": ["k"],       # Convenção p.11: foreign words only (Kg, Km)
    "l": ["l", "ɫ"],  # Convenção p.15: clear onset, velarised coda.
                      #   Article ⟨l⟩ before C = velarised syllabic [ɫ̩].
    "m": ["m"],       # Convenção p.15: also nasality marker before p,b
    "n": ["n"],       # Convenção p.15: also nasality marker elsewhere.
                      #   Word-final n marks nasal vowel (coraçon, melon).
    "p": ["p"],
    "q": ["k"],       # Always followed by u; see digraph ⟨qu⟩
    "r": ["r", "ɾ"],  # Convenção p.16: trill [r] initial and ⟨rr⟩;
                      #   tap [ɾ] intervocalic, clusters, coda
    "s": ["s̺", "z̺"],  # Convenção p.16: APICAL sibilants. [s̺] voiceless
                      #   (initial, after C, coda before voiceless C, ⟨ss⟩).
                      #   [z̺] voiced (intervocalic, before voiced C).
    "t": ["t"],
    "v": ["b"],       # Convenção p.17: betacism. /v/ does not exist in
                      #   Mirandese. Proper nouns keep ⟨v⟩ per Portuguese norms.
    "w": ["w", "b"],  # Convenção p.11: foreign words (whisky, KW, Wagner)
    "x": ["ʃ"],      # Convenção p.17: voiceless postalveolar [ʃ] (xastre, xordo)
    "y": ["j"],       # Convenção p.17: semivowel [j], sometimes slightly
                      #   fricativised. Medieval Leonese tradition.
                      #   (yê, you, yá, yêuga, yêrba, yêrbo)
    "z": ["z̻"],      # Convenção p.17: predorsal voiced sibilant.
                      #   Corresponds to Portuguese ⟨z⟩ (cozer batatas).
                      #   Not used word-finally; only initial, intervocalic,
                      #   or before voiced C.

    # ── Consonant digraphs ────────────────────────────────────────────────
    # Convenção p.11, p.13–15.
    "ch": ["tʃ"],    # Convenção p.13: palatal affricate [tʃ], from Latin
                      #   PL-, CL-, FL-. Contrasts with ⟨x⟩ [ʃ]:
                      #   bucho ≠ buxo. Preserved in Galiza, Minho, Trás-os-
                      #   Montes, Beira Interior.
    "lh": ["ʎ"],     # Convenção p.15: palatal lateral. From Latin L- initial
                      #   (lheite, lheiteiro) AND -LL- (mulhier). Hallmark
                      #   feature shared with Leonese/Western Asturian.
    "nh": ["ɲ"],     # Convenção p.15: palatal nasal, from Latin -NN-
                      #   (anho ← annum, canha ← canna). Equiv. to Sp. ñ.
    "rr": ["r"],     # Convenção p.16: alveolar trill intervocalic (carro)
    "ss": ["s̺"],    # Convenção p.16: voiceless apical [s̺] intervocalic (passo)
    "qu": ["k", "kw"],  # Convenção p.16: [kw] before a (qual, quatro),
                      #   [k] before e,i (questume, eiqui). Not pronounced
                      #   before e,i (the u is silent).
    "gu": ["ɡ", "ɡw"],  # Convenção p.14: [ɡ] before e,i (guelhada, águila)
                      #   with mute u; [ɡw] = exception (guira, guiron)

    # ── Leonese diphthongs (hallmark feature) ─────────────────────────────
    # Convenção p.18: From Latin short Ĕ and Ŏ.
    # Always marked with circumflex in grave/esdrúxula words.
    "iê": ["je"],    # Latin Ĕ → iê: tiêrra, tiêmpo, piêdra, siête,
                      #   biêlho, fiêrro. Written ⟨-iê-⟩.
    "uô": ["wo"],    # Latin Ŏ → uô: puôrta, ruôda, fuônte, cuôrpo.
                      #   Written ⟨-uô-⟩. Some localities reduce to [o].

    # ── Rising (crescente) diphthongs ─────────────────────────────────────
    # Convenção p.18: also ua (qual, quarto, guapa), ia.
    "ia": ["ja"],
    "ua": ["wa"],     # qual, quatro, guapa

    # ── Falling (decrescente) diphthongs ──────────────────────────────────
    # Convenção p.18–19: comprehensive list from the orthographic convention.
    "ai": ["aj"],     # aire, hai, naide, páixaro
    "au": ["aw"],     # acauso, auga, frauga, calhau
    "ei": ["ej"],     # eigreija, einaugade, nheiro, dreito, perreira,
                      #   queiso, streilha, ancuntreis
    "éu": ["ɛw"],    # chapéu, piléu, mantéu (open e + u)
    "eu": ["ew"],     # lheuga
    "iu": ["iw"],     # Dius, friu, niu, ardiu, miu, morriu, comiu
    "oi": ["oj"],     # hoije, coixo, noijo, cambóio
    "ói": ["ɔj"],    # heiról (open o + i)
    "ou": ["ow"],     # oubelha, ourriêta, boube, bielha, touça, pouco,
                      #   outro, dous, sous, amou
    "ui": ["uj"],     #uite, tentamui, to, nuite, buifo, cuiro, apuis,
                      #   pui, alguira

    # ── Nasal vowel endings (word-final V+n) ──────────────────────────────
    # Convenção p.19: In word-final position, nasal vowels are written V+n.
    # In word-internal position, nasality is indicated by m before p/b,
    # n before other consonants (standard Romance convention).
    # Note: "on" is the most distinctive — from Latin -ōnis → -on [õ],
    # distinct from both Pt. -ão and Sp. -ón.
    # We model these as digraphs for word-final nasal vowels.
    "an": ["ɐ̃"],     # pan, panes
    "en": ["ẽ"],      # ben, cen, nien
    "in": ["ĩ"],      # bin (< vinum), fin
    "on": ["õ"],      # lhion, peixon, naçon, coraçon, melon, freijon
    "un": ["ũ"],      # algũ, comũ

    # ── Nasal diphthongs ──────────────────────────────────────────────────
    "ão": ["ɐ̃w̃"],    # Portuguese-contact words
}

# ═══════════════════════════════════════════════════════════════════════════
# Allophone inventory
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_MWL = {
    # ── Plosives ──────────────────────────────────────────────────────────
    "p": ["p"],
    "b": ["b", "β"],       # spirantised intervocalic/post-sonorant (Leonese)
    "t": ["t"],
    "d": ["d", "ð"],       # spirantised intervocalic
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],       # spirantised intervocalic

    # ── Fricatives — the distinctive 4-way sibilant system ────────────────
    "f": ["f"],
    "s̺": ["s̺"],           # voiceless apical (⟨s⟩ initial, ⟨ss⟩, coda)
    "z̺": ["z̺"],           # voiced apical (⟨s⟩ intervocalic, before voiced C)
    "s̻": ["s̻"],           # voiceless predorsal/dental (⟨ç⟩, ⟨c⟩ before e/i)
    "z̻": ["z̻"],           # voiced predorsal/dental (⟨z⟩)
    "ʃ": ["ʃ"],            # voiceless postalveolar (⟨x⟩)
    "ʒ": ["ʒ"],            # voiced postalveolar (⟨j⟩, ⟨g⟩ before e/i)

    # ── Affricate ─────────────────────────────────────────────────────────
    "tʃ": ["tʃ"],          # from PL-, CL-, FL- (chamar, chubar, chispa)

    # ── Rhotics ───────────────────────────────────────────────────────────
    "r": ["r"],             # alveolar trill (initial, ⟨rr⟩, post-n/l)
    "ɾ": ["ɾ"],            # alveolar tap (intervocalic, clusters, coda)

    # ── Nasals ────────────────────────────────────────────────────────────
    "m": ["m"],
    "n": ["n", "ŋ"],       # [ŋ] before velars
    "ɲ": ["ɲ"],            # from Latin -NN-

    # ── Laterals ──────────────────────────────────────────────────────────
    "l": ["l"],             # clear (onset)
    "ɫ": ["ɫ"],            # velarised (coda); article ⟨l⟩ before C
    "ʎ": ["ʎ"],            # from Latin L- initial AND -LL-

    # ── Glides ────────────────────────────────────────────────────────────
    "w": ["w"],
    "j": ["j"],

    # ── Oral vowels ───────────────────────────────────────────────────────
    "a": ["a"],
    "ɐ": ["ɐ"],
    "e": ["e"],
    "ɛ": ["ɛ"],
    "ɨ": ["ɨ"],            # centralised, unstressed (Convenção footnote 1)
    "i": ["i"],
    "o": ["o"],
    "ɔ": ["ɔ"],
    "u": ["u"],

    # ── Nasal vowels ─────────────────────────────────────────────────────
    "ɐ̃": ["ɐ̃"],
    "ẽ": ["ẽ"],
    "ĩ": ["ĩ"],
    "õ": ["õ"],
    "ũ": ["ũ"],
    "ɨ̃": ["ɨ̃"],           # unique Mirandese: unstressed nasal centralised
                            # (bendima, sembrado — Convenção p.19 note)
}

# ═══════════════════════════════════════════════════════════════════════════
# Positional graphemes
# ═══════════════════════════════════════════════════════════════════════════

POSITIONAL_MWL = {
    # ── Obstruent lenition (shared Ibero-Romance pattern) ─────────────────
    "b": {
        GP.DEFAULT: ["b"],           # initial, post-nasal (buôno, ambeija)
        GP.INTERVOCALIC: ["β"],      # between vowels (abê, cebada)
    },
    "d": {
        GP.DEFAULT: ["d"],           # initial, post-nasal (deimingo), post-l (caldo)
        GP.INTERVOCALIC: ["ð"],      # between vowels (eidade, bida)
    },
    "g": {
        GP.DEFAULT: ["ɡ"],           # initial (gato), post-nasal (pongo)
        GP.INTERVOCALIC: ["ɣ"],      # between vowels (fago, alhargo)
    },
    # ── Rhotics ───────────────────────────────────────────────────────────
    "r": {
        GP.WORD_INITIAL: ["r"],      # trill: rato, ruôda
        GP.INTERVOCALIC: ["ɾ"],      # tap: caro, crecer
        GP.ONSET: ["ɾ"],             # in clusters: drento, berdade
        GP.CODA: ["ɾ"],             # syllable-final: cardo, cantar
    },
    # ── Laterals ──────────────────────────────────────────────────────────
    "l": {
        GP.ONSET: ["l"],             # clear: salir, maquila, ciêlo
        GP.CODA: ["ɫ"],             # velarised: calcaldo, Manuel, l perro
                                     # (article ⟨l⟩ before C → syllabic [ɫ̩])
    },
    # ── Nasals ────────────────────────────────────────────────────────────
    "n": {
        GP.DEFAULT: ["n"],           # onset: naide, ganado
        GP.CODA: ["n", "ŋ"],       # before velars: [ŋ]; otherwise [n]
    },
    # ── Apical sibilant ⟨s⟩ ──────────────────────────────────────────────
    # Convenção p.16–17: ⟨s⟩ is voiceless [s̺] before voiceless C and
    # word-initially; voiced [z̺] intervocalically and before voiced C.
    "s": {
        GP.WORD_INITIAL: ["s̺"],     # saber, screber (also s before C)
        GP.INTERVOCALIC: ["z̺"],     # coser, amisa (= voiced apical)
        GP.CODA: ["s̺", "z̺"],      # [s̺] before voiceless C (fiêsta, triste);
                                     # [z̺] before voiced C (mesmo, cismar)
    },
}

# ═══════════════════════════════════════════════════════════════════════════
# Sendinês (meridional subdialect)
# Key differences: monophthongization of -iê-/-uô-, NO L-palatalization.
# Convenção p.18, footnote 7: In Sendim, [je] → [i] and [wo] → [u].
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_MWL_SENDIM = {
    **GRAPHEMES_MWL,
    # Diphthongs reduce to simple vowels in Sendinês
    "ie": ["i"],      # tirra (= tiêrra), not [je]
    "uo": ["u"],      # curpo (= cuôrpo), not [wo]
    # Override the standard diphthong entries
    "iê": ["i"],      # monophthongised
    "uô": ["u"],      # monophthongised
}

ALLOPHONES_MWL_SENDIM = {
    **ALLOPHONES_MWL,
    # No L-palatalization: lh- initial → [l] not [ʎ]
    # (luna not lhuna, lobo not lhobu)
    # This is captured in notes; grapheme ⟨l⟩ rather than ⟨lh⟩ used in Sendinês
}

# ═══════════════════════════════════════════════════════════════════════════
# Ifanês (Ifanes subdialect — mentioned in Convenção footnotes)
# Key differences: [je] → [e], [wo] sporadic, post-palatal [j] semivowel
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_MWL_IFANES = {
    **GRAPHEMES_MWL,
    # Convenção p.18 footnote 7: In Ifanes, [je] reduces to [e]
    "iê": ["e"],      # monophthongised to [e] (not [i] like Sendim)
    "uô": ["wo"],     # retained but sporadic
}

ALLOPHONES_MWL_IFANES = {
    **ALLOPHONES_MWL,
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
        positional_graphemes=POSITIONAL_MWL,
        parent="ast-ES-x-leon",
        ancestors=(
            Ancestor("ast-ES-x-leon", P, 0.75,
                     "Primary descent from the Leonese branch of Asturleonese. "
                     "Mirandese is the easternmost Leonese variety, isolated "
                     "in NE Portugal since the medieval period."),
            Ancestor("cel", SUB, 0.04,
                     "Celtic (Astures) substrate: Terra de Miranda was within "
                     "the ancient Astures territory; some toponymy."),
            Ancestor("xaq", SUB, 0.02,
                     "Proto-Basque substrate: minimal but present via "
                     "pre-Roman NW Iberian connections."),
            Ancestor("got", SUP, 0.02,
                     "Visigothic superstrate: Kingdom of León heritage."),
            Ancestor("xaa", AD, 0.02,
                     "Arabic adstrate: minimal — NE Portugal was reconquered "
                     "early; some lexical items."),
            Ancestor("pt-PT", AD, 0.10,
                     "Portuguese adstrate: strong ongoing contact language. "
                     "Conjugated infinitive borrowed from Portuguese. "
                     "Diglossia situation since at least 19th century."),
        ),
        notes=(
            "Central Mirandese (standard normative variety). Asturleonese "
            "language, official in Portugal since 1999 (Law 7/99). ~1,500 "
            "regular speakers. Key features: L-palatalization (Latin L- → [ʎ], "
            "written ⟨lh-⟩), betacism (/v/→[b]), unique 4-way sibilant system "
            "(/s̺ z̺ s̻ z̻/ — apical vs predorsal contrast, shared with NE "
            "Portuguese dialects), Leonese diphthongs (Lat. Ĕ → [je] ⟨-iê-⟩, "
            "Lat. Ŏ → [wo] ⟨-uô-⟩), initial ei- diphthongization (eibangelho, "
            "eisemplo — unique to Mirandese), -ōnis → -on [õ] (nasal ending "
            "distinct from both Pt. -ão and Sp. -ón). Maintenance of Latin "
            "intervocalic -l- and -n- (salir, cheno — unlike Pt. sair, cheio). "
            "Conjugated infinitive borrowed from Portuguese contact. "
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
        positional_graphemes=POSITIONAL_MWL,
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
    "mwl-x-ifanes": LanguageSpec(
        code="mwl-x-ifanes",
        name="Ifanês (Mirandese septentrional)",
        family="Asturleonese",
        script="Latin",
        graphemes=GRAPHEMES_MWL_IFANES,
        allophones=ALLOPHONES_MWL_IFANES,
        positional_graphemes=POSITIONAL_MWL,
        parent="mwl",
        notes=(
            "Ifanês subdialect of Mirandese, spoken in Ifanes (Infantes) "
            "in the northern part of Terra de Miranda. Differs from central "
            "Mirandese in: (1) monophthongization of -iê- → -e- (not -i- "
            "like Sendinês); (2) -uô- is sporadic, not systematically "
            "reduced. Noted in Convenção footnote 7 and Vasconcellos (1900)."
        ),
    ),
}