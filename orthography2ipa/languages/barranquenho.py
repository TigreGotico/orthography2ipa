"""Barranquenho (ext-PT-x-barrancos) — grapheme→IPA and allophone mappings.

A contact language spoken in Barrancos, Alentejo, Portugal, arising from
prolonged contact between southern Portuguese (Alentejano), Extremaduran,
and Andalusian Spanish. Recognised by Portuguese law (Lei nº 97/2021).

Sources:
- Convenção Ortográfica do Barranquenho (2025). M.F. Gonçalves, M.V. Navas,
  V.M.D. Correia. Universidade de Évora. ISBN 978-972-778-463-9.
- Gonçalves, M.F. / Navas, M.V. (eds.) (2021). *O barranquenho como língua
  de contacto no contexto românico*. Lisboa: Colibri.
- Navas, M.V. (1992). "El Barranqueño: un modelo de lenguas en contacto".
  Revista de Filología Románica, 9, pp. 225–246.
- Leite de Vasconcelos, J. (1901). *Esquisse d'une dialectologie portugaise*.
- Leite de Vasconcelos, J. (1955). *Filologia Barranquenha*.
- Correia, V.M.D. (2014). Inquérito sociolinguístico em Barrancos (PhD thesis,
  Universidade de Évora).
- Clements, J.C. (2009). *The Linguistic Legacy of Spanish and Portuguese
  Colonial Expansion and Language Change*. Cambridge University Press.

Conventions:
- Code ext-PT-x-barrancos: ext = Extremaduran (closest macro-classification
  for this Iberian border contact variety), PT = Portugal, x-barrancos =
  private-use subtag for Barrancos locality.
- Orthography follows the 2025 Convenção Ortográfica do Barranquenho.
- Key distinctive features: betacism (/v/→/b/), sibilant aspiration
  (/s/→[h] in coda), loss of final /-l/ and /-ɾ/, diphthong
  monophthongization (/ej/→[e], /ow/→[o]), unstressed final [ɐ̃w̃]→[õ].

Linguistic classification note:
  Barranquenho is described in the literature as "essencialmente de base
  portuguesa com forte presença de traços fonéticos, morfossintáticos e
  lexicais do espanhol" (Gonçalves & Navas 2021). Its phonological system
  is fundamentally southern European Portuguese (Alentejano), with heavy
  Extremaduran and Andalusian Spanish adstrate influence. The parent is
  therefore pt-PT (European Portuguese), with ext (Extremaduran) and
  es-ES-x-andalusia-w (Western Andalusian) as adstrate contacts.
"""
from orthography2ipa.types import (
    Ancestor, AncestorRole, LanguageSpec, GraphemePosition as GP,
)

P = AncestorRole.PARENT
AD = AncestorRole.ADSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# Grapheme → IPA mappings
# ═══════════════════════════════════════════════════════════════════════════
#
# Based on the "Correspondência entre grafias e sons do barranquenho" table
# in the Convenção Ortográfica do Barranquenho (2025), pp. 17–19.

