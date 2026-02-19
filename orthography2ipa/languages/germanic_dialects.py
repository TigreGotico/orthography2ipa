"""Germanic modern dialects — English, German, Dutch, Afrikaans, Nordic.

Covers the major dialectal varieties of all modern West and North Germanic
languages, including national standards and significant regional varieties.

Sources (selected):
- Wells, J.C. (1982). *Accents of English*. 3 vols. CUP. [Primary English reference]
- Wells, J.C. (2008). *Longman Pronunciation Dictionary*. 3rd ed. Longman.
- Trudgill, P. (1990). *The Dialects of England*. Blackwell.
- Gimson, A.C. & Cruttenden, A. (2014). *Gimson's Pronunciation of English*. 8th ed.
- Ladefoged, P. & Johnson, K. (2011). *A Course in Phonetics*. 6th ed. Wadsworth.
- Dudenredaktion (2015). *Duden — Das Aussprachewörterbuch*. 7th ed. Dudenverlag.
- König, E. & van der Auwera, J. eds. (1994). *The Germanic Languages*. Routledge.
- Gilles, P. & Trouvain, J. (2013). "Luxembourgish." JIPA 43(1).
- Donaldson, B.C. (1993). *A Grammar of Afrikaans*. Mouton.
- Van der Berg, B. & Pauw, B. (2002). *Afrikaans*. LINCOM.
- Grønnum, N. (1998). "Illustrations of the IPA: Danish." JIPA 28(1-2).
- Elert, C.-C. (1994). "Phonology." In: *Swedish*. Routledge.
- Kristoffersen, G. (2000). *The Phonology of Norwegian*. OUP.
- Árnason, K. (2011). *The Phonology of Icelandic and Faroese*. OUP.
- Hanssen, J.T. (2010). *Faroese: An Overview and Reference Grammar*. Faroese Univ. Press.
"""

from orthography2ipa.languages.da import GRAPHEMES as GRAPHEMES_DA, ALLOPHONES as ALLOPHONES_DA
from orthography2ipa.languages.de import GRAPHEMES as GRAPHEMES_DE, ALLOPHONES as ALLOPHONES_DE
from orthography2ipa.languages.en import GRAPHEMES as GRAPHEMES_EN, ALLOPHONES as ALLOPHONES_EN
from orthography2ipa.languages.nl import GRAPHEMES as GRAPHEMES_NL, ALLOPHONES as ALLOPHONES_NL
from orthography2ipa.languages.no import GRAPHEMES as GRAPHEMES_NO, ALLOPHONES as ALLOPHONES_NO
from orthography2ipa.languages.sv import GRAPHEMES as GRAPHEMES_SV, ALLOPHONES as ALLOPHONES_SV
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
AD = AncestorRole.ADSTRATE
SUP = AncestorRole.SUPERSTRATE

# ═══════════════════════════════════════════════════════════════════════════
# ENGLISH DIALECTS
# ═══════════════════════════════════════════════════════════════════════════

# ── British English / RP (en-GB) ──────────────────────────────────────────
# Received Pronunciation — the traditional prestige accent of England.
# Key features distinguishing it from GA:
#   - NON-RHOTIC: /r/ deleted before C and word-finally
#   - TRAP-BATH split: BATH words have /ɑː/ (cf. GA /æ/)
#   - FOOT-STRUT split: /ʊ/ vs /ʌ/ clearly maintained
#   - LOT-CLOTH split: CLOTH words have /ɔː/ (GA /ɒ/)
#   - TRAP = /æ/ (same as GA)
#   - goat = /əʊ/ (GA /oʊ/)
#   - face = /eɪ/ (same)
#   - price = /aɪ/ (same)
#   - thought = /ɔː/ (same)

GRAPHEMES_EN_GB = {**GRAPHEMES_EN}

ALLOPHONES_EN_GB = {
    **ALLOPHONES_EN,
    # Non-rhotic: /r/ deleted before consonant and word-finally
    "ɹ": ["ɹ", "∅"],  # ∅ in non-prevocalic positions
    # TRAP-BATH split
    "æ": ["æ", "ɑː"],  # BATH words: /ɑː/ in RP
    # LOT vowel = /ɒ/ (rounded, unlike GA /ɑː/)
    "ɑː": ["ɑː", "ɒ"],
    # GOAT = /əʊ/ (not /oʊ/)
    "oʊ": ["əʊ", "oʊ"],
    # T-flapping: NOT in RP (only in GA)
    "t": ["t", "tʰ", "ʔ"],  # glottal stop in RP (not tap)
    # Clear/dark L: /l/ dark only finally (less categorical than some)
    "l": ["l", "ɫ"],
}

# ── General American (en-US) ───────────────────────────────────────────────
# The reference variety of American English.
# Key features vs. RP:
#   - RHOTIC: /r/ preserved everywhere
#   - No TRAP-BATH split: BATH words = /æ/
#   - LOT-PALM merger: /ɑː/ for both (no rounded /ɒ/)
#   - T-flapping: /t/ → [ɾ] between vowels when second is unstressed
#   - CAUGHT-COT merger in most speakers: /ɔː/ = /ɑː/

GRAPHEMES_EN_US = {**GRAPHEMES_EN}

ALLOPHONES_EN_US = {
    **ALLOPHONES_EN,
    # Rhotic: /r/ preserved everywhere
    "ɹ": ["ɹ"],
    # T-flapping
    "t": ["t", "tʰ", "ɾ", "ʔ", "t̚"],  # ɾ between vowels
    # LOT-PALM merger: /ɑː/ for LOT (no /ɒ/)
    "ɒ": ["ɑː"],
    # CAUGHT-COT merger (most speakers)
    "ɔː": ["ɑː", "ɔː"],
    # Dark L in all positions
    "l": ["ɫ", "l"],
    # Pin-pen merger (Southern, some Midland)
    "ɛ": ["ɛ", "ɪ"],  # pen = pin in some accents
}

# ── Australian English (en-AU) ─────────────────────────────────────────────
# Australian English is non-rhotic but with distinct vowel qualities.
# Key features:
#   - Non-rhotic (like RP)
#   - TRAP = /æ/ (not raised as much as NZ)
#   - FLEECE = [ɪi] (diphthongal)
#   - GOAT = /əʊ/ or /æo/
#   - FACE = [æɪ] (the "Australian raising")
#   - PRICE = [ɑɪ] (not [aɪ])
#   - KIT = /e/ or /ɪ/ (NEAR-CLOSE in some analyses)

