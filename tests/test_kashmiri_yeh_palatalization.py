"""Kashmiri (`kas`) grapheme-table regression test.

`kas_arab_broad.tsv` (WikiPron, Wiktionary-scraped gold) exposed ؠ (U+0620,
'Kashmiri yeh') mapped to a glide ([j], with [ɨ] as a fallback candidate) when
the gold shows it is the palatalisation diacritic [ʲ] on the preceding
consonant: 100 of 101 gold rows containing ؠ transcribe it as plain Cʲ, never
a glide and never fused into a distinct single segment.

Every word below is drawn verbatim from the WikiPron gold; see
orthography2ipa/data/kas.json for the full provenance note.
"""
from orthography2ipa import transcribe


def test_yeh_is_palatalization_not_glide():
    # gold: آشَنؠ -> aː ʃ a nʲ
    assert transcribe("آشَنؠ", "kas") == "aːʃanʲ"


def test_yeh_after_aspirated_stop():
    # gold: بُتھؠ -> b u t̪ʰʲ (spec's تھ key is plain tʰ, no dental diacritic;
    # out of scope for this fix -- only the trailing ؠ is under test here)
    assert transcribe("بُتھؠ", "kas") == "butʰʲ"


def test_yeh_alone_is_bare_palatalization():
    # gold: ؠ -> ʲ
    assert transcribe("ؠ", "kas") == "ʲ"
