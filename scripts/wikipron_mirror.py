#!/usr/bin/env python3
"""Build the pinned WikiPron mirror with restored orthography.

WikiPron's ``data/scrape/tsv`` is a moving target: it lives on a branch
that upstream keeps editing, so a benchmark that reads it scores against
different data from one week to the next with no code change. This
script takes a snapshot at one commit, records that commit, and
republishes every file in a three-column schema that carries the
recovered display headword beside the scraped page title.

The schema is ``orthography``, ``restored_orthography``, ``ipa``. The
first and third columns are WikiPron's own two columns, byte for byte.
The second is the headword English Wiktionary displays for that language
where ``restore_wikipron_orthography.py`` could recover it, and empty
everywhere else — a refusal is visible in the data rather than a missing
row.

Commands::

    python scripts/wikipron_mirror.py pin --clone-dir /tmp/wikipron
    python scripts/wikipron_mirror.py screen --clone-dir /tmp/wikipron
    python scripts/wikipron_mirror.py build --clone-dir /tmp/wikipron \
        --restored-dir restored/ --out-dir mirror/
    python scripts/wikipron_mirror.py diff --old old_manifest.json \
        --new mirror/manifest.json
    python scripts/wikipron_mirror.py upload --out-dir mirror/

``docs/wikipron_mirror.md`` documents the whole refresh.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import unicodedata
from typing import Dict, List, Optional, Tuple

UPSTREAM = "https://github.com/CUNY-CL/wikipron.git"
TSV_PATH = "data/scrape/tsv"
LANG_META = "data/scrape/lib/languages.json"
DATASET = "TigreGotico/wikipron-restored-orthography"
HEADER = "orthography\trestored_orthography\tipa"
LICENSE = "CC BY-SA 4.0"

#: Verdicts a language can carry in the manifest.
#:
#: ``confirmed``            a style policy states that titles drop marks the
#:                          display form keeps, and the gold agrees.
#: ``confirmed_empirical``  no policy statement, but the marks the gold IPA
#:                          transcribes are absent from every orthography.
#: ``not_affected``         a policy mentions diacritics and titles, but it
#:                          does not create a title/display split here — the
#:                          marks are present in the gold, or the policy bans
#:                          them from the headword line too.
#: ``no_policy_page``       ``Wiktionary:About <Language>`` does not exist.
#: ``inconclusive``         the page exists and says nothing decisive.
VERDICTS = ("confirmed", "confirmed_empirical", "not_affected",
            "no_policy_page", "inconclusive")

#: Hand-read verdicts, keyed by WikiPron's ISO 639-3 code. The quote is
#: verbatim from ``Wiktionary:About <Language>``, with wiki markup
#: removed. ``marks`` are the combining characters the policy says a
#: title drops; the screen counts them in the gold and a policy that
#: predicts zero and finds thousands is downgraded, not believed.
SCREEN: Dict[str, Tuple[str, Optional[str], List[str]]] = {
    "ajp": ("confirmed",
            "Page titles never include diacritics, including shadde.",
            ["َ", "ُ", "ِ", "ّ", "ْ", "ً",
             "ٌ", "ٍ"]),
    "ang": ("confirmed",
            "Consequently, Old English entries here should be without "
            "diacritical marks in the page title.", ["̄"]),
    "apc": ("confirmed",
            "Page titles never include diacritics, including shadde.",
            ["َ", "ُ", "ِ", "ّ", "ْ", "ً",
             "ٌ", "ٍ"]),
    "ara": ("confirmed_empirical", None,
            ["َ", "ُ", "ِ", "ّ", "ْ"]),
    "car": ("confirmed",
            "Irregular stresses should not be marked in entry names, but "
            "should be marked with an acute accent in alternative display "
            "parameters.", ["́"]),
    "ceb": ("confirmed",
            "Diacritics are normally not used in written Cebuano, but are "
            "used for headwords in most Cebuano dictionaries to distinguish "
            "homographs.", ["́", "̀", "̂"]),
    "dum": ("confirmed", "Diacritics should not be used in entry names.",
            ["̄", "́", "̀"]),
    "evn": ("confirmed",
            "Long vowels are not represented in the entry name, but should "
            "always be indicated in the headword with a macron.",
            ["̄"]),
    "ewe": ("confirmed_empirical", None, ["́", "̀"]),
    "gmh": ("confirmed",
            "Certain letters with diacritics (ë ā ē ī "
            "ō ū ȥ) are not used in article titles, but are "
            "used when displaying the word.", ["̄"]),
    "gml": ("confirmed",
            "When creating a Middle Low German entry, the head (but not the "
            "actual page title) should follow the tradition of Middle Low "
            "German research to mark originally short vowels with a macron "
            "and original long vowels and diphthongs with a circumflex.",
            ["̄", "̂"]),
    "goh": ("confirmed",
            "This macron is to be used only for display, not in entry "
            "names.", ["̄"]),
    "grc": ("confirmed", "Entry names do not have macrons or breves.",
            ["̄", "̆"]),
    "hau": ("confirmed",
            "Diacritical marks should not be used in page titles, but "
            "should always be used in headwords.",
            ["́", "̀", "̄", "̂"]),
    "hbs": ("confirmed",
            "In the headword line, such accent marks should be specified as "
            "alternative displays, by means of the head= parameter.",
            ["̏", "̑"]),
    "heb": ("confirmed",
            "Do not use niqqud (vowel points) in page names, but do include "
            "it in headword-line templates.",
            ["ְ", "ֱ", "ִ", "ֵ", "ֶ", "ַ",
             "ָ", "ֹ", "ֻ", "ּ"]),
    "nci": ("confirmed",
            "Long vowels are marked with macrons only within the text of "
            "pages, not in page names.", ["̄"]),
    "nya": ("confirmed",
            "The circumflexed letter ŵ should not be in entry titles, "
            "but it should be in headword lines. Tones should also be marked "
            "in headword lines, using the acute to mark high tones.",
            ["́", "̂"]),
    "okm": ("confirmed",
            "The entry titles for Middle Korean terms should be written in "
            "the Hangul script as invented by Sejong, without tone marks.",
            []),
    "osx": ("confirmed",
            "This macron is to be used only for display, not in entry "
            "names, so the additional parameter that is available in many "
            "templates should be used to change the displayed form without "
            "affecting the link.", ["̄"]),
    "pam": ("confirmed",
            "Headwords should have diacritics as a pronunciation guide.",
            ["́", "̀", "̂"]),
    "pan": ("confirmed",
            "Similarly, diacritics can be utilised in the page body, but "
            "should also be avoided in page titles.",
            ["َ", "ُ", "ِ", "ّ", "ْ"]),
    "sga": ("confirmed",
            "This parallels Wiktionary's approach to Latin and Old English, "
            "where macrons are used in display but not in page titles.",
            ["̄"]),
    "tgl": ("confirmed",
            "Diacritics are normally not used in written Tagalog, but are "
            "used for headwords in most Tagalog dictionaries to distinguish "
            "homographs.", ["́", "̀", "̂"]),
    "yor": ("confirmed",
            "The underdot vowels, ẹ and ọ, should be used in page "
            "titles, but the tones should be marked in the headword line.",
            ["́", "̀", "̄"]),
    "yrk": ("confirmed",
            "Long and short vowel diacritics are to be supplied in the "
            "headwords of the appropriate entries.", ["̄"]),
    "cat": ("not_affected",
            "It is encouraged to use sort=(the page name without diacritics) "
            "in headword-line templates.", ["́", "̀"]),
    "cop": ("not_affected",
            "Other sporadically appearing diacritics such as circumflexes, "
            "acute accents, and the like should generally not be used in "
            "entry names or headword lines of main lemmas.",
            ["́", "̂"]),
    "enm": ("not_affected",
            "Middle English entries here should be without diacritical "
            "marks, whether in the page title or within the entry itself.",
            ["̄", "́"]),
    "got": ("not_affected",
            "As in other old languages, macrons are not used in these entry "
            "names, although the got-rom template allows a head= parameter "
            "to display them if necessary.", ["̄"]),
    "haw": ("not_affected",
            "Macrons and the okina should always be used in page titles.",
            ["̄"]),
    "lat": ("not_affected",
            "For these reasons, the page name for Latin entries should not "
            "contain diacritical marks.", ["̄"]),
    "nld": ("not_affected",
            "On Wiktionary, entry names containing stress marks are "
            "permitted only where they are used to distinguish one word from "
            "another.", ["́"]),
    "vec": ("not_affected",
            "The headword should always match the entry title — no "
            "additional diacritics should be added.", ["́", "̀"]),
    "yid": ("not_affected",
            "Normal entries should have titles that use all appropriate "
            "diacritical marks, including subscript vowels and other "
            "niqqudim.", ["ַ", "ָ"]),
    "amh": ("not_affected", None, []),
    "fas": ("not_affected", None,
            ["َ", "ُ", "ِ", "ّ", "ْ"]),
    "ota": ("not_affected", None,
            ["َ", "ُ", "ِ", "ّ", "ْ"]),
    "ind": ("inconclusive",
            "The headword line is the line directly below the part of "
            "speech header, in which the word is repeated, along with a "
            "alternative spelling with diacritics if applicable.",
            ["́"]),
}

#: Why a language with no usable policy statement got the verdict it did.
#: Every one of these was settled in the data.
NOTES: Dict[str, str] = {
    "amh": "no title/display split; the vowel is written into the syllabary "
           "character itself, so nothing is stripped",
    "ara": "no statement on the About page; not one short-vowel mark appears "
           "in any scraped word, while the transcriptions are fully "
           "vocalised",
    "ewe": "no About page; the scraped words are all but untoned and the "
           "transcriptions mark tone throughout",
    "fas": "no title/display split; short vowels are absent from the "
           "displayed headword too, so there is nothing to restore",
    "ota": "no title/display split; short vowels are absent from the "
           "displayed headword too, so there is nothing to restore",
}

#: Languages sharing the Arabic harakat result with ``ara``. They carry no
#: statement of their own on ``Wiktionary:About <Language>``, and the gold
#: settles it: not one short-vowel mark appears in any orthography.
_ARABIC_EMPIRICAL = ("acm", "acw", "afb", "ary", "arz", "ayl", "msa")
for _code in _ARABIC_EMPIRICAL:
    SCREEN[_code] = SCREEN["ara"]
    NOTES[_code] = NOTES["ara"]


# ─── upstream snapshot ──────────────────────────────────────────────────────

def _run(args: List[str], cwd: Optional[str] = None) -> str:
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True,
                          text=True).stdout.strip()


def pin(clone_dir: str, commit: Optional[str] = None) -> Dict[str, str]:
    """Clone or update the upstream scrape and report the pinned commit.

    A blobless sparse clone of one directory: the whole repository is
    several gigabytes and the scrape is 225 MB of it.
    """
    if not os.path.isdir(os.path.join(clone_dir, ".git")):
        os.makedirs(clone_dir, exist_ok=True)
        _run(["git", "clone", "--filter=blob:none", "--no-checkout",
              UPSTREAM, clone_dir])
        # leading slashes: without them git reads the paths as glob
        # patterns and silently checks out more than asked for
        _run(["git", "sparse-checkout", "set", "--no-cone",
              "/" + TSV_PATH + "/", "/" + LANG_META], cwd=clone_dir)
    else:
        _run(["git", "fetch", "origin", "master"], cwd=clone_dir)
    _run(["git", "checkout", commit or "FETCH_HEAD"], cwd=clone_dir) \
        if commit else None
    sha = _run(["git", "rev-parse", "HEAD"], cwd=clone_dir)
    date = _run(["git", "show", "-s", "--format=%cs", sha], cwd=clone_dir)
    return {"repo": "CUNY-CL/wikipron", "path": TSV_PATH,
            "commit": sha, "commit_date": date}


def read_gold(path: str) -> List[Tuple[str, str]]:
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) == 2:
                rows.append((parts[0], parts[1]))
    return rows


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ─── the screen ─────────────────────────────────────────────────────────────

def mark_counts(words: List[str], marks: List[str]) -> Dict[str, int]:
    """How often each policy-named mark occurs in *words*, NFD."""
    out = {m: 0 for m in marks}
    for word in words:
        for ch in unicodedata.normalize("NFD", word):
            if ch in out:
                out[ch] += 1
    return out


#: A policy predicting "no such mark in titles" tolerates a handful of
#: strays — an editor moving a page, an entry created before the rule.
#: It does not tolerate the mark on every other word. Latin sits at 1.31
#: marks per row and Old English, under an almost identical policy, at
#: 0.00005; nothing observed falls between.
STRAY_RATE = 0.01


def screen_language(code: str, words: List[str], policy_page: Optional[str]
                    ) -> Dict[str, object]:
    """The verdict for one language, with the evidence that supports it.

    A curated verdict is never taken on trust. ``confirmed`` claims the
    marks the policy names are kept out of titles; if the scraped words
    carry them at any rate worth speaking of, the policy does not reach
    this data and the verdict is written down as ``not_affected`` with
    the rate that overturned it. This is what separates Latin — whose
    policy reads almost word for word like Old English's, but whose
    scraped words carry macrons on most rows — from the languages where
    the defect is real.
    """
    verdict, quote, marks = SCREEN.get(
        code, ("inconclusive" if policy_page else "no_policy_page",
               None, []))
    found = sum(mark_counts(words, marks).values())
    rate = found / len(words) if words else 0.0
    if verdict == "confirmed" and rate > STRAY_RATE:
        verdict = "not_affected"
    return {"verdict": verdict, "rows": len(words),
            "policy_quote": quote, "policy_page": policy_page,
            "note": NOTES.get(code),
            "marks_named_by_policy": marks,
            "marks_found_in_gold": found,
            "marks_per_row": round(rate, 5)}


# ─── build ──────────────────────────────────────────────────────────────────

def policy_pages(clone_dir: str, out_path: str) -> Dict[str, str]:
    """Fetch ``Wiktionary:About <Language>`` once per language.

    Cheap on purpose: fifty titles per query, no page renders, one pass
    over the whole language list. Absence of a page is a screen result,
    not a failure, so a missing page is simply left out of the map.

    Language names come from upstream's own metadata, pinned with the
    scrape, so a language renamed on Wiktionary shows up as a changed
    file rather than a silently wrong link.
    """
    import urllib.parse
    import urllib.request

    meta = json.load(open(os.path.join(clone_dir, LANG_META),
                         encoding="utf-8"))
    by_title = {}
    for code, m in meta.items():
        by_title.setdefault(
            "Wiktionary:About " + m["wiktionary_name"], []).append(code)
    titles = sorted(by_title)
    found: Dict[str, str] = {}
    for i in range(0, len(titles), 50):
        batch = titles[i:i + 50]
        query = {"action": "query", "format": "json", "formatversion": "2",
                 "redirects": "1", "titles": "|".join(batch)}
        req = urllib.request.Request(
            "https://en.wiktionary.org/w/api.php",
            data=urllib.parse.urlencode(query).encode(),
            headers={"User-Agent": "orthography2ipa-wikipron-screen/1.0 "
                                   "(https://github.com/TigreGotico/"
                                   "orthography2ipa; openvoiceos@gmail.com)"})
        with urllib.request.urlopen(req, timeout=60) as fh:
            body = json.loads(fh.read().decode("utf-8"))["query"]
        back = {n["to"]: n["from"]
                for key in ("normalized", "redirects")
                for n in body.get(key, [])}
        for page in body.get("pages", []):
            if page.get("missing"):
                continue
            title = page["title"]
            for _ in range(4):
                title = back.get(title, title)
            for code in by_title.get(title, []):
                found[code] = ("https://en.wiktionary.org/wiki/"
                               + urllib.parse.quote(title.replace(" ", "_")))
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(found, fh, ensure_ascii=False, indent=1, sort_keys=True)
    return found


def build(clone_dir: str, restored_dir: str, out_dir: str,
          pages: Dict[str, str]) -> Dict[str, object]:
    """Write the mirror and its manifest.

    Restoration maps are keyed by ISO code and hold ``title -> display``
    for that language only, so a title shared by two languages — ``ade``
    is both Ewe and Yoruba — never crosses over.
    """
    src = os.path.join(clone_dir, TSV_PATH)
    data_dir = os.path.join(out_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    meta = pin(clone_dir)
    files: Dict[str, object] = {}
    words_by_code: Dict[str, List[str]] = {}
    maps: Dict[str, Dict[str, str]] = {}
    attempted: Dict[str, bool] = {}
    for name in sorted(os.listdir(src)):
        if not name.endswith(".tsv"):
            continue
        code = name.split("_")[0]
        if code not in maps:
            path = os.path.join(restored_dir, f"{code}.json")
            # A restoration map on disk is the record that the language
            # was run. Its absence means nobody has tried yet, which is
            # a different fact from having tried and found nothing.
            attempted[code] = os.path.exists(path)
            maps[code] = (json.load(open(path, encoding="utf-8"))
                          if attempted[code] else {})
        rows = read_gold(os.path.join(src, name))
        words_by_code.setdefault(code, []).extend(w for w, _ in rows)
        restored = 0
        out_path = os.path.join(data_dir, name)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(HEADER + "\n")
            for word, ipa in rows:
                display = maps[code].get(word, "")
                restored += bool(display)
                fh.write(f"{word}\t{display}\t{ipa}\n")
        files[name] = {
            "language": code, "rows": len(rows), "restored": restored,
            "sha256_upstream": sha256(os.path.join(src, name)),
        }
    screen = {code: screen_language(code, words, pages.get(code))
              for code, words in sorted(words_by_code.items())}
    for code, record in screen.items():
        record["restored_rows"] = sum(
            f["restored"] for f in files.values() if f["language"] == code)
        record["restoration_attempted"] = attempted.get(code, False)
    silent = sorted(code for code, record in screen.items()
                    if record["restoration_attempted"]
                    and not record["restored_rows"])
    if silent:
        # Tundra Nenets ran clean and recovered nothing, because
        # upstream's metadata gives it the code ``yrk`` while Wiktionary
        # tags its headwords ``yrk-tun``. A human reading printed counts
        # caught that. Nothing should depend on a human reading counts.
        raise SystemExit(
            "restoration ran and recovered nothing for: "
            + ", ".join(silent)
            + "; check the Wiktionary language code and section name in "
              "scripts/restore_wikipron_orthography.py LANGS")
    manifest = {
        "dataset": DATASET, "license": LICENSE, "upstream": meta,
        "schema": ["orthography", "restored_orthography", "ipa"],
        "verdicts": list(VERDICTS),
        "file_count": len(files), "files": files, "screen": screen,
    }
    with open(os.path.join(out_dir, "manifest.json"), "w",
              encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1, sort_keys=True)
    with open(os.path.join(out_dir, "README.md"), "w",
              encoding="utf-8") as fh:
        fh.write(card(manifest))
    return manifest



# ─── dataset card ───────────────────────────────────────────────────────────

_VERDICT_LABEL = {
    "confirmed": "confirmed",
    "confirmed_empirical": "confirmed, no policy page",
    "not_affected": "not affected",
    "no_policy_page": "no policy page",
    "inconclusive": "inconclusive",
}

_CARD_HEAD = """---
license: cc-by-sa-4.0
task_categories:
- text-to-speech
tags:
- phonetics
- g2p
- wiktionary
- wikipron
configs:
- config_name: default
  data_files: data/*.tsv
---

# WikiPron with restored orthography

A pinned mirror of every pronunciation scrape in
[CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron), with a second
orthography column holding the headword English Wiktionary actually
displays.

## The defect

WikiPron pairs a pronunciation with the English Wiktionary MediaWiki
**page title**. For a number of languages the title is not the word the
page displays, because the language's style policy keeps diacritics out
of titles and puts them back only on the headword line.
[`Wiktionary:About Middle High German`](https://en.wiktionary.org/wiki/Wiktionary:About_Middle_High_German)
states it plainly:

> certain letters with diacritics (\u00eb \u0101 \u0113 \u012b \u014d \u016b \u0225) are not used in
> article titles, but are used when displaying the word

> this does not apply to the umlauted vowels \u00e4, \u00f6, \u00fc, \u00e6, \u0153, which are
> treated as separate letters and thus appear in titles like any other
> letter

The pronunciation still transcribes what the title threw away. A
grapheme-to-phoneme system scored on those rows is asked to recover
tone, vowel length or vocalisation from an input that no longer writes
them, and the resulting error rate measures the input, not the system.

## The recovery

`restored_orthography` holds the headword Wiktionary renders for that
language, read from the MediaWiki API. Nothing is guessed:

* A page holds one section per language. `Adam` renders an English
  `Adam` and an Ewe `\u00c1d\u00e0m`. The wikitext is cut to the target
  `==Language==` section before any headword template is read, and the
  rendered headword is matched on its `lang` attribute.
* A page with no headword override, no section for the language, or two
  headwords that disagree contributes an empty cell. One unpointed title
  often spells several distinct words \u2014 `aba` renders `ab\u00e0`, `ab\u00e1`,
  `\u00e0ba` and `\u00e0b\u00e1` \u2014 and the row is refused rather than assigned a
  winner.
* A restored form must differ from the title only in diacritics. If the
  base-letter spine changes, the cell stays empty.

An empty `restored_orthography` therefore means one of: the language was
screened and is not affected, the language is affected but has not been
restored yet, or the row was refused. The manifest says which.

## Schema

`orthography`, `restored_orthography`, `ipa`, tab separated, one header
row. Columns one and three are WikiPron's own two columns, byte for
byte. File names are WikiPron's: `<iso639-3>_<script>_<broad|narrow>`,
with a dialect segment where upstream carries one.

Consumers choose the column. Score `orthography` to reproduce a WikiPron
number; score `restored_orthography` on the rows where it is filled to
measure a system against an input that encodes the contrast.

## Screen

Each language was screened once against
`Wiktionary:About <Language>`, then checked against the data. A policy
saying macrons never reach titles predicts zero macrons in the scraped
orthography, and the count either bears that out or it does not.

Latin is why the second half is not optional. Its policy says the page
name "should not contain diacritical marks", in almost the same words as
Old English's, and yet the scraped Latin words carry 1.31 macrons per
row against Old English's 0.00005. The disagreement was noticed by
reading the two together, and Latin is recorded as `not_affected` on
that basis. The build also enforces it: a `confirmed` verdict whose
data carries the marks above a stray rate is downgraded automatically,
so the next language like Latin does not depend on someone noticing.

A verdict is a snapshot against a live wiki, and the wiki moves.
Mandarin is recorded `no_policy_page`, yet `Wiktionary:About Mandarin`
redirects to `Wiktionary:Chinese entry guidelines`, which exists. That
page describes no title/headword split, so the verdict stands, and the
mismatch is what drift looks like: expect some `no_policy_page` to have
grown a page since. This is the same reason the scrape itself is pinned
— only the snapshot is stable.

Negative results are recorded on purpose. They are the reason nobody has
to screen these languages again.

"""

_CARD_TAIL = """

## Limitations

Coverage is partial and always will be. Restoration costs one page
render per word, so the largest affected languages are screened and
recorded but not restored; their `restored_orthography` column is empty
throughout, and the manifest marks them.

This is English Wiktionary only. It inherits WikiPron's own quality
issues without correcting any of them \u2014 crowd-sourced transcriptions,
uneven transcription traditions inside one language, and entries whose
headword line and pronunciation line were written independently.

Two results are easy to over-read:

* Ewe restores to a near-zero error rate against a grapheme-to-phoneme
  system. Tone-marked Ewe spelling is very nearly a transliteration of
  its own phonemic transcription, so the row is easy rather than the
  system good.
* Middle High German gets **worse** after restoration. The restored
  input carries \u27e8\u00eb \u0101 \u0113 \u012b \u014d \u016b \u0225\u27e9, which the system tested had no
  rules for at all. A lossy input had been hiding a real gap: while the
  input never contained those letters, nothing could reveal they were
  unmapped.

## Licence and attribution

The text is English Wiktionary content, licensed
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), and this
dataset carries the same licence. WikiPron's Apache 2.0 covers its
scraper, not the scraped text. Attribute both English Wiktionary and
[CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron).
"""


def card(manifest: Dict[str, object]) -> str:
    """The dataset card, rendered from the manifest so the two agree."""
    up = manifest["upstream"]
    parts = [_CARD_HEAD]
    parts.append(
        f"## Snapshot\n\n"
        f"`{up['repo']}` commit `{up['commit']}`, dated {up['commit_date']},"
        f" path `{up['path']}`. {manifest['file_count']} files.\n\n"
        f"WikiPron publishes its scrapes on a branch it keeps editing, so a"
        f" benchmark reading it directly cannot tell a system change from an"
        f" upstream edit. Every file here is copied from that one commit and"
        f" `manifest.json` records each file's upstream SHA-256, which is"
        f" what makes a refresh a diff rather than a guess.\n\n"
        f"## Screen verdicts and coverage\n\n"
        f"A `confirmed` language with no restored rows has not been run.\n"
        f"\u201cnot attempted\u201d in the table and"
        f" `restoration_attempted: false` in `manifest.json` say so"
        f" explicitly, because a language that was run and recovered"
        f" nothing would mean a broken lookup, not an empty Wiktionary,"
        f" and the two must not look alike. The build refuses to publish"
        f" the second case.\n\n"
        f"| Language | Rows | Verdict | Restored | Policy |\n"
        f"|---|---|---|---|---|\n")
    rank = {"confirmed": 0, "confirmed_empirical": 1, "not_affected": 2}
    rows = sorted(manifest["screen"].items(),
                  key=lambda kv: (rank.get(kv[1]["verdict"], 9), kv[0]))
    listed = [(c, r) for c, r in rows if r["verdict"] in rank]
    for code, rec in listed:
        quote = rec["policy_quote"]
        page = rec["policy_page"]
        if quote and page:
            policy = f"[\u201c{quote}\u201d]({page})"
        elif quote:
            policy = f"\u201c{quote}\u201d"
        else:
            policy = rec["note"] or "no statement; screened in the data"
        if rec["restoration_attempted"]:
            restored = str(rec["restored_rows"])
        else:
            restored = "not attempted"
        parts.append(
            f"| `{code}` | {rec['rows']} | {_VERDICT_LABEL[rec['verdict']]} |"
            f" {restored} | {policy} |\n")
    counts = {v: sum(1 for _, r in rows if r["verdict"] == v)
              for v in VERDICTS}
    parts.append(
        f"\nOf the remaining languages, {counts['no_policy_page']} have no"
        f" `Wiktionary:About <Language>` page at all and"
        f" {counts['inconclusive']} have one that says nothing about"
        f" diacritics in titles. Absence of a policy is an answer too: there"
        f" is no documented title/display split to recover, and their"
        f" `restored_orthography` column is empty. `manifest.json` carries a"
        f" verdict for every language, with the marks each policy names and"
        f" how often they occur in the scraped words.\n")
    parts.append(_CARD_TAIL)
    return "".join(parts)


def diff(old_path: str, new_path: str) -> int:
    """Report what moved between two snapshots.

    This is the whole point of pinning: a benchmark reading upstream's
    branch cannot tell an engine change from an upstream edit, and this
    tells the two apart.
    """
    old = json.load(open(old_path, encoding="utf-8"))
    new = json.load(open(new_path, encoding="utf-8"))
    print(f"{old['upstream']['commit'][:12]} ({old['upstream']['commit_date']})"
          f" -> {new['upstream']['commit'][:12]} "
          f"({new['upstream']['commit_date']})")
    o, n = old["files"], new["files"]
    for name in sorted(set(n) - set(o)):
        print(f"  added   {name} ({n[name]['rows']} rows)")
    for name in sorted(set(o) - set(n)):
        print(f"  removed {name}")
    for name in sorted(set(o) & set(n)):
        if o[name]["sha256_upstream"] != n[name]["sha256_upstream"]:
            print(f"  changed {name} "
                  f"({o[name]['rows']} -> {n[name]['rows']} rows)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("pin", "screen", "build"):
        p = sub.add_parser(name)
        p.add_argument("--clone-dir", required=True)
        if name == "screen":
            p.add_argument("--policy-pages", default="policy_pages.json")
        if name == "build":
            p.add_argument("--restored-dir", default="restored")
            p.add_argument("--out-dir", required=True)
            p.add_argument("--policy-pages", default="policy_pages.json")
    p = sub.add_parser("diff")
    p.add_argument("--old", required=True)
    p.add_argument("--new", required=True)
    args = ap.parse_args(argv)
    if args.cmd == "pin":
        print(json.dumps(pin(args.clone_dir), indent=1))
    elif args.cmd == "diff":
        return diff(args.old, args.new)
    elif args.cmd == "screen":
        found = policy_pages(args.clone_dir, args.policy_pages)
        print(f"{len(found)} languages have a Wiktionary:About page")
    elif args.cmd == "build":
        pages = json.load(open(args.policy_pages, encoding="utf-8"))
        m = build(args.clone_dir, args.restored_dir, args.out_dir, pages)
        print(f"{m['file_count']} files at {m['upstream']['commit'][:12]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
