"""Tests for scripts/benchmark.py's ``load_vox_communis`` loader
(fdemelo/vox-communis-parallel-g2p).

Network access is mocked out via ``benchmark._fetch`` so these run offline
and deterministically, mirroring the other loader test modules.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402

_HEADER = "aligned_sentence\tphonemized_sentence"


def _tsv(rows):
    return "\n".join([_HEADER] + ["\t".join(r) for r in rows])


def test_spn_placeholder_tokens_are_not_scored_as_gold(monkeypatch):
    """``spn`` is the aligner's lexicon-miss marker, not a transcription.

    Admitting it makes PER unbounded: PER normalises by the gold length, so
    a real word scored against the 3-character ``spn`` can exceed 1.0 on
    its own. Whole vox_communis rows sat above PER 2.0 because of it.
    """
    text = _tsv([("хыдаран уи ҳәа ианкаҳа",
                  "χ ə d a r a n | w j | spn | j a n kʼ a ħ a")])
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: text)

    pairs = benchmark.load_vox_communis("ab", 100)

    assert ("хыдаран", "χədaran") in pairs
    assert ("ианкаҳа", "jankʼaħa") in pairs
    assert "ҳәа" not in [w for w, _ in pairs]
    assert "spn" not in [g for _, g in pairs]


def test_marker_lookalike_phones_are_kept_they_are_real_words(monkeypatch):
    """Only ``spn`` may be filtered — the siblings are real transcriptions.

    ``sil``/``sp``/``nsn``/``noise`` occur in these files overwhelmingly as
    genuine phone strings for real words: Welsh ``sul`` → /sil/ alone is
    336 rows, plus Amharic ``ሲል``, Bulgarian ``сп``, Tamil ``ஸ்ப்``,
    Korean ``실``, Punjabi ``ਸੀਲ``. Filtering on the phone string would
    silently delete all of them.
    """
    text = _tsv([("sul ሲል сп", "s i l | s i l | s p")])
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: text)

    pairs = benchmark.load_vox_communis("cy", 100)

    assert ("sul", "sil") in pairs
    assert ("ሲል", "sil") in pairs
    assert ("сп", "sp") in pairs


def test_only_spn_is_registered_as_non_speech():
    assert benchmark._VOX_COMMUNIS_NON_SPEECH == frozenset({"spn"})


def test_real_phones_are_still_kept(monkeypatch):
    text = _tsv([("este tipo de", "e s t̪ e | t̪ i p o | d̪ e")])
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: text)

    assert benchmark.load_vox_communis("es", 100) == [
        ("este", "est̪e"), ("tipo", "t̪ipo"), ("de", "d̪e"),
    ]


def test_zh_is_not_registered_han_script_cannot_be_scored():
    """The o2i ``zh`` spec consumes pinyin; ``zh-cn.tsv`` is Han script.

    Every row transcribed to the empty string, so the board carried a
    ``per: 1.0`` row that measured a missing hanzi→pinyin front-end, not
    Mandarin. Same disposition as ``yue`` and the ipa-dict ``zh_*`` files.
    """
    assert "zh" not in benchmark._VOX_COMMUNIS_FILES
    assert "yue" not in benchmark._VOX_COMMUNIS_FILES
    assert "zh-cn" not in benchmark._VOX_COMMUNIS_FILES.values()


def test_wired_tag_count_matches_the_documented_figure():
    """docs/benchmark_datasets.md states the wired tag count; keep them in step."""
    assert len(benchmark._VOX_COMMUNIS_FILES) == 69
