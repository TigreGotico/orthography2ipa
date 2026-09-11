"""Kashmiri (`kas`) grapheme-table regression tests.

`kas_arab_broad.tsv` (WikiPron, Wiktionary-scraped gold) exposed two gaps in
the Perso-Arabic grapheme table this spec models:

1. أ (U+0623, alef with hamza above) had no grapheme key of its own and was
   falling through to its NFD components -- alef (aː) plus the hamza-above
   diacritic (ə) -- emitting a spurious `aːə` where the gold has plain `ə`.
   The Wikipedia "Kashmiri alphabet" table gives أ the IPA value [ə] directly.
2. Word-initial او (a bare wāw needs a preceding alif to carry a vowel) was
   likewise falling through to alif's aː plus wāw's glide w, instead of the
   long vowel [oː] Wikipedia's table glosses it as.

Every word below is drawn verbatim from the WikiPron gold; see
orthography2ipa/data/kas.json for the full provenance note.
"""
from orthography2ipa import transcribe


def test_alef_hamza_above_is_schwa_not_aː_plus_schwa():
    # gold: أدٕر -> ə d ɨ r
    assert transcribe("أدٕر", "kas") == "ədɨr"


def test_alef_hamza_above_word_alone():
    # gold: أر -> ə r
    assert transcribe("أر", "kas") == "ər"


def test_alef_hamza_above_does_not_leak_aː():
    out = transcribe("أہرُن", "kas")
    assert "aː" not in out


def test_wordinitial_aw_digraph_is_long_o():
    # gold: اوش -> oː ʃ
    assert transcribe("اوش", "kas") == "oːʃ"
