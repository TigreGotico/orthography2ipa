"""Proto-Iranian and Middle Persian — ancestral chain for all Persian/Iranian dialects.

This module covers the reconstructed and attested proto-languages from
Proto-Indo-Iranian through to Middle Persian (Pahlavi), which are the
necessary ancestral nodes for all modern Iranian dialects.

Genealogical chain:
  Proto-Indo-Iranian (iir)    ~2500–2000 BCE
       ↓
  Proto-Iranian (ira)         ~1500–1000 BCE
       ↓
  Old Iranian                 ~1000–400 BCE
    ├── Old Persian (peo)     ~600–400 BCE  (Achaemenid inscriptions)
    └── Old Avestan / Young Avestan (ave)   (Zoroastrian scriptures)
       ↓
  Middle Iranian              ~400 BCE – 900 CE
    ├── Middle Persian / Pahlavi (pal)  ~224–900 CE  (Sasanian)
    └── Parthian (xpr)                  ~247 BCE – 224 CE
       ↓
  New Persian / Early New Persian (fa-x-early) ~900–1200 CE
       ↓
  Modern Persian dialects (fa, fa-AF, tg, ...)

Sources:
- Windfuhr, G. ed. (2009). *The Iranian Languages*. Routledge.
  [Comprehensive reference for all stages]
- Schmitt, R. (2014). *Old Persian*. Reichert Verlag.
- Skjærvø, P.O. (2009). "Old Iranian." In: Windfuhr (2009).
- Lazard, G. (1963). *La langue des plus anciens monuments de la prose persane*.
  Klincksieck. [Early New Persian]
- Brunner, C.J. (1977). *A Syntax of Western Middle Iranian*. Undena.
- Mackenzie, D.N. (1971). *A Concise Pahlavi Dictionary*. OUP.
- Sundermann, W. (1989). "Parthian." In: *Compendium Linguarum Iranicarum*.
  Reichert.
- Lubotsky, A. (2009). "Vedic and Indo-Iranian." In: *The Ancient Languages
  of Asia and the Americas*. CUP.
- Fortson, B.W. (2010). *Indo-European Language and Culture*. 2nd ed. Blackwell.
- Kümmel, M.J. (2009). "Phonology of Old Iranian." In: Windfuhr (2009).
"""

from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE
SUP = AncestorRole.SUPERSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-INDO-IRANIAN (iir)  ~2500–2000 BCE
# ═══════════════════════════════════════════════════════════════════════════
#
# Proto-Indo-Iranian (also "Aryan") is the common ancestor of the Indo-Aryan
# (Sanskrit, Hindi, etc.) and Iranian (Persian, Avestan, etc.) branches.
#
# RELATIONSHIP TO PIE:
#   PIE *bʰ → PII *bʰ (breathy voiced preserved)
#   PIE *e, *a, *o → PII *a (SATEM VOWEL MERGER — the "a-merger")
#   PIE *ḱ, *ĝ, *ĝʰ → PII *ś, *ź (PALATOVELARS → SIBILANTS — satem feature)
#   PIE palatal series *kʲ → PII /ɕ/ (merged with *s in some environments)
#
# KEY PII CONSONANT INVENTORY:
#   Voiceless stops: p, t, k (+ labiovelars kʷ)
#   Voiced stops: b, d, g
#   Voiced aspirates (breathy): bʱ, dʱ, gʱ (from PIE voiced aspirates)
#   Fricatives: s, z (from PIE *s, *z), ś (from PIE *ḱ, *ĝ) 
#   Sibilant: š (from PIE *sk, *ks, and other palatalisations)
#   Laryngeals: h₁, h₂, h₃ → merging into /H/ or lost
#   Resonants: m, n, l, r, y, v

