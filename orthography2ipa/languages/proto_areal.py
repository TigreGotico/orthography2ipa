"""Proto-languages for Austroasiatic and Tibeto-Burman branches.

Provides ancestor specs required by the Munda and Tibeto-Burman modern
language entries (sat, unr, brx, mni, kha).

These are reconstructed proto-languages with speculative phonetics.
They exist as ancestors of attested modern languages and ensure
connectivity in the ancestry graph.

Sources (Proto-Munda):
- Pinnow, H.-J. (1959). *Versuch einer hist. Lautlehre der Kharia-Sprache*.
- Anderson, G.D.S. (2008). *The Munda Languages*. Routledge.
- Donegan, P. & Stampe, D. (2004). "Rhythm and the synthetic drift of Munda."

Sources (Proto-Tibeto-Burman / Boro-Garo / Kuki-Chin):
- Matisoff, J.A. (2003). *Handbook of Proto-Tibeto-Burman*. UC Press.
- Benedict, P.K. (1972). *Sino-Tibetan: A Conspectus*. CUP.
- VanBik, K. (2009). *Proto-Kuki-Chin*. UC Berkeley dissertation.
- Burling, R. (2003). "The Tibeto-Burman languages of Northeastern India."
  In: *The Sino-Tibetan Languages*, ed. Thurgood & LaPolla. Routledge.

Sources (Proto-Mon-Khmer):
- Shorto, H.L. (2006). *A Mon-Khmer Comparative Dictionary*. Pacific Linguistics.
- Diffloth, G. (2005). "The contribution of linguistic palaeontology to
  the homeland of Austro-Asiatic."
"""
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-MUNDA (sat-x-proto-munda)
# ═══════════════════════════════════════════════════════════════════════════
#
# Reconstructed ancestor of all Munda languages (Santali, Mundari, Ho,
# Korku, Kharia, Sora, Juang, Gta', etc.).
# Austroasiatic > Munda branch.
# Time depth: ~4000–3000 BCE (speculative; pre-attestation).
#
# Key reconstructed features (Anderson 2008, Pinnow 1959):
# - Sesquisyllabic word structure (minor presyllable + main syllable)
# - Register contrast (breathy/clear or modal/creaky vowels)
# - No tones (unlike Mon-Khmer daughters)
# - Rich consonant clusters in onsets
# - 5–6 vowel system with contrastive length
# - Glottal stop phonemic
# - No retroflex consonants (these develop later under IA contact)

