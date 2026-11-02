#!/usr/bin/env python3
"""Correct the IPA of the LLM-generated gold sets with Claude, per sentence.

The LLM-generated sets (``spain_romance_tts``, ``portuguese_tts``,
``arabic_tts``, ``kabyle_tts``, ``iberian_creole_tts``, ``gold20_arabic``,
``mirandese_dict``, ``barranquenho_dict``) are silver labels. Several of them
are engine-pinned: their ``ipa`` column is the engine's own ``transcribe``
output. This tool writes an independent reading for every row:

pass A
    transcribes the sentence from its text, the lect code, and the lect
    spec's notes and cited sources. It never sees the engine output or the
    existing ``ipa``.
pass B
    does the same task under a different framing (word by word, then
    connected speech). It is also blind.
pass C
    runs only when A and B disagree after the scorer's broad normalisation,
    or when they agree and the engine disagrees. It sees A, B, the engine
    output and the lect's cited rules, and returns one transcription, a flag
    (``agreed``, ``adjudicated`` or ``uncertain``) and a one-line reason.

Every pass uses structured output (a JSON schema). Full runs go through the
Message Batches API; ``--sync`` sends one request at a time for small
pilots. The output is one JSONL file per set,
``<out-dir>/<set>.llm-corrected.jsonl``; the original files stay unchanged.
The tier of every output row is ``llm-corrected``: still silver.

Spend: before any request the tool prints an upper-bound estimate (one input
token per UTF-8 byte of the prompt plus a fixed overhead per request, and
``--max-tokens`` output tokens per request, with pass C counted for every row
whose A and B are not known yet) and refuses to start when it exceeds
``--max-usd``. ``--sync`` also stops before a request that would take the
run's actual spend past the cap.

Resume: every response is cached under ``--cache-dir``, keyed on the set,
the row id, the model and a hash of the request. A run that stops continues
from the cache and from any batch still pending, and pays for no row twice.

Credentials: the API key comes from the file named by ``O2I_ANTHROPIC_KEY_FILE``
or from ``ANTHROPIC_API_KEY``. The tool never prints or logs it. A dry run
needs no key and makes no API call.

Requires the ``silver-correction`` extra for live runs::

    uv pip install -e '.[silver-correction]'

Pilot (20 rows per lect, synchronous)::

    python scripts/correct_silver_ipa.py \\
        --dataset spain_romance_tts portuguese_tts arabic_tts \\
        --lect es-ES pt-PT ar --limit 20 --sync --max-usd 40

See docs/contributing/silver_correction.md.
"""
from __future__ import annotations

import argparse
import csv
import functools
import hashlib
import json
import os
import sys
import time
import traceback
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, Iterable, Iterator, List, Mapping, \
    NamedTuple, Optional, Protocol, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import benchmark  # noqa: E402
import orthography2ipa  # noqa: E402

GOLD_DIR = REPO_ROOT / "orthography2ipa" / "data" / "gold"
DEFAULT_CACHE_DIR = REPO_ROOT / ".silver_correction_cache"

#: Sets held in this repository: one ``<lect>.tsv`` per lect under
#: ``orthography2ipa/data/gold/<set>/`` with ``id``, ``sentence`` and ``ipa``
#: columns.
LOCAL_SETS = ("arabic_tts", "iberian_creole_tts", "kabyle_tts",
              "portuguese_tts", "spain_romance_tts")
#: Sets published elsewhere, read through their ``scripts/benchmark.py``
#: loader. Their rows carry no id, so a row's id is its position in the
#: loader's output.
REMOTE_SETS = ("barranquenho_dict", "gold20_arabic", "mirandese_dict")
SILVER_SETS = LOCAL_SETS + REMOTE_SETS

TIER = "llm-corrected"
FLAGS = ("agreed", "adjudicated", "uncertain")
AGREED_REASON = ("passes A and B and the engine agree after broad "
                 "normalisation")
OUTPUT_FIELDS = {"dataset", "lect", "id", "sentence", "ipa",
                 "ipa_llm_original", "ipa_engine", "model", "passes", "flag",
                 "reason", "tier", "source_row"}

KEY_FILE_ENV = "O2I_ANTHROPIC_KEY_FILE"
KEY_ENV = "ANTHROPIC_API_KEY"
REDACTED = "[REDACTED]"

DEFAULT_MODEL = "claude-opus-5-5"
#: Input tokens added to every request's estimate for the API's own framing
#: of the system prompt, the messages and the output schema.
REQUEST_OVERHEAD_TOKENS = 1000
#: Requests per batch submission, well under the API's 100,000 limit.
BATCH_CHUNK = 5000


