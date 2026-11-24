import dataclasses

import pytest

from orthography2ipa import G2P, Pipeline, get
from orthography2ipa.exceptions import EngineSourceUnavailable
from orthography2ipa.ir import cache


def test_a_hangul_word_with_a_final_consonant_hits_the_lexicon():
    g = G2P("ko", pipeline=Pipeline(lexicon={"한국어": "XYZ", "닭": "QQ"}))
    assert g.transcribe("닭 한국어") == "QQ XYZ"
    assert g.transcribe_word("한국어") == "XYZ"


def test_a_hangul_word_with_a_final_consonant_hits_word_exceptions():
    spec = dataclasses.replace(get("ko"), word_exceptions={"한국어": "WX"})
    assert G2P("ko", spec=spec).transcribe("한국어") == "WX"


def test_the_word_of_a_word_transcription_is_nfc():
    word = G2P("ko").transcribe_detailed("한국어").words[0].word
    assert [hex(ord(c)) for c in word] == ["0xd55c", "0xad6d", "0xc5b4"]


def test_an_install_without_engine_source_still_transcribes(monkeypatch):
    def unavailable(name):
        raise EngineSourceUnavailable(name)

    cache._engine_bytes.cache_clear()
    cache._interpreters.clear()
    monkeypatch.setattr(cache.source_revision, "_module_source", unavailable)
    try:
        assert G2P("es-ES").transcribe("casa") == "ˈkasa"
    finally:
        cache._engine_bytes.cache_clear()
        cache._interpreters.clear()
