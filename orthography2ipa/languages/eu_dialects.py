"""Basque dialects — grapheme→IPA and allophone mappings.

Basque has traditionally been divided into dialects by Bonaparte (1869)
and refined by Zuazo (2008). The six historical dialects show significant
phonological variation, especially in sibilant systems and aspiration.

Sources:
- Hualde, J.I. (1991). *Basque Phonology*. Routledge.
- Hualde, J.I. & Ortiz de Urbina, J. (2003). *A Grammar of Basque*. Mouton.
- Zuazo, K. (2008). *Euskalkiak: euskararen dialektoak*. Elkar.
- Txillardegi (1980). *Euskal fonologia*. Elkar.
- Oñederra, M.L. (2004). Basque. In: *Fonetika eta fonologia* I.

Conventions:
- eu = Standard Basque (Euskara Batua) — already in base module.
- eu-x-bizkaiera = Biscayan (Western).
- eu-x-gipuzkera = Gipuzkoan (Central).
- eu-x-nafarra-garaia = Upper Navarrese (includes Pamplona basin).
- eu-x-zuberera = Souletin (easternmost, France — included for completeness).
- eu-x-nafarra-beherea = Lower Navarrese (France).
"""
from orthography2ipa.languages.eu import GRAPHEMES, ALLOPHONES
from orthography2ipa.types import LanguageSpec

# ═══════════════════════════════════════════════════════════════════════════
# Biscayan / Bizkaiera (Western Basque)
# Strongest phonological divergence from standard
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_BIZK = {
    **GRAPHEMES,
    # Biscayan: palatalization of sibilants after /i/
    "s": ["s̺", "ʃ"],  # [ʃ] after /i/ in many contexts (busturi)
    "z": ["s̻", "ʃ"],
    # Biscayan often merges some sibilant pairs
}

ALLOPHONES_BIZK = {
    **ALLOPHONES,
    # Sibilant palatalization after /i/
    "s̺": ["s̺", "ʃ"],  # apical → [ʃ] after /i/
    "s̻": ["s̻", "ʃ"],  # laminal → [ʃ] after /i/
    # No aspiration (unlike eastern dialects)
    "h": ["∅"],  # /h/ generally not pronounced
    # Vowel: tendency toward -a raising in unstressed
    "a": ["a", "e"],  # some speakers raise final unstressed /a/
}