class Price(NamedTuple):
    """US dollars per million tokens."""
    input: float
    output: float
    cache_read: float


#: Standard first-party prices. A cache write costs 1.25 times the input
#: price; the Message Batches API bills half of every price.
PRICES: Dict[str, Price] = {
    "claude-opus-5-5": Price(4.0, 20.0, 0.20),
    "claude-sonnet-5-5": Price(2.0, 10.0, 0.20),
    "claude-fable-5-1": Price(10.0, 50.0, 0.25),
}
CACHE_WRITE_FACTOR = 1.25
BATCH_DISCOUNT = 0.5

_IPA = {"type": "string",
        "description": "Broad IPA of the whole text, words separated by "
                       "single spaces, primary stress marked with ˈ."}
SCHEMAS: Dict[str, dict] = {
    "A": {"type": "object", "properties": {"ipa": _IPA},
          "required": ["ipa"], "additionalProperties": False},
    "B": {"type": "object",
          "properties": {
              "word_forms": {"type": "array", "items": {"type": "string"},
                             "description": "Citation form of each word, "
                                            "in order, as broad IPA."},
              "ipa": _IPA},
          "required": ["word_forms", "ipa"], "additionalProperties": False},
    "C": {"type": "object",
          "properties": {
              "ipa": _IPA,
              "flag": {"type": "string", "enum": list(FLAGS)},
              "reason": {"type": "string",
                         "description": "One line that names the rule or "
                                        "source that decides the case."}},
          "required": ["ipa", "flag", "reason"],
          "additionalProperties": False},
}

SYSTEM_TEXT = """\
You are a phonetician. You transcribe text written in one lect into broad IPA.

The lect description below is your authority. Its notes state the \
transcription conventions and the phonological rules of the lect, and its \
sources are the published works those rules cite. Where your own knowledge \
and the notes disagree, follow the notes unless a cited source says \
otherwise.

Transcribe what a native speaker of this lect says when reading the text \
aloud at a normal pace. Write broad IPA: phonemes, plus the allophones the \
notes say the convention writes. Mark primary stress with ˈ before the \
stressed syllable of each stressed word. Separate words with single spaces. \
Do not transcribe punctuation.

"""

USER_TEXT = {
    "A": "Transcribe this text into broad IPA.\n\nText: {sentence}",
    "B": ("Work word by word. First write the citation form of each word of "
          "the text in this lect, in order, as broad IPA. Then apply the "
          "connected-speech processes the lect notes describe across word "
          "boundaries, such as elision, resyllabification, assimilation and "
          "sandhi, and write the whole text as broad IPA.\n\n"
          "Text: {sentence}"),
    "C": ("Two independent transcriptions of a text and the output of a "
          "rule-based engine follow. They disagree, or the engine disagrees "
          "with both transcriptions. Decide the correct broad IPA of the "
          "text in this lect.\n\n"
          "The engine applies the lect's rules mechanically and can be "
          "wrong. Either transcription can also be wrong. Decide each "
          "difference by what the lect notes and cited sources state.\n\n"
          "Return one transcription, a flag and a one-line reason. Use the "
          "flag \"agreed\" when the candidates differ only in notation, "
          "\"adjudicated\" when the notes or sources support the reading "
          "you return, and \"uncertain\" when the notes and sources do not "
          "settle the case.\n\n"
          "Text: {sentence}\n"
          "Transcription A: {a}\n"
          "Transcription B: {b}\n"
          "Engine output: {engine}"),
}


# ─── credentials and reporting ──────────────────────────────────────────────

class CredentialError(Exception):
    """No usable API key. The message names variables, never values."""


def load_api_key(env: Mapping[str, str]) -> str:
    """Read the key from the file named by ``O2I_ANTHROPIC_KEY_FILE``, else
    from ``ANTHROPIC_API_KEY``."""
    key_file = env.get(KEY_FILE_ENV)
    if key_file:
        try:
            key = Path(key_file).expanduser().read_text("utf-8").strip()
        except OSError as exc:
            raise CredentialError(
                f"{KEY_FILE_ENV} names a file that cannot be read "
                f"({exc.strerror})") from None
        if not key:
            raise CredentialError(f"the file named by {KEY_FILE_ENV} is empty")
        return key
    key = env.get(KEY_ENV, "").strip()
    if not key:
        raise CredentialError(
            f"no API key: set {KEY_FILE_ENV} to the path of a key file, or "
            f"set {KEY_ENV}")
    return key


def redact(text: str, secrets: Iterable[str]) -> str:
    for secret in secrets:
        text = text.replace(secret, REDACTED)
    return text


