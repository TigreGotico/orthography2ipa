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


ALL_ROWS = _gold_rows(6)
ROWS = ALL_ROWS[:2]
ENGINE = {r["sentence"]: G2P("es-ES").transcribe(r["sentence"])
          for r in ALL_ROWS}
NOTE_CONFLICT = "the note on stress in -ea- words disagrees with hualde2005"


def _pass_of(params):
    for name, schema in csi.SCHEMAS.items():
        if params["output_config"]["format"]["schema"] == schema:
            return name
    raise AssertionError("request carries no known pass schema")


def _sentence_of(params):
    user = params["messages"][-1]["content"]
    found = [r["sentence"] for r in ALL_ROWS if r["sentence"] in user]
    assert len(found) == 1, user
    return found[0]


def _onset_stress(ipa):
    """The same stress, with the mark put inside the onset of three words
    and doubled word spacing."""
    moved = (ipa.replace("ˈθj", "θˈj").replace("ˈkl", "kˈl")
             .replace("ˈno", "nˈo"))
    assert moved != ipa
    return "  ".join(moved.split())


def _answer(params):
    """Row 2: B disagrees, so pass C must run. Every other row: A and B
    agree with the engine up to where the stress mark sits in the onset and
    word spacing."""
    name, sentence = _pass_of(params), _sentence_of(params)
    engine = ENGINE[sentence]
    if name == "A":
        return {"ipa": engine}
    if name == "B":
        if sentence == ROWS[1]["sentence"]:
            return {"word_forms": [], "ipa": "x" + engine}
        if sentence == ROWS[0]["sentence"]:
            return {"word_forms": engine.split(),
                    "ipa": _onset_stress(engine)}
        return {"word_forms": engine.split(), "ipa": engine}
    return {"ipa": "adjudicated " + engine, "flag": "adjudicated",
            "reason": "rule cited in hualde2005",
            "note_conflict": NOTE_CONFLICT}


def _message(payload):
    return {"text": json.dumps(payload, ensure_ascii=False),
            "stop_reason": "end_turn",
            "usage": {"input_tokens": 1000, "output_tokens": 200,
                      "cache_creation_input_tokens": 0,
                      "cache_read_input_tokens": 0}}


class FakeTransport:
    """Answers every call from ``_answer``; records what it was asked.

    *fail_after* calls succeed before a network failure; *unusable_after*
    calls succeed before the key fails with *unusable_reason*. *log* is a
    list shared by the fakes of one run, filled with *name* per call."""

    def __init__(self, fail_after=None, batch_server=None, *, name=None,
                 log=None, unusable_after=None,
                 unusable_reason="HTTP 400 credit balance"):
        self.calls = []
        self.fail_after = fail_after
        self.name = name
        self.log = log if log is not None else []
        self.unusable_after = unusable_after
        self.unusable_reason = unusable_reason
        self.server = batch_server if batch_server is not None else {
            "batches": {}, "submissions": [], "polls_left": 0}

    def _check_key(self):
        if (self.unusable_after is not None
                and len(self.calls) >= self.unusable_after):
            raise csi.KeyUnusable(self.unusable_reason)

    def create_message(self, params):
        if self.fail_after is not None and len(self.calls) >= self.fail_after:
            raise RuntimeError("simulated network failure")
        self._check_key()
        self.calls.append(params)
        self.log.append(self.name)
        return _message(_answer(params))

    def count_tokens(self, params):
        raise AssertionError("count_tokens is not expected in these tests")

    def submit_batch(self, requests):
        self._check_key()
        self.calls.append(requests)
        batch_id = f"msgbatch_{self.name}_{len(self.server['batches'])}"
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
    return (benchmark.normalize(a, False, True, extra_strip=marks)
            == benchmark.normalize(b, False, True, extra_strip=marks))