GRAPHEMES_BRQ = {
    # ── Oral vowels ────────────────────────────────────────────────────────
    "a": ["a", "ɐ"],       # [a] pássaru, biba; [ɐ] cahtelu, boca
    "e": ["e", "ɛ", "ɨ"],  # [e] ehti; [ɛ] pedra; [ɨ] pretonic (rare)
    "i": ["i"],             # figu, figuêra, frenti
    "o": ["o", "ɔ"],       # [o] comu; [ɔ] porcu
    "u": ["u"],             # númeru, donu

    # ── Accented vowels (distinctive Barranquenho diacritical usage) ──────
    "á": ["a"],   # stressed open — marks deleted final -l/-r: cantá, Migué→á
    "à": ["a"],   # contraction (prep. a + det. a): à porta; or grave accent
                  #   marking open átona before deleted liquid: açucà, amabè
    "â": ["ɐ"],   # rare — only in inherited Portuguese words
    "ã": ["ɐ̃"],   # nasal: manhán
    "é": ["ɛ"],   # stressed open-mid: colhé (subst.)
    "ê": ["e"],   # stressed close-mid from monophthongized /ej/: bêju, casê
                  #   or from monophthongized /ow/: sô→ê; also ⟨ou⟩→⟨ô⟩
    "è": ["ɛ"],   # grave: open vowel before deleted liquid: amabè, impossibè
    "í": ["i"],   # stressed: aquí
    "ó": ["ɔ"],   # stressed open-mid: abó; also marks deleted -l: ehpanhó
    "ô": ["o"],   # close-mid from monophthongized /ow/: dotô, sonhô, labô
    "õ": ["õ"],   # nasal (in diphthongs: patrõi)
    "ú": ["u"],   # stressed: azú (< azul)
    "ò": ["ɔ"],   # contraction (prep. a + det. o): ò contráriu

    # ── Single consonants ─────────────────────────────────────────────────
    "b": ["b"],             # covers all historical /b/ AND /v/ (betacism):
                            #   bassora (vassoura), bibu (vivo), trabalhaba
    "c": ["k", "s"],        # /k/ before a,o,u; /s/ before e,i (certu)
    "ç": ["s"],             # coraçãu
    "d": ["d"],             # denti, dedu
    "f": ["f"],             # faba, alcofifa
    "g": ["ɡ", "ʒ"],       # /ɡ/ before a,o,u (gatu); /ʒ/ before e,i (genti)
    "h": ["h", ""],         # [h] aspiration of coda /s/: heringu, mehmu
                            #   or silent (etymological h: omen < homem)
    "j": ["ʒ"],             # janela, jogu, juba
    "k": ["k"],             # (loanwords only)
    "l": ["l"],             # lata, falta; NB: deleted in stressed final
                            #   syllable: ehpanhó (< espanhol), Brasí, azú
    "m": ["m"],             # meningiti, amô
    "n": ["n"],             # Nodà
    "p": ["p"],             # peli
    "q": ["k"],             # (only in ⟨qu⟩)
    "r": ["ɾ", "r", "ʀ"],  # Convention: ⟨r-, -r-⟩ = [ɾ] (Marqui, caru);
                            #   ⟨r; -rr-⟩ = [r]~[ʀ] (rapazi, carru, Barrancu)
                            #   NB: deleted in stressed final: cantá, senhô
    "s": ["s", "z", "h"],   # [s] initial/geminate; [z] intervocalic (asa);
                            #   [h] in coda before C (aspiration): mehmu
    "t": ["t"],             # tenhu, artihta
    "v": ["b"],             # betacism — ⟨v⟩ only in imported toponyms/proper nouns
    "w": ["w"],             # (loanwords)
    "x": ["ʃ", "ks", "z", "s"],  # [ʃ] chobi, xaili; [ks] crucifixu;
                                  #   [z] exami; [s] próximu
    "y": ["j"],             # (loanwords)
    "z": ["z"],             # zebra, dezanobi

    # ── Consonant digraphs ─────────────────────────────────────────────────
    "ch": ["ʃ"],            # chobi, choriçu (Convention: ch = [ʃ])
    "lh": ["ʎ"],            # colhé, lhanu
    "nh": ["ɲ"],            # senhô
    "rr": ["r", "ʀ"],       # alveolar trill or uvular trill: carru, Barrancu
    "ss": ["s"],            # passu, fossi
    "tch": ["tʃ"],          # affricate from Spanish loans: catchondeu
    "qu": ["k", "kw"],      # [k] que, aquí; [kw] cuatru (with labiovelar)
    "gu": ["ɡ", "ɡw"],      # [ɡ] guerra; [ɡw] in some contexts
    "gü": ["ɡw"],           # explicit labiovelar (güe, güi): agüentá, lingüíhtica

    # ── Oral diphthongs ────────────────────────────────────────────────────
    # NB: ⟨ei⟩ and ⟨ou⟩ do NOT appear in native Barranquenho — they
    # monophthongize to ⟨ê⟩ and ⟨ô⟩ respectively (Convention §1.7).
    "ai": ["aj"],           # rare — cf. ⟨ãi⟩ nasal
    "au": ["aw"],
    "eu": ["ew"],
    "iu": ["iw"],
    "oi": ["oj"],
    "ui": ["uj"],

    # ── Nasal vowel digraphs (Convention §1.8) ─────────────────────────────
    # Each nasal context (before m/n in coda) is represented as a digraph
    "am": ["ɐ̃"],            # ambu, campu
    "an": ["ɐ̃"],            # cantá, manhán, canton
    "em": ["ẽ"],            # embora, sempri, tempu
    "en": ["ẽ"],            # entãu, tentu, quen
    "im": ["ĩ"],            # impériu
    "in": ["ĩ"],            # seguinti, min, sintu
    "om": ["õ"],            # ombru, pomba
    "on": ["õ"],            # canton, eron, ehtabon, ponta, bon
    "um": ["ũ"],            # chumbu
    "un": ["ũ"],            # assuntu, un, mundu

    # ── Nasal diphthongs (Convention §1.8.3) ───────────────────────────────
    "ãu": ["ɐ̃w̃"],          # stressed final: fejãu, sãu, nãu, comunhãu
    "ãi": ["ɐ̃j̃"],          # mãi, pãi
    "õi": ["õj̃"],           # patrõi, liçõi
    "eãu": ["jɐ̃w̃"],        # leãu (triphthong, Convention §1.8.3)
}


