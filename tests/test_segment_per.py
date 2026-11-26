"""The shared segment rule of the PER board (``benchmark.segments``)."""
import os
import unicodedata
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import benchmark  # noqa: E402


@pytest.mark.parametrize("ipa,expected", [
    ("ˈt͡ʃa.ʧu", ["t͡ʃ", "a", "t͡ʃ", "u"]),
    ("ɐ̃ˈkĩɲɐ", ["ɐ̃", "k", "ĩ", "ɲ", "ɐ"]),
    ("kʰaː", ["kʰ", "aː"]),
    ("o ʤɔ", ["o", "d͡ʒ", "ɔ"]),
])
def test_segments(ipa, expected):
    assert benchmark.segments(ipa) == [unicodedata.normalize("NFD", s) for s in expected]


def test_segment_per_is_micro_over_the_closest_variant(monkeypatch):
    class Engine:
        def __init__(self, *a, **k):
            pass

        def transcribe_word(self, word):
            return {"ab": "ab", "abcd": "abxx"}[word]

    import orthography2ipa
    monkeypatch.setattr(orthography2ipa, "G2P", Engine)
    # ab: 0 edits / 2 segments (the closer variant); abcd: 2 edits / 4.
    n, per = benchmark.segment_per([("ab", "ab"), ("ab", "zz"), ("abcd", "abcd")], "pt-PT")
    assert (n, per) == (2, 2 / 6)


def test_an_empty_transcription_counts_as_a_full_deletion(monkeypatch):
    class Engine:
        def __init__(self, *a, **k):
            pass

        def transcribe_word(self, word):
            return {"ab": "ab", "cd": ""}[word]

    import orthography2ipa
    monkeypatch.setattr(orthography2ipa, "G2P", Engine)
    assert benchmark.segment_per([("ab", "ab"), ("cd", "cd")], "pt-PT") == (2, 2 / 4)
