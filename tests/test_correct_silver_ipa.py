"""Tests for scripts/correct_silver_ipa.py, the silver-IPA correction tool.

Every test replaces the network with a fake transport. No test opens a
socket, and no test needs an API key: the credential tests use a fake key
and check that it never reaches any output.
"""
import csv
import hashlib
import json
import os
import socket
import sys
from pathlib import Path

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402
import correct_silver_ipa as csi  # noqa: E402
from orthography2ipa import G2P  # noqa: E402

GOLD_TSV = (Path(__file__).resolve().parent.parent / "orthography2ipa" / "data"
            / "gold" / "spain_romance_tts" / "es-ES.tsv")
FAKE_KEY = "sk-ant-api03-FAKEKEY-" + "q7Zx" * 12


def _gold_rows(n):
    with open(GOLD_TSV, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))[:n]


ROWS = _gold_rows(2)
ENGINE = {r["sentence"]: G2P("es-ES").transcribe(r["sentence"]) for r in ROWS}


def _pass_of(params):
    for name, schema in csi.SCHEMAS.items():
        if params["output_config"]["format"]["schema"] == schema:
            return name
    raise AssertionError("request carries no known pass schema")


def _sentence_of(params):
    user = params["messages"][-1]["content"]
    found = [r["sentence"] for r in ROWS if r["sentence"] in user]
    assert len(found) == 1, user
    return found[0]


def _answer(params):
    """Row 1: A and B agree with the engine up to stress marks and spacing.
    Row 2: B disagrees, so pass C must run."""
    name, sentence = _pass_of(params), _sentence_of(params)
    engine = ENGINE[sentence]
    if name == "A":
        return {"ipa": engine}
    if name == "B":
        if sentence == ROWS[0]["sentence"]:
            return {"word_forms": engine.split(),
                    "ipa": "  ".join(engine.replace("ˈ", "").split())}
        return {"word_forms": [], "ipa": "x" + engine}
    return {"ipa": "adjudicated " + engine, "flag": "adjudicated",
            "reason": "rule cited in hualde2005"}


def _message(payload):
    return {"text": json.dumps(payload, ensure_ascii=False),
            "stop_reason": "end_turn",
            "usage": {"input_tokens": 1000, "output_tokens": 200,
                      "cache_creation_input_tokens": 0,
                      "cache_read_input_tokens": 0}}


class FakeTransport:
    """Answers every call from ``_answer``; records what it was asked."""

    def __init__(self, fail_after=None, batch_server=None):
        self.calls = []
        self.fail_after = fail_after
        self.server = batch_server if batch_server is not None else {
            "batches": {}, "submissions": [], "polls_left": 0}

    def create_message(self, params):
        if self.fail_after is not None and len(self.calls) >= self.fail_after:
            raise RuntimeError("simulated network failure")
        self.calls.append(params)
        return _message(_answer(params))

    def count_tokens(self, params):
        raise AssertionError("count_tokens is not expected in these tests")

    def submit_batch(self, requests):
        batch_id = f"msgbatch_{len(self.server['batches'])}"
        self.server["batches"][batch_id] = list(requests)
        self.server["submissions"].append([r["custom_id"] for r in requests])
        return batch_id

    def batch_status(self, batch_id):
        if self.server["polls_left"] > 0:
            self.server["polls_left"] -= 1
            return "in_progress"
        return "ended"

    def batch_results(self, batch_id):
        for req in self.server["batches"][batch_id]:
            yield req["custom_id"], _message(_answer(req["params"]))


def _argv(tmp_path, *extra):
    return ["--dataset", "spain_romance_tts", "--lect", "es-ES",
            "--limit", "2", "--out-dir", str(tmp_path / "out"),
            "--cache-dir", str(tmp_path / "cache"), *extra]


def _run(tmp_path, transport, *extra, env=None):
    env = {"ANTHROPIC_API_KEY": FAKE_KEY} if env is None else env
    return csi.main(_argv(tmp_path, *extra), env=env,
                    transport_factory=lambda key: transport)


def _output(tmp_path):
    path = tmp_path / "out" / "spain_romance_tts.llm-corrected.jsonl"
    return [json.loads(line) for line in path.read_text("utf-8").splitlines()]


# ─── transport fake ─────────────────────────────────────────────────────────

def test_every_network_call_goes_through_the_injected_transport(
        tmp_path, monkeypatch):
    def no_socket(*args, **kwargs):
        raise AssertionError("a socket was opened outside the transport")
    monkeypatch.setattr(socket, "socket", no_socket)
    fake = FakeTransport()
    assert _run(tmp_path, fake, "--sync", "--max-usd", "50") == 0
    passes = sorted(_pass_of(p) for p in fake.calls)
    assert passes == ["A", "A", "B", "B", "C"]
    assert all(p["model"] == "claude-opus-5-5" for p in fake.calls)