class Reporter:
    """The one place the tool writes messages: stdout or stderr, and the run
    log. Every message passes through :func:`redact` first."""

    def __init__(self, log_path: Optional[Path] = None):
        self.log_path = log_path
        self.secrets: List[str] = []

    def say(self, message: str, *, error: bool = False) -> None:
        message = redact(message, self.secrets)
        print(message, file=sys.stderr if error else sys.stdout)
        if self.log_path is not None:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
            with open(self.log_path, "a", encoding="utf-8") as fh:
                fh.write(f"{stamp} {message}\n")


# ─── transport ──────────────────────────────────────────────────────────────

class Transport(Protocol):
    """Every network call the tool makes. A response is a plain dict:
    ``{"text", "stop_reason", "usage"}``; a failed batch item is
    ``{"error": <type>}``."""

    def create_message(self, params: dict) -> dict: ...

    def count_tokens(self, params: dict) -> int: ...

    def submit_batch(self, requests: Sequence[dict]) -> str: ...

    def batch_status(self, batch_id: str) -> str: ...

    def batch_results(self, batch_id: str) -> Iterator[Tuple[str, dict]]: ...


USAGE_FIELDS = ("input_tokens", "output_tokens",
                "cache_creation_input_tokens", "cache_read_input_tokens")


def _message_dict(message) -> dict:
    return {
        "text": "".join(b.text for b in message.content if b.type == "text"),
        "stop_reason": message.stop_reason,
        "usage": {name: getattr(message.usage, name, None) or 0
                  for name in USAGE_FIELDS},
    }


class AnthropicTransport:
    """The transport for live runs, on the official ``anthropic`` SDK."""

    def __init__(self, api_key: str):
        try:
            import anthropic
        except ImportError:
            raise SystemExit("the anthropic SDK is missing: install the "
                             "silver-correction extra "
                             "(uv pip install -e '.[silver-correction]')")
        self._client = anthropic.Anthropic(api_key=api_key)

    def create_message(self, params: dict) -> dict:
        return _message_dict(self._client.messages.create(**params))

    def count_tokens(self, params: dict) -> int:
        counted = {k: v for k, v in params.items() if k != "max_tokens"}
        return self._client.messages.count_tokens(**counted).input_tokens

    def submit_batch(self, requests: Sequence[dict]) -> str:
        return self._client.messages.batches.create(requests=list(requests)).id

    def batch_status(self, batch_id: str) -> str:
        return self._client.messages.batches.retrieve(batch_id).processing_status

    def batch_results(self, batch_id: str) -> Iterator[Tuple[str, dict]]:
        for item in self._client.messages.batches.results(batch_id):
            if item.result.type == "succeeded":
                yield item.custom_id, _message_dict(item.result.message)
            else:
                yield item.custom_id, {"error": item.result.type}


# ─── rows, engine and prompts ───────────────────────────────────────────────

@dataclass(frozen=True)
class Row:
    dataset: str
    lect: str
    id: str
    sentence: str
    ipa: str
    source_row: Dict[str, str] = field(default_factory=dict)


def set_lects(dataset: str) -> List[str]:
    if dataset in LOCAL_SETS:
        return sorted(p.stem for p in (GOLD_DIR / dataset).glob("*.tsv"))
    return list(benchmark.DATASETS[dataset][1])


def _local_rows(dataset: str, lect: str, limit: int) -> List[Row]:
    rows: List[Row] = []
    with open(GOLD_DIR / dataset / f"{lect}.tsv", encoding="utf-8") as fh:
        for record in csv.DictReader(fh, delimiter="\t"):
            sentence = (record.get("sentence") or "").strip()
            ipa = (record.get("ipa") or "").strip()
            if not sentence or not ipa:
                continue
            extra = {k: v for k, v in record.items()
                     if k not in ("id", "sentence", "ipa")}
            rows.append(Row(dataset, lect, record["id"], sentence, ipa, extra))
            if len(rows) >= limit:
                break
    return rows


def _remote_rows(dataset: str, lect: str, limit: int) -> List[Row]:
    loader = benchmark.DATASETS[dataset][0]
    return [Row(dataset, lect, f"{lect}-{n:04d}", text, ipa)
            for n, (text, ipa) in enumerate(loader(lect, limit), 1)]


def load_rows(datasets: Sequence[str], lects: Optional[Sequence[str]],
              limit: Optional[int]) -> List[Row]:
    """The rows of *datasets*, restricted to *lects* when given, at most
    *limit* rows per lect."""
    cap = sys.maxsize if limit is None else limit
    rows: List[Row] = []
    for dataset in datasets:
        read = _local_rows if dataset in LOCAL_SETS else _remote_rows
        for lect in set_lects(dataset):
            if lects is None or lect in lects:
                rows.extend(read(dataset, lect, cap))
    return rows


