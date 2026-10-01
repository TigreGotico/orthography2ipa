"""The de-DE/ipa_childes row: four notation folds and one gold error.

The gold aspirates every voiceless stop, writes ʀ, lengthens open-syllable
vowels and tenses the lax vowels: notation, 0.3948 -> 0.1507. It also reads
word-final ⟨-e⟩ as ɛː in 3568 of 3750 words, which German does not do: that
is a gold error, sized (0.0771) but never matched. No `valid_ceiling`.
"""
from orthography2ipa import json_loader
from orthography2ipa.g2p import G2P


def test_ipa_childes_is_an_audit_not_a_ceiling():
    spec = json_loader.load_json_spec("de-DE")
    assert "ipa_childes" not in (spec.valid_ceiling or {})
    entry = spec.audit["ipa_childes"]
    assert entry.conclusion == "at_ceiling_documented"
    for number in ("0.3948", "0.3407", "0.2877", "0.1922", "0.1507", "0.0771", "3568"):
        assert number in entry.measured, number
    assert "error in the gold" in entry.measured


def test_final_e_stays_schwa_whatever_the_gold_says():
    # the spec follows Duden, Wiese and Kohler, not epitran
    g = G2P("de-DE")
    for word in ("heute", "rote", "eine", "Katze"):
        assert g.transcribe_word(word).endswith("ə"), word
