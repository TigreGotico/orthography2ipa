"""
adapted from: https://github.com/lingz/pyphone - MIT License

Distinctive-feature matrix for IPA phones used by PyPhone.

This table encodes a hybrid SPE/IPA feature system for segment-to-segment
distance computation and classification. Each phone maps to a vector of
21 features. Features are boolean where applicable; `None` denotes that
a feature is not defined for a particular phone.

Feature index layout (0–20):

0  syllabic              — Major-class feature
1  sonorant              — Major-class feature
2  consonantal           — Major-class feature
3  continuant            — Manner feature
4  delayed_release       — Affrication feature
5  lateral               — Lateral airflow
6  nasal                 — Nasality
7  strident              — Sibilance/noise
8  voice                 — Voicing
9  spread_glottis        — Aspiration
10 constricted_glottis   — Ejective/creaky articulation
11 anterior              — Coronal place (dental/alveolar)
12 coronal               — Coronal major place
13 distributed           — Blade vs tip distinction
14 labial                — Labial place (bilabial/labiodental)
15 high                  — High vowel/glide or palatal consonant
16 low                   — Low vowel or pharyngealization
17 back                  — Back vowel or dorsal consonant
18 round                 — Lip rounding or labiovelar articulation
19 tense                 — Vowel tenseness
20 long                  — Length mark (ː)

The feature system aligns with features used in generative phonology
and acoustic modeling, but values are hand-curated for each IPA symbol.
"""
import warnings
from typing import Any, Dict, List, Optional, Union

import numpy as np

NUM_FEATURES = 23

# ---------------------------------------------------------------------------
# phone_features:
#   A mapping of IPA phones to a 21-element feature vector.
#
# Notes:
# - Values are manually derived from articulatory definitions in IPA
#   and standard distinctive-feature systems.
# - `None` indicates the feature is not defined for the phone's class.
# - Used internally for computing similarity/distance between phones.
# ---------------------------------------------------------------------------

