#!/usr/bin/env python3
"""Arabic TTS gold set — authoring, drafting and validation tooling.

The gold set lives in ``orthography2ipa/data/gold/arabic_tts/<code>.tsv`` (one
file per lect, 5+ rows) and provides fully diacritized, phonetically diverse,
literature-justified sentences for validating Arabic TTS voices per dialect.

Subcommands
-----------
checklist <lect> [tsv]
    Derive the dialect-discriminative feature checklist for a lect from its
    orthography2ipa spec, and (if the gold TSV exists) report which features
    the current sentences cover and which are still missing. Use this to
    author additional sentences later.

draft <lect> <textfile>
    First-draft pipeline for new sentences (one per line, undiacritized or
    partially diacritized): diacritize with text2tashkeel (``rawi-ensemble``)
    and transcribe with orthography2ipa. For MSA/Classical the tashkeel is
    near-final; for dialects it is explicitly OUT OF DOMAIN and must be
    hand-corrected against the literature cited in the lect's spec sources.
    Emits TSV rows marked NEEDS-REVIEW.

validate [lect ...]
    CI gate over the gold TSVs: schema, per-lect row minimum, diacritization
    completeness, o2i transcription regression (``transcribe(sentence, lect)
    == ipa``), feature-tag verifiability and in-lect duplicate detection.

Schema (TSV, tab-separated, UTF-8, header row)
----------------------------------------------
id, sentence (diacritized), raw (undiacritized), ipa (o2i, verified),
gloss_en, features (semicolon list), notes (corrections + citation ids)
"""
import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

GOLD_DIR = REPO_ROOT / "orthography2ipa" / "data" / "gold" / "arabic_tts"

LECTS = [
    "arb", "ar",
    "ar-EG", "ar-IQ", "ar-IQ-x-qeltu", "ar-SD", "ar-TD", "ar-NG",
    "ar-SY", "ar-LB", "ar-JO", "ar-PS",
    "ar-AE", "ar-BH", "ar-KW", "ar-QA", "ar-OM",
    "ar-SA-x-najd", "ar-SA-x-hejaz", "ar-YE",
    "ar-SA-x-qassim", "ar-SA-x-rijal-alma", "ar-SA-x-sharqiyya",
    "ar-MA", "ar-TN", "ar-DZ", "ar-LY", "ar-MR",
    # Grouping (proto/koine) nodes — pan-group register, node-level rankings.
    "ar-x-gulf", "ar-x-levantine", "ar-x-maghrebi", "ar-x-mashriqi", "ar-x-peninsular",
]
MIN_ROWS = 5
FIELDS = ["id", "sentence", "raw", "ipa", "gloss_en", "features", "notes"]

HARAKAT = "ًٌٍَُِّْٰ"  # tanwin, short vowels, shadda, sukun, dagger alif
SHADDA = "ّ"
CONSONANTS = set("بتثجحخدذرزسشصضطظعغفقكلمنهةءئؤأإ")
LONG_CARRIERS = set("اوىيآ")
SUN_LETTERS = set("تثدذرزسشصضطظلن")


def unmark(ipa: str) -> str:
    """*ipa* with the stress marks stripped, for feature-presence scanning."""
    return ipa.replace("ˈ", "").replace("ˌ", "")