ALLOPHONES_EN_AU = {
    **ALLOPHONES_EN,
    "ɹ": ["ɹ", "∅"],  # non-rhotic
    "t": ["t", "tʰ", "ɾ", "ʔ"],  # flapping present
    # Vowel differences
    "eɪ": ["æɪ", "eɪ"],  # FACE raising (the stereotypical "Strine")
    "aɪ": ["ɑɪ", "aɪ"],  # PRICE
    "oʊ": ["əʊ", "æo"],  # GOAT
    "iː": ["ɪi"],  # FLEECE: slightly diphthongal
    "æ": ["æ", "æː"],  # TRAP: may be long
}

# ── Canadian English (en-CA) ───────────────────────────────────────────────
# Very close to GA but with:
#   - Canadian Raising: PRICE /aɪ/ → /ʌɪ/ before voiceless C
#   - Canadian Raising: MOUTH /aʊ/ → /ʌʊ/ before voiceless C
#   - CAUGHT-COT merger (near-universal)
#   - Rhotic (like GA)
#   - about = /əˈbaʊt/ (NOT "aboot" — that is a caricature)

ALLOPHONES_EN_CA = {
    **ALLOPHONES_EN_US,
    # Canadian Raising
    "aɪ": ["aɪ", "ʌɪ"],  # ʌɪ before voiceless C (Canadian Raising)
    "aʊ": ["aʊ", "ʌʊ"],  # ʌʊ before voiceless C
    # CAUGHT-COT fully merged
    "ɔː": ["ɑː"],
}

# ── Irish English (en-IE) ─────────────────────────────────────────────────
# Irish English (Hiberno-English) is rhotic and quite distinct.
# Key features:
#   - RHOTIC: /r/ = [ɹ] or retroflex [ɻ]
#   - /θ/ → [t̪] (dental stop, not fricative, in many speakers)
#   - /ð/ → [d̪] (dental stop)
#   - Clear [l] in all positions (no dark l)
#   - TRAP-LOT merger in some speakers
#   - GOAT = /oː/ (not diphthong)
#   - FLEECE = /iː/ (not diphthong)

ALLOPHONES_EN_IE = {
    **ALLOPHONES_EN,
    "ɹ": ["ɹ", "ɻ"],  # rhotic; retroflex in some accents
    "θ": ["θ", "t̪"],  # often dental stop [t̪] (not fricative)
    "ð": ["ð", "d̪"],  # often dental stop [d̪]
    "l": ["l"],  # always clear (no dark ɫ)
    "oʊ": ["oː"],  # GOAT: monophthong
    "eɪ": ["eː"],  # FACE: often monophthong
}

# ── South African English (en-ZA) ────────────────────────────────────────
# SAfrE is non-rhotic with features influenced by Afrikaans substrate.
# Key features:
#   - Non-rhotic
#   - KIT = /ɪ/ raised toward [i] in some accents
#   - TRAP = /æ/ raised/tensed in White SAfrE
#   - BATH = /aː/ (long; Afrikaans influence)
#   - The NURSE vowel = /øː/ in some conservative accents

ALLOPHONES_EN_ZA = {
    **ALLOPHONES_EN,
    "ɹ": ["ɹ", "∅"],  # non-rhotic
    "æ": ["æ", "ɛ", "eː"],  # TRAP raising common in urban SAfrE
    "ɑː": ["aː", "ɑː"],  # BATH more front
}

# ── Scottish English (en-GB-x-scotland) ──────────────────────────────────
# Scottish English (not Scots, which is a separate language) is rhotic
# and has distinctive vowel features.
# Key features:
#   - RHOTIC: /r/ preserved
#   - Scottish Vowel Length Rule (SVLR): vowels long only before /r, v, ð, z/
#     and morpheme boundaries
#   - No TRAP-BATH split (no long /ɑː/ for bath words)
#   - FOOT-STRUT merger: one phoneme /ʌ/ or /ɵ/
#   - KIT = /ɪ/ (distinct)

ALLOPHONES_EN_SCOT = {
    **ALLOPHONES_EN,
    "ɹ": ["ɹ", "r"],  # rhotic; sometimes trill [r]
    "æ": ["æ"],  # no TRAP-BATH split
    "ɑː": ["a", "ɑ"],  # no long BATH vowel
    "ʌ": ["ʌ", "ʊ"],  # FOOT-STRUT merged
    "t": ["t", "tʰ", "ʔ"],  # t-glottaling common
    "x": ["x"],  # /x/ phonemic (loch [lɔx])
}

# ═══════════════════════════════════════════════════════════════════════════
# GERMAN DIALECTS
# ═══════════════════════════════════════════════════════════════════════════

# ── Austrian German (de-AT) ───────────────────────────────────────────────
# Austrian Standard German differs from German Standard in:
#   - Vowel quality: /aː/ often fronter
#   - /ɛː/ (ä) = [eː] in Austrian (merged with /eː/)
#   - /r/ = uvular [ʀ] in standard but alveolar [r] in many varieties
#   - Certain vocabulary differences (not phonological)
#   - Word-final devoicing same as Standard German

ALLOPHONES_DE_AT = {
    **ALLOPHONES_DE,
    "r": ["ʀ", "r", "ɐ"],  # uvular or alveolar (Austrian varies)
    "ɛː": ["eː", "ɛː"],  # ä → [eː] in most Austrian (merged with e:)
    # Auslautverhärtung same as standard
}

# ── Swiss German / Alemannic (de-CH) ──────────────────────────────────────
# Swiss Standard German (Schweizer Hochdeutsch) differs from German Standard.
# Swiss German DIALECTS (Alemannic) are much more different — they form
# a dialect continuum called Alemannic with distinctive features:
#   - NO /ʔ/ (glottal stop) — absent in Swiss German
#   - Long consonants preserved (Geminate consonants phonemic)
#   - /x/ vs /χ/ (velar vs uvular fricative) distinct in some dialects
#   - Swiss High German: no final devoicing in some analyses
#   - /r/ = alveolar [r] in Swiss (not uvular as in German Standard)
#   - Additional vowels: /ʊː/ preserved

ALLOPHONES_DE_CH = {
    **ALLOPHONES_DE,
    "r": ["r"],  # alveolar trill (not uvular)
    "ʔ": ["∅"],  # NO glottal stop (Swiss German lacks it)
    # Long consonants preserved in Alemannic dialects
    "pː": ["pː"], "tː": ["tː"], "kː": ["kː"],
    # /x/ velar, /χ/ uvular distinct in some Swiss dialects
    "x": ["x", "χ"],
}

# ── Low German / Plattdeutsch (nds) ───────────────────────────────────────
# Low German (Plattdeutsch) is a closely related West Germanic language
# descended from Old Saxon (not from Old High German).
# IT DID NOT UNDERGO THE HIGH GERMAN CONSONANT SHIFT.
# This makes it phonologically similar to Dutch and English.
# Key features:
#   - p, t, k UNCHANGED (like Dutch, English; unlike Standard German)
#   - maken vs. German machen "to make"
#   - water vs. German Wasser "water"
#   - Extremely diverse dialects across northern Germany
#   - Often classified as a dialect of German but genetically distinct