def test_dry_run_needs_no_key_and_makes_no_call(tmp_path, capsys):
    def factory(key):
        raise AssertionError("dry run built a transport")
    assert csi.main(_argv(tmp_path, "--dry-run"), env={},
                    transport_factory=factory) == 0
    out = capsys.readouterr().out
    assert "estimate" in out.lower()
    assert not (tmp_path / "out").exists()


# ─── agreement logic ────────────────────────────────────────────────────────

def _scorer_equal(a, b, lect):
    marks = benchmark._prosody_marks(lect)
    return (benchmark.normalize(a, True, True, extra_strip=marks)
            == benchmark.normalize(b, True, True, extra_strip=marks))


@pytest.mark.parametrize("a,b", [
    ("ˈkasa ˈβlanka", "kasa βlanka"),      # stress marks only
    ("ˈkasa ˈβlanka", "ˈkasaˈβlanka"),     # word spacing only
    ("ˈkasa", "ˈkaza"),                    # a real segment difference
    ("ˈt͡ʃiko", "ˈtʃiko"),                  # tie bar only
])
def test_same_ipa_is_the_scorer_normalisation(a, b):
    assert csi.same_ipa(a, b, "es-ES") is _scorer_equal(a, b, "es-ES")


def test_same_ipa_ignores_stress_and_spacing_but_not_segments():
    assert csi.same_ipa("ˈkasa ˈβlanka", "kasa  βlanka", "es-ES")
    assert not csi.same_ipa("ˈkasa", "ˈkaza", "es-ES")


@pytest.mark.parametrize("a,b,engine,expected", [
    ("ˈkasa", "kasa", "ˈkasa", False),   # A, B and engine agree
    ("ˈkasa", "kasa", "ˈkaza", True),    # A and B agree, engine differs
    ("ˈkasa", "ˈkaza", "ˈkasa", True),   # A and B disagree
    ("ˈkasa", "ˈkaza", "ˈkaza", True),   # B agrees with the engine, A not
])
def test_needs_adjudication(a, b, engine, expected):
    assert csi.needs_adjudication(a, b, engine, "es-ES") is expected


def test_passes_a_and_b_are_blind_to_engine_and_original():
    params_by_pass = {}
    row = csi.load_rows(["spain_romance_tts"], ["es-ES"], 1)[0]
    engine = ENGINE[row.sentence]
    for name in ("A", "B"):
        params_by_pass[name] = csi.build_request(
            name, row, engine=engine, a=None, b=None,
            model="claude-opus-5-5", effort="high", max_tokens=8000)
    for params in params_by_pass.values():
        blob = json.dumps(params, ensure_ascii=False)
        assert engine not in blob
        assert row.ipa not in blob
    assert (params_by_pass["A"]["messages"]
            != params_by_pass["B"]["messages"])
    # The row is engine-pinned (its ipa IS the engine output), so pass C is
    # given a distinct engine string to show the original ipa stays out.
    c = csi.build_request("C", row, engine="ˈengine", a="ˈa", b="ˈb",
                          model="claude-opus-5-5", effort="high",
                          max_tokens=8000)
    blob = json.dumps(c, ensure_ascii=False)
    assert "ˈengine" in blob and "ˈa" in blob and "ˈb" in blob
    assert row.ipa not in blob


# ─── spend cap ──────────────────────────────────────────────────────────────

def test_usd_uses_the_published_per_token_price():
    # claude-opus-5-5: $4 per million input tokens, $20 per million output.
    assert csi.usd(1_000_000, 1_000_000, "claude-opus-5-5", batch=False) \
        == pytest.approx(24.0)
    # The Message Batches API bills half.
    assert csi.usd(1_000_000, 1_000_000, "claude-opus-5-5", batch=True) \
        == pytest.approx(12.0)


def test_upper_bound_counts_one_token_per_byte_plus_overhead():
    params = {"model": "claude-opus-5-5", "max_tokens": 700,
              "system": [{"type": "text", "text": "ab"}],
              "messages": [{"role": "user", "content": "é"}],
              "output_config": {"format": {"type": "json_schema",
                                           "schema": {}}}}
    # 2 bytes + 2 bytes ("é" is two bytes in UTF-8) + 2 bytes ("{}").
    assert csi.upper_bound_tokens(params) == (
        6 + csi.REQUEST_OVERHEAD_TOKENS, 700)