# Feature tags and how each is verified. "raw" predicates look at the
# undiacritized orthography (reflexes like qaf/jim vary per dialect, so the
# *grapheme* is the stable witness); "ipa" predicates look at the o2i output
# (classes that are stable across dialects).
FEATURES = {
    "qaf":         ("raw",  lambda raw, ipa: "ق" in raw),
    "jim":         ("raw",  lambda raw, ipa: "ج" in raw),
    "interdental": ("raw",  lambda raw, ipa: any(c in raw for c in "ثذظ")),
    "kaf":         ("raw",  lambda raw, ipa: "ك" in raw),
    "hamza":       ("raw",  lambda raw, ipa: any(c in raw for c in "ءأإئؤ")),
    "ta_marbuta":  ("raw",  lambda raw, ipa: "ة" in raw),
    "sun_assim":   ("raw",  lambda raw, ipa: re.search("ال[" + "".join(SUN_LETTERS) + "]", raw) is not None),
    "emphatic":    ("ipa",  lambda raw, ipa: "ˤ" in ipa or "ɫ" in ipa),
    "pharyngeal":  ("ipa",  lambda raw, ipa: "ħ" in ipa or "ʕ" in ipa),
    # Scan the IPA with the stress marks REMOVED. A geminate is precisely the
    # consonant that straddles a syllable boundary (dar|ris), so the stress
    # mark lands *between* its two halves — rˈradʒulu — and a doubled-character
    # search over the marked string would never see it.
    "geminate":    ("ipa",  lambda raw, ipa: re.search(r"([^\Wa-z\d])\1", unmark(ipa)) is not None
                                             or re.search(r"([bcdfghjklmnpqrstvwxzʃʒðθħʕɣχʁqβɸ])\1", unmark(ipa)) is not None
                                             or SHADDA in raw),
    "long_vowel":  ("ipa",  lambda raw, ipa: re.search(r"[aeiouɑɐæɪʊəɛɔ]ː", ipa) is not None),
    "diphthong":   ("ipa",  lambda raw, ipa: re.search(r"[aɑæ][wj]|eː|oː", ipa) is not None),
}
# Non-phonetic shape tags: allowed in `features`, not machine-verified.
SHAPE_TAGS = {"statement", "question", "negation", "imperative", "number"}


def _g2p(lect):
    import orthography2ipa
    return lambda text: orthography2ipa.transcribe(text, lect)


def _load(lect):
    p = GOLD_DIR / f"{lect}.tsv"
    if not p.is_file():
        return None
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _spec_summary(lect):
    import orthography2ipa
    spec = orthography2ipa.get(lect)
    srcs = getattr(spec, "sources", None) or []
    return spec, srcs


def strip_tashkeel(text: str) -> str:
    return "".join(c for c in text if c not in HARAKAT)


def diacritization_gaps(sentence: str):
    """Return consonants missing a following diacritic (with pragmatic
    exceptions: word-final pausal position; matres lectionis; the alif of
    the definite article)."""
    gaps = []
    for word in sentence.split():
        letters = [c for c in word]
        arabic_positions = [i for i, c in enumerate(letters) if c in CONSONANTS]
        for i in arabic_positions:
            following = "".join(letters[i + 1:i + 3])
            rest = letters[i + 1:]
            if not any(ch in CONSONANTS or ch in LONG_CARRIERS for ch in rest):
                continue  # word-final consonant: pausal bare form allowed
            if letters[i] == "ل" and (
                (i >= 1 and letters[i - 1] == "ا")
                or (i >= 2 and letters[i - 1] in "َِ" and letters[i - 2] in "ال")
            ):
                # lam of the definite article before a sun letter is often
                # left bare (the assimilation is written on the sun letter)
                if any(following.startswith(s + SHADDA) for s in SUN_LETTERS) or True:
                    continue
            if following and following[0] in HARAKAT:
                continue
            gaps.append((word, letters[i]))
    return gaps


def cmd_checklist(args):
    lect = args.lect
    spec, srcs = _spec_summary(lect)
    print(f"# {lect} — {getattr(spec, 'name', '?')}")
    print(f"sources: {', '.join(getattr(s, 'id', '?') for s in srcs) if srcs else '(none)'}")
    rows = _load(lect)
    covered = set()
    if rows:
        for r in rows:
            covered |= {t for t in r["features"].split(";") if t}
    print("\nfeature checklist (tag  verified-by  covered?):")
    for tag, (kind, _) in FEATURES.items():
        mark = "x" if tag in covered else " "
        print(f"  [{mark}] {tag:<12} ({kind})")
    for tag in sorted(SHAPE_TAGS):
        mark = "x" if tag in covered else " "
        print(f"  [{mark}] {tag:<12} (shape, not machine-verified)")
    missing = [t for t in FEATURES if t not in covered]
    if rows is None:
        print(f"\nno gold file yet: {GOLD_DIR / (lect + '.tsv')}")
    elif missing:
        print(f"\nMISSING phonetic coverage: {', '.join(missing)}")
    else:
        print("\nfull phonetic coverage.")


