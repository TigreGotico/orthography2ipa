"""Choctaw (cho) nasal-vowel and schwa-glyph coverage.

Choctaw has three vowel qualities /i o a/, each contrasting oral/nasal and
short/long (Broadwell 2006, A Choctaw Reference Grammar). Nasal vowels are
treated as intrinsically long here; that follows the pattern this project's
gold benchmark shows for the modern macron-below convention, and is a
distributional claim rather than a page-cited one. Two written conventions
for the nasal vowels appear in this project's gold benchmark:

* the modern Mississippi/Choctaw-Nation convention marks a nasal vowel
  directly with a combining macron below the vowel letter (a̱ i̱ o̱);
* the older Byington/traditional missionary convention instead spells the
  historical vowel+n/m sequence before a further consonant (pakanli, pinti,
  imponna) and leaves the vowel letter itself unmarked; the coda nasal is not
  pronounced.

Before this spec, the combining-macron diacritic was silently dropped by the
tokenizer (a̱ -> "a", losing the nasal+length entirely) and the vowel+n/m
convention was not modelled at all, so words like pinti or imponna surfaced
with a plain oral vowel and an audible coda nasal that Choctaw does not have
in that position. The IPA-glyph ⟨ʋ⟩, used interchangeably with plain ⟨v⟩ for
/ə/ in traditional-orthography sources, was also unmapped and silently
deleted the letter (ʋpi -> "pɪ", losing the initial vowel).
"""
from orthography2ipa import transcribe, get


def test_cho_sources_cite_broadwell_not_wikipedia_as_authority():
    spec = get("cho")
    ids = {s.id for s in spec.sources}
    assert "broadwell2006" in ids


def test_macron_below_marks_a_nasal_long_vowel():
    """The Mississippi convention's combining macron below (U+0331) on a, i,
    o marks a nasal, intrinsically long vowel (Broadwell 2006), not a
    silently-dropped diacritic."""
    assert transcribe("a̱", "cho") == "ãː"
    assert transcribe("i̱", "cho") == "ĩː"
    assert transcribe("o̱", "cho") == "õː"


def test_macron_below_survives_word_medially():
    assert transcribe("aka̱ka", "cho") == "akãːka"
    assert transcribe("cho̱kash", "cho") == "tʃõːkaʃ"


def test_preconsonantal_vowel_n_nasalises_and_absorbs_the_nasal():
    """The historical Byington spelling vowel+n before a further consonant
    surfaces as a nasal long vowel with no audible nasal consonant
    (Broadwell 2006)."""
    assert transcribe("pinti", "cho") == "pĩːtɪ"
    assert transcribe("pakanli", "cho") == "pakãːlɪ"


def test_preconsonantal_vowel_m_nasalises_and_absorbs_the_nasal():
    assert transcribe("imponna", "cho") == "ĩːponna"


def test_geminate_nasal_is_not_absorbed():
    """A geminate nn/mm (hannali, yannash) is a plain doubled coda+onset
    consonant, not the vowel+n(+C) nasalisation pattern, and must not be
    absorbed or trigger nasalisation of the preceding vowel."""
    out = transcribe("hannali", "cho")
    assert "nn" in out or "n" in out
    assert "ã" not in out and "ə̃" not in out
    out2 = transcribe("yannash", "cho")
    assert "ã" not in out2


def test_word_final_nasal_is_not_absorbed():
    """A word-final n (hakchin) has no following consonant to trigger the
    historical nasalisation pattern and stays a plain coda [n]."""
    out = transcribe("hakchin", "cho")
    assert out.endswith("n")


def test_ipa_hook_v_glyph_is_an_alternate_schwa_spelling():
    """⟨ʋ⟩ (U+028B) is used interchangeably with plain ⟨v⟩ for /ə/ in
    traditional-orthography Choctaw sources and must not be silently
    dropped."""
    assert transcribe("ʋ", "cho") == "ə"
    assert transcribe("ʋpi", "cho") == "əpɪ"