@functools.lru_cache(maxsize=None)
def _engine(lect: str) -> orthography2ipa.G2P:
    return orthography2ipa.G2P(lect)


def engine_ipa(row: Row) -> str:
    """The engine output for *row*, through the API the scorer uses for an
    entry of its granularity."""
    engine = _engine(row.lect)
    if benchmark._is_multiword(row.sentence):
        return engine.transcribe(row.sentence)
    return engine.transcribe_word(row.sentence)


def _cite(source) -> str:
    parts = [f"{source.id}: {source.author} ({source.year}). {source.title}."]
    if source.publisher:
        parts.append(f"{source.publisher}.")
    if source.pages:
        parts.append(f"{source.pages}.")
    if source.notes:
        parts.append(source.notes)
    return " ".join(parts)


@functools.lru_cache(maxsize=None)
def system_text(lect: str) -> str:
    """The task instructions and the lect's notes and cited sources."""
    spec = orthography2ipa.get(lect)
    lines = [SYSTEM_TEXT + f"Lect: {spec.name} ({lect})", "", "Notes:",
             spec.notes.strip() or "(none)", "", "Cited sources:"]
    lines += [f"- {_cite(s)}" for s in spec.sources] or ["(none)"]
    return "\n".join(lines)


def build_request(pass_name: str, row: Row, *, engine: str,
                  a: Optional[str], b: Optional[str], model: str,
                  effort: str, max_tokens: int) -> dict:
    """Messages API parameters for one pass over one row. Passes A and B
    receive neither *engine* nor the row's existing ``ipa``."""
    if pass_name == "C":
        user = USER_TEXT["C"].format(sentence=row.sentence, a=a, b=b,
                                     engine=engine)
    else:
        user = USER_TEXT[pass_name].format(sentence=row.sentence)
    return {
        "model": model,
        "max_tokens": max_tokens,
        "system": [{"type": "text", "text": system_text(row.lect),
                    "cache_control": {"type": "ephemeral"}}],
        "messages": [{"role": "user", "content": user}],
        "output_config": {"effort": effort,
                          "format": {"type": "json_schema",
                                     "schema": SCHEMAS[pass_name]}},
    }


