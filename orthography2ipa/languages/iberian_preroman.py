"""Pre-Roman languages of the Iberian Peninsula — grapheme→IPA and allophone mappings.

These are EXPERIMENTAL reconstructions based on epigraphy, comparative
linguistics, and substrate evidence.  Quality of reconstruction varies
enormously — from Celtiberian (reasonably well understood Celtic language
with bilingual/biscriptal evidence) to Tartessian (script only partially
deciphered, linguistic affiliation hotly debated).

All use LATIN ALPHABET TRANSCRIPTION even when the original writing system
was different (Iberian semi-syllabary, Tartessian/Southwestern script,
Greek alphabet, or Latin alphabet).  The original scripts are noted.

IMPORTANT CAVEATS
─────────────────
1. These are scholarly reconstructions, not "known" pronunciations.
2. The phonological systems are inferred from: (a) writing systems,
   (b) comparison with related languages, (c) loanwords and onomastics,
   (d) substrate evidence in later Romance languages.
3. Vowel quality for non-IE languages (Iberian) is largely unknown
   beyond the number of distinctions the script makes.
4. Allophone maps are speculative for all pre-Roman languages.

Sources:
- Wodtko, D.S. et al. (2008). *Nomina im Indogermanischen Lexikon*. Winter.
- Untermann, J. (1975–1997). *Monumenta Linguarum Hispanicarum* I–IV.
- de Hoz, J. (2010). *Historia lingüística de la Península Ibérica* I–II. CSIC.
- Jordán, C. (2004). *Celtibérico*. Universidad de Zaragoza.
- Villar, F. (2000). *Indoeuropeos y no indoeuropeos en la Hispania prerromana*.
- Gorrochategui, J. (1984). *Estudio sobre la onomástica indígena de Aquitania*.
- Ferrer i Jané, J. (2005). "Novetats sobre el sistema dual de escriptura ibèrica."
- Correa, J.A. (2005). "Escritura tartesia." In: *Palaeohispanica* 5.
- Koch, J.T. (2011). *Tartessian 2*. Celtic Studies Publications.
  [NB: Koch's Celtic identification of Tartessian is disputed; see de Hoz 2010]
"""
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# CELTIBERIAN (xce)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Celtic > Continental Celtic > Hispano-Celtic
# Attestation: ~200 inscriptions (3rd–1st c. BCE), including:
#   - Botorrita bronzes (Contrebia Belaisca) — longest texts
#   - Peñalba de Villastar rock inscription
#   - Tesserae hospitales (hospitality tokens)
#   - Coin legends
# Scripts: (a) Eastern Iberian semi-syllabary (adapted), (b) Latin alphabet
# Time depth: ~3rd century BCE to ~1st century CE (Romanisation)
# Geography: Upper Ebro valley, Meseta (modern Aragón, eastern Castile)
#
# PHONOLOGICAL RECONSTRUCTION:
# The Iberian semi-syllabary forces certain interpretations:
#   - Syllabic signs (ka/ke/ki/ko/ku, ta/te/ti/to/tu, ba/be/bi/bo/bu)
#     don't distinguish voicing → we infer voicing from Celtic comparison
#   - The "dual system" (Ferrer 2005) may mark voicing in some texts
#   - Latin-alphabet inscriptions resolve many ambiguities
#
# Key Celtic features preserved:
#   - PIE *p → ∅ (Celtic p-loss): PIE *ph₂tēr → *atir (cf. OIr. athir)
#   - PIE *kʷ → k (labial loss, like Brythonic but unlike Goidelic q > c)
#     Actually debated: some argue kʷ → kʷ preserved in some forms
#   - PIE *gʷ → b (cf. Gaul. -bo- "cow" < PIE *gʷou-)
#   - Lenited intervocalic stops → fricatives (like all Celtic)
#   - /f/ absent (inherited from Celtic p-loss)
#   - Distinctive: preserved *-nd- cluster (unlike Goidelic *-nd- → -nn-)
#
# The mapping below uses Latin-alphabet conventions from the inscriptions.