# ═══════════════════════════════════════════════════════════════════════════
# Allophone inventory
# ═══════════════════════════════════════════════════════════════════════════
#
# All attested surface realisations for each underlying phoneme.
# Convention references: §2 Consonantismo, §1 Vocalismo.

ALLOPHONES_BRQ = {
    # ── Plosives ───────────────────────────────────────────────────────────
    "p": ["p"],
    "b": ["b", "β"],       # [β] intervocalic in rapid speech (Spanish-like)
    "t": ["t"],
    "d": ["d", "ð"],       # [ð] intervocalic (marginal, from Sp. influence)
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],       # [ɣ] intervocalic (Spanish-like lenition)

    # ── Fricatives ─────────────────────────────────────────────────────────
    "f": ["f"],
    "s": ["s", "h"],        # [h] in coda before C (sibilant aspiration, §2.1)
    "z": ["z"],
    "ʃ": ["ʃ"],
    "ʒ": ["ʒ"],
    "h": ["h"],             # aspiration product of coda /s/ and Sp. loans

    # ── Affricate ──────────────────────────────────────────────────────────
    "tʃ": ["tʃ"],           # Spanish loans only: catchondeu (§2.2)

    # ── Rhotics (Convention: [ɾ] tap and [r]~[ʀ] trill) ──────────────────
    "r": ["r", "ʀ"],        # alveolar trill or uvular trill (word-initial,
                            #   after ⟨n⟩, geminate ⟨rr⟩)
    "ɾ": ["ɾ"],             # alveolar tap (intervocalic, clusters)
                            #   NB: deleted in word-final stressed position

    # ── Nasals ─────────────────────────────────────────────────────────────
    "m": ["m"],
    "n": ["n"],
    "ɲ": ["ɲ"],

    # ── Laterals ───────────────────────────────────────────────────────────
    "l": ["l"],             # NB: deleted in stressed final syllable (§2.6)
    "ʎ": ["ʎ"],

    # ── Glides ─────────────────────────────────────────────────────────────
    "w": ["w"],
    "j": ["j"],

    # ── Monophthongs ───────────────────────────────────────────────────────
    "a": ["a"],
    "ɐ": ["ɐ"],
    "e": ["e"],
    "ɛ": ["ɛ"],
    "ɨ": ["ɨ"],             # marginal — pretonic in Portuguese-inherited words
    "i": ["i"],
    "o": ["o"],
    "ɔ": ["ɔ"],
    "u": ["u"],

    # ── Nasal vowels ───────────────────────────────────────────────────────
    "ɐ̃": ["ɐ̃"],
    "ẽ": ["ẽ"],
    "ĩ": ["ĩ"],
    "õ": ["õ"],
    "ũ": ["ũ"],
}