phone_features: Dict[str, List[Optional[bool]]] = {
    # Example (one phone explained as template):
    #
    # "c": [
    #   False,  # 0 syllabic — stops are not syllabic
    #   False,  # 1 sonorant — stops are not sonorant
    #   True,   # 2 consonantal — major-class consonant
    #   False,  # 3 continuant — plosive stops are non-continuant
    #   False,  # 4 delayed_release — not an affricate
    #   False,  # 5 lateral — not lateral
    #   False,  # 6 nasal — not nasal
    #   None,   # 7 strident — stridency undefined for non-fricative stops
    #   False,  # 8 voice — voiceless
    #   False,  # 9 spread_glottis — not aspirated
    #   False,  # 10 constricted_glottis — no ejective/creaky state
    #   False,  # 11 anterior — velars not coronal/anterior
    #   False,  # 12 coronal — velars are dorsal, not coronal
    #   None,   # 13 distributed — irrelevant for dorsals
    #   False,  # 14 labial — not labial
    #   True,   # 15 high — dorsal place implies [+high] in SPE terms
    #   False,  # 16 low — not low
    #   False,  # 17 back — front velar [c] is [-back]
    #   False,  # 18 round — not rounded
    #   None,   # 19 tense — undefined for consonants
    #   False,  # 20 long — not lengthened
    # ],
    #
    # All other entries follow the same feature-index ordering.
    # -----------------------------------------------------------------------
    # Feature indices 0-20: original 21 features
    # Feature index 21: click (True for click consonants)
    # Feature index 22: nasal_vowel (True for nasalized vowels)
    #
    # All existing phones get False for indices 21 and 22.
    # -----------------------------------------------------------------------
    # Plosives / stops
    "c": [False, False, True, False, False, False, False, None, False, False, False, False, False, None, False, True,
          False, False, False, None, False, False, False],
    "ɡ": [False, False, True, False, False, False, False, None, True, False, False, False, False, None, False, True,
          False, True, False, None, False, False, False],
    "k": [False, False, True, False, False, False, False, None, False, False, False, False, False, None, False, True,
          False, True, False, None, False, False, False],
    "q": [False, False, True, False, False, False, False, None, False, False, False, False, False, None, False, False,
          False, True, False, None, False, False, False],
    "ɖ": [False, False, True, False, False, False, False, None, True, False, False, False, True, False, False, False,
          False, False, False, None, False, False, False],
    "ɟ": [False, False, True, False, False, False, False, None, True, False, False, False, False, None, False, True,
          False, False, False, None, False, False, False],
    "ɠ": [False, False, True, False, False, False, False, None, True, False, True, False, False, None, False, True,
          False, True, False, None, False, False, False],
    "ɢ": [False, False, True, False, False, False, False, None, True, False, False, False, False, None, False, False,
          False, True, False, None, False, False, False],
    "ʄ": [False, False, True, False, False, False, False, None, True, False, True, False, False, None, False, True,
          False, False, False, None, False, False, False],
    "ʈ": [False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False,
          False, False, False, None, False, False, False],
    "ʛ": [False, False, True, False, False, False, False, None, True, False, True, False, False, None, False, False,
          False, True, False, None, False, False, False],
    "b": [False, False, True, False, False, False, False, None, True, False, False, True, False, None, True, False,
          False, False, False, None, False, False, False],
    "d": [False, False, True, False, False, False, False, False, True, False, False, True, True, False, False, False,
          False, False, False, None, False, False, False],
    "p": [False, False, True, False, False, False, False, None, False, False, False, True, False, None, True, False,
          False, False, False, None, False, False, False],
    "t": [False, False, True, False, False, False, False, False, False, False, False, True, True, False, False, False,
          False, False, False, None, False, False, False],
    "ɓ": [False, False, True, False, False, False, False, None, True, False, True, True, False, None, True, False,
          False, False, False, None, False, False, False],
    "ɗ": [False, False, True, False, False, False, False, False, True, False, True, True, True, False, False, False,
          False, False, False, None, False, False, False],
    # Fricatives
    "x": [False, False, True, True, False, False, False, None, False, False, False, False, False, None, False, True,
          False, True, False, None, False, False, False],
    "ç": [False, False, True, True, False, False, False, None, False, False, False, False, False, None, False, True,
          False, False, False, None, False, False, False],
    "ħ": [False, False, True, True, False, False, False, None, False, False, False, False, False, None, False, False,
          True, True, False, None, False, False, False],
    "ɣ": [False, False, True, True, False, False, False, None, True, False, False, False, False, None, False, True,
          False, True, False, None, False, False, False],
    "ʁ": [False, False, True, True, False, False, False, None, True, False, False, False, False, None, False, False,
          False, True, False, None, False, False, False],
    "ʂ": [False, False, True, True, False, False, False, True, False, False, False, False, True, False, False, False,
          False, False, False, None, False, False, False],
    "ʃ": [False, False, True, True, False, False, False, True, False, False, False, False, True, True, False, False,
          False, False, False, None, False, False, False],
    "ʐ": [False, False, True, True, False, False, False, True, True, False, False, False, True, False, False, False,
          False, False, False, None, False, False, False],
    "ʒ": [False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False,
          False, False, False, None, False, False, False],
    "ʕ": [False, False, True, True, False, False, False, None, True, False, False, False, False, None, False, False,
          True, True, False, None, False, False, False],
    "ʝ": [False, False, True, True, False, False, False, None, True, False, False, False, False, None, False, True,
          False, False, False, None, False, False, False],
    "χ": [False, False, True, True, False, False, False, None, False, False, False, False, False, None, False, False,
          False, True, False, None, False, False, False],
    "f": [False, False, True, True, False, False, False, None, False, False, False, True, False, None, True, False,
          False, False, False, None, False, False, False],
    "s": [False, False, True, True, False, False, False, True, False, False, False, True, True, False, False, False,
          False, False, False, None, False, False, False],
    "v": [False, False, True, True, False, False, False, None, True, False, False, True, False, None, True, False,
          False, False, False, None, False, False, False],
    "z": [False, False, True, True, False, False, False, True, True, False, False, True, True, False, False, False,
          False, False, False, None, False, False, False],
    "ð": [False, False, True, True, False, False, False, False, True, False, False, True, True, True, False, False,
          False, False, False, None, False, False, False],
    "ɸ": [False, False, True, True, False, False, False, None, False, False, False, True, False, None, True, False,
          False, False, False, None, False, False, False],
    "β": [False, False, True, True, False, False, False, None, True, False, False, True, False, None, True, False,
          False, False, False, None, False, False, False],
    "θ": [False, False, True, True, False, False, False, False, False, False, False, True, True, True, False, False,
          False, False, False, None, False, False, False],
    "ɧ": [False, False, True, True, True, False, False, None, False, False, False, False, True, True, False, True,
          False, None, False, None, False, False, False],
    "ɕ": [False, False, True, True, True, False, False, True, False, False, False, True, True, True, False, True, False,
          False, False, None, False, False, False],
    "ɬ": [False, False, True, True, True, True, False, False, False, False, False, True, True, False, False, None, None,
          None, False, None, False, False, False],
    "ɮ": [False, False, True, True, True, True, False, False, True, False, False, True, True, False, False, None, None,
          None, False, None, False, False, False],
    "ʑ": [False, False, True, True, True, False, False, True, True, False, False, True, True, True, False, True, False,
          False, False, None, False, False, False],
    # Nasals
    "ɱ": [False, True, True, False, None, False, True, None, True, False, False, True, False, None, True, None, None,
          None, False, None, False, False, False],
    "ʔ": [False, True, False, False, False, False, False, None, False, False, True, False, False, None, False, False,
          False, False, False, None, False, False, False],
    "ŋ": [False, True, True, False, False, False, True, None, True, False, False, False, False, None, False, True,
          False, True, False, None, False, False, False],
    "ɳ": [False, True, True, False, False, False, True, False, True, False, False, False, True, None, False, False,
          False, False, False, None, False, False, False],
    "ɴ": [False, True, True, False, False, False, True, None, True, False, False, False, False, None, False, False,
          False, True, False, None, False, False, False],
    "m": [False, True, True, False, False, False, True, None, True, False, False, True, False, None, True, False, False,
          False, False, None, False, False, False],
    "n": [False, True, True, False, False, False, True, False, True, False, False, True, True, False, False, False,
          False, False, False, None, False, False, False],
    "ɲ": [False, True, True, False, False, False, True, False, True, False, False, True, False, None, False, True,
          False, False, False, None, False, False, False],
    # Approximants / glides
    "ɥ": [False, True, False, True, None, False, False, None, True, False, False, None, False, None, True, True, False,
          False, True, True, False, False, False],
    "ɰ": [False, True, False, True, None, False, False, None, True, False, False, None, False, None, False, True, False,
          None, False, True, False, False, False],
    "ʋ": [False, True, False, True, None, False, False, None, True, False, False, True, False, None, True, None, None,
          None, False, None, False, False, False],
    "ʀ": [False, True, True, True, None, False, False, None, True, False, False, None, False, None, False, False, False,
          True, False, None, False, False, False],
    "ʙ": [False, True, True, True, None, False, False, None, True, False, False, True, False, None, True, None, None,
          None, False, None, False, False, False],
    "ʟ": [False, True, True, True, None, True, False, None, True, False, False, None, False, None, False, True, False,
          None, False, None, False, False, False],
    "ɭ": [False, True, True, True, None, True, False, False, True, False, False, False, True, False, False, None, None,
          None, False, None, False, False, False],
    "ɽ": [False, True, True, True, None, False, False, False, True, False, False, False, True, False, False, None, None,
          None, False, None, False, False, False],
    "ʎ": [False, True, True, True, None, True, False, None, True, False, False, False, True, True, False, True, False,
          False, False, None, False, False, False],
    "r": [False, True, True, True, None, False, False, False, True, False, False, True, True, False, False, None, None,
          None, False, None, False, False, False],
    "ɫ": [False, True, True, True, None, True, False, False, True, False, False, True, True, False, False, False, False,
          True, False, None, False, False, False],
    "ɺ": [False, True, True, True, None, True, False, False, True, False, False, True, True, False, False, None, None,
          None, False, None, False, False, False],
    "ɾ": [False, True, True, True, None, False, False, False, True, False, False, True, True, False, False, None, None,
          None, False, None, False, False, False],
    "ʍ": [False, True, False, True, False, False, False, None, False, False, False, False, False, None, True, True,
          False, True, True, None, False, False, False],
    "h": [False, True, True, True, False, False, False, False, False, False, False, False, False, None, False, False,
          False, False, False, None, False, False, False],
    "j": [False, True, False, True, False, False, False, None, True, False, False, False, False, None, False, True,
          False, False, False, None, False, False, False],
    "w": [False, True, False, True, False, False, False, None, True, False, False, False, False, None, True, True,
          False, True, True, None, False, False, False],
    "ɹ": [False, True, False, True, False, False, False, False, True, False, False, False, True, False, False, True,
          False, True, True, None, False, False, False],
    "ɻ": [False, True, False, True, False, False, False, False, True, False, False, False, True, False, False, False,
          False, False, False, None, False, False, False],
    "l": [False, True, True, True, False, True, False, False, True, False, False, True, True, False, False, False,
          False, False, False, None, False, False, False],
    "ɦ": [False, True, True, True, False, False, False, None, False, False, False, False, False, None, False, False,
          False, False, False, None, False, False, False],
    # Vowels (oral)
    "ɑ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, False, False,
          True, True, False, True, False, False, False],
    "ɘ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, False, False,
          False, False, False, True, False, False, False],
    "ɞ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, True, False,
          False, False, True, False, False, False, False],
    "ɤ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, False, False,
          False, True, False, True, False, False, False],
    "ɵ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, True, False,
          False, False, True, True, False, False, False],
    "ʉ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, True, True, False,
          False, True, True, False, False, False],
    "a": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          True, True, False, True, False, False, False],
    "e": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          False, False, False, True, False, False, False],
    "i": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True,
          False, False, False, True, False, False, False],
    "o": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          False, True, True, True, False, False, False],
    "u": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, True, True,
          False, True, True, True, False, False, False],
    "y": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, True, True,
          False, False, True, True, False, False, False],
    "æ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          True, False, False, True, False, False, False],
    "ø": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          False, False, True, True, False, False, False],
    "œ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          False, False, True, False, False, False, False],
    "ɒ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          True, True, True, True, False, False, False],
    "ɔ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          False, True, True, False, False, False, False],
    "ə": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          False, True, False, False, False, False, False],
    "ɜ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          False, True, False, True, False, False, False],
    "ɛ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False],
    "ɨ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True,
          False, True, False, True, False, False, False],
    "ɪ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True,
          False, False, False, False, False, False, False],
    "ɯ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True,
          False, True, False, False, False, False, False],
    "ɶ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          True, False, True, True, False, False, False],
    "ʊ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True,
          False, True, True, False, False, False, False],
    "ɐ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          False, True, False, True, False, False, False],
    "ʌ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False,
          False, True, False, True, False, False, False],
    "ʏ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True,
          False, False, True, False, False, False, False],
    # ─── Click consonants ───────────────────────────────────────────────
    # Clicks: non-syllabic, non-sonorant, consonantal, non-continuant stops
    # with click=True (idx 21). Place varies by click type.
    "ǀ": [False, False, True, False, False, False, False, None, False, False, False, True, True, True, False, False,
           False, False, False, None, False, True, False],   # dental click
    "ǁ": [False, False, True, False, False, True, False, None, False, False, False, True, True, False, False, False,
           False, False, False, None, False, True, False],   # lateral click
    "ǂ": [False, False, True, False, False, False, False, None, False, False, False, False, True, True, False, True,
           False, False, False, None, False, True, False],   # palatal click
    "ǃ": [False, False, True, False, False, False, False, None, False, False, False, True, True, False, False, False,
           False, False, False, None, False, True, False],   # alveolar click
    "ʘ": [False, False, True, False, False, False, False, None, False, False, False, True, False, None, True, False,
           False, False, False, None, False, True, False],   # bilabial click
    # ─── Ejective stops ─────────────────────────────────────────────────
    # Ejectives: voiceless, constricted_glottis=True
    "pʼ": [False, False, True, False, False, False, False, None, False, False, True, True, False, None, True, False,
            False, False, False, None, False, False, False],
    "tʼ": [False, False, True, False, False, False, False, False, False, False, True, True, True, False, False, False,
            False, False, False, None, False, False, False],
    "kʼ": [False, False, True, False, False, False, False, None, False, False, True, False, False, None, False, True,
            False, True, False, None, False, False, False],
    "qʼ": [False, False, True, False, False, False, False, None, False, False, True, False, False, None, False, False,
            False, True, False, None, False, False, False],
    "tsʼ": [False, False, True, False, True, False, False, True, False, False, True, True, True, False, False, False,
             False, False, False, None, False, False, False],
    "tʃʼ": [False, False, True, False, True, False, False, True, False, False, True, False, True, True, False, False,
             False, False, False, None, False, False, False],
    # ─── Prenasalized stops ─────────────────────────────────────────────
    "ᵐb": [False, False, True, False, False, False, True, None, True, False, False, True, False, None, True, False,
            False, False, False, None, False, False, False],
    "ⁿd": [False, False, True, False, False, False, True, False, True, False, False, True, True, False, False, False,
            False, False, False, None, False, False, False],
    "ᵑɡ": [False, False, True, False, False, False, True, None, True, False, False, False, False, None, False, True,
            False, True, False, None, False, False, False],
    # ─── Nasalized vowels ───────────────────────────────────────────────
    # Nasalized vowels: same as oral counterpart but nasal=True, nasal_vowel=True (idx 22)
    "ã": [True, True, False, True, False, False, True, None, True, False, False, False, False, False, False, False,
          True, True, False, True, False, False, True],
    "ẽ": [True, True, False, True, False, False, True, None, True, False, False, False, False, False, False, False,
          False, False, False, True, False, False, True],
    "ĩ": [True, True, False, True, False, False, True, None, True, False, False, False, False, False, False, True,
          False, False, False, True, False, False, True],
    "õ": [True, True, False, True, False, False, True, None, True, False, False, False, False, False, False, False,
          False, True, True, True, False, False, True],
    "ũ": [True, True, False, True, False, False, True, None, True, False, False, False, False, False, True, True,
          False, True, True, True, False, False, True],
}