def _estimate(tmp_path, capsys, *mode):
    assert csi.main(_argv(tmp_path, "--dry-run", *mode), env={},
                    transport_factory=None) == 0
    line = [ln for ln in capsys.readouterr().out.splitlines()
            if ln.startswith("estimate:")][0]
    return float(line.split("$")[1].split()[0])


def test_spend_cap_refuses_above_the_estimate(tmp_path, capsys):
    estimate = _estimate(tmp_path, capsys, "--sync")
    assert estimate > 0
    fake = FakeTransport()
    assert _run(tmp_path, fake, "--sync",
                "--max-usd", f"{estimate * 0.99:.4f}") != 0
    assert fake.calls == []
    assert "refus" in capsys.readouterr().out.lower()
    assert not (tmp_path / "out").exists()
    assert _run(tmp_path, fake, "--sync",
                "--max-usd", f"{estimate * 1.01:.4f}") == 0
    assert len(fake.calls) == 5


def test_batch_estimate_is_half_the_sync_estimate(tmp_path, capsys):
    sync = _estimate(tmp_path, capsys, "--sync")
    batch = _estimate(tmp_path, capsys)
    assert batch == pytest.approx(sync / 2, rel=1e-3)


def test_batch_spend_cap_refuses_before_submitting(tmp_path):
    fake = FakeTransport()
    assert _run(tmp_path, fake, "--max-usd", "0.0001") != 0
    assert fake.server["submissions"] == []


def test_a_live_run_requires_a_cap(tmp_path):
    with pytest.raises(SystemExit):
        _run(tmp_path, FakeTransport(), "--sync")


# ─── resume ─────────────────────────────────────────────────────────────────

def test_sync_resume_does_not_pay_twice(tmp_path):
    first = FakeTransport(fail_after=3)
    assert _run(tmp_path, first, "--sync", "--max-usd", "50") != 0
    assert len(first.calls) == 3
    second = FakeTransport()
    assert _run(tmp_path, second, "--sync", "--max-usd", "50") == 0
    assert len(second.calls) == 2
    done = {json.dumps(p, sort_keys=True, ensure_ascii=False)
            for p in first.calls}
    assert not done & {json.dumps(p, sort_keys=True, ensure_ascii=False)
                       for p in second.calls}
    third = FakeTransport()
    assert _run(tmp_path, third, "--sync", "--max-usd", "50") == 0
    assert third.calls == []
    assert len(_output(tmp_path)) == 2


def test_batch_resume_collects_a_pending_batch_without_resubmitting(tmp_path):
    server = {"batches": {}, "submissions": [], "polls_left": 1}
    first = FakeTransport(batch_server=server)
    assert _run(tmp_path, first, "--max-usd", "50", "--no-wait") == 0
    assert [len(s) for s in server["submissions"]] == [4]
    second = FakeTransport(batch_server=server)
    assert _run(tmp_path, second, "--max-usd", "50",
                "--poll-seconds", "0") == 0
    # Run two collects the pending A/B batch and submits pass C for the one
    # row whose passes disagree. A and B are not submitted again.
    assert [len(s) for s in server["submissions"]] == [4, 1]
    ids = [cid for s in server["submissions"] for cid in s]
    assert len(ids) == len(set(ids))
    rows = _output(tmp_path)
    assert [r["flag"] for r in rows] == ["agreed", "adjudicated"]


def test_cache_key_changes_with_model_and_prompt():
    base = csi.cache_key("spain_romance_tts", "es-ES-001", "claude-opus-5-5",
                         "p" * 64)
    assert base != csi.cache_key("spain_romance_tts", "es-ES-001",
                                 "claude-sonnet-5-5", "p" * 64)
    assert base != csi.cache_key("spain_romance_tts", "es-ES-001",
                                 "claude-opus-5-5", "q" * 64)
    assert base != csi.cache_key("spain_romance_tts", "es-ES-002",
                                 "claude-opus-5-5", "p" * 64)
    assert base != csi.cache_key("portuguese_tts", "es-ES-001",
                                 "claude-opus-5-5", "p" * 64)


# ─── output schema ──────────────────────────────────────────────────────────

