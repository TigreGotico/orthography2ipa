"""Ojibwe ⟨ng⟩ spells the cluster /n/ + lenis ⟨g⟩, realised [ŋɡ].

The consonant inventory the spec encodes has only /m n/ in the nasal row, and
⟨ng⟩ is one of the permitted consonant clusters, several of which — ⟨ng⟩
included — also occur word-finally. The /n/ assimilates to [ŋ] before the
velar, so the ⟨g⟩ is a segment of its own and is not swallowed by a velar
nasal that the language has no phoneme for.

Short ⟨a i o⟩ stay phonemic. The WikiPron gold writes them lax, but it mixes
transcription conventions and the description this spec follows gives short
/a/ a range of stressed values rather than one, so the phonetic values stay in
`allophones`.
"""
from orthography2ipa import transcribe


def test_ng_keeps_the_lenis_velar():
    assert transcribe("bangii", "oji") == "baŋɡiː"


def test_word_final_ng_keeps_the_lenis_velar():
    assert transcribe("anang", "oji") == "anaŋɡ"


def test_ng_before_w():
    assert "ŋɡw" in transcribe("zhingwaak", "oji")


def test_short_vowels_stay_phonemic():
    out = transcribe("abi", "oji")
    assert out == "abi"
    assert "ʌ" not in out and "ɪ" not in out


def test_long_aa_stays_front():
    out = transcribe("aanimaa", "oji")
    assert "aː" in out
    assert "ɑ" not in out