# ---------------------------------------------------------------------------
# vowel_features / consonant_features:
#   Feature index sets used when computing similarity metrics.
#   They define which features contribute to vowel or consonant distance.
# ---------------------------------------------------------------------------

vowel_features = {
    0,  # syllabic
    1,  # sonorant
    3,  # continuant
    8,  # voice
    14,  # labial (relevant for rounding/labiality in vowels)
    15,  # high
    16,  # low
    17,  # back
    18,  # round
    19,  # tense
    20,  # long
    22,  # nasal_vowel
}

consonant_features = {
    1, 2, 3, 4, 5, 6, 7, 8, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19,
    21,  # click
}

# ---------------------------------------------------------------------------
# modifiers:
#   IPA diacritics that flip or assign features.
#   Each dictionary maps a feature index to the updated boolean value.
# ---------------------------------------------------------------------------

modifiers = {
    "ː": {20: True},  # length mark: [+long]

    " ̻": {13: True},  # laminal articulation: [+distributed]

    "ˤ": {  # pharyngealization: typically [+back, +low]
        16: True,
        17: True,
    },

    "˞": {  # rhoticization
        11: False,  # rhotics are non-anterior
        15: True,  # raised/tighter tongue position
        18: True,  # lip rounding (common in approximant rhotics)
    },

    "̃": {  # nasalization: [+nasal, +nasal_vowel]
        6: True,
        22: True,
    },

    "̥": {  # voicelessness: [-voice]
        8: False,
    },

    "ʲ": {  # palatalization: [+high, -back]
        15: True,
        17: False,
    },

    "ʷ": {  # labialization: [+labial, +round]
        14: True,
        18: True,
    },

    "ⁿ": {  # prenasalization: [+nasal]
        6: True,
    },

    "ʼ": {  # ejective: [+constricted_glottis]
        10: True,
    },
}