def prompt_hash(params: dict) -> str:
    prompt = {k: v for k, v in params.items()
              if k not in ("model", "max_tokens")}
    blob = json.dumps(prompt, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def cache_key(dataset: str, row_id: str, model: str, prompt: str) -> str:
    blob = json.dumps([dataset, row_id, model, prompt], ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


# ─── agreement ──────────────────────────────────────────────────────────────

def _broad(ipa: str, lect: str) -> str:
    return benchmark.normalize(ipa, strip_stress=True, broad=True,
                               extra_strip=benchmark._prosody_marks(lect))


def same_ipa(x: str, y: str, lect: str) -> bool:
    """Equal under the scorer's broad normalisation for *lect*."""
    return _broad(x, lect) == _broad(y, lect)


def needs_adjudication(a: str, b: str, engine: str, lect: str) -> bool:
    """Pass C runs unless A, B and the engine all agree."""
    return not (same_ipa(a, b, lect) and same_ipa(a, engine, lect))


def parse_result(pass_name: str, message: dict) -> Tuple[Optional[dict], str]:
    """The pass's JSON object, or ``None`` and the reason it is unusable."""
    if "error" in message:
        return None, f"batch item {message['error']}"
    if message["stop_reason"] != "end_turn":
        return None, f"stop_reason {message['stop_reason']}"
    try:
        data = json.loads(message["text"])
    except json.JSONDecodeError:
        return None, "response is not JSON"
    schema = SCHEMAS[pass_name]
    if not isinstance(data, dict) or set(data) != set(schema["required"]):
        return None, "response does not match the pass schema"
    if not isinstance(data["ipa"], str) or not data["ipa"].strip():
        return None, "response has an empty ipa"
    if pass_name == "C" and data["flag"] not in FLAGS:
        return None, "response has an unknown flag"
    return data, ""


# ─── spend ──────────────────────────────────────────────────────────────────

def usd(input_tokens: int, output_tokens: int, model: str, *, batch: bool,
        cache_write_tokens: int = 0, cache_read_tokens: int = 0,
        prices: Mapping[str, Price] = PRICES) -> float:
    price = prices[model]
    total = (input_tokens * price.input
             + cache_write_tokens * price.input * CACHE_WRITE_FACTOR
             + cache_read_tokens * price.cache_read
             + output_tokens * price.output) / 1_000_000
    return total * (BATCH_DISCOUNT if batch else 1.0)


def upper_bound_tokens(params: dict) -> Tuple[int, int]:
    """``(input, output)`` token bounds for one request: one input token
    per UTF-8 byte of the prompt plus :data:`REQUEST_OVERHEAD_TOKENS`, and
    ``max_tokens`` output tokens."""
    text = "".join(block["text"] for block in params["system"])
    text += "".join(m["content"] for m in params["messages"])
    text += json.dumps(params["output_config"]["format"]["schema"],
                       ensure_ascii=False)
    return (len(text.encode("utf-8")) + REQUEST_OVERHEAD_TOKENS,
            params["max_tokens"])


@dataclass
class Spend:
    requests: int = 0
    input: int = 0
    cache_write: int = 0
    cache_read: int = 0
    output: int = 0
    usd: float = 0.0

    def add(self, usage: Mapping[str, int], model: str, *, batch: bool,
            prices: Mapping[str, Price]) -> None:
        self.requests += 1
        self.input += usage["input_tokens"]
        self.cache_write += usage["cache_creation_input_tokens"]
        self.cache_read += usage["cache_read_input_tokens"]
        self.output += usage["output_tokens"]
        self.usd += usd(usage["input_tokens"], usage["output_tokens"], model,
                        batch=batch,
                        cache_write_tokens=usage["cache_creation_input_tokens"],
                        cache_read_tokens=usage["cache_read_input_tokens"],
                        prices=prices)

    def line(self) -> str:
        return (f"actual: {self.requests} requests, input {self.input} tokens "
                f"(cache write {self.cache_write}, cache read "
                f"{self.cache_read}), output {self.output} tokens, "
                f"${self.usd:.4f}")


# ─── cache ──────────────────────────────────────────────────────────────────

class Cache:
    """Responses already paid for, and batches submitted but not collected.

    ``responses.jsonl`` is append-only, one record per usable response.
    ``pending_batches.json`` lists each pending batch with the cache record
    each of its requests will fill."""

    def __init__(self, directory: Path):
        self.directory = directory
        self.responses = directory / "responses.jsonl"
        self.pending_file = directory / "pending_batches.json"
        self.records: Dict[str, dict] = {}
        if self.responses.exists():
            for line in self.responses.read_text("utf-8").splitlines():
                record = json.loads(line)
                self.records[record["key"]] = record
        self.pending: List[dict] = (
            json.loads(self.pending_file.read_text("utf-8"))
            if self.pending_file.exists() else [])

    def result(self, key: str) -> Optional[dict]:
        record = self.records.get(key)
        return None if record is None else record["result"]

    def put(self, record: dict) -> None:
        self.directory.mkdir(parents=True, exist_ok=True)
        with open(self.responses, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        self.records[record["key"]] = record

    def pending_keys(self) -> set:
        return {meta["key"] for batch in self.pending
                for meta in batch["requests"].values()}

    def save_pending(self) -> None:
        self.directory.mkdir(parents=True, exist_ok=True)
        tmp = self.pending_file.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.pending, ensure_ascii=False, indent=1),
                       "utf-8")
        os.replace(tmp, self.pending_file)


# ─── planning ───────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Request:
    """One pass over one row, with its cache identity."""
    row: Row
    pass_name: str
    params: dict
    prompt: str
    key: str

    def meta(self) -> dict:
        return {"key": self.key, "dataset": self.row.dataset,
                "lect": self.row.lect, "row_id": self.row.id,
                "pass": self.pass_name, "model": self.params["model"],
                "prompt_hash": self.prompt}


@dataclass(frozen=True)
class Settings:
    model: str
    effort: str
    max_tokens: int

    def request(self, pass_name: str, row: Row, engine: str,
                a: Optional[str] = None, b: Optional[str] = None) -> Request:
        params = build_request(pass_name, row, engine=engine, a=a, b=b,
                               model=self.model, effort=self.effort,
                               max_tokens=self.max_tokens)
        prompt = prompt_hash(params)
        key = cache_key(row.dataset, row.id, self.model, prompt)
        return Request(row, pass_name, params, prompt, key)


@dataclass
class Job:
    row: Row
    engine: str


def blind_requests(job: Job, settings: Settings) -> List[Request]:
    return [settings.request(name, job.row, job.engine) for name in "AB"]


def adjudication_request(job: Job, settings: Settings,
                         cache: Cache) -> Optional[Request]:
    """Pass C for *job*, or ``None`` when A or B is unknown or C is not
    needed."""
    a, b = (cache.result(r.key) for r in blind_requests(job, settings))
    if a is None or b is None:
        return None
    if not needs_adjudication(a["ipa"], b["ipa"], job.engine, job.row.lect):
        return None
    return settings.request("C", job.row, job.engine, a["ipa"], b["ipa"])


@dataclass
class Estimate:
    cached: int = 0
    blind: int = 0
    adjudication: int = 0
    input: int = 0
    output: int = 0

    def add(self, request: Request, counter: Optional[Callable]) -> None:
        tokens_in, tokens_out = upper_bound_tokens(request.params)
        if counter is not None:
            tokens_in = counter(request.params)
        self.input += tokens_in
        self.output += tokens_out


def estimate(jobs: Sequence[Job], settings: Settings, cache: Cache,
             counter: Optional[Callable] = None) -> Estimate:
    """Upper bounds for every request the run still has to pay for. Pass C
    is counted for every row whose A or B is unknown, with the engine output
    standing in for A and B."""
    skip = set(cache.records) | cache.pending_keys()
    total = Estimate()
    for job in jobs:
        blind = blind_requests(job, settings)
        for request in blind:
            if request.key in skip:
                total.cached += 1
            else:
                total.blind += 1
                total.add(request, counter)
        if all(cache.result(r.key) is not None for r in blind):
            adjudication = adjudication_request(job, settings, cache)
        else:
            adjudication = settings.request("C", job.row, job.engine,
                                            job.engine, job.engine)
        if adjudication is None:
            continue
        if adjudication.key in skip:
            total.cached += 1
        else:
            total.adjudication += 1
            total.add(adjudication, counter)
    return total


# ─── output ─────────────────────────────────────────────────────────────────

def output_row(job: Job, settings: Settings, cache: Cache) -> Optional[dict]:
    """The corrected row, or ``None`` while a pass it needs is missing."""
    a, b = (cache.result(r.key) for r in blind_requests(job, settings))
    if a is None or b is None:
        return None
    c = None
    if needs_adjudication(a["ipa"], b["ipa"], job.engine, job.row.lect):
        request = settings.request("C", job.row, job.engine, a["ipa"],
                                   b["ipa"])
        c = cache.result(request.key)
        if c is None:
            return None
    row = job.row
    return {
        "dataset": row.dataset, "lect": row.lect, "id": row.id,
        "sentence": row.sentence,
        "ipa": a["ipa"] if c is None else c["ipa"],
        "ipa_llm_original": row.ipa,
        "ipa_engine": job.engine,
        "model": settings.model,
        "passes": {"A": a["ipa"], "B": b["ipa"], "C": c},
        "flag": "agreed" if c is None else c["flag"],
        "reason": AGREED_REASON if c is None else c["reason"],
        "tier": TIER,
        "source_row": row.source_row,
    }


def output_path(out_dir: Path, dataset: str) -> Path:
    return out_dir / f"{dataset}.llm-corrected.jsonl"


def write_outputs(jobs: Sequence[Job], settings: Settings, cache: Cache,
                  out_dir: Path, reporter: Reporter) -> None:
    """Merge the finished rows into each set's output file, sorted by lect
    and id. Rows from earlier runs stay unless this run rewrote them."""
    by_set: Dict[str, List[dict]] = {}
    missing = 0
    for job in jobs:
        row = output_row(job, settings, cache)
        if row is None:
            missing += 1
        else:
            by_set.setdefault(row["dataset"], []).append(row)
    for dataset, rows in sorted(by_set.items()):
        path = output_path(out_dir, dataset)
        merged: Dict[Tuple[str, str], dict] = {}
        if path.exists():
            for line in path.read_text("utf-8").splitlines():
                old = json.loads(line)
                merged[(old["lect"], old["id"])] = old
        merged.update({(r["lect"], r["id"]): r for r in rows})
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8") as fh:
            for _, record in sorted(merged.items()):
                fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        os.replace(tmp, path)
        reporter.say(f"wrote {len(rows)} rows to {path} "
                     f"({len(merged)} rows in the file)")
    if missing:
        reporter.say(f"{missing} rows are incomplete; run the same command "
                     f"again to finish them")


# ─── live runs ──────────────────────────────────────────────────────────────

@dataclass
class Run:
    transport: Transport
    settings: Settings
    cache: Cache
    reporter: Reporter
    prices: Mapping[str, Price]
    max_usd: float
    spend: Spend = field(default_factory=Spend)

    def record(self, meta: dict, message: dict, *, batch: bool) -> bool:
        """Cache a usable response; report an unusable one."""
        if "usage" in message:
            self.spend.add(message["usage"], meta["model"], batch=batch,
                           prices=self.prices)
        result, problem = parse_result(meta["pass"], message)
        if result is None:
            self.reporter.say(f"{meta['dataset']} {meta['row_id']} pass "
                              f"{meta['pass']}: unusable response, "
                              f"{problem}", error=True)
            return False
        self.cache.put(dict(meta, result=result, usage=message["usage"],
                            batch=batch))
        return True

    # sync

    def send(self, request: Request) -> bool:
        tokens_in, tokens_out = upper_bound_tokens(request.params)
        bound = usd(tokens_in, tokens_out, self.settings.model, batch=False,
                    prices=self.prices)
        if self.spend.usd + bound > self.max_usd:
            raise CapReached(
                f"stopping: the next request could take the spend of this "
                f"run past --max-usd ${self.max_usd:.4f}")
        message = self.transport.create_message(request.params)
        return self.record(request.meta(), message, batch=False)

    def run_sync(self, jobs: Sequence[Job]) -> None:
        for job in jobs:
            for request in blind_requests(job, self.settings):
                if self.cache.result(request.key) is None:
                    if not self.send(request):
                        break
            adjudication = adjudication_request(job, self.settings,
                                                self.cache)
            if adjudication and self.cache.result(adjudication.key) is None:
                self.send(adjudication)

    # batch

    def submit(self, requests: Sequence[Request]) -> None:
        for start in range(0, len(requests), BATCH_CHUNK):
            chunk = requests[start:start + BATCH_CHUNK]
            batch_id = self.transport.submit_batch(
                [{"custom_id": r.key, "params": r.params} for r in chunk])
            self.cache.pending.append(
                {"batch_id": batch_id,
                 "requests": {r.key: r.meta() for r in chunk}})
            self.cache.save_pending()
            self.reporter.say(f"submitted batch {batch_id} with "
                              f"{len(chunk)} requests")

    def collect(self, wait: bool, poll_seconds: float) -> bool:
        """Collect every pending batch. ``False`` when a batch is still
        running and *wait* is off."""
        for batch in list(self.cache.pending):
            status = self.transport.batch_status(batch["batch_id"])
            while status != "ended":
                if not wait:
                    self.reporter.say(f"batch {batch['batch_id']} is "
                                      f"{status}; run the same command again "
                                      f"to collect it")
                    return False
                time.sleep(poll_seconds)
                status = self.transport.batch_status(batch["batch_id"])
            for custom_id, message in self.transport.batch_results(
                    batch["batch_id"]):
                self.record(batch["requests"][custom_id], message, batch=True)
            self.cache.pending.remove(batch)
            self.cache.save_pending()
            self.reporter.say(f"collected batch {batch['batch_id']}")
        return True

    def run_batches(self, jobs: Sequence[Job], wait: bool,
                    poll_seconds: float) -> None:
        if not self.collect(wait, poll_seconds):
            return
        skip = set(self.cache.records)
        blind = [r for job in jobs for r in blind_requests(job, self.settings)
                 if r.key not in skip]
        if blind:
            self.submit(blind)
            if not self.collect(wait, poll_seconds):
                return
        adjudication = [r for r in (adjudication_request(job, self.settings,
                                                         self.cache)
                                    for job in jobs)
                        if r is not None and r.key not in self.cache.records]
        if adjudication:
            self.submit(adjudication)
            self.collect(wait, poll_seconds)


class CapReached(Exception):
    pass


# ─── command line ───────────────────────────────────────────────────────────

def parse_args(argv: Optional[Sequence[str]]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dataset", nargs="+", choices=SILVER_SETS,
                    default=list(SILVER_SETS),
                    help="sets to correct (default: every LLM-generated set)")
    ap.add_argument("--lect", nargs="+",
                    help="only these lects (default: every lect of the sets)")
    ap.add_argument("--limit", type=int,
                    help="at most this many rows per lect, in file order")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--effort", default="high",
                    choices=("low", "medium", "high", "xhigh", "max"))
    ap.add_argument("--max-tokens", type=int, default=8000,
                    help="output token limit per request, thinking included")
    ap.add_argument("--max-usd", type=float,
                    help="refuse to start when the estimate exceeds this; "
                         "required unless --dry-run")
    ap.add_argument("--usd-per-mtok", nargs=2, type=float,
                    metavar=("INPUT", "OUTPUT"),
                    help="US dollars per million input and output tokens, "
                         "for a model the price table does not hold; cache "
                         "reads are priced at a tenth of the input price")
    ap.add_argument("--sync", action="store_true",
                    help="one request at a time instead of the Message "
                         "Batches API")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the estimate; no key, no API call")
    ap.add_argument("--count-tokens", action="store_true",
                    help="estimate input with the token-counting endpoint "
                         "instead of the byte bound")
    ap.add_argument("--no-wait", action="store_true",
                    help="submit or collect batches, then exit")
    ap.add_argument("--poll-seconds", type=float, default=60.0)
    ap.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE_DIR)
    ap.add_argument("--out-dir", type=Path, default=GOLD_DIR)
    args = ap.parse_args(argv)
    if args.max_usd is None and not args.dry_run:
        ap.error("--max-usd is required unless --dry-run")
    if args.count_tokens and args.dry_run:
        ap.error("--count-tokens calls the API; it cannot run with --dry-run")
    return args


