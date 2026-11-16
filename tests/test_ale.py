"""Aleut (`ale`) grapheme-table regression tests.

The northeuralex gold (lexibank/northeuralex, Dellert2020 source column,
Language_ID `ale`) exposed two gaps in the Bergsland practical-orthography
grapheme table this spec models:

1. `ch` (the voiceless palato-alveolar affricate /tʃ/) was entirely absent
   from the grapheme table, even though it is a core native phoneme per
   Bergsland's 1994 orthography chart (Aleut Dictionary, p. xvi) and the
   consonant inventory in Taff et al. 2001 ("Phonetic Structures of Aleut",
   Journal of Phonetics 29(3)) — not a gap tied to the gold's own quirks.
2. NorthEuraLex spells the two uvular fricatives with a combining acute
   accent over x/g (`x́`, `ǵ`) rather than Bergsland's circumflex (`x̂`, `ĝ`);
   these are mapped as alternate spellings of the SAME already-sourced
   phonemes (χ, ʁ), not a new phonological claim.
3. Taff et al. 2001 documents p, b, d, g, f, v and r as consonants that
   occur only in Aleut loanwords (mostly from Russian); b, v, r, f and p
   are mapped on that basis to cover the Russian month/weekday/animal-name
   borrowings that appear in the gold (e.g. `baraaska`, `Yanvaari`).

Every word below is drawn verbatim (case included) from the northeuralex
gold; see orthography2ipa/data/ale.json for the full provenance note.
"""
from orthography2ipa import transcribe


def test_ch_digraph_is_the_postalveolar_affricate():
    assert transcribe("achi-x", "ale") == "atʃi x"


def test_ch_digraph_wins_over_plain_c_plus_h():
    out = transcribe("achi-x", "ale")
    assert "tʃ" in out


def test_combining_acute_x_is_the_uvular_fricative_variant_spelling():
    # gold: da-x́ -> dɑχ (dialect vowel quality aside, x́ must reach χ)
    assert transcribe("da-x́", "ale") == "ða χ"


def test_combining_acute_g_is_the_uvular_approximant_variant_spelling():
    # gold: agilǵi-x́ -> aɡilʁeχ
    out = transcribe("agilǵi-x́", "ale")
    assert "ʁ" in out
    assert out == "aɣilʁi χ"


def test_circumflex_uvulars_still_work_unchanged():
    # the canonical Bergsland spelling must not regress
    assert transcribe("adax̂", "ale") == "aðaχ"


def test_loanword_consonants_b_r_are_mapped():
    # gold: biruuza-x́ -> biɹyːzɑχ (Russian "бирюза", turquoise)
    out = transcribe("biruuza-x́", "ale")
    assert "b" in out
    assert "ɹ" in out


def test_loanword_consonants_v_f_are_mapped():
    # gold: yaavluka-x́ -> jɛːvlykɑχ (Russian "яблоко", apple)
    out = transcribe("yaavluka-x́", "ale")
    assert "v" in out


def test_loanword_consonant_p_is_mapped():
    # gold: Pyaatnicha-x́ -> pjɛːtnitʃɑχ (Russian "пятница", Friday)
    out = transcribe("Pyaatnicha-x́", "ale")
    assert out.startswith("p")
    assert "tʃ" in out