GRAPHEMES_IIR = {
    # ── Stops ─────────────────────────────────────────────────────────────
    "p": ["p"],
    "b": ["b"],
    "bʱ": ["bʱ"],  # breathy voiced bilabial
    "t": ["t"],
    "d": ["d"],
    "dʱ": ["dʱ"],  # breathy voiced dental
    "k": ["k"],
    "g": ["ɡ"],
    "gʱ": ["ɡʱ"],  # breathy voiced velar
    "kʷ": ["kʷ"],  # labiovelar

    # ── Sibilants (SATEM shifts already in progress) ─────────────────────
    "s": ["s"],
    "z": ["z"],
    "ś": ["ɕ"],  # palatal sibilant < PIE *ḱ (satem shift)
    "ź": ["ʑ"],  # voiced palatal < PIE *ĝ
    "š": ["ʃ"],  # postalveolar
    "ž": ["ʒ"],

    # ── Fricatives ────────────────────────────────────────────────────────
    "H": ["h"],  # merged laryngeals (h₁, h₂, h₃ → /h/ or ∅)
    "h": ["h"],

    # ── Resonants ─────────────────────────────────────────────────────────
    "m": ["m"],
    "n": ["n"],
    "l": ["l"],
    "r": ["r"],
    "y": ["j"],
    "v": ["w"],  # labial glide/fricative

    # ── Vowels (the a-merger is complete: *e, *a, *o → a) ─────────────────
    "a": ["a"],
    "ā": ["aː"],
    "i": ["i"],
    "ī": ["iː"],
    "u": ["u"],
    "ū": ["uː"],
    # Syllabic resonants
    "r̥": ["r̩"],
    "l̥": ["l̩"],
    "m̥": ["m̩"],
    "n̥": ["n̩"],
}