@pytest.mark.parametrize("a,b", [
    ("ˈkasa ˈβlanka", "ˈkasaˈβlanka"),     # word spacing only
    ("ˈkasa", "ˈkaza"),                    # a real segment difference
    ("ˈt͡ʃiko", "ˈtʃiko"),                  # tie bar only
    ("ˈkasa ˈβlanka", "ˈkasa βlanka"),     # one stress mark missing
])
def test_same_ipa_is_the_scorer_normalisation_with_stress_kept(a, b):
    # On pairs that put each stress mark at the same place, the agreement
    # test is the scorer's broad comparison with stress kept.
    assert csi.same_ipa(a, b, "es-ES") is _scorer_equal(a, b, "es-ES")


def test_same_ipa_ignores_where_the_onset_holds_the_stress_mark():
    assert csi.same_ipa("esˈta", "eˈsta", "es-ES")
    assert csi.same_ipa("ˈklaɾo", "kˈlaɾo", "es-ES")
    assert csi.same_ipa("el ˈθjelo", "el  θjˈelo", "es-ES")
    # The board scores primary stress only.
    assert csi.same_ipa("ˌkasaˈβlanka", "kasaˈβlanka", "es-ES")


def test_same_ipa_keeps_stress_and_segments():
    assert not csi.same_ipa("ˈesta", "esˈta", "es-ES")
    assert not csi.same_ipa("ˈkasa", "kasa", "es-ES")
    assert not csi.same_ipa("ˈkasa", "ˈkaza", "es-ES")


@pytest.mark.parametrize("a,b,engine,expected", [
    ("esˈta", "eˈsta", "esˈta", False),   # A, B and engine agree
    ("esˈta", "esˈta", "esˈte", True),    # A and B agree, engine differs
    ("esˈta", "esˈte", "esˈta", True),    # A and B disagree
    ("esˈta", "esˈte", "esˈte", True),    # B agrees with the engine, A not
    ("ˈesta", "esˈta", "esˈta", True),    # A and B differ only in stress
    ("esˈta", "esˈta", "ˈesta", True),    # the engine differs in stress
])
def test_needs_adjudication(a, b, engine, expected):
    assert csi.needs_adjudication(a, b, engine, "es-ES") is expected


def test_prompts_take_pronunciation_from_published_descriptions():
    row = csi.load_rows(["spain_romance_tts"], ["es-ES"], 1)[0]
    system = csi.system_text(row.lect)
    assert "transcription conventions" in system
    assert "published phonological descriptions" in system
    c = csi.build_request("C", row, engine="ˈengine", a="ˈa", b="ˈb",
                          model="claude-opus-5-5", effort="high",
                          max_tokens=8000)
    assert "note_conflict" in c["messages"][-1]["content"]
    assert "note_conflict" in csi.SCHEMAS["C"]["required"]


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
    assert agreed["note_conflict"] == ""
    assert adjudicated["note_conflict"] == NOTE_CONFLICT
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

KEYS = {name: f"sk-ant-api03-FAKE{name.upper()}-" + "w4Rt" * 12
        for name in ("ovos", "jarbas", "invoices")}


def _key_files(tmp_path, names=tuple(KEYS)):
    directory = tmp_path / "secret"
    directory.mkdir(exist_ok=True)
    paths = []
    for name in names:
        path = directory / f"anthropic-{name}.key"
        path.write_text(KEYS[name] + "\n", encoding="utf-8")
        paths.append(str(path))
    return {csi.KEY_FILE_ENV: ":".join(paths)}


def test_key_files_win_over_the_environment_variable(tmp_path):
    env = dict(_key_files(tmp_path), **{csi.KEY_ENV: "other"})
    assert csi.load_api_keys(env) == [
        (f"anthropic-{name}.key", key) for name, key in KEYS.items()]
    assert csi.load_api_keys({csi.KEY_ENV: FAKE_KEY}) == [
        (csi.KEY_ENV, FAKE_KEY)]