# ---------------------------------------------------------------------------
# Weights used for feature-distance scoring.
# feature_weights[i] gives the weight of feature index i.
#
# Values are hand-tuned. Higher weights correspond to major-class features.
# ---------------------------------------------------------------------------

feature_weights = [
    0.13793103448275862,  # 0 syllabic          (major class)
    0.13793103448275862,  # 1 sonorant          (major class)
    0.13793103448275862,  # 2 consonantal       (major class)
    0.06896551724137931,  # 3 continuant
    0.03448275862068965,  # 4 delayed release
    0.03448275862068965,  # 5 lateral
    0.03448275862068965,  # 6 nasal
    0.01724137931034483,  # 7 strident
    0.01724137931034483,  # 8 voice
    0.01724137931034483,  # 9 spread_glottis
    0.01724137931034483,  # 10 constricted_glottis
    0.03448275862068965,  # 11 anterior
    0.03448275862068965,  # 12 coronal
    0.01724137931034483,  # 13 distributed
    0.03448275862068965,  # 14 labial
    0.03448275862068965,  # 15 high
    0.03448275862068965,  # 16 low
    0.03448275862068965,  # 17 back
    0.03448275862068965,  # 18 round
    0.03448275862068965,  # 19 tense
    0.01724137931034483,  # 20 long
    0.01724137931034483,  # 21 click
    0.01724137931034483,  # 22 nasal_vowel
]

