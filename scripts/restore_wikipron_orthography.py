#!/usr/bin/env python3
"""Restore the display headword onto a WikiPron gold's orthography column.

WikiPron scrapes the English Wiktionary MediaWiki *page title*, not the
headword Wiktionary displays. Several language style policies strip
diacritics from titles while keeping them in the display form, so for
those languages the gold's orthographic input is lossy — it no longer
encodes distinctions the gold IPA still transcribes.

``Wiktionary:About Middle High German`` states the policy verbatim:

    certain letters with diacritics (ë ā ē ī ō ū ȥ) are not used in
    article titles, but are used when displaying the word

    this does not apply to the umlauted vowels ä, ö, ü, æ, œ, which are
    treated as separate letters and thus appear in titles like any other
    letter

The display form is recoverable from the MediaWiki API. This script
fetches a WikiPron gold file, reads each page, and takes the headword
that Wiktionary renders for the target language. The IPA column is never
touched.

Correctness rules, in order of importance:

* A Wiktionary page holds many language sections. ``Adam`` renders an
  English ``Adam`` and an Ewe ``Ádàm``. Extraction is scoped twice: the
  wikitext is cut down to the target ``==Language==`` section before any
  headword template is read, and the rendered headword is matched on its
  ``lang`` attribute. A page-wide match would silently import another
  language's orthography.
* Nothing is guessed. A page with no headword, no target section, or two
  conflicting headwords for the target language emits no row and counts
  as uncovered.
* A restored form must differ from the title only in diacritics. The
  base-letter skeleton (NFD with combining marks removed) has to match,
  or the row is discarded and counted as a skeleton mismatch.

Usage::

    python scripts/restore_wikipron_orthography.py ee gmh yo he --out-dir out/
"""
from __future__ import annotations

import argparse
import concurrent.futures
import html
import json
import os
import re
import sys
import threading
import time
import unicodedata
import urllib.parse
import urllib.request
from typing import Dict, Iterable, List, Optional, Set, Tuple

WIKIPRON_BASE = (
    "https://raw.githubusercontent.com/CUNY-CL/wikipron/master/data/"
    "scrape/tsv/"
)
API = "https://en.wiktionary.org/w/api.php"
USER_AGENT = (
    "orthography2ipa-wikipron-restore/1.0 "
    "(https://github.com/TigreGotico/orthography2ipa; openvoiceos@gmail.com)"
)
CACHE_DIR = os.environ.get(
    "O2I_WIKT_CACHE", os.path.expanduser("~/tmp/o2i-wiktionary-cache"))

#: One entry per affected WikiPron gold: the scrape file, the English
#: Wiktionary ``==L2==`` section heading, and the Wiktionary language code
#: that headword templates are tagged with.
LANGS: Dict[str, Tuple[str, str, str]] = {
    "ee": ("ewe_latn_broad.tsv", "Ewe", "ee"),
    "gmh": ("gmh_latn_broad.tsv", "Middle High German", "gmh"),
    "yo": ("yor_latn_broad.tsv", "Yoruba", "yo"),
    "he": ("heb_hebr_broad.tsv", "Hebrew", "he"),
}

#: Requests per second against the MediaWiki API. Deliberately gentle.
RATE = float(os.environ.get("O2I_WIKT_RATE", "3"))
#: Concurrent in-flight requests. Round-trip latency, not throughput, is
#: the limit here; a handful of workers under the same global rate cap
#: keeps the load on Wikimedia identical while the wall clock drops.
WORKERS = int(os.environ.get("O2I_WIKT_WORKERS", "4"))
_last_call = [0.0]
_rate_lock = threading.Lock()


def _throttle() -> None:
    with _rate_lock:
        wait = _last_call[0] + 1.0 / RATE - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        _last_call[0] = max(time.monotonic(), _last_call[0] + 1.0 / RATE)