def execute(args: argparse.Namespace, jobs: Sequence[Job],
            settings: Settings, cache: Cache, transport: Optional[Transport],
            reporter: Reporter, prices: Mapping[str, Price]) -> int:
    """Estimate, check the cap, run, and write the finished rows."""
    counter = transport.count_tokens if args.count_tokens else None
    planned = estimate(jobs, settings, cache, counter)
    batch = not args.sync
    bound = usd(planned.input, planned.output, settings.model, batch=batch,
                prices=prices)
    reporter.say(f"passes: {planned.cached} cached or pending, "
                 f"{planned.blind} A/B to request, at most "
                 f"{planned.adjudication} C to request")
    reporter.say(f"estimate: ${bound:.4f} upper bound (input at most "
                 f"{planned.input} tokens, output at most {planned.output} "
                 f"tokens, {'batch' if batch else 'sync'} prices)")
    if args.dry_run:
        if args.max_usd is not None:
            verdict = "within" if bound <= args.max_usd else "above"
            reporter.say(f"the estimate is {verdict} --max-usd "
                         f"${args.max_usd:.4f}")
        return 0
    if bound > args.max_usd:
        reporter.say(f"refusing to start: the estimate ${bound:.4f} is above "
                     f"--max-usd ${args.max_usd:.4f}")
        return 3

    run = Run(transport, settings, cache, reporter, prices, args.max_usd)
    try:
        if args.sync:
            run.run_sync(jobs)
        else:
            run.run_batches(jobs, wait=not args.no_wait,
                            poll_seconds=args.poll_seconds)
    except CapReached as exc:
        reporter.say(str(exc))
        return 3
    finally:
        reporter.say(run.spend.line())
        write_outputs(jobs, settings, cache, args.out_dir, reporter)
    return 0