def test_output_schema_and_original_untouched(tmp_path):
    before = hashlib.sha256(GOLD_TSV.read_bytes()).hexdigest()
    assert _run(tmp_path, FakeTransport(), "--sync", "--max-usd", "50") == 0
    assert hashlib.sha256(GOLD_TSV.read_bytes()).hexdigest() == before

    rows = _output(tmp_path)
    assert [r["id"] for r in rows] == [r["id"] for r in ROWS]
    for out, gold in zip(rows, ROWS):
        assert set(out) == csi.OUTPUT_FIELDS
        assert out["tier"] == "llm-corrected"
        assert out["dataset"] == "spain_romance_tts"
        assert out["lect"] == "es-ES"
        assert out["sentence"] == gold["sentence"]
        assert out["ipa_llm_original"] == gold["ipa"]
        assert out["ipa_engine"] == ENGINE[gold["sentence"]]
        assert out["model"] == "claude-opus-5-5"
        assert set(out["passes"]) == {"A", "B", "C"}
        assert out["flag"] in {"agreed", "adjudicated", "uncertain"}
        assert out["reason"]
        assert out["source_row"]["gloss_en"] == gold["gloss_en"]

    agreed, adjudicated = rows
    assert agreed["flag"] == "agreed"
    assert agreed["passes"]["C"] is None
    assert agreed["ipa"] == agreed["passes"]["A"] == ENGINE[ROWS[0]["sentence"]]
    assert adjudicated["flag"] == "adjudicated"
    assert adjudicated["passes"]["C"]["flag"] == "adjudicated"
    assert adjudicated["ipa"] == "adjudicated " + ENGINE[ROWS[1]["sentence"]]
    assert adjudicated["reason"] == "rule cited in hualde2005"


def test_output_merges_runs_over_different_lects(tmp_path):
    assert _run(tmp_path, FakeTransport(), "--sync", "--max-usd", "50") == 0
    path = tmp_path / "out" / "spain_romance_tts.llm-corrected.jsonl"
    extra = dict(_output(tmp_path)[0], lect="es-AR", id="es-AR-001")
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(extra, ensure_ascii=False) + "\n")
    assert _run(tmp_path, FakeTransport(), "--sync", "--max-usd", "50") == 0
    assert [(r["lect"], r["id"]) for r in _output(tmp_path)] == [
        ("es-AR", "es-AR-001"), ("es-ES", ROWS[0]["id"]),
        ("es-ES", ROWS[1]["id"])]


# ─── credentials ────────────────────────────────────────────────────────────

def test_key_file_wins_over_the_environment_variable(tmp_path):
    key_file = tmp_path / "key"
    key_file.write_text(FAKE_KEY + "\n", encoding="utf-8")
    env = {csi.KEY_FILE_ENV: str(key_file), csi.KEY_ENV: "other"}
    assert csi.load_api_key(env) == FAKE_KEY
    assert csi.load_api_key({csi.KEY_ENV: FAKE_KEY}) == FAKE_KEY


def test_missing_key_error_names_the_variables_not_a_value(tmp_path):
    with pytest.raises(csi.CredentialError) as exc:
        csi.load_api_key({})
    assert csi.KEY_FILE_ENV in str(exc.value)
    assert csi.KEY_ENV in str(exc.value)
    key_file = tmp_path / "key"
    key_file.write_text("", encoding="utf-8")
    with pytest.raises(csi.CredentialError) as exc:
        csi.load_api_key({csi.KEY_FILE_ENV: str(key_file)})
    assert csi.KEY_FILE_ENV in str(exc.value)


class LeakyTransport(FakeTransport):
    """A transport whose errors echo the key, as a careless SDK error might."""

    def __init__(self, key):
        super().__init__()
        self.key = key

    def create_message(self, params):
        if len(self.calls) == 2:
            raise RuntimeError(f"401 invalid x-api-key {self.key}")
        return super().create_message(params)


def test_key_never_appears_in_any_output_or_log(tmp_path, capsys):
    key_file = tmp_path / "secret" / "key"
    key_file.parent.mkdir()
    key_file.write_text(FAKE_KEY, encoding="utf-8")
    env = {csi.KEY_FILE_ENV: str(key_file)}
    seen = []

    def factory(key):
        seen.append(key)
        return LeakyTransport(key)

    status = csi.main(_argv(tmp_path, "--sync", "--max-usd", "50"), env=env,
                      transport_factory=factory)
    assert seen == [FAKE_KEY]
    assert status != 0
    captured = capsys.readouterr()

    texts = {"stdout": captured.out, "stderr": captured.err}
    for path in tmp_path.rglob("*"):
        if path.is_file() and "secret" not in path.parts:
            texts[str(path)] = path.read_text("utf-8", errors="replace")
    assert any(name.endswith("run.log") for name in texts)
    leaked = [name for name, text in texts.items() if FAKE_KEY in text]
    assert leaked == []
    # The leaking error was reported, with the key replaced.
    assert csi.REDACTED in captured.err
