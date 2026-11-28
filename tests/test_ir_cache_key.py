"""The IR cache key moves with every input the compiler reads."""
import pytest

from orthography2ipa.ir import cache


@pytest.fixture(autouse=True)
def _fresh_engine_bytes():
    cache._engine_bytes.cache_clear()
    yield
    cache._engine_bytes.cache_clear()


def test_a_phonematcher_release_moves_the_cache_key(monkeypatch):
    before = cache.cache_key("pt-PT", cache.DEFAULT_OPTIONS)
    cache._engine_bytes.cache_clear()
    monkeypatch.setattr(cache, "PHONEMATCHER_VERSION", "0.0.0")
    assert cache.cache_key("pt-PT", cache.DEFAULT_OPTIONS) != before