GRAPHEMES_PROTO_MUNDA = {
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ə": ["ə"],

    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "g": ["ɡ"],
    "ʔ": ["ʔ"],

    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "s": ["s"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
}

ALLOPHONES_PROTO_MUNDA = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "k": ["k"], "ɡ": ["ɡ"],
    "ʔ": ["ʔ"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "s": ["s"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ə": ["ə"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-BORO-GARO (brx-x-proto-boro-garo)
# ═══════════════════════════════════════════════════════════════════════════
#
# Ancestor of Bodo, Garo, Dimasa, Kokborok, Tiwa, Rabha, etc.
# Sino-Tibetan > Tibeto-Burman > Sal > Boro-Garo branch.
# Time depth: ~2000–1500 BCE (speculative).
#
# Key features (Matisoff 2003, Burling 2003):
# - Aspirated / plain stop contrast
# - Incipient tone development (from lost codas)
# - Prefixing morphology (unusual for TB)
# - SVO word order (rare for TB; possibly areal)
# - Affricate series *ts / *dz

GRAPHEMES_PROTO_BORO_GARO = {
    "a": ["a"], "i": ["i"], "u": ["u"],
    "e": ["e"], "o": ["o"], "ə": ["ə"],

    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"],
    "t": ["t"], "tʰ": ["tʰ"], "d": ["d"],
    "k": ["k"], "kʰ": ["kʰ"], "g": ["ɡ"],
    "ʔ": ["ʔ"],

    "ts": ["ts"], "dz": ["dz"],

    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "s": ["s"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
}

ALLOPHONES_PROTO_BORO_GARO = {
    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"],
    "t": ["t"], "tʰ": ["tʰ"], "d": ["d"],
    "k": ["k"], "kʰ": ["kʰ"], "ɡ": ["ɡ"], "ʔ": ["ʔ"],
    "ts": ["ts"], "dz": ["dz"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "s": ["s"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "i": ["i"], "u": ["u"],
    "e": ["e"], "o": ["o"], "ə": ["ə"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-KUKI-CHIN (mni-x-proto-kuki-chin)
# ═══════════════════════════════════════════════════════════════════════════
#
# Ancestor of Meitei/Manipuri, Mizo/Lushai, Thadou, Hmar, Paite, etc.
# Sino-Tibetan > Tibeto-Burman > Kuki-Chin-Naga (grouping debated).
# Time depth: ~2000–1500 BCE (speculative).
#
# Key features (VanBik 2009, Matisoff 2003):
# - Tone develops from lost final stops (*-p, *-t, *-k → register)
# - Initial consonant clusters *Cr-, *Cl-
# - Sesquisyllabic tendency (presyllables reduced)
# - Aspirated / plain stop contrast
# - Final stop codas still present at proto-stage

GRAPHEMES_PROTO_KUKI_CHIN = {
    "a": ["a"], "i": ["i"], "u": ["u"],
    "e": ["e"], "o": ["o"], "ə": ["ə"],

    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"],
    "t": ["t"], "tʰ": ["tʰ"], "d": ["d"],
    "k": ["k"], "kʰ": ["kʰ"], "g": ["ɡ"],
    "ʔ": ["ʔ"],

    "ts": ["ts"], "tʃ": ["tʃ"],

    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "s": ["s"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
}

ALLOPHONES_PROTO_KUKI_CHIN = {
    "p": ["p"], "pʰ": ["pʰ"], "b": ["b"],
    "t": ["t"], "tʰ": ["tʰ"], "d": ["d"],
    "k": ["k"], "kʰ": ["kʰ"], "ɡ": ["ɡ"], "ʔ": ["ʔ"],
    "ts": ["ts"], "tʃ": ["tʃ"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "s": ["s"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "i": ["i"], "u": ["u"],
    "e": ["e"], "o": ["o"], "ə": ["ə"],
}

# ═══════════════════════════════════════════════════════════════════════════
# PROTO-MON-KHMER (kha-x-proto-mon-khmer)
# ═══════════════════════════════════════════════════════════════════════════
#
# Ancestor of Mon, Khmer, Vietnamese, Khasi, Nicobarese, Aslian, etc.
# Austroasiatic > Mon-Khmer branch (the non-Munda branch of AA).
# Time depth: ~4000–3000 BCE (speculative).
#
# Key features (Shorto 2006, Diffloth 2005):
# - Sesquisyllabic *Cə.CVC structure
# - Register/phonation contrast (breathy vs. clear voice)
# - Rich vowel system with contrastive length
# - No tones at proto-stage (tonogenesis secondary in daughters)
# - Palatal stop series *c / *ɟ (retained in Khmer, Khasi)

GRAPHEMES_PROTO_MON_KHMER = {
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ə": ["ə"], "əː": ["əː"],

    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "c": ["c"], "ɟ": ["ɟ"],
    "k": ["k"], "g": ["ɡ"],
    "ʔ": ["ʔ"],

    "m": ["m"], "n": ["n"], "ɲ": ["ɲ"], "ŋ": ["ŋ"],
    "s": ["s"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
}

ALLOPHONES_PROTO_MON_KHMER = {
    "p": ["p"], "b": ["b"],
    "t": ["t"], "d": ["d"],
    "c": ["c"], "ɟ": ["ɟ"],
    "k": ["k"], "ɡ": ["ɡ"], "ʔ": ["ʔ"],
    "m": ["m"], "n": ["n"], "ɲ": ["ɲ"], "ŋ": ["ŋ"],
    "s": ["s"], "h": ["h"],
    "l": ["l"], "r": ["r"],
    "j": ["j"], "w": ["w"],
    "a": ["a"], "aː": ["aː"],
    "i": ["i"], "iː": ["iː"],
    "u": ["u"], "uː": ["uː"],
    "e": ["e"], "eː": ["eː"],
    "o": ["o"], "oː": ["oː"],
    "ə": ["ə"], "əː": ["əː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "sat-x-proto-munda": LanguageSpec(
        code="sat-x-proto-munda",
        name="Proto-Munda (reconstructed)",
        family="Austroasiatic",
        script="Latin",
        graphemes=GRAPHEMES_PROTO_MUNDA,
        allophones=ALLOPHONES_PROTO_MUNDA,
        parent=None,
        notes=(
            "Proto-Munda (~4000–3000 BCE). Reconstructed common ancestor of "
            "all Munda languages (Santali, Mundari, Ho, Korku, Kharia, Sora). "
            "Austroasiatic > Munda branch. "
            "Sesquisyllabic word structure; register/phonation contrast; "
            "no tones; rich onset clusters; no retroflexes at proto-stage. "
            "Refs: Pinnow (1959), Anderson (2008), Donegan & Stampe (2004)."
        ),
    ),

    "brx-x-proto-boro-garo": LanguageSpec(
        code="brx-x-proto-boro-garo",
        name="Proto-Boro-Garo (reconstructed)",
        family="Tibeto-Burman",
        script="Latin",
        graphemes=GRAPHEMES_PROTO_BORO_GARO,
        allophones=ALLOPHONES_PROTO_BORO_GARO,
        parent=None,
        notes=(
            "Proto-Boro-Garo (~2000–1500 BCE). Reconstructed ancestor of "
            "Bodo, Garo, Dimasa, Kokborok, Tiwa, Rabha. "
            "Sino-Tibetan > Tibeto-Burman > Sal branch. "
            "Aspirated/plain stop contrast; incipient tone; "
            "prefixing morphology; SVO order (atypical for TB). "
            "Refs: Matisoff (2003), Burling (2003), Benedict (1972)."
        ),
    ),

    "mni-x-proto-kuki-chin": LanguageSpec(
        code="mni-x-proto-kuki-chin",
        name="Proto-Kuki-Chin (reconstructed)",
        family="Tibeto-Burman",
        script="Latin",
        graphemes=GRAPHEMES_PROTO_KUKI_CHIN,
        allophones=ALLOPHONES_PROTO_KUKI_CHIN,
        parent=None,
        notes=(
            "Proto-Kuki-Chin (~2000–1500 BCE). Reconstructed ancestor of "
            "Meitei/Manipuri, Mizo/Lushai, Thadou, Hmar, Paite. "
            "Sino-Tibetan > Tibeto-Burman > Kuki-Chin-Naga. "
            "Tone from lost final stops; Cr-/Cl- clusters; sesquisyllabic. "
            "Refs: VanBik (2009), Matisoff (2003)."
        ),
    ),

    "kha-x-proto-mon-khmer": LanguageSpec(
        code="kha-x-proto-mon-khmer",
        name="Proto-Mon-Khmer (reconstructed)",
        family="Austroasiatic",
        script="Latin",
        graphemes=GRAPHEMES_PROTO_MON_KHMER,
        allophones=ALLOPHONES_PROTO_MON_KHMER,
        parent=None,
        notes=(
            "Proto-Mon-Khmer (~4000–3000 BCE). Reconstructed ancestor of "
            "Mon, Khmer, Vietnamese, Khasi, Nicobarese, Aslian, Bahnaric. "
            "Austroasiatic > Mon-Khmer (the non-Munda AA branch). "
            "Sesquisyllabic *Cə.CVC; register/phonation contrast; "
            "rich vowels with length; palatal stops *c/*ɟ; no proto-tones. "
            "Refs: Shorto (2006), Diffloth (2005)."
        ),
    ),
}