total_vowel_weight = sum(feature_weights[i] for i in vowel_features)
total_consonant_weight = sum(feature_weights[i] for i in consonant_features)

standard_weights = [1 / NUM_FEATURES] * NUM_FEATURES
zero_weights = [0] * NUM_FEATURES

# Cache for feature vectors of composite phones.
# Composite phones (like "ɜ˞") require merging multiple feature sets.
# Since merging costs time, we store results after first computation.
_phone_memory = {}

# Normalization table for irregular or ambiguous IPA symbols.
# When a phone appears in this map, it should be replaced with the canonical form.
_bad_phones = {
    "ɝ": "ɜ˞",
}


def vectorize_phones(phones: str) -> List[Union[bool, None]]:
    """
    Resolve a phone or phone-with-modifiers into a phonetic feature vector.

    Phones can be:
        - A single IPA symbol (e.g. "p", "a", "ʒ")
        - A composite sequence (e.g. "ɜ˞") where modifiers adjust features

    How this works:
        1. If the phone is known to require normalization, normalize it.
        2. If the phone consists of exactly one symbol:
              return its feature vector directly.
        3. If it contains multiple symbols:
              • Some symbols represent modifiers that override features.
              • Others represent base phones that contribute their features.
              • We merge the base features first.
              • Then we apply modifiers that overwrite specific features.

    Feature vector rules:
        - Each feature index holds True, False, or None (unknown/irrelevant).
        - When merging:
              • A True anywhere forces the feature True.
              • Otherwise, if any base phone sets False, keep False.
              • If all base phones leave a feature None, it remains None.
        - Modifiers overwrite final values for specific feature indices.
    """
    global _phone_memory

    if not phones:
        raise ValueError("Phone is empty or None.")

    # --- Step 1: normalize irregular phones ---
    if phones in _bad_phones:
        phones = _bad_phones[phones]

    # --- Step 2: fast path for simple phones ---
    if len(phones) == 1:
        try:
            return phone_features[phones]
        except KeyError:
            raise ValueError(f"Unrecognized phone '{phones}'")

    # --- Step 3: cached result for composite phones ---
    if phones in _phone_memory:
        return tuple(_phone_memory[phones])

    # --- Step 4: compute vector for composite phone ---
    try:
        # Start with an empty feature list (None = no information yet)
        vec = [None] * NUM_FEATURES

        # A list of modifier dicts that will be applied later
        new_modifiers = []

        # Merge all base phone feature contributions
        #
        # For every feature index, we scan all characters:
        #   - If character is a modifier, mark for later.
        #   - If character is a base phone, check its feature value.
        #
        # Merging logic:
        #   True dominates everything (immediate)
        #   False sets only if we have not seen a True
        #   None means "no influence" unless no other phones give a value
        #
        for f_idx in range(NUM_FEATURES):
            merged_val = None
            for p in phones:
                if p in modifiers:
                    new_modifiers.append(modifiers[p])
                    continue

                # Base phone feature lookup
                base_val = phone_features[p][f_idx]

                # Dominance rule: True > False > None
                if base_val is True:
                    merged_val = True
                    break
                elif base_val is False:
                    merged_val = False

            vec[f_idx] = merged_val

        # Apply modifiers, which can overwrite any feature position.
        # Modifiers represent diacritics or IPA secondary articulations.
        for mod in new_modifiers:
            for feature_idx, mod_val in mod.items():
                vec[feature_idx] = mod_val

        # Save result to cache
        vec = tuple(vec)
        _phone_memory[phones] = vec
        return vec

    except KeyError as e:
        raise ValueError(f"Unrecognized phone '{e.args[0]}'")