GRAPHEMES_XCE = {
    # --- Vowels (5-vowel system, standard IE) ---
    # Celtiberian preserves the IE 5-vowel system without major shifts.
    # Long/short distinction likely phonemic (as in all old Celtic)
    # but not consistently marked in writing.
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],

    # Long vowels (occasionally marked by doubling in some inscriptions)
    "aa": ["aː"],
    "ee": ["eː"],
    "ii": ["iː"],
    "oo": ["oː"],
    "uu": ["uː"],

    # --- Diphthongs (well-attested in onomastics) ---
    "ai": ["aj"],
    "ei": ["ej"],
    "oi": ["oj"],
    "au": ["aw"],

    # --- Consonants ---
    # STOPS: The Iberian script doesn't distinguish voicing, but
    # Latin-script inscriptions and Celtic etymology confirm the system.

    # Labial stops
    "b": ["b"],
    # NO /p/ IN NATIVE WORDS — this is the hallmark Celtic feature.
    # PIE *p was lost entirely in Proto-Celtic.
    # /p/ appears only in loanwords (from Iberian, Latin).
    "p": ["p"],  # loanwords only

    # Dental stops
    "t": ["t"],
    "d": ["d"],

    # Velar stops
    "k": ["k"],
    "c": ["k"],  # Latin-alphabet convention
    "g": ["ɡ"],
    "q": ["kʷ"],  # labiovelar (debated: may have merged with /k/)

    # FRICATIVES
    "s": ["s"],  # voiceless alveolar (well-attested)
    "z": ["z", "ts"],  # debated: possibly affricate [ts] or [dz]
    # NO /f/ — Celtic p-loss means *p > ∅, never > f (unlike Germanic)
    # /f/ appears in loanwords only

    # NASALS
    "m": ["m"],
    "n": ["n"],

    # LIQUIDS
    "l": ["l"],
    "r": ["r"],  # probably trilled (standard IE)

    # GLIDES
    "u": ["u", "w"],  # /w/ before vowels
    "i": ["i", "j"],  # /j/ before vowels

    # --- Digraphs and special combinations ---
    "ku": ["kʷ"],  # labiovelar in some transcriptions
    "gu": ["ɡʷ"],  # from PIE *gʷ (but → /b/ in most positions)
    "st": ["st"],
    "nt": ["nt"],
    "nd": ["nd"],  # preserved (unlike Goidelic → nn)
    "nk": ["ŋk"],
    "ng": ["ŋɡ"],

    # Geminates (attested in inscriptions)
    "ss": ["sː"],
    "ll": ["lː"],
    "nn": ["nː"],
    "rr": ["rː"],
    "tt": ["tː"],
}