ALLOPHONES_IIR = {
    "p": ["p"], "b": ["b"], "bʱ": ["bʱ"],
    "t": ["t"], "d": ["d"], "dʱ": ["dʱ"],
    "k": ["k"], "ɡ": ["ɡ"], "ɡʱ": ["ɡʱ"],
    "kʷ": ["kʷ"],
    "s": ["s"], "z": ["z"],
    "ɕ": ["ɕ", "s"], "ʑ": ["ʑ", "z"],  # palatal sibilants
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "h": ["h", "∅"],
    "m": ["m"], "n": ["n", "ŋ"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-IRANIAN (ira)  ~1500–1000 BCE
# ═══════════════════════════════════════════════════════════════════════════
#
# Proto-Iranian separates from Proto-Indo-Iranian by several key innovations
# that distinguish all Iranian languages from Indo-Aryan:
#
# KEY INNOVATIONS (PII → Proto-Iranian):
#
#   1. *s → h (THE defining Iranian shift)
#      PII *s- (word-initial) → Ir. h- in many positions
#      PII *hapta "seven" → OIr. hapta (OPers. haptan)
#      Compare: PII *saptá → Sanskrit saptá (preserves s-)
#
#   2. Voiced aspirates DEASPIRATED
#      PII *bʱ *dʱ *gʱ → PIr. *b *d *g (breathy voice lost)
#      Compare: Sanskrit preserves bh, dh, gh
#
#   3. *ś (palatal sibilant) → *s then → *h
#      PIE *ḱ → PII *ś → PIr. *s (or directly h in some positions)
#
#   4. *v (labial glide) preserved as *v (not merged with b)
#
#   5. Labiovelar *kʷ → *k (labialisation lost; cf. Greek split kʷ→k/p)
#
#   6. New voiceless fricative *θ from *t in some environments
#      (this develops further into the Old Iranian system)

GRAPHEMES_PROTO_IR = {
    # ── Stops (deaspirated from PII) ─────────────────────────────────────
    "p": ["p"],
    "b": ["b"],  # < PII *b AND *bʱ (deaspiration)
    "t": ["t"],
    "d": ["d"],  # < PII *d AND *dʱ
    "k": ["k"],  # < PII *k AND *kʷ (labialisation lost)
    "g": ["ɡ"],  # < PII *g AND *gʱ

    # ── THE IRANIAN SHIFT: *s → h ─────────────────────────────────────────
    "h": ["h"],  # < PII *s (word-initial/intervocalic positions)
    "s": ["s"],  # residual *s (in clusters, after consonants)

    # ── Fricatives ────────────────────────────────────────────────────────
    "f": ["f"],  # from *p in certain contexts (developing)
    "θ": ["θ"],  # from *t in fricative environments (developing)
    "x": ["x"],  # from *k in fricative environments (developing)

    # ── Sibilants ─────────────────────────────────────────────────────────
    "z": ["z"],
    "š": ["ʃ"],
    "ž": ["ʒ"],

    # ── Resonants ─────────────────────────────────────────────────────────
    "m": ["m"],
    "n": ["n"],
    "r": ["r"],
    "y": ["j"],
    "v": ["v"],  # labial fricative/approximant (PIr. innovation vs. PII *w)
    # /l/ is RARE in Iranian — it survives in some loanwords and words
    # where it derives from PII *r or was borrowed
    "l": ["l"],

    # ── Vowels ────────────────────────────────────────────────────────────
    "a": ["a"],
    "ā": ["aː"],
    "i": ["i"],
    "ī": ["iː"],
    "u": ["u"],
    "ū": ["uː"],
    # Diphthongs developing
    "ai": ["aj"],
    "au": ["aw"],
}

ALLOPHONES_PROTO_IR = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "f": ["f"], "θ": ["θ"], "x": ["x"],
    "h": ["h"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "m": ["m"], "n": ["n", "ŋ"],
    "r": ["r"], "l": ["l"],
    "j": ["j"], "v": ["v", "w"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "aj": ["aj"], "aw": ["aw"],
}

# ═══════════════════════════════════════════════════════════════════════════
# OLD PERSIAN (peo)  ~600–400 BCE  (Achaemenid cuneiform)
# ═══════════════════════════════════════════════════════════════════════════
#
# Old Persian is directly attested in ~500 cuneiform inscriptions,
# primarily from Darius I and Xerxes I (~520–465 BCE).
# It is the direct ancestor of Middle Persian and all modern Persian dialects.
#
# KEY OLD PERSIAN PHONOLOGICAL FEATURES:
#   1. Three-stop series: voiceless (p t k), voiced (b d g), + fricatives (f θ x)
#   2. FRICATIVISATION: *p → f; *t → θ; *k → x (in certain environments)
#      (these are Old Iranian spirant allophones)
#   3. *θr → θr (unlike Avestan which has θr > sp)
#   4. *v → v (labial fricative/approximant)
#   5. Vowel system: a, i, u short + ā, ī, ū long + diphthongs ai, au
#   6. Some diphthong monophthongisation beginning: ai → ē, au → ō
#
# Script: Cuneiform (syllabary, imprecise for consonant clusters).
# Romanisation follows Schmitt (2014) and Kent (1953).

GRAPHEMES_OLD_PERSIAN = {
    # Stops
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "g": ["ɡ"],
    # Fricatives
    "f": ["f"],  # < PIr. *p in fricative position
    "θ": ["θ"],  # < PIr. *t in fricative position
    "x": ["x"],  # < PIr. *k in fricative position
    "v": ["v"],
    "h": ["h"],
    # Sibilants
    "s": ["s"],
    "z": ["z"],
    "š": ["ʃ"],
    "ž": ["ʒ"],  # marginal; mainly in clusters
    "č": ["tʃ"],  # < PIr. *tš clusters
    # Nasals
    "m": ["m"],
    "n": ["n"],
    # Liquids
    "r": ["r"],
    "l": ["l"],  # rare in native vocabulary
    # Glides
    "y": ["j"],
    # Vowels
    "a": ["a"],
    "ā": ["aː"],
    "i": ["i"],
    "ī": ["iː"],
    "u": ["u"],
    "ū": ["uː"],
    # Diphthongs
    "ai": ["aj", "eː"],  # monophthongisation beginning: ai → ē
    "au": ["aw", "oː"],  # au → ō developing
}

ALLOPHONES_OLD_PERSIAN = {
    "p": ["p", "f"],  # p ~ f allophony in some environments
    "b": ["b"],
    "t": ["t", "θ"],  # t ~ θ allophony
    "d": ["d"],
    "k": ["k", "x"],  # k ~ x allophony
    "ɡ": ["ɡ"],
    "f": ["f"], "θ": ["θ"], "x": ["x"],
    "v": ["v", "w"],
    "h": ["h"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"],
    "tʃ": ["tʃ"],
    "m": ["m"], "n": ["n", "ŋ"],
    "r": ["r"], "l": ["l"],
    "j": ["j"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "aj": ["aj", "eː"],
    "aw": ["aw", "oː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# MIDDLE PERSIAN / PAHLAVI (pal)  ~224–900 CE  (Sasanian Empire)
# ═══════════════════════════════════════════════════════════════════════════
#
# Middle Persian (Pahlavi) is the language of the Sasanian Empire (224–651 CE)
# and the Zoroastrian religious texts (Mēnōg ī Xrad, Bundahišn, etc.).
# It is the direct ancestor of New Persian.
#
# KEY MIDDLE PERSIAN PHONOLOGICAL FEATURES:
#
#   1. CONSONANT LENITION in intervocalic positions:
#      *p → w / b (intervocalic); *t → d; *k → g → ɣ
#      *f → (maintained); *θ → d (interdental lost → dental)
#      This is the key change from Old Persian to Middle Persian
#
#   2. DIPHTHONG MONOPHTHONGISATION (complete):
#      Old Persian *ai → MP ē [eː]
#      Old Persian *au → MP ō [oː]
#
#   3. VOWEL SYSTEM: Moves toward 6-vowel system
#      ā, ē [eː], ī, ō [oː], ū, a (short); eventually reduces to 6 qualities
#
#   4. LOSS OF VOICED FRICATIVES in some positions:
#      *w (< *p) often written as w; *β sometimes
#
#   5. SCRIPT: Pahlavi (Aramaeographic script — letters from Aramaic
#      used as logograms for Persian words "huzvarishn")
#
#   6. ARABIC CONQUEST (651 CE): Arabic becomes language of administration,
#      massive Arabic loanwords begin entering from ~8th century onwards.
#      Arabic consonants ħ, ʕ, q, θ, ð etc. introduced in loanwords but
#      mostly assimilated to Persian phonology (h, ∅, ɣ, s, z respectively).

GRAPHEMES_MIDDLE_PERSIAN = {
    # Stops
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "g": ["ɡ"],
    # Fricatives / Spirants
    "f": ["f"],
    "w": ["w", "v"],  # < Old Persian *p intervocalic
    "θ": ["θ"],  # still present early MP; → d later
    "ð": ["ð"],  # developing in some positions
    "x": ["x"],
    "xw": ["xʷ"],  # labiovelar fricative (→ New Persian xw- / x-)
    "γ": ["ɣ"],  # < *k intervocalic
    "h": ["h"],
    # Sibilants
    "s": ["s"],
    "z": ["z"],
    "š": ["ʃ"],
    "ž": ["ʒ"],
    "č": ["tʃ"],
    "j": ["dʒ"],
    # Nasals
    "m": ["m"],
    "n": ["n"],
    # Liquids
    "r": ["r"],
    "l": ["l"],
    # Glides
    "y": ["j"],
    # Vowels (6-quality system developing)
    "a": ["a"],
    "ā": ["aː"],
    "i": ["i"],
    "ī": ["iː"],
    "u": ["u"],
    "ū": ["uː"],
    # Monophthongised diphthongs
    "ē": ["eː"],  # < OPers. *ai
    "ō": ["oː"],  # < OPers. *au
}

ALLOPHONES_MIDDLE_PERSIAN = {
    "p": ["p", "b", "w"],  # lenition in intervocalic: p → w
    "b": ["b", "β"],
    "t": ["t", "d", "θ"],  # lenition: t → d (θ → d late MP)
    "d": ["d", "ð"],
    "k": ["k", "ɡ", "ɣ"],  # lenition: k → g → γ
    "ɡ": ["ɡ", "ɣ"],
    "f": ["f"],
    "w": ["w", "v"],
    "θ": ["θ", "d"],
    "ð": ["ð", "d"],
    "x": ["x"], "xʷ": ["xʷ", "x"],
    "ɣ": ["ɣ"],
    "h": ["h"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "m": ["m"], "n": ["n", "ŋ"],
    "r": ["r"], "l": ["l"],
    "j": ["j"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "eː": ["eː"], "oː": ["oː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# EARLY NEW PERSIAN (fa-x-early)  ~900–1200 CE
# ═══════════════════════════════════════════════════════════════════════════
#
# Early New Persian (Classical Persian, Dari) is attested from ~900 CE in
# the eastern Islamic world (Khorasan, Transoxiana). Key literary works:
# Shahnameh (Ferdowsi, ~1000 CE), Divan of Rumi, etc.
#
# KEY PHONOLOGICAL DEVELOPMENTS FROM MIDDLE PERSIAN:
#
#   1. MASSIVE ARABIC LOANWORDS (from ~8th century):
#      Arabic consonants θ, ð, ħ, ʕ, q mostly ASSIMILATED:
#        Arabic ث (θ) → Persian /s/
#        Arabic ذ (ð) → Persian /z/
#        Arabic ح (ħ) → Persian /h/
#        Arabic ع (ʕ) → Persian /ʔ/ (glottal stop, often weak)
#        Arabic ق (q) → Persian /q/ then later /ɣ/ or /ɡ/
#      (Some learned speech maintained θ, ð in Arabic loanwords)
#
#   2. VOWEL SYSTEM RESTRUCTURING:
#      MP ē [eː] → New Persian ē (maintained as /eː/ in Classical)
#      MP ō [oː] → New Persian ō (maintained as /oː/ in Classical)
#      Later: ē → /e/ (shortened), ō → /o/ (shortened) in New Persian
#
#   3. Word-final consonant clusters simplified
#
#   4. /v/ stabilised (vs. Middle Persian w/v variation)
#
#   5. Script: Arabic script (nastaliq style for Persian)
#      This introduces Arabic spelling conventions for Arabic loanwords,
#      meaning that θ, ð, ħ, ʕ APPEAR in writing but are pronounced as s, z, h, ʔ.

GRAPHEMES_EARLY_NEW_PERSIAN = {
    # ── Native consonants ─────────────────────────────────────────────────
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "g": ["ɡ"],
    "f": ["f"],
    "v": ["v"],
    "x": ["x"],
    "ɣ": ["ɣ"],  # < Middle Persian γ; also Arabic غ/ق in loanwords
    "h": ["h"],
    "s": ["s"],
    "z": ["z"],
    "ʃ": ["ʃ"],
    "ʒ": ["ʒ"],
    "tʃ": ["tʃ"],
    "dʒ": ["dʒ"],
    "m": ["m"],
    "n": ["n"],
    "r": ["r"],
    "l": ["l"],
    "j": ["j"],

    # ── Arabic loanword consonants (in spelling; mostly assimilated in phonology) ─
    "θ": ["s"],  # Arabic ث → /s/ in pronunciation
    "ð": ["z"],  # Arabic ذ → /z/
    "ħ": ["h"],  # Arabic ح → /h/
    "ʕ": ["ʔ"],  # Arabic ع → /ʔ/ (often weak)
    "q": ["q", "ɣ"],  # Arabic ق → /q/ (learned) or /ɣ/ (vernacular)

    # ── Vowels (Classical 6-vowel system) ────────────────────────────────
    "a": ["a"],
    "aː": ["aː"],
    "eː": ["eː"],  # < Middle Persian ē; later shortens to /e/
    "oː": ["oː"],  # < Middle Persian ō; later shortens to /o/
    "iː": ["iː"],
    "uː": ["uː"],
    # Short i and u begin merging/reducing
    "i": ["i", "e"],
    "u": ["u", "o"],
}

ALLOPHONES_EARLY_NEW_PERSIAN = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "f": ["f"], "v": ["v"],
    "x": ["x"], "ɣ": ["ɣ"],
    "h": ["h"],
    "s": ["s"], "z": ["z"],
    "ʃ": ["ʃ"], "ʒ": ["ʒ"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "ʔ": ["ʔ", "∅"],
    "q": ["q", "ɣ"],
    "m": ["m"], "n": ["n", "ŋ"],
    "r": ["r", "ɾ"], "l": ["l"],
    "j": ["j"],
    "a": ["a"], "aː": ["aː"],
    "eː": ["eː", "e"],
    "oː": ["oː", "o"],
    "iː": ["iː"],
    "uː": ["uː"],
    "i": ["i", "e"],
    "u": ["u", "o"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "iir": LanguageSpec(
        code="iir",
        name="Proto-Indo-Iranian",
        family="Indo-European",
        script="Latin",
        graphemes=GRAPHEMES_IIR,
        allophones=ALLOPHONES_IIR,
        parent="ine",
        ancestors=(
            Ancestor("ine", P, 1.0, "Descent from Proto-Indo-European"),
        ),
        notes=(
            "Proto-Indo-Iranian (~2500–2000 BCE). Ancestor of Indo-Aryan "
            "(Sanskrit, Hindi, etc.) and Iranian (Persian, Avestan, etc.) branches. "
            "Key innovations vs. PIE: "
            "(1) The 'a-merger': PIE *e, *a, *o → PII *a (three vowel qualities "
            "    collapse to one); "
            "(2) Satem shift: PIE palatovelars *ḱ, *ĝ → PII palatal sibilants *ś, *ź; "
            "(3) Voiced aspirates *bʱ, *dʱ, *gʱ preserved (distinct from Greek which "
            "    lost aspiration, and Germanic which shifted to fricatives); "
            "(4) Laryngeals merging toward /H/ or lost. "
            "Evidence: Rigveda (Sanskrit), Avesta (Iranian), Mitanni loanwords "
            "in Hurrian (~1400 BCE) — earliest IE attestation outside Europe."
        ),
    ),

    "ira": LanguageSpec(
        code="ira",
        name="Proto-Iranian",
        family="Indo-Iranian",
        script="Latin",
        graphemes=GRAPHEMES_PROTO_IR,
        allophones=ALLOPHONES_PROTO_IR,
        parent="iir",
        ancestors=(
            Ancestor("iir", P, 1.0, "Descent from Proto-Indo-Iranian"),
        ),
        notes=(
            "Proto-Iranian (~1500–1000 BCE). Ancestor of all Iranian languages: "
            "Persian, Avestan, Sogdian, Parthian, Bactrian, Pashto, Kurdish, "
            "Ossetic, Balochi, etc. "
            "KEY INNOVATIONS vs. Proto-Indo-Iranian: "
            "(1) *s → h: THE diagnostic Iranian change (PII *saptan → PIr. *haptan "
            "    'seven'; cf. Sanskrit saptá); "
            "(2) Voiced aspirates DEASPIRATED: *bʱ, *dʱ, *gʱ → b, d, g "
            "    (Iranian loses the breathy-voice series; Sanskrit preserves it); "
            "(3) *w → *v (labial fricative/approximant); "
            "(4) Labiovelars *kʷ → *k (labialisation lost); "
            "(5) Spirant allophones of stops developing: "
            "    *p → f, *t → θ, *k → x in fricative environments. "
            "Script: romanization (unattested proto-language)."
        ),
    ),

    "peo": LanguageSpec(
        code="peo",
        name="Old Persian",
        family="Iranian",
        script="Latin",
        graphemes=GRAPHEMES_OLD_PERSIAN,
        allophones=ALLOPHONES_OLD_PERSIAN,
        parent="ira",
        ancestors=(
            Ancestor("ira", P, 1.0, "Descent from Proto-Iranian"),
        ),
        notes=(
            "Old Persian (~600–400 BCE). Attested in ~500 cuneiform inscriptions "
            "of the Achaemenid Empire (Darius I, Xerxes I, Artaxerxes I). "
            "Directly ancestral to Middle Persian and all modern Persian dialects. "
            "THREE-STOP + SPIRANT SERIES: p/b/f, t/d/θ, k/g/x. "
            "Diphthongs *ai, *au still present (monophthongisation beginning). "
            "Script: Old Persian cuneiform (syllabic — imprecise for consonants). "
            "ISO 639-2: peo. Primary sources: DNa, DNb, XPh inscriptions. "
            "References: Schmitt (2014), Kent (1953)."
        ),
    ),

    "pal": LanguageSpec(
        code="pal",
        name="Middle Persian (Pahlavi)",
        family="Iranian",
        script="Latin",
        graphemes=GRAPHEMES_MIDDLE_PERSIAN,
        allophones=ALLOPHONES_MIDDLE_PERSIAN,
        parent="peo",
        ancestors=(
            Ancestor("peo", P, 1.0, "Descent from Old Persian"),
        ),
        notes=(
            "Middle Persian / Pahlavi (~224–900 CE). Language of the Sasanian "
            "Empire (224–651 CE) and Zoroastrian religious texts. "
            "KEY INNOVATIONS vs. Old Persian: "
            "(1) Intervocalic consonant LENITION: p→w/b, t→d (θ→d), k→g→γ; "
            "(2) Diphthong MONOPHTHONGISATION: *ai → ē [eː], *au → ō [oː]; "
            "(3) 6-quality vowel system: a, ā, ē, ī, ō, ū; "
            "(4) xw- cluster preserved as /xʷ/ (later → x in New Persian). "
            "Script: Pahlavi (Aramaeographic; Aramaic logograms 'huzvarishn'). "
            "Arabic conquest (651 CE): Arabic becomes administrative language; "
            "Arabic loanwords begin entering. "
            "ISO 639-2: pal (Pahlavi). References: Mackenzie (1971), Brunner (1977)."
        ),
    ),

    "fa-x-early": LanguageSpec(
        code="fa-x-early",
        name="Early New Persian (Classical Persian)",
        family="Iranian",
        script="Arabic",
        graphemes=GRAPHEMES_EARLY_NEW_PERSIAN,
        allophones=ALLOPHONES_EARLY_NEW_PERSIAN,
        parent="pal",
        ancestors=(
            Ancestor("pal", P, 0.85, "Descent from Middle Persian/Pahlavi"),
            Ancestor("ar", AD, 0.12,
                     "Arabic adstrate: massive loanword influx from 8th century; "
                     "Arabic script adopted; Arabic consonants θ/ð/ħ/ʕ/q appear "
                     "in writing but mostly assimilated phonologically: "
                     "θ→s, ð→z, ħ→h, ʕ→ʔ, q→ɣ"),
        ),
        notes=(
            "Early New Persian / Classical Persian (Dari) (~900–1200 CE). "
            "First attested ~900 CE in eastern Khorasan/Transoxiana. "
            "Literary corpus: Shahnameh (Ferdowsi ~1000), Divan of Hafez, Rumi. "
            "KEY INNOVATIONS vs. Middle Persian: "
            "(1) Arabic script adopted (with additional letters پ چ ژ گ for Persian); "
            "(2) Massive Arabic loanwords — Arabic consonants θ, ð, ħ, ʕ, q "
            "    appear in spelling but assimilated phonologically to s, z, h, ʔ, ɣ; "
            "(3) Classical 6-vowel system: ā, ē/eː, ī, ō/oː, ū, a; "
            "(4) /v/ stabilised; /r/ → [ɾ] (tap) in most positions. "
            "This Classical system is the reference for Dari (fa-AF) and Tajik (tg)."
        ),
    ),
}