def is_vowel_phone(phone: str) -> bool:
    """
    Return True if the phone is a vowel, else False.

    Convention:
        The data model places the vowel/consonant flag in feature[0].
        A True at feature[0] means vowel.
    """
    try:
        return vectorize_phones(phone)[0]
    except (ValueError, KeyError, IndexError):
        return False


def phonetic_distance(phone_a: str, phone_b: str) -> float:
    """
    Compute a normalized phonetic distance between two IPA phones.

    Key rules:
        - Space ' ' is considered a phone but can only match itself.
        - Vowel ↔ consonant mismatches always yield distance = 1.0.
        - Otherwise, distance is computed from weighted feature mismatches.
        - The mismatch sum is normalized by a precomputed total weight.
        - Consonants are scaled by factor 2.0; vowels by 1.0.

    Algorithm:
        1. Handle special case: if either phone is a space.
        2. If one is vowel and the other is consonant → return 1.0.
        3. Determine if phones are vowels or consonants.
        4. Select feature subset and normalization constants:
              vowels → smaller set, factor 1
              consonants → larger set, factor 2
        5. Retrieve feature vectors.
        6. Compare only the relevant feature indices:
              if vecA[i] != vecB[i], add weight[i] to difference sum.
        7. Normalize difference sum:
              distance = (difference_sum / total_weight) * factor

    Result Range:
        • For vowels: 0 → 1
        • For consonants: 0 → 2 (due to factor 2)
    """
    # --- Step 1: special-case for space phones ---
    if phone_a == ' ' or phone_b == ' ':
        # Identical spaces match with distance 0, else fully dissimilar
        return 0.0 if phone_a == phone_b else 1.0

    # --- Step 2: vowel/consonant mismatch ---
    vowel = is_vowel_phone(phone_a)
    if vowel != is_vowel_phone(phone_b):
        return 1.0

    # --- Step 3: choose feature subset and scaling factor ---
    if vowel:
        # Vowels use a limited feature set and factor = 1
        total_weights = total_vowel_weight
        feature_indices = vowel_features
        factor = 1.0
    else:
        # Consonants use more features and factor = 2
        total_weights = total_consonant_weight
        feature_indices = consonant_features
        factor = 2.0

    # --- Step 4: retrieve merged feature vectors ---
    try:
        vecA = vectorize_phones(phone_a)
        vecB = vectorize_phones(phone_b)
    except (ValueError, KeyError, IndexError):
        return 3.0

    # --- Step 5: accumulate weighted mismatches ---
    diff_sum = 0.0
    for idx in feature_indices:
        # Any inequality counts as a mismatch
        if vecA[idx] != vecB[idx]:
            diff_sum += feature_weights[idx]

    # --- Step 6: normalize & scale ---
    return (diff_sum / total_weights) * factor