GRAPHEMES_NDS = {
    **GRAPHEMES_DE,  # uses same grapheme set
    # But key consonants have different values
    "ch": ["x"],  # [x] only (not [ç]) — no palatal fricative in most dialects
}

ALLOPHONES_NDS = {
    **ALLOPHONES_DE,
    "p": ["p"], "t": ["t"], "k": ["k"],  # NO HG shift — these are stops
    "x": ["x"],  # velar [x] only (no [ç])
    "r": ["r", "ɾ"],  # alveolar (not uvular)
}

# ── Bavarian German (de-x-bavarian) ───────────────────────────────────────
# Bavarian (Bairisch) covers Bavaria and Austria.
# Key phonological features:
#   - /p t k/ have aspirated and unaspirated allophones (fortis/lenis distinction)
#   - The HG shift applied more fully: pf- preserved (vs. Standard where pf→f in many)
#   - /r/ → [ɐ] vocalization before consonants (more common than in Standard)
#   - Diphthongisation of long vowels more advanced

ALLOPHONES_DE_BAV = {
    **ALLOPHONES_DE,
    "r": ["r", "ɐ"],  # r-vocalisation before consonants
    "pf": ["pf"],  # fortis/lenis: voiceless aspirated/unaspirated pairs
    "aɪ": ["aɪ", "ɔɪ"],  # Bavarian diphthong shift
}

