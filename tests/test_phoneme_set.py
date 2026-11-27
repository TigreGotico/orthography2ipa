"""The phoneme set of the IR holds every segment the interpreter emits."""
import random

import pytest

import benchmark
from orthography2ipa import phoneme_set
from orthography2ipa.ir import cache, compiler
from orthography2ipa.phonemes import ir_phonemes, segments
from orthography2ipa.registry import resolve

LEADERS = ["pt-PT", "pt-BR", "es-CO", "fr-FR", "it-IT", "de-DE", "nl-NL", "da-DK", "kab", "hi-IN", "bn-IN"]


def _words(keys, n, seed):
    rng = random.Random(seed)
    return list(keys) + ["".join(rng.choice(keys) for _ in range(rng.randint(2, 6))) for _ in range(n)]


@pytest.mark.parametrize("lang", LEADERS)
def test_no_transcribed_segment_is_outside_the_set(lang):
    code = resolve(lang)
    ir = compiler.build_ir(code)
    allowed = set(ir["phonemes"])
    it = cache.interpreter(code, **cache.DEFAULT_OPTIONS)
    keys = [e["key"] for e in ir["entries"]]
    outside = {}
    for word in _words(keys, 3000, lang):
        for seg in segments(it.transcribe(word)):
            if seg not in allowed:
                outside.setdefault(seg, word)
    assert outside == {}


def test_set_is_the_ir_field():
    assert phoneme_set("pt-PT") == frozenset(ir_phonemes(compiler.build_ir("pt-PT")))


def test_values():
    pt = phoneme_set("pt-PT")
    assert {"ʎ", "ɐ̃", "ʃ", "ɨ"} <= pt
    # The nasal mark joins only a nasal carrier in pt-PT.
    assert "b̃" not in pt
    # Hindi candrabindu reads as the nasal mark alone, so after a virama the
    # beam splices it onto a consonant: क्ँ gives k̃.
    assert "k̃" in phoneme_set("hi-IN")
    assert "ˈ" not in pt and "." not in pt


@pytest.mark.parametrize("ipa", ["ˈt͡ʃɐ̃w̃.ʃ", "ʧaːˌʤ", "kʰa‿ʔ i", "t͜s", "õː"])
def test_segments_are_the_board_rule(ipa):
    assert segments(ipa) == benchmark.segments(ipa)
