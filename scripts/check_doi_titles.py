#!/usr/bin/env python3
"""Check that every DOI-bearing citation in ``orthography2ipa/data/`` points at
the work its spec says it does.

A DOI resolving is not evidence that it is the *right* DOI: it is only
evidence that the identifier is well-formed and registered. Several specs
have cited a real, resolvable DOI that belongs to an unrelated paper (issue
#1407) — the wrong identifier carried a wrong phonological analysis for as
long as nobody happened to follow the link. This script queries CrossRef for
every cited DOI and flags citations whose registered title does not match
the title recorded beside it, for human review.

It needs network access, so it does not belong in the ordinary pytest suite
(there is no offline snapshot to assert against, unlike
``check_glottolog_codes.py``). Run it periodically, and whenever a citation
with a DOI is added or edited::

    python scripts/check_doi_titles.py              # report only
    python scripts/check_doi_titles.py --lang kab    # scope to one spec

A full run resolves every distinct DOI once (about 80 lookups at the time of
writing) with a 0.1s delay between requests and a ``mailto:`` User-Agent, per
CrossRef's polite-pool convention. That took under two minutes.

## Why a naive similarity score is not enough

Specs legitimately append a series descriptor that CrossRef does not store,
writing "Amharic (Illustrations of the IPA)" where CrossRef has just
"Amharic". A plain difflib ratio on the full strings scores that as a
mismatch and buries the real defects under benign ones. The check here first
asks whether the CrossRef title survives as a normalized substring of the
spec title (or vice versa) — which the series-descriptor pattern always
satisfies — and only falls back to a difflib ratio, at a stricter threshold,
for the titles that fail the substring test.
"""
from __future__ import annotations

import argparse
import difflib
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

_DATA = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")
_MAILTO = "openvoiceos@gmail.com"
_UA = {"User-Agent": f"orthography2ipa DOI check (mailto:{_MAILTO})"}
_DELAY = 0.1
_RATIO_THRESHOLD = 0.55

_DOI_RE = re.compile(r"10\.\d{4,9}/\S+", re.IGNORECASE)


def normalize(title: str) -> str:
    """Lowercase, strip punctuation/parentheticals, collapse whitespace."""
    title = re.sub(r"\([^)]*\)", " ", title)  # drop parenthetical descriptors
    title = re.sub(r"[^\w\s]", " ", title.lower())
    return re.sub(r"\s+", " ", title).strip()


def extract_doi(url_or_doi: str) -> str | None:
    if not url_or_doi:
        return None
    m = _DOI_RE.search(url_or_doi)
    return m.group(0).rstrip(".,;)") if m else None


def iter_citations(lang: str | None = None):
    """Yield (spec_code, path, source_dict) for every sourced citation."""
    for path in sorted(glob.glob(os.path.join(_DATA, "*.json"))):
        code = os.path.splitext(os.path.basename(path))[0]
        if lang and code != lang:
            continue
        with open(path, encoding="utf-8") as fh:
            raw = json.load(fh)
        if not isinstance(raw, dict):
            continue
        for src in raw.get("sources", []) or []:
            doi = extract_doi(src.get("doi") or src.get("url") or "")
            if doi:
                yield code, path, src, doi


def crossref_title(doi: str) -> str | None:
    url = f"https://api.crossref.org/works/{doi}?mailto={_MAILTO}"
    req = urllib.request.Request(url, headers=_UA)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.load(resp)
            titles = data.get("message", {}).get("title") or []
            return titles[0] if titles else None
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            time.sleep(1 + attempt)
        except (urllib.error.URLError, TimeoutError):
            time.sleep(1 + attempt)
    return None


def titles_match(spec_title: str, crossref_title_: str) -> tuple[bool, float]:
    a, b = normalize(spec_title), normalize(crossref_title_)
    if not a or not b:
        return False, 0.0
    if a in b or b in a:
        return True, 1.0
    ratio = difflib.SequenceMatcher(None, a, b).ratio()
    return ratio >= _RATIO_THRESHOLD, ratio


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", help="restrict to a single spec code (e.g. kab)")
    args = ap.parse_args()

    # Resolve each distinct DOI once even if several specs cite it.
    citations = list(iter_citations(args.lang))
    dois = sorted({doi for *_, doi in citations})
    print(f"Checking {len(dois)} distinct DOI(s) across {len(citations)} citation(s)...",
          file=sys.stderr)

    resolved: dict[str, str | None] = {}
    for i, doi in enumerate(dois):
        resolved[doi] = crossref_title(doi)
        if resolved[doi] is None:
            print(f"  [{i + 1}/{len(dois)}] {doi} -> UNRESOLVED", file=sys.stderr)
        time.sleep(_DELAY)

    flagged = []
    unresolved = []
    for code, path, src, doi in citations:
        spec_title = src.get("title") or ""
        cr_title = resolved.get(doi)
        if cr_title is None:
            unresolved.append((code, doi, spec_title))
            continue
        ok, ratio = titles_match(spec_title, cr_title)
        if not ok:
            flagged.append((code, doi, spec_title, cr_title, ratio))

    if flagged:
        print("\n=== LOW TITLE SIMILARITY (human review) ===")
        for code, doi, spec_title, cr_title, ratio in sorted(flagged, key=lambda r: r[4]):
            print(f"\n{code}  doi:{doi}  ratio={ratio:.2f}")
            print(f"  spec title:     {spec_title}")
            print(f"  CrossRef title: {cr_title}")

    if unresolved:
        print("\n=== UNRESOLVED (not evidence of error; CrossRef does not index everything) ===")
        for code, doi, spec_title in unresolved:
            print(f"{code}  doi:{doi}  {spec_title}")

    print(f"\n{len(flagged)} flagged, {len(unresolved)} unresolved, "
          f"{len(dois) - len(flagged) - len(unresolved)} clean, out of {len(dois)} distinct DOIs.")
    return 1 if flagged else 0


if __name__ == "__main__":
    raise SystemExit(main())