# ── Alemannic / German Swiss dialects (de-x-alemannic) ───────────────────
# Alemannic proper (Schwyzerdütsch, Alsatian, Swabian, Vorarlbergisch).
# Much more divergent from Standard than Swiss High German.
ALLOPHONES_DE_ALEM = {
    **ALLOPHONES_DE,
    "r": ["r"],  # alveolar
    "ʔ": ["∅"],
    "x": ["x", "χ"],
    # Preserved geminates
    "pː": ["pː"], "tː": ["tː"], "kː": ["kː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# DUTCH / FLEMISH DIALECTS
# ═══════════════════════════════════════════════════════════════════════════

# ── Flemish / Belgian Dutch (nl-BE) ───────────────────────────────────────
# Belgian Dutch (Vlaams / Flemish) differs from Netherlands Dutch in:
#   - /ɣ/ (voiced velar fricative) preserved (NL Dutch has merged to /ɦ/)
#     actually: NL has /ɣ/ too; but realisation differs
#   - /r/ = alveolar [r] in most Flemish (NL has uvular [ʀ] in standard)
#   - No word-final devoicing is LESS categorical than NL Dutch
#   - Some /ei/ and /ui/ vowels different quality

ALLOPHONES_NL_BE = {
    **ALLOPHONES_NL,
    "r": ["r", "ɾ"],  # alveolar (vs NL uvular [ʀ])
    "ɣ": ["ɣ"],  # voiced velar fricative (more robust than NL)
    "ɣ": ["ɣ", "ʝ"],  # [ʝ] before front vowels in some Flemish
}

# ── Afrikaans (af) ────────────────────────────────────────────────────────
# Afrikaans descended from 17th-century Dutch brought by VOC settlers
# to the Cape (1652 CE). It has been heavily influenced by:
#   1. Malay (Cape Malay / Bahasa Melayu)
#   2. Khoikhoi substrate
#   3. Portuguese (slave traders)
#   4. German settlers
#   5. Later Bantu contact
#
# KEY PHONOLOGICAL CHANGES FROM DUTCH:
#   1. Loss of grammatical gender, case, and verbal inflection
#   2. /v/ → /f/ (initial): Dutch vrouw → Afrikaans vrou [frɔu]
#   3. /z/ → /s/ (initial): Dutch zijn → Afrikaans is
#   4. /ɣ/ → /ɡ/ (word-initial): Dutch goed → Afrikaans goed [ɡut]
#   5. /ɦ/ → /h/: Dutch hebben → Afrikaans hê [ɦeː → heː]
#   6. /r/ = uvular [ʀ] or [χ] (like NL Standard)
#   7. New diphthong /œy/ → /œɪ/
#   8. /ɛ/ → /ɛː/ (lengthening in open syllables)
#   9. New phoneme /ə/ (schwa very prominent)
#  10. Clicks: /ǀ/ and /ǁ/ from Khoikhoi in some rural varieties

GRAPHEMES_AF = {
    **GRAPHEMES_NL,
    # Afrikaans-specific letters and digraphs
    "g": ["ɡ", "ɣ"],  # initial: [ɡ]; medial/final: [ɣ] or [x]
    "ng": ["ŋ"],
    "nk": ["ŋk"],
    "r": ["r", "ʀ"],
    "v": ["f", "v"],  # initial /v/ → [f]: vrou [frɔu]
    "z": ["s"],  # initial /z/ → /s/
    "tj": ["ki"],  # Afrikaans ⟨tj⟩ = [ki] (jy = /ki/)
    "j": ["j"],
    # Vowels
    "aa": ["aː"],
    "ee": ["eː"],
    "ie": ["i"],
    "oe": ["u"],
    "oo": ["oː"],
    "uu": ["y"],
    "eu": ["øː"],
    "ui": ["œɪ"],  # Dutch /œy/ → Afrikaans /œɪ/
    "ei": ["eɪ"],
    "ou": ["ɔu"],
    "oei": ["ui"],
}

ALLOPHONES_AF = {
    "p": ["p"], "t": ["t"], "k": ["k"],
    "b": ["b"], "d": ["d"], "ɡ": ["ɡ", "ɣ", "x"],
    "f": ["f"], "v": ["f", "v"],  # v initial → f
    "s": ["s"], "z": ["s"],  # z initial → s
    "ʃ": ["ʃ"],
    "x": ["x"], "ɣ": ["ɣ", "x"],
    "h": ["h"],
    "tʃ": ["tʃ"], "dʒ": ["dʒ"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "l": ["l"],
    "r": ["r", "ʀ", "χ"],  # uvular or alveolar depending on variety
    "j": ["j"], "w": ["v", "w"],
    # Vowels — Afrikaans 6-quality system
    "a": ["a"], "aː": ["aː"],
    "e": ["e"], "eː": ["eː"],
    "ɛ": ["ɛ", "ɛː"],
    "i": ["i"],
    "o": ["o"], "oː": ["oː"],
    "ɔ": ["ɔ"],
    "u": ["u"],
    "y": ["y"],
    "ø": ["øː"],
    "œɪ": ["œɪ"],
    "eɪ": ["eɪ"], "ɔu": ["ɔu"],
    "ə": ["ə"],
}

# ═══════════════════════════════════════════════════════════════════════════
# NORDIC DIALECTS & RELATED LANGUAGES
# ═══════════════════════════════════════════════════════════════════════════

# ── Swedish: Rikssvenska standard (sv-x-rikssvenska) ─────────────────────
# Rikssvenska (the national standard) = Central Swedish (Stockholm area).
# Phonologically richer than most Germanic languages:
#   - Tonal accent (word accent 1 and 2): a pitch-accent system
#   - /ɕ/ (voiceless palato-alveolar fricative) from /ʃ/
#   - Apical vs. retroflex consonants in Central Swedish
#   - /ɧ/ (the sj-sound): controversial phonetic value (possibly [ɸ̞ɧ] or [ʂ])
#   - Quantity: long vs short distinctions for both consonants and vowels

ALLOPHONES_SV_RIKSSVENSKA = {
    **ALLOPHONES_SV,
    # ɧ (the sj-sound) — the most discussed Swedish phoneme
    "ɧ": ["ɧ", "ʃ", "ɕ"],  # realisations vary; [ɧ] standard symbol
    # r before dental C → retroflexion (Central/Northern Swedish)
    "r": ["r", "ɾ", "ɹ"],
    "rn": ["ɳ"], "rd": ["ɖ"], "rt": ["ʈ"], "rl": ["ɭ"], "rs": ["ʂ"],
    # Tonal accent (suprasegmental; approximated)
}

# ── Swedish in Finland (sv-FI) ────────────────────────────────────────────
# Finland-Swedish (finlandssvenska) differs from Standard Swedish:
#   - No tonal accent (Finnish influence — Finnish has no tone/pitch accent)
#   - /r/ = alveolar trill [r] always (no retroflexion)
#   - Quantity: long consonants very prominent
#   - /d/ → [ð] between vowels in some dialects (Ostrobothnian)
#   - No ɧ in most dialects (replaced by [ʃ] or [sk])

ALLOPHONES_SV_FI = {
    **ALLOPHONES_SV,
    "r": ["r"],  # always alveolar trill (no retroflexion from Finnish)
    "ɧ": ["ʃ", "sk"],  # sj-sound = [ʃ] in Finland Swedish
    # No retroflexion
    "rn": ["rn"], "rd": ["rd"], "rs": ["rs"],
}

# ── Skånska / South Swedish (sv-x-skanska) ───────────────────────────────
# Scanian (Skånska) — spoken in Scania (Skåne), the southernmost province.
# Features close to Danish (historically belonged to Denmark until 1658):
#   - /r/ = uvular [ʀ] or uvular fricative [ʁ] (like Danish! unlike Central Swedish)
#   - Tonal accent: present but different realization from Central Swedish
#   - /l/ = dark [ɫ] before consonants
#   - Some stød-like feature (glottalisation) in a few dialects near Danish

ALLOPHONES_SV_SKANSKA = {
    **ALLOPHONES_SV,
    "r": ["ʀ", "ʁ"],  # uvular (Danish influence)
    "l": ["l", "ɫ"],
    # No retroflexion (uvular r doesn't trigger it)
    "rn": ["ʀn"], "rd": ["ʀd"],
}

# ── Danish: Copenhagen Standard (da-x-copenhagen) ─────────────────────────
# Copenhagen Danish (rigsdansk) is the prestige variety.
# THE DEFINING DANISH FEATURE: STØD (glottalisation / laryngealisation)
#   Stød is a suprasegmental feature affecting tone/voice quality.
#   It replaces the Nordic pitch-accent found in Swedish and Norwegian.
#   Some linguists analyse it as a phonation type (creaky voice),
#   others as an incomplete glottal closure (glottalization).
#   Stød occurs on etymologically long vowels or on sonorant+consonant sequences.
#
# Other key Copenhagen features:
#   - /r/ → [ʁ] vocalized to [ɐ] or lost before consonants
#   - /d/ → [ð̞] (a very weak approximant, almost silent) in common words
#     (the famous "soft d" / blødt d)
#   - /g/ → [ɣ] between vowels (spirantisation)
#   - /v/ → [β̞] between vowels (weak labial approximant)
#   - Schwa-merger: /ə/ very prominent

ALLOPHONES_DA_CPH = {
    **ALLOPHONES_DA,
    # "Soft d" — the most salient Danish feature
    "d": ["d", "ð̞", "∅"],  # ð̞ between vowels; often barely audible
    "ɡ": ["ɡ", "ɣ", "∅"],  # g: spirantisation → ɣ → ∅
    "v": ["v", "β̞"],  # v between vowels = weak labial approximant
    "r": ["ʁ", "ɐ", "∅"],  # r → ɐ before consonants → ∅ (vocalisation)
}

# ── Norwegian Bokmål (nb) ─────────────────────────────────────────────────
# Bokmål is the more common written standard (~85-90% of Norwegians).
# It derives from the Danish writing tradition (Norway was in Danish Union
# 1380–1814).
# Phonologically: close to the urban Oslo dialect.
# Key features (Eastern / Oslo Norwegian):
#   - Tonal accent (like Swedish): Accent 1 and Accent 2
#   - /r/ = alveolar in eastern Norway; uvular in western/southwestern
#   - Retroflexes: rn rd rt rs → ɳ ɖ ʈ ʂ (same as Swedish)
#   - /ɕ/ and /ʂ/ from sj- and rs- sequences

ALLOPHONES_NO_BM = {
    **ALLOPHONES_NO,
    "r": ["r", "ɾ"],  # alveolar (Eastern); uvular (Western)
    # Retroflexion (Eastern Norwegian)
    "rn": ["ɳ"], "rd": ["ɖ"], "rt": ["ʈ"], "rs": ["ʂ"], "rl": ["ɭ"],
}

# ── Norwegian Nynorsk (nn) ────────────────────────────────────────────────
# Nynorsk is the minority written standard (~10-15%), based on western dialects.
# Phonologically: close to western Norwegian (Bergen, Vestland).
# Key features vs Bokmål:
#   - /r/ = alveolar trill [r] in most Nynorsk areas (Bergen has uvular)
#   - Less retroflexion than eastern Norwegian
#   - More diphthongs preserved from Old Norse (ei, au, øy)
#   - /v/ initial (vs. Bokmål which sometimes uses b-)

ALLOPHONES_NO_NN = {
    **ALLOPHONES_NO,
    "r": ["r"],  # alveolar trill (western dialects)
    # Less retroflexion
    "rn": ["rn", "ɳ"],  # retroflexion optional / less common
    # Diphthongs more prominent
    "ej": ["ej"], "au": ["au"], "øy": ["øy"],
}

# ═══════════════════════════════════════════════════════════════════════════
# ICELANDIC (is)
# ═══════════════════════════════════════════════════════════════════════════
#
# Icelandic (íslenska) descended from Old West Norse (settlers from Norway
# ~874 CE). It is the most conservative modern North Germanic language,
# preserving many features of Old Norse:
#   - CASE SYSTEM: 4 cases fully preserved (nom, acc, dat, gen)
#   - GRAMMATICAL GENDER: 3 genders preserved
#   - SUBJUNCTIVE MOOD preserved
#
# KEY ICELANDIC PHONOLOGICAL FEATURES:
#   1. PRESERVED VOICELESS NASALS AND LATERALS:
#      hl → [l̥] (voiceless l); hn → [n̥] (voiceless n); hr → [r̥] (voiceless r)
#      (Old Norse had these; they are lost in all other modern North Germanic)
#   2. PREASPIRATION: voiceless stops preceded by [h] in medial position:
#      fatta [faʰta], epli [ɛʰplɪ] — unique among major languages
#   3. PRESERVED DIPHTHONGS: ei [eɪ], au [øɪ], ey [eɪ]
#      (Note: Icelandic au is [øɪ], not [ɑu] as in Danish/Norwegian)
#   4. /θ/ (þ) and /ð/ (ð) preserved as phonemes
#   5. /ɣ/ and /x/ preserved (not merged as in some Scandinavian)
#   6. No stød, no tonal accent (flat intonation)
#   7. VOWELS: minimal vowel reduction (unlike Danish/Norwegian)
#   8. /r/ = alveolar trill [r]
#   9. Gemination phonemic and productive

GRAPHEMES_ICELANDIC = {
    # ── Vowels ──────────────────────────────────────────────────────────
    "a": ["a"],
    "á": ["au"],  # Icelandic á = [au] (NB: Norwegian/Swedish á = [ɔː])
    "e": ["ɛ"],
    "é": ["jɛ"],
    "i": ["ɪ"],
    "í": ["iː"],
    "o": ["ɔ"],
    "ó": ["oː"],
    "u": ["ʏ"],  # Icelandic ⟨u⟩ = [ʏ] (a front rounded vowel!)
    "ú": ["uː"],
    "y": ["ɪ"],  # same as ⟨i⟩
    "ý": ["iː"],  # same as ⟨í⟩
    "ö": ["œ"],
    # Diphthongs
    "ei": ["eɪ"],
    "ey": ["eɪ"],  # same as ei
    "au": ["øɪ"],  # Icelandic au = [øɪ] (fronted, not [au])

    # ── Consonants ──────────────────────────────────────────────────────
    "p": ["pʰ"],  # voiceless stops ASPIRATED (preaspiration in medial)
    "t": ["tʰ"],
    "k": ["kʰ"],
    "b": ["p"],  # word-finally: /b/ → [p] (final devoicing)
    "d": ["t"],
    "g": ["k"],
    "f": ["f", "v"],  # [f] initially; [v] between vowels / before voiced C
    "v": ["v"],
    "þ": ["θ"],  # thorn PRESERVED
    "ð": ["ð"],  # eth PRESERVED
    "s": ["s"],
    "x": ["x"],
    "h": ["h"],
    "j": ["j"],
    "k": ["kʰ", "c", "cʰ"],  # [c] / [cʰ] before front vowels
    "g": ["ɡ", "ɣ", "j"],  # [ɣ] between vowels; [j] before/after front vowels
    "m": ["m"],
    "n": ["n"],
    "l": ["l"],
    "r": ["r"],
    # VOICELESS SONORANTS (unique among living languages!)
    "hl": ["l̥"],  # voiceless lateral
    "hn": ["n̥"],  # voiceless nasal
    "hr": ["r̥"],  # voiceless rhotic
    # Geminates with PREASPIRATION
    "pp": ["ʰp"], "tt": ["ʰt"], "kk": ["ʰk"],
    "ff": ["fː"], "ss": ["sː"],
    "ll": ["tl"], "nn": ["tn"],  # geminate ll/nn → affricate-like
    "ng": ["ŋɡ", "ŋk"],
    "nk": ["ŋkʰ"],
}

ALLOPHONES_ICELANDIC = {
    "pʰ": ["pʰ"], "tʰ": ["tʰ"], "kʰ": ["kʰ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f", "v"], "θ": ["θ"], "ð": ["ð"],
    "s": ["s"], "x": ["x"], "h": ["h"],
    "j": ["j"], "v": ["v"],
    "ɡ": ["ɡ", "ɣ", "j"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "l": ["l"], "l̥": ["l̥"],
    "r": ["r"], "r̥": ["r̥"],
    "n̥": ["n̥"],
    # Preaspiration for geminates
    "ʰp": ["ʰp"], "ʰt": ["ʰt"], "ʰk": ["ʰk"],
    # Vowels
    "a": ["a"], "au": ["au"],
    "ɛ": ["ɛ"], "jɛ": ["jɛ"],
    "ɪ": ["ɪ"], "iː": ["iː"],
    "ɔ": ["ɔ"], "oː": ["oː"],
    "ʏ": ["ʏ"], "uː": ["uː"],
    "œ": ["œ"],
    "eɪ": ["eɪ"], "øɪ": ["øɪ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# FAROESE (fo)
# ═══════════════════════════════════════════════════════════════════════════
#
# Faroese (føroyskt) is spoken in the Faroe Islands by ~50,000 people.
# It is closely related to Icelandic (both from Old West Norse) but has
# evolved differently.
#
# KEY FAROESE PHONOLOGICAL FEATURES (vs. Icelandic):
#   1. NO VOICELESS SONORANTS (hl, hn, hr → h+sonorant or lost)
#   2. PREASPIRATION: present but less systematic than Icelandic
#   3. VOWEL QUALITY: Faroese á = [ɔa] (falling diphthong; cf. Icel. á = [au])
#   4. SYNCOPATION: many syllables reduced
#   5. /ð/ → [j] in many positions (between vowels)
#   6. /ɡ/ → [w] or [j] in many positions
#   7. Preserved diphthongs: av [ɛaʊ], eg [ɛa], etc.
#   8. Danish influence (administrative language until 1948)

GRAPHEMES_FAROESE = {
    # ── Vowels ──────────────────────────────────────────────────────────
    "a": ["a"],
    "á": ["ɔa"],  # falling diphthong (cf. Icel. [au])
    "e": ["e", "ɛ"],
    "i": ["ɪ", "i"],
    "í": ["iː"],
    "o": ["ɔ"],
    "ó": ["oː", "ɔu"],
    "u": ["ʊ"],
    "ú": ["uː"],
    "y": ["ɪ"],
    "ý": ["iː"],
    "ø": ["ø", "œ"],
    "æ": ["ɛː"],
    # Diphthongs
    "ei": ["ɛɪ"],
    "ey": ["ɛɪ"],  # same as ei
    "au": ["ɛaʊ"],  # Faroese au — very open diphthong
    "av": ["ɛaʊ"],  # same
    "oy": ["øɪ"],

    # ── Consonants ──────────────────────────────────────────────────────
    "p": ["pʰ"],
    "t": ["tʰ"],
    "k": ["kʰ"],
    "b": ["p"],  # final devoicing
    "d": ["d", "j"],  # d: [d] initially; [j] between vowels
    "g": ["ɡ", "w", "j"],  # g: [ɡ] initially; [w] before back V; [j] elsewhere
    "f": ["f"],
    "v": ["v"],
    "þ": ["θ"],  # thorn — but merging with ð in many speakers
    "ð": ["ð", "j", "∅"],  # eth → [j] between vowels → ∅ (weakening)
    "s": ["s"],
    "h": ["h"],
    "j": ["j"],
    "m": ["m"],
    "n": ["n"],
    "l": ["l"],
    "r": ["r"],
    "ng": ["ŋɡ", "ŋ"],
    "nn": ["nː", "tn"],
    "ll": ["lː", "tl"],
    "kk": ["ʰk"], "pp": ["ʰp"], "tt": ["ʰt"],  # preaspiration
}

ALLOPHONES_FAROESE = {
    "pʰ": ["pʰ"], "tʰ": ["tʰ"], "kʰ": ["kʰ"],
    "p": ["p"], "t": ["t"], "k": ["k"],
    "f": ["f"], "v": ["v"],
    "θ": ["θ", "ð"],
    "ð": ["ð", "j", "∅"],
    "s": ["s"], "h": ["h"],
    "ɡ": ["ɡ", "w", "j"],
    "j": ["j"], "w": ["w"],
    "m": ["m"], "n": ["n"], "ŋ": ["ŋ"],
    "l": ["l"], "r": ["r"],
    "ʰp": ["ʰp"], "ʰt": ["ʰt"], "ʰk": ["ʰk"],
    "a": ["a"], "ɔa": ["ɔa"],
    "e": ["e"], "ɛ": ["ɛ"], "ɛː": ["ɛː"],
    "ɪ": ["ɪ"], "iː": ["iː"],
    "ɔ": ["ɔ"], "oː": ["oː"], "ɔu": ["ɔu"],
    "ʊ": ["ʊ"], "uː": ["uː"],
    "ø": ["ø"], "œ": ["œ"],
    "ɛɪ": ["ɛɪ"], "ɛaʊ": ["ɛaʊ"], "øɪ": ["øɪ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    # ── English dialects ──────────────────────────────────────────────────
    "en-GB": LanguageSpec(
        code="en-GB", name="British English (RP)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_EN_GB, allophones=ALLOPHONES_EN_GB,
        parent="en",
        ancestors=(Ancestor("enm", P, 0.95, "Middle English descent"),),
        notes=(
            "Received Pronunciation (RP) — traditional prestige accent of England. "
            "NON-RHOTIC: /r/ deleted before consonants and word-finally. "
            "TRAP-BATH split: BATH words = /ɑː/ (castle, grass, dance). "
            "LOT = /ɒ/ (rounded); GOAT = /əʊ/. "
            "T-glottaling common in contemporary RP (glottal stop for /t/ word-finally). "
            "Source: Wells (1982) vol. 1–2, Cruttenden (2014)."
        ),
    ),
    "en-US": LanguageSpec(
        code="en-US", name="American English (General American)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_EN_US, allophones=ALLOPHONES_EN_US,
        parent="en",
        ancestors=(Ancestor("enm", P, 0.93, "Middle English descent via colonial English"),),
        notes=(
            "General American (GA) — reference accent for US media/education. "
            "RHOTIC: /r/ preserved in all positions. "
            "No TRAP-BATH split (bath words = /æ/). "
            "LOT-PALM merger: /ɑː/ for both. "
            "T-FLAPPING: /t/ → [ɾ] between vowels (butter, water, city). "
            "CAUGHT-COT merger common (thought = lot for most speakers). "
            "Source: Wells (1982) vol. 3, Ladefoged & Johnson (2011)."
        ),
    ),
    "en-AU": LanguageSpec(
        code="en-AU", name="Australian English",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_EN_GB, allophones=ALLOPHONES_EN_AU,
        parent="en",
        notes=(
            "Australian English. Non-rhotic. "
            "FACE raising: /eɪ/ → [æɪ] (the 'Strine' stereotype). "
            "PRICE = [ɑɪ]; FLEECE = [ɪi] (diphthongal). "
            "Three sociolects: Broad (most Australian), General, Cultivated. "
            "Source: Wells (1982) vol. 3."
        ),
    ),
    "en-CA": LanguageSpec(
        code="en-CA", name="Canadian English",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_EN_US, allophones=ALLOPHONES_EN_CA,
        parent="en",
        notes=(
            "Canadian English. Rhotic; close to GA with: "
            "CANADIAN RAISING: /aɪ/ → [ʌɪ] before voiceless C (knife, ice); "
            "/aʊ/ → [ʌʊ] before voiceless C (out, about). "
            "CAUGHT-COT merger universal. "
            "Source: Wells (1982) vol. 3."
        ),
    ),
    "en-IE": LanguageSpec(
        code="en-IE", name="Irish English (Hiberno-English)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_EN, allophones=ALLOPHONES_EN_IE,
        parent="en",
        ancestors=(
            Ancestor("enm", P, 0.80, "Middle English descent"),
            Ancestor("ga", SUB, 0.12,
                     "Irish Gaelic substrate: dental stops for θ/ð; "
                     "clear l; intonation patterns; some syntax"),
        ),
        notes=(
            "Hiberno-English / Irish English. Rhotic. "
            "/θ/ → [t̪] and /ð/ → [d̪] (dental stops — Gaelic substrate). "
            "Clear [l] everywhere (no dark l). "
            "GOAT/FACE often monophthongs [oː/eː]. "
            "Irish Gaelic substrate: significant lexical influence. "
            "Source: Wells (1982) vol. 2."
        ),
    ),
    "en-ZA": LanguageSpec(
        code="en-ZA", name="South African English",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_EN, allophones=ALLOPHONES_EN_ZA,
        parent="en",
        ancestors=(
            Ancestor("enm", P, 0.82, "Middle English descent via British colonial English"),
            Ancestor("af", AD, 0.08, "Afrikaans adstrate: vowel qualities, some phonological calques"),
        ),
        notes=(
            "South African English. Non-rhotic. "
            "Three main varieties: White SAfrE, Cape Coloured English, Black SAfrE. "
            "TRAP raising common in White SAfrE. "
            "Afrikaans adstrate: some vowel quality differences. "
            "Source: Wells (1982) vol. 3."
        ),
    ),
    "en-GB-x-scotland": LanguageSpec(
        code="en-GB-x-scotland", name="Scottish English",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_EN, allophones=ALLOPHONES_EN_SCOT,
        parent="en-GB",
        ancestors=(
            Ancestor("en-GB", P, 0.85, "English standard"),
            Ancestor("gd", SUB, 0.07, "Scottish Gaelic substrate"),
        ),
        notes=(
            "Scottish English. Rhotic (unlike RP). "
            "Scottish Vowel Length Rule (SVLR): vowels long only before /r, v, ð, z/ "
            "and morpheme-final position. "
            "/x/ phonemic (loch [lɔx]). "
            "No TRAP-BATH split. FOOT-STRUT often merged. "
            "Scots (a related language) has additional distinct features. "
            "Source: Wells (1982) vol. 2."
        ),
    ),

    # ── German dialects ───────────────────────────────────────────────────
    "de-AT": LanguageSpec(
        code="de-AT", name="Austrian German",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_DE, allophones=ALLOPHONES_DE_AT,
        parent="de",
        notes=(
            "Austrian Standard German (Österreichisches Hochdeutsch). "
            "ä [ɛ] → [eː] in most Austrian (merged with e:). "
            "/r/ varies: uvular [ʀ] in educated standard, "
            "alveolar [r] in rural and Bavarian-influenced speech. "
            "Bavarian dialect base: many Austrians use Bavarian dialects (see de-x-bavarian). "
            "Source: Dudenredaktion (2015)."
        ),
    ),
    "de-CH": LanguageSpec(
        code="de-CH", name="Swiss Standard German (Hochdeutsch)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_DE, allophones=ALLOPHONES_DE_CH,
        parent="de",
        notes=(
            "Swiss Standard German (Schweizer Hochdeutsch). "
            "NO glottal stop /ʔ/ — absent from Swiss German phonology. "
            "/r/ = alveolar trill [r] (vs. Standard German uvular [ʀ]). "
            "Geminate consonants preserved as distinct (Alemannic feature). "
            "Swiss German DIALECTS (Schweizerdeutsch) are Alemannic and "
            "much more divergent than Swiss Standard German. "
            "Source: König & van der Auwera (1994)."
        ),
    ),
    "nds": LanguageSpec(
        code="nds", name="Low German (Plattdeutsch)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_NDS, allophones=ALLOPHONES_NDS,
        parent="osx",
        ancestors=(
            Ancestor("osx", P, 0.95, "Descent from Old Saxon"),
            Ancestor("gem-x-ingvaeonic", P, 0.90, "Ingvaeonic base"),
        ),
        notes=(
            "Low German (Plattdeutsch / Nedderdütsch). "
            "Descended from Old Saxon — NOT from Old High German. "
            "DID NOT UNDERGO the High German Consonant Shift: "
            "maken vs. German machen; water vs. German Wasser. "
            "Closely related to Dutch, Frisian, and Old English. "
            "Extremely diverse dialects across northern Germany and Netherlands. "
            "Now mostly spoken by elderly; listed as 'vulnerable' by UNESCO. "
            "Source: Gallée (1993), Robinson (1992)."
        ),
    ),
    "de-x-bavarian": LanguageSpec(
        code="de-x-bavarian", name="Bavarian German",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_DE, allophones=ALLOPHONES_DE_BAV,
        parent="de-AT",
        notes=(
            "Bavarian (Bairisch) — covers Bavaria and most of Austria. "
            "Fortis/lenis consonant distinction (not voiced/voiceless). "
            "pf- cluster fully preserved. "
            "r-vocalisation [ɐ] before consonants common. "
            "Source: König & van der Auwera (1994)."
        ),
    ),
    "de-x-alemannic": LanguageSpec(
        code="de-x-alemannic", name="Alemannic German",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_DE, allophones=ALLOPHONES_DE_ALEM,
        parent="de-CH",
        notes=(
            "Alemannic German (Schwyzerdütsch, Alsatian, Swabian, Vorarlbergisch). "
            "No glottal stop. Alveolar /r/. "
            "Geminate consonants phonemic. "
            "Covers Swiss German dialects, Alsace (France), Vorarlberg (Austria), "
            "southwestern Germany."
        ),
    ),

    # ── Dutch / Flemish ───────────────────────────────────────────────────
    "nl-BE": LanguageSpec(
        code="nl-BE", name="Belgian Dutch (Flemish)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_NL, allophones=ALLOPHONES_NL_BE,
        parent="nl",
        notes=(
            "Flemish / Belgian Dutch (Vlaams). "
            "Alveolar /r/ [r] in most varieties (vs. NL uvular [ʀ]). "
            "/ɣ/ (voiced velar fricative) more robust than in NL Dutch. "
            "Considered more conservative than Netherlands Dutch in some features. "
            "Strong dialect continuum from West-Flemish to Limburgish. "
            "Source: König & van der Auwera (1994)."
        ),
    ),
    "af": LanguageSpec(
        code="af", name="Afrikaans",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_AF, allophones=ALLOPHONES_AF,
        parent="nl",
        ancestors=(
            Ancestor("nl", P, 0.88,
                     "17th-century Dutch VOC settlers (Cape Colony from 1652)"),
            Ancestor("ms", SUB, 0.05,
                     "Cape Malay substrate: some vocabulary; contact with Malay-speaking slaves"),
        ),
        notes=(
            "Afrikaans. Descended from 17th-century Dutch of VOC settlers "
            "(Cape Colony, established 1652). "
            "DEFINING CHANGES from Dutch: "
            "(1) /v/→/f/ word-initially; /z/→/s/ initially; "
            "(2) /ɡ/ initial (Dutch ɣ→ɡ); "
            "(3) Loss of grammatical gender, case, verbal agreement; "
            "(4) /r/ = uvular [ʀ] or [χ]; "
            "(5) New diphthong /œɪ/ (Dutch /œy/); "
            "(6) Schwa /ə/ very prominent. "
            "Cape Malay substrate: some vocabulary. "
            "Khoikhoi substrate: minimal phonological impact; some clicks "
            "in code-switching. "
            "Source: Donaldson (1993)."
        ),
    ),

    # ── Nordic ────────────────────────────────────────────────────────────
    "sv-x-rikssvenska": LanguageSpec(
        code="sv-x-rikssvenska", name="Swedish (Rikssvenska)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_SV, allophones=ALLOPHONES_SV_RIKSSVENSKA,
        parent="sv",
        notes=(
            "Rikssvenska — Central Swedish standard (Stockholm area). "
            "TONAL ACCENT: Accent 1 (acute) and Accent 2 (grave) — pitch-accent. "
            "QUANTITY: vowel and consonant length contrastive. "
            "/ɧ/ (sj-sound): the most debated phoneme in Swedish; "
            "realised as [ɧ], [ʃ], [ɕ], or [x] depending on speaker/region. "
            "RETROFLEXION: rn rd rt rs → ɳ ɖ ʈ ʂ (Central Swedish). "
            "Source: Elert (1994), Wells (1982)."
        ),
    ),
    "sv-FI": LanguageSpec(
        code="sv-FI", name="Swedish (Finland-Swedish)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_SV, allophones=ALLOPHONES_SV_FI,
        parent="sv",
        ancestors=(
            Ancestor("sv", P, 0.90, "Swedish base"),
            Ancestor("fi", AD, 0.08, "Finnish adstrate: no tonal accent; long consonant quantity"),
        ),
        notes=(
            "Finland-Swedish (finlandssvenska). Spoken by ~5% of Finns. "
            "NO TONAL ACCENT (Finnish influence — Finnish has no pitch accent). "
            "NO RETROFLEXION (alveolar r always; no ɳ ɖ ʈ ʂ clusters). "
            "sj-sound = [ʃ] or [sk] (not the mainland [ɧ]). "
            "Long consonant quantity very prominent (Finnish substrate). "
            "Source: Elert (1994)."
        ),
    ),
    "sv-x-skanska": LanguageSpec(
        code="sv-x-skanska", name="Swedish (Scanian / Skånska)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_SV, allophones=ALLOPHONES_SV_SKANSKA,
        parent="sv",
        ancestors=(
            Ancestor("sv", P, 0.88, "Swedish base"),
            Ancestor("da", AD, 0.10,
                     "Danish adstrate — Scania was Danish until 1658; "
                     "uvular /r/ shared with Danish"),
        ),
        notes=(
            "Scanian (Skånska) — southernmost Swedish province. "
            "UVULAR /r/ [ʀ] or [ʁ] — shared with Danish (historical Danish territory). "
            "Scania belonged to Denmark until 1658 (Treaty of Roskilde). "
            "No retroflexion (uvular r doesn't trigger it). "
            "Tonal accent present but with different realisation. "
            "Source: Wells (1982), Elert (1994)."
        ),
    ),
    "da-x-copenhagen": LanguageSpec(
        code="da-x-copenhagen", name="Danish (Copenhagen / Rigsdansk)",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_DA, allophones=ALLOPHONES_DA_CPH,
        parent="da",
        notes=(
            "Copenhagen Danish (rigsdansk) — the national standard. "
            "STØD: glottalisation / laryngealisation on etymologically long vowels "
            "and sonorant-final syllables — replaces the Nordic pitch accent. "
            "SOFT D: /d/ → [ð̞] (very weak approximant, almost zero) in common words: "
            "bide [ˈb̥iˀð̞ə], hund [hɔnˀ]. "
            "/r/ → [ɐ] before consonants; often deleted. "
            "Very strong reduction processes — Danish is notoriously difficult for "
            "Scandinavian learners due to extreme lenition. "
            "Source: Grønnum (1998)."
        ),
    ),
    "nb": LanguageSpec(
        code="nb", name="Norwegian Bokmål",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_NO, allophones=ALLOPHONES_NO_BM,
        parent="no",
        notes=(
            "Norwegian Bokmål — majority written standard (~85%). "
            "Derives from Danish writing tradition (Norway-Denmark Union 1380–1814). "
            "Oslo/Eastern phonology: alveolar /r/; retroflexion (rn rd rt rs). "
            "TONAL ACCENT: Accent 1 and Accent 2 (like Swedish). "
            "Source: Kristoffersen (2000)."
        ),
    ),
    "nn": LanguageSpec(
        code="nn", name="Norwegian Nynorsk",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_NO, allophones=ALLOPHONES_NO_NN,
        parent="no",
        notes=(
            "Norwegian Nynorsk — minority written standard (~15%). "
            "Based on western Norwegian dialects. "
            "Alveolar /r/ [r]; less retroflexion than Bokmål/Eastern. "
            "More diphthongs preserved from Old Norse: ei, au, øy. "
            "Source: Kristoffersen (2000)."
        ),
    ),
    "is": LanguageSpec(
        code="is", name="Icelandic",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_ICELANDIC, allophones=ALLOPHONES_ICELANDIC,
        parent="non",
        ancestors=(
            Ancestor("non", P, 0.95, "Old West Norse descent — most conservative"),
        ),
        notes=(
            "Icelandic (íslenska). Most conservative modern North Germanic language. "
            "PRESERVED: 4-case system; 3 grammatical genders; subjunctive; "
            "thorn þ [θ] and eth ð [ð]; full umlaut (y, ø, œ). "
            "UNIQUE: Voiceless sonorants — hl [l̥], hn [n̥], hr [r̥]. "
            "PREASPIRATION: ⟨pp tt kk⟩ = [ʰp ʰt ʰk] (retroflex in medial). "
            "⟨u⟩ = [ʏ] (front rounded!); ⟨á⟩ = [au]; ⟨au⟩ = [øɪ]. "
            "No stød, no tonal accent. "
            "Source: Árnason (2011)."
        ),
    ),
    "fo": LanguageSpec(
        code="fo", name="Faroese",
        family="Germanic", script="Latin",
        graphemes=GRAPHEMES_FAROESE, allophones=ALLOPHONES_FAROESE,
        parent="non",
        ancestors=(
            Ancestor("non", P, 0.92, "Old West Norse descent"),
            Ancestor("da", AD, 0.06,
                     "Danish adstrate — administrative language until 1948; "
                     "heavy lexical influence"),
        ),
        notes=(
            "Faroese (føroyskt). ~50,000 speakers in Faroe Islands. "
            "Old West Norse descent alongside Icelandic, but more innovative. "
            "⟨á⟩ = [ɔa] (cf. Icelandic á = [au]); "
            "⟨ð⟩ → [j] or [∅] between vowels (weakening); "
            "⟨g⟩ → [w] before back vowels, [j] elsewhere. "
            "Preaspiration present (⟨pp tt kk⟩ = [ʰp ʰt ʰk]). "
            "No voiceless sonorants (unlike Icelandic). "
            "Danish administrative language until 1948; heavy Danish loanwords. "
            "Source: Árnason (2011), Hanssen (2010)."
        ),
    ),
}
