"""Proto-Indo-European (ine) — reconstructed grapheme→IPA and allophone mappings.

PIE is the reconstructed common ancestor of the Indo-European language
family (~4500–2500 BCE, Pontic-Caspian steppe hypothesis). The phonological
system is well-established through the comparative method, though details
remain debated.

This module uses the STANDARD NOTATION system of Indo-Europeanist
linguistics. The "graphemes" here are the conventional reconstruction
symbols (preceded by * in running text, but stored without *).

Sources:
- Fortson, B.W. (2010). *Indo-European Language and Culture*. 2nd ed. Blackwell.
- Ringe, D. (2006). *From Proto-Indo-European to Proto-Germanic*. OUP.
- Meier-Brügger, M. (2003). *Indo-European Linguistics*. De Gruyter.
- Beekes, R.S.P. (2011). *Comparative Indo-European Linguistics*. 2nd ed. Benjamins.
- Byrd, A.M. (2015). *The Indo-European Syllable*. Brill.
- Kümmel, M.J. (2007). *Konsonantenwandel*. Reichert.

Conventions:
- ISO 639-5: ine (Indo-European family); no ISO 639-3 for PIE itself.
- Notation: standard comparative IE symbols.
- Laryngeals: h₁ h₂ h₃ (= *H, *Ha, *Ho in some traditions).
- "Voiced aspirated" series: written bʰ dʰ ɡʰ etc. (= "breathy voiced"
  or "murmured" — exact phonetic value debated).
- Labiovelars: kʷ ɡʷ ɡʷʰ.
- Syllabic resonants: m̥ n̥ l̥ r̥.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # ═══════════════════════════════════════════════════════════════════
    # STOPS — the three-way laryngeal contrast
    # Voiceless / Voiced / Voiced aspirated (or "breathy")
    # ═══════════════════════════════════════════════════════════════════

    # Labial
    "p": ["p"],
    "b": ["b"],
    "bʰ": ["bʱ"],  # breathy voiced (murmured)

    # Dental/Alveolar
    "t": ["t"],
    "d": ["d"],
    "dʰ": ["dʱ"],

    # Velar (plain)
    "k": ["k"],
    "g": ["ɡ"],
    "gʰ": ["ɡʱ"],

    # Labiovelar
    "kʷ": ["kʷ"],
    "gʷ": ["ɡʷ"],
    "gʷʰ": ["ɡʷʱ"],

    # ═══════════════════════════════════════════════════════════════════
    # FRICATIVE
    # ═══════════════════════════════════════════════════════════════════
    "s": ["s"],

    # ═══════════════════════════════════════════════════════════════════
    # LARYNGEALS — the three "H" phonemes
    # Exact phonetic values debated; conventional IPA approximations
    # ═══════════════════════════════════════════════════════════════════
    "h₁": ["h"],  # "neutral" laryngeal; possibly [h] or [ʔ]
    "h₂": ["ħ"],  # "a-colouring"; possibly [ħ], [χ], or [ʕ]
    "h₃": ["hʷ"],  # "o-colouring"; possibly [hʷ], [ɣʷ], or [ʕʷ]

    # ═══════════════════════════════════════════════════════════════════
    # RESONANTS (sonorants) — consonantal forms
    # ═══════════════════════════════════════════════════════════════════
    "m": ["m"],
    "n": ["n"],
    "l": ["l"],
    "r": ["r"],

    # Glides
    "y": ["j"],  # palatal glide (*y in PIE notation)
    "w": ["w"],  # labial-velar glide

    # ═══════════════════════════════════════════════════════════════════
    # SYLLABIC RESONANTS — vocalic allophones of sonorants
    # ═══════════════════════════════════════════════════════════════════
    "m̥": ["m̩"],  # syllabic m (> Gk. α, Lat. em/am, Skt. a)
    "n̥": ["n̩"],  # syllabic n (> Gk. α, Lat. en/an, Skt. a)
    "l̥": ["l̩"],  # syllabic l (> Gk. αλ/λα, Lat. ol, Skt. r̥)
    "r̥": ["r̩"],  # syllabic r (> Gk. αρ/ρα, Lat. or, Skt. r̥)

    # ═══════════════════════════════════════════════════════════════════
    # VOWELS — the ablaut system
    # PIE had only *e and *o at the basic level; *ē *ō are lengthened grades
    # ═══════════════════════════════════════════════════════════════════

    # Short (e-grade and o-grade)
    "e": ["e"],  # basic "e-grade" (the default ablaut vowel)
    "o": ["o"],  # "o-grade"
    "a": ["a"],  # rare; possibly from *h₂e

    # Long (lengthened grade)
    "ē": ["eː"],
    "ō": ["oː"],
    "ā": ["aː"],  # rare; from *eh₂

    # Schwa (reduced/zero grade with laryngeal)
    "ə": ["ə"],  # "schwa indogermanicum" — laryngeal vocalisation
}

ALLOPHONES = {
    # Voiceless stops
    "p": ["p"],
    "t": ["t"],
    "k": ["k"],
    "kʷ": ["kʷ"],

    # Voiced stops
    "b": ["b"],
    "d": ["d"],
    "ɡ": ["ɡ"],
    "ɡʷ": ["ɡʷ"],

    # Breathy/murmured voiced stops (phonetic value debated)
    "bʱ": ["bʱ", "bʰ"],
    "dʱ": ["dʱ", "dʰ"],
    "ɡʱ": ["ɡʱ", "ɡʰ"],
    "ɡʷʱ": ["ɡʷʱ", "ɡʷʰ"],

    # Fricative
    "s": ["s", "z"],  # [z] allophone before voiced stops

    # Laryngeals (all approximate — exact values unknown)
    "h": ["h", "ʔ"],  # h₁
    "ħ": ["ħ", "χ", "ʕ"],  # h₂
    "hʷ": ["hʷ", "ɣʷ"],  # h₃

    # Nasals
    "m": ["m"],
    "n": ["n", "ŋ"],  # [ŋ] before velars
    "m̩": ["m̩"],
    "n̩": ["n̩"],

    # Liquids
    "l": ["l"],
    "r": ["r"],
    "l̩": ["l̩"],
    "r̩": ["r̩"],

    # Glides
    "j": ["j"],
    "w": ["w"],

    # Vowels
    "e": ["e"],
    "o": ["o"],
    "a": ["a"],
    "eː": ["eː"],
    "oː": ["oː"],
    "aː": ["aː"],
    "ə": ["ə"],
}

SPECS = {
    "ine": LanguageSpec(
        code="ine",
        name="Proto-Indo-European (reconstructed)",
        family="Indo-European",
        script="Latin",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        notes=(
            "Reconstructed Proto-Indo-European phonology (~4500–2500 BCE). "
            "Standard comparative reconstruction per Fortson (2010), Ringe "
            "(2006), Beekes (2011). Three-way stop contrast: voiceless / "
            "voiced / breathy-voiced (the 'voiced aspirates'). Three "
            "laryngeals (h₁ h₂ h₃) with debated phonetic values — h₁ "
            "neutral, h₂ a-colouring, h₃ o-colouring. Labiovelar series "
            "(kʷ gʷ gʷʰ). Single fricative /s/ (with [z] allophone). "
            "Ablaut system: e-grade / o-grade / zero-grade / lengthened "
            "grade. Syllabic sonorants (m̥ n̥ l̥ r̥). The system here "
            "represents the 'standard' reconstruction; glottalic theory "
            "and other alternative models are not reflected."
        ),
    ),
}