# ═══════════════════════════════════════════════════════════════════════════
# Gipuzkoan / Gipuzkera (Central Basque)
# Closest to Batua; reference variety for standardization
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_GIPUZ = {
    **ALLOPHONES,
    # Full sibilant contrasts maintained: apical/laminal/postalveolar
    "s̺": ["s̺"],
    "s̻": ["s̻"],
    "ʃ": ["ʃ"],
    # Aspiration marginal (mainly in borrowed words)
    "h": ["h", "∅"],
    # Palatal stops well preserved
    "c": ["c"],
    "ɟ": ["ɟ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Upper Navarrese / Nafar-Garaia (Southern, Pamplona basin)
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_NAV = {
    **ALLOPHONES,
    # Heavy Spanish influence in phonology
    "s̺": ["s̺", "s"],  # apical/laminal distinction weakening
    "s̻": ["s̻", "s"],
    "h": ["∅"],  # no aspiration
    # Yeísmo tendency from Spanish contact
    "ʎ": ["ʎ", "ʝ"],  # weakening in younger speakers
    # Spanish-like lenition creeping in
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Souletin / Zuberera (easternmost, France)
# Most divergent from standard; preserves /h/ and has /y/
# ═══════════════════════════════════════════════════════════════════════════

GRAPHEMES_ZUB = {
    **GRAPHEMES,
    "ü": ["y"],  # front rounded vowel /y/ (unique among Basque dialects)
    "h": ["h"],  # fully pronounced aspirate
}

ALLOPHONES_ZUB = {
    **ALLOPHONES,
    "h": ["h"],  # aspirate phoneme fully functional
    # Additional vowel /y/ (like French u)
    "y": ["y"],
    # Aspirated stops in some contexts
    "p": ["p", "pʰ"],
    "t": ["t", "tʰ"],
    "k": ["k", "kʰ"],
    # Sibilant system preserved but with different distributions
    "s̺": ["s̺"],
    "s̻": ["s̻"],
    "ʃ": ["ʃ"],
    # More vigorous allophony of voiced stops
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

# ═══════════════════════════════════════════════════════════════════════════
# Lower Navarrese / Nafar-Beherea (France)
# ═══════════════════════════════════════════════════════════════════════════

ALLOPHONES_NAV_BH = {
    **ALLOPHONES,
    "h": ["h"],  # aspirate fully pronounced
    # Aspiration in plosives (less systematic than Souletin)
    "p": ["p", "pʰ"],
    "t": ["t", "tʰ"],
    "k": ["k", "kʰ"],
    "s̺": ["s̺"],
    "s̻": ["s̻"],
    "ʃ": ["ʃ"],
    "b": ["b", "β"],
    "d": ["d", "ð"],
    "ɡ": ["ɡ", "ɣ"],
}

SPECS = {
    "eu-x-bizkaiera": LanguageSpec(
        code="eu-x-bizkaiera",
        name="Biscayan Basque (Bizkaiera)",
        family="Isolate",
        script="Latin",
        graphemes=GRAPHEMES_BIZK,
        allophones=ALLOPHONES_BIZK,
        parent="eu",
        notes=(
            "Biscayan (Bizkaiera/Bizkaia). Western Basque dialect. "
            "Key features: sibilant palatalization after /i/ ([s̺,s̻] → [ʃ]), "
            "loss of aspiration /h/, tendency toward unstressed /a/ raising, "
            "some sibilant pair mergers. Morphologically most divergent from "
            "Batua (unique verb auxiliaries, case forms)."
        ),
    ),
    "eu-x-gipuzkera": LanguageSpec(
        code="eu-x-gipuzkera",
        name="Gipuzkoan Basque (Gipuzkera)",
        family="Isolate",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES_GIPUZ,
        parent="eu",
        notes=(
            "Gipuzkoan (Gipuzkera). Central Basque dialect, closest to "
            "Euskara Batua standard. Full three-way sibilant contrast "
            "maintained (apical/laminal/postalveolar). Palatal stops "
            "[c, ɟ] well preserved. Primary reference variety for "
            "standardization."
        ),
    ),
    "eu-x-nafarra-garaia": LanguageSpec(
        code="eu-x-nafarra-garaia",
        name="Upper Navarrese Basque",
        family="Isolate",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES_NAV,
        parent="eu",
        notes=(
            "Upper Navarrese (Goi-Nafar). Southern Basque dialect including "
            "the Pamplona basin. Heavy Spanish contact influence: "
            "sibilant distinction weakening, incipient yeísmo, "
            "Spanish-like lenition of voiced stops. No aspiration."
        ),
    ),
    "eu-x-zuberera": LanguageSpec(
        code="eu-x-zuberera",
        name="Souletin Basque (Zuberera)",
        family="Isolate",
        script="Latin",
        graphemes=GRAPHEMES_ZUB,
        allophones=ALLOPHONES_ZUB,
        parent="eu",
        notes=(
            "Souletin (Zuberera/Xiberotarra). Easternmost Basque dialect, "
            "spoken in Soule/Zuberoa (France). Most divergent variety. "
            "Unique features: front rounded vowel /y/ (⟨ü⟩, like French), "
            "fully functional aspirate /h/, aspirated stops [pʰ, tʰ, kʰ], "
            "distinctive verb morphology. French phonological influence."
        ),
    ),
    "eu-x-nafarra-beherea": LanguageSpec(
        code="eu-x-nafarra-beherea",
        name="Lower Navarrese Basque",
        family="Isolate",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES_NAV_BH,
        parent="eu",
        notes=(
            "Lower Navarrese (Behe-Nafar). Spoken in Basse-Navarre (France). "
            "Shares aspiration and plosive aspiration features with Souletin "
            "but less systematic. Fully productive /h/. Intermediate between "
            "southern (Spanish-side) and eastern (Souletin) varieties."
        ),
    ),
}