# ═══════════════════════════════════════════════════════════════════════════
# Positional graphemes
# ═══════════════════════════════════════════════════════════════════════════
#
# Context-sensitive IPA overrides for specific phonological positions.

POSITIONAL_BARRANQUENHO = {
    "s": {
        GP.WORD_INITIAL: ["s"],
        GP.INTERVOCALIC: ["z"],       # Portuguese-like voicing (asa → [aza])
        GP.CODA: ["h", "ʃ"],          # aspiration (Sp. influence) + palatal (Pt.)
        GP.WORD_FINAL: ["h", "ʃ"],    # same distribution: maih, poih, doih
    },
    "b": {
        GP.DEFAULT: ["b"],
        GP.INTERVOCALIC: ["β"],        # Spanish-like lenition
    },
    "d": {
        GP.DEFAULT: ["d"],
        GP.INTERVOCALIC: ["ð"],        # marginal — Spanish contact influence
        GP.WORD_FINAL: ["ð", "∅"],     # rare contexts
    },
    "g": {
        GP.DEFAULT: ["ɡ"],
        GP.INTERVOCALIC: ["ɣ"],        # Spanish-like lenition
    },
    "r": {
        GP.WORD_INITIAL: ["r", "ʀ"],   # trill: rapazi
        GP.INTERVOCALIC: ["ɾ"],         # tap: caru, Marqui
        GP.CODA: ["ɾ"],                # tap in coda (often deleted finally)
    },
    "l": {
        GP.ONSET: ["l"],
        GP.CODA: ["l", "ɫ"],           # velarised variant in coda
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# Language specification
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "ext-PT-x-barrancos": LanguageSpec(
        code="ext-PT-x-barrancos",
        name="Barranquenho",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_BRQ,
        allophones=ALLOPHONES_BRQ,
        positional_graphemes=POSITIONAL_BARRANQUENHO,
        parent="pt-PT-x-alentejo",
        ancestors=(
            Ancestor(
                "pt-PT", P, 0.70,
                "Primary descent: Portuguese-based phonological system "
                "(Alentejano variety). Nasal vowels, vowel reduction, "
                "sibilant system, and basic phoneme inventory are Portuguese.",
            ),
            Ancestor(
                "ext", AD, 0.15,
                "Extremaduran adstrate: betacism (/v/→[b]), coda sibilant "
                "aspiration (/s/→[h]), Latin F- → [h] in some lexemes, "
                "Leonese archaisms. Demographic: ~80% of Barrancos population "
                "had Spanish (Extremaduran/Onubense) ancestry by 1894.",
            ),
            Ancestor(
                "es-ES-x-andalusia-w", AD, 0.10,
                "Western Andalusian adstrate: reinforced coda aspiration, "
                "loss of final /-l/ and /-ɾ/, intervocalic -d- deletion, "
                "morphosyntactic features (pseudo-reflexives, gerund use). "
                "Contact via Aroche, Encinasola, Rosal de la Frontera."
                "General Castilian Spanish adstrate: lexical loans "
                "(barruntá, cohquilha, pantorrilha), /tʃ/ affricate in "
                "borrowings (catchondeu), trilinguality in community.",
            ),
        ),
        notes=(
            "Contact language of Barrancos, Portugal (Lei nº 97/2021). "
            "Portuguese-based phonology with Extremaduran/Andalusian features: "
            "betacism (/v/→[b]), sibilant aspiration (/s/→[h] in coda), "
            "loss of final /-l/ and /-ɾ/ in stressed syllables, "
            "monophthongization of /ej/→[e] and /ow/→[o], "
            "unstressed final [ɐ̃w̃]→[õ] (-on ending), "
            "marginal /tʃ/ from Spanish loans. "
            "Orthography per Convenção Ortográfica do Barranquenho (2025). "
            "First documented by Leite de Vasconcelos (1901); name "
            "'barranquenho' coined by same author (1929)."
        ),
    ),
}