def test_key_files_need_distinct_file_names(tmp_path):
    env = _key_files(tmp_path, ["ovos"])
    other = tmp_path / "other"
    other.mkdir()
    (other / "anthropic-ovos.key").write_text(KEYS["jarbas"],
                                              encoding="utf-8")
    env[csi.KEY_FILE_ENV] += ":" + str(other / "anthropic-ovos.key")
    with pytest.raises(csi.CredentialError) as exc:
        csi.load_api_keys(env)
    assert "distinct" in str(exc.value)


def test_missing_key_error_names_the_variables_not_a_value(tmp_path):
    with pytest.raises(csi.CredentialError) as exc:
        csi.load_api_keys({})
    assert csi.KEY_FILE_ENV in str(exc.value)
    assert csi.KEY_ENV in str(exc.value)
    key_file = tmp_path / "secret" / "empty.key"
    key_file.parent.mkdir()
    key_file.write_text("", encoding="utf-8")
    with pytest.raises(csi.CredentialError) as exc:
        csi.load_api_keys({csi.KEY_FILE_ENV: str(key_file)})
    assert csi.KEY_FILE_ENV in str(exc.value)
    assert "empty.key" in str(exc.value)
    # The error names the file, never the directory that holds the keys.
    assert str(key_file.parent) not in str(exc.value)


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


# ─── several keys ───────────────────────────────────────────────────────────

def _fakes(**options):
    """One fake per key, sharing a log of which key served each call."""
    log = []
    return log, {name: FakeTransport(name=f"anthropic-{name}.key", log=log,
                                     **options.get(name, {}))
                 for name in KEYS}


def _run_keys(tmp_path, fakes, *extra, names=tuple(KEYS)):
    by_key = {KEYS[name]: fake for name, fake in fakes.items()}
    return csi.main(_argv(tmp_path, *extra), env=_key_files(tmp_path, names),
                    transport_factory=by_key.__getitem__)


def _cache_records(tmp_path):
    path = tmp_path / "cache" / "responses.jsonl"
    return [json.loads(line) for line in path.read_text("utf-8").splitlines()]


@pytest.mark.parametrize("status,error_type,message,expected", [
    (401, "authentication_error", "invalid x-api-key", "HTTP 401"),
    (402, "billing_error", "payment required", "HTTP 402"),
    (403, "permission_error", "not allowed", "HTTP 403"),
    (400, "invalid_request_error",
     "Your credit balance is too low to access the Anthropic API.",
     "HTTP 400 credit balance"),
    (400, "billing_error", "billing problem", "HTTP 400 billing_error"),
    (400, "invalid_request_error", "max_tokens: field required", None),
    (429, "rate_limit_error", "rate limited", None),
    (500, "api_error", "internal error", None),
    (529, "overloaded_error", "overloaded", None),
])
def test_key_failure_classification(status, error_type, message, expected):
    assert csi.key_failure(status, error_type, message) == expected


def test_sync_requests_go_to_the_keys_in_turn(tmp_path):
    log, fakes = _fakes()
    assert _run_keys(tmp_path, fakes, "--sync", "--max-usd", "50") == 0
    names = [f"anthropic-{name}.key" for name in KEYS]
    assert log == (names * 2)[:5]
    # The cache records which key file served each response, by name only.
    assert [r["key_name"] for r in _cache_records(tmp_path)] == log


def test_sync_fails_over_after_a_credit_error(tmp_path, capsys):
    log, fakes = _fakes(jarbas={"unusable_after": 0})
    assert _run_keys(tmp_path, fakes, "--sync", "--max-usd", "50") == 0
    assert log == ["anthropic-ovos.key", "anthropic-invoices.key",
                   "anthropic-ovos.key", "anthropic-invoices.key",
                   "anthropic-ovos.key"]
    assert fakes["jarbas"].calls == []
    assert [r["flag"] for r in _output(tmp_path)] == ["agreed",
                                                      "adjudicated"]
    err = capsys.readouterr().err
    assert "anthropic-jarbas.key failed (HTTP 400 credit balance)" in err