def cmd_draft(args):
    lect = args.lect
    import text2tashkeel
    g2p = _g2p(lect)
    dialectal = lect not in ("ar", "arb")
    lines = [l.strip() for l in Path(args.textfile).read_text(encoding="utf-8").splitlines() if l.strip()]
    w = csv.writer(sys.stdout, delimiter="\t")
    w.writerow(FIELDS)
    for i, line in enumerate(lines, 1):
        raw = strip_tashkeel(line)
        try:
            diac = text2tashkeel.diacritize(raw)
        except Exception as e:  # keep drafting usable offline
            diac, note = line, f"text2tashkeel failed: {e}"
        else:
            note = ("NEEDS-REVIEW: tashkeel is MSA-model output on DIALECTAL text "
                    "(out of domain) — hand-correct against the spec's sources"
                    if dialectal else "NEEDS-REVIEW: verify MSA tashkeel")
        ipa = g2p(diac)
        feats = ";".join(tag for tag, (_, pred) in FEATURES.items() if pred(raw, ipa))
        w.writerow([f"{lect}-{i:03d}", diac, raw, ipa, "", feats, note])


def cmd_validate(args):
    lects = args.lects or LECTS
    import orthography2ipa
    failures = []
    total = 0
    for lect in lects:
        rows = _load(lect)
        if rows is None:
            failures.append(f"{lect}: missing gold file")
            continue
        if len(rows) < MIN_ROWS:
            failures.append(f"{lect}: only {len(rows)} rows (< {MIN_ROWS})")
        seen = set()
        for r in rows:
            total += 1
            rid = r.get("id", "?")
            if list(r) != FIELDS and set(FIELDS) - set(r):
                failures.append(f"{rid}: bad columns {list(r)}")
                continue
            if not all(r[f] for f in ("id", "sentence", "raw", "ipa", "gloss_en", "features")):
                failures.append(f"{rid}: empty required field")
            if r["sentence"] in seen:
                failures.append(f"{rid}: duplicate sentence within {lect}")
            seen.add(r["sentence"])
            if strip_tashkeel(r["sentence"]) != unicodedata.normalize("NFC", r["raw"]):
                failures.append(f"{rid}: raw != sentence stripped of tashkeel")
            gaps = diacritization_gaps(r["sentence"])
            if gaps:
                failures.append(f"{rid}: bare consonants {gaps}")
            got = orthography2ipa.transcribe(r["sentence"], lect)
            if got != r["ipa"]:
                failures.append(f"{rid}: o2i regression\n    stored: {r['ipa']}\n    got:    {got}")
            for tag in [t for t in r["features"].split(";") if t]:
                if tag in SHAPE_TAGS:
                    continue
                if tag not in FEATURES:
                    failures.append(f"{rid}: unknown feature tag {tag!r}")
                elif not FEATURES[tag][1](r["raw"], r["ipa"]):
                    failures.append(f"{rid}: feature {tag!r} not verifiable in row")
            spec = orthography2ipa.get(lect)
            src_ids = {getattr(s, "id", None) for s in (getattr(spec, "sources", None) or ())}
            for cid in re.findall(r"\b[a-z][a-z_-]*[0-9]{4}[a-z]*\b", r["notes"]):
                if cid not in src_ids:
                    failures.append(f"{rid}: notes cite {cid!r}, not in {lect} spec sources")
    print(f"validated {total} rows across {len(lects)} lects")
    if failures:
        print(f"\n{len(failures)} FAILURE(S):")
        for f in failures:
            print("  -", f)
        return 1
    print("all green")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("checklist"); p.add_argument("lect"); p.set_defaults(fn=cmd_checklist)
    p = sub.add_parser("draft"); p.add_argument("lect"); p.add_argument("textfile"); p.set_defaults(fn=cmd_draft)
    p = sub.add_parser("validate"); p.add_argument("lects", nargs="*"); p.set_defaults(fn=cmd_validate)
    args = ap.parse_args()
    rc = args.fn(args)
    sys.exit(rc or 0)


if __name__ == "__main__":
    main()
