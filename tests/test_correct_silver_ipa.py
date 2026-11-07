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
from collections import Counter
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
SHEET = ("# Transcription conventions: Spanish (es-ES)\n\n## Stress\n\n"
         "Stress follows the written accent rules. Source: RAE 2010.\n")
CONVENTIONS_ANSWER = {
    **{name: {"choice": f"the {name} choice, as in ˈkasa",
              "source": "Hualde 2005, ch. 12"}
       for name, _, _ in csi.CONVENTION_TOPICS},
    "other": [{"topic": "Rhotics", "choice": "the tap ɾ between vowels",
               "source": "Navarro Tomás 1918, § 111"}]}


def _pass_of(params):
    if params["output_config"]["format"]["schema"] == csi.CONVENTIONS_SCHEMA:
        return "conventions"
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
    name = _pass_of(params)
    if name == "conventions":
        return CONVENTIONS_ANSWER
    sentence = _sentence_of(params)
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
    return {"ipa": "adjudicated" + engine, "flag": "adjudicated",
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


def _sheet(tmp_path, lect="es-ES", text=SHEET):
    path = tmp_path / "conventions" / f"{lect}.md"
    if text is None:
        return path
    path.parent.mkdir(exist_ok=True)
    if not path.exists():
        path.write_text(text, encoding="utf-8")
    return path


def _argv(tmp_path, *extra, sheet=SHEET):
    _sheet(tmp_path, text=sheet)
    return ["--dataset", "spain_romance_tts", "--lect", "es-ES",
            "--limit", "2", "--out-dir", str(tmp_path / "out"),
            "--cache-dir", str(tmp_path / "cache"),
            "--conventions-dir", str(tmp_path / "conventions"), *extra]


def _request(name, row, **overrides):
    """Parameters of one pass over *row*, with the engine reading and the
    test sheet."""
    engine, words = csi.engine_reading(row)
    options = dict(engine=engine, words=words, sheet=SHEET, a=None, b=None,
                   model="claude-opus-5-5", effort="high", max_tokens=8000)
    options.update(overrides)
    return csi.build_request(name, row, **options)


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
    system = csi.system_text(row.lect, SHEET)
    assert "transcription conventions" in system
    assert "published phonological descriptions" in system
    c = _request("C", row, engine="ˈengine", a="ˈa", b="ˈb")
    assert "note_conflict" in c["messages"][-1]["content"]
    assert "note_conflict" in csi.SCHEMAS["C"]["required"]


def test_passes_a_and_b_are_blind_to_engine_and_original():
    params_by_pass = {}
    row = csi.load_rows(["spain_romance_tts"], ["es-ES"], 1)[0]
    engine = ENGINE[row.sentence]
    for name in ("A", "B"):
        params_by_pass[name] = _request(name, row)
    for params in params_by_pass.values():
        blob = json.dumps(params, ensure_ascii=False)
        assert engine not in blob
        assert row.ipa not in blob
    assert (params_by_pass["A"]["messages"]
            != params_by_pass["B"]["messages"])
    # The row is engine-pinned (its ipa IS the engine output), so pass C is
    # given a distinct engine string to show the original ipa stays out.
    c = _request("C", row, engine="ˈengine", a="ˈa", b="ˈb")
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
    assert adjudicated["ipa"] == "adjudicated" + ENGINE[ROWS[1]["sentence"]]
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
    # key, and no A or B was submitted again. Row 2, in the share of the
    # first key, has its A and B, so its pass C went out while the batch of
    # the missing key stays pending.
    assert [len(s["submissions"]) for s in servers.values()] == [2, 1, 1]
    records = {r["key"]: r for r in _cache_records(tmp_path)}
    [late] = servers["ovos"]["submissions"][1:]
    assert [(records[k]["pass"], records[k]["row_id"]) for k in late] == [
        ("C", ROWS[1]["id"])]
    assert sorted({r["key_name"] for r in records.values()}) == [
        "anthropic-jarbas.key", "anthropic-ovos.key"]
    assert len(records) == 9


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


# ─── convention sheets ──────────────────────────────────────────────────────

def _conventions(tmp_path, transport, *extra):
    return csi.main(["conventions", "--conventions-dir",
                     str(tmp_path / "conventions"), "--cache-dir",
                     str(tmp_path / "cache"), *extra],
                    env={"ANTHROPIC_API_KEY": FAKE_KEY},
                    transport_factory=lambda key: transport)


def test_conventions_writes_one_sheet_per_lect_from_a_blind_request(
        tmp_path):
    fake = FakeTransport()
    assert _conventions(tmp_path, fake, "--lect", "es-ES", "pt-PT",
                        "--max-usd", "5") == 0
    assert [_pass_of(p) for p in fake.calls] == ["conventions"] * 2
    for params, (dataset, lect) in zip(
            fake.calls, [("spain_romance_tts", "es-ES"),
                         ("portuguese_tts", "pt-PT")]):
        system = params["system"][0]["text"]
        assert csi.orthography2ipa.get(lect).notes.strip() in system
        blob = json.dumps(params, ensure_ascii=False)
        for row in csi.load_rows([dataset], [lect], 20):
            assert row.sentence not in blob
            assert row.ipa not in blob
            assert csi.engine_reading(row)[0] not in blob
        sheet = (tmp_path / "conventions" / f"{lect}.md").read_text("utf-8")
        for _, heading, _ in csi.CONVENTION_TOPICS:
            assert f"\n## {heading}\n" in sheet
        assert "Source: Hualde 2005, ch. 12" in sheet
        assert "### Rhotics" in sheet
        assert sheet.rstrip().endswith(csi.segmentation_text(lect))
        assert "## Word segmentation" in sheet


def test_conventions_keeps_an_edited_sheet_unless_forced(tmp_path):
    path = _sheet(tmp_path, text="# edited by hand\n")
    fake = FakeTransport()
    assert _conventions(tmp_path, fake, "--lect", "es-ES",
                        "--max-usd", "5") == 0
    assert fake.calls == []
    assert path.read_text("utf-8") == "# edited by hand\n"
    assert _conventions(tmp_path, fake, "--lect", "es-ES", "--force",
                        "--max-usd", "5") == 0
    assert len(fake.calls) == 1
    assert path.read_text("utf-8").startswith(
        "# Transcription conventions: ")


def test_conventions_spend_cap_refuses_before_any_call(tmp_path, capsys):
    fake = FakeTransport()
    assert _conventions(tmp_path, fake, "--lect", "es-ES", "pt-PT", "ar",
                        "--max-usd", "0.0001") == 3
    assert fake.calls == []
    assert "refusing to start" in capsys.readouterr().out
    assert not (tmp_path / "conventions").exists()


@pytest.mark.parametrize("mode", [("--dry-run",), ("--sync", "--max-usd",
                                                   "50")])
def test_a_run_refuses_a_lect_without_a_sheet(tmp_path, capsys, mode):
    def factory(key):
        raise AssertionError("a transport was built for a lect with no sheet")
    assert csi.main(_argv(tmp_path, *mode, sheet=None),
                    env={"ANTHROPIC_API_KEY": FAKE_KEY},
                    transport_factory=factory) == 2
    err = capsys.readouterr().err
    assert "no convention sheet" in err
    assert "conventions --lect es-ES" in err
    assert not (tmp_path / "out").exists()


def test_every_pass_reads_the_sheet_after_the_notes(tmp_path):
    fake = FakeTransport()
    assert _run(tmp_path, fake, "--sync", "--max-usd", "50") == 0
    assert sorted(_pass_of(p) for p in fake.calls) == ["A", "A", "B", "B",
                                                       "C"]
    for params in fake.calls:
        (block,) = params["system"]
        assert block["cache_control"] == {"type": "ephemeral"}
        assert SHEET.strip() in block["text"]
        assert block["text"].index(SHEET.strip()) > block["text"].index(
            "Cited sources:")


def test_editing_the_sheet_changes_the_cache_key(tmp_path):
    assert _run(tmp_path, FakeTransport(), "--sync", "--max-usd", "50") == 0
    unchanged = FakeTransport()
    assert _run(tmp_path, unchanged, "--sync", "--max-usd", "50") == 0
    assert unchanged.calls == []
    _sheet(tmp_path).write_text(SHEET + "\n## Glides\n\nWrite j w.\n",
                                encoding="utf-8")
    edited = FakeTransport()
    assert _run(tmp_path, edited, "--sync", "--max-usd", "50") == 0
    assert len(edited.calls) == 5


# ─── word segmentation ──────────────────────────────────────────────────────

def test_each_pass_gets_the_engine_word_split():
    row = csi.Row("portuguese_tts", "pt-PT", "pt-PT-x",
                  "Ele liga-me amanhã.", "ˈelɨ ˈliɡɐmɨ ɐmɐˈɲɐ̃")
    engine, words = csi.engine_reading(row)
    # The hyphen splits the clitic from its host, as in the engine output.
    assert words == ("ele", "liga", "me", "amanhã")
    assert len(engine.split()) == len(words)
    listed = "Words (4): ele | liga | me | amanhã"
    for name in "ABC":
        params = _request(name, row, a="ˈa", b="ˈb")
        assert listed in params["messages"][-1]["content"]


@pytest.mark.parametrize("ipa,engine,expected", [
    ("ˈelɨ ˈliɡɐ mɨ", "ˈelɨ ˈliɡɐ mɨ", {"ipa": 3, "engine": 3, "ok": True}),
    ("ˈelɨ ˈliɡɐmɨ", "ˈelɨ ˈliɡɐ mɨ", {"ipa": 2, "engine": 3, "ok": False}),
    ("ˈelɨ  ˈliɡɐ   mɨ", "ˈelɨ ˈliɡɐ mɨ", {"ipa": 3, "engine": 3,
                                            "ok": True}),
])
def test_word_count(ipa, engine, expected):
    assert csi.word_count(ipa, engine) == expected


class JoiningTransport(FakeTransport):
    """Passes A and B join the first two words of the first row. The
    agreement test ignores spaces, so the row is agreed without pass C."""

    def create_message(self, params):
        message = super().create_message(params)
        if (_pass_of(params) in "AB"
                and _sentence_of(params) == ROWS[0]["sentence"]):
            ipa = ENGINE[ROWS[0]["sentence"]].replace(" ", "", 1)
            message = _message({"ipa": ipa} if _pass_of(params) == "A"
                               else {"word_forms": [], "ipa": ipa})
        return message


def test_a_word_count_that_differs_from_the_engine_is_flagged_not_fixed(
        tmp_path, capsys):
    assert _run(tmp_path, JoiningTransport(), "--sync",
                "--max-usd", "50") == 0
    joined, kept = _output(tmp_path)
    engine = ENGINE[ROWS[0]["sentence"]]
    assert joined["flag"] == "agreed"
    assert joined["ipa"] == engine.replace(" ", "", 1)
    assert joined["word_count"] == {"ipa": len(engine.split()) - 1,
                                    "engine": len(engine.split()),
                                    "ok": False}
    assert kept["word_count"]["ok"] is True
    err = capsys.readouterr().err
    assert f"{ROWS[0]['id']}: the ipa has" in err
    assert ROWS[1]["id"] not in err


def test_conventions_spreads_concurrent_calls_over_the_keys(tmp_path):
    log, fakes = _fakes(jarbas={"unusable_after": 0})
    by_key = {KEYS[name]: fake for name, fake in fakes.items()}
    lects = ["es-ES", "pt-PT", "ar", "gl", "ca", "it"]
    assert csi.main(["conventions", "--lect", *lects, "--concurrency", "4",
                     "--max-usd", "5",
                     "--conventions-dir", str(tmp_path / "conventions"),
                     "--cache-dir", str(tmp_path / "cache")],
                    env=_key_files(tmp_path),
                    transport_factory=by_key.__getitem__) == 0
    assert sorted(p.stem for p in (tmp_path / "conventions").glob("*.md")) \
        == sorted(lects)
    assert len(log) == len(lects)
    assert "anthropic-jarbas.key" not in log
    assert set(log) == {"anthropic-ovos.key", "anthropic-invoices.key"}


def test_conventions_defaults_to_every_lect_of_the_sets(tmp_path, capsys):
    assert csi.main(["conventions", "--dataset", "spain_romance_tts",
                     "--dry-run", "--conventions-dir",
                     str(tmp_path / "conventions")], env={},
                    transport_factory=None) == 0
    out = capsys.readouterr().out
    count = len(csi.set_lects("spain_romance_tts"))
    assert f"convention sheets to write: {count}" in out


# ─── batch scheduling, the cap and canonical output ─────────────────────────

class ScheduledBatchTransport(FakeTransport):
    """A batch ends only when the test puts its id in ``server["ended"]``.
    A custom id in ``server["unusable"]`` comes back once as an errored
    item."""

    def batch_status(self, batch_id):
        return "ended" if batch_id in self.server["ended"] else "in_progress"

    def batch_results(self, batch_id):
        for custom_id, message in super().batch_results(batch_id):
            if custom_id in self.server["unusable"]:
                self.server["unusable"].discard(custom_id)
                yield custom_id, {"error": "errored"}
            else:
                yield custom_id, message


def _passes_of(server, batch_id):
    return [(_pass_of(r["params"]), _sentence_of(r["params"]))
            for r in server["batches"][batch_id]]


def test_pass_c_goes_out_while_an_a_b_retry_is_still_running(tmp_path):
    server = {"batches": {}, "submissions": [], "ended": set(),
              "unusable": set()}

    def run():
        return _run(tmp_path, ScheduledBatchTransport(batch_server=server),
                    "--max-usd", "50", "--no-wait")

    assert run() == 0
    [first] = server["batches"]
    assert sorted(_passes_of(server, first)) == sorted(
        (name, r["sentence"]) for r in ROWS for name in "AB")
    # Pass B of row 1 comes back unusable. Row 2 has its A and B, and they
    # disagree, so row 2 needs pass C.
    retry = next(r["custom_id"] for r in server["batches"][first]
                 if _pass_of(r["params"]) == "B"
                 and _sentence_of(r["params"]) == ROWS[0]["sentence"])
    server["ended"].add(first)
    server["unusable"].add(retry)

    assert run() == 0
    later = [b for b in server["batches"] if b != first]
    submitted = sorted(p for b in later for p in _passes_of(server, b))
    # The retry of B for row 1 is still running, and pass C for row 2 went
    # out in the same run.
    assert submitted == [("B", ROWS[0]["sentence"]),
                         ("C", ROWS[1]["sentence"])]
    assert not any(b in server["ended"] for b in later)

    server["ended"].update(later)
    assert run() == 0
    # Only the unusable B went out twice.
    counts = Counter(cid for batch in server["submissions"] for cid in batch)
    assert counts.pop(retry) == 2
    assert sorted(counts.values()) == [1, 1, 1, 1]
    assert [r["flag"] for r in _output(tmp_path)] == ["agreed", "adjudicated"]


def test_a_low_cap_still_collects_batches_already_submitted(tmp_path,
                                                            capsys):
    server = {"batches": {}, "submissions": [], "polls_left": 1}
    assert _run(tmp_path, FakeTransport(batch_server=server),
                "--max-usd", "50", "--no-wait") == 0
    assert [len(s) for s in server["submissions"]] == [4]
    capsys.readouterr()

    # Pass C of row 2 costs more than the cap, so the run submits nothing
    # new. The A/B batch is paid for already: the run collects it.
    assert _run(tmp_path, FakeTransport(batch_server=server),
                "--max-usd", "0.0001", "--poll-seconds", "0") == 3
    assert "refus" in capsys.readouterr().out.lower()
    assert [len(s) for s in server["submissions"]] == [4]
    assert {(r["pass"], r["row_id"]) for r in _cache_records(tmp_path)} == {
        (name, r["id"]) for r in ROWS for name in "AB"}
    pending = tmp_path / "cache" / "pending_batches.json"
    assert json.loads(pending.read_text("utf-8")) == []
    assert [(r["id"], r["flag"]) for r in _output(tmp_path)] == [
        (ROWS[0]["id"], "agreed")]


class AsciiGTransport(FakeTransport):
    """Every answer writes ASCII g (U+0067) where the fake writes k, so A
    and B disagree with the engine and every row needs pass C."""

    def create_message(self, params):
        message = super().create_message(params)
        return dict(message, text=message["text"].replace("k", "g"))


def test_written_ipa_uses_the_ipa_letter_for_the_velar_stop(tmp_path):
    assert _run(tmp_path, AsciiGTransport(), "--sync", "--max-usd", "50") == 0
    rows = _output(tmp_path)
    assert [r["sentence"] for r in rows] == [r["sentence"] for r in ROWS]
    for row in rows:
        engine = ENGINE[row["sentence"]]
        assert "k" in engine
        assert row["ipa"] == ("adjudicated" + engine).replace("k", "\u0261")
        # The passes stay as the model wrote them.
        assert row["passes"]["A"] == engine.replace("k", "g")
        assert row["passes"]["C"]["ipa"] == ("adjudicated"
                                             + engine).replace("k", "g")