def test_all_keys_exhausted_stops_cleanly_and_resumes(tmp_path, capsys):
    log, fakes = _fakes(ovos={"unusable_after": 1},
                        jarbas={"unusable_after": 1},
                        invoices={"unusable_after": 0,
                                  "unusable_reason": "HTTP 402"})
    assert _run_keys(tmp_path, fakes, "--sync", "--max-usd", "50") == 4
    assert log == ["anthropic-ovos.key", "anthropic-jarbas.key"]
    assert len(_cache_records(tmp_path)) == 2
    assert "no usable key is left" in capsys.readouterr().err

    log, fakes = _fakes()
    assert _run_keys(tmp_path, fakes, "--sync", "--max-usd", "50",
                     names=["invoices"]) == 0
    assert len(log) == 3
    assert [r["flag"] for r in _output(tmp_path)] == ["agreed",
                                                      "adjudicated"]


def test_batch_mode_sends_one_batch_per_key_with_an_even_split(tmp_path):
    log, fakes = _fakes()
    assert _run_keys(tmp_path, fakes, "--max-usd", "50", "--limit", "6",
                     "--poll-seconds", "0") == 0
    blind = {name: fake.server["submissions"][0]
             for name, fake in fakes.items()}
    assert [len(ids) for ids in blind.values()] == [4, 4, 4]
    all_ids = [cid for ids in blind.values() for cid in ids]
    assert len(set(all_ids)) == 12
    # Pass C for the one row that needs it is the second batch of the
    # first key; each key collected its own batches.
    assert [len(f.server["submissions"]) for f in fakes.values()] == [2, 1, 1]
    names = {r["key"]: r["key_name"] for r in _cache_records(tmp_path)}
    for name, fake in fakes.items():
        for ids in fake.server["submissions"]:
            assert {names[cid] for cid in ids} == {f"anthropic-{name}.key"}
    assert len(_output(tmp_path)) == 6


def test_batch_share_of_a_failed_key_goes_to_the_keys_left(tmp_path):
    log, fakes = _fakes(jarbas={"unusable_after": 0})
    assert _run_keys(tmp_path, fakes, "--max-usd", "50", "--limit", "6",
                     "--poll-seconds", "0") == 0
    sizes = {name: [len(ids) for ids in fake.server["submissions"]]
             for name, fake in fakes.items()}
    assert sizes == {"ovos": [4, 2, 1], "jarbas": [], "invoices": [4, 2]}
    assert len(_output(tmp_path)) == 6


def test_a_pending_batch_waits_for_its_own_key(tmp_path, capsys):
    servers = {name: {"batches": {}, "submissions": [], "polls_left": 1}
               for name in KEYS}
    options = {name: {"batch_server": server}
               for name, server in servers.items()}
    _, fakes = _fakes(**options)
    assert _run_keys(tmp_path, fakes, "--max-usd", "50", "--limit", "6",
                     "--no-wait") == 0
    assert [len(s["submissions"]) for s in servers.values()] == [1, 1, 1]
    capsys.readouterr()

    _, fakes = _fakes(**options)
    assert _run_keys(tmp_path, fakes, "--max-usd", "50", "--limit", "6",
                     "--poll-seconds", "0", names=["ovos", "jarbas"]) == 0
    err = capsys.readouterr().err
    assert "with key anthropic-invoices.key" in err
    assert "stays pending" in err
    # The two batches of the keys present were collected with their own
    # key; nothing was submitted again.
    assert [len(s["submissions"]) for s in servers.values()] == [1, 1, 1]
    assert sorted({r["key_name"] for r in _cache_records(tmp_path)}) == [
        "anthropic-jarbas.key", "anthropic-ovos.key"]
    assert len(_cache_records(tmp_path)) == 8