ALLOPHONES_XCE = {
    # Based on comparative Celtic reconstruction
    "p": ["p"],
    "b": ["b", "β"],  # lenition: [β] intervocalic (pan-Celtic)
    "t": ["t"],
    "d": ["d", "ð"],  # lenition: [ð] intervocalic
    "k": ["k"],
    "ɡ": ["ɡ", "ɣ"],  # lenition: [ɣ] intervocalic
    "kʷ": ["kʷ"],
    "s": ["s"],
    "z": ["z", "ts"],
    "m": ["m"],
    "n": ["n", "ŋ"],  # [ŋ] before velars
    "l": ["l"],
    "r": ["r"],
    "j": ["j"],
    "w": ["w"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "aː": ["aː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],
    "sː": ["sː"], "lː": ["lː"], "nː": ["nː"], "rː": ["rː"], "tː": ["tː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# IBERIAN (xib)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: UNCLASSIFIED (language isolate or family isolate)
#   NOT related to Basque despite repeated attempts to connect them.
#   NOT Indo-European.
#   Possibly related to other pre-IE Mediterranean substrates (speculative).
#
# Attestation: ~2000+ inscriptions (5th–1st c. BCE), including:
#   - Lead plaques (commercial texts)
#   - Coin legends (abundant)
#   - Pottery stamps/graffiti
#   - Rock inscriptions
#   - Greek-alphabet Iberian texts (Emporion, Ullastret)
# Scripts: (a) Northeastern Iberian semi-syllabary (most common)
#          (b) Southeastern Iberian semi-syllabary
#          (c) Greek alphabet (Greco-Iberian, Contestania/Alicante)
# Geography: Mediterranean coast from Languedoc to Murcia, Ebro valley
#
# CRITICAL LIMITATION:
# We can READ the script (values assigned through bilingual coin legends
# and the Greco-Iberian texts) but we CANNOT TRANSLATE the language.
# The phonological system below is based on:
#   1. The distinctions the writing system makes
#   2. Patterns in the onomastic material
#   3. Comparison with later substrate elements in Romance
#   4. The Greco-Iberian texts (which use Greek letters with known values)
#
# PHONOLOGICAL SYSTEM (from the script):
# The semi-syllabary has:
#   - 5 vowel signs: a, e, i, o, u
#   - 5 series of syllabic signs: ka/ke/ki/ko/ku, ta/te/ti/to/tu,
#     ba/be/bi/bo/bu, and (in dual system) ga/ge/gi/go/gu, da/de/di/do/du
#   - Continuous consonant signs: s, ś (two sibilants!), n, m, l, r, ŕ (two rhotics!)
#
# The DUAL SYSTEM (Ferrer 2005) demonstrates that the script originally
# distinguished voiced and voiceless stops in some varieties, but many
# texts use the "simple" system without this distinction.
#
# KEY FEATURES:
#   - Two sibilant phonemes: /s/ (written ⟨s⟩) and /ś/ (written ⟨ś⟩)
#     Exact phonetic values debated: [s] vs [ʃ]? [s̺] vs [s̻]?
#   - Two rhotic phonemes: /r/ (written ⟨r⟩) and /ŕ/ (written ⟨ŕ⟩)
#     Likely tap [ɾ] vs trill [r] (parallel to Basque and later Spanish)
#   - No /f/, /h/, or /θ/ attested
#   - Possibly no distinction between /o/ and /u/ in some dialects
#
# We transcribe in Latin alphabet following Untermann (MLH) conventions.

GRAPHEMES_XIB = {
    # --- Vowels (5 in the script; some dialects may merge o/u) ---
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],

    # --- Stops (voicing distinction from dual system) ---
    # The semi-syllabary is inherently ambiguous for voicing.
    # Dual-system texts and Greco-Iberian confirm the distinction.
    "b": ["b"],
    "p": ["p"],  # only distinguishable in dual-system texts
    "d": ["d"],
    "t": ["t"],
    "g": ["ɡ"],
    "k": ["k"],

    # --- Sibilants (TWO — a diagnostic Iberian feature) ---
    # ⟨s⟩ and ⟨ś⟩ in Untermann's transcription.
    # Phonetic values debated; we follow the most common interpretation:
    "s": ["s"],  # possibly apical [s̺]
    "ś": ["ʃ"],  # possibly laminal [s̻] or postalveolar [ʃ]
    # Alternative: some scholars reverse these, or propose [ts] for one

    # --- Nasals ---
    "n": ["n"],
    "m": ["m"],
    # /m/ is rare in Iberian; some scholars argue it's an allophone of /n/
    # or appears only in loans.  Most inscriptions show very few ⟨m⟩.

    # --- Liquids ---
    # TWO rhotics — like Basque and later Ibero-Romance
    "r": ["ɾ"],  # "simple r" — probably tap
    "ŕ": ["r"],  # "vibrant r" — probably trill
    "l": ["l"],

    # --- Semi-syllabic combinations ---
    # These represent the syllabary: each stop sign inherently includes
    # a vowel.  In Latin transcription we separate them, but the original
    # writing is syllabic.
    "ba": ["ba"], "be": ["be"], "bi": ["bi"], "bo": ["bo"], "bu": ["bu"],
    "ta": ["ta"], "te": ["te"], "ti": ["ti"], "to": ["to"], "tu": ["tu"],
    "ka": ["ka"], "ke": ["ke"], "ki": ["ki"], "ko": ["ko"], "ku": ["ku"],
}

ALLOPHONES_XIB = {
    # Highly speculative — based on patterns visible in the writing system
    # and substrate influence on later Romance
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "ɡ": ["ɡ"],
    "s": ["s"],
    "ʃ": ["ʃ", "s̻"],  # uncertain exact value
    "n": ["n"],
    "m": ["m"],
    "ɾ": ["ɾ"],
    "r": ["r"],
    "l": ["l"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════
# LUSITANIAN (xlg)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: Indo-European — EXACT BRANCH DEBATED
#   Three main hypotheses:
#   (a) Italic (sister to Latin/Oscan/Umbrian) — Tovar, Untermann
#   (b) Celtic (or Para-Celtic) — Prósper, Koch
#   (c) Independent IE branch — Villar, Wodtko
#   The language preserves PIE *p (unlike Celtic) and has features
#   incompatible with both Italic and Celtic as usually defined.
#   Currently (c) is gaining ground.
#
# Attestation: ~5 inscriptions in LATIN ALPHABET, including:
#   - Cabeço das Fráguas (Guarda) — sacrificial inscription
#   - Lamas de Moledo (Viseu) — dedication
#   - Arroyo de la Luz I & II (Cáceres) — fragmentary
#   Plus extensive onomastic material (place names, theonyms, anthroponyms)
# Geography: Western Iberia (modern central Portugal, Extremadura)
# Time: ~1st century BCE (possibly earlier oral tradition)
#
# PHONOLOGICAL FEATURES (from the inscriptions + IE comparison):
#   - PRESERVES PIE *p (unlike Celtic!): *porcom "pig" (cf. Lat. porcum)
#     This is the key argument AGAINST Celtic classification.
#   - Has /f/ (? — debated; possibly from *bh or a substrate)
#   - Has both /k/ and /kʷ/ (or reflexes thereof)
#   - Nasal vowels or nasal codas (? — inferred from spelling)
#   - The -nd- cluster preserved (shared with Celtiberian; unlike Goidelic)
#   - Some scholars see "Italic" features like medial -f- < *-bh-
#
# Since the texts are in Latin alphabet, the transcription is direct.

GRAPHEMES_XLG = {
    # --- Vowels (standard IE 5-vowel system) ---
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],

    # Long vowels (reconstructed from IE etymology; not marked in script)
    "ā": ["aː"],
    "ē": ["eː"],
    "ī": ["iː"],
    "ō": ["oː"],
    "ū": ["uː"],

    # --- Diphthongs (attested in inscriptions) ---
    "ai": ["aj"],
    "ei": ["ej"],
    "oi": ["oj"],
    "au": ["aw"],
    "ou": ["ow"],

    # --- Consonants ---
    # LABIAL — crucially, Lusitanian HAS /p/ (unlike Celtic)
    "p": ["p"],  # < PIE *p (PRESERVED — anti-Celtic evidence)
    "b": ["b"],  # < PIE *b (rare) or *bʰ
    "f": ["f"],  # debated: < PIE *bʰ? (would be Italic-like)

    # DENTAL
    "t": ["t"],
    "d": ["d"],

    # VELAR
    "c": ["k"],  # Latin-alphabet convention
    "g": ["ɡ"],
    "q": ["kʷ"],  # labiovelar (in PORCOM etc.)

    # FRICATIVE
    "s": ["s"],
    "h": ["h"],  # rare; possibly from PIE *s in some positions

    # NASALS
    "m": ["m"],
    "n": ["n"],

    # LIQUIDS
    "l": ["l"],
    "r": ["r"],  # probably trilled

    # --- Clusters attested in inscriptions ---
    "nd": ["nd"],
    "nt": ["nt"],
    "mb": ["mb"],
    "nk": ["ŋk"],
    "ng": ["ŋɡ"],

    # --- Notable words for reference ---
    # PORCOM "pig" (acc.sg.) — cf. Lat. porcum, PIE *porḱom
    # TAVROM "bull" — cf. Lat. taurum, Greek ταῦρος
    # IFADEM "?" — the /f/ is significant for classification
    # CROUGEAI "to Crougea" (theonym) — dative in -ai
    # LAEBO "?" — divine epithet
}

ALLOPHONES_XLG = {
    "p": ["p"],
    "b": ["b"],
    "f": ["f"],  # if genuine, not a Celtic feature
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "ɡ": ["ɡ"],
    "kʷ": ["kʷ"],
    "s": ["s"],
    "h": ["h"],
    "m": ["m"],
    "n": ["n", "ŋ"],
    "l": ["l"],
    "r": ["r"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
    "aː": ["aː"], "eː": ["eː"], "iː": ["iː"], "oː": ["oː"], "uː": ["uː"],
}

# ═══════════════════════════════════════════════════════════════════════════
# TARTESSIAN / SOUTHWESTERN (txr)
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: HOTLY DEBATED
#   - Koch (2009, 2011): Celtic (based on morphological analysis)
#   - de Hoz (2010): Non-IE or pre-IE
#   - Untermann (1997): Possibly related to Iberian
#   - Correa (2005): Script mostly deciphered, language unidentified
#   - Valério (2008): Partially deciphered, structural analysis
#   The honest assessment: WE DON'T KNOW what language this is.
#
# Attestation: ~95 inscriptions in the SOUTHWESTERN SCRIPT
#   - Mostly funerary stelae (Algarve, Alentejo, southwestern Spain)
#   - Script is a variant of Phoenician-derived Paleo-Hispanic scripts
#   - Sign values partly established through comparison with Iberian script
#   - REDUNDANCY FEATURE: vowels written both as independent signs AND
#     as part of syllabic signs (e.g., ta-a instead of just ta)
# Geography: Southern Portugal (Algarve, Baixo Alentejo), Huelva
# Time: ~7th–5th century BCE (contemporary with Tartessos civilisation)
#
# PHONOLOGICAL SYSTEM (from the script, very tentative):
# The script suggests:
#   - 5 vowels: a, e, i, o, u
#   - Dental, labial, velar stop series (voicing unclear from script)
#   - At least one sibilant /s/
#   - Nasals /n/, /m/
#   - Liquids /l/, /r/
#   - Possible nasal vowels (inferred from certain spellings)
#
# THIS IS THE MOST SPECULATIVE ENTRY IN THE ENTIRE PACKAGE.
# We model only what the script structure allows us to infer.

GRAPHEMES_TXR = {
    # --- Vowels ---
    # The script has 5 independent vowel signs
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],

    # --- Stops ---
    # Three series in the script: labial, dental, velar
    # Voicing distinction UNKNOWN from the script alone
    "b": ["b", "p"],  # script doesn't distinguish
    "t": ["t", "d"],  # script doesn't distinguish
    "k": ["k", "ɡ"],  # script doesn't distinguish

    # --- Sibilant ---
    "s": ["s"],

    # --- Nasals ---
    "n": ["n"],
    "m": ["m"],

    # --- Liquids ---
    "l": ["l"],
    "r": ["r"],

    # --- The redundant vowel notation ---
    # In SW script, syllabic signs like ⟨ta⟩ are followed by the
    # vowel sign ⟨a⟩: written ta-a = /ta/.  This redundancy is
    # characteristic and helps identify the script.  We don't model
    # it here since we use Latin transcription of the resolved values.
}

ALLOPHONES_TXR = {
    # Maximally uncertain — we list only what the script forces
    "b": ["b", "p"],
    "t": ["t", "d"],
    "k": ["k", "ɡ"],
    "s": ["s"],
    "n": ["n"],
    "m": ["m"],
    "l": ["l"],
    "r": ["r"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════
# AQUITANIAN (xaq) — the ancestor of Basque
# ═══════════════════════════════════════════════════════════════════════════
#
# Classification: VASCONIC (ancestor of Basque / Euskara)
# This is the earliest attestable stage of the Basque language family,
# known from ~400 personal names and ~70 divine names in Latin
# inscriptions from Roman Aquitania (1st–3rd c. CE).
#
# Attestation:
#   - Roman-era votive altars and funerary inscriptions from the
#     Pyrenean region (Comminges, Couserans, Béarn, Bigorre)
#   - Names written in LATIN ALPHABET by Roman inscribers
#   - No connected text — only onomastic material
#
# The connection to Basque is CERTAIN and universally accepted:
#   - Aquitanian ANDERE = Basque andere "lady/woman"
#   - Aquitanian SEMBE = Basque seme "son"
#   - Aquitanian CISON = Basque gizon "man"
#   - Aquitanian HARS- = Basque hartz "bear"
#   - Aquitanian BELES/BELEX = Basque beltz "black"
#   - Aquitanian -BERRI = Basque berri "new"
#
# PHONOLOGICAL RECONSTRUCTION (Gorrochategui 1984, Lakarra 2006):
# The system matches proto-Basque reconstructions closely:
#   - 5-vowel system /a e i o u/
#   - Aspirate /h/ (preserved in Souletin Basque today)
#   - Sibilant system: /s/ and /ś/ (→ Basque s vs z or s̺ vs s̻)
#   - Two rhotics: /r/ and /ŕ/ (→ Basque tap/trill distinction)
#   - NO /f/ (like Basque; borrowed from Latin/Romance)
#   - NO /p/ initially (like Basque; b- is common, p- is very rare)
#   - Voiceless stops word-initially are rare (Basque pattern)
#   - The affricate /ts/ or /tz/ is attested (BASQUE tz)
#
# Sources:
# - Gorrochategui, J. (1984). *Estudio sobre la onomástica indígena
#   de Aquitania*. UPV/EHU.
# - Lakarra, J.A. (2006). "Protovasco, munda y nostrático."
# - Trask, R.L. (1997). *The History of Basque*. Routledge.
# - Michelena, L. (1961/2011). *Fonética histórica vasca*. Gipuzkoako
#   Foru Aldundia. [= FHV, the foundational work]

GRAPHEMES_XAQ = {
    # --- Vowels (5-vowel system, identical to Basque) ---
    "a": ["a"],
    "e": ["e"],
    "i": ["i"],
    "o": ["o"],
    "u": ["u"],

    # --- Stops ---
    # Proto-Basque/Aquitanian probably had a fortis/lenis distinction
    # rather than a true voice distinction (Michelena's analysis).
    # Word-initial voiceless stops are RARE in native words (like Basque).
    "b": ["b"],
    "p": ["p"],  # rare initially; more common medially
    "d": ["d"],
    "t": ["t"],
    "g": ["ɡ"],
    "c": ["k"],  # Latin spelling convention for /k/
    "k": ["k"],

    # --- Aspirate ---
    # /h/ is well-attested in Aquitanian names (HARS-, HANN-, HER-)
    # and preserved in modern Souletin/Lower Navarrese Basque
    "h": ["h"],

    # --- Sibilants (two, as in Basque) ---
    # Written ⟨s⟩ and ⟨x⟩ or ⟨ss⟩ in Latin transcription
    "s": ["s"],  # possibly apical [s̺]
    "x": ["ʃ"],  # or laminal [s̻]; the "second sibilant"
    "ss": ["s̺"],  # geminate or marked sibilant

    # --- Affricate ---
    "ts": ["ts"],  # → Basque tz
    "tz": ["ts"],  # alternate notation

    # --- Nasals ---
    "n": ["n"],
    "nn": ["ɲ"],  # geminate n → palatal (as in Basque)
    "m": ["m"],

    # --- Liquids ---
    # Two rhotics (tap vs trill), as in Iberian and later Basque
    "r": ["ɾ"],  # simple r → tap
    "rr": ["r"],  # double r → trill
    "l": ["l"],
    "ll": ["ʎ"],  # possibly palatal lateral (Basque pattern)

    # --- Glides ---
    # Attested in diphthongs within names
    "i": ["i", "j"],
    "u": ["u", "w"],
}

ALLOPHONES_XAQ = {
    # Based on comparison with proto-Basque (Michelena/FHV)
    "p": ["p"],
    "b": ["b"],
    "t": ["t"],
    "d": ["d"],
    "k": ["k"],
    "ɡ": ["ɡ"],
    "h": ["h"],
    "s": ["s", "s̺"],
    "ʃ": ["ʃ", "s̻"],
    "ts": ["ts"],
    "n": ["n"],
    "ɲ": ["ɲ"],
    "m": ["m"],
    "ɾ": ["ɾ"],
    "r": ["r"],
    "l": ["l"],
    "ʎ": ["ʎ"],
    "j": ["j"],
    "w": ["w"],
    "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
}

# ═══════════════════════════════════════════════════════════════════════════
# SPECS
# ═══════════════════════════════════════════════════════════════════════════

SPECS = {
    "xce": LanguageSpec(
        code="xce", name="Celtiberian",
        family="Celtic", script="Latin",
        graphemes=GRAPHEMES_XCE, allophones=ALLOPHONES_XCE,
        parent="cel",
        notes=(
            "Celtiberian (3rd–1st c. BCE). Continental Celtic language of "
            "the upper Ebro valley and Meseta. Attested in ~200 inscriptions "
            "in Iberian semi-syllabary and Latin alphabet. Key feature: "
            "Celtic p-loss (no native /p/). Preserves *-nd- cluster. "
            "Intervocalic lenition of stops (pan-Celtic). Five-vowel "
            "system with phonemic length. Two sibilants debated. "
            "Classification: Celtic > Continental > Hispano-Celtic."
        ),
    ),
    "xib": LanguageSpec(
        code="xib", name="Iberian",
        family="Isolate", script="Latin",
        graphemes=GRAPHEMES_XIB, allophones=ALLOPHONES_XIB,
        notes=(
            "Iberian (5th–1st c. BCE). UNCLASSIFIED language isolate of "
            "Mediterranean Iberia. ~2000+ inscriptions in Iberian semi-"
            "syllabary and Greek alphabet. Script is READABLE but language "
            "is UNTRANSLATED. Phonological system inferred from writing: "
            "5 vowels, two sibilants /s/ vs /ś/, two rhotics /r/ vs /ŕ/ "
            "(paralleling Basque), stops with probable voicing distinction "
            "(dual script system). NOT related to Basque despite attempts. "
            "Possibly related to other pre-IE Mediterranean substrates."
        ),
    ),
    "xlg": LanguageSpec(
        code="xlg", name="Lusitanian",
        family="Indo-European", script="Latin",
        graphemes=GRAPHEMES_XLG, allophones=ALLOPHONES_XLG,
        parent="ine",
        notes=(
            "Lusitanian (1st c. BCE). Indo-European language of western "
            "Iberia, known from ~5 inscriptions in Latin alphabet (Cabeço "
            "das Fráguas, Lamas de Moledo, Arroyo de la Luz). PRESERVES "
            "PIE *p (porcom 'pig') — rules out Celtic classification. "
            "Has /f/ (possibly < *bh, suggesting Italic affinity). "
            "Exact IE branch debated: possibly Italic, para-Celtic, or "
            "independent. Key evidence for IE dialectology."
        ),
    ),
    "txr": LanguageSpec(
        code="txr", name="Tartessian (Southwestern)",
        family="Unclassified", script="Latin",
        graphemes=GRAPHEMES_TXR, allophones=ALLOPHONES_TXR,
        notes=(
            "Tartessian / Southwestern (7th–5th c. BCE). ~95 inscriptions "
            "in Southwestern script (Algarve, Alentejo, Huelva). Language "
            "affiliation UNKNOWN — Koch (2011) argues Celtic, de Hoz (2010) "
            "says non-IE, Untermann links to Iberian. Script partially "
            "deciphered; characteristic redundant vowel notation. "
            "THIS IS THE MOST SPECULATIVE ENTRY: only the phonological "
            "distinctions forced by the script structure are modelled. "
            "The voicing distinction in stops is UNRESOLVABLE from the "
            "script alone."
        ),
    ),
    "xaq": LanguageSpec(
        code="xaq", name="Aquitanian (Proto-Basque)",
        family="Vasconic", script="Latin",
        graphemes=GRAPHEMES_XAQ, allophones=ALLOPHONES_XAQ,
        notes=(
            "Aquitanian (1st–3rd c. CE). Ancestor of Basque, known from "
            "~400 personal names and ~70 theonyms in Latin inscriptions "
            "from Roman Aquitania. Connection to Basque CERTAIN: andere "
            "= Basque 'lady', seme = 'son', gizon = 'man', hartz = "
            "'bear'. Phonological system matches proto-Basque: 5 vowels, "
            "aspiration /h/, two sibilants, two rhotics, rare initial "
            "voiceless stops, affricate /ts/. Key evidence for the "
            "antiquity and continuity of the Basque language family."
        ),
    ),
}
