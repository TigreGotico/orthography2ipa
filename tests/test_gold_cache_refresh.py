"""Refreshing the gold cache, and reporting when upstream has moved.

A board row is only as current as the gold file the box that scored it
happened to hold, and a stale snapshot looks exactly like a current one.
These tests pin the escape hatch: the cache is authoritative by default,
and a refresh says whether it still matches upstream.
"""
import os
import sys
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import pytest  # noqa: E402

import benchmark  # noqa: E402


@pytest.fixture
def served(tmp_path, monkeypatch):
    """A fake upstream whose payload the test can change between fetches."""
    monkeypatch.setattr(benchmark, "CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setattr(benchmark, "REFRESH_CACHE", False,
                        raising=False)
    state = {"payload": b"first", "fail": False}

    def _retrieve(url, dest):
        if state["fail"]:
            raise OSError("network down")
        with open(dest, "wb") as fh:
            fh.write(state["payload"])

    monkeypatch.setattr(urllib.request, "urlretrieve", _retrieve)
    return state


def _read(path):
    with open(path, "rb") as fh:
        return fh.read()


class TestTheCacheIsAuthoritativeByDefault:
    def test_a_second_fetch_does_not_go_to_the_network(self, served):
        first = benchmark._fetch_file("http://x/gold.tsv", "gold.tsv")
        served["payload"] = b"second"
        again = benchmark._fetch_file("http://x/gold.tsv", "gold.tsv")
        assert _read(again) == b"first", (
            "scoring must not change under a caller's feet: without an "
            "explicit refresh the cached snapshot is what gets scored")
        assert again == first


class TestRefreshing:
    def test_it_replaces_the_cached_copy(self, served, monkeypatch):
        benchmark._fetch_file("http://x/gold.tsv", "gold.tsv")
        served["payload"] = b"second"
        monkeypatch.setattr(benchmark, "REFRESH_CACHE", True,
                            raising=False)
        path = benchmark._fetch_file("http://x/gold.tsv", "gold.tsv")
        assert _read(path) == b"second"

    def test_it_reports_that_upstream_changed(self, served, monkeypatch,
                                              capsys):
        benchmark._fetch_file("http://x/gold.tsv", "gold.tsv")
        fresh = b"a much longer second payload"
        served["payload"] = fresh
        monkeypatch.setattr(benchmark, "REFRESH_CACHE", True,
                            raising=False)
        benchmark._fetch_file("http://x/gold.tsv", "gold.tsv")
        err = capsys.readouterr().err
        assert "UPSTREAM CHANGED" in err
        assert str(len(b"first")) in err and str(len(fresh)) in err, (
            f"both byte counts belong in the report, got: {err}")

    def test_it_reports_an_unchanged_cache_too(self, served, monkeypatch,
                                               capsys):
        benchmark._fetch_file("http://x/gold.tsv", "gold.tsv")
        monkeypatch.setattr(benchmark, "REFRESH_CACHE", True,
                            raising=False)
        benchmark._fetch_file("http://x/gold.tsv", "gold.tsv")
        err = capsys.readouterr().err
        assert "cache is current" in err
        assert "UPSTREAM CHANGED" not in err

    def test_a_failed_refresh_keeps_the_gold(self, served, monkeypatch):
        path = benchmark._fetch_file("http://x/gold.tsv", "gold.tsv")
        monkeypatch.setattr(benchmark, "REFRESH_CACHE", True,
                            raising=False)
        monkeypatch.setattr(benchmark, "_FETCH_BACKOFF_SECONDS", 0,
                            raising=False)
        served["fail"] = True
        assert _read(benchmark._fetch_file("http://x/gold.tsv",
                                           "gold.tsv")) == b"first"
        assert _read(path) == b"first"

    def test_a_first_download_that_fails_still_raises(self, served,
                                                      monkeypatch):
        monkeypatch.setattr(benchmark, "_FETCH_BACKOFF_SECONDS", 0,
                            raising=False)
        served["fail"] = True
        with pytest.raises(OSError):
            benchmark._fetch_file("http://x/missing.tsv", "missing.tsv")


class TestTheFlagIsReachableFromTheCommandLine:
    def test_refresh_cache_is_an_option(self):
        import inspect
        assert "--refresh-cache" in inspect.getsource(benchmark.main)