def _get(url: str, data: Optional[bytes] = None) -> str:
    _throttle()
    req = urllib.request.Request(url, data=data,
                                 headers={"User-Agent": USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return fh.read().decode("utf-8")
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def _write_atomic(path: str, text: str) -> None:
    """Write via a sibling temp file: an interrupted run must not leave a
    truncated file behind that the next run treats as a cache hit."""
    tmp = f"{path}.part-{os.getpid()}-{threading.get_ident()}"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.replace(tmp, path)


def _cache_path(kind: str, key: str) -> str:
    safe = urllib.parse.quote(key, safe="")[:180]
    d = os.path.join(CACHE_DIR, kind)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, safe + ".txt")


# ─── skeleton / normalization helpers ───────────────────────────────────────

def skeleton(word: str) -> str:
    """The base-letter spine: NFD, combining marks dropped, then NFC."""
    decomposed = unicodedata.normalize("NFD", word)
    return unicodedata.normalize(
        "NFC", "".join(c for c in decomposed if not unicodedata.combining(c)))


_TAG = re.compile(r"<[^>]+>")
_WIKILINK = re.compile(r"\[\[(?:[^\[\]|]*\|)?([^\[\]|]*)\]\]")


def clean_wiki(value: str) -> str:
    value = _WIKILINK.sub(r"\1", value)
    value = value.replace("'''", "").replace("''", "")
    value = _TAG.sub("", value)
    return unicodedata.normalize("NFC", value.strip())


def has_residue(value: str) -> bool:
    """True if template or markup leftovers survived cleaning."""
    return bool(set("{}[]|<>=") & set(value)) or not value


# ─── wikitext: section scoping and candidate detection ──────────────────────

_L2 = re.compile(r"^==\s*([^=].*?)\s*==\s*$", re.M)


def language_section(wikitext: str, section_name: str) -> Optional[str]:
    """The ``==Language==`` section body, or None when absent.

    This is the guard against importing another language's orthography:
    every downstream read happens inside the returned slice.
    """
    bounds = [(m.start(), m.end(), m.group(1)) for m in _L2.finditer(wikitext)]
    for i, (_, end, name) in enumerate(bounds):
        if name == section_name:
            stop = bounds[i + 1][0] if i + 1 < len(bounds) else len(wikitext)
            return wikitext[end:stop]
    return None


_TEMPLATE = re.compile(r"\{\{([^{}]*)\}\}")


def headword_args(section: str, code: str) -> Set[str]:
    """Values a headword template in *section* could be displaying.

    Recognises ``{{head|<code>|…}}`` and the per-language ``{{<code>-…}}``
    headword templates. The values are candidates only — they decide
    whether the page is worth rendering, never what gets written out.
    """
    out: Set[str] = set()
    for body in _TEMPLATE.findall(section):
        parts = body.split("|")
        name = parts[0].strip()
        if name == "head":
            if len(parts) < 2 or parts[1].strip() != code:
                continue
            # ``{{head|ee|noun|…}}``: parameter 1 is the language code
            # itself, never a headword
            parts = parts[1:]
        elif not name.startswith(code + "-"):
            continue
        for part in parts[1:]:
            value = part.split("=", 1)[1] if "=" in part else part
            value = value.split("<", 1)[0]
            out.add(clean_wiki(value))
    return {v for v in out if v}


def worth_rendering(title: str, section: str, code: str) -> bool:
    """Whether any headword argument looks like a diacritic restoration.

    A page whose headword templates carry no argument sharing the title's
    skeleton has nothing to restore, and is skipped without spending an
    API render.
    """
    spine = skeleton(title)
    return any(skeleton(v) == spine and v != title
               for v in headword_args(section, code))


# ─── rendered HTML: the authoritative display form ──────────────────────────

_HEADWORD = re.compile(
    r'<strong[^>]*class="[^"]*\bheadword\b[^"]*"[^>]*lang="([^"]+)"[^>]*>'
    r'(.*?)</strong>', re.S)


def rendered_headwords(page_html: str, code: str) -> Set[str]:
    """Display headwords the page renders for language *code*."""
    return {clean_wiki(html.unescape(text))
            for lang, text in _HEADWORD.findall(page_html)
            if lang == code}


# ─── API ────────────────────────────────────────────────────────────────────

def _fetch_wikitext_batch(batch: List[str]) -> Dict[str, str]:
    """One 50-title revision query, written straight into the cache."""
    query = {
        "action": "query", "prop": "revisions", "rvslots": "main",
        "rvprop": "content", "format": "json", "formatversion": "2",
        "titles": "|".join(batch),
    }
    data = json.loads(_get(API, urllib.parse.urlencode(query).encode()))
    got = {}
    for page in data.get("query", {}).get("pages", []):
        revs = page.get("revisions")
        got[page["title"]] = (
            revs[0]["slots"]["main"]["content"] if revs else "")
    # normalized and redirected titles come back renamed; map them back
    norm = {n["to"]: n["from"]
            for n in data.get("query", {}).get("normalized", [])}
    out = {t: "" for t in batch}
    for title, text in got.items():
        key = norm.get(title, title)
        if key in out:
            out[key] = text
    for title, text in out.items():
        _write_atomic(_cache_path("wikitext", title), text)
    return out


def fetch_wikitext(titles: List[str]) -> Dict[str, str]:
    """Wikitext for *titles*, batched 50 per request and cached to disk."""
    out: Dict[str, str] = {}
    missing = []
    for title in titles:
        path = _cache_path("wikitext", title)
        if os.path.exists(path):
            out[title] = open(path, encoding="utf-8").read()
        else:
            missing.append(title)
    batches = [missing[i:i + 50] for i in range(0, len(missing), 50)]
    if batches:
        with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as p:
            for got in p.map(_fetch_wikitext_batch, batches):
                out.update(got)
    return out


def fetch_render(title: str) -> str:
    """Rendered HTML for the whole page *title*.

    Expanding only the section's headword templates instead is roughly
    twice as fast on a warm API, but its natural cache key is the page
    title while its result depends on the language whose templates were
    sent — ``ade`` is both an Ewe and a Yoruba entry — so the saving buys
    a cache that silently returns another language's headword. The page
    render has no such split: one page, one result, scoped afterwards by
    the ``lang`` attribute.
    """
    path = _cache_path("html", title)
    if os.path.exists(path):
        return open(path, encoding="utf-8").read()
    query = {"action": "parse", "page": title, "prop": "text",
             "format": "json", "formatversion": "2"}
    body = _get(API, urllib.parse.urlencode(query).encode())
    text = json.loads(body).get("parse", {}).get("text", "")
    _write_atomic(path, text)
    return text


def prefetch_renders(titles: List[str]) -> None:
    """Warm the render cache for *titles* with a few workers in flight."""
    todo = [t for t in titles if not os.path.exists(_cache_path("html", t))]
    if not todo:
        return
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        for n, _ in enumerate(pool.map(fetch_render, todo), 1):
            if n % 200 == 0:
                print(f"   rendered {n}/{len(todo)}", file=sys.stderr,
                      flush=True)


def fetch_gold(fname: str) -> List[Tuple[str, str]]:
    path = _cache_path("gold", fname)
    if os.path.exists(path):
        text = open(path, encoding="utf-8").read()
    else:
        text = _get(WIKIPRON_BASE + fname)
        _write_atomic(path, text)
    rows = []
    for line in text.strip().split("\n"):
        parts = line.split("\t")
        if len(parts) == 2:
            rows.append((parts[0], parts[1]))
    return rows


# ─── the restoration itself ─────────────────────────────────────────────────

def restore_word(title: str, wikitext: str, section_name: str, code: str,
                 render) -> Tuple[Optional[str], str]:
    """Return ``(restored_or_None, outcome)`` for one gold row.

    Outcomes: ``restored``, ``unchanged`` (the title already is the
    display form), ``no_section``, ``no_headword``, ``conflict``,
    ``residue`` or ``skeleton_mismatch``.
    """
    section = language_section(wikitext, section_name)
    if section is None:
        return None, "no_section"
    if not worth_rendering(title, section, code):
        return None, "no_headword"
    heads = rendered_headwords(render(title), code)
    heads = {h for h in heads if h}
    if not heads:
        return None, "no_headword"
    if len(heads) > 1:
        return None, "conflict"
    head = unicodedata.normalize("NFC", heads.pop())
    if has_residue(head):
        return None, "residue"
    if head == unicodedata.normalize("NFC", title):
        return None, "unchanged"
    if skeleton(head) != skeleton(title):
        return None, "skeleton_mismatch"
    return head, "restored"


def restore_language(lang: str, limit: int = 0):
    fname, section_name, code = LANGS[lang]
    gold = fetch_gold(fname)
    if limit:
        gold = gold[:limit]
    titles = sorted({w for w, _ in gold})
    wikitext = fetch_wikitext(titles)
    counts = {k: 0 for k in ("restored", "unchanged", "no_section",
                             "no_headword", "conflict", "residue",
                             "skeleton_mismatch")}
    rows: List[Tuple[str, str]] = []
    baseline: List[Tuple[str, str]] = []
    mismatches: List[Tuple[str, str]] = []
    prefetch_renders(
        [t for t in titles
         if (sec := language_section(wikitext.get(t, ""), section_name))
         is not None and worth_rendering(t, sec, code)])
    cache: Dict[str, Tuple[Optional[str], str]] = {}
    for word, ipa in gold:
        if word not in cache:
            cache[word] = restore_word(
                word, wikitext.get(word, ""), section_name, code, fetch_render)
        restored, outcome = cache[word]
        counts[outcome] += 1
        if outcome == "skeleton_mismatch":
            mismatches.append((word, ipa))
        if restored is None:
            continue
        rows.append((restored, ipa))
        baseline.append((word, ipa))
    return rows, baseline, counts, mismatches, len(gold)


def diacritic_rate(words: Iterable[str]) -> float:
    words = list(words)
    if not words:
        return 0.0
    marked = sum(1 for w in words if skeleton(w) != unicodedata.normalize(
        "NFC", w))
    return marked / len(words)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("langs", nargs="+", choices=sorted(LANGS))
    ap.add_argument("--out-dir", default=".")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args(argv)
    os.makedirs(args.out_dir, exist_ok=True)
    for lang in args.langs:
        rows, baseline, counts, mismatches, total = restore_language(
            lang, args.limit)
        before = diacritic_rate([w for w, _ in baseline])
        after = diacritic_rate([w for w, _ in rows])
        out = os.path.join(args.out_dir, f"{lang}.tsv")
        with open(out, "w", encoding="utf-8") as fh:
            fh.writelines(f"{w}\t{ipa}\n" for w, ipa in rows)
        print(f"{lang}: {total} rows, restored {counts['restored']}, "
              f"uncovered {total - counts['restored']}, "
              f"skeleton mismatches {counts['skeleton_mismatch']}, "
              f"diacritic coverage {before:.3f} -> {after:.3f}")
        print(f"   breakdown: {counts}")
        for word, _ in mismatches[:10]:
            print(f"   mismatch: {word}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