def main(argv: Optional[Sequence[str]] = None, *,
         env: Optional[Mapping[str, str]] = None,
         transport_factory: Optional[Callable[[str], Transport]]
         = AnthropicTransport) -> int:
    args = parse_args(argv)
    env = os.environ if env is None else env
    reporter = Reporter(None if args.dry_run else args.cache_dir / "run.log")

    prices = dict(PRICES)
    if args.usd_per_mtok:
        tokens_in, tokens_out = args.usd_per_mtok
        prices[args.model] = Price(tokens_in, tokens_out, tokens_in * 0.1)
    if args.model not in prices:
        reporter.say(f"no price for {args.model}: pass --usd-per-mtok",
                     error=True)
        return 2

    if args.lect:
        known = {lect for d in args.dataset for lect in set_lects(d)}
        unknown = sorted(set(args.lect) - known)
        if unknown:
            reporter.say(f"no selected set has the lects {unknown}",
                         error=True)
            return 2
    rows = load_rows(args.dataset, args.lect, args.limit)
    if not rows:
        reporter.say("no rows selected", error=True)
        return 2
    jobs = [Job(row, engine_ipa(row)) for row in rows]
    lects = {(r.dataset, r.lect) for r in rows}
    reporter.say(f"rows: {len(rows)} in {len(lects)} lects of "
                 f"{len({d for d, _ in lects})} sets; model {args.model}, "
                 f"effort {args.effort}")

    transport = None
    if not args.dry_run:
        try:
            key = load_api_key(env)
        except CredentialError as exc:
            reporter.say(str(exc), error=True)
            return 2
        reporter.secrets.append(key)
        transport = transport_factory(key)
    settings = Settings(args.model, args.effort, args.max_tokens)
    try:
        return execute(args, jobs, settings, Cache(args.cache_dir), transport,
                       reporter, prices)
    except Exception:  # transport errors: report them through redaction
        reporter.say(traceback.format_exc(), error=True)
        return 2

if __name__ == "__main__":
    sys.exit(main())
