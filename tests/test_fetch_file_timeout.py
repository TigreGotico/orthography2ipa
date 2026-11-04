"""_fetch_file must give up on a gold server that accepts the connection and
never answers.

urlretrieve has no timeout of its own, so a stalled server held the
benchmark-regression CI job silent until someone cancelled it. The fake
server here accepts every connection and never sends a byte.
"""
import os
import socket
import sys
import threading

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


def _silent_server():
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    held = []

    def accept_and_hold():
        while True:
            try:
                conn, _ = srv.accept()
            except OSError:
                return
            held.append(conn)

    threading.Thread(target=accept_and_hold, daemon=True).start()
    return srv, held


def test_stalled_server_raises_within_the_timeout(tmp_path, monkeypatch):
    monkeypatch.setattr(benchmark, "CACHE_DIR", str(tmp_path))
    monkeypatch.setattr(benchmark, "_FETCH_ATTEMPTS", 2)
    monkeypatch.setattr(benchmark, "_FETCH_BACKOFF_SECONDS", 0)
    monkeypatch.setattr(benchmark, "_FETCH_TIMEOUT_SECONDS", 1, raising=False)
    srv, held = _silent_server()
    url = f"http://127.0.0.1:{srv.getsockname()[1]}/slovari.rar"
    outcome = {}

    def fetch():
        try:
            outcome["path"] = benchmark._fetch_file(url, "slovari.rar")
        except Exception as exc:
            outcome["exc"] = exc

    worker = threading.Thread(target=fetch, daemon=True)
    worker.start()
    worker.join(timeout=15)
    try:
        assert not worker.is_alive(), "_fetch_file still blocked after 15 s"
        assert isinstance(outcome.get("exc"), TimeoutError), outcome
        assert len(held) == 2, "each attempt must open its own connection"
        assert os.listdir(tmp_path) == []
        assert socket.getdefaulttimeout() is None
    finally:
        srv.close()
        for conn in held:
            conn.close()
