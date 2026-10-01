"""Regression test for scripts/benchmark.py's _fetch_file() leaving a
truncated file at the final cache path when a download is interrupted.

_fetch_file downloaded straight to CACHE_DIR/name with urlretrieve. If the
download died partway through (killed process, network drop, disk full),
whatever bytes had already landed stayed at the final path. The next run's
`os.path.exists(dest)` check then treated that truncated file as a valid
cache hit forever — a stale/truncated cached TSV silently poisoned every
later read of that dataset.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


def test_interrupted_download_leaves_no_file_at_final_path(tmp_path, monkeypatch):
    monkeypatch.setattr(benchmark, "CACHE_DIR", str(tmp_path))
    monkeypatch.setattr(benchmark, "_FETCH_ATTEMPTS", 1)

    def boom(url, dest):
        # simulate a download that dies mid-transfer: some bytes already
        # written to the destination path before the failure.
        with open(dest, "wb") as fh:
            fh.write(b"truncated-partial-content")
        raise ConnectionError("simulated interrupted download")

    monkeypatch.setattr(benchmark.urllib.request, "urlretrieve", boom)

    dest = os.path.join(str(tmp_path), "poisoned.tsv")
    try:
        benchmark._fetch_file("http://example.invalid/poisoned.tsv",
                               "poisoned.tsv")
        assert False, "expected the simulated download failure to propagate"
    except ConnectionError:
        pass

    assert not os.path.exists(dest), (
        "an interrupted download must not leave a truncated file at the "
        "final cache path")
    # no stray temp file left behind in the cache dir either
    assert os.listdir(str(tmp_path)) == []


def test_successful_download_lands_at_final_path(tmp_path, monkeypatch):
    monkeypatch.setattr(benchmark, "CACHE_DIR", str(tmp_path))

    def fake_retrieve(url, dest):
        with open(dest, "wb") as fh:
            fh.write(b"complete-content")

    monkeypatch.setattr(benchmark.urllib.request, "urlretrieve", fake_retrieve)

    result = benchmark._fetch_file("http://example.invalid/ok.tsv", "ok.tsv")
    assert os.path.exists(result)
    with open(result, "rb") as fh:
        assert fh.read() == b"complete-content"
    # no leftover temp artifact
    assert os.listdir(str(tmp_path)) == [os.path.basename(result)]