def phoneme_embeddings(spec: "LanguageSpec") -> "dict[str, Any]":
    """Deprecated: moved to orthography2ipa.lm.phoneme_embeddings."""
    warnings.warn(
        "orthography2ipa.feats.phoneme_embeddings is deprecated; "
        "use orthography2ipa.lm.phoneme_embeddings instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    from orthography2ipa.lm import phoneme_embeddings as _impl
    return _impl(spec)


def build_ngram_lm(words: "list[str]", spec: "LanguageSpec", n: int = 3) -> dict:
    """Deprecated: moved to orthography2ipa.lm.build_ngram_lm."""
    warnings.warn(
        "orthography2ipa.feats.build_ngram_lm is deprecated; "
        "use orthography2ipa.lm.build_ngram_lm instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    from orthography2ipa.lm import build_ngram_lm as _impl
    return _impl(words, spec, n)


def perplexity(lm: dict, test_words: "list[str]", spec: "LanguageSpec", n: int = 3) -> float:
    """Deprecated: moved to orthography2ipa.lm.perplexity."""
    warnings.warn(
        "orthography2ipa.feats.perplexity is deprecated; "
        "use orthography2ipa.lm.perplexity instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    from orthography2ipa.lm import perplexity as _impl
    return _impl(lm, test_words, spec, n)