class LeakyKeyTransport(FakeTransport):
    """Fails with an error that echoes its own key."""

    def __init__(self, key, unusable, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.unusable = unusable

    def create_message(self, params):
        if self.unusable:
            raise csi.KeyUnusable(f"HTTP 401 invalid x-api-key {self.key}")
        if self.calls:
            raise RuntimeError(f"connection reset for key {self.key}")
        return super().create_message(params)


def test_no_key_of_the_list_appears_in_any_output_or_log(tmp_path, capsys):
    transports = {
        KEYS["ovos"]: LeakyKeyTransport(KEYS["ovos"], True),
        KEYS["jarbas"]: LeakyKeyTransport(KEYS["jarbas"], True),
        KEYS["invoices"]: LeakyKeyTransport(KEYS["invoices"], False),
    }
    status = csi.main(_argv(tmp_path, "--sync", "--max-usd", "50"),
                      env=_key_files(tmp_path),
                      transport_factory=transports.__getitem__)
    assert status != 0
    captured = capsys.readouterr()
    texts = {"stdout": captured.out, "stderr": captured.err}
    for path in tmp_path.rglob("*"):
        if path.is_file() and "secret" not in path.parts:
            texts[str(path)] = path.read_text("utf-8", errors="replace")
    assert any(name.endswith("run.log") for name in texts)
    leaked = [(name, key_name) for name, text in texts.items()
              for key_name, key in KEYS.items() if key in text]
    assert leaked == []
    # Two key failures and one traceback were reported, each redacted.
    assert captured.err.count(csi.REDACTED) >= 3
    assert "anthropic-ovos.key failed" in captured.err
    assert "anthropic-jarbas.key failed" in captured.err


class StressOnlyTransport(FakeTransport):
    """Pass B puts the stress of the first row on another syllable."""

    def create_message(self, params):
        message = super().create_message(params)
        if (_pass_of(params) == "B"
                and _sentence_of(params) == ROWS[0]["sentence"]):
            ipa = ENGINE[ROWS[0]["sentence"]].replace("esˈta", "ˈesta")
            assert ipa != ENGINE[ROWS[0]["sentence"]]
            message = _message({"word_forms": [], "ipa": ipa})
        return message


def test_a_stress_only_difference_between_a_and_b_requests_pass_c(tmp_path):
    fake = StressOnlyTransport()
    assert _run(tmp_path, fake, "--sync", "--max-usd", "50") == 0
    c_rows = [_sentence_of(p) for p in fake.calls if _pass_of(p) == "C"]
    assert sorted(c_rows) == sorted(r["sentence"] for r in ROWS)


def _sdk_error(status, body):
    import anthropic
    import httpx2
    request = httpx2.Request("POST", "https://api.anthropic.com/v1/messages")
    response = httpx2.Response(status, json=body, request=request)
    return anthropic.APIStatusError(body["error"]["message"],
                                    response=response, body=body)


@pytest.mark.parametrize("status,body,unusable", [
    (400, {"type": "error", "error": {
        "type": "invalid_request_error",
        "message": "Your credit balance is too low to access the "
                   "Anthropic API."}}, True),
    (401, {"type": "error", "error": {"type": "authentication_error",
                                      "message": "invalid x-api-key"}}, True),
    (429, {"type": "error", "error": {"type": "rate_limit_error",
                                      "message": "rate limited"}}, False),
])
def test_anthropic_transport_turns_key_failures_into_key_unusable(
        status, body, unusable):
    class Messages:
        def create(self, **params):
            raise _sdk_error(status, body)

    transport = csi.AnthropicTransport(FAKE_KEY)
    transport._client = type("Client", (), {"messages": Messages()})()
    if unusable:
        with pytest.raises(csi.KeyUnusable) as exc:
            transport.create_message({})
        assert str(exc.value).startswith(f"HTTP {status}")
        assert exc.value.__cause__ is None
    else:
        import anthropic
        with pytest.raises(anthropic.APIStatusError):
            transport.create_message({})
